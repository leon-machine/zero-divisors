# Run 2026-11-09-solvable: report

Leon asked for the open problems that can be solved, with new routes. A triage of all 32 picked four clusters: topology
and horizon modes, algebra and gauge loose ends, a mod-24 lead on generations, and an independence sweep over free numbers.
Method: two attackers per cluster (8), a bridge-hunter, two blind referees, one fix round, two maintainer agents,
close-out. Fifteen results accepted (two after restatement). No problem changed status; several attack items closed.

## Accepted
C1 topology and horizon modes
- synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial (SOUND WITH FIXES): k <= 2 forces L + L stably trivial;
  on L^{2m+1}(4) the spin class q1(L + L) = 2y^2 != 0, so k >= 3 > ht = 2 on every side from dimension 5; conditional on
  classical lens-space facts cited from memory (Leon: derive, not import).
- synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height (SOUND WITH FIXES): a k-rung completion forces
  2^{k-1}(1 - xi) = 0 in K(Sigma); k >= 1 + floor(n/2) on L^{2n+1}(4), unbounded at fixed ht = 2; conditional likewise.
  The triage's Adams/RP^n lead was irrelevant (on RP^n ht = e).
- synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional (SOUND WITH FIXES; one failing step
  repaired): J3's channel-reduction clause derived in GA (static GTG gauge) for spins 0, 1/2, 1, no import; spin 1/2
  decays as e^{kappa r_*} (order sqrt f), correcting the stored text; not uniform in l.
- op.odd-towers item 1: already answered in the store (no proposal).
C2 algebra and gauge
- synthesis.gauge-factor-sugawara-parts-satisfy-virasoro-relations-on-the-band (SOUND): Virasoro on the band domain
  with c = 32/7, 2, 1, 1 and coset 52/7; no Virasoro algebra on a finite window.
- synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge (SOUND WITH FIXES): the two-doublet
  differential, 't Hooft gauge exactness and mixing cancellation; common masses at a stationary vacuum.
- synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets (SOUND WITH FIXES): BRST holds at every
  vacuum; Goldstone rank 0, 3, 4; the pattern comes from the potential.
- synthesis.joint-clifford-clause-is-an-instance-of-the-signed-direction-postulates (SOUND WITH FIXES): clause (f) of the
  slot-module hypothesis is (F2) and (F3) once the twisted Majoranas are declared the directions.
- synthesis.koide-middle-mass-bound-closes-the-remaining-quark-dressing-class (SOUND WITH FIXES): Koide triples have
  middle/largest >= 17/2 - 6 sqrt 2; no up-quark triple below the charm mass satisfies Koide.
C3 mod-24 lead
- synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays (SOUND WITH FIXES): U =
  e^{2 pi J n/24} Gamma on a window; U = Gamma iff 24 | n; a choice, independent of the cone by two models (n_g = 1, 3);
  under J3, 3 | n_g. Prior art: Wang arXiv:2312.14928; Garcia-Etxebarria and Montero (Z9 baryon triality).
- synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content (OVERSTATED, restated; Leon
  accepted): with additive bosons c = 16 n_g + 2 n_V + n_s + 2 eps (two doublets fail at n_g = 3; a graviton fails all);
  under J3, c = 16 n_g and 3 | n_g. Leon: a test, not a premise.
C4 independence sweep
- synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free (OVERSTATED, restated; Leon accepted): the window is
  free at residues 3 and 5 (ratio about 9.94 in the second model); at residues 1 and 7 Premise U fixes the lowest member.
- synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3 (SOUND WITH FIXES): on the orbit reading of licensing; the fit
  moves to eps (5.364 at eps about 0.917).
- synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping (SOUND WITH FIXES).
- synthesis.georgi-jarlskog-weight-free-on-the-stored-relations (SOUND WITH FIXES): the second family's factor 3 is an
  input of the record.
- synthesis.d-term-level-free-at-fixed-n (SOUND WITH FIXES): xi G free at fixed N, consistent with the register.

## Leon's decisions
Lens-space facts derived, not imported (results conditional; attack item added); recurrence a test only; clause (f)
restated as (F2)-(F3); J3 narrowed; both restated proposals accepted; assumes edges added ((Q) v3, the window reading, C2,
Premise U); open-problem bookkeeping applied.

## Maintainer pass
J3 v2: channel reduction premise for spin 2 only, the current-boson identification and partial-wave lift premise for
every field (narrower than "spin 2 only": the derivation proves the channel clause, not the identification); dependants
restated or noted (helicity-lift joints v6, the two collapse results, hyp-s-slot-statistics v10). Slot-module hypothesis
v5 clause (f). Wording fixes: Koide dressing (iv) v2, stored-asymmetry v10, R2 v3, P3 v3 note, lens-space wall v6, rung
unit v4 note. Thirteen open problems updated (known, attack items, entities, source); no status changed. 97 edges
repinned; W405 on the new assumes premises excused in coverage.yaml (Premise U touched in the Bott check).

## Checks
Baseline 0 errors 0 warnings. Final gate: all fifteen check4 exit 0, no warnings; validate ok; style clean. Final tp check
0 errors 0 warnings; build 0 errors; layout, site, lock; 394 tests OK (1 skipped).

## Costs (approximate subagent tokens)
Attackers with fixes about 2.98M, bridge 0.20M, referees 0.80M, maintainers 0.55M: about 4.5M.
