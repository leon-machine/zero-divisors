---
id: synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure
kind: claim
version: 1
title: 'Cohomology of the quarter-turn lens spaces from the equivariant cell structure'
status: proved
region: synthesis
subject: walls
tags: [classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-09-three
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-three
review: draft
derivations:
- name: main
  uses:
  - synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_quarter_turn_in_the_algebra
- kind: check
  ref: check.py::check_cell_complex
- kind: check
  ref: check.py::check_diagonal_approximation_is_a_chain_map
- kind: check
  ref: check.py::check_four_group_ring_identities
- kind: check
  ref: check.py::check_cup_products_and_bocksteins
- kind: check
  ref: check.py::check_euler_class_sections
- kind: check
  ref: check.py::check_presented_ring_orders
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial
  - synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height
extraction:
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'The in-statement hypothesis (AH) of clause (6) is now the imported Fact synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory, cited by a uses edge and in the proof, by decision of 9 November 2026; the label (AH) and every clause are kept; the lambda-operations, the spin class and the background (G) stay hypotheses.'
  open_problem: op.wall-class-invariant
  note: >-
    Derivation in the store of the lens-space inputs that
    synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial and
    synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height cited from memory at their version 1 (decision
    of 9 November: derive, do not import, except the Atiyah-Hirzebruch filtration, which is imported as one general
    Fact). What is derived here, on the general background (G) of the formal level: the integral, mod-2 and
    mod-4 cohomology of L^{2n+1}(4) with cup products, from the equivariant cell structure and an explicit diagonal
    approximation; the Bocksteins; the Euler classes of the quarter-turn and half-turn plane bundles; the first
    Stiefel-Whitney class of the flat line; the stable tangent bundle. What is not derived: the spin class q1
    (existence, 2 q1 = p1, stability), which stays a cited hypothesis of the first result; the complex K-ring, which is
    reduced in clause (6) to the Atiyah-Hirzebruch filtration of complex K-theory (AH), a general classical fact
    held as the imported Fact synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory (a uses edge of
    this result; the label (AH) is kept), and is not derived from nothing. Hypotheses discharged (recorded in both
    results at their version 2, which cite this one). In the two-rung result: (L1) in full, by
    clauses (2), (3), (4), (5); the parts of (L2) "orientable iff w1 = 0, spin iff w2 = 0" and "p1 = e^2 for oriented
    plane bundles" are not touched; (L3) holds given (AH), by clause (6). In the lens-space K-theory result: the use
    of (L3) (Sq^1 = 0 on classes lifting to Z4, to get x^2 = 0) is replaced by the direct computation x^2 = 0 of
    clause (3), and Sq^1 = 0 on these spaces is clause (4) given the identification of Sq^1 with the mod-2 Bockstein;
    (L2) holds given (AH), by clause (6); (L1) there (lambda-operations) is not touched. So after this result the two
    stored results are conditional on: the spin class (first result), the general K-theory facts (AH) (second result; last
    sentence of the first result's clause (4)) and the lambda-operations (second result only), and the background
    (G). On the K-ring, clause (6) gives both halves given (AH): that the relations hold, and that there are no
    others (the count 4^n on both sides, which is what the stored lower bound on the order of 1 - xi uses); without
    (AH) nothing about K-theory is derived here. The stable tangent bundle of clause (5) enters the stored results
    only in remarks on the walls, not in their lower bounds. Prior art, cited from memory: the cell structure and diagonal approximation are textbook (Cartan and
    Eilenberg, Homological Algebra, chapter XII; Hatcher, Algebraic Topology, example 3.41 and section 3.E for
    Bocksteins); for the K-ring, Atiyah (K-Theory, 1967; section number not verified), Kobayashi and Sugawara ("K_Lambda-rings of lens
    spaces L^n(4)", Hiroshima Math. J.; year and pages not verified) for the order four treated here, Mahammed for
    general order, and Kambe (1966), which as far as is known here treats odd primes only. The background (G), the
    spin class and the lambda-operations are hypotheses, not stored entities; deriving them is an open item. The
    filtration (AH) is an imported Fact, cited from memory there and not checked against its sources. Transport-absent: classical
    topology written out for the store's use.
outside_ga:
  kind: other
  why: 'The statement is algebraic topology: cellular chains over the group ring of the cyclic group, cup products from a diagonal approximation, Bocksteins and obstruction classes. The group action, its freeness, the tangent splitting and the sections computing the Euler classes are written in geometric algebra; the chain-level computation is integer linear algebra with no geometric-algebra form.'
---

## formal
Let $J(v) = v \cdot B$ with $B = e_{1}e_{2} + e_{3}e_{4} + \dots + e_{2n+1}e_{2n+2}$ on $\R^{2n+2}$, the quarter turn in every coordinate plane, $G = \langle g \rangle \cong \Z_{4}$ acting on the unit sphere $S^{2n+1}$ by $g = J$, and $\Sig_{n} = L^{2n+1}(4) = S^{2n+1}/G$. Let $\eta$ be the flat oriented plane bundle on which $g$ acts by the quarter turn, $\eta^{2}$ the one on which it acts by the half turn, and $\shL$ the flat real line on which $g$ acts by $-1$, so that $\shL \oplus \shL = \eta^{2}$. Background (G), general and classical, not derived here: cellular chains of a regular cell structure compute singular (co)homology; for a free cellular action the cochains of the quotient are the invariant cochains; cup products are computed by any equivariant chain map $C \to C \otimes C$ preserving the augmentation, in the degrees where $C \otimes C$ is acyclic (comparison theorem); the algebraic K\"unneth theorem (so that $C \otimes C$ has no homology in degrees $0 < k < 2n+1$); the cup product is natural under cellular inclusions; the Euler class of an oriented plane bundle and $w_{1}$ of a line bundle are the primary obstructions to a nowhere-zero section.
\begin{enumerate}
\item \emph{(The action; proved.)} $J^{2} = -1$, $Q(J(v)) = Q(v)$, $v \cdot J(v) = 0$, and $J^{a} - 1$ is invertible for $a = 1, 2, 3$: the action on the sphere is free, and $J(v)$ is a nowhere-zero tangent field.
\item \emph{(The cell complex; proved given (G).)} $S^{2n+1}$ has a $G$-invariant cell structure with one free orbit of cells $g^{a}e_{k}$ in each dimension $0 \leq k \leq 2n+1$, and $\partial e_{2r+1} = (g - 1)e_{2r}$, $\partial e_{2r} = Ne_{2r-1}$, $N = 1 + g + g^{2} + g^{3}$. The complex is exact in degrees $0 < k < 2n+1$.
\item \emph{(Diagonal and cup products; proved given (G).)} The map $\Delta(e_{k}) = \sum_{p+q=k}\Delta_{p,q}$ with $\Delta_{p,q} = e_{p} \otimes e_{q}$ for $p$ even, $e_{p} \otimes g e_{q}$ for $p$ odd and $q$ even, and $\sum_{0 \leq r < j \leq 3} g^{r}e_{p} \otimes g^{j}e_{q}$ for $p, q$ odd, extended equivariantly for the diagonal action, is a chain map preserving the augmentation. With $\varepsilon_{k}$ the invariant cochain equal to $1$ on $e_{k}$: $\delta\varepsilon_{2r-1} = 4\varepsilon_{2r}$, $\delta\varepsilon_{2r} = 0$, and $\varepsilon_{p} \cup \varepsilon_{q} = \varepsilon_{p+q}$ unless $p$ and $q$ are both odd, when it is $6\varepsilon_{p+q}$ (up to the sign convention of the cup product). Hence $H^{2r}(\Sig_{n}; \Z) = \Z_{4}$ for $1 \leq r \leq n$, generated by $y^{r}$, $y := [\varepsilon_{2}]$; $H^{\mathrm{odd}}(\Sig_{n}; \Z) = 0$ below the top degree and $H^{2n+1} = \Z$; $H^{\mathrm{even}}(\Sig_{n}; \Z) = \Z[y]/(4y, y^{n+1})$. With $\Z_{2}$ coefficients every $\varepsilon_{k}$ is a cocycle, $x := [\varepsilon_{1}]$ and $u := [\varepsilon_{2}]$ generate, $x^{2} = 6u = 0$, $xu^{r} = [\varepsilon_{2r+1}] \neq 0$, so $H^{*}(\Sig_{n}; \Z_{2}) = \Lambda[x] \otimes \Z_{2}[u]/(u^{n+1})$ and $u$ is the reduction of $y$. With $\Z_{4}$ coefficients the square of the degree-one generator is $2[\varepsilon_{2}] \neq 0$. For the same formulas with $\Z_{2}$ in place of $\Z_{4}$ (real projective space) the coefficient is $1$ and $x^{2} \neq 0$.
\item \emph{(Bocksteins; proved given (G).)} The integral Bockstein of $x$ is $\beta x = 2y$, of order two. The Bockstein of $0 \to \Z_{2} \to \Z_{4} \to \Z_{2} \to 0$ vanishes on every class of $H^{*}(\Sig_{n}; \Z_{2})$, and every such class lifts to $\Z_{4}$ coefficients. Given the classical identification of $Sq^{1}$ with this Bockstein, $Sq^{1} = 0$ on $H^{*}(\Sig_{n}; \Z_{2})$.
\item \emph{(Bundles; proved given (G).)} $w_{1}(\shL) = x$; the Euler class of $\eta$ is $\pm y$ and that of $\eta^{2} = \shL \oplus \shL$ is $\pm 2y$ (the sign is the orientation convention), of orders four and two; and $T\Sig_{n} \oplus \underline{\R} \cong (n+1)\,\eta$.
\item \emph{(The K-ring; proved given (AH).)} Let (AH) be the imported Fact \claimref{synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory}, in the form of its clauses (i), (iii) and (iv): complex K-theory of a finite complex $X$ is a commutative ring with a multiplicative decreasing filtration $F^{2r}$ (classes vanishing on the $(2r-1)$-skeleton); when $H^{\mathrm{odd}}(X; \Z)$ is zero or torsion-free and concentrated in the top degree, $F^{2r}/F^{2r+2} \cong H^{2r}(X; \Z)$ compatibly with products; and for a line bundle $\ell$ the class $\ell - 1$ lies in $F^{2}$ with image $c_{1}(\ell)$, the Euler class of the underlying plane bundle. Then, with $\chi$ the class of $\eta$ as a complex line and $s = \chi - 1$, the reduced group being $F^{2}$ (since $H^{1}(\Sig_{n}; \Z) = 0$) and $F^{2n+2} = 0$: $\chi^{4} = 1$, $s^{n+1} = 0$, the $4^{n}$ elements $\sum_{r=1}^{n}a_{r}s^{r}$, $0 \leq a_{r} < 4$, are distinct and exhaust the reduced group, and $K(\Sig_{n}) \cong \Z[\chi]/(\chi^{4} - 1, (\chi - 1)^{n+1})$, whose augmentation ideal has order exactly $4^{n}$. In this ring the order of $1 - \chi^{2}$ is $2^{\lfloor (n+1)/2 \rfloor}$ for $1 \leq n \leq 14$ (computed); in particular $2(1 - \chi^{2}) = 0$ for $n = 1, 2$ and not for $n = 3$.
\end{enumerate}
Not derived: the spin class $q_{1}$ with $2q_{1} = p_{1}$; the lambda-operations of K-theory; the background (G). (AH) is not derived either: it is the imported Fact cited in (6).

## technical
Two stored results on the rung count of lens-space walls were conditional on classical facts about the lens spaces $L^{2n+1}(4)$, cited from memory. This result derives those that can be derived at reasonable length, and says exactly which remain cited. The sphere carries a cell structure with one orbit of cells in each dimension, whose chain complex over the group ring alternates multiplication by $g - 1$ and by the norm element; it is the beginning of the standard periodic resolution of a cyclic group. An explicit equivariant diagonal on this complex, checked to be a chain map in integer arithmetic (the formulas repeat with period two in each degree, so finitely many cases cover all), gives the cup products of the quotient by counting terms: all products of the invariant cochains have coefficient one, except a product of two odd-degree cochains, which has coefficient six, the number of ordered pairs $r < j$ among four group elements. So the integral cohomology in even degrees is a truncated polynomial ring on a class of order four, the degree-one class with coefficients mod two squares to zero, and the same count for the group of order two gives coefficient one, the familiar nonzero square on projective space. The Bocksteins are read from the coboundary $4\varepsilon_{2r}$: the integral Bockstein of the degree-one class is twice the generator, and the Bockstein that represents the first Steenrod square vanishes identically. The Euler classes come from explicit sections in the algebra: a vector's first coordinate plane component, which winds once around the first circle, and the reflection $v e_{1} v$, which winds twice and changes sign under the quarter turn. The stable tangent bundle is read from the ambient space, on which the group acts linearly. For K-theory the full ring is not derived from nothing; it is shown to follow from the Atiyah-Hirzebruch filtration, a general property of K-theory held in the store as an imported Fact, together with the cohomology ring derived here, by a count: the presented ring and the K-group both have reduced order $4^{n}$. The spin class used by the first stored result is not derived; it needs the cohomology of the classifying space of the spin group. All of this rests on the general machinery of cellular cohomology, which is stated as background.

## lay
Earlier results in this collection about how many extra directions are needed to repair a wall where the geometry changes signature relied on textbook facts about a family of spaces called lens spaces, quoted from memory. This result works those facts out inside the collection, on top of the general textbook machinery of cell complexes, which is assumed, not derived. A lens space here is a sphere in which each point is identified with its images under a quarter turn. The sphere is cut into pieces that the quarter turn permutes, one family of pieces in each dimension, and the way the pieces fit together, together with a rule for how a piece sits diagonally inside the product of the sphere with itself, determines the algebra of the space's twisting classes by counting. The count shows that the simplest twist class multiplies with itself to zero, unlike on the related space made with a half turn, and that an integer class of order four survives in every even dimension. These are the facts the earlier results used. Two further ingredients they used are not worked out here and remain quoted: a refined class of spinning bundles, and the general theory behind a finer invariant called K-theory, although the particular K-theory fact about lens spaces is reduced to that general theory.

## one-liner
Given standard cellular cohomology and obstruction theory (stated background), from the equivariant cell structure of the sphere under the quarter turn and an explicit diagonal approximation, $H^{\mathrm{even}}(L^{2n+1}(4); \Z) = \Z[y]/(4y, y^{n+1})$, $H^{*}(L^{2n+1}(4); \Z_{2}) = \Lambda[x] \otimes \Z_{2}[u]/(u^{n+1})$ with $x^{2} = 0$, $\beta x = 2y$, the Bockstein of $\Z_{2} \to \Z_{4} \to \Z_{2}$ vanishes, the quarter-turn and half-turn plane bundles have Euler classes $\pm y$ and $\pm 2y$, $T\Sig \oplus \underline{\R} \cong (n+1)\eta$, and the K-ring $\Z[\chi]/(\chi^{4} - 1, (\chi - 1)^{n+1})$ follows from the Atiyah-Hirzebruch filtration; the spin class is not derived.
