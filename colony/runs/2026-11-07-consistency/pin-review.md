# Run 2026-11-07-consistency: pin review (agent PR1)

Acting for Leon as maintainer under PIN_REVIEW.md. No commits, no agents spawned, one tp check run.

## Counts

| | pins |
|---|---|
| Stale pins in scope at start (store-wide) | 751 |
| Skipped: dependant on a GTG list (gtg_1/2/3.txt) | 70 (on 27 dependants, listed below) |
| N repinned (notation only) | 571 + 5 follow-up (see below) = 576 |
| R repinned (use holds as cited, note added) | 106 |
| R updated (quotation of the old statement updated, then repinned) | 4 |
| R left (use no longer holds) | 0 |

Follow-up: two dependants were bumped for their quotation updates (dark-matter.asymmetry-arrow-counted-fifteenth-refutation
5 -> 6, synthesis.tower-charge-sector-label-temperature-not 4 -> 5). The five entities pinning asymmetry-arrow@5
(mirror-share-assembled, stored-asymmetry-charge-not-number, neutrino.imported-ceiling-under-hypothesis-u-arrow,
one-relation.imported-flag-arrow-superselection, one-relation.record-chain-votes-measurement-without-collapse) were
repinned to @6 as N (only a "not claimed" remark changed; none of them uses it). Nothing pinned tower-charge@4.

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`: 0 errors, 0 warnings
(108 information findings, I213 subject notices and I305). After the review the only stale pins in the store are the
70 skipped GTG ones.

## Method

Every stale pin's version equals the target's version in store/.tp-lock.json, so the old formal statement was taken
from the lock commit (79c425d) and compared with the current formal; status and assumes edges were compared with the
lock entry. 211 targets: 46 have a formal unchanged byte for byte (bumped for proofs, checks, links or edges), 2 are
equal after normalising notation.yaml macros, the units i/I_4/I_5/I_7/J and whitespace, and 163 differ. I read all
163 diffs. 134 are notation: GA rewrites with the component form kept as a labelled reading, units named by the unit
principle, "which unit acts where" sentences, the store's curvature sign named (values unchanged), version labels for
(Q), (HS), C_loc, citation and key changes. 29 are R (decided restatements C1, B2, B3, C2, B6, A3, G1, G2, G3, H2, A7,
A15, and six corrections to a clause or constant; I counted a few clarifications that touch a clause, such as the
corner lemma's stated setting, as R to be safe). For every R pin I read the dependant's citations, proof steps and
premise() calls of that target. Each R dependant has an extraction note `maintainer_pass_pin_review` with one sentence
per reviewed target naming the change.

Repins touch only `- id@n` lines under derivations/specialises/supports (one identical line inside a merged-entity
record in singularity.descent-parity-average's extraction was left as history). Pins are outside the substantive
hash, so repins and notes need no bump; the four quotation updates are text changes and were bumped once relative to
the lock where needed, each with a credit entry (source: maintainer pass 2026-11-07 (pin review)).

## R pins (one line per dependant and target; mass.weight-polynomial-two-series pins its target in two derivations)

- dark-matter.asymmetry-arrow-counted-fifteenth-refutation -> dark-matter.imported-trichotomy-descents-data 5->6 [clause (2) restated]: holds as cited; repinned, note added
- dark-matter.asymmetry-arrow-counted-fifteenth-refutation -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: UPDATED: formal (ii)'s remark on the mirror's angle named P2 for (iv); now the common ceiling coupling. v5 -> v6
- dark-matter.coefficients-floors-they-give-what-gravity -> dark-matter.imported-massless-graviton-production-rate 1->2 [F14: reduced Planck mass written bar M_P]: holds as cited; repinned, note added
- dark-matter.coefficients-floors-they-give-what-gravity -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-matter.imported-gravity-only-coupling -> dark-energy.acoustic-no-go-one-way-grip 5->6 [H2: no channel outside the C-even neutral sector]: holds as cited; repinned, note added
- dark-matter.mirror-share-assembled -> dark-matter.mirror-share-one-how-fragile 6->7 [C1: (i) rests on the ceiling-coupling premise]: holds as cited; repinned, note added
- dark-matter.mirror-share-assembled -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-matter.mirror-share-assembled -> dark-matter.population-count-one-share-half-percent 5->6 [C1: share of one rests also on the ceiling-coupling premise]: holds as cited; repinned, note added
- dark-matter.mirror-share-assembled -> dark-matter.stored-asymmetry-charge-not-number 8->9 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- dark-matter.mirror-share-one-how-fragile -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-matter.mirror-share-one-how-fragile -> dark-matter.no-coupling-rule-odd-towers-follows 4->5 [B2: formal is three facts; "no rule follows" moved to a remark]: holds as cited; repinned, note added
- dark-matter.mode-counts-two-modules-which-one -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-matter.no-coupling-rule-odd-towers-follows -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-matter.open-channels-their-costs -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-matter.population-count-one-share-half-percent -> dark-matter.mirror-share-one-how-fragile 6->7 [C1: (i) rests on the ceiling-coupling premise]: holds as cited; repinned, note added
- dark-matter.population-count-one-share-half-percent -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-matter.population-count-one-share-half-percent -> dark-matter.no-coupling-rule-odd-towers-follows 4->5 [B2: formal is three facts; "no rule follows" moved to a remark]: UPDATED: (iii) formal and technical quoted 'no rule follows from the series'; now cites facts (b), (c). v6 kept
- dark-matter.population-count-one-share-half-percent -> dark-matter.which-towers-can-carry-arrow 4->5 [C1: ceiling coupling equated for the mirror by the new premise]: holds as cited; repinned, note added
- dark-matter.radiation-audit-what-theorem-closes-what -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-matter.radiation-audit-what-theorem-closes-what -> dark-matter.stored-asymmetry-charge-not-number 8->9 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- dark-matter.seeding-gravity-floor-dark-towers-temperature -> dark-matter.imported-massless-graviton-production-rate 1->2 [F14: reduced Planck mass written bar M_P]: holds as cited; repinned, note added
- dark-matter.stored-asymmetry-charge-not-number -> dark-matter.imported-trichotomy-descents-data 5->6 [clause (2) restated]: holds as cited; repinned, note added
- dark-matter.stored-asymmetry-charge-not-number -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-matter.total-function-thickness -> dark-matter.population-count-one-share-half-percent 5->6 [C1: share of one rests also on the ceiling-coupling premise]: holds as cited; repinned, note added
- dark-tower-matter.mirrors-composition -> dark-matter.stored-asymmetry-charge-not-number 8->9 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- dark-tower-matter.mirrors-composition -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- dark-tower-matter.mirrors-temperature-p2 -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: UPDATED: proof said (iv), (v) rest on P2; now 'as T14 states them (version 8)'. v7 kept
- dark-tower-matter.mirrors-temperature-p2 -> dark-matter.stored-asymmetry-charge-not-number 8->9 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- dark-tower-matter.r1-has-no-mechanism-odd-towers -> dark-matter.mirror-share-one-how-fragile 6->7 [C1: (i) rests on the ceiling-coupling premise]: holds as cited; repinned, note added
- families.three-identical-families-mixing-shared-slots -> families.imported-one-derived-generation-hypothesis-s 6->7 [G3: (S) now derived]: holds as cited; repinned, note added
- interior.unipotency-across-kerr-family -> interior.gauge-trajectory-unipotent-ray 8->9 [(iv): kernel direction e_r null only for the limit form]: holds as cited; repinned, note added
- mass.de-sitter-scale-frozen-point -> mass.imported-thomas-operator 2->3 [(n,0,J) consistency remark corrected]: holds as cited; repinned, note added
- mass.mass-weight-dictionary -> mass.imported-thomas-operator 2->3 [(n,0,J) consistency remark corrected]: holds as cited; repinned, note added
- mass.weight-polynomial-two-series -> mass.imported-unitary-representations-de-sitter-group 4->5 [B6: no-shift normalisation moved out to a hypothesis]: holds as cited; repinned, note added
- neutrino.empty-twistor -> neutrino.imported-derived-content-singlets 7->8 [G3: (S) now derived]: holds as cited; repinned, note added
- neutrino.imported-mass-bracket-quantum-numbers -> neutrino.imported-derived-content-singlets 7->8 [G3: (S) now derived]: holds as cited; repinned, note added
- neutrino.leptogenesis-suppressed-alignment-reheating-premise-new -> neutrino.real-breaking-assumption 1->2 [C2: adds a real charged-lepton matrix]: holds as cited; repinned, note added
- neutrino.seesaw-what-gauge-invariance-proves-what -> neutrino.imported-derived-content-singlets 7->8 [G3: (S) now derived]: holds as cited; repinned, note added
- odd-extensions.imported-copy-theorem-soldered-residue -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- one-relation.overlap-table-sorted -> dark-energy.acoustic-no-go-one-way-grip 5->6 [H2: no channel outside the C-even neutral sector]: holds as cited; repinned, note added
- rule2.imported-rule-2-matrix-units-forgotten -> transport.corner-even-subalgebra 4->5 [setting (p - q = 1 mod 4) stated in the formal]: holds as cited; repinned, note added
- scrambling.epoch-modular-period-two-unknowns-become -> scrambling.area-law-test 4->5 [A15: 1-nat convention stated]: holds as cited; repinned, note added
- scrambling.spreading-law-chaos-bound-saturated -> scrambling.area-law-test 4->5 [A15: 1-nat convention stated]: holds as cited; repinned, note added
- sheaf.schwarzschild-degeneration-boundary-tame -> sheaf.gauge-field-cometric 3->4 [degeneration at r = 0 corrected as above]: holds as cited; repinned, note added
- simulations.halo-shapes -> simulations.imported-mirror 5->6 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- simulations.imported-mirror -> dark-matter.mirror-share-one-how-fragile 6->7 [C1: (i) rests on the ceiling-coupling premise]: holds as cited; repinned, note added
- simulations.imported-mirror -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- simulations.imported-mirror -> dark-matter.radiation-audit-what-theorem-closes-what 7->8 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- simulations.imported-mirror -> dark-matter.stored-asymmetry-charge-not-number 8->9 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- simulations.merger -> simulations.imported-mirror 5->6 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- standard-model.imported-sectors-superselection-mirror-copy -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- synthesis.adiabatic-deposit-modulation-is-a-time-shift -> dark-matter.stored-asymmetry-charge-not-number 8->9 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- synthesis.attachment-transport-is-flat-only-where-weyl-vanishes -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.charged-vaidya-cauchy-horizon-tractor-threshold -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.clausius-on-the-action-shell-ties-entropy-density-to-period -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.cold-mirror-needs-non-equilibrium-descent -> dark-tower-matter.mirrors-temperature-p2 6->7 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.de-sitter-field-fixes-the-observer-tube-point -> synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale 2->3 [A3: signs in (ii)]: holds as cited; repinned, note added
- synthesis.de-sitter-field-fixes-the-observer-tube-point -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.de-sitter-horizon-translation-is-conformal-null-rotation -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.dimmed-burst-time-rescaled-copy -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- synthesis.dirac-causal-propagator-between-nearby-null-leaves-tends-to-the-generator-car-on-every-geodesic-null-hypersurface -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.frozen-phase-spectrum-not-red -> mass.imported-unitary-representations-de-sitter-group 4->5 [B6: no-shift normalisation moved out to a hypothesis]: holds as cited; repinned, note added
- synthesis.frozen-point-geometry-reads-descent-as-vacuum -> mass.imported-unitary-representations-de-sitter-group 4->5 [B6: no-shift normalisation moved out to a hypothesis]: holds as cited; repinned, note added
- synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.gauge-algebra-by-tower -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.hadamard-scaling-limit-premise -> synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field 5->6 [(HS) now a theorem]: holds as cited; repinned, note added
- synthesis.indifference-is-curie-plus-single-valuedness -> dark-tower-matter.mirrors-temperature-p2 6->7 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- synthesis.integrated-loc-curvature-clause-forced-matter-clause-independent -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.kerr-ring-connection-limit-null-rotation-winding-three -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.mirror-asymmetry-route-one -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- synthesis.mirror-asymmetry-route-one -> dark-tower-matter.mirrors-temperature-p2 6->7 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- synthesis.mirror-temperature-measures-deposit-under-r -> dark-matter.stored-asymmetry-charge-not-number 8->9 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- synthesis.mirror-temperature-measures-deposit-under-r -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state -> synthesis.local-normality-at-the-edge-gives-the-null-ground-state 3->4 [A7: ln(9/8) normalisation in (v)]: holds as cited; repinned, note added
- synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants -> synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field 5->6 [(HS) now a theorem]: holds as cited; repinned, note added
- synthesis.operator-join-casimir-shifts -> mass.imported-unitary-representations-de-sitter-group 4->5 [B6: no-shift normalisation moved out to a hypothesis]: holds as cited; repinned, note added
- synthesis.operator-join-point-spectrum-on-positive-energy-modules -> synthesis.operator-join-casimir-shifts 2->3 [B6: (iii) under an explicit, unproved normalisation hypothesis]: holds as cited; repinned, note added
- synthesis.operator-join-positive-energy-no-finite-energy-zero-modes -> synthesis.operator-join-casimir-shifts 2->3 [B6: (iii) under an explicit, unproved normalisation hypothesis]: holds as cited; repinned, note added
- synthesis.operator-join-seed-has-no-diagonal-matrix-elements -> synthesis.operator-join-casimir-shifts 2->3 [B6: (iii) under an explicit, unproved normalisation hypothesis]: holds as cited; repinned, note added
- synthesis.point-spectrum-boost-admits-no-half-sided-translations -> hawking.imported-algebra-boundary-modes-car-algebra 5->6 [charge preserved, not advanced]: holds as cited; repinned, note added
- synthesis.quadratic-flows-cannot-thermalise-descent -> hawking.imported-algebra-boundary-modes-car-algebra 5->6 [charge preserved, not advanced]: holds as cited; repinned, note added
- synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.s-wave-array-is-a-boundary-mode-set -> hawking.imported-algebra-boundary-modes-car-algebra 5->6 [charge preserved, not advanced]: holds as cited; repinned, note added
- synthesis.schwarzschild-horizon-translations-are-no-conformal-symmetry -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.seeding-remainder-excludes-perturbative-pati-salam -> dark-matter.imported-massless-graviton-production-rate 1->2 [F14: reduced Planck mass written bar M_P]: holds as cited; repinned, note added
- synthesis.seeding-remainder-excludes-perturbative-pati-salam -> dark-matter.population-count-one-share-half-percent 5->6 [C1: share of one rests also on the ceiling-coupling premise]: holds as cited; repinned, note added
- synthesis.tower-charge-sector-label-temperature-not -> dark-matter.stored-asymmetry-charge-not-number 8->9 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- synthesis.tower-charge-sector-label-temperature-not -> synthesis.mirror-asymmetry-route-one 2->3 [G2: offered scoping is now P2 v2; (v) has both routes]: UPDATED: Reading and proof said the scoping is 'offered without proof'; now first offered at v2, stated by P2 v2. v4 -> v5
- synthesis.tower-charge-sector-label-temperature-not -> dark-matter.mirror-tower-copy-one 8->9 [C1: (iv) now Premise common-ceiling-coupling; caveat at P2 v1 reach]: holds as cited; repinned, note added
- synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point -> mass.imported-thomas-operator 2->3 [(n,0,J) consistency remark corrected]: holds as cited; repinned, note added
- synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point -> mass.imported-unitary-representations-de-sitter-group 4->5 [B6: no-shift normalisation moved out to a hypothesis]: holds as cited; repinned, note added
- synthesis.twistor-flat-fields-give-nordstrom-not-einstein -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.untuned-fit-caps-lightest-heavy-neutrino -> dark-matter.imported-massless-graviton-production-rate 1->2 [F14: reduced Planck mass written bar M_P]: holds as cited; repinned, note added
- synthesis.weyl-flat-fields-need-no-scaling-limit-premise-and-robertson-walker-generators-see-the-schwarzian -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel -> synthesis.imported-gtg-dictionary 1->2 [(iv) component sign R(g^g) = -R(e^e)]: holds as cited; repinned, note added
- transport.embedding-independent-minimality-fusion -> transport.corner-even-subalgebra 4->5 [setting (p - q = 1 mod 4) stated in the formal]: holds as cited; repinned, note added
- transport.rule-2-ideal-fusion-sharp-form -> transport.corner-even-subalgebra 4->5 [setting (p - q = 1 mod 4) stated in the formal]: holds as cited; repinned, note added
- transport.where-obstruction-lies-commuting-square -> transport.corner-even-subalgebra 4->5 [setting (p - q = 1 mod 4) stated in the formal]: holds as cited; repinned, note added
- pred.no-dark-radiation -> dark-matter.radiation-audit-what-theorem-closes-what 7->8 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- pred.no-indirect-dark-signals -> dark-matter.stored-asymmetry-charge-not-number 8->9 [G1: cold-mirror caveat]: holds as cited; repinned, note added
- pred.no-objective-collapse -> one-relation.record-chain-votes-measurement-without-collapse 6->7 [B3: assumes the recorded-sectors postulate]: holds as cited; repinned, note added

## For Leon

No pin was left: every R use still holds as cited. Points the review raised:

1. The theta angle. dark-matter.asymmetry-arrow-counted-fifteenth-refutation (ii) said the mirror's angle equals ours
   "only by P2 along the reversal orbit (Theorem mirror-tower-copy-one (iv))". At version 9 that (iv) is the
   common-ceiling-coupling premise, whose text covers "every other coupling of the copied theory at M". I read the
   theta angle as such a coupling and changed the remark to name the common ceiling coupling. If you do not count
   theta among those couplings, the remark should say instead that nothing in the store equates the two angles.
2. A possible overstatement in a target (not a pin failure). synthesis.mirror-asymmetry-route-one v3 (iii) says P2
   at version 2 reaches the stored charge "and not the temperature (Theorem tower-charge-sector-label-temperature-not)".
   That theorem says that the scoping leaves xi free on every finite window, and on the full algebra only when the sum
   in its (iii) converges; when infinitely many boundary modes share a frequency band it reaches xi and gives xi = 1.
   Route one's sentence drops that condition. I did not edit the target (outside my brief).
3. 60 of the repinned pins (on non-GTG dependants) point at targets on the GTG lists (for example
   dark-energy.frozen-point-makes-stelle-west-vector@6, synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@3,
   synthesis.tractor-transport-weak-null-crossing@5). I reviewed them against those targets' current text. The fix
   round (FIX_GTG.md) may still edit those targets within their current versions. If a fixer changes a formal
   statement, the dependants of that target need another check.
4. The massless-graviton rate Fact now writes bar M_P. Its dependants still write M_P in the rate, and where they
   evaluate it they use 2.435e18 GeV, the reduced mass. So they agree with the Fact, but the symbols differ (F11/F14
   left that to each entity's next revision).

## Skipped GTG dependants' stale pins (for the orchestrator)

- dark-energy.frozen-point-makes-stelle-west-vector: dark-energy.stelle-west-vector-frozen-point@5 (now 6)
- dark-energy.gravity-pre-metric-forces-degenerate-exactly: dark-energy.frozen-point-makes-stelle-west-vector@5 (now 6)
- dark-energy.walls-free-sector: dark-energy.frozen-point-makes-stelle-west-vector@5 (now 6)
- pairing.curvature-which-loops-move-vacuum: pairing.imported-schwarzschild-connection-curvature@5 (now 6); pairing.imported-weyl-scalars-petrov-type-schwarzschild@2 (now 3); pairing.loop-classes-are-weyl-components@4 (now 5); synthesis.imported-gtg-dictionary@1 (now 2)
- pairing.loop-classes-are-weyl-components: pairing.imported-weyl-scalars-petrov-type-schwarzschild@2 (now 3); synthesis.imported-gtg-dictionary@1 (now 2)
- pairing.regular-frame-class-vanishes-horizon-changes: pairing.imported-schwarzschild-connection-curvature@5 (now 6); pairing.imported-spin-coefficients-null-tetrad@2 (now 3); pairing.two-frames-share-vacuum-selected-transport@5 (now 6)
- pairing.static-frame-only-expansion-survives: pairing.imported-schwarzschild-connection-curvature@5 (now 6); pairing.imported-spin-coefficients-null-tetrad@2 (now 3)
- synthesis.boundary-mode-first-law-of-entanglement: state-selection.partner-purification-are-canonical@4 (now 5)
- synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet: sheaf.gauge-field-cometric@3 (now 4); synthesis.imported-gtg-dictionary@1 (now 2); synthesis.positive-null-energy-gives-r-premises@7 (now 8)
- synthesis.cosmological-horizon-completed-pair: synthesis.de-sitter-static-boost-frozen-point@5 (now 6)
- synthesis.diagonal-kasner-momentum-constraint: dark-energy.variable-exponents-residue-pointwise-corrections-are@4 (now 5); dark-energy.wall-counterterm@4 (now 6)
- synthesis.einstein-condition-is-infinity-vacuum-incidence: interior.imported-tractor-connection@2 (now 3)
- synthesis.euler-entropy-of-a-horizon-patch-is-an-edge-term: dark-energy.wall-counterterm@4 (now 6); synthesis.einstein-equations-from-c-loc-and-clausius@7 (now 8); synthesis.euler-entropy-first-order-rate-on-local-patches@2 (now 3); synthesis.euler-term-horizon-entropy-shift@4 (now 5); synthesis.imported-gauss-bonnet-with-corners-poincare-hopf-and-edge-term@1 (now 2); synthesis.imported-gtg-dictionary@1 (now 2); synthesis.sds-clausius-fixes-area-constant@4 (now 5); synthesis.series-wald-entropy-changes-without-flux-on-local-horizons@2 (now 3)
- synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared: dark-energy.frozen-point-makes-stelle-west-vector@5 (now 6); synthesis.imported-gtg-dictionary@1 (now 2); synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@2 (now 3); synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale@2 (now 3); synthesis.promoted-norm-weyl-clock-flat-weight@6 (now 7)
- synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff: dark-energy.frozen-point-makes-stelle-west-vector@5 (now 6); synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared@2 (now 3); synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@2 (now 3)
- synthesis.kasner-curvature-wall-is-negative-weight-helicity: synthesis.imported-gtg-dictionary@1 (now 2); synthesis.nondiagonal-kasner-residue-weighted-shear@3 (now 4); synthesis.unit-boost-residue-needs-nonpositive-exponent@3 (now 4)
- synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points: synthesis.attachment-transport-is-flat-only-where-weyl-vanishes@2 (now 3); synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching@3 (now 4)
- synthesis.killing-horizon-value-factor-is-the-generator-boost: field-theory.second-quantisation@5 (now 6); synthesis.imported-gtg-dictionary@1 (now 2); transport.group-null-rotations@4 (now 5)
- synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons: dark-energy.frozen-point-makes-stelle-west-vector@5 (now 6); rule2.rule-2-kaluza-klein-algebra@6 (now 7); synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@2 (now 3)
- synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part: dark-energy.frozen-point-makes-stelle-west-vector@5 (now 6); synthesis.einstein-condition-is-infinity-vacuum-incidence@3 (now 4); synthesis.imported-gtg-dictionary@1 (now 2); synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale@3 (now 4); synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale@2 (now 3); synthesis.series-wald-entropy-changes-without-flux-on-local-horizons@2 (now 3)
- synthesis.nondiagonal-kasner-residue-weighted-shear: dark-energy.cosmological-constant-does-not-change-residue@6 (now 7); dark-energy.frozen-point-datum-kasner-wall@7 (now 8); dark-energy.variable-exponents-residue-pointwise-corrections-are@4 (now 5); synthesis.diagonal-kasner-momentum-constraint@3 (now 4)
- synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale: synthesis.imported-gtg-dictionary@1 (now 2); synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale@3 (now 4); synthesis.positive-structure-is-twistor-form-at-imaginary-time@4 (now 5)
- synthesis.promoted-norm-one-global-pair: dark-energy.imported-henneaux-teitelboim-promotion@5 (now 6)
- synthesis.promoted-norm-weyl-clock-flat-weight: dark-energy.frozen-point-datum-kasner-wall@7 (now 8); dark-energy.imported-henneaux-teitelboim-promotion@5 (now 6)
- synthesis.series-wald-entropy-changes-without-flux-on-local-horizons: synthesis.einstein-equations-from-c-loc-and-clausius@7 (now 8); synthesis.euler-term-horizon-entropy-shift@4 (now 5); synthesis.sds-clausius-fixes-area-constant@4 (now 5)
- synthesis.taub-nut-cauchy-horizon-is-taub-point-with-complex-residue: synthesis.imported-gtg-dictionary@1 (now 2)
- synthesis.tractor-transport-weak-null-crossing: interior.imported-tractor-connection@2 (now 3)
