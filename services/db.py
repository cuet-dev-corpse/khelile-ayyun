import json
from typing import Optional


HANDLES_PATH = "db/handles.json"


def get_handle(uid: int) -> Optional[str]:
    with open(HANDLES_PATH) as f:
        entries: list[dict] = json.loads(f.read())
    for entry in entries:
        if entry["uid"] == uid:
            return entry["handle"]


def set_handle(uid: int, handle: str):
    with open(HANDLES_PATH) as f:
        entries: list[dict] = json.loads(f.read())
    already_exsits = False
    for entry in entries:
        if entry["uid"] == uid:
            entry["handle"] = handle
            already_exsits = True
    if not already_exsits:
        entries.append({"uid": uid, "handle": handle})
    with open(HANDLES_PATH, "w") as f:
        f.write(json.dumps(entries))
