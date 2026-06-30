import os

from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine


metadata = MetaData()

students = Table(
    "lesson9_students",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("email", String(150), nullable=False, unique=True),
)


def get_engine():
    database_url = os.getenv("DATABASE_URL")

    if database_url is None:
        raise RuntimeError("Set DATABASE_URL environment variable")

    return create_engine(database_url)


def create_tables(engine):
    metadata.create_all(engine)
