"""Pages of the Physics Graph that need no JavaScript: for AI agents reading the web, for search
engines, and for anyone whose browser cannot run the main page.

Written by `python -m tp.site` beside index.html (and left out of git and of the preview
artifact's file list; the public host serves them):

  results/<id>.html     one page per result: title, status, the one-line, plain and formal
                        statements, what it holds given, what it rests on and what rests on it
                        (as links), its proofs, its checks with the command that runs them, and
                        its credit. Maths stays as LaTeX, typeset by MathJax where scripts run.
  results/index.html    every result, by subject.
  subjects/<id>.md      a whole subject in dependency order (the MCP `digest`), for reading in
                        one fetch.
  conventions.md        how the graph is written (store/conventions.md).
  open-problems.md      the curated open problems.
  llms.txt              what this is and where an AI should start (llmstxt.org).
  sitemap.xml, robots.txt   when site_url is set.
"""
import html
import os
import re
import shutil

from .checkone import command

H = html.escape
STATUS = {"proved": "Proved", "imported": "Imported from the literature", "postulate": "Postulate (assumed)",
          "defined": "Definition", "conjectured": "Conjecture", "refuted": "Refuted", "live": "Prediction (live)",
          "confirmed": "Prediction (confirmed)", "killed": "Prediction (killed)", "open": "Open question",
          "settled": "Settled question"}
EVIDENCE = {"pass": "machine-checked: its own exact check passes",
            "pass-legacy": "machine-checked by the paper's verify script",
            "proof-only": "a written proof, with no machine check",
            "fail": "a check fails", "none": "no check recorded", "unverified": "not checked here"}
FOLDERS = ("results", "subjects")
FILES = ("conventions.md", "open-problems.md", "llms.txt", "sitemap.xml", "robots.txt")


def _claim_html(text, titles):
    """Store LaTeX for an HTML page: \\claimref to links, a few text commands to tags, lists to
    lists, blank lines to paragraphs; the maths itself is left for MathJax."""
    if not text:
        return ""
    refs = {}

    def ref(m):
        rid = m.group(1).strip()
        key = f"\x00{len(refs)}\x00"
        refs[key] = (f'<a href="{H(rid)}.html">{H(titles.get(rid, rid))}</a>' if rid in titles
                     else H(rid))
        return key
    t = re.sub(r"\\claimref\s*\{([^{}]*)\}", ref, text)
    t = H(t, quote=False)
    t = re.sub(r"\\label\{[^{}]*\}", "", t)
    t = re.sub(r"\\(?:emph|textit)\{([^{}]*)\}", r"<em>\1</em>", t)
    t = re.sub(r"\\textbf\{([^{}]*)\}", r"<b>\1</b>", t)
    t = re.sub(r"\\cite[pt]?(?:\[([^\]]*)\])?\{([^{}]*)\}",
               lambda m: "[" + m.group(2).replace(",", ", ") + (", " + m.group(1) if m.group(1) else "") + "]", t)
    t = re.sub(r"\\begin\{(itemize|enumerate)\}", lambda m: "<ul>" if m.group(1) == "itemize" else "<ol>", t)
    t = re.sub(r"\\end\{(itemize|enumerate)\}", lambda m: "</ul>" if m.group(1) == "itemize" else "</ol>", t)
    t = re.sub(r"\\item(?:\[([^\]]*)\])?\s*", lambda m: "<li>" + (f"<b>{m.group(1)}</b> " if m.group(1) else ""), t)
    t = t.replace("~", "&nbsp;").replace("``", "&ldquo;").replace("''", "&rdquo;")
    paras = [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip()]
    out = "\n".join(p if p.startswith(("<ul>", "<ol>")) else f"<p>{p}</p>" for p in paras)
    for k, v in refs.items():
        out = out.replace(k, v)
    return out


def _claim_md(text, titles):
    return re.sub(r"\\claimref\s*\{([^{}]*)\}",
                  lambda m: (f"[{titles.get(m.group(1).strip(), m.group(1).strip())}]"
                             f"(../results/{m.group(1).strip()}.html)"), text or "")


def _mathjax(notation):
    import json
    mac = {}
    for k, v in (notation or {}).items():
        n = [int(x) for x in re.findall(r"#(\d)", str(v))]
        mac[k] = [v, max(n)] if n else v
    cfg = ('window.MathJax={tex:{inlineMath:[["$","$"],["\\\\(","\\\\)"]],displayMath:[["\\\\[","\\\\]"],["$$","$$"]],'
           'macros:' + json.dumps(mac).replace("<", "\\u003c") + '},svg:{fontCache:"global"}};')
    return (f"<script>{cfg}</script>"
            '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.js"></script>')


CSS = ("body{font:17px/1.6 Georgia,'Source Serif 4',serif;max-width:46em;margin:0 auto;padding:1.5em 16px 4em;"
       "color:#1d2330;background:#fbfaf7}a{color:#2f5bd3}h1{font-size:1.7em;line-height:1.25;margin:.2em 0 .4em}"
       "h2{font:600 1em/1.4 system-ui,sans-serif;text-transform:uppercase;letter-spacing:.06em;color:#5b6475;"
       "margin:2em 0 .5em}.meta,.nav,footer,.chips{font:14px/1.5 system-ui,sans-serif;color:#5b6475}"
       ".chips span{display:inline-block;border:1px solid #c9cfda;border-radius:99px;padding:0 .6em;margin:0 .3em .3em 0}"
       ".one{font-size:1.1em}.box{border-left:3px solid #c9cfda;padding:.1em 0 .1em 1em}"
       "code{font:14px ui-monospace,monospace;background:#eef0f4;padding:.1em .3em;border-radius:3px}"
       "li{margin:.2em 0}footer{margin-top:3em;border-top:1px solid #dde1e8;padding-top:1em}"
       "@media (prefers-color-scheme:dark){body{background:#0b0f16;color:#d9dee8}a{color:#8fb0ff}"
       "h2,.meta,.nav,footer,.chips{color:#9aa3b5}code{background:#1a2130}.box{border-color:#374055}}"
       "mjx-container{overflow-x:auto;overflow-y:hidden;max-width:100%}")


def _page(title, desc, body, canonical, mathjax):
    canon = f'<link rel="canonical" href="{H(canonical)}">' if canonical else ""
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<title>{H(title)} | Zero Divisors: Physics Graph</title>"
            f"<meta name=\"description\" content=\"{H(desc)}\">{canon}"
            f"<style>{CSS}</style>{mathjax}</head><body>{body}</body></html>")


def _list(ids, titles, empty="none"):
    ids = [x for x in ids if x in titles]
    if not ids:
        return f"<p>{empty}</p>"
    return "<ul>" + "".join(f'<li><a href="{H(x)}.html">{H(titles[x])}</a></li>' for x in ids) + "</ul>"


def write(site, lab, site_url="", mcp_url="", checks=None):
    """Write the pages into `site` from an MCP Lab (tp.mcp_server.Lab); returns how many results."""
    from .site import _display_title, _plain_tex
    st = lab.store
    checks = checks if checks is not None else lab.checks
    for d in FOLDERS:
        shutil.rmtree(os.path.join(site, d), ignore_errors=True)
        os.makedirs(os.path.join(site, d))
    for f in FILES:
        if os.path.exists(os.path.join(site, f)):
            os.remove(os.path.join(site, f))
    base = site_url or ""
    graph = site_url or "../index.html"
    ents = {x: e for x, e in st.entities.items() if e.kind != "note"}
    titles = {x: _display_title(e.title) or x for x, e in ents.items()}
    subjects = {s["id"]: s for s in st.subjects}
    mj = _mathjax(st.notation)
    by_subject = {}
    for eid, e in sorted(ents.items()):
        by_subject.setdefault(e.meta.get("subject"), []).append(eid)
        lv = {k: (e.levels.get(k) or "").strip() for k in ("one-liner", "lay", "technical", "formal")}
        lv = {k: ("" if v == "pending" else v) for k, v in lv.items()}
        subj = subjects.get(e.meta.get("subject"), {})
        prem = sorted({p.split("@")[0] for d in e.derivations() if isinstance(d, dict)
                       for p in (d.get("uses") or []) + (d.get("assumes") or [])})
        users = sorted(lab.direct_users.get(eid, []))
        holds = lab.conds.get(eid, [])
        ev = checks.get(eid)
        kinds = [c for c in (e.meta.get("checked_by") or []) if isinstance(c, dict)]
        credit = [c for c in (e.meta.get("credit") or []) if isinstance(c, dict)]
        status = STATUS.get(e.status, e.status)
        parts = [
            f'<p class="nav"><a href="index.html">All results</a> · '
            f'<a href="../subjects/{H(str(e.meta.get("subject")))}.md">{H(subj.get("title", ""))} (whole subject)</a> · '
            f'<a href="{H(graph)}#{H(eid)}">Open in the Physics Graph</a></p>',
            f"<h1>{H(titles[eid])}</h1>",
            f'<p class="chips"><span>{H(status)}</span>'
            + (f"<span>{H(EVIDENCE.get(ev, ev))}</span>" if ev and ev not in ("none", "unverified") else "")
            + f'<span>id <code>{H(eid)}</code>, version {e.version}</span></p>']
        if lv["one-liner"]:
            parts.append(f'<div class="one">{_claim_html(lv["one-liner"], titles)}</div>')
        if holds:
            parts.append("<h2>Holds given</h2><p>These postulates or imported facts sit somewhere "
                         "beneath it; it holds if they do.</p>" + _list(holds, titles))
        if lv["lay"]:
            parts.append("<h2>In plain words</h2>" + _claim_html(lv["lay"], titles))
        if lv["formal"]:
            parts.append('<h2>Statement</h2><div class="box">' + _claim_html(lv["formal"], titles) + "</div>")
        for name, text in e.proofs.items():
            if text.strip():
                parts.append(f"<h2>Proof{'' if name == 'main' else ' (' + H(name) + ')'}</h2>"
                             + _claim_html(text.strip(), titles))
        if e.meta.get("imported_from"):
            parts.append(f"<h2>Source</h2><p>{H(str(e.meta.get('imported_from')))}</p>")
        parts.append("<h2>Rests on</h2>" + _list(prem, titles))
        parts.append("<h2>Used by</h2>" + _list(users, titles))
        if kinds:
            rows = []
            for c in kinds:
                if c.get("kind") == "check":
                    rows.append(f"<li>exact check <code>{H(str(c.get('ref')))}</code></li>")
                elif c.get("kind") == "legacy":
                    rows.append(f"<li>the paper's verify script <code>{H(str(c.get('script')))}</code></li>")
                elif c.get("kind") == "proof":
                    rows.append("<li>a written proof</li>")
                else:
                    rows.append(f"<li>{H(str(c.get('kind')))}</li>")
            parts.append("<h2>Checks</h2><ul>" + "".join(rows) + "</ul><p>Run them on a clone of the "
                         f"repository: <code>{H(command(eid))}</code></p>")
        if credit:
            parts.append("<h2>Credit</h2><p>" + "; ".join(
                H(c.get("name", "")) + f" ({H(c.get('role', ''))}"
                + (f", version {c['version']}" if c.get("version") else "") + ")" for c in credit) + ".</p>")
        parts.append("<footer>Zero Divisors: Physics Graph. Results are licensed CC BY 4.0. "
                     '<a href="https://github.com/leon-machine/zero-divisors">Source and contributions</a> · '
                     '<a href="../llms.txt">For AI agents</a></footer>')
        desc = _plain_tex(lv["one-liner"] or titles[eid])[:280]
        canon = f"{base}results/{eid}.html" if base else ""
        with open(os.path.join(site, "results", eid + ".html"), "w", encoding="utf-8") as fh:
            fh.write(_page(titles[eid], desc, "\n".join(parts), canon, mj))
    # index of every result
    sec = []
    for s in st.subjects:
        ids = by_subject.get(s["id"]) or []
        if not ids:
            continue
        sec.append(f'<h2 id="{H(s["id"])}">{H(s.get("title", s["id"]))}</h2>'
                   f'<p class="meta">{H(s.get("about", ""))} · <a href="../subjects/{H(s["id"])}.md">'
                   "the whole subject in one file</a></p>" + _list(ids, titles))
    body = ('<p class="nav"><a href="../index.html">The Physics Graph</a> · '
            '<a href="../llms.txt">For AI agents</a></p><h1>Every result, by subject</h1>'
            f"<p>{len(ents)} results of the Transport Papers, each with its statement, proof, premises "
            "and checks.</p>" + "".join(sec))
    with open(os.path.join(site, "results", "index.html"), "w", encoding="utf-8") as fh:
        fh.write(_page("Every result", "Every result of the Physics Graph, by subject.", body,
                       f"{base}results/index.html" if base else "", mj))
    # a whole subject per file, and the conventions
    for s in st.subjects:
        if not by_subject.get(s["id"]):
            continue
        md = lab.digest(s["id"], "technical", limit=100000)
        head = (f"# {s.get('title', s['id'])}\n\n{s.get('about', '')}\n\nPart of the Physics Graph "
                "(Zero Divisors). Results in dependency order: each one's statement, what it rests on "
                "and its proof. Maths is LaTeX; the macros are listed in the conventions "
                "(../conventions.md). Each result's own page is results/<id>.html.\n\n")
        with open(os.path.join(site, "subjects", s["id"] + ".md"), "w", encoding="utf-8") as fh:
            fh.write(head + _claim_md(md, titles))
    shutil.copyfile(os.path.join(st.root, "conventions.md"), os.path.join(site, "conventions.md"))
    # open problems
    ops = st.open_problems or []
    lines = ["# Open problems", "", "What the Physics Graph does not yet settle. Each says why it matters, "
             "what is known, where to start and what would settle it. Work on one goes in as a pull request "
             "(https://github.com/leon-machine/zero-divisors, CONTRIBUTING.md).", ""]
    for op in ops:
        lines += [f"## {op.get('title', op.get('id'))}", "",
                  f"`{op.get('id')}` · {op.get('area', '')} · {op.get('kind', '')} · "
                  f"{op.get('difficulty', '')} · {op.get('status', '')}", ""]
        for k, label in (("statement", ""), ("why", "Why it matters"), ("known", "What is known"),
                         ("routes", "Routes of attack"), ("settles", "What would settle it")):
            v = op.get(k)
            if not v:
                continue
            if isinstance(v, list):
                v = "\n".join(f"- {x}" for x in v)
            lines += [(f"**{label}.** " if label else "") + _claim_md(str(v).strip(), titles), ""]
        if op.get("entities"):
            lines += ["Start from: " + ", ".join(f"[{titles.get(x, x)}](results/{x}.html)"
                                                 for x in op["entities"]), ""]
    with open(os.path.join(site, "open-problems.md"), "w", encoding="utf-8") as fh:
        fh.write(_claim_md("\n".join(lines), titles).replace("](../results/", "](results/"))
    # llms.txt
    u = base
    connect = (f"- Remote MCP server (no install): {mcp_url}. Add it to your AI as a remote MCP server "
               "(in claude.ai, a custom connector), then call `conventions` first.\n" if mcp_url else "")
    llms = [
        "# Zero Divisors: Physics Graph", "",
        "> Every result of the Transport Papers (a research programme reading general relativity and "
        "quantum theory through the zero divisors of Clifford algebras) as one entry: its statement at "
        "four levels, its proof, the results it rests on, pinned to versions, and an exact machine check. "
        "Written in geometric algebra. Not yet peer reviewed; the papers on Zenodo are the version of record.", "",
        "Read `conventions.md` before anything else: it explains the notation, the two imaginary units and "
        "how results are stored. Each result page says what the result holds given (its postulates and "
        "imported facts), so trace those before relying on a result.", "",
        "## Connect an AI", "",
        connect + "- Local MCP server (needed to contribute): clone https://github.com/leon-machine/zero-divisors, "
        "`pip install -r requirements.txt`, run `python -m tp.mcp_server --store store` as a stdio server.",
        "- Corrections and new results come in as pull requests; CONTRIBUTING.md has the rules.",
        "- The files below are the same content for reading only, a whole subject at a time. An MCP server is "
        "better for exploring: it can search the graph, trace what a result rests on and move between "
        "neighbouring results, and some subject files are large.", "",
        "## Start here", "",
        f"- [Conventions]({u}conventions.md): how the graph is written",
        f"- [Every result, by subject]({u}results/index.html)",
        f"- [Open problems]({u}open-problems.md): what is not yet settled", "",
        "## Subjects (each a whole subject in dependency order)", ""]
    for s in st.subjects:
        if by_subject.get(s["id"]):
            llms.append(f"- [{s.get('title', s['id'])}]({u}subjects/{s['id']}.md): "
                        f"{s.get('about', '')} ({len(by_subject[s['id']])} results)")
    llms += ["", "## Optional", "",
             "- [The papers on Zenodo](https://zenodo.org/communities/transport-papers)",
             "- [Source repository](https://github.com/leon-machine/zero-divisors)", ""]
    with open(os.path.join(site, "llms.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(llms))
    if site_url:
        urls = ([site_url] + [site_url + p for p in ("principle.html", "ga.html", "singularity.html")]
                + [site_url + "results/index.html"]) + [f"{site_url}results/{x}.html" for x in sorted(ents)]
        with open(os.path.join(site, "sitemap.xml"), "w", encoding="utf-8") as fh:
            fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                     + "".join(f"<url><loc>{H(x)}</loc></url>\n" for x in urls) + "</urlset>\n")
        with open(os.path.join(site, "robots.txt"), "w", encoding="utf-8") as fh:
            fh.write(f"User-agent: *\nAllow: /\nSitemap: {site_url}sitemap.xml\n")
    return len(ents)
