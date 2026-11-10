import os, re, sys, json
root = "/home/claude/phys-graph/store/claims"
pats = [r"M_\{P\}\s*/\s*H", r"the-number-n", r"G\\Lambda", r"G\s*\\Lambda", r"\\pi N\^\{2\}", r"N\^\{-2\}", r"v/H", r"N\s*=\s*M_", r"N \\approx", r"10\^\{61\}", r"10\^\{122\}", r"10\^\{60\}", r"10\^\{120\}"]
rows = []
for d in sorted(os.listdir(root)):
    p = os.path.join(root, d, "entity.md")
    if not os.path.exists(p): continue
    t = open(p).read()
    head, _, body = t.partition("\n## formal")
    st = re.search(r"^status:\s*(\S+)", head, re.M)
    tag = "the-number-n" in head
    formal = body.split("\n## technical")[0]
    hits = [q for q in pats if re.search(q, formal)]
    if tag or hits:
        rows.append((d, st.group(1) if st else "?", tag, len(hits)))
json.dump(rows, open("/home/claude/phys-graph/colony/runs/2026-11-10-phase2/work/NA/n_mentions.json", "w"), indent=0)
print(len(rows))
from collections import Counter
print(Counter(r[1] for r in rows))
for r in rows: print(r[1][:5], "T" if r[2] else " ", r[3], r[0])
