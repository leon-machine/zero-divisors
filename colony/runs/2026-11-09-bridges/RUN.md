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
