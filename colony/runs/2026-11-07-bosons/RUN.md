# Run 2026-11-07-bosons: what is specific to this run

LAB = /home/claude/phys-graph. Run folder: colony/runs/2026-11-07-bosons/ (findings/, work/<name>/, verify/).
Read colony/BRIEF.md and colony/POLICIES.md; this file overrides them where they differ.

## Target
File into the store the boson result of Leon's working document "From the Bit to the Numbers" (7 November 2026),
Step 6 and objection 4, where new. Not an attack on an open problem: use extraction.note provenance, as the
2026-11-06 scalars-session entities did (see store/claims/synthesis.blade-square-signs-f2-quadratic-form/entity.md).

## The result (computed in a scratch workspace; work/session-checks.py reproduces it with numpy object arrays)
(i) Collective modes of the tower. For N steps with mutually commuting step operators b_i (even elements of each
    step, e.g. pairs b = a1^dag a2 on two fermion modes; pairs on different blocks commute in the graded product, single
    fermion operators on different steps anticommute and give no boson), B = (b_1 + ... + b_N)/sqrt N satisfies
    [B, B^dag] = 1 - 2k/N on k-excitation symmetric (Dicke) states (Holstein-Primakoff), exactly; N -> infinity gives the
    bosonic relation. In general the fluctuation algebra of a product state on an infinite tensor product is a Weyl (CCR)
    algebra with symplectic form s(Q,R) = state expectation of [Q,R] (quantum central limit theorem).
(ii) Pair commutator: [b, b^dag] = n1 - n2 for b = a1^dag a2 (exact). Expectations: 1 in the polarised vacuum (lower mode
    filled, upper empty); tanh(omega/2T) in a thermal state (exactly 1/2 at e^{omega/T} = 3); 0 in the trace state.
(iii) Density modes rho_q = sum_k c^dag_{k+q} c_k on M modes: [rho_q, rho_q^dag] equals, as an operator, the occupation of
    the q lowest modes minus that of the q highest (exact, M = 6, 8; sign by convention): pure edge effect at finite size;
    the constant q (a Weyl algebra) exactly when the low edge is filled and the high edge empty, i.e. the filled sea;
    0 in the trace state.
(iv) Consequence for the series: under (N+) the state on every horizon generator is the filled sea of the chiral Fermi
    field (store: op.r-premises-external known text; synthesis.positive-null-energy-gives-r-premises), so its density /
    pair modes form a Weyl algebra with non-degenerate symplectic form: bosons as density waves of the tower's filled sea,
    needing the infinite tower (completion) and the (N+) state. Only the trace state degenerates.

## Literature (checked against sources on 7 Nov 2026 by the orchestrator)
- C. D. Cushen and R. L. Hudson, A quantum-mechanical central limit theorem, J. Appl. Probab. 8 (1971) 454-469, doi:10.2307/3212170.
- D. Goderis, A. Verbeure, P. Vets, Non-commutative central limits, Probab. Th. Rel. Fields 82 (1989) 527-544; D. Goderis and
  P. Vets, Central limit theorem for mixing quantum systems and the CCR-algebra of fluctuations, Commun. Math. Phys. 122 (1988)
  249-265 (Weyl relations with s(Q,R) = sum_k phi([tau_k Q, R]); as cited in RIMS Kokyuroku 1278-8).
- D. C. Mattis and E. H. Lieb, J. Math. Phys. 6 (1965) 304-312, doi:10.1063/1.1704281: density commutators vanish for finite
  particle number and not in the filled-Dirac-sea limit. ALREADY a store Fact: synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra.
- Holstein and Primakoff, Phys. Rev. 58 (1940): from memory.

## Duplicate check first (mandatory)
Read in full and compare: synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra,
synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off, singularity.bosonisation-bridge-s-wave-sector,
dark-energy.imported-s-wave-current-algebra-external, synthesis.imported-local-quasi-equivalence-of-hadamard-states,
synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i, and anything else find_text turns up
for "bosonisation", "central term", "Schwinger", "Weyl", "fluctuation". File only what is new; cite what is stored.

## Gate and rules
As BRIEF.md: exact arithmetic in checks (Fractions; GA.py where the algebra does the work, e.g. fermion modes from Witt pairs
in Cl(N,N)), import GA, premise() per premise, mutation-sensitive; check4.py exits 0 and validate_draft ok; at most 2 proposals.
Do not create imported Facts or assumes edges (list Cushen-Hudson and Goderis-Verbeure-Vets as Facts to import). Credit
{name: Claude Opus 5.5, role: proposal and drafting, source: run 2026-11-07-bosons}. House style: no em dashes; never
"honest"/"honestly"; never "load-bearing"; no agent/run names in store text. Do not edit store/, commit or spawn agents.
