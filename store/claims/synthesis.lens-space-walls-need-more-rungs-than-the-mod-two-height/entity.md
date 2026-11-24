---
id: synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height
kind: claim
version: 3
title: Lens-space walls need more rungs than the mod-2 height, without bound
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
  role: restatement, the K-ring hypothesis (L2) and the Steenrod-square hypothesis (L3) replaced by citations of the stored cohomology theorem, the result left conditional on the lambda-operations (L1)
  version: 2
  source: maintainer pass of 2026-11-09
- name: Claude Fable 5.2
  role: restatement of clause (2), the order of the doubled dying line given for every n by citation of the valuation result, in place of a lower bound for every n and an equality computed for n up to 8
  version: 3
  source: run 2026-11-24-number-theory
amendments:
- version: 3
  kind: restatement
  defect: 'clause (2) gave the order of 1 - xi as at least 2^floor(n/2) for every n and equal to 2^floor((n+1)/2) only for n up to 8, by computation; the order is 2^ceil(n/2) = 2^floor((n+1)/2) for every n (clause (ii) of the valuation result), so the larger bound 1 + floor((n+1)/2) on the rungs holds for every n and the bound 1 + floor(n/2) was one less, at odd n, than what the obstruction of clause (1) gives; clause (4) quoted the smaller bound r on L^(4r-1)(4), now r + 1'
  evidence: 'check.py::check_order_of_one_minus_chi_squared_in_the_stored_k_ring_is_two_to_the_ceiling_of_n_over_two of the valuation result (n up to 40), and its proof of clause (ii)'
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
  - synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure@1
  - synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-in-the-ring-of-the-quarter-turn@1
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_lambda_series_forces_power_of_two_multiple
- kind: check
  ref: check.py::check_k_ring_order_of_dying_line_on_lens_spaces
- kind: check
  ref: check.py::check_gaussian_bound_on_powers
- kind: check
  ref: check.py::check_lens_walls_exist_with_both_sides
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - sheaf.wall-class
  - synthesis.wall-rung-count-is-height-of-dying-line-class
  - synthesis.lens-space-wall-rung-count-sees-the-integral-twist
extraction:
  amendment_2026_11_24:
    by: run 2026-11-24-number-theory
    date: '2026-11-24'
    note: 'Version 2 -> 3 (Leon''s decision of 24 November 2026): clause (2) restated. The order of 1 - xi in the stored K-ring is now given for every n, 2^ceil(n/2), by clause (ii) of synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-in-the-ring-of-the-quarter-turn (new uses edge), and the bound on the rungs is 1 + ceil(n/2) for every n. The lower bound through the ring of the quarter turn and the lattice computation for n up to 8 stay in the proof as the original argument and agree with it; clauses (1) and (3), the other edges and the checks are unchanged, and clause (4) is unchanged except that its bound on $L^{4r-1}(4)$ reads r + 1 in place of r. The result stays conditional on the lambda-operations (L1).'
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Note only, version kept: two later results sharpen the rung count on the quarter-turn lens walls. synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side: three rungs fail on every side from dimension five, so k >= 4 there (dimension five given the spin class). synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five, with synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components: on the definite side of the walls with cross-section L^5(4), k = 5 (an explicit five-component odd map; no four-component one, given the imported Fact synthesis.imported-steenrod-cup-one-square-is-a-natural-cohomology-operation and the stated cellular background). The lower bounds of this result (at least three rungs in dimension seven, growing without limit with the dimension) are consistent with them; in dimensions five and seven the later bound is the stronger one. Statement, proof and check unchanged.'
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Cross-reference: the intended citation of the companion spin-class result is now a plain cross-reference to its stored id (extraction note only); statement unchanged.'
  maintainer_pass_2026_11_09b:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Version 1 -> 2 (decisions of 9 November 2026): restated, the K-ring of the lens spaces (L2) is no longer cited from memory but is clause (6) of synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure (new uses edge; a stored theorem given the imported Atiyah-Hirzebruch filtration), and the Steenrod-square hypothesis (L3) is dropped, x^2 = 0 being its clause (3) computed directly; the result stays conditional on the lambda-operations (L1), which clause (1) uses; bounds, proof steps and check are unchanged.'
  open_problem: op.wall-class-invariant
  note: >-
    Attack item 1 of op.wall-class-invariant (indefinite sides, walls of dimension at least four). The obstruction
    found is stable: it does not come from the failure of the stable-range step of the lens-space proof but from the
    complex K-theory class of the doubled dying line, which the mod-2 class x does not see. On the lead that Adams'
    theorem on RP^n would separate ht, k and e: on RP^n the only nontrivial line is the tautological one, where
    ht(x) = e(L) = n + 1, so k = n + 1 on every side and Adams' 2^phi(n) (which concerns multiples mL) never enters;
    Adams-type input enters instead through the order of L - 1 in K-theory, on lens spaces. Of the classical inputs
    (L1) to (L3), cited from memory at version 1, two are now taken from the store (version 2). The K-ring of the
    lens space, K(S^{2n+1}/Z_4) = Z[chi]/(chi^4 - 1, (chi - 1)^{n+1}) (L2), is clause (6) of
    synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure, a stored theorem given
    the imported Atiyah-Hirzebruch filtration (literature for the ring, from memory: M. F. Atiyah, K-Theory, Benjamin
    1967; M. F. Atiyah, Characters and cohomology of finite groups, Publ. Math. IHES 9 (1961); T. Kambe, J. Math. Soc.
    Japan 18 (1966) 135). The Bockstein fact Sq^1 = 0 on classes that lift to Z_4 (L3) is no longer used: x^2 = 0
    is clause (3) of that theorem, computed directly from the cell structure. What remains cited from memory and
    not in the store is (L1), the lambda-operations on K-theory (Atiyah, K-Theory), which clause (1) uses and on
    which every clause is conditional; deriving them is an open item. Not claimed: the exact rung count of any lens-space wall of dimension at least seven (only lower
    bounds, against the parent's upper bound e(L) <= dim + 1); the general order formula 2^{floor((n+1)/2)} beyond
    n = 8, which is computed, not proved, there; anything on L^5(4), where the complex K-class gives no obstruction
    (a real or spin invariant might). The companion result synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial
    proves k >= 3 on L^5(4) and L^7(4) by the spin class q1, so the failure
    of k = ht on indefinite sides starts in dimension five, and builds walls of physical type (1, 2n+1) for every n; this
    result owns the general K obstruction and the unbounded excess. Transport-absent: the result is bundle topology of the stored wall setting.
outside_ga:
  kind: other
  why: 'Clauses (1) and (2) compute in the complex K-ring of the wall, a ring of stable classes of complex vector bundles with its lambda-operations; the lambda-operations are taken from the literature as the explicit hypothesis (L1) of the statement (cited from memory, not in the store) and the K-ring of the lens spaces from the stored cohomology theorem. The complex structure of the doubled dying line is the unit bivector of each fibre plane of L + L, as in the parent lens-space result; the K-ring itself and the ring map to the Gaussian integers (written with the GA unit I = e1e2, I^2 = -1) are not geometric-algebra statements.'
---

## formal
Let $(M, G)$ be a tame corank-one degeneration (\claimref{sheaf.tameness}) with compact wall $\Sig$, physical side $\Mp$ of any signature $(p,q)$, $p \geq 1$, dying line $\shL$, $x := w_1(\shL)$, and $k(\Sig)$ the least number of rungs of a completion in the sense of \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}. Let $\xi \in K(\Sig)$ be the class of the complexification of $\shL$: the plane bundle $\shL \oplus \shL$ with the unit bivector of each fibre plane as complex structure. Given the classical fact (L1), cited from memory and not in the store: (L1) complex K-theory $K(X)$ of a finite complex is a commutative ring with lambda-operations, $\lambda_t$ additive-to-multiplicative, $\lambda_t(\ell) = 1 + \ell t$ on line bundles and $\lambda^{j}(E) = 0$ for $j > \operatorname{rank} E$; and with (L2) $K(L^{2n+1}(4)) = \Z[\chi]/(\chi^{4} - 1, (\chi - 1)^{n+1})$, $\chi^{e}$ the flat line on which the generator acts by $\chi^{e}$, supplied by clause (6) of Theorem \claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure} (proved there given the imported Atiyah-Hirzebruch filtration and its stated background of cellular cohomology), and the former (L3) on $Sq^{1}$ replaced by clause (3) of the same theorem ($x^{2} = 0$, computed directly); the following hold.
\begin{enumerate}
\item \emph{(A stable obstruction on every side.)} If a $k$-rung completion exists, then $2^{k-1}(1 - \xi) = 0$ in $K(\Sig)$. Hence $k(\Sig) \geq 1 + \log_{2} \operatorname{ord}(1 - \xi)$, whatever the signature of the physical side.
\item \emph{(Lens-space walls.)} Let $\Sig = L^{2n+1}(4) = S^{2n+1}/\mathbb{Z}_{4}$, the generator acting by a complex structure, and $x \neq 0$. Then $x^{2} = 0$ (clause (3) of the cited theorem), so $\operatorname{ht}(x) = 2$, in every dimension; with $K(\Sig)$ as in (L2) and $\xi = \chi^{2}$, the order of $1 - \xi$ is $2^{\lceil n/2 \rceil} = 2^{\lfloor (n+1)/2 \rfloor}$ for every $n \geq 1$ (clause (ii) of Theorem \claimref{synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-in-the-ring-of-the-quarter-turn}; before version 3 this clause had the lower bound $2^{\lfloor n/2 \rfloor}$ for every $n$ and the equality for $1 \leq n \leq 8$ only). So on every side
\[
k(\Sig) \;\geq\; 1 + \lceil n/2 \rceil \;=\; 1 + \lfloor (n+1)/2 \rfloor \quad (\text{all } n \geq 1),
\]
for instance $k \geq 3$ on $L^{7}(4)$, $k \geq 4$ on $L^{11}(4)$ and $k \geq 5$ on $L^{15}(4)$, while $\operatorname{ht}(x) = 2$. At $n = 1$ the bound is $2$, consistent with the stored two-rung completion of the $L(4,1)$ wall with an indefinite side (\claimref{synthesis.lens-space-wall-rung-count-sees-the-integral-twist}).
\item \emph{(The walls exist, with either side.)} For $n$ odd, $\Sig \times \R$ carries tame walls with cross-section $L^{2n+1}(4)$, dying line $\shL$ with $x \neq 0$, and physical side of signature $(2n+1, 1)$ (one negative direction) or $(2n+2, 0)$. The obstruction of (1) and (2) holds on every side, including the physical type $(1, 2n+1)$, but the walls built here have one negative direction, not that type. On a definite side $k(\Sig) = e(\shL)$: with $N(\overline G) = 0$, clause (1) of the parent gives $\shL \oplus N \cong \underline{\R}^{k}$, so $k \geq e(\shL)$, and clause (2) gives $k \leq e(\shL)$.
\item \emph{(Consequence for the open question.)} On the walls of (3) with cross-section $L^{4r-1}(4)$, $r \geq 2$, and the indefinite side $(4r-1, 1)$, $k(\Sig) = \operatorname{ht}(x)$ fails, and no function of $\operatorname{ht}(x)$ bounds $k(\Sig)$: along $L^{4r-1}(4)$ the class $x$ has height $2$, $\beta x$ has order $2$ and $(\beta x)^{2} = 0$, while $k(\Sig) \geq r + 1$ grows without bound. The excess over $\operatorname{ht}(x)$ is a stable K-theoretic datum, present on definite and indefinite sides alike, not a failure of the stable range.
\end{enumerate}
Every clause is conditional on (L1), the lambda-operations, which is not derived in the store; clauses (2) and (4) rest in addition on the cited cohomology theorem, and through it on the imported Atiyah-Hirzebruch filtration and on that theorem's stated background.

## technical
The parent claim bounds the rung count of a tame wall below by the height of the mod-2 class of the dying line and above by the least rank of a trivial bundle containing it, and its necessity clause says more: $k$ rungs give a bundle $N$ of rank $k-1$ with $N(\overline G) \oplus \shL \oplus N \cong N(\overline G) \oplus \underline{\R}^{k}$. Complexifying and passing to K-theory removes $N(\overline G)$, so the class of $N$ is $k - \xi$, and an actual bundle of rank $k-1$ has vanishing exterior powers above $k-1$; the coefficient of $t^{k}$ in $(1+t)^{k}(1+\xi t)^{-1}$ is $(1-\xi)^{k} = 2^{k-1}(1-\xi)$ (as $\xi^{2} = 1$), so this must vanish. That is an obstruction on every side, independent of the stable-range step, and it sees what $x$ cannot: on the lens spaces $L^{2n+1}(4)$ the class $x$ always squares to zero, but the order of $1 - \xi$ in the K-ring, which the stored cohomology theorem (\claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure}) derives from the Atiyah-Hirzebruch filtration, grows with $n$. A ring map to the Gaussian integers modulo a power of $1 + I$ (with $I$ the GA unit $e_1e_2$) sends $1 - \xi$ to $2$ and gives the bound $k \geq 1 + \lfloor n/2 \rfloor$ in every dimension; an exact lattice computation gives the sharper $1 + \lfloor (n+1)/2 \rfloor$ up to $n = 8$, which is $3$ already on $L^{7}(4)$; and the order is in fact $2^{\lfloor (n+1)/2 \rfloor}$ for every $n$, by a divisibility in the same ring (the valuation result cited in clause (2)), so the sharper bound holds in every dimension.

The walls are explicit: on the unit sphere of $\HH^{r}$, with the $\mathbb{Z}_{4}$ generated by left multiplication by the rotor bivector $B = e_2e_3$, left multiplication by $e_3e_1$, which anticommutes with $B$, is a unit tangent field that changes sign under the generator, so its span descends to the twisted line inside $T^*\Sig$; collapsing the metric along it, with a time direction of either sign, gives tame walls with a definite side or an indefinite side with one negative direction. On $L(4,1)$ the bound is $2$, matching the stored completion; complex K-theory says nothing on $L^{5}(4)$, and on the walls built here the obstruction first bites in dimension seven. What this result adds to the first attack item is unboundedness: on these walls the rung count with an indefinite side is not the mod-2 height and is not bounded by any function of it. All of this assumes the tame-wall setting of the parent claim and the lambda-operations of K-theory (L1), cited from memory; the K-ring of the lens spaces and the vanishing of $x^{2}$ are taken from the stored cohomology theorem.

## lay
At a wall where the geometry changes signature in the well-behaved way the series assumes, an earlier result counted the extra pairs of directions needed to repair the wall: at least the number of times the twist of the dying direction can be multiplied by itself before it vanishes, and on one small three-dimensional example exactly that many. This result shows that in higher dimensions the count can be much larger. On a family of walls shaped like lens spaces the twist always vanishes after two multiplications, yet the repair needs at least three extra pairs in seven dimensions, four in eleven, five in fifteen, and more without limit as the dimension grows. The extra cost is invisible to the usual mod-2 bookkeeping and is read off from the K-theory of the wall, an algebra of bundles; it applies whatever the signature on the physical side.

## one-liner
Assuming the tameness hypotheses and the lambda-operations of K-theory (cited from memory; the K-ring of the lens spaces is a stored theorem given the imported Atiyah-Hirzebruch filtration), a $k$-rung completion forces $2^{k-1}(1 - \xi) = 0$ in the K-theory of the wall ($\xi$ the complexified dying line), on every side; on lens-space walls $L^{2n+1}(4)$, where $\operatorname{ht}(w_1\shL) = 2$, this gives $k \geq 1 + \lceil n/2 \rceil$ for every $n$ (so $k \geq 3$ in dimension seven), the order of $1 - \xi$ being $2^{\lceil n/2 \rceil}$ by the cited valuation result, so the rung count is not bounded by the mod-2 height.
