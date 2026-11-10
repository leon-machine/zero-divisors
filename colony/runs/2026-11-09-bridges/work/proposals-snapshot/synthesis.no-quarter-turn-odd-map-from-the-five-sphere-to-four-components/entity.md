---
id: synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components
kind: claim
version: 1
title: 'No quarter-turn-odd map from S^5 to four components: a cup-one square, given Steenrod'
status: proved
region: synthesis
subject: walls
tags: [classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-09-bridges
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-bridges
review: draft
derivations:
- name: main
  uses:
  - synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_quarter_turn_rotor_and_quaternion_fibre
- kind: check
  ref: check.py::check_product_cell_complex
- kind: check
  ref: check.py::check_higher_diagonal_on_the_factors
- kind: check
  ref: check.py::check_higher_diagonal_on_the_product
- kind: check
  ref: check.py::check_fibre_class_is_an_integral_cocycle
- kind: check
  ref: check.py::check_cup_one_square_is_the_top_class
- kind: check
  ref: check.py::check_chain_level_section_exists
- kind: check
  ref: check.py::check_controls_other_orders_and_trivial_action
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial
  - synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height
extraction:
  open_problem: op.wall-class-invariant
  note: >-
    Derives, by exact computation in the stored cell model, the one obstruction that the lower bound of five rungs
    on a definite side of the wall with cross-section L^5(4) needs: there is no continuous map from the five-sphere
    to the punctured four-space that changes sign under the quarter turn. Intended citation, for the maintainer:
    the proposal synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five proves the
    index form of the rung count and the upper bound five, and proves this non-existence statement (its clause
    (4)) given three classical theories (Steenrod squares with the Cartan formula, Chern classes with the splitting
    principle, the cohomology of a Thom space); once that proposal is accepted its clause (4) can cite the present
    result in place of those. This entity does not cite it, because a proposal cannot cite a proposal. What is
    proved outright here: the cochain identities of clauses (2) and (3) and the algebraic non-existence statement
    of clause (4). What is conditional: clause (5), the topological statement, on the stated background (G) of
    the cited theorem, (P) (cells of a product) and one classical theorem (S) (the cup-one square is a natural
    operation), which is cited from memory and is not in the store; importing (S) as a Fact is a maintainer
    decision. (S) belongs to the first of the three theories; (P) is additional background. No Cartan formula, no Chern classes, no Thom space, no homotopy group of a sphere and no stability
    of the squaring operations is used. Prior art, cited from memory and not checked: N. E. Steenrod, "Products
    of cocycles and extensions of mappings", Annals of Mathematics 48 (1947), which introduces the cup-i products
    and classifies maps of a complex of dimension n + 1 to the n-sphere by the square of degree two; Steenrod and
    Epstein, "Cohomology Operations" (1962), for the construction on regular cell complexes by equivariant acyclic
    carriers; the level of projective spaces (Pfister and Stolz, Comment. Math. Helv. 62 (1987) 286-291; Stolz, Comment.
    Math. Helv. 64 (1989) 661-674), which, as quoted in secondary sources, contains the statement proved here
    (level 5 at m = 3); primary texts not read. Graph note: the past cone of this entity contains
    synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory through the cited theorem, but only
    clauses (2) and (3) of that theorem are used here, and they do not depend on it; the inherited dependence is
    not a real one. Transport-absent: classical topology applied to the store's walls.
outside_ga:
  kind: other
  why: 'The statement is algebraic topology: a cohomology operation on a finite cell complex. The quarter turn (a rotor), the fibre (the unit sphere of the even subalgebra of Cl(3,0), on which the deck transformation acts as the rotor of a full turn, -1) and the cells are written in geometric algebra; the chain-level computation is integer arithmetic on cells and has no geometric-algebra form.'
---

## formal
Let $J(v) = v \cdot B$, $B = e_{1}e_{2} + e_{3}e_{4} + e_{5}e_{6}$ in $\Cl(6,0)$, be the quarter turn, $G = \langle g \rangle \cong \Z_{4}$ acting on $S^{5}$ by $g = J$, $\Sig_{2} = L^{5}(4) = S^{5}/G$, with the cell complex $C$ (cells $g^{a}e_{k}$, $0 \leq k \leq 5$), the diagonal $\Delta_{0} := \Delta$, the invariant cochains $\varepsilon_{k}$ and the classes $x$, $u$ of Theorem \claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure}, whose background (G) is assumed where stated. Let $\HH$ be the even subalgebra of $\Cl(3,0)$, a four-dimensional real space on which $q\tilde q$ is a positive definite scalar form, $S^{3}$ its unit sphere, and let $g$ act on $\HH$ by $-1$ (the rotor of a full turn). Let $D$ be the cell complex of $S^{3}$ given by the same formulas for the group $\{1, T\}$ of order two, $T = -1$ (cells $T^{b}d_{q}$, $0 \leq q \leq 3$), $P = C \otimes D$ the product complex with $g$ acting by $g \otimes T$ and $\partial(c \otimes d) = \partial c \otimes d + (-1)^{\deg c}c \otimes \partial d$, and $M = (S^{5} \times S^{3})/G$ with projection $p : M \to \Sig_{2}$. Write $N = 1 + g + g^{2} + g^{3}$, $N' = g + g^{2} + g^{3}$ on $C$ and $N = 1 + T$, $N' = T$ on $D$, $t$ for the exchange of the two factors of a tensor square, and for a mod-2 cochain $a$ and a map $\Delta_{1}$ of degree $+1$ into the tensor square, $a \cup_{1} a := (a \otimes a)\Delta_{1}$.

Background assumed in clause (5) only. (G): as in the cited theorem. (P): the cellular chain complex of a product of two cell complexes is the tensor product of theirs with the boundary above, and the projection to a factor induces the chain map that keeps $c \otimes d$ for $d$ a vertex (sending it to $c$) and kills the other cells. (S), cited from memory and not in the store: there is a map $Sq^{2} : H^{3}(X; \Z_{2}) \to H^{5}(X; \Z_{2})$, defined for cell complexes $X$ and natural for continuous maps, such that when $X = Y/G$ for a finite regular cell complex $Y$ with a free cellular action of a finite group $G$, and $\Delta_{0}, \Delta_{1}$ are $G$-equivariant maps from the cellular chains of $Y$ to their tensor square, carried by closed cells (the value on a cell lies in the tensor square of the chains of its closure), with $\Delta_{0}$ a chain map preserving the augmentation and $\partial\Delta_{1} + \Delta_{1}\partial = \Delta_{0} + t\Delta_{0}$ modulo $2$, then $Sq^{2}[a] = [a \cup_{1} a]$ for every invariant mod-2 cocycle $a$ of degree $3$. This is Steenrod's theorem in the form obtained from the acyclic-carrier construction on regular complexes by carrying the deck group along; that passage is part of the assumption (S) and is not derived here.
\begin{enumerate}
\item \emph{(Odd maps are sections; proved.)} Continuous maps $F : S^{5} \to \R^{4} \setminus \{0\}$ with $F(J(v)) = -F(v)$ correspond, on identifying $\R^{4}$ with $\HH$ and dividing by the length, to continuous sections $s$ of $p$ ($p \circ s$ the identity), $s[v] = [v, F(v)]$.
\item \emph{(The higher diagonal; proved.)} Define $\Delta_{1}$ on $C$, equivariantly, by $\Delta_{1}(e_{0}) = 0$ and
\[
\Delta_{1}(e_{1}) = e_{1} \otimes e_{1}, \quad \Delta_{1}(e_{2}) = Ne_{1} \otimes e_{2}, \quad \Delta_{1}(e_{3}) = e_{3} \otimes e_{1} + N'e_{1} \otimes e_{3},
\]
\[
\Delta_{1}(e_{4}) = Ne_{3} \otimes e_{2}, \quad \Delta_{1}(e_{5}) = e_{1} \otimes e_{5} + N'e_{3} \otimes e_{3} + e_{5} \otimes e_{1},
\]
and on $D$ by the same formulas up to $d_{3}$. Then on $C$ and on $D$, modulo $2$, $\partial\Delta_{1} + \Delta_{1}\partial = \Delta_{0} + t\Delta_{0}$, and $\Delta_{0}$, $\Delta_{1}$ are carried by closed cells. On $P$, with the two middle factors interchanged, $\Delta_{0}^{P} = \Delta_{0}^{C} \otimes \Delta_{0}^{D}$ and $\Delta_{1}^{P} = \Delta_{1}^{C} \otimes t\Delta_{0}^{D} + \Delta_{0}^{C} \otimes \Delta_{1}^{D}$ are $G$-equivariant, carried by closed cells, and satisfy the same identity modulo $2$ on all $48$ orbits of cells.
\item \emph{(The fibre class and its square; proved.)} The $G$-invariant integral cochain $\theta$ of $P$ with
\[
\theta(g^{a}e_{0} \otimes T^{a}d_{3}) = 1, \qquad \theta(g^{a}e_{1} \otimes T^{a}d_{2}) = 1, \qquad \theta(g^{a}e_{2} \otimes T^{b}d_{1}) = -1,
\]
and zero on the other cells of dimension $3$, is a cocycle with value $1$ on the fibre sphere $(1 + T)(e_{0} \otimes d_{3})$. With $a = \theta \bmod 2$, $\pi$ the chain map of (P) and $\beta$ the invariant cochain equal to $1$ on the cells $g^{a}e_{4} \otimes T^{a}d_{0}$ and to $0$ on the other cells of dimension $4$,
\[
a \cup_{1} a = \pi^{*}\varepsilon_{5} + \delta\beta \pmod 2 ,
\]
and neither $a \cup_{1} a$ nor $\pi^{*}\varepsilon_{5}$ is a coboundary modulo $2$ of an invariant cochain. The same class results from the other product formula $\Delta_{1}^{C} \otimes \Delta_{0}^{D} + t\Delta_{0}^{C} \otimes \Delta_{1}^{D}$ and from the transposes $t\Delta_{1}^{P}$.
\item \emph{(No section at chain level; proved.)} There is no triple $(\sigma, h_{0}, h_{1})$ of $G$-equivariant maps with: $\sigma : C \to P$ an integral chain map with $\pi\sigma$ the identity; $h_{0} : C \to P \otimes P$ of degree $1$ with $\partial h_{0} + h_{0}\partial = \Delta_{0}^{P}\sigma + (\sigma \otimes \sigma)\Delta_{0}^{C}$ modulo $2$; $h_{1}$ of degree $2$ with $\partial h_{1} + h_{1}\partial = \Delta_{1}^{P}\sigma + (\sigma \otimes \sigma)\Delta_{1}^{C} + h_{0} + t h_{0}$ modulo $2$. Chain maps $\sigma$ with $\pi\sigma$ the identity do exist: the obstruction is not visible to the chain complexes without their diagonals.
\item \emph{(No odd map; proved given (G), (P) and (S).)} $Sq^{2}(\rho\,[\theta]) = p^{*}(xu^{2})$ in $H^{5}(M; \Z_{2})$, $\rho$ the reduction modulo $2$. Hence $p$ has no continuous section, and there is no continuous $F : S^{5} \to \R^{4} \setminus \{0\}$ with $F(J(v)) = -F(v)$; nor, by restriction to the first three planes, any continuous $F : S^{2n+1} \to \R^{4} \setminus \{0\}$ odd under the quarter turn, $n \geq 2$.
\item \emph{(Controls; computed.)} For the cyclic group of even order $d$ acting on $S^{5}$ by the turn through $2\pi/d$ in every plane and on $\HH$ by $-1$, the same formulas (with $N$, $N'$ for that group; the identity of (2) is verified for $d = 2, 4, 6, 8, 12, 16$) give: for $4 \mid d$ the cocycle $\theta_{d}$ with $-d/4$ in place of $-1$, and $a \cup_{1} a$ cohomologous to $\pi^{*}\varepsilon_{5}$ for $d = 4, 12$ and to zero for $d = 8, 16$; for $d = 2, 6$ the cocycle equations force an even value on the fibre sphere (the obstruction is then primary). With $G$ acting trivially on $\HH$ (the product $\Sig_{2} \times S^{3}$, which has sections) the square of the fibre cocycle is a coboundary, and over $S^{3}$ in place of $S^{5}$ it is a coboundary. The vanishing for $d = 8, 16$ is the vanishing of this obstruction only; it does not construct a map.
\end{enumerate}
Not derived: (G), (P), (S). The Cartan formula, Chern classes, the cohomology of Thom spaces, homotopy groups of spheres and the stability of squaring operations are not used.

## technical
The question whether four components suffice is a secondary obstruction, invisible to the cohomology ring of the lens space (the stored classes $x$, $2y$, $(2y)^{2} = 0$) and to its complex K-theory. Here it is made a primary computation by passing to the total space $M$ of the sphere bundle whose sections are the odd maps. $M$ is a quotient of $S^{5} \times S^{3}$ by a free cellular action, with $48$ orbits of cells, and its fibre sphere carries an integral class $\theta$ because the Euler class $(2y)^{2}$ vanishes. A section would pull $\theta$ back to the lens space, which has no integral class of degree three, so it would pull the cup-one square of $\theta$ back to zero; but that square is the pull-back of the top mod-2 class of the lens space, which a section pulls back to itself. The square is computed from an explicit chain homotopy $\Delta_{1}$ between the stored diagonal and its transpose, found for the stored complex and verified cell by cell, and only one pair of cells contributes: $(e_{2} \otimes d_{1}) \otimes (e_{2} \otimes d_{1})$, with coefficient $(d/4)^{2}$ for the group of order $d$, which is why the obstruction is present for $d \equiv 4$ and absent for $d \equiv 0$ modulo $8$ in the cases computed. What the computation cannot do by itself is compare an arbitrary continuous section with the chain-level diagonals: clause (4) shows that the algebra forbids any section that comes with the two homotopies $h_{0}, h_{1}$, and the classical theorem (S) is exactly the statement that every continuous map comes with them (naturality of the cup-one square). That is the one step where a general theorem remains, since no finite computation ranges over all continuous maps. With the index form of the rung count (in a proposal not yet accepted, named in the extraction note) the statement says that a wall with cross-section $L^{2n+1}(4)$, $n \geq 2$, twisted dying line and definite physical side needs at least five rungs. Transport-absent.

## lay
A sphere in six dimensions can be turned by a quarter turn in three planes at once. Is there a rule that assigns to every point of the sphere four numbers, never all zero and varying continuously, such that all four change sign when the point is moved by the quarter turn? Five numbers can be arranged, by an explicit formula given in a companion result; this result shows that four cannot, for the quarter turn on the five-dimensional sphere and on its higher-dimensional analogues. The proof is a finite calculation with whole numbers on a decomposition of the sphere into cells that the collection already holds, together with one classical theorem of topology from 1947 that the collection does not contain and that is stated as an assumption: a certain squaring rule for cell-by-cell data is respected by every continuous map. The companion argument needs three bodies of classical theory; this one needs one theorem from the first of them, without the product formula for the squares, and nothing from the other two. The calculation also shows why the answer is delicate: the same question for an eighth of a turn meets no such obstacle. The result is classical topology applied to the collection's walls; it is what makes five the exact number of rungs for one family of walls once the companion result is accepted.

## one-liner
Given standard cellular background and Steenrod's theorem that the cup-one square is a natural operation (cited, not stored), there is no continuous $F : S^{5} \to \R^{4} \setminus \{0\}$ with $F(J(v)) = -F(v)$ for the quarter turn $J$: on the sphere bundle $(S^{5} \times S^{3})/\Z_{4}$, in the stored cell model with an explicit higher diagonal, the cup-one square of the integral fibre cocycle is the pull-back of the top class $xu^{2}$ of $L^{5}(4)$, which no section allows; the cochain identities and a chain-level non-existence statement are proved outright.
