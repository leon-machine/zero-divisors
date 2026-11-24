# Attack H-A (angle A, constructive): op.deposit-state-is-hadamard, route "CPT-symmetric wall"

Run 2026-11-24-three-routes. Model: Claude Fable 5.2. Status: attack round complete, one proposal filed.
Labels: proved / computed / argued / conjectured. Literature from memory is flagged; one source was read in part.

## Routes considered
1. (Named, executed.) The mirror as the far side of the radical-normal wall (both signs of conformal time), the state
   invariant under a conjugation across the wall, hypothesis (CW). Delivers a selection if the invariant state is
   unique. Needs a conjugation that is a symmetry of the doubled field's Dirac equation, so M = m a odd in conformal
   time (radiation-type descent). Fails if there is no invariant state or a continuum (H1), or a power-law tail (H2).
2. (Alternative, not executed.) The Riemannian far side of attack item 5 for the Dirac field (weight t^-3/4): a
   selection by boundedness, of ground-state type, which can tell the vacuum from the filled sea where a symmetry
   cannot (see "Unexpected links" 3).
3. (Alternative, not executed.) Least occupation over the late-time adiabatic vacuum with no symmetry: selects the
   late-time vacuum itself (occupation zero), a Hadamard state; it needs a premise naming that vacuum and the
   orientation.

## Kill conditions (pre-registered in RUN.md before computing) and their outcome
- H1 (no invariant quasi-free state, or a continuum): FIRED, in the second form. For the conjugation the route needs,
  the invariant states are a disk of Bloch vectors per momentum-helicity sector (a circle of Fock states). (CW)
  selects no state. Proved.
- H2 (power-law tail): NOT FIRED for the invariant state of least occupation (tail (1/4) exp(-pi k^2/(m a')));
  FIRED for another invariant state, the instantaneous vacuum at the wall (stored tail mu^2/(16 k^4)). So (CW) does
  not imply (HD). Proved (the exact exponent: classical special functions, from memory, numerically confirmed).
- H3 (contradiction with a stored result): no stored theorem is contradicted. A tension with the series' cold
  mirror is real and is argued: a (CW)-invariant quasi-free state reads the same occupations on the two sides
  (temperature ratio 1), against the cap 0.448. With the energy-reversing conjugation the invariant pure states
  have occupation one half, which is (O1). Argued for the mirror; proved for the one half.
- H4 (massless invariant state is not the conformal vacuum): FIRED for (CW) alone: every stationary
  charge-symmetric deposit is invariant, thermal at any temperature included, and so are the filled sea and the
  tracial state. NOT FIRED once purity, the orientation and least occupation are added (then it is the conformal
  vacuum). Proved.
Own sharpening, written before computing: H1 is tested on the stored two-level form (I u' = H u, H = M sigma_3 +
k sigma_1, Bloch form s' = -2I(h ^ s)); "continuum" means the invariant Bloch vectors at the wall form a set of
positive dimension for each k.

## What was established (proposal: synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none)
check4 exit 0 (0 errors, 0 other findings), validate_draft ok (E610 ORCID warning only, as on every AI entry),
runcheck 6/6. Conditional on three named hypotheses, none a store premise: (RD) radiation-type descent, (DF) the
far side is the other sign of conformal time with a odd, (CW) invariance under the conjugation across the wall.

1. Which conjugation (proved, GA, exact check in Cl(1,3) and Cl(3,0)). The reflection in the wall acts on the
   even-multivector field as W chi(eta, x) = g0 chi(-eta, x) g0 (the reflection's outermorphism). It is a symmetry
   of the Hestenes-form equation exactly when M is odd; it commutes with the mass part of the mode generator and
   the right unit I sigma_3, anticommutes with the momentum part. On Bloch vectors exactly two reflections
   s(eta) -> O s(-eta) exist for mu > 0: O_A (reflection along sigma_3) and O_B (half turn about sigma_3).
   W as an automorphism gives O_B and reverses the energy (vacuum to filled sea). W with charge conjugation
   (chi -> chi sigma_1, antilinear), or W with the particle-hole exchange, gives O_A, which keeps the energy sign:
   this is the one the route needs. The stored conjugation's type (point-fixing, energy-reversing) acts as s -> -s,
   exchanges no sides, and fixes only the tracial state. So the stored conjugation cannot serve; the route's
   conjugation is a new object (the wall reflection with charge conjugation), part of (CW).
2. Existence and uniqueness (proved). O_A-invariant states: v(0).sigma_3 = 0, a disk per sector. O_B-invariant:
   v(0) along sigma_3; its two Fock states have occupation exactly 1/2 over the wall-instant vacuum and
   (1 -+ exp(-pi k^2/(2 m a')))/2 over the late-time vacuum: a tracial tail, never Hadamard.
3. Massless (proved). Every stationary charge-symmetric deposit t(k) sigma_1 is O_A-invariant. (CW) adds nothing to
   stationarity. Invariant + stationary + pure = conformal vacuum or filled sea.
4. Massive, the profile (proved, with the exponent classical). q = occupation of the early-time vacuum over the
   late-time vacuum = (s_out(0).sigma_3)^2 = exp(-pi k^2/(m a')). Invariant Fock states: occupation
   (1 - sqrt(1-q) cos chi)/2 over the late-time vacuum, chi a free angle per k. Every invariant state has
   n0 <= n <= 1 - n0, n0 = (1 - sqrt(1 - exp(-pi k^2/(m a'))))/2, 4 n0 (1 - n0) = q, and every profile in that band
   is realised. So the single consequence of (CW) for a massive field is a floor. The floor is attained by one
   Fock state (the midpoint of the early-time and late-time vacua), with no free number and a Gaussian tail.
   Elementary part, no special functions (proved, exact check to order 6): the late-time vacuum agrees with the
   adiabatic series to every order, |s_out - S_N| <= C_N (mu/k^2)^N for all eta, so q falls faster than every power.
   Numerical confirmation in scratch (computed, floats, not in the check): q = exp(-pi nu) and n0 to nine digits at
   five (k, mu); number density integral 0.012760 (mu/pi)^(3/2) per sector, the value in Boyle, Finn and Turok.
5. Hadamard (proved lemma; conclusion given the imported Fact). New lemma, the sufficiency half of a massive
   analogue of the stored moment criterion: two homogeneous states of the class whose sector vectors differ by an
   amount with all moments finite differ by a smooth kernel on every collar eta > eps (for Fock states: all moments
   of the occupation finite). With Fact (c) of synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-
   states-are-hadamard for the late-time vacuum: the floor state is Hadamard; so is every invariant state with
   1 - t(k) and 1 - cos chi(k) rapidly decreasing; the wall-instant vacuum and the tracial state are invariant and
   not Hadamard. The identification "agrees with the adiabatic series to every order = adiabatic of infinite order
   in the Fact's sense" is the stored massive result's own and is argued, not proved. The necessity half of a
   massive moment criterion is not proved here.
6. What selects (proved). Among invariant states, least occupation over the late-time vacuum selects the floor
   state; this uses the orientation datum (the invariant set is symmetric under v -> -v).

## Deliverable 3: confrontation (argued unless marked)
- (O1): confirmed in this setting, proved: the only state fixed by all the conjugations is the tracial one; the
  energy-reversing ones give one half; the invariant set of O_A is symmetric under v -> -v, so (CW) does not supply
  the orientation datum.
- (O5): does not transfer. Unlike the conformal group, the wall conjugation leaves every thermal deposit invariant
  (massless). So (CW) neither selects nor excludes a hot deposit. (Sibling H-B's note (c) assumed the invariant
  massless state is the conformal vacuum; that is one invariant state among all the stationary ones.)
- Cold mirror: if the mirror is the far side, it is not a second algebra (the fields at -eta are the Cauchy
  evolution of those at eta), hypothesis (B) of the cold-mirror theorem fails, and every invariant state reads
  equal occupations on the two sides: ratio 1. If the mirror is a co-present species exchanged by the conjugation,
  invariance gives conjugate marginals, again ratio 1 for stationary massless states, and restricts neither
  marginal. A cold mirror in a quasi-free state is not (CW)-invariant; the invariant state with unequal
  temperatures is the stored non-quasi-free mixture (clause (iii) of the cold-mirror theorem).
- The mirror's deposit law (xi^4 = (4/3) Y_B epsilon): untouched if the far side is not the mirror; in conflict
  with (CW) on the thermal part if it is (xi = 1 forced).
- What the route selects: with purity, orientation and least occupation added, a vacuum part with no free number
  (conformal vacuum for massless fields; occupations n0(k^2/(m a')) for massive ones). What it does not: a
  temperature, the thermal bath, the spectrum.

## Ledger
Transport-absent. Standard quantum field theory of a Dirac field with mass linear in conformal time, in the store's
GA form. Prior art: Boyle, Finn and Turok, PRL 121 (2018) 251301 and the longer arXiv:1803.08930, which I read in
part through a summarising fetch: they state that CPT leaves a free function eta(p) for spinors, with occupation
(1 - cos 2eta cos lambda)/2, and fix it by least particle number and energy. So the non-selection by CPT alone and
the profile are theirs. New in the store's terms: the classification against the stored conjugation, mixed states
and the floor, the elementary all-orders bound, the Hadamard statements, the wall-instant vacuum as an invariant
non-Hadamard state.

## Next steps (not done)
- Necessity half of a massive moment criterion (smooth difference implies finite moments), by the stored moment
  lemma; would make clause (v) an equivalence.
- The scalar field under (CW) (Boyle, Finn and Turok treat it; the stored bounded-band result is the reference).
- The Riemannian far side for the massive Dirac field (attack item 5 of the problem), a different selector.
- A reading of the prior-art papers in full by Leon (the fetch covered the first 100000 characters of the long one).

## Unexpected links
1. The stored result that the instantaneous vacuum is not Hadamard where m a' != 0
   (synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard (ii)) supplies, with no new
   work, a (CW)-invariant state that is not Hadamard: the instantaneous vacuum at the wall is exactly conjugation
   invariant, and m a' != 0 at a radiation origin. The most natural "state defined at the wall" is the bad one.
2. The stored adiabatic series is invariant under the conjugation to every order: at the wall it has no sigma_3
   part. The early-time and late-time vacua differ only beyond all orders (exp(-pi k^2/(2 m a')) in the Bloch
   vector). So adiabatic regularity (HD) and the conjugation are compatible but independent conditions.
3. Attack item 5 (Riemannian far side) and this route differ in kind: boundedness on the Euclidean side picks the
   vacuum for one branch of sqrt(t) and the filled sea for the other, that is, it supplies the orientation datum
   up to the branch; the real reflection tau -> -tau is the deck map of the same double cover and cannot. The two
   could be combined: the deck map plus the choice of branch.
4. Sibling H-B (a1): the stored conjugation's vector part -1 sends hb to -hb, that is a to -a at the same point; the
   doubled field with a odd is therefore symmetric under the wall reflection composed with the stored conjugation's
   vector part. This is coherent with the route but does not change the count above.
5. (O5) versus (CW): the conformal group excludes hot deposits among invariant states; the wall conjugation does
   not exclude any stationary deposit.

## Decisions for Leon
1. Whether to adopt (CW) at all. Recommendation: no, not as a premise. It does not derive (HD) and selects no
   state; for massless fields it is empty beyond stationarity; and with the mirror read as the far side or as the
   exchanged species it forces a temperature ratio 1 for quasi-free states, against the cold mirror.
2. If a vacuum part for massive fields is wanted with no free number, the hypothesis that does the work is not (CW)
   alone but (CW) + purity + least occupation over the late-time vacuum + the orientation datum. Whether to record
   that bundle as a named hypothesis (it gives n0 and a Hadamard state) is a separate decision; it would be a
   postulate, maintainer-only.
3. The doubling (DF): whether the far side of the radical-normal wall, as the other sign of conformal time, is a
   reading the series wants beside the Riemannian continuation in t. The filed result treats it as a hypothesis.
4. Imports the filed result would cite as Facts if accepted (now cited from memory in the proof and note):
   Zener 1932 (transition probability) or Whittaker and Watson sections 16.5 to 16.52 (Weber functions); Boyle,
   Finn and Turok 2018 as prior art. Status of clause (iv)(c): proved given those classical facts; if that is not
   acceptable for a proved entity, the clause can be relabelled as resting on an imported Fact.
5. The attack item to file on the problem from this route (maintainer pass): "CPT-symmetric wall: decided for the
   Dirac field on a radiation-type descent. Invariance across the wall leaves a disk of states per mode; its one
   consequence is the floor n0 for massive fields; the floor state is Hadamard and needs least occupation and the
   orientation; the energy-reversing conjugation gives one half."
6. Obstruction (O5) on the problem record could carry a sentence that it is specific to the conformal group and does
   not extend to the wall conjugation.

## Correction after review (fix round)
The number density 0.012760 (m a'/pi)^(3/2) quoted above as "per sector" is the density summed over the two
helicities; per sector it is 0.006380 (m a'/pi)^(3/2). The per-sector floor holds for isotropic states (or for the
sector-wise conjugation); without isotropy only the pair bound n_k + n_{-k} >= 2 n0 holds. See fixes-H-A.md.
