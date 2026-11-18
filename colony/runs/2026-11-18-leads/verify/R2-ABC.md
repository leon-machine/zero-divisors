# Second-pass referee report, group ABC (run 2026-11-18-leads)

Read: REFEREE.md (common part, "Second pass" and "Second pass, group ABC"), colony/BRIEF.md (Standards, referee
role), POLICIES.md section 2, the first-pass reports R-A.md, R-B.md, R-C.md, the eight proposal folders as they
now stand, the fix-round gate logs (check4_fix_*.log, validate_fix_*.log), and these store entities:
synthesis.seeding-remainder-excludes-perturbative-pati-salam, synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries@2,
synthesis.de-sitter-field-fixes-the-observer-tube-point@4, std-algebra.spin-double-cover@1, obj.std-algebra.pin-spin,
primer.centre@3. Not read: findings/, work/, RUN.md, ATTACK.md, LEADS-source.md, the attackers' briefs.
Scratch: /tmp/referee-R2ABC/ (a1.py, b1.py, perturbed check copies a1p/ a2p/ a3p/ b1p/ b2p/ c1p/ c2p/ c3p/).
No sympy; exact Fractions and GA.py where exactness matters, floats only for the A1 margins (checked against the
check's exact brackets).

Gates: all eight check4_fix logs report 0 errors, check result pass. All eight runcheck runs pass on the
unmodified checks. validate: seven ok; the fixed-form-completion log fails with five errors (E214 three times,
E201, E204), and every one of them is the missing entity
synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two (E204 is the consequence:
effective status "unsupported" because that `uses` target is missing). Confirmed: that is the only cause.

| item | verdict |
|---|---|
| A1 heating coefficients / chain's bath | ACCEPT WITH (two figures, two sentences) |
| A2 rotation weights, no trace at nonzero weight | ACCEPT |
| A3 spreading law (v7, conjectured) | ACCEPT |
| B1 tube-point clause on black-hole fields | ACCEPT WITH (reading of "other than K", (vii)'s condition, a de Sitter remark, check docstring) |
| B2 even-parity Zerilli equivalence | ACCEPT |
| C1 position vector in codimension three, clause (L) | ACCEPT (one optional label) |
| C2 fixed-form completion over a ball | ACCEPT (after C1 is stored; one optional label) |
| C3 corank-one wall eigenbundle class | ACCEPT WITH (one technical-level sentence) |

---

## A1. synthesis.heating-coefficients-across-curvature-couplings-and-on-the-chains-bath

**Verdict: ACCEPT WITH** the wording changes below. Clause (iii) is now correct; the WRONG verdict is cured.

**Restated conclusion recomputed by my own route** (a1.py: c from the formula of (i), c* scaled by
kappa_s(g)/kappa_s(100) computed from the stored kappa_s formula, not from the g^{3/2} shortcut):
- g = 188 + 84 + 42 = 314; kappa_s(100) = 145.26, kappa_s(314) = 808.24, ratio 5.5641 = 3.14^{3/2}; c* = 75.087.
- Per-vector coefficient ratio 2.1891. 22 vectors: c = 1.15848, margin **2.837**. Four SM contents (all scalars at
  xi = 0, tau_D = 16, tau_B = 188): c = 5.08735, margin **1.9600**. Counts: c*/c = 1425.9 vectors, 59.04 SM contents.
- Inconsistent case (c* left at 13.4949): 1.847 and 1.276, as stated.
- Four chain copies (C_D = 584): c = 15.888 (xi = 0), 10.251 (xi = 1/6); margins 1.4744 and 1.6451; interval ends
  xi = -0.14026 and 0.47359, as stated.
- The physics of the second entry is right: Y = n/s is conserved through the later thresholds, so the yield at
  production must use g_s and g_* of the bath at production, and c* goes as g_s g_*^{1/2}.

So the brief's "2.83 and 1.95" are lower bounds, not the values: the margins are 2.84 (2.837) and 1.96 (1.9600).
The formal's brackets "between 2.83 and 2.84" and "between 1.95 and 1.97" are true. The technical and one-liner
round them wrongly ("2.83 and 1.95"). 1.95 is not a rounding of 1.9600 either way.

**Fixes of the first referee, level by level.**
- c* recomputed with the chain's bath: done in formal (iii), technical, lay, one-liner, proof, check and coverage.
- Reading's "dependence that matters" conclusion replaced; no level says or implies that the exclusion fails at
  the tree-level value. The only mention is the extraction note's history, labelled as the wrong first version.
  The check keeps 1.84 and 1.27 explicitly as "the inconsistent case".
- Bath restricted to N_s = 188, the clause's own chain. The chains with 64 and 68 scalars are said to be not
  treated.
- "Least of the stored unification scales" corrected to 8.9e14 GeV.
- Four copies labelled as this result's construction.
- (i): "does not decrease" with the constant case stated.
- Right-handed-neutrino mass caveat added (scope and extraction).

**New overclaim from the fix round.** Lay: "it does not depend on the curvature number of any spinless particle".
Technical: "No stored reading of a coupling decides anything in the heating." Neither is shown, and the first is
false. On the chain's bath with every scalar (bath and four SM copies) at one coupling, the four-contents clause
fails for |1 - 6 xi| > 4.92 (xi < -0.65 or xi > 0.99). At the stored tilt window (tau = 66.2 to 68.7) it fails
with c = 530 to 571 against c* = 75.1, margin 0.61 (a1.py). The 22-vector clause is untouched (vectors are blind
to couplings). The formal Reading is correctly qualified ("at either stored reading").

**Wording changes.**
1. Technical and one-liner: "become 2.83 and 1.95" -> "become 2.84 and 1.96".
   Optional: the four-copies margin at xi = 1/6 is 1.645; write "1.65", or "between 1.64 and 1.65" as the proof
   does.
2. Lay: "and it does not depend on the curvature number of any spinless particle" -> "and at the two values of
   the curvature number that the store assigns, the answer is the same".
3. Technical, last sentence: "No stored reading of a coupling decides anything in the heating" -> "On the chain's
   bath neither stored assignment, 0 or 1/6, decides the clause; the tilt window's coupling on the chain's scalars
   is not treated."

Perturbations (both caught, chain-bath function only): threshold scaled as g^2 in place of g^3 in its square (that
is, kappa_s taken as proportional to g_s alone); chain vectors 21 -> 24. Status: (i) proved, (ii) and (iii)
computed, as labelled.

---

## A2. synthesis.rotation-weights-of-pair-sources-fix-the-channel-weights-and-give-no-trace-at-nonzero-weight

**Verdict: ACCEPT.**

Every fix of the first referee is applied:
- (v) now states that it is conditional and that "all its content is in the hypothesis".
- The title is renamed. The old id survives nowhere in the folder.
- The Reading says the fermion coefficient is not unchanged at G^3 (the trace-free vacuum response rescales every
  c_i c_j), and only the trace-anomaly part is zero.
- The interacting-theory sentence is marked as resting on the helicity of the state, not on (v). This appears in
  the extraction note and in the Reading.
- The pointer now reads clause (v) of the Weyl-flat theorem.

The lay and technical levels repeat these qualifications and claim no more. No new "proved" clause; the
mathematics of (i) to (vi) is unchanged from the first pass.

Perturbations (both caught):
- Orthogonality factor N_i N_j/5 -> /4 in the prediction: the channel-weight check fails.
- Fermion norm s^2/4 -> s^2/3: the channel-weight and pair-weight checks fail.

---

## A3. scrambling.spreading-law-chaos-bound-saturated (v7)

**Verdict: ACCEPT.**

- Status is `conjectured`. checked_by has no `kind: proof`, and proof-main.tex opens "This file is not a proof".
- Clauses (a) to (d) are each headed "stored" with the theorem cited. (e) is headed "The estimate; conjectured".
- Technical: "nothing new is proved". Lay: "It is not proved". One-liner: "(conjectured)". No level claims the law
  proved.
- The orientation fix is applied in (a): the one-unitary-group theorem's reversed parameter and e^{+-kappa t} are
  stated, with "|t_*|" and "in the direction of time in which the flow dilates". Technical repeats it.
- The amendment and the extraction note record the refused status raise.
- The duplicated version-6 credit entry is inherited from the stored v6; it was not introduced here. The
  maintainer may drop it.

Perturbations (both caught):
- Squared amplitude 1/N -> 1/(N+1): the affine-cell check fails.
- kappa = f'(2M)/4: the rate check fails.

R-A's remark that check_rate_is_modular_rate touches scrambling.mode-count and not the (N+) theorem still holds.
check4 records the (N+) theorem as declared and untouched, which is accurate.

---

## B1. synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent

**Verdict: ACCEPT WITH** the four changes below. (i) to (vi) and the restricted closing paragraph are now true as
worded. (vii) is true under one precise reading of "other than K", which the text must state.

**Fixes of the first referee.**
1. (iv) and the closing paragraph are restricted to gauges in which K generates a positive multiple of xi, and the
   overclaiming sentence is gone: done at every level.
2. "Other than K itself": done, in the preamble.
3. Reading (c): done, labelled argued.
4. General-lapse connection form: proved in one line in the proof. Lie-theory facts: labelled standard and not
   proved. n_O-coefficient positivity in (iii): added.
5. Store wording flagged: decision (4).

**(vii) verified as stated.**
- Proof algebra: psi^{-1} B_tau psi = boost composed with R_J(c tau); J commutes with psi; the centraliser of
  a xi + cJ in R xi (+) so(3) is span(xi, J). The check confirms the conjugation identity on 72 points.
- My own derivation of the axis points X = I-hat + (1 - sigma^2)^{1/2} w +- sigma W-hat, for I = n_inf +
  (Lambda/6) n_O and J = e3 e4: normalising the n_O-coefficient gives foot 0 and
  rho^2 = (12/Lambda_I)(1 - sigma^2)/(1 +- sigma)^2. That is the stated rho, with the sign attached to the choice
  of +-n_J.
- For a general axis n_J = cos phi v_0 + sin phi W-hat, the foot is sigma cos phi (2 alpha beta)^{1/2} v_0 /
  (alpha (1 + sigma sin phi)): on the line R v_0 through the centre, as stated.
- The norm a^2 f - c^2 r^2 sin^2 theta is correct.

**Precision needed 1: what "other than K" means.** In the twisted gauge the symmetries commuting with K are the
abelian span(K, J), and xi = (K - cJ)/a is one of them.
- I checked exactly (b1.py) that xi fixes none of the axis points (J.X = 0 there, so xi.X = K.X/a, not a multiple
  of X).
- So under the literal reading "every symmetry commuting with K that is not a multiple of K", no tube point is
  fixed in the twisted gauge. The same holds in every field, de Sitter included, because K + B fixes nothing when
  B fixes the point.
- The conclusion of (vii) holds when the symmetries "other than K" are the compact ones (the rotations). In
  span(K, J) that is the line of J, and in (iv) it is the so(3). This also agrees with the store's "transverse".

Change the preamble's "read throughout as: m is fixed by the symmetries of the field commuting with K other than K
itself" to: "read throughout as: m is fixed by the rotations among the symmetries of the field commuting with K
(those generating a compact group: the so(3) in (iv), the group of J in (vii)); read as every symmetry commuting
with K that is not a multiple of K, the condition is met in no field, since K + B fixes no compatible tube point
that B fixes". Use the same words in (vii) and in reading (a) of the closing paragraph.

**Precision needed 2: (vii)'s condition on the symmetries.** The stated condition ("the field has no symmetries
beyond xi and the so(3)") is sufficient. What the proof uses is weaker: that the centraliser of a xi + cJ in the
field's symmetry algebra is span(xi, J).
- I computed exactly (b1.py) that this weaker condition holds in the de Sitter field. Its 10-dimensional algebra
  of bivectors commuting with I_Lambda gives a centraliser of K + cJ of dimension 2, equal to span(K, J), at
  c = 1 and c = 3/7. This is the Cartan subalgebra of so(1,4).
- So the twisted gauge exists in de Sitter too. The stored de Sitter theorem is a fixed-gauge computation and stays
  true. But the stored clause's "What it is for" sentence ("so the clause fixes rho there") holds only under
  reading (a), like the black-hole result.

Changes:
- In (vii), replace the condition with "when the symmetries of the field commuting with a xi + cJ are spanned by
  xi and J (true if the field has no symmetries beyond xi and the so(3), standard for the two fields and cited
  from memory; true also for the de Sitter field, whose centraliser of a xi + cJ is a Cartan subalgebra)".
- Add to decision (1) that the de Sitter selection of the stored clause also rests on reading (a).
- Technical, first lines: "In the de Sitter field this picks one observer" -> "In the de Sitter field, with the
  boost as the horizon's flow, this picks one observer".

**Cosmetic.** check.py line 1 still carries the old id
(synthesis.tube-point-clause-fixes-no-observer-where-rotations-have-no-fixed-point). Rename it.

Perturbations (both caught, twisted-gauge function only):
- rho = 2c/(1 + sign s) in place of (1 - sign s).
- Sign of the rotation back in the conjugation identity flipped.

Status: "proved" is right for (i) to (vi); for (vii) it is right conditionally on the cited symmetry algebra, as
the text says, and once the reading of "other than K" is stated.

---

## B2. synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations

**Verdict: ACCEPT.**

All four fixes are applied:
- (6) now reads "superseded on oscillating channels only", with the time-general forward implication left as
  stored.
- omega is given weight -1 (w weight -2) in the formal and in the proof.
- The description of (C3) is reworded: (C3) = clause (4), and what clause (5) of the stored theorem needs beyond
  it is clause (5) here.
- (6) is headed "given (C1) and (C2)" and repeats it inside.

The optional "real omega" was kept; that is harmless. No new claim.

Perturbations (both caught by the two reconstruction checks):
- V_e constant 18 -> 17.
- V_e coefficient 6 lambda^2 r^2 -> 5 lambda^2 r^2.

The potential in the check is the standard Zerilli form at M = 1 (consistent with my recollection, which is not
used as evidence).

---

## C1. synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two (clause (L))

**Verdict: ACCEPT.**

**The closed lemma, checked line by line.** Rotors are now *defined* as even versors of unit vectors (Spin^+ of
obj.std-algebra.pin-spin). In definite signature R R~ = prod Q(u_i) = 1, so Spin = Spin^+, and SO^+ = SO follows
from Pin -> O surjective with determinant (-1)^k. The cited theorem (spin-double-cover@1) gives exactly what is
used: twisted adjoint, Pin -> O and Spin^+ -> SO^+ surjective, kernel {+-1}.

Compactness is proved by showing that the closed, bounded set S (even R, R R~ = 1, Ad_R preserving vectors) equals
the rotors. The argument through the centre is correct:
- Ad_R is an isometry, so the cited theorem gives a unit versor g with g^ v g^{-1} = R v R~.
- y = g^{-1} R satisfies v y = g^{-1}^ R v, which I checked.
- If g is odd, y is odd and anticommutes with every vector. Blade by blade, an odd blade commutes with each basis
  vector it contains, so y = 0, which is impossible.
- So y is even and central. By primer.centre@3 the even part of the centre is R (the pseudoscalar is odd for n
  odd), so y = lambda, lambda^2 = 1, and R = +-g.

The norm <A~ A>_0 is the sum of the squares of the blade coefficients in Cl(n,0), so S is bounded. Consequences
(a) and (b) are correct (compactness, continuity of Ad, kernel {+-1}). The path lift, its uniqueness, and the strip
induction for continuity on the square are correct, including the triangle-inequality exclusion of the minus sign.
So are the constancy of sigma and sigma(1) = 1. This closes R-C's gap. The new check function tests the blade
facts the centre step uses, for n = 1..6.

**Other fixes.**
- (6) now says that (4) with W_0 = 0 rules out every repair, and that the computation covers only the form
  x + beta E.
- The group is named.
- Codimension five's infinite order is marked "classical, from memory".

**Optional label.** (6): "it is not seen on any circle of the sphere, the circle bounding a disc over which G_+ is
trivial". This uses that the bundle is trivial over every disc of the sphere, which is standard and is not
argued. It is one line from the rotation covariance of the family (the frames of (1) rotated, away from any point
missing the disc). Add "(standard)" or the line.

Perturbations (both caught):
- Rotor end expected as (-1)^{k+1}: the rotor-lift check fails.
- Odd blades admitted as "central": the new centre check fails.

---

## C2. synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial

**Verdict: ACCEPT** (to be accepted after C1, whose clause (L) it uses).

**Fixes of the first referee.**
- Fix 1: K_0 is now stated exactly as 1_c (+) (-1_{c'}) (+) 1_N in (2).
- Fix 2: the lifting lemma is no longer copied; (4) cites C1's clause (L).

**The widening.** For any nondegenerate K_0' on W_0 of signature (c + N, c'), Sylvester's law gives a constant
invertible Lambda with K_0' = Lambda^T K_0 Lambda, and (1 (+) Lambda)^T h-hat (1 (+) Lambda) is continuous,
symmetric, invertible, and equal to G (+) K_0' outside B. That is correct and complete. It is proved in the proof
text ("Other forms of the same signature") and tested in the check: a non-orthogonal Lambda, signature (6,2) at
every sampled point, and the exterior equal to G (+) K_0'. The widening is to forms of that one signature only,
and no level claims more: technical says "any fixed form of that signature". It is consistent with (1), whose
necessity for K_0' gives G_+ (+) R^{c+N} trivial.

Optional: label Sylvester's law as standard (not in the store).

**validate.** All five errors are the not-yet-stored C1 id (see top). Nothing else.

Perturbations (both caught):
- The change of basis applied on one side only: the fixed-form check fails.
- F in place of F^{-1} in Phi_t: the rotation-homotopy and fixed-form checks fail.

---

## C3. synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line

**Verdict: ACCEPT WITH** one sentence.

**Fixes of the first referee, now applied.**
- One-liner, technical (3) and the extraction note now say "of the same form as the stored one-sided necessity
  clause" and "relation not decided", and no longer identify the stored N.
- Lay: the false "all follow" and "the same object" sentences are gone. Naturality and conservation are said to be
  not shown.
- Reading: marked argued, two-sided, and dependent on G-bar_- (q).
- Hypothesis sentence: now runs through the hypotheses of the one-rung theorem, the side signatures, a thin collar
  and homotopy invariance (labelled standard, from memory).
- Weyl's inequality and the dimension axiom are flagged. Adding the axiom to the Fact is listed for the
  maintainer.
- Title and (5): "relative across the collar". The w(Sigma) reading is stated, with the lens-space ambiguity noted.
- (4): "constant" hyperbolic plane.

**Remaining.** The technical level's opening parenthesis still reads "(every tame corank-one wall with compact
cross-section; first-order vanishing is not needed)". That is the unqualified sentence the formal level corrected.
Replace it with "(every wall satisfying the hypotheses of the stored one-rung theorem, with the collar thin enough;
first-order vanishing is not needed)".

Perturbations (both caught by the two-rung function):
- The l-component of b replaced by a constant (untwisted).
- K_ph of signature (3,1) in place of (2,2).

---

## Possible memory items

None about the user.
