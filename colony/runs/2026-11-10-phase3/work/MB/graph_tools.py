"""Light graph reader over build/graph.json (read only). Used for cones of the dark-matter postulates."""
import json, collections, sys
LAB = '/home/claude/phys-graph'
G = json.load(open(LAB + '/build/graph.json'))
N = {n['id']: n for n in G['nodes']}
OUT = collections.defaultdict(list)   # src -> (kind, dst)   src depends on dst
IN = collections.defaultdict(list)    # dst -> (kind, src)
for e in G['edges']:
    OUT[e['src']].append((e['kind'], e['dst']))
    IN[e['dst']].append((e['kind'], e['src']))
DEP = ('uses', 'assumes')
def past(x, kinds=DEP):
    seen = set(); st = [x]
    while st:
        a = st.pop()
        for k, b in OUT[a]:
            if k in kinds and b not in seen:
                seen.add(b); st.append(b)
    return seen
def future(x, kinds=DEP):
    seen = set(); st = [x]
    while st:
        a = st.pop()
        for k, b in IN[a]:
            if k in kinds and b not in seen:
                seen.add(b); st.append(b)
    return seen
DM = [l.strip() for l in open(sys.argv[1])] if len(sys.argv) > 1 else []
