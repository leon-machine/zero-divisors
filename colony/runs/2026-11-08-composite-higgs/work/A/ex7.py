import numpy as np
from explore import build
for Om in (3,4,5):
  for P in (1,2):
    for GD in (0.2,0.5,0.8,0.95,1.2,3.0):
        GS=1.0; N=2*P; best=None
        for Nc in range(0,N+1):
            for N1 in range(0,N-Nc+1):
                N2=N-Nc-N1
                if N1>N2 or max(N1,N2,Nc)>Om: continue
                H,st=build(Om,0,0,GS,GD,(N1,N2,Nc))
                e=np.linalg.eigvalsh(H)[0]
                if best is None or e<best[0]-1e-9: best=(e,(N1,N2,Nc))
        wD=(GS-GD)*(Om-P+1); band=min(-GS*P*(Om-P+1),-GD*P*(Om-P+1))
        print(Om,P,GD,'wD',round(wD,2),'ground',round(best[0],4),best[1],'band min',band, 'OK' if abs(best[0]-band)<1e-9 else 'OFF')
