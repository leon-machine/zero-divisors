# own route: index tensors R[ab][cd], condition R_{abcd}+R_{bcad}+R_{cabd}=0; rank mod prime
import itertools
p=1000003
def rank(rows,n):
    rows=[r[:] for r in rows]; rk=0
    for c in range(n):
        piv=next((i for i in range(rk,len(rows)) if rows[i][c]%p),None)
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]; inv=pow(rows[rk][c],p-2,p)
        rows[rk]=[v*inv%p for v in rows[rk]]
        for i in range(len(rows)):
            if i!=rk and rows[i][c]%p:
                f=rows[i][c]; rows[i]=[(a-f*b)%p for a,b in zip(rows[i],rows[rk])]
        rk+=1
    return rk
for d in (3,4,5,6):
    pairs=list(itertools.combinations(range(d),2)); n=len(pairs); idx={q:i for i,q in enumerate(pairs)}
    def var(a,b,c,e):
        if a==b or c==e: return None
        s=1
        if a>b: a,b=b,a; s=-s
        if c>e: c,e=e,c; s=-s
        return idx[(a,b)]*n+idx[(c,e)],s
    rows=[]
    for a,b,c in itertools.combinations(range(d),3):
        for e in range(d):
            r=[0]*(n*n)
            for (x,y,z) in ((a,b,c),(b,c,a),(c,a,b)):
                v=var(x,y,z,e)
                if v: r[v[0]]+=v[1]
            rows.append(r)
    rk=rank(rows,n*n)
    sym=[]
    for i in range(n):
        for j in range(i+1,n):
            r=[0]*(n*n); r[i*n+j]=1; r[j*n+i]=-1; sym.append(r)
    print(d,'rank',rk,'kernel',n*n-rk,'formula',d*d*(d*d-1)//12,'kernel symmetric:',rank(rows+sym,n*n)==rk,'sym dim',n*(n+1)//2)
