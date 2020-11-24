from typing import List

import crypto
import models
import schemas
from decorators import schema_model_mapping
from type_hints import Repository, Model, Schemas
from utils import clean_empty_keys


class UserNotFound(Exception):
    pass


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
    return repo.update(item_id, clean_empty_keys(data))


def replace_tasks_list(
    repo: Repository, item_id: int, replacement: schemas.TasksListCreate
) -> models.TasksList:
    return repo.update(item_id, replacement.dict())


def delete_tasks_list(repo: Repository, item_id: int) -> None:
    repo.delete(item_id)


def create_user(repo: Repository, user: schemas.UserCreate) -> models.User:
    user.password = crypto.hash_password(user.password)
    user_model = convert_to_model(user)
    return repo.add(user_model)


def get_user(repo: Repository, user_id: int) -> models.User:
    user = repo.get(user_id)
    if not user:
        raise UserNotFound()
    return user


def get_all_users(repo: Repository) -> List[models.User]:
    return repo.get_all()


def update_user(repo: Repository, item_id: int, data: dict) -> models.User:
    sanitized = clean_empty_keys(data)
    if "password" in sanitized:
        data["password"] = crypto.hash_password(data["password"])
    return repo.update(item_id, sanitized)


def delete_user(repo: Repository, item_id: int) -> None:
    get_user(repo, item_id)
    repo.delete(item_id)
