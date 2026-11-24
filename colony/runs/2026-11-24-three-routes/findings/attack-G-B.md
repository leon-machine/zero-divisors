# Findings, attacker G-B (angle B), run 2026-11-24-three-routes

Target: op.gravitational-field-at-null-momentum. Sibling G-A executes "palatial pair". This file: the other side.
Work files: colony/runs/2026-11-24-three-routes/work/G-B/. Labels: proved / computed / argued / conjectured.
Status of this file: complete for the attack round (kill conditions were registered before any computation of
this run; the section was written first and has not been edited since, apart from this line).

## Orientation (lookups made before computing)
- op.gravitational-field-at-null-momentum; conventions, "Gravity and the graviton".
- Earlier findings read: 2026-11-18-navigate/attack-main.md (part C), 2026-11-18-leads/attack-G.md and fixes-G.md,
  2026-11-08-current-algebra/REPORT.md.
- Stored results that already cover part of line 1 (not redone here):
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum (vi): density waves of the
    null vacuum on one generator are canonical bosons on a stated domain.
  - synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off: on a floor the central term
    is an edge operator, value min(p, 2N - p) on the sea.
  - synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra (import; the Schwinger term).
  - synthesis.density-modes-bosonise-only-along-one-null-direction (window identity; strip differences).
  - synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins: a pair mode rho_q(M) has helicity h iff
    [W, M] = hM; for h != 0 M is nilpotent, so not normal, so never a canonical boson on the edge-clean vectors.
    Stated for a FINITE channel set with the rotation acting by diagonal weights.
  - synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators: the photon's null data are two chiral
    current algebras per generator; pair currents reach them only as a contraction over many generators.
  - dark-energy.acoustic-no-go-one-way-grip: in the s-wave current algebra "the graviton mode is T", the Sugawara
    stress tensor (weight two, not a weight-one current).
  So the helicity-one case of line 1 is settled in the store. What is not stored: the helicity-two channel, and the
  test of a composite as the free part of the stored lattice model.

## Routes considered (angle B is free to choose)
R1. Composite on the generators (the run's line 1): a current of light-ray fermions as the free part.
    Delivers: the requirement met with no canonical pair posited. Needs: (a) a helicity-two current with a central
    commutator; (b) the commutator function of the field equation. Fails if (a) or (b) fails.
R2. From another subject (one-relation): the recording premises make the source a number. Delivers: no signal with
    no field variables. Needs: recording before the first-order signal builds, and the registered phase to survive.
R3. Own: a mediator that is not at null momentum at all, i.e. any stored local quantum system (the fermions
    themselves) carrying the response, with the first-order criterion read on expectations (Kubo) and not on
    central commutators. Delivers: a weaker sufficient condition than canonical commutators. Fails if the medium's
    response function is not the retarded function of the first-order field equation.
R4. Breaking the palatial route: a stored result that a canonical pair on the two directions contradicts, or a
    gravitational constraint that forbids a dressed detection.
Choice: R1 first (the run's priority), with R3 as the form in which its second limb is tested (the criterion on
expectations is weaker than centrality, so a failure of R3's criterion is a failure of R1 a fortiori); R2 and R4
by lookup and short computation.

## Kill conditions (registered 24 November before computing)
- G3 (the run's, mine in particular): a structure already stored meets the requirement with no states on the two
  directions. Then the palatial pair is not forced.
- KB1 (line 1, first limb): on one generator, in the helicity-two channel (the rotation about the generator
  multiplying the current by e^{2 theta J}), the sea value of [X_q, X_q^*] vanishes for the candidate current X_q,
  or no candidate exists at the order considered. Registered expectations before computing: bilinear order, no
  candidate for channel weights +1/2 and -1/2 (to be proved, not assumed); quartic order, a candidate exists and
  its sea value is a polynomial in q of degree higher than one (so the commutator function along the generator is
  a higher derivative of the delta function, not the first).
- KB2 (line 1, second limb): the composite's commutator function is not the one whose retarded response restores
  commutation. Registered test: (i) along the generator, the sea value of the commutator as a function of q
  against the value q of a weight-one current; (ii) off the null plane, the first moment (the double commutator
  with the light-front energy) of the composite's commutator function against that of a free massless mode with
  the same longitudinal and transverse momentum. KB2 fires if either differs.
- KB3 (line 2): the recording route dies if making the source a number before the first-order signal builds also
  removes the registered phase, that is if the signal and the phase are proportional to the same matter factor
  [J, O] and the phase accrued before the recording time is below the registered threshold.
- KB4 (line 3): "the palatial pair contradicts a stored result" dies if no stored result at its present version
  has a hypothesis that covers a canonical pair on polynomials for the two directions.
- KB5 (line 3): "the three positions are jointly inconsistent on the stored models" dies if in the stored lattice
  model there is a field value in the matter algebra that differs between the two paths and commutes with every
  detection U^{-1} P_1 U.

## Results

Proposal filed (one): synthesis.helicity-two-composites-of-light-ray-fermions-on-a-generator-and-off-the-null-plane
(proposals/; check4 exit 0 with 0 errors and 0 other findings, validate_draft ok with the standing ORCID warning
E610 only; five checks, all exact). Ledger: transport-absent in content (standard current algebra and kinematics);
the window forms and the reading against the stored lattice model are the store's.

### Line 1. Composite on the generators (work: fock.py, c2_sea_values.py, c3_noncentral.py, the proposal's check)
What was already stored and is not refiled: helicity zero (density waves are canonical bosons on a domain; the
central term is an edge operator on a floor), helicity one (quasi-spins, never canonical), the photon's null data.
New, all for one generator with channel weights +1/2 and -1/2:
- proved: no pair mode (bilinear) has helicity two, for any number of channels: helicities of a*_alpha a_beta are
  w_alpha - w_beta in {-1, 0, 1}. So KB1's first registered expectation holds: no candidate at bilinear order.
- proved (counting, with a generating function) and checked exactly on windows: the lowest four-fermion
  helicity-two modes have sea values of [X_q, X_q*] equal to C(q+1, 3) = (q^3 - q)/6 for two flavours
  (q = 1..5: 0, 1, 4, 10, 20) and C(q+3, 7) for one species (q = 1..7: 0, 0, 0, 1, 8, 36, 120). A current has q.
  The least generator momentum of a helicity-two vector over the sea is 2 (two flavours) and 4 (one species).
- computed exactly: the commutator of the two-flavour mode is not a number on edge-clean vectors (1, 0, 3 at
  q = 2 and 4, 2, 10 at q = 3 on the sea and two one-pair vectors; the total density mode gives 4q on all of
  them), and X_q*^2 annihilates the sea at q = 2, 3 (no second quantum).
- proved (GA, Cl(1,3)): for two future null momenta, Q(p_1 + p_2) = |alpha_2 p_1perp - alpha_1 p_2perp|^2 /
  (alpha_1 alpha_2), zero only for parallel momenta. Argued from it: a pair mode at one transverse point
  superposes all relative transverse momenta, so its vectors lie at Q(P) > 0, where the stored first-order
  theorem says the field is fixed by its source; the free directions are at Q(k) = 0 only.
- proved (exact identity, any algebra) and computed in a five-mode fermion ring: in the stored two-path model
  with ANY medium coupled at a point, [phi_n(t), O] = W_<t^-1 [phi0_n(t), W_>=t^-1 O W_>=t] W_<t. It vanishes
  wherever the medium's own elements commute with the later source elements; no canonical commutator is used
  (14 of 20 events zero, the six the rule names nonzero). The medium's response depends on its state (0 in the
  empty medium, -sin a = -4/5 on a one-quantum vector, where a linear response would give -a).
- argued (the decision asked for): a composite of light-ray fermions cannot serve as the free part of clause (4)
  of the stored lattice result in the helicity-two channel. Three independent reasons: no weight-one current of
  helicity two exists on a generator; the four-fermion modes that do exist have a commutator that is not a
  number; off the plane the composite sits at non-null momentum. The exception is one space dimension, where
  there is no transverse momentum and the density waves are canonical on their domain; the reduction of horizon
  channels under joint J3 is of that kind, is a premise, and is not touched.
- argued, and a correction of my own registered test: KB2(i) compared the sea value with the value q of a
  weight-one current. The gauge-invariant null datum of a helicity-two field is a curvature, one derivative
  more, with value q^3. The two-flavour mode's (q^3 - q)/6 matches that form at large q, in the sea's
  expectation only. So the registered comparison with q was the wrong yardstick for the curvature; with the
  right one the form matches asymptotically and the failure is carried by non-centrality and by the off-plane
  test, not by the degree in q. I report this as found after computing.
Outcomes: KB1 fired at bilinear order (no candidate), did not fire at four fermions (the sea value is nonzero, of
degree three or seven). KB2 fired: (i) literally (not q), with the caveat above; (ii) fired, in the stronger form
that the total momentum is not null at all unless the pair is parallel (the registered first-moment test was
replaced by this exact statement; the moment itself was not computed).
Not done: the transversally smeared contraction over many generators for helicity two (the analogue of clause
(v) of the stored photon result), and bilinears with transverse derivatives (orbital helicity). For the second I
have only an argument, not in the proposal: with transverse momentum transfer P the channel matrix is f(p) times
a shift by P, which is normal only if |f| is constant, so the commutator carries an operator unless P = 0.

### Line 2. The recording route (lookup and a short computation)
Read: one-relation.recording-irreversible-stated-so-it-can@1, one-relation.recorded-sectors-superselected-premise@1,
one-relation.record-chain-votes-measurement-without-collapse, synthesis.records-of-unbounded-length-...@1, the
device result@1, pred.gravity-entangles-standard-phase@3.
- argued (it fails, as expected), by three steps. (1) The stored signal is pq[a(cos theta - 1) + b sin theta],
  linear in the coherence (a, b) of the superposed quantum, and the registered phase is read from the same
  coherence. A record of N pairs of overlap c multiplies every interference of an element that does not reach
  the record pairs by c^N (the stored record result), so signal and fringe are multiplied by the same c^N:
  recording cannot lower the signal relative to the registered effect. (2) Timing: the signal outside the cone
  is bounded by the phase accrued in one light-crossing time (the stored Phi_w); a record written early enough
  to stop it leaves at most Phi_w of entangling phase, about 1.3e-13 in the proposed experiments, ten orders
  below the registered threshold. To bring the order-one signal of the 190 kg case below 1e-3 needs
  c^N < 1e-3, which removes the fringe by the same factor. (3) The recording premises are about laboratory
  measurements writing records within the modular period; the registered prediction is stated "with coherence
  kept for the duration", which is the regime with no record. Under hypothesis (D) the device is a number and
  writes none. If the recorded sectors are superselected exactly, [J, O] = 0 for every admissible O (kb5 script:
  with pq = 0 the commutant of the detections contains J), and signal and phase vanish together.
- consequence for pred.gravity-entangles-standard-phase: making the source a number before the first-order
  signal builds would turn the prediction into "no entanglement"; it is the mean-field outcome by another name.
Outcome: KB3 fired. The recording route is dead.

### Line 3. Breaking the palatial route; the prior art
Lookups: field-theory.no-canonical-commutation-relations-tower@3, field-theory.imported-statistics-no-go-palatial-
algebra@2, field-theory.fock-space-maxwell-modes@5, the Krein premise (KF)@3, dark-matter.p2-indifference, the
conventions' section.
- lookup (KB4 fired: no contradiction found). The no-CCR theorem is about floors and bounded elements of the
  CAR limit; a pair on polynomials is outside its hypothesis, and the stored photon is exactly such a pair.
  (KF) already puts the polarisation modes of "the series' gauge fields" on the palatial representation and
  lists "the Krein quartet of induced gravity" among results resting on it; nothing in it excludes the
  gravitational gauge field. P2's finite deposited mode set counts modes, and the stored photon modes are
  already canonical pairs under it. What a pair on the two directions contradicts is the first paragraph of the
  conventions' section ("the series holds no quantum of that field"), a decision of 10 November and not a
  theorem. So the palatial route cannot be broken from the store; its cost is that decision.
- argued (constraints and dressing; the sibling's G1a is the computation). The mass, momentum and centre of
  mass of a closed system are boundary values of the gravitational constraints (a double divergence, with no
  charge of the opposite sign), so a dressing of compact support exists only for rearrangements that keep all
  three. A single mass on two sites changes the centre of mass; a closed model with the recoiling apparatus does
  not. So a dressed detection that commutes at spacelike separation needs the recoil in the model. For the
  registered phase the recoil body's contribution is smaller by about (d/R)^3, d the separation of the masses
  and R the distance from the second mass to the recoiling body (corrected in the fix round: the entangling
  term is bilinear in the two displacements, G m_A m_B dx_A dx_B / d^3, and the recoil body, displaced by
  -m_A dx_A / M, gives G m_A m_B dx_A dx_B / R^3; my first figure (d/R)^2 was the ratio of the path-dependent
  forces, not of the phases). The factor is geometric and need not be small in an actual apparatus; this is an
  argument, with no stored result behind it.
- proved in two lines and checked (kb5_trilemma_lemma.py): in the stored two-path model the elements of the
  matter algebra that commute with P_1 and with one mixing detection U^-1 P_1 U (pq != 0) are the numbers. So
  the three positions are jointly inconsistent on that model: (S) the field's values lie in the matter algebra,
  (L) they commute with every detection the experimenter may choose at spacelike separation, (E) they differ
  between the two paths. This generalises clause (2) of the stored result from multiples of J to every element;
  its substance is already stored. KB5 did not fire. Not filed (thin, and it overlaps the stored clause).
- prior art, FROM MEMORY and not re-read: Galley, Giacomini and Selby, "A no-go theorem on the nature of the
  gravitational field beyond quantum theory", Quantum 6 (2022) 779. As I recall it: in generalised probabilistic
  theories, (i) gravity entangles two systems, (ii) the two systems interact only through the mediator, (iii)
  the mediator is classical, cannot all hold. What the stored lattice results reproduce: only the two
  degenerate corners. A mean-field (number) source gives no entangling phase (field-theory.operator-newtonian-
  coupling), which is (iii) with (ii) kept and (i) lost. A field slaved to the operator source has no state
  space at all: it is not a classical mediator but no mediator, a direct interaction, so it gives up (ii), and
  the lattice results compute the price, the failure of commutation and under (D) a first-order signal. The
  general step of the published theorem, that a classical system with variables of its own cannot entangle,
  is not in the store. The published theorem also does not say the mediator must be a canonical pair, only that
  it is not classical; clause (v) of the proposal is the same remark on the stored model.

### Kill condition G3
Not fired. No stored structure meets the requirement for the gravitational field with no states on the two
directions. Examined: the composite on the generators (fails, line 1), the recording premises (fail, line 2),
joint J3's current-boson identification (a premise, and only for a horizon's channels, which the experiment's
configuration does not have), a medium with causal commutators (meets the requirement, clause (v), but is not
the gravitational field unless the field is the response of the stored quantum fields, which no stored result
gives). Not examined: the central limit of fluctuation states
(synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit), which gives canonical pairs only in
a limit. What the run does change: commutation at spacelike separation does not by itself force a canonical
pair. It forces a pair only together with a field that obeys the first-order equation with a response that is
a fixed function. That is a sharpening of the problem, not G3.

## Unexpected links
- The stored statistics theorem's clause "bosons made of fermions are not excluded" is closed off for helicity
  two on a generator by the same weights that give the fermions helicity one half: synthesis.light-ray-good-
  part-of-a-spinor-is-two-chirality-arrays (iv) is the obstruction.
- dark-energy.acoustic-no-go-one-way-grip calls the Sugawara stress element "the graviton mode" of the s-wave
  current algebra. It is a weight-two, helicity-zero element with a non-central commutator: the same kind of
  object as the four-fermion modes here, and for the same reason not a free part.
- Clause (v) links this problem to op.einstein-from-the-field-theory: if the gravitational field were the
  response of the stored quantum fields, the requirement would hold with no further premise, and the open
  question would become the pole at null momentum of that response. The stored induced-gravity results
  (synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off) are the nearest.
- The helicity-one quasi-spin theorem and clause (i) here are window forms of Pryce's 1938 theorem against the
  neutrino theory of light (from memory); the store does not cite it.
- The dipole point of the sibling (G1a) and the registered phase: the recoil body restores the centre of mass,
  and its share of the phase is of relative order (d/R)^3 (corrected in the fix round), a geometric factor that
  need not be small.

## Decisions for Leon
1. The proposal (accept, or not): it records that a composite of light-ray fermions is not the free part of the
   stored lattice result in the helicity-two channel. It decides nothing about whether the two directions carry
   states.
2. The reading in the proposal's last paragraph: that the requirement leaves two ways, a canonical pair on the
   two directions or the field as the response of the stored quantum fields. If you accept it, the open problem's
   statement could name both and point the second at op.einstein-from-the-field-theory. Recommendation: record
   it as an attack item, labelled argued.
3. Whether to add a short note or claim with the commutant lemma (the three positions are jointly inconsistent
   on the stored two-path model) and the published trilemma as prior art. Recommendation: a note on the open
   problem; the paper has to be read first, it is cited here from memory.
4. Prior art to import or cite, all from memory: Galley, Giacomini and Selby 2022; Pryce 1938 (on the stored
   helicity-one result); Weinberg and Witten 1980 is already cited.
5. The conventions: the palatial route contradicts no stored theorem (KB4), only the sentence "the series holds
   no quantum of that field". That sentence is the whole cost on the store's side.
