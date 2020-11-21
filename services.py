from typing import List

import models
import schemas
from decorators import schema_model_mapping
from type_hints import Repository, Model, Schemas


def convert_to_model(schema: Schemas) -> Model:
    args = schema.dict()
    class_ = schema_model_mapping[schema.__class__]
    return class_(**args)


def create_tasks_list(
    repo: Repository, tasks_list: schemas.TasksListCreate
) -> models.TasksList:
    task_list_model = convert_to_model(tasks_list)
    return repo.add(task_list_model)


def get_tasks_list(repo: Repository, item_id: int) -> models.TasksList:
    return repo.get(item_id)


def get_all_tasks_lists(repo: Repository) -> List[models.TasksList]:
    return repo.get_all()


def update_tasks_list(repo: Repository, item_id: int, data: dict) -> models.TasksList:
    return repo.update(item_id, data)


def replace_tasks_list(
    repo: Repository, item_id: int, replacement: models.TasksList
) -> models.TasksList:
    return repo.replace(item_id, replacement)


def delete_tasks_list(repo: Repository, item_id: int) -> None:
    repo.delete(item_id)
