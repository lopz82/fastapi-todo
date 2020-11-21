from sqlalchemy.orm import Session

import models


class TaskRepository:
    def __init__(self):
        self._tasks = set()

    def add(self, task):
        self._tasks.add(task)


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

    def update(self, item_id: int, data: dict) -> models.TasksList:
        updated = (
            self.session.query(models.TasksList)
            .filter(models.TasksList.id == item_id)
            .update(data, synchronize_session="fetch")
        )
        self.session.commit()
        return updated

    def replace(self, item_id: int, replacement: models.TasksList) -> models.TasksList:
        return self.update(
            item_id, {"name": replacement.name, "description": replacement.description}
        )
