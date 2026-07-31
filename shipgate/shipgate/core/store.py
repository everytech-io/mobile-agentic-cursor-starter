from __future__ import annotations

from shipgate.core.models import CheckItem, Checklist, ItemStatus


class ChecklistStore:
    """In-memory checklist store — Level 1 domain layer."""

    def __init__(self, seed: bool = True) -> None:
        self._checklists: dict[str, Checklist] = {}
        if seed:
            self._seed()

    def _seed(self) -> None:
        release = Checklist.create(
            "Release v1.0",
            ["Tests green", "Changelog updated", "Staging smoke passed"],
        )
        for item in release.items[:2]:
            item.status = ItemStatus.PASSED
        self._checklists[release.id] = release

    def list_checklists(self) -> list[Checklist]:
        return sorted(self._checklists.values(), key=lambda c: c.created_at)

    def get(self, checklist_id: str) -> Checklist | None:
        return self._checklists.get(checklist_id)

    def create(self, name: str, item_labels: list[str] | None = None) -> Checklist:
        checklist = Checklist.create(name, item_labels)
        self._checklists[checklist.id] = checklist
        return checklist

    def set_item_status(
        self, checklist_id: str, item_id: str, status: ItemStatus
    ) -> Checklist:
        checklist = self._require(checklist_id)
        item = self._require_item(checklist, item_id)
        item.status = status
        return checklist

    def toggle_item_passed(self, checklist_id: str, item_id: str) -> Checklist:
        checklist = self._require(checklist_id)
        item = self._require_item(checklist, item_id)
        # Exercise 05 bug: FAILED items jump straight to PASSED on toggle (should go to PENDING).
        if item.status == ItemStatus.PASSED:
            item.status = ItemStatus.PENDING
        else:
            item.status = ItemStatus.PASSED
        return checklist

    def is_ready_to_ship(self, checklist_id: str) -> bool:
        checklist = self._require(checklist_id)
        return checklist.all_passed

    def empty_message(self, checklist_id: str) -> str:
        """Return human-readable message when checklist has no items.

        Exercise 02: implement this — currently returns blank string.
        """
        checklist = self._require(checklist_id)
        if not checklist.is_empty:
            return ""
        return ""

    def get_item_detail(self, checklist_id: str, item_id: str) -> dict[str, str]:
        """Return detail for one checklist item.

        Exercise 03: implement — raises NotImplementedError until then.
        """
        raise NotImplementedError("Exercise 03: add get_item_detail")

    def _require(self, checklist_id: str) -> Checklist:
        checklist = self.get(checklist_id)
        if checklist is None:
            raise KeyError(f"Checklist not found: {checklist_id}")
        return checklist

    def _require_item(self, checklist: Checklist, item_id: str) -> CheckItem:
        for item in checklist.items:
            if item.id == item_id:
                return item
        raise KeyError(f"Item not found: {item_id}")
