import sys, time
from proto import *
Om, s = int(sys.argv[1]), int(sys.argv[2])
t=time.time(); Wm = matrix(Om, (s, s+1, 1), {(0,1):1, (0,2):1, (1,2):1}); print('dim', len(Wm), 'build', round(time.time()-t,2))
for a in map(int, sys.argv[3:]):
    t=time.time()
    Mm = [[(F(a) if i == j else 0) - Wm[i][j] for j in range(len(Wm))] for i in range(len(Wm))]
    print('a', a, inertia(Mm), round(time.time()-t,2))
