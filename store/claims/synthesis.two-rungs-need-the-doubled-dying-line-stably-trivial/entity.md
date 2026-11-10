---
id: synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial
kind: claim
version: 2
title: 'Spin class of the doubled dying line obstructs two rungs'
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, tameness, hyperbolic-plane, no-go]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
- name: Claude Fable 5.2
  role: restatement, the lens-space hypotheses (L1) and (L3) replaced by citations of the stored cohomology theorem, the result left conditional on the spin class (L2)
  version: 2
  source: maintainer pass of 2026-11-09
review: draft
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - synthesis.wall-rung-count-is-height-of-dying-line-class@2
  - synthesis.lens-space-wall-rung-count-sees-the-integral-twist@6
  - sheaf.degeneration-sheaf@6
  - sheaf.imported-real-line-bundles@1
  - synthesis.imported-whitney-product-formula-and-projective-space@1
  - std-algebra.spin-double-cover@1
  - synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure@1
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_lens_action_and_walls
- kind: check
  ref: check.py::check_spin_lift_of_doubled_line
- kind: check
  ref: check.py::check_spin_class_of_doubled_line_on_lens_spaces
- kind: check
  ref: check.py::check_k_theory_cross_check
- kind: check
  ref: check.py::check_quaternionic_odd_map_bounds_embedding_rank
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - sheaf.wall-class
  - synthesis.lens-space-wall-rung-count-sees-the-integral-twist
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Note only, version kept: two later results sharpen the rung count on the quarter-turn lens walls. synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side: three rungs fail on every side from dimension five, so k >= 4 there (dimension five given the spin class). synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five, with synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components: on the definite side of the walls with cross-section L^5(4), k = 5 (an explicit five-component odd map; no four-component one, given the imported Fact synthesis.imported-steenrod-cup-one-square-is-a-natural-cohomology-operation and the stated cellular background). The bound of this result on L^5(4), at least three rungs, is consistent with them and is superseded as a count; its criterion for two rungs is unchanged. The lay level now says at least three and points to the later count. Statement, proof and check unchanged.'
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Cross-reference: the intended citation of the companion K-theory result is now a plain cross-reference to its stored id (extraction note only); statement unchanged.'
  maintainer_pass_2026_11_09b:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Version 1 -> 2 (decisions of 9 November 2026): restated, the hypotheses (L1) (cohomology rings and stable tangent bundle of the quarter-turn lens spaces) and (L3) (their K-ring, used in one remark) are no longer cited from memory but taken from synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure (new uses edge), so the result is conditional on the spin class (L2) alone among the classical inputs; clauses, bounds, proof steps and check are unchanged.'
  open_problem: op.wall-class-invariant
  note: >-
    Attack item 1 of op.wall-class-invariant (walls of dimension at least four). The lead from Adams' theorem on
    real projective walls was tested and dropped: on RP^n the only nontrivial line is the tautological one, with
    ht(x) = e(L) = n + 1, so k = n + 1 is already fixed and nothing separates there. What does separate is the
    stable class of L + L: clause (1) of the parent claim at k = 2 forces the complement line N to be L, so a
    two-rung completion on either side makes L + L stably trivial, and the spin Pontryagin class q1 = p1/2 of
    L + L (canonically spin when x^2 = 0, its Spin(2) bundle a square root of L + L through the rotor double
    cover) obstructs that. On L^{2m+1}(4) the square root is the quarter-turn plane bundle, q1 = 2y^2, nonzero in
    H^4 = Z_4 for m >= 2. Of the classical facts (L1) to (L3) of the formal level, cited from memory at version 1,
    two are now taken from the store (version 2): the integral and mod-2 cohomology of L^{2m+1}(4) and its stable
    tangent bundle (L1) are clauses (3) and (5) of
    synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure, proved there on its
    stated background of cellular cohomology and obstruction theory, and the complex K-ring of these lens spaces
    Z[eta]/(eta^4 - 1, (eta - 1)^{m+1}), used only in the cross-check remark (L3), is its clause (6), given the
    imported Atiyah-Hirzebruch filtration. What remains cited from memory and not in the store (by decision, not
    imported) is (L2): the spin class q1 with 2 q1 = p1 (Thomas), natural and stable, p1 = e^2 for oriented plane
    bundles (Milnor and Stasheff), orientable iff w1 = 0 and spin iff w2 = 0. The result is conditional on (L2);
    deriving q1 in the store is an open item. Only necessity is proved: stable triviality of L + L is necessary
    for two rungs, not shown sufficient. The K-theory cross-check at m = 3 is
    the same computation as clause (1) at n = 3 of
    synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height, which also holds the all-k obstruction and
    the unbounded growth. Transport-absent: bundle algebra of symmetric forms, with the store's wall theory as the
    only series input.
outside_ga:
  kind: imported
  why: 'The obstruction is a characteristic class in integral cohomology (the spin class q1 = p1/2 of the plane bundle L + L, read through the cohomology ring of a lens space), and the dimension-seven cross-check uses the complex K-theory ring of the lens space; the spin class is a classical input cited from memory, the cohomology ring and the K-ring are taken from the stored cohomology theorem. The group actions, the walls, the spin lift and the embeddings are computed in GA.'
---

## formal
Given the classical facts (L2) below on the spin class, cited from memory and not in the store, and with (L1) and (L3) below supplied by Theorem \claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure}, let $(M, G)$ be a tame corank-one degeneration (\claimref{sheaf.tameness}) with compact wall $\Sig$, physical side $\Mp$ of signature $(p,q)$, $p \geq 1$, dying line $\shL$, $x := w_{1}(\shL)$, and $k(\Sig)$, $\operatorname{ht}(x)$, $e(\shL)$ as in \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}.
\begin{enumerate}
\item \emph{(Two rungs.)} On every side, definite or indefinite, and in every dimension: if $k(\Sig) \leq 2$ then $\shL \oplus \shL$ is stably trivial. If the physical side is definite ($q = 0$), then $k(\Sig) = e(\shL)$ exactly.
\item \emph{(The obstruction.)} If $x^{2} = 0$, the oriented plane bundle $\shL \oplus \shL$ is spin. If each of its spin structures has nonzero spin class $q_{1} = p_{1}/2 \in H^{4}(\Sig; \mathbb{Z})$, then $\shL \oplus \shL$ is not stably trivial and $k(\Sig) \geq 3$ on every side.
\item \emph{(Lens walls.)} Let $\Sig_{m} = L^{2m+1}(4) = S^{2m+1}/\langle J \rangle$, $J(v) = v \cdot B$ with $B = e_{1}e_{2} + e_{3}e_{4} + \dots + e_{2m+1}e_{2m+2}$, and $\shL$ the flat line on which $J$ acts by $-1$. Then $x \neq 0 = x^{2}$, so $\operatorname{ht}(x) = 2$, the Euler class of $\shL \oplus \shL$ is $2y \neq 0$ with $y$ of order four, and $q_{1}(\shL \oplus \shL) = 2y^{2}$ for both spin structures, nonzero in $H^{4}(\Sig_{m}; \mathbb{Z}) = \mathbb{Z}_{4}$ when $m \geq 2$. Hence every tame wall with cross-section $\Sig_{m}$, $m \geq 2$, and dying line $\shL$ has $k(\Sig) \geq 3 > \operatorname{ht}(x)$, whatever the signature of the physical side; such walls exist on $\Sig_{m} \times \R$ with physical side of signature $(1, 2m+1)$ and $(2m+2, 0)$, and on $\Sig_{m} \times T^{j}$ in every dimension $2m + 1 + j \geq 5$. On $\Sig_{3} = L^{7}(4)$, $3 \leq k(\Sig) \leq e(\shL) \leq 6$ on every side.
\item \emph{(Dimension five.)} In particular the tame wall on $L^{5}(4) \times \R$ with physical side of signature $(1,5)$ has $k(\Sig) \geq 3 > 2 = \operatorname{ht}(x)$: on indefinite sides $k(\Sig) = \operatorname{ht}(x)$ fails for walls of dimension five. A necessary condition for two rungs is that $\shL \oplus \shL$ be stably trivial; on $L^{5}(4)$ it fails, detected by $q_{1}(\shL \oplus \shL) = 2y^{2}$. The mod-2 data do not see this, and neither does $p_{1} = (\beta x)^{2} = 4y^{2} = 0$; $q_{1} = 2a^{2}$ for any $a$ with $2a = \beta x$, so $q_{1}$ is a function of $\beta x$ through the integral cup product, and this result does not show that $k(\Sig)$ is undetermined by $W(\Sig)$, $\beta x$ and the signature. Given (L3), complex K-theory does not see the obstruction on $L^{5}(4)$: the complexification of $\shL \oplus \shL$ is stably trivial there.
\end{enumerate}
The inputs on lens spaces. (L1), stored: $H^{\mathrm{even}}(\Sig_{m}; \mathbb{Z}) = \mathbb{Z}[y]/(4y, y^{m+1})$ with $y$, up to sign, the Euler class of the quarter-turn plane bundle $\eta$, $H^{*}(\Sig_{m}; \mathbb{Z}_{2}) = \Lambda[x] \otimes \mathbb{Z}_{2}[u]/(u^{m+1})$ with $x = w_{1}(\shL)$, and $T\Sig_{m} \oplus \underline{\R} \cong (m+1)\,\eta$; these are clauses (3) and (5) of Theorem \claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure} (there with $n$ for $m$), proved there given its stated background (G) of cellular cohomology and obstruction theory. (L2), assumed, cited from memory and not in the store: the spin class $q_{1}$ generating $H^{4}(B\mathrm{Spin}; \mathbb{Z})$, natural and stable, with $2q_{1} = p_{1}$, $p_{1} = e^{2}$ for oriented plane bundles, and a bundle is orientable iff $w_{1} = 0$ and spin iff $w_{2} = 0$. (L3), stored: $K(\Sig_{m}) = \mathbb{Z}[\eta]/(\eta^{4} - 1, (\eta - 1)^{m+1})$, used only for the last sentence of (4); it is clause (6) of the same theorem, proved there given the imported Atiyah-Hirzebruch filtration. The Whitney product formula is Fact \claimref{synthesis.imported-whitney-product-formula-and-projective-space}(i). Each clause that uses (L2) is conditional on it; the clauses that use (L1) or (L3) hold on the background and the imported Fact of the cited theorem.

## technical
The parent claim bounds the number of rungs of a tame wall between the height of the dying line's class and the least rank of a trivial bundle containing the dying line, and the lens-space result showed that with an indefinite physical side the lower bound is attained on $L(4,1)$, so that in dimension three only a definite side sees past the mod-2 class. This result shows that from dimension five on an indefinite side sees past it too. At two rungs the parent's necessity clause supplies a line bundle $N$ with $N(\overline G) \oplus \shL \oplus N \cong N(\overline G) \oplus \underline{\R}^{2}$; its first Stiefel-Whitney class is $x$, so $N \cong \shL$, and after adding a complement of $N(\overline G)$ the doubled dying line $\shL \oplus \shL$ is stably trivial. The negative part of the physical metric, which the indefinite construction on $L(4,1)$ borrows, only cancels unstably; it cannot change the stable class. With a definite side the same clause puts $\shL$ inside the trivial rung bundle, so there the count is exactly the embedding rank $e(\shL)$.

When $x^{2} = 0$ the plane bundle $\shL \oplus \shL$ is spin, and its spin class $q_{1} = p_{1}/2$ is a stable obstruction in integral cohomology that $p_{1}$ itself can miss. Only necessity is proved: stable triviality of $\shL \oplus \shL$ is a necessary condition for two rungs. Of the classical inputs, the cohomology of the lens spaces and, for a cross-check, their K-ring are taken from the stored cohomology theorem (\claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure}); the spin class is cited from memory and stated as a hypothesis, the one on which the result remains conditional. On the lens space $L^{2m+1}(4)$, the quotient of the sphere by the quarter turn $J$ in every coordinate plane, the doubled dying line is the flat plane bundle on which $J$ acts by the half turn, and the half turn is the image of the rotor $e_{1}e_{2}$ under the rotor double cover; so its spin structures are the quarter-turn plane bundle and its conjugate, with Euler class $\pm y$, and $q_{1} = 2y^{2}$. In $H^{4} = \mathbb{Z}_{4}$ this is nonzero once $m \geq 2$, while $p_{1} = 4y^{2} = 0$. Every wall with such a cross-section therefore needs three rungs on any side, against a mod-2 lower bound of two; walls with an indefinite physical side of signature $(1, 2m+1)$ are written down explicitly. The first case is $L^{5}(4)$, of dimension five; in dimension four the obstruction cannot occur on a closed wall (argued in the proof). A quaternionic odd map bounds the count on $L^{7}(4)$ by six. In complex K-theory the obstruction is visible on $L^{7}(4)$ but not on $L^{5}(4)$, where $q_{1}$ alone detects it. All of this assumes the tame-wall setting of the parent claim.

## lay
Where the geometry of spacetime changes signature, the degeneracy can be repaired by adding extra pairs of directions (rungs), and earlier results bounded how many are needed by how the dying direction twists along the wall. On three-dimensional walls the simple twist class alone set the price whenever the side we live on has directions of both signs. This result shows that this stops being true from five dimensions on. Two rungs can only work if two copies of the dying direction, taken together, can be untwisted after adding enough straight directions. An integer-valued characteristic class of that doubled direction, half its Pontryagin class, read through the half-turn spinor that squares to minus one, can forbid this even when the simple twist class and the Pontryagin class itself allow it. On a five-dimensional lens space it does (granting one classical fact, the existence and properties of that half Pontryagin class, which the store cites but does not hold; the facts about lens spaces themselves are now derived in the store), so at least three rungs are needed whatever the signature, although the simple twist class asks for only two (later results in the collection raise the count on these walls to at least four on every side, and to exactly five on a side where all directions have the same sign); even the ordinary complex invariants of the doubled direction miss this case.

## one-liner
Under the tameness hypotheses and the classical spin class $q_{1}$ (cited from memory; the cohomology of the lens spaces is a stored theorem), two rungs force the doubled dying line to be stably trivial on every side (and a definite side needs exactly $e(\shL)$ rungs); its spin class $2y^{2}$ forbids that on the lens spaces $L^{2m+1}(4)$, $m \geq 2$, so their walls need at least three rungs with any physical signature although $\operatorname{ht}(x) = 2$, from dimension five on, where complex K-theory is still blind.
