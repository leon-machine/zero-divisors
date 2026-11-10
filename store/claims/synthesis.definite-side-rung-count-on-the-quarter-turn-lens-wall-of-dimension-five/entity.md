---
id: synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five
kind: claim
version: 1
title: 'Definite-side rung count on the L^5(4) wall: at most five, five given Steenrod''s theorem'
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
  - synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial@2
  - synthesis.wall-rung-count-is-height-of-dying-line-class@2
  - synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components@1
  - synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side@1
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_explicit_map_into_five_dimensions
- kind: check
  ref: check.py::check_twisted_cochain_complex
- kind: check
  ref: check.py::check_squaring_operation_on_the_thom_space
- kind: check
  ref: check.py::check_square_of_the_second_chern_class
- kind: check
  ref: check.py::check_chern_character_lattice
- kind: check
  ref: check.py::check_upper_bounds_by_blocks
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height
extraction:
  open_problem: op.wall-class-invariant
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Clause (4) now takes the non-existence of a four-component odd map from the stored exact cup-one computation (given the imported Steenrod Fact and the backgrounds (G), (P)) and keeps the Thom-space argument as a second route conditional on (T); clause (3) cites the stored three-rung result for the twisted cohomology; the tameness premise is an assumes edge (decision 12 of 9 November). Version kept: the entity was accepted in the same pass.'
  note: >-
    Works the attack item of op.wall-class-invariant on the exact rung count on a definite side as an equivariant
    index. What is proved outright: the index form (clause 1), the upper bounds by explicit maps written in the
    algebra (clause 2), the twisted cohomology of the stored cell model and the vanishing of the primary obstruction
    to three rungs (clause 3, on the background (G+)). What is
    conditional: the lower bound five (clause 4) rests on the non-existence of a four-component odd map, which is
    clause (5) of synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components: an exact cup-one
    computation in the stored cell model, given Steenrod's theorem (S), now the imported Fact
    synthesis.imported-steenrod-cup-one-square-is-a-natural-cohomology-operation, and the backgrounds (G), (P)
    stated there. The Thom-space argument given here is kept as a second route to the same statement; it is
    proved given the classical facts (T) on Steenrod squares, Chern classes and Thom spaces, which are stated in
    the statement, cited from memory and not in the store, and nothing rests on it. The lower bound does not use
    the spin class. The background of clause (3) is an extension (G+) of
    the stored background (G), stated in the statement. Relation to the result on three rungs
    (synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side): the twisted cohomology of
    clause (3) is its clause (2), cited from there;
    with clause (2) here, e(L) is at most 5 on L^5(4) with no condition, so 4 <= k <= 5 on every side of the L^5(4)
    walls (lower bound from that result, conditional there at n = 2), and k = 5 on the definite side given the
    Steenrod Fact and the stated backgrounds. The statement is about tame walls: the tameness premise is an
    assumes edge of the derivation.
    Prior art. The least k with an equivariant map from projective space with the involution induced by a complex
    structure to a sphere is the level of the projective space (Dai, Lam and Peng; Pfister and Stolz, "On the level
    of projective spaces", Comment. Math. Helv. 1987, earlier bounds; Stolz, "The level of real projective
    spaces", Comment. Math. Helv. 64 (1989) 661-674). Stolz's theorem, as given in the published review of the
    paper (the paper itself was not read): for m >= 2 the level s(m) of the projective space of dimension 2m - 1
    is m + 1 for m = 0, 2 modulo 8, m + 2 for m = 1, 3, 4, 5, 7 modulo 8, and m + 3 for m = 6 modulo 8; the review
    notes that the two bounds of the source do not coincide at m = 4 modulo 8 while the theorem lists m + 2. With
    m = n + 1 this gives, as prior art not derived here, k_+(L^5(4)) = 5 and k_+(L^7(4)) = 6, so the window
    5 <= k_+(L^7(4)) <= 6 would close at the upper end, and the upper bound ceil(3(n+1)/2) of clause (2) is sharp
    for n = 1, 2, 3, 5 and not for n = 4, 6, 7 (7, 9, 9 against 8, 11, 12). The upper bound by quadratic maps is
    likely classical (the 1987 paper is reported to contain an upper bound of this kind; its exact form was not
    verified) and is not presented as new. The present proof uses none of this literature. Transport-absent: classical
    topology applied to the store's walls.
outside_ga:
  kind: other
  why: 'The statement is algebraic topology: obstruction classes, characteristic classes and a Steenrod square on a Thom space. The quarter turn, the walls, and the explicit maps that give the upper bounds are written in geometric algebra; the cohomological computation is integer arithmetic with no geometric-algebra form.'
---

## formal
Let $\Sig_{n} = L^{2n+1}(4) = S^{2n+1}/\langle J \rangle$, $J(v) = v \cdot B$ with $B = e_{1}e_{2} + \dots + e_{2n+1}e_{2n+2}$ in $\Cl(2n+2, 0)$, and $\shL$ the flat line on which $J$ acts by $-1$, with $x = w_{1}(\shL)$, $y$ and $u$ as in Theorem \claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure}. Let $k_{+}(\Sig_{n})$ be the rung count $k(\Sig)$ of a tame wall (\claimref{sheaf.tameness}) with cross-section $\Sig_{n}$, dying line $\shL$ and definite physical side, in the sense of \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}; such walls exist on $\Sig_{n} \times \R$ with side $(2n+2, 0)$ for $n \geq 2$, and $k_{+} = e(\shL)$, the least $k$ with $\shL \hookrightarrow \underline{\R}^{k}$ (\claimref{synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial}, clauses (1) and (3)). Write $w_{r}$ for the component of $v$ in the plane of $e_{2r+1}, e_{2r+2}$.
\begin{enumerate}
\item \emph{(Index form; proved.)} For a line bundle $\shL$ over a compact space $\Sig$ with unit-vector double cover $\widetilde\Sig$, $e(\shL)$ is the least $k$ for which there is a continuous map $\widetilde\Sig \to \R^{k} \setminus \{0\}$ that changes sign under the deck involution. For $\Sig_{n}$: $e(\shL)$ is the least $k$ with a continuous $F : S^{2n+1} \to \R^{k} \setminus \{0\}$, $F(J(v)) = -F(v)$. So on a definite side $k_{+}$ is one plus the least $j$ with an equivariant map of the double cover to $S^{j}$ with the antipodal action, as argued in the open problem.
\item \emph{(Upper bounds by explicit maps; proved.)} In $\Cl(6,0)$ let $\bar w_{1} = (w_{1}\cdot e_{3})e_{1} - (w_{1}\cdot e_{4})e_{2}$ (the mirror image of $w_{1}$ in the first plane) and
\[
F(v) = w_{0}e_{1}w_{0} - \bar w_{1} e_{1} \bar w_{1} + 2(w_{0}\cdot \bar w_{1})\,e_{3} + w_{2}e_{5}w_{2}.
\]
Then $F$ is a vector with no $e_{4}$ component, $F(J(v)) = -F(v)$ and $Q(F(v)) = (Q(w_{0}) + Q(w_{1}))^{2} + Q(w_{2})^{2}$, so $F \neq 0$ off the origin and $k_{+}(\Sig_{2}) \leq 5$. The first three terms alone give $k_{+}(\Sig_{1}) \leq 3$, the value stored for $L(4,1)$, and sums of such blocks give $k_{+}(\Sig_{n}) \leq \lceil 3(n+1)/2 \rceil$ for every $n$ (so $k_{+}(\Sig_{3}) \leq 6$), which is below the general bound $2n + 2$ for $n \geq 1$. Upper bounds of this kind for the level of projective spaces are likely classical (see the note on prior art); the map is given here in the algebra and is not claimed as new.
\item \emph{(Twisted cohomology and the primary obstruction; proved on the background (G+) below.)} With integer coefficients twisted by $x$ (the generator acting by $-1$), the cochain complex of the stored cell model is $\Z$ in each degree with coboundaries $-2, 0, -2, 0, \dots$: $H^{j}(\Sig_{n}; \Z_{x}) = \mathbb{Z}_{2}$ for $j$ odd, $0$ for $j$ even, $j \leq 2n+1$ (clause (2) of Theorem \claimref{synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side}, on the same background), and reduction modulo $2$ is injective on it. The primary obstruction to a map as in (1) into $\R^{3} \setminus \{0\}$, a class in $H^{3}(\Sig_{2}; \Z_{x}) = \mathbb{Z}_{2}$, vanishes: the three-component map of (2) is defined on the three-skeleton $S^{3}$ (the existence of that map needs no background). The lower bound $k_{+}(\Sig_{n}) \geq 3$ for $n \geq 1$ holds because two copies of $\shL$ form the half-turn plane bundle, with Euler class $\pm 2y \neq 0$ (clause (5) of the cited theorem).
\item \emph{(The secondary obstruction; proved given the imported Fact (S) and the backgrounds (G), (P) of the cited theorem; a second route given (T).)} There is no continuous $F : S^{5} \to \R^{4} \setminus \{0\}$ with $F(J(v)) = -F(v)$: this is clause (5) of Theorem \claimref{synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components}, an exact cup-one computation in the stored cell model, which holds given Steenrod's theorem on the cup-one square (the hypothesis (S) there, an imported Fact) and the cellular backgrounds (G) and (P) stated there. Hence
\[
k_{+}(L^{5}(4)) = 5, \qquad k_{+}(L^{2n+1}(4)) \geq 5 \ (n \geq 2), \qquad 5 \leq k_{+}(L^{7}(4)) \leq 6,
\]
against the stored window $3 \leq k \leq 6$ on $L^{5}(4)$ and $L^{7}(4)$. The obstruction is a class in $H^{5}(\Sig_{2}; \pi_{4}(S^{3})) = \mathbb{Z}_{2}$. A second route to the same non-existence statement, conditional on the classical facts (T) below and independent of the first, reads it off as follows: $\Sig_{2}$ is the unit circle bundle of the complex line bundle $\lambda$ of degree $4$ over the complex projective plane, four copies of $\shL$ are the pull-back of the plane bundle $V_{0}$ that is the sum of the line bundles of degrees $2$ and $-2$, a map $F$ would trivialise that pull-back and so extend $V_{0}$ to a bundle $V$ over the Thom space of $\lambda$ with $c_{1}(V) = 0$ and $c_{2}(V) = \mp U h$; but $Sq^{2}(U h) = U h^{2} \neq 0$ modulo $2$ while $Sq^{2}c_{2}(V) = c_{1}c_{2} + c_{3} = 0$.
\item \emph{(What the obstruction sees; computed, and argued where marked.)} For the quotient of $S^{5}$ by the cyclic group of order $d$ (even) with the line on which the generator acts by $-1$, the same computation gives: $d = 2$ (projective space), no integral class $nUh$ exists, the obstruction to four components is primary; $d \equiv 4 \pmod 8$, $n = -d/4$ is odd and $Sq^{2}(nUh) = n(d+1)Uh^{2} \neq 0$, a secondary obstruction; $d \equiv 0 \pmod 8$, the squaring test does not obstruct (whether four components then suffice is not decided here). On $L^{5}(4)$ the mod-2 class $x$, $\beta x = 2y$ and $(\beta x)^{2} = 0$ do not see it and neither does complex K-theory (stored); in terms of a class $a$ with $2a = \beta x$ the cases $d = 4, 8$ are separated by the reduction modulo $2$ of $a$ ($u$ against $0$), and the obstruction is not zero, $H^{5}(\Sig_{2}; \mathbb{Z}_{2})$ having the single nonzero class $x u^{2}$. That the secondary obstruction to four rungs is $x \cup \rho(a)^{2}$ on general walls is argued from these two cases only.
\end{enumerate}
The classical facts (T), cited from memory and not in the store. (T1) The Steenrod square $Sq^{2} : H^{j}(X; \mathbb{Z}_{2}) \to H^{j+2}(X; \mathbb{Z}_{2})$ is natural and additive, $Sq^{2}a = a^{2}$ in degree $2$, and on reductions of integral classes (where $Sq^{1} = 0$) it satisfies $Sq^{2}(ab) = Sq^{2}(a)\,b + a\,Sq^{2}(b)$. (T2) Complex vector bundles over finite complexes have natural Chern classes $c_{i}$, zero above the rank, with the product formula for sums and $c_{1}$ of the line bundle of degree $m$ over the projective plane equal to $mh$; and for every complex vector bundle $V$ over a finite complex $X$ there is a map $p : \mathrm{Fl}(V) \to X$ with $p^{*}V$ a sum of line bundles and $p^{*}$ injective on cohomology with coefficients $\Z$ and $\mathbb{Z}_{2}$. (T3) For a complex line bundle $\lambda$ over a finite complex $B$, the reduced cohomology of the Thom space is the free $H^{*}(B)$-module on a class $U$ of degree $2$ that restricts to $c_{1}(\lambda)$ on the zero section, with $U^{2} = c_{1}(\lambda)U$; and $H^{*}(\mathbb{CP}^{2}; \Z) = \Z[h]/(h^{3})$. The proof of (4) also uses two elementary constructions: the clutching of a bundle over the disc bundle with a product bundle over the cone along a trivialisation over the circle bundle, and the existence of Hermitian metrics. Clause (4) and the lower bounds in it hold given the Fact (S) and the backgrounds (G), (P) of the cited theorem on odd maps; only the second route of clause (4) is conditional on (T), and no bound rests on it. Clauses (1) and (2) use nothing beyond the algebra; clause (3) is on the background (G+): the stated background (G) of the cited theorem (cellular cohomology and obstruction classes for oriented plane bundles and for lines) extended by cellular cohomology with local coefficients and by the statement that the primary obstruction to a section of the sphere bundle of a bundle of rank $r$ is a class in $H^{r}$ with integers twisted by $w_{1}$. (G+) is not in the store.

## technical
The reduction of the definite-side rung count to an equivariant index is elementary once the stored equality $k = e(\shL)$ is used: an injection of a line bundle in a trivial bundle is, on unit vectors, a map to a punctured vector space that is odd under the deck involution. The upper bound comes from a quadratic map built from the double-angle map $w \mapsto w e_{1} w$ of the cited theorem: for two planes the three components $w_{0}e_{1}w_{0} - \bar w_{1}e_{1}\bar w_{1}$ and $2\,w_{0}\cdot \bar w_{1}$ have squared length $(Q(w_{0}) + Q(w_{1}))^{2}$ (in complex coordinates, $z_{1}^{2} - \bar z_{2}^{2}$ and $2\,\mathrm{Re}\,z_{1}z_{2}$, the map $q \mapsto \bar q j q$ of the quaternions), and a third plane adds its own double-angle map. So five components suffice in dimension five, and the map on the first two planes shows that the first obstruction to three components vanishes, as the twisted cohomology group $\mathbb{Z}_{2}$ allows. The lower bound is a secondary obstruction with coefficients $\pi_{4}(S^{3}) = \mathbb{Z}_{2}$. It is taken from the stored result on odd maps from the five-sphere to four components, an exact cup-one computation in the stored cell model that holds given Steenrod's theorem (an imported Fact) and the cellular backgrounds stated there. A second route, kept here, computes it without homotopy groups by moving the question to the projective plane: the lens space is a circle bundle over it, the bundle of four copies of the line is pulled back from it, and a trivialisation over the circle bundle is the same as an extension over the Thom space, where a squaring operation contradicts the Chern classes the extension would have. A cross-check through the Chern character gives the same parity $n(d+1)$ and is recorded in the check. The second route depends on the classical facts (T), which the store does not hold; the lower bound itself does not. The walls are tame walls, assuming the tameness premise.

## lay
Earlier results in this collection ask how many extra pairs of directions, called rungs, are needed to repair a wall where the geometry changes signature, when the wall is twisted. For a family of five-dimensional walls shaped like a lens space, a sphere with points identified under a quarter turn, the stored answer on a side where all directions are alike was only a window: between three and six. This result closes the window to five, with one caveat. That five rungs are enough is shown outright, by writing down an explicit rule that assigns to each point of the sphere five numbers, never all zero, which all change sign under the quarter turn. That four are not enough is shown in a companion result of the collection by a finite calculation on cells, given one classical theorem of Steenrod that the collection holds as an imported fact and standard background on cells. A second argument, kept here, reaches the same conclusion with three standard textbook tools of topology that the collection does not contain, and is conditional on them; they are listed. The obstruction to four rungs is of a subtle kind: none of the simpler invariants the collection already computes for these walls can see it, and the test that detects it finds nothing if the quarter turn is replaced by an eighth of a turn. The same reasoning shows that at least five rungs are needed on all the larger walls of the family, and gives a general upper limit of about one and a half rungs per pair of dimensions.

## one-liner
On a definite side the rung count of the lens wall $L^{2n+1}(4)$ is the least $k$ with a map $F : S^{2n+1} \to \R^{k}\setminus\{0\}$, $F(J(v)) = -F(v)$; an explicit quadratic map in $\Cl(6,0)$ gives $k \leq 5$ on $L^{5}(4)$ and $k \leq \lceil 3(n+1)/2 \rceil$ in general, the primary obstruction to three vanishes, and four is excluded by the stored cup-one computation in the cell model, given Steenrod's theorem (an imported Fact) and standard cellular background (a second route is given through Steenrod squares, Chern classes and Thom spaces, cited and not stored), so, assuming tameness, $k = 5$ on $L^{5}(4)$ and $5 \leq k \leq 6$ on $L^{7}(4)$.
