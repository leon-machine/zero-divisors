# Attacker QA, run 2026-11-10-phase3, cluster Q (quantum field theory scope)

Own items: Q1 (constructive), Q4 (findings, note text). Adversarial on QB's Q2 and Q3.
Status of this file: COMPLETE for the attack round (Q1 filed; Q4 drafted; adversarial tests of Q2 and Q3 done on QB's drafts in work/QB, since QB's findings file still showed only routes and kill conditions when read three times).

## Q1. One-loop self-energy and vertex by extension of distributions

### Orientation (direct lookup)
- Stored base: synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants (v4).
  It already holds: scaling degrees 5 (self-energy), omega = 1; vertex omega = 0; covariant difference spaces
  4 / 2 (self-energy, without / with reflection), 2 / 1 (vertex); joint space under the Ward-Takahashi identity
  2 with reflection and c_V = -c_2 forced. So the RUN's "first computation" (degrees, number of constants) is
  ALREADY STORED. Not refiled.
- What the stored result does not have (its own flags): EXISTENCE of a Ward-preserving extension of self-energy and
  vertex is imported (Scharf; Fact synthesis.imported-epstein-glaser-...(iii)), "proved here only for the vacuum
  polarisation". The self-energy kernel itself is stored only as "numerator structure x/s^3" in Feynman gauge; the
  vertex kernel is not written down at all.
- So the target is: explicit extended kernels, and the Ward identity as a theorem about them (not imposed).

### Routes
1. Differential renormalisation of the vertex (Freedman, Johnson, Latorre): split the vertex into total derivatives
   plus one 1/s^2 delta piece; then verify the Ward identity. Delivers the textbook form; needs an 8-dimensional
   finite-part computation to fix the constant; termwise z-integrals are infrared divergent. Heavy.
2. Momentum space with a regulator and translate. Delivers nothing new, needs a regulator: against the item's point.
3. (Own) Cut-off extensions adapted to the Ward identity: extend the vertex by subtracting the test function's value
   at the origin on the cylinder |x - y| < 1/mu (the length of the photon line), the self-energy by first-order
   Taylor subtraction on the ball |x - y| < 1/mu. The z-integrated vertex is, off the diagonal, (x-y)_nu Sigma(x-y)
   (position-space form of the differential Ward identity). Then the Ward identity for the extended pair reduces to
   an identity of absolutely convergent integrals. Delivers existence constructively; exact constants by radial
   integrals; the relation to route 1 as a rational number (the ratio of the two differential-renormalisation scales).
Choice: route 3, with the route-1 scale relation as an exact corollary and cross-check against the literature.

### Kill conditions (registered before computing)
- K1: the Ward defect of the common-radius pair is not zero, or is not computable exactly. Then report the defect
  and record that the Ward identity is imposed by a finite renormalisation, not derived.
- K2: the scale relation implied for differential renormalisation disagrees with the literature value
  (ln(M_Sigma/M_V) = 1/4 in Feynman gauge, from memory, to be checked on the web). Then conventions or proof wrong.
- K3: the log coefficients of the explicit extensions contradict the stored c_V = -c_2 or the textbook
  Z_2 coefficient (gauge parameter times e^2/(16 pi^2), zero in Landau gauge).
- K4 (scope): if the argument needs an infrared regulator anywhere (z-integral, test function not compact), say so.

### Result (Q1)
Proposal filed: `synthesis.one-loop-self-energy-and-vertex-extend-with-the-ward-identity-holding-at-a-common-cut-off-length`
(check4 exit 0, no findings; validate ok; registered with propose_claim; coverage.yaml in the folder).
Scripts: proposals/<id>/check.py; drafts in work/QA/draft-q1/.

Established, with labels:
- (computed) Kernels on the Euclidean section in Cl(4,0), covariant gauge parameter xi:
  Sigma(w) = -xi e^2 w/(4 pi^4 s^3) + (3 + xi) e^2 m/(16 pi^4 s^2) + (degree <= 3). The massless self-energy
  vanishes identically off the origin in the Landau gauge. Degrees 5 and 8, omega 1 and 0: as already stored.
- (proved) Off the coincident point: div_z Lambda = delta(v) Sigma(u) - delta(u) Sigma(v), and the z-integrated
  vertex is (n.w) Sigma(w) (position-space form of dS/dp = -S gamma S; proof by uniqueness of the decaying
  solution of (nabla + m) G = 0). Both for every m >= 0 and ANY photon kernel depending on x - y alone.
- (proved) The Ward-Takahashi identity holds on the EXTENDED kernels, exactly, for the pair: self-energy with
  first-order Taylor subtraction on the ball |x - y| < l; vertex with the value at the origin subtracted on the
  cylinder |x - y| < l (photon vertex anywhere). No constant is chosen: K1 did not fire. The identity is an identity
  of absolutely convergent integrals (Fubini, integration by parts in the photon vertex, and the chain-rule fact
  that the t-gradient of f at 0 is the gradient of F(w) = f(w,0) - f(0,w) at 0).
- (computed) Different lengths: the identity fails by (xi e^2/(8 pi^2)) ln(l_V/l_Sigma) times a local term. Scale
  derivatives +xi e^2/(8 pi^2) (self-energy, coefficient of dslash delta) and the negative (vertex): the stored
  c_V = -c_2, and the textbook Z_2 coefficient xi e^2/(16 pi^2) per ln mu^2. K3 did not fire.
- (computed, exact pairings) In the logarithmic form of the stored result the cut-off extensions have
  ln(M^2 l^2) = 1 (order zero) and 3/2 (order one); the identity holds exactly when ln(M_Sigma^2/M_V^2) = 1/2,
  i.e. ln(M_Sigma/M_V) = 1/4, the differential-renormalisation value (checked on the web: quoted as eq. (36) of
  arXiv:hep-th/9709067, attributed there to Haagensen and Latorre for a general covariant gauge; the 1992 paper is
  cited from memory). K2 did not fire. A second, cut-off-free route to the 1/2 is in the check (Leibniz rule on
  w_nu times the logarithmic form).
- (stored count + the above) All Ward-preserving covariant reflection-symmetric pairs at one loop: this pair plus
  delta m and Z_2 = Z_1. So the stored import of EXISTENCE (Scharf) is no longer needed for these two kernels at
  one loop. It is still needed at higher orders and for the four-photon and three-current kernels.
- K4 (infrared): no infrared regulator. The vertex falls off as |z|^-6, so the z-integral converges; the
  test function t_nu g(w) of the zero-transfer form is never used as a test function (the proof pairs with
  compactly supported f only). NOT treated: on-shell conditions, the infrared divergence of the on-shell Z_2,
  the adiabatic limit.

Candour on Q1.
- Everything is textbook physics; transport-absent. The geometric algebra adds no content beyond notation: on the
  Euclidean section the kernels are products of vectors of Cl(4,0), no matrices and no imaginary unit. I say so in
  the entity's note. The only possibly new element is the arrangement (cylinder cut-off, which makes the identity
  exact without computing the vertex); not claimed as new.
- The RUN's "first computation" (scaling degrees, number of constants) was already stored in clause (i), (iii) of
  the regulator-free result; I did not refile it.
- The massive case is proved GIVEN standard properties of the massive Euclidean propagator (fundamental solution
  on both sides, exponential decay, local integrability, the stored short-distance expansion); the checks are on
  the massless kernels and the order-m coefficient only.
- The check cannot test clause (iii) itself by an eight-dimensional integral; it tests the ingredients (monogenic
  propagator with unit flux, dslash(w_nu S0) = gamma_nu S0, the Taylor matching, the constants). The theorem is the
  proof. A referee should attack Steps 3 to 5 of the proof.
- The form factor F_2(0) = alpha/(2 pi) is NOT recomputed by extension (stored with regulator fields).
- Wick rotation to the Feynman distributions is taken as in the stored result, not shown.

Answers in advance to QB's adversarial list (RUN): Ward identity checked or imposed: derived, not imposed, for the
common-length pair; imposed (one constant) for any other pair. Gauge parameter: every xi, the anomalous term is
proportional to xi; Landau gauge degenerate at m = 0. Infrared regularisation: none hidden (above). Does the GA
form add anything: no.

## Q4. What a full theory would need (findings; a note is maintainer-only)

Scope fixed by Leon's decision 2 of this run: the matter and gauge sector on the classical GTG background. The
series' position is that the graviton does not exist; quantising the gravitational gauge fields is neither a gap
nor a goal and is not listed below.

Kill condition registered before searching: the store already holds a route to a non-perturbative interacting
theory. Result: partly fired. The RUN's sentence "no route to a non-perturbative interacting theory exists in the
graph" is slightly too strong: the store holds a non-perturbative DEFINITION AT FINITE SPACING for one factor
(the weak factor's rotor lattice in Wilson's form, `synthesis.weak-factor-rotor-lattice-strong-coupling-area-law`,
with `synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law`
and the colour subgroup result `synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three`).
What is absent is every step from there to a theory: a continuum limit, dynamical chiral fermions, the other
factors, covariance.

What the store has (perturbative, each with its scheme): free Dirac and photon fields; tree level; one loop with
regulator fields under the Krein premise; the regulator-free vacuum polarisation and, with Q1, self-energy and
vertex at one loop; two-loop vacuum polarisation in dimensional regularisation; an LSZ tree cross section; the
triangle anomaly; chiral abelian loops (BMHV); field-level BRST; imported causal perturbation theory (formal power
series, local algebras without the adiabatic limit, Yang-Mills renormalisable on gravitational fields); local
covariance with scaling (imported); the leading curved-field kernel.

What a full theory needs and the series lacks:
1. A definition of the interacting theory that is not a formal power series. All stored loop results are
   coefficients of a series in the coupling. Literature (from memory): the series is expected to diverge (Dyson)
   and not to be Borel summable in four dimensions (renormalons). Extension of distributions (the stored scheme)
   is order by order by construction and cannot supply this.
2. Either of the two known kinds of definition:
   (a) a regulated theory with a controlled limit. Stored: the floors keep the charge and the continuity equation
   but no boost, for every weighting (`synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off`).
   IMPORTANT reading point: that no-go excludes the floors as a COVARIANT regulator. It does not exclude them as a
   constructive cut-off: the constructive theories that exist (below) all use non-covariant cut-offs (lattice,
   momentum, box) and prove covariance of the LIMIT. What the series lacks is the limit and the proof, not a
   covariant cut-off. No covariant non-perturbative regulator is known to anyone; asking for one is asking for
   more than the literature has.
   (b) the continuum limit of the rotor lattice. Needs, none stored: (i) existence of the limit at weak coupling
   for the non-abelian factors (asymptotic freedom makes it plausible; unproved in four dimensions, the Yang-Mills
   existence problem; partial ultraviolet stability results by Balaban, from memory); (ii) the abelian factor and
   the scalar quartics: expected trivial as continuum theories (phi^4 in four dimensions proved trivial, Aizenman
   and Duminil-Copin 2021, from memory; QED triviality expected, not proved), so these sectors exist only with a
   physical cut-off or inside a larger asymptotically free structure; the store already shows the scalar sector
   reaching strong coupling at a few TeV on one branch
   (`synthesis.rung-field-quartics-run-to-strong-coupling-within-a-few-tev-on-the-transmutation-branch`);
   (iii) chiral fermions: the stored lattice results have no dynamical fermions (a frozen doublet only); a lattice
   with the series' chiral content meets fermion doubling (Nielsen and Ninomiya), exact lattice chirality exists
   for vector-like theories (Ginsparg-Wilson), and a non-abelian chiral gauge theory on a lattice is an open
   problem in the literature (from memory); (iv) recovery of Lorentz and displacement-gauge covariance in the
   limit; (v) reflection positivity and the reconstruction of a positive state space (the gauge-invariant lattice
   needs no Krein form, stored; a statement of Osterwalder-Schrader positivity in the series' algebra, with the
   unit I_4 and the Wick rotation the loop results use as "standard", is not stored).
3. A positive physical state space beyond perturbation theory. The Krein premise and BRST are perturbative
   (stored: Neuberger's 0/0 for lattice BRST, Gribov copies). Only the gauge-invariant lattice avoids this, and it
   is at finite spacing.
4. Control of the infrared: charged states, the adiabatic limit of causal perturbation theory in electrodynamics,
   the on-shell field normalisation (infrared divergent at one loop; Q1 does not treat it). Confinement in the
   continuum does not follow from the stored strong-coupling area law (the stored result says so).
5. On a gravitational background: the perturbative theory is covered by the imported local-covariance framework
   (existence of Ward-preserving extensions on the field is not; see the adversarial notes on Q2). Non-perturbative
   results on curved backgrounds are essentially absent from the literature even in low dimension (from memory:
   P(phi)_2 on de Sitter space, Barata, Jaekel and Mund).
6. The tower gives CAR only (`field-theory.no-canonical-commutation-relations-tower`): the photon is attached as
   an elementary Fock field. A full theory built on the tower must say whether gauge bosons are elementary
   (then the construction problem is the standard one) or composite (then nothing stored constructs them).

Prior art, constructive results in low dimension (all from memory, to be checked before a note is stored):
P(phi)_2 and phi^4_2 (Glimm, Jaffe; Nelson; Lorentz covariance of the limit by Cannon and Jaffe), Yukawa_2,
phi^4_3 (Glimm and Jaffe; Feldman and Osterwalder), the Gross-Neveu model in two dimensions (Gawedzki and
Kupiainen; Feldman, Magnen, Rivasseau and Seneor), which is the nearest to the series since it is fermionic and
asymptotically free and its expansion converges because of the Pauli principle; Yang-Mills in two dimensions;
abelian Higgs in two and three dimensions (Brydges, Froehlich and Seiler; King); ultraviolet stability of lattice
Yang-Mills in three and four dimensions (Balaban) and of QED_3 (Dimock); triviality of phi^4_4 (Aizenman and
Duminil-Copin). No interacting theory satisfying the Wightman or Haag-Kastler axioms has been constructed in four
dimensions by anyone.

Stored places that count a graviton (reported per decision 2; NOT extended, not read in full; from a text search
for "graviton"): `hawking.helicity-lift-joints-itemised` (joint J1 kinematics; spin-2 clause),
`hawking.joint-j3-s-wave-reduction` (the spin-2 channel clause of J3),
`synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional`,
`synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature` and
`synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet` (J3 for graviton channels),
`scrambling.imported-collars-coframe-exceptional-set-helicity`,
`synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free` and
`synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content` (additive counting
readings with a graviton term, epsilon = 1), `synthesis.dimmed-burst-time-rescaled-copy` (emission "plus
gravitons"), `dark-matter.imported-massless-graviton-production-rate` with its users
`dark-matter.seeding-gravity-floor-dark-towers-temperature`, `dark-matter.coefficients-floors-they-give-what-gravity`,
`synthesis.seeding-remainder-excludes-perturbative-pati-salam`, `synthesis.untuned-fit-caps-lightest-heavy-neutrino`
(graviton-mediated production: this is a dark-matter seeding RATE that depends on a graviton exchange, not only a
count), `dark-matter.imported-gravity-only-coupling`, `dark-energy.acoustic-no-go-one-way-grip`,
`dark-energy.lift-inherits-no-go-steps-itemised`, `dark-energy.conclusion-does-not-depend-ontology-level`
("composite and fundamental reading of the graviton"), `dark-energy.point-infinity-has-no-physical-fluctuation`,
`synthesis.promoted-norm-one-global-pair`, the notes `note.hawking.point-contact-weinberg-witten-triage`,
`note.mass.point-contact-what-gravity-why-everything`, `note.standard-model.what-settled-what-gravitational-channel-cannot`
(graviton loops in the running), and open-problem text near lines 1569 to 1606, 2914 to 2941, 3263 to 3281 of
store/open_problems.yaml. The "nonlinear graviton" entities of the correspondence subject use Penrose's name for
a classical construction and do not count a quantum.

### Draft note text (for the maintainer; house style; not filed)
Title: Scope of the quantum field theory in the series: perturbative, on a classical gravitational field

The quantum field theory of the series is perturbative and lives on a classical gravitational field. The
gravitational gauge fields are not quantised and the series does not hold that a graviton exists; this note
concerns the matter and gauge sector only. What is stored: free Dirac and photon fields with the unit $I_{4}$;
tree-level exchange; one-loop electrodynamics; the one-loop vacuum polarisation, and the one-loop self-energy and
vertex with their Ward identity, by extension of distributions with no regulator; the two-loop vacuum polarisation
in dimensional regularisation; one S-matrix element; the chiral anomaly and its cancellation per generation; and
the imported framework of causal perturbation theory with local covariance on gravitational fields. Each is a
coefficient of a formal power series in the couplings. Nothing stored defines an interacting theory beyond that
series, and later work should not reopen the question without one of the following, none of which the series has.
(1) A limit of a regulated theory. The floors of the tower keep the charge but no boost; that excludes them as a
covariant regulator, not as a cut-off whose limit is shown to be covariant, which is how every existing
construction proceeds. The limit and the proof are missing. (2) A continuum limit of the rotor lattice. The store
defines the weak factor on a lattice of rotors without gauge fixing and computes its strong-coupling expansion;
missing are the weak-coupling limit, dynamical chiral fermions (fermion doubling; a non-abelian chiral gauge
theory on a lattice is open in the literature), the abelian factor and the scalar quartics (expected to have no
interacting continuum limit on their own), the recovery of covariance, and reflection positivity in the series'
algebra. (3) A positive state space beyond perturbation theory: the Krein-form premise and BRST are perturbative.
(4) Control of the infrared: charged states, the adiabatic limit, confinement in the continuum. Under these
limits the stored loop results are to be read as the perturbative content of whatever theory exists, with the
scheme of each stated on it. Prior art: interacting theories have been constructed in two and three dimensions
(scalar, Yukawa, Gross-Neveu, abelian Higgs, two-dimensional Yang-Mills) and none in four; the four-dimensional
scalar quartic theory is proved to be free in the continuum. These are quoted from memory and are to be checked
before this note is stored.

## Adversarial: Q2 and Q3 (QB)

QB's findings file showed routes and kill conditions only; I tested the drafts in work/QB
(`synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion`, entity and check;
`synthesis.curved-field-vacuum-polarisation-freedom-is-five-local-covariant-constants-of-which-one-is-transverse`,
check only, entity not yet written). I file nothing on Q2 or Q3.

### Q3 (protraction identity). Verdict: holds up; three points to state.
Independent exact test, my own script work/QA/q3_adversarial.py (lib/gtg.py, a generic non-diagonal polynomial
coframe at a rational point, not QB's samples):
- torsion-free Omega (solved): d_a ^ calR(a ^ b) = 0 for all b, curvature nonzero, pair symmetry holds. K3a not fired.
- generic added torsion, and an axial torsion with a constant spin trivector (the Einstein-Cartan case of a Dirac
  source): the identity FAILS. So the derivation from torsion is not empty. K3b not fired.
- QB's clause (ii), (1/2) C_R(g^mu) = D ^ Theta^mu - Theta^nu ^ D_nu g^mu, recomputed independently with my own
  jets: holds with QB's signs on both torsion samples (nonzero both sides), and trivially on the others.
- Counter-model to the CONVERSE: Omega = 0 with a non-holonomic coframe has zero curvature, so the identity
  holds, and nonzero torsion. The identity is necessary for vanishing torsion, not sufficient. QB's draft does not
  claim the converse, but the stored curved-field result says "vanishing torsion is used in the form of the
  protraction identity", and it also uses the spin connection of the derived metric, which needs vanishing torsion
  itself. Suggest one sentence in QB's entity: the converse fails (model above).
"Already stored under another name?" Searched store, docs and lib for protraction, Bianchi, cyclic, pair symmetry.
Not stored as a result. It is (a) a named hypothesis of the curved-field result, (b) a constraint imposed to define
Weyl-type maps in several checks, (c) reachable only through the imported dictionary
(`synthesis.imported-gtg-dictionary`, clause (iv): calR read as the Riemann tensor of the derived metric, then the
classical identity), and (d) several entities say "torsion-free (the curvature of Omega obeys the first Bianchi
identity)" as if the two were the same condition, which by the counter-model they are not
(`synthesis.curvature-only-tractor-actions-are-macdowell-mansouri` and the frozen-point Weyl-squared result use
that wording; not read in full).
"Is the proof a restatement of a definition?" No. In the store's definition vanishing torsion is a field equation
for spinless matter (clause (f)), not part of the definition of the field, and the identity fails without it
(samples). It IS classical (Lasenby, Doran and Gull, Section 5; QB says so) and transport-absent; with the
dictionary Fact it was already available by import. What the store gains is a proof inside the algebra and the
torsion formula of clause (ii). The clause (iv) kernel dimensions d^2(d^2 - 1)/12 are the classical count of
algebraic curvature tensors; "computed for d = 3, 4, 5" is the right label.
Scope remark for the store: with Dirac matter as a SOURCE (Einstein-Cartan choice of clause (f)) the identity
fails; results that apply it to fields sourced by spin must say the field is torsion-free by hypothesis.

### Q2 (local covariance and the curved-field freedom). Verdict: the count is right as far as I can test it; the
clause is NOT closed by it; six conditions must be on the statement.
What QB's check does (read, not rerun in full): invariant tensors under the Lorentz algebra for the terms the Fact's
clause (iii) allows, then K(D chi) = 0 on K = c1 Lap + c2 D(D.) + c3 m^2 + c4 calR + c5 calR(.), solution
(c, -c, 0, 0, c), the Maxwell operator D.(D ^ A): five constants, one transverse.
1. Parity-odd terms. The Fact's covariance is under embeddings preserving orientation, so the pseudoscalar is an
   allowed invariant. QB's count is over the connected Lorentz algebra, so it includes them (four invariants with
   four vector slots, six bilinear forms on bivector maps): correct. They disappear for two different reasons that
   the entity should state separately: the term with the alternating tensor on two derivatives vanishes because
   second covariant derivatives of the scalar delta commute on a torsion-free field; the dual-Ricci term
   (a ^ b contracted with I calR) vanishes BY THE PROTRACTION IDENTITY (6 -> 2 in QB's check). So Q2 depends on
   Q3: a cross-link, and a reason to cite Q3's result, not the hypothesis. With torsion both terms survive.
2. Time-ordered product against parametrix against state. The Fact is about time-ordered products (state
   independent). The stored curved-field result is about the trace form of the parametrix, "not a state's current
   two-point function". The freedom statement is correct for the c-number part of T(j j); a state's kernel differs
   by smooth state-dependent terms that have no extension freedom. The entity must say which object it is about.
3. The Fact's sources. Checked on the web: Hollands and Wald (gr-qc/0103074) "restrict consideration in this paper
   to the theory of a real scalar field", and require ANALYTIC dependence on the metric ("continuity alone would
   not eliminate non-analytic local curvature ambiguities"). So for the Dirac current the Fact is used outside its
   sources, as the Fact itself flags. Candidate sources for the Dirac case, found on the web, content not read in
   full: J. Zahn, "The renormalized locally covariant Dirac field", arXiv:1210.4031; J. Zahn, "Locally covariant
   charged fields and background independence", arXiv:1311.7661 (Proposition 3.2 there is a Ward identity for the
   divergence of the gauge current; its Section 3.1 says current conservation can be ensured by a choice of the
   parametrix). These are what K2c needs: EXISTENCE of a Ward-preserving local covariant extension on the field is
   not in the stored Fact. Maintainer-only: add them to the Fact, or import the curved-field Ward identity.
4. "Difference" only. The result classifies differences of two Ward-preserving extensions. Without existence it
   says: if any exist, they differ by Z_3. That is the same logical shape as the flat clause (iii) of the stored
   theorem before Q1. Title "freedom is five constants of which one is transverse" should carry "if a
   Ward-preserving extension exists" at every level.
5. Does it close clause (iv) of the curved-field result? No. Clause (iv) rests on clause (iii) there (degree
   counting, argued, with the first Hadamard transport equation as an unstored hypothesis). The new result closes
   only the sentence "that the Ward identity on the field then leaves the single constant Z_3 is argued and not
   derived here", and only conditionally on existence and on the Fact covering the Dirac current. Clause (v) of
   the flat theorem stays argued.
6. Class of fields. The Fact needs a smooth globally hyperbolic derived metric on the invertible region and a
   torsion-free field. Stored fields with horizons in the Painleve-Gullstrand gauge are fine away from the
   singularity; fields with spin torsion are outside. Transversality is tested on sample fields (sampled check):
   "computed", unless the proof gives D.(D ^ D chi) = 0 in general (it should: D ^ D chi = 0 without torsion and
   D.D. of a bivector vanishes by the symmetry of the Ricci map, which again is Q3).
Not found wrong: the count 5 (2 symmetric derivative terms, m^2, scalar curvature, Ricci) and the single transverse
combination agree with what the classical Maxwell operator on a curved field requires.

## Unexpected links
- Q3 -> Q2: the parity-odd dimension-two term of the curved-field freedom is killed exactly by the protraction
  identity, and the general transversality of the Maxwell combination uses the symmetry of the Ricci map, also Q3.
- Q1 -> curved field: the Ward identity of Q1 uses only that the electron propagator is a fundamental solution on
  both sides and that the photon kernel depends on the electron line's ends alone. With a Hadamard parametrix (a
  fundamental solution up to a smooth kernel) the same cylinder cut-off should give the identity on a gravitational
  field up to smooth terms. Not attempted. Candidate route to the missing "Ward identity on the curved field" for
  the self-energy and vertex; the vacuum polarisation needs a different argument.
- Q1 -> floors: the floor cut-off keeps the Ward identity and no boost; the cut-off extension keeps both. The two
  results together say that the obstruction to a native regulator is covariance of a mode cut-off, not the Ward
  identity.
- Q4 -> floor no-go: the stored no-go is about covariant regulators; constructive theory never needs one. The
  open problem's attack item "the floors are excluded for every weighting" reads too strongly.
- Q4 -> dark matter: the seeding results use a graviton-mediated production rate (an imported Fact). Under
  decision 2 that is more than a count; flagged for the maintainer, not touched.
- Counter-model of Q3's converse against stored wording that equates "torsion-free" with "obeys the first Bianchi
  identity".

## Decisions for Leon
(Fix round: item 2 is corrected by findings/fixes-QA.md. The Q1 result holds on the Euclidean section only and supports, without discharging, the imported existence for the time-ordered products; statements above that the import "is no longer needed" are withdrawn.)
1. Q1 premise edge (maintainer-only): the Q1 proposal has the Krein-form premise in its cone through the stored
   regulator-free result and states it in the text; should it carry its own `assumes` edge to
   synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields, as the stored result does?
   Recommendation: yes, for the same reason.
2. Record on the stored result: the regulator-free result's flag "existence of Ward-preserving extensions beyond
   the vacuum polarisation is imported" is now false at one loop for self-energy and vertex if Q1 is accepted.
   Recommendation: a note on that entity and on op.qft-loops-and-renormalisation (attack items 1 and 2: done at
   one loop for these two kernels; four-photon, three-current and two loops remain). Do NOT retire the
   Pauli-Villars clause of the Krein premise yet: F_2(0) is stored only with regulator fields.
3. Q4 position (the one real decision): does the series claim that a continuum interacting theory of its matter
   and gauge sector exists, or that the physical theory is the cut-off one (finite floors, covariance emergent)?
   The abelian and scalar sectors are expected to have no interacting continuum limit on their own, and the stored
   scalar sector reaches strong coupling at a few TeV on one branch. Recommendation: record the scope note (draft
   above) now with neither claimed, and open no problem until one of routes (1), (2) has a first computation.
4. Q4 wording: restate the open problem's line "the floors are excluded for every weighting" as "excluded as a
   covariant regulator; not excluded as a cut-off with a covariant limit". Recommendation: yes.
5. Q4 prior art: the constructive-theory citations in the draft note are from memory. Import as a Fact after a web
   check, or keep the note without names? Recommendation: check and keep the names; no Fact (nothing uses them).
6. Q2 (from the adversarial test): add the Dirac-field sources (Zahn, arXiv:1210.4031 and arXiv:1311.7661) to the
   local-covariance Fact, and decide whether to import the curved-field Ward identity (existence), which QB's
   result needs to be more than conditional. Recommendation: import after reading the two papers; until then QB's
   result is stated with "if a Ward-preserving extension exists".
7. Q3 wording in the store: entities that say "torsion-free (the curvature obeys the first Bianchi identity)" as
   one condition should be reworded: the identity is necessary, not sufficient (Omega = 0 counter-model).
   Recommendation: routine wording fix at the maintainer pass once Q3's result is accepted.
8. Graviton places (decision 2): the list is in the Q4 section. The dark-matter seeding rate
   (dark-matter.imported-massless-graviton-production-rate and its four users) depends on graviton exchange as a
   process, not as a count. Nothing was changed. Recommendation: Leon decides whether "the graviton does not
   exist" leaves a classical-field reading of that rate; I did not examine it.
