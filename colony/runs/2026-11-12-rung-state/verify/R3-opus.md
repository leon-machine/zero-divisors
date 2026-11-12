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
