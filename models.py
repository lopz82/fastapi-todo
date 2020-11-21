from sqlalchemy import Column, Integer, String

from database import Base


class TasksList(Base):
    __tablename__ = "taskslists"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    description = Column(String(100))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    password = Column(String(30), nullable=False)
