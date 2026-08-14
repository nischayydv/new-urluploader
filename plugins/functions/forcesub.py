import os
import asyncio
from plugins.config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant, ChatAdminRequired, PeerIdInvalid, ChannelInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.emojis import E, BTN

async def handle_force_subscribe(bot, message):
    if not Config.UPDATES_CHANNEL:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"{E.ALERT} <b>Uᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ɪs ɴᴏᴛ ᴄᴏɴғɪɢᴜʀᴇᴅ.</b>\n\n{E.ARROW} <i>Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴀᴅᴍɪɴ.</i>",
            disable_web_page_preview=True,
        )
        return 400

    try:
        invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    except (ChatAdminRequired, PeerIdInvalid, ChannelInvalid, KeyError, ValueError) as e:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"{E.ERROR} <b>Bᴏᴛ ɪs ᴍɪssɪɴɢ ᴀᴄᴄᴇss ᴛᴏ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ.</b>\n\n{E.ARROW} <i>Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴀᴅᴍɪɴ!</i>",
            disable_web_page_preview=True,
        )
        return 400

    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), message.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=message.from_user.id,
                text=f"{E.LOCK} <b>Yᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ.</b>",
                disable_web_page_preview=True,
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"{E.CHANNEL} <b>Jᴏɪɴ Rᴇǫᴜɪʀᴇᴅ</b>\n\n<blockquote>{E.ARROW} Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.\n{E.ARROW} Tʜᴇɴ ᴛᴀᴘ <b>Rᴇғʀᴇsʜ</b>.</blockquote>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📢 Jᴏɪɴ Cʜᴀɴɴᴇʟ", url=invite_link.invite_link)],
                    [InlineKeyboardButton(BTN.REFRESH, callback_data="refreshForceSub")]
                ]
            ),
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"{E.ERROR} <b>Aɴ ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ.</b>\n\n{E.JOIN} <i>Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ sᴜᴘᴘᴏʀᴛ.</i>",
            disable_web_page_preview=True,
        )
        return 400
