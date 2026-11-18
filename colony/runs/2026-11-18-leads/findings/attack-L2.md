# Attack L2 (values), run 2026-11-18-leads

Problem: op.positivity-of-values. Four leads and one cross-link. Labels: PROVED / COMPUTED / ARGUED / CONJECTURED /
OUT OF REACH. Scripts in colony/runs/2026-11-18-leads/work/L2/. Nothing under store/ is edited.

Orientation (lookups): the problem record; synthesis.premise-positivity-of-values;
synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them;
synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects;
synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records;
synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state; earlier working
history in runs 2026-11-10-phase1 (attack-EA) and 2026-11-10-phase2 (attack-BA, attack-BB). The earlier scratch
computation on the Gleason item: weights depending only on the integer vector modulo 2, 3 or 4 are constant.

## Lead 1. The Gleason-type item (size four over Q)

Setting. Cl_Q(2,2) is the 4 by 4 rational matrices, the adjoint is the transpose in the basis s_0..s_3 of the stored
result, projectors are symmetric idempotents, atoms are r r^T / (r.r), r a nonzero rational vector. A non-negative
additive weight on projectors is the same thing as a frame function: f >= 0 on rational rays of Q^4 with
f(r_1)+f(r_2)+f(r_3)+f(r_4) = 1 on every orthogonal frame (every rational subspace has an orthogonal rational
basis). Linear means f(r) = r^T rho r / (r.r).

Routes.
- R1 (the problem's own, constructive): adapt the elementary proof of Gleason's theorem (continuity from
  non-negativity by great-circle descent, then extension to the reals). Delivers: linearity, conditional on the real
  theorem. Needs: each geometric step with rational witnesses; a near-supremum pole with a rational quarter turn.
  Fails if: a step has no rational witness.
- R2 (from another subject: the quaternion form of Cl(0,2) / the even subalgebra, and the stored two-adic facts on
  sums of squares): rays of Q^4 are the nonzero rational quaternions up to scale, i.e. the group SO(3,Q); frames are
  the cosets K x of the Klein four-groups K of half turns about a rational orthogonal triple. A counter-model would be
  a bounded function on the group whose K-averages are all 1/4 and which is not a matrix element of the rotation
  representation. Candidates: functions that factor through a finite quotient of the two-adic completion (the
  rational quaternions are a division algebra at 2, so that completion is compact and has finite quotients), i.e.
  functions of the primitive integer vector modulo 2^n. Delivers: an exact counter-model, or the exclusion of a
  whole class level by level.
- R3 (own): odd primes. The form is isotropic there; a counter-model would have to come from a unitary
  representation of PGL_2(Q_l) without K-fixed vectors.

Choice: R2 first (a finite exact computation decides each level), R1 in parallel on paper, R3 by argument only.

Kill conditions, registered before computing (14:30):
- K1a. Counter-model of residue type at level 8: a non-constant function of the primitive integer vector modulo 8
  (up to sign) that satisfies the frame equation on every sampled integer orthogonal frame. If the exact rank of the
  sampled system leaves only the constants, the residue class at modulus 8 is DEAD as a source of counter-models (a
  subset of the frame equations already forces constancy, so this is a proof for that class). If a non-constant
  solution survives, it is a CANDIDATE only: it must then be shown to satisfy all frames (by the classification of
  frames modulo 8), otherwise it is reported as undecided.
- K1b. Same at modulus 16 if the machine allows (7680 two-adic projective points); same rule.
- K1c. For R1: the route is dead if the monotonicity chain (descent along great circles) has an arithmetic
  obstruction that cannot be bypassed; partial results are then reported as partial.

Outcomes so far (14:50).
- K1a: COMPUTED, the residue class at modulus 8 is DEAD. frames_mod.py 8 9000 1: 1920 classes of primitive vectors
  modulo 8 up to sign, 9000 integer orthogonal frames (quaternion construction K x), rank 1920 over F_p, p = 2^31 - 1,
  so only the constants. (Modulus 4 rerun: 120 classes, rank 120, agreeing with the scratch of 10 November.)
- K1b (modulus 16) not run: 30720 classes need a dense elimination beyond the shared machine. Replaced by the
  structural argument below (representations of the two-adic quotient) and left as a named gap.
- Side computation, no kill condition (it could only inform): frames_box.py and frames_proj.py. Without the sign
  condition the frame equations inside a box of integer entries are far from forcing quadratic forms: in dimension
  4 the solutions on the 40 rays with entries in {0, 1, -1} form a space of dimension 19 (quadratic forms: 10), and
  enlarging the box to entries up to 2 and up to 3 (272 and 1120 rays, 380 and 2652 frames) does not cut it (19
  both times). So any proof must use non-negativity, as over the reals.

Second kill condition, registered before computing (14:52):
- K1d (linear programme on boxes). On the box T of rays with entries bounded by B, with f >= 0, all frame equations
  inside T, and f(e_0) = 1: maximise and minimise f((1,1,0,0)). A quadratic form gives exactly 1/2. If for some B the
  maximum and minimum are both 1/2, linearity is forced on that pair by a finite rational certificate (evidence for
  the statement, and a provable finite lemma). If the range stays [0, 1] or stays away from 1/2 as B grows, that is
  evidence for a counter-model (by compactness a sequence of feasible points on growing boxes with a fixed gap gives
  a global non-negative frame function that is not quadratic, provided the boxes exhaust the rays). Floating point
  here: exploration only, any certificate is redone in exact arithmetic.

Outcome of K1d (15:00): COMPUTED (floating point, exploration). With f(e_0) = 1 the range of f((1,1,0,0)) on the box
is [0,1] for B = 1, 2, [1/3, 2/3] for B = 3, [3/8, 5/8] for B = 4, [2/5, 3/5] for B = 5 (frames_lp.py): it shrinks
towards the quadratic value. In a mixed case and in the interior case (frames_lp2.py, frames_lp3.py: values fixed on
ten rays that determine the quadratic form) the values at the other tested rays are pinned to the quadratic value
exactly from B = 4 on. So no counter-model in sight, and the pinning is by equalities, not inequalities.

That changed the plan. Follow-up computations (no new kill condition needed for an exploration; the kill condition
for the resulting theorem is K1e below):
- frames_proj.py 4 1 4: over F_p the solutions of the frame system on the box B = 4 (2928 rays, 8756 frames),
  restricted to the 40 rays with entries in {0, 1, -1}, form a space of dimension 10, the quadratic forms (19 for
  B <= 3). So additivity alone, with no sign condition, forces linearity there.
- frames_closure.py 1 4: all rays of the box B = 4 of norm 5, 6, 9, 10, 12, 15, 18, 20, 30, 45 are fixed by the
  values on the 40 small rays; norm 7 enters at B = 5 (frames_cert.py 1 5 2,1,1,1 finds a certificate).
- frames_cert.py 1 4 2,1,0,0: an exact certificate, 34 frames with coefficients in (1/10)Z, verified in Fractions:
  f((2,1,0,0)) is a fixed rational combination of the weight and of the values on 18 of the 24 rays of norm 1, 2, 4.

The theorem this points to, and its proof (R2 turned constructive). Rays are the nonzero elements x of the even
subalgebra of Cl_Q(3,0) (the rational quaternions) up to scale, i.e. the group G = SO(3,Q) of rational rotors up to
scale; two rays are orthogonal iff x y^{-1} is a bivector (a half turn); frames are the cosets K x, K = {1, a, b, ab}
the half turns about a rational orthogonal triple. Let A = Q[G] / (the two-sided ideal spanned by the elements
(1 + a + b + ab) x). A function with frame sums zero is a linear map on A. The rotation representation R: A -> M_3(Q)
is onto. Steps:
 1. The 24 rays of norm 1, 2, 4 with entries in {0, 1, -1} are the octahedral group O (order 24). Its image W in A
    has dimension at most 9 (rank 15 of the 24 frame relations inside O), so R: W -> M_3(Q) is an isomorphism and A
    contains a copy of M_3(Q) with the same unit.
 2. [2 + B_1] lies in W (the certificate above). So does every element of the group G_1 generated by O and 2 + B_1.
 3. Every integer rotor of norm 5^t is a product of the six rotors 2 +- B_k and a unit (a finite table modulo 5), so
    it lies in G_1.
 4. For a rational bivector n (a half turn h_n) and g = (2 + B_1)^s = a + b B_1 with N(n) dividing b up to powers of
    5 (s exists: 2 + B_1 is a unit modulo the part of N(n) prime to 5), n g n^{-1} is an integer rotor of norm a
    power of 5 up to scale, hence in G_1. So v = R(h_n)[h_n] commutes with R(g); the same with B_2. Two rotations
    about different axes by angles other than 0 and pi generate M_3(Q), so v commutes with W.
 5. On a rational orthogonal triple the relation 1 + [h_a] + [h_b] + [h_a][h_b] = 0 with central factors gives
    v = 1. So [h_n] is in W for every n, half turns generate G, A = W = M_3(Q), and every additive weight on the
    rational rays of Q^4 is a quadratic form divided by the norm. No sign condition is used.
Consequence for the lead: DECIDED, positively and in a stronger form: on two modes over Q every weight on the
projectors that is additive on orthogonal projectors is the restriction of a linear functional; with non-negativity
and normalisation it is a state of (P).

Third kill condition, registered before the proposal's check is run (15:25):
- K1e. The theorem is dead (as a proved statement) if any of these exact computations fails: (a) the 24 rays do not
  close under the product up to scale, or the rank of the 24 frame relations is below 15, or R(O) does not span
  M_3(Q); (b) the 34-frame certificate, re-derived with S restricted to the 24 rays, does not verify in Fractions or
  disagrees with the quadratic value on a basis of the ten quadratic forms; (c) some class y modulo 5 with norm 0
  has no left divisor among 2 +- B_k; (d) the two rotations do not generate a 9-dimensional algebra; (e) an
  end-to-end sample fails: for sample bivectors n the conjugate n g n^{-1} is not an integer rotor of norm 5^t or
  does not factor. Independent of the proof: (f) a sampled frame function test, if some ray's value fixed by box
  frames differs from the quadratic value.
Prior art (web, 15:20). D. Kh. Mushtari, The Gleason theorem for the field of rational numbers and residue fields,
Mat. Zametki 64 (1998) 584-591 (abstract read): charges on the logic of ALL projectors (idempotents) of a
finite-dimensional space over Q are tr(T P). D. Kh. Mushtari, Some remarks on measures on orthogonal rational
projections and the rational sphere, Lobachevskii J. Math. 9 (2001) 47-53 (abstract read; the full text could not
be opened from here: mathnet.ru fetch was blocked): it "examines measures on the quantum logic of all projections
with rational n x n matrices and on its sublogic generated by" the lines through rational unit vectors, which is
exactly this setting. Whether it contains the statement proved here is NOT known to this pass. No priority is
claimed; the proof here is self-contained.

Outcome of K1e (15:20): no failure. All nine check functions pass (runcheck), check4 on the proposal: 0 errors, 0
other findings; validate_draft ok. (a) 24 rays closed, rank 15, R(O) of rank 9; (b) the 34-frame identity verifies
and agrees with the quadratic value on the ten basis forms; (c) 145 classes modulo 5, each with a left divisor;
(d) rank 9 for all ten sample bivectors; (e) the ten samples factor end to end; (f) the norm-7 ray (2,1,1,1) is
fixed by frames of the box B = 5 (exploration script, exact verification of the identity printed).
FILED 1: synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear.
- PROVED (with four finite exact computations in the check): every weight on the projectors of Cl_Q(2,2) that adds
  on orthogonal projectors, with values in any rational vector space and NO sign condition, is the restriction of a
  linear functional. Lead 1 is decided, positively, in a stronger form than asked.
- PROVED: with non-negativity and normalisation these are exactly the states of (P) on two modes. So the linearity
  in (P) is not an extra assumption there; what (P) adds to "weights exist, are non-contextual and add" is the sign.
  The stored functional of value 4 is an additive weight; its weight on the atom of (1,0,0,1) is -1/4.
- PROVED (exact counter-model on a smaller set): on the atoms of rational unit vectors alone a parity colouring
  gives non-negative additive weights that are not linear (values alpha_i on one odd coordinate, 1/4 on four).
  This extends the Meyer / Godsil-Zaks colouring of dimension three (from memory) to dimension four with proof.
- Transport-absent: a theorem about the rational matrix algebra; the series' content is where it places (P).
- Not done: more than two modes; other ordered fields; the 16-class computation at modulus 16 (now moot: the
  theorem excludes every non-linear weight, of residue type or not).
- Caveat for the referee and for Leon: Mushtari 2001 (see prior art above) treats this very logic and was not read.

## Lead 2. The running-maxima item

Statement. Pure-state values of the sector are the rationals X with 8 - X^2 a rational square (stored clause (ii)).
A value P/Q in lowest terms is a running maximum if it exceeds every such value of smaller denominator and is the
largest of its own denominator. Stored: computed for denominators up to 400 that the running maxima are the Pell
values S_n = 2 x_n / Q_n.

Routes. (r1, the problem's own) extend the computation: no. (r2, from the denominator law itself) classify the
deficit: 8 Q^2 - P^2 = R^2 forces P = 2a, R = 2b, a^2 + b^2 = 2 Q^2 with a, b, Q odd; b = 1 is Pell; show b >= 7
otherwise and compare with the previous Pell denominator, whose ratio to the next is below 3 + 2 sqrt 2. (r3, own:
continued fractions of 2 sqrt 2) heavier, not needed. Choice: r2.

Kill condition, registered before computing (15:30): the claim is REFUTED if for some lowest-terms pure value with
b >= 3 no Pell value of smaller denominator exceeds it; the proof route is dead if b = 3 or b = 5 occurs with
gcd(P, Q) = 1, or if Q_{n+1}^2 < 34 Q_n^2 fails for some n, or if 34 * 4 < 4 * 49 fails (it reads 136 < 196). The
check enumerates all pure values with denominator up to 1000 and compares exactly.

Outcome (15:40): the kill condition did not fire. 317 positive pure values of denominator up to 1000; b takes the
values 1, 7, 17, 23, 31, ... (all 1 or 7 modulo 8), never 3 or 5; every non-Pell value is below the Pell value of
the largest smaller denominator; records at denominators 1, 5, 29, 169, 985. check4: 0 errors.
FILED 2: synthesis.pell-values-are-the-running-maxima-of-the-pure-state-chsh-values-over-the-rationals.
- PROVED for every denominator: a pure-state value P/Q in lowest terms has deficit 4 b^2 / Q^2 with b = 1 (Pell) or
  b >= 7 (2 is not a square modulo 3 or 5); Q_{n+1}^2 < 34 Q_n^2; so a value with b >= 7 has deficit at least
  196/Q^2 > 136/Q^2 > 4/Q_n^2 and is below S_n. The running maxima are exactly the Pell values.
- Transport-absent (elementary number theory on the stored set of values). It can be folded into clause (v) of the
  stored theorem instead of standing alone: maintainer's choice.

## Cross-link: positivity of values on the matter algebra Cl(1,1) of the lattice model of 18 November

Entity read: synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation (clauses (1),
(2)): [phi_n(t), O] = g [J, O] sum G, [J, O] = (c1 - c2) p q e2.
Kill condition, registered before computing (15:50). Claim: (P) is silent on the commutator. Precisely: (a) J and O
are self-adjoint for the split and [J, O] is anti-self-adjoint, so by the reality clause every state of (P) gives it
the value 0, whatever the model; (b) the element is nonzero while states of (P) exist, so (P) does not imply
commutation; (c) the quantity a distant party could read, the first-order change of the value of O under a kick
generated by the field, is the value of the self-adjoint element I [phi, O] with I a unit commuting with the matter
algebra (not an element of Cl(1,1)); (P) bounds its value by the coefficient and the bound is attained. Dead if:
[J, O] is not a multiple of e2 or e2 is not anti-self-adjoint; or (1 +- I e2)/2 are not self-adjoint idempotents;
or a positive functional on Cl(1,1) gives e2 a nonzero value.

Outcome (15:55): the kill condition did not fire (work/L2/crosslink_cl11.py, exact, GA.py).
- PROVED (for the stored model): J and O are self-adjoint for the split of Cl(1,1), [J, O] = (c1 - c2) p q e2 is
  anti-self-adjoint (e2^dagger = -e2), so by the reality clause of (P) EVERY state gives the commutator the value
  0, and (P) puts no condition on the element: the states of Cl_Q(1,1) are a disc (rho = 1 + a e1 + b e1e2,
  a^2 + b^2 <= 1) and the commutator is nonzero for all of them. So (P) does not imply commutation at spacelike
  separation, and does not forbid the slaved field. SILENT.
- PROVED: the signal a distant party could read is the value of the self-adjoint element I [phi, O], with I a unit
  commuting with the matter pair (I = e3 e4 in a larger algebra; no such element in Cl(1,1), whose only
  anti-self-adjoint blade is e2). I e2 is self-adjoint of square 1, so (P) on the larger algebra bounds its value by
  1 in modulus and the bound is attained on the atom (1 + I e2)/2: the first-order signal is at most
  g |c1 - c2| |p q| |sum G| per unit kick, and positivity does not make it vanish.
- ARGUED (a pairing of two stored facts): positivity and no-signalling are independent in both directions. The
  stored functional of value 4 gives no-signalling tables and violates (P); the slaved field of the lattice model
  lives in an algebra whose states all satisfy (P) and it signals. For cluster G, lead 1: (P) belongs in the list of
  stored premises that do NOT imply commutation of the field with matter observables at spacelike separation.
Not filed (it is a remark on cluster G's entity; two lines there would hold it).

## Lead 3. Parity-odd observables: what each setting costs (no choice made)

Routes: (r1) the problem's own, a premise that selects a setting: none found, not attempted further; (r2) from the
new theorem: compare what additivity gives in each setting; (r3) own: where the stored counter-models put their
negative weights. Chosen r2 + r3; nothing computed beyond the checks of proposal 1, so no separate kill condition.
Setting O (every self-adjoint element, odd ones included, is an observable; outcomes are all rational projectors):
- gain, PROVED (proposal 1): on two modes, weights that exist, do not depend on the context and add on orthogonal
  projectors are linear; with non-negativity they are the states of (P). Linearity is not an extra assumption.
- gain, stored: one mode per party suffices for a CHSH value above 2 (with the Klein twist); the Kochen-Specker
  obstruction holds on two modes.
- cost, stored: the parity average of the descent sends the odd elements to zero; the record of a mixed-parity
  observable breaks evenness of states; univalence then restricts states but not these observables.
Setting E (only parity-even elements are observables; outcomes are the even projectors):
- cost, PROVED from the stored clause (iii) of the two-valued-weights result: on two modes the even projectors are
  the projectors of two corners of size two, a non-negative additive weight on them need not be linear (a
  two-valued one exists), so there the residual postulate does not give (P): linearity has to be assumed.
- PROVED (one line, from proposal 1 (i)): for an even LINEAR functional, non-negativity on the even projectors
  already gives (P) (its matrix is block diagonal on span(s0, s3) and span(s1, s2), and each block is positive).
  So in setting E what is missing on two modes is exactly linearity; in setting O it is exactly nothing.
- cost, stored: CHSH above 2 needs two modes per party (four modes, corners of size eight).
- CONJECTURED, not proved: on four modes the even subalgebra is two blocks of size eight and the theorem of
  proposal 1 should hold in each block, so that in the realisation that violates CHSH setting E would get
  linearity from additivity as well. First step: the extension below.
- noticed (r3), COMPUTED in proposal 1's check: the stored functional of value 4 has weight -1/4 on the atom of
  (1,0,0,1) = s0 + s3, which is a parity-EVEN atom (an equal superposition of both modes full and both empty).
  So non-negativity on even projectors alone already excludes that functional; the restriction to even elements
  does not shelter it.
What would decide between the settings is still a premise; the theorem changes the price list, not the choice.

Extension to more modes (OUT OF REACH in this pass; outline, ARGUED). For Q^n, n >= 7 (so sizes 8, 16, ...): if every
4-dimensional rational subspace U similar to the standard one carries the theorem (it does: a similarity maps rays to
rays and frames to frames, and frames of U extend to frames of Q^n by a fixed orthogonal basis of the complement),
then q(x) = f(x)(x.x) is a quadratic form on every such U. A plane lies in such a U iff its discriminant is a sum of
three rational squares (not -1 times a 2-adic square). For a pair (u, v) spanning a bad plane choose w orthogonal
to both with N(w) of a suitable 2-adic class and size; the five planes of (u, w), (v, w), (u, v - 2w),
(u + w, v - w), (u - w, v - w) are then good, and the five parallelogram identities on them add up to the
parallelogram identity for (u, v) (verified by hand: the terms in q(v - w), q(w) cancel). Then q is a quadratic
form on Q^n. What it needs beyond this pass: that positive definite rational forms of dimension >= 4 represent
every positive rational (Hasse-Minkowski, literature from memory), used to find w and to complete good planes to
good 4-spaces; that makes the result conditional on an import. First step for whoever takes it: state and import
that representation fact, then write the five-plane lemma with its 2-adic choice.

## Lead 4. Independence of (P): what a proof needs beyond the stored counter-model; the attempt

Routes: (r1) the problem's own: a model of every other premise with a value assignment violating positivity; (r2)
from the Born account: read the residual postulate (weights exist and add) on projectors and ask whether it gives
(P); (r3) own: a finite formal model per outcome set. Chosen r2, because proposal 1 decides it on two modes.
Kill condition (registered with K1e, same computations): the reduction below is dead if a non-negative additive
weight on all rational projectors of two modes exists that is not a state. None exists (proposal 1 (iii), (iv)).
Result, PROVED on two modes over Q:
  (P)  <=>  every rational projector E (self-adjoint for the split) has a weight mu(E) that (W1) does not depend
            on the context, (W2) adds on orthogonal projectors, (W3) is non-negative, with mu(1) = 1.
The reality clause only fixes the extension to elements that are not self-adjoint. So:
- (P) is NOT independent of the residual postulate if that postulate is read as W1 to W3 for all rational
  projectors: it follows from it. The stored reading (weights on effects, additivity across effects that do not
  commute, argued) can be replaced by this one, which asks additivity only inside a context.
- What an independence proof needs beyond the stored counter-model is therefore exactly one of: a model of the other
  premises in which some rational projector is not the label of a record (W1 to W3 not asked of it); or weights that
  depend on the context; or no additivity inside a context. By proposal 1 any linear or additive assignment that is
  not a state has a negative weight on an ATOM. For the stored family lambda_c (c != -1) the negative weights are on
  the joint outcomes of the commuting pair U, V, which are not local products (stored); for the functional of value
  4 they include the even atom of (1,0,0,1).
- The attempt. With record labels restricted to products of local outcomes, the stored family lambda_c is the
  independence model: it meets the algebra, linearity, normalisation, reality, evenness, the parity averages and
  non-negative weights at all pairs of local directions, and violates (P) (stored, clause (iv); that the stored
  recording premises speak only of local products is argued there, not proved). With record labels all rational
  projectors, no independence model exists on two modes. I could not find a stored premise that says which
  projectors can label a record: one-relation.recorded-sectors-superselected-premise speaks of "the sectors
  labelled by a measurement's records" without fixing them. So independence of (P) from the full premise set is
  NOT PROVED and NOT REFUTED here; it is reduced to that one question, which is a premise decision.
- Derivation side: nothing here derives W3 (non-negativity) from the record-chain account; a weight read as a
  frequency of records is non-negative by meaning, which is an argument, not a theorem of the store.
OUT OF REACH: the independence proof against the whole store. Reason: the store does not yet say which projectors
are record labels. First step: Leon's decision D1 below; under its first branch the item closes by derivation on
two modes, under the second by the stored model once "records are local products" is stated as a premise.

## Unexpected links
- To cluster G (lead 1): (P) is silent on the slaved field's commutator; positivity and no-signalling are
  independent in both directions (above). The signal is the value of I [phi, O], which needs the unit I of the
  field theory; in the matter algebra alone it cannot even be written.
- To cluster W / op.order-four-anomaly-and-sixteen (a resemblance, not tested): the proof of proposal 1 runs
  through the two-adic structure of the rational rotors (argued, not written out: the octahedral group is the quotient of the rotor group
  by its two-adic congruence subgroup, and the parity colouring of clause (v) is its mod-2 shadow); the stored
  mod-8 and mod-16 counts of that problem also come from 2-adic properties of sums of squares.
- To synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three: the same finite
  group of quarter-turn rotors appears; here its group algebra modulo the frame relations is the 3 by 3 matrices.
- To the Born account (one-relation.measure-indifference-borns-rule-located): its sentence that the
  non-contextuality assumption is "relocated into (P), not removed" can be sharpened on two modes: what is assumed
  is non-contextual additive non-negative weights on projectors; linearity across non-commuting elements follows.

## Decisions for Leon
D1 (premise reading; decides lead 4 on two modes). Which projectors can label a record? (a) every projector with
   rational coefficients that is self-adjoint for the split, with weights that are non-negative, do not depend on
   the context and add inside a context: then on two modes (P) is a theorem of that reading of the residual
   postulate and need not be a separate premise there; (b) only products of local outcomes: then (P) stays
   independent, by the stored family lambda_c. Recommendation: state (a) or (b) explicitly as the content of the
   residual postulate; I lean to (a) only if parity-odd elements are admitted as observables, since the theorem
   needs the odd projectors (see lead 3). This is tied to the parity choice and should be decided with it.
D2 (maintainer). Proposal 2 can be folded into clause (v) of the stored Pell theorem instead of standing alone.
D3 (maintainer / literature). Mushtari 2001 (Lobachevskii J. Math. 9, 47) should be read before proposal 1 is
   described as new anywhere; mathnet.ru could not be opened from here. If it contains clause (iii), the result
   stands as a self-contained proof with the citation added; if it contains a counter-example, the proof has an
   error that the referee should find (I found none; every finite step is machine-checked).
D4 (maintainer). After acceptance: the open problem's fifth and sixth attack items can be marked done, the
   sentence "linearity is undecided" in its known-paragraph and in the stored two-valued-weights result updated,
   and (P)'s own text can say what it assumes on two modes (weights, additivity in context, sign).
D5 (import, only if the extension to more modes is wanted): representation of positive rationals by positive
   definite rational forms of dimension at least four.

## Proposals filed (2 of 3)
1. synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear (lead 1; bears on leads 3, 4).
2. synthesis.pell-values-are-the-running-maxima-of-the-pure-state-chsh-values-over-the-rationals (lead 2).

## Fix round (referee report verify/R-E.md)
E2 (Pell running maxima): SOUND, no change.
E1 (additive weights are linear): SOUND WITH FIXES, all six applied in proposals/<id>/ (entity.md, proof-main.tex);
no conclusion reversed, nothing declined, check.py and coverage.yaml unchanged (runcheck: 9 PASS).
1. Clause (iv), Reading, technical, one-liner: "what (P) adds is the sign condition only" replaced. Stated now: the
   weights on rational projectors are the restriction of one linear L; for rational combinations of commuting
   rational projectors the value is L; for other elements, the CHSH element among them (eigenvalues 0 and
   +-2 sqrt 2, spectral projectors not rational), that the value is L(x) remains part of (P); of what (P) asserts
   about projectors only the sign is not implied. This also corrects my own summary of lead 4 above: the
   equivalence "(P) <=> W1 to W3" holds for the weights on projectors, not for the values of all elements.
2. Lay: the non-contextuality assumption is stated in plain words; "the usual rule follows" dropped.
3. Proof: the 34 frames with their coefficients and the resulting identity (18 coefficients on O) are in
   proof-main.tex.
4. Prior art (flagged as read through abstracts and a summary, to be confirmed by Leon from the papers): Mushtari
   2001 poses the question as Problem G, open; clause (iii) answers it for n = 4 in the signed form; his
   Proposition 4 already gives a two-valued weight on the unit atoms of Q^4, so clause (v) is not claimed as new and
   "carried to dimension four here" is dropped; Mushtari 1995 / 1998 (all rational idempotents, a larger domain)
   cited. Technical level says what is and is not claimed as new.
5. Preliminaries: w_j = v_j^dagger is from the definition of the adjoint; the ladder relations in Cl(2,2) are checked
   directly.
6. Ledger stated: transport-absent.
The id's slug still describes the result.
