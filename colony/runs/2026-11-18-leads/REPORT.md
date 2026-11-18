# Report, run 2026-11-18-leads

Request (Leon, 18 November 2026, 14:04): adopt the computed mean energy per creation event in the gravitational
floor, and run through all the leads of the morning's survey. Reading taken: every lead of the survey (sections A,
B, C), the leads of the message on the impact of the conjecture's refutation, and the open items of the previous
report. Method: RUN.md (one attacker per cluster, blind referee, fix round, second pass on what was restated).

## 1. The energy per creation event (maintainer pass; refereed, SOUND)
The floor is now defined with the mean energy of the rate integral: each leg is weighted by E^3 f(E), so a Bose leg
carries 4 zeta(5)/zeta(4) T and a Fermi leg (30/7) zeta(5)/zeta(4) T; an event deposits 7.873 T (scalar), 7.890 T
(chiral fermion, vector, nine vectors), 7.889 T (the Standard Model's content); energy fraction about 10.5 Y where
4 Y stood; prefactor 1.23e-3 where 9.6e-4 stood. Floors: mirror 6.6e-4 (was 5.2e-4), nine vectors 8.1e-4 (was
6.4e-4); eta' at the mirror's floor 2.1 (was 4.4, still above one); under (R) the mirror's floor is below 3.1e-5.
Thirteen entities restated (maintainer-energy.md lists each number old to new). Conclusions that changed: two round
bounds on Delta N_eff (now 2e-12 and 2e-11); the floor at the rescue temperature no longer equals the hot deposit
(the hot deposit's 3T is a stipulated figure); the floor's share under (R) is below 2e-8, not 1e-8.

The mirror's composition at the present floor was recomputed with the papers suite's own scripts, staged into the
workspace and run with three values added to their grids (24 checks, 0 failures; outputs in work/housekeeping/):
at 6.6e-4 the mirror is still neutron-rich for L <= 0 (83 to 96 percent neutrons, was 96 to 100), only moderately
degenerate (Fermi energy over thermal deposit 2.7, was 49 to 84; chemical potential 3.5 to 3.7 temperatures, was 18
to 23), and the helium branch's burning reheat is 1.9 (was 3.0 to 3.2). Six entities restated to these figures.

## 2. Results by cluster (thirteen proposals, all accepted)
Verdicts are the first referee's, then the outcome after the fix round and, where restated, the second pass.

### Walls (op.eigenbundle-class-of-degenerations, op.wall-class-invariant, op.kerr-ring)
- synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two. SOUND WITH FIXES, ACCEPT.
  Proved: the positive eigenbundle of the position vector on the least module of Cl(3,0) is not stably trivial (the
  clutching loop's rotor lift ends at -1; lifting lemma proved in the text; no Bott periodicity); on k copies a
  fixed-form completion exists exactly when k is even.
- synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial. SOUND WITH FIXES,
  ACCEPT. Proved: sufficiency by explicit construction, for every fixed form of the stated signature; a
  winding-two family has no rank-two completion and one added direction repairs it.
- synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line. SOUND WITH FIXES, ACCEPT WITH. Proved:
  compared across a collar the class is the dying line, the information of the stored pair; two-sided completions
  carry its opposite. Not shown: the class relative to the whole base, naturality, conservation, and any relation
  to the stored one-sided rung count.
- Kerr ring: no proposal. The winding three is the degree of the field strength in the ring coordinate; the
  cometric does not degenerate at the ring, so no completion statement applies; only the parity is a class
  (computed, not stored).
- Tested and narrowed: jumps invisible to the tower's residues are those by a multiple of four eigenvalues, not
  every even jump; the link to the order-four anomaly through real K-theory is a resemblance (the class of the
  RP^5 wall has order eight; computed, not stored).

### The gravitational field (op.gravitational-field-at-null-momentum)
- synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints. SOUND
  WITH FIXES, ACCEPT WITH. Proved: kernel 6 at null momentum and 4 off the cone; four of the equations are
  constraints; the two free directions are the transverse trace-free maps.
- synthesis.two-dimensional-lattice-maxwell-coulomb-slaved-field-fails-and-string-dressed-detection-commutes.
  OVERSTATED, restated, ACCEPT WITH. Proved in an exact lattice Maxwell model: the Coulomb slaved field fails on 76
  of 82 links; the retarded slaved field fails at 878 of 2750 events, all in the source's forward cone; with the
  field's own transverse variables a string-dressed detection commutes off the string. Withdrawn: that constraint
  and dressing never restore commutation, and that every slaved field obeying the field equation fails.
- synthesis.with-a-coupled-device-the-slaved-field-failure-is-a-first-order-signal-and-a-survey-finds-no-stored-bound.
  SOUND WITH FIXES, ACCEPT. Proved in the lattice model under a local hypothesis (D): a classical source changes a
  distant detection probability at first order. Argued for gravity: about 1.3e-13 in the proposed experiments, of
  order one near 190 kg at a metre against a superposed mass of 1e-14 kg, outside the light cone; caused by the
  field having no variables of its own; untested (it needs mesoscopic superpositions and timing within about 3
  ns). Survey: no stored premise bounds it; unitarity does not imply commutation.

### Heating, couplings, scrambling
- synthesis.heating-coefficients-across-curvature-couplings-and-on-the-chains-bath. WRONG in clause (iii),
  recomputed, ACCEPT WITH. Proved: couplings enter the summed coefficient through one product. Computed: on the
  Standard Model's scalars the two stored assignments differ by 0.11 percent; on the chain's bath (g = 314) the
  stored Pati-Salam margins 2.2 and 1.5 become 2.84 and 1.96 (the threshold scales with the bath). The first
  version kept the threshold of the Standard Model's bath and concluded the exclusion fails at the tree-level
  value: withdrawn.
- synthesis.rotation-weights-of-pair-sources-fix-the-channel-weights-and-give-no-trace-at-nonzero-weight. SOUND
  WITH FIXES, ACCEPT. Proved: all nine stored channel weights without angular integration; a source of nonzero
  rotation weight is trace-free. Argued: the stored trace statement gives the fermion channel no trace part at
  the next order; the vacuum's trace-free response changes it at order G^3.
- scrambling.spreading-law-chaos-bound-saturated, version 7. SOUND WITH FIXES (nothing new), ACCEPT. Status stays
  conjectured; the entity now says which clauses are stored theorems and which is the paper's estimate.

### Horizons (op.which-capacity, op.helicity-per-boundary-mode)
- synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent. OVERSTATED,
  restated, ACCEPT WITH. Proved: with the boost a positive multiple of the horizon's Killing flow, no observer of
  the Schwarzschild exterior or of the static region of Schwarzschild-de Sitter meets the clause's condition; in a
  twisted gauge every observer on the axis does, at every scale, and the same gauge exists in de Sitter.
- synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations. SOUND WITH FIXES,
  ACCEPT. Proved identically: sixteen first-order Ricci components; every Zerilli solution rebuilds a vacuum
  field; on oscillating channels the converse. The stored result's cited fact (C3) is now proved.

### Values (op.positivity-of-values)
- synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear. SOUND WITH FIXES, fixes applied.
  Proved: every additive weight on the projectors of Cl_Q(2,2), of every rank, with values in a rational vector
  space and no sign condition, is the restriction of a linear functional. What (P) still adds: the sign condition
  and the values of elements whose spectral projectors are not rational. Prior art (Mushtari 2001, 1995) was read
  through summaries only and is flagged for Leon to confirm.
- synthesis.pell-values-are-the-running-maxima-of-the-pure-state-chsh-values-over-the-rationals. SOUND.

## 3. Leon's decisions (18 November, about 19:00)
1. The three proposals restated after WRONG or OVERSTATED verdicts: accepted.
2. Gravity: the series requires no signal outside the light cone; the slaved field is not the full account; how
   the requirement is met stays open.
3. Tube-point clause: the rotations commuting with the boost, the boost being the horizon flow; silent on
   black-hole fields, rho free there.
4. sheaf.wall-class restated as drafted.

## 4. Housekeeping (survey rows 5, 8, 9, 10)
- Rows 5 and 8 were stale flags: the predictions and claims concerned already carry their basis and motivation
  links; six flags removed. pred.gravity-entangles-standard-phase (version 3) now uses the operator Newtonian
  coupling as its basis; the element reading and its premises stay outside the store.
- Row 9: three conjectured claims listed under op.qft-structural-inputs, op.qft-bosons-and-the-rung-field,
  op.hypothesis-s.
- Row 10 was partly wrong: Premise (N) already registers the number N. New open problem op.the-number-n holds its
  six claims. The id prefix "refuted" on one of them is Leon's decision of 10 November and stays.

## 5. Left open, with the reason
- Walls in codimension five and beyond (needs an integer invariant or Bott periodicity imported).
- More than two modes for the linearity theorem (needs an imported representation fact).
- The fuzzy-sphere identification of the partial waves; deriving the trace-free channel; independence of (P)
  (reduced to which projectors can label a record).
- The papers and legacy/verify_T14.py still carry the first-imported coefficients and floor; five setting notes
  quote the papers' figures. These are the papers' text and need a derivation session, not a store edit.
- The stored Pati-Salam clause still states its margins on the Standard Model's bath; the new result records that
  they are larger on the chain's bath. Not restated.

## 6. Maintainer passes and the final gate
- maintainer-energy.md (the energy restatement and the composition follow-up), maintainer-M1.md (eleven entities and
  the conventions, by the decisions of section 3), maintainer-M2.md (twelve open problems; two change status from
  open to reformulated). M1 left J3 un-narrowed (a premise; not among the decisions) and recorded the dimension
  axiom's provenance as from memory.
- All thirteen proposals: check4 exit 0 and validate ok after the last edit (verify/gate_summary.txt). One
  bookkeeping correction at acceptance: two proposals declared their departure from the algebra in coverage.yaml;
  it belongs in the entity's front matter and was moved there.
- Six warnings appeared on the new entities at the first full check (five missing conditions at the plain levels,
  one decimal) and were fixed. Final check: 0 errors, 1 warning, the baseline's. Build 2412 entities, 0 errors.
  Unit tests: 445 run, 1 skipped, OK.
- Subagent tokens: about 5.0M (attackers 2.9M with their fix rounds, referees 1.4M, maintainers 1.2M less overlap).

## 7. For Leon
- Read Mushtari, Lobachevskii J. Math. 9 (2001) 47, before the linearity theorem is called new.
- J3: narrow it to what remains ((C1), (C2), the fuzzy sphere), and import (C1), (C2) as Facts, or leave it.
- The norm and free-fall candidates select one radius in Schwarzschild-de Sitter with one scale per horizon; they
  are not adopted.
- Which projectors can label a record (all rational ones, or local products only): this decides whether (P) is a
  theorem on two modes up to the sign condition and the irrational spectral projectors, or stays independent.
- The papers (T14 and its verify script) carry the first-imported rate and floor; the store no longer does.
