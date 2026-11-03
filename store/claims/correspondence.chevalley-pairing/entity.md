---
id: correspondence.chevalley-pairing
kind: claim
version: 4
title: "The Chevalley pairing"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors, spinor-modules]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:lem:chevalley
- kind: check
  ref: check.py::check_vanishing_and_perfect_on_chiralities
- kind: check
  ref: check.py::check_antisymmetry
- kind: check
  ref: check.py::check_vectors_self_transpose
- kind: check
  ref: check.py::check_bivectors_infinitesimally_invariant
locators:
  paper: T09
  number: Lem 3.3
  label: lem:chevalley
  line: 376
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Chevalley pairing on the Fock model: vanishing on equal chiralities, perfect on CS- x CS, antisymmetric, vectors self-transpose, orthogonal bivectors skew. Version 2 -> 3. Check strengthened: sample inputs moved to module level and the values the mutation test could not see pinned. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: No edges; the pairing is classical (Chevalley) but no imported claim for it is in the store,
      so no standard route.
  source_title: "The Chevalley pairing"
  source_formal: |-
    Define $B(x, y) := \operatorname{top}\bigl(\alpha(x) \wedge y\bigr)$ for $x, y \in \Lambda^\bullet W$. Then:
    \begin{enumerate}
    \item $B$ vanishes on $\T \times \T$ and on $\T' \times \T'$, and restricts to a perfect pairing between $\T$ and $\T'$;
    \item $B$ is antisymmetric: $B(y,x) = -B(x,y)$ for all $x, y$;
    \item every vector is $B$-self-transpose: $B\bigl(c(v)x,\, y\bigr) = B\bigl(x,\, c(v)y\bigr)$ for all $v \in V_\C$;
    \item $B$ is infinitesimally $\mathrm{Spin}$-invariant: for the bivector $\beta_{uv} := \tfrac12 c(u)c(v)$ with $\ip{u}{v} = 0$, $B(\beta_{uv}x, y) + B(x, \beta_{uv}y) = 0$.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor and dual twistor space to the conformal spinor space and its opposite chirality (\\CS, \\CSm) in the statement and proof. The complexified Fock model ($\\Lambda^\\bullet W$, $V_\\C$) is kept as it stands, since $I_6$ anticommutes with vectors and so cannot serve as the complex unit of $V_\\C$."
---

## formal
Define $B(x, y) := \operatorname{top}\bigl(\alpha(x) \wedge y\bigr)$ for $x, y \in \Lambda^\bullet W$. Then:
\begin{enumerate}
\item $B$ vanishes on $\CS \times \CS$ and on $\CSm \times \CSm$ (the conformal spinor space $\CS = \Lambda^{\mathrm{even}}W$ and its opposite chirality $\CSm = \Lambda^{\mathrm{odd}}W$; twistor and dual twistor space), and restricts to a perfect pairing between $\CS$ and $\CSm$;
\item $B$ is antisymmetric: $B(y,x) = -B(x,y)$ for all $x, y$;
\item every vector is $B$-self-transpose: $B\bigl(c(v)x,\, y\bigr) = B\bigl(x,\, c(v)y\bigr)$ for all $v \in V_\C$;
\item $B$ is infinitesimally $\mathrm{Spin}$-invariant: for the bivector $\beta_{uv} := \tfrac12 c(u)c(v)$ with $\ip{u}{v} = 0$, $B(\beta_{uv}x, y) + B(x, \beta_{uv}y) = 0$.
\end{enumerate}

## technical
On the Fock module $\Lambda^\bullet W$ let $\alpha$ act on $\Lambda^k W$ by $(-1)^{k(k-1)/2}$ and let $\operatorname{top}$ take the coefficient of the top form $w_1\wedge w_2\wedge w_3$; the Chevalley pairing is $B(x,y) = \operatorname{top}(\alpha(x)\wedge y)$. It vanishes on $\CS\times\CS$ and on $\CSm\times\CSm$, restricts to a perfect pairing between $\CS$ and $\CSm$, and is antisymmetric, $B(y,x) = -B(x,y)$.

Every vector is self-transpose, $B(c(v)x, y) = B(x, c(v)y)$ for $v \in V_\C$, and each bivector $\beta_{uv} = \tfrac12 c(u)c(v)$ with $\ip{u}{v} = 0$ is skew, $B(\beta_{uv}x, y) + B(x, \beta_{uv}y) = 0$: the pairing is infinitesimally $\Spin$-invariant.

## lay
The spinor space of the completion carries a natural way, due to Chevalley, of pairing two spinors to give a number. This result fixes all its signs: it pairs the two chirality halves with each other, it changes sign when the two inputs are swapped, and it is compatible with the action of vectors and of the infinitesimal symmetries.

## one-liner
The Chevalley pairing on the Fock module pairs the two chiralities perfectly, is antisymmetric, makes every vector self-transpose and is infinitesimally $\Spin$-invariant.
