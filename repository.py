from typing import List

from sqlalchemy.orm import Session

import models


class TaskRepository:
    def __init__(self):
        self._tasks = set()

    def add(self, task):
        self._tasks.add(task)


class FakeTasksListRepository:
    def __init__(self):
        self._repo = set()

    @property
    def next_id(self):
        return len(self._repo)

    def add(self, tasks_list: models.TasksList) -> models.TasksList:
        tasks_list.id = self.next_id
        self._repo.add(tasks_list)
        return tasks_list

    def get(self, item_id: int) -> models.TasksList:
        [result] = [tasks_list for tasks_list in self._repo if tasks_list.id == item_id]
        return result

    def update(self, item_id: int, data: dict) -> models.TasksList:
        item = self.get(item_id)
        self.delete(item_id)
        item.__dict__.update(data)
        self._repo.add(item)
        return item

    def delete(self, item_id: id):
        [item] = [tasks_list for tasks_list in self._repo if tasks_list.id == item_id]
        self._repo.remove(item)


class SQLTasksListRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, tasks_list: models.TasksList) -> models.TasksList:
        self.session.add(tasks_list)
        self.session.commit()
        self.session.refresh(tasks_list)
        return tasks_list

    def get(self, item_id: int) -> models.TasksList:
        return self.session.query(models.TasksList).get(item_id)

    def get_all(self) -> List[models.TasksList]:
        return self.session.query(models.TasksList).all()

    def update(self, item_id: int, data: dict) -> models.TasksList:
        self.session.query(models.TasksList).filter(
            models.TasksList.id == item_id
        ).update(data, synchronize_session="fetch")
        self.session.commit()
        return self.get(item_id)

    def replace(self, item_id: int, replacement: models.TasksList) -> models.TasksList:
        updated = self.update(
            item_id, {"name": replacement.name, "description": replacement.description}
        )
        self.session.commit()
        return updated

    def delete(self, item_id: int):
        self.session.query(models.TasksList).filter(
            models.TasksList.id == item_id
        ).delete(synchronize_session="fetch")
        self.session.commit()
