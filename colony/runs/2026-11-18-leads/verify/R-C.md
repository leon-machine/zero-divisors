# Referee report, group C (walls), run 2026-11-18-leads

Read: REFEREE.md (common part, group C), colony/BRIEF.md (referee role, Standards), POLICIES.md section 2; the
three proposal folders; the store entities synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump
(v1), std-algebra.spin-double-cover (v1, with its proof), obj.std-algebra.pin-spin, std-algebra.periodicity (v2),
synthesis.wall-class-one-rung-obstruction (v3), synthesis.wall-rung-count-is-height-of-dying-line-class (v2, with
its proof where needed), sheaf.tameness (v1), sheaf.wall-class (v3),
synthesis.lens-space-wall-rung-count-sees-the-integral-twist (v6), transport.obstructions-are-moved-never-destroyed
(v4), the two imported Facts used by C3, and op.eigenbundle-class-of-degenerations. Not read: findings/, work/,
RUN.md, ATTACK.md, LEADS-source.md.

check4 logs: all three report "0 error(s), 0 other finding(s); check result: pass". runcheck: all functions PASS
(C1 6/6, C2 5/5, C3 3/3). Scratch and own scripts: /tmp/referee-C/.

---------------------------------------------------------------------------------------------------------------

## C1. synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two

**Verdict: SOUND WITH FIXES.** The claim really is the stable one, and the proof of stability is genuine. The
fixes are a gap in the lifting lemma (it is easy to close) and one sentence that does not follow.

**Stable or unstable (the failure the brief asked about).** It is not dressed up. In (3), triviality of
G_+ (+) R^N is assumed for an arbitrary N. The clutching loop in SO(2k+N) is gamma (+) id_N. The lift that is
exhibited is the product of the k plane rotors in Cl(2k+N,0), and it ends at (-1)^k for every N. The null-homotopy
c(u,t) = alpha_N(y_N) alpha_S(y_S)^{-1} is built correctly: alpha_N = gamma alpha_S on the equator, c(1,.) is
constant at the poles, c(u,0) = c(u,1), and det c = 1 because c(0,0) = 1. The lemma then forces the lift to close.
So "(-1)^k is an invariant of the stable class" is proved for each N separately, which is what stable
non-triviality needs. The proof never names the group pi_1(SO); it needs only the lemma.

**Lifting lemma (proof read line by line).** Points (a) and (b), the path lift, the lift of the square and the
constancy of sigma are all correct. Gap: the lemma proves the rotors compact by *defining* them as "the even R with
R R~ = 1 that map vectors to vectors" and calling that set closed. The cited spin-double-cover@1 is a statement
about Spin^+ = even *versors* (obj.std-algebra.pin-spin). That the two sets are equal (the Lipschitz statement) is
neither proved nor cited. Two smaller unstated steps:
- SO^+ = SO in definite signature.
- Spin^+ consists of unit-norm elements.

**Fix:** add two lines. If R is even, R R~ = 1 and Ad_R preserves vectors, then Ad_R lies in O(n) and has
determinant 1. Take a versor R' with Ad_R' = Ad_R. Then R'~R is even and commutes with every vector, so it is a
scalar by primer.centre, and R = +-R'. In Cl(n,0) every product of unit vectors has prod Q = 1, so SO^+ = SO. C2
copies the same lemma and needs the same fix.

**Other steps.**
- (1) The frames and their squares (1 +- x3)/4 hold, and so does the equator relation.
- (2) R_a f1 R~_a = cos a f1 - sin a f2, matching gamma.
- (4) Correct use of clause (4) of the stored theorem: M = R^3 is contractible, and U is bounded, so the sphere of
  radius r lies in M \ U.
- (5) Correct. T = S p4 (+) S e1 p4 is checked exactly, and on T, (x + beta e4)^2 = Q(x) + beta^2.
- (b) Both directions of "iff k even" hold: (4) gives k odd with any W0 and K0, and (5) gives k even with W0 = 0.
- The G_- case reduces correctly to G_+ by the antipodal pull-back.

**Fix (6).** "On S no nonzero symmetric map anticommutes with e1, e2, e3, so no repair without added directions
exists there either" is a non sequitur: a repair need not have the form x + beta E. The conclusion is true, but
because of (4) with W0 = 0. Reword it so: (4) with W0 = 0 rules out every repair, and the computation shows only
that none of the form x + beta E exists.

**Minor.**
- "A class of order two": name the group. It is stable classes over S^2 under direct sum; (3) and (5) prove the
  order is exactly 2.
- The extraction note says the infinite order in codimension five is "cited in the stored result". The stored
  Reading cites only non-removability (ABS), not the order. Drop that clause or mark it as from memory.

**No Bott or characteristic classes in any proof step (c).** The w_2 / KO~(S^2) reading is flagged as from memory
and is not used. periodicity@2 is used only to name S the least module.

**Own route.** I = e1e2e3 is central with I^2 = -1, so G_+ is a complex line bundle. I verified exactly at 22
equator points that n2 = I n1, s2 = I s1 and s1 = (cos a - I sin a) n1. The complex transition function has
winding -1, so G_+ is the (conjugate) Hopf bundle. That is consistent with the claimed real turn and with w_2 != 0.
Script: /tmp/referee-C/own/c1_complex.py.

**Perturbations (all caught).**
- Rotor through the full angle: rotor-lift check FAIL.
- End sign expected as (-1)^(k+1): FAIL.
- North frame replaced by (pi p, pi e1 p): frame and clutching checks FAIL.

The rotor check tests the rotor in an abstract Cl(5,0), not the module frames. The link between the two rests on
the proof text, which is fine.

**Status.** "Proved" is right once the lemma is fixed. Every clause is proved in the text. (6) rests on an exact
full-rank linear system: complete, not sampled.

**Duplication.** The theorem itself duplicates nothing in the store. The lemma is duplicated in C2, so store it once.

---------------------------------------------------------------------------------------------------------------

## C2. synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial

**Verdict: SOUND WITH FIXES.**

**(a) Necessity.** This is clause (4) of the stored theorem: R^m is contractible and contains the closed exterior
of B, including the sphere dB. The (K_0)_+- are fixed subspaces. Correct.

**(a) Sufficiency.** The checks:
- Phi_{pi/2}: I recomputed R_{pi/2}(1 (+) X)R_{pi/2}^{-1} = X (+) 1, so Phi_{pi/2} = 1.
- The seams at r = 2rho/3 and r = rho/3 match.
- Invertibility holds in every region.
- Continuity at the centre holds.
- (3) is correct: G_+ (+) R^c trivial gives G_- (+) R^{p+c} trivial, so take c' = p + c.

Own nontrivial example: the winding-two family [[x^2-y^2, 2xy], [2xy, y^2-x^2]], which has no rank-two completion.
I took c = c' = 0, N = 2, rho = 2 and F = the rotation through a, and built the four regions exactly at 10 circle
points, with t parametrised by rational tan(t/2). Results:
- Phi is orthogonal.
- h is symmetric with signature (3,1) at all 150 points.
- Phi_0 D Phi_0^T = sgn g (+) 1.
- Phi_{pi/2} D Phi_{pi/2}^T = D.

Script: /tmp/referee-C/own/c2_construction.py.

**Fix 1 (a real error in the statement).** (2) says only that "K_0 [is] positive definite on the first and third
summands and negative definite on the second". The seam at r = 2rho/3 needs K_0 = 1_c (+) (-1_{c'}) (+) 1_N
exactly, because sgn g (+) K_0 must equal Phi_0 D Phi_0^{-1}. The proof does say "on which K_0 is the identity",
but the statement is wider. Either state K_0 as that exact matrix, or add an interpolation from a general definite
form.

**Fix 2.** The lifting lemma has the same Spin^+ gap as C1; fix it the same way.

**(b) Hypotheses.** All are stated:
- base R^m;
- the degeneration set inside an open ball;
- model completions as in the stored theorem;
- continuous, not smooth. The completions built are only continuous, so this does not speak to the smooth one-sided
  rung completions.
- the rank added, N = n + c + c', explicitly not claimed least.

"Stably trivial" is defined as a sum with a fixed R^c. (1)-(4) say exactly which form is meant: G_+ (+) (K_0)_+
trivial is necessary for that K_0, not sufficient for it (4), and sufficient after flat directions are added. That
answers the open problem's wording.

**(c) Winding-two family.** Verified:
- The positive line is spanned by (x,y), so it is trivial; the map into RP^1 has degree 2.
- sgn G s_0 is the rotation through 2a.

The double-lift argument through j: Spin(2) -> SO(2) is correct (it encodes "winding 2 is not null-homotopic").
The one-direction repair with nu = (-beta y, beta x, 1 - beta) is correct: Q(nu) > 0, it equals sgn G (+) 1 where
beta = 1, and the radial rescaling reaches G (+) 1.

**Perturbations (both caught).**
- Phi without the final R_t^{-1}: two checks FAIL.
- nu made radial: the winding-two check FAIL.

**Status.** "Proved" is right. Transport-absent in its proof, which the proposal says itself. It does not
contradict the refutation entity: clause (5) reproduces the three stored escaping families.

---------------------------------------------------------------------------------------------------------------

## C3. synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line

**Verdict: SOUND WITH FIXES.** The mathematics of (1)-(4) is correct. The fixes are in the wording, and they matter
because they claim the stored one-sided theory.

**Proof steps.**
- Tool (b), the projection-family isomorphism, is correct.
- (1) is correct. The spectral gap and the uniform continuity argument hold. It uses Weyl's eigenvalue perturbation
  bound without saying so: elementary, but flag it.
- (2) is correct. It needs nondegeneracy only on the collar, and nothing along Sigma.
- (3) is correct. sig K_far = (k+1, k-1), det N = L, w(N) = (1+x)^{-1}, x^j = 0 for j >= k. It uses the dimension
  axiom of Stiefel-Whitney classes (w_j = 0 above the rank). That axiom is not in the quoted text of
  synthesis.imported-whitney-product-formula-and-projective-space@1. The stored rung-count proof has the same
  silent use, so this is a pre-existing gap: add the axiom to the Fact.
- (4) is correct. The one-rung exclusions hold only with *constant* hyperbolic and definite planes, which is the
  natural reading of "the hyperbolic plane". The two-rung form has n and b orthonormal, signature (4,2) and the
  right end forms.
- (5) is correct.

Own check: I built h = 1 - 2(nn^T + bb^T) myself and checked, exactly on a 7 x 6 grid:
- signature (4,2);
- the end forms;
- the V-block at t = pi/2 equals G(-1);
- h does not restrict to G at the wall.

Script: /tmp/referee-C/own/c3_own.py.

**Perturbations (both caught).**
- K_far untwisted (n constant): FAIL.
- b without its l-term: FAIL.

**(a) Tameness.** (W) is a model-free set of hypotheses, and nothing of (T3) is used. The sentence "every tame
corank-one degeneration with compact wall and product collar satisfies (W)" silently needs three things:
- the side signatures, which are hypotheses of the stored theorems, not part of tameness;
- a collar thin enough to avoid other degeneracy;
- the identification of V on Sigma x [-1,1] with a pull-back, which is homotopy invariance of bundles: standard,
  from memory, not in the store.

**Fix:** "every degeneration satisfying the hypotheses of synthesis.wall-class-one-rung-obstruction", and flag
the pull-back as cited or make it a hypothesis only.

**(b) Two-sided versus one-sided.** Formal (3) states the difference correctly. Elsewhere it does not:
- **One-liner** ("which for k rungs is the stored necessity clause ... with N the far form's negative eigenbundle")
  and **technical (3)** ("the stored necessity clause of the rung count, with N identified"): wrong. The stored
  clause concerns one-sided completions, which have no far form. Its N is not identified by this result.
- **Extraction note**: "the bundle N of the stored clause is identified ..." is false for the same reason.
- **Lay**: "The conditions the earlier wall results found one by one all follow from this single statement" is
  false. None of the following follow: the one-sided necessity, both sufficiency clauses, the twisted-rung clause
  (5) of one-rung-obstruction, and the lens-space counts.
- **Lay**: "the invariant ... the earlier conjecture asked for and the twist of the general theorem are the same
  object" overclaims. Naturality and conservation, clauses (b) and (c) of sheaf.wall-class, are not shown.
- **Reading**: "the rung count is the number of flat directions needed to cancel the class" should be marked as
  argued, and as being about the two-sided count. The count also depends on G-bar_- (that is, on q), not on the
  class alone.

**Also.** The class computed is local to the collar, a comparison of the two slices. The stored transfer class is
relative to M and can carry exterior information: clause (5) of one-rung-obstruction needs w_1(L) to lie in the
image of H^1(M_+). Title (5) should say "relative across the collar". "Exactly the information of W(Sigma)" holds
if w(Sigma) is the clock mismatch, as in one-rung-obstruction. But the lens-space entity uses w(Sigma) = 1 as the
Stiefel-Whitney class of Sigma. The store is ambiguous, so say which reading is meant.

**(c) Duplication.**
- Partly duplicative: (4)'s one-rung failure is an instance of stored one-rung clause (3), and its two-rung form is
  an instance of stored rung-count clause (2).
- (3) at k = 1 re-proves the necessity half of one-rung clause (3).
- New: the eigenbundle bookkeeping (1), the slice-to-slice transfer (2), and the identification of N for two-sided
  completions.
- It is not a restatement of the wall-class theorem.

**Status.** "Proved" is right for formal (1)-(5) once the hypothesis sentence is fixed. The overclaims sit in the
one-liner, technical, lay and extraction text.

---------------------------------------------------------------------------------------------------------------

## Cross-checks (all three)

- **Lens-space rung counts:** no contradiction. With q = 0, C3 (3) at k = 2 needs L (+) L = R^2, which fails on
  L(4,1), so the two-sided count is at least 3 there. That agrees with the stored k = 3 = e(L). With q >= 1 the
  condition G-bar_- (+) L (+) L = G-bar_- (+) R^2 can hold, which agrees with the stored k = 2.
- **transport.obstructions-are-moved-never-destroyed v4:** all three are consistent with "refuted as stated;
  transfer holds". C2 turns transfer into a criterion only for model completions over R^m with the degeneration in
  a ball, and keeps C2 (4) as the counterexample to sufficiency for the given form.
- **C1 and C2 agree:** odd k is not stably trivial, so there is no model completion. Even k needs no added
  direction, which beats the bound N of C2.

## Possible memory items (from this review, not from memory)

None about the user.
