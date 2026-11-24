# Attack H-B: op.deposit-state-is-hadamard, adversarial and cross-subject side

Run 2026-11-24-three-routes. Attacker H-B (angle B). Model: Claude Fable 5.2. Status of this file: live, updated as work proceeds.
Labels used: proved / computed / argued / conjectured. Literature cited from memory is flagged "(from memory)".

## 0. Kill conditions, registered before any computation (24 November, before the first script was written)

Line 1, trace anomaly against the tame wall.
- HB1 (the premise of the line is wrong). Computed in the store's GTG form (field strength of (hb, Omega) on the
  spatially flat Robertson-Walker gauge field), the Euler density on the radiation field a = t^(1/2) is zero, or the
  anomalous trace vanishes for the stored content (the coefficients cancel). Then the line is dead and the anomaly is
  harmless for an algebraic reason.
- HB2 (the chain breaks). The time t* at which the anomalous term equals the radiation density, for the stored
  content, is not earlier than the earliest time the store's dating of the descent uses (equivalently the anomalous
  term is of order one or more on the collar the chain uses). Then the radiation-type hypothesis fails on the collar
  itself and the chain breaks at step (2) as stored.
- HB3 (harmless in the window). t* is earlier than every time in the store's window by a stated factor, so on the
  collar the anomaly is a correction of stated relative size; the outcome is then "the radiation-type hypothesis holds
  only later than t*", and the open question is only whether the wall at t = 0 is the limit of the corrected field.
- HB4 (the renormalisation freedom removes it). The local curvature terms that the imported stress tensor leaves
  free (the square-of-R term, whose trace is a multiple of box R) can be chosen so that the exact radiation power
  law, or a field asymptotic to it at the wall, solves the field equation with the anomalous source. Then the anomaly
  does not decide anything without a ruling on that coefficient.
Prediction written before computing: HB1 does not fire (the Euler density is -3/(2 t^4), the a-coefficient is a sum of
positive terms for ordinary fields; the Krein quartet has to be checked); t* is near the Planck time for content of
order a thousand weighted fields, so HB3 rather than HB2 unless the store dates the descent at the Planck time; HB4
does not fire for the exact power law because R = 0 there kills the box R term.

Line 2, necessity (lookup and argue; no computation). Kill condition HB5: the store nowhere requires finite
fluctuations of a Wick polynomial of the Dirac field beyond the two-point level (number, energy), or the
Fewster-Verch class does not contain Dirac fields on a Robertson-Walker collar. Then (HD) does not follow from a
requirement the store already makes and the item is recorded as a lead only.

Line 3, against the constructive route. Kill condition HB6 (for the sibling's route, tested by lookup): a stored
proved result is contradicted by a quasi-free Dirac state invariant under a conjugation across the wall. Candidates
to test: the cold-mirror result, the mirror's deposit law, obstruction (O1), the stored statement that Dirac fields
smooth across the wall in t vanish in the flat frame, the ruling of 7 November on the stored CPT conjugation.

## 1. Orientation (lookups done; nothing below repeats settled work)

Earlier findings: no earlier run's findings file names this problem; the only earlier mention of the trace anomaly is
one "next step" line of run 2026-11-18-navigate (the fermion channel's trace part of the gravitational rate), not this
question. The store has no entity on back-reaction at the descent (searched: back-reaction, trace anomaly, anomalous
trace, Starobinsky, sudden singularity). What the store does hold that the three lines use:
- synthesis.imported-heat-kernel-coefficients-and-background-field-gauge (i): the full coefficient a_4 with its
  curvature terms (5R^2 - 2Ric^2 + 2Riem^2 + 60RE + 180E^2 + 30 Omega^2)/360; (iii) the statistics weights. From these
  the anomaly coefficients of the three spins follow by arithmetic (section 2). What is NOT stored and is cited from
  memory: that the trace anomaly of a conformally covariant free field is its a_4 density (Christensen and Duff;
  Birrell and Davies ch. 6), and the Dirac value of Dappiaggi, Hack and Pinamonti, whose stored Fact says only that the
  anomaly "is computed explicitly there".
- synthesis.imported-sakharov-induced-gravity-coefficients (c): Boyle and Turok's cancellation of the Weyl anomaly
  (48 Weyl fields, 12 vectors, 36 dimension-zero scalars), stored only as a remark on the count 48 = 4 x 12; (d)
  Tichy and Flanagan: for massless fields the renormalised stress is fixed up to the two fourth-order tensors.
- The content: 12 vectors, 48 Weyl fields, two elementary doublets (8 real scalars), curvature coupling xi = 0 at tree
  level (synthesis.krein-quartet-...(iv); decision of 10 November).
- The store's dating: the descent "froze at the beginning" (standard-model.dating-descent, conjectured); the reheat
  temperature T_desc is bounded by the ceiling 6 x 10^14 GeV (dark-matter.ceiling-valued-inherited-success,
  synthesis.mirror-temperature-measures-deposit-under-r); stored tests use T_d <= 10^12 GeV and T_d >= 1 MeV.
- synthesis.radical-normal-...(iv): the radiation field is t g_{1,0}, R = 0, Ricci square (3/4) t^-4. With zero Weyl
  part the Euler density is -2 times that Ricci square: the number -3/(2 t^4) is already implied by the store.
- lib/gtg.py has euler_density, kretschmann, weyl_op, flrw_flat on exact jets, in the store's sign.

## 2. Line 3 first (written early for H-A): what a conjugation-invariant state runs into

All of this is lookup and short argument; labels as stated. H-A: items (a) and (b) are the ones that bear on your
steps 1 and 3.

(a) The stored conjugation is not a reflection across the wall and reverses energy (lookup).
dark-matter.premise-cpt-covariance v4 and synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation v5:
C = Ad(I_6) o kappa is -1 on the vectors of R^{2,4}, fixes every bivector (every conformal generator) and is
antilinear; maintainer note of 7 November: "it reverses the energy and is not that operator". Two consequences.
(a1) On points of spacetime C is the identity (X -> -X is the same projective point); what it does to the descended
field is hb -> -hb, that is a -> -a for the scale factor. So "the far side" on which a(tau) = tau/2 is negative is
the C-image of the near side as a gauge field (the vector part of C restricted to spacetime vectors is -1, which is
Ad(I_4), not a rotor of Cl(1,3): I_4 I_4~ = -1, clause (1) of the stored result). This is coherent with the route
(Boyle, Finn and Turok's a(-tau) = -a(tau), from memory), but the map tau -> -tau itself is not part of the stored
C; it has to be added as part of hypothesis (CW).
(a2) (argued; a three-line lemma, proof below.) A gauge-invariant quasi-free state of one Dirac field that is
invariant under an antilinear automorphism a(f) -> a(Cf) with C exchanging the positive- and negative-frequency
subspaces of the reference has, for every unit positive-frequency f, omega(particles in f) + omega(antiparticles in
Cf) = 1. Proof: with omega(a*(f)a(g)) = <g, Gamma f>, invariance under the antilinear automorphism reads
conj<g, C^-1 Gamma C f> = conj<g, Gamma f>, so Gamma commutes with C; the particle number in f is <f, Gamma f>
(f in P_+ K) and the antiparticle number in Cf is 1 - <Cf, Gamma Cf> = 1 - <f, Gamma f>. So the mean occupation
over each exchanged pair is one half, every moment M_k of the stored criterion is infinite, and the state is not
Hadamard. This is obstruction (O1) of the problem record made exact for a conjugation: an energy-reversing
conjugation cannot tell the vacuum from the filled sea and returns the tracial occupation. So the route needs a
conjugation that preserves the frequency split asymptotically (the field-theory CPT operator composed with the time
reflection), and that operator is NOT in the store: it is a new hypothesis, to be named as such in anything filed.
If H-A's invariant state comes out as the conformal vacuum for the massless field, the conjugation used was not the
stored C.

(b) The mirror (lookup, argued). The store's mirror is the co-present reversal tower, which gravitates here and now
(dark-matter.superselected-hence-dark-exactly-stable; the 5.364 ratio; pred.no-dark-radiation). Two readings of
"the mirror is the far side":
(b1) far side = the other sheet tau < 0 (before the wall). Then it is not co-present, carries no dark matter here,
and is not T14's mirror; the cold-mirror result and the deposit law xi^4 = (4/3) Y_B epsilon
(synthesis.mirror-temperature-measures-deposit-under-r) are untouched, and the word "mirror" should not be used.
(b2) far side = the co-present reversal tower. Then a quasi-free state invariant under the exchange has equal
occupation profiles in the two towers, so xi = 1 and Delta N_eff = 7.45
(synthesis.cold-mirror-needs-non-equilibrium-descent (i)), against the cap xi < 0.448
(dark-matter.open-channels-their-costs). Clause (iii) of the cold-mirror result is the exact statement: an
exchange-invariant state with xi != 1 in its components exists but is a mixture and is not quasi-free, while (HD)'s
deposit is quasi-free. So in reading (b2) kill condition H3 fires.

(c) The vacuum is cold, the deposit is hot (argued; see also section 3, clause C0). If the invariant state of the
massless field is the conformal vacuum (H4 not firing), it has no quanta. But the route's field a = tau/2 is the
radiation field, whose source is the density C/a^4 of a hot state of the same content. With the conformal vacuum as
the state the density is the anomalous one alone (6 alpha H^4, section 3), and the only solutions of the field
equation are the flat field and the de Sitter field with H^2 = Mbar^2/(2 alpha). So the invariant vacuum is not a
state whose own stress sources the field on which it was selected. This is (O5) again (the Hadamard invariant states
are the vacuum alone, so a hot deposit is never invariant), now for the wall conjugation instead of the conformal
group. In Boyle, Finn and Turok the radiation is a separate classical fluid; in the series the deposit has to be it.

(d) The stored statement that Dirac fields smooth across the wall in t vanish in the flat frame
(synthesis.radical-normal-...(ii)) is not contradicted: an invariant state is a symmetry condition on the double
cover t = tau^2/4 (both signs of tau), not smoothness in t. No conflict found; but note that the reflection
tau -> -tau is the deck map of the double cover and is trivial in the wall's own coordinate t.

(e) The anomaly (section 3): the route needs M = m a exactly odd and analytic in tau through the wall. That is the
exact radiation law at the wall, which a Hadamard state of content with nonzero a-coefficient does not allow
(section 3). Boyle and Turok cancel both anomaly coefficients with 36 dimension-zero scalars for this reason (stored
Fact (c); their motivation is from memory); the stored content has no such scalars and its coefficient is 1008 (1016
with the eight doublet components) in units of one real scalar. So (CW) needs either that content, or the wall
treated as kinematic with no field equation imposed between it and the collar.

## 3. Line 1, the trace anomaly against the tame wall (done; filed)

Routes considered. (1) The problem's own: test the chain's second step, the radiation-type descent, against the
state it is meant to carry. (2) From another subject (the Einstein and induced-gravity results): the stored
heat-kernel coefficient a_4 and content counts give the anomaly weights with no new import of numbers; the stored
Tichy-Flanagan Fact names the one free coefficient. (3) Own: solve the corrected Friedmann equation exactly rather
than estimate when the anomalous term matters. Chosen: all three in one result, because (2) supplies the number that
(1) needs and (3) turns "when does it matter" into a bound. Kill conditions HB1 to HB4 of section 0.

Proposal filed: synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall
(proposals/..., check4 exit 0 with no findings, validate_draft ok apart from the environmental ORCID warning E610;
five check functions, all exact). Named hypotheses, neither a stored premise: (A) the anomalous trace
alpha E + b box R of a Hadamard state of free conformal content on Weyl-flat fields (standard, cited from memory,
NOT imported); (E) the expected stress, whole, is the source of the field equation.

Established, with labels:
- proved (exact, GTG form): on the Robertson-Walker gauge field R(g0 ^ gi) = (addot/a) g0 gi, R(gi ^ gj) = H^2 gi gj
  (store sign); Euler density 24 H^2 addot/a; on every field the Euler density is -4 Tr((I_4 R)^2), the trace over
  bivectors of the dual of the field strength squared (proof by the three-part split; checked on Weyl-flat and
  Weyl-curved fields). On the radiation field: scalar 0, Euler density -3/(2 t^4) = -2 x the stored Ricci square.
- computed (from the stored a_4 and statistics weights; the operators and the identification with the anomaly are
  from memory): weights (Weyl square, Euler) = (3, 1), (9, 11/2), (36, 62) per real scalar, Weyl field, gauge vector;
  all Euler weights positive. Stored content: 1008 = 28 x 36 (48 Weyl + 12 vectors), 1016 with the eight doublet
  components; alpha = 127/(720 pi^2). The stored Boyle-Turok Fact (c) is reproduced by these weights (dimension-zero
  scalar: -28, -8).
- proved given (A): the stress is rho = C/a^4 + 6 alpha H^4 + b(H R' - R^2/12 + H^2 R); the alpha term is the map
  T_A(a) = 2 alpha [Ric(Ric(a)) - (2/3) R Ric(a) - (1/2) Ric^2 a + (1/4) R^2 a]; on the radiation field
  rho_A = 3 alpha/(8 t^4), P_A = 5 alpha/(8 t^4) (so "w" of the anomalous part is 5/3, not 1/3) and the b term is
  identically zero.
- proved given (A), (E): the exact radiation field solves the field equation for no state and no b unless alpha = 0
  (trace: 0 against -12 pi G alpha t^-4). For power laws t^p the order t^-4 cancels exactly when
  2 alpha p^2 = 3 b (2p - 1): p = 1/2 only at alpha = 0. So no power-law origin has a tame bracket in cosmic time.
- proved given (A), (E), b = 0: 3 Mbar^2 H^2 (1 - x) = C/a^4, x = 2 alpha H^2/Mbar^2. The branch joined to late
  radiation has H^2 < Mbar^2/(4 alpha), C/a^4 <= 3 Mbar^4/(8 alpha), a^4 >= 8 alpha C/(3 Mbar^4): it ends at a
  positive scale factor with H finite and the scalar unbounded, before any wall. With C = 0: flat or de Sitter with
  H^2 = Mbar^2/(2 alpha).
- computed (stored content, g = 116): T_max^4 = (2025/3683) Mbar^4, T_max = 0.861 Mbar_P, about 2.1 x 10^18 GeV;
  the anomalous trace equals the density on the radiation field at t_eq = sqrt(2 alpha)/Mbar, 0.94 to 0.95 Planck
  times (the anomalous density equals it at half that time); at the stored ceiling 6 x 10^14 GeV, C/a^4 is
  6.7 x 10^-15 of its largest value and the anomalous share of the density is below 1.7 x 10^-15, so t_ceiling is
  about 1.2 x 10^7 t_eq.
- argued: on the collar the deposit results use only a smooth scale factor and Weyl-flatness, which stand; what is
  lost is the extrapolation to the wall (M = m a linear in conformal time through it; any continuation across it).
- argued, from memory: interactions give the real plasma a state-dependent trace of relative size far above
  10^-15 at these temperatures (order g^4); the store already notes in one remark that "a real bath is not exactly
  trace-free" (clause (vii) of the stored pair-production result). Not treated.
Ledger: transport-absent.

Outcome of line 1, in the three forms the task allowed: "the radiation-type hypothesis holds only later than a
stated time". Precisely: under (A) and (E) it never holds exactly; on the window the store uses (T <= 6 x 10^14 GeV)
it holds to better than 2 parts in 10^15; it fails at order one at about one Planck time (T about 0.86 Mbar_P), and
the wall at t = 0 is not the past boundary of the corrected field. The chain of the problem does not break on the
collar. It does break as an extrapolation to the wall at step (2), in the sentence "for the conformally covariant
fields the radiation origin is the initial slice of half of Minkowski space": true for the matter's field equations
on a prescribed radiation field, not for the field its own stress sources. The third form ("harmless because the
wall is approached where no stress is defined") is available only as a ruling: see Decisions.

What the store already said about back-reaction at the descent: nothing (section 1). Nothing here contradicts a
stored result; it qualifies a stated hypothesis.

## 4. Line 2, necessity (lookup and argue; no proposal)

The paper (from memory, not looked up): C. J. Fewster and R. Verch, Class. Quantum Grav. 30 (2013) 235027. As I
recall its statement: for the Klein-Gordon field on ultrastatic slabs with compact Cauchy surfaces, the Wick squares
of all time derivatives of the field, normal ordered with respect to a quasi-free state, have finite fluctuations
only if that state is Hadamard (a converse to Brunetti and Fredenhagen). Hypotheses: real scalar field; ultrastatic
slab; compact sections; a quasi-free reference; ALL time-derivative orders. It does not treat the Dirac field (as far
as I recall; the stored Fewster-Lang Fact is about spin-product states on the same slabs, not about necessity).

The implication, stated precisely for the store's class.
- argued (one line from the stored moment criterion): for a homogeneous diagonal deposit of the massless Dirac field
  over the conformal vacuum, the odd moment M_{2m+1} is, up to a constant, the expectation value of the local
  bilinear with 2m + 1 time derivatives (m = 0: the energy density), and since occupations lie in [0, 1],
  M_{2m} <= const + M_{2m+1}. With clause (ii) of the stored criterion: the deposit is Hadamard exactly when every
  such bilinear has a finite expectation value. So in the stored class the necessity statement holds in a stronger
  form than Fewster and Verch's (expectation values suffice, no fluctuations needed) and needs no import.
- lookup: what the store requires to be finite is, in each case, finitely many moments. The renormalised stress
  uses M_1; the shot-noise bound and the white energy noise use number and energy spread (M_0, M_1 and a second
  energy moment); the (OS) rate uses stress two-point functions (one derivative per leg); (HS) and the scaling limit
  use M_0. Obstruction (O3) of the problem record already says this, and the stored profile (1 + p/T)^-6 passes every
  one of these while failing (HD).
- conclusion: kill condition HB5 fires in both halves. The store makes no requirement from which (HD) follows; and
  the Fewster-Verch class does not reach Dirac fields on a Robertson-Walker collar (two gaps: spin; and for massive
  fields M = m a makes the conformal frame non-ultrastatic; for massless fields conformal covariance and periodic
  sections would bridge the second gap).
- what would have to be adopted to make (HD) a consequence: one requirement, (W-infinity), "every local bilinear of
  the free fields on the collar, with any number of derivatives, has a finite expectation value in the deposit"
  (the deposit is a state on the extended algebra of the stored stress-tensor Fact). In the stored diagonal class it
  is equivalent to (HD), so it is a restatement in terms of observables, not a derivation; for deposits with pair
  coherence or inhomogeneity the implication (W-infinity with finite fluctuations) => Hadamard would need an import
  that I can vouch for only for the scalar field. Label: argued. Not filed: it adds one sentence to a stored theorem.

## 5. Line 3, read against H-A's filed proposal (midway check done)

H-A filed synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none.
Its clause (i)(c) is my item (a2) of section 2 (energy-reversing conjugation gives the tracial state), so I file
nothing on it. Its outcome (a disk of invariant states per mode; no selection; massless: every stationary deposit
invariant) agrees with (c) of section 2: the conjugation cannot supply the temperature. What my side adds to it:
its hypotheses (RD) and (DF) (a = a' eta exactly through the wall, M odd) are incompatible with (A) and (E) for the
stored content by the filed result here; its Gaussian floor exp(-pi k^2/(m a')) for the massive field uses M linear
through the wall, exactly the extrapolation the anomaly removes. This is not an error in H-A's result (its
hypotheses are named); it is a cost to record on it. Reading (b2) of the mirror (section 2) stands as a kill of the
"mirror" wording if the far side is meant to be the co-present reversal tower. (Fix round, bridge entry B6:
that tension is with (CW) in reading (b2) alone; P2 is scoped to labels, not states, and no stored premise asks the
state to be exchange-invariant, so no stored premise is touched.)

## 6. Outcome of the kill conditions

- HB1 (Euler density or weight vanishes): did not fire. Euler density -3/(2 t^4) in GTG form; weight 1016 (1008).
- HB2 (chain breaks on the collar): did not fire. At the ceiling the anomalous share is below 1.7 x 10^-15.
- HB3 (harmless in the window by a stated factor): fired, as predicted before computing. Factor above 5 x 10^14.
- HB4 (the free coefficient restores the tame radiation origin): did not fire. No b gives p = 1/2; b != 0 gives
  power-law origins with p != 1/2 (argued beyond power laws: not treated).
- HB5 (necessity gives nothing the store already requires): fired. Recorded as a lead, not a result.
- HB6 / run condition H3 (a stored result contradicted by a conjugation-invariant state): fires only in reading (b2)
  (far side = co-present mirror tower, quasi-free invariant state => xi = 1 against the cap); does not fire in
  reading (b1). The energy-reversing stored conjugation gives the tracial state ((O1) made exact; filed by H-A).

## Unexpected links

1. The number 1008 = 28 x 36. The Euler weight of the series' fermions and vectors is exactly the amount Boyle and
   Turok cancel with 36 dimension-zero scalars, and the stored Fact (c) records their count only as a coincidence
   with 48 = 4 x 12. Their reason for cancelling it (from memory) is the one found here: a radiation-type origin that
   is analytic through the wall needs the anomaly to vanish. So the constructive route of this target and the stored
   Fact (c) are the same question from two sides.
2. The stored Ricci square (3/4) t^-4 of the tame-wall result is, up to the factor -2, the Euler density: the
   quantity that makes the radiation wall a curvature singularity "invisible to conformal fields" is the one that
   their anomaly sees.
3. The free coefficient b of the stored Tichy-Flanagan Fact (d) is the coefficient of the square-of-R term, that is
   of Starobinsky's model (from memory), and the solution C = 0 of clause (v) is its de Sitter solution with
   H^2 = Mbar^2/(2 alpha) (about (5.3 Mbar_P)^2 for the stored content). The store's position on the primordial
   spectrum is "no mechanism"; the store therefore already imports, as a renormalisation freedom, the one number of
   the best-known one-parameter mechanism. Conjectured lead only: nothing was computed, the amplitude would be a fit
   of b, and the store's hypothesis (D) (no inflation after the descent) and its dating would have to change.
4. Weyl-flat variations carry only the stress trace, and classically massless matter has none (the stored
   whole-stress result). The anomaly is the one trace massless content does have, so in the Weyl-flat class the
   field of massless content is sourced by C/a^4 through the trace-free channel and by the anomaly through the trace.
5. A ceiling for free: under (A), (E), b = 0 the radiation temperature is bounded by 0.86 Mbar_P for the stored
   content, which is the hypothesis (QP) ("deposit quanta below the Planck mass") of the sparse-deposit result in
   order of magnitude, here derived rather than assumed.
6. The necessity line gives (HD) an observable-side reading in the stored class: Hadamard exactly when every
   derivative bilinear has a finite expectation. No stored result needs more than three moments.

## Decisions for Leon

1. Accept or not the filed result, and how to hold its hypothesis (A): import as Facts the anomaly identification
   (Christensen and Duff; Birrell and Davies ch. 6; Dappiaggi, Hack and Pinamonti's explicit Dirac value) and the
   gravitational vector operator, or leave (A) a named hypothesis. Recommendation: import; they are textbook and the
   numbers are reproduced from the already stored a_4. Until checked against the sources the citations are from
   memory.
2. The scope of the radiation-type hypothesis. Three options: (a) restate it as a statement about the collar only
   ("Robertson-Walker with smooth scale factor, radiation-type up to the anomalous correction; nothing is asserted
   between the wall and the collar"), with a note on (HD), on clause (iv) of the tame-wall result and on the problem
   record; (b) keep the wall and add content that cancels the Euler weight (36 dimension-zero scalars, a new content
   premise); (c) rule that the field equation with the expected stress as source is not imposed at the wall (the
   descent as a division event outside the metric sector). Recommendation: (a), and record (c) as the reading under
   which wall-based routes (attack item 5, the wall conjugation) are stated. Not (b).
3. (Reworded in the fix round, after the bridge pass.) Whether the WHOLE expected stress, its state-independent
   anomalous part T_A included, is the source near the descent. (E) says nothing on mean field against operator
   source: it is compatible with (OS), whose expectation it is at first order. Its content relative to the store is
   the word "whole": the stored Clausius theorem takes T as given ((H3): classical or a renormalised expectation
   value) and the stored inverse-problem result fixes the heat tensor only up to a matter-independent term, which
   T_A is. With the state-dependent part alone as source the exact radiation field is a solution. So this is one
   yes/no ruling: is T_A part of the source. Tied to op.einstein-from-the-field-theory. (My earlier wording, "the
   mean-field source that the stored (OS) discussion sets against the operator source", conflated two readings and
   is withdrawn.)
4. The free coefficient b: leave free (present position, Fact (d)), or set to zero by a ruling. With b = 0 clause (v)
   applies and there is no origin at all; with b != 0 there are power-law origins with p != 1/2. Recommendation:
   leave free and say so on the problem record.
5. The word "mirror" in this target's route: if the far side of the wall is the other sign of conformal time it is
   not T14's mirror (which is co-present and gravitates here). Recommendation: do not use "mirror" for it.
6. (HD) restated or annotated with its observable form (section 4): add a note on (HD) that in the diagonal class it
   is equivalent to finiteness of every derivative bilinear, and that no stored requirement uses more than finitely
   many moments. Recommendation: note only; do not import Fewster and Verch (it does not reach the Dirac field).
7. Attack items to add to op.deposit-state-is-hadamard: (i) the wall is outside the reach of (A) + (E): any wall-based
   selection must say which of options (a) to (c) it assumes; (ii) the corrected field with b != 0 beyond power laws;
   (iii) the Starobinsky lead of link 3, on op.descent-state-and-spectrum, as a lead only.

## Not done, and why

- The solutions with b != 0 beyond their power-law origins (a third-order equation for H): outside the budget; the
  proposal claims only the power-law statement.
- Massive fields and interacting content (state-dependent trace): not treated; the proposal says so.
- The Weyl-curved (Kasner) branch: the anomaly there has the Weyl-square term (weights 3, 9, 36 are computed in the
  check but not used); not pursued.
- Fewster and Verch, Boyle and Turok, Starobinsky and the Brown-Cassidy form were not looked up; every statement of
  them here is from memory and flagged.
- The conservation of the map T_A on Weyl-flat fields that are not Robertson-Walker is not proved (not claimed).
