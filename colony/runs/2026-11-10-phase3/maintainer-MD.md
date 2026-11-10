# Maintainer pass MD, run 2026-11-10-phase3 (10 November 2026)

Scope: MAINTAINER.md section "MD: dark energy, spectrum, gap entries" (D1 to D7). Files of sections MM and MQ were
not touched. In store/open_problems.yaml only op.descent-state-and-spectrum was edited and two entries were added.
No commit, no repin, no lock, no build, no full check, no folder removed, no agent spawned.

## Validation

`tp check --store store --layers 1,2,3 --keep-going --author leon`, last run after all edits:
**1 error, 0 warnings** (baseline 0 / 0). The one error is not on my files:

- `E205 dark-matter.p4-democracy-asymmetry-over-oriented-towers` (the retirement of P4 by MM; it goes when the
  orchestrator removes the folder).

No check.py was changed. Three entities had proof-main.tex and coverage.yaml changed (the new assumes edge recorded
under `untouched_premises`); check4 on each: "0 error(s); check result: pass" (the MacDowell-Mansouri principle, the
GTG-pair result, the Clausius-on-the-action-shell result). store/open_problems.yaml loads (37 entries at my last read; another agent may add to it).

## Entities changed

Each carries `extraction.maintainer_pass_2026_11_10`; each version bump has a credit entry.

- pred.dark-energy-w-minus-one: 4 -> 5 (D1). Kill condition registered as the point (w0, wa) = (-1, 0) excluded at
  five standard deviations by each of two independent surveys, shared CMB prior allowed, published frequentist
  distance, Bayesian evidence recorded beside it; "at any epoch" kept as the model-independent reading under the same
  rule; "the rule is conservative" said at formal, technical, lay and in the threshold. Note "no fallback" labelled
  argued (a search, not a proof), citing the released-norm result and naming the w = -1/4 branch of
  synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands (ii). Observation row 2026-11.
- synthesis.field-space-premise-parallel-frozen-point (FS): 1 -> 2 (D1). Refutation clause (a) carries the same rule
  and the no-fallback sentence; technical, lay and one-liner aligned. Premise unchanged.
- synthesis.number-n-registered-free-input (N): 1 -> 2 (D1). Last refutation clause likewise. No assumes edge added.
- synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part: 4 -> 5 (D2). `assumes` (FS)@2; one sentence in the
  Reading and one in the proof; coverage: untouched premise.
- synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation: 2 -> 3 (D2).
  `assumes` (FS)@2; Reading and proof say so; pin to the MacDowell-Mansouri principle moved 4 -> 5; coverage.
- synthesis.clausius-on-the-action-shell-ties-entropy-density-to-period: 1 -> 2 (D2, a third edge, see below).
  `assumes` (FS)@2; pin to the MacDowell-Mansouri principle moved 4 -> 5; coverage. Text unchanged.
- synthesis.kasner-approach-gives-horizon-exit-and-index-three: 4 -> 5 (D3). The "not covered" sentence (formal,
  technical) points to the Kasner scalar-sector result. Text reference only, no edge.
- synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling: 3 -> 4 (D3). Same
  pointer; its pin to the index-three result moved 4 -> 5.
- pred.gravity-entangles-standard-phase: 1 -> 2 (D5). Scope sentence at all four levels (phase only, no claim about a
  mediator, not a test of a quantised gravitational field, which the series does not hold). Observation row 2026-11,
  verdict pending, status unchanged.
- pred.neutrino-mass-sum-floor: 2 -> 3 (D6). Kill condition: the cosmological bound is read in the model with w = -1,
  the series' own. Note labelled argued on the opposite exposure of the two predictions, taken from the entity's own
  stored observation rows (below 0.049 eV with w = -1, below 0.077 eV with w0, wa free). Prediction unchanged.
- synthesis.norm-released-locally-on-isotropic-fields-tracks-dust-and-never-accelerates: 1 -> 1 (D7). Lineage to
  the index ledger; note sentence.
- synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources: 1 -> 1 (D7). Lineage
  to the released-norm result; the phrase "listed in the run's findings" replaced by a pointer to the open problem;
  pins to the two Kasner results moved to 5 and 4.
- synthesis.scalar-sector-at-the-isotropic-scalar-kasner-point-obeys-the-spectator-equation: 1 -> 1 (D7). The note
  names the index ledger by id (it was "the sibling result, not yet stored"); lineage; pins moved to 5 and 4. No
  uses edge to the ledger: the ledger uses this result, an edge back would be a circle.

store/open_problems.yaml:
- op.descent-state-and-spectrum (D3; this is the exact id): `known` gains "Results and Leon's decision of 10
  November": position kept (no mechanism, free initial data); what was examined (criterion, ledger, Kasner scalar
  sector; moduli, pair channel, density waves, horizon arrays examined and not candidates, argued); the corrected
  statement with the red Kaluza-Klein row at p = 1/2, index -1; the survey labelled argued with the five stored
  index results outside the ledger named; the rule that a future index match counts only with a second number
  (amplitude or running). `source` extended; in `entities` the criterion replaces
  synthesis.local-conversion-cannot-redden-a-gaussian-spectator (the list is at its limit of eight; that result is
  still cited in the text). Status stays `reformulated`, the problem stays open.
- op.strong-cp (new, D4; area standard-model).
- op.matter-asymmetry-origin (new, D4; area dark-matter).
- No entry for a quantised graviton.

## Pins the orchestrator must move (stale after this pass; layers 1-3 raise nothing on them)

- synthesis.field-space-premise-parallel-frozen-point @1 -> @2: dark-energy.vacuum-region-registration-condition
  (assumes).
- synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part @4 -> @5:
  synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared,
  synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff,
  synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise,
  synthesis.inverse-problem-for-the-clausius-route,
  synthesis.curvature-only-tractor-actions-are-macdowell-mansouri,
  synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons,
  synthesis.frozen-point-action-is-bf-transport-broken-by-the-blade-i-wedge-x.
- synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation @2 -> @3:
  synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point.
- synthesis.kasner-approach-gives-horizon-exit-and-index-three @4 -> @5:
  synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching,
  synthesis.kasner-hidden-scale-coupled-scalars-stay-blue.
- synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling @3 -> @4:
  synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching,
  synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point,
  synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt.
- pred.gravity-entangles-standard-phase @1 -> @2: field-theory.operator-newtonian-coupling.
- No pinned dependant found for pred.dark-energy-w-minus-one, pred.neutrino-mass-sum-floor, Premise (N) or the
  Clausius-on-the-action-shell result.

All of these are content-neutral for the dependant: the bumped entities changed only by an added edge, a pointer
sentence or a scope sentence; no clause a dependant cites was altered.

## D2: the future cone of (FS)

Before: 2 entities (the registration condition and the prediction). After: **19** (13 einstein, 4 dark-energy claims,
1 prediction, 1 quantum-fields): the registration condition, the prediction, the three results given an edge, and
14 that reach them through `uses`. Premise (N): cone still 0 (no edge added, as instructed).

## Dependants whose content may be affected (beyond pins)

- dark-energy.vacuum-region-registration-condition (not edited): its formal still says "a confirmed detection of
  w != -1 at any epoch refutes the frozen-point reading, with no parameter available to absorb the result". True as
  the model-independent reading, but it does not carry the registered rule. One sentence there would align it.
- note.programme.setting-falsifiable-claims and the dark-energy setting notes (paper text): they restate the old
  wording of the kill condition. Not edited (notes of the papers).
- neutrino.double-prediction-sum-predicted-floor (conjectured, not edited): its sentence "within the frozen-point
  cosmology" now agrees with the kill condition of the floor prediction; nothing to change.
- (FS)'s own older extraction note (2026-11-01) says "none of them has an assumes edge to it". That is now history;
  the new pass entry says edges were added. The old note was left as written.

## Differences from the instructions, for Leon

1. D2, what the cone of 19 means. The two named results do take (FS) as their field space, and the edges are added.
   But the cone by edges now overstates in the other direction. Fourteen of the 19 are there only through a `uses` chain to one of the three results given an edge (not read one
   by one; for the principle the clauses used are typically (i) to (iii), identities of the functional that are true
   without (FS)). Six of those are the very results (FS) lists as its equivalent readings or as "not supplied by" (slot
   frozen, infinitely stiff, Weyl-squared on transport, parallel on matter regions, inverse-frame-free, duality
   structure): they analyse the premise and do not rest on it. So a refuted (FS) takes, in content, the
   registration condition, the prediction, clause (iv) of the principle, clause (i) of the GTG-pair result read as
   the series' field equations, and premise (A) of the Clausius-on-the-action-shell result; the rest survive as
   mathematics. The text added to the two results says which clauses need the premise. If the cone is to be exact,
   clause (iv) would have to be split off as its own entity carrying the edge; not done (not decided).
2. D2, a third edge. synthesis.clausius-on-the-action-shell-ties-entropy-density-to-period names (FS) in its
   statement as premise (A) and had no edge. I added it (version 1 -> 2). It was not in the list of two; say if it
   should come off.
3. D2, not given an edge: the promoted-norm results that state frame equations with matter under (Mat)
   (synthesis.promoted-norm-weyl-clock-flat-weight, synthesis.promoted-norm-one-global-pair) do not name (FS) and
   their field space is the promoted one; the released-norm result of this run varies the norm, which is outside
   (FS). No edge added to any of them.
4. D1, observation row. Stored only what I read on the web today in the abstracts: DES full survey
   (arXiv:2605.27221: 2.2, 2.3 and 3.0 sigma with the w0, wa values; 2.3 to 3.2 sigma leaving one probe out) and
   DESI DR2 (arXiv:2503.14738: 3.1 sigma with the CMB; 2.8 to 4.2 with a supernova sample). Left out of the row,
   because they are not in an abstract I could read: the DESI w0, wa values, the per-combination table of the DES
   paper, "no single survey exceeds 2.2 sigma" as a general statement, and "no DESI DR3" (my search did not settle
   it; the 2026-10 row already says it).
5. D1, why the w = -1/4 branch is no fallback. The bridge-hunter's numbers (w0 about -0.92, wa about +0.16, a 30 per
   cent mismatch) use density fractions from memory, so they are not stored. The stored text gives the reasons that
   need no outside number: the branch is unadopted, it is a dark-matter component with no pressure derived, it has
   w > -1 at every epoch approaching -1 from above (so wa > 0 and no crossing, against the quadrant of the survey
   fits), and its share grows by the stored factor between 189 and 190 since 1 + z = 1090.
6. D1, "independent". The registered text defines two surveys as independent when their late-time data are disjoint.
   That definition is from the attacker's draft, not from DECISIONS.md. Confirm or reword.
7. D3, the rule's justification. The look-elsewhere figures (14 per cent over 24 trials) are in the findings, not in
   the store; the open problem states the rule with a qualitative reason labelled argued (about two dozen
   parameter-free rows tried, an index range more than a hundred times the three-sigma window, five stored
   one-parameter families that reach the window).
8. D4, strong CP: "what the graph holds: nothing" is true of the angle itself, but the store does hold neighbouring
   structure, which the entry lists (the fifteenth refutation's clause on the theta-term, the mirror's angle equal
   to ours only under a premise, the CPT premise, real breaking for leptons only, one quark-stage result needing a
   phase near a quarter turn). The entry's statement of the bound "below about 10^-10" is the one quoted in the
   stored fifteenth refutation; no new Fact was imported.
9. D4, matter asymmetry: the store already contains a dynamics that generates an asymmetry, the heavy neutrinos.
   It is switched off by the alignment at leading order (proved), by Premise (R) and by the real-breaking postulate,
   not by a theorem. The entry says so and makes the pair's split and widths the first computation.
10. D5: the row uses four arXiv abstracts read today (2507.21211, 2601.06608, 2602.19306, 2604.19696). The reply
    paper does not name the authors of the Nature paper it disputes in its abstract, so the row cites "Nature 646,
    813 (2025)" without names. An et al. and Fuchs et al. were not rechecked and are not in the new row.
11. D6 changes the wording of a kill condition (it now names the model). That is what the instruction asks; flagged
    because a kill condition is a registration.

## Not done

- The "no fallback" sentence in the dark-energy setting note (attack-DA decision 4 suggested it; D1 names only the
  prediction, (FS) and Premise (N)).
- No housekeeping open problem for the dark-energy exposure (attack-DA decision 8; not decided).
- No Fact imported for the Planck running of the index, for newer n_s combinations or for the neutron dipole bound.
- No edit to the stored theorem behind the red Kaluza-Klein row under the graviton position (fixes-SA flag): it is a
  mode of the five-dimensional gravitational field given a vacuum state; the ledger's note already says the result
  does not adopt that as the series' own structure. Left for the pass that works through MQ's list.

## Worth remembering (for the main session)

- The w = -1 kill rule registered on 10 November 2026: two independent surveys, each five sigma on
  (w0, wa) = (-1, 0), shared CMB prior allowed, frequentist distance decides (DECISIONS.md items 1 and 4).
- The series keeps "no mechanism" for the primordial spectrum; a future index match counts only with a second
  number (DECISIONS.md item 8).
