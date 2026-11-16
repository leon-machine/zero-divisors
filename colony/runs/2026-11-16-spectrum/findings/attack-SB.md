# attack-SB (angle B, adversarial) : op.descent-state-and-spectrum, run 2026-11-16-spectrum

Status of this file: FINAL for the attack round (sections 0 to 2 were written before computing and are kept as written). Labels: proved / computed /
argued / conjectured. Nothing here is in the store until a proposal id is given.

## 0. Objections to S1 and S2 (for SA; read this first)

Written from a first pass by hand (argued, to be checked in exact arithmetic in work/SB/). Sign conventions:
slice data psi (curvature perturbation of the slice), kappa (perturbation of its expansion), sigma (shear
potential), matter data delta rho and q (momentum potential, T^0_i = d_i q) as seen by the slice's normals.
Constraints (linear, any slice): energy  H kappa + (k^2/a^2) psi = -4 pi G delta rho ; momentum
(1/3)(kappa - (k^2/a^2) sigma) = -4 pi G q. Slice-independent combinations: R = psi - H q/(rho+p),
zeta~ = psi - delta rho/(3(rho+p)), Delta_com = (delta rho - 3 H q)/rho, and R - zeta~ = Delta_com/(3(1+w)).

O1 (S1 is under-stated, not wrong). The conversion from slice data to the conserved growing mode needs BOTH matter
   data, delta and q, and ONE geometric datum of the slice. In the radiation era, to leading order in
   x = k/(a_d H_d):   R_final = R_d + Delta_com,d / 4 = psi + delta/4 - 2 H q/(rho+p).
   (Projection on the exact growing solution; the decaying solution has R + Delta_com/4 = 0 to the two leading
   orders.)  Consequences:
   (a) Reading (A) needs only kappa = 0 (uniform expansion). "Matter at rest" and "no shear" are not extra
       hypotheses: with kappa = 0 the momentum term is down by k/(a_d H_d) against the density term. So
       R_final = -(3/2)(a_d H_d/k)^2 delta (1 + O(x)) and the 9/4 of S1 stands. The white deposit under (A) IS a
       growing mode (R_d = R_final to leading order); its decaying admixture is in Phi, not in R.
   (b) Reading (B) as stored (zeta = delta/4, index 3) needs MORE than a flat slice: it needs the longitudinal
       momentum noise to vanish. On a flat slice R_final = delta/4 + 2r, r = -H q/(rho+p). A thermal (or any
       mixed quasi-free) deposit has white momentum-density noise, <P_i P_j> = delta_ij T (rho+p) V, so
       P_r = (a H/k)^2 T/(rho+p) and  Delta_R^2 = (1 + 12 (a_d H_d/k)^2) Delta_delta^2/16 : index +1, not 3,
       and an amplitude (a_d H_d/k)^2 above the stored reading (still below 1e-36 at the pivot, so the
       amplitude verdict of clause (iv) survives under (B); the INDEX 3 does not, for mixed deposits).
       So the stored "white noise, index 3" is the reading: flat slice AND matter at rest on it. Three
       readings, three indices for one thermal deposit: 3 (flat, at rest), +1 (flat, thermal momentum noise),
       -1 (uniform expansion).
   (c) "Time shift" (the stored separate-universe reading) is a fourth thing: pure growing mode, in which q is
       slaved to delta (H q/(rho+p) = delta/4 on the flat slice) and Delta_com = O(x^2). Quantum shot noise of a
       state is not of that form (its delta and q are independent operators), so the time-shift result does not
       cover the shot term.
O2 (S1(A) is not admissible on an unbounded slice). Index -1 means <R^2> = int dk/k Delta^2 diverges like
   1/k_IR. With a thermal deposit Delta_R^2 = C (H/T)^3 (a_d H_d/k) reaches 1 at a_d H_d/k = (T/H)^3/C: beyond
   that comoving length the "perturbed spatially flat field" does not exist (the slice's intrinsic curvature,
   which the constraint equates to 16 pi G delta rho, closes it up). So (A) + white + infinite homogeneous
   slice is self-inconsistent; (A) can only be stated with an infrared end, and what it gives is a BOUND
   (ceiling on T_d, or on the slice's extent), not a spectrum. The store already has this pattern: the
   Ford-Parker import and the Hadamard result's "no red law on a band reaching k = 0".
O3 (what would select (B)). A stored statement that every patch of the descended field is SPATIALLY FLAT
   (local Friedmann constraint absorbed in the Hubble rate, not in curvature). Reading (A) is exactly: each
   patch has the common Hubble rate and spatial curvature K = (8 pi G/3) a^2 delta rho. So (A) versus (B) is the
   flatness question asked patch by patch. Searching the store for what fixes spatial flatness of the descended
   field (results below, section 1).
O4 (S2). To be tested: (i) the ENERGY structure factor of a pure Fermi ball, not the number one; (ii) the
   momentum term of O1(b), which for a pure translation-invariant state should vanish at k = 0 as well;
   (iii) whether the store's deposit can be pure at all (the I-state has entropy; (L_E) conserves occupations).

## 1. Pre-registered kill conditions (written before the computations)

K1 (S1, from RUN.md). A stored premise or proved result forces the flat-slice reading (B)  =>  the dichotomy is
   not new; record the premise and whether the stored statements cite it.
K2 (S1 conversion). Project uniform-expansion data (kappa = 0, white delta, arbitrary q) on the exact
   radiation-era solutions. If the growing-mode amplitude is NOT -(3/2)(a_d H_d/k)^2 delta at leading order
   (for instance, if it is suppressed by a power of x, so that the white deposit is mostly decaying), S1's (A)
   amplitude and index are killed.
K3 (thermal amplitude). Recompute by the heat-capacity route (Var E = T^2 C_V at zero chemical potential) and by
   the quasi-free route (Var = Tr f E f (1-E) with Fermi-Dirac occupations). If the coefficient is not
   135/(pi^4 g) (H/T)^3 (a_d H_d/k), report the true one; if T_d at A_s is outside [1e9, 1e10] GeV for
   g = 106.75, the orchestrator's number is killed.
K4 (stored index 3 under (B)). If the longitudinal momentum-density noise of a thermal quasi-free deposit does
   not vanish at k = 0, the stored "index 3" is not the index of a thermal deposit on a flat slice (it is +1);
   that is a correction to the stored reading. Killed if the exact projection shows the momentum term is
   decaying-mode only.
K5 (S2). The energy structure factor of a pure gauge-invariant deposit does not vanish linearly at k = 0  =>
   the index-0 row is killed (RUN.md). Mine in addition: if the store's deposit cannot be pure (entropy of the
   I-state conserved from the descent), S2 is a statement about a deposit the store does not have.
K6 (S3). Exhibit an exchangeable state whose slice two-point function is NOT white plus a zero mode  =>  S3 is
   refuted. Otherwise prove it; and name the stored group, if any, smaller than the symmetric group.
K7 (S5). Exhibit a homogeneous quasi-free CAR state with structure factor above 2, or a sparse deposit that
   reaches A_s on the whole observed band with sub-Planckian quanta  =>  S5 is refuted.
K8 (S4). A stored map from rungs to comoving scales exists  =>  S4 is not dead; otherwise one paragraph.

## 2. Routes (S1/S2 attack)

R1 (the problem's own). Read the stored entities for the conversion they use; find the hypothesis.
R2 (another subject). Search the gravity/wall/frozen-point subjects for what fixes the slice: spatial flatness
   of the descended field, the frozen point's flat slicing, the tame wall, the Weyl-flat collar, P1.
R3 (my own). Initial-value projection: the linear map (psi, delta, q) -> growing-mode amplitude from the exact
   radiation-era solutions, exact rational series; then every reading is a row of one table.
Choice: R3 first (it decides K2, K4 and gives SA the full map), then R2 for K1.

## 3. Results

### 3.1 The projection (computed, exact series; work/SB/proj.py) : K2 and K4 both NOT triggered
Radiation era, x = k eta, Phi'' + (4/x) Phi' + Phi/3 = 0. Exact Frobenius series:
  growing  Phi_g = 1 - x^2/30 + ...        R_g = 3/2 - x^2/12 + ...     Delta_g = -(2/3) x^2 + ...
  decaying Phi_d = x^-3 + x^-1/6 - x/72... R_d = x^-1/6 - x/36 + ...    Delta_d = -(2/3) x^-1 - x/9 + ...
with R = Phi + (x Phi' + Phi)/2 and Delta_com = -(2/3) x^2 Phi (the slice-independent Poisson relation). The
determinant R_g Delta_d - Delta_g R_d is exactly -1/x, so for ANY data (R, Delta_com) at x:
  A = R (2/3 + x^2/9 - ...) + Delta_com (1/6 - x^2/36 + ...),   R_final = (3/2) A = R + Delta_com/4 + O(x^2).
In slice data: R_final = psi + delta/4 - 2 H q/(rho+p) + O(x^2 terms).
  - uniform expansion (kappa = 0): psi = -(3/2) delta/x^2, and the O(1) delta terms cancel:
    R_final = -(3/2)(a_d H_d/k)^2 delta + 2r + O(x^2 delta).  S1's 9/4 in the power stands (K2 not triggered);
    the deposit is a growing mode; "matter at rest, no shear" is not needed.
  - flat slice (psi = 0): R_final = delta/4 + 2r.  The stored |zeta| = delta/4 needs r = 0 as well (K4 not
    killed: the momentum term feeds the growing mode with coefficient 2).
  - time shift: r = -delta/4 on the flat slice, Delta_com = 0, R_final = -delta/4 (pure growing mode).
SA: your KILL-1c will pass. Please carry the momentum term into the theorem; without it the flat-slice row of a
mixed deposit is stated with the wrong index. For a thermal deposit (computed by hand, to be put in a check):
  P_delta = 4T/rho, P_u = T/(rho+p) (u the longitudinal momentum contrast), cross term zero by isotropy, so
  flat slice:        Delta_R^2 = (1 + 12 (a_d H_d/k)^2) Delta_delta^2 / 16      (index +1)
  uniform expansion: Delta_R^2 = (9/4)(a_d H_d/k)^4 Delta_delta^2 (1 + O(x)) (index -1)
A pure state invariant under translations has neither term at k = 0. Pure pair states with partners at
opposite momentum (the form cosmological pair creation gives) have white ENERGY noise, twice the mixed value,
4 w^2 n(1-n) per pair, and NO momentum noise at k = 0: for them the flat-slice index is 3 and the stored reading
is exact. So the stored index 3 is right for pair deposits and wrong (+1) for the I-state read as a mixed state
of independent modes.

### 3.2 Thermal amplitude under (A) (computed by hand, two routes agree; exact brackets go in a check) : K3 passes
Route 1, heat capacity: Var E = T^2 dE/dT = 4 rho V T at zero chemical potential (bosons and fermions alike), so
P_delta = 4T/rho, Delta_delta^2 = (60/(pi^4 g)) (k_ph/T)^3, and with (A)
  Delta_R^2(k) = (135/(pi^4 g)) (H_d/T_d)^3 (a_d H_d/k).   The orchestrator's coefficient is right.
Route 2, quasi-free: Var = Tr(f E f(1-E)) -> int w^2 n(1-n) d^3p/(2 pi)^3 = T^2 d rho/dT, the same.
Numbers (g = 106.75, M_P = 1.2209e19 GeV, stored a_d H_d/k_* > 3.2e20 at 1e12 GeV, scaling as T_d):
  T_d = 1e12 GeV : Delta_R^2(k_*) = 11.5 (not a perturbation)
  equals A_s at the pivot for T_d = 3.7e9 GeV (orchestrator: 4e9, confirmed)
  at the stored (R) ceiling 7.3e8 GeV : 3.3e-12 at the pivot (1.6e-3 of A_s), 7.3e-10 at k = a_0 H_0
  (0.29 of the measured power there, since the white term grows as 1/k and k_*/a_0 H_0 = 222).
So under (A) the observed band bounds T_d by the LARGEST observed scale, not the pivot: the white term stays
below the measured spectrum at k = a_0 H_0 only for T_d < about 1.0e9 GeV; a tighter figure needs a low-multipole
likelihood (not done; the Sachs-Wolfe plateau of an index -1 term falls as 1/l in l(l+1)C_l).

### 3.3 Infrared admissibility under (A) (argued)
Index -1 has <R^2> = int dk/k Delta^2 linear in 1/k_IR. Delta_R^2 = 1 at k_NL = C (H_d/T_d)^3 a_d H_d: at the
(R) ceiling that is 7e-10 a_0 H_0, a comoving length of 1.4e9 present Hubble radii; at 1e12 GeV it is INSIDE the
observed band. An unbounded homogeneous white deposit on a uniform-expansion slice is not a perturbed flat
field beyond 1/k_NL. Under hypothesis (F) the frozen point's length |x_d| = 4.3 Hubble radii is far below
1/k_NL for T_d below about 1e9 GeV, so (A) is admissible there with the frozen point's range as the infrared end.

### 3.4 What selects the reading: the search for K1 (argued, by reading; no selector found)
Candidates read in full at the formal level, and what each does:
  (s1) synthesis.adiabatic-deposit-modulation-is-a-time-shift: ASSUMES flat patches ("each patch is an
       unperturbed descended universe", zeta_gamma = delta ln T_d on the uniform-time slice, which is
       zeta = -psi + delta/4 with psi = 0). It is reading (B) as a hypothesis of a result about classical
       modulations; it does not derive it and does not cover a state's shot noise (O1(c)).
  (s2) standard-model.dating-descent, second reading of the join ("the frozen phase ending at the descent with
       the scale factor continuous"): IF this is read as continuity of the slice's whole first fundamental form
       (the weakest junction condition) AND the frozen side's slice is a level set of the frozen point's flat
       slicing, then psi = 0 on the descended side: reading (B), with the momentum term still free. Neither "if"
       is stored: the junction condition is not in the store (gravity before the descent is the pre-metric
       sector, degenerate, with no induced metric to continue), and the primary reading (F) states no join
       condition at all. This is the nearest thing to a selector and it is a conjecture, not a premise.
  (s3) synthesis.field-space-premise-parallel-frozen-point (FS): the parallel frozen point has <X, I> = 1 in the
       physical scale on every configuration, matter included, so its scale function is constant there and
       defines NO time function, hence no slice. No selection.
  (s4) synthesis.radical-normal-tame-wall-...: background statement (the radiation origin is a regular initial
       surface of the conformally rescaled field); smoothness selects no state; nothing on perturbations. If the
       descent were AT that origin, the regular data would be the growing mode alone with the wall's conformal
       3-geometry free and the comoving contrast zero at the wall (Tod, from memory): then "deposit" has no
       matter datum at all and neither (A) nor (B) is the question. The store puts the descent at finite T_d
       (the window), so both modes are admissible data.
  (s5) synthesis.hadamard-deposit-premise (HD): a smooth globally hyperbolic collar and a Hadamard state; fixes
       the ultraviolet only ("The occupation profile ... is free data"). No selection; but an unbounded (A) is
       excluded as in 3.3 if "collar" is read as a perturbed Robertson-Walker field.
  (s6) dark-matter.p1-single-frozen-point: one metric for all towers; "an independent choice on conformally flat
       regions". No slice condition.
  (s7) synthesis.promoted-norm-one-global-pair: Sigma compact, one global pair; the conjugate time advances by
       an integral of the Weyl square; no local time function on Weyl-flat fields. No selection.
  (s8) synthesis.finite-range-...: its statement is about a covariance of zeta "on the comoving slice of the
       descent", and its clause (ii) takes the descended phase flat from the record values. Flatness of the
       background is the record's, not a derived property of the descent; nothing extends it patch by patch.
Verdict on K1: NOT triggered. No stored premise or proved result forces (B). The store holds BOTH conversions
already: index 3 for the thermal deposit in the quasi-free result (flat reading, unnamed) and "an extensive
capacity gives -1" in synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window(i) (Poisson
reading, through the imported string-gas conversion at Hubble exit). The two rows are the same white energy
noise read two ways.

### 3.5 S2 (argued; SA computes the structure factor)
The store's deposit is not pure on the modes that carry the energy: synthesis.quadratic-flows-cannot-thermalise-
descent(iv) has the descent deposit "the Fermi-Dirac occupations directly, mode by mode, for instance as the
restriction of pure pair states"; occupations n(1-n) > 0, so S(0) > 0. A purification by partners does not help:
if the partners gravitate (positive energy on the slice) the pair state has energy variance 4 w^2 n(1-n) per
pair, twice the mixed value; only partners of opposite boost energy (the horizon pair, which is not on the
slice) leave the energy sharp. So K5's second clause is triggered: the Harrison-Zel'dovich row of S2 is a
statement about a deposit (a filled Fermi ball) that the stored state rules do not produce. It is still a
legitimate row of the ledger under (A), reported as a miss (n_s = 1 exactly).

### 3.6 The conversion tested against the two stored Facts (computed; in the check of proposal P3)
- synthesis.imported-large-scale-potential-and-sachs-wolfe-relations: R = (3w+5)/(3(w+1)) Phi, 3/2 at w = 1/3. The
  growing Frobenius solution has R_g/Phi_g = 3/2 at leading order: agrees.
- synthesis.imported-superhorizon-zeta-conservation: zeta constant "up to terms suppressed by (k/aH)^2". The
  uniform-density variable is R - Delta_com/4 and Delta_com = -(2/3) x^2 Phi, so the neglected terms are x^2 Phi.
  For growing data they are small against zeta. For data with a decaying part Phi is of order zeta/x^2 or larger
  and they are NOT small: under (A) zeta is conserved to relative order x^2 (the deposit is a growing mode);
  on a flat slice with the deposit at rest zeta = +delta/4 on the slice and -delta/4 afterwards (same size,
  opposite sign: the stored number survives by the magnitude only); with momentum noise it changes by 2Xu. So the
  stored step "carried unchanged as an adiabatic zeta" is right for a deposit GIVEN as a zeta (the finite-range
  result) and for time-shift data, and is not a statement about a matter deposit read on its slice. The Fact
  itself is consistent as stored; no correction to it is proposed.

### 3.7 S3, exchangeable deposits: PROVED, in a sharper form. Proposal P1
id: synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape (check4: 0 errors, 0 other findings)
- (proved) Invariance under a relabelling group transitive on unordered pairs of units (exchangeable, or any
  doubly transitive group) leaves the covariance (v - c) 1 + c U: two numbers.
- (proved) On any slice Var(phi(f)) = (v - c) sum f_i^2 + c (sum f_i)^2: every dependence on k is the embedding's
  form factor; localised cells give white noise plus a k = 0 term. K6 not triggered for localised cells; for
  extended profiles the seed as worded was too strong and is restated (the shape is the embedding's, the same
  for every such state).
- (proved) The criterion is exact: if the group is not transitive on unordered pairs each further orbit is a
  further free second moment (ring of six cells, nearest-neighbour covariance: 5/4, 3/4, 1/2 on the three
  cosine modes). The check found a group (x -> a^2 x + b on seven labels) that is NOT doubly transitive and
  still forces two numbers, so the right hypothesis is transitivity on UNORDERED pairs, not double transitivity.
- (proved) Exchangeable fermion states: no pairing, real one-particle matrix (n - e) 1 + e U, |e| <= 1/(N - 1);
  quasi-free case in closed form; the stored ladder states are the worked non-Gaussian example (total sharp,
  white beneath).
- (proved) Similarities of a Euclidean slice are transitive on ordered pairs of points: an invariant kernel of
  weight zero is constant, of weight Delta the single power Q(x - y)^(-Delta). A conformal structure alone leaves
  one exponent.
- Reading (argued): the pre-metric escape of the finite-range result is narrowed to deposits whose state
  already carries the separations of its units. Stored groups: the symmetric group on tower blocks (ladder
  states); the similarities the frozen point's stabiliser induces at its late-time boundary (one exponent, the
  stored weight reading); the Lorentz group on null directions is triply transitive (standard, not used); the
  Euclidean group of a slice is not transitive on pairs (orbits = separations), which is the stored finite-range
  setting. Transport-absent core, transport-convenient clause (iv).

### 3.8 S5, sparse or energetically broad quasi-free deposits (attack item 3): Proposal P2
id: synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta
(check4: 0 errors, 0 other findings)
- (proved) Pauli count: quanta softer than kappa number at most g kappa^3/(6 pi^2); so the stored shot term obeys
  s <= (2(2f + eta)/pi) X^-3 (w_max + kappa)/M_H, M_H the Hubble mass, X = a_d H_d/k, f the share of the density.
  What fixes the number of quanta of a deposit that does not conserve entropy is the ENERGY BUDGET, not the
  record of the entropy.
- (proved) The longitudinal momentum density has the same shot bound, mode by mode.
- (proved, conditional on each conversion, which are hypotheses there) to reach A = 2.0e-9 at k = a_0 H_0:
    flat slice, deposit at rest : a quantum above 3.0e15 Hubble masses (1 MeV), 9.6e60 (1e12 GeV)
    flat slice, momentum noise  : above 0.034 Hubble masses (1 MeV), 5.0e13 (1e12 GeV); in reduced Planck masses
                                  above 2.3e42 and 1.1e27, the least value in the window being at its top
    uniform expansion           : the condition is below 2.5e-30 Hubble masses at the pivot at 1e12 GeV, where
                                  T_d is above 1e-20 Hubble masses: thermal quanta meet it; NOTHING is closed.
- Verdict on S5: under both flat-slice readings item 3 closes for deposits whose quanta are field quanta
  (argued criterion: energies below the Planck mass; NOT a stored premise). Under (A) the seed's count closes
  nothing; a deposit is bounded there by the shape of its structure factor on the band. K7 not triggered under
  the flat readings; under (A) the seed's hope of closing by counting is dead.
- The seed's "S(k) <= 2" is the right bound for the NUMBER structure factor only. The ENERGY one is bounded by
  the energy spread, which is why "energetically broad" deposits were open; the w_max form handles both.
- Candour: under (C0) this is the stored finite-range obstruction seen from the quanta (a white contrast
  reaching 16 A at X is 16 A X^3 > 3.9e15 at the Hubble scale). The new content is the Pauli/energy-budget
  inequality, the momentum row, and the statement that the uniform-expansion row is NOT closed.

### 3.9 Correction of a stored entity: Proposal P3
id: synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise, version 4 -> 5, kind restatement
(check4: 0 errors, 0 other findings; all five stored check functions kept, one added)
- Defect: clause (iv), the consequence, the technical and lay levels and the one-liner compared the shot term of
  the CONTRAST with A_s and called it index 3 without a conversion. Restated as conditional on hypothesis (FR)
  (flat slice, deposit at rest); a marked note gives the three readings with their indices and sizes; every
  inequality and number of (i) to (iv) is unchanged. Two imported Facts added to its uses (plain uses edges, no
  assumes edge). Evidence: check.py::check_conversion_readings_of_the_shot_term (exact series projection, the
  three readings on rational data, the thermal ratio 3/16, the numbers).
- It is self-contained (it cannot pin SA's proposal, which is not in the store). After acceptance of SA's
  conversion theorem the maintainer should add a uses edge to it and may shorten the note.
- LABELS TO HARMONISE in the fix round: mine (FR), (FM), (UE) in P3 and (C0), (C1), (CA) in P2; SA's (LC) with
  matter at rest, (LC), (UE). Same three readings, same coefficients (checked against SA's filed text: 1/16,
  (1 + 12 X^2)/16, (9/4) X^4, and the sign change of zeta under the flat reading at rest).

### 3.10 S4, the tower as a cascade (one paragraph, as instructed): DEAD
No stored map takes rungs or tower floors to comoving scales. Searched: every entity naming rungs together with
comoving, wavenumber, Hubble length or scale factor (three hits, none a map: the dating, the asymmetry
register, the tree-level couplings), and every entity naming a dilatation together with tower planes or floors.
The stored rung-frame boost is the real-rapidity flow of 2 T_3R, an internal flow
(synthesis.majorana-scale-not-carried-by-rung-frame-boost); the dilatation in the frozen point's stabiliser acts
on the slice, not on rungs; the pair channel is one shell with no spatial mode (10 November). And by P1 the idea
cannot be rescued without that map: a state with one independent, identically distributed bit per rung is
invariant under relabelling of rungs, so it supplies two numbers and every dependence on scale is the
embedding's; "equal variance per logarithmic interval" is then exactly the assumption that rungs sit at equal
logarithmic spacing in k, which is the answer put in by hand. K8 not triggered. Not to be reopened without a
stored rung-to-scale map.

### 3.11 Kill conditions: outcome
K1 not triggered (no selector found; nearest candidate is s2, conjectural). K2 not triggered (S1's (A)
conversion stands, 9/4, growing mode). K3 passed (135/(pi^4 g) confirmed; A_s at 3.7e9 GeV). K4 TRIGGERED AS
PREDICTED: the stored index 3 is not the index of a thermal deposit on a flat slice (it is +1) unless the
deposit is at rest. K5 second clause triggered (the store's deposit is not pure; S2 is a row about a deposit the
stored state rules do not produce). K6 not triggered (S3 proved, sharpened). K7 not triggered under flat
readings; under (A) the count closes nothing. K8 not triggered (S4 dead).

### 3.12 What was killed
- S1's extra hypotheses "matter at rest, no shear" (not needed; and "all three at once" is automatic).
- S1(A) as a SPECTRUM on an unbounded slice (inadmissible in the infrared; it survives as a bound with an
  infrared end, argued).
- The stored "index 3" for mixed deposits on a flat slice (it is +1), and the stored unconditional "far below
  A_s" (true under the flat readings only).
- S2 as a statement about the store's deposit (the I-state is mixed; pair purifications that gravitate double
  the energy noise).
- S3's wording for extended profiles (restated to the form-factor statement).
- S5's closing under (A).
- S4.
Not killed: the dichotomy itself (S1's main lead), the thermal number, S3's core, S5 under flat readings.

## 4. Unexpected links

L1. The store already holds both conversions for one white energy noise: index 3 in the quasi-free result and
    "an extensive capacity gives -1" in synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-
    window(i). Neither names its slice. (Found independently by SA.)
L2. Under (A) the ceiling on T_d from the thermal white term at the present Hubble scale, about 1e9 GeV, falls
    within a factor of two of the stored (R) ceiling 7.3e8 GeV of
    synthesis.untuned-fit-caps-lightest-heavy-neutrino, which comes from the lightest heavy neutrino of an untuned
    Pati-Salam fit under Premises (EW) and (R) and has nothing to do with the spectrum. At 7.3e8 GeV the white term is about a third of the measured power at k = a_0 H_0 and 1.6e-3
    of it at the pivot. Two unrelated ceilings agreeing to a factor of two is recorded as a coincidence, NOT as
    evidence; a low-multipole likelihood would turn it into a real bound or a real tension under (A).
L3. (A) versus (B) is the flatness question asked patch by patch. The series has no reason for the flatness of
    the descended field (the record's Omega is taken as given), so it has no reason for (B) either. A derivation
    of spatial flatness from the frozen point that worked locally would select (B); one that worked only
    globally would leave (A).
L4. The nearest stored thing to a selector is the dating's second reading of the join, "the scale factor
    continuous": if read as continuity of the slice's whole first fundamental form from a flat frozen-point
    slice it gives a flat descent slice, reading (B). The primary reading (F) states no join condition.
L5. Tod's isotropic singularities (from memory): if the descent were AT the conformally regular origin of the
    tame-wall result, only the growing mode would be admissible and the free datum would be the wall's conformal
    3-geometry, with the comoving contrast zero at the wall. Then "deposit" has no matter datum and the spectrum
    is a property of the wall's geometry. The store places the descent at finite T_d, so this is a different
    picture; it is the picture in which S3's conclusion bites hardest (the datum must be a 3-geometry with
    separations in it).
L6. P1 and the ladder states: the store's own non-Gaussian collective states are exchangeable, so by P1 they are
    white on any slice. The 10 November item "non-Gaussian entangled states such as the families sector's
    frozen vacuum of bosonic face modes, if deposited" is therefore closed for every such state that is
    permutation symmetric in its blocks, as far as shape goes (amplitude aside).
L7. Under the flat reading with momentum noise a sparse deposit reaching A_s at 1 MeV consists of lumps of a few
    percent of a Hubble mass, the mass scale of primordial black holes at formation. Poisson noise of such
    lumps as a source of large-scale power is a known idea in the literature (from memory, not checked); it is
    outside the quasi-free class of fields and outside the series.

## 5. Decisions for Leon

D1. Accept the restatement of synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise (version 5)? It names a
    hypothesis, (FR), in the text of a proved result and makes four sentences conditional on it. No status
    changes, no assumes edge, no new postulate entity. Recommendation: accept; the stored text compared two
    different quantities.
D2. Whether to ADOPT a reading. Options: (FR)/(B) flat slice (the store's tacit one); (UE)/(A) uniform
    expansion; neither (record the dichotomy and leave the slice as a free datum of the descent, in the manner
    of the 1 November decision on the infrared datum). Recommendation: neither, for now. Nothing stored selects
    one, and adopting (B) to keep the old numbers would be choosing a premise for its consequence.
D3. If (A) is ever adopted or entertained: the window's ceiling. Under (A) a thermal deposit is excluded above
    about 1e9 GeV at the largest observed scale (3.7e9 GeV at the pivot), and at 1e12 GeV it is not a
    perturbation at all. Whether to record this as a conditional ceiling on T_d is Leon's call (it would be a new
    conditional prediction-like statement; SA's proposal carries the numbers).
D4. The criterion "quanta of the deposit have energies below the Planck mass" is used in P2 only as an argued
    reading. Whether to make it part of the Hadamard-deposit premise (HD), or leave it as a remark, is a premise
    decision.
D5. The junction reading L4 ("scale factor continuous" = first fundamental form continuous from a flat
    frozen-point slice) would select (B) if adopted as a premise of the join. Not recommended without a reason
    from the series; listed because it is the one stored phrase that points at a selector.
D6. Imports the accepted results would rest on, for the maintainer to create (I cannot): the linearised
    constraint equations and radiation-era solutions of cosmological perturbation theory (cited from memory in
    P2 and P3; SA's proposal derives them in the lab's GTG engine, which would remove the need); Tod's theorem
    on isotropic singularities and the 3-transitivity of the Lorentz group on null directions are mentioned
    only as remarks and need no import unless promoted.

## 6. Proposals filed (3 of 3)

P1 synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape           check4 0 errors
P2 synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta
                                                                                     check4 0 errors
P3 synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise (version 5, restatement)   check4 0 errors
Scratch: work/SB/ (proj.py, the three draft folders, patch_qf.py with qf_newcheck.txt which rebuilds P3 from
the stored files).

## 7. Next steps (not done)
- A low-multipole likelihood for an index -1 term under (A) (turns L2 into a bound).
- The energy structure factor of the store's actual deposit with partners placed on the slice (pairing case of
  the stored bound, clause (ii)); P2 covers gauge-invariant deposits only.
- General equation of state in the projection (only the radiation era was done here).
