from pathlib import PurePath
from pyrogram import Client
from loguru import logger
import asyncio


async def getChatInfo(chaturl):
    app = Client("VKR")
    chat_info = {}
    app.start()
    async with app:
        chatname = chaturl[13:]
        chat = await app.get_chat(chatname)
        chat_member_count = await app.get_chat_members_count(chatname)
        chat_id = chat.id
        chat_title = chat.title
        chat_description = chat.description
        await app.download_media(message=chat.photo.big_file_id, file_name=f"{chatname}_profile_photo.jpg")
        app.stop()
        profile_photo_path = str(PurePath().joinpath(f"{chatname}_profile_photo.jpg"))
        logger.debug(chat)
        logger.debug(f"ID чата: {chat_id}")
        logger.debug(f"Никнейм чата: {chatname}")
        logger.debug(f"Название чата: {chat_title}")
        logger.debug(f"Подписчиков чата: {chat_member_count} чел.")
        logger.debug(f"Описание чата: {chat_description}")
        logger.debug(f"Путь к фото чата: {profile_photo_path}")
        
    chat_info["tg_id"] = str(chat_id)
    chat_info["url"] = chaturl
    chat_info["title"] = chat_title
    chat_info["chatname"] = chatname
    chat_info["members_count"] = chat_member_count
    chat_info["description"] = chat_description
    chat_info["photo_profile_path"] = profile_photo_path
    logger.error(chat_info)
    return chat_info

