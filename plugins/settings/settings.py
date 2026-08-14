import asyncio

from pyrogram import Client, filters, types, errors
from pyrogram.types import Message

from plugins.config import Config
from plugins.database.add import AddUser
from plugins.database.database import db
from plugins.emojis import E, BTN

ON = "✅"
OFF = "❌"

YTDL_FILTERS = ["mp4", "mkv", "webm", "audio"]


def _flag(value: bool, on_text="On", off_text="Off") -> str:
    return f"{ON} {on_text}" if value else f"{OFF} {off_text}"


SETTINGS_TEXT = f"""{E.SETTINGS} <b>Bᴏᴛ Sᴇᴛᴛɪɴɢs Pᴀɴᴇʟ</b>

<blockquote>{E.RIGHT} <b>Uᴘʟᴏᴀᴅ Mᴏᴅᴇ</b> : {{mode}}
{E.CREATE} <b>Tʜᴜᴍʙɴᴀɪʟ</b> : {{thumb}}
{E.SEARCH} <b>Yᴛᴅʟ Fɪʟᴛᴇʀ</b> : {{ytdl}}
{E.INBOX} <b>Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ</b> : {{caption}}
{E.CHANNEL} <b>Dᴜᴍᴘ Cʜᴀɴɴᴇʟ</b> : {{dump}}
{E.ALERT} <b>Bʟᴏᴄᴋʟɪsᴛ Wᴏʀᴅs</b> : {{blocklist}}
{E.MANAGE} <b>Cᴜsᴛᴏᴍ Mᴇᴛᴀᴅᴀᴛᴀ</b> : {{metadata}}</blockquote>

{E.ALERT} <b>Nᴏᴛᴇs</b>
{E.ARROW} Sᴇᴛᴛɪɴɢs ᴀᴘᴘʟʏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ғᴜᴛᴜʀᴇ ᴜᴘʟᴏᴀᴅs
{E.ARROW} Sᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs ᴍᴀʏ ɴᴇᴇᴅ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss

{E.POINTER} <i>Tᴀᴘ ᴀɴʏ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴄʜᴀɴɢᴇ ɪᴛ.</i>"""


def _short(value, limit=28):
    if not value:
        return "Nᴏᴛ sᴇᴛ"
    text = str(value).replace("\n", " ")
    return (text[:limit] + "…") if len(text) > limit else text


async def build_settings(user_id: int):
    """Return (text, InlineKeyboardMarkup) for the settings panel."""
    data = await db.get_user_data(user_id) or {}

    def g(key):
        return data.get(key, db.DEFAULTS.get(key))

    upload_as_doc = bool(g("upload_as_doc"))
    thumbnail = g("thumbnail")
    blocklist = g("blocklist_words") or []

    text = SETTINGS_TEXT.format(
        mode="🎥 Vɪᴅᴇᴏ" if upload_as_doc else "📁 Fɪʟᴇ",
        thumb="✅ Sᴇᴛ" if thumbnail else "❌ Nᴏᴛ sᴇᴛ",
        ytdl=g("ytdl_filter") or "mp4",
        caption=_short(g("caption")),
        dump=_short(g("dump_channel")),
        blocklist=f"{len(blocklist)} ᴡᴏʀᴅ(s)" if blocklist else "Nᴏɴᴇ",
        metadata=_short(g("metadata")),
    )

    B = types.InlineKeyboardButton
    rows = [
        [
            B(f"📁 Uᴘʟᴏᴀᴅ {'Vɪᴅᴇᴏ' if upload_as_doc else 'Fɪʟᴇ'}", callback_data="st_toggle_upload_as_doc"),
            B(f"🔔 Bᴏᴛ Uᴘᴅᴀᴛᴇs: {_flag(g('bot_updates'))}", callback_data="st_toggle_bot_updates"),
        ],
        [
            B(f"🖼 {'Cʜᴀɴɢᴇ' if thumbnail else 'Sᴇᴛ'} Tʜᴜᴍʙɴᴀɪʟ", callback_data="setThumbnail"),
            B(f"🔎 Yᴛᴅʟ Fɪʟᴛᴇʀ: {g('ytdl_filter')}", callback_data="st_cycle_ytdl_filter"),
        ],
        [
            B(f"📸 Sᴄʀᴇᴇɴsʜᴏᴛs: {_flag(g('generate_ss'), 'True', 'False')}", callback_data="st_toggle_generate_ss"),
            B(f"🎇 Sᴘᴏɪʟᴇʀ: {_flag(g('spoiler'))}", callback_data="st_toggle_spoiler"),
        ],
        [
            B("📝 Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ", callback_data="st_ask_caption"),
            B(f"🔒 Nᴏ Fᴏʀᴡᴀʀᴅs: {_flag(g('no_forwards'))}", callback_data="st_toggle_no_forwards"),
        ],
        [
            B(f"🧹 Fɪʟᴇɴᴀᴍᴇ Cʟᴇᴀɴᴇʀ: {_flag(g('filename_cleaner'))}", callback_data="st_toggle_filename_cleaner"),
            B("⚙️ Cᴜsᴛᴏᴍ Mᴇᴛᴀᴅᴀᴛᴀ", callback_data="st_ask_metadata"),
        ],
        [
            B(f"🎬 Sᴀᴍᴘʟᴇ Vɪᴅᴇᴏ: {_flag(g('generate_sample_video'))}", callback_data="st_toggle_generate_sample_video"),
            B(f"▶️ Sᴛʀᴇᴀᴍɪɴɢ: {_flag(g('streaming'))}", callback_data="st_toggle_streaming"),
        ],
        [
            B(f"⬆️ Cᴀᴘᴛɪᴏɴ Uᴘ: {_flag(g('caption_up'))}", callback_data="st_toggle_caption_up"),
            B("🗂 Dᴜᴍᴘ Cʜᴀɴɴᴇʟ", callback_data="st_ask_dump_channel"),
        ],
        [
            B("⚠️ Bʟᴏᴄᴋʟɪsᴛ Wᴏʀᴅs", callback_data="st_ask_blocklist_words"),
            B(f"📦 Aᴜᴛᴏ Uɴᴢɪᴘ: {_flag(g('auto_unzip'), 'Enabled', 'Disabled')}", callback_data="st_toggle_auto_unzip"),
        ],
    ]
    if thumbnail:
        rows.append([
            B("👀 Sʜᴏᴡ Tʜᴜᴍʙɴᴀɪʟ", callback_data="showThumbnail"),
            B("🗑 Dᴇʟᴇᴛᴇ Tʜᴜᴍʙ", callback_data="deleteThumbnail"),
        ])
    rows.append([B("♻️ Rᴇsᴇᴛ Sᴇᴛᴛɪɴɢs", callback_data="st_reset")])
    rows.append([
        B(BTN.PLANS, callback_data="plans"),
        B(BTN.HELP, callback_data="help"),
    ])
    rows.append([
        B(BTN.HOME, callback_data="home"),
        B(BTN.CLOSE, callback_data="close"),
    ])

    return text, types.InlineKeyboardMarkup(rows)


async def OpenSettings(m: "types.Message"):
    """Render/refresh the settings panel on an existing (editable) message."""
    user_id = m.chat.id
    try:
        text, markup = await build_settings(user_id)
    except Exception as err:
        Config.LOGGER.getLogger(__name__).error(err)
        await m.edit(f"{E.ERROR} <b>Fᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ʏᴏᴜʀ ᴅᴀᴛᴀ ғʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ!</b>")
        return

    try:
        await m.edit(text=text, reply_markup=markup, disable_web_page_preview=True)
    except errors.MessageNotModified:
        pass
    except errors.FloodWait as e:
        await asyncio.sleep(getattr(e, "value", 5))
        await OpenSettings(m)
    except Exception as err:
        Config.LOGGER.getLogger(__name__).error(err)


@Client.on_message(filters.private & filters.command("settings"))
async def settings_handler(bot: Client, m: Message):
    await AddUser(bot, m)
    editable = await m.reply_text(f"{E.REFRESH} <b>Lᴏᴀᴅɪɴɢ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs...</b>", quote=True)
    await OpenSettings(editable)
