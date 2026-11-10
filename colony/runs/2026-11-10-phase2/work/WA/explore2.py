# scratch: occupation of array modes (window-restricted plane waves, antiperiodic, r=1) in the continuum I-state
import math as m
pi=m.pi
def nk(k,N=400000,X=4000.0):
    xk=2*pi*(k+.5)
    # integrate (2/pi) cos^2(x/2)/((x-xk)^2 (e^x+1)) over [-X, 60]
    a,b=-X,60.0; h=(b-a)/N; tot=0.0
    for i in range(N+1):
        x=a+i*h; d=x-xk
        if abs(d)<1e-9: val=0.25  # limit cos^2(x/2)/d^2 -> 1/4
        else: val=m.cos(x/2)**2/(d*d)
        val/= (m.exp(x)+1) if x<700 else float('inf')
        w=1 if i in (0,N) else (4 if i%2 else 2)
        tot+=w*val
    tail=(1/(X+xk))/2  # int_{-inf}^{-X} cos^2/(x-xk)^2 ~ 1/(2(X+xk))
    return (2/pi)*(tot*h/3+tail)
for k in [0,1,2,5,20,100]:
    n=nk(k); xk=2*pi*(k+.5)
    print(k,'n_k=%.6f'%n,'Gibbs=%.3e'%(1/(m.exp(xk)+1)),'pi*x_k*n_k=%.4f'%(pi*xk*n))
