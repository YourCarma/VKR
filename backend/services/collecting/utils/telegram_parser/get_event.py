from pyrogram import Client, idle
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait
from pyrogram import filters
from loguru import logger


from services.collecting.utils.text_processing import TextProcessor

channel_ids = [-1001730870551, 'test_chatVKR', 'warhistoryalconafter', 'voenacher']  # Примеры ID каналов, замените их на свои


async def listen_event(chanels_list, websocket, session, news, insert_row):
    app = Client("VKR")
    
    async def message_handler(client, message):
        message_info = {}
        if message.text:
            text_to_process = message.text
        else:
            text_to_process = message.caption
        message_info["text"] = text_to_process
        text_processor = TextProcessor(text_to_process)
        message_info["source_id"] = message.chat.id
        message_info["date"] = message.date
        message_info["named_entities"] = text_processor.getNER()
        message_info["class"] = 'Тестовый'
        logger.debug(message_info)
        await insert_row(message_info, news, session)
        logger.success('Сообщение в БД загружено!')
        message_info["chat_title"] = message.chat.title
        await websocket.send_text(f"{message_info}")
    
    logger.success("Клиент запущен!")
    app.add_handler(MessageHandler(message_handler, filters.chat(chanels_list) & ~filters.forwarded))
    await app.start()
    
    await idle()
    
    await app.stop()
    # Запускаем прослушивание сообщений
    logger.error('Клиент остановлен!')
    
  