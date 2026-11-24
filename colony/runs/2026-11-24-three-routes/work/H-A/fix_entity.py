P='/home/claude/leon-machine/zero-divisors/proposals/synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none/'
e=open(P+'entity.md').read()
def rep(old,new,cnt=1):
    global e
    assert e.count(old)==cnt,(e.count(old),old[:80])
    e=e.replace(old,new)

# --- class of states (fix 1) ---
rep("The states considered are the gauge-invariant quasi-free states that are homogeneous, diagonal in helicity and charge-symmetric: one vector $v_{k}(\\eta)$ with $|v_{k}| \\le 1$ per sector, solving the Bloch equation,",
    "The states considered in (i) to (vi) are the gauge-invariant quasi-free states that are homogeneous, isotropic, diagonal in helicity with the same vector in the two helicities, and charge-symmetric: one vector $v_{k}(\\eta)$ with $|v_{k}| \\le 1$, depending on $k = |\\vec k|$ only and the same in every sector of that $k$, solving the Bloch equation,")
rep("The wall-instant vacuum is the solution with $v(0) = \\sigma_{1} = \\hat h(0)$, the tracial state is $v = 0$.",
    "The wall-instant vacuum is the solution with $v(0) = \\sigma_{1} = \\hat h(0)$, the tracial state is $v = 0$. Clause (vii) drops isotropy. \\emph{The background is prescribed.} (RD) and (DF) fix the gravitational field, and the Dirac field is a test field on it; with the expected stress of a Hadamard state of the series' content as the source, the exact radiation field does not reach the wall (the result filed alongside, synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall, given its hypotheses (A) and (E)), so (RD), (DF), (A) and (E) do not hold together and the present result is for a prescribed background, not a self-consistent one.")
# --- (i)(b), (i)(c) ---
rep("$O_{A}$ is induced by $\\theta$ acting as an automorphism (an antiunitary map of the one-particle space), and by $W$ followed by the exchange of particles and holes, $\\tfrac12(1 + s) \\mapsto \\tfrac12(1 - s)$; it keeps $\\sigma_{1}$.",
    "$O_{A}$ is induced by $\\theta$ acting as an automorphism (an antiunitary map of the one-particle space, which carries each sector of momentum $\\vec k$ to a sector of momentum $-\\vec k$), and, within each sector, by $W$ followed by the exchange of particles and holes, $\\tfrac12(1 + s) \\mapsto \\tfrac12(1 - s)$; it keeps $\\sigma_{1}$. For the isotropic class the two give the same condition, sector by sector.")
rep("acts on Bloch vectors as $s \\mapsto -s$, exchanges no sides of the wall, and has the tracial state as its only invariant state; followed by the exchange of particles and holes it is the identity.",
    "acts on Bloch vectors as $s \\mapsto -s$ (between the sectors of momenta $\\vec k$ and $-\\vec k$, being antilinear), exchanges no sides of the wall, and has the tracial state as its only invariant state in the isotropic class; followed by the exchange of particles and holes it is the identity.")
# --- (iv)(c): O_B Fock states argued not Hadamard; credit (fix 3, 6) ---
rep("the $O_{B}$-invariant Fock states have occupation $\\tfrac12(1 \\mp e^{-\\pi k^{2}/(2ma')})$ over $s_{\\mathrm{out}}$.",
    "the $O_{B}$-invariant Fock states have occupation $\\tfrac12(1 \\mp e^{-\\pi k^{2}/(2ma')})$ over $s_{\\mathrm{out}}$, tending to $\\tfrac12$ (so, argued and not proved, they are not Hadamard). \\emph{Credit.} The pure-state profile of (b), the transition probability of (c) and the choice of least number in (vi) are those of Boyle, Finn and Turok, arXiv:1803.08930: the free function of the invariant vacua is their Eq. (3.48), the occupation $(1 - \\cos 2\\eta\\cos\\lambda)/2$ in their notation their Eq. (3.49), and $|\\beta| = e^{-\\pi p^{2}/(2\\gamma)}$ for the mass $\\gamma\\tau$ their Eq. (5.13); these locators were confirmed in review against the arXiv text.")
# --- (v)(b) tracial (fix 3) ---
rep("and is not Hadamard (clause (ii) of the cited massive result at $M_{1} = \\mu$); the tracial state is invariant and not Hadamard. So (CW) neither implies (HD) nor is implied by it,",
    "and is not Hadamard (clause (ii) of the cited massive result at $M_{1} = \\mu$, itself given the same Fact); the tracial state is invariant and is not Hadamard, which is proved for $\\mu = 0$ (the stored moment criterion) and argued, not proved, for $\\mu > 0$ (its two-point function is one half of the anticommutator distribution, whose wave front set contains both $C^{(+)}$ and $C^{(-)}$; no necessity criterion for massive fields is stored). So, given the Fact, (CW) neither implies (HD) nor is implied by it,")
# --- (vi) and new (vii) ---
rep("\\item[(vi)] \\emph{(What selects; proved.)} Among the $O_{A}$-invariant states the one of least occupation over the late-time vacuum in every sector is $s_{0}$, a Fock state:",
    "\\item[(vi)] \\emph{(What selects; proved.)} Among the $O_{A}$-invariant states of the isotropic class the one of least occupation over the late-time vacuum in every sector is $s_{0}$, a Fock state:")
rep("attained by $s_{\\mathrm{out}}$, which is not $O_{A}$-invariant for $\\mu > 0$.\n\\end{enumerate}",
    "attained by $s_{\\mathrm{out}}$, which is not $O_{A}$-invariant for $\\mu > 0$.\n\\item[(vii)] \\emph{(Without isotropy; proved.)} For homogeneous, helicity-diagonal, charge-symmetric states with one vector $v_{\\vec k, h}$ per sector, invariance under $\\theta$ is $v_{-\\vec k, h'}(0) = O_{A}v_{\\vec k, h}(0)$ for each pair of sectors $(\\vec k, h)$, $(-\\vec k, h')$ that $\\theta$ exchanges, and it restricts no single sector. For $\\mu > 0$ the occupations over $s_{\\mathrm{out}}$ of such a pair satisfy\n\\[\nn_{\\vec k, h} + n_{-\\vec k, h'} \;=\; 1 - \\sqrt{1 - q}\;v_{\\vec k, h}(0)\\cdot\\hat m \;\\ge\; 2n_{0},\n\\]\nwith equality exactly when $v_{\\vec k, h}(0) = \\hat m$, and the floor of (iv)(b) fails sector by sector: $v_{\\vec k, h} = s_{\\mathrm{out}}$ with $v_{-\\vec k, h'} = s_{\\mathrm{in}}$ is invariant, with occupations $0$ and $q$. So $s_{0}$ is still the invariant state of least number in every pair, hence of least total number. Invariance under $W$ followed by the exchange of particles and holes is a condition within each sector, and (ii), (iv)(b) and (vi) hold for it without isotropy.\n\\end{enumerate}")
# --- technical (fix 3 and class) ---
rep("its invariant pure states sit at occupation one half at the wall and approach one half at large momentum, so it cannot give a Hadamard state.",
    "its invariant pure states sit at occupation one half at the wall and approach one half at large momentum, so, as the tracial state, it gives no Hadamard state (argued: the occupation tends to one half).")
rep("is the one the proposal needs, and its invariant states form a disk per mode: a continuum.",
    "is the one the proposal needs, and its invariant states, among homogeneous, isotropic, helicity-diagonal, charge-symmetric quasi-free states, form a disk per mode: a continuum. (The conjugation pairs momentum $\\vec k$ with $-\\vec k$; without isotropy the bound below holds only for the sum of the two occupations of a pair.)")
rep("The profile and the non-uniqueness are in the papers of Boyle, Finn and Turok;",
    "The background is prescribed and the Dirac field is a test field on it: with the expected stress as the source the exact radiation field does not reach the wall, given the hypotheses of the trace-anomaly result filed alongside. The profile and the non-uniqueness are in the paper of Boyle, Finn and Turok (arXiv:1803.08930, Eqs. (3.48), (3.49), (5.13));")
# --- lay (fix 5) ---
rep("The state that sits exactly on the minimum is well behaved and has no adjustable number,",
    "The state that sits exactly on the minimum is well behaved, given a standard theorem on such states, and has no adjustable number,")
rep("gives a state with every level half filled, which is not well behaved. The demand also makes the two sides equally hot, which sits badly with the series' cold mirror.",
    "gives a state with every level half filled, which is argued not to be well behaved. The demand would also make the two sides equally hot (argued), which sits badly with the series' cold mirror.")
# --- one-liner (fix 2) ---
rep("the invariant quasi-free Dirac states are a disk of Bloch vectors per mode, not one state:",
    "the invariant quasi-free Dirac states (homogeneous, isotropic, diagonal in helicity, charge-symmetric) are a disk of Bloch vectors per mode, not one state:")
rep("the energy-reversing conjugation gives occupation one half; the wall-instant vacuum is invariant and not Hadamard.",
    "without isotropy only the pair bound $n_{\\vec k} + n_{-\\vec k} \\ge 2n_{0}$ holds; the energy-reversing conjugation gives occupation one half; the wall-instant vacuum is invariant and not Hadamard (given the same Fact); the background is prescribed, the Dirac field a test field on it.")
# --- front matter: note, flags, checked_by ---
rep("- kind: check\n  ref: check.py::check_weber_form_and_transition_probability_bookkeeping\n",
    "- kind: check\n  ref: check.py::check_pair_bound_without_isotropy\n- kind: check\n  ref: check.py::check_weber_form_and_transition_probability_bookkeeping\n")
rep("clauses (i) to (iv)(b), (v)(a) and (vi) are proved here, with the exact checks;",
    "clauses (i) to (iv)(b), (v)(a), (vi) and (vii) are proved here, with the exact checks;")
rep("the Reading is argued. The\n    class of states is homogeneous, diagonal in helicity and charge-symmetric; states outside it only enlarge the\n    invariant set.",
    "the statements that the tracial state (for $\\mu > 0$) and the Fock states of the energy-reversing\n    reflection are not Hadamard are argued; the Reading is argued. The class of states of clauses (i) to (vi) is\n    homogeneous, isotropic, diagonal in helicity with equal vectors in the two helicities, and charge-symmetric;\n    isotropy is needed because the antilinear conjugation pairs momentum $\\vec k$ with $-\\vec k$, and clause (vii)\n    gives what holds without it (a bound on each pair, not on each sector). States outside the class only enlarge\n    the invariant set. The check of the Weber clause tests the exponent arithmetic and the reduction to Weber's\n    equation only, not the special-function facts. The background is prescribed: the result filed alongside on the\n    trace anomaly (synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall) shows that (RD) and\n    (DF) do not hold together with its hypotheses (A) and (E).")
rep("251301 and arXiv:1803.08930 (read in part, through a summarising fetch, so to be confirmed against the papers):\n    the free function left by CPT invariance, its fixing by least particle number and energy, the profile and the\n    number density are theirs;",
    "251301 (from memory) and arXiv:1803.08930, Eqs. (3.48), (3.49), (5.13), (5.15), (5.16) (locators confirmed in\n    review against the arXiv text): the free function left by CPT invariance, its fixing by least particle number\n    and energy, the profile and the number density are theirs;")
rep("  - 'the Reading (mirror, obstructions) is argued and is not part of the statement'\n",
    "  - 'the Reading (mirror, obstructions) is argued and is not part of the statement'\n  - 'prescribed background: (RD) and (DF) are not jointly available with the hypotheses (A) and (E) of the trace-anomaly result filed alongside'\n  - 'clauses (i) to (vi) are for the isotropic class; clause (vii) is the statement without isotropy'\n")
open(P+'entity.md','w').write(e)
print("entity ok")
