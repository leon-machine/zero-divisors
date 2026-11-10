# attack-KA (cluster K, angle A constructive), run 2026-11-10-phase1

Status: pre-registration written before any computation. Kept current below.

## Orientation (direct lookups, done)
Read: pred.boundary-mode-density, scrambling.mode-count, singularity.c1/c2/c3, scrambling.residue-each-convention,
scrambling.epoch-modular-period-two-unknowns-become, scrambling.integer-holographic-form-identification,
singularity.stretched-singularity-count, scrambling.slice-volume-exactly-per-unit-killing,
scrambling.intrinsic-clock-ic-flagged-premise, synthesis.c-loc-local-horizon-premise,
synthesis.c-loc-is-a-second-placement-of-the-count, synthesis.cutoff-count-is-not-a-local-density-on-sds,
synthesis.kerr-ring-count-misses-area-law, synthesis.imported-kerr-surface-gravity-entropy,
interior.imported-kerr-schild-form-kerr-gauge, hawking.i-state-continuum, synthesis.de-sitter-mode-count,
op.kerr-ring, op.residue-killing-weights.
Already in the store (not to be refiled): (Loc) at the registered value gives A_+/4 on Kerr at every spin
(c-loc-is-a-second-placement (ii)), as a density statement with no volume count; the literal cutoff count fails
for a >= 2(2M)^{2/3} (ring regime); the small-spin regime of the literal count is declared "not treated".

## Routes
R-a (the problem's own): restate the Schwarzschild epoch count N = nu * V' * beta as horizon data and carry each
   algebraic form to Kerr. Delivers exact ratios in (M, a). Fails if the restatement is not unique (expected: it is not).
R-b (from another subject, the SdS result): compute the three-volume rate of Killing-invariant surfaces of the
   Kerr field exactly and ask which surface, if any, gives the area law over 2 pi / kappa_+; the stretched horizon at
   fixed proper distance is the candidate. Delivers a geometric (not definitional) horizon count. Fails if the density
   per unit horizon area depends on latitude or spin.
R-c (own): the literal (C1) count in the untreated small-spin regime (cutoff locus a closed spacelike surface
   between the horizons), to second order in the spin. Delivers the slow-rotation test RUN.md asks for on the
   stored placement itself. Fails if the integrand is not controlled.
Choice: R-b as the main line with R-a as its bookkeeping, R-c as the control computation. Reason: R-a alone is
dimensional matching; R-b is a volume count as the Schwarzschild one is; R-c tests the stored rule without reinterpretation.

## Pre-registered kill conditions (written before computing)
K1. Claim to test: the Schwarzschild count has a restatement in horizon data only. KILL: if the three stored forms of
    the rate (8 pi nu M; nu/T_H = nu * 2 pi / kappa; and area times surface gravity, 2 nu kappa A) give different
    counts on Kerr, then the Schwarzschild formula does not determine its own carry and K1 is answered "not unique";
    the horizon reading is then a choice, to be justified by a placement (R-b) and not by the formula.
K2. Claim to test: nu modes per Planck cell on the stretched horizon at fixed proper distance rho_0, counted over
    2 pi / kappa_+ of the co-rotating flow, gives A_+/4 with the SAME nu * rho_0 as Schwarzschild. KILL: if the
    count per unit horizon area depends on latitude, or on a/M at leading order in rho_0/r_+, or needs a
    spin-dependent rho_0 or nu. Slow rotation: KILL if the O(a^2/M^2) coefficient of N/(A_+/4) is nonzero.
    Control (R-c): the literal cutoff count at small spin. Pre-registered expectation: it mismatches, by a function of
    a/(2M)^{1/3} and not of a/M. KILL of that expectation: ratio equal to 1 through second order in a.
K3. Verdict rule fixed now: (a) if K2 survives AND the result follows from the definition of surface gravity alone
    (kappa cancels between rate and period on any Killing horizon), the test is declared a TAUTOLOGY: Kerr does not
    test pred.boundary-mode-density, whose kill condition is then neither met nor probed; (b) if K2 is killed, name
    the premise. The test counts as REAL only if some ingredient independent of the definition of kappa_+ and A_+
    (for example a latitude dependence, or the choice of Killing flow) could have failed and is checked.
    I-state: KILL of "superradiant channels fail" if the fermionic symbol (1 + e^{beta h})^{-1} is a valid symbol
    for every sign of h (then no channel of the horizon CAR algebra fails and the failure is elsewhere).
K4. Claim to test: the count rate carries the spin through Smarr, dN/dt = 16 pi nu T S = 8 pi nu (M - 2 Omega_H J).
    KILL: if the identity fails exactly at any rational (M, a), or if the rate needs J beyond this combination.
    Two-array unit: expectation (stored, argued) that it does not see the spin in the generator grid; KILL if the
    entropy per mode differs between h and -h.

## Results (current; status: attack round complete, one proposal filed)

Proposal filed: `synthesis.stretched-horizon-count-on-kerr-gives-the-area-law-at-every-spin`
(proposals/, check4 0 errors 0 findings, validate_one ok, runcheck 4/4 pass). Scratch: work/KA/.

### K1. What the Schwarzschild count counts (kill condition FIRED: the restatement is not unique)
- Stored count: N_epoch = nu * V' * Delta t, V' = 8 pi M (three-volume of the cutoff slice per unit Killing time),
  Delta t = beta = 8 pi M. Which step used what: V' uses (C1) (the slice) and (C2) (nu per cell) and the interior
  geometry; Delta t = 2 pi / kappa uses (IC) and the horizon only; N = A/4 then fixes nu = 1/16 pi. [read from store]
- In horizon data, on Schwarzschild 8 pi M = 2 pi / kappa = 2 kappa A = 4 pi r_+ = 16 pi T S: all equal. On Kerr
  they are different functions (proved, exact): over beta_+ at nu = 1/16 pi the count ratio N/(A_+/4) is
  M/s (rate 8 pi nu M), M r_+/(2 s^2) (rate nu/T_H), 1 (rate 2 nu kappa A), with s = sqrt(M^2 - a^2).
  So the stored formula does not determine its own carry; the stored wording "accrual rate nu/T_H" is a Schwarzschild
  coincidence (T S = M/2 = 1/(16 pi T) there). Premises: epoch theorem, stretched-singularity-count, Kerr Fact.
- A carry has to be justified by a placement. The geometric content of the Schwarzschild epoch count is
  nu * (thermal circumference beta |K| of the counted surface) * (its area) = nu * 4 pi A_H. [computed]

### K2. Carry to Kerr on chi = d_t + Omega_H d_phi (kill condition did NOT fire)
- Proved: on r = const the Gram determinant of (d_t + Omega d_phi, d_u, d_phi) is -Delta Sigma for every Omega, so
  V'(r) = 2 pi sqrt|Delta| * Int sqrt(r^2 + a^2 u^2) du for every Killing flow; the co-rotating flow enters only
  through the period. (Premise: Kerr-Schild Fact. Hand proof by the rank-one determinant rule; exact check.)
- Proved: rate per unit horizon area per unit proper distance from the locus -> kappa_+ at every latitude (zeroth
  law form), also kappa_- at the inner locus. Hence the stretched horizon at proper distance rho_0 sweeps
  kappa_+ rho_0 A_+ per unit time (leading order in rho_0/M at fixed a/M < 1) and the count per modular period is
  2 pi nu rho_0 A_+ = A_+/4 with the Schwarzschild value nu rho_0 = 1/8 pi (nu = 1/16 pi, rho_0 = 2). SAME nu, no
  spin-dependent input. Slow rotation: the O(a^2/M^2) coefficient is 0 (against 1/2 and 3/4 for the other two forms).
- Exact rate: 2 nu kappa_+ A_+ = 8 pi nu sqrt(M^2 - a^2). Exact criterion on r = const surfaces:
  N = A_+/4 iff sqrt|Delta(r)| I(r) = 4 s. Schwarzschild: r^3 |2M - r| = 4 M^2 has exactly three roots (M^2 > 64/27):
  near the cutoff radius and at proper distance 2 on either side of the horizon. (proved)
- Extremal limit: rate -> 0, period -> infinity, product -> 4 pi nu A_+ finite; at a = M no surface at finite proper
  distance along grad r and no modular period: the count exists only as a limit. (proved)
- Control (R-c), literal cutoff count at small spin: computed independently here (work/KA/explore.py): on the
  level set Sigma = rho^2 the Gram determinant is -(rho^2/r)^2 (r^2 + a^2(1-u^2) - 2 M r^3/rho^2), which equals
  KB's form -rho^2 [Delta + (1-u^2) a^4 u^2/r^2]; V' <= 8 pi M (1 - a^2/(12 rho_c^2)), so the literal count falls
  short at second order in a with coefficient 1/(12 (2M)^{2/3}), a function of a/(2M)^{1/3} and not of a/M
  (the area law needs 1/(2 M^2)). NOT FILED by me: sibling KB files this (KB-1); my computation agrees with it.

### K3. Verdict (pre-registered rule applied): (a), and it is a TAUTOLOGY
- The horizon reading reproduces A_+/4 identically. kappa_+ cancels between rate and period because
  |K| = kappa * (proper distance) is what surface gravity is, and the latitude independence is its constancy on the
  horizon. No (M, a) could have given anything else. The Kerr comparison does not probe pred.boundary-mode-density:
  its kill condition is neither met nor tested. The only thing that could have failed and was checked is the
  uniformity over latitude and the flow independence of V', and both are classical (zeroth law; shear invariance).
- Content left over: (1) the literal cutoff reading is wrong off Schwarzschild (stored for the ring regime, KB-1
  for small spin); (2) the forms 8 pi nu M and nu/T_H are wrong on Kerr; (3) (C1) as a horizon statement would
  read "(SH): the modes sit on the Killing-invariant surface at proper distance rho_0 from the horizon locus, nu per
  Planck cell, nu rho_0 = 1/(8 pi) (1/(8 pi ln 2) in the capacity convention)". Schwarzschild is unchanged at leading
  order (rate 8 pi M either way); the subleading terms differ (cutoff slice: factor sqrt(1 - r_c/2M), relative
  M^{-2/3}; stretched horizon: relative M^{-2}, argued). (SH) is the three-volume form of (Loc)'s constant density,
  eta = 2 pi nu rho_0; it adds no content to (Loc) beyond making it a count.
- Blame, for the literal reading's failure: (C1) (the placement), as the store already records; not (C2), (C3),
  the residue or (N+).
- Rotating I-state (argued, no proposal): hawking.i-state-continuum holds for every self-adjoint h and its symbol
  (1 + e^{beta h})^{-1} is bounded for either sign of h. With h the generator of the co-rotating flow on the
  horizon mode algebra (h = omega - m Omega_H in asymptotic labels) and beta = 2 pi / kappa_+, the theorem applies
  verbatim: no channel of the CAR algebra fails. Kill condition "superradiant channels fail" FIRED: they do not.
  Superradiant channels (0 < omega < m Omega_H, h < 0) have occupation above 1/2 (n(h) + n(-h) = 1), and the same
  entropy as their mirror (binary entropy is symmetric), so the count and the entropy do nothing with them. What
  fails is elsewhere: (1) the stored `known` sentence (no global KMS state at fixed angular velocity) is true for
  bosons, where the Bose factor is singular at h = 0 and negative below (Kay and Wald 1991, from memory), and for
  the state's extension to the whole exterior, where K is spacelike beyond the velocity-of-light surface (for
  fermions a Hartle-Hawking-like state exists but is regular only inside that surface: Casals, Dolan, Nolan,
  Ottewill and Winstanley 2013, from memory); (2) (R_loc) on Kerr is argued only, since Kerr is outside the scope
  of (N+). Not filed: it is the stored theorem with h renamed, and the scope of (N+) is Leon's decision.

### K4. Angular-momentum ledger (kill condition did NOT fire)
- Proved (clause (v) of the proposal): the area-form rate is 16 pi nu T_H S = 8 pi nu (M - 2 Omega_H J) by Smarr,
  equal to 8 pi nu sqrt(M^2 - a^2). So the rate per unit co-rotating Killing time carries the spin exactly through
  the Smarr heat term; the count per period carries it only through A_+.
- Two-array unit (argued): the unit entropy is blind to the sign of h (symmetric binary entropy; at the (Q) v3
  weights kappa(k + 1/2) in the generator grid nothing changes), so the unit does not see the spin, in agreement
  with the stored note of 1 November. A spinning-hole test of the unit would need the asymptotic-time grid and Kerr
  inside (N+).

### What failed / limits
- No independent test of nu was found. The constructive route delivers a consistency statement only.
- (iii) is leading order in rho_0/M at fixed a/M < 1; the error term is not uniform toward extremality in the
  proof as written (delta/M = O(rho_0^2/M^2) is uniform, but the proof states the limit at fixed a/M only).
- The proper distance is measured along the gradient lines of r; another definition of "distance from the horizon"
  agrees at leading order only.

## Overlap with sibling KB (for the duplicates pass)
- KB-1 (small-spin literal count): not filed by me; cited as an intended sibling in my extraction note.
- KB-2 (monomial carries, fitted slice): my clause (v) lists the three stored forms with their ratios and clause
  (vi) gives the exact r = const criterion; KB-2 generalises both. If KB-2 is accepted, (v) can be cut to the Smarr
  rate plus a citation, and the criterion in (vi) to a citation. The Smarr rate identity is a main clause of mine.

## Unexpected links
- kappa_+ A_+ = kappa_- A_- = 4 pi sqrt(M^2 - a^2): the inner horizon locus at the same proper distance carries the
  same rate, so a horizon-placed count cannot tell the two horizons apart by its rate; only the epoch does. Bears on
  op.kerr-ring's remark that the count should be placed before the Cauchy horizon.
- The Schwarzschild cutoff slice lies at proper time 2/3 (leading order) from the singular locus, and (C2') has
  nu' = (2/3) kappa_s: the 2/3 of synthesis.exceptional-boundary-measure-one-calibration is that proper time
  (computed here as Int_0^{r_c} sqrt(r/2M) dr = 2/3; not checked against that entity's proof).
- SdS: the stored result that the cutoff count over 2 pi / kappa_b gives u/(3u - 2) is the same phenomenon as the
  mass form on Kerr (M/s): a rate that is 8 pi M and not 2 kappa A. Under (SH) SdS would give A_b/4 too, for both
  horizons, again by cancellation (argued, not computed here).
- For the bridge-hunter: the count per period is nu times a Euclidean volume (thermal circle times area), the same
  geometry as the entanglement entropy of the Rindler wedge at a cutoff distance; the link to cluster E would be
  mode pairs across the horizon, not checked.

## Decisions for Leon
1. Whether to adopt (SH) as the restatement of (C1) away from Schwarzschild (a premise decision). Recommendation:
   do not adopt it as a new premise; record it as the three-volume form of (Loc), since it adds no testable content.
2. Whether the wording "the accrual rate is nu/T_H" (scrambling.mode-count, singularity.stretched-singularity-count,
   and "the singularity keeps the horizon's clock") should carry a scope note: on Kerr under the horizon placement the
   rate is 16 pi nu T_H S, proportional to T_H S, and nu/T_H overshoots by M r_+/(2 s^2). Recommendation: add the
   note in the maintainer pass.
3. Whether op.kerr-ring's `known` sentence on superradiance should say that it is a statement about bosons and about
   the exterior extension, and that the stored I-state theorem covers every channel of the fermionic horizon algebra
   for the co-rotating flow. Recommendation: yes, as an argued note; a filed claim would need Kerr inside (N+).
4. Whether Kerr is brought inside the scope of (N+) (needed before any rotating state statement is more than argued).
5. Literature cited from memory in the proposal's note ('t Hooft 1985 brick wall; Susskind, Thorlacius and Uglum
   1993) and here (Kay and Wald 1991; Casals et al. 2013; Unruh 1974 for fermion superradiance): import as Facts only
   if a filed result comes to rest on them; none does now.
