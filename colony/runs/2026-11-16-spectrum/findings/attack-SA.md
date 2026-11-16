# Attack SA (constructive): op.descent-state-and-spectrum, run 2026-11-16-spectrum

Status: attack round complete. Two proposals filed (check4 exit 0, 0 findings each; validate_draft ok). The
kill conditions below were written before any computation (first version of this file).

## Pre-registered kill conditions (written first)

K1 (seed S1, the slicing gap). The claim to be tested: on the descent slice the linearised energy constraint of
   the gravitational gauge fields leaves one scalar function free, so that the map from the deposit's density
   contrast to the curvature perturbation zeta is not fixed by the deposit; the flat-slice reading (zeta = delta/4
   for radiation, the reading of the stored quasi-free clause (iv)) and the uniform-expansion reading
   (zeta = (3/2)(a_d H_d/k)^2 delta at leading order) are both solutions of the constraints.
   KILL-1a: a stored premise or proved result forces the flat-slice reading (B) (or forces any one reading).
            Then the dichotomy is not new; record which premise does it and whether the stored statements cite it.
   KILL-1b: the constraint identity fails when derived from the stored field equation G(a) + Lambda a = -8 pi T(a)
            on a perturbed flat Robertson-Walker h-field, in exact arithmetic (coefficient 3/2, power (aH/k)^2, the
            relation zeta = delta/(3(1+w)) - psi). Any coefficient that differs is reported as found.
   KILL-1c: the uniform-expansion datum is not a solution with constant zeta outside the Hubble length (if the
            white contrast under (A) is a pure decaying mode, the enhancement is void). Test: solve the linearised
            equations for the radiation field exactly as a power series in k*eta and read zeta at late times from
            data given at the descent.
K2 (seed S2, structure factor). The claim: a pure gauge-invariant quasi-free state with occupation the indicator
   of a ball has number structure factor S(k) = 3k/(4 k_F) - k^3/(16 k_F^3) for k <= 2 k_F, and its ENERGY
   structure factor also vanishes linearly at k = 0.
   KILL-2a: the energy structure factor of a pure gauge-invariant deposit does not vanish linearly at k = 0
            (a constant term, or a different leading power). This kills the index-0 row.
   KILL-2b: the amplitude under (A) at any Fermi momentum inside the stored window is within a factor 10^3 of A_s
            at the pivot. (Pre-registered as a check against over-reading: the seed says it is far short; if it
            is not, the row becomes a fit with k_F as its parameter and is reported as such.)
   KILL-2c: the store's deposit (the I-state, occupations conserved, entropy conserved, the charge reading) does
            not admit a pure deposit carrying the density. Then the index-0 row is recorded as a statement about a
            deposit the store excludes, and the stored deposit's row is the mixed one (index -1 under (A)).
K3 (own route, see R4 below). Pre-registered before computing: "the local density parameter of the descent slice".
   Claim: the free function of K1 is exactly the first-order local density parameter Omega_Sigma - 1 =
   delta - 2 delta_H, so reading (B) is local criticality of the slice and (A) is a uniform Hubble rate.
   KILL-3: the slice's intrinsic curvature is not 6 H^2 (Omega_Sigma - 1) at first order in exact arithmetic.
Index rule (Leon, 10 November): n_s = 1 exactly is a miss at about 8 sigma and is reported as a miss; nothing is
tuned to the measured tilt; a one-parameter family that reaches the window is a fit with its parameter named.

## Routes
R1 (the seed's own, S1). Linearised constraints of the gauge fields on a slice of a perturbed flat Robertson-Walker
   h-field. Delivers: an identity among zeta, the slice's density contrast and the slice's expansion perturbation;
   the two pure readings as its two special cases; the index ledger under (A). Needs: the stored field equation
   only (transport-absent). Fails if a stored premise selects a reading (KILL-1a).
R2 (from another subject). The regular-initial-surface results (radical-normal tame wall, the Weyl-flat collar
   and Hadamard premises, Tod's isotropic singularities cited from memory): a regular beginning admits only the
   growing mode, with the conformal 3-geometry as free datum and the rest-frame contrast slaved (compensated).
   Delivers: a candidate selector of (B)-type data. Needs: a stored statement that the descent slice is such a
   surface for the perturbed field. Fails if the stored results are background statements only.
R3 (the seed's S2). Exact structure factor of pure gauge-invariant quasi-free states from the stored variance
   formula Var = Tr(f E f (1 - E)); the lens volume for a ball; the energy-weighted version. Delivers the
   hyperuniform row (index 0 under (A)), its amplitude, its running. Fails on KILL-2a.
R4 (my own, from the graph). The stored separate-universe proof of the time-shift result takes the slice flat
   "in the separate-universe gauge"; the stored dating has a flat descended phase. Read the constraint's free
   function as the local density parameter and ask whether the series' own flatness (if it has a reason for the
   background's Omega = 1) extends region by region. Delivers: a named hypothesis ("local criticality") that is
   the exact content of reading (B), and a test of whether the store's reason for flatness is local.
R5 (my own, from the graph; secondary). The stored area-law reading (problem clause (vii)) imports an area-law
   heat capacity from string-gas cosmology. A pure Fermi sea has an area law with a logarithm for its number
   variance from the CAR algebra alone. Delivers: the stored index-0 row of (vii) re-derived from the store's own
   algebra under (A), with its amplitude. Subsumed in R3 if R3 survives.

Choice: R1 with R4 as its sharpened statement (one proposal), then R3 (second proposal). R2 is run as the test of
KILL-1a, not as a proposal.

## Work log

### Orientation (lookups, no computation)
- Stored conversions in use: the finite-range result is stated for zeta itself on "the comoving slice of the
  descent"; the quasi-free clause (iv) bounds the contrast of the modes' energy and then calls it "the deposit's
  spectrum", index 3; the time-shift result takes the slice "flat (psi = 0) in the separate-universe gauge" inside
  its proof; the holographic result uses the imported Poisson conversion P_Phi = 8 G^2 k^-4 <delta rho^2> and
  records "an extensive capacity gives -1". So the store already holds both conversions, in different entities,
  for the same white energy noise (index 3 in one, -1 in the other). The gap is real at the level of the texts.
- Search for a selector (KILL-1a): patterns "separate universe", "uniform time", "simultaneous", "descent slice",
  "spatially flat", "flatness", "junction", "Weyl-flat", "energy/momentum/Hamiltonian constraint", "Poisson"
  over store/claims/*/entity.md, and reading of the dating, the Hadamard premise (HD), the radical-normal tame
  wall, the time-shift result, P1. Found: (HD) and the tame-wall result are statements about the background
  collar (Weyl-flat, conformal vacuum admissible) and fix no first-order datum of the slice; the dating takes the
  record's flat Robertson-Walker field; no entity gives a reason for spatial flatness of the descended field, of
  the whole or of a patch. KILL-1a NOT triggered (argued: a pattern search with reading, not a cone audit).

### Computed so far (scripts in work/SA/: pert0-5.py, lune.py; draft check in work/SA/p1/check.py, all pass)
- KILL-1b not triggered. The lab's GTG engine (lib/gtg.py, Omega solved from the torsion equation, exact jets
  with the perturbation parameter as an extra jet label) gives, for hb^-1(e_0) = a(1 + phi cos)e_0,
  hb^-1(e_1) = a(1 - psi cos)e_1 + a b sin e_0, hb^-1(e_j) = a(1 - psi cos)e_j:
    n.G(n) first order = (2/a^2)(k^2 psi + 3 Hc(psi' + Hc phi) - Hc k b) cos,
    m_1.G(n) = (2/a^2) k (psi' + Hc phi) sin,  theta = 3Hc/a + (-3(psi' + Hc phi) + k b) cos/a,
    3R(slice) = -4 (k/a)^2 psi cos, and the Gauss relation 3R + (2/3) theta^2 + 2 n.G(n) = 0 to first order.
  Hence (k/a)^2 psi = H kappa - (3/2) H^2 delta and 3R = 6 H^2 (delta - 2 delta_H): KILL-3 not triggered; the free
  function is the first-order local density parameter of the slice.
- KILL-1c not triggered, and the seed is UNDER-stated (same finding as SB's O1, reached independently): the
  growing-mode amplitude in the radiation era is, exactly,
    zeta_inf = -[R (cos x + x sin x) + (delta_c/4) cos x],  x = k/(sqrt3 a_d H_d),
    R = psi + u, delta_c = delta + 4u, u = (a_d H_d/k) v (v the matter's longitudinal velocity on the slice),
  so zeta_inf = (3/2)(aH/k)^2 (delta - 2 delta_H) - delta/4 - 2u + higher orders. Three data, three powers of
  aH/k. A white deposit reads: index -1 (uniform expansion), +1 (flat slice, thermal momentum noise), +3 (flat
  slice and matter at rest on it: the stored reading). The decaying solution has R = cos x/(2x) exactly.
- Thermal deposit under uniform expansion: Delta^2(k) = (135/(pi^4 g))(H/T)^3 (a_d H_d/k) confirmed; at the pivot
  it is (g^(2/3) g_s0^(1/3)/60)(T_d/M_P)^4 (a_0 T_0/k_*) (pi drops out): 3.5e-12 at the window ceiling 7.3e8 GeV
  (590 to 610 below A_s at the pivot, but 0.37 A_s at k = a_0 H_0 since the index is -1), A_s at 3.6 to 3.7e9 GeV,
  12.4 at 1e12 GeV (not a perturbation).

### Midway reading of attack-SB.md (their objections, and what was done with each)
- O1 (the conversion needs both matter data and one geometric datum; momentum term with coefficient 2): accepted
  in full; I had reached the same map independently before reading (work log above). It is in the filed theorem
  as clause (iii), in closed form, with the momentum term in the ledger (v) and in the thermal numbers (vi).
- O2 (index -1 is not admissible on an unbounded slice): accepted. Clause (v) states that under uniform expansion
  a white contrast is a perturbation only on a band with an infrared end; clause (vi) gives the end at the
  window's ceiling (beyond 1.2e9 present Hubble radii). I do not file the resulting bound on T_d (SB's).
- O3 (flatness patch by patch): the same as my route R4; in the theorem as the local density parameter.
- O4 / their 3.5 (the stored deposit is not pure; pairs have white energy noise and no momentum noise): agreed and
  sharpened in my second proposal: for one Weyl field the white term is p^2 (mixedness)/2 + |p ^ mu|^2, pairs
  being the second term; a purification by partners removes it only if partners are degenerate with their modes,
  at an energy cost of at least int w (1 - n), infinite for Fermi-Dirac occupations.
- Names: my (UE) is SB's (UE). My (LC) is "flat slice" alone; SB's (FR) in their restated quasi-free entity is
  (LC) plus the deposit at rest, and their (FM) is (LC) with thermal momentum noise. The orchestrator may want one
  set of letters across the three proposals; the statements agree.
- Not filed by me because SB filed it: the restated quasi-free entity (version 5). My suggested wording for its
  clause (iv) is below under Decisions; SB's note covers the same ground and the numbers agree
  (their "more than twenty times A_s at 1e10 GeV for f >= 1/2" against my 59 A_s for the whole bath).

## What was established (labels)

P1 `synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit`  (check4: 0 errors, 0 findings)
 1. PROVED (computed exactly with the lab's GTG engine at generic rational jets; sampled, not symbolic): on a slice
    of a first-order scalar perturbation of the flat Robertson-Walker h-field, the field equation contracted with
    the slice normal gives (k/a)^2 psi = H kappa - (3/2) H^2 delta; the slice's scalar curvature is
    6 H^2 (delta - 2 delta_H), its first-order local density parameter; Omega to first order is displayed (its
    spatial part carries k Psi). KILL-1b and KILL-3 not triggered.
 2. PROVED: R = psi + u, zeta = -psi + delta/(3(1+w)), delta_c = delta + 3(1+w)u, Psi = psi - Hc b/k are slice
    independent (generic w), and k^2 Psi = -(3/2) Hc^2 delta_c on every slice.
 3. PROVED (radiation field, perfect fluid; exact series to x^18): zeta_inf = -[R (cos x + x sin x) + (delta_c/4) cos x],
    x = k/(sqrt3 a_d H_d); the decaying solution has R = cos x/(2x). So outside the Hubble length
    zeta_inf = (3/2)(a_d H_d/k)^2 (Omega_Sigma - 1) - delta/4 - 2 (a_d H_d/k) v. KILL-1c not triggered.
 4. PROVED: readings (UE) uniform expansion, (LC) local criticality (flat slice), (LC) at rest; a mixed slice is of
    the first kind below k ~ a_d H_d sqrt(6|lambda|). Index ledger -1 / +1 / +3 for a white deposit.
 5. COMPUTED: thermal deposit under (UE): Delta^2(k) = (135/(pi^4 g))(H/T)^3 (a_d H_d/k); at the pivot
    (g^(2/3) g_s0^(1/3)/60)(T_d/M_P)^4 a_0 T_0/k_*: 2 to 3e-60 at 1 MeV, 3.4 to 3.6e-12 at 7.3e8 GeV (0.36 to 0.39
    A_s at k = a_0 H_0), A_s between 3.6 and 3.7e9 GeV, 12 to 13 at 1e12 GeV. Under (LC): index +1, below 4e-41.
 6. ARGUED: where the stored results stand (the finite-range bound is about zeta and stands; the quasi-free clause
    (iv) and the time-shift result's flat slice are (LC) with matter at rest; the thermal reading with a heat
    capacity is (UE)); no stored premise fixes delta_H (pattern search with reading); free quanta change only the
    order-one coefficient.
 Classification: transport-absent.

P2 `synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary`  (check4: 0 errors, 0 findings)
 1. PROVED: for a homogeneous gauge-invariant quasi-free state S_E(0) = int tr[H E H (1 - E)], zero exactly for
    pure stationary states (up to zero modes of H); the momentum term vanishes exactly for pure states.
 2. PROVED (in Cl(3,0), checked with GA.py): for one Weyl field, E_p = (nu + mu)/2,
    tr[p E p (1 - E)] = p^2 (nu(2 - nu) - mu^2)/2 + |p ^ mu|^2: mixedness plus a squared bivector. Three classes:
    mixed stationary (2 p^2 n(1-n), with momentum noise), pure pairs (4 p^2 n(1-n), no momentum noise), pure
    stationary (neither).
 3. PROVED (exact bipolar integrals): filled ball, excess over the vacuum
    (k_F^4 k/(8 pi^2))(1 - kappa^3/30 + kappa^4/96) for k <= k_F; contrast (4/g) kappa^4 (...). KILL-2a not
    triggered: the energy structure factor vanishes linearly. The seed's number formula 3k/4 - k^3/16 is confirmed
    for trivial overlap; with the Weyl overlap the number lune is 3k/4 - 5k^3/32.
 4. PROVED under the stated Hypothesis (C) (zeta = gamma (a_d H_d/k)^2 delta): index s - 1; filled ball n_s = 1
    with correction -kappa^3/10: a MISS, 8.3 to 8.4 standard deviations. Amplitude gamma^2 H_d^2/(6 pi^2 M_P^2),
    3 H_d^2/(8 pi^2 M_P^2) at gamma = 3/2, independent of g and k_F: 3.5 to 3.7e-39 at the ceiling's density,
    1.2 to 1.3e-26 at 1e12 GeV; A_s at rho^(1/4) = 4.9 to 5.0e16 GeV. KILL-2b not triggered (short by > 1e17).
 5. COMPUTED (in the proof text): thermal sea S_E = S_E(T=0) F(k/T), F = 2 int_0^1 mu coth(y mu/2): white below
    k ~ 4aT; measured tilt at k/aT in (19.1, 19.3) with running t(2 - t) = +0.069 (a fit of one number; the
    two-term model S(0) + ck gives +0.034).
 6. ARGUED: KILL-2c IS triggered. Under (L_E) occupations and hence the entropy are conserved; the stored
    deposit has k_*/(a_d T_d) < 2e-26, twenty-seven orders inside the white regime; a purification by partners
    does not help unless the partners are degenerate with the modes and carry at least int w (1 - n). So the
    scale-invariant row is about a deposit the stored state rules exclude, and the stored deposit's row under
    (C) is index -1.
 Classification: transport-absent (the Clifford algebra is the language of the Weyl one-particle space).

## What was killed (plainly)
- Seed S1, "(A) = uniform Hubble rate, matter at rest, no shear": the last two are not hypotheses; kappa = 0 alone
  gives the (a_d H_d/k)^2 term, and the momentum term is down by k/(a_d H_d).
- Seed S1, "(B): zeta ~ delta/4, index 3": true only with no longitudinal momentum noise. For a thermal deposit
  on a flat slice the index is +1 and the amplitude is (3/4)(a_d H_d/k)^2 above the stored reading.
- Seed S2, "corrections of relative order (k/k_F)^2": for the energy of a Weyl sea they are kappa^3/30 (Pauli
  blocking of vacuum pairs) and kappa^4; the kappa^2 term belongs to the number factor with trivial overlap.
- Seed S2, amplitude (9g/16 pi^2)(k_F/M_P)^4: that used the number structure factor. With the energy factor it is
  (g/pi^2)(k_F/M_P)^4 (unreduced mass) = 3 H_d^2/(8 pi^2 M_P^2) (reduced), 16/9 larger. Still far short.
- Seed S2, running +0.034 at the measured tilt: that is the two-term model. The thermal sea gives +0.069. Either
  is far from the Planck running as I remember it (-0.0045 +- 0.0067; not a stored Fact; flagged).
- The scale-invariant row as a candidate: a miss on the index (8.4 sigma), on the amplitude (> 1e17), and on the
  state (the stored deposit has entropy). Reported as a miss. Nothing was tuned.
- My own lead (R5), the area law: the number variance of the sea in a sharp ball goes as R^2 ln R. Read through
  the string-gas rule "variance at R = 1/k" it would give a logarithmic red tilt -1/ln(k_F a_d/k), about -0.016
  at the pivot. That is an artefact of the sharp window: the constraint converts Fourier modes and the spectrum
  has no logarithm. Killed (argued; and -0.016 would itself be 4.5 sigma off).
- A third proposal: not filed. The correction of the stored quasi-free clause is SB's (filed).

## Routes, as they ended
R1 chosen and filed (P1). R2 (regular initial surface) run as the test of KILL-1a: the stored tame-wall and (HD)
statements are background statements; Tod's theorem (from memory) would make the conformal 3-geometry the only
free datum at a conformally regular origin, with the rest-frame contrast vanishing there, so "deposit" would
carry no datum of its own; the store places the descent at finite T_d with a pre-metric sector before it, where
both solutions are admissible. Note that under a pure growing solution the question does not go away: a white
contrast in the rest frame still gives index -1 (delta_c = (4/3) x^2 zeta) and a white contrast on the flat slice
gives 3. R3 chosen and filed (P2). R4 (my own: the local density parameter) is the sharpened form of P1's
constraint. R5 (my own: the area law from the CAR algebra) is in P2 as the hyperuniform class, with the killed
logarithm above.
Not filed, computed by hand (argued): for constant w the leading projection is
zeta_inf = -R_Sigma - (2w/(3(1 - w^2))) delta_c (radiation: 1/4; dust: 0, R is conserved for both solutions).

## Unexpected links
1. The store already holds both conversions for the same white energy noise: index 3 in the quasi-free result,
   "extensive capacity gives -1" in the thermal reading with a heat capacity. (Found independently by SB.)
2. The time-shift result has a hidden fourth local datum, the patch's own curvature: its three data
   (T_d, n_Q, epsilon) assume flat patches. With it, the adiabatic direction is not only a field of delays.
3. In the gauge fields themselves: the spatial bivector part of Omega(e_j) is (k psi - Hc b) sin kx e_1 e_j, the
   slice-independent potential times k. The Bardeen potential is a component of the rotation-gauge field.
4. The three terms of zeta_inf are the classical ladder of large-scale density spectra (white for uncompensated
   mass, k^2 for uncompensated momentum, k^4 when both are compensated; Zel'dovich, Peebles: from memory).
5. Entropy and index under the Poisson conversion: a deposit with entropy gives -1, a pure stationary one 0. The
   tilt would then measure the purity of the deposit on observed scales (crossover at k ~ 19 a T).
6. For one Weyl field the white energy noise splits in the algebra as mixedness plus |p ^ mu|^2: heat and pair
   creation are two terms of one Clifford identity.
7. The filled sea's amplitude under uniform expansion, 3 H_d^2/(8 pi^2 M_P^2), is the slow-roll formula
   H^2/(8 pi^2 epsilon M_P^2) at epsilon = 1/3. Recorded as a coincidence of form; no meaning is claimed.
8. Under (UE) the thermal deposit reaches A_s at the pivot at 3.6e9 GeV, within a factor five of the stored
   window ceiling 7.3e8 GeV, which comes from the heavy-neutrino fit; at the ceiling it is 0.37 A_s at the
   present Hubble scale. A coincidence unless (UE) is adopted; then it is a bound on T_d from the largest scales
   (SB's item).
9. The stored result on the area-law reading (problem clause (vii)) and the filled sea give the same index for
   the same reason (fluctuations on a surface, not in a volume); the sea needs no imported heat capacity.

## Decisions for Leon
D1 (premise). The descent slice's first-order expansion datum. Options: (UE) uniform expansion; (LC) local
   criticality (flat slice), with or without the deposit at rest; neither, recording the slice's local density
   parameter as a free datum of the descent beside the charge and the spectrum. Recommendation: neither for now.
   Nothing stored selects one; (LC) keeps the old numbers but would be adopted for that consequence; (UE) is the
   reading of "one simultaneous event" and would make the hot deposit visible on the largest scales and cap T_d
   near 1e9 GeV. Both proposals state their clauses conditionally; neither creates a postulate or an assumes edge.
D2 (corrections to stored entities; none made by me).
   a. synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise clause (iv) and its "Consequently": SB filed
      version 5. Wording I would use: "the spectrum of the deposit's density contrast" in place of "the deposit's
      spectrum"; "under a flat descent slice with the deposit at rest the shot term is the primordial one up to
      1/16 (index 3); for a thermal deposit on a flat slice the index is +1 and the amplitude at most 4e-41 at the
      pivot; on a slice of uniform expansion the index is -1 and the amplitude is (9/4)(a_d H_d/k)^4 times the shot
      term, equal to A_s at the pivot near 3.6e9 GeV for the thermal bath".
   b. synthesis.adiabatic-deposit-modulation-is-a-time-shift: name the hypothesis that patches are spatially flat
      (it is (LC)), and say that a fourth local datum, the patch's curvature, adds
      (3/2)(a_d H_d/k)^2 (Omega - 1).
   c. synthesis.finite-range-descent-deposit-cannot-seed-cmb: clause (i) stands. The closing sentence "a deposit of
      finite range at the Hubble or thermal length gives (kR)^3" should read "a deposit whose zeta has finite
      range"; a matter deposit of finite range has zeta of finite range only under (LC) with compensated momentum.
   d. synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window: note that its conversion is
      the (UE) reading and that its row "extensive capacity gives -1" applies to the stored thermal deposit itself.
   e. op.descent-state-and-spectrum, "known": "the shot term at the pivot is below 1e-77" is a statement about the
      contrast; three ledger rows to add: -1 (thermal deposit, uniform expansion, with its amplitude), +1 (thermal
      deposit, flat slice), 0 (filled sea, uniform expansion; a miss).
D3 (edges). If P1 is accepted, P2's Hypothesis (C) at gamma = 3/2 can cite it (a uses edge the maintainer adds).
   P1 cites the time-shift result, the thermal reading and the window ceiling without edges, because the first
   rests on Hypothesis (U) and the other two on Premise (EW), which contradict (E307 if all are declared).
D4 (imports for the maintainer; all cited from memory, none used in a proof step): Zel'dovich and Peebles on
   minimal large-scale spectra; Magueijo and Pogosian 2003 on thermal fluctuations; Tod, and Anguige and Tod 1999,
   on isotropic singularities; York's conformal method; Torquato and Stillinger on hyperuniformity; Gabrielli,
   Joyce and Sylos Labini 2002; Gioev and Klich 2006; the Planck 2018 running of the index. The last is the only
   one a statement would need (to turn "running +0.069" into "excluded"); it is kept out of every statement level.
D5 (letters). (UE), (LC) in P1; (C) in P2; SB's restated entity uses (FR), (FM), (UE). One convention is needed.

## Proposal ids
- synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit (new; check4 exit 0, 0 findings)
- synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary (new; check4 exit 0, 0 findings)
Scratch: colony/runs/2026-11-16-spectrum/work/SA/ (pert0-5.py, lune.py, lune2.py, p1/, p2/, staged/).

## Next step (not done)
- General equation of state in the exact projection (leading order above is by hand).
- The anisotropic-stress noise of free quanta at order one (argued only).
- A low-multipole likelihood for the index -1 term under (UE) (SB's item).
