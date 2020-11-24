from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False, unique=True)
    email = Column(String(20), nullable=False, unique=True)
    password = Column(String(60), nullable=False)

    tasks_lists = relationship("TasksList", back_populates="owner")


class TasksList(Base):
    __tablename__ = "taskslists"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    description = Column(String(100))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks_lists")
    tasks = relationship("Task", back_populates="list_owner")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    description = Column(String(100))
    list_id = Column(Integer, ForeignKey("taskslists.id"))

    list_owner = relationship("TasksList", back_populates="tasks")
