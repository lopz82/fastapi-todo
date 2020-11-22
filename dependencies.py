import os

from database import SessionLocal
from repository import SQLTasksListRepository, FakeTasksListRepository, FakeSession
from type_hints import Repository


def get_repository() -> Repository:
    if os.getenv("FASTAPI_ENV", "TEST") == "TEST":
        session = FakeSession()
        repo = FakeTasksListRepository(session)
    else:
        session = SessionLocal()
        repo = SQLTasksListRepository(session)
    try:
        yield repo
    finally:
        session.close()
