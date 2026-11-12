# attack-AB (adversarial, cross-pollinating): op.matter-asymmetry-origin

Status: in progress. Labels used: proved / computed / argued / conjectured.

## Pre-registered kill conditions (written before any computation)

K1 (Q1, the exchange). Claim under attack: "the exchange of set and clear is an automorphism of all stored
structure, so the orientation is a label". My attack: find a stored structure the exchange does not preserve.
Kill condition for the attack: if for each of the six candidates (F1's zero, postulate (P), the datum of (N+), the
energy sign of the Z-adapted flag, chirality, the integer forms) an exact computation shows the exchange maps the
structure to an isomorphic one with only labels moved, the attack is dead and the label statement stands. Kill
condition for the label statement: one stored structure S, fixed by the kinematics and not by a solution, with
exchange(S) not isomorphic to S, or a second bit that the exchange cannot move together with the flag bit.

K2 (Q2, the operator). Claim under attack: "the stored charge Q is one operator, superselected, conserved by every
stored dynamics". Attack: compute on the sixteen (exactly, in the mode algebra) the abelian charges commuting with
(a) the stored gauge algebra, (b) the Dirac pair terms, (c) the Majorana element, (d) the slot-pair mixing
generators, and the mixed weak-isospin anomaly coefficient of each. Kill condition for the attack: if baryon number
n_B (the charge the measured baryon density reads) commutes with every stored term and has zero mixed anomaly
coefficient, or if the superselected tower charge is shown to be n_B, the attack is dead. Kill condition for the
constructive claim: n_B fails to commute with a stored term, or has a nonzero anomaly coefficient while the store
itself uses the equilibrium of the anomalous process, or the superselected tower charge is a different operator
(the residue label) whose superselection implies nothing about n_B.

K3 (Q2, counter-model). A model of the named premises (CPT covariance, flag as datum, Hypothesis (S), Premise (R),
real breaking) in which the baryon charge per unit entropy changes after the descent. Kill condition: if every
candidate model violates one of the named premises as stored (pinned text), no counter-model.

K4 (Q3, independence). Two states satisfying every stored premise except the valuation clause of Premise (epsilon),
with different epsilon (one of them zero). Kill condition: a stored premise or theorem that restricts the charge
sector (other than the valuation from the measured baryon density), found by lookup of the past cone of the charge
result. Look-elsewhere: no numerical match to 8.7e-11 will be attempted; none is reported.

## Orientation (direct lookups)
Read: the open problem; the flag chain (imported-flag-arrow-superselection v7, orientation-arrow-seventeenth-refutation
v10, premise-cpt-covariance v3, premise-flag-as-datum v4, superselected-hence-dark-exactly-stable v5,
stored-asymmetry-charge-not-number v10 with its proof, tower-charge-sector-label-temperature-not v5, z-adapted flags v1,
cpt-conjugation v4, arrow-frequency-are-one-bit-level v4, mirror-asymmetry-route-one v4, (N+) v12); the bit and switch
results and the note on the two orders; F1; the Standard-Model chain on the sixteen (proton-decay v5 and its check,
majorana-element v7, automorphisms-preserve-slot-pair-split v7, (S) v10, invariant-pairing v5, imported-anomaly-
coefficients v1, mass-terms-are-pair-terms v1); the neutrino premises; dark-tower-matter.mirrors-composition v3 and its
check; from other subjects: synthesis.imported-jarlskog-commutator-identity v2, quantity.jarlskog-invariant,
synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase v4, standard-model.fits-record-level.
Searches: "sphaleron" (one hit, a check), "anomalous electroweak" (none), "B - L", "baryon number", "CP violation".

Results in other subjects that bear on the problem (the cross-pollination):
- OBSTRUCTION from generations/flavour: the store holds a nonzero Jarlskog invariant and a result that the Cabibbo
  element needs a non-real up-down phase near a quarter turn. The conjugation of the CPT premise is antilinear and
  is premised to leave every action functional and its parameters unchanged. These collide (proposal B).
- TECHNIQUE from standard-model: the anomaly conditions are stored as an imported Fact for Y; the same traces for
  n_B, n_L, B - L were not computed anywhere (proposal A).
- COUNTER-MODEL from dark-tower-matter: the check of mirrors-composition already uses the equilibrium of the anomalous
  weak process (B = 28/79 (B - L), L/B = -51/28). The store therefore uses a baryon-number-changing dynamics after
  the descent while the charge result says the charge cannot be produced afterwards (proposal A, clause (vi)).

## Routes
Q1. R1 (the problem's own): test each listed candidate structure against the exchange. R2 (from flavour): test the
exchange against the stored family matrices, where the laws are known not to be conjugation-invariant. R3 (own):
the whole group of partial exchanges (Z_2)^5 on the five modes, to find which members are symmetries of the gauge
structure and which reverse which charge. Chosen: R2 with R3. Reason: R1's candidates all turn out to be marked
vectors or orientation conventions (AA's kill condition was not triggered by them, and I agree, see below), so the
only place an exchange can fail to be an automorphism is the laws' parameters; R2 goes there.
Q2. R1 (the problem's own): bound each channel. R2 (from superselection): identify the superselected operator. R3
(own): classify over the whole commutant of the gauge algebra on the sixteen which abelian charges each stored term
type conserves, and add the anomaly coefficients. Chosen: R3 with R2 as an identification. Reason: a class over
charges gives completeness on the charge side, which AA's class over dynamics does not (AA classifies the
generators against named charges; I classify every charge against the term types).
Q3. R1: independence by exhibiting sectors. R2: a derived relation that makes epsilon a function of another datum.
Chosen: both, briefly; no numerical matching attempted.

## What was established

### Q2 (kill condition K2 triggered against the constructive claim; K3 counter-model found)
Proposal A: synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them (check4 exit 0, validate ok).
Script: work/AB/q2_charges.py and the proposal's check.py.
- PROVED and COMPUTED (exact): the commutant of su(3)+su(2)_L+u(1)_Y on the sixteen is six-dimensional (species
  projections). Charges conserved by the Dirac pairings B(psi, a phi), a a slot operator, one doublet: span{Y, n_B,
  n_L}. Majorana element: leaves span{Y, n_B}. The 24 slot-pair root vectors: leave span{Y, B-L}. Mixed weak
  coefficient A_2 = 6 x_Q + 2 x_L: A_2(n_B) = A_2(n_L) = 2 per family, zero on Y and B - L; colour coefficient zero on
  all three. All conditions together: span{Y}. So no abelian charge of the sixteen except hypercharge is conserved
  by every stored or store-used term. n_B is broken by the slot-pair generators (stored) and has A_2 = 2 (new).
- COMPUTED: tr n_B = tr n_L = tr (B-L) = tr Y = 0 on the sixteen. The unit of the module (x = 1 on all species) is
  conserved by the Dirac terms only with slot charges h_v = h_w = -2, i.e. only as the colour-anomalous fourth charge
  of a two-doublet assignment (A_3 = A_2 = 8). So an excess equal on all sixteen states carries no baryon number.
- PROVED (arithmetic) GIVEN an imported equilibrium the store already uses: B_final = (28/79)(B - L)_initial.
  Counter-models to "no stored dynamics after the descent changes the baryon charge": initial (B, L) = (0, -79) ends
  with B = 28 (generation from zero baryon number); (79, 79) ends with B = 0 (erasure). Neither violates CPT
  covariance, the flag as datum, (S), (R) or real breaking, none of which constrains how the descent's datum is
  split between B and L. K3 met.
- ARGUED (reading of stored text): the stored statements are about three objects. The superselected "tower charge"
  is the residue r, a constant on a tower's sector (superselected-hence-dark step (1)): its superselection forbids
  exchange between towers and implies nothing inside a tower. Premise (R) protects "the descent's B - L". The
  charge Proposition and Premise (epsilon) speak of baryon number and baryons per unit entropy. Clause (ii) of the
  charge Proposition ("cannot be produced afterwards: the one channel superselection leaves open") infers
  conservation inside the tower from superselection between towers; that inference does not hold.
- Literature cited from memory (not stored Facts): the anomaly of the baryon current ('t Hooft 1976); its
  equilibrium above the weak scale (Kuzmin, Rubakov, Shaposhnikov 1985); 28/79 (Harvey and Turner 1990).
- Transport-absent (standard global-symmetry analysis); new for the store in scope and in what it is set against.

### Q1 (K1: the six listed candidates do not break the exchange; a seventh structure does)
Proposal B: synthesis.reversing-baryon-number-is-a-conjugation-and-reverses-the-jarlskog-invariant (check4 exit 0).
- The six candidates of RUN.md, one by one:
  (a) F1's zero. PROVED (one line): complement x -> x + 1 is not an automorphism of (F_2, +, .): it sends 0 + 0 = 0
      to 1, and 1 + 1 = 0; Aut(F_2) is trivial, and complement is an isomorphism onto the dual structure (XNOR, OR).
      So F1 as worded does distinguish nothing from something. Whether that survives depends on the order of
      construction: in the ladder order F1's bits label blades (directions) and the exchange fixes every label (AA's
      clause (ii); taken from AA, not recomputed by me); in the switch order F1's bit is the state of a
      switch and the off state is marked. Only correlates two labels unless the foundation identifies F1's zero with
      the Fock vacuum, which would make the flag kinematic and refute Premise flag-as-datum by its own condition.
      ARGUED. This is a decision, see below.
  (b) Postulate (P) and (c) the datum of (N+): (N+) says in its own text that the orientation of the unit relative
      to the time orientation is a datum it assumes. A correlation of two labels. Read, not recomputed.
  (d) Energy sign of the Z-adapted flag: stored clause (iv) already shows s_0 and the family both flip under J -> -J
      and their product does not. A correlation; the invariant product is a kinematic sign. Read, not recomputed.
  (e) Chirality: the total exchange on three pairs reverses the volume element (AA (iii), stored). Correlation.
  (f) Integer forms: AA (v), (vi): no invariant integer state, an invariant one with a half. Agreed; a marked
      vector again.
  None fixes the sign. On these I agree with AA.
- The seventh structure, from flavour. PROVED (exact, check): every linear map of the sixteen normalising the gauge
  algebra fixes n_B (Q is the only species of dimension 6, hypercharges distinct). COMPUTED (exhaustive): of the 32
  partial exchanges of set and clear on the five modes, 4 reverse n_B, 2 normalise the gauge algebra (identity and
  total), 1 reverses Y, B - L, n_B together (total), and it maps the sixteen to the conjugate sixteen: as a map of
  the sixteen it is antilinear. PROVED: det[H_u, H_d] is unchanged by a change of family basis and reversed by
  conjugation, so J -> -J; zero for real pairs. ARGUED (clause (iv) and reading): with J != 0 no map is both an
  automorphism of the laws at fixed direction of time and a reversal of the baryon charge. The product
  sign(baryon charge) x sign(J) is invariant under the whole class.
- Consequence for the constructive answer (ARGUED): "the orientation is a label by an exact automorphism" holds for
  the algebra and for the gauge structure, and fails for the stored laws unless the conjugation is read as carrying
  each family term to its adjoint, in which case it reverses the arrow too. The orientation is a joint label (with
  sign J, or with the arrow). The sign of the baryon charge relative to J and the arrow is not made initial data by
  the exchange argument; with J != 0 it is of the kind a dynamics could fix. Not decided: whether a stored dynamics
  does.
- Transport-absent (textbook CP analysis; the kaon charge asymmetry and Sakharov 1967 cited from memory).

### Q3 (K4: no restricting premise found; independence is by the premise's own wording, plus one relation)
- ARGUED from stored results: Theorem tower-charge-sector-label (i), (ii) puts every charge sector in every window
  and gives every Gibbs product state positive weight on every sector; nothing in the past cone of the charge result
  restricts the sector. So states with any epsilon, including zero, satisfy every stored premise except the
  valuation clause of Premise (epsilon). This is independence only in the sense the premise already declares; I do
  not count it as a new result and did not file it.
- From proposal A (vi), a relation that does bear on the register: if the anomalous process equilibrated, the
  baryons per unit entropy are 28/79 of the descent's B - L per unit entropy, so the free input is (B - L)/s =
  (79/28) x 8.7e-11 = 2.45e-10 (arithmetic), and the registered number is a derived one. This does not trigger the
  refutation condition (B - L per entropy is not another registered number), but the premise's wording should name
  the datum.
- Bound: per mode |epsilon| <= 1/2 from exclusion (AA (v): |q| <= m). Nothing sharper. No numerical match to
  8.7e-11 was attempted; look-elsewhere count: zero trials.

## Where I disagree with AA
1. AA's reading of the exchange claim says the positions of a switch "are not distinguished by anything the
   foundation holds" in the ladder order, and that in the switch order the orientation "is a label, moved by an inner
   automorphism". The algebra is right (I reproduced the action on n_B, B - L, Y on all 32 states). The inference to
   "label" needs the exchange to be an automorphism of the laws, which AA leaves open. Proposal B computes that it is
   not, in the quark sector, unless it also reverses J or the arrow: det[H_u*, H_d*] = -det[H_u, H_d], pinned values
   576 I, -(27815/27) I, 14 I on three samples.
2. AA's exchange is complex-linear and inner in Cl(5,5). As a map of the sixteen it lands in the conjugate sixteen;
   by proposal B (i) no linear map of the sixteen normalising the gauge algebra reverses n_B. So "inner" is true of
   the algebra and says nothing about the module of one chirality, which is where the matter content lives.
3. AA's membership table and my proposal A overlap on the Majorana element and the 24 generators (same facts, mine
   over the whole commutant of charges, AA's over the generators). No contradiction. The referee should treat A's
   clauses (iii), (iv) as restating AA's table and judge A on (i), (ii), (v), (vi) and the reading. Merge candidates.
4. AA concludes "inheritance is forced is FALSE as an unconditional theorem". Agreed, and stronger: by A (v), (vi) it
   is false for baryon number even with the unification-scale bosons decoupled.

## Unexpected links
- Hypothesis (B') of tower-charge-sector-label represents the residue superselection by invariance under a uniform
  rotation of each tower's boundary modes, i.e. it makes each tower's mode number N superselected. The mass-terms
  theorem (ii) has [N, X] = -2X for every pair term, Dirac and Majorana alike, and only N_a - N_c commutes with
  both. So under (B') read with the uniform rotation no mass term is an observable. Either the rotation of (B') is
  the N_a - N_c one (then the superselected charge is a spin-like label and not a matter number) or (B') excludes
  the stored mass terms. ARGUED from the two stored statements, not recomputed. A possible contradiction for the
  next consistency run.
- The two-doublet Dirac assignment has a fourth conserved charge with colour coefficient -2(h_v + h_w): the store's
  five-mode algebra contains the Peccei-Quinn-type charge exactly when slot creation and contraction are not
  conjugate. This bears on attack item 4 of the problem (a relaxing angle) and on op.strong-cp. COMPUTED (A (ii)).
- The mirror: mirrors-composition finds the mirror plasma degenerate from the start. The coefficient 28/79 is a
  linear-response number for a hot plasma. If the datum copied along the reversal orbit is B - L, the mirror's
  baryon number is c' (B - L) with c' not shown equal to 28/79, and the mirror share f_2 = 1 (equal baryon number)
  does not follow from the copy. CONJECTURED lead; nothing computed.

## Decisions for Leon
1. Which operator is the inherited charge. Recommendation: B - L. Restate Premise (epsilon), the charge Proposition
   (i), (ii) and the open problem's "known" so that the datum of the descent is the total B - L per unit entropy,
   2.45e-10 if the anomalous process equilibrated, with baryon number derived. Reword the sentence "cannot be
   produced afterwards: the one channel superselection leaves open" in the charge Proposition (ii): superselection of
   the residue does not bear on a charge inside the tower.
2. Import as Facts (currently used but not stored): the anomalous weak process and its B + L violation; its
   equilibrium above the weak scale; the coefficient 28/79 with its conditions. Cited from memory in proposal A.
3. The CPT premise's action clause against the quark phase. Options: (a) restrict the action clause to the gauge
   and gravitational sectors and state that in the family sector the conjugation carries each term to its adjoint
   (then it is the true CPT type and reverses the arrow, consistent with the one-bit result); (b) keep it as worded
   and accept that it requires J = 0, against the stored Cabibbo result and the recorded J. Recommendation: (a),
   and add to the seventeenth refutation a sentence that what it makes initial data is the orientation jointly with
   the arrow, not the sign of the baryon charge relative to the quark phase.
4. The open problem. Recommendation: keep open, and reword the success clause's second branch: a no-go must be for
   B - L, conditional on (R); for baryon number the stored content already contains a counter-model. Add to
   "known": the commutant classification, the coefficient, and that with J != 0 the sign of the asymmetry relative
   to the quark phase and the arrow is not a label. Add as a new attack item: decide whether the descent's state
   has a definite B - L and whether the Majorana washout under (R) is bounded (a rate, not computed here).
5. F1's zero. Decide whether the foundation identifies "nothing" with the off state of a switch (the switch order)
   or only with the empty blade label (the ladder order). In the first case the flag is kinematic at the foundation
   and Premise flag-as-datum needs restating. Recommendation: record the dichotomy in the note on the two orders; no
   premise change now.
6. Hypothesis (B') against the mass terms (first unexpected link): send to the next consistency run.
7. The mirror's conversion coefficient (third unexpected link): a new open item under the dark-to-baryon count if
   decision 1 is taken.

## Next step
A rate-level treatment of the Majorana washout under (R) and of the freeze-out of the anomalous process, both
outside exact algebra; and how the conjugation acts on spinor fields, which the conjugation result leaves uncovered.
