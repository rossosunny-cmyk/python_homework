from uuid import uuid4

import pytest
from sqlalchemy import select

from db_client import create_tables, get_engine, students


def get_unique_email():
    return f"student_{uuid4().hex}@example.com"


@pytest.fixture()
def engine():
    db_engine = get_engine()
    create_tables(db_engine)
    return db_engine


@pytest.fixture()
def cleanup_students(engine):
    pass
    emails = []

    yield emails

    with engine.begin() as connection:
        for email in emails:
            delete_query = students.delete().where(students.c.email == email)
            connection.execute(delete_query)


def test_add_student(engine, cleanup_students):
    email = get_unique_email()
    cleanup_students.append(email)

    with engine.begin() as connection:
        insert_query = students.insert().values(
            name="Алеся",
            email=email,
        )
        connection.execute(insert_query)

        select_query = select(students).where(students.c.email == email)
        student = connection.execute(select_query).mappings().one()

    assert student["name"] == "Алеся"
    assert student["email"] == email


def test_update_student(engine, cleanup_students):
    email = get_unique_email()
    cleanup_students.append(email)

    with engine.begin() as connection:
        insert_query = students.insert().values(
            name="Алеся",
            email=email,
        )
        connection.execute(insert_query)

        update_query = (
            students.update()
            .where(students.c.email == email)
            .values(name="Алеся Ломакина")
        )
        connection.execute(update_query)

        select_query = select(students).where(students.c.email == email)
        student = connection.execute(select_query).mappings().one()

    assert student["name"] == "Алеся Ломакина"
    assert student["email"] == email


def test_delete_student(engine):
    email = get_unique_email()

    with engine.begin() as connection:
        insert_query = students.insert().values(
            name="Алеся",
            email=email,
        )
        connection.execute(insert_query)

        delete_query = students.delete().where(students.c.email == email)
        connection.execute(delete_query)

        select_query = select(students).where(students.c.email == email)
        student = connection.execute(select_query).mappings().first()

    assert student is None
