from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

import models
from decorators import bound


class TaskBase(BaseModel):
    name: str
    description: str
    due: Optional[datetime]
    created: datetime = datetime.now()


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    tasklist_id: int
    owner_id: int


class TasksListBase(BaseModel):
    name: str
    description: str


class TasksListPatch(TasksListBase):
    name: Optional[str]
    description: Optional[str]
    tasks: Optional[List[Task]]


@bound(model=models.TasksList)
class TasksListCreate(TasksListBase):
    pass


@bound(model=models.TasksList)
class TasksList(TasksListBase):
    id: int
    tasks: List[Task]

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str


@bound(model=models.User)
class UserCreate(UserBase):
    password: str


@bound(model=models.User)
class User(UserBase):
    id: int
    tasks_lists: List[TasksList]

    class Config:
        orm_mode = True


class UserSecret(User):
    password: str


class UserPatch(UserBase):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
