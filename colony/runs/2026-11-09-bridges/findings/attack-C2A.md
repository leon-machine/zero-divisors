# Attack C2A (constructive), run 2026-11-09-bridges, cluster C2

Labels: proved / computed / argued / conjectured; "memory" = literature cited from memory, unchecked.
Status of this file: final. The pre-registration below was written before any computation (orientation by lookups
and pencil reasoning only) and is unchanged.

## Pre-registered kill conditions (written first)

Y2 (exact rung count on L^5(4), definite side). Route chosen: (a) reduce k = e(L) to "kL has a nowhere-zero
section", equivalently a map f: S^5 -> S^{k-1} with f(Jv) = -f(v) (prove from stored clauses); (b) upper bound by an
explicit quadratic map in Cl(6,0); (c) primary obstructions in the twisted cochain complex of the stored cell model;
(d) the secondary obstruction for k = 4 (pi_4(S^3) = Z2, class in H^5(L^5(4); Z2)) through the circle fibration
L^5(4) -> CP^2 and its Thom space. Kill conditions:
 K2a. The reduction is killed if the stored definite-side equality k = e(L) uses more than clauses (1), (2) of the
      parent (then the index statement is not a consequence of stored clauses).
 K2b. The route is killed as an "exact" result if deciding k = 4 against k = 5 needs a classical theorem that the
      store does not hold (homotopy of spheres, Steenrod squares, Thom isomorphism, real K-theory). Then the outcome
      is the narrowed window plus the named obstruction, the theorem listed as a decision for Leon, and the claim is
      filed conditional and labelled so.
 K2c. Internal control: the same method must give k = 3 on L^3(4) (stored), must not exclude 4 on L^5(8), and must
      exclude 4 on RP^5 at the primary level. If a control fails the method is wrong and nothing is filed.
 Prediction recorded before computing: k = 5 (upper bound 5 by the map (z1^2 - conj(z2)^2, 2 Re z1 z2, z3^2); lower
 bound from Sq^2(U h) = (c1 + 1) U h^2 on the Thom space of O(4) over CP^2). If the explicit map fails its norm
 identity the upper bound falls back to 6.

Y1 (scaling degree on a Weyl-curved field). Route chosen: the exact form of the one-loop vacuum-polarisation kernel
of the stored Dirac Hadamard parametrix, G = (D + m)(U/sigma + V log sigma), U = Delta^{1/2} R: the transport
rotors cancel from the leading term, which is Delta times the flat kernel in the vector D sigma; the next terms
through D_x U from the stored Taylor data. Kill conditions:
 K1a. (the bridge's kill) only generator-level bounds are stored. Checked by lookup before computing: NOT fired,
      the bulk scaling theorem (hadamard-dirac-states-scale-..., clause (ii), (iii)) is stored and already used by
      clause (v) of the vacuum-polarisation result, which is "argued".
 K1b. Killed if the leading kernel's degree on a Weyl-curved field differs from 6, or a degree-5 term survives
      (then the flat count fails or needs a first-order counterterm).
 K1c. Killed as "flat count" if a Weyl-linear term of degree 4 is present in the kernel: then the Weyl field
      strength carries its own extension freedom c(x) delta and the count is the flat one only after covariance.
      Prediction: absent, because gamma^mu R(e_mu ^ xi) is the Ricci vector (protraction-free field strength), so
      D_x U is Ricci-linear at first order.
 K1d. The result stays "argued" if the passage from kernels of the form (smooth) sigma^{-k} to scaling degrees
      needs a lemma not in the store (products with smooth functions vanishing to order j lower the degree by j;
      Brunetti and Fredenhagen, memory). Then it is filed as proved given that lemma, named.

Y3 (order-four anomaly and sixteen). Route: find the store's order-four element on the slot module, compute its
charges on the sixteen components exactly, test commutation with the stored gauge chain and the descent. Kills:
 K3a. No order-four element with square the grading acts on the slot module in the store's own sense (the Klein
      twist lives on the field net, not on the internal sixteen): then record that and stop.
 K3b. The charges on the sixteen are not all odd, or the element is in the gauge group times the grading (then the
      Z4 is not independent: a gauge transformation has no anomaly beyond the stored ones and the mod-16 argument
      does not separate 15 from 16).
 K3c. The mod-16 statement is literature (memory); nothing is imported; a necessary condition is filed only if it
      is derived from stored objects.

Y4 (short tests, findings only). Each test has kill "no exact computation is defined by the stored objects".

## Y2. Exact rung count on L^5(4), definite side (op.wall-class-invariant, new attack item)
Routes considered: (1) the problem's own: obstruction tower in the stored cell model (primary class in twisted H^3,
then pi_3(S^2), pi_4(S^3)); (2) from another subject: real K-theory / the level of projective spaces (Stolz; memory),
which is what the general answer rests on, a heavy import; (3) my own: explicit quadratic maps in the algebra for
the upper bound, and the secondary obstruction moved to the Thom space of O(4) over CP^2, where it is a Steenrod
square. Chosen: (3) with (1) for the primary classes; reason: the upper bound becomes an exact identity in Cl(6,0)
and the lower bound needs no homotopy groups and no K-theory.
Established:
- proved: on a definite side k = e(L) = least k with F: S^{2n+1} -> R^k \ 0, F(Jv) = -F(v) (the reduction of the
  bridge lead R7; uses only the stored equality k = e(L) of two-rungs clause (1); kill K2a not fired).
- proved (exact identity, grids meeting the degree bounds): F(v) = w0 e1 w0 - u e1 u + 2 (w0.u) e3 + w2 e5 w2 is odd
  under J, has five components and Q(F) = (Q(w0)+Q(w1))^2 + Q(w2)^2. So k <= 5 on L^5(4); blocks give
  k <= ceil(3(n+1)/2) on L^{2n+1}(4) (2, 3, 5, 6, 8, 9 for n = 0..5).
- proved on the stored background (G): twisted cohomology H^j(L^{2n+1}(4); Z_x) = Z2 (j odd), 0 (j even); the primary
  obstruction to three components (class in twisted H^3 = Z2) VANISHES (the three-component map lives on the
  3-skeleton). So the first computation named in the bridge file gives zero and the tower has to be climbed.
- proved given (T) (Steenrod Sq^2 with Cartan formula; Chern classes with splitting principle; cohomology of the
  Thom space of a line bundle): no odd map S^5 -> R^4 \ 0. Hence k = 5 on L^5(4) definite side, k >= 5 on every
  L^{2n+1}(4), n >= 2, and 5 <= k <= 6 on L^7(4). The obstruction is Sq^2(Uh) = (d+1) U h^2 on Th(O(d) | CP^2) against
  Sq^2 c_2 = c_1 c_2 + c_3 = 0; second route (Chern character lattice, 5/2 not an integer) agrees: parity n(d+1).
- computed controls (K2c): d = 2 (RP^5) obstruction primary; d = 8 none; L^3(4) no obstruction (stored k = 3). Passed.
- Kill K2b FIRED in the pre-registered sense: the lower bound rests on classical theorems the store does not hold.
  Filed as conditional and labelled so at every level.
- argued: the secondary obstruction to four rungs on a general wall is x cup rho(a)^2 for a class a with 2a = beta x
  (it is x u^2 on L^5(4) and 0 on L^5(8)); this is the shape the sharpened success clause asks for.
- not reached: k on L^7(4) (5 or 6); indefinite sides (sibling's P1: k >= 4 on every side).
Proposal: synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five
  (check4 exit 0, no findings; validate ok; registered).
Next step: L^7(4): is there an odd map S^7 -> R^5 \ 0 (Pfister and Stolz, memory, say yes: level m + 1 at m = 4)?
The obstructions are in H^6(;pi_5(S^4)) and H^7(;pi_6(S^4)); the quadratic maps built from Clifford generators do
not give it (five anticommuting symmetric involutions and J would need Cl(5,1), whose module has dimension 16).

## Y1. Scaling degree on a Weyl-curved field (op.qft-loops-and-renormalisation, attack item 3)
Routes considered: (1) the bridge's: the generator-level bound "null vacuum plus kernel of degree at most 0"; fails
as feared (one null direction), and is not needed; (2) from thermality: the stored BULK theorem
(hadamard-dirac-states-scale-..., clauses (i), (ii)), which gives the parametrix U/sigma + V log sigma with Taylor
data; (3) my own: write the kernel covariantly in s = D sigma and the transport rotor and see what cancels. Chosen
(2)+(3). Lookup finding: the stored vacuum-polarisation result ALREADY cites the bulk theorem in its clause (v)
("argued"); the bridge's "no path" was between the generator results and the loop result only. K1a not fired.
Established:
- proved (two-line algebra; exact samples as control): the transport rotors cancel from the leading kernel,
  Pi_6 = -Delta [2 (a.s)(b^.s) - (a.b^) Q(s)] / sigma^4, b^ = R b R~: the flat trace in s, times Van Vleck, for any
  field strength. Mass cross terms are odd and vanish; no degree 5 (K1b not fired).
- proved from the stored Taylor data: a.D_x R = -(1/4) Riem(a ^ xi) R, so D_x R = -(1/4) Ric(xi) R (the trivector
  part is the protraction identity); D_x U = -(5/12) Ric(xi) R + O(xi^2) in the stored conventions. A Weyl-type field
  strength contributes NOTHING at this order (checked on type D, rotated copies and sums). K1c not fired: there is
  no Weyl-linear term of degree 4.
- proved given (SD) (three scaling-degree rules from memory; K1d fired in that sense): degrees 6, none at 5, 4 with
  coefficients m^2, Ricci map and V(x,x) only, Weyl only at degree <= 3.
- proved given (SD) and the imported extension theorem (ii): omega = 2 at every point whatever the Weyl field
  strength; pointwise freedom 15 derivatives of delta per index pair as on the flat field; the Weyl terms extend
  uniquely; the stored flat extension in normal coordinates extends the leading part with the stored log coefficient.
- argued, not filed: the reduction of the pointwise freedom to Z_3 by covariance and dimension (a coefficient
  Weyl x dd delta has scaling degree 6, so scaling degree alone does NOT exclude it; excluding it needs the
  Hollands and Wald scaling axiom, memory); that no Ward anomaly can carry the Weyl field strength (no contraction
  of Weyl with one free index and one derivative).
- not done: transversality of an extension on the curved field; the value of the Ricci terms of degree 4.
Proposal: synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
  (check4 exit 0, no findings; validate ok; registered).
Where the generator-level bounds fail, for the record: they bound a kernel restricted to one generator after a
transverse smearing; the vacuum-polarisation kernel needs the unrestricted two-point kernel near the diagonal of
M x M. Nothing is lost, because the bulk form is stored.

## Y3. Order-four anomaly and sixteen components (op.order-four-anomaly-and-sixteen)
Routes: (1) the problem's: charges of the sixteen under the store's order-four element; (2) from the walls: a
fixed-point count on RP^5 (needs an index theorem, not in the store); (3) mine: charge-sum arithmetic for the Z4 and
the U(1) that contains it. Chosen (1) + (3), as far as stored objects go. Nothing filed (the sibling files the
negative clauses; see its P2; I add no proposal so that nothing is filed twice).
- computed (exact, Cl(10,0), work/C2A/y3/y3.py): the pseudoscalar omega of the ten Majoranas of the slot-module
  premise has omega^2 = -1, anticommutes with every generator, commutes with every bivector (so with the whole
  gauge chain, which lies in the even subalgebra) and anticommutes with five-blades. On the slot module omega is
  a unit times the grading, so it is a scalar on each chirality half: uniform charge 1 (mod 4) on all sixteen.
- consequence (K3b fired in part): every order-four candidate commuting with the chain is a function of the grading
  (the Klein twist P+ + I P-, and omega); the charges carry no information about the content beyond "all odd".
- computed: with X = 5 - 2N on N = 0, 2, 4 (1 + 10 + 5 components; e^{I pi X/2} = omega up to the unit):
  sixteen: all X = 1 mod 4, sum X = 0, sum X^3 = 0, count 16 = 0 mod 2, 4, 16;
  fifteen (no N = 0): all X = 1 mod 4, sum X = -5, sum X^3 = -125, count 15 odd.
  So every level of the consistency condition separates 15 from 16 through the PARITY of the number of components of
  odd charge; the mod-16 refinement is not needed for this bit. argued: the weakest sufficient import is "the index
  of the Dirac operator on a closed spin four-manifold is even" (two zero modes per Weyl field on K3, so the phase
  I^(2k) = (-1)^k must be 1; Ibanez and Ross, memory), not the bordism group Z16. Both are literature; none is in
  the store; no necessary condition is DERIVED from stored objects (K3c).
- computed: a five-blade (the Majorana-type element, the 126 direction) is odd under omega: a Majorana term for the
  singlet breaks the order-four element to its square. So with the stored Majorana premise the Z4 is not a symmetry
  of the full theory and the anomaly argument applies only above that scale (argued). Same conclusion as the
  sibling's (ii), reached independently.
- not decided: whether the descent preserves omega (no stored statement ties the descent to the internal Cl(10)).
Verdict for the success clause: the second branch, "it does not constrain the content beyond a parity", is what
the store's own objects give; the positive branch rests on one imported index statement (decision below).

## Y4. Short tests (findings only)
- C7/N4 (so(10) level 4 in su(16) level 1; T-phases). computed arithmetic: c = 4*45/12 = 15; weight of the 16 is
  (45/8)/12 = 15/32 = 255/544, the su(16) level-one fundamental weight; vacuum T-phase exp(-2 pi I c/24) is trivial
  iff 24 | c: c = 16 n_g gives 3 | n_g, c = 15 n_g gives 8 | n_g. The sector of weight 15/32 has a phase of order 32
  at n_g = 3, so T is not trivial beyond the vacuum sector. No new condition from T beyond 24 | c; the S-matrix at the
  self-dual point was not computed. No result dropped out; no open problem warranted beyond N4 as it stands.
- R12/C8 (helicity as boost weight). Kill fired (argued from the stored one-liner): the "helicity" of
  synthesis.kasner-curvature-wall-is-negative-weight-helicity is theta ^ d theta of a coframe (a twist, Frobenius
  type), not a spin helicity; the two results share a word and the reading "boost weight", not an object. No link.
- C5 (wall rungs against descent rungs). Kill fired: the wall rung summand is a trivial bundle with a form; no
  state is stored on a collar. As algebra only: k rungs give Cl(k,k) = M_{2^k}(R), a k-mode Fock space, and
  descent-lift counts one rung of record per mode; nothing forces the two to be the same modes. With Y2: the
  definite L^5(4) wall needs five rungs, Cl(5,5) = M_32(R); the 32 equals the dimension of the slot module, flagged as
  a coincidence (Cl(10,0) is a different real form of the same matrix algebra; no map is stored).
- N5 (walls by parallel-tractor type). First exact computation (linear algebra, not filed): at the zero set of a
  scale the collar form sigma^2 g^{-1} vanishes on the whole cotangent space, so a completion in the stored sense
  must contain T*M as a totally isotropic subspace of T*M + R^{2k} with signature (p + k, q + k); the Witt index
  min(p, q) + k must be at least p + q, so k >= max(p, q): three rungs for a (1,3) side, not one. The tractor
  bundle (one hyperbolic plane, Witt index 2 in signature (2,4)) is NOT a completion of the total-radical wall in
  the stored sense; it completes the conformal class, not the form sigma^2 g^{-1}. The suggested open problem should
  be restated: either change what "restricts to G along the wall" means for weighted forms, or the answer is
  k = max(p, q). An open problem is warranted only in the restated form.
- N6 (recovery maps). First computation (exact, two lines): for the expectation E(x) = (x + alpha(x))/2 of an
  order-two automorphism, the Petz map with an invariant reference state is the inclusion, and a state is recovered
  iff it is alpha-invariant, iff the relative entropy to the reference is unchanged by E. On a matrix factor with
  alpha = Ad(sigma_3) this is "diagonal states only". This restates the stored one-way property; an open problem
  is warranted only if a stored state of an evicted window is not parity-invariant (none found).
- N7 (edge-mode reading of the vector weight). computed from the stored weights: the Sakharov weights are
  -4 s^2 (-1)^(2s) per field of helicity s (0, +1, -4 for s = 0 conformal, 1/2, 1; 8 per graviton in the stored
  supertrace is s^2 = 4 times the vector's 2). So the vector's -4 is the pure helicity count with remainder ZERO:
  no edge term is visible in the attachment-module character. Kabat's 2 - 6 is the same number split against two
  minimally coupled scalars. Equivalent form: a helicity-s state weighs like a scalar with
  xi_R = (1 + 2 s^2)/6 (1/6, 1/2, 3/2 for s = 0, 1, 2). No open problem warranted; see the link below.

## Unexpected links
- Y2 to the generations/standard-model side: the obstruction that decides four against five rungs is the same
  Sq^2 / "w_2-type" parity that distinguishes d = 4 from d = 8 (quarter turn against eighth turn). The bridge file
  noted that L^5(4) carries a Z8 structure for the rotor lift; the rung obstruction disappears exactly at Z8.
  argued, one data point each side.
- Y2 to the success clause of op.wall-class-invariant: the datum is rho(a)^2 cup x for 2a = beta x, a secondary
  class invisible to x, beta x, (beta x)^2 and complex K-theory. This supports "k is a function of the ring data
  of a", against the alternative "a pair with isomorphic data and different k". argued.
- Y1 to interior/horizon results: the transport rotors cancel from the leading vacuum-polarisation kernel exactly as
  the field strength cancels from the leading null singularity in the stored generator result; and the mechanism
  that removes the Weyl term (gamma^mu Riem(e_mu ^ xi) = Ricci) is the protraction identity, the same contraction
  that makes the stored type-D Schwarzschild field strength invisible to the Ricci map. computed.
- Y1 to X3/C1 (xi_R): the degree-four part of the kernel has Ricci and scalar-curvature coefficients only; the
  scalar-curvature coefficient enters through V(x,x), the same place a curvature coupling of a scalar would enter.
  Whoever fixes xi_R for the rung field fixes the analogous degree-two coefficient there. argued.
- N7 to C1: xi_R = 1/2 is the value at which a scalar weighs like a vector helicity state; the earlier run found
  xi_R = 1/2 gives n_g = 4 in the Sakharov zero. computed arithmetic, no structure claimed.

## Decisions for Leon
1. Y2: import as one Fact the classical inputs (T) of the rung-count proposal (Steenrod squares with the Cartan
   formula; Chern classes with the splitting principle; cohomology of the Thom space of a line bundle), or keep the
   lower bound five conditional on them as filed. Recommendation: import; they are textbook (Milnor and Stasheff),
   and the earlier decision imported the Atiyah-Hirzebruch filtration on the same footing. Alternative single import:
   integrality of the Chern character with the Thom isomorphism of K-theory (second route in the check).
2. Y2: whether to record the literature on the level of projective spaces (Pfister and Stolz; Stolz) as prior art
   after checking it against the sources; it would settle L^7(4) (5 or 6) and the periodicity question.
3. Y1: import the three scaling-degree rules (SD) as a Fact (Brunetti and Fredenhagen 2000), or extend the existing
   imported extension-theorem Fact with them. Recommendation: extend the existing Fact.
4. Y1: whether clause (v) of the stored vacuum-polarisation result should be split: first half (degrees, leading
   coefficient) now cites the new result; second half (reduction to Z_3 by covariance) stays argued and needs the
   Hollands and Wald scaling axiom as an import. Maintainer edit plus an import decision.
5. Y1: the hypothesis "vanishing torsion" is stated in the new result; the stored bulk theorems use the spin
   connection of the derived metric without saying so. Whether to add the same sentence there.
6. Y3: whether to import an index statement at all. If yes, the parity statement (even index on closed spin
   four-manifolds) already separates fifteen from sixteen; the Z16 bordism statement is stronger than needed for
   that bit. And whether the Majorana premise, which breaks the order-four element, is to be read as making the
   argument inapplicable below its scale.
7. N5: restate or drop the suggested open problem on total-radical walls (the one-rung tractor answer is excluded
   in the stored sense by a Witt-index count).
