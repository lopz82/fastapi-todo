from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_api_create_user():
    resp = client.post(
        "/users",
        json={
            "name": "fake_user",
            "email": "fake_email",
            "password": "fake_password",
            "retype_password": "fake_password",
        },
    )

    assert resp.status_code == 201
    assert resp.json() == {
        "id": 1,
        "name": "fake_user",
        "email": "fake_email",
        "tasks_lists": [],
    }


def test_api_get_all_users():
    resp = client.post(
        "/users",
        json={
            "name": "another_fake_user",
            "email": "another_fake_email",
            "password": "fake_password",
            "retype_password": "fake_password",
        },
    )

    assert resp.status_code == 201

    resp = client.get("/users")

    assert resp.status_code == 200
    assert resp.json() == [
        {
            "id": 1,
            "name": "fake_user",
            "email": "fake_email",
            "tasks_lists": [],
        },
        {
            "id": 2,
            "name": "another_fake_user",
            "email": "another_fake_email",
            "tasks_lists": [],
        },
    ]


def test_api_get_user():
    resp = client.get(
        "/users/1",
    )

    assert resp.status_code == 200
    assert resp.json() == {
        "id": 1,
        "name": "fake_user",
        "email": "fake_email",
        "tasks_lists": [],
    }


def test_api_patch_user():
    resp = client.patch("/users/1", json={"email": "updated_fake_email"})

    assert resp.json() == {
        "id": 1,
        "name": "fake_user",
        "email": "updated_fake_email",
        "tasks_lists": [],
    }
    assert resp.status_code == 200


def test_api_delete_user():
    _ = client.delete("/users/1")
    resp = client.delete("/users/2")

    assert resp.status_code == 200

    resp = client.get("/users/1")

    assert resp.status_code == 404

    resp = client.delete("/users/1")

    assert resp.status_code == 404
