"""Interactive settings actions: toggles, cycles and text-input flows."""

from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from plugins.database.database import db
from plugins.emojis import E, BTN
from plugins.settings.settings import OpenSettings, YTDL_FILTERS

# user_id -> {"key": str, "prompt_id": int}
PENDING = {}

TOGGLE_KEYS = {
    "upload_as_doc",
    "bot_updates",
    "generate_ss",
    "spoiler",
    "no_forwards",
    "filename_cleaner",
    "generate_sample_video",
    "streaming",
    "caption_up",
    "auto_unzip",
}

ASK_TEXTS = {
    "caption": (
        f"{E.INBOX} <b>Sᴇɴᴅ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ɴᴏᴡ</b>\n\n"
        f"<blockquote>{E.ARROW} Aᴠᴀɪʟᴀʙʟᴇ ᴠᴀʀɪᴀʙʟᴇs :\n"
        f"<code>{{filename}}</code> • <code>{{filesize}}</code> • <code>{{duration}}</code></blockquote>\n\n"
        f"{E.ARROW} Sᴇɴᴅ <code>clear</code> ᴛᴏ ʀᴇᴍᴏᴠᴇ ɪᴛ."
    ),
    "metadata": (
        f"{E.MANAGE} <b>Sᴇɴᴅ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴛɪᴛʟᴇ / ᴀᴜᴛʜᴏʀ ᴛᴀɢ</b>\n\n"
        f"{E.ARROW} Exᴀᴍᴘʟᴇ : <code>@NY_BOTS</code>\n"
        f"{E.ARROW} Sᴇɴᴅ <code>clear</code> ᴛᴏ ʀᴇᴍᴏᴠᴇ ɪᴛ."
    ),
    "dump_channel": (
        f"{E.CHANNEL} <b>Sᴇɴᴅ ʏᴏᴜʀ ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ ID</b>\n\n"
        f"<blockquote>{E.ARROW} Exᴀᴍᴘʟᴇ : <code>-1001234567890</code>\n"
        f"{E.ARROW} Aᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴛʜᴇʀᴇ ғɪʀsᴛ.</blockquote>\n\n"
        f"{E.ARROW} Sᴇɴᴅ <code>clear</code> ᴛᴏ ʀᴇᴍᴏᴠᴇ ɪᴛ."
    ),
    "blocklist_words": (
        f"{E.ALERT} <b>Sᴇɴᴅ ʙʟᴏᴄᴋʟɪsᴛ ᴡᴏʀᴅs</b>\n\n"
        f"<blockquote>{E.ARROW} Sᴇᴘᴀʀᴀᴛᴇ ᴛʜᴇᴍ ᴡɪᴛʜ ᴄᴏᴍᴍᴀs\n"
        f"{E.ARROW} Exᴀᴍᴘʟᴇ : <code>spam, ads, 18+</code></blockquote>\n\n"
        f"{E.ARROW} Sᴇɴᴅ <code>clear</code> ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀʟʟ."
    ),
}

CANCEL_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🚫 Cᴀɴᴄᴇʟ", callback_data="st_cancel_input")]]
)


async def handle_settings_callback(bot, update) -> bool:
    """Handle every `st_*` callback. Returns True when handled."""
    data = update.data
    user_id = update.from_user.id

    if not data.startswith("st_"):
        return False

    # ---------------------------------------------------------- toggles
    if data.startswith("st_toggle_"):
        key = data[len("st_toggle_"):]
        if key in TOGGLE_KEYS:
            new_value = await db.toggle_setting(user_id, key)
            await update.answer(
                f"{'✅ Enabled' if new_value else '❌ Disabled'} • {key.replace('_', ' ').title()}"
            )
            await OpenSettings(update.message)
        else:
            await update.answer("Unknown setting!", show_alert=True)
        return True

    # ------------------------------------------------------ ytdl filter
    if data == "st_cycle_ytdl_filter":
        current = await db.get_setting(user_id, "ytdl_filter") or YTDL_FILTERS[0]
        try:
            nxt = YTDL_FILTERS[(YTDL_FILTERS.index(current) + 1) % len(YTDL_FILTERS)]
        except ValueError:
            nxt = YTDL_FILTERS[0]
        await db.set_setting(user_id, "ytdl_filter", nxt)
        await update.answer(f"🔎 Ytdl filter: {nxt}")
        await OpenSettings(update.message)
        return True

    # ---------------------------------------------------------- reset
    if data == "st_reset":
        await db.reset_settings(user_id)
        await update.answer("♻️ All settings restored to default!", show_alert=True)
        await OpenSettings(update.message)
        return True

    # ------------------------------------------------- cancel an input
    if data == "st_cancel_input":
        PENDING.pop(user_id, None)
        await update.answer("🚫 Cancelled")
        await OpenSettings(update.message)
        return True

    # ------------------------------------------------- text input asks
    if data.startswith("st_ask_"):
        key = data[len("st_ask_"):]
        if key not in ASK_TEXTS:
            await update.answer("Unknown setting!", show_alert=True)
            return True
        PENDING[user_id] = {"key": key, "prompt_id": update.message.id}
        await update.answer()
        await update.message.edit(
            text=ASK_TEXTS[key],
            reply_markup=CANCEL_MARKUP,
            disable_web_page_preview=True,
        )
        return True

    return False


@Client.on_message(filters.private & filters.text, group=-1)
async def collect_settings_input(bot: Client, m: Message):
    """Capture the next text message when the user is filling a setting."""
    pending = PENDING.get(m.from_user.id)
    if not pending:
        return
    if m.text.startswith("/"):
        PENDING.pop(m.from_user.id, None)
        return

    key = pending["key"]
    value = m.text.strip()
    PENDING.pop(m.from_user.id, None)

    if value.lower() in ("clear", "/clear", "none", "delete"):
        await db.set_setting(m.from_user.id, key, [] if key == "blocklist_words" else None)
        note = f"{E.CLEAR} <b>{key.replace('_', ' ').title()} ᴄʟᴇᴀʀᴇᴅ!</b>"
    elif key == "dump_channel":
        try:
            channel_id = int(value)
        except ValueError:
            await m.reply_text(
                f"{E.ERROR} <b>Iɴᴠᴀʟɪᴅ ᴄʜᴀɴɴᴇʟ ID.</b>\n\n{E.ARROW} Exᴀᴍᴘʟᴇ : <code>-1001234567890</code>",
                quote=True,
            )
            return m.stop_propagation()
        try:
            chat = await bot.get_chat(channel_id)
            await bot.send_message(channel_id, f"{E.CONFIRM} <b>Dᴜᴍᴘ ᴄʜᴀɴɴᴇʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!</b>")
        except Exception as err:
            await m.reply_text(
                f"{E.ERROR} <b>Cᴀɴɴᴏᴛ ᴀᴄᴄᴇss ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ.</b>\n\n<code>{err}</code>\n\n"
                f"{E.ARROW} <i>Aᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.</i>",
                quote=True,
            )
            return m.stop_propagation()
        await db.set_setting(m.from_user.id, key, channel_id)
        note = f"{E.CONFIRM} <b>Dᴜᴍᴘ ᴄʜᴀɴɴᴇʟ sᴇᴛ ᴛᴏ</b> <code>{chat.title if hasattr(chat, 'title') else channel_id}</code>"
    elif key == "blocklist_words":
        words = [w.strip().lower() for w in value.replace("\n", ",").split(",") if w.strip()]
        await db.set_setting(m.from_user.id, key, words)
        note = f"{E.CONFIRM} <b>Sᴀᴠᴇᴅ {len(words)} ʙʟᴏᴄᴋʟɪsᴛ ᴡᴏʀᴅ(s).</b>"
    else:
        await db.set_setting(m.from_user.id, key, m.text)
        note = f"{E.CONFIRM} <b>{key.replace('_', ' ').title()} sᴀᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!</b>"

    editable = await m.reply_text(note, quote=True)
    await OpenSettings(editable)
    m.stop_propagation()
