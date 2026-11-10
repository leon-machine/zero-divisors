# attack-BB (cluster B, angle B adversarial), run 2026-11-10-phase2

Status: pre-registration written before any computation. Sibling BA files the base statement B1 (Born weights from
(P) and sharpness); I do not file it and name it as intended citation.

## Orientation (direct lookups)
Read: op.positivity-of-values in full; synthesis.premise-positivity-of-values; the CHSH base (clauses iii to viii);
the counter-model; the four measurement premises; one-relation.measure-indifference-borns-rule-located;
one-relation.imported-envariance-born-rule; synthesis.indifference-is-curie-plus-single-valuedness;
singularity.descent-parity-average; singularity.p-univalence; singularity.imported-univalence-superselection-rule;
dark-matter.premise-flag-as-datum. The store has no entity mentioning Gleason, Kochen-Specker or contextuality.

## Routes considered
B1: (r1) the problem's own: C-S plus PAP = kP; (r2) from another subject: the classification of the algebras over Q
(D in {Q, Q(I), H}) to find a primitive idempotent with PAP larger than kP and a second sharp state; (r3) my own:
Gleason/Kochen-Specker in the stored algebras, to say what linearity in (P) imports. Chosen: r2 as the attack on
uniqueness, r3 as the statement of what is relocated.
B2: (r1) positivity of the conditional expectation E; (r2) the phase 1 box functional pushed through E and through a
record map; (r3) a parity-even box functional on two modes per party. Chosen r2 + r3: counter-models.
B3: finite formal models (algebra, record projectors, record map, weights) separating each premise.
B4: (r1) flag datum J against the split; (r2) univalence closed under the record map; chosen r2 first.

## Kill conditions (registered before computing)
- K-B1a (non-uniqueness attack). If exact linear algebra finds, in any of Cl_Q(1,1), Cl_Q(2,0), Cl_Q(0,2), Cl_Q(3,0),
  Cl_Q(2,2), a state satisfying all three clauses of (P), sharp on a self-adjoint primitive idempotent P (for the
  stored split), and different from <Px>_0/<P>_0, then B1 is REFUTED there. If none is found and the argument
  sym(PAP) = kP holds, my attack on uniqueness is dead and I say so. Separately registered sub-claims that must be
  exhibited exactly or dropped: (i) without the reality clause uniqueness fails; (ii) for an idempotent that is
  primitive but not self-adjoint for the split (a boosted frame) there are several sharp (P)-states, none of trace form.
- K-B1b (Gleason type). Claim: in matrix size 2 (one mode) a non-negative weight on self-adjoint idempotents, additive
  on orthogonal pairs, need not be linear. Dead if additivity inside contexts forces linearity there. Claim: in
  Cl_Q(2,2) no weight with values in {0,1} exists on rational primitive self-adjoint idempotents (18 idempotents, 9
  contexts). Dead if the exhaustive search over 2^18 assignments finds one, or the 18 are not in the algebra over Q.
  Exploratory, no claim registered: a non-linear non-negative frame function on rational rays in size 4.
- K-B2. Independence model: an even functional (omega o alpha = omega), linear, normalised, real, with non-negative
  no-signalling tables in every context of two parties, CHSH value 4. Dead if the functional turns out non-negative
  on every x x-dagger, or fails evenness or a table. Claim: the parity average of the phase 1 functional is still not
  positive: dead if lambda o E is positive. Claim: after the record map of a measured context the functional is
  positive; after a coarse record (of K) it is not. Dead if either sign comes out the other way.
- K-B3. For each of the four premises, under an explicit formalisation, a finite model where it fails and the other
  three hold. Dead for a premise if every model of the other three satisfies it (then it is derivable: report that).
- K-B4. Claim: for an observable a (a-dagger = a, a^2 = 1), the record map E_a(x) = (x + a x a)/2 sends every even
  state to an even state iff alpha(a) = +a or -a. Dead if a mixed-parity observable preserves evenness of all even
  states, or a homogeneous one does not. Consequence claimed: in the one-mode Klein-twisted realisation every even
  (P)-state gives at most 2 at parity-homogeneous settings. Dead if an even state exceeds 2 there. Flag: claim that
  the datum J does not fix the split; dead if all J-compatible splits coincide.

## Results (final)
Scratch: work/BB/b1.py (corners, reality, boosted idempotent, size 2), ks.py (18 atoms, square of nine blades),
gl.py (congruence frame functions), b2.py (box functionals, records, parity), b4.py (local values, record maps).
Gate for all three proposals: check4 exit 0 with no findings; validate_one ok with no warnings; registered with
propose_claim (coverage.yaml copied back). Originals kept in work/BB/aside/.

### B1 (base statement is BA's: synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional,
the intended citation; not re-proved, not filed by me)
- K-B1a FIRED AGAINST MY ATTACK. COMPUTED (exact, 9 algebras incl. the quaternionic Cl(0,2), Cl(4,0), Cl(1,3) and
  the complex Cl(3,0)): the corner PAP has dimension 1, 2 or 4 and its self-adjoint part always dimension 1. ARGUED
  (classification over Q is the real one; a positive involution on Q(I) or on the rational quaternions has only
  scalars symmetric): no second sharp state exists in any Cl_Q(p,q). B1 is not refuted; the rational field does not
  break uniqueness.
- Circularity verdict (ARGUED): B1 does not assume the trace form (the form comes out of PxP = c(x)P and cyclicity);
  it is not circular. It RELOCATES: everything is carried by linearity across non-commuting elements plus
  positivity, i.e. by (P). The envariance argument's residual postulate ("weights exist and add") is not reduced.
- COMPUTED: without reality, omega = 2<Px>_0 + 3<fx>_0 on Cl(1,1) is normalised, has the Born quadratic form,
  is sharp on P = (1+e)/2 and differs from the Born functional on f (BA has the same point).
- COMPUTED (signature dependence; not in BA's B1): for the boosted idempotent Pb = (1 + (5/4)e + (3/4)f)/2 of
  Cl_Q(1,1), primitive and not self-adjoint for the stored split, the (P)-states sharp on it form a segment
  (x = 4/5, |z| <= 3/5), none of trace form; the state <(1+e)x>_0 gives Pb the "weight" 9/8 and 1 - Pb the weight
  -1/8. So "sharp on a primitive idempotent" must mean self-adjoint for the split, and the Born weights of a
  boosted observer's outcomes are not probabilities. Not filed (BA's split proposal is the home for it).
- Gleason / Kochen-Specker. FILED 3: synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them.
  PROVED (complete search): 18 rational atoms of Cl_Q(2,2) in 9 contexts admit no 0/1 weight; nine blades in a
  square admit no multiplicative signs. PROVED: the even subalgebra of two modes admits a 0/1 additive weight
  (two corners of size 2), so for parity-even elements a statement of this type needs three modes.
  Size 2 (one mode): Gleason fails (COMPUTED here, filed by BA inside its results).
  Size 4 over Q, Gleason proper (non-negative additive weights on atoms are linear): NOT DECIDED. COMPUTED:
  weights depending only on the integer vector mod 2, 3 or 4 are constant (1120 rays, 2652 tetrads, entries up to
  3). Over the reals it is Gleason's theorem (imported, from memory; needs the completion).

### B2. FILED 1: synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values
No kill condition fired.
- PROVED: (P) => (L) => CHSH bound for directions, (L) = non-negative weights at EVERY pair of local directions
  (one twisted mode per party). No cross-setting positivity, no reality. So the stored sentence "positivity across
  settings is the part that cannot be dropped" is too strong in this realisation: what cannot be dropped is
  non-negativity at all local setting pairs, not only the four of a configuration.
- PROVED: the phase 1 box functional fails (L): weight -1/10 at a rational setting outside its four.
- PROVED (independence, stated precisely): lambda_c = <(1 - U - V + cK)x>_0, K = e1 f2, agree on all nine local
  products (hence on every local weight and every CHSH value of directions), are real, even, satisfy (L); (P) holds
  iff c = -1. (P) is independent OF: the algebra, linearity, normalisation, reality, evenness (univalence),
  invariance under the total-parity average, and the values of all local products. What separates the models is
  the value of one blade, equivalently the joint weights of the commuting pair U = X1X2, V = Z1Z2.
  ARGUED, not audited over the cone: that the stored record premises speak only of recorded local values.
- PROVED (descent): the mode-wise average E_N turns (P) into non-negativity of the 4 number-sector weights and maps
  the box and every lambda_c to the same (P)-state; the total-parity average does not give (P) (box o E has value
  -1/4 on an idempotent). So "derive (P) from the descent" fails for the total-parity descent and succeeds, in a
  trivial way, for the mode-wise one; the descent is defined on all functionals, the failure is not a domain issue.
- COMPUTED (b2.py, not filed; BA's ground): an even box in Cl(4,4) with parity-even observables, value 4; and for
  every box, the record map of one measured setting pair gives the positive functional <(1 + s A_i B_j)x>_0, the
  coarse record of K changes nothing.

### B3 (findings only; BA has the finite models, I did not duplicate them)
- From filed 1 (ARGUED consequence): any formalisation of irreversibility, superselection of recorded sectors and
  supervenience as statements about recorded local values is satisfied or violated by lambda_{-1} and lambda_c
  together, so none of them, nor their conjunction, gives (P).
- From filed 2: superselection of recorded sectors (read as the record map) and univalence are NOT independent of
  the choice of observables: together they force recorded observables to be parity-homogeneous.
- COMPUTED: after the record of a full setting pair the box functional is positive: (P) for post-record values
  follows from the superselection reading plus non-negative weights in the recorded context, for these functionals.
- Agreement with BA: the superselection premise is stored as a conditional on irreversibility; indifference is
  redundant for branch weights given (P) and sharpness.

### B4. FILED 2: synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables
No kill condition fired.
- PROVED (any ordered field, any number of modes): E_a(x) = (x + axa)/2 sends every even state to an even state iff
  a is even or odd.
- PROVED: one twisted mode per party, homogeneous settings: every even (P)-state gives |omega(C)| <= 2 (all 256
  choices). The 14/5 on an even state uses a mixed-parity direction whose record breaks evenness (12/25 on an odd
  element). Two modes per party with four odd blades: 8/3 on an even state.
- ARGUED (the reading): records act by E_a and univalence holds after records. Then parity-odd observables are
  allowed, mixed ones are not, and two modes per party are needed in both recorded settings.
- Flag as datum: NOT COMPUTED. ARGUED: the stabiliser of an orthogonal complex structure J on R^{2,4} is U(1,2),
  not inside the stabiliser O(2) x O(4) of a split, so J fixes the split only up to a 4-parameter family, and
  J -> -J has the same compatible splits: (P) does not see the orientation bit. BA's third proposal treats the
  null pairs.

## Where BA is exposed
1. BA's effects result (states of (P) = non-negative additive weights on effects) is close to definitional:
   non-negativity on effects IS positivity, and additivity over Q IS linearity. Its content is the reading of the
   stored residual postulate as additivity on effects, including sums of non-commuting effects, which is the
   non-contextuality assumption again; BA labels the reading "argued", and it should say so in title and one-liner.
   Effects are not outcomes of the stored record account (records are of two-valued observables).
2. BA's B1 atoms: existence "proved", the corner table "sampled (two greedy sets per signature)". My independent
   computation agrees on 9 cases. The general reason (only scalars symmetric in the corner) is the positivity of
   the involution; referees should check BA proves it and does not infer it from the sample.
3. BA's B1 speaks of "the weight of a projector E": it is a probability only for E self-adjoint for the same split
   (my boosted example: 9/8 and -1/8). BA's split proposal should carry that sentence.
4. BA's parity statement (even states see X u + Z Gamma, up to 14/5) is correct and is NOT the last word: those
   settings are of mixed parity and their records break univalence (filed 2). The two proposals must cite each
   other after acceptance or the store will hold "14/5 on an even state" and "at most 2" without the link.
5. BA's "the parity average creates no positivity" holds for the total parity; for the mode-wise average the
   statement needs the rider of filed 1 (v): there (P) is four non-negative weights.

## Unexpected links
- singularity.p-reduced-metric-level-reading-many (the mode-wise descent E_N, stored as a CHOICE between sheaf and
  net assembly) decides whether (P) has content: under E_N, (P) is non-negativity of number-sector weights and no
  CHSH value exceeds 2; under the total-parity (net) reading (P) is a separate premise. BA's split proposal finds
  that the states common to all adapted splits are exactly the mixtures of number-sector projectors: the same set.
  So the mode-wise reading removes at once the dependence on the split, the need for (P) beyond ordinary weights,
  and all Bell violation at the metric level.
- The dagger of the stored algebras over Q or R is a transpose: the self-adjoint local elements have no third
  ("Y") component, K = e1 f2 is the product of the two anti-self-adjoint local elements, and local values do not
  fix a state. This is the known failure of local tomography in quantum theory over the reals (Wootters; Hardy and
  Wootters; from memory). Renou et al., Nature 600 (2021) 625 (from memory) show real quantum theory with
  independent sources is experimentally distinguishable from complex: relevant to whether the series needs its
  complex unit (I_7 of the odd extension) in the algebra of two parties.
- one-relation.measure-indifference-borns-rule-located says the located Born density is relative to the
  laboratory frame gamma_0, "declared unsourced". In Cl(1,3) the blade inverse is x -> gamma_0 x~ gamma_0: the
  split of (P) IS that frame. The two unsourced data are one.
- Barnum, Beigi, Boixo, Elliott, Wehner 2010 (checked on the web): local quantum measurements plus no-signalling
  give quantum correlations. Filed 1 (ii) is its elementary one-mode case.
- The stored value 14/5 (the Pell record of phase 1) appears as the largest CHSH value of lambda_c on my grid and
  as the value at the mixed setting (3/5, 4/5).

## Decisions for Leon
1. Wording of synthesis.premise-positivity-of-values and op.positivity-of-values: "positivity on elements that
   combine quantities never measured together cannot be dropped" should become "for the CHSH bound, non-negative
   weights at every pair of local settings suffice in the one-mode realisation; (P) is strictly more and its excess
   is invisible to local values". Recommendation: restate at acceptance of filed 1 (maintainer edit).
2. Which descent on several modes: mode-wise (E_N) or total parity. It now decides whether (P) is a premise with
   content and whether the metric level carries any Bell violation. Recommendation: do not choose yet; record the
   consequence on singularity.p-reduced-metric-level-reading-many.
3. Adopt, or not, the reading "records act by E_a and univalence holds after a record" (filed 2 is conditional on
   it only in its Reading paragraph). If adopted: the one-mode Klein-twisted violation (clause (vii)/(viii) of the
   CHSH base, with its saturating state) is no longer a physical realisation and the two parity settings merge
   into "two modes per party". New assumes edges (to singularity.p-univalence and the superselection premise)
   would be maintainer-only.
4. Whether (L), non-negative local weights, should be a named weaker premise beside (P). Recommendation: no new
   postulate; mention in (P)'s text.
5. Imports (maintainer-only): Barnum et al. 2010; Kochen-Specker / Cabello et al. 1996; Peres-Mermin square;
   Gleason 1957 (needed for any statement that weights are linear over the completion).
6. Open and worth a target: Gleason over Q in size 4 (do non-negative additive weights on the rational atoms of
   two modes have to be linear). If not, linearity in (P) needs the completion postulate F4.
