# Run 2026-11-07-boson-items: what is specific to this run

LAB = /home/claude/phys-graph. Run folder: colony/runs/2026-11-07-boson-items/ (findings/, work/<name>/, verify/).
Read colony/BRIEF.md and colony/POLICIES.md; this file overrides them where they differ. The baseline (store at 1cfac5d)
is 0 errors, 0 warnings (baseline.log).

## Leon's standing rules (binding on every proposal)
- Everything in geometric algebra: Clifford-algebra objects, not matrices, tensors-with-indices or forms, wherever a GA
  formulation exists; gravity in Gauge Theory Gravity on a flat background.
- Derive, do not import: a result that would otherwise be imported is derived in GA inside the entity; literature is cited
  as prior art in the extraction note only. Do not create imported Facts. If a step genuinely cannot be derived, say so and
  list it as a decision for Leon.
- No imaginary unit: write complex structure with the GA unit chosen by the store's unit principle
  (colony/runs/2026-11-07-ga-units/RESOLVE.md, U1 to U6): I4 for even values and numbers, the transverse bivector J where
  the transport/fermion operators must commute with it, the central pseudoscalar of the odd extension for vectors.
- House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; no agent or run names in store text.

## Background: what is already in the store (read these first)
- synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum (accepted today): bosons as collective
  pair modes of the tower; exact Holstein-Primakoff; edge identity; band restriction of the null vacuum; algebraic core of the
  quantum central limit theorem (commutator converges in mean square; convergence of states NOT derived).
- singularity.bosonisation-bridge-s-wave-sector, field-theory.how-close-tower-comes-ccr, field-theory.no-canonical-commutation-
  relations-tower, hawking.current-commutator-exactly-edge-split, synthesis.null-vacuum-on-a-horizon-generator,
  synthesis.n-plus-null-ground-state (postulate (N+); the orientation of i relative to time is an assumed datum).
- Today's item-4 result (to be filed by filer U, below): see "Item 4" and work/unit-session.py, work/commutant-session.py.

## Item 4 (filer U files it; attackers may cite it as the proposal id synthesis.<chosen by U>)
Within a tower level Cl(N, N+2) = anisotropic kernel (0,2) x N hyperbolic (transport) planes:
(a) In the hyperbolic tower Cl(N,N) the commutant of the even part is span{1, Gamma}, Gamma = product of the plane
    pseudoscalars, Gamma^2 = +1: no element squares to -1, so self-adjoint boson fields have no canonical unit inside the
    transport steps (checked N = 1, 2, 3).
(b) J = g1 g2 (kernel bivector): J^2 = -1, J^dag = -J (CAR adjoint: reversion composed with sign flip of negative-square
    generators), J commutes with every transport generator (fermion modes and pairs).
(c) The commutant of the whole transport subalgebra in Cl(N, N+2) is span{1, J, Gamma g1, Gamma g2}, a quaternion algebra; its
    only even (fermion-parity preserving) unit is +-J (checked N = 1, 2).
(d) The level pseudoscalar I_n = +-J Gamma, I_n^2 = -1, I_n^dag = -I_n; Gamma = (-1)^F anticommutes with each mode and
    commutes with pairs; so I_n = +-J on each fermion-parity sector (consistent with U1/U2 and the rule never to identify them).
(e) For collective pairs S = sum_k a_{2k}^dag a_{2k+1}: phi = S + S^dag and pi = J(S^dag - S) are self-adjoint and
    [phi, pi] = 2 J sum_k (n_{2k} - n_{2k+1}) exactly (checked M = 1, 2 blocks); in the polarised or filled-sea state the
    normalised relation is the Hermitian canonical commutator with unit J.
(f) The sign of J is the (N+) orientation datum, now shared by fermions and bosons; the bosons' phase circle is exp(theta J),
    the rotations of the kernel plane (period 2 pi).

## Targets for the attackers (use the target id in extraction.open_problem)
Cluster S (structure), attackers SA (constructive) and SB (adversarial):
- bos.spin-statistics: on the ladder, prove (or refute) that half-integer spin goes with anticommutation (local to each
  transport step) and integer spin with commutation (collective, needing the limit). Make "spin" precise in GA (the action
  of the 2 pi rotor exp(pi J) or of the rotor group on the modes) and test whether collective pair modes carry integer spin
  and single modes half-integer, exactly, on finite towers.
- bos.qclt-states: derive in GA the convergence of the fluctuation STATES (not only the commutator): that the characteristic
  function (Weyl-operator expectation) of the normalised collective fields in a product state tends to the Gaussian
  (quasi-free) boson state with the covariance and symplectic form of the store entity. A finite exact statement with an
  explicit error bound is the goal (cumulants of order >= 3 scale as N^{1 - k/2}).
- bos.dynamics: derive the dynamics of the density-wave bosons: the Sugawara form (fermion kinetic energy on a generator is
  quadratic in the densities, with the central term), linear dispersion, and how a density-density interaction (Luttinger
  type) stays solvable; all in GA on the tower. Check what the store already holds (find_text Sugawara, Luttinger, Kac-Moody).
Cluster G (gauge and dimension), attackers GA (constructive) and GB (adversarial):
- bos.gauge-bosons: the quantum algebra of the Standard Model bosons. The series treats gauge fields classically as
  bivector-valued connections. Goal: derive the canonical commutation relations of a free gauge field (start with Maxwell in
  STA: F = E + I4 B) from the tower with unit J or I4, or prove an obstruction; say what part of photon quantisation the
  ladder gives (transverse modes, two helicities as the two orientations of the transverse plane?) and what it does not.
  Do not claim gluons, W, Z or the Higgs without a derivation.
- bos.dimension: exact bosonisation is special to one dimension. Determine what survives in higher dimension: e.g. that
  density modes of a filled sea in 3+1 dimensions satisfy canonical relations only up to explicit corrections (compute their
  size exactly on finite towers), or that bosons on each null generator (the series' setting) suffice because horizon modes
  are one-dimensional along generators. A precise statement of what the series needs is a success.
- op.r-premises-external (item 7): new angle only, using today's results: the sign of the unit J is now a datum shared by
  fermions and bosons; test whether bosonic positivity (a positive-energy boson Fock state) fixes the orientation of J and so
  the fermionic ground-state clause, or whether the orientation remains free (then say so precisely). Read the 2026-11-06
  run report first (colony/runs/2026-11-06-edge-normality/REPORT.md) and do not redo it.

## Gate and rules
As BRIEF.md: exact arithmetic in checks (Fractions; lib/GA.py), import GA, premise() per premise, mutation-sensitive checks;
check4.py exits 0 (environmental E401 acceptable) and validate_draft ok (helper:
colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py); register the proposal with
`python3 colony/labcli.py propose_claim @<abs path to draft json>` so it carries proposal.json. At most 2 proposals per attacker,
one strong one preferred. Credit {name: Claude Opus 5.5, role: proposal and drafting, source: run 2026-11-07-boson-items}.
Read your sibling's findings file midway and at the end; never file what they filed. One gate process at a time; the machine
has 2 CPUs and other agents share it; never kill other processes; do not edit store/, commit, push or spawn agents.
