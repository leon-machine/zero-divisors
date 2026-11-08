"""Restater T1 helpers: copy a stored entity into proposals/, bump its version with the
maintainer note, credit and amendment, and apply exact string edits (each must match once)."""
import os
import re
import shutil
import sys

LAB = "/home/claude/phys-graph"
RUN = "2026-11-08-frozen-point-datum"


def find_stored(eid):
    for sub in ("claims", "objects", "notes", "predictions", "questions"):
        p = os.path.join(LAB, "store", sub, eid)
        if os.path.isdir(p):
            return p
    raise SystemExit(f"{eid} not in store")


def start(eid):
    src = find_stored(eid)
    dst = os.path.join(LAB, "proposals", eid)
    if os.path.exists(dst):
        raise SystemExit(f"{dst} exists")
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
    return dst


def yq(s):
    return "'" + s.replace("'", "''") + "'"


def bump(eid, note, defect, evidence=None, kind="restatement"):
    """Version v -> v+1, maintainer note first under extraction, credit, amendment."""
    p = os.path.join(LAB, "proposals", eid, "entity.md")
    t = open(p, encoding="utf-8").read()
    head, sep, body = t[4:].partition("\n---\n")
    m = re.search(r"^version: (\d+)$", head, re.M)
    v = int(m.group(1))
    head = head[:m.start()] + f"version: {v + 1}" + head[m.end():]
    full_note = (f"Version {v} -> {v + 1}. Leon's decision of 8 November 2026 "
                 f"(op.frozen-point-rational-datum): " + note)
    mp = (f"  maintainer_pass_2026_11_08:\n    by: ai-maintainer-pass\n"
          f"    note: {yq(full_note)}\n")
    if re.search(r"^extraction:\n", head, re.M):
        head = re.sub(r"^extraction:\n", lambda _: "extraction:\n" + mp, head, count=1, flags=re.M)
    else:
        head = head.rstrip("\n") + "\nextraction:\n" + mp.rstrip("\n")
    # credit: append after the last item of the credit list
    cm = re.search(r"^credit:\n((?:[- ] .*\n)+)", head + "\n", re.M)
    entry = (f"- name: Claude Opus 5.5\n  role: restated with H as the rational datum\n"
             f"  version: {v + 1}\n  source: run {RUN}\n")
    am = (f"amendments:\n- version: {v + 1}\n  kind: {kind}\n  defect: {yq(defect)}\n"
          + (f"  evidence: {evidence}\n" if evidence else ""))
    if re.search(r"^amendments:\n", head, re.M):
        raise SystemExit("amendments already present: extend by hand")
    end = cm.end()
    head = head[:end] + entry + am + head[end:]
    open(p, "w", encoding="utf-8").write("---\n" + head.rstrip("\n") + "\n---\n" + body)
    return v, v + 1


def edit(eid, fname, pairs):
    p = os.path.join(LAB, "proposals", eid, fname)
    t = open(p, encoding="utf-8").read()
    for old, new in pairs:
        n = t.count(old)
        if n != 1:
            raise SystemExit(f"{eid}/{fname}: {n} matches for {old[:80]!r}")
        t = t.replace(old, new)
    open(p, "w", encoding="utf-8").write(t)


def style(eid):
    """House-style scan of the proposal's text files."""
    d = os.path.join(LAB, "proposals", eid)
    bad = []
    for f in os.listdir(d):
        if f.endswith((".md", ".tex", ".py")):
            t = open(os.path.join(d, f), encoding="utf-8").read()
            for pat in ("—", "honest", "load-bearing", "T1 ", "restater"):
                if pat in t:
                    bad.append((f, pat))
    return bad


H_BLOCK = '''

# The frozen point's datum: Lambda = 3H^2 (de Sitter) and Lambda = -3H'^2 (anti-de Sitter), H, H' rational,
# against Lambda = 6 and 7/3, where Lambda/3 = 2 and 7/9 are not rational squares.
DATUM_H = [F(1), F(1, 2), F(3, 7)]
DATUM_HP = [F(1), F(2, 5)]
DATUM_NOT_SQUARE = [F(6), F(7, 3)]


def {name}():
    """In Cl(2,4) (e0 of square 1, e1..e3 of square -1, n_O, n_inf null with <n_O, n_inf> = 1), I = n_inf + (Lambda/6) n_O
    and W = n_inf - (Lambda/6) n_O. With Lambda = 3 eps h^2 the unit e5 = W/h has Q(e5) = -eps, e0..e3, e5 is an
    orthogonal basis of I-perp with squares (1, -1, -1, -1, -eps), omega = e0 e1 e2 e3 e5 is central with
    omega^2 = eps (doubled Cl(1,4) for eps = 1, complexified Cl(2,3) for eps = -1) and the reversed form gives
    omega'^2 = -eps (Cl(4,1), Cl(3,2)). With Lambda/3 not a rational square, omega^2 = Lambda/3 on e0..e3, W, so no
    rational rescaling of W is a unit (the theorem synthesis.frozen-point-datum-is-h, (ii), (iii), (v)(e))."""
{premises}    sq = (1, -1, -1, -1, 1, -1)
    rev = tuple(-s for s in sq)
    n0 = GA.scal(F(1, 2), GA.sub(GA.gen(4), GA.gen(5)))
    ninf = GA.add(GA.gen(4), GA.gen(5))
    frame = [GA.gen(0), GA.gen(1), GA.gen(2), GA.gen(3)]
    ok = GA.dot(n0, ninf, sq) == 1 and GA.dot(n0, n0, sq) == 0 and GA.dot(ninf, ninf, sq) == 0

    def volume(vs, form):
        out = GA.sc(1)
        for v in vs:
            out = GA.mul(out, v, form)
        return out

    for eps, hs in ((1, DATUM_H), (-1, DATUM_HP)):
        for h in hs:
            lam = 3 * eps * h * h
            I = GA.add(ninf, GA.scal(lam / 6, n0))
            W = GA.sub(ninf, GA.scal(lam / 6, n0))
            basis = frame + [GA.scal(1 / h, W)]
            ok = ok and GA.dot(I, I, sq) == eps * h * h
            ok = ok and all(GA.dot(b, I, sq) == 0 for b in basis)
            gram = [[GA.dot(a, b, sq) for b in basis] for a in basis]
            ok = ok and gram == [[1, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, -1, 0],
                                 [0, 0, 0, 0, -eps]]
            om = volume(basis, sq)
            ok = ok and GA.eq(GA.mul(om, om, sq), GA.sc(eps)) and all(GA.commutes(om, b, sq) for b in basis)
            omr = volume(basis, rev)
            ok = ok and GA.eq(GA.mul(omr, omr, rev), GA.sc(-eps))
            if eps == 1:
                e = GA.scal(F(1, 2), GA.add(GA.sc(1), om))
                ok = ok and GA.eq(GA.mul(e, e, sq), e) and not GA.eq(e, GA.sc(1))
    for lam in DATUM_NOT_SQUARE:
        W = GA.sub(ninf, GA.scal(lam / 6, n0))
        om = volume(frame + [W], sq)
        d = lam / 3
        ok = ok and GA.eq(GA.mul(om, om, sq), GA.sc(d))
        p, q = d.numerator, d.denominator
        ok = ok and all(k * k != p * q for k in range(p * q + 1))
    GA.check("Lambda = 3 eps h^2: W/h is a unit of I-perp, omega^2 = eps (mirror -eps); Lambda = 6, 7/3: omega^2 = Lambda/3, no square", ok)
    assert ok is not False, "{name}"
    return ok
'''


def h_block(name, premises):
    pre = "".join(f'    premise("{p}")' + "\n" for p in premises)
    return H_BLOCK.replace("{name}", name).replace("{premises}", pre)


def add_check(eid, fn):
    p = os.path.join(LAB, "proposals", eid, "entity.md")
    t = open(p, encoding="utf-8").read()
    assert t.count("\nchecked_by:\n") == 1
    t = t.replace("\nchecked_by:\n", f"\nchecked_by:\n- kind: check\n  ref: check.py::{fn}\n", 1)
    open(p, "w", encoding="utf-8").write(t)
