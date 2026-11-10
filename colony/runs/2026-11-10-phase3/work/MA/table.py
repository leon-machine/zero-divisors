import json, collections, re, os, sys
g=json.load(open('build/graph.json'))
N={n['id']:n for n in g['nodes']}
P=[l.split(' |')[0] for l in open(sys.argv[1]) if 'subject: dark-matter' in l]
DEP={'uses','assumes','founded_on','specialises','derived_from'}
inc=collections.defaultdict(list)
for e in g['edges']: inc[e['dst']].append(e)
def cone(p):
    seen=set(); st=[p]
    while st:
        x=st.pop()
        for e in inc[x]:
            if e['kind'] in DEP and e['src'] not in seen:
                seen.add(e['src']); st.append(e['src'])
    return seen
# text mentions
ment=collections.defaultdict(set)
for d in os.listdir('store/claims'):
    f='store/claims/%s/entity.md'%d
    if not os.path.exists(f): continue
    t=open(f).read()
    for m in re.findall(r'claimref\{([^}]+)\}',t): ment[m].add(d)
out={}
for i,p in enumerate(P,1):
    dirc=collections.defaultdict(list)
    for e in inc[p]: dirc[e['kind']].append(e['src'])
    c=cone(p)
    cl=[x for x in c if N[x]['kind']=='claim']
    outs=[x for x in c if N[x].get('subject')!='dark-matter']
    dep_direct=set(sum((dirc[k] for k in DEP),[]))
    m_only=sorted(ment[p]-dep_direct-{p})
    out[p]=dict(direct={k:sorted(v) for k,v in dirc.items()},cone=sorted(c),outside=sorted(outs),mention_only=m_only)
    print(f"\n#{i} {p} v{N[p]['version']}")
    for k,v in dirc.items(): print('  ',k,len(v),v if len(v)<=8 else v[:8]+['...'])
    print('   cone',len(c),'claims',len(cl),'outside-subject',len(outs), collections.Counter(N[x].get('subject') for x in outs).most_common(6))
    print('   mention-only (claimref, no dep edge):',len(m_only),m_only[:6])
json.dump(out,open(os.path.dirname(__file__)+'/table.json','w'),indent=1)
