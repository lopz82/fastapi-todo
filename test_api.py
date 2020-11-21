import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.mark.skip
def test_api_returns_created_tasks_list():
    resp = client.post("/taskslists", json={"name": "Test", "description": "Test list"})

    assert resp.status_code == 201
    assert resp.json() == {"id": 1, "name": "Test", "description": "Test list"}
