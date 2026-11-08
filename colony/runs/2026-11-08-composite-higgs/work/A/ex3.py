import sys, numpy as np
from explore import build
res=[]
for Om in (2,3,4,5):
  for GS,GD in ((3,0.1),(3,1),(3,2),(3,2.9),(3,3),(3,4),(1,2)):
    for s in range(0,Om):
        H,st=build(Om,0,0,GS,GD,(s,s+1,1))
        ev=np.sort(np.linalg.eigvalsh(H))
        ED=-(GS*s+GD)*(Om-s)
        print(Om,GS,GD,'s',s,'min',round(ev[0],4),'ED',ED,'ED-min',round(ED-ev[0],4),'ratio/GD',round((ED-ev[0])/GD,4))
