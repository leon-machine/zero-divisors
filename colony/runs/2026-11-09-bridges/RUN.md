# Run 2026-11-09-bridges: what is specific to this run

LAB = /home/claude/phys-graph (branch run/2026-11-09-bridges, stacked on run/2026-11-09-three, whose results are in the
store). Run folder: colony/runs/2026-11-09-bridges/ (findings/, work/<name>/, verify/). Read colony/BRIEF.md and
colony/POLICIES.md; this file overrides them. Baseline: baseline.log (0 errors, 0 warnings).

## Goal
Leon asked for all the cross-pollination items of the earlier run to be worked. Source of every target:
colony/runs/2026-11-09-three/findings/bridges.md (read it in full: each item there has entity ids, a first computation
and a kill condition; sections "Cross-links between subjects" C1-C9, "New areas" N1-N7, and R7 under T1). Also read
colony/runs/2026-11-09-three/REPORT.md and DECISIONS.md. Each target starts with the first computation named in the
bridges file; go on from there as far as the result is exact. A kill firing is a result: file the negative if it is
established with exact checks, otherwise record it in findings.

## Cluster C1: exact, mostly finite computations (attackers C1A constructive, C1B adversarial)
- X1. Finite averages in place of the Haar imports (bridges C3): synthesis.signed-directions-and-the-integer-clifford-algebra
  (the extraspecial group) against synthesis.imported-haar-average-purity and any other Haar import the entropy and
  scrambling results use (find them). Question: do averages over the finite Clifford/normaliser group, parity-preserving
  where the CAR superselection requires it, reproduce the Haar moments those results need (which moments: list them per
  dependant)? First: mean purity over the parity-preserving normaliser at n = 4. Success: a theorem that the needed
  moments agree (a design statement with its exact order), so the imports can be replaced by a derived result; or the
  exact moment at which they differ and which stored results that touches. Kill: parity superselection breaks the
  2-design property.
- X2. Dark-tower running (bridges C4, N3; op.dark-tower-running):
  synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces applied to synthesis.gauge-algebra-by-tower
  with the towers' stored content (dark-tower-matter.* content entities). The one-loop b coefficient per tower and per
  factor; which factors are asymptotically free; what the store's content says about confinement scales relative to the
  visible sector only if no new input is needed (otherwise say which input). Consequences for op.odd-towers and
  op.thickness-deposit-rule stated, not forced.
- X3. The curvature coupling across subjects (bridges C1; op.curvature-coupling-across-subjects): evaluate the Sakharov
  coefficient B = 16 n_g - 48 + N_S(1 - 6 xi_R) at the value of xi_R the Kasner tilt fit needs
  (synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling), decide whether the
  three appearances are one scalar field or different fields (which fields carry each xi_R in the stored statements), and
  what, if anything, in the store constrains xi_R (conformal coupling 1/6 from the tractor/conformal structure is the
  obvious candidate: is it forced for the attachment's scalar?). The maintainer's unreviewed figures in the open problem
  (B about -65 at the tilt window; zero between seven and eight generations) are to be recomputed.
- X4. Majorana mass as tower pairing (bridges C6): the stored pairing.* gap on a two-mode (nu_L, nu_R) block against
  neutrino.m-framework-realises-majorana-term-scale: does the pairing structure return M and m^2/M (the seesaw) exactly,
  and is the Majorana term a pairing term of the tower in the store's own sense (fermion-number breaking, quasi-spin)?
  Kill: pairing results hold only at fixed charges. Also bridge lead R5: the commutator of the window number current with
  a pair term on the sixteenth array, and what it does to the 3 | n_g recurrence verdict.

## Cluster C2: harder structure (attackers C2A constructive, C2B adversarial)
- Y1. Hadamard scaling as the curved-field clause of extension of distributions (bridges C2;
  op.qft-loops-and-renormalisation attack item 3): synthesis.hadamard-scaling-limit-premise and the restricted-parametrix
  result against the one-loop vacuum-polarisation extension. First: the scaling degree at the diagonal of the squared
  stored parametrix on a field with nonzero Weyl curvature, and whether it equals the flat degree so the extension count
  (the dimension of the freedom) is the flat one. Success: the clause proved (for the photon vacuum polarisation at one
  loop at least) from stored results; or the exact place the generator-level bounds fail to give the four-dimensional
  degree. Everything about microlocal scaling degree that is not derived is prior art cited from memory and flagged.
- Y2. Equivariant rung counts (bridges R7, N2; op.wall-class-invariant, the new attack item): with the cell model of
  synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure, decide the argued statement
  "on a definite side k = 1 + least j with a Z2-equivariant map from the double cover to S^j" from the stored clauses
  (prove or refute the reduction), then compute the primary obstruction to an equivariant map into S^2 in twisted
  integral H^3 on L^5(4) (stored window 3 <= k <= 6), and go up the obstruction tower as far as exact computation
  reaches. Success: the exact k on L^5(4) definite side, or a narrowed window with the next obstruction named.
- Y3. Order-four anomalies and sixteen components (bridges R6, N1; op.order-four-anomaly-and-sixteen): find in the store
  the order-four element whose square is the grading (the Klein twist) and decide whether the descent preserves it;
  compute the charges of the sixteen arrays of one generation under it; state the consistency condition on RP^5-type
  walls as far as the store's own objects allow (the mod-16 statement is literature cited from memory: Pin+/Z4 bordism
  Z16; do not import it yourself, list it as a decision for Leon), and compute what can be computed exactly: the
  charge sum conditions for 15 against 16 components. Success: a derived necessary condition separating 15 from 16, or
  a statement of exactly which imported theorem the claim would rest on and what remains conjectural.
- Y4. Smaller links, one short test each, findings only unless a result drops out: so(10) level 4 inside su(16) level 1
  and the T-phases of its sectors for n_g copies (C7, N4); helicity as boost weight in
  synthesis.kasner-curvature-wall-is-negative-weight-helicity and hawking.helicity-lift-joints-itemised (R12/C8);
  wall rungs against descent rungs (C5); walls by parallel-tractor type (N5) and recovery maps for the descent's
  conditional expectation (N6) and the edge-mode reading of the vector's Sakharov weight (N7): for these three say what
  the first exact computation gives and whether an open problem is warranted.

## Gate and rules
As BRIEF.md and the previous run (colony/runs/2026-11-09-three/RUN.md "Gate and rules" applies verbatim with this run's
name): check4.py exits 0 with no warnings; validate_one ok
(python3 colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py <dir> colony/runs/2026-11-09-bridges/verify/final);
register with propose_claim; coverage kinds are only exact, complete, sampled, partial; a proposal cannot cite another
proposal. Everything in GA (declare outside_ga otherwise); results derived, not imported; a result that truly rests on
a literature theorem lists it as a decision for Leon. House style: no em dashes; never "honest"/"honestly"/
"load-bearing"; Q(v) for squares; no agent or run names in store text. Credit {name: Claude Fable 5.2, role: proposal
and drafting, source: run 2026-11-09-bridges}. Up to 3 proposals per attacker (4 for C1 if four results are established),
one per target preferred; siblings read each other's findings midway and never file the same result. Lessons from the
previous run's referee, to apply before filing: a sampled check is "computed", not "proved", unless a degree bound or a
basis argument is in the proof; independence claims are "argued" unless both models are checked against the full joint
cone; scope (frame, range of l or n, hypotheses) goes in title, one-liner, statement and lay level alike. Run checks with
PYTHONDONTWRITEBYTECODE=1. One gate process at a time per agent (2 CPUs shared by four attackers: keep scripts light);
never kill other processes; do not edit store/, commit, push, switch branch or spawn agents. sympy is not available.
Findings: findings/attack-<name>.md (C1A, C1B, C2A, C2B), written early and kept current, ending with "Unexpected
links" and "Decisions for Leon".

## Cluster C3, added 22:50 on Leon's decisions (one constructive attacker each; a third blind referee follows)
- Z1 (attacker C3A). Leon asked for the classical topology behind the lower bound k >= 5 on L^5(4) to be derived, not
  imported. The proposal synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five (read it in
  proposals/, and findings/attack-C2A.md, attack-C2B.md sections Y2) proves k <= 5 and reduces k >= 5 to: there is no map
  F: S^5 -> R^4 minus 0 with F(Jv) = -F(v), J the quarter turn; its proof uses (T): Steenrod Sq^2 with the Cartan
  formula, Chern classes with the splitting principle, the cohomology of a Thom space. C2B's second route: four
  components exist iff the quaternionic line bundle L (x) H is trivial (H the even subalgebra of Cl(3,0)), iff a map
  Sigma -> CP^2 -> S^4 is null. Task: derive the one obstruction the proof needs by exact computation in the store's own
  cell model (synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure: the Z4 cell
  complex with its explicit equivariant diagonal), not by quoting the general theory: for example compute the relevant
  Sq^2 as a cup-1 (cup-i) product from an explicit higher diagonal (a chain homotopy between the diagonal and its
  transpose) on the finite complex concerned, or run the equivariant obstruction tower for odd maps to S^3 cell by cell
  (primary obstruction zero, stored; the secondary obstruction as an explicit cocycle), or any other finite exact route.
  State exactly what general background remains assumed (it should be no more than the background (G) of the stored
  cohomology result, plus whatever you must add: name each addition; "obstruction theory identifies the secondary
  obstruction with this cocycle" is an addition and must be said). Success: the non-existence of the odd map as a
  stored-style theorem with exact checks and a strictly smaller, named background than (T); or the exact step at which
  a finite computation cannot replace the general theorem. GA where it is natural (quaternions as an even subalgebra,
  rotors for the deck action); declare outside_ga for the chain-level part. Kill condition to pre-register: the
  secondary obstruction is not computable from the stored diagonal without importing a theorem at least as strong as (T).
- Z2 (attacker C3B). Leon asked for the tensor product in the eviction comparisons to be replaced with geometric
  algebra. Find the stored eviction and Page/Haar comparison results (eviction-keeps-one-replica-saddle,
  eviction-keeps-one-of-catalan-many, the eviction theorem, synthesis.imported-haar-average-purity,
  singularity.imported-page-average-entropy-subsystem, singularity.descent-parity-average, and what cites them; use
  search_claims/find_text/cone). Task: (a) state the GA split: a subsystem is the sub-Clifford algebra generated by a
  subset of the mode generators, reduction is the projection (conditional expectation) onto it, purity is the scalar
  part of rho^2 suitably normalised; (b) prove its relation to the ordinary tensor-product split: the two subalgebras'
  generators anticommute; a Klein twist (stored: find the Klein-twist entities) gives commuting subalgebras and the
  ordinary tensor product; for even states say exactly which reduced quantities agree and which differ; (c) recompute
  each stored comparison on the GA split for the states the store actually uses (after the descent's parity average:
  even states, one parity sector), giving the changed subleading terms exactly (the parity-sector mean purity
  (dA + dB)/(dA dB + 2) is proved in the sibling proposal
  synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector: do not re-file it;
  name it as the intended citation); (d) decide for each stored eviction result whether its statement and proof survive
  unchanged, survive with a changed subleading term, or fail, with exact checks. File: one new claim carrying (a), (b)
  and the dictionary, and corrected versions (version + 1, every stored file kept, amendments entry) of the stored
  comparison results whose text changes, up to three proposals; anything further listed for the maintainer. Leon has
  decided to retire synthesis.imported-haar-average-purity in favour of the derived second moment (sibling proposal
  synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three); say which dependants that
  touches. Kill condition to pre-register: an eviction result whose leading term changes on the GA split.
Gate and rules as above. Findings: findings/attack-C3A.md, attack-C3B.md. Scratch: work/C3A, work/C3B. The two referees
are running: keep to one light process each, never kill other processes.
