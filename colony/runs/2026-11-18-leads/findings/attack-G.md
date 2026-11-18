# Findings, cluster G (the gravitational field), run 2026-11-18-leads

One attacker, both angles. Problem: op.gravitational-field-at-null-momentum (four attack items), the trace-free
channel item of op.einstein-from-the-field-theory, the basis of pred.dimmed-evaporation-bursts (term g).
Work files: colony/runs/2026-11-18-leads/work/G/. Labels: proved / computed / argued / conjectured.
The floor's numbers (dark-matter.seeding-gravity-floor-dark-towers-temperature and the other entities owned by the
energy restatement) are being restated in this run by another agent; they are cited here as they stand.

## Orientation (read before computing)
- op.gravitational-field-at-null-momentum; the two stored results of 18 November in full (statement, proof, check);
  conventions "Gravity and the graviton"; field-theory.operator-newtonian-coupling@4;
  field-theory.no-canonical-commutation-relations-tower@3; singularity.c1-curvature-cutoff, singularity.c2-cell-density,
  singularity.stretched-singularity-count, scrambling.mode-count, synthesis.c-loc-local-horizon-premise;
  pred.gravity-entangles-standard-phase@2; pred.dimmed-evaporation-bursts@7 and its basis
  synthesis.dimmed-burst-time-rescaled-copy; op.einstein-from-the-field-theory and
  synthesis.weyl-flat-variations-...-trace-free-channel@1; synthesis.locality-of-the-attached-free-fields-...,
  synthesis.interacting-fields-of-causal-perturbation-theory-..., the Krein premise (KF);
  field-theory.fock-space-maxwell-modes; note.synthesis.where-stored-text-names-a-graviton; the notebook rows
  qg-radiated-record, qg-radiative-sector, qg-peierls; previous run's REPORT.md, findings, LEADS.
- The working notes of 12 October (QG_radiated_record, QG_radiative_sector, QG_peierls) are Project documents and are
  not in the repository; only their notebook rows were read. The notebook row says the draft's claim of safety "was
  withdrawn as resting on an assumed Planck-length floor".

## Routes considered
Lead 1 (state the condition). (a) lookup of every stored statement that mentions commutation at spacelike separation,
signalling, or locality, and what each is about; (b) from another subject: the causal perturbation theory result (its
interacting fields are local to every order: does its hypothesis cover the gravitational field?); (c) own: a
counter-model for "unitarity implies commutation", the slaved model itself written with its unitary. Chosen: all
three, they are cheap; (c) is the only computation.

Lead 2 (localisation floor). (a) the problem's own: derive a floor from (C1), (C2) or the mode count; (b) from the
literature behind the October notes (Belenchia et al.: the which-path record read by a probe whose position cannot be
resolved below the Planck length; cited from memory): a second-order effect on the visibility; (c) own: read the
stored failure operationally. A nonzero [phi, O] at first order is a first-order change of <O> under Bob's unitary
exp(-I lambda phi): a phase shift of Alice's fringe by a classical source in Bob's hands, which needs no localised
probe at all. Chosen: (c), with (a) as a lookup, because (c) decides whether a floor on localisation is the relevant
protection at all; (b) is recorded as the route not taken (it concerns a second-order effect that exists only if the
first-order one is absent).

Lead 3 (constraint and dressing). (a) one space dimension, a gauge field with no transverse part at all (the field is
the constraint's solution): cheap, but in one dimension the constrained field of a neutral rearrangement vanishes
outside it, so the answer would be an artefact; (b) two space dimensions, lattice Maxwell field with a Gauss
constraint, matter one quantum on two sites, recombiner dressed by a string (Wilson line) or by the constrained
(Coulomb) field; compare the field with transverse variables and the field without; (c) a symmetric-tensor lattice
field with the linearised Hamiltonian and momentum constraints: closest to gravity, too heavy for this run. Chosen:
(b), with (a) as a clause (the one-dimensional case inside the same code), and the spin-two constraint split done in
the algebra at fixed momentum under lead 4 instead of (c).

Lead 4 (the free part and g). (a) exact linear algebra of the stored Einstein map at null momentum: which two
directions, what the image is, where the pole is; (b) the constraint split in a frame (which components carry no
second time derivative); (c) the options for g read against the stored basis of the burst prediction. All three.

Lead 5 (trace-free channel). (a) lookup: (OS) states the whole stress map as source, so it assumes the clause; (b)
own: recompute the stored bilinear with a trace-only source normalised to the same Newtonian coupling, to see which
stored numbers use the trace-free channel. Both.

## Kill conditions (written 18 November before any computation of this run)

K1 (lead 1). The negative answer "no stored premise implies commutation of the gravitational field with matter
observables at spacelike separation" dies if a stored entity at its present version states or entails that
commutation for a field built from the matter's numbers (entities to read: the locality theorem, the Dimock and
Guido-Longo imports, the causal perturbation theory result, (KF), (C_loc), the Newtonian coupling). The independence
statement "unitarity does not imply it" dies if the slaved model's evolution is not a unit of the algebra with
inverse its reverse-type conjugate (U U^-1 = 1 fails) or if its commutator with the detection vanishes.

K2 (lead 2). Registered meaning of "cannot be observed": let eps be the largest change, over Alice's recombiners, of
her detection probability caused by Bob's choice between acting and not acting at an event spacelike to the detection.
The failure is unobservable in an experiment of N runs if eps * sqrt(N) < 1; for the proposed experiments (masses of
order 1e-14 kg, separations of order 1e-4 m, at most 1e6 runs) the registered threshold is eps < 1e-3.
 K2a. If in the lattice model eps has no term of first order in Bob's coupling at any spacelike event (the change is
 second order or zero for a classical source in Bob's hands), route (c) dies and the question returns to the
 visibility (second order), where a localisation floor could matter.
 K2b (control). If with the free part the same eps is nonzero at a spacelike event, the computation is wrong.
 K2c. The claim "a floor on localisation does not protect" dies if eps depends on the width of any wave packet of
 Bob's device, that is if the model's signal cannot be produced by a device with no quantum degree of freedom.
 K2d. The claim "(C1), (C2) and the mode count give no bound" dies if either premise at its pinned version constrains
 matter away from the cutoff surface of a hole, or if a stored result bounds the product of two masses or the phase
 G m_A m_B/(hbar c) from them.
 Prediction written before computing (for the gravitational transfer, argued): eps <= (1/2) Phi_s with
 Phi_s <= (G m_A m_B/(hbar c)) * D * |1/r_1 - 1/r_2|, about (m_A m_B/m_P^2)(d/D); for two masses of 1e-14 kg this is
 of order 1e-13, far below the threshold with no floor; for a classical source of a kilogram at a metre it is of
 order one.

K3 (lead 3).
 K3a. "A free transverse part with canonical commutators and a string dressing restore commutation" dies if the
 string-dressed detection fails to commute with the electric field on any link off the string at equal time, or at
 any event outside the string's cone.
 K3b. "The constraint and dressing alone do not restore it" dies if, in two space dimensions, with the field equal
 to the constraint's solution and no transverse variable, the field commutes with the recombined detection on every
 link away from the two sites.
 K3c (control on my understanding). In one space dimension the constrained field of the two paths must differ only
 between the two sites; if it differs outside, the model is wrong.
 K3d. The bare recombiner must fail to commute with the constraint and the dressed one must commute with it at every
 site; otherwise the dressing is wrong.

K4 (lead 4).
 K4a. "The free directions are the two transverse trace-free ones" dies if at a null momentum the kernel of the
 stored Einstein map is not the displacements plus the two transverse trace-free maps.
 K4b. "The equation at null momentum is solvable exactly when the source has no transverse trace-free part" dies if
 the image of the Einstein map at a null momentum is not the conserved sources that pair to zero with those two maps.
 K4c. "The other four are fixed by constraints, with no pole on the null cone" dies if for a conserved source at
 null momentum T - (1/2) id tr T minus its transverse trace-free part is not a displacement (so the curvature would
 have a pole in another component), or if the components of the Einstein map along a timelike direction e_0 carry a
 second power of the frequency.
 K4d. The dimension-three control: in Cl(1,2) the kernel at null momentum must be the displacements only (no free
 part in three dimensions); otherwise the count is not about helicity two.

K5 (lead 5). "The stored rate uses the trace-free channel, which the static coupling does not test" dies if the
trace-only bilinear normalised to the same Newtonian coupling gives the stored channel weights for the conformal
species (chiral fermions, vectors), or if the static bilinear separates the two channels.

## Results
(filled in below as each computation is run)

### Leads 4 and 5, computations (work/G/null_kernel.py, null_kernel2.py, null_kernel3.py)
Outcomes of the kill conditions: K4a not fired, K4b not fired, K4c not fired, K4d not fired, K5 not fired.
- computed, then proved in general (see the proposal's proof): at null k the kernel of the stored Einstein map is
  {h : h(k) = (1/2) tr(h) k} = displacements + the two transverse trace-free maps n_+, n_x (rank of
  displacements + tt = 6 = kernel, at (1,0,0,1), (5,3,0,4), (-5,3,0,4)).
- proved: the Einstein map is symmetric for the stored pairing (formula; computed at five momenta), so its image at
  null k is the annihilator of the kernel: the conserved sources with <T, n_+> = <T, n_x> = 0 (rank 4 = 6 - 2). The
  first-order equation at null momentum has a solution exactly when the source has no transverse trace-free part.
- proved: for a conserved source at null k, T - (1/2) id tr T - P_tt T is a displacement, so the curvature of the
  remainder vanishes: the pole of the first-order curvature at the cone is in the two tt components only.
- proved: on conserved sources at null k the stored bilinear B is (1/2)<T1,n_+><T2,n_+> + (1/2)<T1,n_x><T2,n_x>:
  positive, rank two, signature (2,0) with radical of dimension 4. At timelike k its signature is (5,1) (the
  negative direction is the trace), at spacelike k (3,3) (computed at two momenta each).
- computed, with a general proof from conservation: the components of the Einstein map along e_0 have degree 0
  (e_0 e_0) and 1 (e_0 e_i) in the frequency; the spatial ones degree 2. Four constraint equations.
- computed: I4 R[n_+](B) = -/+ R[n_x](B) (sign = minus the handedness of (m1, m2, direction)): the curvatures of the
  two free directions are one I4-complex line per null momentum, as for the stored photon's mode space.
- controls: Cl(1,2): kernel at null k = displacements only (no free part in three dimensions); Cl(1,4): five extra.
- lead 5, computed: static bodies m1, m2: trace-free part (2/3) m1 m2, trace part -(1/6) m1 m2, B = (1/2) m1 m2; the
  trace-only bilinear (1/2) tau1 tau2 gives the same (1/2) m1 m2. The static coupling does not separate the channels.
  For pair sources the trace-only bilinear vanishes on chiral fermions, vectors and conformally coupled scalars;
  scalar pair to scalar pair (xi = 0) it is s^2/2 against -t u.

### Lead 3, computation (work/G/gauge_model.py; check of the proposal in work/G/P1/check.py)
Outcomes: K3a not fired (0 of 82 links off the string at equal time; 0 of 2750 spacelike events with the exact
cone). K3b not fired (the constrained field fails on 76 of 82 links in two space dimensions). K3c passed (on a chain
the constrained part of the string is the string). K3d passed (the bare recombiner fails to commute with the
constraint at the two sites; the string-dressed one commutes at all 49).
- proved in the model (exact; lattice Maxwell field, Gauss constraint, one quantum on two sites in Cl(1,1)):
  (1) the bare recombiner is not an observable, the string-dressed one is; (2) with the field's own variables the
  string-dressed detection commutes with E on every link off the string; (3) the constrained (gradient) part alone
  and the transverse part alone each fail on 76 of 82 links and cancel; (4) a field with no variable of its own is
  the constrained part, an element of the matter algebra, and fails on those 76 links: the constraint fixes which
  function multiplies the stored matter factor (the difference of the two paths' constrained fields) and does not
  remove it; (5) a detection dressed by the constrained field fails on the same links even when the field has its
  own variables; (6) in one space dimension the difference vanishes outside the two sites; (7) with an exact cone
  the slaved retarded field of the constrained model fails at 878 of 2750 spacelike events while satisfying the
  constraint at every step.
- argued: the transfer to gravity (monopole and dipole of the constrained field fixed by conservation, quadrupole
  difference left; a compactly supported dressing differs from the constrained field by a state of the two free
  components). Standard facts cited from memory, not used in proof steps.
- answer to the lead: the dressed observable commutes at spacelike separation only when the field has transverse
  variables with canonical commutators and the dressing is the compactly supported one. Constraint plus dressing,
  with no variable of the field's own, do not restore commutation.
- not done: route (c), a symmetric-tensor lattice field with the linearised Hamiltonian and momentum constraints
  (first step: the lattice double-divergence constraint in two dimensions and the existence of compactly supported
  solutions for a source with no monopole and no dipole); the visibility of the string-dressed detection (the
  overlap of the two field states), which is where the price of the local dressing appears.
Proposal: synthesis.constraint-and-dressing-do-not-restore-commutation-for-a-slaved-field-and-the-transverse-part-does
(validate_draft ok; check4 0 errors, 0 other findings; coverage.yaml in place).

### Leads 1 and 2, computation (check of the proposal in work/G/P3/check.py)
Outcomes: K1 not fired (lookup: no stored entity implies the condition; the slaved model is unitary, V V^dagger = 1,
and its commutator with the detection is nonzero, so unitarity does not imply it). K2a not fired (the change of
the detection probability is first order in the device's strength: coefficient g S (c1 - c2) p q b, nonzero at 172
of 502 spacelike events, 32 of the 252 not later than the detection). K2b passed (with the free part the coefficient
is the stored sum of G + Delta, zero at all 502). K2c not fired (the device is a number; no wave packet enters).
K2d not fired (lookup: (C1)@5 and (C2)@4 place modes on the cutoff surface of a hole and are read as a
Schwarzschild calibration; (Loc) of (C_loc)@6 is an entropy density with no mode count; no stored bound on the
product of two masses; the curvature level of (C1) is below 1e-90 near a tonne).
The prediction written before computing held: Phi_w = 1.27e-13 for the proposed experiments (written: of order
1e-13), 5.3e-3 for a kilogram at a metre (written: of order one for a kilogram, which was too large by two orders;
of order one needs a few hundred kilograms).
- proved in the model, given hypothesis (D) (a classical source couples to the field by the model's own coupling,
  unitary evolution): change of probability p q [a (cos th - 1) + b sin th], th = lam g S (c1 - c2), at most
  |sin(th/2)|; the slaved model is unitary.
- argued: the gravitational size, at most (G m_A m_B / hbar c) D |1/r_1 - 1/r_2| within the light-crossing time.
- lead 1, the list (what the store does and does not imply), is clause (S) of the proposal: (a) the locality
  theorem is about a free field's own bracket (scalar, spinor, photon); (b) the Dimock import is about the Dirac
  field on a background field; (c) the causal perturbation theory result covers interaction densities that are Wick
  monomials at a point, with no gravitational coupling in its list, and a slaved field's interaction is not of that
  form; (d) the stored static coupling is an equal-time coupling at a distance and states no condition; (e)
  unitarity (P-ii) does not imply the condition and turns its failure into a signal; (f) (C1), (C2), (C_loc) are
  silent; (g) the conventions record it as not decided. Also read: the scope note on the store's field theory
  (it lives on a classical gravitational field, where the question does not arise; it arises once the field is an
  element of the matter algebra). What the series puts in its place: nothing stored.
- lead 2: no bound from (C1), (C2) or the mode count; and a floor on localisation is not the relevant protection
  for the first-order effect, because the device needs no localisation. By the registered measure the failure is
  unobservable in the proposed experiments by ten orders, for the reason that G m^2 / hbar c is small. Counter-model
  to "a floor hides it in principle": a classical source mass with m_A m_B (D |1/r_1 - 1/r_2|) of the order of the
  Planck mass squared.
- route not taken: the second-order effect (visibility lowered when a probe with a wave packet reads the which-path
  record), where the literature's Planck-length floor lives; it comes from the fluctuations of the field's free
  part (cited from memory), so it is not available to a field without one. Out of reach in this run: a model of
  that effect inside the slaved theory (first step: a second two-level system as probe in Cl(1,2) x Cl(1,2), the
  visibility as a function of the entangling phase).
Proposal: synthesis.slaved-field-failure-is-a-first-order-signal-from-a-classical-source-and-no-stored-premise-bounds-it
(validate_draft ok; check4 0 errors, 3 informational findings on premises read only in the survey).

### Leads 4 and 5, proposal
Proposal: synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints
(validate_draft ok; check4 0 errors, 0 other findings).
- lead 4, the basis of pred.dimmed-evaporation-bursts under each option (not chosen): the stored theorem's ratio is
  D = (2 + g_h + o)/(1 + g_s), g_h the hole's emission into the two free directions, g_s that of the standard
  expectation. Free part with states, emitting as in standard physics: D = (2 + g + o)/(1 + g), the stored form;
  its basis is then the burst theorem, the spin-two clause of (J3) (whose even-parity half cluster L1 proves in
  this run) and a ground state for the two components. No emission into them (no free part, or a free part with no
  state): D = (2 + o)/(1 + g) against the standard expectation; the stored parenthesis "g = 0 gives D = 2 + o" is
  the ratio to a baseline that is not the standard expectation. The options differ by g/(1 + g): 0.02 at
  g = 2/98 (Page 1976, abstract read on the web: 2 percent of the power in gravitons for a hole emitting massless
  neutrinos, photons and gravitons), less for a hot hole. The kill condition (an undimmed burst) does not
  distinguish them.
- lead 4, the palatial question: the two free directions are one mode over span{1, I4} per null momentum, the
  counterpart of the stored photon mode; if given states as the photon is, that is a canonical pair on
  polynomials per null momentum, not an element of a floor (computed for the mode structure; the rest is reading).
- lead 5: (OS) takes the whole stress map as source, so it assumes the clause "the trace-free stress is a source" at
  the level of operators and does not derive it; nor does it show it independent. What it adds: the static coupling
  and the entangling phase do not test the clause (B splits 2/3 - 1/6 and equals the trace-only bilinear), and the
  stored production rate does (a trace-only source gives 15360/1519247, about one percent, of the mirror's rate and
  none of the vectors'). Since the mean stress of an isotropic bath sources a Weyl-flat field, the heating is
  carried by the fluctuations of the trace-free stress. The attack item itself (derive the clause, or prove it
  independent) is out of reach here: first step, a variational principle on the series' field space in which the
  five directions off the Weyl-flat class are or are not varied, which the stored first-order theorem says is the
  whole content of the clause.
The numbers of the floors that use the stored rate are being restated in this run by the energy restatement; clause
(vii) cites the rate's coefficients as they stand in the stored rate result, which that restatement does not own.

## Unexpected links
- From cluster H (its lead 2): at timelike momentum the conserved sources are a trace line plus five trace-free
  components, with pair sources of rotation weight 0, 1, 2. That is the timelike companion of clause (iv) of the
  null-cone proposal here (B has signature (5,1) at timelike momentum, rank two on the cone): only the weight-two
  part survives to the cone. Its statement that a scalar-curvature term never touches the trace-free channel agrees
  with clause (vii) here. Overlap, not duplication: H's result is about channel weights, this one about what tests
  the clause.
- From cluster L1 (its cross-link): the two free directions at a radial null momentum are one even and one odd
  under the reflection that separates the parities, so around a static hole they are the Regge-Wheeler and Zerilli
  master functions per (omega, l, m). With L1's proposal on the even-parity channel the classical channel reduction
  of the helicity-two field is complete; what the term g needs beyond it is a state on those channels, which is the
  open question here.
- To the scope note on the store's field theory (note.synthesis.scope-of-the-quantum-field-theory-...): its item
  (5), elementary or composite gauge bosons, is the same question for the photon that this problem asks for the
  gravitational field's two components; the photon is attached as an elementary Fock field, and a free part of the
  gravitational field with states would be attached in the same way.
- To op.einstein-from-the-field-theory: the constraint split (four equations without second time derivative) is
  where "one algebra holding the field and matter" would have to put the constrained part of the field: it is an
  element of the matter algebra on the constraint surface (lattice model, clause (3)).
- The store imports Wilson's lattice gauge theory (synthesis.imported-wilson-lattice-gauge-theory-...); the
  constrained model here is its abelian Hamiltonian relative. Not cited in the proposal; a maintainer may add it.

## Decisions for Leon
1. Whether the series requires its gravitational field to commute with matter observables at spacelike
   separation (unchanged; three results now bear on it: the failure is a first-order signal under unitarity; the
   constraint and dressed observables do not repair it; the transverse variables do).
2. The two free components: states or none. Under "states" the conventions would read "no quantum is posited; the
   free part of the field carries states", the construction being the stored photon's on one mode per null
   momentum; under "none" a rule at null momentum is needed (retarded, advanced, symmetric) and the first-order
   signal stands.
3. pred.dimmed-evaporation-bursts: its sentence "g = 0 gives D = 2 + o" compares with a baseline that is not the
   standard expectation; against the standard expectation the form is (2 + o)/(1 + g). A wording fix whichever
   option is taken (maintainer edit; no proposal filed against the prediction).
4. Hypothesis (D) of the signal result (a device couples to the slaved field by the model's own coupling) is local
   to that result, like (OS); whether the series holds that its gravitational field can be coupled to by a
   classical source is part of decision 1.
5. Whether the survey clause (S) should become a note on the open problem instead of a clause of a claim.

## Gate results
- synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints:
  validate_draft ok (I305 only); check4 exit 0, 0 errors, 0 other findings; 7 check functions pass.
- synthesis.constraint-and-dressing-do-not-restore-commutation-for-a-slaved-field-and-the-transverse-part-does:
  validate_draft ok; check4 exit 0, 0 errors, 0 other findings; 5 check functions pass.
- synthesis.slaved-field-failure-is-a-first-order-signal-from-a-classical-source-and-no-stored-premise-bounds-it:
  validate_draft ok; check4 exit 0, 0 errors, 3 informational (I405: premises read only in the survey); 5 pass.
check4 was run on staged copies (work/G/stage/<id>/) before filing; small wording edits made after it touched only
entity.md and proof-main.tex (the grad convention sentence, two dates, the lambda factor), not the checks.

## Files
work/G/null_kernel.py, null_kernel2.py, null_kernel3.py (leads 4, 5); gauge_model.py (lead 3 exploration);
P1/, P2/, P3/ (the three drafts: entity.md, proof-main.tex, check.py, coverage.yaml, draft.json); stage/ (copies
named by id for check4); show.py, mkdraft.py (helpers).

## Fix round
See findings/fixes-G.md. One conclusion of the first filing was withdrawn after the referee's counterexample was
checked: a field with no variable of its own is not fixed by the constraint, so the equal-time failure belongs to
the Coulomb slaved field, and the failure that holds for every slaved field obeying the field equation is the
dynamical one, at events in the source's forward cone.
