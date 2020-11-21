from database import SessionLocal
from repository import SQLTasksListRepository
from type_hints import Repository


def get_repository() -> Repository:
    session = SessionLocal()
    try:
        yield SQLTasksListRepository(session)
    finally:
        session.close()
