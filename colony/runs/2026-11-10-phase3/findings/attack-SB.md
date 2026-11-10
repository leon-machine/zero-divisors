# attack-SB: Cluster S, the primordial spectrum (adversarial)

Status: complete for the attack round. One proposal filed. Sibling SA files the base statement
(`synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources`: the criterion, the
ledger, the dust-plus-constant scaling); nothing here duplicates it, and my proposal names it as the intended base
citation in its extraction note (a proposal cannot cite a proposal).

Open problem: op.descent-state-and-spectrum (status reformulated). The store already holds about fifteen negative
results on it. The adversarial work was therefore an audit of those kills and of what SA keeps.

## Routes considered
R1. Gauge-artefact test of the Kasner kill (stored index three is for a spectator; the stored results list the
    scalar sector and the conversion to the curvature perturbation as "not covered"). CHOSEN for the proposal: it is
    the one objection that an exact computation in the stored setting can settle.
R2. Tree-level-artefact test of the coupling kill (one-loop flow of the curvature coupling). Findings only: it
    rests on a literature form of the flow, which only the maintainer can import.
R3. De Sitter boundary modes: is the stored thermal state the standard de Sitter result in disguise. Findings.
R4. Look-elsewhere accounting. Findings.
R5. Attack on what SA keeps (the dust-plus-constant contraction). Findings, addressed to SA.

## Kill conditions (registered before computing; unchanged)
K1 (R1). The gauge-artefact objection SUCCEEDS (the stored kill is an artefact) if the pump field of the curvature
    perturbation or of the tensor modes at the stored isotropic Kasner point has Bessel order different from 0.
    Otherwise the kill stands.
K2 (R2). The tree-level objection SUCCEEDS if the one-loop flow can carry a stored coupling into the window
    without a chosen number (a chosen scale ratio or coupling counts as a fit). It FAILS for couplings below the
    conformal value if the flow is homogeneous in the departure from the conformal value.
K3 (R3). "Standard result in disguise" is CONFIRMED if the stored thermal state and conversion give index exactly
    0 and an amplitude equal to a pure number times Q(I_Lambda)/M_P^2, the form of the textbook de Sitter spectra;
    REFUTED if the stored structure gives a different power or a nonzero index with no fitted number.
K4 (R4). A "hit" by any structure counts as evidence only if its trial factor leaves it below one chance in
    twenty; otherwise it is a coincidence.
K5 (cluster kill, RUN.md). No structure gives n_s < 1 without a fitted number: then the series needs a new premise.

## Results

### R1. The Kasner kill is not a gauge artefact (PROVED; exact check). Proposal filed.
Proposal: `synthesis.scalar-sector-at-the-isotropic-scalar-kasner-point-obeys-the-spectator-equation`
(check4 exit 0, no findings; validate ok; registered).
At the isotropic point of the scalar Kasner disk (exponents 1/3 each, 8 pi G q^2 = 2/3; the common reduction of the
five-dimensional vacuum ends (1/2,1/2,1/2,-1/2) and (0,0,0,1)), in the gauge with unperturbed spatial metric, with
lapse perturbation f, shift b and scalar perturbation u (in units of its rate):
- the time-space equation forces f = u; a transverse diagonal equation forces b = tau^(2/3) u'/k; the time-time
  equation is then exactly u'' + u'/tau + k^2 tau^(-2/3) u = 0, the stored spectator equation, Bessel order 0; the
  other components hold identically (all ten components computed exactly with a formal engine; three controls fail
  as they should);
- the gauge-invariant curvature perturbation is zeta = u/3, its pump field z = 3 q a is a constant times the scale
  factor (the background combination a^3 phi_0'^2/H is constant there, which is why no extra term appears);
- so, given the stored adiabatic vacuum, the curvature perturbation itself has the stored blue index (2 to 3,
  k^3 log^2 outside), the same as the spectator and the cross (tensor) modes. No conversion step, no free number.
K1 verdict: the objection FAILS; the stored kill stands, now for a gauge-invariant quantity. Scope: the isotropic
point only (anisotropic disk points couple the scalar sector to the diagonal shear modes: not done); the vacuum
normalisation is taken k-independent (textbook quadratic action of the curvature variable, not rederived).
Remark, not in the proved statement (computed, given textbook normalisations): with z proportional to a the
tensor-to-scalar ratio of a constant-w single-clock stage is 16 epsilon = 24(1 + w): 48 at this point, 24 for a dust
contraction, 0.276 for the expanding power law that would give the Planck tilt (p = 20351/351, w = -20117/20351),
23.9 for its Wands dual (w = -117/40351, the stored -0.0029). Against r < 0.036 (BICEP/Keck 2021, from memory; the
search hit arXiv 2110.00483 was not opened) every constant-w single-clock stage that matches the tilt fails on r
with no free number. A spectator plus conversion escapes this, at the cost of a conversion coefficient.
Classification: transport-absent (standard perturbation theory placed in the store's setting); the Clifford content
is only the frame and the completed residue.

### R2. The tree-level kill of the coupling route (ARGUED, given a literature form of the flow)
Web check: arXiv hep-th/0311229 (read on the web) gives, for a quartic scalar in the minimal
subtraction scheme, beta_xi = lambda (xi - 1/6)/(4 pi)^2: homogeneous in the departure from the conformal value. The
same paper says the conformal value is NOT a fixed point for a massive field away from the ultraviolet regime
(inhomogeneous term of relative size 1/30 in the infrared), and gives nothing beyond one loop.
Consequence, arithmetic on the stored formula 4 nu^2 = (lambda_h - 1)^2 + 6 xi at the isotropic point:
- a coupling starting at or below 1/6 (the stored tree-level 0 of the rung doublets and of the stored actions)
  stays below 1/6 under the homogeneous flow for any amount of running, so 6 xi < 1, 4 nu^2 < 5 with the stored
  hidden-scale weights, index above 3 - sqrt 5 = 0.76: blue. No scale ratio can repair it.
- a coupling starting in (1/6, 1/2] (the dictionary values -w/6) reaches the window only if the departure from 1/6
  grows by a factor between 4.068 and 4.144 (from 1/2; more from smaller values): a chosen product of coupling and
  logarithm of a scale ratio, that is a fit.
K2 verdict: the objection FAILS at one loop in the massless regime, for the stored zero; it is NOT excluded for a
massive field in the infrared or beyond one loop. The stored kill is not an artefact of tree level at the order
the literature fixes. Not filed: it needs the flow as an imported Fact (decision 2).

### R3. The de Sitter boundary modes (COMPUTED: arithmetic on stored formulas plus textbook values)
- The stored thermal state (every boundary mode of the cosmological horizon thermal at T_Lambda = sqrt(Q(I))/2 pi,
  synthesis.de-sitter-temperature-frozen-point-norm) is the static-patch restriction of the de Sitter-invariant
  state (the stored import synthesis.imported-de-sitter-invariant-hadamard-state-unique): this is the
  Gibbons-Hawking statement, not a new source.
- Thermality does not give scale invariance. The index of a bulk field in that state is -2 w_lead (stored:
  synthesis.frozen-phase-spectrum-not-red): 0 only at the massless point, 2 for the conformal weight. The textbook
  scale-invariant spectrum is the order-3/2 massless minimally coupled boson, amplitude (H/2 pi)^2 = T_Lambda^2.
- The stored holographic conversion at the frozen point's temperature gives index exactly 0 and
  P_Phi = 2 lambda H^2/(pi M_Pl^2) (synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window
  (iii)). The textbook graviton spectrum of de Sitter space is 2 H^2/(pi^2 M_red^2) = 16 H^2/(pi M_Pl^2). So the
  stored expression is lambda/8 times the standard tensor spectrum: the same pure-number-times-1/N^2 form.
  K3 verdict: CONFIRMED. It is the standard de Sitter result in disguise, about 1e-122, and the modes that leave the
  frozen point's horizon are today's Hubble-scale modes, not primordial ones (stored: observed modes are inside).
- The boundary modes themselves are fermionic arrays: occupations at most one, shot noise (stored). SA's row 22
  kill is not an artefact: nothing in the count is bosonic.
- With cluster D: a red tilt from a de Sitter-like stage is -2 epsilon - eta in slow-roll language and needs
  w > -1 during exit (exactly: the expanding power law with the Planck tilt has w = -20117/20351 = -0.98850). The
  stored frozen point with the Henneaux-Teitelboim promotion has d Lambda = 0, w = -1 exactly, epsilon = 0: index
  exactly 0 and no adiabatic curvature perturbation at all (no clock). So the series' sharpest dark-energy
  prediction and a quasi-de Sitter origin of the tilt exclude each other within the stored structures (argued).
Prior art (web): the thermal reading of de Sitter fluctuations is standard (Gibbons and Hawking 1977, from memory);
search hits not opened: arXiv 1404.2222 (tilted tensor spectrum from the Gibbons-Hawking temperature),
hep-th/0307045 (holographic temperature bound in slow roll).

### R4. Look-elsewhere accounting (COMPUTED; work/SB/lookelsewhere.py)
- Parameter-free trials: SA's ledger has 24 rows; none hits. Indices reached without a fit lie in about [-1, 3]
  (plus the anisotropic red values at or below -3). With the Planck three-sigma window of width 0.0252, a
  structure with an index spread evenly over [-1, 3] hits by chance with probability 0.63 per cent; over 24 trials
  about 14 per cent. K4 verdict for the future: a single three-sigma match of the index by one more stored
  structure would NOT count as evidence (14 per cent > 5 per cent) unless a second number (amplitude, running,
  tensor ratio, isotropy) comes with it.
- One-parameter fits already in the store that reach the tilt: the curvature coupling (xi in [1.5226, 1.5481]),
  the Kaluza-Klein potential's exponent (p in (0.4556, 0.4570), stored as not a route), the holographic
  temperature exponent (0.01755), the Wands-dual equation of state (-0.0029), and SA's exit time of a
  dust-plus-constant contraction. Five continuous families for one datum: each reaches the window with certainty
  and carries no evidential weight.
- Small numbers cannot do it: no Bessel order a/b with b <= 20 lies in the Planck three-sigma window
  [1.51125, 1.52385] (least denominator 32/21; one-sigma: 41/27). Every stored order is a ratio or a square root
  of ratios of small integers, so every stored structure misses by construction; a match needs a number of order
  2/(1 - n_s), about 57 (integer power-law exponents 43 to 89 at three sigma), or a tuned continuous one.
- Rational-coupling numerology: in the stored window the only xi = a/b with b <= 12 is 17/11; the expected number
  of such rationals in a random window of that width in [0, 2] is 1.2. So "the fitted coupling is a simple
  fraction" would carry no weight either.
- Dataset dependence (web, arXiv 2510.18656 read): n_s = 0.9649 +- 0.0042 (Planck 2018, the stored Fact);
  0.9709 +- 0.0038 (Planck + ACT DR6); 0.9743 +- 0.0034 and 0.9752 +- 0.0030 (with lensing and DESI DR1, DR2);
  0.9647 +- 0.0037 (SPT-3G + Planck); 0.9684 +- 0.0030 (SPT + Planck + ACT). Scale invariance stays excluded at 8.3
  to 10.5 standard deviations in every combination, so every stored kill survives; the stored fit windows move
  (the coupling window becomes [1.5158, 1.5340] at three sigma for the DESI DR2 combination, and 17/11 drops out).

### R5. Attack on SA's near-candidate: dust plus the frozen point's constant, run as a contraction (ARGUED)
For SA (do not file from here; the scaling is in your base statement):
1. It is a published model: Cai and Wilson-Ewing, "A Lambda CDM bounce scenario", arXiv 1412.2914 (abstract read on
   the web): the tilt comes from the positive constant making the effective equation of state slightly negative
   at exit; they predict positive running and r = 24 c_s^3 with a small sound speed of the cold matter.
2. Hidden numbers: (a) the exit is at the SOUND Hubble radius, so the tilt at the pivot depends on the dust's sound
   speed, which the store does not hold; (b) with exactly the stored constant and the observed matter density run
   backwards, exit of the pivot (k about 220 H_0) is at a = Omega_m H_0^2/k^2, about 6e-6, where the ratio
   x = rho_Lambda/rho_m = 2.2 a^3 is below 1e-15 (and where radiation, which gives no exit, dominates the
   observed history); the tilt 12 x is nil: scale invariant at best, 8.4 sigma off. Matching the tilt needs
   x = 0.0029 at the pivot's exit, a chosen dust density of the pre-descent stage: a fit.
3. Running: the tilt is -12 x with x proportional to a^3 and exit at k proportional to a^(-1/2), so the tilt
   scales as k^-6 and the running is +6 (1 - n_s) = +0.21 at the measured tilt, against -0.0045 +- 0.0067 (Planck
   2018, from memory): 32 standard deviations, with no free number once the tilt is matched at one scale. The
   measured tilt is constant over three decades; this mechanism cannot hold it over one.
4. Tensor ratio 24 for the adiabatic mode with unit sound speed (R1 remark): excluded unless the sound speed is
   small, the second chosen number.
5. Not stored: any dust before the descent ((P1) postulates a Kasner stage, stiff or vacuum), and the matching
   (P2). The candidate fails clauses (a) and (c) of SA's secondary kill.

### Checks of other kills against the two artefact classes (ARGUED, brief)
- Finite-range bound, shot-noise bound, Hermite-rank bound: inequalities on correlators, no gauge or loop order
  enters. Not artefacts.
- Frozen-point index -2w: a Ward identity of the stabiliser's dilatation; loop corrections preserve it while the
  state is invariant (anomalous dimensions would shift w, which is then the fitted number). The massless point
  w = 0 is protected only by a shift symmetry; no stored field has one except, argued by SA, the pair channel.
- Sudden descent: the feature is a statement about the instantaneous vacuum; the stored non-Hadamard result
  already says that state is not admissible, so this kill is of a straw candidate, correctly labelled.
- Kasner cross modes on the BKL circle (red on one axis): gauge-invariant at linear order on a vacuum background
  (stored); the anisotropy kill is of the measured isotropy, not of the gauge.

- SA's rows 20 and 21 (the tower's pair channel promoted to a field; density-wave bosons on a null generator),
  both labelled argued by SA: the best either can give is index 0 (a shift-symmetric massless field, or a
  one-dimensional phase field), which is scale invariance, excluded at 8.3 to 10.5 sigma, never a red tilt; and
  each lacks a stored step (a spatial field for the pair channel; a map from generators to a slice, where
  uncorrelated generators give a blue index). Neither is a candidate; neither kill depends on a gauge choice.

## Cluster verdict (K5)
No stored structure gives n_s < 1 without a fitted number; my audit removes the two standing objections (gauge,
tree level at one loop) to the Kasner kills and finds SA's one near-candidate to be a known model with two chosen
numbers and a running excluded at about 32 sigma. The pre-registered kill of the cluster is met: the series needs
a new premise for the spectrum.

## Unexpected links
1. The five-dimensional vacuum end (0,0,0,1), which reduces to the isotropic scalar point, is flat: it is the
   compactified Milne field of the ekpyrotic and cyclic literature (Khoury, Ovrut, Seiberg, Steinhardt, Turok 2001;
   Tolley and Turok 2002, arXiv hep-th/0204091, read on the web). The store already marks it as the one
   non-singular Kasner wall in the text of (P2). Tolley and Turok give a matching rule across exactly this wall
   (free-field continuation, argued unique by locality and time reversal) under which free fields cross with no
   particle production. That is a concrete candidate form for (P2), with the consequence that nothing is created
   at the wall: the spectrum would be whatever exited before, index 3 by R1.
2. Cluster D: exact w = -1 (the promotion, d Lambda = 0) is the same statement that makes the frozen stage's
   spectrum exactly scale invariant with no curvature perturbation. A measured departure of dark energy from -1
   and a red tilt from a de Sitter-like stage would be the same missing structure (a clock on the frozen point).
3. Bridge to the phase 2 window results: the "amplitude 1/N^2" of every de Sitter boundary spectrum is the
   inverse of the horizon entropy pi N^2 up to a pure number (2 lambda/pi against pi): fluctuation of order
   one over the mode count, as for any thermal array. Nothing new, but it is why no boundary count can reach 1e-9.
4. The constancy of a^3 phi_0'^2/H at the isotropic scalar point (the reason the scalar sector reduces to the
   spectator equation) is the completed-residue statement 1 - B_w^2 = c^2 read as a first integral.

## Decisions for Leon
1. Accept or not the filed proposal (it is a test of a stored kill, transport-absent, and closes two "not covered"
   items of the stored Kasner results at the isotropic point only). If accepted, the "not covered" sentences of
   synthesis.kasner-approach-gives-horizon-exit-and-index-three and
   synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling, and the
   known-text of op.descent-state-and-spectrum, should point to it (maintainer edit).
2. Import as Facts (maintainer-only), if the R2 and R1-remark statements are to be stored: (a) the one-loop flow
   of the curvature coupling, beta_xi = lambda (xi - 1/6)/(4 pi)^2 in minimal subtraction, with its stated
   limits (not a fixed point for massive fields in the infrared), source arXiv hep-th/0311229; (b) the quadratic
   action of the curvature variable and of tensor modes (r = 16 epsilon), Mukhanov, Sasaki, from memory; (c) the
   tensor bound r < 0.036 (BICEP/Keck 2021) and the running of the index (Planck 2018), both from memory here.
3. Update or supplement the imported Planck 2018 Fact with the 2025-2026 combinations (ACT DR6, SPT-3G, DESI):
   the central value of n_s moves by up to 2.4 Planck standard deviations between combinations, no stored kill
   changes, the stored fit windows do. Recommendation: keep Planck 2018 as the pinned Fact, add one Fact for the
   newer combinations, and state the fit windows as dataset-dependent.
4. Whether to record the Tolley-Turok matching rule as a candidate form of (P2) (a premise decision). It would
   make the Kasner route definite and, with R1, definitely blue. Recommendation: record it as a note on (P2), not
   as a premise.
5. The cluster's pre-registered kill is met: a new premise is needed for the spectrum (or the spectrum stays
   recorded as the deposit's free infrared datum, as now). Options seen in this audit, none recommended as
   derived: a clock on the frozen point (conflicts with the registered w = -1, cluster D); a fitted curvature
   coupling (conflicts with the Sakharov zero and Newton matching, stored); a dust contraction with a constant
   (two chosen numbers, running excluded). Recommendation: keep "no mechanism" as the stored position and add the
   look-elsewhere rule of R4 to the open problem: a future index match counts only with a second number.
6. Not taken up: the scalar sector at anisotropic disk points; the vacuum normalisation of the curvature mode
   in the store's own terms; the flow of the coupling beyond one loop.
