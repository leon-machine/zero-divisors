# attack-NB (cluster N, angle B: cross-pollinating and adversarial)

Status: COMPLETE (attack round). Kill conditions below were written before any computation; outcomes are under Results.

## Orientation (direct lookups, done)
Read in full: standard-model.why-large (v3, conjectured), refuted.the-number-n-is-a-mystery-of-largeness (v2),
refuted.the-number-n-is-a-coincidence-dirac (v2), standard-model.largeness-number-universes-boundary-modes (v3),
standard-model.trichotomy-what-kind-number (v11, proof and check), synthesis.number-n-registered-free-input (v1),
tower.fock-module-one-qubit-per-rung, rungs.imported-tower-one-qubit-per-rung, tower.witt-index-quantum-capacity,
tower.answers-iteration-question, standard-model.pair-count-dimension, standard-model.imported-pair-systems-two-chirality-halves,
standard-model.gauge-algebra-minimal-massive-composite, synthesis.de-sitter-mode-count, synthesis.promoted-norm-one-global-pair,
synthesis.d-term-level-free-at-fixed-n, synthesis.rung-unit-second-free-number (v3). One-liners of all 63 claims that
mention N, M_P/H, G Lambda or v/H (list in work/NB/N_mentions.txt), and the 61 further entities that mention the Hubble
or Planck scale without N.

What the stored wording is: "the pair construction iterated from the minimal base case of three so that each level's
objects are the fermionic pairs of the level above ... counts 3, 2^3 = 8, 2^8 = 256, 2^256". The base three is the pair
count of a conformal spinor's pair system (Witt index of the complexified six-dimensional ambient space,
standard-model.pair-count-dimension). The store itself already says: the reading is unproved; the proved tower adds one
qubit per rung; the reading places every count above 2^256 "between the third and fourth levels", so the horizon count
does not test it.

## N1/N2 (the reading: precise forms, and whether the counts are canonical)
Routes considered.
- R1 (the problem's own): take the wording literally as a functor. Objects of a level = a basis of the Fock module
  Lambda W of the level's pair system; these become the creators of the next level, so W' = Lambda W, V' = W' + W'^*
  (hyperbolic doubling). Counts dim = 3, 8, 256, 2^256. Delivers the stored counts; needs nothing but dimension; fails
  to use any structure the tower theorems prove.
- R2 (from another subject: spinor forms, std-algebra and the chirality halves of the standard-model subject): the Fock
  module of Cl(k,k) carries invariant bilinear forms (from the two antiautomorphisms) and the Fock inner product (from the
  stored adjoint v_j^* = w_j). If the level's objects are to BE vectors of the next algebra using structure the store
  holds, the quadratic form on them is one of these. Count the pairs (Witt index) each gives at k = 3 and iterate.
- R3 (mine): enumerate the choice points in the wording (pairs as modes or as two-fermion states; all states or one
  chirality half; real or complex Witt index for the base; which level is first; ordered or unordered) and compute the
  sequence for each exactly.
Choice: R2 + R3 (the adversarial job); R1 is the constructive sibling's base statement and I will not file it.

Kill conditions (pre-registered):
- K-N1 (numerology charge fails): if every formalisation that uses only structure stored for the tower (Fock module,
  its parity halves, its invariant forms, the stored adjoint, the two-fermion subspace) gives 8 at the second level, the
  reading is canonical at that level and I report that instead. First computation: the second-level count under each.
- K-N2 (the reading is selected by the proved tower): if the proved tower results contain, or imply by an exact
  computation, an identification of the Fock module of rung k with the ladder generators of rung 2^k that respects the
  Clifford action (the invariant form making the module a split quadratic space of Witt index 2^k), the exponential
  reading follows from the tower and the adversarial thesis is dead. Conversely the thesis "it contradicts the tower" is
  dead if the functor of R1 is consistent with the tower as a subsequence of rungs (expected: consistent, not selected).
- K-N2b (a specific claim I expect and will test): at k = 3 the invariant symmetric form on the 8-dimensional module is
  split of Witt index 4, and 4 = 3 + 1 is the tower's own next rung; 2^(k-1) = k+1 only at k = 3. Dead if the symmetric
  invariant form at k = 3 does not exist or is not neutral.

## N3 (independence of N: does it survive the promoted action, the rung register, every stored relation)
Routes: (a) the rescaling Lambda -> s^2 Lambda at fixed G and fixed xi G (two solutions of one promoted theory);
(b) the same at fixed v/M_P; (c) discrete obstruction from integrality of the horizon count.
Kill conditions (pre-registered):
- K-N3 (independence dies): a stored relation at its pinned version, not an identity in N, that contains N (or H with
  M_P) and whose remaining entries are fixed by the rest of the premise set, so that the pair of models differing only in
  N cannot both satisfy it. Search: all entities in work/NB/N_mentions.txt and the further Hubble/Planck list.
- K-N3a (my sub-claim "v/M_P is not exactly N-independent at fixed level"): dead if the stored D-term vacuum does not give
  v^2 = 2 sqrt(m*^2 + H^4), i.e. (v/M_P)^4 = 4 c^2 (xi G)^2 + 4 N^-4 with c = g'^2/(g^2+g'^2).
- K-N3b (my sub-claim "integrality obstructs continuous independence"): dead if no stored statement asserts the horizon
  mode count |J| = pi N^2/ln 2 is an exact integer (if the count is stated at leading order only, the obstruction is
  not a stored relation and is reported as a remark only).
- K-N3c: under the promotion, the two models must be two solutions of one theory; dead (as a survival statement) if the
  stored promoted functional has a parameter or boundary condition that ties Lambda to another fixed number.

## Results

### N1/N2. The reading is rule-dependent from the second level on (PROVED for the forms; ARGUED for "equal claim")
Proposal filed: synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level
(check4: 0 errors, 0 warnings, check pass; validate_draft ok; registered with propose_claim; coverage.yaml added).
Scripts: work/NB/readings.py (exploration), work/NB/<id>/ (proposal source), check runs in under 2 s.
- K-N1 did NOT hold (so the numerology charge stands at the level of the numbers): the Fock module F_k = B_k p_k of
  k rungs carries exactly two bilinear forms for which every vector is self-adjoint (eps = +1, reverse) or
  anti-self-adjoint (eps = -1, reverse with grade involution), unique up to a factor, read off
  tau(psi) phi = beta(psi, phi) v_1...v_k. PROVED for all k (three-line proofs from the antiautomorphism and the
  irreducibility in tower.fock-module-one-qubit-per-rung); COMPUTED in GA.py for k <= 3 (uniqueness by exact nullity
  one) and k <= 4 (symmetry, signature).
- Symmetry sign eps^k (-1)^(k(k-1)/2): a symmetric invariant form exists unless k = 2 mod 4; when symmetric it is
  neutral, Witt index 2^(k-1). So with any quadratic form at all, 2^k objects are the vectors of at most 2^(k-1)
  fermionic pairs (tower.witt-index-quantum-capacity). "8 objects, 8 pairs" needs 8 further annihilators adjoined.
- At k = 3: reverse form antisymmetric (4 canonical pairs of the bosonic kind), the other symmetric of signature (4,4)
  with the two 4-dimensional parity halves totally null and dual: FOUR fermionic pairs. K-N2b held: 4 = 3 + 1 is the
  proved tower's own next rung, and 2^(k-1) = k + 1 only at k = 3.
- At k = 2 (the REAL Witt index of Cl(2,4)): both forms antisymmetric, no invariant quadratic form; the form rule does
  not start. Real against complex counting therefore matters: the base "three" is a complex pair count.
- Two rules, both using the stored words: (A) states become creators, annihilators adjoined, k -> 2^k:
  3, 8, 256, 2^256; (B) states become the generating vectors under the invariant form, k -> 2^(k-1):
  3, 4, 8, 128, 2^127 (state counts 8, 16, 256, 2^128; every later term is 0 mod 4 so the form exists).
  8 and 256 occur in both with different meanings; the "third level" number is 1.2e77 in A and 3.4e38 in B.
- K-N2 (selection by the proved tower) did not fire in either direction: both rules are consistent with the tower as
  subsequences of rungs; no stored tower result relates the module of one rung to the vectors of a later one
  (ARGUED: search of tower.*, rungs.*, not a full-cone audit). The only proved growth, one pair per rung, agrees with
  B at three and with A nowhere.
- Other choice points (exact arithmetic, not filed; NA's findings cover the literal-pairs one): two-fermion states
  Lambda^2: C(n,2) = n only at n = 3, so the literal reading "pairs of the objects" is STATIONARY at three
  (3, 3, 3, ...); chiral objects (the conformal spinor is one 4-dimensional half, standard-model.imported-pair-systems-two-chirality-halves)
  with rule A: 3, 4, 8, 128 again; base two with rule A: 2, 4, 16, 65536, 2^65536; base four: 4, 16, 65536.
- What survives of the reading (candid): the qualitative claim "fast growth is generic" holds under A and B alike
  (both are towers of exponentials), fails under the literal-pairs reading and on the proved tower (linear). The
  specific counts 8, 256, 1e77 are not canonical. No rule and base in this family gives 405 to 408 as a level's
  base-two logarithm or the horizon count as a level, so there is no numerological fit to be suspicious of either:
  the reading has no contact with the value of N.

### N3. Independence of N survives the adversarial tests (ARGUED overall; exact pieces COMPUTED in work/NB/n3_tests.py)
Not filed by me: NA files the base statement (two models at fixed G, xi G and couplings). Tests:
- K-N3 (a stored non-identity relation tying N to fixed numbers): NOT FOUND. Searched 63 claims and 15 notes that
  mention N, M_P/H, G Lambda, v/H (work/NB/N_mentions.txt) and 61 further entities mentioning the Hubble or Planck
  scale. Every N-containing statement is an identity in N (smallness monomials, pi N^2, 4 pi kappa_c N^2,
  2 pi N^2/(c ln 2), Q = eps N, 16 pi/N^2, chi pi N^2/2), a classification of N, a record value, or a statement the
  store itself marks hypothetical or refuted (pion N^(2/3), the frame-boost Majorana relation). ARGUED: one-liners read
  for all, formal levels for the dozen that matter; not a full joint-cone audit.
- K-N3a HELD (my sub-claim is right, and already stored in weaker words): at fixed level the stored vacuum gives
  exactly (v/M_P)^4 = 4 c^2 (xi G)^2 + 4 N^-4 and (v/H)^4 = 4 c^2 (xi G)^2 N^4 + 4, c = g'^2/(g^2 + g'^2). So an
  independence statement must hold xi G fixed, not v/M_P: "m/M_P invariant under the rescaling" (granted as a
  hypothesis in families.why-kinematic-attacks-had-fail and used in standard-model.one-number-explain and
  refuted.the-number-n-is-a-coincidence-dirac) is exact only as a hypothesis and holds to relative order (H/v)^4 on
  the stored D-term branch. Exact rational pair with rational H: (G, H, m*, N*) = (1/100, 2, 3, 5) and
  (1/250, 2, 15/2, 17/2): equal xi G, N^2 = 25 and 125/2, (v/M_P)^4 = 1/100 and 289/62500.
- A dilation acting on every scale (G -> G/s^2, H -> sH, m* -> s^2 m*) fixes N, xi G and v/M_P (computed). The move
  that changes N is a change of the datum Lambda at fixed G, not a symmetry: covariance under the homothety (NA's
  route (b)) proves N-independence only of structures that contain no G.
- K-N3b did NOT hold as a stored relation: the horizon count is a density times an area (scrambling.integer-holographic-form-identification,
  synthesis.de-sitter-mode-count), nowhere asserted to be an integer. REMARK only: if the units statement of the
  trichotomy ("qubits, one per rung", pi N^2/ln 2 of them) were read literally, rungs being counted by integers
  (tower.fock-module-one-qubit-per-rung), N^2 would lie in (ln 2/pi) Z, N would not "take every positive value"
  (synthesis.promoted-norm-one-global-pair (iv)), and only the discrete family s^2 = n'/n of rescalings would remain.
  The spacing is about 1e-62 in N. A decision for Leon, not a contradiction in the store as worded.
- K-N3c did not fire: under the promotion G and xi are constants of the action, the two models are two solutions of
  one theory (stored: synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion). One point not
  stored: the lift locus Q(c) = -H^2 contains the promoted field, so the rung sector contributes to the lambda
  equation; that equation fixes dT (the advance of tau), not lambda, so d lambda = 0 stands (ARGUED, two lines, not
  checked against synthesis.promoted-norm-weyl-clock-flat-weight's formula for the advance, which was derived without
  the rung sector).
- The exponential reading against Premise (N): if a level count were ever asserted to BE the horizon count, N would be
  derived and the premise's refutation condition met. The stored wording avoids this ("between levels"), and my
  clause (v) shows it avoids it under either rule.

### N4 (findings)
- Where 4.8e122 (between 2^407 and 2^408) falls: A: between 2^256 and 2^(2^256); B: between 2^127 and 2^(2^127 - 1)
  as pair counts (between 2^128 and 2^(2^127) as state counts); base two with A: between 65536 and 2^65536;
  literal pairs: never reached; proved tower: rung 407 (states) or rung 4.8e122 (pairs), not distinguished. Nothing in
  the store selects it; under every unbounded rule it lies "between two levels", which is no information (the store
  already says so for A).
- What to restate if Leon agrees (maintainer edits, not filed): standard-model.why-large (i): say the counts are those
  of the rule that adjoins new annihilators, that the rule using the module's invariant form gives 3, 4, 8, 128, that
  the base three is a complex count, and that at three the invariant-form rule is the tower's own rung;
  refuted.the-number-n-is-a-mystery-of-largeness: add that the level numbers are rule-dependent, the qualitative
  point (fast growth under either rule, linear on the proved tower) unchanged;
  refuted.the-number-n-is-a-coincidence-dirac: nothing from the reading; its "m/M_P invariant" could carry "to relative
  order (H/v)^4 on the D-term branch" as the rung-unit premise already does.

## Where NA is exposed (tested against attack-NA.md as of midway)
- Route (b), the homothety: see above; it cannot carry the independence of G-containing relations.
- K-N2-5 ("levels carry no inherited fermionic structure"): true for the second-quantised lift they tested; the module
  does inherit a quadratic structure (my proposal), which gives four pairs, so "nothing more than rungs a_n" should be
  worded as a statement about that lift, not about every canonical structure.
- E-pairs: C(3,2) = 3 is not just "differs from 8", it is a fixed point, and only at three.
- The base: NA states the reading on Cl(3,3) (Witt index 3). The stored base is the complex pair count of the
  (2,4) ambient space; over the reals that space has Witt index 2. Their base statement should say which.
- Independence: must fix xi G (they do), will find v/M_P moving at order N^-4, and should label the "every stored
  relation" clause by the audit actually done. Models with rational H exist (pair above), so
  synthesis.frozen-point-datum-is-h is no obstacle.
- Not exposed: E-asc killed (4, not 8) agrees with my K-N2b from an independent route.
Intended citation: NA's base statement of the reading (E-fock arithmetic and the ascent) and NA's base independence
statement for N. I filed neither. My proposal quotes only the counts of rule A.

## Unexpected links
1. Three is special three times over, exactly: 2^(k-1) = k + 1 only at k = 3 (invariant-form rule = one rung);
   C(n,2) = n only at n = 3 (two-fermion states of three objects are three objects, the antisymmetric pair of two
   colours being an anti-colour); and k = 3 is the first k with a symmetric form on a module whose parity halves are
   dual. ARGUED lead, not checked: (F_3, beta_-) is, as a module of the three-rung spin group, the even half of the
   next rung's module F_4 = F_3 (x) Lambda(R v_4), so "the eight objects of level one" are a half-spinor of rung four,
   which triality of the eight-dimensional split form (literature, from memory) puts on the footing of rung four's
   vectors. This would make the invariant-form rule at three literally the stored ascent.
2. Cluster B, the split behind (P): by the uniqueness clause, every form on the Fock module that treats all vectors
   alike is neutral or alternating, never positive. A positive form needs the generators split into self-adjoint and
   anti-self-adjoint ones (the stored adjoint v_j^* = w_j), which is the split (P) is stated relative to, and the
   rung-frame boost v -> mu v, w -> w/mu changes it. So positivity cannot come from the spin-invariant structure of
   the module: an exact input to B4 (which premise supplies the split).
3. k = 2 mod 4 (two real null pairs, the real conformal algebra's own count) has only alternating forms: the four
   states are two canonical pairs of the bosonic kind. Lead for the correspondence subject
   (note.correspondence.setting-statistics-refutes-naive-identification; not read in full, untested).
4. Cluster W / bridge: the base-two logarithm 407 quoted in the trichotomy and in my clause (v) is for the residue
   1/(4 ln 2); with 3/(4 pi) units per Planck area the count is 3 N^2, between 2^406 and 2^407 on the record bracket
   (computed). No verdict about the readings changes.
5. The exact relation (v/H)^4 = 4 c^2 (xi G)^2 N^4 + 4 has a floor v >= sqrt(2) H at zero level (the balanced frame):
   the three registered numbers N, xi G, v/H satisfy one exact relation on the stored D-term branch, of which
   G v^2 N^2 = (v/H)^2 is the identity part.

## Decisions for Leon
1. Restate standard-model.why-large and refuted.the-number-n-is-a-mystery-of-largeness as in N4 (maintainer edits)?
   Recommendation: yes; the numbers 8, 256, 1e77 are one rule's, and the base three is a complex count.
2. Is the horizon's count of qubits an integer (then N is discretely quantised and "every positive value" needs a
   qualifier in synthesis.promoted-norm-one-global-pair and Premise (N)), or a leading-order density times area (as
   stored)? Recommendation: keep as stored and add one sentence saying the units statement is not an integrality
   claim.
3. Cluster N has no open problem in store/open_problems.yaml (op.t12-n-after-the-count is settled), so my proposal
   carries no extraction.open_problem. Create one ("the exponential reading and the status of N") or leave it.
4. The classical forms theorem is cited from memory (Chevalley 1954, Harvey 1990): import as a Fact or leave as prior
   art in the note.
5. Whether the triality lead (link 1) is worth a follow-up: it is the one route by which the reading could become a
   statement about the proved ascent rather than a parallel construction.
