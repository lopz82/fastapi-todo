from typing import List, Optional

from sqlalchemy.orm import Session

import models
from utils import update_dict


class TaskRepository:
    def __init__(self):
        self._tasks = set()

    def add(self, task):
        self._tasks.add(task)


fake_set = set()


class FakeSession:
    def close(self):
        pass


class FakeTasksListRepository:
    def __init__(self, session):
        self.session = session
        self._repo = fake_set

    @property
    def next_id(self):
        return len(self._repo) + 1

    def add(self, tasks_list: models.TasksList) -> models.TasksList:
        tasks_list.id = self.next_id
        self._repo.add(tasks_list)
        return tasks_list

    def get(self, item_id: int) -> Optional[models.TasksList]:
        result = [tasks_list for tasks_list in self._repo if tasks_list.id == item_id]
        if not result:
            return None
        return result[0]

    def get_all(self) -> List[models.TasksList]:
        return sorted(list(self._repo), key=lambda x: x.id)

    def update(self, item_id: int, data: dict) -> models.TasksList:
        item = self.get(item_id)
        self.delete(item_id)
        update_dict(item.__dict__, data)
        self._repo.add(item)
        return item

    def replace(self, item_id: int, replacement: models.TasksList) -> models.TasksList:
        return self.update(
            item_id, {"name": replacement.name, "description": replacement.description}
        )

    def delete(self, item_id: id) -> None:
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

    def get(self, item_id: int) -> Optional[models.TasksList]:
        return self.session.query(models.TasksList).get(item_id)

    def get_all(self) -> List[models.TasksList]:
        return self.session.query(models.TasksList).order_by(models.TasksList.id).all()

    def update(self, item_id: int, data: dict) -> models.TasksList:
        self.session.query(models.TasksList).filter(
            models.TasksList.id == item_id
        ).update(data, synchronize_session="fetch")
        self.session.commit()
        return self.get(item_id)

    def delete(self, item_id: int) -> None:
        self.session.query(models.TasksList).filter(
            models.TasksList.id == item_id
        ).delete(synchronize_session="fetch")
        self.session.commit()


class SQLUserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: models.User) -> models.User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get(self, item_id: int) -> models.User:
        return self.session.query(models.User).get(item_id)

    def get_all(self) -> List[models.User]:
        return self.session.query(models.User).order_by(models.User.id).all()

    def update(self, item_id: int, data: dict) -> models.User:
        self.session.query(models.User).filter(models.User.id == item_id).update(
            data, synchronize_session="fetch"
        )
        self.session.commit()
        return self.get(item_id)

    def delete(self, item_id: int) -> None:
        self.session.query(models.User).filter(models.User.id == item_id).delete(
            synchronize_session="fetch"
        )
        self.session.commit()
