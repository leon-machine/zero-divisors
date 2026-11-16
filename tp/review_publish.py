"""Where a finished review goes: the open review log first, then a pull request on the Physics
Graph (docs/REVIEWS.md).

The log entry is written before the maintainer can see the review, so nothing submitted can be
quietly dropped: merging the pull request only decides what shows on the result page.

  LocalPublisher   writes both into local folders (tests, and a trial run on a clone)
  GitHubPublisher  the open review log is a repository only the review server writes to: the
                   entry is committed straight to its default branch. The signed part goes to a
                   new branch of the Physics Graph and a pull request is opened. It uses the
                   GitHub REST API with a token, so the server needs neither git nor a clone.
"""
from __future__ import annotations

import base64
import json
import os
import urllib.error
import urllib.request

import yaml


def entry_json(entry: dict) -> str:
    return json.dumps(entry, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def signed_yaml(signed: dict) -> str:
    return yaml.safe_dump(signed, sort_keys=True, allow_unicode=True)


def _title(entry: dict) -> str:
    s = entry["signed"]
    who = entry.get("by") or entry.get("orcid")
    if s["kind"] == "review":
        what = "endorsement" if s.get("verdict") == "endorse" else "objection"
        return f"Review: {what} of {s['result']} v{s['version']} by {who}"
    return f"Review record: {s['kind']} on {s['result']} by {who}"


class LocalPublisher:
    def __init__(self, store_root: str, log_dir: str):
        self.store_root, self.log_dir = store_root, log_dir

    def publish(self, h: str, entry: dict) -> dict:
        os.makedirs(os.path.join(self.log_dir, "records"), exist_ok=True)
        log_path = os.path.join(self.log_dir, "records", h + ".json")
        with open(log_path, "w", encoding="utf-8") as fh:
            fh.write(entry_json(entry))
        folder = os.path.join(self.store_root, "reviews", entry["signed"]["result"])
        os.makedirs(folder, exist_ok=True)
        rec_path = os.path.join(folder, h + ".yaml")
        with open(rec_path, "w", encoding="utf-8") as fh:
            fh.write(signed_yaml(entry["signed"]))
        return {"log": log_path, "record": rec_path, "pull_request": None}


class GitHubError(RuntimeError):
    pass


class GitHubPublisher:
    def __init__(self, token: str, graph_repo: str, log_repo: str, base: str = "main",
                 api: str = "https://api.github.com", opener=None):
        self.token, self.graph, self.log, self.base, self.api = (token, graph_repo, log_repo,
                                                                 base, api.rstrip("/"))
        self._open = opener or urllib.request.urlopen

    def _call(self, method, path, body=None):
        req = urllib.request.Request(
            f"{self.api}{path}", method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={"Authorization": f"Bearer {self.token}",
                     "Accept": "application/vnd.github+json",
                     "X-GitHub-Api-Version": "2022-11-28",
                     "User-Agent": "physics-graph-review"})
        try:
            with self._open(req, timeout=30) as r:
                text = r.read().decode("utf-8")
                return json.loads(text) if text else {}
        except urllib.error.HTTPError as exc:
            raise GitHubError(f"{method} {path}: {exc.code} {exc.read()[:300]!r}")

    def _put_file(self, repo, path, text, message, branch=None):
        body = {"message": message, "content": base64.b64encode(text.encode()).decode()}
        if branch:
            body["branch"] = branch
        return self._call("PUT", f"/repos/{repo}/contents/{path}", body)

    def publish(self, h: str, entry: dict) -> dict:
        signed = entry["signed"]
        title = _title(entry)
        # 1. the open review log, before anyone can decide anything about it
        log = self._put_file(self.log, f"records/{h}.json", entry_json(entry), title)
        # 2. the signed part on a branch of the Physics Graph, and a pull request
        sha = self._call("GET", f"/repos/{self.graph}/git/ref/heads/{self.base}")["object"]["sha"]
        branch = f"review/{h[:16]}"
        self._call("POST", f"/repos/{self.graph}/git/refs",
                   {"ref": f"refs/heads/{branch}", "sha": sha})
        self._put_file(self.graph, f"store/reviews/{signed['result']}/{h}.yaml",
                       signed_yaml(signed), title, branch=branch)
        pr = self._call("POST", f"/repos/{self.graph}/pulls", {
            "title": title, "head": branch, "base": self.base,
            "body": (f"A review record submitted through the review service.\n\n"
                     f"- record: `{h}`\n- result: `{signed['result']}` version {signed['version']}\n"
                     f"- open review log: {(log.get('content') or {}).get('html_url', '')}\n\n"
                     "Merging decides only whether it shows on the result page; it is in the open "
                     "review log either way. `tp reviews check` verifies ORCID's signature.")})
        return {"log": (log.get("content") or {}).get("html_url"), "record": None,
                "pull_request": pr.get("html_url")}
