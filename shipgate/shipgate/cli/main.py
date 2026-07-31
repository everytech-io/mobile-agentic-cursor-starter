from __future__ import annotations

import argparse
import json
import sys

from shipgate.core.store import ChecklistStore


def main() -> None:
    parser = argparse.ArgumentParser(description="ShipGate CLI — pre-ship checks")
    sub = parser.add_subparsers(dest="command", required=True)

    list_cmd = sub.add_parser("list", help="List checklists")
    list_cmd.set_defaults(func=cmd_list)

    check_cmd = sub.add_parser("check", help="Check if checklist is ready to ship")
    check_cmd.add_argument("checklist_id", help="Checklist UUID")
    check_cmd.set_defaults(func=cmd_check)

    args = parser.parse_args()
    sys.exit(args.func(args))


def cmd_list(_args: argparse.Namespace) -> int:
    store = ChecklistStore()
    rows = [
        {"id": c.id, "name": c.name, "ready": c.all_passed}
        for c in store.list_checklists()
    ]
    print(json.dumps(rows, indent=2))
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    store = ChecklistStore()
    try:
        ready = store.is_ready_to_ship(args.checklist_id)
    except KeyError:
        print(f"Checklist not found: {args.checklist_id}", file=sys.stderr)
        return 2
    if ready:
        print("READY")
        return 0
    print("NOT READY")
    return 1


if __name__ == "__main__":
    main()
