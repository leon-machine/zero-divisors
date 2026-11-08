import numpy as np
from explore import build
for Om in (2,3,4,5,6):
    for s in range(0,Om):
        if Om==6 and s>3: continue
        H,st=build(Om,0,0,1.0,1.0,(s,s+1,1))   # H = -W
        Hs,_=build(Om,0,0,1.0,0.0,(s,s+1,1))  # -S*S
        w=np.sort(-np.linalg.eigvalsh(H))[::-1]
        lv=[]
        for e in w:
            if not lv or lv[-1][0]-e>1e-7: lv.append([e,1])
            else: lv[-1][1]+=1
        print(Om,'s',s,'XD=(s+1)(Om-s)=',(s+1)*(Om-s),' s(Om-s)=',s*(Om-s),' W levels',[(round(a,3),m) for a,m in lv[:4]], ' maxSS', round(-np.linalg.eigvalsh(Hs)[0],3))
