# Run 2026-11-07-consistency: apply agent D1 (Leon's second-round answers 1 to 6)

Acting for Leon as maintainer on DECISIONS.md, "Leon's answers, second round". No commits, no agents spawned,
no processes of others touched. Every changed entity is at its locked version + 1 (store/.tp-lock.json, lock
fb48481), with a credit entry for that version (source "maintainer pass 2026-11-07 (decisions, second round)")
and an extraction note `maintainer_pass_decisions_2` (by maintainer-2026-11-07; what, why, and for a formal change
the exact evidence). Scratch scripts: /tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/D1/
(v_rest.py, v_kasner.py: the verifications; ed.py, apply1-4.py, repin.py, repin2.py: the edits).

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon` (one run, after all edits):
0 errors, 0 warnings store-wide; on my ids only I213 (subject notice, frozen-point-unique). No check.py was changed
(no assertion encoded an old statement; see below), so no runcheck or check4 was needed.

## Items

### Answer 1: the five formal fixes (exact texts of fix-F1.md, fix-F2.md, fix-F3.md, each verified first)

| entity | version | what | verification |
|---|---|---|---|
| synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale | 3 -> 4 | formal (iii): `l = \nabla(t + x_{1}) = e_{0} - e_{1}` null | GA.py, Cl(1,3): H(a) = 2(a.l)l with l = e0 - e1 on e0, e1, e2 and a generic a; e0 + e1 fails; Q(l) = 0, trace H = 0. Proof and check already had e0 - e1. |
| synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part | 3 -> 4 | formal setting: "Let Lambda != 0, and let"; A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V (that is Omega(a) + hb^-1(a) ^ V/Q(V), so D_aV = hb^-1(a) on both branches). The proof's one display of the Cartan connection also changed (l was no longer defined). | GA.py, Cl(2,4), Q(V) = -3/Lambda at Lambda = 3, -3, 3/4, -12: (-(Lambda/3) u ^ V) x V = u and (u ^ V/Q(V)) x V = u; the old form gives -u at Lambda < 0. No check encodes l. |
| pairing.static-frame-only-expansion-survives | 8 -> 9 | formal and technical: "Every class tends to 0 as F -> 0 (the static gauge is not defined on the horizon locus)"; proof's horizon paragraph and the coverage clause follow | class -F(1 - F^2) at M = 1/2: within F of 0 at F = 1/10 ... 10^-6, static coframe e^1 = dr/F unbounded; -48/125 at F = 3/5 unchanged. The check evaluates the polynomial -F + F^3 at 0, which is the limit, so it holds for the new clause; check.py unchanged. |
| synthesis.frozen-point-unique-where-weyl-has-no-kernel | 5 -> 6 | formal: "Consequently, for c != 0, the Einstein scale ..."; proof's Consequences paragraph states c != 0 | GA.py, Cl(2,4): Q(cI) = c^2 Lambda/3 for Lambda = 3, -6/5, 0 and c = 2, -3/2, 0; c = 0 gives I' = 0 with top slot 0 (no Einstein scale). |
| synthesis.nondiagonal-kasner-residue-weighted-shear | 4 -> 5 | formal (i): "omega(gamma_0) = tau^-1 sum_{l<m} antisym(B)_lm gamma_l ^ gamma_m in the sign of the Definition, D_a = a.nabla + Omega(a) x" | Recomputed (FX1 had not): Levi-Civita from the Christoffel symbols of g, independent of the engine's torsion solver, at tau = 32 and 1, p = (-1/5, 2/5, 4/5), x-dependent theta0, three G with entries above and below the diagonal: nabla_{E0} E_m = W x gamma_m for all m with W the stated bivector; -W fails. The existing check already asserts this value. |

### Answer 2: the two scope-only assumes edges
- dark-matter.which-towers-can-carry-arrow 5 -> 6: assumes edge to synthesis.common-ceiling-coupling-premise@1
  dropped; the one-liner's parenthesis naming the premise (added at close-out for W503) reverted to the version-4
  wording; formal and technical keep the scope as a text mention; coverage untouched_premises entry removed.
  holds_given is now P2, P3 (the premise is gone from it); no plain level states it as a condition.
- dark-matter.no-coupling-rule-odd-towers-follows 5 -> 6: direct edge dropped (P2 kept), coverage entry removed;
  the levels keep the premise as part of what (c) states. Note: holds_given still lists the premise, reached
  through dark-matter.mirror-tower-copy-one@9, which assumes it.

### Answer 3 (record only)
- dark-matter.asymmetry-arrow-counted-fifteenth-refutation 6 -> 7: one note recording that Leon confirmed the
  theta-angle reading. Nothing else changed. (The note is not part of the substantive hash; the bump follows the
  brief's every-changed-entity rule and cost five N repins.)

### Answer 4: route one
- synthesis.mirror-asymmetry-route-one 3 -> 4: (iii) now says that in the boundary-mode model of
  tower-charge-sector-label-temperature-not the scoping leaves the temperature free on every finite window, and on
  the full algebra exactly when the Powers-Stormer sum of its (iii) converges, and that with infinitely many modes
  in one band it reaches xi and gives xi = 1, where route one does not stand. The closing paragraph, the proof's
  Step 4, technical, lay and one-liner carry the same scope. The citation stays text-only (tower-charge pins
  route-one). Evidence: tower-charge's current statement (v5) read clause by clause.

### Answer 5 (record only)
- No edge from synthesis.series-wald-entropy-changes-without-flux-on-local-horizons or
  synthesis.euler-entropy-of-a-horizon-patch-is-an-edge-term to synthesis.c-loc-local-horizon-premise; no entity
  changed. Their extraction notes still say "listed for Leon"; that wording is historical and was left.

### Answer 6: the frozen-point Fact
- dark-energy.imported-frozen-point-geometry 6 -> 7: the formal's sentence naming
  synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection is now a marked remark after the provenance
  ("text only, not part of the Fact"; that theorem rests on the Fact through dark-energy.stelle-west-vector-frozen-point);
  the Fact states the connection by its scale-g display only. Technical, proof opening, lay and one-liner follow.
  No edge existed; check unchanged.
- Consequence: synthesis.two-frozen-points-conformally-flat 4 -> 5 took its flat-scale gauge field from that
  sentence. Its proof now reads the Fact's display at P = 0 and shows, with the computation it already made, that
  Omega_T(a) = -ninf ^ a reproduces it slot by slot. Statement and check unchanged.

## Pins reviewed

Pins are outside the substantive hash, so a repin needed no version bump (and none cascaded). 36 pins on 33
dependants of the bumped entities, all reviewed against the dependant's use: 33 on 31 dependants repinned here,
3 on 2 dependants passed to D2; 0 left for Leon.
- N (5): asymmetry-arrow 6 -> 7 in mirror-share-assembled, stored-asymmetry-charge-not-number,
  neutrino.imported-ceiling-under-hypothesis-u-arrow, one-relation.imported-flag-arrow-superselection,
  one-relation.record-chain-votes-measurement-without-collapse.
- R, use holds, repinned (27), with a sentence in `maintainer_pass_pin_review` (or in my own entities'
  `maintainer_pass_decisions_2`):
  - positive-structure 3 -> 4: de-sitter-field-fixes-the-observer-tube-point ((i) cited), macdowell-mansouri ((ii) cited).
  - macdowell-mansouri 3 -> 4: clausius-on-the-action-shell, parallel-frozen-point-on-matter-regions, inverse-problem-for-the-clausius-route,
    curvature-only-tractor-actions, macdowell-mansouri-is-the-frozen-point-reduction, frozen-point-field-space-is-the-gtg-pair,
    frozen-point-action-is-bf (each cites (i), (ii), (iv) or the sign convention).
  - static-frame 8 -> 9: two-frames-share-vacuum (classes along e0 on r > 2M).
  - nondiagonal-kasner 4 -> 5: kasner-curvature-wall ((ii), (iv), the Gauss identity of its proof).
  - which-towers 5 -> 6 and no-coupling-rule 5 -> 6: population-count-one-share-half-percent (both), mirror-share-one-how-fragile.
  - route-one 3 -> 4: tower-charge-sector-label-temperature-not (its Reading quotes only route one's version-2 offering).
  - frozen-point-geometry 6 -> 7: vacuum-region-registration-condition, odd-extensions.imported-frozen-point,
    frozen-point-unique, standard-model.imported-norm-frozen-point-not-field, under-action-written-norm-parameter-laws,
    frozen-point-makes-stelle-west-vector, parallel-frozen-point-on-matter-regions, imported-frozen-point-de-sitter-radius,
    stelle-west-norm-is-no-local-output, stelle-west-vector-frozen-point, cosmological-horizon-completed-pair,
    odd-extensions.imported-frozen-point-degenerate-algebras (each uses parallelism, Q(I), the stabilisers, the display
    or the Schouten tensor, all unchanged).
- R, quotation updated (1): two-frozen-points-conformally-flat (above).
- Passed to D2 (items-for-D2.md, 3 pins): frozen-point-integrand (positive-structure@3, macdowell@3) and
  frozen-point-reduces (macdowell@3); reviewed, the uses hold, D2 to repin.

## Not applied exactly, and why
- macdowell-mansouri: beyond fix-F2.md's two formal replacements, the proof's display Omega(a) - hb^-1(a) ^ V/l^2
  was rewritten the same way, since the formal no longer defines l.
- static-frame: the brief's "fix any check that encodes the old statement" did not apply (the check evaluates the
  limit polynomial); only coverage.yaml's clause text changed.

## For Leon (noticed, not acted on)
- The same anti-de Sitter sign may affect other texts with A = Omega - hb^-1 ^ V/l^2:
  dark-energy.imported-macdowell-mansouri-theorem-stelle-west (l from the unit vector V/l),
  dark-energy.frozen-point-makes-stelle-west-vector ("D + e ^ V/Q(V), on flat spacetime Omega(a) - hb^-1(a) ^ V/l^2"),
  odd-extensions.imported-frozen-point, synthesis.macdowell-mansouri-is-the-frozen-point-reduction-... and
  synthesis.frozen-point-action-is-bf-.... e ^ V/Q(V) = -e ^ V/l^2 holds only if Q(V) = -l^2, the de Sitter branch.
  Not checked further (outside this share).
