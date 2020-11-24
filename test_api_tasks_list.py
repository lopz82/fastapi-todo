from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_api_post_tasks_list():
    resp = client.post("/taskslists", json={"name": "Test", "description": "Test list"})

    assert resp.status_code == 201
    assert resp.json() == {
        "id": 1,
        "name": "Test",
        "description": "Test list",
        "tasks": [],
    }


def test_api_get_tasks_list():
    resp = client.get("/taskslists/1")

    assert resp.status_code == 200
    assert resp.json() == {
        "id": 1,
        "name": "Test",
        "description": "Test list",
        "tasks": [],
    }


def test_api_get_all_tasks_list():
    resp = client.post(
        "/taskslists", json={"name": "Test2", "description": "Test list 2"}
    )

    assert resp.status_code == 201

    resp = client.get("/taskslists/")
    assert resp.status_code == 200
    assert resp.json() == [
        {"id": 1, "name": "Test", "description": "Test list", "tasks": []},
        {"id": 2, "name": "Test2", "description": "Test list 2", "tasks": []},
    ]


def test_api_patch_tasks_list():
    resp = client.patch("/taskslists/1", json={"name": "Patched Test"})

    assert resp.status_code == 200
    assert resp.json() == {
        "id": 1,
        "name": "Patched Test",
        "description": "Test list",
        "tasks": [],
    }


def test_api_put_tasks_list():
    resp = client.put(
        "/taskslists/2", json={"name": "Replaced Test", "description": "I used PUT"}
    )

    assert resp.status_code == 200
    assert resp.json() == {
        "id": 2,
        "name": "Replaced Test",
        "description": "I used PUT",
        "tasks": [],
    }


def test_api_delete_tasks_list():
    _ = client.delete("/taskslists/1")
    resp = client.delete("/taskslists/2")

    assert resp.status_code == 200

    resp = client.get("/taskslists/1")

    assert resp.status_code == 404
