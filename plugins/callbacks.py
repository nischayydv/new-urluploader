# ⚠️ Credit: Developed by @NY_BOTS | Support: @NY_BOTS_SUPPORT | Channel: @NY_BOTS
import logging

from pyrogram import Client, types
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from plugins.button import youtube_dl_call_back
from plugins.config import Config
from plugins.database.database import db
from plugins.dl_button import ddl_call_back
from plugins.emojis import E, e
from plugins.script import Translation
from plugins.settings.settings import OpenSettings

logger = logging.getLogger(__name__)


async def _show_home(update):
    await update.message.edit(
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=Translation.START_BUTTONS,
        disable_web_page_preview=True,
    )


async def _refresh_force_sub(bot, update) -> None:
    """Re-check channel membership, then show the home screen."""
    if not Config.UPDATES_CHANNEL:
        await _show_home(update)
        return

    channel = Config.UPDATES_CHANNEL
    channel_chat_id = int(channel) if str(channel).startswith("-100") else channel

    try:
        user = await bot.get_chat_member(channel_chat_id, update.message.chat.id)
        if user.status == "kicked":
            await update.message.edit(
                text=Translation.BANNED_TEXT, disable_web_page_preview=True
            )
            return
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(channel_chat_id)
            join_url = invite_link.invite_link
        except Exception:
            join_url = "https://t.me/NY_BOTS"
        await update.message.edit(
            text=Translation.FORCE_SUB_TEXT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f'{e("CHANNEL")} JOIN CHANNEL', url=join_url)],
                [InlineKeyboardButton(f'{e("REFRESH")} REFRESH', callback_data="refreshForceSub")],
            ]),
            disable_web_page_preview=True,
        )
        return
    except Exception as err:
        logger.error(err)
        await update.message.edit(
            text=Translation.SOMETHING_WRONG, disable_web_page_preview=True
        )
        return

    await _show_home(update)


async def _toggle(update, getter, setter) -> None:
    await update.answer()
    current = await getter(update.from_user.id)
    await setter(update.from_user.id, not current)
    await OpenSettings(update.message)


@Client.on_callback_query()
async def button(bot, update):
    data = update.data

    if data == "home":
        await _show_home(update)

    elif data == "help":
        await update.message.edit(
            text=Translation.HELP_TEXT,
            reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True,
        )

    elif data == "plans":
        await update.message.edit(
            text=Translation.UPGRADE_TEXT,
            reply_markup=Translation.PLANS_BUTTONS,
            disable_web_page_preview=True,
        )

    elif data == "about":
        await update.message.edit(
            text=Translation.ABOUT_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True,
        )

    elif "refreshForceSub" in data:
        await _refresh_force_sub(bot, update)

    elif data == "OpenSettings":
        await update.answer()
        await OpenSettings(update.message)

    elif data == "showThumbnail":
        thumbnail = await db.get_thumbnail(update.from_user.id)
        if not thumbnail:
            await update.answer(f'{e("ALERT")} No custom thumbnail saved!', show_alert=True)
        else:
            await update.answer()
            await bot.send_photo(
                update.message.chat.id,
                thumbnail,
                caption=f"{E.CREATE} <b>Yᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ</b>",
                reply_markup=types.InlineKeyboardMarkup([[
                    types.InlineKeyboardButton(
                        f'{e("CLEAR")} DELETE THUMBNAIL', callback_data="deleteThumbnail"
                    )
                ]]),
            )

    elif data == "deleteThumbnail":
        await db.set_thumbnail(update.from_user.id, None)
        await update.answer(
            f'{e("CLEAR")} Thumbnail deleted. Default thumbnail will be used.',
            show_alert=True,
        )
        await update.message.delete(True)

    elif data == "setThumbnail":
        await update.message.edit(
            text=Translation.TEXT,
            reply_markup=Translation.BUTTONS,
            disable_web_page_preview=True,
        )

    elif data == "triggerGenSS":
        await _toggle(update, db.get_generate_ss, db.set_generate_ss)

    elif data == "triggerGenSample":
        await _toggle(update, db.get_generate_sample_video, db.set_generate_sample_video)

    elif data == "triggerUploadMode":
        await _toggle(update, db.get_upload_as_doc, db.set_upload_as_doc)

    elif "close" in data:
        await update.message.delete(True)

    elif "|" in data:
        await youtube_dl_call_back(bot, update)

    elif "=" in data:
        await ddl_call_back(bot, update)

    else:
        await update.message.delete()
