from pyrogram import Client, idle
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait
from pyrogram import filters
from loguru import logger
import logging

channel_ids = [-1001730870551, 'test_chatVKR', 'warhistoryalconafter', 'voenacher']  # Примеры ID каналов, замените их на свои


async def listen_event(chanels_list, websocket):
    app = Client("VKR")
    async def message_handler(client, message):
        logger.debug(message)
        await websocket.send_text(f"{message}")
    
    logger.success("Клиент запущен!")
    app.add_handler(MessageHandler(message_handler, filters.chat(chanels_list) & ~filters.forwarded))
    await app.start()
    
    await idle()
    
    await app.stop()
    # Запускаем прослушивание сообщений
    logger.error('Клиент остановлен!')
    
  