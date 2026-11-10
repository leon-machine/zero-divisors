# attack-EA: cluster E, angle A (constructive)

Status: IN PROGRESS. Pre-registration written before any computation.

## Orientation (read in full)
F1 to F4, signed-directions (Z[G]/(c+1) is Cl_Z(p,q)), division-gives-the-rationals, the-sign-is-the-rotor-at-infinity
(rational rotors R_t), mode-split (Cl(l,l), parity p_k = f_k e_k, Klein twist y Gamma_A, dagger fixing e_k and
negating f_k, states rho = sum x x^dagger).

## Routes considered (all targets)
R1 (problem's own): Landau operator identity C^2 = 4 - [A1,A2][B1,B2] in the algebra, then a positivity step.
   Needs: a notion of state. Fails if positivity is not available from F1 to F3.
R2 (from another subject, mode-split): realise the two parties as one mode each of Cl(2,2) with the stored Klein
   twist (A: e1, p1; B: e2 p1, p2), so C^2 lies in span{1, J}, J a blade of square one; spectrum read off idempotents.
R3 (own): a sum-of-squares certificate with rational coefficients, 8 - C^2 = (1/2)(Z^dagger Z + {A1,A2}^2 + {B1,B2}^2),
   Z = [A1,A2] - [B1,B2], so that the bound needs no square root and holds over Q; and the dagger taken as group
   inversion of the signed-direction group (blade -> inverse blade), the scalar part as the group-ring trace, so
   positivity <x^dagger x>_0 = sum of squared coefficients is a theorem over Q, not a premise.
Choice: R3 for the bound (it works over Q and names exactly what a state is), R2 for the realisation and the
saturating state, R1 as the first clause.

## Kill conditions (registered before computing)
- E1-K1: the identity C^2 = 4 - [A1,A2][B1,B2] or the certificate of R3 fails on any exact instance in Cl_Q(2,2).
- E1-K2: a state (rho = sum x x^dagger, rational) and self-adjoint square-one commuting settings with w(C)^2 > 8.
- E1-K3 (premise audit): if the bound cannot be had without a positivity premise beyond F1 to F3 plus definitions,
  that premise is named and goes to Leon. Expected before computing: the only non-derived item is the DEFINITION of
  value (expectation = scalar part against a state) and the restriction to self-adjoint observables.
- E2-K: (a) a rational state with rational self-adjoint square-one settings attaining w(C)^2 = 8 exactly (collapse:
  then E2 is trivial the other way); (b) the supremum over rational data is strictly below 2 sqrt 2 (a gap). Either
  outcome is a result. Expected: neither; sup = 2 sqrt 2, not attained, Pell sequence.
- E3-K: an exact three-party state in Cl_Q(3,3) with w(C_AB)^2 + w(C_AC)^2 > 8 for self-adjoint commuting settings;
  or commuting directions on one side with w(C)^2 > 4.
- E4: findings only. No Born-rule claim will be filed.

## Prior art checked on the web (before filing)
- mathlib Algebra.Star.CHSH: CHSH (commutative ordered star-rings) and Tsirelson (any ordered star-ring over R) are
  formalised; the Tsirelson proof is a sum-of-squares decomposition using sqrt 2 and its inverse. So the algebraic
  bound is classical AND machine-checked. Not new here.
- C. Held, arXiv:2007.05301: 2 sqrt 2 in G^3 for vector-valued hidden variables. Different statement (no states).
- Kurzynski, Paterek, Ramanathan, Laskowski, Kaszlikowski, arXiv:1010.2012: sum of squared values of mutually
  anticommuting dichotomic observables is at most 1; Bell monogamy from it, for qubits. Direct prior art for E3.
- Tsirelson 1987 (J. Soviet Math. 36, 557) page found; Tsirelson 1980 and Landau 1987 cited from memory.
- BLOCKED (permission prompt not answered): en.wikipedia.org/wiki/Tsirelson's_bound and arxiv.org/abs/quant-ph/0611001
  (Toner-Verstraete). Both cited from memory.
- Doran-Lasenby multiparticle STA: search hit only (Havel and Doran quant-ph/0106063); from memory otherwise.

## Midway read of attack-EB.md and EB's filed proposals
EB filed (1) the signature list (value above 2 exists exactly outside 14 signatures), including the blade
configuration C^2 = 4 + 4K, the family of rational states (1+K)(1+rC) with values 8r (so: every rational in the
open interval is a value; sup 2 sqrt 2 not attained over Q; attained with sqrt 2), and (2) the parity-even statement
(two modes per party, no twist). I do NOT file: the value set, the "not attained because values are rational" line
as a headline, the signature dependence, the superselection statement, the PR functional.

## E1: established
Filed: synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate
(check4: 0 errors 0 findings; validate ok; registered).
- PROVED (classical): C^2 = 4 - [A1,A2][B1,B2] (sign convention fixed: C = A1(B1+B2) + A2(B1-B2)).
- PROVED (rational certificate; not found in sources read, not claimed new):
  8 - C^2 = (1/2)(Z^dagger Z + {A1,A2}^2 + {B1,B2}^2), Z = [A1,A2] - [B1,B2]. No sqrt 2 anywhere.
- PROVED: for every state w(C)^2 <= w(C^2) <= 8; strict over Q; refinement
  (w(C^2) - 4)^2 <= w(4 - {A1,A2}^2) w(4 - {B1,B2}^2); local case C^2 = 4.
- PROVED: w(C)^2 = 8 forces w({A1,A2}^2) = w({B1,B2}^2) = 0; for directions (unit elements of a party's plane) the
  anticommutator is a scalar, so anticommutation is forced as an identity of elements.
- PROVED (role of the twist): in Cl(2,2), party A = directions x e1 + z p1 of mode 1, party B = directions
  x e2 p1 + z p2 of the Klein-twisted mode 2; C^2 = 4 + 4 (a1^a2)(b1^b2) e1 f2. Untwisted sub-Clifford algebras are
  not two parties (e1 e2 is anti-self-adjoint of square -1).
- PROVED (blade check + proof): saturating state P = (1 + K)/4 + sqrt2 C / 8, primitive idempotent over Q(sqrt 2);
  unique on self-adjoint elements (uniqueness as a functional needs w(x^dagger) = w(x); a positive functional on a
  real star-algebra can carry an antisymmetric part that positivity does not see). P is NOT parity-even.
- PROVED by example: self-adjointness is needed. A = (17/8) e1 + (15/8) f1 has A^2 = 1, value 17/4 > 4.
  The RUN.md wording "for observables of square one" is false as stated; the hypothesis is self-adjoint and square one.
Premises used, exactly: signed-directions@2 (so F1, F2, F3), division-gives-the-rationals@2, mode-split@1 (clause
(ii), for the split only). Order: only "sums of squares are >= 0" in Q. F4: NOT used; clause (v) needs sqrt 2 only.
NOT derived (definition in the claim, premise in substance): a value assignment is linear, normalised, and
non-negative on x x^dagger. Kill conditions E1-K1, E1-K2: did not fire. E1-K3: the audit result is this paragraph.

## Revision of the E1 proposal after the coordinator's relay of EB's exposures (before the referee)
Same id (the id keeps the old slug; the TITLE is now "CHSH bound under positivity of values, with its one-mode
twisted realisation in Cl(2,2)"). Changes, on every level (formal, technical, lay, one-liner, note):
(a) scope: clauses (i), (ii) are signature-free upper bounds; the bound is approached only in some signatures (not
    Cl(3,0), Cl(1,3)); clauses (iv), (v) are Cl(2,2) only. (b) parity: the one-mode directions e1, e2 p1 are odd
    under the total parity; the stored parity average leaves commuting directions and at most 2; with even
    observables two modes per party are needed and (i), (ii) cover that case; "P not even" is said to depend on
    the directions. Added premise singularity.descent-parity-average@5 and a check of the average.
(c) positivity is now "Hypothesis (P)", stated as a hypothesis with content, at every level.
Old registered version moved to work/EA/aside/. Gate after revision: validate ok, check4 0 errors 0 findings.

## E2: established
Filed: synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records (check4 0/0, validate ok).
Not mine and not claimed: non-attainment (one line, values are rational) and "every rational in the open interval is
a value" (EB, signature proposal); the three values 14/5, 82/29, 478/169 of the pair state at rational points (EB,
parity proposal). So the SUPREMUM needs no Pell structure. What the proposal adds:
- PROVED: C and Cq = C I (I = B1 B2; Cq is the CHSH element of (A2, -A1, B1, B2)) anticommute with equal squares;
  every state has w(C)^2 + w(Cq)^2 <= 8.
- PROVED: the pure states of the sector K = 1 are exactly rho_{X,Y} = P_K/2 + (X C + Y Cq)/16 with (X, Y) a RATIONAL
  POINT of the circle X^2 + Y^2 = 8. So a pure-state value S has 8 - S^2 a rational square. The corner algebra is
  the quaternion algebra generated by C (square 8) and I (square -1); it is split over Q, which is why rational
  pure states exist at all, and (2 sqrt 2, 0) is the point where the circle meets an axis.
- PROVED: these states are the orbit of ONE parity-even state rho_0 under y_u = 1 + uI, u in Q or infinity, and
  equivalently rho_0 with party B's directions turned by the stored rational rotor R_u = (1 - uI)/(1 + uI).
  S(u) = 2(1 - 2u - u^2)/(1 + u^2). No square root: the projector is rational for every rational u (only a unit
  VECTOR would need sqrt(1 + u^2)). "Only ratios matter" is true and does not collapse the question.
- PROVED: parity-even pure states of the sector at the blade settings are rho_0 and rho_inf only, values +-2;
  rho_inf IS the stored eviction pair state at equal weights (cs = -1/2).
- PROVED (denominator law): a rational value P/Q in lowest terms has 8 - (P/Q)^2 >= 4/Q^2; equality iff P = 2x,
  x^2 - 2Q^2 = -1. Records S_k = 2, 14/5, 82/29, 478/169, ...: pure-state values, each larger than EVERY state value
  of smaller denominator (mixed states and any directions of these planes included), S_k < 2 sqrt 2 < S_k + 1/Q_k^2.
  The local value 2 is the first Pell record.
- NOT DECIDED: which rationals are values of pure states outside the sector (a rational quaternary form question).
Kill conditions E2-K (a), (b): did not fire. Premises: signed-directions@2, division@2, mode-split@1 (ii) and (v),
the-sign-is-the-rotor-at-infinity@1 (i) to (iii). F4 not used. Hypothesis (P) as in E1.

## E3: established
Filed: synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two (gate status below).
- PROVED: for observables A1, A2 the diagonals A1 + A2 and A1 - A2 anticommute and their squares add to 4.
- PROVED (classical, Toner-Verstraete; method is Kurzynski et al.'s correlation complementarity): under (P),
  w(C_AB)^2 + w(C_AD)^2 <= 8 for any three mutually commuting pairs of observables in any Cl_k(p,q). Rational proof,
  no dimension, no sqrt. Same lemma reproves w(C)^2 <= 8.
- PROVED: commuting directions give C^2 = 4; in a commutative subalgebra C = +-2 on each minimal idempotent; 4 is
  never reached under (P) with self-adjoint elements.
- COMPUTED: attained at (2, 2) over Q on three modes with nested twists; a pair of value 14/5 leaves <= 4/25.
- NOT EXAMINED: whether the whole arc between (2,2) and (2 sqrt 2, 0) is reached by rational states.
Kill condition E3-K: did not fire (147 state/setting combinations, max 1296/169).
Premises: signed-directions@2, division@2, mode-split@1. Hypothesis (P).

## Bridge lead L1 (discrepancy on the pair state): settled by exact computation (work/EA/s4.py)
On the stored pair state with amplitudes c, s (mode-split clause (v)) and the twisted one-mode parties the
correlation matrix in the directions (e, p) is EXACTLY diag(2cs, 1): at (3/5, 4/5) it is diag(24/25, 1), at
(20/29, 21/29) diag(840/841, 1), at (5/13, 12/13) diag(120/169, 1). Maximal squared CHSH value over the planar
directions 4(1 + 4c^2 s^2) (4804/625 at (3/5, 4/5)): the bridge-hunter's formula is right for THAT reading.
EB's 2(c + s) is also right for what EB states: in EB's clause (iv) the state is the EQUAL-WEIGHT pair state and
(c, s) is the rational point of party B's DIRECTIONS, B_+- = c p2 +- s e2 p1, not the amplitudes. At equal weights
the correlation matrix is the identity and 2(c + s) <= 2 sqrt 2. No error in the filed result; the two symbols
(c, s) mean different things. My E3 clause (v) states the non-maximally entangled case with the right maximum,
S = 2(z + 2cs x) <= 2 sqrt(1 + 4c^2 s^2), and my E1 clause (iv) bound 4 + 4|a1^a2||b1^b2| is over all states.
## Bridge lead L2
Done in E3: clause (v) and the note (window mode: a third party is left squared value about 4r^2 < 4; the stored
note note.singularity.monogamy-firewalls-small-corrections-theorem is named as a remark only). Nested twists: three
parties with odd observables need twists by p1 and by p1 p2; BOTH are instances of the stored clause (ii) (second
time with untwisted set {1,2}), so the stored twist theorem does cover it. EB's "covers only two parts" is too
pessimistic; checked exactly (and a single factor p1 on mode 3 fails to commute with party B).

## E4 (findings only; nothing filed)
- What E adds to the stored measurement account: the first statement in the graph that constrains JOINT values
  across incompatible settings; the record-chain results speak of one context at a time.
- What it does not: it derives no probabilities. Everything rests on Hypothesis (P).
- ARGUED (not filed, phase 2 candidate): (P) plus sharpness gives the Born weights. The uniqueness argument of
  E1 clause (v) is general: if w satisfies (P) and w(rho) = 1 for a self-adjoint idempotent rho with
  rho x rho = t(x) rho, then w(h) = t(h) for all self-adjoint h, i.e. the weight of an idempotent q is
  2^l <rho q>_0, "scalar part of the product with the projector". Proved in the E1 proof for one rho; the general
  statement is the same four lines and is ARGUED here. Caution: (P) contains linearity across incompatible
  elements, which is where Gleason's theorem lives; this route replaces the imported envariance argument by a
  named premise, it does not remove the premise.
- ARGUED: for an even number of directions the scalar part is the only normalised linear functional invariant
  under conjugation by the signed directions (stored centre result: every blade other than 1 is negated by some
  generator). That singles out the tracial state by symmetry, in the spirit of envariance, and nothing more.

## Unexpected links
- The stored rational rotor R_u (the-sign-is-the-rotor-at-infinity) is exactly the map between "rational state"
  and "rational directions" in E2; the point u = infinity (the sign -1) is the stored eviction pair state.
- 8 - C^2 = 4(1 - K) is a zero divisor (a multiple of an idempotent): the Tsirelson value is where 8 - C^2 stops
  being invertible. Observation only.
- The pure states of the sector are a conic with a rational point (a split quaternion algebra (8, -1) over Q);
  the same split/non-split question decides EB's signature list (matrix size). One structure read two ways.
- Positivity is frame-dependent in indefinite signature: the adjoint is fixed by the group of signed directions
  and is invariant under O(p) x O(q) only. A boosted direction (17/8) e1 + (15/8) f1 has square one and is not an
  observable; treating it as one gives CHSH 17/4. Any later use of "observable = square one" needs this.
- Monogamy and the horizon: see L2.

## Decisions for Leon
1. Hypothesis (P) (same as EB's decision 1): adopt "values are a linear normalised functional non-negative on
   x x^dagger, dagger = inverse on signed directions" as a named premise (new postulate: maintainer-only), and
   then E1, E2, E3 get an assumes edge to it. Recommendation: adopt; it is also the natural phase 2 premise.
2. Should (P) include w(x^dagger) = w(x)? Without it the saturating state is unique only on self-adjoint elements.
   Recommendation: include it.
3. Parity-odd observables (same as EB's decision 2): my E1 (iv), (v), E2 and E3 (iv) use the one-mode twisted
   realisation with odd directions. If odd elements are not observables these become statements about the twisted
   algebra only, and the physical realisation is EB's two-modes-per-party one, to which my general clauses apply.
   If you decide "even only", E2 should be restated on two modes per party (the circle and the Pell law are
   properties of the corner algebra and carry over; not done).
4. founded_on edges for the three proposals (rooting in F3 via the rational algebra): maintainer-only.
5. Literature to import as Facts if wanted: Tsirelson 1980, Landau 1987, Toner-Verstraete 2006 (all from memory;
   the Toner-Verstraete page could not be opened), Kurzynski et al. 2011 (checked).
6. The id of the E1 proposal still carries the old slug "for-two-subsystems-of-a-clifford-algebra"; rename at
   acceptance if wanted.

## Gate status (final)
- synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate: revised version registered;
  validate ok, check4 0 errors 0 findings.
- synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records: registered; check4 0 errors 0
  findings; validate ok. One proof sentence (a citation of the division result, W215) and one note sentence were
  added after the check4 run; check.py and the derivation are unchanged since it, and validate was rerun (ok, no
  findings).
- synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two: registered; validate ok, check4 0 errors
  0 findings.
Status: COMPLETE for the attack round.
