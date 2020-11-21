from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

import models
from decorators import bound


class TaskBase(BaseModel):
    name: str
    description: str
    due: datetime
    created: datetime


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    tasklist_id: int
    owner_id: int


class TasksListBase(BaseModel):
    name: str
    description: str
    # tasks: List[Task]


class TasksListPatch(TasksListBase):
    name: Optional[str]
    description: Optional[str]


@bound(model=models.TasksList)
class TasksListCreate(TasksListBase):
    pass


@bound(model=models.TasksList)
class TasksList(TasksListBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str
    retype_password: str


class User(UserBase):
    id: int
    password: str
    salt: str
    lists: List[TasksList] = []

    class Config:
        orm_mode = True
