from fractions import Fraction as F
import numpy as np, itertools
I2=np.eye(2,dtype=object); Z=np.array([[1,0],[0,-1]],dtype=object)
LOW=np.array([[0,1],[0,0]],dtype=object)   # |1>=(0,1)^T occupied ->  lowers occupied to empty
def kron(*ms):
    r=np.array([[1]],dtype=object)
    for m in ms: r=np.kron(r,m)
    return r
def site(op,i,N,jw=False):
    return kron(*[(Z if (jw and j<i) else I2) if j!=i else op for j in range(N)])
comm=lambda A,B: A.dot(B)-B.dot(A)
ok=True
# 1. Holstein-Primakoff: N even (paired) steps, b_i commute across steps; B = sum b_i / sqrt N
print("1. Holstein-Primakoff: [B,B^dag] on k-excitation Dicke states = 1 - 2k/N")
for N in range(2,7):
    S=sum(site(LOW,i,N) for i in range(N))       # sqrt(N) * B, b_i = lowering of step i
    C=comm(S,S.T)                                 # N [B,B^dag]
    # Dicke state with k excitations above the polarised reference (all occupied = reference? use all-empty reference: b lowers)
    for k in range(0,N+1):
        v=np.zeros(2**N,dtype=object)
        for occ in itertools.combinations(range(N),N-k):   # N-k occupied sites -> k "holes" relative to full reference
            idx=sum(1<<(N-1-i) for i in occ); v[idx]=1
        val=F(int(v.dot(C.dot(v))), int(v.dot(v)))/N
        ok &= (val == 1-F(2*k,N)) or (val == -(1-F(2*k,N)))
    print(f"   N={N}: holds for k=0..{N}: {ok}")
# 2. pair operator b = a1^dag a2 on two fermion modes (even element)
N=2; a=[site(LOW,i,N,jw=True) for i in range(N)]; n=[x.T.dot(x) for x in a]
b=a[0].T.dot(a[1])
ok2 = np.array_equal(comm(b,b.T), n[0]-n[1]); print("\n2. [b,b^dag] = n1 - n2 for b = a1^dag a2:", ok2)
def expect_product(p1,p2,Op):   # product state, occupation probs p1,p2 of modes 1,2
    rho=np.diag([ (1-p1)*(1-p2), (1-p1)*p2, p1*(1-p2), p1*p2 ]).astype(object)
    return sum(rho[i,i]*Op[i,i] for i in range(4))
C=comm(b,b.T)
for name,p1,p2 in [("polarised vacuum (lower filled, upper empty)",F(1),F(0)),("thermal, e^{beta omega}=3",F(3,4),F(1,4)),("trace state",F(1,2),F(1,2))]:
    print(f"   {name}: <[b,b^dag]> = {expect_product(p1,p2,C)}")
# pairs on different blocks commute (4 modes, graded/JW product)
N=4; a=[site(LOW,i,N,jw=True) for i in range(N)]
b1=a[0].T.dot(a[1]); b2=a[2].T.dot(a[3])
print("   pairs on different blocks commute:", not comm(b1,b2).any() and not comm(b1,b2.T).any())
s1=a[0]; s2=a[2]; print("   single fermion operators on different steps anticommute (no boson):", not (s1.dot(s2)+s2.dot(s1)).any())
# 3. Mattis-Lieb / Schwinger term with M momentum modes k=0..M-1, sea = lower half filled
print("\n3. Schwinger term: [rho_q, rho_-q] with M modes")
for M in (6,8):
    a=[site(LOW,i,M,jw=True) for i in range(M)]; n=[x.T.dot(x) for x in a]
    for q in (1,2):
        rq=sum(a[k+q].T.dot(a[k]) for k in range(M-q))
        Cq=comm(rq,rq.T)
        edge=sum(n[k] for k in range(q))-sum(n[M-1-k] for k in range(q))
        # check operator identity [rho_q, rho_q^dag] = sum_{bottom q} n - sum_{top q} n (up to overall sign convention)
        same = np.array_equal(Cq,edge) or np.array_equal(Cq,-edge)
        sea=sum(1<<(M-1-i) for i in range(M//2))           # lower half filled
        val=Cq[sea,sea]
        # trace-state expectation
        tr=F(int(sum(Cq[i,i] for i in range(2**M))),2**M)
        print(f"   M={M}, q={q}: operator = edge occupations only: {same};  sea expectation = {val};  trace-state expectation = {tr}")
print("\nall section-1 identities:", ok)
