# ⚠️ Credit: Developed by @NY_BOTS | Support: @NY_BOTS_SUPPORT | Channel: @NY_BOTS
"""All user facing copy + inline keyboards, styled with premium emoji.

Message text/captions use `E.NAME` (premium custom emoji).
Inline button labels use `e("NAME")` because Telegram buttons cannot render
custom emoji.
"""

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from plugins.emojis import E, e

# --------------------------------------------------------------------------- #
#  Branding
# --------------------------------------------------------------------------- #
BOT_NAME = "URL Uᴘʟᴏᴀᴅᴇʀ"
SUPPORT_LINK = "https://t.me/NY_BOTS_SUPPORT"
CHANNEL_LINK = "https://t.me/NY_BOTS"
DEV_LINK = "https://t.me/NY_BOTS"

LINE = "━━━━━━━━━━━━━━━━━━━"


def _row(*buttons: InlineKeyboardButton) -> list[InlineKeyboardButton]:
    return list(buttons)


def _btn(label: str, **kwargs) -> InlineKeyboardButton:
    return InlineKeyboardButton(label, **kwargs)


# Reusable button labels (unicode fallbacks — buttons only)
B_SETTINGS = f'{e("SETTINGS")} SETTINGS'
B_HELP = f'{e("POINTER")} HELP'
B_ABOUT = f'{e("STAR")} ABOUT'
B_CLOSE = f'{e("CANCEL")} CLOSE'
B_HOME = f'{e("MAIN_MENU")} HOME'
B_BACK = f'{e("BACK")} BACK'
B_CHANNEL = f'{e("CHANNEL")} UPDATES'
B_SUPPORT = f'{e("USERS")} SUPPORT'


class Translation(object):

    # ----------------------------------------------------------------- texts
    START_TEXT = f"""{E.WELCOME} <b>Hᴇʟʟᴏ {{}}</b>

{E.ROCKET} ⵊ ᴀᴍ <b>{BOT_NAME} Bᴏᴛ</b> — sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ᴀɴᴅ ⵊ'ʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ Tᴇʟᴇɢʀᴀᴍ ᴀs ᴀ <b>ꜰɪʟᴇ</b> ᴏʀ <b>ᴠɪᴅᴇᴏ</b>.

{E.LIGHTNING} <b>Bʟᴀᴢɪɴɢ ꜰᴀsᴛ</b> · {E.SHIELD} <b>Sᴀꜰᴇ</b> · {E.DIAMOND} <b>4GB Sᴜᴘᴘᴏʀᴛ</b>

{E.POINTER} Tᴀᴘ <b>HELP</b> ᴛᴏ ʟᴇᴀʀɴ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ."""

    HELP_TEXT = f"""{E.INBOX} <b>Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ</b>
{LINE}
{E.SETTINGS} <b>1.</b> Oᴘᴇɴ /settings ᴀɴᴅ ᴛᴜɴᴇ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ᴛᴀsᴛᴇ.

{E.CREATE} <b>2.</b> Sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ sᴀᴠᴇ ɪᴛ ᴀs ʏᴏᴜʀ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

{E.LINK} <b>3.</b> Sᴇɴᴅ <code>url | new name.mkv</code> ᴛᴏ ʀᴇɴᴀᴍᴇ ᴡʜɪʟᴇ ᴜᴘʟᴏᴀᴅɪɴɢ.

{E.RIGHT} <b>4.</b> Pɪᴄᴋ ʏᴏᴜʀ ᴅᴇsɪʀᴇᴅ ꜰᴏʀᴍᴀᴛ ꜰʀᴏᴍ ᴛʜᴇ ʙᴜᴛᴛᴏɴs.

{E.SPEAKER} <b>5.</b> Usᴇ /caption ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ ᴛᴏ sᴇᴛ ᴀ ᴄᴀᴘᴛɪᴏɴ.
{LINE}
{E.HEART} <b>Nᴇᴇᴅ ʜᴇʟᴘ?</b> <a href="{SUPPORT_LINK}">Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ</a>"""

    ABOUT_TEXT = f"""{E.CROWN} <b>Aʙᴏᴜᴛ Mᴇ</b>
{LINE}
{E.ROCKET} <b>Nᴀᴍᴇ</b> : {BOT_NAME} Bᴏᴛ
{E.LIGHTNING} <b>Fʀᴀᴍᴇᴡᴏʀᴋ</b> : <a href="https://docs.pyrogram.org/">PʏʀᴏBʟᴀᴄᴋ 2.6.8</a>
{E.DIAMOND} <b>Lᴀɴɢᴜᴀɢᴇ</b> : <a href="https://www.python.org">Pʏᴛʜᴏɴ 3.13</a>
{E.BACKUP} <b>Dᴀᴛᴀʙᴀsᴇ</b> : <a href="https://cloud.mongodb.com">MᴏɴɢᴏDB</a>
{E.USERS} <b>Sᴜᴘᴘᴏʀᴛ</b> : <a href="{SUPPORT_LINK}">NY Sᴜᴘᴘᴏʀᴛ</a>
{E.CHANNEL} <b>Cʜᴀɴɴᴇʟ</b> : <a href="{CHANNEL_LINK}">NY Bᴏᴛs</a>
{E.SHIELD} <b>Dᴇᴠᴇʟᴏᴘᴇʀ</b> : <a href="{DEV_LINK}">@NY_BOTS</a>
{LINE}
{E.LOVE} <i>Tʜᴀɴᴋs ꜰᴏʀ sᴛᴀʏɪɴɢ ᴡɪᴛʜ ᴜs.</i>"""

    UPGRADE_TEXT = f"""{E.MONEY_BAG} <b>Pʀᴇᴍɪᴜᴍ Pʟᴀɴs</b>
{LINE}
{E.CONFIRM} Nᴏ ᴀᴅs & ɴᴏ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ
{E.LIGHTNING} Pʀɪᴏʀɪᴛʏ ᴜᴘʟᴏᴀᴅ sᴘᴇᴇᴅ
{E.DIAMOND} Uɴʟɪᴍɪᴛᴇᴅ ᴅᴀɪʟʏ ᴛᴀsᴋs
{LINE}
{E.POINTER} Cᴏɴᴛᴀᴄᴛ <a href="{DEV_LINK}">@NY_BOTS</a> ᴛᴏ ᴜᴘɢʀᴀᴅᴇ."""

    SETTINGS_TEXT = f"""{E.SETTINGS} <b>Yᴏᴜʀ Sᴇᴛᴛɪɴɢs</b>
{LINE}
{E.POINTER} Tᴀᴘ ᴀ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴄʜᴀɴɢᴇ ɪᴛ."""

    PROGRESS = f"""{E.CHART} <b>Pʀᴏɢʀᴇss</b> : {{0}}%
{E.CONFIRM} <b>Dᴏɴᴇ</b> : {{1}}
{E.INBOX} <b>Tᴏᴛᴀʟ</b> : {{2}}
{E.ROCKET} <b>Sᴘᴇᴇᴅ</b> : {{3}}/s
{E.CALENDAR} <b>Eᴛᴀ</b> : {{4}}
{LINE}"""

    PROGRES = """<code>{}</code>\n{}"""

    INFO_TEXT = f"""{E.USERS} <b>Yᴏᴜʀ Pʀᴏꜰɪʟᴇ</b>
{LINE}
{E.SMILE} <b>Fɪʀsᴛ Nᴀᴍᴇ</b> : <b>{{}}</b>
{E.SMILE} <b>Lᴀsᴛ Nᴀᴍᴇ</b> : <b>{{}}</b>
{E.POINTER} <b>Usᴇʀɴᴀᴍᴇ</b> : <b>@{{}}</b>
{E.ID} <b>Usᴇʀ ⵊᴅ</b> : <code>{{}}</code>
{E.LINK} <b>Pʀᴏꜰɪʟᴇ</b> : <b>{{}}</b>
{E.LOCATION} <b>Dᴄ</b> : <b>{{}}</b>
{E.CHANNEL} <b>Lᴀɴɢᴜᴀɢᴇ</b> : <b>{{}}</b>
{E.STAR} <b>Sᴛᴀᴛᴜs</b> : <b>{{}}</b>
{LINE}"""

    # ------------------------------------------------------------- keyboards
    START_BUTTONS = InlineKeyboardMarkup([
        _row(_btn(B_SETTINGS, callback_data="OpenSettings")),
        _row(_btn(B_HELP, callback_data="help"), _btn(B_ABOUT, callback_data="about")),
        _row(_btn(B_CHANNEL, url=CHANNEL_LINK), _btn(B_SUPPORT, url=SUPPORT_LINK)),
        _row(_btn(B_CLOSE, callback_data="close")),
    ])

    HELP_BUTTONS = InlineKeyboardMarkup([
        _row(_btn(B_SETTINGS, callback_data="OpenSettings")),
        _row(_btn(B_BACK, callback_data="home"), _btn(B_ABOUT, callback_data="about")),
        _row(_btn(B_CLOSE, callback_data="close")),
    ])

    ABOUT_BUTTONS = InlineKeyboardMarkup([
        _row(_btn(B_SETTINGS, callback_data="OpenSettings")),
        _row(_btn(B_BACK, callback_data="home"), _btn(B_HELP, callback_data="help")),
        _row(_btn(B_CLOSE, callback_data="close")),
    ])

    PLANS_BUTTONS = InlineKeyboardMarkup([
        _row(_btn(B_ABOUT, callback_data="about")),
        _row(_btn(B_BACK, callback_data="home"), _btn(B_HELP, callback_data="help")),
        _row(_btn(B_CLOSE, callback_data="close")),
    ])

    BUTTONS = InlineKeyboardMarkup([
        _row(_btn(B_CLOSE, callback_data="close")),
    ])

    # ----------------------------------------------------------- short lines
    INCORRECT_REQUEST = f"{E.ERROR} <b>Bᴀᴅ ʀᴇǫᴜᴇsᴛ. Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.</b>"
    DOWNLOAD_FAILED = f"{E.ERROR} <b>Dᴏᴡɴʟᴏᴀᴅ ꜰᴀɪʟᴇᴅ.</b>"
    TEXT = f"{E.CREATE} <b>Sᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴘʜᴏᴛᴏ.</b>"
    IFLONG_FILE_NAME = f"{E.ALERT} <b>Fɪʟᴇ ɴᴀᴍᴇ ᴄᴀɴ ʙᴇ ᴜᴘ ᴛᴏ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs ᴏɴʟʏ.</b>"
    RENAME_403_ERR = f"{E.LOCK} <b>Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴛʜɪs ꜰɪʟᴇ.</b>"
    ABS_TEXT = f"{E.CLOWN} <b>Pʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʙᴇ sᴇʟꜰɪsʜ.</b>"
    FORMAT_SELECTION = f"{E.RIGHT} <b>Sᴇʟᴇᴄᴛ ʏᴏᴜʀ ꜰᴏʀᴍᴀᴛ ʙᴇʟᴏᴡ</b>\n"
    SET_CUSTOM_USERNAME_PASSWORD = (
        f"{E.RIGHT} <b>Vɪᴅᴇᴏ</b> — ᴜᴘʟᴏᴀᴅ ᴀs sᴛʀᴇᴀᴍᴀʙʟᴇ\n\n"
        f"{E.INBOX} <b>Fɪʟᴇ</b> — ᴜᴘʟᴏᴀᴅ ᴀs ᴅᴏᴄᴜᴍᴇɴᴛ\n\n"
        f"{E.SHIELD} <b>Pᴏᴡᴇʀᴇᴅ ʙʏ</b> : @NY_BOTS"
    )
    NOYES_URL = (
        f"{E.ALERT} <b>Sʟᴏᴡ URL ᴅᴇᴛᴇᴄᴛᴇᴅ.</b>\n\n"
        f"{E.POINTER} Pʟᴇᴀsᴇ sᴇɴᴅ ᴀ ꜰᴀsᴛᴇʀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ sᴏ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴀʀᴇɴ'ᴛ sʟᴏᴡᴇᴅ ᴅᴏᴡɴ."
    )
    SLOW_URL_DECED = NOYES_URL
    DOWNLOAD_START = f"{E.INBOX} <b>Dᴏᴡɴʟᴏᴀᴅɪɴɢ…</b>\n\n{E.LINK} <b>Fɪʟᴇ</b> : <code>{{}}</code>"
    UPLOAD_START = f"{E.ROCKET} <b>Uᴘʟᴏᴀᴅɪɴɢ ᴛᴏ Tᴇʟᴇɢʀᴀᴍ…</b>"
    RCHD_BOT_API_LIMIT = (
        f"{E.ALERT} <b>Fɪʟᴇ ɪs ʟᴀʀɢᴇʀ ᴛʜᴀɴ 50MB.</b> Tʀʏɪɴɢ ᴀɴʏᴡᴀʏ…"
    )
    RCHD_TG_API_LIMIT = (
        f"{E.CONFIRM} <b>Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ</b> <code>{{}}</code> <b>sᴇᴄᴏɴᴅs</b>\n"
        f"{E.CHART} <b>Sɪᴢᴇ</b> : <code>{{}}</code>\n\n"
        f"{E.ERROR} <b>Fɪʟᴇs ᴏᴠᴇʀ 2000MB ᴄᴀɴ'ᴛ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ (Tᴇʟᴇɢʀᴀᴍ ʟɪᴍɪᴛ).</b>"
    )
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = (
        f"{E.CELEBRATE} <b>Tʜᴀɴᴋs ꜰᴏʀ ᴜsɪɴɢ ᴍᴇ!</b> {E.LOVE}"
    )
    SAVED_CUSTOM_THUMB_NAIL = f"{E.CONFIRM} <b>Tʜᴜᴍʙɴᴀɪʟ sᴀᴠᴇᴅ.</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = f"{E.CLEAR} <b>Tʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ.</b>"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = f"{E.CLEAR} <b>Mᴇᴅɪᴀ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.</b>"
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = f"{E.ALERT} <b>Nᴏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ꜰᴏᴜɴᴅ.</b>"
    NO_VOID_FORMAT_FOUND = f"{E.ERROR} <b>Eʀʀᴏʀ</b> : <code>{{}}</code>"
    FILE_NOT_FOUND = f"{E.ERROR} <b>Fɪʟᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ.</b>"
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = f"{E.CHANNEL} Jᴏɪɴ @NY_BOTS ꜰᴏʀ ᴍᴏʀᴇ ʙᴏᴛs."
    ADD_CAPTION_HELP = f"""{E.SPEAKER} <b>Hᴏᴡ ᴛᴏ ᴀᴅᴅ ᴀ ᴄᴀᴘᴛɪᴏɴ</b>
{LINE}
{E.RIGHT} Fᴏʀᴡᴀʀᴅ ᴏʀ sᴇʟᴇᴄᴛ ᴀɴʏ Tᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ.
{E.RIGHT} Rᴇᴘʟʏ ᴛᴏ ɪᴛ ᴡɪᴛʜ ᴛʜᴇ ᴛᴇxᴛ ʏᴏᴜ ᴡᴀɴᴛ — ᴛʜᴀᴛ ʙᴇᴄᴏᴍᴇs ᴛʜᴇ ᴄᴀᴘᴛɪᴏɴ.
{LINE}
{E.POINTER} <a href="https://te.legra.ph/file/ecf5297246c5fb574d1a0.jpg">Sᴇᴇ ᴇxᴀᴍᴘʟᴇ</a>"""

    # -------------------------------------------------------- force subscribe
    FORCE_SUB_TEXT = f"""{E.LOCK} <b>Aᴄᴄᴇss Rᴇsᴛʀɪᴄᴛᴇᴅ</b>
{LINE}
{E.CHANNEL} Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ, ᴛʜᴇɴ ᴛᴀᴘ <b>Rᴇꜰʀᴇsʜ</b>."""
    BANNED_TEXT = (
        f"{E.ENDED} <b>Yᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ.</b>\n\n"
        f'{E.USERS} <a href="{SUPPORT_LINK}">Cᴏɴᴛᴀᴄᴛ Sᴜᴘᴘᴏʀᴛ</a>'
    )
    SOMETHING_WRONG = (
        f"{E.ERROR} <b>Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.</b>\n\n"
        f'{E.USERS} <a href="{SUPPORT_LINK}">Cᴏɴᴛᴀᴄᴛ Sᴜᴘᴘᴏʀᴛ</a>'
    )
    INVALID_TOKEN = f"{E.ERROR} <b>Exᴘɪʀᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ!</b>"
    VERIFIED_TEXT = (
        f"{E.WELCOME} <b>Hᴇʏ {{}}</b>\n\n"
        f"{E.CONFIRM} <b>Yᴏᴜ ᴀʀᴇ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴠᴇʀɪꜰɪᴇᴅ!</b>"
    )
