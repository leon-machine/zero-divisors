import sys
d=sys.argv[1]
E=open(d+'/entity.md').read(); P=open(d+'/proof-main.tex').read(); C=open(d+'/check.py').read()
def rep(s,a,b,n=1):
    assert s.count(a)==n,(a[:70],s.count(a)); return s.replace(a,b)
B2="synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i"
E=rep(E,"title: 'Geometric modular conjugations on a generator give the null ground state'",
 "title: 'Field-level geometric modular conjugations on a generator give the null ground state'")
E=rep(E,"- citation: 'H. Baumgaertel, M. Jurke and F. Lledo","""- citation: 'H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. Res. Inst. Math. Sci. 6 (1970/71), 385--442.'
  key: Araki1970
  locator: 'purity criterion: a gauge-invariant quasi-free state is pure if and only if its symbol is a projection; only the direction pure implies projection is used (Step 2); cited from memory, not in the pinned Powers-Stormer Fact'
- citation: 'H. Baumgaertel, M. Jurke and F. Lledo""")
E=rep(E,"  - 'K with internal multiplicity","""  - 'purity criterion imported from memory (Araki 1970): the direction used, pure implies projection symbol, is not in the pinned Fact synthesis.imported-powers-stormer-takesaki-disjointness, which supplies only the factor property'
  - 'the sign eta is not a convention: it is the orientation of the imaginary unit relative to the time orientation, an open datum that (N+) assumes; eta = -1 is a named assumption of the equivalence with (N+)'
  - 'K with internal multiplicity""")
E=rep(E," The orientation sign is\n    the sign eta of the reflection relative to the Klein twist built with the field algebra's imaginary unit.",
""" The orientation sign is
    the sign eta of the reflection relative to the Klein twist built with the field algebra's imaginary unit;
    it is not fixed by the series (the orientation of i relative to time is an open datum that (N+) assumes),
    so eta = -1 is a named assumption here. The net-level failure (local gauge transforms of the vacuum, the
    Fermi seas) is the companion result """+B2+""", cited, not reproved.
    Compared with the stored KMS form, this result trades the modular group for the class assumption
    (gauge-invariant quasi-free states).""")
E=rep(E,"Transport-absent. Literature: Loewner's theorem cited from memory","Transport-absent. Literature: Loewner's theorem and Araki's purity criterion cited from memory")
E=rep(E,"the converse (Bisognano-Wichmann for\n    the chiral Fermi field, twisted second quantisation) cited from memory.",
 "the converse (the field-level twisted reflection of the chiral Fermi field: Brunetti-Guido-Longo,\n    Baumgaertel-Jurke-Lledo) cited from memory; the pinned Fact angle.imported-theorems-deliver-their-hypotheses\n    gives only the modular group.")
E=rep(E,"\\emph{(One cut: purity; proved, given Powers-Stormer.)}","\\emph{(One cut: purity; proved, given Powers-Stormer and the purity criterion.)}")
E=rep(E,"and then $\\omega$ is pure: $T$ is a projection.","and then $\\omega$ is pure, so $T$ is a projection (Araki's criterion, direction pure implies projection, cited from memory \\cite{Araki1970}).")
E=rep(E,"Stationarity, positivity of the null translations and the period $2\\pi$ of the geometric modular group are outputs.",
"Stationarity, positivity of the null translations and the period $2\\pi$ of the geometric modular group are outputs. The sign $\\eta$ is not a convention: it records the orientation of the imaginary unit of the field algebra relative to the time orientation, a datum the series does not fix and (N$_{+}$) assumes; the equivalence with (N$_{+}$) below holds under the named assumption $\\eta = -1$.")
E=rep(E,"""\\emph{(Converse; imported.)} $\\omega_{0}$ satisfies CGMA$_{-1}$ at every cut, and its time reverse CGMA$_{+1}$ (Bisognano-Wichmann for the chiral Fermi field, Fact \\claimref{angle.imported-theorems-deliver-their-hypotheses}, with the KMS property of $\\omega_{0}$ about every point, Theorem \\claimref{synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state}(ii)).""",
"""\\emph{(Converse; imported from memory.)} $\\omega_{0}$ satisfies CGMA$_{-1}$ at every cut, and its time reverse CGMA$_{+1}$. The modular group (the boost about $a$ at rapidity $-2\\pi t$) is supplied by the pinned Fact \\claimref{angle.imported-theorems-deliver-their-hypotheses} and the KMS property of $\\omega_{0}$ about every point (Theorem \\claimref{synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state}(ii)); the field-level action of $J_{a}$ as the twisted charge-conjugating reflection is not in that Fact and rests on \\cite{BGL1993, BJL2002}, cited from memory, with the one-particle identity argued by analytic continuation.""")
E=rep(E,"So for gauge-invariant quasi-free states on one generator, (N$_{+}$) is equivalent to CGMA$_{-1}$","So for gauge-invariant quasi-free states on one generator, given this converse and the assumption $\\eta = -1$, (N$_{+}$) is equivalent to CGMA$_{-1}$")
E=rep(E,"so it is locally normal to $\\omega_{0}$ and generator-Hadamard at every point.",
"so it is generator-Hadamard at every point, and it is locally normal to $\\omega_{0}$ on every bounded interval: the compressed symbol difference is a difference of positive trace-class operators, so the Powers-Stormer inequality and criterion (Fact \\claimref{synthesis.imported-powers-stormer-takesaki-disjointness}(a), (c)) give local quasi-equivalence.")
E=rep(E,"which violate the charge symmetry of (ii) for $k \\ne 0$ (proof, Step 8(d));",
"which violate the charge symmetry of (ii) for $k \\ne 0$ (the companion result on net-level modular data, "+B2+", proves the net-level identity; Step 8(d) only applies it);")
E=rep(E,"(v) imported; (vi)(b) argued.","(i) also rests on Araki's purity criterion (cited from memory); (v) imported from memory (BGL1993, BJL2002), the pinned Fact giving only the modular group; (vi)(b) argued.")
E=rep(E,"This result uses a weaker-looking ingredient of modular theory: only the modular conjugation $J$",
"This result uses a weaker-looking ingredient of modular theory, at a price: unlike the stored thermality theorem, which assumes nothing about the class of the state, it assumes the state gauge-invariant and quasi-free, so it trades the modular group for the class assumption. It uses only the modular conjugation $J$")
E=rep(E,"Within gauge-invariant quasi-free states it gives (N$_{+}$) for $\\eta = -1$ and the time-reversed vacuum for $\\eta = +1$,",
"Within gauge-invariant quasi-free states it gives (N$_{+}$) for $\\eta = -1$ and the time-reversed vacuum for $\\eta = +1$; the sign is the orientation of the imaginary unit relative to time, which the series does not fix, so $\\eta = -1$ is an assumption, not a convention,")
E=rep(E,"and the algebra-level form admits the Fermi-level states.","and the algebra-level form admits the Fermi-level states (the companion result on net-level modular data).")
E=rep(E,"or into its time-reversed image, which a sign in the mirror distinguishes.","or into its time-reversed image, which a sign in the mirror distinguishes; which sign is right is not settled by anything else in the series and is assumed.")
E=rep(E,"The condition is a reformulation of the assumption","The result holds for the simplest class of states (those fixed by their two-point correlations), and the condition is a reformulation of the assumption")
E=rep(E,"For gauge-invariant quasi-free states on a horizon generator, requiring the modular conjugation",
"For gauge-invariant quasi-free states on a horizon generator, requiring (at the field level) the modular conjugation")
E=rep(E,"gives (N$_{+}$) for $\\eta = -1$ and its time reverse for $\\eta = +1$, with no stationarity",
"gives (N$_{+}$) for $\\eta = -1$ (an assumed sign: the orientation of $i$ relative to time is an open datum) and its time reverse for $\\eta = +1$, with no stationarity")
# proof
P=rep(P,"so $T$ is a projection (a gauge-invariant quasi-free state is pure exactly when its symbol is a projection; standard, cited from memory).",
"so $T$ is a projection. This last step is the only-if direction of Araki's purity criterion (a gauge-invariant quasi-free state is pure if and only if its symbol is a projection; \\cite{Araki1970}, cited from memory); it is not part of the pinned Fact, which supplies only the factor property used above.")
P=rep(P,"\\emph{Step 7 (the converse, imported).} By the Bisognano-Wichmann property of the chiral Fermi field (Fact \\claimref{angle.imported-theorems-deliver-their-hypotheses}, the abstract form for half-line algebras with positive translations, and the stored theorem",
"\\emph{Step 7 (the converse, imported from memory).} The pinned Fact \\claimref{angle.imported-theorems-deliver-their-hypotheses} (its abstract form for half-line algebras with positive translations; Borchers' $JU(s)J = U(-s)$ is also in Fact \\claimref{synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem}(ii)) and the stored theorem")
P=rep(P,"$\\Delta_{a}^{it}$ is the boost about $a$ at rapidity $-2\\pi t$, and the modular conjugation is the twisted charge-conjugating reflection about $a$ (\\cite{BGL1993}; for the twisted fermionic second quantisation \\cite{BJL2002}; both cited from memory).",
"give the modular group: $\\Delta_{a}^{it}$ is the boost about $a$ at rapidity $-2\\pi t$. That the modular conjugation acts on the fields as the twisted charge-conjugating reflection about $a$ is not in the pinned Fact; it rests on \\cite{BGL1993} and, for the twisted fermionic second quantisation, \\cite{BJL2002}, both cited from memory.")
P=rep(P,"which is the value $-i\\eta\\,\\omega(B(y)B(\\rho_{a}x))$ of Step 4 with $\\eta = -1$ (argued). So $\\omega_{0}$ satisfies CGMA$_{-1}$ at every cut and its time reverse CGMA$_{+1}$; with Step 6,",
"which is the value $-i\\eta\\,\\omega(B(y)B(\\rho_{a}x))$ of Step 4 with $\\eta = -1$ (argued); the sign so obtained agrees with the one fixed independently by the proved positivity of Step 4, a consistency check, not a proof of the converse. So $\\omega_{0}$ satisfies CGMA$_{-1}$ at every cut and its time reverse CGMA$_{+1}$; with Step 6, under the assumption $\\eta = -1$ (the sign of $i$ relative to time being a datum the series does not fix),")
P=rep(P,"so it is locally normal to $\\omega_{0}$ at every point (a bounded kernel difference on bounded intervals, Hilbert-Schmidt there) and passes the generator microlocal condition.",
"so it passes the generator microlocal condition at every point. It is locally normal to $\\omega_{0}$ on every bounded interval $O$: $\\chi_{O}(T_{S} - T_{0})\\chi_{O} = \\chi_{O}\\chi_{(0, 2)}(P)\\chi_{O} - \\chi_{O}\\chi_{(-2, 0)}(P)\\chi_{O}$ is a difference of positive trace-class operators (each is $X^{*}X$ with $X = \\chi_{(0, 2)}(P)\\chi_{O}$, resp. $\\chi_{(-2, 0)}(P)\\chi_{O}$, Hilbert-Schmidt since its kernel is bounded and $O$ is bounded), so the compressed symbols $A$, $B$, and $1 - A$, $1 - B$, differ by trace-class operators; the Powers-Stormer inequality (Fact \\claimref{synthesis.imported-powers-stormer-takesaki-disjointness}(c)) makes $A^{1/2} - B^{1/2}$ and $(1 - A)^{1/2} - (1 - B)^{1/2}$ Hilbert-Schmidt, and criterion (a) gives quasi-equivalence of the restrictions to the algebra of $O$.")
P=rep(P,"(d) The net-level form (only $J_{a}\\mathcal{R}_{I}J_{a} = Z\\mathcal{R}_{\\rho_{a}I}Z^{*}$) is satisfied by every $\\omega_{0}\\circ\\gamma_{g}$, including",
"(d) The net-level form (only $J_{a}\\mathcal{R}_{I}J_{a} = Z\\mathcal{R}_{\\rho_{a}I}Z^{*}$) is satisfied by every $\\omega_{0}\\circ\\gamma_{g}$, by the net-level identity of the companion result "+B2+" (not reproved here; it is the first sentence of (a)), including")
old=C[C.index("    # direct: (1/2 pi)"):C.index("def check_two_cuts_do_not_give_stationarity")]
new='''    # independent route: int_0^2 sin(p s) dp, expanded in s, integrating p^{2k+1} over [0, 2] exactly
    q_coeffs = []
    for k in range(4):
        prim = [F(0)] * (2 * k + 3)
        prim[2 * k + 2] = F(1, 2 * k + 2)                 # antiderivative of p^{2k+1}
        q_coeffs.append(F((-1) ** k, _fact(2 * k + 1)) * GA.peval(prim, F(2)))
    GA.check("int_0^2 sin(ps) dp has the same series as (1 - cos 2s)/s", q_coeffs == coeffs)


'''
C=C.replace(old,new)
open(d+'/entity.md','w').write(E); open(d+'/proof-main.tex','w').write(P); open(d+'/check.py','w').write(C)
print("ok")
