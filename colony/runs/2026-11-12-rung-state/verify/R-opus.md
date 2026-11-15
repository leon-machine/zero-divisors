# Referee report R-opus, run 2026-11-12-rung-state

Claims refereed:
1. `synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight` (v1)
2. `synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws` (v1)

I did not read `work/`. My scripts are in `verify/work-R/`. They use `lib/GA.py` for blade products and my own
helpers (`myalg.py`) for everything else. Where I could, I recomputed by a second route: an explicit real
Jordan-Wigner matrix representation of Cl_Q(n,n), in which the (P) adjoint is the transpose (`r0_selftest.py`
checks the Clifford relations, adjoint = transpose and faithfulness for n = 1, 2, 3). All arithmetic is exact
(Fractions). Labels: **proved**, **computed** (exact, finite cases), **argued**, **conjectured**. Literature
cited from memory is marked (mem).

Summary of verdicts:
- Claim 1: **SOUND WITH FIXES**. Clauses (i) to (iii) are correct. The uniqueness in (ii) holds up better than the
  author says. Clause (iv) has a hidden hypothesis (odd tests), and under the store's univalence premise its
  conclusion is false. The lay text and the one-liner say more than the proof does about "without end".
- Claim 2: **SOUND WITH FIXES**. Every computation is correct, one sentence in (i) is wrong as worded, and the
  technical level's "the stored content holds no selector" is broader than the evidence. The store does hold a
  one-way map that ends interference in the record basis (the multi-mode descent), and the claim does not
  mention it.

---

## A. Proof steps, citations, checks, recomputations

### Claim 1

**(i) proved, correct.** I checked each step by hand. on = (1+p)/2 with p = fe is even, self-adjoint, and commutes with A_l. For x = a + be + cf + dp: on x on = (a+d) on, and on x off = (b+c) e off, so g = b + c. Also (g e off)(g e off)^dagger = g on g^dagger = gg^dagger on. The map a -> a on is injective on A_l, because A_{l+1} = A_l + A_l e + A_l f + A_l p is a direct sum. That gives E_1(xx^dagger) = E_1(x)E_1(x)^dagger + gg^dagger, so positivity holds. Reality holds, and the bound
t in [0,1] is necessary for every extension, product or not (Omega(on on^dagger) = Omega(on) >= 0, and the same for off). The
proof leaves the step "a on = 0 implies a = 0" implicit (fix F6).

**(ii) proved, correct, and stronger than stated** (see B). An automorphism invariant under sigma_e and sigma_f vanishes on A_l e, A_l f and A_l p. Uniqueness holds among all linear functionals, with no positivity needed.

**(iii) proved, correct.** Gamma anticommutes with every generator (the dimension 2m is even), so it commutes with every even element. Gamma P_s = c(-1)^{|s|} P_s. A sign change of f_j flips entry j of a string, and pairs of flips are
Ad(f_i f_j). Recomputed by the matrix route (`r2_strings.py`):
- 8 rank-one orthogonal projectors summing to 1;
- Gamma P_s = c(-1)^{|s|} P_s with one overall sign c;
- Gamma commutes with all 15 bivectors;
- a breadth-first orbit of P_000 under conjugation by 21 unitary rotors (pure bivectors and 3/5 + 4/5 bivector) reaches exactly the 4 even strings.

**(iv) computed as stated, with a hidden hypothesis.** See B4.

**Cited entities.**
- `set-and-clear`, `ladder-pairs`, `exchange... (v)` and `no-two-valued... (i)` say what the proof uses, at the pinned versions.
- `rungs.imported-totality-minimality-completion@6` is stated for real Cl(V) with p + q >= 3. The case l = 1 (A_1 = Cl(1,1), p + q = 2) and the field Q are outside its hypotheses. The algebra of the claim does not use the Fact beyond the motivation "a step adjoins one hyperbolic plane", so nothing breaks, but the citation does not cover l = 1 (fix F5).

**Check perturbations** (`perturb.py`, run on copies):
- (P) adjoint replaced by the plain reverse: `check_both_values...` and `check_a_string...` FAIL. They are sensitive to the adjoint.
- `psd` made to return True: `check_both_values...` FAILs. The negative cases t = -1/5 and 6/5 are real tests.
- Symmetry set reduced to {sigma_f}, {sigma_e} or {sigma_e sigma_f}: `check_one_invariant...` FAILs. The check's
  uniqueness test is tied to the full group, as it should be.
- Not detectable by the checks: the only extensions sampled are the product family Omega_t, so "only t = 1/2 is invariant" is
  tested only inside that family. Uniqueness among correlated extensions rests on the blade argument, which is complete. My own linear solve below confirms it.

### Claim 2

**(i) proved, computed, one wrong sentence.** The matrix route (`r3_selector.py`) finds exactly 5 states in the integer box {-2,...,2}^3, which is wider than the author's {-1,0,1}^3. Their weights on "on" are 0, 1/2, 1/2, 1/2 and 1. Two survive the switch form: on and off.
The m-rung argument (Cauchy-Schwarz, then P_s x P_s in Q P_s because P_s is rank one) is correct. The phrase "each rung's algebra is the 2x2 matrices" is loose, since the rungs are graded-tensored, but the conclusion holds.
**Wrong as worded:** "none has a weight strictly between 0 and 1 ... on any e_j". A string state has omega(e_j) = 0,
so its weight on the test (1 + e_j)/2 of the Q-algebra is 1/2. The definiteness holds only for tests inside the
switch's integer form (fix G1).

**(ii) proved/computed, correct; one sentence too weak.**
- Centre of the even subalgebra: I computed dimension 2 for Cl(2,2), Cl(3,3) and Cl(4,4). The claim states it only for
  Cl(2,2) but uses it on Cl(4,4) (fix G2).
- The record example, recomputed by the matrix route: rho idempotent, X^2 = 1, U orthogonal, record weights 9/25 and 16/25 with perfect correlation, the same Gamma sign on both branches, O = 24/25, and 0 after removing the interference. Every number agrees.
- **Missed, and it strengthens the claim:** an odd homogeneous coupling U_odd = off_1 e_4 + on_1 e_3 is unitary and
  odd, writes the record on a single rung, and keeps even states even. By clause (ii) of the cited
  records theorem it is allowed. It changes the parity of both branches together, so they stay in one sector
  (computed: weights 9/25 and 16/25, both branches with sign +1, even observable value 24/25). The general fact, **proved** in one line: Gamma U = +-U Gamma for homogeneous U, so a homogeneous unitary maps a sector into a single sector. The sentence about U' implies that parity-changing couplings are excluded. Only inhomogeneous ones are (fix G3).

**(iii) computed, correct.** R is orthogonal, and the weights from (1,0) are 9/25 and 16/25 (matrix route). See C for what it shows.

**(iv) correct.** The product of two symmetric extensions gives the four strings weight 1/4 each.

**Check perturbations:**
- Adjoint replaced by the reverse: (i) and (ii) FAIL. (iii) passes, correctly, since R is unit for both.
- Amplitudes swapped (4/5, 3/5): (ii) FAILs.
- `psd` made to return True: (i) FAILs.

The checks are not vacuous.

---

## B. Hidden hypotheses and overclaiming

**B1. Is "symmetry of the step" the right group? computed (`r1_uniqueness.py`, l = 0, 1, 2).** I solved, exactly, the linear system lambda = omega on A_l plus lambda(gx) = lambda(x) for each group's generators, with and without reality, and counted the free parameters of the invariant extensions.

| group | free params (with reality), l = 0/1/2 | weight on "on" forced to 1/2? |
|---|---|---|
| authors' {sigma_e, sigma_f} | 0 / 0 / 0 | yes |
| all isometries of the new plane, O(1,1)(Q) (adds the boost (5/4, 3/4)) | 0 / 0 / 0 | yes |
| all automorphisms fixing A_l and commuting with dagger (inner: Ad(e Gamma_old), Ad(3/5 + 4/5 f Gamma_old)) | 0 / 0 / 0 | yes |
| inner rotations only | 0 / 1 / 6 | yes |
| the exchange sigma_f alone | 1 / 3 / 10 | yes |
| sigma_e alone | 0 / 1 / 6 | yes |
| joint flip sigma_e sigma_f alone | 1 / 3 / 10 | **no** (every Omega_t invariant) |
| the switch-preserving group (boosts v -> lambda v, w -> w/lambda, plus the joint flip) | 1 / 3 / 10 | **no** |

Findings:
- **Uniqueness survives the two larger natural groups.**
  - The isometries of the plane are the natural group, because the Fact says the plane is unique up to isometry.
  - Every automorphism that fixes A_l and commutes with dagger is inner, by an element of the centraliser {1, eGamma, fGamma, p} of A_l (Skolem-Noether, mem; argued). Those elements are similitudes for dagger, so the restriction "maps the new plane to itself" in the definition is not needed.
- **The weight 1/2 needs only one element that moves "on".** Any group containing one forces the weight 1/2, including a rational rotation that does not exchange on and off.
- **Uniqueness, "not sharp" and "not integer" fail for the exchange alone.** Under sigma_f alone the extension omega times the state (1+e)/2 is a state under (P), is sigma_f-invariant, and is sharp: its new-rung density is an idempotent. Its value on e is 1, it is integer-valued on the blades, and its weight on "on" is 1/2 (computed, l = 0, 1, 2). This is the omega(e) = +-1 state of claim 2 (i).
- **Nothing is forced under the group that preserves the switch as a switch.** If set and clear keep their roles (boosts and the joint flip), every t is invariant. On and off are then not exchanged by any symmetry, and the first clause of H-datum survives.

So the claim's (ii) holds exactly when the exchange of set and clear counts as a symmetry. The stored exchange theorem itself says that "whether the exchange is a symmetry of the stored laws is not decided here, and the stored results point the other way for the linear map". The extraction note flags the reading. The formal level does not, and the lay level does not either ("The construction has a symmetry that swaps on with off"). See fix F4.

**B2. Q.** argued.
- Nothing above depends on Q beyond needing 2 to be invertible, which is already in the store.
- Rational rotors exist (Pythagorean triples), so the inner group is available over Q.
- One small Q effect: no single rational pair rotor takes a sharp string to weights (1/2, 1/2), since c^2 = 1/2 has no rational solution. The "coin" is reachable only as a mixture or with non-unit rational vectors. Nothing in either claim uses this.

**B3. Infinite tower.** proved from the stored import and a computed lemma.
- Every element supported away from rung j commutes with on_j (computed for m = 3; this is the general reason). So on the algebraic (or CAR) tower, two strings that differ in infinitely many places are not related by any element of the tower.
- By `synthesis.imported-powers-stormer-takesaki-disjointness` (a) and (d), the string states are pure Fock-type states, and those that differ on infinitely many modes are disjoint (A - B is an infinite-rank projection difference, so it is not Hilbert-Schmidt).
- So under the inner (local) symmetries the strings fall into 2^aleph0 classes, each a superselection sector. Under all sign-change automorphisms (outer, particle-hole on infinite sets) there is still one orbit.

On the infinite tower, the question Leon actually asked ("iterating the transport without end"), clause (iii) and H-datum are **UNCLEAR**: the answer turns on whether outer automorphisms count as symmetries. The claim says the infinite tower is not treated. Its one-liner ("so iterating the transport supplies two-state systems but ... no bits of data") and its lay text ("adding switches without end gives an endless supply of coins") do not restrict themselves to finite towers. That is an overclaim (fix F3).

**B4. Clause (iv) needs odd tests.** computed and proved (`r5_even_weights.py`).
- The atom of weight 1/2 used in (iv) (y = P_s + v_j P_s) is not even.
- The cited theorem's own clause (iii) says that the even subalgebra of two modes does admit two-valued weights.
- Explicit construction, **proved**, and checked on 32 even line projectors and 256 sampled even contexts. The even subalgebra is M_2 + M_2, the two Gamma sectors. Put g = 1 on the rank-one projectors of the sector containing s whose line has slope m in (-1, 1], measured in the basis (P_s, other string), and g = 0 on everything else. Then g is additive on orthogonal pairs, sums to 1 on every context, and gives P_s the value 1.

So **under the store's univalence premise** (physical states even, observable algebra even: `singularity.p-univalence`,
`descent-lift.imported-descent-modes-univalence-supplied-class`), a string *does* extend to a pre-assignment
of outcomes to every (even) test. (iv) holds only if odd atoms are tests, and (P) explicitly leaves that open. This is the main correctness fix for claim 1 (F1).

**B5. "The orientation bit already counted".** argued.
- The rotor-class bit of an m-rung string is a chirality: which family of maximal isotropic subspaces (pure spinors) the string belongs to.
- The stored orientation bit is the sign of the Witt flag on the descent's three pairs.
- The two are bits of the same kind. That they are the same bit is asserted in the Reading and the extraction note, not shown. On the infinite tower there is no volume element at all (F2).

**B6. Claim 2 levels.**
- The technical level says "So the stored content holds no selector". The evidence is four named candidates on finite towers, and the extraction note itself calls the result a survey. See D and fix G4.
- The lay level, "the framework as it stands contains no chooser", is the same overreach. My own search (E) supports it for *choosing* (b), but not for the reason given.

---

## C. Were the pre-registrations fair tests?

Every prediction came true. Given how the kill conditions were written, that was close to guaranteed, so "outcome as predicted" carries little evidential weight here.

- **H-forced.** Killed if both on and off extend omega. This is true for every state on every algebra once a 2x2 tensor factor is adjoined (product extensions), so the outcome was fixed in advance by elementary state theory. It is a fair formalisation of the question but an uninformative test.
- **H-datum.** The first kill clause ("a symmetry of the step exchanges on and off") is satisfied by definition once sigma_f is put into the group, and the author chose the group. Under the switch-preserving group the clause fails (B1), and on the infinite tower under local symmetries the second clause fails too (B3). As written, H-datum was set up to die. I would call it a straw man unless the group choice is defended.
- **H-coin.** A fair, non-trivial test. Uniqueness could have failed and does fail for smaller groups. The prediction survives the larger natural groups (B1).
- **C1 (integer states).** Near-tautological: an integer-valued normalised positive weight on orthogonal projectors is 0/1. The kill ("definiteness only by removing superposition") is correct, and the prediction was certain.
- **C2 (parity sectors).** The kill follows from a one-line theorem: homogeneous unitaries preserve sectors, and a 2-sector rule cannot separate more than two outcomes anyway. More importantly, it tested the *weakest* parity idea, total parity. The store's own descent on many modes is the mode-wise parity average composed over modes, which is complete dephasing in the string basis (`obj.singularity.multi-mode-descent`), and that does end interference between records (E1). That stronger stored form was not tested. The kill text "a coupling that does change parity is not even and sends an even state to a state that is not even" is also false as a general statement (odd homogeneous couplings, A).
- **C3 (deterministic law).** A straw man taken alone: with the string itself as the only hidden variable, a sharp start is a point mass, and a function maps point masses to point masses. The fair version allows hidden data beyond the string, which is C4. C3 and C4 together are fair.
- **C4.** Its kill ("no stored premise makes the string actual") is a statement about the store, settled without a recorded search. I searched (E) and also found none. The flag-as-datum premise makes one bit a datum, not strings.

---

## D. Is the conclusion broader than the evidence?

"The stored content holds no selector; one could be added only as new premises."

- **What the computations support (proved/computed):** on finite towers and under (P), none of the four candidates selects, and iteration by itself fixes no value on a rung.
- **What is broader:**
  1. "The stored content" means 1402 claims. Four candidates were examined. The store contains a one-way, algebra-forced map whose range it calls "the classical algebra of occupation records" (E1), and an imported disjointness theorem that gives Hepp-type exact decoherence in the infinite limit (E2). The claim misses both. Neither *selects*, so the "no selector" conclusion survives, but the stated reason ("the one exact superselection rule cannot do (a)") understates what the store holds for half (a).
  2. The infinite tower is where the question lives, and it was not treated (B3).
  3. "Only as new premises" is argued. Underneath it is the counting argument of `one-relation.record-chain-votes-measurement-without-collapse`, which counts *data items* ("two numbers and one bit"). The two numbers are declared *continuous* (`one-relation.imported-flag-arrow-superselection`), and a continuous datum carries unboundedly many bits. A finite seed plus a deterministic law also produces outcome strings that no finite experiment tells apart from fair ones. So what excludes a selector in the store is the absence of a *law*, not the finiteness of the count (argued; E5). The conclusion "one could be added only as new premises" is right, but for that reason.

---

## E. Search for a mechanism

I searched the store with `search_claims` and `find_text` for: descent, eviction, pinching, one-way door, modular period, boundary modes, orientation bit, infinite tower or CAR, disjointness, state selection and Hepp. Results by candidate:

**E1. The multi-mode descent (stored).**
- *Where in the store.* `obj.singularity.multi-mode-descent`; `descent-lift.imported-descent-modes-univalence-supplied-class`, which says "on nu modes the composite of the mode-wise averages is the pinching onto the joint-number-diagonal algebra"; and `descent-lift.within-supplied-dynamics-descent-has-no` (lift), which makes it one-way within the supplied dynamics.
- *What it delivers.* (a) exactly: it ends interference between strings, irreversibly. It preserves the Born weights. It does not deliver (b).
- *Computed (`r3_selector.py`).* Applied to the author's post-record state it gives exactly the record-diagonal state: O goes from 24/25 to 0, and the weights stay 9/25 and 16/25.
- *The catch.* Applied before any record, it also kills the system's own interference (hop observable 24/25 -> 0). So it needs a premise saying which modes are pinched and when: at records, not always. Applied unconditionally it has C1's defect.

**E1'. The corner read-out D(x) = PxP of the descent (stored, `transport.pinching-kernel`).**
- It does "select": conditioning on P = on_3 gives the system branch with weight 1 (computed).
- The selected corner is fixed by the choice of descent projector, not drawn with weight Omega(P) (= 9/25 here). Renormalising is Lueders conditioning, that is, the collapse postulate.
- Born-weighted selection would need the corner to be chosen at random with weight Omega(P). That is a stochastic premise. Killed as a mechanism; it is the collapse rule restated.

**E2. Coleman-Hepp records on the CAR limit (stored: `tower.car-limit-even-charge` plus Powers-Stormer (a), (d)).**
- *Set-up, with my prediction written in the script before it ran.* The system is one quantum on two rungs (3/5, 4/5). The apparatus is N rung pairs, and the even record coupling rotates each pair by (c, s).
- *Computed (`r4_hepp.py`, N = 1, 2, 3, c = 3/5 and c = 0).* The squared Frobenius norm of the interference block visible to *any* observable on the system plus k pairs equals the prediction (12/25)^2 c^{2(N-k)} exactly. For c = 0 it is 0 unless k = N.
- *Proved, given the import.* As N -> infinity, the state converges on every element of the algebraic tower to the mixture, and the two branch states become disjoint.
- *What it delivers.* (a), exact only in the limit, and in that limit for every observable of the tower. This is the store-language version of Hepp (1972, mem). It bears directly on the "disanalogy" gap of the record-chain result, because it turns "recorded sectors are superselected" into a theorem in the infinite-record limit, with a geometric rate at finite size.
- *What it does not deliver.* (b).
- *Costs.* Bell's objection applies (1975, mem): at every finite stage the interference is there, for an observable touching all record rungs. The infinite coupling is not a unitary of the algebra.
- *Status.* This is the one candidate I would add to the store as a positive result about (a).

**E3. Tail classes of the infinite tower (proved from the import plus the lemma).**
- There are 2^aleph0 disjoint sectors under local symmetries (B3). They give the framework a place for an *infinite datum*, the actual tail class.
- Local dynamics preserve them, so they are static and supply no per-event bits without a law reading ever deeper rungs. That makes this E4. No selection by itself.

**E4. A deterministic law reading an actual infinite string (C4 made explicit).**
- The unique symmetric state, iterated, is the uniform product measure on {0,1}^N. A deterministic read rule ("read rungs until 9/25 is decided") reproduces any rational Born weight exactly.
- *Computed (`r6_bits.py`).*
  - With a bounded number k of reads, only dyadic weights j/2^k are possible. 9/25 is not dyadic: its binary expansion has period 20.
  - With unbounded reads, P(read > k) = 2^-k, the expected number of rungs read is 2 per binary event, and the error is at most the undecided mass, which goes to 0.
- *What it delivers.* (b) with correct weights, combined with E1 or E2 for (a).
- *What it needs.* Two new premises (the string is actual; the law reads it). It also needs an order in which rungs are "fresh", and the store denies that order: `tower.answers-iteration-question` says the tower is Morita-stationary ("the clock never ticks"), and that rungs beyond the first sit on shadow walls "displaced successively away from the physical region". The author did not use this, and it counts against C4 being even natural.
- *Status.* Available only as new premises, as the author said, and against stored structure.

**E5. Pseudo-random or superdeterministic selection from finite or continuous stored data** ('t Hooft's cellular automaton interpretation, mem).
- It evades the counting argument as stated (D). It needs a law, and no law of that kind is stored.
- Telling it apart from fresh randomness is a question of algorithmic randomness (Martin-Lof, mem), not of any finite experiment.
- Argued only. Not a stored mechanism.

**E6. "Eviction keeps one of Catalan-many replica saddles".** The "selection" is saddle dominance in an entropy (Renyi) computation, not the selection of a measurement outcome. Argued from the statement. Not relevant.

**E7. The KMS simplex / extremal decomposition (`state-selection.imported-general-statement`).**
- Selecting an extremal (pure-phase) component is fixed by boundary data, like spontaneous symmetry breaking.
- The rung's 1/2 state is the beta = 0 (tracial) state. The CAR algebra has a unique trace (mem), so the simplex is a point and there is nothing to select. Takesaki disjointness is between different temperatures, not between outcomes.
- Argued. Killed.

**E8. Outside the store (mem, not computed).**
- GRW/CSL: stochastic. E4's coins could serve as their noise source, which still means two new premises.
- Diosi-Penrose: needs a gravitational self-energy, which the tower algebra lacks. Not assessed.
- Bohm, Bell's fermion-number beables and Vink: C3 and C4.
- Consistent histories and many-worlds: no selection. Many-worlds is the store's own stance.

Net result of E: the store supplies half (a) twice, as a forced one-way map (E1) and as an exact limit theorem (E2). It nowhere supplies half (b) with Born weights. Every route to (b) I found needs a stochastic premise or a law reading data, the same two premises the author named.

---

## F. Verdicts and fixes

### Claim 1: SOUND WITH FIXES
- **F1 (needed).** Clause (iv): add "if the atoms of mixed parity are tests". Add the converse: "if only even elements are tests (univalence), a string does extend to a two-valued additive weight on all even self-adjoint idempotents (clause (iii) of the cited theorem)". Change the Reading, technical and lay sentences ("a pattern of settings could not, even in principle, fix the answers to all possible measurements") to match.
- **F2.** Reading and extraction note: replace "which is the orientation bit the store already counts" with "a chirality bit of the same kind as the stored orientation bit; that it is that bit is not shown".
- **F3.** One-liner and lay: restrict to finite towers ("on every finite tower ..."). Add to the note that on the infinite tower, under local symmetries, strings fall into uncountably many disjoint classes (Powers-Stormer), so the datum question there turns on whether outer automorphisms are symmetries.
- **F4.** Formal (ii), or a remark: state that uniqueness holds unchanged for all isometries of the new plane and for all dagger-commuting automorphisms fixing A_l (so "maps the new plane to itself" can be dropped), and that the weight 1/2 is forced by any group containing an element that moves "on". State that under sigma_f alone uniqueness fails and a sharp invariant extension exists (omega(e) = 1), and that under the group preserving set and clear (boosts and the joint flip) every t is invariant. Lay: "if swapping on with off counts as a symmetry".
- **F5.** The totality/completion Fact covers p + q >= 3 over R. Either note that l = 1 and Q lie outside it and that the clause does not use it, or cite the tower entity for the step.
- **F6 (minor).** In (i), say that a -> a on is injective on A_l (direct sum).

### Claim 2: SOUND WITH FIXES
- **G1.** (i): replace "or on any e_j" with "on any element of the switch's integer form (their weight on the test (1+e_j)/2 of the rational algebra is 1/2)".
- **G2.** (ii): state the centre for Cl(n,n) in general. It is standard, and I computed it for n = 2, 3, 4.
- **G3.** (ii): add that every homogeneous unitary maps a Gamma-sector into one sector (Gamma U = +-U Gamma). Add that an odd homogeneous record coupling (off_1 e_4 + on_1 e_3) is allowed and still leaves both branches in one sector, with interference 24/25 visible. Drop the suggestion that parity-changing couplings as such are excluded.
- **G4.** Technical and lay: replace "So the stored content holds no selector" with "None of the four candidates is a selector on finite towers". Add that the store's multi-mode descent does end interference in the record basis (complete dephasing to the joint-number-diagonal algebra, one-way within the supplied dynamics), so half (a) is available as a stored map if a premise places it at records, while half (b) is absent. Cite `obj.singularity.multi-mode-descent`.
- **G5.** (iii): say explicitly that the only hidden variable is the string itself. Add that with unread rungs as further hidden data, a deterministic read rule gives exactly dyadic weights for bounded reads and any rational weight for unbounded (almost surely finite, mean 2 rungs) reads.
- **G6.** (iv)/Reading: note `tower.answers-iteration-question` (no clock; rungs beyond the first on shadow walls away from the physical region) as a stored reason the "fresh rungs" reading lacks support. Mark "no stored premise makes a string actual" as the result of a search, not a computation.

### Answer to the maintainer's question

Is there a mechanism for the collapse of the wave function in this framework, building on the tower? **No, not in what is stored. A collapse needs two things: ending interference, and choosing one outcome with the Born weights. The store does the first and not the second.**

The first half is there, and the authors missed it. The descent on many modes is a one-way map, forced by the algebra, that removes all interference between occupation records while keeping their weights. On the infinite tower, records of unbounded length make the branches exactly disjoint for every observable of the tower, with interference falling off geometrically at finite size (a Coleman-Hepp result in the store's own terms).

Nothing in the store chooses. The descent's corner read-out picks a fixed branch, not a weighted one. Integer states, parity, deterministic laws on strings, the symmetric "coin" state, eviction and the KMS structure do not choose either. Every route to choosing that I found needs either randomness supplied from outside or a law that reads data, such as unread rungs or digits of a stored number. Those are the two new premises the authors named. The tower's structure (no clock, rungs on walls away from the physical region) gives no support for treating rungs as fresh coins.

How confident should he be?
- **High** that nothing stored selects outcomes with Born weights. This rests less on the four tests, whose outcomes were close to fixed when the kill conditions were written, than on the structural point that selection needs a stochastic input or a law, and the store has neither.
- **Moderate** that "one could be added only as new premises" is the whole story. That is argued, not proved, and the counting argument underneath it counts data items, not information.
- **Low** that the finite-tower results answer his literal question about iterating without end. The infinite tower is where the interesting structure is (uncountably many disjoint sectors, exact decoherence in the limit), and the authors did not treat it. Whether rung values there are data depends on a choice of symmetry group that nobody has made.

---

### Files
- Scripts (all exact, all run clean): `verify/work-R/myalg.py`, `r0_selftest.py`, `r1_uniqueness.py`,
  `r2_strings.py`, `r3_selector.py`, `r4_hepp.py`, `r5_even_weights.py`, `r6_bits.py`, `perturb.py`.
- On pre-registration: my prediction for E2 is written in the `r4_hepp.py` docstring, which existed before the run. For the other computations I knew the expected outcomes but did not write them down first.
- Nothing under `store/` was changed. No commits were made.
- Decisions for Leon: whether the exchange of set and clear is a symmetry of the step; whether odd elements are tests; whether to store E2 as a theorem about records in the infinite limit.
