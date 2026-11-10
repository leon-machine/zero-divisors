import subprocess, sys, os
LAB = "/home/claude/phys-graph"; W = LAB + "/colony/runs/2026-11-10-phase1/verify/work-R1"
P = {
 "cert": ("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate", [
   ("Z = X + Y in the certificate", "    Z = GA.sub(X, Y)\n    SA, SB = acomm(sq, A1, A2), acomm(sq, B1, B2)\n    rhs", "    Z = GA.add(X, Y)\n    SA, SB = acomm(sq, A1, A2), acomm(sq, B1, B2)\n    rhs"),
   ("certificate factor 1/2 -> 1/4", "rhs = GA.scal(F(1, 2), GA.add(mul(sq, dagger(Z), Z)", "rhs = GA.scal(F(1, 4), GA.add(mul(sq, dagger(Z), Z)"),
   ("dagger = plain reverse", "    return {b: (c if sum(1 for i in b if i % 2 == 1) % 2 == 0 else -c) for b, c in r.items()}", "    return dict(r)"),
   ("K = e1 f1 instead of e1 f2", "    K = mul(sq, e[0], f[1])\n    assert GA.eq(dagger(K), K) and GA.eq(mul(sq, K, K), ONE)", "    K = mul(sq, e[0], f[0])\n    assert GA.eq(dagger(K), K) and GA.eq(mul(sq, K, K), ONE)"),
   ("17/8 example with a self-adjoint A = e1", "A = lin(F(17, 8), e[0], F(15, 8), f[0])", "A = lin(F(1), e[0], F(0), f[0])"),
   ("P with sqrt2 coefficient 1/8 -> 1/4", "P = (GA.scal(F(1, 4), GA.add(ONE, K)), GA.scal(F(1, 8), C))", "P = (GA.scal(F(1, 4), GA.add(ONE, K)), GA.scal(F(1, 4), C))"),
 ]),
 "rat": ("synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records", [
   ("gap >= 5 (law is tight)", "            assert gap >= 4\n", "            assert gap >= 5\n"),
   ("rho0 with + A2B2", "mul(GA.add(ONE, mul(A1, B1)), GA.sub(ONE, mul(A2, B2)))", "mul(GA.add(ONE, mul(A1, B1)), GA.add(ONE, mul(A2, B2)))"),
   ("circle of square radius 9", "X * X + Y * Y == F(8)", "X * X + Y * Y == F(9)"),
   ("pell recursion altered", "x, q = 3 * x + 4 * q, 2 * x + 3 * q\n", "x, q = 3 * x + 4 * q, 2 * x + 3 * q + 2\n"),
   ("stored pair state with cs = +1/2", "GA.scal(F(-1, 2), GA.add(mul(w[0], w[1]), mul(v[1], v[0])))", "GA.scal(F(1, 2), GA.add(mul(w[0], w[1]), mul(v[1], v[0])))"),
 ]),
 "three": ("synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two", [
   ("bound 8 -> 15/2 in the sampled trade-off", "            assert t <= F(8)\n", "            assert t <= F(15, 2)\n"),
   ("near state: bound for D 4/25 -> 0", "        assert value(near, CAD) ** 2 <= F(4, 25)", "        assert value(near, CAD) ** 2 <= F(0)"),
   ("pair-state third-party bound: left -> left/1000", "            assert t <= left\n", "            assert t <= left / 1000\n"),
 ]),
 "sig": ("synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two", [
   ("(3,1) put on the excluded list", "        (4, 0): (False, 5, 6), (1, 3): (False, 5, 6), (0, 4): (False, 5, 6),", "        (4, 0): (False, 5, 6), (3, 1): (False, 5, 6), (0, 4): (False, 5, 6),"),
   ("(3,1) configuration B2 = e0e1e2", "(3, 1): ((0,), (1,), (2, 3), (0, 1, 3)),", "(3, 1): ((0,), (1,), (2, 3), (0, 1, 2)),"),
   ("matrix-size table: quaternionic drop 2 -> 0", "4: 2, 6: 2, 5: 3", "4: 0, 6: 2, 5: 3"),
   ("positivity sample at r = 3/8 expected non-negative", "for r in (F(1, 3), F(-7, 20), F(239, 676)):\n            assert 8 * r * r <= 1", "for r in (F(1, 3), F(-7, 20), F(3, 8)):\n            assert 8 * r * r <= 2"),
 ]),
 "par": ("synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist", [
   ("two-mode party A uses the odd e_1", "    a1, a2 = p[0], prod(sq, e[0], f[1])\n    b1, b2 = p[2]", "    a1, a2 = p[0], e[0]\n    b1, b2 = p[2]"),
   ("no twist on party B", "    tw = prod(sq, e[1], p[0])\n    for o in (p[0], e[0], p[1], tw):", "    tw = e[1]\n    for o in (p[0], e[0], p[1], tw):"),
   ("pair state cs = -1/2", "                 GA.scal(F(1, 2), GA.add(prod(sq, w[0], w[1]), prod(sq, v[1], v[0]))))\n    assert dagger(rho, sq) == rho and prod(sq, rho, rho) == rho", "                 GA.scal(F(-1, 2), GA.add(prod(sq, w[0], w[1]), prod(sq, v[1], v[0]))))\n    assert dagger(rho, sq) == rho and prod(sq, rho, rho) == rho"),
   ("one-mode party with odd observable", "for a1, a2 in ((p[0], p[0]), (p[0], GA.neg(p[0])), (ONE, p[0])):", "for a1, a2 in ((p[0], e[0]), (p[0], GA.neg(p[0])), (ONE, p[0])):"),
 ]),
 "pos": ("synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state", [
   ("box functional 1 + C/2", "    m = GA.add(ONE, c)\n", "    m = GA.add(ONE, GA.scal(F(1, 2), c))\n"),
   ("A2' without the P- part", "    a2 = GA.add(prod(sq, e[0], plus), prod(sq, p[0], minus))", "    a2 = GA.add(prod(sq, e[0], plus), prod(sq, e[0], minus))"),
   ("B2 untwisted in the box", "    b = (p[1], prod(sq, e[1], p[0]))", "    b = (p[1], e[1])"),
 ]),
}
for key, (pid, perts) in P.items():
    src = open(f"{LAB}/proposals/{pid}/check.py").read()
    for i, (name, old, new) in enumerate(perts):
        assert src.count(old) == 1, (key, name, src.count(old))
        d = f"{W}/pert/{key}{i}"; os.makedirs(d, exist_ok=True)
        open(d + "/check.py", "w").write(src.replace(old, new))
        r = subprocess.run([sys.executable, LAB + "/colony/runcheck.py", d + "/check.py"], capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
        fails = [l.split()[1] for l in r.stdout.splitlines() if l.startswith("FAIL")]
        print(f"{key}{i} [{name}] -> exit {r.returncode}; FAIL: {fails if fails else 'NONE (perturbation not detected)'}")
