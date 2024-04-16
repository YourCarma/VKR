from pyrogram import Client, idle
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait
from pyrogram import filters
from loguru import logger
from pathlib import Path

from services.collecting.utils.text_processing import TextProcessor
from services.collecting.utils.tag_predict_onnx import RuBERTONNX

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
        current_dir = Path.cwd()
        logger.warning(str(current_dir / 'rubert2-tiny_onnx' / 'model.onnx'))
        predictor = RuBERTONNX(str(current_dir / 'rubert2-tiny_onnx' / 'model.onnx'), str(current_dir / 'rubert2-tiny_onnx'), 300) 
        message_info["source_id"] = message.chat.id
        message_info["date"] = message.date
        message_info["named_entities"] = text_processor.getNER()
        message_info["class"] = predictor.predict(text_to_process)
        logger.debug(message_info)
        await insert_row(message_info, news, session)
        logger.success('Сообщение в БД загружено!')
        message_info["title"] = message.chat.title
        message_info["date"] = message.date.isoformat()
        logger.warning(message_info)
        await websocket.send_text(str(message_info).replace("\'", "\""))
    
    logger.success("Клиент запущен!")
    app.add_handler(MessageHandler(message_handler, filters.chat(chanels_list) & ~filters.forwarded))
    await app.start()
    
    await idle()
    
    await app.stop()
    # Запускаем прослушивание сообщений
    logger.error('Клиент остановлен!')
    
  