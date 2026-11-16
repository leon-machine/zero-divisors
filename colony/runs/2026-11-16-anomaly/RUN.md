# Run 2026-11-16-anomaly: what is specific to this run

LAB = /home/claude/phys-graph (branch run/2026-11-16-anomaly, from main at 87351bd). Run folder:
colony/runs/2026-11-16-anomaly/ (findings/, work/<name>/, verify/). Read colony/BRIEF.md and colony/POLICIES.md;
this file overrides them. Session name for proposals: 2026-11-16-anomaly. Model for credit entries: Claude Fable 5.2.
LEADS.md in the run folder is the survey that led to the choice of targets.

## Goal
Three problems, one cluster, one idea. Read each in full (labcli get_open_problem) with its linked entities.

- op.strong-cp (never attacked)
- op.matter-asymmetry-origin (run 2026-11-12-asymmetry worked it; read its REPORT.md and findings first)
- op.order-four-anomaly-and-sixteen (runs 2026-11-09-three and 2026-11-09-bridges worked it)

The idea to test on all three: the anomaly of a charge of the sixteen. Locally it is the pairing of a charge with
the pseudoscalar part of a gauge field's square (stored for the triangle:
synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation;
the mixed weak coefficient of the abelian charges is in
synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them). Globally it is the fixed-point count of
the order-four pseudoscalar on a closed five-manifold. The colour pairing bears on the strong CP angle, the weak
pairing on the asymmetry, the global form on the sixteen.

## Targets, in order of priority

### S. op.strong-cp
S1. The colour angle term in the store's language: the grade-four part of the colour field square. Its sign under
    the flag reversal, under the stored CPT conjugation (dark-matter.premise-cpt-covariance,
    synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation) and under the reversal that relates
    this tower to the mirror. State exactly what each premise then says: forces the angle to zero, relates the two
    towers' angles, or says nothing.
S2. The determinant phase. On the stored quark structure (the su(2)_R-covariant completion with Y on c and Y-tilde
    on c*, the bidoublet standard-model.bidoublet-complex, the one-type quark stages of
    synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase, the real-breaking assumption
    neutrino.real-breaking-assumption, the adjoint reading of the CPT conjugation on the quark family matrices)
    compute the phase of det(M_u M_d) as a function of the stored data. Decide: is it fixed, is it zero on any
    stored reading, and is a nonzero Jarlskog invariant compatible with a real determinant there. A real
    determinant alone is half a result; say so.
S3. The colour pairing on charges and on scalar phases. Extend the stored list of abelian charges of the sixteen
    with their colour coefficient. Then the two rung doublets: does the stored rung action (the hypercharge D-term
    action, synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus; the linear field,
    synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum; the level branch) have a phase
    symmetry of the doublets with nonzero colour coefficient (a Peccei-Quinn symmetry)? If it does on some reading
    of the second invariant W(N), the neutral normal pair's odd member shifts the angle, the angle relaxes, and
    the field is a weak-scale axion: confront it with the searches (literature with checked references; decay
    constant near the weak scale is long excluded, say by which measurements). If the stored couplings (Y on c and
    Y-tilde on c* together) admit no such charge, prove it. Either way this decides the "relaxing angle" items of
    both op.strong-cp and op.matter-asymmetry-origin and constrains W(N) (op.rung-unit).
S4. The decision. From S1 to S3: the series fixes the physical angle, or it is a free input. If free, draft the
    registration (format of synthesis.matter-asymmetry-registered-free-input) with a refutation condition, as a
    decision for Leon (new postulates are maintainer-only: do not file it, describe it).

### A. op.matter-asymmetry-origin
A1. The anomalous weak process as a selection rule: from the stored mixed weak coefficient, the charges a process
    driven by the weak field's four-form can change (B + L by the number of families times ..., B - L not). The
    existence and rate of the process is literature: find and check the reference; do not import (list as a
    decision).
A2. The equilibrium coefficient c = n_B/(B - L) as exact linear algebra over the rationals: chemical potentials of
    the sixteen per family, the constraints from each equilibrated interaction, hypercharge neutrality. Derive
    the general formula (8 N_f + 4 N_H)/(22 N_f + 13 N_H) and the two values 28/79 and 8/23; state which
    interactions must be in equilibrium. Fix the doublet count on the working (level) branch, where the second
    doublet is heavy, and say what the stored bidoublet's two doublet couplings mean for it. Also the value after
    the weak transition if the process freezes out below it.
A3. The conditional inheritance theorem for B - L (third attack item of the problem): state and prove it with
    every premise named.
A4. The relaxing angle: with S3.

### G. op.order-four-anomaly-and-sixteen
G1. The fixed-point count on real projective five-space, derived in the store and in geometric algebra: spinor
    fields on the unit five-sphere as restrictions of monogenic homogeneous polynomials on the six-space
    (the spherical Dirac operator, its eigenvalues +-(k + 5/2), multiplicities from the Fischer decomposition),
    the lift of the antipodal map to the spinors (the volume element of the six-space, of square -1) combined
    with omega so that the pair has square one, its sign on each eigenspace, and the eta invariant as an
    Abel-summed alternating series. Prove what can be proved exactly (dimension counts, signs, the generating
    function); say plainly which analytic step (the equality of the Abel sum with the eta invariant at zero) is
    argued or imported. Leon's decision of 9 November: the modulo-16 statement of the literature is not imported.
G2. What the count says for content: the phase per Weyl component, sixteen against fifteen, and why the lens
    space L^5(4) is not the relevant space (the stored remark: an order-eight structure). The step from the
    invariant to a consistency condition on walls (that the phase is the anomaly) is literature: name it, check
    the reference, and state the result as conditional on it.
G3. The link asked for by the problem: tie it to the wall theory (synthesis.wall-rung-count-is-height-of-dying-line-class
    on real projective walls) or show that no stored structure makes the tie.

## Run-specific rules
- One cluster, two attackers: attack-A (constructive) and attack-B (cross-pollinating and adversarial: counter-
  models, independence, refutations, circularity, literature checks at source with web search). B concentrates on
  breaking what the idea claims: a hidden Peccei-Quinn charge the store overlooked or its absence, a determinant
  phase that contradicts the neutron bound on a stored reading (that would be a refutation of a stored reading
  and is a first-class result), the wrong space or structure in G.
- Division to avoid duplicates: A files S2, A2, A3, G1. B files S1, S3, G2/G3 and anything adversarial. Each reads
  the other's findings file midway. At most 3 proposals each.
- Geometric algebra throughout; no imaginary unit where a pseudoscalar or bivector does the work (declare
  outside_ga where it cannot).
- Web search is allowed for checking literature at source. Quote nothing at length; cite.
- Do not edit store/. Do not commit or push. Do not run tp check. One gate process at a time each.
- The orchestrator reads your findings file while you work: keep it current, results labelled
  proved / computed / argued / conjectured.
