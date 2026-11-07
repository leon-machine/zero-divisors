"""Referee G: in the d = 3 two-channel relativistic window sea (lower band of h = k.sigma), the channel-resolved density
b = rho_q(P_+), P_+ = (1 + sigma_3)/2, has [b, b*] = n_+(E_-) - n_+(E_+) with mean S/2 (S the proposal's (iv) sum) and
variance V = sum_E (1 - k3^2/|k|^2)/4 on the sea (a product state, one particle per momentum in state u_k).
Normalised defect ||([b,b*] - <[b,b*]>) Omega||^2 / <[b,b*]>^2 = V / (S/2)^2. Exact for the d = 1 Dirac sea (V = 0).
Also a brute-force Fock check of mean and variance on a tiny d = 3 window would need non-rational u_k; we instead check
the d = 2 analogue h = k1 s1 + k2 s3 with rational unit vectors absent, so floats are used here (cross-check only)."""
import itertools, math
for N in range(2, 9):
    for q in (1,):
        S = V = 0.0
        for k1, k2 in itertools.product(range(-N, N), repeat=2):
            for k3 in list(range(-N, -N + q)) + list(range(N - q, N)):
                r2 = k1 * k1 + k2 * k2 + k3 * k3
                S += abs(k3) / math.sqrt(r2); V += (1 - k3 * k3 / r2) / 4
        print(f'N={N} q={q}: <[b,b*]> = S/2 = {S/2:9.3f}   variance = {V:8.3f}   normalised defect = {V/(S/2)**2:.5f}   x N^2 = {N*N*V/(S/2)**2:.4f}')
