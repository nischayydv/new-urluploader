# (c) @AbirHasan2005

import datetime
import motor.motor_asyncio
from plugins.config import Config


class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            apply_caption=True,
            upload_as_doc=False,
            thumbnail=None,
            caption=None,
            bot_updates=True,
            ytdl_filter="mp4",
            generate_ss=False,
            spoiler=False,
            no_forwards=False,
            filename_cleaner=False,
            metadata=None,
            generate_sample_video=False,
            streaming=True,
            caption_up=False,
            dump_channel=None,
            blocklist_words=[],
            auto_unzip=False,
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_apply_caption(self, id, apply_caption):
        await self.col.update_one({'id': id}, {'$set': {'apply_caption': apply_caption}})

    async def get_apply_caption(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('apply_caption', True)

    async def set_upload_as_doc(self, id, upload_as_doc):
        await self.col.update_one({'id': id}, {'$set': {'upload_as_doc': upload_as_doc}})

    async def get_upload_as_doc(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('upload_as_doc', False)

    async def set_thumbnail(self, id, thumbnail):
        await self.col.update_one({'id': id}, {'$set': {'thumbnail': thumbnail}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('thumbnail', None)

    async def set_caption(self, id, caption):
        await self.col.update_one({'id': id}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('caption', None)

    # ------------------------------------------------ generic settings store
    DEFAULTS = {
        "apply_caption": True,
        "upload_as_doc": False,
        "thumbnail": None,
        "caption": None,
        "bot_updates": True,
        "ytdl_filter": "mp4",
        "generate_ss": False,
        "spoiler": False,
        "no_forwards": False,
        "filename_cleaner": False,
        "metadata": None,
        "generate_sample_video": False,
        "streaming": True,
        "caption_up": False,
        "dump_channel": None,
        "blocklist_words": [],
        "auto_unzip": False,
    }

    async def get_setting(self, id, key):
        user = await self.col.find_one({'id': int(id)})
        if not user:
            await self.add_user(int(id))
            return self.DEFAULTS.get(key)
        return user.get(key, self.DEFAULTS.get(key))

    async def set_setting(self, id, key, value):
        await self.col.update_one({'id': int(id)}, {'$set': {key: value}}, upsert=True)

    async def toggle_setting(self, id, key):
        current = await self.get_setting(id, key)
        new_value = not bool(current)
        await self.set_setting(id, key, new_value)
        return new_value

    async def reset_settings(self, id):
        await self.col.update_one({'id': int(id)}, {'$set': dict(self.DEFAULTS)}, upsert=True)

    async def get_generate_ss(self, id):
        return await self.get_setting(id, 'generate_ss')

    async def set_generate_ss(self, id, value):
        await self.set_setting(id, 'generate_ss', value)

    async def get_generate_sample_video(self, id):
        return await self.get_setting(id, 'generate_sample_video')

    async def set_generate_sample_video(self, id, value):
        await self.set_setting(id, 'generate_sample_video', value)

    async def get_user_data(self, id) -> dict:
        user = await self.col.find_one({'id': int(id)})
        if not user:
            await self.add_user(int(id))
            user = await self.col.find_one({'id': int(id)})
        return user or None


db = Database(Config.DATABASE_URL, "UploadLinkToFileBot")
