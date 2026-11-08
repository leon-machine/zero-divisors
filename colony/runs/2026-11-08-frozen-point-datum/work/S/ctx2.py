import os,re,sys
ROOT="/home/claude/phys-graph/store"
P=re.compile(r"\\sqrt\s*\{[^{}]*(\\Lambda|3/|\\ell|Q\(I)|\\sqrt\{\|\\Lambda|sqrt\((Lam|lam|3)|\\kappa_\{?\\Lambda|kappa_L|R_\{?h\}?\b|S[Oo]\(\s*(1,\s*4|4,\s*1|2,\s*3|3,\s*2)\)|\\mathfrak\{so\}\(\s*(1,\s*4|2,\s*3)|e_\{?W\}?|unit (ambient )?boost|bifurcation sphere|null eigen|de Sitter radius|\\ell\s*=|Lambda\s*=\s*3\s*H|3H\^\{?2|H\s*=\s*\\sqrt|Cl\(\s*(1,\s*4|4,\s*1)\)|\\langle\s*[-+]?\s*\\?t?frac(13|\{1\}\{3\})|I_\{?\\Lambda\}?/|/\\sqrt\{Q|\\hat\{?I")
W=int(os.environ.get("W","110"))
for e in sys.argv[1:]:
    d=None
    for k in ("claims","objects","notes","predictions"):
        if os.path.isdir(f"{ROOT}/{k}/{e}"): d=f"{ROOT}/{k}/{e}"
    t=open(d+"/entity.md").read()
    title=re.search(r"^title: (.*)$",t,re.M).group(1); ver=re.search(r"^version: (.*)$",t,re.M).group(1)
    st=re.search(r"^status: (.*)$",t,re.M); st=st.group(1) if st else ""
    print(f"\n##### {e} v{ver} [{st}]: {title}")
    parts=[]
    body=t.split("\n---\n",1)[-1] if t.startswith("---") else t
    for m in re.finditer(r"^## (\S+)\n(.*?)(?=^## |\Z)",body,re.M|re.S): parts.append((m.group(1),m.group(2)))
    if not parts: parts=[("body",body)]
    for fn in sorted(os.listdir(d)):
        if fn.endswith((".tex",".py")) and not fn.startswith("orig"): parts.append((fn,open(f"{d}/{fn}").read()))
    for name,txt in parts:
        hits=list(P.finditer(txt))
        if not hits: continue
        out=[]
        last=-999
        for m in hits:
            if m.start()<last+W: continue
            last=m.start()
            out.append(txt[max(0,m.start()-W):m.end()+W].replace("\n"," "))
            if len(out)>=3: break
        print(f"  [{name}] ({len(hits)}) "+" || ".join(out))
