# Referee report 3, run 2026-11-12-rung-state (Claude Opus 5.5)

Brief: REFEREE-3.md. Diff against c19c7d973e34230d83842477ff8930562a14320a. Nothing under `store/` was edited and nothing was committed.
Own code in `verify/work-R3/`:
- `r3_recompute.py` (log `r3_recompute.log`): own Clifford product and own Fock module (Jordan-Wigner string over the *higher* modes), all exact.
- `perturb.py` (log `perturb.log`, copies in `pert/`): 9 perturbations.

All four store checks pass as they stand.

Claims: 1 = state-of-a-new-rung, 2 = selector-candidates, 3 = records-of-unbounded-length, 4 = infinite-strings (renamed folder).

---

## Task 1. Were R2's verdict fixes applied?

**Claim 3**
- Fix 1 (c = 0 sentence): applied as R2 worded it, but R2's wording was itself wrong. See **P1**.
- Fix 2 (equals the mixture; pointwise, not in norm): applied. The phrase "in norm" became "not uniform", with no bound on the elements. See **P6** (minor).
- Fixes 3 to 7: applied correctly.
- Fix 8 (optional; the branches as tail classes): appears only in claim 4's Reading. Acceptable.

**Claim 4**
- Rename; the comparison rule as clause (v); fixes 1 to 6: all applied. P_0 is defined. "von Neumann" was replaced by Knuth and Yao. The premise count now agrees with claim 2 ("of two kinds").
- New problems in the text: **P2 to P5**.

**Claim 1**
- Fixes 1 to 5: applied.
- One qualification from R2's text was dropped: at ℓ = 0, σ_e alone does give uniqueness. See **P7**.

**Claim 2**
- Fixes 1 and 2: applied. Correct.

---

## Problems (exact fixes)

**P1. Claim 3 (iii), last sentence: still WRONG (computed).**
- The sentence: "For c = 0, ω_{Ψ_N}(x) equals the mixture's value as soon as at least one of the N coupled pairs is not involved by x; in particular for N > p + 1."
- Why it fails: Ψ_0 fills only pairs j < N. Pairs j ≥ N are empty in Ψ_N, but filled in ω_A and ω_B.
- Counterexample: c = 0, N = 1, x = on_{a_1}.
  - Pair 0 is coupled and not involved by x, so the hypothesis holds.
  - ω_{Ψ_1}(x) = 0, but the mixture gives 9/25·0 + 16/25·1 = 16/25.
  - The same element also fails for c = 3/5 at N = 1 (0 against the limit 481/625). That value is reached from N = 2 on.
- The "in particular" clause is correct. The proof is correct, because it works under "N beyond the largest pair in K".
- Fix: "For c = 0, ω_{Ψ_N}(x) equals the mixture's value as soon as every pair x involves is among the N coupled pairs and at least one of these N pairs is not involved by x; in particular for N > p + 1, where p ≥ 0 is the largest index of a pair x involves (for N = 1 both O_1 and on_{a_1} fail: 24/25 against 0, and 0 against 16/25)."

**P2. Claim 4 (v), why the rule is not linear: the reason given is wrong.**
- The text says "it is not linear in the state, since it reads the value a² itself". The technical level repeats it ("it reads the weight itself").
- That does not follow. The rule "outcome = ω_ψ(on_0)" also reads a², and it is linear.
- What the rule actually is: the sign of the value of the single element Y_n − on_0. Its outcome is 1[ω_ψ(Y_n − on_0) < 0], a step function of one value.
- Fix in (v): "it is not linear in the state: its outcome is the indicator that the value of the one element Y_n − on_0 is negative, a step function of that value."
- Fix in the technical level: "it declares the outcome by the sign of a value, not by the value."

**P3. Claim 4, proof of (iv): the dividing line is misplaced.**
- The text: "The argument concerns one element at a time; a rule built from the values of two or more elements by a function that is not linear … is not covered."
- This suggests that rules using one element are excluded. They are not: (v) uses one element, Y_n − on_0, through a threshold.
- Fix: "The argument concerns rules whose outcome is the value of an element; a rule whose outcome is a function that is not linear of values, even of the value of one element (the comparison of (v) is the sign of the value of Y_n − on_0), is not covered."
- Also in the proof of (v), replace "each a quadratic form …, so its outcome is not the value of one element" with "its outcome is two-valued and not constant in ψ, so by (iv) it is not the value of any one element".

**P4. Claim 4, lay level: says more than the proof.**
- The text: "It cannot do so through any single quantity of the framework read off the combined state."
- That is false as worded: the comparison is a test on the single quantity Y_n − on_0.
- Fix: "It cannot do so if the result is simply the value of one quantity of the framework in the combined state."

**P5. Claim 4, Reading: "No single rung's value is a datum under any of the four." False for G_4 alone.**
- (i) treats only G_1, G_2, G_3 and ⟨G_1, G_4⟩.
- Under G_4 alone, the all-on and all-off strings are fixed points. Their orbits are singletons, so every rung's value is constant on them.
- Fix: "under any of the four cases of (i) (G_1, G_2, G_3, and G_1 with G_4)."

**P5b. Claim 4 (v), notation (minor).**
- The setting numbers the planes H_1, H_2, …, and (iii) uses off_1 off_2.
- But (v) puts the system on rungs 0 and 1 (v_0, v_1, on_0), which the setting does not define.
- Fix: either number the planes from H_0, or write φ_0 = v_1|0⟩, φ_1 = v_2|0⟩ and use on_1, with data rungs d_k ≥ 3.

**P6. Claim 3 (iii): "not uniform" without a bound (minor).**
- Any nonzero pointwise convergence fails to be uniform over all elements, by scaling. So the sentence as written says nothing.
- Fix: "not uniform over elements of norm at most 1 (O_N² is an idempotent, so ‖O_N‖ ≤ 1), i.e. not in norm."

**P7. Claim 1 (ii), "each of them alone admits other invariant extensions": false for σ_e at ℓ = 0.**
- At ℓ = 0, invariance under σ_e kills the values on e and fe. Reality kills the value on f, because f† = −f. So the extension is unique (computed).
- The lay sentence "if either does not count, this conclusion fails" has the same gap.
- Fix in the formal level: "each of them alone admits other invariant extensions (σ_f alone for every ℓ; σ_e alone for ℓ ≥ 1, while for ℓ = 0 reality forces Ω(f) = 0 and σ_e alone gives uniqueness)."
- Fix in the lay level: "… if either does not count, this conclusion fails in general."
- Trivial, same sentence: "the state with ω(e) = 1" should read Ω(e) = 1.

---

## Task 2. New statements verified (one line each)

**Claim 1**
- σ_e-counterexample at ℓ = 1: correct (own code).
  - e_1 f is self-adjoint with square 1.
  - Its state is positive: exact Gram matrix on all 16 blades.
  - It is σ_e-invariant and not σ_f-invariant.
  - It restricts to ⟨·⟩_0 on A_1, with Ω(on) = ½ and Ω(e_1 f) = 1.
- σ_f-counterexample at ℓ = 0: correct (values 1, 1, 0, 0; on-weight ½).
- "Boosts do not commute with †": correct.
- (iv) transport g∘α: correct. Additivity on the four even P_s gives exactly one string with value 1; a sign change of the f_j preserves the even subalgebra and †, so g∘α is again a two-valued additive weight.

**Claim 3**
- Spectator independence of I_K: correct. Algebraically, c_j x c_j† = (−1)^{|x|} x on the spectator; computed 72/125 for 1, 2, 3 filled pairs.
- Non-uniformity: correct. The gap is 24/25 for N ≤ 3, c ∈ {3/5, 0}, ω_∞(O_N) = 0, and O_N² is idempotent on the sector.
- Coverage note on odd elements: correct.
- New HS sentence 2 + 2s²N: correct (system diag(1, −1) gives 2; each pair gives 2s²).
- Reading's ignorance sentence: correct. ω_∞(x) = 9/25 ω_A(x) + 16/25 ω_B(x) on every x. At finite N the state is a pure vector state, and O_N separates it from the mixture. The sentence is correctly labelled a premise and not a mechanism.

**Claim 4**
- (i), three orbits under ⟨G_1, G_4⟩: correct. Each type is one orbit, and finite / cofinite / neither is invariant.
- (i), "no single rung's value constant on a class": correct for the four cases of (i).
- (ii), symmetric state: correct as argued from the import. Clause (a) states factoriality. The entries of A^{1/2} − P_s are 1/√2 or 1/√2 − 1, never 0, so the difference is not Hilbert-Schmidt, and the states are not quasi-equivalent, hence disjoint.
- (iii), P_0 = off off: this is the vacuum projector, and the four atoms are orthogonal projections with sum 1 (own code).
- (iv), pointwise-limit sentence: correct (three directions determine the three coefficients).
- (v), frequency ⌈2^n a²⌉/2^n and bound a² ≤ freq < a² + 2^{−n}: correct.
  - By enumeration, n ≤ 8 and 120 rational targets.
  - In my own Fock module, n = 5 and three values of a.
- (vi), agreement of the two rules: correct.
  - Checked by hand, and by enumeration for n ≤ 9 and 86 non-dyadic targets.
  - The non-dyadic hypothesis is needed only for the undecided string: for a² = ½ with digits 1000, that string gives the second outcome.
- Reading: correct apart from P5.
  - The two kinds of premises match claim 2.
  - Typicality, fresh rungs, independence and access to the state are listed.

**Claim 2**
- Changed wording ("premises of two kinds", "argued from the Powers and Stormer criterion"): correct.

---

## Task 3. Titles, one-liners and levels

- Claim 1: title and one-liner correct. Technical level correct. Lay level: see P7.
- Claim 2: correct.
- Claim 3: title, one-liner and lay level correct. The technical sentence "with complete records (c = 0) it is zero unless the element involves every pair" is correct for the interference itself; P1 concerns only the comparison with ω_∞.
- Claim 4: title and one-liner correct. Technical level: P2. Lay level: P4.

## Task 4. New or changed checks, and perturbations (`perturb.log`)

- **Claim 1**, `check_either_sign_change_alone_…`: it tests what it says.
  - Broken: u = e_0 e_new in place of e_0 f_new. Caught.
  - Deleting the restriction assertion passes, as expected for a removed line.
- **Claim 3**, `check_record_modes_…`: it now computes the symbols from the branch vectors.
  - Broken: one pair left unrotated. Caught.
  - Broken: mode sign (c, +s). Caught.
- **Claim 4**, `check_comparison_rule_…`:
  - Broken: threshold shifted by 1/32. Caught.
  - Broken: agreement test reversed. Caught.
  - "<" replaced by "≤" passes, which is harmless because a² is not dyadic in the check.
- **Claim 4**, `check_rung_permutations_…`:
  - Broken: e ↦ f in the permutation. Caught.
  - Broken: wrong image string. Caught.
- Coverage still calls `check_comparison_rule_…` "complete" for n = 4 only. Acceptable, since it says "general n is the proof".

---

## Verdicts

- **Claim 1: NOT READY.** One clause: P7. A universal statement in the formal level is false at ℓ = 0. Ready once P7 is applied.
- **Claim 2: READY.**
- **Claim 3: NOT READY.** P1: the corrected c = 0 sentence is still false (counterexample on_{a_1}, N = 1). P6 is minor.
- **Claim 4: NOT READY.** P2 to P5 misstate the dividing line that is the claim's content (the comparison is a threshold on one element's value), and the Reading's "any of the four" is false for G_4 alone. P5b is notation.

---

## Confirmation pass (commit 8712d68, diff HEAD~1..HEAD on store/claims)

All changed sentences were read at every level, along with proof-main.tex, check.py and coverage.yaml of claims 1, 3 and 4.
- Own computations: `work-R3/conf_l2.py` (log `conf_l2.log`).
- One perturbation of the new check lines: `work-R3/pert/conf_C3_pair1_filled/` (log `conf_perturb.log`). It was caught.
- All store checks still pass: claim 1 6/6, claim 2 5/5, claim 3 4/4, claim 4 7/7.

**P1 (claim 3 (iii)): applied correctly.**
- Formal statement: correct. It now has both conditions (every involved pair is coupled; one coupled pair is not involved), and "in particular N > p + 1".
- The two N = 1 counterexamples are right: O_1 gives 24/25 against 0, and on_{a_1} gives 0 against 16/25 (own Fock).
- The proof's added explanation (Ψ_N fills only pairs j < N) is correct.
- New check lines: they test what they say. Changing Ψ_1 to fill pair 1 makes the check fail.

**P6 (claim 3): applied correctly.** "Not uniform over elements of norm at most 1, that is not in norm", with ‖O_N‖ ≤ 1 from O_N² idempotent.

**P2 and P3 (claim 4 (iv), (v), technical level, proof): applied correctly.**
- The rule is now the sign of the value of Y_n − on_1.
- "By (iv) it is not the value of any one element" now follows from the outcome being two-valued and not constant in ψ (for each fixed s, the outcome is 1[y(s) < a²], which changes with a).
- The dividing line is stated as value against sign of a value.

**P4 (claim 4 lay): applied correctly.**

**P5 (claim 4 Reading): applied correctly.** "In any of the four cases of (i) (G_1; G_2; G_3; G_1 with G_4)" is true.

**P5b (rung numbering in claim 4): applied correctly.**
- The setting (H_1, H_2, …), (iii) (rungs 1, 2), (v) (system on rungs 1, 2, data on further rungs, on_1) and the one-liner (on_1) agree.
- The proof notes that the script numbers from 0. No stale on_0 or v_0 remains in claim 4's text.
- Recomputed with the system on rungs 1, 2 and data on rungs 3 to 7: the frequency of [value of Y − on_1 < 0] equals ⌈2^n a²⌉/2^n for a = 3/5 and 5/13, n = 5.

**P7 (claim 1 (ii)): applied correctly.**
- At ℓ = 0, σ_e alone gives uniqueness among states. Invariance kills the values on e and fe, and reality kills the value on f because f† = −f. Checked by hand; the new check lines test exactly these sign actions.
- "Ω(e)" is corrected.
- Technical level, "for one or more old rungs under that of e alone": the proof shows ℓ = 1. I computed ℓ = 2 as well: ½(1 + e_1 f) gives a positive state (exact Gram matrix), σ_e-invariant, equal to the trace on A_2, with on-weight ½ and value 1 on e_1 f. The general ℓ ≥ 1 case is the same argument.
- Lay level, "fails in general": correct.

**Titles, one-liners and lay levels of all four claims, re-read: nothing says more than its proof.** Two optional points:
- Claim 4, technical level: "A rule that declares the outcome by the sign of a value does select" reads as if it covered every such rule. Optional: "Such a rule can select: …".
- Claim 3, coverage.yaml: the two clause (iii) counterexamples live in `check_interference_is_full_…`, whose clauses list only (ii). The (iv) entry still says "clause (iii), a limit, … is not computed". Optional: add (iii) to that function's clauses.

**New errors introduced: none found.**

**Verdicts after the confirmation pass:** claim 1 READY; claim 2 READY; claim 3 READY; claim 4 READY.

---

## No-collapse restatement and open problem

Read:
- `store/open_problems.yaml`, entry `op.outcome-selector-premises` (commit 804c6f4).
- `git diff HEAD~1 HEAD` for `one-relation.record-chain-votes-measurement-without-collapse`, version 8 to 9 (commit 0fb5114), and `pred.no-objective-collapse`.

Stored entities checked against: the indifference instrument Fact, `tower.answers-iteration-question`, `singularity.p-reduced-metric-level-reading-many`, the registered free inputs, `docs/CONTRIBUTING-rules.md` (amendment kinds), and the four reviewed claims.

### (1) op.outcome-selector-premises

**Premises (A), (B), (C) compared with claim 4's Reading.**
- The Reading lists premises of two kinds. Actuality: the occupation context is the level of facts; one string is actual; it is typical for the uniform weight; fresh rungs are used for each event; the rungs are independent of the system. A law: the rule of (v), and an order of reading.
- (A) matches Actuality except that it **omits "fresh rungs for each event"**. (B) and (C) split the Law into two premises.
- The regrouping into three is legitimate, but nowhere is it said that it is a regrouping of the Reading's two kinds.

**Problems**

- **Q1, statement (A): a premise is missing.**
  - Fix: "(A) the occupation context is the level of facts and one string of rung values is actual, typical for the uniform weight, read on fresh rungs for each event, and independent of the system measured".
  - Fix: after (C), add "((A) is the Reading's premise of actuality; (B) and (C) together are its law)".

- **Q2, known: "a deterministic law on strings [is] not a selector". As written, this contradicts claim 4.**
  - Claim 2 (iii) excludes only a rule mapping strings of a fixed finite set of rungs to strings, with the string as the only hidden datum. It says such a law "is stochastic, or draws on data outside those rungs".
  - Claim 4 (v) is a deterministic rule that draws on data outside those rungs.
  - Fix: "a deterministic law mapping strings of a fixed finite set of rungs to strings, with the string the only hidden datum, is not a selector".
  - The same qualifier is needed in the no-collapse proof (R4 below).

- **Q3, known: "a limit state that is the mixture of two disjoint states".**
  - The mixture is proved on the algebraic tower (claim 3 (iii)).
  - The disjointness is argued from the import (claim 3 (iv)).
  - Fix: "the mixture of the two branch states on every element (proved), states that are disjoint in the completed algebra (argued from the imported Powers and Stormer criterion)".

- **Q4, known: the stored bearing of the indifference premise is assigned to the wrong premise.**
  - The stored Fact (`one-relation.imported-indifference-instrument`) reads first: "Indifference forbids uncaused structure: a construction may not carry distinctions nothing in the framework determines".
  - Claim 1 (i) shows that the completion determines no rung value.
  - So an actual string is, on the face of that wording, such a distinction. The stored premise bears directly on (A), not only on (B).
  - Against this stands the Fact's moduli clause ("genuine moduli are data rather than smoothed away"), which may admit a tail class as a datum.
  - Fix: under "Against premise (A)" add: "the indifference premise in its stored wording forbids distinctions nothing in the framework determines (Fact one-relation.imported-indifference-instrument), and by Theorem synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight (i) the completion determines no rung value, so an actual string is on its face such a distinction; whether the moduli clause of the same Fact admits a tail class as a datum is open".
  - Fix: under (B), replace "nothing stored; …" with "nothing stored beyond the indifference premise, whose clause on uncaused selections does not obviously apply to a selection fixed by an actual string and the state; the question moves to (A)".

- **Q5, why and success: overstated, and inconsistent with no-collapse version 9.**
  - "If the premises can be derived, the framework has a mechanism" is too strong. A derivation gives a deterministic selector of outcomes with the weights of (P). Ending interference still rests on the stored recorded-sectors premise, or on the record limit (claim 3). Claim 2 names both jobs.
  - "A derivation of all three … refutes the no-collapse stance as registered" contradicts the sentence version 9 adds. The registered stance (no objective-collapse signature) concerns stochastic and gravitational collapse, and the deterministic rule "is not a collapse of that kind, and what signature, if any, it would have is not examined".
  - Fix in why: "If the premises can be derived, the framework has a selector of outcomes with the weights of (P) (the end of interference still resting on the recorded-sectors premise or the record limit), and the conclusions of the no-collapse result (all branches occupied; no selector within the framework) must be withdrawn".
  - Fix in success: "A derivation of all three gives the framework a selector and refutes the vote's conclusion that all branches are occupied; whether it touches the registered stance on objective-collapse signatures depends on whether the rule has a signature, which is not examined".

- **Q6 (minor), known: "Against premise (A): the symmetric state … is disjoint from every string state".**
  - This is not evidence against (A). It shows only that (A) cannot be read off the symmetric state.
  - Fix: "Bearing on premise (A)".

- **Q7 (minor), attack 2: "the first half of (A) follows" says more than the cited Proposition.**
  - The Proposition gives "the metric level is the joint-diagonal algebra" under the sheaf assembly.
  - That this is "the level of facts" is a further identification, which claim 4 (iii) also leaves as a reading.
  - Fix: "… the metric level is the joint-diagonal algebra by theorem, and the first half of (A) reduces to identifying the metric level with the level of facts".

**Checked and correct**
- Statement: "no mechanism … a survey, not a proof" and the description of the sign rule with the citation of claim 4 (v), (vi). The weights hold to within 2^{-n}, and exactly when read until decided, given typicality.
- Known, finite towers: claim 1 (i) to (iii) and (ii) are correctly stated.
- Known, multi-mode descent: correct.
- Known, infinite tower: the three cases, "no single rung's value constant on a class", and linear against sign of a value, all as claim 4 states them.
- Known, the ignorance premise in the limit: as claim 3's Reading states it (argued).
- Known, against (C): matches `tower.answers-iteration-question` (frozen clock; one rung per shadow wall, displaced away from the physical region).
- Why: "the no-collapse result argues that a selector would need unboundedly many fresh bits" is fair to version 8.
- Attack, last bullet: the registered free inputs do outnumber the papers' two numbers. See (2).

**Verdict (1): NOT READY.** Q1, Q2, Q4 and Q5 need the fixes above. Q3 is a strength flag; Q6 and Q7 are minor.

### (2) No-collapse claim, version 8 to 9

**Correct as cited**
- **"the store has since registered further free inputs beside the two numbers": correct.** The store registers, as postulates:
  - `synthesis.number-n-registered-free-input` (N);
  - `synthesis.matter-asymmetry-registered-free-input` (ε);
  - `synthesis.down-type-126-weight-registered-free-input` (w_d);
  - `synthesis.majorana-scale-free-input` (an input "beside N and v/H").
  The list is finite, which is all the argument uses.
- **"it counts items of data, not information": correct.** It is a fair scope statement: one registered rational or real number can carry unboundedly many bits, so a finite count of items bounds nothing in bits.
- **"with both sign changes … counted as symmetries, gives the values no meaning beyond a relabelling": correct.** Under the group of sign changes, all strings are one orbit (claim 1 (iii)). The one class bit appears only under rotors, so it is rightly not mentioned here. The citation of clauses (i) to (iii) is right.
- **The sentence added to the first gap (records of unbounded length): correct and at the right strength.** It says "model coupling written by hand", "what the premise says holds in the limit", "premise not derived", and the mixture is on the algebraic tower's elements. The proof cites claim 3 (i) to (iii).
- **The sentence added to the registered stance: correct.** It is consistent with claim 4 (the rule is deterministic given its premises), and "signature not examined" is honest.
- **Amendment kind "restatement": correct.** `docs/CONTRIBUTING-rules.md` defines restatement as "the formal statement changed", and the formal level changed.
- **Defect text: fair to version 8.** Version 8 says "a mechanism that uses freedom the framework does not possess is not an open alternative within it", stated as closing the question.
- **The original two arguments, premises and registered stance: unchanged verbatim.**
- **Lay and one-liner: accurate at lay strength**, apart from the omission covered in R2.
- **`pred.no-objective-collapse`, repinned @8 to @9: still holds as cited.** Its basis ("a collapse mechanism would be the uncaused selector the framework forbids"; null results consistent; one signature refutes) survives verbatim in version 9. Version 9 states that the deterministic rule is not a collapse of that kind.

**Problems**

- **R1, "a selection determined by an actual string and the system's state is not on its face an uncaused selection, so the first argument does not by itself exclude it": misleading by omission (same point as Q4).**
  - The stored indifference Fact forbids "uncaused structure: … distinctions nothing in the framework determines". The actual string on which the selection rests is, on the face of that wording, such structure (claim 1 (i)).
  - So the first argument bears on premise (A) even if not on the rule.
  - Fix: "A selection determined by an actual string and the system's state is not on its face an uncaused selection; but the actual string it rests on is, on the face of the stored wording of the indifference premise (which forbids distinctions nothing in the framework determines), uncaused structure, since the completion determines no rung value (Theorem synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight (i)); so the first argument bears on the premise of an actual string rather than on the rule, and whether it excludes it, given the moduli clause of the same premise, is part of that problem."
  - In the proof, change "an observation about the wording of the indifference premise" so that it names both clauses.

- **R2, the formal and technical premise lists are incomplete compared with claim 4's Reading.**
  - Formal: "(one string of rung values is actual, typical and independent of the system; …)" omits "the occupation context is the level of facts" and "fresh rungs for each event".
  - Fix (formal): "(the occupation context is the level of facts and one string of rung values is actual, typical, read on fresh rungs for each event and independent of the system; the sign rule is a law; rungs are read in an order)".
  - Fix (technical): make the corresponding change.
  - Fix (lay): "that one pattern of settings is real and typical".
  - The formal phrase "given an actual typical string" in the sentence on clauses (v), (vi) should likewise read "given an actual typical string, with fresh rungs for each event, independent of the system".

- **R3, proof: "its Reading lists the three premises" is inaccurate.**
  - Claim 4's Reading lists premises of two kinds.
  - Fix: "its Reading lists the premises, of two kinds (actuality; a law with an order of reading), grouped here as three; they are argued there and not stored."

- **R4, proof: "That integer states, parity sectors and a deterministic law on strings do not select" needs the qualifier of claim 2 (iii).** As Q2 notes, claim 4's rule is a deterministic law that selects.
  - Fix: "a deterministic law mapping strings of a fixed finite set of rungs to strings, with the string the only hidden datum".

- **R5 (minor), formal: "it shows that a selector of outcomes is not among the framework's stored structures" credits the counting argument with what the survey shows.**
  - The counting argument shows that the stored free data cannot supply a fresh bit per event. That no stored structure selects is the result of the survey (claims 2 and 4).
  - Fix: "it shows that the stored free data do not supply a fresh uncaused bit per event (that no stored structure selects is the survey of the results cited below), not that a selector cannot be added".

- **R6 (minor), maintainer note: "This entity's open_problem field still names op.trichotomy-exhaustiveness".**
  - That problem is in `open_problems_settled.yaml`.
  - The note is accurate, but the field should name `op.outcome-selector-premises`, or the note should say the named problem is settled.

**Verdict (2): NOT READY.** R1 to R4 need the fixes above; R5 and R6 are minor. The conclusions of the two arguments, the premises and the registered stance are untouched, and the restatement kind and the dependent prediction are right.

---

## Confirmation pass 2 (commit 4e65c53)

Read: `git diff HEAD~1 HEAD` on `store/open_problems.yaml` and the no-collapse claim. I then re-read the whole open-problem entry and all four levels and the proof of the no-collapse claim as they now stand.

**Fixes applied as written, all correct:**
- Open problem: Q1, Q2, Q3, Q4, Q5 (why and success), Q6, Q7.
  - Q3 also gained "for an element reaching every record". That is correct (claim 3 (ii)).
- No-collapse claim: R1 (formal, and the proof's two-clause reading of the Fact), R2 (formal, technical and lay, plus "with fresh rungs for each event, independent of the system" on the clauses (v), (vi) sentence), R3, R4, R5, R6.
- The why and success of the open problem now agree with each other and with the no-collapse claim's stance sentence. A derivation would refute the vote's conclusion; the registered signature stance is left open.

**Changes beyond my list:**
- **(a) Attack item widened to "Premises (A) and (B) against indifference": correct, and an improvement.** It now poses both questions the stored Fact raises: an actual string as a distinction nothing determines, against the moduli clause; and the clause on uncaused selections.
- **(b) Entities: `one-relation.recorded-sectors-superselected-premise` replaced by `one-relation.imported-indifference-instrument`: acceptable.**
  - The indifference Fact is now cited by `\claimref` in "known". The recorded-sectors premise is named only in words in "why".
  - The eight `\claimref`s in the text now equal the eight entities.
  - I did not find a written limit of eight in `docs/`, so the reason given is unverified. The choice is right either way.
- **(c) No-collapse technical: "the indifference premise, as worded, bears against the first of these": accurate but one step stronger than the formal.**
  - The formal adds that the moduli clause of the same premise may admit a string or its tail class.
  - Optional fix: "the indifference premise, as worded, bears against the first of these, though its clause on moduli may admit it".
- **(c) No-collapse lay: "The first of these sits badly with the framework's own rule against unexplained distinctions, since nothing in the framework fixes the settings": acceptable at lay strength.** Optional, same caveat: add "though the same rule lets genuinely free numbers stand as data, which might cover it".

**Re-read in full.** Nothing else says more than its proof.
- Statement, why, known and success of the open problem are each supported at the stated strength.
- The no-collapse one-liner's "one exists given three premises" uses "one" for "a mechanism that selects". That matches the formal's "can be written". The lay level now says "a rule that picks one".
- pred.no-objective-collapse still holds as cited.

**Problems:** none blocking. The two optional points are the caveat in (c), technical and lay.

**Verdicts:**
- **op.outcome-selector-premises: READY.**
- **No-collapse restatement (version 9): READY.**
