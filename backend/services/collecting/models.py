from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, ARRAY, UUID, Text

from datetime import datetime
metadata = MetaData()


sources = Table(
    "sources",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("tg_id", String, nullable=False),
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
    Column("id", Integer, primary_key=True),
    Column("source_id", Integer, ForeignKey("sources.tg_id")),
    Column("text", Text, nullable=False),
    Column("date", TIMESTAMP, nullable=False),
    Column("locations", ARRAY(String), nullable=True),
)

processed_news = Table(
    "processed_news",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("news_id", UUID, ForeignKey("news.id")),
    Column("class", Integer, nullable=True),
    Column("locations", ARRAY(String), nullable=True),
    Column("persons", ARRAY(String), nullable=True),
    Column("organisations", ARRAY(String), nullable=True),
    Column("location_coordinates", ARRAY(String), nullable=True),

)