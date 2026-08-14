"""Helpers that apply the user's settings to real uploads."""

import asyncio
import logging
import os
import re

from plugins.database.database import db
from plugins.emojis import E

logger = logging.getLogger(__name__)

JUNK_PATTERNS = [
    r"www\.[^\s]+\.[a-z]{2,4}",
    r"@[\w_]+",
    r"\[[^\]]*\]",
    r"\{[^\}]*\}",
    r"[_\.]+",
]


def clean_filename(file_name: str) -> str:
    """Remove junk (site names, usernames, brackets) from a file name."""
    if not file_name:
        return file_name
    name, ext = os.path.splitext(file_name)
    for pattern in JUNK_PATTERNS:
        name = re.sub(pattern, " ", name, flags=re.IGNORECASE)
    name = re.sub(r"\s{2,}", " ", name).strip(" -_")
    return f"{name or 'file'}{ext}"


async def maybe_clean_filename(user_id: int, file_name: str) -> str:
    if await db.get_setting(user_id, "filename_cleaner"):
        return clean_filename(file_name)
    return file_name


async def build_caption(user_id: int, file_name: str, file_size: str = "", duration: str = "") -> str:
    """Build the final caption using the user's custom caption template."""
    template = await db.get_setting(user_id, "caption")
    if not template:
        return f"<b>{file_name}</b>"
    try:
        return template.format(filename=file_name, filesize=file_size, duration=duration)
    except Exception:
        return template


async def upload_flags(user_id: int) -> dict:
    """Common upload keyword arguments derived from settings."""
    return {
        "streaming": bool(await db.get_setting(user_id, "streaming")),
        "spoiler": bool(await db.get_setting(user_id, "spoiler")),
        "protect": bool(await db.get_setting(user_id, "no_forwards")),
        "caption_up": bool(await db.get_setting(user_id, "caption_up")),
    }


async def is_blocked(user_id: int, text: str):
    """Return the matched blocklist word, if the text contains one."""
    words = await db.get_setting(user_id, "blocklist_words") or []
    lowered = (text or "").lower()
    for word in words:
        if word and word in lowered:
            return word
    return None


async def _run(cmd: list) -> bool:
    try:
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL,
        )
        await process.communicate()
        return process.returncode == 0
    except Exception as err:
        logger.error(f"ffmpeg failed: {err}")
        return False


async def generate_screenshots(file_path: str, out_dir: str, count: int = 5) -> list:
    """Grab evenly spaced screenshots from a video."""
    os.makedirs(out_dir, exist_ok=True)
    shots = []
    for index in range(1, count + 1):
        out_file = os.path.join(out_dir, f"ss_{index}.jpg")
        ok = await _run([
            "ffmpeg", "-y", "-ss", str(index * 30), "-i", file_path,
            "-vframes", "1", "-q:v", "3", out_file,
        ])
        if ok and os.path.exists(out_file) and os.path.getsize(out_file) > 0:
            shots.append(out_file)
    return shots


async def generate_sample(file_path: str, out_dir: str, seconds: int = 30):
    """Cut a short sample clip from a video."""
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "sample.mp4")
    ok = await _run([
        "ffmpeg", "-y", "-ss", "60", "-i", file_path, "-t", str(seconds),
        "-c", "copy", out_file,
    ])
    if ok and os.path.exists(out_file) and os.path.getsize(out_file) > 0:
        return out_file
    return None


async def apply_metadata(user_id: int, file_path: str):
    """Rewrite media metadata (title/author) when the user configured it."""
    tag = await db.get_setting(user_id, "metadata")
    if not tag or not os.path.exists(file_path):
        return file_path
    base, ext = os.path.splitext(file_path)
    out_file = f"{base}.meta{ext or '.mkv'}"
    ok = await _run([
        "ffmpeg", "-y", "-i", file_path, "-map", "0", "-c", "copy",
        "-metadata", f"title={tag}",
        "-metadata", f"author={tag}",
        "-metadata", f"artist={tag}",
        "-metadata", f"comment={tag}",
        out_file,
    ])
    if ok and os.path.exists(out_file) and os.path.getsize(out_file) > 0:
        try:
            os.remove(file_path)
        except Exception:
            pass
        return out_file
    return file_path


async def extract_archive(file_path: str, out_dir: str) -> list:
    """Auto-unzip an archive and return the extracted file paths."""
    lowered = file_path.lower()
    os.makedirs(out_dir, exist_ok=True)
    try:
        if lowered.endswith(".zip"):
            import zipfile
            with zipfile.ZipFile(file_path) as archive:
                archive.extractall(out_dir)
        elif lowered.endswith((".tar", ".tar.gz", ".tgz", ".tar.bz2")):
            import tarfile
            with tarfile.open(file_path) as archive:
                archive.extractall(out_dir)
        else:
            return []
    except Exception as err:
        logger.error(f"unzip failed: {err}")
        return []

    files = []
    for root, _dirs, names in os.walk(out_dir):
        for name in names:
            files.append(os.path.join(root, name))
    return files


async def send_to_dump(bot, user_id: int, message):
    """Copy a finished upload to the user's dump channel."""
    dump = await db.get_setting(user_id, "dump_channel")
    if not dump or message is None:
        return
    try:
        await message.copy(int(dump))
    except Exception as err:
        logger.error(f"dump copy failed: {err}")
        try:
            await bot.send_message(
                user_id,
                f"{E.ALERT} <b>Cᴏᴜʟᴅ ɴᴏᴛ ᴄᴏᴘʏ ᴛᴏ ʏᴏᴜʀ ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ.</b>\n\n<code>{err}</code>",
            )
        except Exception:
            pass
