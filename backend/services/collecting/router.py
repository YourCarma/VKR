from datetime import date
from pathlib import Path
import pyautogui
from loguru import logger
from fastapi import APIRouter,  HTTPException, Depends, Request, WebSocket, WebSocketDisconnect, BackgroundTasks
from websockets.exceptions import ConnectionClosed

from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import func
from database import get_async_session

from services.collecting.schemas import CreateSource
from services.collecting.models import sources, news
from services.collecting.utils.telegram_parser.get_chanel import getChatInfo
from services.collecting.utils.telegram_parser.get_event import listen_event



router = APIRouter(
    prefix="/collecting",
    tags=["Collecting"]
)


def rawDBdataToDict(query_result: tuple):
    """Преобразование результатов запроса SELECT в массив JSON'ов

    Args:
        query_result (tuple): Результат выполнения SQL-транзакции

    Returns:
        _List_: _description_
    """
    return [dict(data._mapping) for data in query_result]



async def select_byDate(table, 
                        fish_id: int, 
                        session):
    '''
    Выбор по дате
    '''
    stmt = (
            select(table.c.date)
            .where(table.c.fish_id == fish_id)
            .order_by(table.c.date.desc())
            .limit(1)
            )
    result = await session.execute(stmt)
    last_date = result.scalar_one_or_none()
    return last_date



async def insert_row(schema, 
                     model, 
                     session):
    '''
    Вставка строки по схеме Pydantic (schema) в указанную таблицу (model) БД
    '''
    
    stmt = model.insert().values(**schema)
    await session.execute(stmt)
    await session.commit()

# async def update_row(schema, 
#                      model, 
#                      session, 
#                      date):

#     last_amount_stmt = (
#                         select(model.c.amount)
#                         .where(model.c.fish_id == schema.fish_id)
#                         .where(fish_recieved.c.date == date)
#                         .limit(1)
#                         )
#     last_amount_result = await session.execute(last_amount_stmt)
#     last_amount = last_amount_result.scalar_one_or_none()
#     stmt =  (
#             update(model)
#             .where(model.c.fish_id == schema.fish_id)
#             .where(model.c.date == date)
#             .values(amount = last_amount+schema.amount)
#             )
#     await session.execute(stmt)
#     await session.commit()

# async def select_unit_using_byDate(table, 
#                                    fish_id: int, 
#                                    session):
#     stmt = (
#             select(table.c.unit_using)
#             .where(table.c.fish_id == fish_id)
#             .order_by(table.c.date.desc())
#             .limit(1)
#             )
#     result = await session.execute(stmt)
#     last_unit_using = result.scalar_one_or_none()
#     return last_unit_using

# async def select_volume_using_byDate(table, 
#                                      fish_id: int, 
#                                      session):
#     stmt = (
#             select(table.c.volume_using)
#             .where(table.c.fish_id == fish_id)
#             .order_by(table.c.date.desc())
#             .limit(1)
#             )
#     result = await session.execute(stmt)
#     last_volume_using = result.scalar_one_or_none()
#     return last_volume_using

# async def select_all_table(model, session):
#     '''
#     Получение всей таблицы из БД (model).
#     '''
#     query = (
#             select(model)
#             .select_from(model)
#             )
#     result = await session.execute(query)
#     return result

# async def delete_row_byID(model, 
#                           target_id, 
#                           session):
#     '''
#     Удаление строки из таблицы БД (model) по указанному ID (target_id)
#     '''
#     stmt = (
#             delete(model)
#             .where(model.c.id == target_id)
#             )
#     await session.execute(stmt)
#     await session.commit()

# async def  delete_company_byID(target_id, 
#                                session):
#     '''
#     Удаление компании из таблицы companies в БД. Приводит к удалению всех строк с данной компанией из дочерних таблиц (fish_recieved, fishes).
#     '''
#     stmts = [
#                 (
#                 delete(fish_recieved)
#                 .where(fishes.c.company_id == target_id)
#                 .where(fish_recieved.c.fish_id == fishes.c.id)
#                 ),
#                 (
#                 delete(pivot_table)
#                 .where(fishes.c.company_id == target_id)
#                 .where(pivot_table.c.fish_id == fishes.c.id)
#                 ),
#                 (
#                 delete(fishes)
#                 .where(fishes.c.company_id == target_id)
#                 ),
#                 (
#                 delete(companies)
#                 .where(companies.c.id == target_id)
#                 )
#             ]
#     for stmt in stmts:
#         await session.execute(stmt)
#     await session.commit()

# async def delete_fish_byID(target_id, session):
#     '''
#      Удаление FISH-зонда из таблицы fishes в БД. Приводит к удалению всех строк с данной компанией из дочерних таблиц (fish_recieved).
#     '''
#     stmts = [
#                 (
#                 delete(fish_recieved)
#                 .where(fish_recieved.c.fish_id == target_id)
#                 ),
#                 (
#                 delete(pivot_table)
#                 .where(pivot_table.c.fish_id == fishes.c.id)
#                 ),
#                 (
#                 delete(fishes)
#                 .where(fishes.c.id == target_id)
#                 )
#             ]
#     for stmt in stmts:
#         await session.execute(stmt)
#     await session.commit()

# async def delete_recieve_byID(target_id, session):
#     '''
#      Удаление поступления из таблицы fish_recieved в БД.
#     '''
#     stmt = (
#             delete(fish_recieved)
#             .where(fish_recieved.c.id == target_id)
#             ),
#     await session.execute(stmt)
#     await session.commit()




@router.get("/get_sources")
async def get_allfishes(session: AsyncSession = Depends(get_async_session)):
    stmt = (
            select(sources)
            )
    result = await session.execute(stmt)
    rawData = rawDBdataToDict(result)
    elefants = []
    rats = []
    for src in rawData:
        src["photo_profile_path"] =  src["photo_profile_path"]
        if src["politic_view"] == "Пророссийский":
            elefants.append(src)
        else:
            rats.append(src)
    return {"elefants": elefants, "rats": rats}

@router.post("/add_source")
async def add_fish(new_source: CreateSource, 
                   session: AsyncSession = Depends(get_async_session)):
    result = await getChatInfo(new_source.url)
    result["politic_view"] = new_source.politic_view
    await insert_row(result, sources, session)
    return {"status": f"Новый источник: {new_source.url} успешно добавлен!"}


import threading
import time
import logging

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, session: AsyncSession = Depends(get_async_session)):
    logger.debug("Запрос списка источников из БД...")
    stmt = (
            select(sources)
            )
    
    await websocket.accept()
    try:
        while True:
            status = await websocket.receive_text()
            if status == "True":
                result = await session.execute(stmt)
                rawData = rawDBdataToDict(result)
                chat_list = [x["tg_id"] for x in rawData]
                logger.success(f"Список источников загружен! {chat_list}")
                await listen_event(chat_list, websocket, session, news, insert_row)
                
            else:
                pyautogui.hotkey('CTRL', 'C')
    except (WebSocketDisconnect, ConnectionClosed):
        # Клиент отключился
        logger.debug("Client disconnected")
        
@router.get("/get_news")
async def get_news(session: AsyncSession = Depends(get_async_session)):
    stmt = (
            select(sources.c.title, news).join(news).order_by(news.c.date.desc())
            )
    result = await session.execute(stmt)
    rawData = rawDBdataToDict(result)
    return rawData
# @router.delete("/delete_sourcse/{fish_id}")
# async def delete_fish(fish_id: int, session: AsyncSession = Depends(get_async_session)):
#     await delete_fish_byID(fish_id, session)
#     return {"status": "FISH-зонд успешно удален!"}

