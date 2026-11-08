"""The build: validate, compute derived state, compile the store.

Outputs (in <lab>/build/):
  graph.json    nodes + edges + derived fields, read by the map and showcases
  store.sqlite  the same, queryable (entities, edges, findings tables)
  report.md     findings grouped by code, plus summary counts
"""
from __future__ import annotations

import json
import os
import sqlite3
from collections import Counter

from . import derive
from .model import load_store
from .validate import LAYER_NAMES, validate


def compile_store(store_root: str, out_dir: str, run_mutants=True, author=None,
                  layers=(1, 2, 3, 4, 5, 6)):
    store = load_store(store_root)
    rep = validate(store, layers=layers, keep_going=True, author=author,
                   run_mutants=run_mutants)
    st = derive.staleness(store, rep.check_failed, rep.graph)
    past, future = rep.past or {}, rep.future or {}
    if not past:
        past, future = derive.cones(rep.graph, store.entities.keys())
    conds = derive.conditions(store, past)
    fnd = derive.foundation_of(store, past)
    stale_edge_keys = {(e.src, e.dst, e.derivation) for e in st["stale_edges"]}
    nodes = []
    for eid, e in sorted(store.entities.items()):
        nodes.append({
            "id": eid, "kind": e.kind, "version": e.version, "title": e.title,
            "status": e.status, "effective": rep.eff.get(eid),
            "ledger": rep.ledger.get(eid), "check": rep.check_results.get(eid, "none"),
            "stale": eid in st["stale"], "region": e.meta.get("region", ""),
            "subject": e.meta.get("subject", ""),
            "review": e.meta.get("review", ""), "ai_involved": e.meta.get("ai_involved"),
            "proposed_by": (e.meta.get("proposed_by") or {}).get("kind"),
            "credit": e.meta.get("credit") or [],
            "locators": e.meta.get("locators") or {},
            "one_liner": e.levels.get("one-liner", ""),
            "formal": e.levels.get("formal", ""),
            "technical": e.levels.get("technical", ""),
            "lay": e.levels.get("lay", ""),
            "flags": (e.meta.get("extraction") or {}).get("flags", []),
            "typing_note": ((e.meta.get("extraction") or {}).get("typing") or {}).get("note", ""),
            "has_proof": bool(e.proofs),
            "derivations": len(e.derivations()),
            "past": sorted(past.get(eid, ())), "future_size": len(future.get(eid, ())),
            "conditional_on": conds.get(eid, []),
            "foundation": fnd.get(eid, []),
            "is_foundation": derive.is_foundation(e),
            "imported_from": e.meta.get("imported_from") or [],
            "kill_condition": e.meta.get("kill_condition"),
            "observations": e.meta.get("observations") or [],
            "refuted_by": e.meta.get("refuted_by") or [],
        })
    edges = [{"src": ed.src, "kind": ed.kind, "dst": ed.dst, "pin": ed.pin,
              "derivation": ed.derivation,
              "stale": (ed.src, ed.dst, ed.derivation) in stale_edge_keys}
             for ed in derive.edges(store) if ed.dst in store.entities]
    summary = {
        "entities": Counter(e.kind for e in store.entities.values()),
        "status": Counter(e.status for e in store.entities.values()),
        "effective": Counter(rep.eff.values()),
        "ledger": Counter(v for k, v in rep.ledger.items()
                          if store.entities[k].kind == "claim"),
        "checks": Counter(rep.check_results.values()),
        "edges": Counter(e["kind"] for e in edges),
        "findings": Counter(f.code for f in rep.findings),
        "stale": len(st["stale"]),
        "layers_run": rep.layers_run,
    }
    os.makedirs(out_dir, exist_ok=True)
    graph = {"nodes": nodes, "edges": edges, "summary": summary,
             "subjects": store.subjects,
             "findings": [{"code": f.code, "entity": f.entity, "message": f.message}
                          for f in rep.findings]}
    with open(os.path.join(out_dir, "graph.json"), "w", encoding="utf-8") as fh:
        json.dump(graph, fh, indent=1, default=list)
    _sqlite(os.path.join(out_dir, "store.sqlite"), nodes, edges, rep.findings)
    _report(os.path.join(out_dir, "report.md"), summary, rep)
    return store, rep, graph


def _sqlite(path, nodes, edges, findings):
    if os.path.exists(path):
        os.remove(path)
    db = sqlite3.connect(path)
    db.execute("create table entities (id text primary key, kind text, version int, "
               "title text, status text, effective text, ledger text, check_result text, "
               "stale int, region text, one_liner text, formal text, future_size int)")
    db.execute("create table edges (src text, kind text, dst text, pin int, "
               "derivation text, stale int)")
    db.execute("create table findings (code text, entity text, message text)")
    db.executemany("insert into entities values (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   [(n["id"], n["kind"], n["version"], n["title"], n["status"],
                     n["effective"], n["ledger"], n["check"], int(n["stale"]),
                     n["region"], n["one_liner"], n["formal"], n["future_size"])
                    for n in nodes])
    db.executemany("insert into edges values (?,?,?,?,?,?)",
                   [(e["src"], e["kind"], e["dst"], e["pin"], e["derivation"],
                     int(e["stale"])) for e in edges])
    db.executemany("insert into findings values (?,?,?)",
                   [(f.code, f.entity, f.message) for f in findings])
    db.commit()
    db.close()


def _report(path, summary, rep):
    lines = ["# Store build report", ""]
    for k in ("entities", "status", "effective", "ledger", "checks", "edges"):
        lines.append(f"**{k}**: " + ", ".join(f"{a} {b}" for a, b in
                                             sorted(summary[k].items(), key=str)))
    lines.append(f"**stale claims**: {summary['stale']}")
    lines.append(f"**layers run**: " + ", ".join(f"{n} ({LAYER_NAMES[n]})"
                                                 for n in summary["layers_run"]))
    lines.append("")
    by = {}
    for f in rep.findings:
        by.setdefault(f.code, []).append(f)
    lines.append("## Findings by code\n")
    lines.append("| Code | Count | Example |")
    lines.append("| --- | --- | --- |")
    for code in sorted(by):
        ex = by[code][0]
        msg = ex.message.replace("\n", " ").replace("|", "/")[:140]
        lines.append(f"| {code} | {len(by[code])} | {ex.entity}: {msg} |")
    lines.append("")
    for code in sorted(by):
        if code.startswith("I4"):
            continue
        lines.append(f"### {code}\n")
        for f in by[code][:400]:
            lines.append("    " + f.render().replace("\n", "\n    "))
        lines.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
