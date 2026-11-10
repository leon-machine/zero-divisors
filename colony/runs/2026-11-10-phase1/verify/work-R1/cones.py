import json, subprocess, sys
LAB = "/home/claude/phys-graph"
uses = {
 "certificate": ["synthesis.signed-directions-and-the-integer-clifford-algebra", "synthesis.division-gives-the-rationals", "synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product", "singularity.descent-parity-average"],
 "rationals": ["synthesis.signed-directions-and-the-integer-clifford-algebra", "synthesis.division-gives-the-rationals", "synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product", "synthesis.the-sign-is-the-rotor-at-infinity"],
 "three-party": ["synthesis.signed-directions-and-the-integer-clifford-algebra", "synthesis.division-gives-the-rationals", "synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product"],
 "signatures": ["synthesis.signed-directions-and-the-integer-clifford-algebra", "synthesis.blade-square-signs-f2-quadratic-form", "transport.classification-real-clifford-algebras"],
 "parity": ["synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product", "singularity.descent-parity-average"],
 "positivity": ["synthesis.signed-directions-and-the-integer-clifford-algebra", "synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product"],
}
cache = {}
def cone(i):
    if i not in cache:
        out = subprocess.run([sys.executable, LAB + "/colony/labcli.py", "cone", json.dumps({"id": i})], capture_output=True, text=True).stdout
        cache[i] = json.loads(out)
    return cache[i]
for k, ids in uses.items():
    allc = {}
    for i in ids:
        c = cone(i)
        items = c if isinstance(c, list) else c.get("past", c.get("cone", []))
        for it in items: allc[it["id"]] = it
    st = {}
    for it in allc.values(): st.setdefault((it["kind"], it["status"]), []).append(it["id"])
    print("==", k, "cone size", len(allc))
    for (kind, status), v in sorted(st.items()):
        show = v if status not in ("proved",) else v[:0]
        print("   ", kind, status, len(v), show[:40])
    hg = set()
    for i in ids:
        r = json.loads(subprocess.run([sys.executable, LAB + "/colony/labcli.py", "get_claim", json.dumps({"id": i})], capture_output=True, text=True).stdout)
        hg |= set(r["derived"].get("holds_given") or [])
    print("    holds_given inherited:", sorted(hg))
