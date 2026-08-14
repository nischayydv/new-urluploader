# ⚠️ Credit: Developed by @NY_BOTS | Support: @NY_BOTS_SUPPORT | Channel: @NY_BOTS
import asyncio
import logging

from pyrogram import Client, errors, filters, types
from pyrogram.types import Message

from plugins.config import Config
from plugins.database.add import AddUser
from plugins.database.database import db
from plugins.emojis import E, e
from plugins.script import Translation

logger = logging.getLogger(__name__)


def _settings_text(upload_as_doc: bool, thumbnail) -> str:
    mode = "Dᴏᴄᴜᴍᴇɴᴛ" if upload_as_doc else "Vɪᴅᴇᴏ"
    thumb = "Sᴀᴠᴇᴅ" if thumbnail else "Nᴏᴛ sᴇᴛ"
    return (
        f"{E.SETTINGS} <b>Yᴏᴜʀ Sᴇᴛᴛɪɴɢs</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"{E.RIGHT} <b>Uᴘʟᴏᴀᴅ Mᴏᴅᴇ</b> : <b>{mode}</b>\n"
        f"{E.CREATE} <b>Tʜᴜᴍʙɴᴀɪʟ</b> : <b>{thumb}</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"{E.POINTER} Tᴀᴘ ᴀ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴄʜᴀɴɢᴇ ɪᴛ."
    )


async def OpenSettings(m: "types.Message"):
    usr_id = m.chat.id
    user_data = await db.get_user_data(usr_id)
    if not user_data:
        await m.edit(f"{E.ERROR} <b>Fᴀɪʟᴇᴅ ᴛᴏ ꜰᴇᴛᴄʜ ʏᴏᴜʀ ᴅᴀᴛᴀ.</b>")
        return

    upload_as_doc = user_data.get("upload_as_doc", False)
    thumbnail = user_data.get("thumbnail", None)

    buttons_markup = [
        [types.InlineKeyboardButton(
            f'{e("RIGHT")} UPLOAD AS · {"VIDEO" if upload_as_doc else "DOCUMENT"}',
            callback_data="triggerUploadMode",
        )],
        [types.InlineKeyboardButton(
            f'{e("CREATE")} {"CHANGE" if thumbnail else "SET"} THUMBNAIL',
            callback_data="setThumbnail",
        )],
    ]
    if thumbnail:
        buttons_markup.append([types.InlineKeyboardButton(
            f'{e("SEARCH")} SHOW THUMBNAIL', callback_data="showThumbnail",
        )])
    buttons_markup.append([
        types.InlineKeyboardButton(f'{e("BACK")} BACK', callback_data="home"),
        types.InlineKeyboardButton(f'{e("CANCEL")} CLOSE', callback_data="close"),
    ])

    try:
        await m.edit(
            text=_settings_text(upload_as_doc, thumbnail),
            reply_markup=types.InlineKeyboardMarkup(buttons_markup),
            disable_web_page_preview=True,
        )
    except errors.MessageNotModified:
        pass
    except errors.FloodWait as ex:
        await asyncio.sleep(getattr(ex, "value", getattr(ex, "x", 5)))
        await OpenSettings(m)
    except Exception as err:
        logger.error(err)


@Client.on_message(filters.private & filters.command("settings"))
async def settings_handler(bot: Client, m: Message):
    await AddUser(bot, m)
    editable = await m.reply_text(f"{E.LIGHTNING} <b>Lᴏᴀᴅɪɴɢ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs…</b>", quote=True)
    await OpenSettings(editable)
