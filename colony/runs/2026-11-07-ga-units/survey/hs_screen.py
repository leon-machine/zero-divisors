# Screening checks for op.hypothesis-s bridge survey (exact, Fractions only).
import sys, itertools
from fractions import Fraction as Fr
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA  # imported per house rule; arithmetic below is plain Fractions

# ---------- (A) Fock slot modules over b doublets: U(2) content and CPT-closure test ----------
# weights of C^2 (x) C^b: each mode has U(2) weight (1,0) or (0,1); Lambda^n by subsets.
def u2_content(b, n):
    modes = [(1,0)]*b + [(0,1)]*b
    wts = {}
    for S in itertools.combinations(range(2*b), n):
        w = (sum(modes[i][0] for i in S), sum(modes[i][1] for i in S))
        wts[w] = wts.get(w,0)+1
    # decompose character into irreducibles F_(l1,l2), l1>=l2
    irr = {}
    wts = dict(wts)
    while any(v for v in wts.values()):
        top = max((w for w,v in wts.items() if v>0), key=lambda w: w[0]-w[1])
        m = wts[top]; l1,l2 = top
        irr[(l1,l2)] = irr.get((l1,l2),0)+m
        for t in range(l1-l2+1):
            wts[(l1-t,l2+t)] -= m
    return {k:v for k,v in irr.items() if v}
def cpt_closed(b):
    F = {n:u2_content(b,n) for n in range(2*b+1)}
    ok = all(not F[n] for n in range(3,2*b+1))
    ok = ok and set(F[2].keys()) <= {(1,1)} and F[2].get((1,1),0) == F[0].get((0,0),0)
    return ok, {n:F[n] for n in range(min(4,2*b+1))}
for b in range(1,5):
    ok, F = cpt_closed(b)
    print("Fock over %d doublet(s): CPT-closed=%s; F_0..F_3 content %s" % (b, ok, F))

# ---------- (B) five-mode module: commutant of gauge + even pair algebra; halvings ----------
N=5; SL=[0,1]; PR=[2,3,4]
states = list(itertools.product([0,1],repeat=N))
idx = {s:i for i,s in enumerate(states)}
def apply(ops, s):
    # ops: list of (mode, dagger) applied right to left; returns (sign, state) or None
    s=list(s); sign=1
    for (m,d) in reversed(ops):
        if s[m]==d: return None
        sign *= (-1)**sum(s[:m]); s[m]=d
    return sign, tuple(s)
def connections(oplist):
    E=[]
    for ops in oplist:
        for s in states:
            r=apply(ops,s)
            if r: E.append((idx[s], idx[r[1]]))
    return E
gauge = [[(i,1),(j,0)] for i in SL for j in SL if i!=j] + [[(i,1),(j,0)] for i in PR for j in PR if i!=j]
pair_even = [[(i,1),(j,1)] for i in PR for j in PR if i<j] + [[(i,0),(j,0)] for i in PR for j in PR if i<j]
slot_pair_create = [[(0,1),(1,1)],[(0,0),(1,0)]]  # su(2)_R off-diagonal part
def classes(E):
    par=list(range(len(states)))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for a,c in E: par[f(a)]=f(c)
    cl={}
    for i in range(len(states)): cl.setdefault(f(i),[]).append(i)
    return list(cl.values())
# number operators of each mode are diagonal with distinct joint eigenvalues, so commutant elements are diagonal
def nk(s): return (sum(s[i] for i in SL), sum(s[i] for i in PR))
def isotype(n,k):
    j = Fr(1,2) if n==1 else Fr(0)
    col = {0:'1',1:'3',2:'3b',3:'1'}[k]
    return (j,col,Fr(3*n-2*k,6))
conjcol={'1':'1','3':'3b','3b':'3'}
def content(signs, half):
    out={}
    for i,s in enumerate(states):
        if signs[i]==half:
            n,k=nk(s); out[(n,k)]=out.get((n,k),0)+1
    iso={}
    for (n,k),d in out.items():
        t=isotype(n,k); dim2 = 2 if n==1 else 1; dcol = 3 if k in (1,2) else 1
        iso[t]=iso.get(t,0)+Fr(d,dim2*dcol)
    return iso
def is_cpt(signs):
    P=content(signs,1); M=content(signs,-1)
    conjP={(j,conjcol[c],-y):m for (j,c,y),m in P.items()}
    return conjP==M
def anomaly_free(signs):
    P=content(signs,1); A=[Fr(0)]*5
    for (j,c,y),m in P.items():
        d2=int(2*j+1); dc=1 if c=='1' else 3
        if c!='1': A[0]+=m*d2*Fr(1,2)*y; A[4]+=m*d2*(1 if c=='3' else -1)
        if d2==2: A[1]+=m*dc*Fr(1,2)*y
        A[2]+=m*d2*dc*y**3; A[3]+=m*d2*dc*y
    return all(a==0 for a in A)
def survey(E,label):
    cls=classes(E)
    good=[]; ncpt=0
    for pat in itertools.product([1,-1],repeat=len(cls)):
        signs=[0]*len(states)
        for c,sg in zip(cls,pat):
            for i in c: signs[i]=sg
        if is_cpt(signs):
            ncpt+=1
            if anomaly_free(signs): good.append(signs)
    std=[(-1)**sum(s) for s in states]
    kinds=[]
    for g in good:
        kinds.append('+(-1)^N' if g==std else ('-(-1)^N' if g==[-x for x in std] else 'other'))
    print("%s: commutant dim %d, CPT halvings %d, anomaly-free %d: %s" % (label,len(cls),ncpt,len(good),kinds))
    return cls
survey(connections(gauge),"gauge only")
survey(connections(gauge+pair_even),"gauge + even pair algebra (su(4)/so(2,4) complexified)")
survey(connections(gauge+slot_pair_create),"gauge + su(2)_R slot-pair creation")
# vacuum-swapped halving: (-1)^N except on empty and full states
sw=[(-1)**sum(s) for s in states]; sw[idx[(0,)*5]]*=-1; sw[idx[(1,)*5]]*=-1
print("swapped halving CPT=%s anomaly-free=%s" % (is_cpt(sw),anomaly_free(sw)))
E=connections(pair_even)
print("swapped commutes with even pair algebra:", all(sw[a]==sw[c] for a,c in E))
# product form: Gamma = f(n) * w(k)
cnt=0; good=0; only=True
for f in itertools.product([1,-1],repeat=3):
    for w in itertools.product([1,-1],repeat=4):
        signs=[f[nk(s)[0]]*w[nk(s)[1]] for s in states]
        if is_cpt(signs):
            cnt+=1
            if anomaly_free(signs):
                good+=1
                std=[(-1)**sum(s) for s in states]
                only = only and (signs==std or signs==[-x for x in std])
print("product-form f(n)w(k): CPT halvings %d (as sign patterns), anomaly-free %d, all equal +-(-1)^N: %s" % (cnt,good,only))

# ---------- (C) Klein twist: split-preserving bivectors unchanged; grading still odd ----------
def op_matrix(ops):
    M={}
    for s in states:
        r=apply(ops,s)
        if r: M[(idx[r[1]],idx[s])]=r[0]
    return M
def mul(A,B):
    C={}
    for (i,k),a in A.items():
        for (k2,j),b in B.items():
            if k==k2: C[(i,j)]=C.get((i,j),0)+a*b
    return {k:v for k,v in C.items() if v}
def add(A,B,cb=1):
    C=dict(A)
    for k,v in B.items(): C[k]=C.get(k,0)+cb*v
    return {k:v for k,v in C.items() if v}
def majoranas(m):
    cd=op_matrix([(m,1)]); c=op_matrix([(m,0)])
    return [add(cd,c), add(cd,c,-1)]  # gamma_1 = c+c^dag, gamma_2 = c^dag - c (times i omitted; real check)
Pk={(i,i):(-1)**sum(states[i][j] for j in PR) for i in range(32)}
G={(i,i):(-1)**sum(states[i]) for i in range(32)}
slot=[g for m in SL for g in majoranas(m)]; pairs=[g for m in PR for g in majoranas(m)]
untw=[mul(g,Pk) for g in slot]   # Klein-untwisted (commuting) slot operators: JW slot ops times pair parity
anticomm=lambda A,B: add(mul(A,B),mul(B,A))=={}
comm=lambda A,B: add(mul(A,B),mul(B,A),-1)=={}
print("JW slot Majoranas anticommute with pair Majoranas:", all(anticomm(s,p) for s in slot for p in pairs))
print("untwisted slot Majoranas commute with pair Majoranas:", all(comm(s,p) for s in untw for p in pairs))
print("slot-slot bivectors identical in both conventions:", all(mul(untw[a],untw[b])==mul(slot[a],slot[b]) for a in range(4) for b in range(4)))
print("(-1)^N anticommutes with both conventions' slot operators:", all(anticomm(G,s) for s in slot+untw))
