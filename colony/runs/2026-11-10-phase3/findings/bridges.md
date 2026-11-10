# Bridges: run 2026-11-10-phase3

Status: complete (midway pass). Read: RUN.md, DECISIONS.md, attack-DA, SA, SB, MA, MB in full; attack-QA (outline,
Q4 graviton list, links, decisions); attack-QB (partial file, links pending). Nothing filed, nothing in store/ or
proposals/ touched. Labels: proved / computed / argued / dead. "By cone" means the dependence edges uses, assumes,
founded_on, specialises, derived_from of build/graph.json (the baseline build), walked by work/bridge/cone_lib.py.
Exact checks: work/bridge/bridge_checks.py (Fractions only, runs in under a second).

Three findings the attackers did not have, in order of weight:
1. A stored structure with late-time equation of state different from -1 exists and was missed by cluster D's search:
   the standing-R3 branch with a static hidden direction, w = -1/4 for 31.6 per cent of the dark matter (link B7).
2. Postulate D is NOT in the dark-energy exposure cone by edges; the link is text only (link B3).
3. The letters (P1) and (P2) name two unrelated pairs of premises, and the findings files use both without marking
   which (link B5).

## B1. Exact w = -1 against a quasi-de Sitter origin of the tilt (SB link 2, SA link 2; clusters S and D)

Statement tested. "The series' w = -1 and a red tilt from a de Sitter-like stage exclude each other within the
stored structures" (SB, R3, labelled argued).

Test. Stored-entity read plus one exact identity.
- The no-go half is already a stored theorem. synthesis.frozen-phase-spectrum-not-red (version 4, proved): (i) the
  dilatation of the flat slicing lies in the frozen point's stabiliser; (iii) every unitary-series weight gives
  n_s >= 1, a red tilt needs a real weight 0 < w < 1, m^2 < 0; (iv) under the promotion d Lambda = 0, so the frozen
  point's spatial transform is supported at k = 0. Its closing sentence already names the way out: the state must
  break the dilatation, "the source amplitude then changing by the fraction (1 - n_s)/2 per e-fold". That is SB's
  "clock on the frozen point". synthesis.promoted-norm-one-global-pair (version 5, proved) clause (ii) gives
  d lambda = 0. So SB's sentence restates stored clauses (iii) and (iv); it is not a new result.
- Exact identity (computed): on a constant-w expanding power law, n_s - 1 = 6 (1 + w)/(1 + 3w). It vanishes exactly
  at w = -1, is red for -1 < w < -1/3 and BLUE for w < -1. At w = -20117/20351 it is -351/10000 (SB's number
  recovered). In SA's one equation the de Sitter stage (f, kappa, P) = (-3, kappa, 0) is red iff kappa > 0.

Verdict. Split.
- "On the exact frozen-point de Sitter stage no series field gives a red tilt, and the promoted norm supplies no
  local source": PROVED, stored. Cite it; do not refile.
- "A measured w != -1 and a red tilt would be the same missing structure": ARGUED, and weaker than stated, for
  three reasons. (a) Epochs: the tilt needs 1 + w = 234/20351 during exit of the observed modes; the registered
  prediction concerns the late universe. They are one structure only if the frozen point's own stage is the exit
  stage, and then SB's own R3 gives amplitude about 1e-122 and stored row 10 says the observed modes are inside.
  (b) Sign: the identity gives a red tilt only for w > -1. The survey best fits (DA's table: w0 = -0.82,
  wa = -0.63) have 1 + w = +9/50 today and -9/20 as a -> 0, crossing at a = 5/7. A clock of that kind is blue on the
  phantom side. The data do not point at "the" clock the spectrum needs. (c) No curvature perturbation at
  epsilon = 0 is textbook (pump field proportional to sqrt epsilon), not stored.
- What w = -1 does NOT exclude: a quasi-de Sitter stage driven by something other than the frozen point. The store
  has no such field; that is absence, not exclusion. Under the promotion one further sentence is available and
  unstored: d lambda = 0 on a connected solution forbids an early stage with a different value of the same
  constant (argued).

Referee should check: that SB's proposal and SA's ledger row 9/19 cite frozen-phase-spectrum-not-red for this and
claim nothing beyond it; that no text says w = -1 "forbids inflation".

## B2. The neutrino-mass floor coupled to w = -1 (DA link 2; clusters D and the stored predictions)

Stored entities. pred.neutrino-mass-sum-floor (version 2, live): sum at the normal-ordering floor, about 0.059 eV,
under Premise (H). Kill condition as stored: "Below: a physical-prior cosmological bound confirmed below the floor,
or confirmed inverted ordering. Above: a sum determined meaningfully above the floor (near 0.075 eV), or m1 measured
above a few meV". neutrino.double-prediction-sum-predicted-floor (version 1, status conjectured): "This framework
cannot use that option [evolving dark energy] ... The two stances are therefore one joint prediction ... within the
frozen-point cosmology the neutrino-mass tension must resolve at the floor".

Test (by cone, computed). The past cone of pred.neutrino-mass-sum-floor has 115 entities and contains none of: the
field-space premise, dark-energy.vacuum-region-registration-condition, pred.dark-energy-w-minus-one,
dark-energy.frozen-point-makes-stelle-west-vector, the frozen-point geometry Fact. The double-prediction claim has
no dependence edge at all (three motivated_by edges, one to the registration condition). pred.dark-energy-w-minus-one
does not mention neutrinos. So the coupling exists only in the text of a conjectured claim.

Joint exposure, stated exactly.
- Logically the floor (seesaw plus (H)) is independent of w = -1. What is coupled is the confrontation.
- The coupling is anticorrelated. With w = -1 held, the bounds on record are 0.064 eV (DESI DR2 with CMB) and
  0.049 eV in one full-shape reanalysis, the second below the floor. With (w0, wa) free the same data give 0.077,
  0.111 (stored) and 0.18 eV (DA, from the DES paper; not rechecked here), all above the floor.
- So: if w = -1 falls at the registered threshold, pred.dark-energy-w-minus-one dies and the floor prediction is
  relieved, not killed. If w = -1 stands, the floor is the prediction under pressure. The conjunction (the "fourth
  registered stance") fails if either fails; it survives only if LCDM bounds saturate at or above 0.059 eV.
- The defect: the floor's kill condition does not name the cosmological model in which the bound is derived. Under
  Leon's five-sigma rule w = -1 will "stand" for the series through a period in which the field quotes relaxed
  w0-wa bounds. Read with the series' own cosmology the kill is tighter (LCDM bounds count); read with the field's
  it is looser. The stored text of the double prediction ("within the frozen-point cosmology") implies the first.

Verdict. COMPUTED (cone) for independence; ARGUED for the exposure reading. Not one result: two predictions and one
conjectured conjunction.

Referee should check: the 0.18 eV figure at source; that the DA registration text for w = -1 does not silently change
which bound counts against the floor.

## B3. Dark-matter postulate D inside the dark-energy exposure cone (MA link 2, DA table row; clusters M and D)

Test (by cone, computed). dark-matter.d-democracy-total-mass: past cone empty; dependants
dark-matter.democracy-de-sitter-radius-unit-ball (assumes D, R3) and dark-matter.two-reductions (uses
dark-matter.imported-induced-equations-hypersurface, assumes D). None of the three is in the future cone of the
field-space premise (2 entities), the registration condition (1), dark-energy.frozen-point-makes-stelle-west-vector
(156), the frozen-point geometry Fact (227) or the Henneaux-Teitelboim Fact (80). The stored Fact that defines the
radius, dark-matter.imported-frozen-point-de-sitter-radius (future cone 21, itself in the cone of the frozen-point
geometry), is used by neither dependant. Text: D's formal says "the same total mass on its de Sitter sphere" and
cites nothing; of the 23 postulate texts D is the only one that names the de Sitter radius or Lambda (grep over all
23).

Verdict. DEAD by cone, ARGUED by text. The link is real in content (D's unit is the de Sitter radius, so it needs a
constant Lambda) and invisible in the graph. DA's table already had to add it by hand. This is the same
under-recording DA reports for (FS): the exposure cone computed from edges is a lower bound.

Referee should check: nothing. Maintainer: one edge (Decisions 3).

## B4. Released norm's equation against the promoted norm's clock density (DA link 1; cluster D and stored)

Test (computed, exact). From the reduced functional on the isotropic family, L = 24 (u y' - n s)(y^2 - s^2/u), which
equals DA's 24 n s^3 u (alpha - 1/u)(beta - 1/u): dL/dn = -24 s^3 (beta - 1/u), dL/ds = 24 n s^2 (3/u - 2 alpha -
beta), dL/du = 24 n s^3 (alpha beta - 1/u^2) (three rational samples; the y-equation gives 2s(s' - n y) = u' y^2 by
hand). On the frame equations with a fluid, 24 (alpha beta - 1/u^2) = E - (8/3) Lambda^2 = (4/3)[Lambda (rho - 3p) -
rho (rho + 3p)] on 27 rational samples, the stored display of synthesis.promoted-norm-weyl-clock-flat-weight (v)
(version 7, proved).

Verdict. ONE result, PROVED, and by definition rather than by coincidence. Stored clause (iii) defines the clock
density as "the derivative of the Lagrangian in u at fixed frame and connection". Releasing u locally sets that same
derivative to zero. Promotion: dL/du is the rate of the conjugate time. Release: dL/du = 0. So "the released norm's
equation is the clock density set to zero" is an identity of one function read under two variational principles.
Consequences already stored and recovered by DA: the dust zero "only at 8 pi G rho = Lambda" (stored (v)) is DA's
tracking solution; "the conjugate time does not advance where the Weyl part vanishes" (stored (iv)) is DA's vacuum
degeneracy F = 0 with free u. What DA adds that can fail: the frame equations keep their algebraic form with
torsion solved and u varying (u' enters only the torsion equation), so the stored polynomial is unchanged off the
torsion-free, constant-norm solutions.

Referee should check: that the check of clause (iii) in DA's proposal tests that extension (frame equations with
torsion) and not the identity dL/du = dL/du; the proposal text correctly says "1/24 of the density", so the wording
is sound. One sentence should say the equality with the stored display is definitional.

## B5. The Milne wall, Tolley-Turok matching, and the premises called (P2) (SB link 1, MA link 3; clusters S and M)

Stored entities (read).
- synthesis.pre-descent-state-carried-into-descended-phase-premise (version 1, postulate, subject dark-energy):
  "(P2) of the Kasner exit": a rule exists carrying the exited state across the wall or the descent; "it does not
  give its form". Dependence cone: past 0, future 0.
- dark-matter.p2-indifference (version 2, postulate): equates sector labels along the reversal orbit. Future cone 151.
- scrambling.indifference-structural-premise-series (version 2, postulate, subject programme): "forbids uncaused
  structure". Future cone 232.
- Likewise (P1): synthesis.pre-descent-contracting-kasner-stage-premise (Kasner exit) against
  dark-matter.p1-single-frozen-point.

Test 1 (by cone, computed). Future cones: Kasner (P2) and dark-matter P2 share 0 entities; Kasner (P2) and the
programme premise share 0; dark-matter P2 and the programme premise share 121, with no edge between the two (neither
is in the other's cone). So MA's "one premise held twice" is quantified: 121 entities carry both.

Test 2 (exact, computed). At the five-dimensional Milne end a mode with no hidden momentum obeys the order-0 Bessel
equation in k tau. Write solutions a J_0 + b Y_0 in k|tau| on each side. The Klein-Gordon form with measure |tau|
has opposite sign in that basis on the two sides, so a matching is canonical iff its determinant is -1. The
logarithm gives two continuations, Y_0 -> Y_0 +- 2i J_0. Then, as 2x2 matrices over the Gaussian rationals:
- positive-frequency mode continued one way and its conjugate the other way: J -> -J, Y -> Y, real, det -1, the
  incoming positive-frequency mode goes to minus the outgoing one: no mixing. This is the Tolley-Turok rule;
- the opposite pairing: J -> 3J, Y -> Y, det 3: not canonical;
- one branch for both frequencies: det +1 and not real;
- the equal-weight average of the two branches (the uniform weight on the two-element orbit, which is what the
  stored theorem synthesis.indifference-is-curie-plus-single-valuedness (2) returns for an invariant weight):
  J -> J, Y -> Y, det +1: anti-canonical, it sends the positive-norm incoming mode to a negative-norm outgoing one;
- real canonical rules form a family: J -> -J, Y -> Y + c J has det -1 for every c and |beta|^2 = c^2/4 (checked at
  c = 0, 1, -3/2). Covariance under conjugation (the Curie half of indifference) is satisfied by all of them.

Verdict. HOMONYMS, and DEAD as an identification. The three "P2" are three premises: an existence clause for a
matching rule; a scoped equality of labels; a programme-level principle. The Tolley-Turok rule is a candidate FORM
for the first. It is not an instance of the third: indifference as covariance does not select it (a one-parameter
family at least survives), and indifference as equal weights on the two continuations gives a rule that is not
canonical. What selects it is analytic continuation paired with the frequency sign, a separate assumption. Given
analyticity, reality and canonicity it is unique at order 0 (computed). Scope: order 0, zero hidden momentum; the
sign of the form on the contracting side is my derivation (measure |tau|), not a stored statement; the content of
Tolley and Turok is taken from SB's reading, not reread.

Consequence for S: with that rule nothing is created at the wall, so the Kasner route with (P1), (P2) in this form
is definite and blue (SB R1). Each other member of the family adds a k-independent occupation c^2/4 per mode, a
free number.

Referee should check: wherever a findings file or proposal writes "(P1)" or "(P2)" which pair is meant (DA's table
row "dark-matter" uses the dark-matter P1; SB R5 item 5 and SA Decision 4 use the Kasner P1).

## B6. Where the store names a graviton (Leon's position: the graviton does not exist)

Method: text search for "graviton" over all of store/ (89 files, 51 entities plus 5 top-level files); one sentence
per entity; reported, not extended. Ids ending in "(id only)" contain the word only inside another entity's id.

(a) Kinematics (helicity and homogeneity tables; joint J1)
- hawking.helicity-lift-joints-itemised: "photon kinematics are at homogeneities -4 and 0 (s = +-1), graviton
  kinematics at -6 and +2 (s = +-2)".
- scrambling.imported-collars-coframe-exceptional-set-helicity: "two channels at homogeneities -2s - 2 (-4 and 0 for
  the photon, -6 and +2 for the graviton)".
- note.hawking.point-contact-weinberg-witten-triage: "The bosonic sector's lift contains a graviton candidate
  (homogeneities -6, +2 ...), and a composite graviton must answer [Weinberg-Witten]".
- note.hawking.setting-introduction, note.hawking.setting-what-proved-what-imported-what: "the composite-graviton
  triage".

(b) Channel count (the spin-2 clause of J3; horizon channels)
- hawking.joint-j3-s-wave-reduction (postulate, version 2): "For the even-parity channels of the massless spin-2
  field, the graviton, the near-horizon reduction ... identifies each (omega, l, m)"; "the photon's channels begin at
  l = 1 and the graviton's at l = 2". Future cone 31, including pred.boundary-mode-density.
- hawking.helicity-lift-joints-itemised: "the channel-reduction step is premise only for the even-parity channels of
  the graviton".
- synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional: "The two graviton channels
  per (omega, l, m), l >= 2, are the count used for eps = 1".
- synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature and
  synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet: "derived ... for the odd-parity channels of
  gravitons, and assumed through J3 only for their even-parity channels".
- open problems op.helicity-per-boundary-mode, op.counted-mode-energy: "the channel-reduction clause is assumed for
  spin 2 only, the graviton's channels"; "integer-weight fields (the photon, the graviton, scalars) lie outside the
  CAR count".

(c) Counting readings (additive, eps = 1)
- synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free: "twelve vectors, eight rung components
  and a graviton reads 34 <= 16 n_g and gives n_g >= 3"; "passes two generations unless the graviton is counted".
- synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content (title: "with additive
  bosons, scalars and graviton set the verdict"): "a graviton counted additively, as J3's species list would have
  it, makes every content fail".
- open problem op.qft-structural-inputs: "fails for every content once the graviton is counted"; "If the
  integer-weight fields (gauge bosons, the Higgs, the graviton) share the sea it is 78".

(d) Processes and rates (emission or exchange of a graviton; more than a count)
- dark-matter.imported-massless-graviton-production-rate (imported): "Dark matter produced from the Standard-Model
  plasma by massless graviton exchange has rate per volume R(T) = alpha T^8 / M_P^4". Future cone 31 entities,
  including the live predictions pred.no-dark-radiation and pred.no-indirect-dark-signals; NOT in the past cone of
  the fitted total (unit-ball-rule, total-function-thickness, population-count).
- its users: dark-matter.seeding-gravity-floor-dark-towers-temperature ("heated by graviton-mediated production"),
  dark-matter.coefficients-floors-they-give-what-gravity ("graviton-mediated heating gives temperature floors"),
  synthesis.seeding-remainder-excludes-perturbative-pati-salam (proof: "a tower heated by graviton-mediated
  production at rate c T^8/M_P^4"), synthesis.untuned-fit-caps-lightest-heavy-neutrino (id only),
  dark-matter.radiation-audit-what-theorem-closes-what (check: "the mirror's larger graviton-rate coefficient").
- pred.no-indirect-dark-signals: "annihilation products only at the rate of graviton exchange, suppressed by powers
  of E/M_P".
- synthesis.dimmed-burst-time-rescaled-copy and pred.dimmed-evaporation-bursts: "against the standard expectation
  (this tower plus gravitons) the factor is D = (2 + g + o)/(1 + g), at least 2 only if the odd towers emit at least
  as much as the gravit[ons]". Open problem op.odd-towers repeats it.
- note.standard-model.what-settled-what-gravitational-channel-cannot: "contributes to the running of a gauge
  coupling only through graviton loops, which are suppressed by (mu/M_P)^2".
- notes that refer to the rate: note.dark-matter.setting-levels-results, setting-machine-verification,
  setting-position-series, setting-premises-attacked-what-would-refute (id only),
  setting-seeding-gravity-why-no-coupling (id only); quantity.reduced-planck-mass ("the graviton-rate Fact").

(e) Ontology readings (the graviton as a collective mode, or left open)
- dark-energy.acoustic-no-go-one-way-grip: "The graviton mode is T ... the linear susceptibility of the graviton
  mode to O vanishes identically". Future cone 63, five live predictions.
- dark-energy.lift-inherits-no-go-steps-itemised: "the four-dimensional two-point function between the graviton mode
  and any probe decomposes over partial waves".
- dark-energy.conclusion-does-not-depend-ontology-level: "holds on either reading of the graviton's ontology ... If
  the graviton is the framework's collective mode ... If the graviton is fundamental: by Weinberg's soft theorem".
- dark-matter.imported-gravity-only-coupling: "zero linear overlap with the graviton mode". Future cone 59.
- note.dark-energy.setting-introduction, note.dark-energy.setting-one-way-grip-acoustic-no ("If the graviton is a
  collective mode of the boundary-mode pairs, an acoustic mode of the correlations"),
  note.mass.point-contact-what-gravity-why-everything ("the action paper leaves the graviton's ontology open").

(f) Polarisation count of the classical field, and quantised linear modes of it
- dark-energy.point-infinity-has-no-physical-fluctuation: "the graviton carries no (delta I, delta V) polarisation".
- synthesis.promoted-norm-one-global-pair: "the graviton still carries no (delta I, delta V, delta lambda)
  polarisation"; lay: "the graviton count is untouched".
- synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling (proof and check
  only): "graviton cross mode at isotropic point has order 0"; "unlike a graviton, whose strain is the physical
  amplitude". Here the off-diagonal modes of the gravitational field are given an adiabatic vacuum, that is, they
  are quantised, without the word appearing in the entity text.

(g) Prior art and names (no quantum of the series implied)
- correspondence.imported-nonlinear-graviton, correspondence.googly-localisation-quartic-order,
  correspondence.no-real-lorentzian-vacuum-half-flat, synthesis.quartic-ordering-tensor-locally-trivial, and notes
  note.correspondence.boundary-stated-plainly, setting-nonlinear-graviton-boundary-googly-conjecture,
  setting-ordering-quartic-order-ordering-insensitivity, setting-prior-art, setting-what-proved-what-imported-what,
  setting-contribution: Penrose's "nonlinear graviton", a classical construction.
- synthesis.imported-null-plane-modular-hamiltonian-first-law: "stated for spinors, Maxwell and linearised
  gravitons".
- synthesis.weyl-flat-variations-carry-only-the-stress-trace-...: "Weinberg's soft-graviton universality ... read
  classically".
- note.hawking.setting-prior-art, note.dark-energy.setting-prior-art ("graviton-photon conversion ... Gertsenshtein").
- Top-level files: references.yaml (Penrose76, Weinberg1964), labels.yaml (T09 and T14 labels), tags.yaml (three tag
  descriptions, one reading "the graviton and its absence or production"), notebook.yaml entry qg-peierls ("Does
  microcausality fix the free graviton field's unit of action to the matter's?").

Cross-cluster consequences of the position (each one line, tested):
- Cluster S (computed by cone): three rows of SA's ledger have the graviton-exchange rate in their past cone: row 16
  (synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window) and row 17
  (synthesis.pati-salam-chain-defects-cannot-source-spectrum), both through
  synthesis.untuned-fit-caps-lightest-heavy-neutrino; row 18 (synthesis.adiabatic-deposit-modulation-is-a-time-shift)
  through dark-matter.stored-asymmetry-charge-not-number. Rows 2, 3 and 23 (cross modes) and SB's remarks on the
  tensor-to-scalar ratio (R1 remark, R3 "textbook graviton spectrum", R5 item 4) use a vacuum state for the tensor
  modes. With the gravitational gauge fields not quantised those are not available as in-series arguments (argued).
  SB's R1 result itself (the curvature perturbation zeta = u/3, fixed by the constraints from the matter field) does
  not need them.
- Cluster M (computed by cone): synthesis.indifference-is-curie-plus-single-valuedness, the theorem MA uses to read
  P2 as a specialisation, has the rate in its past cone (through dark-tower-matter.mirrors-temperature-p2 and the
  seeding floor). The exclusion of xi = 1 that forced P2's rescoping rests on that floor.
- Stored prediction (computed): at g = 0 the dimming ratio is D = 2 + o, at least 2 for every o. The stored
  condition "at least 2 only if the odd towers emit at least as much as the gravitons" then drops out.
- Not examined: whether the element reading (geometry's coefficients in the commuting algebra of the matter's
  number operators) reproduces the T^8/M_P^4 rate as a matter-matter process with no quantum of the field. That is
  the question that decides group (d).

## B7. A stored structure with w different from -1 that cluster D's search did not list (clusters M and D)

Stored (read): synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands (version 1, proved,
subject dark-matter; cited by MB for another purpose). Clause (ii): with R3 standing and a static hidden direction
the five-dimensional towers' projected density goes as a^(-9/4), "an effective equation of state w = -1/4 ... (no
pressure is derived)", for a fraction between 0.316 and 0.317 of the dark matter.

Test (computed; Omega_dm = 0.265 and Omega_Lambda = 0.685 from memory, not stored Facts). Read that component
together with the constant as one "dark energy": w(a) = -1 + (3/4) r/(1 + r), r proportional to a^(-9/4); today
w0 = -0.918, wa = +0.164. It never crosses -1 and wa is positive; the survey best fits have wa negative (-0.4 to
-1.75 in DA's table). The share grows by a factor between 189 and 190 since 1 + z = 1090 (189^4 < 1090^3 < 190^4,
exact), so the matter density inferred at recombination and today would differ by about 30 per cent (argued:
excluded by the agreement of the two at the per cent level; not computed against data).

Verdict. COMPUTED that it exists and what it gives; ARGUED that it is no fallback (wrong sign of wa, and the
matter-density mismatch). It bears on two of DA's texts: the findings sentence "no stored entity proposes an
evolving dark-energy density" needs this entry in its list (it is an evolving dark component with w = -1/4, found
under "effective equation of state", none of DA's search words), and the stored kill condition's clause "with no
parameter available to absorb it" should be read against the exponent beta of the hidden direction, which is such a
parameter in a stored, unadopted branch. DA's proposal makes no claim about the whole store, so the proposal is
not affected.

Referee should check: DA's D3 item (3) and Decision 4 ("the series has no fallback") name this branch and say why it
is not one.

## Smaller links, tested in one line each
- B8 (SB link 3; computed). Boundary amplitude against the horizon entropy: P = 2 lambda H^2/(pi M_Pl^2) and
  S = pi N^2 with N^2 = M_Pl^2/H^2 give P S = 2 lambda exactly. Nothing new, as SB says; it is the reason no boundary
  count reaches 1e-9.
- B9 (SA link 2; argued, not a link to D as stated). The exponent 6 of the running in the dust-plus-constant
  contraction comes from a constant Lambda. This is a property of a stage the store does not hold; no test possible
  against a stored entity.
- B10 (MB link 4; computed by cone). The programme's indifference premise is assumed directly by five results:
  dark-energy.imported-walls-sphere-theorem, dark-energy.lift-inherits-no-go-steps-itemised,
  families.imported-indifference-instrument, one-relation.imported-indifference-instrument (which also assumes
  dark-matter P2) and scrambling.principality-indifference-sphere. If P2's scope note is copied to the programme premise, these five
  are the places to check that the unrestricted form was not used.

## Not tested (said so that no one assumes otherwise)
- RUN.md's suggested bridges "local covariance against the horizon states" and "the protraction identity against
  the dark-matter slices": QB's file was partial (links pending). A grep finds no use of the Bianchi or protraction
  identity in dark-matter, dark-tower-matter or simulations entities, so the second has no stored anchor (dead by
  search). The first was not examined.
- "The de Sitter boundary modes against the window results of phase 2": only B8; phase 2's report was not read
  beyond its headings.

## Leads for the attackers (for the orchestrator to relay)
- DA: B7 (add the w = -1/4 branch to D3 and to Decision 4); B3 (D is outside the cone by edges: say "by text");
  B2 (the model in the floor's kill condition); B4 (one sentence that the equality in clause (iii) is definitional).
- SA and SB: B1 (cite synthesis.frozen-phase-spectrum-not-red (iii), (iv) for the w = -1 remark; the sign point);
  B5 (mark which (P1), (P2)); B6 consequences for rows 16 to 18 and for the tensor-ratio remarks.
- MA and MB: B5 test 1 (121 shared entities, no edge); B6 (the theorem behind the P2 specialisation rests on the
  graviton-exchange rate); B10.
- QA: B6 groups (d) and (f) extend the Q4 list: pred.no-indirect-dark-signals, pred.dimmed-evaporation-bursts,
  the notebook entry qg-peierls, and the quantised cross modes of the Kasner results.

## Rejected
- "Exact w = -1 and the red tilt are one missing structure" as a result: rejected as stated (B1: epochs differ,
  sign differs, the no-go half is stored).
- "Tolley-Turok matching is the indifference premise at the wall": rejected (B5, computed).
- "D is in the exposure cone": rejected as a cone statement (B3); kept as a text statement.

## Decisions for Leon
1. Graviton, group (d), the one with consequences. The seeding rate alpha T^8/M_P^4 is imported as graviton
   exchange and sits under 31 entities and two live predictions; pred.no-indirect-dark-signals states graviton
   exchange as its only annihilation channel; the dimmed-burst baseline counts graviton emission. Decide whether
   "the graviton does not exist" (a) keeps these as processes of the classical field sourced by matter operators
   (then the rate Fact needs rewording and a derivation in that reading is owed), or (b) removes them (then the
   seeding floor, the cold-mirror exclusion behind P2 version 2, and the two predictions lose their basis).
   Recommendation: (a) as the working position, recorded as owed, with no change to the store until the element
   reading is shown to give the tree-level rate.
2. Graviton, the dimmed-burst prediction. With no graviton emission the ratio is D = 2 + o and the stored proviso
   disappears. Recommendation: restate pred.dimmed-evaporation-bursts with g = 0 only after decision 1, since it is
   the same question for emission.
3. Graviton, groups (a), (b), (c), (e), (f). Wording passes, none urgent: (b) and (c) are the places DECISIONS.md
   already names; (e) is where the store itself offers a reading without a fundamental graviton (the collective
   mode T) and says its conclusion holds "on either reading": decide whether the fundamental-graviton branch of
   dark-energy.conclusion-does-not-depend-ontology-level stays as a stated alternative. (f): "the graviton carries no
   polarisation" can read "the gravitational field has no further polarisation". The Kasner cross modes are
   quantised in the stored spectra; decide whether those rows stand as spectator-equivalent mathematics only.
   The notebook entry qg-peierls asks a question about quantising the free graviton field; decide whether it is
   closed as out of position. Recommendation: one maintainer wording pass after decision 1; close qg-peierls with a
   note rather than delete it.
4. Record D's dependence on Lambda by an edge: dark-matter.democracy-de-sitter-radius-unit-ball and
   dark-matter.two-reductions `uses` dark-matter.imported-frozen-point-de-sitter-radius (maintainer-only).
   Recommendation: yes; with DA's Decision 3 it makes the exposure cone show what the data would take.
5. The floor's kill condition (pred.neutrino-mass-sum-floor): name the cosmological model. Recommendation: "a
   physical-prior bound derived with w = -1, while pred.dark-energy-w-minus-one stands by its registered rule";
   and give neutrino.double-prediction-sum-predicted-floor a dependence edge to the registration condition, or
   keep it conjectured and say on both predictions that the confrontation, not the derivation, is coupled. This
   is the stricter reading and the one the stored text implies.
6. The w = -1/4 branch (B7): add to the dark-energy record that the one stored structure with a late-time
   equation of state other than 0, 1/3 and -1 is the standing-R3 branch with a static hidden direction, that it
   gives (w0, wa) near (-0.92, +0.16) if read as dark energy, and that it is not adopted. Recommendation: yes,
   before the registration of the five-sigma rule, so that "no parameter available to absorb it" is true as
   written.
7. Names: rename or always qualify the two pairs (P1), (P2) ("Kasner-exit (P1), (P2)" against "dark-matter P1,
   P2"). Recommendation: yes, at the next maintainer pass; two findings files of this run already mix them.
8. P2 and the programme's indifference premise: MA and MB recommend a `specialises` edge. Add to that decision the
   count (121 entities under both) and the five direct users of the programme premise to recheck (B10).
   Recommendation: as MA and MB, with MB's scope note.
9. Tolley-Turok matching as a note on the Kasner-exit (P2) (SB's Decision 4): if recorded, record it as "the unique
   real canonical rule given analytic continuation, at order 0", with the one-parameter family of other canonical
   rules named, and not as a consequence of indifference. Recommendation: as SB, a note, not a premise.
