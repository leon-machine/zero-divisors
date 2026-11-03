---
id: interior.stabilisers-flat-model
kind: claim
version: 5
title: Stabilisers in the flat model
status: proved
region: interior
subject: einstein
tags: [conformal-model, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.bivector-lie-algebra@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:4.3
- kind: check
  ref: check.py::check_vector_stabiliser_is_poincare
- kind: check
  ref: check.py::check_ray_stabiliser_is_maximal_parabolic
- kind: check
  ref: check.py::check_nilradical_null_shears_and_translations
locators:
  paper: T06
  number: Prop 4.3
  label: prop:flatstab
  line: 478
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.bivector-lie-algebra where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in Cl(2,4) the stabiliser of ninf is computed (dimension 10 = Lambda^2 W + ninf ^ W, abelian ideal, Poincare) and of its ray (11, maximal: adding any n0 ^ e_i generates all 15); N = ninf ^ w has N^2(v) = -(ninf . v) Q(w) ninf and N^3 = 0, two-step iff Q(w) != 0, and exp(tN) X(x) = X(x - t w). Version 2 -> 3. Sample inputs moved to module level; no change to what is tested. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'The element-level no-go theorem in context_refs is cited only to identify the shears with its transvections, not as a premise of the stabiliser computation, so it was not added.'
  env: proposition
  context_refs:
  - transport.no-go-level-elements
  eqrefs: 2
---

## formal
Fix the null vector $\nInf$ and a second null vector $\nO := (1,0,0)$ with $\ip{\nInf}{\nO} = 1$, and let $W := \{\nInf, \nO\}^\perp \cong \R^{1,3}$. Decompose $\Lambda^2 V = \R\,(\nInf \wedge \nO) \oplus \Lambda^2 W \oplus (\nInf \wedge W) \oplus (\nO \wedge W)$. Then:
\begin{enumerate}
\item the stabiliser subalgebra of the vector $\nInf$ is $\Lambda^2 W \oplus (\nInf \wedge W) \cong \mathfrak{so}(1,3) \ltimes \R^4$, the Poincar\'e algebra, of dimension $10$;
\item the stabiliser subalgebra of the ray $\R^+\nInf$ adds the grading element $\nInf \wedge \nO$ and is the $11$-dimensional maximal parabolic $\mathfrak{p} = (\mathfrak{so}(1,3) \oplus \R) \ltimes \R^4$;
\item the nilradical $\nInf \wedge W$ acts on the point space \eqref{eq:flatembed} as the translations, and on $V$ by null shears: for $w \in W$, $(\nInf \wedge w)^2(V) \subseteq \R\,\nInf$ and $(\nInf \wedge w)^3 = 0$, the nilpotency being two-step exactly for non-null $w$ and one-step for null $w$, since $(\nInf \wedge w)^2(v) = -\ip{\nInf}{v}\,Q(w)\,\nInf$. These are precisely the transvections that obstruct the element-level completion in \cite[Thm.~4.2]{ButlerT1}.
\end{enumerate}

## technical
Fix null vectors $\nInf$ and $\nO$ with $\ip{\nInf}{\nO} = 1$ and let $W = \{\nInf, \nO\}^\perp \cong \R^{1,3}$, so that $\Lambda^2 V = \R(\nInf\wedge\nO) \oplus \Lambda^2 W \oplus (\nInf\wedge W) \oplus (\nO\wedge W)$. The stabiliser of the vector $\nInf$ is $\Lambda^2 W \oplus (\nInf\wedge W)$, the ten-dimensional Poincar\'e algebra; adding the grading element $\nInf\wedge\nO$ gives the eleven-dimensional maximal parabolic that stabilises the ray.

The nilradical acts on the point space as translations, $e^{tN}X(x) = X(x - tw)$ for $N = \nInf\wedge w$, and on $V$ by null shears with $N^2(v) = -\ip{\nInf}{v}\,Q(w)\,\nInf$ and $N^3 = 0$: two-step nilpotent for non-null $w$, one-step for null $w$. These shears are the transvections that obstruct the element-level completion.

## lay
In the flat model of the series' six-dimensional ambient space, the point at infinity is a direction of zero length. The symmetries that fix it are exactly those of flat spacetime, Lorentz transformations and translations, ten in all, with one extra rescaling if only its direction must be kept. The translations act as shears that tilt everything towards the point at infinity, and they are the same shears that block the naive way of dividing by zero.

## one-liner
In the flat model the stabiliser of the null vector $\nInf$ is the Poincar\'e algebra, that of its ray is the eleven-dimensional maximal parabolic, and the nilradical acts as translations through null shears.
