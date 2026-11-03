"""Resolve the \\ref and \\eqref that store text still carries.

Store text keeps a paper's own cross-references where the extractor could not
turn them into \\claimref (remarks, sections, tables, equations stated in the
running text). The registry store/labels.yaml (written by tp.notes) says what
now carries each label. ``resolve`` rewrites a text for a reader that has no
paper in front of them:

* a label carried by an entity becomes \\claimref{id};
* "Section 4.4" becomes the section's title, in quotation marks;
* an equation of the running text is written out where it is short enough;
* a table becomes a pointer to the result it accompanies;
* a figure becomes "a figure of the original" (figures are not in the store).

The function is used by the document generator and by the site, so both read
the same way.
"""
from __future__ import annotations

import os
import re

import yaml

REF_ANY = re.compile(
    r"(?P<pre>(?:Sections?|Subsections?|Secs?\.|Appendix|Appendices|Tables?|Figures?|Figs?\."
    r"|Remarks?|Rems?\.|Examples?|Exs?\.|Equations?|Eqs?\.|Theorem|Proposition|Lemma|Corollary"
    r"|Definition|Fact|Conjecture|Premise|Observation)\s*~?\s*|\\S\s*~?\s*)?"
    r"\\(?P<cmd>ref|eqref|cref|Cref|autoref)\{(?P<labs>[^}]+)\}")
SHORT_DISPLAY = 140
RESULT_WORD = re.compile(r"^(Remarks?|Rems?\.|Examples?|Exs?\.|Theorem|Proposition|Lemma|"
                         r"Corollary|Definition|Fact|Conjecture|Premise|Observation)$")


def load(store_root):
    p = os.path.join(store_root, "labels.yaml")
    if not os.path.exists(p):
        return {}
    return yaml.safe_load(open(p, encoding="utf-8")) or {}


def _q(title):
    return "``" + title.rstrip(".") + "''"


def resolve(text, code, registry, entities=None, plain=False):
    """-> text with every resolvable reference of paper `code` rewritten.

    entities: ids that exist (a \\claimref is written only for these).
    plain:    True for the site, where quotation marks are typographic.
    """
    if not text or not code or not registry:
        return text
    lq, rq = ("\u201c", "\u201d") if plain else ("``", "''")

    def quote(t):
        return lq + t.rstrip(".") + rq

    def one(lab, cmd, pre):
        rec = registry.get(f"{code}:{lab.strip()}")
        if not rec:
            return None
        ent = rec.get("entity")
        if ent and (entities is None or ent in entities):
            return (pre or "") + "\\claimref{" + ent + "}"
        if "section" in rec:
            return "the section " + quote(rec["section"])
        if "display" in rec:
            d = re.sub(r"\\(?:tag|label)\*?\{[^}]*\}|\\nonumber|\\notag", "", rec["display"])
            d = re.sub(r"(?:\s|\\[,;!]|[.,;])+$", "", d)
            if len(d) <= SHORT_DISPLAY and "\\\\" not in d and "\\begin" not in d:
                return ("the relation " if pre else "") + "$" + d + "$"
            near = rec.get("near")
            if near and (entities is None or near in entities):
                return "the relation displayed with \\claimref{" + near + "}"
            return "a relation of the original text"
        if "table" in rec:
            near = rec.get("near")
            if near and (entities is None or near in entities):
                return "the table accompanying \\claimref{" + near + "}"
            return "a table of the original"
        if rec.get("kind") == "figure" or lab.startswith("fig:"):
            return "a figure of the original"
        return None

    def sub(m):
        pre, cmd = m.group("pre"), m.group("cmd")
        outs = [one(l, cmd, None) for l in m.group("labs").split(",")]
        if any(o is None for o in outs):
            return m.group(0)
        joined = outs[0] if len(outs) == 1 else ", ".join(outs[:-1]) + " and " + outs[-1]
        if not pre:
            return joined
        word = pre.strip().rstrip("~").strip()
        if RESULT_WORD.match(word) and all(o.startswith("\\claimref") for o in outs):
            return pre + joined        # "Remark 12", "Theorem 3"
        if all(o.startswith("\\claimref") for o in outs):
            return "the result " + joined if len(outs) == 1 else "the results " + joined
        return joined                  # the section, table, relation or figure names itself
    out = REF_ANY.sub(sub, text)
    # a section sign left in front of words ("\S\S\ref{a}--\ref{b}" ranges)
    out = re.sub(r"(?:\\S)+~?\s*(?=the sections?\b|the results?\b|a figure|the table)", "", out)
    # "(the relation $...$)" reads oddly inside parentheses: drop "the relation"
    out = re.sub(r"\(\s*the relation (\$[^$]+\$)\s*\)", r"(\1)", out)
    return out
