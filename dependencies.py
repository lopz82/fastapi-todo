from database import SessionLocal
from repository import (
    SQLTasksListRepository,
    FakeTasksListRepository,
    FakeSession,
    SQLUserRepository,
)
from type_hints import Repository


def get_repository() -> Repository:
    try:
        session = SessionLocal()
        repo = SQLTasksListRepository(session)
        yield repo
    finally:
        session.close()


def get_users_repository() -> Repository:
    try:
        session = SessionLocal()
        repo = SQLUserRepository(session)
        yield repo
    finally:
        session.close()


def get_test_repository() -> Repository:
    try:
        session = FakeSession()
        repo = FakeTasksListRepository(session)
        yield repo
    finally:
        session.close()
