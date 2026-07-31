from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from release_ready.core.models import Checklist, ItemStatus
from release_ready.core.store import ChecklistStore

app = FastAPI(title="Release Ready", version="0.1.0")
store = ChecklistStore()


class CreateChecklistBody(BaseModel):
    name: str = Field(min_length=1)
    items: list[str] = Field(default_factory=list)


class ItemStatusBody(BaseModel):
    status: ItemStatus


def _serialize_checklist(checklist: Checklist) -> dict:
    return {
        "id": checklist.id,
        "name": checklist.name,
        "ready_to_ship": checklist.all_passed,
        "items": [
            {
                "id": item.id,
                "label": item.label,
                "status": item.status.value,
                "note": item.note,
            }
            for item in checklist.items
        ],
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/checklists")
def list_checklists() -> list[dict]:
    return [_serialize_checklist(c) for c in store.list_checklists()]


@app.get("/checklists/{checklist_id}")
def get_checklist(checklist_id: str) -> dict:
    checklist = store.get(checklist_id)
    if checklist is None:
        raise HTTPException(status_code=404, detail="Checklist not found")
    payload = _serialize_checklist(checklist)
    payload["empty_message"] = store.empty_message(checklist_id)
    return payload


@app.post("/checklists", status_code=201)
def create_checklist(body: CreateChecklistBody) -> dict:
    checklist = store.create(body.name, body.items)
    return _serialize_checklist(checklist)


@app.patch("/checklists/{checklist_id}/items/{item_id}")
def update_item_status(
    checklist_id: str, item_id: str, body: ItemStatusBody
) -> dict:
    try:
        checklist = store.set_item_status(checklist_id, item_id, body.status)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return _serialize_checklist(checklist)


@app.post("/checklists/{checklist_id}/items/{item_id}/toggle")
def toggle_item(checklist_id: str, item_id: str) -> dict:
    try:
        checklist = store.toggle_item_passed(checklist_id, item_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return _serialize_checklist(checklist)


@app.get("/checklists/{checklist_id}/ready")
def ready_to_ship(checklist_id: str) -> dict[str, bool]:
    try:
        ready = store.is_ready_to_ship(checklist_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {"ready_to_ship": ready}
