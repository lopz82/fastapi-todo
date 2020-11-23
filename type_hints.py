from typing import Protocol, TypeVar, Union, List, Optional

import models
import schemas

Model = Union[models.TasksList]
Schemas = Union[schemas.TasksList, schemas.TasksListCreate]

T = TypeVar("T")


class Repository(Protocol[T]):
    def add(self, item: T) -> T:
        ...

    def get(self, item_id: int) -> Optional[T]:
        ...

    def get_all(self) -> List[T]:
        ...

    def update(self, item_id: int, data: dict) -> T:
        ...

    def replace(self, item_id: int, replacement: T) -> T:
        ...

    def delete(self, item_id: int) -> ModuleNotFoundError:
        ...
