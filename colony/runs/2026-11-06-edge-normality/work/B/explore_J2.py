import numpy as np, itertools
exec(open('explore_J.py').read().split("run(1, 1, 1)")[0])
def fit(n0,n1,r):
    n=n0+n1; a=jw(n)
    G = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); Q,_=np.linalg.qr(G)
    E = Q[:, :r] @ Q[:, :r].conj().T
    Om = slater(E,a)
    gens=[[np.eye(2**n),a[j],a[j].conj().T,a[j].conj().T@a[j]] for j in range(n)]
    def monos(idx):
        out=[]
        for combo in itertools.product(*[range(4) for _ in idx]):
            m=np.eye(2**n,dtype=complex); name=[]
            for j,c in zip(idx,combo):
                m=m@gens[j][c]; name.append(['1','a%d'%j,'a%d*'%j,'n%d'%j][c])
            out.append((' '.join(name),m))
        return out
    Mb=[m for _,m in monos(range(n0))]
    Jm,D=modular(Om,Mb)
    Jf=lambda Op: Jm@Op.conj()@Jm.conj()
    allm=monos(range(n))
    B=np.array([m.flatten() for _,m in allm]).T
    X=E[n0:,:n0]; U,s,Vh=np.linalg.svd(X); W=U[:,:n0]@Vh
    print('W=',np.round(W,4))
    for j in range(n0):
        c=np.linalg.lstsq(B,Jf(a[j]).flatten(),rcond=None)[0]
        print('J a%d J ='%j, [(nm,np.round(cc,4)) for (nm,_),cc in zip(allm,c) if abs(cc)>1e-8])
fit(1,1,1); fit(2,2,2)
