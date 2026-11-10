# Attack C2B (cluster C2, angle B: adversarial and cross-pollinating), run 2026-11-09-bridges

Labels: proved / computed / argued / conjectured; "memory" = literature cited from memory, unchecked.
Status of this file: pre-registration first (below, unchanged); results sections added 22:25 onwards.

## Pre-registered kill conditions (written first)

Y1 (Hadamard scaling as the curved-field clause). My claim under attack: the stored bounds are statements on one
null generator (a restricted kernel) and cannot give the scaling degree of the squared parametrix at the diagonal of
M x M. Kill of my attack: a stored clause (at the pinned versions) that bounds the kernel in a full neighbourhood of
the diagonal in four dimensions, or from which the four-dimensional degree follows by a stated restriction argument
whose hypotheses the stored kernel meets. If the kill fires the constructive clause stands and I say so.

Y2 (rung count as an equivariant index). (a) Reduction: my attack is that "k = 1 + least j with an equivariant map
to S^j" needs more than the stored clauses. Kill of the attack: clause (3) of the lens-wall result and clause (2) of
the rung-count result give k = e(L) on a definite side with no further hypothesis, and e(L) is the coindex by the
classifying-map correspondence. (b) Independent bound: claim to test by hand reasoning before any script: on a
definite side k <= 4 forces the quaternionic line bundle L (x) H to be trivial, and on L^5(4) it is not, because
Sq^2 : H^3 -> H^5 (mod 2) is nonzero there; with the explicit five-component map (conj(q) j q, z_3^2) this would give
k = 5 exactly. Kill: Sq^2(xy) = 0 on L^5(4), or an explicit exact equivariant map S^5 -> R^4 minus 0 with
f(Jv) = -f(v), or a stored wall-existence clause that fails for L^5(4) with a definite side (then the count is a
statement about e(L) only). Also kill if the primary obstruction e(3L) in twisted H^3 is nonzero (then the tower
stops at the first step and my route is unnecessary).

Y3 (order-four element and sixteen). Claims to test: (i) the stored order-four element (Klein twist) is a function
of the grading operator alone, so it exists for every content and its preservation by the descent is automatic and
carries no information; (ii) the only order-four element with a uniform odd charge on the sixteen components is the
complex unit on the generation space (the centre of the Spin(10) stage), and a Majorana pair term on the singlet
anticommutes with it, so with the stored Majorana premise it is broken to the grading. Kill for (i): the stored
element is not in the span of 1 and the grading (it acts with a charge on generators). Kill for (ii): the pair term
commutes with the order-four element, or the stored Majorana premise is not a pair term in the slot module's sense.
The mod-16 statement is literature from memory and stays a decision for Leon.

Y4 (short tests). One kill each: C7 conformal embedding so(10)_4 in su(16)_1: kill if c or the weight of the 16
disagree as exact fractions; T-phase triviality for n_g copies: kill if the phase condition gives anything other than
the stored 24 | 16 n_g type condition; R12: kill if the two helicity weights have different signs or normalisations
in the stored statements; C5: kill if no state is stored on the collar (then "capacity" is undefined).

## Midway note for the sibling (written after reading attack-C2A.md at 22:10)
C2A is filing the definite-side count k = 5 on L^5(4) (Thom-space route). I do NOT file that. I reached k = 5
independently by a different route (see Y2 below), which is a second derivation of C2A's lower bound.
What I intend to file, so that nothing is filed twice:
 P1 (Y2): three rungs force the doubled dying line stably trivial when twisted H^2 vanishes; so k >= 4 on EVERY side
    of the quarter-turn lens walls (indefinite sides included), n >= 2. Not the definite-side count.
 P2 (Y3): the negative side: the Klein twist is a polynomial in the grading (carries no charge, exists for every
    content); the Majorana element T is odd under the uniform order-four element (the pseudoscalar of the ten
    Majoranas), so a vev along T breaks it to the grading; parity obstruction for fifteen components.
    If C2A files the existence and charges of the order-four element, my P2 keeps only the negative clauses.

## Y2. Rung count as an equivariant index (op.wall-class-invariant)
Routes: (R-a) the problem's own: obstruction tower for sections of kL in the stored cell model; (R-b) from another
subject (the rotor/quaternion structure of the store's lens completions): kL at k = 1, 2, 4 is L tensored with the
reals, the plane's even subalgebra, the quaternions (the even subalgebra of Cl(3,0)), and a nowhere-zero section
trivialises it as a line over that algebra; (R-c) my own: the complement N of the stored necessity clause at k = 3 is
a plane bundle, classified by a twisted Euler class. Chosen: R-b to test the sibling's count independently, R-c for
a result of my own on indefinite sides.
- Kill (a) (reduction needs more than the stored clauses): did not fire. Clause (3) of the lens-wall result gives
  k = e(L) on a definite side from clauses (1), (2) of the parent with N(G-bar) = 0; e(L) = coindex is the
  classifying-map correspondence. The wall with a definite side on L^5(4) x R is stored (two-rung result, existence
  paragraph); note that L does NOT embed in T Sigma there (w_5(T Sigma (x) L) = x u^2 != 0, computed from the stored
  classes), the stored embedding c(x) uses the normal direction. proved/lookup.
- Primary obstruction e(3L) in twisted H^3 = Z_2: zero (it is 2y times e(L)). So the tower does not stop there.
- Independent derivation of k = 5 on a definite side of L^5(4) (argued, classical inputs from memory: cohomotopy of
  a 5-complex, pi_5(S^4) = Z_2 detected by Sq^2, cells of HP^infinity): four components <=> the quaternionic line
  L (x) H is trivial <=> the map Sigma -> CP^2 -> S^4 (degree 4 on CP^2) is null. [Sigma, S^4] = Z_8 because
  Sq^2 : H^3 -> H^5 is x u -> x u^2 != 0 (Cartan, Sq^1 x = x^2 = 0), and the map is 4 times a generator: not null.
  Same conclusion as C2A's Thom-space argument by a different route; the two agree on every control
  (L^3(4): 3; RP^5: primary; L^5(8): no obstruction). My route gives more at d = 8: there the map IS null, so four
  components exist on L^5(8) (C2A's clause (5) only says its obstruction vanishes). argued.
- Upper bound: (2 Im z1 z2, conj(z1)^2 + z2^2, z3^2) is odd under the quarter turn with norm^2
  (|z1|^2+|z2|^2)^2 + |z3|^4; C2A's map is the same up to a change of basis. Not filed by me.
- Established and filed (P1): three rungs force L + L stably trivial whenever H^2(Sigma; Z^x) = 0 (plane bundle with
  nowhere to put its twisted Euler class has a section, and the remaining line is L). On L^{2n+1}(4), twisted
  cohomology is Z_2 in odd and 0 in even degrees (computed, stored cell model), so k >= 4 on EVERY side for n >= 2:
  for n >= 3 from the stored K-ring alone (2(1 - chi^2) != 0), no spin class and no lambda-operations; for n = 2
  conditional on the spin class (L2) of the stored two-rung result. Stored bound was 3 at n = 2, 3, 4.
  proved on background (G), n = 2 conditional. Proposal:
  synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side, check4 exit 0 (two I405 notes, no
  warning), validate ok, registered.
- With C2A's e(L) <= 5: on indefinite sides of L^5(4), k is 4 or 5. Next obstruction named: a rank-three N with
  w_1 = x and N(G-bar) + L + N = N(G-bar) + R^4, an unstable question (rank 5 over a 5-complex when q = 1).
- Conjectured (same guess as C2A, from L^5(4) and L^5(8) only): the secondary obstruction to four components on a
  definite side is x u_a^2, u_a the mod-2 reduction of a class a with 2a = beta x. Fits the open problem's success
  clause (ring data of a).
- Literature (memory, unchecked): Stolz's table for the level of RP^{2m-1} gives m + 2 = 5 at m = 3, consistent;
  my recollection of the table gives 3 at m = 1 where the true value is 2, so the table as I remember it is not
  reliable and nothing rests on it.

## Y3. Order-four element and sixteen (op.order-four-anomaly-and-sixteen)
Routes: (R-a) the problem's own: take the stored Klein twist and compute its charges; (R-b) from the standard-model
subject: the pseudoscalar of the ten Majoranas (centre of the rotor group) and the stored Majorana element T;
(R-c) import the mod-16 theorem. Chosen: R-a and R-b, exact; R-c is Leon's decision.
- Kill (i) did not fire: stored Z = (1 + I_4 Theta)/(1 + I_4) and V = (1 + I_4 k)(1 + I_4)^{-1} equal
  p_+ - I p_-, a polynomial in the grading. Ad_V(a) = -I a k on odd a: grade two in the two-mode model, not a
  phase on generators. So the element the open problem names exists for every content and constrains nothing; its
  preservation by the descent, or by anything that keeps the grading, is automatic. proved (exact check in Cl(4,1)).
- The uniform-charge element exists and is the pseudoscalar omega of the ten: omega^2 = -1, commutes with the 45
  bivectors, omega = I Gamma, so the unit I on all sixteen. It is a product of five mode rotors inside the
  Pati-Salam algebra: a gauge transformation at Pati-Salam, u(5), so(10). proved (Cl(10,0)).
- Kill (ii) did not fire: omega T omega^{-1} = -T for the stored Majorana element; [sum of mode bivectors, T] =
  +-10 I T. So omega is not in the Standard Model group and a vev along T breaks it to the grading. proved.
- Consequence (argued): in the stored chain there is no stage where omega is an unbroken symmetry that is not a
  gauge transformation, unless the Majorana term is absent (against Premise (M)). Where it is gauge, the sixteenth
  component is already forced by the multiplet structure. So the mod-16 statement, even if imported, adds no
  constraint within the stored chain; it would bite only in a Dirac-neutrino reading.
- Arithmetic (computed): signed counts on fifteen components are always odd; three fifteen-component generations
  never give an even total; 15 n_g = 0 mod 16 first at n_g = 16; sixteen gives 16 (uniform) or 0 (balanced).
- Does the mod-16 statement apply to the store's structure at all? argued: (1) the five-manifolds of the bordism
  statement are auxiliary (inflow) manifolds for four-dimensional fields; a wall with cross-section RP^5 lives in a
  six-dimensional M, not in the store's (1,3) fields, so "RP^5 walls" is not where the condition would be read;
  (2) RP^5 with tautological line does satisfy w_2(T) = x^2 (the condition for the twisted spin structure), while
  L^5(4) has w_2 = u != 0 = x^2 (computed from stored classes), so the bridge file's exclusion of L^5(4) stands,
  for this reason rather than the order-eight rotor; (3) the generator of the bordism group is cited from memory in
  the open problem and I could not confirm it.
- Proposal: synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element, check4 exit 0 with no
  findings, validate ok, registered.

## Y1. Hadamard scaling as the curved-field clause
- My pre-registered attack is killed: the store does hold a bulk scaling statement (clause (a) of the scaling-limit
  theorem; hadamard-dirac-states-scale-to-the-flat-massless-vacuum, clauses (ii), (iii)), and clause (v) of the
  vacuum-polarisation theorem already cites it in text. The bridge's two named entities (generator level) are the
  wrong inputs: by the stored text itself (clause (v) of the bulk theorem) the generator restriction is not a
  pullback and scales one direction. So the exact place the generator-level bounds fail is stated in the store.
- Test of C2A's central step (their proposal on the kernel): sum_mu gamma^mu W(e_mu ^ xi) = 0 on the Schwarzschild
  form of the Weyl map, 3 lam xi on lam B, and a non-Weyl control fails: exact, work/C2B/y1_weyl_contraction.py.
  Their arithmetic -1/4 - 1/6 = -5/12 agrees with the stored Taylor data. computed. Their claim survives.
- Where the clause still fails to be a theorem (argued), in order of weight:
  1. The count. On a fixed field the transverse local kernels of order two are NOT a one-dimensional space: the
     Euler-Lagrange kernel of the integral of c(x) F^2, a -> d_mu(c F^{mu nu}), is transverse and gauge invariant
     for every smooth c (antisymmetry). On the flat field translation invariance makes c constant; on a curved
     field nothing stored does. "The extension count is the flat one" needs local covariance with scaling
     (Hollands and Wald, memory), which is not in the store. C2A flags this as "not part"; their clause (iv)
     "as on the flat field" is true only pointwise.
  2. Point against diagonal: the stored limit is at a point with both arguments scaled; the extension theorem
     needs the degree transverse to the diagonal, locally uniformly. Derivable from the stored joint smoothness of
     sigma_l, not stated.
  3. Regularity: the stored state remainder S is only C^1; the product of a C^1 function with a boundary value of
     sigma^{-2} is not defined in general. C2A's result is about the parametrix kernel only (they say so).
  4. No Wick rotation on a general field: the stored flat proof is Euclidean; the curved clause needs the
     boundary-value product (C2A's (SD), memory).
- Nothing filed by me on Y1 (the constructive result is C2A's; the counter-model in 1 is a one-line identity).

## Y4. Short tests
- C7/N4 (computed): c(so(10)_4) = 180/12 = 15 = 255/17 = c(su(16)_1); embedding index of the 16 is 4; weight of the
  16 is (45/8)/12 = 15/32 = 255/544. The 210 has C_2 = 12, weight 1: the 210 currents of su(16) outside so(10).
  Vacuum T-phase for n_g copies: so(10) part alone 24 | 15 n_g, that is 8 | n_g; with the number current (c = 16)
  24 | 16 n_g, that is 3 | n_g: the two stored verdicts, nothing new. The fermion sector (weight 1/2) gives the
  same condition through T^2. Kill stands (no Virasoro algebra on a window). No open problem warranted.
- R12/C8 (lookup): killed. The "helicity" of the Kasner wall result is the coframe twist theta ^ d theta, not the
  spin helicity of the helicity-lift result. A homonym, not a link.
- C5 (lookup, argued): killed as posed. A k-rung completion is a symmetric form on a bundle; no state is stored on
  the collar, so "capacity" is undefined. The descent's rungs are rungs of record for nu modes.
- N5 (argued, Witt index): at the zero set of a scale the form sigma^2 g^{-1} vanishes entirely and to second order,
  so (T2) and (T3) of tameness fail; a completion in the stored sense must make a totally isotropic T*M of rank n
  nondegenerate, which needs at least n rungs, not the one hyperbolic plane of the tractor bundle. The suggested
  "one rung" is refuted in the stored sense of completion; an open problem would need a new definition first.
- N6 (argued): the descent is the trace-preserving expectation onto the commutant of P; states that commute with P
  are fixed and recovered trivially, and a state is recoverable relative to a P-invariant reference exactly when it
  commutes with P. For thermal product states of an evicted window the question is empty. No open problem unless a
  stored state fails to commute with P.
- N7: not reached.

## Unexpected links
- The thresholds 1, 2, 4 of the definite-side rung count are the division algebras the store already uses as even
  subalgebras: k <= 2 iff L (x) C is trivial (the stored integral twist beta x), k <= 4 iff L (x) H is trivial.
  The stored L(4,1) completion ("adjoint frame of the half-turn rotor") is the first instance.
- Y3 against C1's X4 (proposal on mass terms as pair terms): the same fact read twice. The Majorana element has
  charge 2 under the pseudoscalar's generator; "only the charge separates Majorana from Dirac" is the statement
  that a Dirac term commutes with omega and a Majorana term anticommutes.
- Y3 against Y2: the twisted-spin condition w_2 = x^2 holds on RP^5 and fails on L^5(4), read from the stored
  classes; the walls where the rung count exceeds the mod-2 height are exactly not the ones the anomaly would use.
- Y1: the Weyl field strength is invisible to the one-loop kernel to degree four for the same reason it is
  invisible to the Sakharov coefficient (no rank-two contraction): one identity, two subjects.

## Decisions for Leon
1. Y2: the definite-side count and my every-side bound both rest on classical topology not in the store. For P1:
   the spin class q_1 (already declined once) is needed only at n = 2; accept the n = 2 clause as conditional, or
   import q_1. For C2A's count: Steenrod squares, Chern classes with the splitting principle, the Thom isomorphism.
2. Y3: whether to import the mod-16 anomaly statement at all. My recommendation: no. In the stored chain it adds no
   constraint (omega is gauge above Pati-Salam and broken by T below). If imported, the open problem's success
   clause should be restated around omega, not the Klein twist, and around a reading without the Majorana term.
3. Y3: op.order-four-anomaly-and-sixteen names the Klein twist as the candidate; that sentence should be
   corrected if P2 is accepted, and "walls with cross-section RP^5" reconsidered (six-dimensional setting).
4. Y1: import local covariance with scaling (Hollands and Wald) as a Fact or state it as a premise; without it the
   curved-field count is a function space, not the flat one.
5. N5: whether total-radical walls deserve a definition (it is not an extension of the tame theory).
