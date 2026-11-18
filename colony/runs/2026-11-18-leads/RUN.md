# Run 2026-11-18-leads: what is specific to this run

LAB = /home/claude/phys-graph (branch run/2026-11-18-leads, from main at 749817ed, after pull request 45). Session
name for proposals: 2026-11-18-leads. Model for credit entries: Claude Fable 5.2. Referee: Claude Opus 5.5, blind.
Baseline: baseline.log (the final check of run 2026-11-18-navigate on the same store: 0 errors, 1 warning).

## Request
Leon, 18 November, 14:04: adopt the computed mean energy per creation event in the gravitational floor ("yes do
that"), and "run through all the leads". Reading taken, stated here because the scope was not put to him: every lead
of the survey of 18 November (LEADS-source.md, sections A, B, C), the leads named in the message on the impact of
the conjecture's refutation, and the open items left by the previous run's report. Leads judged out of reach are
recorded with the reason and not dropped.

## Method
One attacker per cluster, working both the constructive and the adversarial angle (no pairs, no bridge-hunter; the
orchestrator reads all findings and relays links). One blind referee pass on every proposal, a fix round, a second
pass on anything restated. Maintainer work: the energy restatement (MAINTAINER-energy.md, one agent) and the
housekeeping rows (the orchestrator). Proposal cap: three per cluster.

## Clusters
- W, walls. op.eigenbundle-class-of-degenerations (all four attack items), op.wall-class-invariant (what the new
  class says beyond tame walls), op.kerr-ring (first attack item, read against the degree-one class), the link to
  op.order-four-anomaly-and-sixteen, the claim that a wall of even rank jump is invisible to the tower
  classification, and sheaf.wall-class clause (c), which still cites the refuted conjecture.
- G, the gravitational field. op.gravitational-field-at-null-momentum (all four attack items), the trace-free
  channel item of op.einstein-from-the-field-theory read against the operator source, and the basis of
  pred.dimmed-evaporation-bursts (its term g).
- H, heating, couplings and scrambling. (1) the curvature coupling in the heating rate against
  op.curvature-coupling-across-subjects; (2) the trace part of the fermion channel at next order; (3) the two
  scrambling estimates lowered to conjectured on 7 November, against
  synthesis.affine-cell-boost-spreads-without-scrambling.
- L1, horizons. op.which-capacity and op.helicity-per-boundary-mode, starting from the leads of 16 November
  (colony/runs/2026-11-16-anomaly/LEADS.md and that run's REPORT.md).
- L2, values. op.positivity-of-values, same starting point.

## Housekeeping (orchestrator; no proposals)
Row 5 (basis of pred.leptonic-cp-trivial), row 8 (four claims flagged for motivation), row 9 (three conjectured
claims to be listed under their problems), row 10 (the cluster on the number N), the three setting notes quoting
old floor figures, the legacy script and the composition clause that need the papers suite.

## Rules specific to this run
- Entities owned by the energy restatement (do not propose corrections to them; cite them as they stand and say
  in the findings that the floor's numbers are being restated): dark-matter.seeding-gravity-floor-dark-towers-
  temperature, dark-matter.coefficients-floors-they-give-what-gravity, dark-matter.stored-asymmetry-charge-not-number,
  dark-matter.radiation-audit-what-theorem-closes-what, simulations.imported-mirror,
  synthesis.mirror-temperature-measures-deposit-under-r, synthesis.adiabatic-deposit-modulation-is-a-time-shift,
  dark-tower-matter.mirrors-composition, dark-matter.mirror-share-one-how-fragile, simulations.s3-mirror-cluster,
  pred.no-dark-radiation.
- The operator source (OS) is a local hypothesis of the results that use it (Leon's decision of 18 November); do
  not propose it as a premise or a postulate.
- The convention on the graviton stands (no quantum is posited); whether the field has a free part is recorded as
  open (Leon's decision of 18 November). Results may sharpen the question; they may not settle it by fiat.
- Kill conditions are written into the findings file before the computation they govern, and their outcome after.
- A negative result, an independence statement or "out of reach, because" is a full result for a lead.
- Machine: 2 CPUs shared by six agents. Run `runcheck.py` freely; run `check4.py` once per proposal at filing and
  never two at a time; no `tp check`, no `tp build`. Never kill a process you did not start.
