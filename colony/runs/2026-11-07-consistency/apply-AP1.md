# Run 2026-11-07-consistency: apply agent AP1 (categories A, G, H)

Acting for Leon as maintainer on DECISIONS.md (Leon's answer 1: apply all A and the routine items). Every changed
entity has a credit entry for its version (source: maintainer pass 2026-11-07 (decisions)) and an extraction note
`maintainer_pass_decisions` (by maintainer-2026-11-07); wording-only edits (lay, one-liner, title, subject,
extraction) kept the version. Versions are relative to store/.tp-lock.json; an entity already raised in this run
kept its version. No commits, no retirements, no status changes; every file kept.

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`, run twice. Final run:
5 errors, none on an AP1 entity (E107/E108 on the two scrambling conjectures, AP2's B1 in progress; E206 on
synthesis.positive-structure-..., a GTG prover's edit in progress). Only I213 subject notices on AP1 ids.

## A. Formal corrections

- A1 synthesis.quadratic-flows-cannot-thermalise-descent 2 -> 3: coherence C_ij = omega(a_j^* a_i) gets e^{-J(omega_i - omega_j)t}; ga_units note marked superseded.
- A2 synthesis.boost-evolution-on-generators-is-one-unitary-group 4 -> 5: alpha_l(a(f)) = a(D_{-l} f) (substitution written out in proof (ii)); antilinear step in proof (iii); "time parameter reversed".
- A3 synthesis.positive-structure-... (gtg_3): passed to items-for-gtg.md with the evidence and R03's text.
- A4 rule2.where-obstruction-sits-commuting-square 5 -> 6: ladder pair f = (1/2)(u +- w), u of square +1, as the twin (formal, technical).
- A5 synthesis.schwarzschild-horizon-translations-are-no-conformal-symmetry 1 -> 2: outgoing gauge, past horizon, white-hole interior; (v) lambda -> e^{-kappa tau} lambda; proof (iv) in u = t - r with g = f du^2 + 2 du dr - r^2 dsigma^2; proof (v) d lambda/du = c e^{-kappa u}; future horizon by time reflection; "Beyond one flat chart" sentence; flag updated. check.py unchanged by A5.
- A6 synthesis.killing-horizon-value-factor-... (gtg_1): passed to items-for-gtg.md.
- A7 synthesis.local-normality-at-the-edge-gives-the-null-ground-state 4 (kept): ln(9/8) stated for |2 pi R/I_4|^2.
- A8 odd-extensions.transport-constrains-frozen-point-only-through 2 -> 3: phi orthogonal to the Lorentz frame of W (formal, technical).
- A9 synthesis.frozen-point-geometry-reads-descent-as-vacuum 2 -> 3 and standard-model.dating-descent 5 -> 6: "> 4e9 at 1 MeV (> 7e9 for k >= a_0H_0)"; the proof now covers k from 2/eta_0 (0.627 x 10^12/168 / 0.83 > 4.49e9, recomputed in Fractions from the check's inputs).
- A10 note.sheaf.wall-class-posed 1 -> 2: dated bracket (the rung leaves both clock positions unchanged). The clause (b) fix on sheaf.wall-class went to items-for-AP2.md (AP2 claimed it for B4).
- A11 synthesis.macdowell-mansouri-... (gtg_1): already applied by the forms rewriter (v3, F = -calW); recorded in items-for-gtg.md as nothing to do.
- A12 synthesis.electron-positron-...: already applied in round 2 (formal (1) has the full spin-sum rule); no edit.
- A13 note.programme.setting-series-paper-paper-2 4 -> 5: T15 row "(the filled twistor, at Y = -1, is e_R, the conjugate of e^c)".
- A14 dark-matter.open-channels-their-costs 5 -> 6: 6.40 -> 6.43 ((8/7)(11/4)^{4/3} + 2(3.044/3) = 6.43254; threshold 0.4647, still 0.47). The check asserted the old value: fixed exactly (p + 2 NNU/3 in (6.432537, 6.432539), threshold in (0.464712, 0.464713)); runcheck pass, check4 on a proposals/ copy 0 errors (copy deleted). G1 applied in the same bump.
- A15 scrambling.area-law-test 4 -> 5: the 1-nat convention and nu Delta t = M/(2 ln 2) stated in the formal.
- A16 dark-energy.wall-counterterm 6 (kept, note only): see "Could not apply exactly".

## G. Stale wording

- G1 (cold mirror an exception to P2 at its version-1 reach; P2 as scoped leaves xi free; non-equilibrium descent), each with formal sentence and, where present, technical and lay sentences: dark-matter.open-channels-their-costs 5 -> 6, dark-matter.radiation-audit-what-theorem-closes-what 7 -> 8, dark-matter.stored-asymmetry-charge-not-number 9 (kept), dark-tower-matter.mirror-against-record 2 -> 3, dark-tower-matter.mirrors-temperature-p2 6 -> 7, dark-tower-matter.towers-built 1 -> 2, simulations.imported-mirror 5 -> 6, pred.no-dark-radiation 2 -> 3; dated brackets in note.dark-tower-matter.abstract 1 -> 2, note.dark-tower-matter.setting-contribution 1 -> 2, note.dark-tower-matter.setting-what-note-depends-what-would 1 -> 2. dark-matter.mirror-tower-copy-one was done by AP2 (claimed). Under Leon's answer 2 (P2 unchanged) the sentence stands.
- G2 synthesis.mirror-asymmetry-route-one 2 -> 3: (iii), close, technical, proof Step 4, lay and one-liner: P2 at version 2 states the scoping, so clause (v) has both routes; no assumes edge.
- G3 families.imported-one-derived-generation-hypothesis-s 6 -> 7, neutrino.imported-derived-content-singlets 7 -> 8 ((S) derived from the slot-module premise; paper sentence stays in source_formal); dated brackets in note.standard-model.setting-content-charges-chirality-2 2 -> 3 (also the thirteenth-generator sentence against standard-model.under-s-composites-state-space-spinor (3)(b)), note.standard-model.setting-introduction 2 -> 3, note.standard-model.setting-successor-problems 2 -> 3, note.neutrino.setting-position-series 1 -> 2.
- G4 standard-model.trichotomy-what-kind-number 11 (kept), standard-model.what 3 -> 4: "which the store adopts (programme.n-parameter-of-the-laws)".
- G5 singularity.sheaf-assembly-sheaf 3 -> 4 (R09's sentence, formal and technical); note.three-routes.setting-metric-level-sheaf 1 -> 2 (dated bracket).
- G6 synthesis.series-wald-... (gtg_2): passed to items-for-gtg.md.
- G7 "(Q) version 2" labels: angle.imported-singularity-papers-state-selection 12 -> 13, singularity.bosonisation-bridge-s-wave-sector 7 -> 8 (Planck value holds at both offsets: the sum telescopes for every offset, checked by hand), synthesis.array-ln2-is-zero-mode-doublet-one-tower 4 -> 5, synthesis.boundary-mode-premises-finite-models 4 -> 5, obj.hawking.boundary-mode-algebra-windows-boost-dynamics 3 -> 4, singularity.universality-temperature-under-g 3 -> 4; the store-wide search found one more, dark-energy.acoustic-no-go-one-way-grip (proof), labelled with H2.
- G8 scrambling.return-delay-...: done by AP2 with B1 (its items file says so).
- G9 new remark note.tower.odd-charge-settled (v1, comments_on q.tower.odd-charge and synthesis.tower-limit-forgets-residue); T03's paper text left as written.
- G10 families.imported-dictionary-exact-join 6 -> 7: massless locus B_Lambda = 0 and h = 0, citing mass.exact-join (5) (formal, technical, proof).
- G11 dated brackets: note.dark-matter.setting-levels-results 1 -> 2, note.dark-matter.setting-predictions-collected 2 -> 3 (D = 2 - g/(1+g)), note.mass.setting-successor-problems 2 -> 3 (many-twistor join proved).
- G12 synthesis.hadamard-scaling-limit-premise 6 -> 7: "Statement version 4 (the current statement)".
- G13 standard-model.pair-count-dimension (extraction only, 4 kept): ga_units note marked superseded; singularity.pseudo-inverse-identities-hyperbolic-atom (extraction only, 4 kept): stale unit_note marked superseded; note.dark-energy.setting-machine-verification CS letter already done by the forms rewriter; q.tower.odd-charge typing note left as history.

## H. Anything else

- H1 "i = I_4" named as the unit I_4: field-theory.coupled-system-tree-level 3 -> 4, field-theory.elementary-photon-ga 4 -> 5, field-theory.fock-space-maxwell-modes 4 -> 5, field-theory.mass 5 (title and one-liner only, kept), field-theory.orientation-relocated 6 -> 7, field-theory.second-quantisation 5 -> 6, synthesis.field-level-brst-... 2 -> 3, synthesis.light-ray-good-part-... 4 -> 5, synthesis.linear-rung-field-... 4 (one-liner only, kept), synthesis.modular-period-on-values-... 4 -> 5, synthesis.one-loop-running-coefficients-... 3 (kept), synthesis.quartet-homotopy-... 3 -> 4, synthesis.unit-i4-keeps-its-three-properties-... 2 -> 3 (title "The unit $I_4$ keeps its properties ..."), synthesis.wedge-reflections-compose-... 4 -> 5, obj.field-theory.single-algebra-field 1 -> 2, notes note.field-theory.choice-unit, setting-decisions-taken, setting-introduction, setting-what-series-own (each 1 -> 2), note.field-theory.what-does-t12 2 -> 3. Extraction notes and source_formal untouched; the regex hits on "\psi = I_4" were excluded.
- H2 dark-energy.acoustic-no-go-one-way-grip 5 -> 6 ("no channel outside the C-even neutral sector"); singularity.non-removability-invariant-argument and synthesis.euler-entropy-first-order-rate-on-local-patches were already fixed in round 2 / by the forms rewriter (no edit).
- H3 nothing left: standard-model.connection-forced and dark-energy.wall-counterterm rewritten by the forms rewriter; pairing.two-frames-share-vacuum-selected-transport restated in GTG (no Lorentz matrix left); three-routes.support-preserving-families-... a false positive (ga2-matrices).
- H4 ga-forms.md is now present and covers its list; remaining reader item applied: synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise 3 (kept): sentence stating that its siblings' dilation slot beta(a) ninf ^ n0 has the opposite sign of beta. W222 index false positives cleared by the rewrite.
- H5 applied: synthesis.duality-complex-structure-does-not-reach-the-frozen-point 3 (kept; i_4, i_6 -> I_4, I_6), dark-matter.residue-soldered-invariant-not-algebraic-one 3 -> 4 (\Mat_2(\HH)), synthesis.restricted-dirac-hadamard-parametrix-... 4 (kept; R02's H_+ sentence), mass.casimir-form-join 8 (kept; E wording), rule2.rule-2-kaluza-klein-algebra 6 -> 7 (gamma = e_0e_1e_2e_3 defined), interior.exact-parallelism-convergence-rate 6 (kept; the two frames named), families.rigidity-pairing-sector-one-event 5 (kept; the two epsilons named). Passed: normality-on-the-closed-generator J/nu to AP2; cosmological-horizon-completed-pair and collapsing-hole-flux normalisation sentences to the GTG provers. Deferred (see below).
- H6 done in round 2 (ga2-matrices: span{1, I_4} or span{1, J} tied at first use); imports keep source form (U4). No edit.
- H7 done in round 2 (declarations present). No edit.
- H8, H9, H14, H15: no action by decision.
- H10 mass.chart-form-spin-isomorphism already has one source_formal key. No edit.
- H11 repins: 219 pins moved on 177 dependants (only pin lines; no substantive hash change). Scope: dependants not owned by AP2 or the GTG provers, pinning a target whose formal text is unchanged since the lock (correction, proof or check bumps), plus the targets of AP1's own restatements after reading each dependant for text that quotes the changed statement (none did): A1, A2, A4, A5, A7, A8, A9, A14, A15, G10, H2's targets. Excluded: every target claimed by AP2 or on a GTG list (still changing within its kept version), synthesis.mirror-asymmetry-route-one (its dependant synthesis.tower-charge-sector-label-temperature-not reads the v2 "offered and not proved" scoping), and one pin not on a single line (singularity.finite-truncation-meet-big-fibres-equals -> singularity.p-reduced-metric-level-reading-many@6). Log: /tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/ap1/repin.log.
- H12 subjects moved (non-substantive, versions kept): synthesis.incidence-vacua-entanglement-light-cones-of-unit-diamond -> conformal-spacetime, synthesis.state-selection-r-and-le-against-t05 -> descent.
- H13 note.simulations.setting-introduction-5 1 -> 2: the empty "()" dropped.

## Items from AP2 applied here

- B1 consequence on synthesis.boost-evolution-...: the uses edge to scrambling.spreading-law-chaos-bound-saturated removed (text kept as a mention), the check's premise() call removed; runcheck pass, check4 0 errors (copy deleted). This cleared the E204 cascade on modular-period and wedge-reflections.
- D1 on synthesis.schwarzschild-horizon-translations-...: positive-null-energy@7 -> null-vacuum-on-a-horizon-generator@1 (i) in uses, formal (v), proof (v) and check.py's premise(); runcheck pass, check4 0 errors (copy deleted).

## Passed to others

- items-for-gtg.md: A3 (with the check instruction), A6, A11 (nothing to do), G6, H5 notation for synthesis.cosmological-horizon-completed-pair and synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet.
- items-for-AP2.md: A10 clause (b) of sheaf.wall-class; H5 J/nu notation in synthesis.normality-on-the-closed-generator-....

## Could not apply exactly, or deferred

1. A16 dark-energy.wall-counterterm: the proposed fix ("omega^{ab} are the Cartan forms, minus Omega on vectors") is not what the computation supports. In lib/GA.py and lib/gtg.py with Fractions, the Definition's Omega(hb(gamma_i)) = -(p_i/tau) gamma_0 gamma_i gives 2 <Omega(e_1), Omega(e_2) x Omega(e_3)>_eps = 8 p1 p2 p3 tau^-2 at p = (-1/3, 2/3, 2/3) and (-2/7, 3/7, 6/7). The standard Cartan forms of the Kasner coframe (omega^{i0} = (p_i/tau) e^i, which is what the check uses) assemble to that same Omega. So the forms rewriter's text (omega^{ab} the components of Omega in the Definition's sign, value +8) is right. I recorded this in the extraction note and changed no text. ga2-gravity.md still lists the item as open; it can be closed.
2. H5 left for each entity's next revision: renaming kappa in synthesis.n-plus-null-ground-state (a postulate with 23 users, the same reasoning as H15); R02 item 10's double letters (B, D, Q_k, R) across six entities, two of them claimed by AP2; R01's U and rho in synthesis.dirac-causal-propagator-...; R04's coupling matrix A -> \mathcal{A} and Hermitian norm N in the rung-field entities (long renames with no target letter fixed for N); the d Omega^2 symbol in about ten entities.
3. H11: 483 stale pins on free dependants whose targets' formal text changed in this run (GA rewrites and readers' restatements) were not repinned. A notation-only change cannot be told from a restatement without reading each pair, so these wait for Leon's review. Pins on AP2-owned and GTG-owned entities were also left alone.
4. Housekeeping: a scratch list of claimed ids was written by mistake to /mine.txt (outside the lab). A safety check refused its removal, so it is still there for Leon to delete. It is harmless.

## Counts

Category A: 16 items. 13 applied by AP1 (A1, A2, A4, A5, A7, A8, A9 on two entities, A10 on the note, A13, A14 with the check fix, A15, and A16 checked and recorded), 3 passed to the GTG provers (A3, A6; A11 already done), and A12 already done. Category G: 13 items. 11 applied (G1 to G5, G7, G9 to G13), 1 passed (G6), and G8 done by AP2. Category H: 15 items. H1, H2, H4, H5 (in part), H11, H12 and H13 applied; H3, H6, H7 and H10 were already done; H8, H9, H14 and H15 need no action by decision. Entities edited by AP1: 80, including 1 new note. 219 pins repinned. 2 checks changed (open-channels, boost-evolution) and 1 check premise() call repointed (schwarzschild). Each ran clean under runcheck and under check4 on a proposals/ copy, and each copy was deleted.
