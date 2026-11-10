# Attack B (angle B: cross-pollinating and adversarial), run 2026-11-09-three

Status: attack round done. One proposal filed (T3). T1 and T2: nothing filed, reasons below. Kill conditions were
written before any computation.

NOTE TO A (coordination, 20:25). B intends to file ONE proposal, on T3: the no-go "pair currents of the light-ray arrays
have helicity 0 or +-1, never +-2, and only helicity-0 ones are canonical, so the one-array-per-helicity-channel rule
cannot be met at any n_g; the capacity inequality as arithmetic passes n_g = 2 on store-allowed contents; the Sakharov
weight has zeros at every n_g in 1..5 once xi_R and the gauge parameter are free" (section T3 below). If A files on T3,
please file only what differs (a conditional theorem with named premises), or leave T3 to B. On T2, B files nothing:
the exact adversarial checks below (intertwiner kernel, l = 0, 1, horizon values, Kruskal form) are offered to A for
the spin-2 proposal's scope clauses. On T1, B files nothing (kill condition fired, see below).

## T1 op.wall-class-invariant (hidden hypotheses; a wall with k not determined by (W, beta x, signature))

Routes.
- R1 (the problem's): comparison pair of walls with the same W, beta x and signature and different k
  (L^7(4) against L(4,1) x T^4, dropped by both attackers of the earlier run).
- R2 (other subject, K-theory against cohomology): a pair on which every ordinary-cohomology datum built from x and
  beta x agrees (including the divided square 2a^2, 2a = beta x, which the stored result already calls "a function of
  beta x") while the K-theoretic order of 1 - xi differs: L^31(4) against L^7(4) x T^24 (w = 1 on both).
- R3 (own, audit): list what each stored conditional result uses of the lens-space facts, and test A's derivations
  against that list (hidden use of the full K-ring: the lower bound on the order of 1 - chi^2 needs injectivity of the
  presented ring into K(Sigma), which no characteristic class supplies).
Choice: R3 first (cheap, and it decides what A must derive), then R2 only if the pair can be made exact.
Kill condition (pre-registered): R2 is dead, and nothing is filed on T1, if the two walls of the pair are separated by
any cup-product datum of a with 2a = beta x (for example a^j = 0 on one and not the other at some j): then k may still
be "a function of beta x through the integral ring" and the pair proves nothing beyond the stored clause (4).

Outcome.
- R3 (audit; argued, by reading the two stored proofs).
  (i) K-theory result: clause (1) (2^{k-1}(1 - xi) = 0) uses only the ring structure and lambda-operations of K
  (lambda^j = 0 above the rank, lambda_t multiplicative, line bundles) and cancellation in the group K: no real
  K-theory, no orientation convention. Clause (2) (the lower bound on the order of 1 - chi^2) uses the HARD half of
  the K-ring: that K(L^{2n+1}(4)) has no relations beyond (chi^4 - 1, (chi - 1)^{n+1}), since the map chi -> I to
  Z[I]/(pi^{n+1}) must be well defined on K(Sigma). The easy half (those relations hold: lambda_{-1}(V) restricts to
  zero on the sphere because V has a section there) gives only upper bounds on orders and is useless for the stored
  use. No characteristic class supplies the hard half: c(2 xi) = (1 + 2y)^2 = 1, and the leading symbol of
  (1 - chi^2)^k in the Atiyah-Hirzebruch filtration is 2^k y^k = 0 for k >= 2. So a "character computation on a
  skeleton" that only verifies relations does not discharge the hypothesis. What does suffice (argued): (a)
  surjectivity of R(Z4) -> K(Sigma) and (b) the order |K~(Sigma)| = 4^n; (b) is the collapse of the
  Atiyah-Hirzebruch spectral sequence (odd integral cohomology vanishes below the top degree), which is itself a
  literature theorem. Test for A: any derivation offered for the K input must produce a lower bound on an order
  (a homomorphism out of K(Sigma), or the count 4^n); if it only checks that relations hold, it derives nothing the
  stored result uses. The exact orders for n <= 8 additionally use the full presentation (lattice membership).
  (ii) q1 result: sign and orientation conventions are harmless (2y^2 = -2y^2 in Z4; q1 is computed for both spin
  structures); it uses q1 natural and stable with 2 q1 = p1 and, silently, that q1 of the canonical spin structure
  on a plane bundle with Spin(2) Euler class a is 2a^2 UP TO SIGN: fine in Z4. It does not use T Sigma + R = (m+1) eta
  for the obstruction (only for remarks on the walls), so that item of the derivation list discharges nothing in the
  lower bounds; A can skip it without loss for lifting the conditions.
- R2: the kill condition FIRED. The pair L^31(4) against L^7(4) x T^24 (both w = 1, x != 0 = x^2, beta x of order 2,
  (beta x)^2 = 0, q1 = 2a^2 != 0 of order 2; k >= 8 against k <= 6 given the stored bounds) is separated by a^4 (nonzero
  on the first, zero on the second; a = y is the class with 2a = beta x, defined up to 2-torsion, and 2a^j does
  not depend on that choice). Every pair I can build from lens spaces,
  products and projectivised flat bundles is separated the same way, because classes pulled back from L(4,1) keep
  y^2 = 0. So no wall is exhibited on which k is undetermined by the integral ring data of x; what IS established by
  the stored clause (4) is weaker and already filed (no function of ht(x), ord(beta x), (beta x)^2 decides k).
  Nothing filed on T1. Conjecture (conjectured, on the lens family only): k depends on (Sigma, x) through the height
  of a class a with 2a = beta x (on L^{2n+1}(4), ord(1 - chi^2) = 2^{floor((n+1)/2)} is a function of ht(y) = n + 1).
Proposal: none. Next step: sharpen the success clause (decision for Leon) before anyone hunts a counterexample again.

## T2 op.helicity-per-boundary-mode, spin 2 (where it fails)

Routes.
- R1 (the problem's): take the Regge-Wheeler and Zerilli pair and test the intertwiner's kernel (the algebraically
  special frequencies), exactly, in rational functions of r with rational M.
- R2 (other subject: the stored helicity lift J1, homogeneities -6 and +2): compare the stored graviton count with the
  derived channel count (two parities per (l, m), l >= 2 only).
- R3 (own): l = 0, 1 (no radiative channel) and the sign of the l = 1 odd potential; gauge and chart dependence of
  "two-dimensional at the horizon".
Choice: R1 and R3 as exact checks handed to A and the referees; file only if A does not cover them and the result
stands alone.
Kill conditions (pre-registered). (a) The claim "the intertwiner is injective on every real-frequency channel" dies if
its kernel solves the Regge-Wheeler equation at a real nonzero frequency (omega^2 > 0). (b) The claim "W regular at the
horizon, rate e^{2 kappa r_*}, not uniform in l" dies if V/f has a pole or zero at r = 2M for some l >= 2 (either
parity). (c) The spin-2 channel count matches the stored graviton reading unless the stored text counts an l < 2
graviton channel; if it does, that is a stored inconsistency to report.

Outcome (work/B/t2.py, exact rational functions of r, M = 1 and 3/7, l = 0..6). Conventions: lam = (l-1)(l+2)/2,
V_- = f(l(l+1)/r^2 - 6M/r^3) (Regge-Wheeler), V_+ = 2f[lam^2(lam+1)r^3 + 3 lam^2 M r^2 + 9 lam M^2 r + 9M^3] /
(r^3 (lam r + 3M)^2) (Zerilli), both cited from memory; ' = d/dr_* = f d/dr.
- computed (exact identities): with g = f/(2r(lam r + 3M)), k = lam(lam+1)/(3M) = (l-1)l(l+1)(l+2)/(12M) and
  w = 6M g + k: V_-+ = w^2 -+ w' - k^2. So -d^2 + V_- + k^2 = (-d + w)(d + w) and -d^2 + V_+ + k^2 = (d + w)(-d + w):
  the intertwiner is d/dr_* + w and (-d + w)(d + w) = omega^2 + k^2 on Regge-Wheeler solutions of frequency omega.
- proved from that: kill condition (a) did NOT fire. The kernel of the intertwiner is the single function
  Z_0 = e^{-k r_*}(lam r + 3M)/r, which solves the Regge-Wheeler equation only with omega^2 = -k^2: time dependence
  e^{+-kt}, no oscillation (the "algebraically special frequency" of the literature, M omega = +-(unit)(l-1)l(l+1)(l+2)/12,
  from memory). So for l >= 2 the intertwiner is injective on every real-frequency channel and invertible there
  (inverse (-d + w)/(omega^2 + k^2)); at the horizon w -> k, so it multiplies e^{-+ J omega r_*} by k -+ J omega != 0
  (J the unit standing for the phase): ingoing stays ingoing, the horizon behaviour is preserved. A's use of the
  intertwiner to reach even parity is therefore sound for l >= 2 at real frequency, and ONLY there: it should say so.
- computed: kill condition (b) did NOT fire. V_-/f at r = 2M is (l(l+1) - 3)/(4M^2) (3, 9, 17, 27, 39 over 4M^2 for
  l = 2..6); V_+/f there is (l(l+1) - 3)/(4M^2) + 3/(2M^2 (2 lam + 3)) (27/7, 123/13, 121/7, 843/31, 1683/43 over
  4M^2). Both regular, positive for l >= 2, growing like l^2: the rate is e^{2 kappa r_*} and the approach is not
  uniform in l, as for the lower spins. The two parities have DIFFERENT horizon coefficients (they are isospectral in
  transmission, not equal as potentials). Pattern across spins (odd/Regge-Wheeler family): V/f at the horizon is
  (l(l+1) + 1 - s^2)/(4M^2), s = 0, 1, 2 (the stored scalar and Maxwell values and this one).
- computed: l = 1. lam = 0, k = 0: the intertwiner's kernel sits at omega = 0, Z_0 = 3M/r, a static solution of the
  l = 1 Regge-Wheeler equation ((1/r)'' = V_- /r exactly). V_- = 2f(r - 3M)/r^3 is NEGATIVE on 2M < r < 3M
  (V_-/f = -1/(4M^2) at the horizon). The formal l = 1 "Zerilli" potential degenerates to 2Mf/r^3. Argued (from
  memory): the l = 1 odd perturbation is the stationary angular-momentum shift and the l = 1 even one is pure gauge,
  so there is no radiative channel and the master functions are not gauge invariant there.
- computed: l = 0. lam = -1, k = 0 and the Zerilli denominator lam r + 3M vanishes at r = 3M, outside the horizon:
  no l = 0 channel equation of this form (argued: the l = 0 perturbation is the mass shift, Birkhoff).
- So the channel count is two (the two parities) per (l, m) for l >= 2 and none for l = 0, 1: this MATCHES the stored
  graviton reading (J1: two helicities, homogeneities -6 and +2); kill condition (c) did not fire on the count.
  But the WORDING of J3 v2 does not match: "the current boson of the s-wave theory is the s-wave reduction of each
  four-dimensional massless field" has no referent for the photon (l >= 1) or the graviton (l >= 2): a field of
  helicity s has no partial wave below l = |s|. This applies to the stored spin-1 result as well (its l = 0 Maxwell
  channel is empty: Y_00 has no gradient). Decision for Leon below.
- argued, with one exact step (frame dependence): "the potential vanishes at the horizon" is a statement in Killing
  null coordinates. With u = t - r_*, v = t + r_*, U = -e^{-kappa u}, V = e^{kappa v} (Kruskal), the channel equation
  4 d_u d_v Z + V_pot Z = 0 becomes d_U d_V Z = -(V_pot e^{-2 kappa r_*}/(4 kappa^2)) Z, and V_pot e^{-2 kappa r_*} =
  C(r) (V_pot/f) with C(2M) = 1/e (exactly f e^{-2 kappa r_*} = (2M/r) e^{-r/2M}), so in horizon-regular null
  coordinates the coupling at the horizon is -(4M^2/e)(V_pot/f)(2M) != 0 for integer spin: -(l(l+1)-3)/e for the
  odd graviton channel, -l(l+1)/e for the photon, -(l(l+1)+1)/e for the scalar. The decay rate e^{2 kappa r_*} is
  exactly the statement that the covariant coupling V_pot/f is regular at the horizon; it is not a decoupling seen by
  an infalling frame. What is frame independent: each channel is a field on the two-dimensional (t, r) quotient, and
  its characteristic data on a horizon generator are free whatever the potential. So "two-dimensional" is robust and
  "free at the horizon" is a Killing-frame statement, for spins 0, 1 and 2 alike (the stored result's clause (4) is
  correct as stated in (t, r_*); it should not be read as frame independent). The PG chart does not change the rate:
  f is the scalar Q(grad r) up to sign, so "V = f W" is chart independent; only the coordinate in which f is
  exponential (r_*) belongs to the static frame.
Proposal: none on T2 (offered to A). Next step: A to state "l >= 2, real frequency" on the intertwiner clause and the
Killing-frame scope on the horizon clause.

## T3 op.qft-structural-inputs, the generation number (counter-models)

Routes.
- R1 (the lead (a), capacity bound): 2 n_V + n_s + 2 eps <= 16 n_g; test against contents the store allows.
- R2 (the lead (b), Sakharov): N_V - N_W/4 = 0 at N_g = 3; test dependence on scalar content, on the Weyl count per
  generation (15 against 16), on the regulator and on which coefficient is required to vanish.
- R3 (own): independence in the two-model form: two contents satisfying every stored premise in the joint cone, with
  different n_g, each passing (or each failing) the candidate conditions; and a look-elsewhere count over the
  candidate rules.
Choice: R3, built from R1 and R2.
Kill condition (pre-registered): the independence statement dies if a stored premise (postulate or proved result, at
its current version) requires either (i) one array per massless helicity channel per light ray, or (ii) the vanishing
of the induced quadratic (Sakharov) coefficient. If (ii) is required by a stored premise and the weight is
N_V - N_W/4 with no scalar term, then n_g = 3 on 12 vectors is a theorem and I say so. What would count as failure of
the "three" readings: a store-allowed content with n_g != 3 passing every candidate rule that was fixed before the
count.

Outcome. Kill condition did not fire: no stored premise requires (i) one array per helicity channel or (ii) a
vanishing induced quadratic coefficient (read: J3 v2, helicity-lift joints v6, array-ln2 v5, the quasi-spin theorem,
the Sakharov cancellation v3, the quartet-regulator result v3, the induced-G result v2; find_text on "Sakharov" and
"induced Einstein-Hilbert" returns only those and the imported coefficients). The stored reading of the cancellation
is the opposite of a requirement: "the route supplies no G", and the stored matching clause needs B > 0.
Established:
- proved (exact, from the stored quasi-spin theorem): pair currents of the light-ray arrays (weights +-1/2) have
  helicity in {-1, 0, 1}; none has helicity +-2; helicity +-1 ones are nilpotent, not normal, not canonical; one
  array's current has helicity 0; n arrays carry at most n commuting canonical towers, all helicity 0. So lead (a)'s
  registration rule cannot be met for a vector or a graviton at ANY n_g; for scalars alone it reads 8 <= 16 n_g.
- computed: the inequality as arithmetic gives n_g >= 3 only at (n_V, n_s, eps) = (12, 8, 1): 34 against 32. The
  recorded content without a graviton gives 32 <= 32 at n_g = 2; one doublet with graviton 30 <= 32. The store has no
  graviton field. So the "3" sits two units above the n_g = 2 threshold and depends on counting eps = 1.
- computed: B = 16 n_g + 8(1 - 6 xi_R) + 12(alpha - 5) has a zero at every n_g = 1..5 in xi_R (-1/2, -1/6, 1/6, 1/2,
  5/6 at alpha = 1) and at n_g = 1, 2, 3 in alpha (11/3, 7/3, 1 at xi_R = 1/6); never with 15 components; with the
  graviton's two helicity-2 states by the stored s^2 rule the zero moves to n_g = 4; the quartic coefficient of the
  same sum vanishes on the recorded content at n_g = 1 (24 + 8 = 32).
- computed: the only conjunction giving 3 is recurrence (currents reading, 3 | n_g) with asymptotic freedom of weak
  isospin (n_g <= 5); the capacity inequality is redundant in it. Neither is a premise (Leon: recurrence is a test).
- look-elsewhere: of eleven rule variants (list fixed AFTER the leads were known, not exhaustive), two single out 3,
  two more contain it, seven exclude it; each of 1..5 is selected by some variant.
- argued: independence in the two-model form (n_g = 2 and 3 both satisfy the stored premises and either rule in a
  store-allowed form), on top of the stored independence from the slot-module premise and anomaly freedom.
Proposal: synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free (FILED, registered in proposals/).
Gate: runcheck 4/4; check4 exit 0, 0 errors, 0 other findings (draft folder and registered folder); validate_one ok,
no E/W codes (W215 fixed before filing); propose_claim accepted_for_review, info I213/I305 only; coverage.yaml copied.
What I could not establish: a theorem n_g = 3 from stored premises (there is none on these leads); that the list of
variants is complete; the partial-wave version of the capacity count (shells of fermions and bosons do not match).
Next step: if Leon wants a generation theorem, it needs a new premise; the candidates and their costs are below.

## Bridge leads (cross-pollination agent), status
- R1 (Sakharov with graviton gives n_g = 4): CONFIRMED by my own computation from the stored s^2 rule; used (clause
  (iv) of the filed claim).
- R2 (B = 16 n_g - 48 + N_S(1 - 6 xi_R)): CONFIRMED against the stored 12(alpha - 1) + 8(1 - 6 xi_R); used.
- R3 (no stored premise requires the zero): CONFIRMED by my own reading (above); used.
- R4 (the count 34 holds only for l >= 2): consistent with my T2 finding (no graviton channel at l = 0, 1); used only
  as a remark (the filed claim is per light ray; the partial-wave count is not filed).
- R5 (3 | n_g needs the number-current sector, broken by the Majorana premise): NOT TESTED (budget). Open lead.
- R7 (definite side: equivariant index): consistent with the stored k = e(L) on definite sides; not tested further.
- R8 (orders 2,2,4,4,8,8,16,16,32): agrees with the stored formula 2^{floor((n+1)/2)}; my point on injectivity stands.
- R10 (one superpotential; kernel at omega^2 < 0): CONFIRMED independently (work/B/t2.py); my kill (a) did not fire.
- R12 (Kasner helicity as boost weight against the helicity lift): NOT TESTED.

## A's routes: where they are exposed (read at 20:50; A's T2 proposal is in proposals/, T1 and T3 not yet written)
- T2, synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional. Cross-checks that PASS:
  A's superpotential, c = lam(lam+1)/(3M), kernel at d_t^2 = +c^2, and horizon values (L-3)/(4M^2) and
  (4 lam^2 + 4 lam + 3)/(4M^2 (2 lam + 3)) agree with my independent computation (27/7 at l = 2).
  Exposed: (1) clause (1), the linearised equations E_t, E_r, E_theta, is verified at TWO sample points in r, "not a
  symbolic identity": linear in the jets, but the r-dependence is a rational function and two points do not pin it;
  a referee should ask for more points than the degree, or an exact rational-function identity. (2) even parity is
  one-directional (span check at two points, L = 6 and 7/2); the converse is cited (C3), and the intertwiner does not
  supply it (it maps odd solutions to Zerilli solutions, not Zerilli solutions to metric perturbations). So "J3's
  channel clause for spin 2" is derived for odd parity and conditional on (C2), (C3) for even parity: the title and
  one-liner should not say more. (3) "obeys the free two-dimensional equation there" is a Killing-frame statement
  (my Kruskal note); (4) Q and Psi are used in the Regge-Wheeler gauge; their gauge invariance is cited through (C2).
  (5) omega != 0 and l >= 2 are stated: good; l = 1 (static kernel 3M/r, negative potential) is correctly excluded.
- T1: not yet written by A. The test is in my T1 audit: a derivation of the K input must give a LOWER bound on an
  order; checking that relations hold in a character ring discharges nothing.
- T3: not yet written by A. If A files a conditional theorem "n_g = 3 under capacity + ...", it is exposed to clauses
  (i) to (iii) of my filed claim.

## Unexpected links
- The quasi-spin theorem (photon pair modes) is an obstruction in the generation question: it is what makes the
  capacity rule unsatisfiable. Two subjects (null-plane photon data; generations) that shared no edge.
- The stored regulated sum has two coefficients with different verdicts on the same content: quadratic zero at
  n_g = 3, quartic zero at n_g = 1 (24 + 8 = 32 = 2 * 16). The quartic balance is also where the additive recurrence
  count c = 48 n_g is blind (stored). Nobody had put the "1" next to the "3".
- Spin pattern at the horizon: V/f at r = 2M is (l(l+1) + 1 - s^2)/(4M^2) for s = 0, 1, 2 (odd family); in Kruskal
  null coordinates the horizon coupling is -(l(l+1) + 1 - s^2)/e. The lowest radiative channel l = s gives s + 1:
  1, 2, 3 (argued pattern, three data points).
- The graviton has no channel below l = 2 and the photon none below l = 1, so "s-wave reduction of each massless
  field" (J3) names an empty set for both; the capacity count's 34 mixes l-ranges (bridge R4).
- T1: on the lens family the K-theoretic order is a function of the height of the half-Bockstein class a (2a = beta x);
  the stored q1 = 2a^2 is its first instance. A conjectural deciding datum: the heights/divided powers of a.

## Decisions for Leon
1. T3: do you want any generation rule adopted as a premise? Recommendation: no. Capacity: unsatisfiable in the exact
   sense, and as arithmetic it needs the graviton counted (not a store field). Sakharov zero: needs xi_R = 1/6 (open
   datum), the Feynman gauge, no graviton, and a reason to want B = 0 when the stored induced-G route needs B > 0.
   Recurrence + asymptotic freedom is the only conjunction giving 3, and you already ruled recurrence a test.
2. T3: record in op.qft-structural-inputs that the two leads of 9 November are closed negatively (if the filed claim
   is accepted), and that the quartic balance singles out n_g = 1 on the recorded content.
3. T2: wording of J3 v2. "s-wave reduction of each four-dimensional massless field" has no referent for helicity 1
   and 2 (channels start at l = |s|). Recommendation: restate as "lowest partial waves l >= |s|" or "each partial-wave
   channel"; a restatement of a postulate is yours to make.
4. T2: add to the stored spin-0, 1/2, 1 result (and A's spin-2 one) a scope sentence: the vanishing of the coupling
   at the horizon is in Killing null coordinates; in Kruskal coordinates it is -(4M^2/e) V/f at r = 2M, nonzero. If
   you want this as a stored result rather than a note, it is a small exact claim (I did not file it).
5. T1: sharpen the success clause of op.wall-class-invariant. "Not determined by W, beta x and the signature" is
   ambiguous: as numerical data (heights, orders) it is already refuted by the stored clause (4); as "the integral
   cohomology ring with x" no counterexample is in sight (every pair I built is separated by a power of a).
   Recommendation: restate the success clause as "k as a function of the ring data of a, 2a = beta x, or a pair of
   walls with isomorphic data (ring, x, a up to 2-torsion, signature) and different k".
6. T1: the K-ring hypothesis cannot be discharged by a relations-only computation. If A's derivation stops short of
   a lower bound, the remaining import is the collapse of the Atiyah-Hirzebruch spectral sequence (or Atiyah's
   Thom/Gysin computation): a new imported Fact, maintainer-only.
