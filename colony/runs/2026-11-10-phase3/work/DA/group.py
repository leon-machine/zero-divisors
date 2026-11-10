import json, os, re, glob, collections
LAB="/home/claude/phys-graph"; os.chdir(LAB)
c=json.load(open("colony/runs/2026-11-10-phase3/work/DA/cones_future.json"))
def text(i):
    for d in ("claims","predictions","notes","objects","quantities","questions"):
        p=f"store/{d}/{i}/entity.md"
        if os.path.exists(p): return open(p).read()
    return ""
FS="synthesis.field-space-premise-parallel-frozen-point"
# every entity naming FS by claimref
named=[]
for p in glob.glob("store/*/*/entity.md"):
    t=open(p).read()
    if FS in t: named.append(p.split("/")[2])
print("entities naming FS:",len(named))
for n in sorted(named): 
    t=text(n); m=re.search(r"^status: (.*)$",t,re.M); s=re.search(r"^subject: (.*)$",t,re.M)
    ass = "ASSUMES" if re.search(r"assumes:\n(\s+- .*\n)*\s+- "+re.escape(FS),t) else ""
    uses = "USES" if re.search(r"uses:\n(\s+- .*\n)*\s+- "+re.escape(FS),t) else ""
    print("  ",n,"|",s and s.group(1),"|",m and m.group(1),ass,uses)
fp=c["dark-energy.frozen-point-makes-stelle-west-vector"]; geo=c["dark-energy.imported-frozen-point-geometry"]
ids={x[0]:x for x in fp}; 
for x in geo: ids.setdefault(x[0],x)
rows=[]
for i,x in ids.items():
    t=text(i); body=t.split("## formal",1)[-1]
    fl=[]
    if FS in t or "(FS)" in t: fl.append("FS")
    if re.search(r"w = -1|w \\neq -1",t): fl.append("w")
    if re.search(r"Henneaux|promot",t): fl.append("HT")
    if re.search(r"\bN = M_|N\^\{?2|\\pi N|registered input|number \$N\$",body): fl.append("N")
    if re.search(r"de Sitter",body): fl.append("dS")
    if re.search(r"Friedmann|FLRW|cosmolog",body): fl.append("cosmo")
    infp = i in {y[0] for y in fp}
    tt=re.search(r"^title: (.*)$",t,re.M)
    rows.append((x[1],i,x[2],"FP" if infp else "geo-only",",".join(fl),tt.group(1)[:70] if tt else ""))
rows.sort()
with open("colony/runs/2026-11-10-phase3/work/DA/cone_table.tsv","w") as f:
    for r in rows: f.write("\t".join(map(str,r))+"\n")
print(len(rows))
cnt=collections.Counter((r[0],r[3]) for r in rows); print(cnt)
