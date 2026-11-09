# Attack C3A (constructive), run 2026-11-09-bridges, cluster C3, target Z1

Target: derive, by exact finite computation in the store's cell model, the obstruction showing there is no map
F : S^5 -> R^4 minus 0 with F(Jv) = -F(v) (J the quarter turn), with a background strictly smaller than (T) of the
proposal synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five; or name the exact step
where a finite computation cannot replace the general theorem.

## Pre-registered kill conditions (written before any computation)
Route chosen (R3 below): the sphere bundle M = (S^5 x S^3)/Z4 (g acting by J on S^5 and by -1 on S^3), whose
sections are the odd maps. Cell model: the stored Z4 complex of S^5 tensored with the antipodal complex of S^3.
Plan: an explicit integral 3-cocycle theta on M (fibre generator), a higher diagonal Delta_1 (chain homotopy from the
diagonal to its transpose) on the product complex built from the stored diagonal, and the cup-1 square
theta cup_1 theta mod 2 in degree 5, compared with p^*(eps_5) (the pull-back of the generator x u^2 of H^5(L;Z2)).
If Sq^2(rho theta) = p^*(x u^2), a section s gives x u^2 = s^* p^*(x u^2) = Sq^2 rho (s^* theta) = 0 because
H^3(L;Z) = 0 (stored), a contradiction.
- K1 (route dead): theta cup_1 theta is cohomologous mod 2 to a class with no p^*(eps_5) part (0 or theta.u only).
  Then this route does not see the obstruction and I say so.
- K2 (computation or argument wrong): the same code for the group of order 8 (g acting by -1 on S^3) gives the same
  obstruction as order 4. Theory (C2A clause (5), C2B) predicts none at order 8; if K2 fires nothing is filed.
  Further controls fixed now: order 2 (projective space): no integral theta with fibre value 1 may exist (the
  obstruction is primary); base S^3 instead of S^5 (L^3(4), stored k = 3 < 4): nothing in degree 5.
- K3 (not well defined): the value depends on the choice of Delta_1 among the equivariant solutions carried by
  closed cells. Then the background statement (S) below is not enough as I state it.
- K4 (RUN.md's kill): the argument from the computed cocycle to non-existence needs, beyond (G), anything as strong
  as (T): the Cartan formula, Chern classes, Thom isomorphism, homotopy groups of spheres, or stability of Sq.
  Expected addition, declared now: (S) Steenrod's theorem that a -> a cup_1 a on mod-2 cocycles of degree n is a
  cohomology operation natural for continuous maps (Sq^{n-1}), computed on a regular cell complex with a free
  cellular action by any equivariant (Delta_0, Delta_1) carried by closed cells. If more than (S) is needed, each
  item is named; if (S) itself is judged as strong as (T), K4 fires and the result is findings only.

## Routes considered
- R1 (RUN.md's first suggestion): Sq^2 on H^3(L;Z2) by cup-1 on the stored complex (x u -> x u^2). Delivers a
  finite computation, but Sq^2(x u) = x u^2 also holds on L^5(8) where there is no obstruction, so it cannot be the
  whole obstruction: one still needs the Thom space or the mapping cone of L -> CP^2 -> S^4 and stability of Sq
  (commutation with the coboundary of a cone), plus a cell model of the map to CP^2. More background, not less.
- R2 (RUN.md's second suggestion): the equivariant obstruction tower cell by cell. The secondary obstruction is one
  element of pi_4(S^3) = Z2 (the indeterminacy vanishes because H^3(L;Z) = 0). Needs pi_4(S^3) and an invariant
  that detects the Hopf class on an explicit map S^4 -> S^3, and the identification of the obstruction cocycle:
  background at least as strong as (T).
- R3 (mine, chosen): move the question to the total space M of the sphere bundle, where the secondary obstruction
  becomes a primary operation on an explicit finite complex: Sq^2 of the reduction of the integral fibre class.
  Needs only naturality of Sq^2 under the section. No Chern classes, no Thom space, no Cartan formula, no homotopy
  groups, no stability.
- R4 (another subject): real K-theory of L^5(4) (order of 4L). Not in the store (the stored K-ring is complex and
  does not see it); a heavy import.
Reason for R3: the only general theorem it uses is the one that cannot be avoided in any route (an arbitrary
continuous F must be compared with a chain-level structure), and everything else is integer arithmetic on a complex
with 48 cell orbits.

## Status: result established and filed; no kill fired
Proposal: synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components
(check4 exit 0, 0 errors, 0 other findings, log in verify/final/; validate ok; registered with propose_claim;
coverage.yaml restored). Check runtime well under a second. Scratch: work/C3A/explore.py (first exploration, with a
linear solver for the higher diagonal and an integer-kernel search for theta), work/C3A/filed (copy of the proposal).

### What was done
1. Sections. Odd maps F : S^5 -> R^4 \ 0 (R^4 = the even subalgebra of Cl(3,0), g acting by the rotor -1) are the
   sections of p : M = (S^5 x S^3)/Z4 -> L^5(4). proved (elementary).
2. Higher diagonal. On the stored complex C (cells e_0..e_5) an explicit Delta_1, found by solving the linear system
   cell by cell over F_2 with the carrier constraint and then written in closed form:
   e_1: e_1(x)e_1; e_2: N e_1(x)e_2; e_3: e_3(x)e_1 + N' e_1(x)e_3; e_4: N e_3(x)e_2;
   e_5: e_1(x)e_5 + N' e_3(x)e_3 + e_5(x)e_1 (N' = g + g^2 + g^3 on the first factor).
   bd Delta_1 + Delta_1 bd = Delta_0 + t Delta_0 mod 2, carried by closed cells; same formulas for the antipodal S^3
   (order 2) and, verified, for orders 6, 8, 12, 16. Product formula on C (x) D verified on all 48 orbits.
   proved (finite, complete check).
3. The class. theta = 1 on g^a e_0 (x) T^a d_3 and g^a e_1 (x) T^a d_2, -1 on all e_2 (x) d_1 cells: integral cocycle,
   value 1 on the fibre. a cup_1 a (a = theta mod 2) = 1 on e_4 (x) T^b d_1 only, = pi^* eps_5 + delta(beta) with beta
   explicit. One pair of cells survives: (e_2 (x) d_1) (x) (e_2 (x) d_1), coefficient (d/4)^2 for order d.
   proved (cochain identities, complete check); four choices of higher diagonal give the same cochain (K3 not fired).
4. Chain-level no-go. No equivariant chain section sigma of C -> C (x) D together with homotopies h_0 (diagonals)
   and h_1 (higher diagonals): pure algebra from 3 plus "an invariant integral 3-cocycle of C is zero" and
   "eps_5 is not a coboundary mod 2". proved, no background. A chain section without the homotopies exists
   (explicit phi: e_0 -> d_0, e_1 -> d_1, e_2 -> 2 d_2, e_3 -> (1 - T) d_3), so the obstruction is invisible to the
   chain complexes without their diagonals.
5. Topological statement: no odd map S^5 -> R^4 \ 0 (and none from S^{2n+1}, n >= 2). proved GIVEN (G), (P), (S).
6. Controls (computed): order 8, 16: square is a coboundary; order 12: obstruction; orders 2, 6: no integral fibre
   class (primary obstruction); trivial action on the fibre and base S^3: nothing. All as pre-registered (K2 not
   fired; the order-12 and order-16 values were predictions of C2A's parity n = -d/4, not fitted).

### Background still assumed (exactly)
- (G): the background of the stored cohomology theorem, unchanged (cellular = singular, invariant cochains for a
  free cellular action). Its obstruction-theory part and its comparison-theorem/Kunneth part are NOT used here.
- (P), an addition, elementary: cellular chains of a product are the tensor product; the projection to a factor
  induces the obvious chain map.
- (S), the one real addition: Steenrod's theorem that a -> a cup_1 a is a cohomology operation (Sq^2 on degree 3),
  natural for continuous maps, computed on the quotient of a regular cell complex by a free cellular action from any
  equivariant (Delta_0, Delta_1) carried by closed cells. Cited from memory (Steenrod 1947; Steenrod and Epstein
  1962), not in the store.
- Removed relative to (T): the Cartan formula, additivity, Sq^2 a = a^2; all of (T2) (Chern classes, product
  formula, splitting principle); all of (T3) (Thom space, H^*(CP^2)). Also not used: homotopy groups of spheres,
  stability of Sq, K-theory.
- Candid qualification on "strictly smaller": (S) is not a logical subset of (T1). (T1) lists axioms of Sq^2;
  (S) is the cochain-level definition of Sq^2 on cell complexes plus naturality. It is one theorem about one
  operation in place of three theories, and the Cartan formula is gone, but the cochain formula is something (T1)
  did not state. K4 judged not fired; the referee may weigh this differently.

### The exact step where finite computation stops
Clause (4) isolates it: the algebra forbids every chain-level section that carries the homotopies h_0, h_1. What no
finite computation supplies is that an ARBITRARY continuous section induces a chain map with such homotopies
(naturality of the cup-one square under continuous maps; a cellular approximation of the section need not respect
closed-cell carriers, so the acyclic-carrier argument that handles Delta_0, Delta_1 does not handle the section).
That statement is (S) and nothing more.

### What failed or was not done
- R1 (Sq^2(x u) = x u^2 on L alone) was not pursued: it holds at order 8 too, so it is not the obstruction.
- No closed-form Delta_1 for all degrees and no proof of the factor identity for general order: verified for
  degrees <= 5 and orders 2, 4, 6, 8, 12, 16 only (all that the result needs is order 4 and 2).
- Order 8: vanishing of this obstruction does not construct a four-component odd map on L^5(8); C2B's claim that
  one exists stays argued.
- L^7(4) (5 or 6) not touched: the next obstruction lives in degree 6/7 with a fibre S^4 and needs cup-2.
- The general-wall form x cup rho(a)^2 stays conjectural; the computation here suggests the mechanism (the square
  of the coefficient -d/4 of the fibre cocycle on the e_2 (x) d_1 cells) but proves nothing beyond the lens family.

## Unexpected links
- The secondary obstruction is literally a cup-one square in the store's own cell model, with one surviving pair of
  cells; the integer -d/4 that C2A found as a Chern number on a Thom space appears here as the coefficient the
  cocycle equations force on theta. Two unrelated routes, same parity.
- Steenrod's 1947 paper introduced cup-i products for exactly this kind of question (maps of an (n+1)-complex to
  S^n); the result is that paper's method run on the store's complex.
- The same machinery (higher diagonals on the stored complex) would give Sq^1, Sq^2 on the lens spaces and their
  sphere bundles generally; a Delta_2 would be needed for L^7(4).

## Decisions for Leon
1. Whether to import (S) as a Fact (maintainer-only). Recommendation: yes, as one Fact "Steenrod's cup-one square
   is a natural operation, computed from carried equivariant higher diagonals", cited to Steenrod 1947 and Steenrod
   and Epstein 1962 after checking the references (they are cited from memory here). It is far smaller than (T).
2. Whether (P) joins the stated background (G) of the cohomology theorem or stays a hypothesis of this claim only.
   Recommendation: leave it in this claim.
3. After acceptance: restate clause (4) of
   synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five to cite this result in place
   of (T) (its Thom-space argument can stay as a second route, or be dropped with (T)). This claim could not cite
   that proposal; the extraction note names it as the intended citation.
4. Whether "proved given (G), (P), (S)" is acceptable as status proved with the hypotheses in the statement
   (the precedent is the cohomology theorem itself), or whether it should wait for decision 1.
