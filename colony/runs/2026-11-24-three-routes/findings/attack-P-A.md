# Attack P-A (constructive), run 2026-11-24-three-routes

Problem: op.positivity-of-values, route "records". Labels: PROVED / COMPUTED / ARGUED / CONJECTURED.
Scripts in colony/runs/2026-11-24-three-routes/work/P-A/. Nothing under store/ is edited.

## Orientation (lookups)
The problem record; synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear (entity, proof,
check); attack-L2 of run 2026-11-18-leads; attack-BA of run 2026-11-10-phase2; RUN.md target P.

## Routes (the named one and two alternatives)
- Named: every two rational vectors of Q^(2^l) lie in a four-dimensional rational subspace similar to the standard
  one; then F(r) = f(r)(r.r) obeys the parallelogram law on every pair, so F is a quadratic form. Needs the
  two-vector embedding (Hasse-Minkowski). Fails if some pair embeds in no such subspace (kill condition P2).
- Alternative 1 (own; chosen after P2 was examined on paper, before any computation): induction on the size of
  the support. Subtract the quadratic form fixed by the values at e_i and e_i + e_j; the difference G vanishes on
  vectors of support at most 4 by the two-mode theorem; a vector r of support k+1 lies in the image W of a
  coordinate four-space under ONE reflection (needs only Q(r) = a sum of four rational squares); G on W is a
  quadratic form by the two-mode theorem and vanishes on the hyperplanes x_i = 0 of W, at least three of which
  are distinct; so G(r) = 0. Needs: a ONE-vector embedding only, hence only the four-square theorem over Q.
- Alternative 2 (from the stored proof): redo the group-algebra argument for Spin(N). Much longer; not pursued.

## Kill conditions (registered in RUN.md before computing)
P1 (a non-linear additive function for three modes), P2 (two vectors of Q^8 in no four-dimensional subspace
similar to the standard one), P3 (the CHSH element is not a rational combination of rational projectors, or its
value is not fixed without additivity across non-commuting summands).
Own addition, registered now (before any script is run): P2' the one-vector embedding fails for some r
(it cannot if the four-square theorem holds over Q; the check will construct it for samples), and P1' a
quadratic form on a four-space that vanishes on three distinct hyperplanes and is not zero (none: two lines).

## Status
Both lines finished; two proposals filed (the cap). Details below.

### 13:10 Extension of the additivity theorem: FILED
Proposal: synthesis.additive-weights-on-the-rational-projectors-of-two-or-more-modes-are-linear
(check4: 0 errors, 0 other findings; validate_draft ok). Ledger: transport-absent.
- PROVED (given the stored two-mode theorem at version 1, not reproved): for every N >= 4 a function on the
  symmetric idempotents of Mat_N(Q) that adds on orthogonal ones, values in any rational vector space, no sign
  condition, is the restriction of a linear functional; hence for Cl_Q(l,l), every l >= 2. With non-negativity and
  normalisation: exactly the restrictions of the states of (P).
- PROVED: Cl_Q(l,l) = Mat_{2^l}(Q) with adjoint = transpose through the Fock elements s_S (COMPUTED completely for
  l = 3, all 64 blades); the even subalgebra is two blocks of size 2^(l-1).
- PROVED: every positive rational is a sum of four rational squares, by rotor norms and a pigeonhole induction on
  primes (five lines; the integer theorem of Lagrange and Hasse-Minkowski are NOT needed; nothing is imported).
- PROVED: P2 FIRES. If u, v lie in a four-dimensional rational subspace similar to the standard one, then
  (u.u)(v.v) - (u.v)^2 is a sum of three rational squares. e_1 and (0,1,1,1,2,0,0,0) have determinant 7, not a sum
  of three rational squares (mod 8). So the first step named in the open problem is false as stated. The proof
  filed uses one vector at a time instead: reflect a vector s of four coordinates with s.s = r.r to r; on the image
  W the remainder G is a quadratic form vanishing on the hyperplanes x_i = 0 of W (induction on the support), at
  least four distinct, and a quadratic form vanishing on three distinct hyperplanes of a four-space is zero.
- PROVED: P1 does not fire: no additive non-linear function exists for three modes (or any l >= 2).
- PROVED (new, bears on the parity item): for l >= 3 the projectors of the EVEN subalgebra alone give linearity on
  the even subalgebra (blocks of size >= 4). For l = 2 this fails (blocks of size 2; stored). So the tie between
  the reading "all rational projectors label records" and parity-odd projectors is an accident of two modes.
- ARGUED, not filed: for N >= 8 a pair embeds in a standard four-space exactly when its determinant is a sum of
  three rational squares (sufficiency via Hasse-Minkowski; not needed for anything).
- Prior art (item 3 of the target): NOT READ. Mushtari 2001: only the abstract was reachable (mathnet.ru,
  core.ac.uk and emis.muni.cz full texts are blocked by the session's network policy). The 2003 colloquium
  abstract (University of Montana) repeats the 1995/1998 result for ALL idempotents of Q^n, n >= 3. The flag stays.

### 13:25 What (RP) leaves of (P); kill condition P3: FILED
Proposal: synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes
(check4: 0 errors, 0 other findings; validate_draft ok). Conditional on Hypothesis (RP), named in the title; no
assumes edge; (P) is not used (the two identities for the bound are rederived). Ledger: transport-absent.
- COMPUTED: at the stored settings C = 2(E11 + E12 + E21 - E22) - 2 with four rational projectors of rank two
  (E_ij = (1 + A_i B'_j)/2). First clause of P3 does NOT fire.
- PROVED: C^3 = 8C, C^2 = 4 + 4K (K = e1 f2), so C is a rational combination of NO family of pairwise commuting
  rational projectors; its only rational spectral projector besides 0 and 1 is the kernel's, (1 - K)/2. C = D1 + D2,
  D1 = T11 - T22, D2 = T12 + T21, each with rational spectral projectors, D1 D2 != D2 D1. Second clause of P3 FIRES
  in its literal form: the value of the ELEMENT C is not given by weights without additivity across D1 and D2.
- PROVED (given the two-mode theorem; no sign used): for an additive function mu on projectors, sum c_i mu(E_i)
  does not depend on the decomposition of x = sum c_i E_i (commuting or not) and equals L(x). So the CHSH sum of
  four correlators, each a difference of two weights, is S = L(C).
- PROVED: with non-negative normalised weights, S^2 <= 4 + 4 L(K) <= 8 and S^2 < 8. So for the quantity a CHSH test
  reports, the consequent of P3 ("(RP) leaves the Tsirelson bound assumed") does NOT follow.
- COMPUTED (restates stored facts): the functional of value 4 is additive, normalised, takes only 0 and 1/2 on the
  sixteen joint outcomes of the four settings, S = 4, and is -1/4 on the atom of (1,0,0,1).
- ARGUED: under (RP) what is left of (P) is (a) nothing about linearity on projectors (derived); (b) the sign, which
  the reading supplies as "a frequency is not negative" and which is needed on projectors that are not joint local
  outcomes of the four settings; (c) the value of an element with irrational spectral projectors (a convention, or
  additivity across D1, D2); (d) the reality clause (fixes the extension to elements that are not self-adjoint).
  Candour: (RP) with non-negative context-independent additive weights is equivalent to (P) on projectors by the
  two-mode theorem, so this relocates (P); it derives neither (P) nor (RP).
- Not filed (depends on the first proposal, not yet stored): the same statements on l modes, and, by its clause
  (vii), with parity-even projectors only from three modes on (the parity-even CHSH setting lives on four modes).

## Kill conditions, outcomes
- P1: did NOT fire. Proved (given the stored two-mode theorem): additive implies linear for every l >= 2.
- P2: FIRED. Proved: e_1 and (0,1,1,1,2,0,0,0) lie in no four-dimensional rational subspace similar to the standard
  one (determinant 7 is not a sum of three rational squares). A different reduction was found and filed.
- P3: first clause did not fire (computed); second clause fired for the value of the element C (proved), and its
  stated consequence does not hold for the sum of four correlators (proved, under (RP)).

## Unexpected links
- The obstruction to the two-vector step is the same two-adic arithmetic that the two-mode theorem meets on unit
  atoms (its clause (v), parity of coordinates): rays are rotors of Cl^+_Q(3,0), the determinant of a pair is the
  norm of the bivector part of y x~, and 7 is not a sum of three squares. Candidate statement (argued only): a pair
  embeds in a standard four-space iff its determinant is a sum of three rational squares.
- Parity item of the same open problem: from three modes on the even subalgebra is two blocks of size >= 4, so
  additive weights on parity-EVEN projectors alone are linear on the even subalgebra. The reading (RP) can therefore
  be restricted to parity-even records without losing the theorem, except on two modes. This bears on attack item 3
  (are parity-odd elements observables) and on item 7 ("tied to the parity item": only at two modes).
- D1 and D2 anticommute (from the computed C^2 = 4 + 4K and D_k^2 = 2 + 2K: {D1, D2} = C^2 - D1^2 - D2^2 = 0). So the
  CHSH element is a sum of two anticommuting context elements of equal square, C^2 = D1^2 + D2^2, each context
  bounded by 2: the factor sqrt 2 is a Pythagorean sum of two contexts. Computed consequence, not filed as a clause.
- Sibling P-B's route R2 (the reversal on one party's algebra fixes every product of local self-adjoint elements):
  such a functional agrees with a state on all local records, and under (RP) it is excluded only by the sign on
  projectors that are not products of local outcomes, the same place where the functional of value 4 fails.

## Decisions for Leon
1. Adopt (RP) or not, and in which form: all rational self-adjoint projectors, or (from three modes on) only those
   of the even subalgebra. Recommendation: record it as a named hypothesis only; it is equivalent to (P) on
   projectors, so adopting it as a premise would replace (P) rather than derive it.
2. What "the CHSH value" means in the stored statements: the sum of four separately recorded correlators (then
   under (RP) the bound needs nothing more of (P)), or the value of the element C (then additivity across the two
   contexts D1, D2 stays assumed). Recommendation: state both, as the second proposal does.
3. Open-problem record, attack item 7: its "first step" (any two rational vectors lie in a four-dimensional rational
   subspace similar to the standard one) is false; restate it in the maintainer pass. Item 5 "not done: more than
   two modes" is done if the first proposal is accepted.
4. Imports: none needed. Hasse-Minkowski is not used; the four-square theorem in its rational form is derived inside
   the entity. Optional: import Lagrange's theorem as a Fact for the prior-art sentence.
5. Prior art: Mushtari 2001 is still unread beyond its abstract (full text blocked from this session). Before the
   extension is described as new, the paper should be read for (a) the exact statement of Problem G and (b) whether
   it already contains a reduction from Q^n to Q^4. Flag kept in both proposals.
6. After acceptance of the first proposal: extend the second to l modes and add the uses edge (maintainer or a
   later run).
7. Housekeeping: propose_claim does not carry coverage.yaml; both were copied by hand into proposals/<id>/.

## Left unfinished
Other ordered fields (needs the size-four theorem over that field and Pythagoras number at most 4); size N = 3;
sufficiency of the three-square criterion for pairs; the l-mode form of the second proposal; an audit of whether the
stored recording premises already say (RP) (sibling's side).
