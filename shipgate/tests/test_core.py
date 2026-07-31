import pytest

from shipgate.core.models import ItemStatus
from shipgate.core.store import ChecklistStore


def test_seed_has_release_checklist():
    store = ChecklistStore()
    checklists = store.list_checklists()
    assert len(checklists) >= 1
    assert any(c.name == "Release v1.0" for c in checklists)


def test_create_empty_checklist():
    store = ChecklistStore(seed=False)
    checklist = store.create("Empty deploy", [])
    assert checklist.is_empty
    assert store.get(checklist.id) is not None


def test_empty_message_shows_helpful_copy():
    """Exercise 02: implement empty_message — test fails until copy exists."""
    store = ChecklistStore(seed=False)
    checklist = store.create("Solo", [])
    message = store.empty_message(checklist.id)
    assert len(message) >= 10
    lowered = message.lower()
    assert "checklist" in lowered or "item" in lowered


def test_is_ready_false_when_empty():
    store = ChecklistStore(seed=False)
    checklist = store.create("No items", [])
    assert store.is_ready_to_ship(checklist.id) is False


def test_is_ready_true_when_all_passed():
    store = ChecklistStore(seed=False)
    checklist = store.create("Go", ["A", "B"])
    for item in checklist.items:
        store.set_item_status(checklist.id, item.id, ItemStatus.PASSED)
    assert store.is_ready_to_ship(checklist.id) is True


def test_get_item_detail_returns_fields():
    """Exercise 03: implement get_item_detail."""
    store = ChecklistStore()
    checklist = store.list_checklists()[0]
    item_id = checklist.items[0].id
    detail = store.get_item_detail(checklist.id, item_id)
    assert detail["label"]
    assert detail["status"] in ("pending", "passed", "failed")
    assert "blocking_reason" in detail
