from pathlib import Path
from pyrogram import Client
from loguru import logger


app = Client("VKR")
async def getChatInfo(chaturl):
    chat_info = {}
    async with app:
        await app.start()
        chatname = chaturl[13:]
        chat = await app.get_chat(chatname)
        chat_member_count = await app.get_chat_members_count(chatname)
        chat_id = chat.id
        chat_title = chat.title
        chat_description = chat.description
        await app.download_media(message=chat.photo.big_file_id, file_name=f"{chatname}_profile_photo.jpg")
        await app.stop()
        profile_photo_path = Path().joinpath("downloads").joinpath(f"{chatname}_profile_photo.jpg")
        logger.debug(chat)
        logger.debug(f"ID чата: {chat_id}")
        logger.debug(f"Никнейм чата: {chatname}")
        logger.debug(f"Название чата: {chat_title}")
        logger.debug(f"Подписчиков чата: {chat_member_count} чел.")
        logger.debug(f"Описание чата: {chat_description}")
        logger.debug(f"Путь к фото чата: {profile_photo_path}")
        
    chat_info["tg_id"] = chat_id
    chat_info["url"] = chat_url
    chat_info["title"] = chat_title
    chat_info["chatname"] = chatname
    chat_info["description"] = chat_description
    chat_info["photo_profile_path"] = profile_photo_path
    logger.error(chat_info)
    return chat_info

chat_url = "https://t.me/readovkanews"
info = getChatInfo(chat_url)
print(info)