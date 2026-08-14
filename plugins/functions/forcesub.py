# ⚠️ Credit: Developed by @NY_BOTS | Support: @NY_BOTS_SUPPORT | Channel: @NY_BOTS
import asyncio

from pyrogram.errors import (
    ChannelInvalid,
    ChatAdminRequired,
    FloodWait,
    PeerIdInvalid,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from plugins.config import Config
from plugins.emojis import E, e
from plugins.script import Translation

NOT_CONFIGURED = (
    f"{E.ALERT} <b>Uᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ɪs ɴᴏᴛ ᴄᴏɴꜰɪɢᴜʀᴇᴅ.</b>\n\n"
    f"{E.POINTER} Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴀᴅᴍɪɴ."
)
MISSING_ACCESS = (
    f"{E.SHIELD} <b>ⵊ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀᴄᴄᴇss ᴛᴏ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ.</b>\n\n"
    f"{E.POINTER} Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴀᴅᴍɪɴ."
)


async def handle_force_subscribe(bot, message):
    if not Config.UPDATES_CHANNEL:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=NOT_CONFIGURED,
            disable_web_page_preview=True,
        )
        return 400

    try:
        invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    except FloodWait as ex:
        await asyncio.sleep(getattr(ex, "value", getattr(ex, "x", 5)))
        return 400
    except (ChatAdminRequired, PeerIdInvalid, ChannelInvalid, KeyError, ValueError):
        await bot.send_message(
            chat_id=message.from_user.id,
            text=MISSING_ACCESS,
            disable_web_page_preview=True,
        )
        return 400

    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), message.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=message.from_user.id,
                text=Translation.BANNED_TEXT,
                disable_web_page_preview=True,
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=Translation.FORCE_SUB_TEXT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f'{e("CHANNEL")} JOIN CHANNEL', url=invite_link.invite_link)],
                [InlineKeyboardButton(f'{e("REFRESH")} REFRESH', callback_data="refreshForceSub")],
            ]),
            disable_web_page_preview=True,
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=Translation.SOMETHING_WRONG,
            disable_web_page_preview=True,
        )
        return 400
