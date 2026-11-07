# Blind referee report, run 2026-11-07-ga-units

Referee: blind (did not read work/, survey/, filed.md or any findings file). Read: colony/BRIEF.md (referee
role), store/conventions.md (geometric algebra, imaginary units, Leon's 7 November rule), RULINGS.md (Leon's
rulings), the four proposal folders, and every cited premise at its pinned version through tp.mcp_server.Lab.
check4 and validate_draft were not run (already run by the orchestrator). Scratch scripts:
/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/ref/ (perturb.py, own1.py to
own4.py, mut_*.py).

All four checks pass unmodified under colony/runcheck.py. Past cones of every cited premise were inspected:
none contains synthesis.n-plus-null-ground-state, synthesis.attachment-conformal-energy-is-generated-by-z,
dark-matter.premise-flag-as-datum, standard-model.slot-module-hypothesis or standard-model.hyp-s-slot-statistics,
so there is no circularity. No bare imaginary unit, no em dash, no banned words in any of the four.

| # | proposal | verdict |
|---|---|---|
| 1 | synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality | SOUND WITH FIXES |
| 2 | synthesis.z-adapted-witt-flags-energy-sign-and-family-are-independent | OVERSTATED |
| 3 | synthesis.fock-slot-module-is-cpt-closed-only-over-one-doublet | SOUND WITH FIXES |
| 4 | synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space | SOUND WITH FIXES (minor) |

---

## 1. synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality

**Proof steps.** All checked by hand. Step 1: k = w g0 (1 + B_k), B_k^2 = 1, so S_k is the -1 eigenspace of
L_{B_k}; dim 4 by the exchange L_u; D_k = I4 B_k acts as -I4 on S_k; for k = g0 + g1, D = g2 g3 and
exp(theta/2 g2g3) turns g2 to g3 (right-handed about g1 for I3 = g1g2g3 = g0 I4); helicity s/2 relative to I4
follows with the premise's conventions (e^{-I4 theta J}, positive frequency e^{-I4 k.x}). Step 2 is algebra.
Step 3 (commutant of the left rotor action is the right action) is correct and elementary. Step 4: the
classification of a with (Lambda k) a S_k = 0 is correct (the two classes of generators argument is right,
including the case c not containing g0); s' = s(-1)^{|a|} sgn(g0.Lambda k) gives flips exactly for P, PT;
chirality rule and the C, CP examples are right (c(-g1) = -1).

**Premise at pinned version.** field-theory.fock-space-maxwell-modes@4 (current 4) clause (iii) says what is
used. But its formal text does not define chi_e; the projectors chi_e = (1 - e Gamma)/2 live only in its
check.py (_chi). Logically the result uses no premise (the technical level says so), yet the derivation lists
one: inconsistent wording, see fixes.

**Checks run and broken.** Passes. Perturbations (all made the run fail as they should):
- T's expected flip set to -1: (iv) s' fails.
- rotor sign c + s D_k replaced by c - s D_k: (i) helicity fails.
- P's allowed a-set {g0, g0 I4} replaced by {g0, I4}: (iv) classification fails.
- I sigma3 replaced by I sigma1 (= I4 g1 g0): only the C and CP checks fail. The check "(ii) the store's chi_e
  projects onto Gamma = -e" still passes, because it rebuilds chi_e from the local Gamma rather than from the
  premise's IS3 = -g1g2; it is tautological and does not tie the label to the store.
- sigma1 replaced by sigma3: C and CP checks fail.

**Own recomputation** (own1.py, exact, GA.py): for the off-sample direction n = (3g1 + 4g2)/5, dim S_k = 4; the
rotor exp(theta/2 u g3) (u = (-4g1 + 3g2)/5), which turns u to g3 (n, u, g3 positively oriented for I3), acts
on all four kernel vectors as cos - sin I4 (helicity +1/2 relative to I4); a Gamma = +1 vector of S_k maps
under C (psi sigma1) to a Gamma = -1 vector of S_k and under CP (g0 psi g0 sigma1) to a Gamma = +1 vector of
S_{Pk}. Agrees with (i), (iv).

**Duplication.** Clauses (i) and (ii) are already in the store:
- synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays@4 (iii)-(iv): on the canonical part (ker m,
  any null direction by a rotor) L_J = -Gamma i_H and L_J = L_I, i.e. the transverse rotation acts as the
  I4 phase for both chiralities. With m = g0 - g3, B_m = g3g0 and D_m = -J this is exactly L_{D_k} = -L_{I4} on
  S_k and L_{I4} = -Gamma R_{I sigma3}, already for every direction.
- field-theory.where-each-lives@3 (4): "on the chiral subspaces of the Weyl field I4 agrees with Hestenes' right
  I sigma3 up to the chirality sign" is clause (ii).
So "(i) a general proof of the sampled clause (iii) of fock-space-maxwell-modes" is not new. New: (iii) (the
commutant; elementary), (iv) (the classification of the discrete family and the frequency-sign rule), (v).

**Sign conventions.** B_k = g0 n agrees with the wedge entity (B = g0g1 for n+ = g0 + g1) but is minus the
"boost bivector of the generator" of the light-ray entity (B = g3g0 for k = g0 + g3, B k = +k there, B_k k = -k
here). Not an error; both fix S_k the same way, but the proposal should say which.

**Hidden hypotheses and overclaiming.**
- (v) identifies "the chirality of the doublets" with Gamma = L_{I4} R_{I sigma3} on Cl+(1,3). The series'
  doublets are the chiral halves L_0, L_inf of conformal spinors, distinguished by I6 = +I4 or -I4
  (where-each-lives (3)); the dictionary to Gamma is not proved here. The proved content is about Gamma.
- In P1's family "T" is the I4-antilinear time reversal (a odd), which keeps s; (N+) itself calls the filled sea
  "the time reverse of the null vacuum", which is the I4-linear reversal, PT here (x -> -x, flips s). Consistent,
  but unexplained it reads as a contradiction with (N+).
- In standard terms s = -Gamma times the Hestenes frequency sign (from (ii)); saying so would make the
  "independent bits" statement transparent and is a one-line consequence.
- Transport-absent: correct. Literature: Hestenes' C named from memory, flagged. Good.

**Verdict: SOUND WITH FIXES.**
1. Cite synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (iii)-(iv) and
   field-theory.where-each-lives (4) for (i)-(ii), and drop "a general proof of the sampled clause (iii)" (formal
   (i) note, technical, Step 1 last sentence, extraction note); present (i)-(ii) as restated for use.
2. In (v), formal and technical: replace "the chirality of the doublets" by "the chirality Gamma of massless
   even spinors (the label e = -Gamma of field-theory.fock-space-maxwell-modes)", and add one sentence: "its
   identification with the handedness of the series' doublets, the sign of I6 relative to I4 on L_0, L_inf
   (field-theory.where-each-lives (3)), is assumed, not shown". Same change in the one-liner ("not the
   chirality Gamma").
3. Add to Step 4 or (v): "the reversal under which (N+) calls the filled sea the time reverse is the I4-linear
   one, PT in this family; the antilinear T keeps s".
4. Technical: replace "so the result rests on no premise" by "the result uses
   field-theory.fock-space-maxwell-modes only for the chirality label"; and "the projectors chi_e of
   field-theory.fock-space-maxwell-modes" by "the projectors chi_e of that result's check".
5. Check: anchor the chi_e test to the premise by using its literal IS3 = {(1, 2): -1} (or importing its
   _chi), so that perturbing ISIG3 breaks (ii).
6. State that B_k = g0 n is minus the boost bivector B of the light-ray entity.

---

## 2. synthesis.z-adapted-witt-flags-energy-sign-and-family-are-independent

**Proof steps.** Steps 1 to 3 are correct. I6 = e0e1e2e3 nu e- = -(e0 nu)(e1e2)(e3e-) (three swaps); from
w_a psi = 0, Z psi = -s0 psi I6, e1e2 psi = s1 psi I6, e3e- psi = s2 psi I6, hence I6 psi = -s0 s1 s2 psi I6;
the parity argument (w_a odd, R_{I6} even and invertible) is right. Store normalisation checked: in the stored
checks e_+ is the generator of square +1, so nu = e_+, E = nu e- = e_+ e_-, I6 = I4 E as in the conventions.
Step 4 is a count. Step 5 is the reading.

**Premises at pinned version.** positive-conformal-energy@6 (current 6) supplies the frame, Z and (ii); two-
families@6 (current 6) supplies the definition of family. Both say what is used.

**Checks run and broken.** Passes. Perturbations:
- I6 = I4 E replaced by I4 e- nu (= -I6): every (3) family check fails, (2) Z psi = -s0 psi I6 still PASSES.
  So under the opposite orientation of I6 with the same labels s, (ii) keeps its form and (iii) becomes
  +s0 s1 s2. The parenthesis in (iii) "With the opposite orientation of I6 every label s becomes -s; the
  statements keep their form" is wrong as written (under a relabelling s -> -s both formulas change sign; with
  fixed labels only (iii) does).
- w_a sign flipped (x - s y I6 -> x + s y I6): (1), (2), (3) fail.
- planes (e1,e2),(e3,e-) replaced by (e1,e3),(e2,e-): (3) fails.
- expected eps -s0s1s2 replaced by +s0s1s2: (3) fails.

**Own recomputation** (own2.py, exact): pure spinors built by a different route, the product of the commuting
projectors (1 + lambda_a L_{B_a} R_{I6}^{-1})/2, B_a = x_a y_a, applied to all 64 blades: rank 8 for each s;
they satisfy w_a psi = 0; Z sign = -s0; I6 psi = eps psi I6 with eps = -s0 s1 s2; and eps equals the
orientation of J_s relative to I6, e0 ^ J e0 ^ e1 ^ J e1 ^ e3 ^ J e3 = -s0 s1 s2 I6. So (iii) is the standard
pure-spinor fact "chirality of the pure spinor = orientation of the complex structure relative to the
pseudoscalar" (Cartan, Chevalley; cited from memory by me), which is convention-free in that form.

**The main problem: (iv)-(v) misread the stored bit.** dark-matter.premise-flag-as-datum@2 defines the stored
orientation bit as the sign of J relative to the Fock unit: the two values of the bit are J and -J, i.e. W_s
and W_{-s}. On every such conjugate pair both s0 and the family flip (W_{(1,1,1)}: s0 = 1, family -1;
W_{(-1,-1,-1)}: s0 = -1, family +1; the proposal's own check confirms both flips), and s1 s2 is invariant under
s -> -s. So relative to the stored bit, the energy sign is not independent: s0 = -s1s2 . family, with s1s2 fixed
once the descent's J is fixed up to sign. Independence holds only as functions on the set of eight flags, i.e.
across different (non-conjugate) complex structures, which is not what the datum ranges over. Clause (v)
("a second orientation bit of the flag, not the stored family bit") is therefore the opposite of what the
computation shows for the datum, and it runs against one-relation.arrow-frequency-are-one-bit-level and the
imported one-relation.imported-flag-arrow-superselection ("spent once, read twice"), which the proposal does not
mention. The lay level ("knowing one bit does not tell you the other") inherits the error.

**Further points.**
- (ii) "the vacuum lies in T_+ exactly when s0 = 1" silently identifies the scalar i of
  synthesis.attachment-conformal-energy-is-generated-by-z (a Jordan-Wigner C^8 scalar, declared outside_ga)
  with +R_{I6}. The commutant fixes the unit only up to sign (field-theory.orientation-relocated (3)); with
  -R_{I6} T_+ and T_- exchange. This is a convention and must be stated as one.
- (i) "in a minimal left ideal stable under R_{I6}": minimal left ideals of Cl(2,4) are not R_{I6}-stable in
  general; the intended space is CS = Cl+(2,4)P (or its odd counterpart), where the pure spinor is unique up
  to span{1, I6}.
- Duplication: (iii)'s conjugate-flag clause and the orientation reading duplicate
  synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation@3 (2)-(3) (conjugate flag in the other
  family; an isometry exchanging W and its conjugate has det -1) and dark-matter.two-families-are-two-chiralities
  (iii).
- "Transport-essential as the ledger derives it": the algebra is transport-absent; the ledger label is
  inherited from positive-conformal-energy (ledger essential), used only for the frame and Z. Say
  "transport-absent algebra; ledger inherited".

**Verdict: OVERSTATED.** True weaker statement: "For the eight orthogonal complex structures J_s preserving the
planes (e0, nu), (e1, e2), (e3, e-), written with the unit R_{I6}: Z psi = -s0 psi I6 on the pure spinors, and
I6 psi = omega(J_s) psi I6 with omega(J_s) = -s0 s1 s2 the orientation of J_s relative to I6 (the family). As
functions on the eight flags s0 and the family are independent. On each conjugate pair {W_s, W_{-s}}, the two
values of the orientation bit of dark-matter.premise-flag-as-datum, both flip, s0 . family = -s1 s2 fixed; so,
read as the energy sign of the flag's vacuum (with the attachment's unit identified as +R_{I6}), the (N+) datum
is the stored flag bit up to the sign s1 s2 of the descent's complex structure on the four-space orthogonal to
Z, consistent with one-relation.arrow-frequency-are-one-bit-level. Whether the descent's flag is Z-adapted is
open." Exact fixes if refiled:
1. Title: "Energy sign and family of the Z-adapted Witt flags" (drop "are independent bits").
2. (iii): state the family as omega(J_s), the orientation of J_s relative to I6, and delete the parenthesis
   "(With the opposite orientation of I6 every label s becomes -s; the statements keep their form.)"; replace by
   "with the opposite orientation of I6 the family reads +s0 s1 s2 for the same s, and (ii) is unchanged".
3. (iv): keep the count, delete "its family bit, the stored orientation bit of Premise ..., are independent",
   add the conjugate-pair statement above.
4. (v), technical, lay, one-liner: replace the "second orientation bit" reading by the conjugate-pair reading
   and cite one-relation.arrow-frequency-are-one-bit-level and one-relation.imported-flag-arrow-superselection.
5. (ii): add "with the attachment's unit identified as +R_{I6} (a convention; with -R_{I6}, T_+ and T_-
   exchange)".
6. (i): "in CS = Cl+(2,4)P (respectively its odd counterpart)" for "in a minimal left ideal stable under R_{I6}".
7. Cite synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation (2)-(3) for the conjugate-flag
   clause; ledger wording as above.
8. Check: add the conjugate-pair assertion (s0 and family both flip under s -> -s, s1 s2 invariant).

---

## 3. synthesis.fock-slot-module-is-cpt-closed-only-over-one-doublet

**Proof steps.** Step 1 right (polynomial representation, mu acting as mu^n, so F_1 is a multiple of D). Step 2:
the swap identity Lambda^2(V (x) W) = S^2V (x) L^2W + L^2V (x) S^2W is right. Step 3: with F_0 one-dimensional,
clause (1) of the theorem needs F_2 = exactly one F_(1,1) and F_{>=3} = 0; for b >= 2 it fails twice over (C(b,2)
weak triplets and C(b+1,2) >= 3 copies of F_(1,1)), for b = 0 F_2 = 0, for b = 1 it holds. Step 4: right, but
the symmetric module is infinite-dimensional, so it is outside the class to which the theorem's (1) applies;
the proof says "outside the finite-dimensional class of clause (a)" and handles finite truncations. Acceptable;
a direct argument is available and better: Y = (3n - 2k)/6 is bounded below (k <= 3) and unbounded above, while
complex conjugation negates Y, so V is not isomorphic to its conjugate.

**Premise at pinned version.** synthesis.cpt-closure-forces-slot-module-and-chirality@1 (current 1), clause (1),
says what is used. The slot-module hypothesis is cited for (a), (b) only as setting; the theorem's own
statement carries the same setting, so not listing it in `uses` is fine.

**Checks run and broken.** Passes. Perturbations:
- second term of the character identity L^2V x S^2W changed to L^2V x L^2W: (1) fails.
- the symmetric triplet count b(b+1)/2 changed to b(b-1)/2: (2) fails.
- T3 on the down modes given sign +1/2: (3) Casimir counts fail.
- Allowing F_(2,0) in the closure criterion, or relaxing "(1,1) count == a" to ">= a": each alone still
  passes, because the other condition and F_3 != 0 also exclude b >= 2. Not a defect, but it shows that the
  weak-spin-one exclusion highlighted in the text is one of three redundant reasons.

**Own recomputation** (own3.py, plain matrices on the two-slot space, no GA): weak Casimir multiplicities on
Lambda^2(D (x) M): b = 1: 1 singlet; b = 2: 3 triplet states, 3 singlets; b = 3: 9 triplet states, 6
singlets. Symmetric: b = 1: 3 triplet states; b = 2: 9 and 1; b = 3: 18 and 3. Matches C(b,2) triplets,
C(b+1,2) singlets (exterior) and C(b+1,2) triplets, C(b,2) singlets (symmetric).

**Duplication.** (iv) at b = 1 is clause (3) of the stored theorem; the new content is the b >= 2, b = 0 and
symmetric cases, a short corollary of the theorem's (1) and the swap identity.

**Overclaiming.** The Fock clause contains the unique vacuum: F_0 = Lambda^0 F_1 is one-dimensional by
definition, and Step 3 uses exactly this to set a = 1. So the unique vacuum is assumed, not derived. (iv)
itself is careful ("the statistics and the number of doublets are derived"), but the technical level says
"CPT closure alone fixes the statistics (fermionic), the number of doublets (one) and the unique vacuum", the
extraction note says the result "reduces clause (G) (unique vacuum, one doublet ...)", and the lay level
presents the Fock clause as doing the job of "start from one empty state". Transport-absent: correct.

**Verdict: SOUND WITH FIXES.**
1. Technical: "fixes the statistics (fermionic), the number of doublets (one) and the unique vacuum" ->
   "fixes the statistics (fermionic) and the number of doublets (one); the unique vacuum is part of the Fock
   clause".
2. (iv): add "(the unique vacuum is part of the Fock clause)" after "the slot vacuum is unique"; extraction note
   likewise: "replaces the one-doublet part of (G); the unique vacuum is kept, inside the Fock clause".
3. Lay: "a more natural assumption does the same job" -> "a more natural assumption, which keeps the single
   empty state, does the rest of the job".
4. (iii)/Step 4: add the hypercharge argument (Y bounded below, unbounded above, conjugation negates Y), so the
   symmetric case is excluded by CPT closure itself and not only by the finite-dimensionality of clause (a).
5. Say once that (iv) for b = 1 is clause (3) of the theorem.

---

## 4. synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space

**Proof steps.** Step 1: 1 - 2 v_p w_p = e_p f_p (verified: v w = (1 - ef)/2), Gamma_W = e2f2e3f3e4f4, a
single blade with square 1, acting as +1 on the vacuum and -1 per occupied pair; with the ordering pair
creators left of slot creators, pair vectors act as 1 (x) b and slot vectors as a (x) (-1)^k. Step 2 right
(also {a_i K, a_j K} = c^2 {a_i, a_j} = 0). Step 3 right: 6 + 15 = 21 = dim so(4) + so(6). Step 4: the
derivation K beta + beta K = 0 from a_i(K beta + beta K) = 0 = a_i^dagger(...) via a^dagger a + a a^dagger = 1
is right; irreducibility gives K(-1)^k scalar; |c| = 1; c = +-1 for an involution. The blade count (both
cases) is right: case S contains P with |S| even forces S = P; case S disjoint from P with |S| odd would need
all four slot generators, |S| = 4. The conditions are diagonal in the blade basis, so the count covers all K in
the real floor.

**Premises at pinned version.** even-slots-need-a-spectator-generator@3 (current 3) supplies the floor and the
replacement s_i -> s_i Gamma_W of its (iii); blade-square-signs-f2-quadratic-form@2 (current 2) (ii) is the
commutation form used. Both say what is used.

**Checks run and broken.** Passes. Perturbations:
- Gamma_W over two pairs instead of three: (1) and (2) fail.
- commutation form |S||T| + |S cap T| replaced by |S||T| + |S cup T|: (3) fails.
- a slot generator (5) put in the pair set P: (3) fails.
- Fock states reordered with slot creators to the left of pair creators: the check STILL PASSES. The test
  "the two conventions differ by (-1)^k on the Fock basis" holds for either ordering (Gamma_W acts on
  v_K v_J f, or v_J v_K f, as (-1)^k either way), so the check never tests Step 1's identification of the
  untwisted v_i Gamma_W with a (x) 1 in the tensor-product model, which depends on the ordering. The
  mathematics is right; the check is weak there.

**Own recomputation** (own4.py; no Clifford algebra: V = Lambda(C^2) (x) Lambda(C^3) as 32 x 32 integer
Kronecker matrices with Jordan-Wigner signs inside each factor): the linear space of K commuting with a_i,
a_i^dagger and anticommuting with b_p, b_p^dagger has dimension 1 (rank of the 1024-unknown system computed
modulo the prime 2^61 - 1, a rank, not the evidence), and (-1)^k = 1 (x) parity solves it exactly, with the
twisted a_i (-1)^k satisfying the CAR exactly. Agrees with (iv).

**Duplication.** The twist itself is the replacement s_i -> s_i Gamma_W already made in
even-slots-need-a-spectator-generator (iii) (acknowledged), and the device is the commuting-copies twist
x -> x omega of tower.commuting-copies@5 read backwards. New: (iii) convention-free operators, (iv)
uniqueness, (v) the reading. The Klein transformation (Klein 1938, Araki 1961) is flagged as cited from memory
in the note; fine.

**Overclaiming / hidden hypotheses.** None substantive. (v) says every operator the clause produces "is an
operator on V built from them"; the 24 cross bivectors are convention-dependent (only the twisted operators
give Spin(10)), and the residual c = -1 acts on them by Ad of the slot volume element e0f0e1f1, an element of
Spin(10), so Spin(10) is canonical as a subgroup. Worth one sentence. The scope limit (slot operators given in
advance as tower elements) is stated and flagged.

**Verdict: SOUND WITH FIXES (minor).**
1. Check: add a test of Step 1's identification: in the basis v_K v_J f, the matrix of v_i Gamma_W (and
   w_i Gamma_W) is independent of K, i.e. equals a (x) 1, while that of v_i carries (-1)^k; this test fails
   under the reordering perturbation, as it should.
2. (v) or Step 5: add "the 24 cross bivectors depend on the convention; the sign c = -1 acts on them by Ad of
   the slot volume element, an element of Spin(10), so the Spin(10) of clause (f) is canonical".
3. Cite tower.commuting-copies for the twisting device beside even-slots-need-a-spectator-generator (iii).

---

## Across the four

- 1 and 2 both read the (N+) orientation datum against a chirality-type bit. They do not contradict each other
  (1 compares with the per-mode chirality Gamma, 2 with the Witt-flag family), but 2's clause (v) contradicts
  the store's one-relation.arrow-frequency-are-one-bit-level reading and its own conjugate-pair computation;
  1's conclusion is compatible with the store.
- 3 and 4 compose: 3 gives F = Lambda(D) from the Fock clause and CPT closure, and 4 then makes clause (f)
  automatic on V. No conflict.
- Duplicates of stored results: 1 (i)-(ii) (light-ray-good-part (iii)-(iv); where-each-lives (4)); 2 (iii)
  conjugate-flag clause (cpt-conjugation (2)-(3); two-families (iii)); 3 (iv) at b = 1 (cpt-closure theorem (3));
  4's twist (even-slots (iii)).

## Decisions for Leon

- Proposal 2 should not be accepted in its present reading; its algebra (i)-(iii) is right and could be refiled
  under the weaker statement above.
- The store carries two opposite normalisations of "the boost bivector of a null generator" (wedge entity and
  proposal 1: B_k = g0 n, B_k k = -k; light-ray entity: B = n g0, B k = +k). Not an error, but a notation note
  would prevent sign slips.
