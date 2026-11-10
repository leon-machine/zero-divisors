---
id: synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height
kind: claim
version: 1
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
review: draft
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - synthesis.wall-rung-count-is-height-of-dying-line-class@2
  - synthesis.lens-space-wall-rung-count-sees-the-integral-twist@5
  - sheaf.degeneration-sheaf@6
  - sheaf.imported-real-line-bundles@1
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
  open_problem: op.wall-class-invariant
  note: >-
    Attack item 1 of op.wall-class-invariant (indefinite sides, walls of dimension at least four). The obstruction
    found is stable: it does not come from the failure of the stable-range step of the lens-space proof but from the
    complex K-theory class of the doubled dying line, which the mod-2 class x does not see. On the lead that Adams'
    theorem on RP^n would separate ht, k and e: on RP^n the only nontrivial line is the tautological one, where
    ht(x) = e(L) = n + 1, so k = n + 1 on every side and Adams' 2^phi(n) (which concerns multiples mL) never enters;
    Adams-type input enters instead through the order of L - 1 in K-theory, on lens spaces. Classical inputs cited from
    memory, not imported (a decision for the maintainer): the K-ring of a lens space,
    K(S^{2n+1}/Z_m) = Z[chi]/(chi^m - 1, (chi - 1)^{n+1}), from the equivariant Thom isomorphism and the Gysin sequence
    (M. F. Atiyah, K-Theory, Benjamin 1967, Section 2.7; M. F. Atiyah, Characters and cohomology of finite groups,
    Publ. Math. IHES 9 (1961); T. Kambe, J. Math. Soc. Japan 18 (1966) 135); the lambda-operations on K-theory
    (Atiyah, ibid.); and the Bockstein fact Sq^1 = 0 on classes that lift to Z_4 (A. Hatcher, Algebraic Topology,
    Section 4.L). Not claimed: the exact rung count of any lens-space wall of dimension at least seven (only lower
    bounds, against the parent's upper bound e(L) <= dim + 1); the general order formula 2^{floor((n+1)/2)} beyond
    n = 8, which is computed, not proved, there; anything on L^5(4), where the complex K-class gives no obstruction
    (a real or spin invariant might). Transport-absent: the result is bundle topology of the stored wall setting.
outside_ga:
  kind: imported
  why: 'Clauses (1) and (2) compute in the complex K-ring of the wall, a ring of stable classes of complex vector bundles with its lambda-operations, imported from the literature (cited from memory). The complex structure of the doubled dying line is the unit bivector of each fibre plane of L + L, as in the parent lens-space result; the K-ring itself and the ring map to the Gaussian integers (written with the GA unit I = e1e2, I^2 = -1) are not geometric-algebra statements.'
---

## formal
Let $(M, G)$ be a tame corank-one degeneration (\claimref{sheaf.tameness}) with compact wall $\Sig$, physical side $\Mp$ of any signature $(p,q)$, $p \geq 1$, dying line $\shL$, $x := w_1(\shL)$, and $k(\Sig)$ the least number of rungs of a completion in the sense of \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}. Let $\xi \in K(\Sig)$ be the class of the complexification of $\shL$: the plane bundle $\shL \oplus \shL$ with the unit bivector of each fibre plane as complex structure.
\begin{enumerate}
\item \emph{(A stable obstruction on every side.)} If a $k$-rung completion exists, then $2^{k-1}(1 - \xi) = 0$ in $K(\Sig)$. Hence $k(\Sig) \geq 1 + \log_{2} \operatorname{ord}(1 - \xi)$, whatever the signature of the physical side.
\item \emph{(Lens-space walls.)} Let $\Sig = L^{2n+1}(4) = S^{2n+1}/\mathbb{Z}_{4}$, the generator acting by a complex structure, and $x \neq 0$. Then $x^{2} = 0$, so $\operatorname{ht}(x) = 2$, in every dimension; with $K(\Sig) = \Z[\chi]/(\chi^{4} - 1, (\chi - 1)^{n+1})$ (classical, cited from memory) and $\xi = \chi^{2}$, the order of $1 - \xi$ is at least $2^{\lfloor n/2 \rfloor}$ for every $n$ and equals $2^{\lfloor (n+1)/2 \rfloor}$ for $1 \leq n \leq 8$. So on every side
\[
k(\Sig) \;\geq\; 1 + \lfloor n/2 \rfloor \quad (\text{all } n), \qquad k(\Sig) \;\geq\; 1 + \lfloor (n+1)/2 \rfloor \quad (1 \leq n \leq 8),
\]
for instance $k \geq 3$ on $L^{7}(4)$, $k \geq 4$ on $L^{11}(4)$ and $k \geq 5$ on $L^{15}(4)$, while $\operatorname{ht}(x) = 2$. At $n = 1$ the bound is $2$, consistent with the stored two-rung completion of the $L(4,1)$ wall with an indefinite side (\claimref{synthesis.lens-space-wall-rung-count-sees-the-integral-twist}).
\item \emph{(The walls exist, with either side.)} For $n$ odd, $\Sig \times \R$ carries tame walls with cross-section $L^{2n+1}(4)$, dying line $\shL$ with $x \neq 0$, and physical side of signature $(2n+1, 1)$ or $(2n+2, 0)$.
\item \emph{(Consequence for the open question.)} On walls of dimension at least seven with an indefinite physical side, $k(\Sig) = \operatorname{ht}(x)$ fails, and no function of $\operatorname{ht}(x)$ bounds $k(\Sig)$: along $L^{4r-1}(4)$ the class $x$ has height $2$, $\beta x$ has order $2$ and $(\beta x)^{2} = 0$, while $k(\Sig) \geq r$ grows without bound. The excess over $\operatorname{ht}(x)$ is a stable K-theoretic datum, present on definite and indefinite sides alike, not a failure of the stable range.
\end{enumerate}
Classical inputs, cited from memory and not imported: the K-ring of lens spaces (equivariant Thom isomorphism and Gysin sequence), the lambda-operations on $K$, and $Sq^{1} = 0$ on mod-2 classes that lift to $\Z_{4}$.

## technical
The parent claim bounds the rung count of a tame wall below by the height of the mod-2 class of the dying line and above by the least rank of a trivial bundle containing it, and its necessity clause says more: $k$ rungs give a bundle $N$ of rank $k-1$ with $N(\overline G) \oplus \shL \oplus N \cong N(\overline G) \oplus \underline{\R}^{k}$. Complexifying and passing to K-theory removes $N(\overline G)$, so the class of $N$ is $k - \xi$, and an actual bundle of rank $k-1$ has vanishing exterior powers above $k-1$; the coefficient of $t^{k}$ in $(1+t)^{k}(1+\xi t)^{-1}$ is $(1-\xi)^{k} = 2^{k-1}(1-\xi)$ (as $\xi^{2} = 1$), so this must vanish. That is an obstruction on every side, independent of the stable-range step, and it sees what $x$ cannot: on the lens spaces $L^{2n+1}(4)$ the class $x$ always squares to zero, but the order of $1 - \xi$ in the known K-ring grows with $n$. A ring map to the Gaussian integers modulo a power of $1 + I$ (with $I$ the GA unit $e_1e_2$) sends $1 - \xi$ to $2$ and gives the bound $k \geq 1 + \lfloor n/2 \rfloor$ in every dimension; an exact lattice computation gives the sharper $1 + \lfloor (n+1)/2 \rfloor$ up to $n = 8$, which is $3$ already on $L^{7}(4)$.

The walls are explicit: on the unit sphere of $\HH^{r}$, with the $\mathbb{Z}_{4}$ generated by left multiplication by the rotor bivector $B = e_2e_3$, left multiplication by $e_3e_1$, which anticommutes with $B$, is a unit tangent field that changes sign under the generator, so its span descends to the twisted line inside $T^*\Sig$; collapsing the metric along it, with a time direction of either sign, gives tame walls with either kind of physical side. On $L(4,1)$ the bound is $2$, matching the stored completion, so the obstruction only begins to bite in dimension seven; it says nothing on $L^{5}(4)$. The result answers the first attack item in the negative: the rung count of a tame wall of dimension at least seven with an indefinite side is not the mod-2 height, and is not bounded by any function of it. All of this assumes the tame-wall setting of the parent claim.

## lay
At a wall where the geometry changes signature in the well-behaved way the series assumes, an earlier result counted the extra pairs of directions needed to repair the wall: at least the number of times the twist of the dying direction can be multiplied by itself before it vanishes, and on one small three-dimensional example exactly that many. This result shows that in higher dimensions the count can be much larger. On a family of walls shaped like lens spaces the twist always vanishes after two multiplications, yet the repair needs at least three extra pairs in seven dimensions, four in eleven, five in fifteen, and more without limit as the dimension grows. The extra cost is invisible to the usual mod-2 bookkeeping and is read off from the K-theory of the wall, an algebra of bundles; it applies whatever the signature on the physical side.

## one-liner
Assuming the tameness hypotheses, a $k$-rung completion forces $2^{k-1}(1 - \xi) = 0$ in the K-theory of the wall ($\xi$ the complexified dying line), on every side; on lens-space walls $L^{2n+1}(4)$, where $\operatorname{ht}(w_1\shL) = 2$, this gives $k \geq 1 + \lfloor n/2 \rfloor$ (and $k \geq 3$ in dimension seven), so the rung count is not bounded by the mod-2 height.
