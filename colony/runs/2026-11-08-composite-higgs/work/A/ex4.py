import sys, numpy as np
from explore import build
GS,GD=3.0,float(sys.argv[1])
for Om in (3,4,5,6):
    for s in range(0,Om//2+1):
        H,st=build(Om,0,0,GS,GD,(s,s+1,1))
        ev=np.sort(np.linalg.eigvalsh(H))
        lv=[]
        for e in ev:
            if not lv or e-lv[-1][0]>1e-7: lv.append([e,1])
            else: lv[-1][1]+=1
        ED=-(GS*s+GD)*(Om-s); Eth=-GS*s*(Om-s)
        print(Om,'s',s,'ED',ED,'Eth0',Eth,'levels',[(round(a,3),m) for a,m in lv[:5]])
