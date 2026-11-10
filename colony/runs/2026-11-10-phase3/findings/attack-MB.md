# attack-MB: dark-matter premise reduction, adversarial half

Status: attack round complete. One proposal filed. Kept current.

## The 23 dark-matter postulates (status postulate, subject dark-matter), alphabetical by id

Own = owner decides M2 (derive, or model where it fails and the rest hold). Even numbers are MB's, odd are MA's.

| # | id | owner |
|---|---|---|
| 1 | dark-matter.d-democracy-total-mass | MA |
| 2 | dark-matter.p1-single-frozen-point | MB |
| 3 | dark-matter.p2-indifference | MA |
| 4 | dark-matter.p3-nearest-dimension-representatives | MB |
| 5 | dark-matter.p4-democracy-asymmetry-over-oriented-towers | MA |
| 6 | dark-matter.p5-boundary-modes-hold-entropy-not | MB |
| 7 | dark-matter.premise-cpt-covariance | MA |
| 8 | dark-matter.premise-flag-as-datum | MB |
| 9 | dark-matter.r1-equal-mass-per-quantum | MA |
| 10 | dark-matter.r2-one-quantum-per-unit-ball | MB |
| 11 | dark-matter.r3-one-cell-per-unshared-direction | MA |
| 12 | dark-tower-matter.h1-momentum | MB |
| 13 | dark-tower-matter.h2-identification | MA |
| 14 | dark-tower-matter.hypothesis-s-slot-statistics | MB |
| 15 | dark-tower-matter.u-transposition-rule | MA |
| 16 | simulations.c-odd-towers-collisionless | MB |
| 17 | simulations.s1-one-species-per-tower | MA |
| 18 | simulations.s2-sheet-fluid | MB |
| 19 | simulations.s3-mirror-cluster | MA |
| 20 | simulations.s4-our-matter | MB |
| 21 | simulations.s5-halos | MA |
| 22 | synthesis.common-ceiling-coupling-premise | MB |
| 23 | synthesis.matter-asymmetry-registered-free-input | MA |

(dark-matter.hyp-u-equal-rank-one-eigenvalues carries a dark-matter id but subject neutrinos: outside the 23.)

MA files the base statement and the dependency table. MB does not file either.

## Pre-registered kill conditions (written before any computation)

K1 (cluster kill, from RUN.md). None of the 23 is redundant: then the count stands as the cost of the fit.
K2 (MB's own postulates). For each of the 11 even postulates: if no derivation from the other 22 plus foundation is
found AND no model separating it is found, it is recorded "undecided" with what decides it. No postulate is called
independent on the strength of a model that also breaks another postulate.
K3 (ratio sensitivity). Claim under test: "the ratio 5.364 uses only a proper subset of the 23". Killed if the stored
derivation of the ratio cites, directly or through its cone, all 23. Conversely "postulate X is redundant for the
ratio" is killed if dropping X changes the stored ratio expression (computed exactly from the stored formula).
K4 (fit count). Claim under test: "some of the postulates were added or changed after the number was known". Killed
if every postulate in the ratio's cone has version 1 and predates the first stored appearance of the ratio. The
count is reported whichever way it falls.
K5 (challenge to MA). Every derivation MA offers is tested for the derived postulate appearing in the past cone of
the premises used. Every MA equivalence is tested by seeking a separating model; if none is found in a bounded
search the pair is reported "not separated", not "equivalent".

## Proposal filed

synthesis.constituent-momentum-is-the-unique-spin-covariant-quadratic-vector-on-the-spinor-ideal
(proposals/; check4 exit 0 with no findings; validate ok; registered with propose_claim; coverage.yaml added; five
check functions, all kind complete). On postulate 12, H1. Not the base statement and not the table: those are MA's
(synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball), which I cite and attack below.

Content. In the six causal towers of dimension 3, 4, 5:
(i) PROVED (exact rank over Q of the covariance equations): the spin-covariant quadratic maps S -> V form one real
line, spanned by H1's j(psi) = <psi e_t rev(psi)>_1.
(ii) PROVED: psi e_t rev(psi) is a pure vector in dimensions 3 and 4 (H1's projection removes nothing); in dimension 5
it is j + s I with I the central pseudoscalar; invariant quadratic scalars on S: none in dimensions 3, 4, the line of
s in dimension 5.
(iii) PROVED (polynomial identities): in dimension 5, y^2 = 2 s I y, Q(j) = s^2 I^2, m^2(j) = s^2 = (1/2)<x x^dag>_0,
the stored single-constituent law. The mass of one constituent is the square of the part H1 discards.
(iv) PROVED for dimensions 3, 4: for two constituents the covariant quadratic vectors have dimension 3 and 4, more
than the two single momenta, so additivity P = j_1 + j_2 (a clause of the stored Definition) is not forced.
Dimension 5 not computed.
(v) ARGUED: H1's momentum clause in dimensions 3 and 5 is equivalent to "momentum is a nonzero spin-covariant
quadratic vector of the spinor part" plus a real factor. H1 is therefore weakened, not retired: the existence of the
spinor part, quadraticity, covariance and additivity stay assumed.
Circularity: the two premises used (dark-tower-matter.constituents-field@2, dark-tower-matter.where-mass-begins@2)
have no postulate in their past cones; H1 is not in the cone. Transport-absent; classical representation theory
(the vector occurs once in the symmetric square of the spinor module) placed on the series' ideals, prior art cited
from memory. Candour on procedure: kill condition K2 was written before computing; the specific uniqueness
conjecture was formed after the first probe (grades) and was then tested by the rank computation, which could have
returned a dimension above one and did not. Scripts: work/MB/h1_grades.py, h1_mass.py, h1_unique.py.

## M2, M3: verdict on the eleven postulates I own

Labels: PROVED (exact, in my proposal), STORED (an accepted result already says it; id given), ARGUED, UNDECIDED.
No verdict below calls a postulate independent on a model that breaks another postulate; where no such model is
exhibited the label is ARGUED.

2. P1, single frozen point. Three clauses with three different statuses.
   - Metric clause: STORED, both ways. A theorem up to normalisation wherever the Weyl tensor has no kernel vector,
     given one tractor connection (synthesis.frozen-point-unique-where-weyl-has-no-kernel, no postulate in its
     cone); an independent choice on conformally flat regions, de Sitter included
     (synthesis.two-frozen-points-conformally-flat).
   - Orientation clause: STORED as substitutable. synthesis.mirror-asymmetry-route-one (ii) and
     dark-matter.mirror-tower-copy-one (v): the sign is fixed "by the orientation clause of P1 or by P2 applied to
     that discrete datum", and under P2 version 2 the orientation bit is among the labels P2 equates. So given P2
     version 2 the clause is redundant (ARGUED on the stored reading that the bit is a label). Further (my check):
     the share does not see the sign at all, eps_2 = -eps_6 gives the same mirror share, so the total needs the
     clause under neither route.
   - Common N: used by dark-matter.stored-asymmetry-charge-not-number ("the argument uses only that N is common").
     No derivation found. UNDECIDED; decided by whether a second tower can carry its own frozen-point norm, which
     the conformally flat counter-model above suggests it can.
   Verdict: not one postulate. Recommendation in Decisions.
4. P3, nearest-dimension representatives. STORED: follows from Premise U at residues 1, 7; independent at residues
   3, 5 (synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free: every other window-sensitive premise
   holds with the towers at dimension 13, total about 9.94); not needed for the mirror pair
   (synthesis.oriented-causal-towers-mirror-pair-every-window). What stays postulated: the window at residues 3, 5
   and at the even residues. Nothing to add. The total moves when it is dropped (9.94).
6. P5, boundary modes hold entropy, not global charge. ARGUED redundant for its two uses. Its own text says "this is
   what the imported flux already implies here". The used clause (baryon number is not returned; holes are a sink
   for Q: dark-matter.parallel-boundary-mode-spaces-one-wall (iv), dark-matter.stored-asymmetry-charge-not-number
   (ii)) follows from three stored items: the thermal flux under the interface premise
   (hawking.greybody-inheritance-under-interface-premise), energy conservation, and the no-remnant clause already
   carried separately (singularity.rate-models-kinematic-inputs-l-u). Arithmetic: carriers of rest mass m_p are
   emitted without Boltzmann suppression only below M_* = M_Pl^2/(8 pi m_p) = 6.3e36 GeV, so at most M_*/m_p
   baryons, a fraction M_*/M_sun = 5.7e-21 of a solar-mass progenitor's (constants from memory; agrees with the
   stored "below 1e-20"). Not exact: the suppressed emission above M_* needs the greybody integrals, so this is an
   estimate at the import's level, not a proof. What the energetic argument does NOT cover (found here): a global
   charge with a light carrier. Lepton number in this tower is carried by neutrinos; for a massless lightest
   neutrino the threshold argument is empty, and non-return then rests on the flux having no chemical potential for
   a global charge (equal emission of carriers and anti-carriers). That clause is the real content of P5 and is a
   property of the stored thermal state, not of the boundary modes. Verdict: P5 as used is a consequence of
   premises outside the 23 (interface premise, no-remnant); as stated for every global charge it needs the
   zero-chemical-potential clause, UNDECIDED in-store. Not in any cone of the total.
8. Flag as datum. ARGUED independent of CPT covariance as worded, and a typing clause in content. Separating pair:
   (K) two theories T+ and T-, the sign kinematic, C an isomorphism T+ -> T- with S_- o C = S_+; (I) one theory on
   the union, C an automorphism. Both satisfy the CPT premise's sentences; they differ on the flag premise and on
   the conclusion of the seventeenth refutation. The entity says this itself ("two isomorphic theories rather than
   two solutions of one"). My addition: (I) is the disjoint union of (K)'s two theories, so no statement about a
   single solution differs between them and "No observation tests the premise" is exact: the premise is a
   convention on what counts as one theory (M3: convention in disguise). MA reached the same reading and did not
   file a derivation; I agree with that and with the merge recommendation. Not in any cone of the total. Added
   22 October by a maintainer pass, after T14.
10. R2, one quantum per unit ball. For the total: only through MA's (E) (MA's clause (i), which I tested, see
   challenges). On the reversal pair: a consequence of the population count. On the odd towers: independent,
   ARGUED (no stored premise names a number density there: dark-matter.no-coupling-rule-odd-towers-follows), and it
   moves the total when dropped. Two further stored facts bear on it: the clause holds at one epoch only unless the
   hidden direction co-expands (synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands),
   and R3's unit is "the cell radius R2 chose" (dark-matter.contact-mechanism-returns-r3 (iii)), so R2 enters the
   total twice, as a density and as R3's unit. Joint tenability: with D, R1 and R2 all held, equal quanta per ball
   of the de Sitter radius and one quantum per ball of radius a in dimensions 2, 3, 4 force a = ell (exact: x^2 =
   x^3 = x^4 only at x = 1), one quantum per de Sitter ball, against about 5e78 baryons per such ball (argued;
   numbers from memory) and against the stored bound that the counted cell radius is below 2.4e-10 m. So D and R2
   are premises of two alternative readings, as dark-matter.status-rule (iv) says ("replaces R2 by democracy"),
   and must not be counted as jointly held.
12. H1. See the proposal: the formula is forced by covariance (PROVED); what is left of the premise is listed there.
   M3: the momentum formula is a definition (it is the stored object's definition of j) plus an identification.
14. (S) carried to every tower. One dependant (dark-tower-matter.five-dimensional-content), which states the content
   both with and without (S); under no statement of the total. MA's question (does the dimension-four derivation
   of (S) run in dimension five): ARGUED no. The dimension-four proof (standard-model.hyp-s-slot-statistics) uses a
   U(2) doublet of slot creation operators and the chirality as a CPT halving; the five-dimensional towers have one
   slot (hierarchy C^1 tensor C^3) and no chirality (stored), and U(1) equivariance alone does not force a
   creation operator to square to zero (the symmetric algebra on one generator is U(1)-equivariant with a
   nonzero square). So (S) carried is independent there of an equivariance argument; it is an optional branch
   ("used only where stated"), not a commitment. UNDECIDED whether another route gives it.
16. C, odd towers collisionless. Not a premise about the series' structure: STORED as what the cluster bound
   requires (simulations.confinement-scale-does-not-matter: "the cluster bound is met only if the quanta barely
   interact ... which is Premise C"). It is an observational constraint adopted as a premise, and it sits against
   the radiation audit, which closes the three-dimensional towers' radiation channel by confinement and says
   self-interaction there is at composite strength "if their matter is the confined charged matter the closure
   leaves" (dark-matter.radiation-audit-what-theorem-closes-what). UNDECIDED in-store; decided by the
   three-dimensional towers' spectrum.
18. S2, sheet fluid. Conditional on the negation of C for the three-dimensional towers: "At composite strength ...".
   S2 is reading (W) and C is reading (C) of the two simulation results; both results list both as assumed, but
   they are premises of two exclusive branches, and the merger result reports that (W) fails to give a lensing peak.
   Under C, S2 is vacuous for those towers. M3: not a postulate, the specification of a rejected alternative.
20. S4, our matter (adiabatic gas, galaxies 2 percent tracers). A numerical approximation about this tower that is
   false as a statement about nature (gas cools); M3: model specification. Agree with MA's merge of the simulation
   premises, with one correction: they are two models, not one, because of 16 against 18.
22. Common ceiling coupling. STORED independent of P2 version 2 (synthesis.tower-charge-sector-label-temperature-not;
   dark-matter.mirror-share-one-how-fragile (ii): the share is a free function of the coupling difference). For the
   total it is one of two routes to the mirror's term (MA's clause (iii)). It is not implied by R1 on the pair:
   equal proton masses is one condition on several couplings; with one coupling and one-loop running it is
   equivalent (m_2 = m_6 iff delta = 0, by Lambda_2/Lambda_6 = exp(-2 pi delta / b)), ARGUED. Added 7 November,
   after P2 was re-scoped, to restore the equality P2 version 1 had supplied.

## Challenges to MA (K5)

1. MA's proposal, clause (i) (the family m_r = s_r m, nu_r = 1/(s_r V_D d^D) keeps every share). TESTED, exact
   (work/MB/r3_unit.py). True as formalised, with R3's thickness measured in the length d of (E). The store ties
   R3's unit to R2's cell ("its unit is the cell radius R2 chose", dark-matter.contact-mechanism-returns-r3 (iii);
   T(c) counts through c d_b). When R2 fails there are three candidate units: (a) the (E)-length d: shares kept
   for every s; (b) this tower's Wigner-Seitz radius: kept iff s_6 = 1; (c) the tower's own Wigner-Seitz radius:
   the five-dimensional share is multiplied by s^(1/4) and the three-dimensional one by s^(-1/2). Example under
   (c): s = 16 on the five-dimensional towers gives T = 11/3 + 32/(3 pi) = 7.06 with (E) intact. So "the total uses
   R1 and R2 only as mass per unit ball" needs "given R3's thickness is read in the length of (E)" at title,
   one-liner, technical and lay levels; under reading (c) R2's number density enters the total separately. Request
   to MA: restate with the reading, and normalise s_6 = 1 so that d is this tower's cell radius. Not a refutation.
2. MA's P2 as a specialisation of the programme's indifference premise. The stored theorem MA leans on
   (synthesis.indifference-is-curie-plus-single-valuedness) has P2 in its own past cone (through
   dark-matter.residue-soldered-invariant-not-algebraic-one and dark-tower-matter.mirrors-temperature-p2), so as a
   DERIVATION of P2 it is circular in the graph; as a `specialises` relation it is fine. And the direction matters:
   the unrestricted programme premise gives xi = 1, which the record excludes (that theorem's own one-liner: the
   cold mirror requires single-valuedness to fail for the deposited energy). So P2 version 2 is the programme
   premise minus an instance the data refuted, adopted on 22 October. Counting them once is right; calling P2
   derived from the programme premise would export the refuted instance to the programme premise. MA already says
   "the restriction is what is postulated"; I ask that the recommendation say the programme premise needs the same
   scope note.
3. MA's P4 retirement. Graph: no circle (dark-matter.mirror-tower-copy-one has no P4 in its cone). Text: clause (v)
   route one rests on "the stored charge Q = eps N being a sector label", which is
   dark-matter.stored-asymmetry-charge-not-number (i), a result DOWNSTREAM of the copy theorem and of P4 (through
   the fifteenth refutation). There is no logical circle that I can find (the charge reading is per tower and does
   not use universality), but the dependence is an untyped forward reference. If P4's two assumes edges are
   repointed to the copy theorem, the copy theorem's clause (v) should first be given its real premises (P1's
   common N and the charge reading). Verdict on MA's claim: stands, with that repair.
4. MA's merge of the six simulation premises into one model: two models, see 18.
5. MA's count "about 13 distinct assumptions": I get the same list; H1 now carries a proved reduction of its
   formula clause, and P5 an argued one.

## Ratio sensitivity (does 5.364 move when a supposedly redundant postulate is dropped)

From stored results and the tests above. "Moves" means some model satisfying the remaining premises has another total.
- R3 dropped: moves, every value above 1 (stored). P3 at residues 3, 5 dropped: moves, 9.94 (stored). Clause (vi)
  dropped: 6.16 or 8.254 (stored). Population inference dropped: 1 (stored).
- R1 or R2 dropped singly: moves. Both replaced by (E): does not move under reading (a) of R3's unit; moves under
  reading (c) (7.06 in the example above).
- D dropped: does not move (it is in no cone of the stored total).
- Common ceiling dropped with R1 kept, or R1 on the pair dropped with the ceiling kept: does not move. Both dropped:
  the mirror's term is free.
- P1's orientation clause dropped: does not move (the share is even in the sign).
- P4 dropped: does not move. P5, CPT, flag, H1, H2, (S), U, C, S1 to S5, epsilon dropped: no stored statement of the
  total changes (U and H1 touch its conditions through the window and the emptiness of residue 4).

## Counting the fit truthfully (K3, K4)

- Postulates per fitted number. The stored closed form has 5 of the 23 in its past cone (P2, P3, R1, R2, R3). The
  fitted quantity is the remainder 4.364; the mirror's 1 is derived separately. What the remainder rests on: (E)
  on the odd towers (R1 and R2, one premise for the total), R3, P3's window at residues 3, 5 and 1, 7, and two
  conditions that are not postulate entities: the costed single-ideal clause and the inference that the odd towers
  are populated. The second of these is inferred FROM the number it helps to fit ("the observed remainder is the
  evidence that the odd towers hold matter", dark-matter.which-towers-are-populated). So: three registered
  postulates and two unregistered conditions for one number, with a stored look-elsewhere of 14 distinct values
  within one standard deviation among 3136 expressions (dark-matter.status-rule (ii)).
- Added or changed with the number known. K4 fired in the direction of the claim: R1, R2, R3 "were chosen with it
  known" and the relation "was found by solving for the observed value" (dark-matter.status-rule (i), (ii);
  dark-matter.unit-ball-rule). Clause (vi): "chosen knowing that the unit-ball fit needs it" (26 October). D and
  the contact clauses belong to the same section of T14. From the user's memory notes, not from the store: the
  unit-ball section entered T14 as Version 2.0 on 26 September 2026, absorbing a note whose claim was the value
  5.364; P1 to P5 are T14's Section 2 and are older. So of the five postulates under the closed form, three were
  written for the number; P2 and P3 were not, but P2 was re-scoped on 22 October after the mirror-temperature
  conflict with the record, and P3's two alternatives recorded since (the window (W), "found with the fit known";
  the Bott-shifted window) were both examined with the number in hand.
- Added after extraction (store dates): CPT covariance 21 October, flag as datum 22 October, epsilon 1 November,
  common ceiling 7 November. All four are maintainer registrations of assumptions the papers used without an
  entity; none was added to improve the fit, and none is under the closed form.
- The 23 are not one premise set. D against R2 (two readings of the count), S2 against C (two readings of the
  three-dimensional towers), (S) carried (optional branch), epsilon (a register entry used by nothing). "23
  postulates for one fitted ratio" miscounts in both directions: too many, since 15 are under no statement of the
  total; and too few, since two conditions of the fit are not postulate entities at all.
- Kill K1 (none redundant): does not fire. Nothing among my eleven was derived outright from the other 22 plus the
  foundation; H1's formula clause was derived from a weaker covariance premise (proved), P1's orientation clause
  and P5's used clause are redundant on stored or imported grounds (argued), P3 is half a theorem (stored).

## Unexpected links

- H1 and the stored mass law: in dimension five the single-constituent mass (1/2)<x x^dag>_0 of
  dark-tower-matter.where-mass-begins is s^2, the square of the coefficient of the central pseudoscalar in
  psi e_t rev(psi). The same s is the only spin-invariant quadratic form on the spinor ideal, which agrees with
  synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion read on symmetric forms. "Mass begins at one
  constituent" in dimension five and "mass begins at two" in dimensions three and four are then one statement: a
  single constituent is massive exactly where an invariant quadratic scalar exists.
- Additivity of momenta is not forced by covariance (dimension 3: one cross term; dimension 4: two). The stored
  two-constituent mass law m^2 = 2<x x^dag>_0 depends on that clause. A cross term would change where mass begins,
  hence the minimal massive hierarchy and the gauge algebras of the odd towers. Not pursued.
- P5 and lepton number: the energetic support stated for P5 does not cover a global charge with a massless carrier;
  the general clause is a statement about the thermal state (no chemical potential for a global charge), which
  belongs with the thermality premises (Q), (N+), not with the dark-matter subject.
- P2 and the programme's indifference premise: the scope "labels, not states" was added to P2 only; if P2 is typed
  as a specialisation, the programme premise inherits the excluded xi = 1 instance unless it is scoped too. This
  touches the measurement premises of phase 2, which also assume the programme premise.
- Flag as datum and phase 2's question B4 (which premise supplies the split defining the adjoint): the flag premise
  is a convention on what counts as one theory, so it cannot supply a split that any observable depends on. That
  agrees with phase 2's finding that the stored null pairs as vectors fix the split.

## Decisions for Leon

1. Accept or not the filed result on H1 (after review). If accepted: restate H1 as "a constituent has a spinor part
   in S; its momentum is a spin-covariant quadratic vector of it, normalised as j; momenta add", with the formula a
   theorem, or keep H1's text and add a note. Recommendation: note on H1 now, restatement when T14c is next revised.
2. P1: split into its three clauses (one tractor connection and normalisation; common N; orientation), mark the
   orientation clause as following from P2 version 2 on the stored reading and unused by the total, and keep the
   other two as the postulate. Recommendation: yes.
3. P5: retype as a consequence, at the import's level, of the interface premise's thermal flux and the no-remnant
   clause for baryon number in this tower and the mirror, and state the remaining clause (no chemical potential for
   a global charge) where it is used, or keep P5 with a note saying which clause is premise. Recommendation: the
   note now; the retyping needs the greybody estimate written out, a small task.
4. Flag as datum: merge into CPT covariance as its typing clause (MA's recommendation; I concur), or keep both and
   say in each that the flag premise is a convention on what counts as one theory with no observable content.
5. Simulation premises: type the six as model specification; record S2 and C as the two exclusive readings (W) and
   (C) rather than as jointly assumed (the two results' assumes edges list both). Recommendation: yes.
6. D: stop counting it with R1, R2, R3; record that D with R1 and R2 forces one quantum per de Sitter ball, so the
   de Sitter reading and the unit-ball reading cannot be held together. Recommendation: a note on D and on
   dark-matter.status-rule (iv).
7. Register the two unregistered conditions of the total, the costed single-ideal clause and the population of the
   odd towers, as postulate entities (maintainer-only), so that the past cone of the closed form shows what it
   rests on. Recommendation: yes; it raises the count under the total from 5 to 7 and is the truthful number.
8. P2 and the programme's indifference premise: if a `specialises` edge is drawn (MA's recommendation), add the
   scope note "labels, not states" to the programme premise or record there that its unrestricted form is excluded
   at the deposited energy. Recommendation: yes, together.
9. P4: retire as MA recommends, after giving dark-matter.mirror-tower-copy-one (v) its actual premises (common N
   from P1, the charge reading) so that the repointed edges do not hide a forward reference.
10. R3's unit: decide which cell radius R3 means when R2 is not assumed (the length of (E), this tower's cell, or
   the tower's own cell). MA's base result is stated under the first; the contact mechanism's wording suggests the
   cell R2 chose. Recommendation: fix it as this tower's cell radius d_b, the convention of T(c).
11. Not taken up: the two-constituent count in dimension five; whether (S) carried has a derivation by another
   route; the greybody estimate for P5; the common N of P1.
