# Maintainer pass, run 2026-11-18-leads (after Leon's decisions of 18 November 2026, about 19:00)

LAB = /home/claude/phys-graph (branch run/2026-11-18-leads). Thirteen proposals are accepted and stored (ids in
accept.log). Read first: colony/BRIEF.md (Standards), colony/POLICIES.md, the previous run's
colony/runs/2026-11-18-navigate/MAINTAINER.md for the bookkeeping, style and check rules (they apply unchanged;
source string for credit entries: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'; extraction key
maintainer_pass_2026_11_18_leads), then the reports you need: verify/R-A.md to R-E.md, R2-ABC.md, and the findings
files findings/attack-*.md and fixes-*.md of this run (sections "Decisions" and "Links").

## Leon's decisions (binding)
D1. The three proposals restated after WRONG or OVERSTATED verdicts are accepted.
D2. Gravity: "Require no signalling". The conventions state that the series requires no signal outside the light
    cone; so a gravitational field with no variables of its own (the slaved field) is not the full account of the
    field. HOW the requirement is met stays the open problem: do not say that the two null-momentum components
    carry states or variables, do not posit a quantum, and do not say they carry none.
D3. Tube-point clause: "Rotations; silent elsewhere". The stored clause is restated to read: invariance under the
    rotations commuting with the wedge's boost, the boost being (a positive multiple of) the horizon's Killing
    flow. The de Sitter result stands on that reading. On the Schwarzschild exterior and on the static region of
    Schwarzschild-de Sitter no observer meets the condition, the clause is silent there, and rho stays free.
D4. sheaf.wall-class is restated as drafted in work/W/wall_class_restatement_draft.md (clauses (a) and (c); status
    stays conjectured).
Defaults taken without asking, to be carried out as stated: the spreading law stays conjectured (already stored
so); the return-delay estimate stays conjectured and is listed under op.island-dictionary; the Kerr conjecture is
annotated, not reworded; Bott periodicity is not imported; the Pell result stays its own entity and the stored Pell
theorem points to it.

## Ownership (disjoint; touch nothing outside your list)
### M1: store entities
1. sheaf.wall-class: apply the draft (version + 1, amendment kind restatement, all levels, no status change). Check
   the draft against the stored
   synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line as accepted before applying; where the draft
   says more than the stored result, follow the stored result.
2. The tube-point clause (D3): synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries restated at
   every level; then every stored entity that says the clause "decides fields with one horizon" or quotes the
   clause's wording (grep "tube point" over store/claims: at least synthesis.de-sitter-field-fixes-the-observer-
   tube-point, synthesis.wick-rotated-boost-selects-observer-tube-point). Cite
   synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent where the
   restatement rests on it (a uses edge only where a proof step uses it; otherwise a \claimref in the text of a
   dated sentence). The clause is a costed premise of the series: if its entity is a postulate, the restatement is
   by Leon's decision D3 and the amendment says so.
3. synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional: its cited fact (C3) is now
   proved by synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations; say so,
   with what is still cited ((C1), (C2)), and that its clause (3) is superseded on oscillating channels only
   (R-B.md, R2-ABC.md). hawking.joint-j3-s-wave-reduction and hawking.helicity-lift-joints-itemised if they list the
   even-parity spin-2 reduction as open.
4. The imported Fact on Stiefel-Whitney classes used by the rung count (find it from the uses of
   synthesis.wall-rung-count-is-height-of-dying-line-class; R-C.md names it): add the dimension axiom to its
   statement with provenance (a standard axiom; cite a textbook already in store/references.yaml if one is there,
   otherwise flag "quoted from memory" in the provenance). Version + 1.
5. interior.duality-monodromy-fibration-over-ring: a dated note (not a rewording): on a reading of 18 November the
   winding three is the degree of the field strength in the ring coordinate and only its parity is a class of a
   degenerating form; computed in a working file, no stored result. Take the exact content from
   findings/attack-W.md, lead 3; keep it labelled as computed and not refereed.
6. scrambling.return-delay-scrambling-log-recovered: a dated sentence that it has no proved core (the spreading
   law's stored theorems do not reach it) and stays an estimate; no status change.
7. The stored Pell theorem that the new result extends (find it: the entity whose last sentence gives the running
   maxima "for denominators up to 400"): replace "computed up to" by the proved statement with a \claimref, version
   + 1.
8. synthesis.gravitational-pair-production-from-the-operator-source-at-first-order: one dated sentence each (no
   clause changed): its channel weights are rederived without angular integration by the rotation-weights result;
   on the chain's bath the coefficients are those of the heating result. Only if this can be done without a uses
   cycle (the new results use this theorem): a \claimref in a remark, not a uses edge. If the validator objects,
   leave this item and report it.
9. store/conventions.md, section "Gravity and the graviton": a paragraph "Requirement (18 November 2026)" stating D2
   exactly, citing the three stored results of this run on the field (two free directions and four constraints;
   the lattice Maxwell result; the first-order signal with its size, about 1e-13 in the proposed experiments and of
   order one near 190 kg at a metre against a superposed mass of 1e-14 kg, under its local hypothesis), and
   pointing to op.gravitational-field-at-null-momentum for how the requirement is met.
### M2: store/open_problems.yaml only
Update, in the file's own style (dated "Answered", "Answered in part", "Done", "Closed negatively" prefixes on
attack items; statements restated where the question changed; entities lists extended with the new ids; status
changed only where the problem's question is settled or reformulated):
- op.eigenbundle-class-of-degenerations: items 1 (m = 3), 2 (tame walls: agreement, two-sided only), 4
  (sufficiency) answered; item 3 (Kerr) closed negatively as posed (no stored result: say "computed, not stored");
  what remains (codimension five and beyond, the class relative to the whole base, one-sided against two-sided).
- op.wall-class-invariant: what the new results do and do not say about tame walls; sheaf.wall-class restated.
- op.kerr-ring: first attack item, the same negative reading.
- op.gravitational-field-at-null-momentum: item 1 answered (no stored premise implies commutation; unitarity does
  not); item 2 answered (no localisation floor is relevant; no stored bound; the signal's size); item 3 answered
  (the lattice Maxwell result, as restated); item 4 restated (the count; the burst ratio is (2+g+o)/(1+g) if the
  two components emit and (2+o)/(1+g) if not, so the item's "restate the baseline with g = 0" is corrected); and
  the statement updated for D2: the requirement is now adopted, the problem is how it is met.
- op.einstein-from-the-field-theory: the trace-free channel item: the operator source assumes the clause, the
  static coupling does not test it, the rate does (findings/attack-G.md lead 5).
- op.which-capacity: restated for D3 (the clause as restated; silent on black-hole fields; rho free; what is left:
  the norm and free-fall candidates select r_0^3 = 3M/Lambda in Schwarzschild-de Sitter with one scale per horizon,
  unadopted).
- op.helicity-per-boundary-mode: the even-parity spin-2 reduction is proved; J3 narrowed to what remains ((C1),
  (C2) cited; the fuzzy-sphere identification).
- op.positivity-of-values: items 5 (Gleason type) and 6 (running maxima) done; a new item: which projectors can
  label a record (all rational projectors, or local products only), tied to the parity item; more than two modes
  (needs an imported representation fact); the prior art to be read (Mushtari 2001, flagged as read through a
  summary).
- op.curvature-coupling-across-subjects: the heating does not constrain the open datum; on the chain's bath the
  stored exclusion is conservative at both stored assignments; the tilt window on the chain's scalars not treated.
- op.graviton-rate-as-classical-field-process: the fermion channel has no trace part at the next order from the
  stored trace statement; first effect at order G^3.
- op.island-dictionary: add scrambling.return-delay-scrambling-log-recovered to its entities with one sentence.
- op.order-four-anomaly-and-sixteen: one sentence under the relevant item: a link to the eigenbundle class through
  real K-theory was tested and is a resemblance (findings/attack-W.md lead 5b; computed, not stored).
Take every statement from the stored entities as accepted (get_claim), not from the first drafts in findings.

## Rules for both
- Everything truthful to the stored results as accepted; no statement stronger than its source. Where a finding
  is "computed, not stored" or "argued", keep that label.
- House style; no agent, run or method names in store text.
- Checks: `python3 colony/runcheck.py` on any check you touch; `python -m tp check --store store --layers 1-3
  --keep-going --author leon` once at the end (M2: after its last edit; M1: after its last edit; if both run at
  once that is two heavy processes, which is the limit). No layer 4, no check4, no repin, no commit, no push, no
  spawning agents. Never kill a process you did not start.
- Report to colony/runs/2026-11-18-leads/maintainer-M1.md or maintainer-M2.md: each change old -> new, anything you
  declined and why, anything that needs Leon. Final reply under 250 words.
