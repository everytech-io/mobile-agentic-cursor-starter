from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4


class ItemStatus(str, Enum):
    PENDING = "pending"
    PASSED = "passed"
    FAILED = "failed"


@dataclass
class CheckItem:
    id: str
    label: str
    status: ItemStatus = ItemStatus.PENDING
    note: str = ""

    @staticmethod
    def create(label: str) -> CheckItem:
        return CheckItem(id=str(uuid4()), label=label.strip())


@dataclass
class Checklist:
    id: str
    name: str
    items: list[CheckItem] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @staticmethod
    def create(name: str, item_labels: list[str] | None = None) -> Checklist:
        labels = item_labels or []
        items = [CheckItem.create(label) for label in labels if label.strip()]
        return Checklist(id=str(uuid4()), name=name.strip(), items=items)

    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0

    @property
    def all_passed(self) -> bool:
        if self.is_empty:
            return False
        return all(item.status == ItemStatus.PASSED for item in self.items)
