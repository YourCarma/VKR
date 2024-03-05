from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, ARRAY, UUID

from datetime import datetime
metadata = MetaData()




sources_location = Table(
    "sources_location",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
)

sources_category = Table(
    "sources_category",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
)

sources = Table(
    "sources",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("url", String, nullable=False),
    Column("info", String),
    Column('avatar_path', String, nullable=True)
)

news = Table(
    "news",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("source_id", Integer, ForeignKey("sources.id")),
    Column("text", String, nullable=False),
    Column("url", String, nullable=False),
    Column("date", TIMESTAMP, nullable=False),
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