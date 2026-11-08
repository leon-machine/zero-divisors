import sys, numpy as np
from explore import build
Om=int(sys.argv[1]); Kp,Kc,GS,GD=map(float,sys.argv[2:6])
for s in range(0,Om):
    # doublet sector: s S-pairs plus one B_2 pair: N1=s, N2=s+1, Nc=1
    H,st=build(Om,Kp,Kc,GS,GD,(s,s+1,1))
    ev=np.sort(np.linalg.eigvalsh(H))
    ED=2*Kp*s+Kp+Kc-(GS*s+GD)*(Om-s)
    band=2*Kp*(s+1)-GS*(s+1)*(Om-s)
    print('s',s,'dim',len(st),'lowest',np.round(ev[:5],5),'ED',ED,'band(s+1)',band)
