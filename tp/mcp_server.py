"""MCP server for the Physics Graph (JSON-RPC 2.0 over stdio, or over HTTP for hosting).

Run:  python -m tp.mcp_server --store store
Register it with an MCP client (for example Claude) as a stdio server whose
command is `python -m tp.mcp_server --store <path to store>`, with the repository
folder as the working directory (or PYTHONPATH set to it).

Modes:
  (default)      every reading tool, validate_draft, and generate_doc / regenerate_doc, which
                 write generated documents into this copy;
  --read-only    the reading tools only, for a hosted public endpoint (tp/mcp_http.py);
  --maintainer   also propose_claim and list_proposals, the old local review queue. Pull
                 requests are the way in from outside (CONTRIBUTING.md).

Text results (conventions, digest) are returned as text; everything else as compact JSON.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import shutil
import sys
import tempfile
from collections import Counter

import yaml

from . import derive
from .model import ID_RE, load_store, parse_entity_text
from .checkone import command
from .validate import programme_of, validate

PROTOCOL = "2024-11-05"
TOKEN = re.compile(r"[a-z0-9]{2,}")


class Lab:
    def __init__(self, store_root):
        self.root = os.path.abspath(store_root)
        self.lab = os.path.dirname(self.root)
        self.reload()

    def reload(self):
        self.store = load_store(self.root)
        g = derive.logical_graph(self.store)
        self.graph = g
        self.eff = derive.effective_status(self.store)
        self.ledger = derive.ledger(self.store, g)
        self.past, self.future = derive.cones(g, self.store.entities.keys())
        self.conds = derive.conditions(self.store, self.past)
        self.fnd = derive.foundation_of(self.store, self.past)
        gp = os.path.join(self.lab, "build", "graph.json")
        self.checks = {}
        if os.path.exists(gp):
            self.checks = {n["id"]: n["check"] for n in json.load(open(gp))["nodes"]}
        # BM25 index over the four levels and the title
        self.docs = {}
        for eid, e in self.store.entities.items():
            # the title counts three times: it names what the result is about
            ex = e.meta.get("extraction") or {}
            extra = [str(ex.get("unit_note") or "")] + [
                str((ex.get(k) or {}).get("note") or "") for k in ("ga_conversion", "typing")
                if isinstance(ex.get(k), dict)] + list(e.meta.get("tags") or [])
            text = " ".join([e.title] * 3 + [eid.replace(".", " ").replace("-", " ")] + extra +
                            [e.levels.get(k) or "" for k in ("one-liner", "lay", "technical", "formal")])
            self.docs[eid] = Counter(TOKEN.findall(text.lower()))
        self.df = Counter(t for c in self.docs.values() for t in c)
        self._semantic = None           # latent semantic index, built on first use
        # a later paper's "Imported:" Fact, assembled from earlier results of the
        # series, restates them: it is the paper's citation, not a new result
        self.restates = {}
        for eid, e in self.store.entities.items():
            ds = [d for d in e.derivations() if isinstance(d, dict)]
            prem = [p.split("@")[0] for d in ds for p in (d.get("uses") or [])]
            proof = " ".join(e.proofs.values()).strip().lower()
            if e.status == "proved" and prem and (
                    e.title.lower().startswith("imported")
                    or proof.startswith(("restated from", "follows from \\claimref"))
                    and len(proof) < 400):
                self.restates[eid] = sorted(set(prem))
        self.restated_by = {}
        for k, v in self.restates.items():
            for x in v:
                self.restated_by.setdefault(x, []).append(k)
        self.direct_users = {}
        for a, bs in self.graph.items():
            for b in bs:
                self.direct_users.setdefault(b, []).append(a)
        self.namesakes = self._namesakes()
        used = Counter()
        for a, bs in self.graph.items():
            for b in bs:
                used[b] += 1
        self.used_by = used
        lp = os.path.join(self.lab, "build", "layout.json")
        self.pos = json.load(open(lp))["positions"] if os.path.exists(lp) else {}
        self.avg = sum(sum(c.values()) for c in self.docs.values()) / max(len(self.docs), 1)

    # ---- tools -----------------------------------------------------------
    def neighbourhood(self, id, k=12):
        """The results nearest in the argument: direct premises and dependants,
        then the nearest points of the graph's layout (which places each result
        near what it rests on and what rests on it)."""
        if id not in self.store.entities:
            raise ValueError(f"no entity {id!r}")
        e = self.store.entities[id]
        prem = sorted({p.split("@")[0] for d in e.derivations() if isinstance(d, dict)
                       for p in (d.get("uses") or []) + (d.get("assumes") or [])})
        dep = sorted(x for x, o in self.store.entities.items()
                     if any(p.split("@")[0] == id for d in o.derivations() if isinstance(d, dict)
                            for p in (d.get("uses") or []) + (d.get("assumes") or [])))
        near = []
        if id in self.pos:
            p = self.pos[id]
            dist = sorted((math.dist(p, q), x) for x, q in self.pos.items()
                          if x != id and x not in prem and x not in dep)
            near = [self._brief(x, round(d, 3)) for d, x in dist[:int(k)]]
        return {"rests_on": [self._brief(x) for x in prem if x in self.store.entities],
                "used_by": [self._brief(x) for x in dep],
                "nearby": near}

    STEP_SPLIT = re.compile(r"\n\s*\n|(?<=[.:;])\s+(?=\((?:[1-9]|i{1,3}|iv|v|vi{0,3})\)\s)"
                            r"|(?<=[.:;])\s+(?=(?:\\emph\{)?Step\s)")

    def get_proof(self, id):
        """The proof cut into steps (paragraphs and numbered steps), each with
        the results it cites, so a reader can see which step uses which premise."""
        e = self.store.entities.get(id)
        if e is None:
            raise ValueError(f"no entity {id!r}")
        ders = [d for d in e.derivations() if isinstance(d, dict)]
        out = {}
        for name, text in e.proofs.items():
            if not text.strip():
                continue
            steps = [x.strip() for x in self.STEP_SPLIT.split(text) if x and x.strip()]
            premises = set()
            for d in ders:
                if d.get("name") == name:
                    premises = {p.split("@")[0] for p in (d.get("uses") or []) + (d.get("assumes") or [])}
            cited_all = set()
            rows = []
            for k, st in enumerate(steps, 1):
                cites = list(dict.fromkeys(re.findall(r"\\claimref\{([^}]+)\}", st)))
                cited_all.update(cites)
                rows.append({"step": k, "text": st, "cites": cites})
            pointer = (not re.search(r"\\claimref|\$|\\\[", text)
                       and re.search(r"check|script|run|verif|\.py", text, re.I) is not None)
            out[name] = {"steps": rows,
                         "kind": "reference to a verification run" if pointer else "proof text",
                         "premises_not_cited_in_text": sorted(premises - cited_all),
                         "cited_but_not_premises": sorted(c for c in cited_all - premises
                                                          if c in self.store.entities)}
        return {"id": id, "status": e.status, "effective_status": self.eff.get(id),
                "statement": e.levels.get("formal"), "derivations": ders, "proofs": out,
                "imported_from": e.meta.get("imported_from"),
                "holds_given": self.conds.get(id, []),
                "rests_on_foundation": self.fnd.get(id, [])}

    def conventions(self):
        """How to read the store: the model, notation, the two imaginary units and
        their known limits, and a suggested way to work."""
        p = os.path.join(self.store.root, "conventions.md")
        return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

    def notation(self, macro=None):
        """The LaTeX macros the texts use, with their definitions."""
        n = self.store.notation or {}
        if macro:
            m = macro.lstrip("\\")
            if m not in n:
                raise ValueError(f"no macro {macro!r}")
            return {m: n[m]}
        return n

    def trail(self, subject):
        """The guided walk through one subject, step by step, with its prose."""
        from .site import _trails
        for t in _trails(os.path.join(self.lab, "documents")):
            if t["subject"] == subject or t["id"] == subject:
                for s in t["steps"]:
                    s.update(self._brief(s["id"]))
                return t
        raise ValueError(f"no trail for {subject!r}; subjects: "
                         + ", ".join(x["id"] for x in self.store.subjects))

    def digest(self, subject, level="technical", limit=60, include_notes=False):
        """A subject as Markdown for reading in one go: each result's statement or
        level text, its premises, and its proof, in dependency order. Notes (the papers'
        running text, remarks, examples) are left out unless include_notes is set."""
        if level not in ("formal", "technical", "lay", "one-liner"):
            raise ValueError("level must be formal, technical, lay or one-liner")
        if not any(x["id"] == subject for x in self.store.subjects):
            raise ValueError(f"no subject {subject!r}; list_subjects gives them")
        ids = [x for x, e in self.store.entities.items() if e.meta.get("subject") == subject
               and (include_notes or e.kind != "note")]
        if not ids:
            raise ValueError(f"no subject {subject!r}")
        order = [x for x in derive.topo_order(self.graph, self.store.entities.keys()) if x in ids]
        out = []
        if len(order) > int(limit):
            out.append(f"_{len(order)} entries in this subject; the first {int(limit)} in "
                       "dependency order follow (raise limit for more)._\n")
        for x in order[:int(limit)]:
            e = self.store.entities[x]
            text = (e.levels.get(level) or "").strip()
            if e.kind == "note" or not text or text == "pending":
                text = (e.levels.get("formal") or "").strip()
            prem = sorted({p.split("@")[0] for d in e.derivations() if isinstance(d, dict)
                           for p in (d.get("uses") or []) + (d.get("assumes") or [])})
            out.append(f"## {e.title}\n`{x}` · {e.status}"
                       + (f" · holds given {', '.join(self.conds.get(x, []))}" if self.conds.get(x) else "")
                       + f"\n\n{text}\n"
                       + (f"\nRests on: {', '.join(prem)}\n" if prem else "")
                       + "".join(f"\n**{k}**\n{v.strip()}\n" for k, v in e.proofs.items() if v.strip()))
        return "\n".join(out)

    def list_subjects(self, programme=None):
        counts = Counter(e.meta.get("subject") for e in self.store.entities.values())
        dflt = self.store.config.get("default_programme")
        out = [{**s, "programme": s.get("programme") or dflt, "count": counts.get(s["id"], 0)}
               for s in self.store.subjects]
        return [s for s in out if not programme or s["programme"] == programme]

    def _programme_registry(self):
        """store/config.yaml `programmes` as {id: {title, about, maintainers}} (a mapping
        id -> mapping, as E218 requires; a list of ids or mappings is read too)."""
        raw = self.store.config.get("programmes") or {}
        items = raw.items() if isinstance(raw, dict) else [
            ((x.get("id") if isinstance(x, dict) else x), x) for x in raw]
        out = {}
        for k, v in items:
            if not k:
                continue
            v = v if isinstance(v, dict) else {"title": v}
            out[str(k)] = {"title": str(v.get("title") or k), "about": str(v.get("about") or ""),
                           "maintainers": list(v.get("maintainers") or [])}
        return out

    def list_programmes(self):
        """The research programmes the store holds side by side: id, title, about,
        maintainers, whether it is the default, its subjects and its entity counts.
        A programme named by an entity or subject but missing from config.yaml is
        listed with registered: false (the validator reports it as E218)."""
        reg = self._programme_registry()
        dflt = self.store.config.get("default_programme")
        by_prog, kinds = Counter(), {}
        for e in self.store.entities.values():
            p = programme_of(self.store, e)
            by_prog[p] += 1
            kinds.setdefault(p, Counter())[e.kind] += 1
        subs = {}
        for s in self.store.subjects:
            subs.setdefault(s.get("programme") or dflt, []).append(s["id"])
        ids = list(reg) + sorted({p for p in list(by_prog) + list(subs)
                                  if p and p not in reg})
        return [{"id": p, "title": reg.get(p, {}).get("title", p),
                 "about": reg.get(p, {}).get("about", ""),
                 "maintainers": reg.get(p, {}).get("maintainers", []),
                 "default": p == dflt, "registered": p in reg,
                 "subjects": subs.get(p, []), "count": by_prog.get(p, 0),
                 "by_kind": dict(sorted(kinds.get(p, Counter()).items()))}
                for p in ids]

    LABEL_RE = re.compile(r"(?:Hypothesis|Premise|Postulate|Axiom|Principle)\s*\(?([A-Z][A-Za-z0-9]{0,3}(?:_[A-Za-z0-9]+)?)\)?"
                          r"|\(([A-Z][A-Za-z0-9]{0,3})\)")

    def _namesakes(self):
        """Postulates that share a short name ("(S)", "U", "H") across papers."""
        by = {}
        for eid, e in self.store.entities.items():
            if e.status != "postulate":
                continue
            m = self.LABEL_RE.search(e.title)
            if m:
                by.setdefault(m.group(1) or m.group(2), []).append(eid)
        return {k: v for k, v in by.items() if len(v) > 1}

    def _paper_titles(self):
        if getattr(self, "_papers", None) is None:
            from .extract import PAPERS
            from .recreate import paper_title
            suite = os.path.normpath(os.path.join(self.root, self.store.config.get(
                "legacy_scripts_dir") or "..", ".."))
            suite = os.path.dirname(self.lab)
            counts = Counter((e.meta.get("locators") or {}).get("paper")
                             for e in self.store.entities.values() if e.kind != "note")
            out = []
            for code, tex, region, script in PAPERS:
                try:
                    title = paper_title(suite, tex)
                except Exception:
                    title = ""
                out.append({"code": code, "title": title, "id_prefix": region,
                            "results": counts.get(code, 0)})
            self._papers = out
        return self._papers

    def list_papers(self):
        return self._paper_titles()

    SORTS = ("future_cone_size", "future_cone_size_without_restatements", "past_cone_size",
             "used_by", "title", "id")

    def list_entities(self, subject=None, tag=None, status=None, kind=None, paper=None,
                      uncited_premises=None, exclude_restatements=False, include_notes=False,
                      sort_by="id", descending=True, limit=50, offset=0, fields=None,
                      programme=None):
        """Every entity matching the filters (no query needed), sorted and paged."""
        if sort_by not in self.SORTS:
            raise ValueError(f"sort_by must be one of {', '.join(self.SORTS)}")
        rows = []
        for eid, e in self.store.entities.items():
            if e.kind == "note" and not include_notes and kind != "note":
                continue
            if subject and e.meta.get("subject") != subject:
                continue
            if tag and tag not in (e.meta.get("tags") or []):
                continue
            if status and e.status != status:
                continue
            if kind and e.kind != kind:
                continue
            if paper and (e.meta.get("locators") or {}).get("paper") != paper:
                continue
            if programme and programme_of(self.store, e) != programme:
                continue
            if exclude_restatements and eid in self.restates:
                continue
            if uncited_premises is not None:
                has = bool(self._uncited(eid))
                if has != bool(uncited_premises):
                    continue
            rows.append(eid)
        key = {"future_cone_size": lambda x: len(self.future.get(x, ())),
               "future_cone_size_without_restatements": lambda x: len(
                   [y for y in self.future.get(x, ()) if y not in self.restates]),
               "past_cone_size": lambda x: len(self.past.get(x, ())),
               "used_by": lambda x: self.used_by.get(x, 0),
               "title": lambda x: self.store.entities[x].title.lower(),
               "id": lambda x: x}[sort_by]
        rev = descending if sort_by not in ("title", "id") else False
        rows.sort(key=key, reverse=rev)
        page = rows[int(offset):int(offset) + int(limit)]
        return {"total": len(rows), "offset": int(offset),
                "results": [self._summary(x, fields=fields) for x in page]}

    def get_claims(self, ids, fields=None):
        """Several entities at once, optionally only some fields of each summary."""
        return [self._summary(x, fields=fields) if x in self.store.entities
                else {"id": x, "error": "no such entity"} for x in ids[:200]]

    def _uncited(self, eid):
        e = self.store.entities[eid]
        out = []
        for d in e.derivations():
            if not isinstance(d, dict):
                continue
            text = e.proofs.get(d.get("name"), "")
            if not text.strip():
                continue
            cited = set(re.findall(r"\\claimref\{([^}]+)\}", text))
            out += [p.split("@")[0] for p in (d.get("uses") or []) + (d.get("assumes") or [])
                    if p.split("@")[0] not in cited]
        return out

    def find_text(self, pattern, regex=False, include_notes=True, limit=20, where="all"):
        """Literal (or regular-expression) search in the stored LaTeX: statements,
        the other levels, proofs and notes. For formulas and exact phrases, e.g.
        'Q(x)' or 'n_{\\infty}'."""
        try:
            rx = re.compile(pattern if regex else re.escape(pattern), re.I)
        except re.error as exc:
            raise ValueError(f"bad pattern: {exc}")
        hits = []
        for eid, e in sorted(self.store.entities.items()):
            if e.kind == "note" and not include_notes:
                continue
            parts = [("formal", e.levels.get("formal") or "")]
            if where == "all":
                parts += [(lv, e.levels.get(lv) or "") for lv in ("technical", "lay", "one-liner")]
                parts += [("proof-" + k, v) for k, v in e.proofs.items()]
            for name, text in parts:
                m = rx.search(text)
                if m:
                    a, b = max(0, m.start() - 120), min(len(text), m.end() + 120)
                    hits.append({"id": eid, "title": e.title, "kind": e.kind, "in": name,
                                 "context": re.sub(r"\s+", " ", text[a:b])})
                    break
            if len(hits) >= int(limit):
                break
        return hits

    def list_tags(self):
        counts = Counter(t for e in self.store.entities.values()
                         for t in (e.meta.get("tags") or []))
        return [{**t, "count": counts.get(t["id"], 0)} for t in self.store.tags]

    def list_open_problems(self, area=None, kind=None, difficulty=None, status=None,
                           entity=None):
        """The curated open problems (store/open_problems.yaml), filtered; summaries only.
        Pass entity to find the problems that start from a given result."""
        out = []
        for op in self.store.open_problems or []:
            if area and op.get("area") != area:
                continue
            if kind and op.get("kind") != kind:
                continue
            if difficulty and op.get("difficulty") != difficulty:
                continue
            if status and op.get("status") != status:
                continue
            if entity and entity not in (op.get("entities") or []):
                continue
            out.append({k: op.get(k) for k in ("id", "title", "area", "kind", "difficulty",
                                                "status", "source")}
                       | {"statement": op.get("statement")})
        return {"count": len(out), "problems": out,
                "contribute": "Read a problem with get_open_problem, work from its entities, "
                              "then validate_draft and propose_claim; record the problem's id "
                              "under extraction.open_problem in the draft's front matter."}

    def get_open_problem(self, id):
        """One open problem in full, with summaries of the entities it starts from and any
        proposals or store entities that record it under extraction.open_problem."""
        op = next((o for o in self.store.open_problems or [] if o.get("id") == id), None)
        if op is None:
            raise ValueError(f"no open problem {id!r}; list_open_problems lists them")
        ents = [self._brief(x) if x in self.store.entities else {"id": x, "error": "no such entity"}
                for x in op.get("entities") or []]
        work = [eid for eid, e in self.store.entities.items()
                if ((e.meta.get("extraction") or {}).get("open_problem") == id)]
        return {"problem": op, "entities": ents, "work_in_store": work}

    def search_claims(self, query, subject=None, status=None, limit=10, tag=None,
                      include_notes=False, programme=None, fields=None):
        q = TOKEN.findall((query or "").lower())
        if not q:   # no words: list what the filters select
            return self.list_entities(subject=subject, tag=tag, status=status,
                                      include_notes=include_notes, programme=programme,
                                      sort_by="future_cone_size", limit=limit, fields=fields)["results"]
        N = len(self.docs)
        scores = []
        for eid, c in self.docs.items():
            e = self.store.entities[eid]
            if e.kind == "note" and not include_notes:
                continue        # remarks and the papers' running text crowd out results
            if subject and e.meta.get("subject") != subject:
                continue
            if tag and tag not in (e.meta.get("tags") or []):
                continue
            if status and e.status != status:
                continue
            if programme and programme_of(self.store, e) != programme:
                continue
            L = sum(c.values())
            s = 0.0
            for t in q:
                if t in c:
                    idf = math.log(1 + (N - self.df[t] + 0.5) / (self.df[t] + 0.5))
                    s += idf * c[t] * 2.2 / (c[t] + 1.2 * (0.25 + 0.75 * L / self.avg))
            scores.append((s, eid))
        # hybrid ranking: exact words (BM25), meaning (a latent semantic index
        # built from the store's own text, so related wording also matches), and
        # a small prior for results the rest of the store builds on
        best = max((x for x, _ in scores), default=0) or 1.0
        sem = self._semantic_scores(query)
        ranked = []
        for b, eid in scores:
            phrase = 1.0 if query.lower().strip() in self.store.entities[eid].title.lower() else 0.0
            v = (b / best) + 0.7 * max(sem.get(eid, 0.0), 0.0) + 0.3 * phrase \
                + 0.08 * math.log1p(self.used_by.get(eid, 0))
            if b > 0 or sem.get(eid, 0) > 0.35:
                ranked.append((v, eid))
        ranked.sort(reverse=True)
        return [self._brief(eid, round(v, 3), fields) for v, eid in ranked[:int(limit)]]

    def _semantic_scores(self, query):
        """Cosine similarity in a latent semantic space (TF-IDF reduced by SVD)
        trained on the store itself; {} when scikit-learn is unavailable."""
        try:
            if self._semantic is None:
                from sklearn.feature_extraction.text import TfidfVectorizer
                from sklearn.decomposition import TruncatedSVD
                from sklearn.preprocessing import normalize
                ids = list(self.docs)
                texts = [" ".join(t for t, n in self.docs[i].items() for _ in range(min(n, 5)))
                         for i in ids]
                vec = TfidfVectorizer(sublinear_tf=True, min_df=2, max_df=0.5)
                X = vec.fit_transform(texts)
                svd = TruncatedSVD(n_components=min(160, X.shape[1] - 1), random_state=0)
                Z = normalize(svd.fit_transform(X))
                self._semantic = (ids, vec, svd, Z, normalize)
            ids, vec, svd, Z, normalize = self._semantic
            qv = normalize(svd.transform(vec.transform([" ".join(TOKEN.findall(query.lower()))])))
            sims = Z @ qv[0]
            return {i: float(x) for i, x in zip(ids, sims)}
        except Exception:
            return {}

    BRIEF = ("id", "title", "kind", "status", "effective_status", "subject", "one_liner", "evidence",
             "holds_given", "used_by", "past_cone_size", "future_cone_size", "score")

    def _brief(self, eid, score=None, fields=None):
        """The summary the list-style tools return by default: what an agent needs to choose
        what to read next. Empty values and an effective status equal to the status are left
        out; get_claim, get_claims or fields give the rest."""
        if fields:
            return self._summary(eid, score, fields)
        full = self._summary(eid, score)
        out = {k: full[k] for k in self.BRIEF if k in full and full[k] not in (None, [], {}, "none")}
        if out.get("effective_status") == out.get("status"):
            out.pop("effective_status", None)
        return out

    def _summary(self, eid, score=None, fields=None):
        e = self.store.entities[eid]
        one = (e.levels.get("one-liner") or "").strip()
        if not one or one == "pending":           # notes carry only their formal text
            f = re.sub(r"\s+", " ", (e.levels.get("formal") or "")).strip()
            one = f[:200] + ("..." if len(f) > 200 else "")
        out = {"id": eid, "title": e.title, "kind": e.kind, "status": e.status,
               "effective_status": self.eff.get(eid), "subject": e.meta.get("subject"),
               "programme": programme_of(self.store, e),
               "tags": e.meta.get("tags") or [], "one_liner": one,
               "evidence": self.checks.get(eid),
               "holds_given": self.conds.get(eid, []),
               "rests_on_foundation": self.fnd.get(eid, []),
               "past_cone_size": len(self.past.get(eid, ())),
               "future_cone_size": len(self.future.get(eid, ())),
               "future_cone_size_without_restatements": len(
                   [x for x in self.future.get(eid, ()) if x not in self.restates]),
               "used_by": self.used_by.get(eid, 0),
               "source": (e.meta.get("locators") or {})}
        if e.kind == "prediction":
            out["effective_status"] = e.status
            out["basis_status"] = self.eff.get(eid)
        out["restates"] = self.restates.get(eid, [])
        out["restated_by"] = sorted(self.restated_by.get(eid, []))
        out["refuted_by"] = e.meta.get("refuted_by") or []
        out["rests_on"] = sorted(self.graph.get(eid, ()))
        out["used_by_ids"] = sorted(self.direct_users.get(eid, []))
        if score is not None:
            out["score"] = score
        if fields:
            unknown = sorted(set(fields) - set(out) - {"score"})
            if unknown:
                raise ValueError(f"unknown field(s) {unknown}; fields are: "
                                 + ", ".join(sorted(out)))
            keep = set(fields) | {"id"}
            out = {k: v for k, v in out.items() if k in keep}
        else:   # the long lists are for asking about; keep the default summary short
            for k in ("rests_on", "used_by_ids", "restated_by"):
                if len(out[k]) > 12:
                    out[k] = out[k][:12] + [f"... {len(out[k]) - 12} more"]
        return out

    def get_claim(self, id, notes_text=False):
        e = self.store.entities.get(id)
        if e is None:
            if id in self.store.replaced_by:
                raise ValueError(f"{id!r} is retired (a duplicate); it was merged into "
                                 f"{self.store.replaced_by[id]!r}")
            raise ValueError(f"no entity {id!r}")
        notes = []
        for n in self.store.entities.values():
            if n.kind == "note" and id in (n.meta.get("comments_on") or []):
                t = (n.levels.get("formal") or "").strip()
                notes.append({"id": n.id, "kind": n.status, "title": n.title,
                              "text" if notes_text else "opening":
                              t if notes_text else t[:240] + ("..." if len(t) > 240 else "")})
        return {"front_matter": e.meta, "levels": e.levels, "proofs": e.proofs,
                "notes": notes,
                "derived": {"effective_status": (e.status if e.kind == "prediction"
                                                 else self.eff.get(id)),
                            "basis_status": (self.eff.get(id) if e.kind == "prediction"
                                             else None),
                            "namesakes": [x for v in self.namesakes.values() if id in v
                                          for x in v if x != id],
                            "restates": self.restates.get(id, []),
                            "restated_by": sorted(self.restated_by.get(id, [])),
                            "rests_on": sorted(self.graph.get(id, ())),
                            "used_by": sorted(self.direct_users.get(id, [])),
                            "ledger": self.ledger.get(id),
                            "programme": programme_of(self.store, e),
                            "holds_given": self.conds.get(id, []),
                            "evidence": self.checks.get(id),
                            "check_command": (command(id) if e.meta.get("checked_by") else None),
                            "past_cone_size": len(self.past.get(id, ())),
                            "future_cone_size": len(self.future.get(id, ()))}}

    def cone(self, id, direction="past", limit=200, fields=None):
        if id not in self.store.entities:
            raise ValueError(f"no entity {id!r}")
        ids = self.past[id] if direction == "past" else self.future[id]
        return [self._brief(x, fields=fields) for x in sorted(ids)[:int(limit)]]

    PROOF_NAME = re.compile(r"^proof-[A-Za-z0-9_-]{1,60}\.tex$")
    SAFE_LAYERS = (1, 2, 3, 5)      # layer 4 runs code; it runs at review, never over MCP

    def _check_inputs(self, meta, proofs):
        eid = meta.get("id")
        if not isinstance(eid, str) or not ID_RE.fullmatch(eid):
            return f"id {eid!r} is not a valid entity id (lowercase dotted, e.g. 'tower.my-result')"
        for name in (proofs or {}):
            if not isinstance(name, str) or not self.PROOF_NAME.fullmatch(name):
                return f"proof file name {name!r} must look like 'proof-main.tex'"
        return None

    def _baseline(self, layers=(1, 2, 3)):
        # the store's own findings for the same layers the draft runs, so that only what the
        # draft introduces is reported (a layer-5 baseline is needed when layer 5 is asked for)
        cache = self.__dict__.setdefault("_bases", {})
        if layers not in cache:
            rep = validate(self.store, layers=layers, keep_going=True, run_mutants=False)
            cache[layers] = {(f.code, f.entity, f.message) for f in rep.findings}
        return cache[layers]

    def validate_draft(self, entity_md, proofs=None, check_py=None, layers="1-3"):
        """Validate a draft entity against a copy of the store.  Reports every finding
        the draft introduces (not only those on the draft itself).  Evidence checks
        (layer 4) are never run here: they execute code, and run at maintainer review."""
        meta, _, errs = parse_entity_text(entity_md)
        if errs:
            return {"ok": False, "findings": [{"code": e[:4], "message": e[5:]} for e in errs]}
        bad = self._check_inputs(meta, proofs)
        if bad:
            return {"ok": False, "findings": [{"code": "E102", "severity": "error",
                                               "message": bad, "fix": ""}]}
        eid, kind = meta["id"], meta.get("kind", "claim")
        sub = {"claim": "claims", "object": "objects", "prediction": "predictions",
               "question": "questions"}.get(kind, "claims")
        lay = [int(x) for x in re.findall(r"\d", str(layers))] or [1, 3]
        want = range(lay[0], lay[-1] + 1) if "-" in str(layers) else lay
        layers = tuple(x for x in want if x in self.SAFE_LAYERS) or (1, 2, 3)
        base = self._baseline(layers)
        with tempfile.TemporaryDirectory() as tmp:
            root = os.path.join(tmp, "store")
            shutil.copytree(self.root, root, ignore=shutil.ignore_patterns(".tp-cache"))
            folder = os.path.join(root, sub, eid)
            if os.path.realpath(folder).startswith(os.path.realpath(root) + os.sep) is False:
                return {"ok": False, "findings": [{"code": "E102", "severity": "error",
                                                   "message": "bad id", "fix": ""}]}
            existing = os.path.exists(folder)
            credit_findings = []
            old_state = None
            if existing:
                from .model import load_entity, lock_entry
                old_state = lock_entry(load_entity(folder))
                # an amendment keeps every earlier credit and adds its own (E603, E604)
                from .credit import compare, describe
                with open(os.path.join(folder, "entity.md"), encoding="utf-8") as fh:
                    old_meta, _, _ = parse_entity_text(fh.read())
                removed, unclaimed = compare(old_meta.get("credit"), meta.get("credit"),
                                             int(old_meta.get("version") or 0), int(meta.get("version") or 0))
                credit_findings += [{"code": "E603", "severity": "error", "entity": eid,
                                     "message": f"a credit entry of the stored version is missing or changed: {describe(r)}",
                                     "fix": "keep every earlier credit entry as it was"} for r in removed]
                if unclaimed:
                    credit_findings.append({"code": "E604", "severity": "error", "entity": eid,
                                            "message": f"version {meta.get('version')} has no credit entry of its own",
                                            "fix": "add {name, role, version} for yourself and for the AI model that drafted it"})
                shutil.rmtree(folder)      # inside the temporary copy only
            os.makedirs(folder)
            open(os.path.join(folder, "entity.md"), "w").write(entity_md)
            for name, text in (proofs or {}).items():
                open(os.path.join(folder, name), "w").write(text)
            if check_py:
                open(os.path.join(folder, "check.py"), "w").write(check_py)
            # the language is geometric algebra: a draft that leaves it says why (E609)
            from .galang import unexcused
            from .model import load_entity as _le
            _draft = _le(folder)
            _hits = unexcused(_draft)
            if _hits:
                credit_findings.append({"code": "E609", "severity": "error", "entity": eid,
                                        "message": f"written outside geometric algebra ({', '.join(_hits)}) without saying why",
                                        "fix": "translate it, or declare outside_ga: {kind: imported | complex-analysis | bridge | other, why: ...}"})
            if old_state:
                # an amendment says what it fixes, and its kind matches what changed (E605-E608)
                from .amend import findings as amendment_findings
                from .model import load_entity
                credit_findings += [{"code": c, "severity": "error", "entity": eid, "message": m, "fix": f}
                                    for c, m, f in amendment_findings(old_state, load_entity(folder))]
            rep = validate(load_store(root), layers=layers, keep_going=True,
                           run_mutants=False)
        new = [f for f in rep.findings if (f.code, f.entity, f.message) not in base
               or f.entity.split("@")[0] == eid]
        out = {"ok": not any(f.severity == "error" for f in new) and not credit_findings,
               "layers_run": list(layers), "replaces_existing": existing,
               "findings": credit_findings + [{"code": f.code, "severity": f.severity, "entity": f.entity,
                                               "message": f.message, "fix": f.fix} for f in new]}
        if check_py:
            out["note"] = ("check.py was not run (validate_draft never runs code). Put the folder "
                           "under store/ in your copy and run `python -m tp check-one <id> --store "
                           "store`; the pull request's checks run it again")
        return out

    def propose_claim(self, entity_md, proofs=None, check_py=None, author="ai"):
        res = self.validate_draft(entity_md, proofs, check_py)
        if not res["ok"]:
            return {"accepted_for_review": False, **res}
        meta, _, _ = parse_entity_text(entity_md)
        base = os.path.realpath(os.path.join(self.lab, "proposals"))
        folder = os.path.join(base, meta["id"])
        if not os.path.realpath(folder).startswith(base + os.sep):
            return {"accepted_for_review": False, "error": "bad id"}
        if os.path.exists(folder):
            return {"accepted_for_review": False,
                    "error": f"a proposal {meta['id']!r} is already waiting for review"}
        os.makedirs(folder)
        open(os.path.join(folder, "entity.md"), "w").write(entity_md)
        for name, text in (proofs or {}).items():
            open(os.path.join(folder, name), "w").write(text)
        if check_py:
            open(os.path.join(folder, "check.py"), "w").write(check_py)
        json.dump({"author": str(author)[:80], "status": "proposed",
                   "kind": meta.get("kind")},
                  open(os.path.join(folder, "proposal.json"), "w"))
        return {"accepted_for_review": True, "folder": folder, **res}

    def list_proposals(self):
        base = os.path.join(self.lab, "proposals")
        if not os.path.isdir(base):
            return []
        return [{"id": d, **json.load(open(os.path.join(base, d, "proposal.json")))}
                for d in sorted(os.listdir(base))
                if os.path.exists(os.path.join(base, d, "proposal.json"))]

    def generate_doc(self, recipe_yaml):
        from .docgen import generate
        from .docgen import check_doc_id
        recipe = yaml.safe_load(recipe_yaml)
        check_doc_id(recipe.get("doc"))
        os.makedirs(os.path.join(self.lab, "recipes"), exist_ok=True)
        path = os.path.join(self.lab, "recipes", recipe["doc"] + ".yaml")
        open(path, "w").write(recipe_yaml)
        r = generate(self.root, path)
        return {"doc": r["doc_id"], "version": r["version"], "bump": r["bump"],
                "folder": r["folder"], "audit": r.get("audit", [])}

    def regenerate_doc(self, doc_id):
        from .docgen import regenerate, check_doc_id
        check_doc_id(doc_id)
        r = regenerate(self.root, doc_id)
        return {k: r.get(k) for k in ("doc_id", "version", "bump", "changelog",
                                      "conflicts", "audit")}


TOOLS = [
    ("conventions", "Read this first: what the entities and links mean, which fields the "
                    "build derives, the notation, and the two imaginary units (I4 for the "
                    "field theory, I6 on the right for conformal spinors) with their limits.",
     {}),
    ("notation", "The LaTeX macros the store's texts use, with definitions; one macro or all.",
     {"macro": {"type": "string"}}),
    ("list_programmes", "The research programmes the store holds side by side (the Transport "
                        "Papers, standard physics imported once, and any other): title, "
                        "about, maintainers, the default, their subjects and entity counts.",
     {}),
    ("list_subjects", "List the subject areas with their programme and entity counts; "
                      "programme filters them.", {"programme": {"type": "string"}}),
    ("find_text", "Literal or regular-expression search in the stored LaTeX (statements, "
                  "levels, proofs, and notes including the papers' own running text): for "
                  "formulas and exact phrases such as 'Q(x)'.",
     {"pattern": {"type": "string"}, "regex": {"type": "boolean"},
      "include_notes": {"type": "boolean"}, "limit": {"type": "integer"},
      "where": {"type": "string"}}, ["pattern"]),
    ("list_papers", "The series' papers and notes: code (as in an entity's source), title, "
                    "the id prefix its results carry, and how many results it has.", {}),
    ("list_entities", "Every entity matching filters, with no query: subject, tag, status, "
                      "kind, paper, programme, uncited_premises (proofs that never cite a "
                      "premise they list), exclude_restatements; sorted by future_cone_size (most built "
                      "upon), past_cone_size, used_by, title or id; paged with limit and "
                      "offset; fields picks summary fields.",
     {"subject": {"type": "string"}, "tag": {"type": "string"}, "status": {"type": "string"},
      "kind": {"type": "string"}, "paper": {"type": "string"},
      "uncited_premises": {"type": "boolean"}, "exclude_restatements": {"type": "boolean"},
      "include_notes": {"type": "boolean"}, "sort_by": {"type": "string"},
      "descending": {"type": "boolean"}, "limit": {"type": "integer"},
      "offset": {"type": "integer"}, "fields": {"type": "array", "items": {"type": "string"}},
      "programme": {"type": "string"}}),
    ("get_claims", "Summaries of several entities at once (up to 200), optionally only the "
                   "named fields (e.g. future_cone_size, holds_given, evidence).",
     {"ids": {"type": "array", "items": {"type": "string"}},
      "fields": {"type": "array", "items": {"type": "string"}}}, ["ids"]),
    ("list_tags", "List the tag vocabulary (cross-cutting themes) with entity counts.", {}),
    ("list_open_problems", "The curated open problems that agents or users can attack: "
                           "statement, area, kind (research, consistency, housekeeping), "
                           "difficulty (tractable, substantial, frontier) and status; filter by "
                           "any of these, or by an entity the problem starts from.",
     {"area": {"type": "string"}, "kind": {"type": "string"},
      "difficulty": {"type": "string"}, "status": {"type": "string"},
      "entity": {"type": "string"}}),
    ("get_open_problem", "One open problem in full: why it matters, what is known, routes of "
                         "attack, what would settle it, the entities to start from, and work "
                         "already filed against it.", {"id": {"type": "string"}}, ["id"]),
    ("search_claims", "Search claims by text (titles and all four levels); filter by "
                      "subject, status, tag or programme. Each hit is a brief summary; fields "
                      "picks summary fields instead (get_claims lists them).",
     {"query": {"type": "string"}, "subject": {"type": "string"}, "tag": {"type": "string"},
      "programme": {"type": "string"},
      "include_notes": {"type": "boolean"},
      "status": {"type": "string"}, "limit": {"type": "integer"},
      "fields": {"type": "array", "items": {"type": "string"}}}, ["query"]),
    ("get_claim", "One entity: front matter, levels, proofs and derived fields "
                  "(effective status, ledger, postulates it holds given, evidence), and "
                  "the notes on it (settings from the paper's text, remarks, examples): "
                  "their openings, or full text with notes_text=true. A note's id can "
                  "itself be passed to get_claim.",
     {"id": {"type": "string"}, "notes_text": {"type": "boolean"}}, ["id"]),
    ("cone", "The past cone (everything an entity rests on) or future cone "
             "(everything resting on it), as brief summaries; fields picks summary fields.",
     {"id": {"type": "string"}, "direction": {"type": "string", "enum": ["past", "future"]},
      "limit": {"type": "integer"}, "fields": {"type": "array", "items": {"type": "string"}}}, ["id"]),
    ("neighbourhood", "What a result rests on, what rests on it, and the nearest other "
                      "results in the graph's layout: the quickest way to explore around it.",
     {"id": {"type": "string"}, "k": {"type": "integer"}}, ["id"]),
    ("get_proof", "A result's statement, derivations and proofs cut into steps, each with "
                  "the results it cites; premises the text never cites; sources and the "
                  "postulates it holds given.", {"id": {"type": "string"}}, ["id"]),
    ("trail", "The guided walk through one subject: ordered steps with explanatory prose.",
     {"subject": {"type": "string"}}, ["subject"]),
    ("digest", "A whole subject as Markdown in dependency order, with statements, "
               "premises and proofs, for reading in one go. level is formal, technical "
               "(default), lay or one-liner; notes are left out unless include_notes.",
     {"subject": {"type": "string"}, "level": {"type": "string"},
      "limit": {"type": "integer"}, "include_notes": {"type": "boolean"}}, ["subject"]),
    ("validate_draft", "Validate a draft entity.md (plus optional proof files and "
                       "check.py) against the store without changing it: layers 1 to 3 "
                       "(and 5 on request) of the rules a pull request is checked by. It never "
                       "runs check.py; `python -m tp check-one ID` does that locally.",
     {"entity_md": {"type": "string"}, "proofs": {"type": "object"},
      "check_py": {"type": "string"}, "layers": {"type": "string"}}, ["entity_md"]),
    ("propose_claim", "Validate and, if clean, file a draft as a proposal for "
                      "maintainer review.",
     {"entity_md": {"type": "string"}, "proofs": {"type": "object"},
      "check_py": {"type": "string"}, "author": {"type": "string"}}, ["entity_md"]),
    ("list_proposals", "Proposals waiting for review.", {}),
    ("generate_doc", "Generate and store a document from a recipe (YAML text), in this "
                     "copy of the repository.",
     {"recipe_yaml": {"type": "string"}}, ["recipe_yaml"]),
    ("regenerate_doc", "Regenerate a stored document from its last version.",
     {"doc_id": {"type": "string"}}, ["doc_id"]),
]


# which tools each mode offers: the hosted endpoint only reads; the old proposal queue is the
# maintainer's own (pull requests are the way in from outside)
WRITING = {"generate_doc", "regenerate_doc"}
HEAVY = {"validate_draft"}                 # copies the whole store per call
MAINTAINER = {"propose_claim", "list_proposals"}


def offered(mode="local"):
    names = [t[0] for t in TOOLS]
    if mode == "read-only":
        return [n for n in names if n not in WRITING | HEAVY | MAINTAINER]
    if mode == "maintainer":
        return names
    return [n for n in names if n not in MAINTAINER]


def tool_list(mode="local"):
    keep = set(offered(mode))
    out = []
    for t in TOOLS:
        name, desc, props = t[0], t[1], t[2]
        if name not in keep:
            continue
        req = t[3] if len(t) > 3 else []
        writes = name in WRITING | {"propose_claim"}
        out.append({"name": name, "description": desc,
                    "inputSchema": {"type": "object", "properties": props, "required": req},
                    # clients use these to decide what needs the user's confirmation: ChatGPT asks
                    # before every call to a tool not marked read-only
                    "annotations": {"readOnlyHint": not writes, "destructiveHint": False,
                                    "idempotentHint": not writes, "openWorldHint": False}})
    return out


INSTRUCTIONS = (
    "The Physics Graph: every result of the Transport Papers as an entry with its statement at four "
    "levels, its proof, the results it rests on and a machine check, written in geometric algebra. "
    "Call `conventions` first, before reading or writing anything: it explains the notation, the two "
    "imaginary units and how results are stored. Then `search_claims` or `list_subjects` to find a "
    "way in, `get_claim` / `get_proof` / `neighbourhood` to read and move around, and "
    "`list_open_problems` for what is open. Pitch explanations at the user's level. New results and "
    "corrections come in as pull requests to github.com/leon-machine/phys-graph (CONTRIBUTING.md).")

# prompts: one-click starting points that clients show to the user
PROMPTS = [
    ("explain-result", "Explain one result at your level, with what it rests on.",
     [("id", "the result's id, or a few words naming it", True),
      ("level", "beginner, student or expert", False)],
     "Call conventions first. Then find the result {id} (search_claims if it is not an id) and read it "
     "with get_claim and get_proof. Explain it to me at {level} level: what it says, why it matters, "
     "and the proof's idea. List what it rests on, marking which premises are proved and which are "
     "postulated or imported (holds_given), and say how it is machine-checked (check_command)."),
    ("audit-result", "Trace everything a result assumes and look for weak points.",
     [("id", "the result's id", True)],
     "Call conventions first. For the result {id}, read get_claim, get_proof and cone (past). Report "
     "every postulate and imported fact it holds given, any premise its proof lists but never cites, "
     "and any step that looks unjustified. Say which checks cover it and which parts are only "
     "checked at samples. Be specific and sceptical: the aim is to find errors, not to praise."),
    ("attack-open-problem", "Pick up an open problem and plan an attack on it.",
     [("id", "an open problem id (op.*), or leave empty to choose a tractable one", False)],
     "Call conventions first. If {id} is empty, call list_open_problems with difficulty tractable and "
     "pick one; otherwise call get_open_problem for {id}. Read the entities it starts from. Summarise "
     "what is known, then propose a concrete route: the result you would try to prove, in geometric "
     "algebra, what it would rest on, and the exact check.py you would write. Contributions go in as "
     "a pull request (CONTRIBUTING.md); validate_draft checks a draft first."),
    ("tour", "A guided tour of the graph for a newcomer.",
     [("interest", "what draws you: black holes, dark matter, the algebra, particles...", False)],
     "Call conventions first. Then give me a short tour of the Physics Graph, starting from the "
     "geometric algebra at its core and heading towards {interest}. Use list_subjects and trail to pick "
     "the path, show me five or six key results with their one-line statements, and tell me which "
     "are proved, which are assumed and which are predictions that data could refute."),
]


def prompt_list():
    return [{"name": n, "description": d,
             "arguments": [{"name": a, "description": ad, "required": r} for a, ad, r in args]}
            for n, d, args, _ in PROMPTS]


def prompt_get(name, arguments):
    for n, d, args, text in PROMPTS:
        if n == name:
            vals = {a: str((arguments or {}).get(a) or "") for a, _, _ in args}
            for a, _, r in args:
                if r and not vals[a]:
                    raise ValueError(f"prompt {name} needs {a}")
            vals.setdefault("level", "")
            if "level" in vals and not vals["level"]:
                vals["level"] = "an interested non-specialist's"
            if "interest" in vals and not vals["interest"]:
                vals["interest"] = "whatever is most surprising"
            return {"description": d, "messages": [
                {"role": "user", "content": {"type": "text", "text": text.format(**vals)}}]}
    raise ValueError(f"unknown prompt {name}")


def as_text(res):
    """Text results go out as text; the rest as compact JSON (no indentation: it roughly halves
    what an agent reads, and agents parse it as easily)."""
    if isinstance(res, str):
        return res
    return json.dumps(res, ensure_ascii=False, default=str)


def handle(lab, msg, mode="local"):
    mid, method, params = msg.get("id"), msg.get("method"), msg.get("params") or {}
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": mid, "result": {
            "protocolVersion": params.get("protocolVersion", PROTOCOL),
            "capabilities": {"tools": {"listChanged": False}, "prompts": {"listChanged": False}},
            "serverInfo": {"name": "physics-graph", "title": "Zero Divisors: Physics Graph",
                           "version": "1.0"},
            "instructions": INSTRUCTIONS}}
    if method in ("notifications/initialized", "notifications/cancelled"):
        return None
    if method == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": tool_list(mode)}}
    if method == "prompts/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"prompts": prompt_list()}}
    if method == "prompts/get":
        try:
            return {"jsonrpc": "2.0", "id": mid,
                    "result": prompt_get(params.get("name"), params.get("arguments"))}
        except ValueError as exc:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": str(exc)}}
    if method == "tools/call":
        name, args = params.get("name"), params.get("arguments") or {}
        try:
            if name not in offered(mode):
                raise ValueError(f"unknown tool {name}" if name not in {t[0] for t in TOOLS}
                                 else f"{name} is not offered by this server")
            res = getattr(lab, name)(**args)
            if name in ("propose_claim", "generate_doc", "regenerate_doc"):
                lab.reload()
            return {"jsonrpc": "2.0", "id": mid, "result": {
                "content": [{"type": "text", "text": as_text(res)}]}}
        except Exception as exc:
            return {"jsonrpc": "2.0", "id": mid, "result": {
                "content": [{"type": "text", "text": f"{type(exc).__name__}: {exc}"}],
                "isError": True}}
    if mid is None:
        return None
    return {"jsonrpc": "2.0", "id": mid,
            "error": {"code": -32601, "message": f"method not found: {method}"}}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", default="store")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--read-only", action="store_true", help="reading tools only (a public endpoint)")
    g.add_argument("--maintainer", action="store_true", help="also the local proposal queue")
    a = ap.parse_args(argv)
    mode = "read-only" if a.read_only else "maintainer" if a.maintainer else "local"
    lab = Lab(a.store)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            out = {"jsonrpc": "2.0", "id": None,
                   "error": {"code": -32700, "message": "parse error"}}
        else:
            out = handle(lab, msg, mode)
        if out is not None:
            sys.stdout.write(json.dumps(out) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
