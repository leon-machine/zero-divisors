"""Exploration only (floats): two-species single-shell pairing model.
Block b holds modes psi1 = 3b, psi2 = 3b+1, chi = 3b+2.
H = Kp (N1 + N2) + Kc Nchi - GS S*S - GD sum_a Ba* Ba,  S = sum_b w1 w2, B_a = sum_b w_psi_a w_chi.
"""
import itertools, sys
import numpy as np


def build(Om, Kp, Kc, GS, GD, sector):
    n = 3 * Om
    N1, N2, Nc = sector
    states = []
    for m in range(1 << n):
        c = [bin(m & sum(1 << (3 * b + f) for b in range(Om))).count('1') for f in range(3)]
        if tuple(c) == (N1, N2, Nc):
            states.append(m)
    idx = {s: i for i, s in enumerate(states)}

    def ann(i, st):
        out = {}
        for s, c in st.items():
            if s >> i & 1:
                sg = (-1) ** bin(s & ((1 << i) - 1)).count('1')
                t = s ^ (1 << i)
                out[t] = out.get(t, 0) + sg * c
        return out

    def cre(i, st):
        out = {}
        for s, c in st.items():
            if not s >> i & 1:
                sg = (-1) ** bin(s & ((1 << i) - 1)).count('1')
                t = s ^ (1 << i)
                out[t] = out.get(t, 0) + sg * c
        return out

    def pair_ann(f, g, st):  # sum_b w_f w_g
        out = {}
        for b in range(Om):
            for s, c in ann(3 * b + f, ann(3 * b + g, st)).items():
                out[s] = out.get(s, 0) + c
        return out

    def pair_cre(f, g, st):  # (sum w_f w_g)* = sum v_g v_f
        out = {}
        for b in range(Om):
            for s, c in cre(3 * b + g, cre(3 * b + f, st)).items():
                out[s] = out.get(s, 0) + c
        return out

    d = len(states)
    H = np.zeros((d, d))
    for j, s in enumerate(states):
        occ = [bin(s & sum(1 << (3 * b + f) for b in range(Om))).count('1') for f in range(3)]
        H[j, j] += Kp * (occ[0] + occ[1]) + Kc * occ[2]
        for (f, g, G) in ((0, 1, GS), (0, 2, GD), (1, 2, GD)):
            for t, c in pair_cre(f, g, pair_ann(f, g, {s: 1})).items():
                H[idx[t], j] -= G * c
    return H, states


if __name__ == '__main__':
    Om = int(sys.argv[1]); Kp, Kc, GS, GD = map(float, sys.argv[2:6])
    for Nc in range(0, Om + 1):
        for N1 in range(Om + 1):
            for N2 in range(N1, Om + 1):
                H, st = build(Om, Kp, Kc, GS, GD, (N1, N2, Nc))
                if not st:
                    continue
                assert np.allclose(H, H.T)
                ev = np.sort(np.linalg.eigvalsh(H))
                vals = sorted(set(np.round(ev, 6)))
                print((N1, N2, Nc), 'dim', len(st), 'levels', vals[:6])
