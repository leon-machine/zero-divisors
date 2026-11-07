---
id: odd-extensions.exceptional-algebra-residue-completion-both-sides
kind: claim
version: 4
title: Exceptional algebra, residue, and the completion on both sides
status: proved
region: odd-extensions
subject: walls
tags: [cosmological-constant, degenerate-algebras, frozen-point]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
derivations:
- name: main
  uses:
  - odd-extensions.are-ascents-pair-signed@4
  - odd-extensions.imported-frozen-point@6
  - odd-extensions.imported-minimal-completion-degenerate-algebra-rule@5
  - odd-extensions.imported-tame-walls-exceptional-algebra-residue@4
  - odd-extensions.line-tame-wall@4
  - odd-extensions.transport-constrains-frozen-point-only-through@3
  - standard-model.imported-frozen-point-dictionary@8
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_rescaled_family_and_exceptional_algebras
- kind: check
  ref: check.py::check_residue_and_stelle_west_norm
- kind: check
  ref: check.py::check_completion_on_both_sides
- kind: check
  ref: check.py::check_complement_switches_sign
locators:
  paper: T14a
  number: Thm 10.3
  label: thm:lambdawall
  line: 750
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: rescaled family and exceptional signatures (2,3) and (1,4), Lambda (G^-1)_ww = -3 and the residue, the (2,4) completion and the general (p,q) model, and the switching complement. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: theorem
  context_refs:
  - odd-extensions.imported-frozen-point-degenerate-algebras
  outside_pilot_cites:
  - ButlerT12
  typing:
    by: ai-typing-pass
    note: 'Edges kept as extracted, all used in the proof; the frozen-point fact at Lambda = 0 is named
      in (ii) only as the identity the pole is one step from, while the proof draws the norm from the
      other frozen-point fact, so it was not added. Levels pass: conditions already kept; per review item
      14 the technical level now writes Q(V) and Q(I_Lambda) for the vector squares.'
---

## formal
For the tame wall of Proposition \claimref{odd-extensions.line-tame-wall}:
\begin{enumerate}
\item[(i)] the sheaf paper's rescaling of the dying direction, $w_{\Lambda} \mapsto w_{\Lambda}/\sqrt{|\Lambda|}$, is proportional, by the fixed factor $\sqrt 3$, to the dark-energy paper's normalisation of the Stelle-West vector to unit length, $e_{V} = V/|V|$, both being normalisations of the same line; the exceptional algebra at the wall is the Lorentz frame orthogonal to the rate of degeneration, $\Cl(1,3) \perp \langle +\tfrac13\rangle \cong \Cl(2,3)$ approached from $\Lambda < 0$ and $\Cl(1,3) \perp \langle -\tfrac13\rangle \cong \Cl(1,4)$ from $\Lambda > 0$, the cross terms vanishing identically so that the rescaled family is exactly, not asymptotically, block diagonal;
\item[(ii)] the residue of the inverse form at the wall is $-3\,w_{0} \otimes w_{0}$, the coefficient fixed by the normalisation $Q(w_{\Lambda}) = -\Lambda/3$: the pole is the Stelle-West norm, $\Lambda\,Q(V) = -3$, one algebraic step from the imported identity of Fact \claimref{odd-extensions.imported-frozen-point-degenerate-algebras}; the sheaf paper's identification $N^{*}\Sigma \cong L^{\otimes 2}$ reads $d\Lambda \cong -3\, w_{0} \otimes w_{0}$, which is $-3\,I_{0} \otimes I_{0}$ when $a(0)^{2} = 1$, so the dying direction carries the weight of $|\Lambda|^{1/2}$ and the weightless normalisation of the frozen point's complement is by $\sqrt{|\Lambda|/3}$, which for $\Lambda > 0$ is the asymptotic de Sitter rate $H = \sqrt{\Lambda/3}$, the series' $H^{2} = Q(I)$;
\item[(iii)] the rung, with its tractor metric of constant signature $(2,4)$, is a nondegenerate completion of the family on both sides of the wall, of rank one more, the completing direction at the wall being the partner $\varphi$ and away from it the frozen point $I_{\Lambda}$ itself; this is not particular to the cosmological constant: for any $(p,q)$ the family of hyperplanes $\mathrm{span}(f_{1}, \ldots, f_{n}, u + \tfrac{t}{2}v)$ of $\R^{p,q} \perp H$, $H$ hyperbolic with null basis $u, v$, $\ip{u}{v} = 1$, is a tame corank-one family with dying eigenvalue $t$ completed on both sides by the fixed $(p+1,q+1)$, and the $\Lambda$ family is this model with $(p,q) = (1,3)$, $u = I_{0}$, $v = \varphi$, $t = -\Lambda/3$;
\item[(iv)] this does not contradict the conservation of degeneracy, and lies in the case its proof excludes by hypothesis: the complement of $I_{\Lambda}^{\perp}$ in the rung is $\mathrm{span}(I_{\Lambda})$ with $K = Q(I_{\Lambda}) = \Lambda/3$, whose signature is $(1,0)$ on one side and $(0,1)$ on the other, so the completion is not standard in the sense of Fact \claimref{odd-extensions.imported-tame-walls-exceptional-algebra-residue}, and the totals $(2,3) + (0,1) = (1,4) + (1,0) = (2,4)$ match because the complement's line changes type across the wall; on the $\Lambda$ line, where the base is contractible and the wall a point, the conservation theorem reduces to the local constancy of a signature and its content is the constancy clause on $K$ alone.
\end{enumerate}

## technical
For the tame wall at $\Lambda = 0$ on the $\Lambda$ line, the rescaling $w_\Lambda \mapsto w_\Lambda/\sqrt{|\Lambda|}$ of the dying direction is proportional, by the factor $\sqrt 3$, to the normalisation $e_V = V/|V|$ of the Stelle-West vector, both normalising the same line. The exceptional algebra is $\Cl(1,3) \perp \langle +\tfrac13\rangle \cong \Cl(2,3)$ from $\Lambda < 0$ and $\Cl(1,3) \perp \langle -\tfrac13\rangle \cong \Cl(1,4)$ from $\Lambda > 0$, the rescaled family being exactly block diagonal. The residue of the inverse form is $-3\,w_0\otimes w_0$, which is the Stelle-West norm $\Lambda\,Q(V) = -3$; the dying direction carries the weight of $|\Lambda|^{1/2}$, and for $\Lambda > 0$ the weightless normalisation $\sqrt{\Lambda/3}$ is the de Sitter rate $H$.

The rung, with its tractor metric of constant signature $(2,4)$, completes the family nondegenerately on both sides with rank one more, the completing direction being the partner $\varphi$ at the wall and the frozen point $I_\Lambda$ away from it. This is a case of a general model in which hyperplanes $\mathrm{span}(f_1, \dots, f_n, u + \tfrac t2 v)$ of $\R^{p,q} \perp H$ are completed on both sides by the fixed $(p+1, q+1)$. There is no conflict with conservation of degeneracy: the complement $\mathrm{span}(I_\Lambda)$ has $Q(I_\Lambda) = \Lambda/3$, which changes sign across the wall, so the completion is not standard in the sense that theorem requires.

## lay
Treating the cosmological constant as a dial, the algebra built from the frozen point degenerates exactly when the dial reads zero, and this result describes that degeneration in detail. On the two sides the limiting algebras are the anti-de Sitter and de Sitter ones, and the strength of the blow-up at the wall is fixed by the same number that sets the length of the Stelle-West vector. One fixed six-dimensional space completes the family on both sides. That looks like a clash with a conservation law for degeneracy, but it is not, because the extra direction changes type across the wall, a case the law excludes by hypothesis.

## one-liner
On the $\Lambda$ line the wall at $\Lambda = 0$ has exceptional algebras $\Cl(2,3)$ and $\Cl(1,4)$ on its two sides and residue $-3\,w_0\otimes w_0$, and the rung of signature $(2,4)$ completes it on both sides, consistently with conservation of degeneracy because the complement changes type across the wall.
