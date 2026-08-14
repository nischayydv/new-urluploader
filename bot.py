# ⚠️ Credit: Developed by @NY_BOTS | Support: @NY_BOTS_SUPPORT | Channel: @NY_BOTS
"""Entry point: tiny Flask keep-alive server + Pyrogram (PyroBlack) client."""

import logging
import os
import threading

from flask import Flask
from pyrogram import Client

from plugins.config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger("uploader")

web = Flask(__name__)


@web.route("/")
def home() -> str:
    return "✅ Bot is running and Flask is alive!"


def run_web() -> None:
    """Expose a port so hosts like Render/Koyeb keep the service awake."""
    web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


def build_client() -> Client:
    return Client(
        "@UploaderXNTBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        upload_boost=True,  # PyroBlack only
        sleep_threshold=300,
        plugins=dict(root="plugins"),
    )


def main() -> None:
    threading.Thread(target=run_web, daemon=True).start()

    os.makedirs(Config.DOWNLOAD_LOCATION, exist_ok=True)

    logger.info("🎊 I AM ALIVE 🎊  • Support @NY_BOTS_SUPPORT")
    build_client().run()


if __name__ == "__main__":
    main()
