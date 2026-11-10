# attack-KB: cluster K (Kerr entropy test), angle B (adversarial, cross-pollinating)

Status: attack round COMPLETE. One proposal filed (KB-1). KB-2 withdrawn before filing (see below). Labels: proved / computed / argued / conjectured.

## Orientation (direct lookups, done)
What the store already holds, so it is not redone here:
- (C1), (C2), (IC) are already scoped "Schwarzschild calibration only" (Leon, 23 October); away from Schwarzschild the
  store's count is the horizon placement of (Loc) in synthesis.c-loc-local-horizon-premise.
- synthesis.c-loc-is-a-second-placement-of-the-count (ii) already states that the horizon hypothesis (H) at the
  registered value gives A_+/4 for Kerr at every spin. So "the horizon reading reproduces A_+/4" is stored, not new.
- synthesis.kerr-ring-count-misses-area-law covers the literal cutoff count only for a >= 2(2M)^{2/3}; it says of
  small spin "that regime is not treated here".
- op.residue-killing-weights `known` (1 November, argued): the angular-momentum ledger does not separate the unit
  readings in the generator grid.
- hawking.i-state-continuum is stated for every self-adjoint h and notes A_I is bounded even when h is unbounded
  below.
Parametrisation used throughout (exact, rational): t = a/r_+ in [0,1): M = r_+(1+t^2)/2, a = t r_+,
r_- = t^2 r_+, sqrt(M^2-a^2) = r_+(1-t^2)/2, kappa_+ = (1-t^2)/(2 r_+(1+t^2)), A_+ = 4 pi r_+^2 (1+t^2),
Omega_H = t/(r_+(1+t^2)), M Omega_H = t/2, J = aM.

## Kill conditions, pre-registered before computing (10 November)
- K1 (what the count counts). Claim to test: the Schwarzschild count N = 64 pi^2 nu M^2 does not determine its own
  restatement in horizon data; the forms the store writes (rate nu/T_H times modular period; rate 8 pi nu M times
  modular period; kappa_c A per modular period) are three different functions on Kerr. KILLED if two of them agree
  on Kerr identically, or if a stored premise in the cone of scrambling.mode-count selects one of them (then it is
  not an underdetermination).
- K2 (carry to Kerr). Claims to test: (a) the temperature form gives N/(A_+/4) = (1+t^2)/(1-t^2)^2 = 1 + (3/4)(a/M)^2
  + ..., the mass form (1+t^2)/(1-t^2), the area form 1; (b) the literal cutoff count at SMALL spin (a <= rho/2, the
  regime the stored ring result leaves out) has volume rate V'(a) <= V'(0)(1 - a^2/(12 rho^2)), so it falls short of
  the area law at the scale a ~ (2M)^{1/3}, not a ~ M. KILLED (a) if the exact rational identities fail at any
  sample hole; (b) if the Gram determinant of the level set |z| = rho is not -rho^2 [Delta(R) + (1-u^2) a^4 u^2/R^2],
  or if the bound chain needs a hypothesis I cannot state, or if the surface is not spacelike between the horizons
  in the stated regime.
- K3 (verdict). Pre-registered expectation: (a) tautology: the area form is defined from A and cannot fail on any
  horizon whose entropy is A/4. KILLED if a horizon reading built only from stored inputs (no A) is found that
  could have failed on Kerr and passes. Extremal limit: KILLED as a problem if the count per period has a finite
  limit equal to A/4 as kappa -> 0 (then the limit is harmless and only the point a = M is singular).
  Rotating I-state: claim to test: on the CAR algebra the KMS state for the co-rotating flow exists for all
  channels (Fermi symbol in [0,1] for every sign of the co-rotating frequency), so the stored `known` sentence about
  superradiance is a bosonic statement. KILLED if the stored I-state theorem needs h bounded below.
- K4 (angular-momentum ledger). Claim: the rate per unit co-rotating Killing time consistent with the area law is
  4 pi nu A T_H = 8 pi nu (M - 2 Omega_H J), the Smarr heat term; the count per period carries J only through A.
  KILLED if the identity fails at a rational hole.

## Routes considered
1. The problem's own (horizon modular data): restate N in (kappa, A, chi). Delivers the tautology verdict; needs
   nothing; fails to test anything (that is the finding).
2. From another subject (the cutoff-form theorem synthesis.c1-c2-forms-forced-one-number, and the SdS failure
   synthesis.cutoff-count-is-not-a-local-density-on-sds): treat Kerr like SdS, a one-parameter deformation on which
   the literal count is a function of the deformation; ask whether any spin-independent level set |z| = rho(M) of
   the curvature scale can carry the count. Delivers a no-go covering small spin. Needs the induced determinant.
3. My own: classify all monomial carries A^alpha kappa^-beta M^gamma and show exactly one passes; show a fitted
   slice always exists (so "restating C1" is unfalsifiable).
Chosen: 3 for K1/K3 (one proposal) and 2 for K2 (one proposal); 1 is recorded as findings because it is stored.

## NOTE TO SIBLING KA (written midway, after reading attack-KA.md)
To avoid filing the same result twice, KB is filing these two and nothing else unless stated below:
- KB-1 `synthesis.no-spin-independent-curvature-level-set-carries-the-count-to-slow-kerr`: the literal count in the
  untreated small-spin regime, for EVERY level set |z| = rho (not only rho_c), with exact two-sided bounds
  (1 - delta)(1 - eps/3) <= V'(a)/V'(0) <= 1 - eps/12, eps = a^2/rho^2 (this is KA's control route R-c in general
  form; KA please do not file R-c separately, cite this as an intended sibling).
- KB-2 `synthesis.schwarzschild-count-does-not-determine-its-carry-to-kerr`: the two-parameter family of monomial
  restatements A^alpha kappa^-beta M^gamma (all equal on Schwarzschild because A kappa^2 = pi there), exactly one of
  which reproduces A_+/4; a fitted slice r = R_* exists for every (M, a) by the intermediate value theorem; the
  inner-horizon count and N_+ N_- = 4 pi^2 J^2. KA's stretched-horizon proposal (kappa cancels at fixed proper
  distance) is left to KA; KB-2 does not state it. The Smarr rate identity 8 pi nu (M - 2 Omega_H J) appears in
  KB-2 only as one line of the rate clause; if KA files it as a main clause KB will drop it at the fix round.
KB's tests of KA's stretched-horizon route are in the section "Where KA is exposed" below.

(Superseded: KB-2 was NOT filed. KA's proposal, read after it was registered, already holds the three forms, the
Smarr rate, the tautology verdict, the extremal limit and the r = const criterion; a second entity would be a
duplicate. What KB-2 would have added is recorded below as findings.)

## Results

### Proposal filed
`synthesis.no-spin-independent-curvature-level-set-carries-the-count-to-slow-kerr` (proposals/; check4 0 errors
0 findings; validate_one ok; runcheck 4/4; registered with propose_claim; coverage.yaml copied back). Scratch and
source copy: work/KB/<same id>/, work/KB/explore.py (float cross-check of the bounds, not evidence).
Statement (proved, exact bounds; determinant identity proved in the text and sampled at 25 rational points):
for Kerr with rho <= M/3 and 0 < a <= 4 rho/5, the level set |z| = rho of the modulus of the curvature scale is a
closed spacelike surface between the horizon loci, det h = rho^2 [R(2M - R) - a^2 - (1 - u^2) a^4 u^2/R^2],
R = sqrt(rho^2 - a^2 u^2), and (1 - delta)(1 - eps/3) <= V'(a)/V'(0) <= 1 - eps/12 with eps = a^2/rho^2,
delta = (5/2) a^2/(rho(2M - rho)). Hence Q(a)/Q(0) <= (1 - eps/12)/sqrt(1 - a^2/M^2) < 1 for every density: no
spin-independent (nu, rho(M)) of this kind meets the area law at zero and nonzero spin. The count sees the spin on
the scale a ~ rho ((2M)^{1/3} for (C1)); the area law on the scale a ~ M. Kill condition K2(b) did not fire.
Limits, stated in the entity: modulus level sets only (a criterion using the phase of the complex scale, such as
Kretschmann, is not covered, and one tuned function of the phase could in principle cancel the leading deficit:
that would be fitting a function with a function); the window 4 rho_c/5 < a < 2 rho_c^2 is untreated; the deficit
in the proved regime is small (at most a few per cent: G(16/25) is about 0.94), it is its non-vanishing as
M -> infinity at fixed a/rho that carries the conclusion; the comparison is of Q(a)/Q(0) because Q(0) = 1 only at
leading order. Transport-absent.

### K1 (what the count counts): kill condition did not fire; underdetermination established (proved, elementary)
On Schwarzschild A kappa^2 = pi and 4 kappa M = 1, so every N_{p,q} = 4 pi nu A (A/16 pi M^2)^p (4 kappa M)^q equals
the stored 64 pi^2 nu M^2. On Kerr, with t = a/r_+: A/16 pi M^2 = 1/(1 + t^2), 4 kappa M = 1 - t^2, so
N_{p,q}/(4 pi nu A_+) = (1 + t^2)^{-p} (1 - t^2)^q, identically 1 only for p = q = 0 (let t -> 1, then compare any
t). The three stored wordings are (p,q) = (-1,-2) (rate nu/T_H), (-1,-1) (rate 8 pi nu M), (0,0) (kappa_c A per
period). Exact check: work/KB/horizon_forms.py (five rational holes). More generally every dimensionless horizon
datum of Kerr is a function of t alone, so Schwarzschild fixes only F(0) = 1 of a carry N = 4 pi nu A F(t) and the
Kerr entropy is what fixes F = 1. KA's proposal, clause (v), files the three forms; this generalisation is not
filed. Which step used (C1): only V' = 8 pi M (the slice); the epoch 2 pi/kappa used (IC) and the horizon; no
stored premise selects among the forms (argued: read in the cone of scrambling.mode-count, not audited over the
full joint cone).

### K2 (carry): values agree with KA to the last digit (computed independently)
Temperature form (1 + t^2)/(1 - t^2)^2 = M r_+/(2 s^2) = 1 + (3/4)(a/M)^2 + ...; mass form (1 + t^2)/(1 - t^2) =
M/s = 1 + (1/2)(a/M)^2 + ...; area form 1. Kill condition K2(a) did not fire.

### K3 (verdict): (a), tautology; pre-registered kill condition did not fire
- No horizon reading built from stored inputs without A was found. The surviving reading passes in Minkowski
  space on a Rindler horizon (rate a rho_0 A per unit boost time, period 2 pi/a, count 2 pi nu rho_0 A): it uses
  nothing about the hole, so Kerr cannot test it. It also passes on the Kerr inner horizon (A_-/4 over its own
  period), on both SdS horizons and on de Sitter (stored), that is, also where the literal count fails.
- What the Kerr comparison does discriminate (this is its whole content): (1) it removes the two other stored
  wordings of the rate; (2) with KB-1 and the stored ring result, it removes the class of placements that the
  form theorem synthesis.c1-c2-forms-forced-one-number singles out on Schwarzschild (an algebraic, mass-independent
  curvature criterion read on the modulus of the scale): the stretched horizon at fixed proper distance is not in
  that class (the curvature there is of order 1/M^2, mass dependent), so "the form of (C1) is forced" holds on
  Schwarzschild only as a statement about a class Kerr rejects; (3) it does not touch nu, the residue, (IC) as a
  premise, or pred.boundary-mode-density, whose kill condition is neither met nor probed.
- A fitted slice always exists (proved, elementary; exact inputs checked in horizon_forms.py): V'(r) =
  2 pi sqrt(-Delta) Int sqrt(r^2 + a^2 u^2) du is continuous on [r_-, M], zero at r_-, and at least
  4 pi s M >= 8 pi s at r = M when M >= 2. So a spin-dependent restatement of (C1) reproducing A_+/4 exists for
  every hole, and finding one is no evidence.
- Extremal limit: harmless as a limit (rate 8 pi nu s -> 0, period -> infinity, product 4 pi nu A_+ finite), as KA
  files. The per-unit entropy does not move either: the array weights are kappa(k + 1/2), so beta omega =
  2 pi (k + 1/2) for every kappa > 0 and an array carries (1/2) ln 2 at every spin. At a = M itself there is no
  period and all weights are zero: the rule is undefined there and cannot decide between A/4 and 0 for an extremal
  hole (both are in the literature: string counting against Hawking, Horowitz and Ross 1995; from memory).
- Rotating I-state (argued; same conclusion as KA, reached independently): hawking.i-state-continuum is stated
  for every self-adjoint h and notes its symbol is bounded when h is unbounded below, so my kill condition ("the
  stored theorem needs h bounded below") did not fire: no channel of the fermionic horizon algebra fails for the
  co-rotating generator. The store already half-says this: synthesis.imported-kay-wald-uniqueness-and-no-go (b)
  records that the Kerr no-go is for the Klein-Gordon field and "may not extend to Dirac fields". The `known`
  text of op.kerr-ring ("superradiance leaves no global KMS state") therefore states a bosonic, exterior fact
  next to a fermionic, horizon-local mode algebra without saying so.

### K4 (ledger): kill condition did not fire
2 nu kappa_+ A_+ = 8 pi nu (M - 2 Omega_H J) exactly (KA files it). Added here (proved, exact, not filed):
A_+ A_- = (8 pi J)^2 and kappa_+ A_+ = kappa_- A_-, so the two horizon counts of a horizon reading satisfy
N_+ N_- = 4 pi^2 J^2 at nu = 1/16 pi: the product is the spin alone (classical: the area product; Ansorg and
Hennig, Cvetic, Gibbons and Pope, from memory). Omega_H/kappa_+ = 2t/(1 - t^2): a generator winds by that many
turns of phi, times 2 pi, per modular period; nothing in the store uses it. Two-array unit: blind to the spin in
the generator grid (stored, argued; the entropy is even in h).

## Where KA is exposed (tests of attack-KA.md and of KA's proposal)
1. Title against content. "Stretched-horizon count on Kerr gives the area law at every spin" reads as a passed
   test; clause (iv) of the same entity says it cannot fail. The title and one-liner should carry "by the
   definition of surface gravity; no test of the density". (Referee W503 risk.)
2. (SH) is not the carry of the stored count, it is another rule that agrees with it at one point. On
   Schwarzschild the cutoff slice is at proper time 2/3 from the singular locus and the stretched horizon at proper
   distance 2 from the horizon; both give 8 pi M because the rate per unit proper distance is 12 pi M at the
   singular locus (the stored Kasner measure mu_E) and kappa A = 4 pi M at the horizon, and 12 * (2/3) = 4 * 2.
   The coincidence is mu_E = 3 kappa A, true on Schwarzschild only (on SdS mu_E/(3 kappa_b A_b) = u/(3u - 2), the
   stored factor). KA says "same count at leading order" (vi); it should not be read as continuity of placement.
3. Inner locus. Clause (vi) (same leading rate at proper distance rho_0 from r_-) holds at fixed a/M as M grows.
   It is not uniform as a -> 0: there the surface at proper distance 2 from r_- tends to the Schwarzschild slice
   at proper time 2 from the singular locus, whose rate is 24 pi M, three times the cutoff slice's. So an
   interior placement by proper distance cannot be both the Schwarzschild cutoff slice (2/3) and the stretched
   inner horizon (2); only the outer placement has a spin-independent distance. (argued from the two leading
   rates; not bounded)
4. Uniformity toward extremality: KA flags it. My estimate: the correction factor is sinh(y)/y with
   y = rho_0/sqrt(Sigma_+), which does not involve r_+ - r_-, so the leading-order statement should be uniform in
   a/M < 1 (argued, treating Sigma as constant along the short radial segment).
5. "Same nu": only the product nu rho_0 enters, so on the horizon placement the registered density
   nu = 1/(16 pi ln 2) of pred.boundary-mode-density has no separate meaning; what survives is the residue
   kappa_c. KA says this; the proposal's phrase "with the SAME nu" should not outlive it.
6. Numbers: every exact value in KA's clauses (v), (vi) that I recomputed agrees (three forms, Smarr rate,
   kappa_- A_- = kappa_+ A_+, the three Schwarzschild roots and the bound r_c < root < r_c + 1/r_c for r_c >= 2).
   I found no error.

## Unexpected links
1. (Entropy, thermality, residue; computed, floats in work/KB/window_entropy.py, classical integral.) The adopted
   window reading (synthesis.window-reading-array-killing-energy) reads an array as one chiral complex component
   of the light-ray continuum over one window 2 pi/kappa, and for the ENERGY the two agree exactly (-kappa/24 at
   offset 1/2). For the ENTROPY they do not: the array carries (1/2) ln 2 = 0.34657 (stored), the continuum I-state
   over one window carries (1/(kappa beta)) Int s(x) dx = (1/2 pi)(pi^2/3) = pi/6 = 0.52360 (extensive part), a
   ratio pi/(3 ln 2) = 1.5108, independent of kappa and so of spin. If the window reading were applied to entropy as
   it is to energy, a two-component unit would carry pi/3 > ln 2 and the area law would ask for 3/(4 pi) units per
   Planck area per period in place of 1/(4 ln 2). I did not find this comparison in the store by text search
   (not an audit). It bears on op.residue-killing-weights and on the kill condition of pred.boundary-mode-density
   far more than Kerr does.
2. The stored SdS factor and the Kerr mass form are one formula: N/(A/4) = M/(2 T S) on both families (SdS:
   M/(kappa_b r_b^2); Kerr: M/s), and M = 2TS + work terms (2 Omega_H J on Kerr; the Lambda term Lambda r_b^3/3 on
   SdS, exact check in window_entropy.py). The literal count measures the mass (mu_E = 12 pi M does not see Lambda,
   stored); the entropy rate is the Smarr heat term. They agree exactly when Smarr has no work term. (KA notes the
   same link, argued.)
3. For the bridge-hunter: rational Kerr holes (M, a, sqrt(M^2 - a^2) all rational) are the rational points of the
   circle, a/M = 2t/(1 + t^2), s/M = (1 - t^2)/(1 + t^2), with t = a/r_+ = 2 M Omega_H the half-angle parameter,
   and Omega_H/kappa_+ = 2t/(1 - t^2) is the tangent of the same angle: the rational rotors of the plane that
   cluster E uses for E2. Every horizon datum is rational in (r_+, t). A parametrisation, not a result.
4. The Kerr no-go for bosons and the fermionic I-state: the store's boundary modes being CAR modes is what keeps
   a rotating state statement possible at all; with bosonic boundary modes the superradiant channels would have
   no thermal symbol.

## Decisions for Leon
1. Scope of the form theorem. synthesis.c1-c2-forms-forced-one-number says the forms of (C1), (C2) are forced; with
   KB-1 and the ring result the forced class (modulus level sets) fails on Kerr at both ends of the spin range, and
   the surviving horizon placement is outside the class. Recommendation: a scope note on that theorem and on (C1)
   (maintainer pass), no change of premise.
2. Whether to treat the window reading's entropy (link 1) as a problem to attack next: either a reason why the
   array's (1/2) ln 2 and not the continuum's pi/6 is the entropy of a window, or an entry under the refutation
   conditions of the window reading. Recommendation: put it on op.residue-killing-weights as an attack item; it is
   the one place found in this cluster where the registered residue could meet a real test.
3. KA's (SH): I agree with KA's own recommendation not to adopt it as a premise. If it is recorded, record it as
   the three-volume form of (Loc), with the title fixed as in exposure 1.
4. Wording of "the accrual rate is nu/T_H" and "the singularity keeps the horizon's clock" (scrambling.mode-count,
   singularity.stretched-singularity-count): on Kerr under the area law the rate is 4 pi nu A T_H, proportional to
   T_H at fixed area, and nu/T_H overshoots by M r_+/(2 s^2). Recommendation: scope note (same as KA's item 2).
5. op.kerr-ring `known`: qualify the superradiance sentence (bosons, exterior extension), pointing to the Dirac
   remark already in the Kay-Wald Fact; and decide whether Kerr enters the scope of (N+). Until it does, every
   rotating state statement stays argued.
6. Literature cited from memory in this file (Hawking, Horowitz and Ross 1995; the area-product papers): none is
   used by the filed proposal; import only if a later result rests on them.
