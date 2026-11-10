from math import sqrt
def mk(w1,w2):
    def base(r1,r2):
        rho=r1+r2; p=w1*r1+w2*r2
        Lam=rho*(rho+3*p)/(rho-3*p)
        beta=Lam/3+rho/3; alpha=Lam/3-(rho+3*p)/6
        return Lam,beta,alpha
    def dN(f,r1,r2,h=1e-5):
        return (-3*(1+w1)*r1*(f(r1*(1+h),r2)-f(r1*(1-h),r2))/(2*h*r1)
                -3*(1+w2)*r2*(f(r1,r2*(1+h))-f(r1,r2*(1-h)))/(2*h*r2))
    q=lambda a,b: sqrt(base(a,b)[1])
    u=lambda a,b: 3/base(a,b)[0]
    H1=lambda a,b: base(a,b)[2]/(dN(q,a,b)+q(a,b))
    H2=lambda a,b: 2*q(a,b)/(2-dN(u,a,b)*base(a,b)[1])
    dec=lambda a,b: -1-dN(H1,a,b,1e-4)/H1(a,b)
    return base,H1,H2,dec
for (a,b) in [(0,0),(0.2,0.2),(0,1/3),(0,-0.2),(0,-1),(0,-2/3),(0,-0.5),(0.2,-1)]:
    base,H1,H2,dec=mk(a,b)
    print('w',a,b)
    for v in [(1,0.01),(1,0.1),(1,0.3),(1,1),(1,3),(1,30)]:
        try:
            L,be,al=base(*v)
            print('   ',v,'Lam %.4g beta %.4g'%(L,be),'H1 %.5g H2 %.5g'%(H1(*v),H2(*v)),'H^2/rho %.5g'%(H1(*v)**2/(v[0]+v[1])),'q %.5g'%dec(*v))
        except Exception as e: print('   ',v,'fail',e)
