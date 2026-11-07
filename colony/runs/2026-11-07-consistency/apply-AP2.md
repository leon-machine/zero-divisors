# Run 2026-11-07-consistency: apply agent AP2 (categories B, C, D, E, F and Leon's answers 2 to 7)

Acting for Leon as maintainer on DECISIONS.md. Every changed entity has a credit entry for its version (Claude Opus 5.5,
source: maintainer pass 2026-11-07 (decisions)) and an extraction note `maintainer_pass_decisions` (by
maintainer-2026-11-07). Versions are relative to store/.tp-lock.json; an entity already raised in this run kept its
version (marked "kept"). Every file kept (two proof files are no longer attached, see B1). No commits, no retirements.

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`, run once at the end:
1 error store-wide, E206 on synthesis.positive-structure-... (a GTG prover's edit in progress), nothing on an AP2 id
except I213 subject notices. Checks whose files I changed were runchecked (all pass): synthesis.phase-flow-is-time-...,
synthesis.number-diagonal-dynamics-spreads-nothing, synthesis.affine-cell-boost-spreads-without-scrambling,
synthesis.modular-data-on-a-generator-... (premise() calls removed or repointed only; no assertion changed, so no check4).

## New entities (3)
- synthesis.common-ceiling-coupling-premise v1 (postulate; Leon's answer 2, C1): the two towers of the reversal orbit
  share one ceiling M and equal couplings there. States its scope (parameters of the dynamics, neither P2's labels nor
  states; equates no state, so xi stays free; reversal orbit only), its cost (one posited equality between undetermined
  parameters, fixes no coupling value; carries the mass factor of the share of one; without it the share moves by
  e^{-2 pi delta/b}, within 10% only for |delta| < 0.106) and a refutation condition. Extraction says adopted by Leon on
  2026-11-07 and what it costs. P2 unchanged.
- one-relation.recorded-sectors-superselected-premise v1 (postulate; answer 6, B3): T16's Remark rem:recording as a
  premise: under irreversible recording, the recorded flag sectors are superselected in the recording limit (the
  decoherence step taken as exact); cost and refutation condition stated.
- one-relation.imported-envariance-born-rule v1 (imported; B5): Zurek (2005), Born's rule from envariance, with the
  additivity critique; bibliographic data checked against the OSTI record (DOI 10.1103/PhysRevA.71.052105), the steps
  stated from memory (said so).

## B. Status stronger than its proof
- B1 (answer 4) scrambling.spreading-law-chaos-bound-saturated 5 -> 6: proved -> conjectured; derivation keeps its
  premises with a note, proof-main.tex kept on disk but no longer attached (E108: a conjecture carries no proof text);
  lineage.motivated_by added (E107).
- B1 + G8 scrambling.return-delay-scrambling-log-recovered 2 -> 3: conjectured; formal restated as a modular-time
  (rotor-flow) estimate, "Under (L_E) this is a modular-time (rotor-flow) estimate, not a real-time delay"
  (singularity.l-boundary-mode-locality, synthesis.number-diagonal-dynamics-spreads-nothing); flow_note rotor; plain
  levels; proof file detached as above, checked_by kind proof removed, motivated_by added, pin to the spreading law @6.
- B1 consequence (uses edge -> mention, check premise() call removed, runcheck pass): synthesis.phase-flow-is-time-
  rotor-flow-kms-continuation 3 -> 4 (also F9), synthesis.number-diagonal-dynamics-spreads-nothing 2 -> 3,
  synthesis.affine-cell-boost-spreads-without-scrambling 3 -> 4. These analyse the law's growth step and do not rest on
  it; with the edges kept they and five dependants (boost-evolution, killing-horizon, modular-data, modular-period,
  wedge-reflections) went effectively conjectured (E204). boost-evolution was passed to AP1, who applied it.
- B2 (answer 5) dark-matter.no-coupling-rule-odd-towers-follows 5 (kept): formal restated as the three facts (a), (b),
  (c), (c) now naming both P2 (labels, not couplings) and the new ceiling premise (assumes edge added); "any rule is a
  further premise" moved to a marked Remark at the technical level; disclaimer dropped; title "Three obstructions to a
  coupling rule for the odd towers" (old formal and title under source_formal, source_title); status proved.
- B3 (answer 6) one-relation.record-chain-votes-measurement-without-collapse 6 -> 7 and
  one-relation.character-experience-three-record-chain-theorems 4 -> 5: assumes edge to the new recording premise, cited
  where Remark rem:recording was; rem:recording removed from unresolved_refs; status proved given it.
  note.one-relation.measurement-recording-open-remainder 1 -> 2: comments_on the new premise.
  one-relation.overlap-table-sorted 5 -> 6: (ii), (iii) and the constants clause moved into a marked Reading at the
  technical level (text kept in full); formal keeps (i); proof and coverage say which part is proved.
- B4 (answer 7) + A10 (from AP1) sheaf.wall-class 2 -> 3: clause (a) restated as the one-rung completion (torsion part
  vanishes iff a one-rung completion exists; coarse part, the clock mismatch, obstructs the strict completion); (b) "the
  rung shifting both signatures by (1,1) and leaving both clock positions unchanged"; obstruction theorem in lineage;
  conjectured; old formal under source_formal. synthesis.wall-class-one-rung-obstruction 2 -> 3: its two references to
  clause (a) now say "as first posed (its version 2)".
- B5 one-relation.measure-indifference-borns-rule-located 2 -> 3: uses edge to the Zurek Fact, cited in formal and proof.
- B6 mass.imported-unitary-representations-de-sitter-group 4 -> 5: the "same normalisation, with no shift" sentence
  moved out (formal, technical), pointing to the hypothesis; synthesis.operator-join-casimir-shifts 2 -> 3: (iii) states
  the normalisation hypothesis in full as not proved; synthesis.operator-join-point-spectrum-on-positive-energy-modules
  1 -> 2: the sharpness paragraph states the hypothesis and that the bound uses only the central constant and the ordered
  Casimirs of casimir-shifts (i), (ii), not it.

## C. Premise gaps and scope
- C1 (answer 2): assumes edges to synthesis.common-ceiling-coupling-premise@1 from the six results, levels and proofs
  restated where they credited P2 with the coupling: dark-matter.mirror-tower-copy-one 9 (kept; (iv) restated, (v)'s
  first route reads P2 on the stored charge, and G1's caveat wording applied here), dark-matter.mirror-share-assembled
  7 -> 8, dark-matter.mirror-share-one-how-fragile 6 -> 7 ("P2-protected" -> the new premise),
  dark-matter.population-count-one-share-half-percent 5 -> 6, dark-matter.which-towers-can-carry-arrow 4 -> 5,
  dark-matter.no-coupling-rule-odd-towers-follows (with B2). Coverage untouched_premises entries added for the new
  premise in all six. The mention in standard-model.under-s-mirror-inherits-desert 5 -> 6 (proof) now names the store's
  own premise, no edge.
- C2 (answer 3) neutrino.real-breaking-assumption 1 -> 2: "and the charged-lepton matrix is real in the same basis", with
  the reason (circulant result (iv)(c)); pred.leptonic-cp-trivial 2 -> 3: technical, lay, one-liner carry "with a real
  charged-lepton matrix", assumes pin @2; formal and kill condition unchanged.
- C3 rungs.generators-outside-gauge-algebra 7 -> 8, standard-model.left-right-parity-what-breaks-it 7 -> 8: R04's
  which-unit sentence in both proofs.
- C4 synthesis.attachment-conformal-energy-is-generated-by-z 5 (kept): one formal sentence: with nu as e_+,
  I_6 = I_4E = e_0e_1e_2e_3 nu e_- acts on CS as +I_7 (on CS^- as -I_7; the opposite orientation gives -I_7 on CS), so
  the z-adapted result's +I_6 is a consequence. Checked exactly (Gaussian rationals) in the entity's own Jordan-Wigner
  realisation: work-R10/i6_attachment_frame.py (I_6 = I_7 times the chirality; e := chirality, I_6 e = I_7).
- C5 no action (as recommended). C6: no premise-free stored statement of the rotor realisation of the Moebius closing
  was found, so the attachment edge in synthesis.normality-... is kept.

## D. Citations and links
- D1 (synthesis.schwarzschild-..., AP1-claimed): passed to AP1 (items-for-AP1.md); AP1 applied it.
- D2 (synthesis.killing-horizon-..., gtg_1): passed to items-for-gtg.md with the exact edge, citation and check changes.
- D3 synthesis.thermality-of-every-future-half-generator-... 3 -> 4: positive-null-energy@7 -> null-vacuum@1 (ii), (iii);
  stationary-horizon-state@4 -> stationary-generator-states@1 (iii); formal, proof, coverage. 
  synthesis.geometric-modular-conjugations-... 5 (kept): pin to thermality @4.
- D4 synthesis.normality-on-the-closed-generator-... 4 (kept): stationary-horizon-state@4 -> stationary-generator-
  states@1 (i) (edge, proof, coverage); also H5 from AP1 (J -> R_inv in formal (i), nu named as e_+).
  synthesis.modular-data-on-a-generator-... 5 (kept): wedge-reflections@4 -> the premise-free
  synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom@1, carried to the plane by the cyclic rotation
  e1 -> e3 -> e2 -> e1 (fixes I_4); formal, proof, check premise call (runcheck pass).
- D5 synthesis.imported-null-plane-modular-hamiltonian-first-law 1 -> 2 (technical text citation).
- D6 pairing.two-frames-share-vacuum-selected-transport 5 -> 6 (cyclic citation written as a mention).
- D7 scrambling.pair-mode-qubit-one-object 4 -> 5 (cites sheaf.schwarzschild-degeneration-boundary-tame (2), uses edge
  @6, proof sentence, coverage); scrambling.epoch-modular-period-two-unknowns-become 5 -> 6 (text citation only).
- D8 dark-matter.imported-gravity-only-coupling 3 -> 4 (cites obj.dark-matter.frozen-phase-operators, about link; P1 kept).
- D9 synthesis.matter-asymmetry-registered-free-input 1 -> 2 (Theorem -> Proposition, twice).
- D10/E2 interior.gauge-trajectory-unipotent-ray 9 (kept): uses singularity.unipotent-ray@4, singularity.cones-fold@4.
- D11 note.conformal.abstract 1 -> 2 (comments_on conformal.minimal-nondegenerate-completion).
- D12 references.yaml: WeinbergQFT1 removed, merged into WeinbergQFT2; lepton.imported-free-sector-anomaly-conditions
  4 -> 5 and its -external 1 -> 2 repointed (source_formal and orig-proof-main.tex keep the paper's key as history).
- D13 one-relation.imported-square-roots-real-clifford-algebras 2 (kept): "conjugate to the pseudoscalar (one class;
  std-algebra.square-roots-of-minus-one)" at every level.

## E. Duplicates (links; no retirements)
- E1 synthesis.one-loop-vacuum-polarisation-extends-... 3 -> 4: (vii) and Step 8 dropped with a pointer to
  floor-regulator (v); plain levels; the check function kept as a cross-check (coverage says so).
- E3 field-theory.imported-standard-field-theory 4 -> 5: dated pointer to synthesis.imported-adler-bell-jackiw-axial-anomaly.
- equivalent_to added: sheaf.kasner-data-interior 2 -> 3 (E4), interior.imported-equivalence-einstein-equations 2 -> 3
  (E5), three-routes.base-unipotents-their-action-candidates 4 -> 5, hawking.modular-structure-completed-pair 3 -> 4,
  state-selection.partner-purification-are-canonical 5 (kept) (E6), conformal.witt-extension-theorem 1 -> 2 (E7),
  tower.morita-equivalence-algebra-amplification 1 -> 2 (E8), odd-extensions.imported-towers-clock 4 -> 5,
  rungs.imported-fock-representation-bogoliubov-group-external 2 (kept) (E9).
- specialises added: three-routes.change-transversal-canonical-isomorphism-completions 5 -> 6,
  three-routes.no-equivariant-value-boundary 3 -> 4 (E6), odd-extensions.doubling-or-complexification 6 (kept; -> even-
  subalgebra-isomorphism, joining the chain), odd-extensions.volume-element-odd-dimension 3 -> 4 (-> primer.centre,
  primer.sign) (E7), standard-model.imported-tower-commuting-copies-fock-module 5 -> 6 (E9).
- Partial overlaps recorded under extraction.overlaps_with (no pinned link kind fits a clause-level overlap):
  three-routes.join-disqualified-wrong-stalks 3 -> 4, three-routes.it-sheaf-risk-resolves-into-standing 7 (kept),
  three-routes.stalks-are-pointwise-metric-levels 4 -> 5 (E6), odd-extensions.doubling-or-complexification (E7),
  transport.exhaustiveness-every-zero-divisor-annihilated-idempotent 3 -> 4, transport.regularity-localises-zero-
  divisors-idempotents 2 -> 3 (E7), pairing.imported-stabiliser-tangent-external 2 (kept) (E9),
  dark-matter.imported-composition-simulated-external 1 -> 2 (E10).
- E11 synthesis.positive-null-energy-gives-r-premises 8 (kept), synthesis.stationary-horizon-state-is-its-own-edge-
  scaling-limit 4 -> 5: a marked Restatement sentence naming the premise-free home.
- E12: the about link was already present; nothing changed.

## F. Conventions (store/conventions.md)
F1 to F6, F8 to F15 added as one line or bullet each (F3 under Same names; F11, F2, F14 under Notation; F1, F12 after
the n0/ninf paragraph; F9, F10, F6 after the ladder pairs; F15, F4, F5 after the unit principle; F8 after "Where the
unit stands"; F13 in the gravity section). F7: nothing to add. Entity follow-ups: F1
standard-model.imported-frozen-point-dictionary 8 -> 9 (normalisation n0.ninf = +1 named); F9 in phase-flow (iii)
(checked exactly in Cl(1,1): sigma/2 = v*v - 1/2); F13 dark-energy.imported-macdowell-mansouri-theorem-stelle-west
read: it writes R^{ab} for the literature sign and says R(u,v) = -calR(u ^ v), so it names which; no change;
F14 dark-matter.imported-massless-graviton-production-rate 1 -> 2 (bar M_P throughout, source's M_P noted in the
provenance); F11 entities left for their next revision, as decided.

## Items passed to others
- items-for-AP1.md: boost-evolution B1 consequence (applied by AP1), D1 (applied by AP1), G8 (done here).
- items-for-gtg.md: D2 on synthesis.killing-horizon-value-factor-is-the-generator-boost.

## Not applied exactly, and why
1. C1's side recommendations tied to option (a) (rewording the tower-charge Reading; saying f1 = f7, f3 = f5 also follow
   from R2): Leon chose a separate premise with P2 unchanged, under which the Reading stays true; not done.
2. Two of the six C1 assumes edges (dark-matter.which-towers-can-carry-arrow, dark-matter.no-coupling-rule-odd-towers-
   follows) were added as Leon asked, but those results cite the premise only for its scope (the reversal orbit) and
   do not use it as a step; Leon may prefer to drop those two edges.
3. B1: a conjecture may not carry proof text (E108), so the two proof files are kept on disk but detached from their
   derivations (and return-delay's checked_by kind proof removed); the checks stay.
4. E11 and the clause-level E6/E7/E9/E10 overlaps: the store has no clause-level restates link, so the marks are in the
   text (E11) or under extraction.overlaps_with; the build's restatement counts are unchanged.
5. D12: references.yaml is regenerated from the papers' bibliographies, so a rebuild would restore WeinbergQFT1 from
   T12-lepton's bib until the key is merged in the paper source.
6. C6: kept the attachment edge (no premise-free source found).
7. Repins (H11, AP1's category) of dependants pinning AP2-bumped entities were not done; after the restatements (C1,
   C2, B2, B3, B4, B6, E1) the dependants need re-reading first.

## Counts
Entities changed: 69 existing (55 raised by one version, 14 kept at a version already raised in this run) and 3 new
(two postulates, one imported Fact), plus references.yaml and 14 conventions lines (F1 to F6, F8 to F15). Decision items
applied: B1 to B6, C1 to C4 (C5, C6 no change), D3 to D13, E1 and E3 to E11 (E2 with D10, E12 already present), F1 to
F15 (F7 nothing to add), Leon's answers 2 to 7, and from AP1's items A10 and H5. Passed to others: 3 (D1 and the
boost-evolution B1 consequence to AP1, both applied there; D2 to the GTG provers). Not applied exactly: 7 (above).
