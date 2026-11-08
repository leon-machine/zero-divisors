import os,re,sys
ROOT="/home/claude/phys-graph/store"
P=re.compile(os.environ.get("PAT",r"\\sqrt|sqrt\("))
W=int(os.environ.get("W","70")); MAX=int(os.environ.get("MAX","3"))
LV=os.environ.get("LV","formal,technical,one-liner,lay,body").split(",")
for e in sys.argv[1:]:
    d=None
    for k in ("claims","objects","notes","predictions"):
        if os.path.isdir(f"{ROOT}/{k}/{e}"): d=f"{ROOT}/{k}/{e}"
    t=open(d+"/entity.md").read()
    title=re.search(r"^title: (.*)$",t,re.M).group(1); ver=re.search(r"^version: (.*)$",t,re.M).group(1)
    st=re.search(r"^status: (.*)$",t,re.M); st=st.group(1) if st else ""
    print(f"\n##### {e} v{ver} [{st}]: {title}")
    body=t.split("\n---\n",1)[-1]
    parts=[(m.group(1),m.group(2)) for m in re.finditer(r"^## (\S+)\n(.*?)(?=^## |\Z)",body,re.M|re.S)] or [("body",body)]
    if "check" in LV and os.path.exists(d+"/check.py"): parts.append(("check",open(d+"/check.py").read()))
    for name,txt in parts:
        if name not in LV and name!="check": continue
        hits=list(P.finditer(txt))
        if not hits: continue
        out=[];last=-999
        for m in hits:
            if m.start()<last+W: continue
            last=m.start(); out.append(txt[max(0,m.start()-W):m.end()+W].replace("\n"," "))
            if len(out)>=MAX: break
        print(f"  [{name}] ({len(hits)}) "+" || ".join(out))
