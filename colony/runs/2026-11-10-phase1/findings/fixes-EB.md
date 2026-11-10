# fixes-EB (fix round, run 2026-11-10-phase1)

All three proposals revised in place in proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml); ids
unchanged. Only runcheck was run: every check function of the three passes. Edit scripts: work/EB/fix_sig.py,
fix_par.py, fix_pos.py.

## Common fixes (all three)
- C1: Hypothesis (P) stated verbatim as the base's formal level has it (with reality), named, symbol omega; "under
  (P)" in each one-liner; one sentence in each technical and lay level; extraction notes say it is to become an
  assumes edge.
- C2: the frame-dependence sentence in each formal level (signatures adds: the list does not depend on the frame,
  with a proof line).
- C3: tower.commuting-copies@5 pinned in place of the mode-split theorem (parity, positivity); the twist relations
  proved in place in three lines; the pair state written out and its idempotency proved in the parity proof.
  Signatures never pinned the mode-split theorem.
- C5 / overlap ruling: base pinned @1 with claimref in all three; own copies of the identity, the single-pair bound
  and the blade lemma with its positivity proof dropped and replaced by citations of base (i), (iii), (iv), (v).
- C6: "(P) extends the stored definition of a state from elements to functionals" in each formal level.

## Signatures (fixes 1 to 7)
1. List worded "the following fourteen signatures: the nine with 1 <= n <= 3, and (4,0), (1,3), (0,4), (5,0), (1,4)".
2. Cl(1,3): the ONE-copy paragraph (real or rational coefficients; nothing against Bell violation for two systems;
   Cl(4,1) sentence) in the reading clause, technical, lay and note; "there every such experiment stays at 2"
   deleted and replaced by the referee's sentence; "a commuting imaginary unit changes the list" replaced by the
   Cl(4,1) sentence.
3. Reading clause states the (p,q) convention and that (0,0) is left out only by n >= 1.
4. C1, C2 as above.
5. Old clause (i) (identity) and the lemma half of old (iii) are citations; clauses renumbered (i) excluded list,
   (ii) configurations, (iii) reading. Check: the identity function removed (and from checked_by); the table function
   keeps the configurations and one value of the stored functionals as a consistency test, and touches the base.
6. Title: "Signatures in which two commuting pairs of one real Clifford algebra exceed CHSH value 2" (88 characters).
7. "From memory" flag kept on the two-by-two matrix algebra remark, with "the proof here does not use it".

## Parity (fixes 1 to 6; Leon's decision)
- Both settings recorded side by side as "setting E" (parity-even observables) and "setting O" (parity-odd elements
  count), neither called physical, each clause labelled with its setting; the sentences that called the choice a
  premise decision or said observables "repair" nothing are gone.
1. C4: state written "the stored pair state at r = 0, cs = 1/2, rho = (1/4)(1 + p1p2 - e1f2 - f1e2)"; directions
   B+- = z p2 +- x e2p1, value 2(z + x); added the general-amplitude statement: value 2(z + 2cs x), supremum
   2 sqrt(1 + 4c^2s^2), equal to 2(z + x) only at equal weights (proved; checked at (c, s) = (3/5, 4/5): 342/125).
2. Dasenbrook et al. reworded: obtains the violation from two copies, states no no-go. Debarba et al. kept.
3. C1, C2, C3.
4. Clause (ii) heading carries the scope (one mode or its twisted copy).
5. Clause (iii) cites the base lemma for the functionals.
6. 82/29 and 478/169 removed from text and check; 14/5 kept as the one example, with state and directions named.
- Clause (v): the reality clause is now part of (P), so "value 0 for every state" holds without an extra hypothesis.

## Positivity (fixes 1 to 7)
1. One-liner restated as the referee words it (negative on (C - t)^2 for 0.54 < t < 7.46 and on other elements that
   combine different setting pairs, never inside one setting pair; "follows from positivity on (C - phi(C))^2 and
   (1 - K)^2").
2. Technical restated the same way; clause heading "(A sufficient pair of positivity conditions, for this blade
   configuration; proved.)", with "sufficient, not claimed necessary". New clause (ii): inertia (12, 4, 0) of the
   form lambda(x y^dagger) (verified by exact congruence diagonalisation in the check) and the element
   A1(B1+B2) - 2 with value -2 (checked). New in (i): non-negativity inside one setting pair, proved.
3. "extended Q-linearly" at the functional and at the idempotents.
4. C6 paragraph in note, formal and technical; proved in place that 1 + C is not a sum of x x^dagger.
5. C1, C2, C3.
6. Old clause (iii) (anticommutation only on the state) removed with its check function; it is base (ix). The id
   still carries the old wording because ids are not renamed; the note says so. Title unchanged and now matches.
7. Popescu-Rohrlich marked verified by the referee; Summers-Werner and Popescu-Rohrlich 1992 stay "from memory".

## The point I was asked to check
The base's positivity proof of the blade lemma uses y = Pi x with (1/2) omega_r(x x^dagger) =
<x^dagger Pi (1 + rC) Pi x>_0 = <y^dagger y>_0 + r <y^dagger C y>_0. My dropped copies (signatures, parity) used
y = P x with the same line, and the positivity copy used y = Pi x with the factor 1/4 for the three-mode projector.
They agree with the base's corrected form: y = Pi x proves the x x^dagger form, which is the one (P) asks for.

## Not done / to note
- Parity keeps lineage motivated_by the mode-split theorem (lineage, not a uses edge).
- The positivity one-liner carries the decimals 0.54 and 7.46 as the referee worded them; the formal level has
  4 - 2 sqrt 3 and 4 + 2 sqrt 3.

check4: pending (orchestrator)
