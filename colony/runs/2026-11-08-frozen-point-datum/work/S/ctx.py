import os,re,sys,json
ROOT="/home/claude/phys-graph/store"
P=re.compile(sys.argv[1])
W=int(sys.argv[2]) if len(sys.argv)>2 else 160
ids=sys.argv[3:]
for e in ids:
    d=None
    for k in ("claims","objects","notes","predictions"):
        if os.path.isdir(f"{ROOT}/{k}/{e}"): d=f"{ROOT}/{k}/{e}"
    if not d: print("??",e); continue
    t=open(d+"/entity.md").read()
    title=re.search(r"^title: (.*)$",t,re.M).group(1)
    ver=re.search(r"^version: (.*)$",t,re.M).group(1)
    print(f"\n##### {e} v{ver}: {title}")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith((".md",".tex",".py")): continue
        txt=open(f"{d}/{fn}").read()
        if fn=="entity.md":
            # mark levels
            pass
        seen=0
        for m in P.finditer(txt):
            a=max(0,m.start()-W); b=min(len(txt),m.end()+W)
            # level name
            lvl=""
            if fn=="entity.md":
                hs=[x for x in re.finditer(r"^## (\S+)",txt[:m.start()],re.M)]
                lvl=hs[-1].group(1) if hs else "front"
            print(f"  [{fn}{':'+lvl if lvl else ''}] ..."+txt[a:b].replace("\n"," ")+"...")
            seen+=1
            if seen>=6: print("   (more)"); break
