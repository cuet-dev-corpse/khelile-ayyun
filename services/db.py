import json
from typing import Optional
import os

from models import Duel

DB_PATH = "db/"
HANDLES_PATH = DB_PATH + "handles.json"


def get_handle(uid: int) -> Optional[str]:
    if not os.path.exists(HANDLES_PATH):
        with open(HANDLES_PATH, "w") as f:
            f.write(json.dumps([]))
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


def add_duel(gid: int, duel: Duel) -> Optional[Duel]:
    duel_db_path = DB_PATH + str(gid) + "/duels.json"
    if not os.path.exists(duel_db_path):
        os.makedirs(DB_PATH + str(gid))
        with open(duel_db_path, "w") as f:
            f.write(json.dumps([]))
    with open(duel_db_path) as f:
        entries: list[dict] = json.loads(f.read())
    for entry in entries:
        duel_entry = Duel(**entry)
        if duel.challengeeId in [
            duel_entry.challengeeId,
            duel_entry.challengerId,
        ] or duel.challengerId in [
            duel_entry.challengeeId,
            duel_entry.challengerId,
        ]:
            return duel_entry
    entries.append(duel.model_dump())
    with open(duel_db_path, "w") as f:
        f.write(json.dumps(entries))
