from dev import *
globals().update({k: v for k, v in vars(ck).items() if not k.startswith("__")})
zeta = sample_vector(23)
for k in range(4):
    print(k, corner(zeta[k]), "| full:", zeta[k].c)
