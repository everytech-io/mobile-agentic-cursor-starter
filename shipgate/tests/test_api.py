import pytest
from fastapi.testclient import TestClient

from shipgate.api.app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_list_checklists():
    response = client.get("/checklists")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_create_and_get_checklist():
    created = client.post(
        "/checklists",
        json={"name": "Hotfix", "items": ["Rollback plan", "Metrics watched"]},
    )
    assert created.status_code == 201
    checklist_id = created.json()["id"]

    fetched = client.get(f"/checklists/{checklist_id}")
    assert fetched.status_code == 200
    body = fetched.json()
    assert body["name"] == "Hotfix"
    assert len(body["items"]) == 2
    assert body["ready_to_ship"] is False


def test_toggle_item():
    created = client.post("/checklists", json={"name": "Toggle test", "items": ["One"]})
    checklist_id = created.json()["id"]
    item_id = created.json()["items"][0]["id"]

    toggled = client.post(f"/checklists/{checklist_id}/items/{item_id}/toggle")
    assert toggled.status_code == 200
    assert toggled.json()["items"][0]["status"] == "passed"


def test_ready_endpoint():
    checklists = client.get("/checklists").json()
    checklist_id = checklists[0]["id"]
    response = client.get(f"/checklists/{checklist_id}/ready")
    assert response.status_code == 200
    assert "ready_to_ship" in response.json()


def test_item_detail_route_missing_until_exercise_03():
    """Exercise 03: add GET /checklists/{id}/items/{item_id}."""
    checklists = client.get("/checklists").json()
    checklist_id = checklists[0]["id"]
    item_id = checklists[0]["items"][0]["id"]
    response = client.get(f"/checklists/{checklist_id}/items/{item_id}")
    assert response.status_code in (404, 405), "Exercise 03: implement GET item detail route"
