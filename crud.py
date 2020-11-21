from pydantic import BaseModel
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Session

import models
import schemas
from decorators import schema_model_mapping


def convert_to_model(schema: BaseModel) -> DeclarativeMeta:
    args = schema.dict()
    class_ = schema_model_mapping[schema.__class__]
    return class_(**args)


def create_taskslist(db: Session, taskslist: schemas.TasksListCreate):
    db_taskslist = convert_to_model(taskslist)
    db.add(db_taskslist)
    db.commit()
    db.refresh(db_taskslist)
    return db_taskslist


def get_taskslist(db: Session, id: int):
    return db.query(models.TasksList).get(id)
