from pyrogram import Client, idle
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait
from pyrogram import filters
from loguru import logger

channel_ids = [-1001730870551, 'test_chatVKR', 'warhistoryalconafter', 'voenacher']  # Примеры ID каналов, замените их на свои



async def listen_event(chanels_list, websocket):
    
    async def message_handler(client, message):
        logger.debug(message)
        await websocket.send_text(f"{message}")
        
    app = Client("VKR")
    await app.start()
    logger.success("Клиент запущен!")
    app.add_handler(MessageHandler(message_handler, filters.chat(chanels_list) & ~filters.forwarded))
    # Запускаем прослушивание сообщений
    await idle()
    await app.stop()
    logger.error('Клиент остановлен!')
        
  