import models
import repository


def test_repository_can_add_a_tasks_list(session):
    tasks_lists = models.TasksList(name="Test list", description="A simple test list")

    repo = repository.SQLTasksListRepository(session)
    added_item = repo.add(tasks_list=tasks_lists)

    assert added_item is not None
    rows = list(session.execute('SELECT name, description FROM "taskslists"'))
    assert rows == [("Test list", "A simple test list")]


def test_repository_can_read_a_tasks_list(session):
    session.execute(
        'INSERT INTO taskslists (name, description) VALUES ("Test list", "A simple test list")'
    )

    repo = repository.SQLTasksListRepository(session)
    item = repo.get(item_id=1)

    assert item.name == "Test list"
    assert item.description == "A simple test list"


def test_repository_can_update_a_tasks_list(session):
    session.execute(
        'INSERT INTO taskslists (name, description) VALUES ("Test List", "A simple test list")'
    )
    update = {"name": "Updated test list"}

    repo = repository.SQLTasksListRepository(session)
    updated_item = repo.update(item_id=1, data=update)

    assert updated_item is not None
    rows = list(session.execute('SELECT name, description FROM "taskslists"'))
    assert rows == [("Updated test list", "A simple test list")]


def test_repository_can_replace_a_tasks_list(session):
    session.execute(
        'INSERT INTO taskslists (name, description) VALUES ("Test List", "A simple test list")'
    )
    new_tasks_lists = models.TasksList(
        name="Replaced test list", description="A simple replaced test list"
    )

    repo = repository.SQLTasksListRepository(session)
    replaced_item = repo.replace(item_id=1, replacement=new_tasks_lists)

    assert replaced_item is not None
    rows = list(session.execute('SELECT name, description FROM "taskslists"'))
    assert rows == [("Replaced test list", "A simple replaced test list")]
