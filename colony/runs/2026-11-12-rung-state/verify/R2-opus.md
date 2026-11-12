# Referee report 2, run 2026-11-12-rung-state (Claude Opus 5.5)

Brief: REFEREE-2.md. Claims reviewed:
3. `synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit`
4. `synthesis.infinite-strings-tail-classes-and-no-reading-law-inside-the-algebra`
1. `synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight` (as amended)
2. `synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws` (as amended)

Nothing under `store/` was changed and nothing was committed. I did not read `work/`. All my code is in
`verify/work-R2/` and is exact (Fractions). It uses its own explicit sparse matrices: the MSB basis with the
Jordan-Wigner string over the *higher* modes, and elements expanded in Clifford blades `1, e, f, fe` per rung.
The author used the LSB basis, lower-mode strings and the `1, v, w, vw` basis. I did not reuse any of the
author's helpers.

| file | what it does | result |
|---|---|---|
| `mx.py` | own matrix helpers | - |
| `c3_recompute.py` (log `c3_recompute.log`) | claim 3, all clauses | all pass; one counterexample found |
| `c4_recompute.py` (log `c4_recompute.log`) | claim 4, plus a counterexample in amended claim 1 | all pass; two counterexamples found |
| `route_sectors.py` (log `route_sectors.log`) | the route left open (task F) | pass |
| `perturb.py` (log `perturb.log`, copies in `pert/`) | 13 perturbations of the two checks | see B |

Labels used below: **proved** (I checked the argument), **computed** (by my code), **argued** (reasoning only, not a full proof), **mem** (literature cited from memory, not checked).

---

## A. Claims 3 and 4, step by step

### Claim 3

**Setting.**
- **proved.** R_j is an even rotor: h_j = ½(e_a e_b − f_a f_b) is a bivector with h_j³ = −h_j, so R_j = exp(θ h_j) with cos θ = c.
- **computed.** U_j is unitary and U_{N−1}…U_0 Ψ_0 = 3/5 A_N + 4/5 B, for N = 2, 3 and c ∈ {3/5, 0, −5/13}.

**(i), the factor c^(N−k): correct for every element, odd ones included. proved and computed.**
- The proof is valid. x commutes with R_j for j ∉ K. This holds even when x is odd, because R_j is even and supported on pair j only.
- R_j†B = cB − s h_j B. Every other term puts pair j's quantum on b_j. x cannot change that occupation, and in A_K that quantum is on a_j.
- Odd x: both sides vanish, because both branches hold 1 + N quanta.
- Elements that move a quantum between the system and a pair are covered, provided the pair is in K.
- **computed.** My recomputation covers the full blade basis on the system plus K, for every proper K:
  - N = 2: 528 elements; N = 3: 13072 elements.
  - Three values of c, including a negative one.
  - Basis elements with nonzero I_K: 434 at c = 3/5 and 122 at c = 0, for N = 3.
  - 240 random integer combinations, with odd parts, explicit hops v_0 w_a and v_a w_1, and interleaved K = {1}, {0,2}, {2}, {1,2}.
- **computed.** The hypothesis is not idle: with K = {0}, 64 blade elements touching the uncoupled pair 1 violate the factor.
- **Unstated step.** I_K(x) is defined with B and A_K on N pairs, so it depends on N through the filled spectator pairs. The proof of (iii) uses, without saying so, that I_K does not depend on that. That is true (computed: identical for N = 1, 2, 3 with K = {0}), but it should be stated.

**(ii) is correct. computed.**
- For N = 1, 2, 3 and c ∈ {3/5, 0}, on the whole module: O_N is even and self-adjoint, O_N² is idempotent, its value is 24/25, and its branch values are 0.
- **Missing consequence (proved).** O_N is a self-adjoint partial symmetry, so ‖O_N‖ ≤ 1. Hence ‖ω_{Ψ_N} − ω_∞‖ ≥ |ω_{Ψ_N}(O_N) − ω_∞(O_N)| = 24/25 for every N. The convergence in (iii) is pointwise only, never in norm. "Not uniform over elements" says this, but weakly.

**(iii): the limit exists, it is a state, and the mixture formula is right. One sentence is wrong.**
- **proved.** Existence, positivity and the formula ω_∞ = 9/25 ω_A + 16/25 ω_B follow as written.
- ω_A ≠ ω_B (they differ on on_0), so ω_∞ is a genuinely mixed state and a weak* limit of pure ones.
- **Tautological.** "No element of the algebraic tower has a nonzero interference in ω_∞": interference in ω_∞ is never defined (I_K is defined for vectors). Read as ω_∞ − mixture, the sentence just restates the formula. What is proved is exactly: ω_∞(x) = 9/25 ω_A(x) + 16/25 ω_B(x) for every x in A.
- **WRONG (computed counterexample): the last sentence.** It reads: "For c = 0, ω_{Ψ_N}(x) equals the mixture's value as soon as N exceeds the largest pair x involves." Pairs are numbered from j = 0. Take c = 0, N = 1, x = O_1:
  - The largest pair O_1 involves is pair 0, and N = 1 > 0.
  - Yet ω_{Ψ_1}(O_1) = 24/25, while the mixture's value is 0.
  - The proof's own condition (N > k, with K inside the N pairs) is right. The formal paraphrase is off by one. The pre-registration (1c) already had the same slip.

**(iv): the import is applied correctly, as an argument. argued from the import.**
- **computed.** For N = 3 and c ∈ {3/5, 5/13} I computed the full one-particle symbols S_ij = ω(a_j† a_i) of both branches directly from the vectors:
  - both are projections;
  - branch A is quasi-free: all 4096 four-point functions obey Wick's rule;
  - ‖S_A − S_B‖²_HS = 2 + 2s²N (the 2 comes from the system).
- **proved.** For projections both Powers-Stormer conditions reduce to "P − Q is Hilbert-Schmidt", and that fails over infinitely many pairs when s ≠ 0.
- Clause (d) gives purity. Clause (a) gives "not quasi-equivalent", and factor states that are not quasi-equivalent are disjoint.
- The import says what is needed: clause (a) states it for 0 ≤ A, B ≤ 1 over a complex Hilbert space; clause (d) states purity iff A is a projection.
- **Caveats, correctly flagged in the formal level.**
  - The step from the real Clifford tower to the complex CAR algebra is not proved here.
  - The import's statement of (a) and its pages are cited from memory in the Fact itself.
  - The technical level states the disjointness without "argued".

### Claim 4

**Setting.** String states are well defined. **proved.**

**(i): the groups and the orbits.**
- **G1 and G3 are well defined. proved.** Any sign change of generators preserves the relations. On A every element involves finitely many generators, so even an infinite sign change is an automorphism of A. It commutes with †, which is generator-wise (e† = e, f† = −f).
- **G2 is well defined. proved and computed.** Conjugation by an odd unitary of a finite floor is an inner automorphism of A that **negates every generator beyond the floor** (computed for e_0 on 3 rungs). It is an infinite sign change hidden inside G2. It fixes every on_j beyond the floor, so the orbit statement for G2 is right.
- **The orbit statements are right. proved.** Under G1 and G2 the orbits are the tail classes, and there are 2^ℵ0 of them. Under G3 there is one orbit.
- **A natural group is left out, and it changes the picture: permutations of the rungs.** Exchanging the hyperbolic planes H_i ↔ H_σ(i) is a †-commuting automorphism of A (computed for a swap of two rungs: relations and adjoint preserved).
  - Under all bijections σ of the rungs, a string's orbit is fixed by its pair (number of on rungs, number of off rungs).
  - Together with G1 there are exactly **three** orbits: finitely many on; finitely many off; infinitely many of each. So almost every string (all of the third kind, which is every string a fair coin produces) is one orbit. **argued**, elementary.
  - Permutations do not preserve the floors, and the stored tower orders its rungs (one per shadow wall). Whether they count is a reading, exactly like G3. The "per group" answer should list them.
- **Another natural group, which does not change the strings' picture: infinite products of even unitaries on disjoint finite blocks.**
  - It contains the even part of G3. For example, the sign change of every f is ∏_k Ad(f_{2k} f_{2k+1}).
  - It also acts on sectors that contain no string. ∏_j R_j is in it, and it carries the string state A_∅ to claim 3's branch A.
  - So under this group with G1, the two outcomes of claim 3 are one orbit as well. **argued.**

**(ii) is correct. proved.** The Powers-Stormer step is applied correctly: the symbol is diagonal with entries s_j, the difference of two symbols is diagonal with entries in {0, ±1}, and it is Hilbert-Schmidt iff the strings are in one tail class.
- **Missing, and it matters for the Reading. argued from the same import.** On the infinite tower the symmetric (tracial) state is the gauge-invariant quasi-free state with symbol ½·1. By clause (a) it is a factor state. For every string, ½^{1/2} − P_s has every diagonal entry nonzero (1/√2 or 1/√2 − 1), so it is not Hilbert-Schmidt. So **the symmetric state is disjoint from every string state.**
- It is the barycentre of the string states as a weak* integral over the Bernoulli measure. It is not a decomposition inside its own folium: no string state is normal in its GNS representation.
- So reading the symmetric state as ignorance of an actual string leaves its representation altogether. Contrast claim 3's ω_∞, whose two parts are normal in it and canonical.

**(iii) is correct. computed (own matrices for the four atoms).** As the author now says, it is near-tautological: any complete orthogonal family of atoms averages to the trace. The use of the stored proposition is accurate: its antecedent is "a choice, not a consequence". `P_0` is not defined in claim 4's formal level.

**(iv): the lemma is proved without continuity, and its use is correct as stated in the formal level.**
- **The lemma is proved; the proof is correct.**
  - There are infinitely many rational directions, so by pigeonhole one value ν is taken in infinitely many of them.
  - q − ν(a² + b²) is a binary quadratic form vanishing in infinitely many projective points, so it is zero.
  - This holds over any field containing the coefficients, so it also covers the real limits of the "pointwise limit" sentence.
- **What follows is exactly this.** Suppose that, for each fixed datum, the outcome indicator is ψ ↦ ω_{ψ⊗data}(y) for one element y of A (or of α(A), or a pointwise limit), and the data are independent of ψ. Then the indicator is constant in ψ. That is the linearity no-go: an outcome indicator that is linear in the state cannot be two-valued and non-constant.
- **The title, one-liner, lay level and Reading say more ("no reading law inside the algebra", "anything the framework's own mathematics can express"). That broader statement is false. Counterexample, computed (`c4_recompute.py`):**
  - Take system rungs 0, 1, data rungs 2..5 in a string s, and Y = Σ_{k=1..4} 2^{−k} on_{1+k} ∈ A.
  - Rule: outcome 1 iff ω_{ψ⊗s}(Y) < ω_{ψ⊗s}(on_0). Both quantities are values of elements of A in the one joint state.
  - Over the 16 data strings, the frequency of outcome 1 is:

    | ψ | 1 | 0 | (3/5, 4/5) | (4/5, 3/5) | (5/13, 12/13) | (8/17, 15/17) |
    |---|---|---|---|---|---|---|
    | frequency | 1 | 0 | 3/8 | 11/16 | 3/16 | 1/4 |
    | Born weight a² | 1 | 0 | 9/25 | 16/25 | 25/169 | 64/289 |

  - Each frequency is within 2^{−4} of Born, and the odds depend on the state.
  - For a fixed datum the outcome is a non-constant 0/1 function of ψ.
  - Read digit by digit, this is exactly the rule of (v). Every quantity it reads is a value of an element of A: on_{r_k} in the data, on_0 in the system. With unboundedly many reads the probability is exactly a².
- **Rules that escape the argument, and which a reasonable reader would call "inside the algebra":**
  1. Nonlinear functions of values: thresholds, comparisons, digit tests, as above.
  2. Rules using two or more elements, with the order of the field (the ordered field is part of (P)).
  3. Rules whose element depends on the system's state (the rule reads ψ), which (v) also does.
  4. Data correlated with ψ. This is excluded by hypothesis, but only by hypothesis.

  Data that are not a product with the system (any fixed vector of a finite floor) are covered. So is any automorphism of A.
- **What divides (iv) from (v) is linear versus nonlinear in the state, not inside versus outside the algebra.**

**(v): the arithmetic and probabilities are right. proved and computed.**
- The probability is Σ d_k 2^{−k} = p.
- P(T > k) = 2^{−k}, the mean is 2, and T is finite with probability 1.
- The binary period of 9/25 is 20 (the order of 2 mod 25) and the expansion is purely periodic.
- No bounded number of reads gives a non-dyadic weight.
- **Hidden hypothesis.** "Independent unbiased values" is a statement about a probability measure on strings. A single actual string has no probability. Frequencies over repeated events need the actual string to be typical for the uniform measure (random in the Martin-Löf sense), with fresh, never-reused rungs for each event, independent of ψ. Actuality alone does not give that.
- **mem.** The attribution "von Neumann" is doubtful. His 1951 note is known for the opposite construction (fair bits from a biased coin). Knuth and Yao (1976) is the right reference for generating a biased bit from fair bits with mean cost at most 2.

---

## B. Breaking the checks (13 perturbations, `perturb.log`)

**Caught (the checks have teeth here):**
- Claim 3, (i): wrong exponent c^(N−k−1), and a record written on both branches.
- Claim 3, (ii): O_N not conjugated by U.
- Claim 3, (iv): a made-up mode in the Hilbert-Schmidt matrix (fails only because the hard-coded number changes).
- Claim 4, (i): wrong flip target.
- Claim 4, (iii): non-normalised atom.
- Claim 4, (iv): a non-quadratic "form" (a⁴, b⁴). This is the non-trivial part of check (iv): the form equals the directly computed weight.
- Claim 4, (iv): replacing the test on_0 by the identity.
- Claim 4, (v): p = 9/26.

**Weak or tautological:**
1. **Claim 3, (i), odd elements: vacuous.** Dropping every odd word leaves the check passing, including the recorded counts (74, 14). Odd words contribute only 0 = 0, so the pre-registered "open point" on odd signs was never under test.
2. **Claim 3, (iv): not tied to the state.** The Hilbert-Schmidt number comes from a hard-coded 2×2 matrix. Flipping the mode's sign to (c, +s) passes. The divergence and the quasi-free identification are not computed. I computed them: symbols from the vectors, Wick on all 4-point functions.
3. **Claim 4, (iv): the lemma's consequences cannot fail.** Loosening the bound "≤ 4 directions" to "≤ 6" passes; the actual maximum is 2. "0/1 at all seven directions implies constant" cannot fail for any quadratic form. These parts only illustrate the lemma.
4. **Claim 4, (ii): tautological.** It is orthogonality of occupation vectors.
5. **Claim 4, (iii): tautological.** Any orthogonal family of atoms averages to the trace (the author admits this).

Also: claim 3 (iii) is not computed at all (disclosed). Claim 4 (i) checks only finite flips, not the converse orbit statement. In claim 3 (ii), self-adjointness is sampled.

---

## C. Were the fixes F1 to F6 and G1 to G6 applied faithfully?

### Claim 1

- **F1: applied.**
  - New unsupported step: (iv) says clause (iii) of the cited theorem "gives a two-valued additive weight …, so there the obstruction is absent". Clause (iii) gives only *some* g, not one with g(P_s) = 1 for the given string.
  - Missing sentence: the sign changes σ_{f_j} preserve the even subalgebra and permute the P_s transitively, so g∘α has g(P_s) = 1 for any s.
- **F2: only partly applied.**
  - The Reading is fixed.
  - The extraction note still says "the one class bit of the whole string, which is the orientation bit the store already counts".
  - The lay level still says "one overall yes-or-no fact that the framework already counts once".
- **F3: applied.** But the note cites "the stored Powers, Stormer **and Takesaki** import" for the disjointness. Takesaki (KMS temperatures) is irrelevant; only clauses (a) and (d) are used. The same slip is in claim 2's note.
- **F4: partly applied, and the new text has an error.**
  - **WRONG (computed).** The formal level says the uniqueness "fails for smaller groups that do not exchange on with off …: under σ_f alone the invariant extension is not unique". But σ_f does exchange on with off (σ_f(v) = w, computed). It then concludes that uniqueness "needs the exchange of on with off, and a sign change that moves e".
  - σ_e alone satisfies both conditions and uniqueness still fails, for ℓ ≥ 1. Counterexample, computed in `c4_recompute.py` (ℓ = 1):
    - Ω(x) = tr(Px)/tr(P) with P = ½(1 + e_0 f_new), a self-adjoint projection.
    - Ω is a state under (P), restricts to the tracial ω on A_1, and is σ_e-invariant.
    - Ω(on) = ½, yet Ω(e_0 f_new) = 1 ≠ 0 = Ω_{1/2}(e_0 f_new).
  - For ℓ = 0, σ_e alone does give uniqueness, by reality (ω(f) = 0).
  - The correct statement: among the †-commuting symmetries, uniqueness needs both σ_e and σ_f (the whole group). Each subgroup of order two admits other invariant extensions:
    - σ_f alone: the state of ½(1 + e);
    - σ_e alone, ℓ ≥ 1: the state above;
    - σ_eσ_f alone: every Ω_t.
  - Not applied:
    - Boosts do not commute with † (e ↦ ce + sf gives (ce + sf)† = ce − sf). So the "enlarged group of all isometries" lies outside the claim's own definition of a symmetry. The conclusion survives a fortiori, but this should be said.
    - "Maps the new plane to itself" was kept, not dropped.
  - The lay sentence "the only arrangement that respects it is the fifty-fifty one, which has no definite setting at all" is true of the on/off weights only. The σ_f-invariant state of ½(1 + e) is sharp on e.
- **F5 and F6: applied.**

### Claim 2

- **G1 to G6: applied faithfully.** I checked the odd coupling's unitarity and its grading by hand. **proved.**
- **New inconsistency.** Claim 2's Reading says a selector is "two premises" (an actual string; a law reading rungs). Claim 4 says three (adds an order of reading). One of them should be brought in line.

---

## D. Levels of claims 3 and 4

### Claim 3

- **Title: fine.**
- **One-liner** says "a system coupled **by even unitaries**". The result is for the specific controlled pair rotors U_j, not for any even coupling. Fix: "by the controlled pair rotors U_j".
- **Technical level:** disjointness is stated as fact. Add "argued from the imported criterion".
- **Lay level:** "this explains why results stop interfering" is overstated for a coupling written by hand, whose limit no stored dynamics reaches.
- **The Reading is clearly separated.**
- **"Holds in the limit":** the stored premise is about laboratory records within the modular period. The note says so; the Reading's "the statement of Premise … holds" should say "an instance of its content holds".

### Claim 4

- **Title, one-liner, lay level and Reading point (2) are overstated.** "No reading law inside the algebra" and "anything the framework's own mathematics can express" are refuted by the threshold rule in A(iv). The technical level's first sentence is accurate: "cannot be expressed by the value of any element … after any dynamics of the algebra".
- The lay level's "changes smoothly … has to jump" rests on continuity, which the proof avoids. It is a harmless metaphor, but the true contrast is linear versus two-valued.
- **The Reading's list of premises is incomplete.** It needs:
  - (1′) the actual string is typical for the uniform measure, with fresh rungs for each event, independent of the system;
  - (2′) the rule reads the system's state (the value a²).
- **The Reading's support for "one string is actual" omits the disjointness of the symmetric state from every string state (A(ii)).**
- **The "per group" answer omits rung permutations.**
- The Reading is clearly labelled.

---

## E. Pre-registration 3

The pre-registration came before the computation (commit c4e2381, then c19c7d9).
- **1a, labelled TEST, is really a proof with a sanity check.**
  - The factor is the standard Coleman-Hepp computation (mem: Hepp 1972; Bell 1975).
  - The stated surprise, a failure on odd elements, was impossible in advance: number conservation makes both sides 0.
  - The author's note concedes that the open point "turned out empty". It still reports 1a as a test that "holds".
  - The interleaving signs were a real but slight slip risk.
- **1c, PROOF:** contains the c = 0 off-by-one.
- **2a, 2b, 3a, 3b, 3c:** fairly labelled.
- **2c:** the author's own correction stands: its outcome was fixed.
- **2d, SEARCH:** fair; reported.
- **3a's "Prediction"** ("a selector cannot be a law inside the algebra at all") already framed a conclusion broader than 3a can deliver. That framing reached the title.
- **Groups were named in advance, which is an improvement.** But the obvious relabelling group (rung permutations) was not among them.
- **Net: one item mislabelled besides 2c (1a). Nothing in the pre-registration was a test whose failure would have changed the answer.**

---

## F. The overall answer, sentence by sentence

**S1.** "In a model coupling, the stored premise that recorded outcomes cannot interfere becomes a statement that holds in the limit of unbounded records and fails at every finite stage; it selects nothing."
- **Supported, with three corrections.**
- "The stored premise … becomes a statement" overstates. What is shown is a hand-written coupling in which the premise's content holds exactly in the limit, on the algebraic tower. On the C*-completion that is argued from the import. The premise itself (laboratory records, irreversibility within the modular period) is not derived.
- "Fails at every finite stage" is true for one element reaching all records, O_N, whose distance stays 24/25. For any fixed element the interference decays as c^(N−k). With complete records it is exactly zero once one pair is untouched (not, as claim 3 says, once N exceeds the largest pair index).
- **Missing:** in the limit the decomposition ω_∞ = 9/25 ω_A + 16/25 ω_B is canonical. It is the central decomposition into two disjoint factor states, so it is unique (argued; standard, mem: Bratteli and Robinson, Sect. 4.2). With complete records the two outcomes are string states that differ at every rung, so they are two tail classes of Step 2 (computed for N ≤ 3, `route_sectors.py`).

**S2.** "Whether rung values are data on the infinite tower depends on which symmetries count; under changes on finitely many rungs the tail class is an infinite datum that nothing in the algebra connects, under sign changes of arbitrary sets of generators it is a label."
- **Supported** (proved; the C*-level part argued from the import).
- **Missing:**
  - (a) No individual rung value is a datum under any group considered; only the tail class is.
  - (b) Rung permutations, which are †-commuting and natural, give a third answer: with finite changes, three orbits.
  - (c) The symmetric state is disjoint from every string state. So "ignorance of an actual string" is not a decomposition of that state within its representation.
- Also: Step 2 bears directly on Step 1. Whether the two recorded outcomes of the limit are data or labels is the same group question.

**S3.** "Even granting an actual string, no rule expressible by values of elements of the algebra can select an outcome with state-dependent odds; a rule outside the algebra can, and needs three premises the store lacks."
- **False as worded.** A rule that compares values of two elements of A (on_0 and Σ 2^{−k} on_k), or reads values digit by digit, selects with Born odds, computed above. The rule of (v) is itself such a rule.
- **True:** no rule whose outcome, for fixed data independent of the system, is the value of a single element (or a limit of such) in the joint state. That is, the outcome cannot be linear in the state.
- **"Three premises" is route-specific and incomplete.** The string route also needs:
  - the actual string to be typical (random) for the uniform measure, with fresh, never-reused rungs for each event, independent of the system;
  - the rule to read the system's state (the exact value a²). That makes it a hidden-variable law of pilot-wave type, nonlinear in the state.
- Claim 2 says two premises, claim 4 three.

**S4.** "So there is still no mechanism in the stored content; a mechanism would be a theory of a different kind added to it."
- **"No mechanism in the stored content": supported** as the result of a survey (the four candidates, the three steps, my searches), not as a theorem.
- **"A theory of a different kind": overstated.** The threshold rule uses only values of elements and the order of the field, both inside the framework's mathematics. What is missing is a *law*: a dynamical postulate nonlinear in the state, or stochastic, plus a premise of actuality. That is new premises, not new mathematics.

**Routes the answer leaves open.**
1. **Superselection plus ignorance in the record limit** (Hepp; Primas; Landsman, mem). In the limit of unbounded records, ω_∞ has a canonical decomposition into two disjoint sectors, the two recorded outcomes. With complete records these are two tail classes (computed). They are data under G1 and G2 and labels under G3 or under permutations plus G1.
   - One premise, "one sector is actual, with probability equal to its weight", turns the weights 9/25 and 16/25, which (P) already supplies as values of the sectors' projections, into outcome probabilities. This needs no reading rule, no reading order and no random string.
   - This is not a mechanism. Nothing dynamical selects, and the premise is the Born rule read as ignorance. The limit is never reached at a finite stage (Bell's objection, which is claim 3 (ii)), and no stored dynamics writes such records.
   - It does show that "three premises" is not the price of every route. The cheapest stored-adjacent route to definite outcomes costs one premise plus the limit.
   - It also avoids the problem in S2 (c): the sectors are normal in ω_∞, whereas strings are not normal in the symmetric state.
2. **A nonlinear (threshold) law on values**, as computed above. It reproduces Born odds exactly with mean 2 reads. It needs actuality, typicality, independence and access to the state. It is the pilot-wave pattern, and the store holds none of it.
3. **A stochastic nonlinear dynamics** (GRW, Diósi-Penrose; mem). It is not in the store and was not examined. It escapes (iv) because its outcome is not a value of a fixed element.

---

## G. Verdicts

**Claim 3: SOUND WITH FIXES.**
1. (iii), last sentence. Replace it with: "For c = 0, ω_{Ψ_N}(x) equals the mixture's value as soon as at least one of the N pairs is not involved by x; in particular for N > p + 1, p the largest pair x involves. For N = p + 1 it can fail: x = O_{p+1}."
2. (iii). Replace "No element … has a nonzero interference in ω_∞" with: "ω_∞ equals the mixture on every element of A. The convergence is pointwise and not in norm: |ω_{Ψ_N}(O_N) − ω_∞(O_N)| = 24/25 for every N."
3. Proof of (iii): state that I_K(x) does not depend on the filled spectator pairs.
4. One-liner: "coupled by the controlled pair rotors U_j" in place of "by even unitaries".
5. Lay level: replace "this explains why results stop interfering" with "this shows how, in this model, interference becomes undetectable in the limit".
6. Technical level: add "argued from the imported criterion" to the disjointness.
7. Coverage: say that odd elements give 0 = 0. Compute the Hilbert-Schmidt number from the branch symbols, not a hard-coded matrix.
8. Optional: for c = 0 the branches are string states in different tail classes (link to claim 4).

**Claim 4: OVERSTATED.** The formal clauses (i) to (v) are sound. The title, one-liner, lay level and Reading are not.
- True weaker statement for the title and summaries: "no reading law whose outcome, for data independent of the system, is the value in the joint state of one element of the algebra (or a pointwise limit of such)". Rename accordingly, for example "no reading law linear in the state".
- Say that a rule comparing values of elements (a nonlinear function of values) does select with Born odds, and that (v) is such a rule.
- Fixes:
  1. Add rung permutations to the groups of (i): with G1, three orbits.
  2. Add, argued from import (a): the symmetric state of the infinite tower is a factor state disjoint from every string state.
  3. Complete the Reading's premises: typicality and independence of the actual string, fresh rungs for each event, and the rule's access to the state.
  4. Define P_0.
  5. Drop or qualify "von Neumann".
  6. Align the premise count with claim 2.

**Claim 1 (amended): SOUND WITH FIXES.**
1. Replace the group-dependence sentence with: "among the †-commuting symmetries, uniqueness needs both σ_e and σ_f; under σ_f alone a sharp invariant state exists (ℓ = 0: ½(1 + e)); under σ_e alone, for ℓ ≥ 1, the state of ½(1 + e_1 f) is invariant and differs from Ω_{1/2}; under σ_eσ_f every Ω_t is invariant." Do not say that σ_f fails to exchange on with off.
2. Say that boosts do not commute with †.
3. Apply F2 to the extraction note and the lay level.
4. In (iv), add the transport g∘α that gives g(P_s) = 1.
5. Remove "Takesaki" from the disjointness citation.

**Claim 2 (amended): SOUND WITH FIXES (minor).**
1. Remove "Takesaki" from the note.
2. Reconcile "two premises" with claim 4's three.

---

## Error count

| kind | count | items |
|---|---|---|
| wrong mathematics | 2 | claim 3 (iii) off-by-one (counterexample O_1 at N = 1, c = 0); claim 1 (ii) group-dependence sentence (σ_f mischaracterised; σ_e-alone counterexample at ℓ = 1) |
| unsupported or overstated wording, in the claims | 14 | see the list below |
| unsupported or overstated wording, in the overall answer | 4 | S1, S3, S4, and the omitted route of the record limit |
| weak or tautological checks | 5 | see B; claim 3 (iii) not computed is disclosed, so not counted |
| pre-registration mislabelling (besides 2c) | 1 | 1a |

The 14 wording items in the claims:
- Claim 4:
  - title, one-liner and lay level: "inside the algebra" and "anything the framework's mathematics can express";
  - incomplete premise list;
  - rung permutations omitted;
  - disjointness of the symmetric state from strings omitted;
  - the von Neumann attribution.
- Claim 3:
  - one-liner "even unitaries";
  - lay level "explains";
  - the undefined or tautological "interference in ω_∞", with the pointwise-not-norm point missing;
  - technical-level disjointness not flagged as argued.
- Claim 1:
  - F2 not applied in the note and lay level;
  - F4 partial (boosts and †);
  - the (iv) transport step missing.
- Claims 1 and 2: Takesaki cited for disjointness.
- Claims 2 and 4: two versus three premises.
