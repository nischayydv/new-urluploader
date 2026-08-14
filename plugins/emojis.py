# ⚠️ Credit: Developed by @NY_BOTS | Support: @NY_BOTS_SUPPORT | Channel: @NY_BOTS
"""Premium (custom) emoji registry.

Telegram premium emoji are rendered with the HTML entity:

    <emoji id="DOCUMENT_ID">FALLBACK</emoji>

`DOCUMENT_ID` is the custom emoji document id, `FALLBACK` is the plain unicode
emoji shown to clients that cannot render the premium one (and inside inline
buttons, which never support custom emoji).

Usage:
    from plugins.emojis import E, e

    text = f"{E.WELCOME} Hello!"          # premium, for message text/captions
    label = f"{e('ROCKET')} UPLOAD"       # never use E.* inside buttons
"""

# ---------------------------------------------------------------------------
# id -> plain unicode fallback
# ---------------------------------------------------------------------------
EMOJI_IDS: dict[str, str] = {
    "VOTE": "5267095979097610740",
    "JOIN": "6237668294896131350",
    "CANCEL": "6240245571626475799",
    "MAIN_MENU": "6240245571626475799",
    "BACK": "6217402478825049695",
    "CREATE": "5208891329626521299",
    "CONNECT": "5244710862953941180",
    "MANAGE": "6237621548472081271",
    "ADD_VOTES": "6240003971126139705",
    "REMOVE_VOTES": "6240003971126139705",
    "LEADERBOARD": "6240027791014765668",
    "END_GIVEAWAY": "6240085923397114865",
    "ADMIN": "6237595159329113605",
    "BROADCAST": "6237668294896131350",
    "STATS": "6239790794719370356",
    "SETTINGS": "6237621548472081271",
    "USERS": "6237867138997034625",
    "BACKUP": "6237900592497302202",
    "CLEAR": "6240152061598504832",
    "CHANNEL": "6237510794150419802",
    "NOTIFICATION": "6240073270423462835",
    "CONFIRM": "6239815031219820750",
    "REFRESH": "6240085923397114865",
    "WELCOME": "6332080283176672910",
    "FIRE": "6334449730734529256",
    "ARROW": "6332591195306334733",
    "CHART": "6332186798365612896",
    "HEART": "6237558987978447573",
    "ROCKET": "5188481279963715781",
    "CROWN": "6332246180583447893",
    "ERROR": "6334723470475139278",
    "ENDED": "6237572882197650867",
    "STAR": "6239815031219820750",
    "ID": "6237547619200014867",
    "GIFT": "6239894475229895983",
    "WINE": "6237510794150419802",
    "SMILE": "6237867138997034625",
    "LOVE": "6334437167955188087",
    "LIGHTNING": "6240073270423462835",
    "POINTER": "6237732706520668707",
    "ALERT": "6240152061598504832",
    "CLOWN": "6237900592497302202",
    "SEARCH": "6239790794719370356",
    "SPEAKER": "5217968773071401144",
    "LINK": "5289511602393984968",
    "CONFETTI": "6240085923397114865",
    "LOCATION": "6240101054566897479",
    "RIGHT": "6240295371772271503",
    "DIAMOND": "6240003971126139705",
    "CALENDAR": "6240027791014765668",
    "WINNER": "6332435498446888848",
    "MONEY_BAG": "6332246180583447893",
    "CELEBRATE": "6237621707385871360",
    "INBOX": "6237973405077871246",
    "LOCK": "6332490478323243268",
    "SHIELD": "6237595159329113605",
}

FALLBACKS: dict[str, str] = {
    "VOTE": "🗳",
    "JOIN": "📢",
    "CANCEL": "✖️",
    "MAIN_MENU": "🏠",
    "BACK": "🔙",
    "CREATE": "➕",
    "CONNECT": "🔗",
    "MANAGE": "🛠",
    "ADD_VOTES": "💎",
    "REMOVE_VOTES": "💎",
    "LEADERBOARD": "📅",
    "END_GIVEAWAY": "🎉",
    "ADMIN": "🛡",
    "BROADCAST": "📣",
    "STATS": "🔎",
    "SETTINGS": "⚙️",
    "USERS": "👤",
    "BACKUP": "💾",
    "CLEAR": "🧹",
    "CHANNEL": "🍷",
    "NOTIFICATION": "⚡️",
    "CONFIRM": "✅",
    "REFRESH": "🔄",
    "WELCOME": "👋",
    "FIRE": "🔥",
    "ARROW": "➡️",
    "CHART": "📊",
    "HEART": "❤️",
    "ROCKET": "🚀",
    "CROWN": "👑",
    "ERROR": "❌",
    "ENDED": "🚫",
    "STAR": "⭐️",
    "ID": "🆔",
    "GIFT": "🎁",
    "WINE": "🍷",
    "SMILE": "😊",
    "LOVE": "💖",
    "LIGHTNING": "⚡️",
    "POINTER": "👉",
    "ALERT": "🚨",
    "CLOWN": "🤡",
    "SEARCH": "🔍",
    "SPEAKER": "🔊",
    "LINK": "🔗",
    "CONFETTI": "🎊",
    "LOCATION": "📍",
    "RIGHT": "▶️",
    "DIAMOND": "💎",
    "CALENDAR": "🗓",
    "WINNER": "🏆",
    "MONEY_BAG": "💰",
    "CELEBRATE": "🥳",
    "INBOX": "📥",
    "LOCK": "🔒",
    "SHIELD": "🛡",
}


def e(name: str) -> str:
    """Plain unicode fallback — safe everywhere (buttons, alerts, logs)."""
    return FALLBACKS.get(name, "")


def premium(name: str) -> str:
    """Premium emoji HTML entity — for message text and captions only."""
    emoji_id = EMOJI_IDS.get(name)
    if not emoji_id:
        return e(name)
    return f'<emoji id="{emoji_id}">{e(name)}</emoji>'


class _PremiumEmoji:
    """Attribute access sugar: ``E.ROCKET`` -> premium emoji HTML."""

    def __getattr__(self, name: str) -> str:
        if name not in EMOJI_IDS:
            raise AttributeError(f"Unknown premium emoji: {name}")
        return premium(name)

    def __getitem__(self, name: str) -> str:
        return premium(name)


E = _PremiumEmoji()
