# ⚠️ Credit: Developed by @NY_BOTS | Support: @NY_BOTS_SUPPORT | Channel: @NY_BOTS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from plugins.emojis import E, BTN

SUPPORT_LINK = "https://t.me/NY_BOTS_SUPPORT"
CHANNEL_LINK = "https://t.me/NY_BOTS"
OWNER_LINK = "https://t.me/NY_BOTS"


class Translation(object):

    START_TEXT = f"""{E.WELCOME} <b>Hᴇʟʟᴏ {{}}</b>

{E.ROCKET} <b>I ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ <u>URL → Tᴇʟᴇɢʀᴀᴍ Uᴘʟᴏᴀᴅᴇʀ</u></b>

<blockquote>{E.LINK} Sᴇɴᴅ ᴍᴇ ᴀɴʏ <b>ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ</b> ᴀɴᴅ I'ʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ Tᴇʟᴇɢʀᴀᴍ ᴀs ᴀ <b>Fɪʟᴇ</b> ᴏʀ <b>Sᴛʀᴇᴀᴍᴀʙʟᴇ Vɪᴅᴇᴏ</b> — ʙʟᴀᴢɪɴɢ ғᴀsᴛ.</blockquote>

{E.LIGHTNING} <b>Tᴜʀʙᴏ ᴇɴɢɪɴᴇ</b>  •  {E.SHIELD} <b>Sᴀғᴇ & ᴘʀɪᴠᴀᴛᴇ</b>  •  {E.DIAMOND} <b>Pʀᴇᴍɪᴜᴍ ᴜɪ</b>

{E.POINTER} <i>Tᴀᴘ</i> <b>Hᴇʟᴘ</b> <i>ᴛᴏ ʟᴇᴀʀɴ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ.</i>"""

    HELP_TEXT = f"""{E.CREATE} <b>Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ</b>

<blockquote>{E.SETTINGS} <b>1.</b> Oᴘᴇɴ /settings ᴀɴᴅ ᴛᴜɴᴇ ᴛʜᴇ ʙᴏᴛ ᴀs ʏᴏᴜ ʟɪᴋᴇ.
{E.CREATE} <b>2.</b> Sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ sᴀᴠᴇ ɪᴛ ᴀs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
{E.LINK} <b>3.</b> Sᴇɴᴅ <code>url | New Name.mkv</code> ᴛᴏ ʀᴇɴᴀᴍᴇ ᴡʜɪʟᴇ ᴜᴘʟᴏᴀᴅɪɴɢ.
{E.RIGHT} <b>4.</b> Cʜᴏᴏsᴇ ʏᴏᴜʀ ᴜᴘʟᴏᴀᴅ ғᴏʀᴍᴀᴛ ғʀᴏᴍ ᴛʜᴇ ʙᴜᴛᴛᴏɴs.
{E.INBOX} <b>5.</b> Rᴇᴘʟʏ /caption ᴛᴏ ᴀ ғɪʟᴇ ᴛᴏ sᴇᴛ ᴀ ᴄᴀᴘᴛɪᴏɴ.</blockquote>

{E.STATS} <b>Cᴏᴍᴍᴀɴᴅs</b>
{E.ARROW} /start — ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
{E.ARROW} /settings — ᴜᴘʟᴏᴀᴅ ᴘʀᴇғᴇʀᴇɴᴄᴇs
{E.ARROW} /caption — ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ
{E.ARROW} /info — ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ɪɴғᴏ
{E.ARROW} /about — ʙᴏᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ

{E.ALERT} <i>Lɪɴᴋs ᴍᴜsᴛ ʙᴇ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋs.</i>"""

    ABOUT_TEXT = f"""{E.CROWN} <b>Aʙᴏᴜᴛ Tʜɪs Bᴏᴛ</b>

<blockquote>{E.ID} <b>Nᴀᴍᴇ</b> : URL Uᴘʟᴏᴀᴅᴇʀ X
{E.ROCKET} <b>Fʀᴀᴍᴇᴡᴏʀᴋ</b> : <a href="https://docs.pyrogram.org/">PʏʀᴏBʟᴀᴄᴋ 2.6.8</a>
{E.CREATE} <b>Lᴀɴɢᴜᴀɢᴇ</b> : <a href="https://www.python.org">Pʏᴛʜᴏɴ 3.13</a>
{E.BACKUP} <b>Dᴀᴛᴀʙᴀsᴇ</b> : <a href="https://cloud.mongodb.com">MᴏɴɢᴏDB</a>
{E.JOIN} <b>Sᴜᴘᴘᴏʀᴛ</b> : <a href="{SUPPORT_LINK}">NY Sᴜᴘᴘᴏʀᴛ</a>
{E.CHANNEL} <b>Cʜᴀɴɴᴇʟ</b> : <a href="{CHANNEL_LINK}">NY Bᴏᴛs</a>
{E.HEART} <b>Dᴇᴠᴇʟᴏᴘᴇʀ</b> : <a href="{OWNER_LINK}">@NY_BOTS</a></blockquote>

{E.FIRE} <i>Bᴜɪʟᴛ ᴡɪᴛʜ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴜʀᴇ sᴘᴇᴇᴅ.</i>"""

    UPGRADE_TEXT = f"""{E.DIAMOND} <b>Pʀᴇᴍɪᴜᴍ Pʟᴀɴs</b>

<blockquote>{E.STAR} <b>Fʀᴇᴇ</b> — 7GB/ᴅᴀʏ • 2GB/ғɪʟᴇ • 5 MB/s
{E.CROWN} <b>Sɪʟᴠᴇʀ</b> — 25GB/ᴅᴀʏ • 4GB/ғɪʟᴇ • ᴛᴜʀʙᴏ sᴘᴇᴇᴅ
{E.WINNER} <b>Gᴏʟᴅ</b> — Uɴʟɪᴍɪᴛᴇᴅ • ɴᴏ ᴀᴅs • ᴘʀɪᴏʀɪᴛʏ ǫᴜᴇᴜᴇ
{E.GIFT} <b>Sᴛᴜᴅᴇɴᴛ</b> — sᴘᴇᴄɪᴀʟ ᴅɪsᴄᴏᴜɴᴛᴇᴅ ᴘʟᴀɴ</blockquote>

{E.MONEY} <b>Uᴘɢʀᴀᴅᴇ ᴘᴇʀᴋs</b>
{E.ARROW} Bɪɢɢᴇʀ ᴅᴀɪʟʏ & ғɪʟᴇ ʟɪᴍɪᴛs
{E.ARROW} Fᴜʟʟ sᴘᴇᴇᴅ ᴜᴘʟᴏᴀᴅs, ɴᴏ ᴛɪᴍᴇ ɢᴀᴘ
{E.ARROW} Sᴄʀᴇᴇɴsʜᴏᴛs, sᴀᴍᴘʟᴇ ᴠɪᴅᴇᴏ & ᴍᴇᴛᴀᴅᴀᴛᴀ

{E.POINTER} <i>Cᴏɴᴛᴀᴄᴛ</i> <a href="{OWNER_LINK}">@NY_BOTS</a> <i>ᴛᴏ ᴜᴘɢʀᴀᴅᴇ.</i>"""

    PROGRESS = f"""<blockquote>{E.CHART} <b>Pʀᴏɢʀᴇss</b> : {{0}}%
{E.CONFIRM} <b>Dᴏɴᴇ</b> : {{1}}
{E.INBOX} <b>Tᴏᴛᴀʟ</b> : {{2}}
{E.ROCKET} <b>Sᴘᴇᴇᴅ</b> : {{3}}/s
{E.CLOCK} <b>ETA</b> : {{4}}</blockquote>
"""

    PROGRES = """
`{}`\n{}"""

    INFO_TEXT = f"""{E.USERS} <b>Yᴏᴜʀ Aᴄᴄᴏᴜɴᴛ</b>

<blockquote>{E.ID} <b>Fɪʀsᴛ Nᴀᴍᴇ</b> : <b>{{}}</b>
{E.ID} <b>Lᴀsᴛ Nᴀᴍᴇ</b> : <b>{{}}</b>
{E.SMILE} <b>Usᴇʀɴᴀᴍᴇ</b> : <b>@{{}}</b>
{E.LOCK} <b>Usᴇʀ ID</b> : <code>{{}}</code>
{E.LINK} <b>Pʀᴏғɪʟᴇ</b> : <b>{{}}</b>
{E.LOCATION} <b>DC</b> : <b>{{}}</b>
{E.CREATE} <b>Lᴀɴɢᴜᴀɢᴇ</b> : <b>{{}}</b>
{E.LIGHTNING} <b>Sᴛᴀᴛᴜs</b> : <b>{{}}</b></blockquote>"""

    START_BUTTONS = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(BTN.SETTINGS, callback_data='OpenSettings')],
            [
                InlineKeyboardButton(BTN.HELP, callback_data='help'),
                InlineKeyboardButton(BTN.PLANS, callback_data='plans'),
            ],
            [
                InlineKeyboardButton(BTN.ABOUT, callback_data='about'),
                InlineKeyboardButton(BTN.UPDATES, url=CHANNEL_LINK),
            ],
            [InlineKeyboardButton(BTN.SUPPORT, url=SUPPORT_LINK)],
            [InlineKeyboardButton(BTN.CLOSE, callback_data='close')],
        ]
    )

    HELP_BUTTONS = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(BTN.SETTINGS, callback_data='OpenSettings')],
            [
                InlineKeyboardButton(BTN.PLANS, callback_data='plans'),
                InlineKeyboardButton(BTN.ABOUT, callback_data='about'),
            ],
            [
                InlineKeyboardButton(BTN.HOME, callback_data='home'),
                InlineKeyboardButton(BTN.SUPPORT, url=SUPPORT_LINK),
            ],
            [InlineKeyboardButton(BTN.CLOSE, callback_data='close')],
        ]
    )

    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(BTN.OWNER, url=OWNER_LINK),
                InlineKeyboardButton(BTN.UPDATES, url=CHANNEL_LINK),
            ],
            [
                InlineKeyboardButton(BTN.HELP, callback_data='help'),
                InlineKeyboardButton(BTN.PLANS, callback_data='plans'),
            ],
            [InlineKeyboardButton(BTN.HOME, callback_data='home')],
            [InlineKeyboardButton(BTN.CLOSE, callback_data='close')],
        ]
    )

    PLANS_BUTTONS = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("👑 Bᴜʏ Pʀᴇᴍɪᴜᴍ", url=OWNER_LINK)],
            [
                InlineKeyboardButton(BTN.HELP, callback_data='help'),
                InlineKeyboardButton(BTN.ABOUT, callback_data='about'),
            ],
            [
                InlineKeyboardButton(BTN.HOME, callback_data='home'),
                InlineKeyboardButton(BTN.CLOSE, callback_data='close'),
            ],
        ]
    )

    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(BTN.CLOSE, callback_data='close')
        ]]
    )

    INCORRECT_REQUEST = f"{E.ERROR} <b>Iɴᴠᴀʟɪᴅ ʀᴇǫᴜᴇsᴛ, ᴛʀʏ ᴀɢᴀɪɴ.</b>"
    DOWNLOAD_FAILED = f"{E.ERROR} <b>Dᴏᴡɴʟᴏᴀᴅ ғᴀɪʟᴇᴅ!</b>\n\n{E.ALERT} <i>Cʜᴇᴄᴋ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.</i>"
    TEXT = f"{E.CREATE} <b>Sᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴘʜᴏᴛᴏ ɴᴏᴡ.</b>"
    IFLONG_FILE_NAME = f"{E.ALERT} <b>Oɴʟʏ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs ᴀʀᴇ ᴀʟʟᴏᴡᴇᴅ ɪɴ ᴀ ғɪʟᴇ ɴᴀᴍᴇ.</b>"
    RENAME_403_ERR = f"{E.LOCK} <b>Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴛʜɪs ғɪʟᴇ.</b>"
    ABS_TEXT = f"{E.ALERT} <b>Pʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʙᴇ sᴇʟғɪsʜ.</b>"
    FORMAT_SELECTION = f"{E.POINTER} <b>Sᴇʟᴇᴄᴛ ʏᴏᴜʀ ғᴏʀᴍᴀᴛ ʙᴇʟᴏᴡ</b>\n"
    SET_CUSTOM_USERNAME_PASSWORD = (
        f"{E.RIGHT} <b>Vɪᴅᴇᴏ</b> — ᴜᴘʟᴏᴀᴅ ᴀs sᴛʀᴇᴀᴍᴀʙʟᴇ ᴠɪᴅᴇᴏ\n\n"
        f"{E.INBOX} <b>Fɪʟᴇ</b> — ᴜᴘʟᴏᴀᴅ ᴀs ᴅᴏᴄᴜᴍᴇɴᴛ\n\n"
        f"{E.CROWN} <b>Pᴏᴡᴇʀᴇᴅ Bʏ</b> : @NY_BOTS"
    )
    NOYES_URL = f"{E.ALERT} <b>Sʟᴏᴡ URL ᴅᴇᴛᴇᴄᴛᴇᴅ.</b>\n\n{E.LINK} <i>Pʟᴇᴀsᴇ sᴇɴᴅ ᴀ ғᴀsᴛ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ.</i>"
    DOWNLOAD_START = f"{E.INBOX} <b>Dᴏᴡɴʟᴏᴀᴅɪɴɢ...</b>\n\n<blockquote>{E.LINK} <b>Fɪʟᴇ</b> : {{}}</blockquote>"
    UPLOAD_START = f"{E.UPLOAD} <b>Uᴘʟᴏᴀᴅɪɴɢ ᴛᴏ Tᴇʟᴇɢʀᴀᴍ...</b>"
    RCHD_BOT_API_LIMIT = f"{E.ALERT} <b>Sɪᴢᴇ ᴇxᴄᴇᴇᴅs 50MB ʙᴏᴛ ʟɪᴍɪᴛ — sᴛɪʟʟ ᴛʀʏɪɴɢ ᴛᴏ ᴜᴘʟᴏᴀᴅ.</b>"
    RCHD_TG_API_LIMIT = (
        f"{E.CONFIRM} <b>Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ</b> {{}} <b>sᴇᴄᴏɴᴅs</b>\n"
        f"{E.INBOX} <b>Sɪᴢᴇ</b> : {{}}\n\n"
        f"{E.ERROR} <i>I ᴄᴀɴɴᴏᴛ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ʟᴀʀɢᴇʀ ᴛʜᴀɴ 2000MB.</i>"
    )
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = (
        f"{E.CONFETTI} <b>Uᴘʟᴏᴀᴅ Cᴏᴍᴘʟᴇᴛᴇᴅ</b>\n\n{E.LOVE} <i>Tʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!</i>"
    )
    SAVED_CUSTOM_THUMB_NAIL = f"{E.CONFIRM} <b>Tʜᴜᴍʙɴᴀɪʟ sᴀᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = f"{E.CLEAR} <b>Tʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!</b>"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = f"{E.CONFIRM} <b>Mᴇᴅɪᴀ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.</b>"
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = f"{E.ALERT} <b>Nᴏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ғᴏᴜɴᴅ.</b>"
    NO_VOID_FORMAT_FOUND = f"{E.ERROR} <b>Eʀʀᴏʀ</b> : <code>{{}}</code>"
    FILE_NOT_FOUND = f"{E.ERROR} <b>Fɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ!</b>"
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = f"{E.CHANNEL} <b>Jᴏɪɴ</b> @NY_BOTS <b>ғᴏʀ ᴍᴏʀᴇ ᴘʀᴇᴍɪᴜᴍ ʙᴏᴛs.</b>"
    ADD_CAPTION_HELP = f"""{E.CREATE} <b>Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ</b>

<blockquote>{E.ARROW} Fᴏʀᴡᴀʀᴅ ᴏʀ sᴇʟᴇᴄᴛ ᴀɴʏ Tᴇʟᴇɢʀᴀᴍ ғɪʟᴇ.
{E.ARROW} Rᴇᴘʟʏ ᴛᴏ ɪᴛ ᴡɪᴛʜ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ᴛᴇxᴛ.
{E.ARROW} Tʜᴇ ᴄᴀᴘᴛɪᴏɴ ᴡɪʟʟ ʙᴇ ᴀᴛᴛᴀᴄʜᴇᴅ ɪɴsᴛᴀɴᴛʟʏ.</blockquote>

{E.POINTER} <a href="https://te.legra.ph/file/ecf5297246c5fb574d1a0.jpg">Sᴇᴇ ᴇxᴀᴍᴘʟᴇ</a>"""
