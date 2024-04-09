from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, BigInteger, Text, JSON
from sqlalchemy.dialects.postgresql import JSONB

from datetime import datetime
metadata = MetaData()


sources = Table(
    "sources",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("tg_id", BigInteger, nullable=False, unique=True),
    Column("url", String, nullable=False),
    Column("title", String, nullable=False),
    Column("chatname", String, nullable=False),
    Column("description", Text),
    Column('photo_profile_path', String, nullable=True),
    Column('members_count', Integer, nullable=True),
    Column("politic_view", String, nullable=False)
    
)

news = Table(
    "news",
    metadata,
    Column("id", Integer, primary_key=True,  autoincrement=True),
    Column("source_id", BigInteger, ForeignKey("sources.tg_id")),
    Column("text", Text, nullable=False),
    Column("date", TIMESTAMP, nullable=False),
    Column("named_entities", JSONB),
    Column("class", String),
    
)