import cProfile, pstats, time
from engine import *
from sol import *
from t1 import generic_H
H1 = solution(X0, COEFFS[0], 0, 0)
for order in (3, 2):
    Hs = solution(X0, COEFFS[0], 0, 0, order=order)
    t0 = time.time(); einstein_orders(Hs); print("solution order", order, time.time() - t0)
    Hg = generic_H(labels(X0, order), 5)
    t0 = time.time(); einstein_orders(Hg); print("generic order", order, time.time() - t0)
pr = cProfile.Profile(); pr.enable()
einstein_orders(H1)
pr.disable()
pstats.Stats(pr).sort_stats("cumulative").print_stats(18)
