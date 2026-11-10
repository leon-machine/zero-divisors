import sys,os,subprocess
LAB='/home/claude/phys-graph'; W=LAB+'/colony/runs/2026-11-10-phase2/verify/work-R1/pert'
P={'born':'synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional',
'eff':'synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects',
'spl':'synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them',
'loc':'synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values',
'rec':'synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables',
'ks':'synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them'}
T=[('born','nonmaximal set',[("        gens.append(b)\n","        gens.append(b)\n        break\n")]),
('born','drop reality in uniqueness',[("        if dsign(b, sq) == -1:\n            cands.append(blade(b))","        if False:\n            cands.append(blade(b))")]),
('born','example (b) with positive density 1+p+e/3 -> 1+p (should lose nu(e)=1/3)',[("(F(1, 3), e[0]))\n    lam","(F(0), e[0]))\n    lam")]),
('eff','u -> e1 f2 in clause (v)',[("u = prod(sq, e[1], f[0])","u = prod(sq, e[0], f[1])")]),
('eff','example density 1+2p -> 1+p/2',[("m = lin((1, ONE), (2, p[0]))","m = lin((1, ONE), (F(1, 2), p[0]))")]),
('spl','t=4 -> t=3',[("frame(1, *scale(1, 0, 4))","frame(1, *scale(1, 0, 3))")]),
('spl','only first two splits in classification',[("ker, blades = common_real(m, mats)\n        powers","ker, blades = common_real(m, mats[:2])\n        powers")]),
('spl','second split = identity for pair state',[("_, im = reflection(2, *scale(2, 0, 2))","_, im = reflection(2, *scale(2, 0, 1))")]),
('loc','K replaced by U in lam_c (local value moves)',[("        m = lin((1, ONE), (-1, u), (-1, v), (cc, k))\n        lam = lambda x: s0(prod(sq, m, x))\n        vals","        m = lin((1, ONE), (-1, u), (-1, v), (cc, u))\n        lam = lambda x: s0(prod(sq, m, x))\n        vals")]),
('loc','box direction 3/5,4/5 -> 1,0 (a configured setting: weight must be >=0)',[("bb = lin((F(3, 5), x2), (F(4, 5), z2))","bb = lin((F(1), x2), (F(0), z2))")]),
('rec','homogeneous := even only',[("homog = par(a) == a or par(a) == GA.neg(a)","homog = par(a) == a")]),
('rec','mixed setting replaced by homogeneous one',[("    b1 = lin((F(3, 5), x2), (F(4, 5), z2))\n    b2 = lin((F(4, 5), x2), (F(-3, 5), z2))\n    assert is_obs(b1, sq)","    b1 = lin((F(1), x2), (F(0), z2))\n    b2 = lin((F(0), x2), (F(-1), z2))\n    assert is_obs(b1, sq)")]),
('ks','drop ninth context and the multiplicity assertion',[("    [(1, 1, 1, -1), (-1, 1, 1, 1), (1, 0, 0, 1), (0, 1, -1, 0)],\n",""),("    assert all(sum(r in b for b in BASES) == 2 for r in rays)\n",""),("assert len(rays) == 18","assert len(rays) == 18 or True")]),
('ks','one vector changed (0,1,-1,0)->(0,1,1,0) in last context',[("(1, 0, 0, 1), (0, 1, -1, 0)],\n]","(1, 0, 0, 1), (0, 1, 1, 0)],\n]")]),
('ks','third row of the square: X1X2Z1Z2 -> Z1Z2X1X2 sign same? use product in other order',[("sq[2][2] = prod(sq[0][2], sq[1][2])","sq[2][2] = GA.neg(prod(sq[0][2], sq[1][2]))")]),
]
for i,(k,desc,subs) in enumerate(T):
    src=open(f'{LAB}/proposals/{P[k]}/check.py').read(); ok=True
    for a,b in subs:
        if a not in src: ok=False; print('!! pattern missing',k,desc,repr(a[:50]))
        src=src.replace(a,b)
    d=f'{W}/{i}'; os.makedirs(d,exist_ok=True); open(d+'/check.py','w').write(src)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
    out=subprocess.run(['python3',LAB+'/colony/runcheck.py',d+'/check.py'],capture_output=True,text=True,env=env).stdout
    res=[l.split()[0]+' '+l.split()[1][:60] for l in out.splitlines() if l.startswith(('PASS','FAIL','ERROR'))]
    print(f'[{k}] {desc} (applied={ok}):\n    '+'\n    '.join(res))
