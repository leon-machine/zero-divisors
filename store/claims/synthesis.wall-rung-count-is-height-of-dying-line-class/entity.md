---
id: synthesis.wall-rung-count-is-height-of-dying-line-class
kind: claim
version: 2
title: 'A tame wall''s rung count and the height of its dying line''s class'
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, tameness, hyperbolic-plane, no-go]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: consistency pass, torus-wall half-angle sine renamed sigma, freeing s for G^{-1}(u,u)
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - synthesis.wall-class-one-rung-obstruction@3
  - synthesis.twisted-wall-induction-conserves-dying-line-class@2
  - sheaf.one-sided-completion@4
  - sheaf.tame-wall-induction@5
  - sheaf.degeneration-sheaf@6
  - sheaf.wall-gram@3
  - sheaf.imported-real-line-bundles@1
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_wall_block_negative_bundle
- kind: check
  ref: check.py::check_whitney_inverse_forces_height
- kind: check
  ref: check.py::check_torus_two_rung_completion
- kind: check
  ref: check.py::check_twisted_hyperbolic_plane_morita_trivial
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - sheaf.wall-class
  - synthesis.wall-class-one-rung-obstruction
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: "In the proof the torus-wall paragraph wrote the half-angle pair as (c, s) while s is G^{-1}(u,u) in clause (2) and in F; the sine is now sigma, as in synthesis.twisted-wall-induction-conserves-dying-line-class, a pure notation change."
  open_problem: op.wall-class-invariant
  note: >-
    Cross-subject input: stable real line bundles (Whitney product formula, the cohomology ring of
    real projective space, cited from memory to Milnor-Stasheff) and, for the reading of clause (c),
    the graded Brauer group of Donovan and Karoubi (1970, memory, used only in a labelled remark).
    The one-rung necessity argument of synthesis.wall-class-one-rung-obstruction is run with k planes;
    sufficiency confines the twist of the stored twisted coupling to the collar, inside the trivial
    rung bundle, so the dying line need not extend over the physical side. Answers the problem's second
    bullet for k >= 2 and gives clause (c) a definite sense. The bounds can differ (lens space L(4,1)
    at k = 2: the height is 2 while at least 3 rungs are needed when the physical side is definite;
    undecided when it is not). That the Clifford class sees exactly w1(L)^2 in general is the
    Donovan-Karoubi remark, from memory; it is proved here only on the torus wall, where the jump is trivial. Transport-absent: bundle algebra of
    symmetric forms, with the store's wall theory as the only series input.
---

## formal
Let $(M, G)$ be a tame corank-one degeneration (\claimref{sheaf.tameness}) with $\Sig$ compact, separating $M$ into a physical side $\Mp$ of signature $(p,q)$, $p \geq 1$, and a far side, with radical line bundle $\shL \subset T^*M|_\Sig$, $x := w_1(\shL) \in H^1(\Sig; \mathbb{Z}_2)$, and a product collar $C \cong \Sig \times [-1,1]$. For $k \geq 1$ let $T_k := T^*M \oplus \underline{\R}^{2k}$ with $H_k$ the orthogonal sum of $k$ hyperbolic planes on the trivial summand. A \emph{$k$-rung completion} is a smooth symmetric form $h$ on $T_k$ over $\Mp$, nondegenerate at every point of $\Mp$ including $\Sig$, with $h|_{T^*M} = G$ along $\Sig$ and $h = G \perp H_k$ outside $C$.
\begin{enumerate}
\item \emph{(Necessity.)} If a $k$-rung completion exists, there is a vector bundle $N$ of rank $k-1$ over $\Sig$ with $N(\overline G) \oplus \shL \oplus N \cong N(\overline G) \oplus \underline{\R}^{k}$, where $N(\cdot)$ denotes a maximal negative subbundle and $\overline G$ the induced form on $T^*M|_\Sig/\shL$. Hence $w(N) = (1 + x)^{-1}$ and $x^{j} = 0$ for every $j \geq k$.
\item \emph{(Sufficiency.)} If $\shL$ is isomorphic to a subbundle of the trivial bundle $\underline{\R}^{k}$ over $\Sig$, a $k$-rung completion exists. It is the restriction to $\Mp$ of a form on $T_k$ over $M$, standard outside $C$ on both sides, whose far-side shadow wall $\Sig'$ is tame with dying line $\shL' \cong \shL$ under the collar identification; $\shL$ need not extend over $\Mp$.
\item \emph{(Rung count.)} Hence the least $k$ for which a $k$-rung completion exists, $k(\Sig)$, satisfies $\operatorname{ht}(x) \leq k(\Sig) \leq e(\shL) \leq \dim \Sig + 1$, with $\operatorname{ht}(x)$ the least $j$ with $x^{j} = 0$ and $e(\shL)$ the least $k$ with $\shL \hookrightarrow \underline{\R}^{k}$. $k(\Sig) = 1$ iff $x = 0$. On the stored torus wall $x \neq 0 = x^{2}$ and $k(\Sig) = 2$, with an explicit two-rung completion; on $\Sig = \R P^{n}$ with tautological dying line (a tame wall on $\R P^n \times \R$), $k(\Sig) = n + 1$.
\item \emph{(Clause (c).)} Over the collar, $\Cl(T^*M, G)$ on the far side is graded Morita equivalent to $\Cl(T^*M, G)$ on the physical side tensored (graded) with $\Cl(\shL \otimes \R^{0,2})$, because $\Cl(\shL \otimes \R^{1,1})$ has a global primitive idempotent. On the torus wall $\shL \oplus \shL$ is trivial, so this jump is the constant $\Cl(0,2)$ bundle of an untwisted wall: the Clifford sheaves of the two sides do not determine $x$, while $x$ obstructs one rung. So $W(\Sig) = (w(\Sig), x)$ determines the sheaf-level Clifford jump, which depends on $\shL$ only through $\shL \oplus \shL$, and on the torus wall it is strictly finer than that jump.
\end{enumerate}

## technical
The one-rung result showed that $x = w_1$ of the dying line obstructs exactly the completions with one adjoined hyperbolic plane that restrict to $G$ along the wall. This result asks, under the tameness hypotheses, how many planes the torsion costs. The necessity argument is the one-rung argument run with $k$ planes: at the wall, the orthogonal complement of a complement of $\shL$ is a nondegenerate block of rank $2k+1$ containing $\shL$ as an isotropic line, whose negative part is a copy of $\shL$ plus the negative part of $\shL^\perp/\shL$, of rank $k-1$; comparing with the exterior and applying the Whitney product formula gives $x^{j} = 0$ for $j \geq k$. Sufficiency splits the trivial null space $\underline{\R}^k$ of $H_k$ as $\shL \oplus N$ on the collar, so $H_k$ there is a twisted plane on $\shL$ plus a hyperbolic block on $N$, and the stored twisted coupling on the first summand does the rest; the twist lives inside the trivial rung bundle, so nothing has to extend over the physical side, and the shadow wall's dying line is again a copy of $\shL$. On the stored torus wall two rungs suffice, explicitly; on a projective-space wall of dimension $n$ the count is $n+1$.

For clause (c): adding a hyperbolic plane twisted by a line bundle never changes the Clifford sheaf up to graded Morita equivalence, so the change of the Clifford sheaf across the wall is the Clifford bundle of the negative definite plane $\shL \oplus \shL$, and the Clifford sheaves see the dying line only through that plane. On the torus wall this plane is trivial, so there the Clifford sheaves see nothing of the twist that obstructs a single rung. Which part of the twist the Clifford class sees on a general wall is not decided here (by the graded Brauer group of Donovan and Karoubi, cited from memory, it would be $x^{2}$), and $x^{2} = 0$ does not by itself give a two-rung completion.

## lay
At a wall where the geometry changes signature in the well-behaved (tame) way the series assumes, an earlier result showed that one extra pair of directions repairs the wall exactly when the dying direction does not twist like a Moebius band. This result counts how many extra pairs a twisted wall needs. The answer is set by how many times the twist can be multiplied by itself before it vanishes: two pairs for the stored torus example, and up to one more than the wall's dimension in general (four for a three-dimensional wall shaped like real projective space). The twist itself is handed on unchanged to every later wall, but the cost it imposes is absorbed by enough extra directions, while the coarse signature mismatch never is. The Clifford algebras of the two sides see the twist only through the doubled dying direction, and on the torus example they cannot see it at all, so there the twist is a strictly finer invariant than the mod-8 clock read sheaf by sheaf.

## one-liner
Assuming the tameness hypotheses, a completion with $k$ adjoined hyperbolic planes restricting to $G$ along the wall needs $w_1(\shL)^k = 0$ and exists when the dying line sits in a trivial rank-$k$ bundle (two planes for the stored torus wall, $n+1$ for a projective-space wall), and the Clifford sheaves see the dying line only through $\shL \oplus \shL$, which is trivial on the torus wall.
