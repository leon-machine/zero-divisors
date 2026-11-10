from explore1 import *
import io
p = F(1,3); D=4; c2=F(2,3)
def run(alpha, bterm, phi):
    G = [[{} for _ in range(D)] for _ in range(D)]
    Gi = [[{} for _ in range(D)] for _ in range(D)]
    Phi = {(F(0), 0, 1, 0): F(alpha)} if alpha else {}
    G[0][0] = eadd(mono(-1, 0), escal(-2, Phi)); Gi[0][0] = eadd(mono(-1, 0), escal(2, Phi))
    for i in range(1, D):
        G[i][i] = mono(1, 2 * p); Gi[i][i] = mono(1, -2 * p)
    b = bterm
    G[0][1] = G[1][0] = b
    Gi[0][1] = Gi[1][0] = escal(-1, emul(emul(b, mono(-1, 0)), mono(1, -2 * p))) if b else {}
    Ric, _ = ricci(G, Gi, D)
    src = {(0, 0): eadd(mono(c2, -2), {(F(-1), 1, 1, 0): 2 * c2*phi}), (0, 1): {(F(-1), 0, 2, 1): -c2*phi}}
    return {k: eadd(Ric[k], escal(-1, src.get(k, {}))) for k in Ric}
print("Phi only");  [print(k, v) for k, v in run(1, {}, 0).items() if v]
print("b only (g0x = A sin)");  [print(k, v) for k, v in run(0, {(F(0),0,2,0):F(1)}, 0).items() if v]
print("dphi only"); [print(k, v) for k, v in run(0, {}, 1).items() if v]
print("full, unreduced"); [print(k, v) for k, v in run(1, {(F(2,3),1,2,-1):F(-1)}, 1).items() if v]
