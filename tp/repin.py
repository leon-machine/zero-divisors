"""Re-confirm pinned edges: after a reviewer has checked that a dependant still
holds with its premise's new version, move the pin to that version.
"""
import re

from .model import load_store, parse_pin

PIN_LINE = re.compile(r"^(\s*- )([a-z][a-z0-9.-]*)@(\d+)\s*$", re.M)


def repin(store_root, only=()):
    store = load_store(store_root)
    n = 0
    for eid, e in store.entities.items():
        if only and eid not in only:
            continue
        path = e.path + "/entity.md"
        text = open(path, encoding="utf-8").read()

        def sub(m):
            nonlocal n
            tgt = store.entities.get(m.group(2))
            if tgt is not None and int(m.group(3)) < tgt.version:
                n += 1
                return f"{m.group(1)}{m.group(2)}@{tgt.version}"
            return m.group(0)
        new = PIN_LINE.sub(sub, text)
        if new != text:
            open(path, "w", encoding="utf-8").write(new)
    return n
