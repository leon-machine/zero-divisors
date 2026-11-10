import json,sys,collections
g=json.load(open('/home/claude/phys-graph/build/graph.json'))
N={n['id']:n for n in g['nodes']}
DEP={'uses','assumes','founded_on','specialises','derived_from'}
out=collections.defaultdict(set); inn=collections.defaultdict(set); allk=collections.Counter()
for e in g['edges']:
    allk[e['kind']]+=1
    if e['kind'] in DEP:
        out[e['src']].add(e['dst']); inn[e['dst']].add(e['src'])
def cone(r,adj):
    seen=set(); st=[r]
    while st:
        x=st.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y); st.append(y)
    return seen
past=lambda r:cone(r,out); fut=lambda r:cone(r,inn)
def edges(i):
    return [(e['kind'],e['dst']) for e in g['edges'] if e['src']==i],[(e['kind'],e['src']) for e in g['edges'] if e['dst']==i]
