---
id: angle.wedge-reflection-translations-are-ascent
kind: claim
version: 3
title: The wedge reflection and the translations are in the ascent
status: proved
region: angle
subject: thermality
tags: [rotors-and-stabilisers, conformal-model, horizons]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-angle, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - angle.imported-conformal-model-null-rotations@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_boost_rotor
- kind: check
  ref: check.py::check_imaginary_rapidity_is_the_wedge_reflection
- kind: check
  ref: check.py::check_null_rotations_translate_points_in_the_completion
locators:
  paper: T05-angle
  number: Prop 3.1
  label: prop:geometry
  line: 148
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the boost rotor matrix, the imaginary-rapidity rotor iB as the wedge reflection, and T_a as the null rotation translating X(x) in Cl(2,4). Version 2 -> 3.'
  env: proposition
  context_refs:
  - angle.imported-conformal-model-null-rotations
  typing:
    by: ai-typing-pass
    added:
    - angle.imported-conformal-model-null-rotations
    note: 'Added the imported conformal-model fact (from context_refs): clause (iii) identifies the translations
      as its null rotations R_u and uses its representation X(x).'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$\eta = i\pi/2$, $iB$: rapidity continued to a complex parameter, with $i$ a commuting complex scalar
      (complex analysis); $I_{4}$ cannot stand here, since $(I_{4}B)x(I_{4}B)^{\sim}$ is $-BxB$, not $BxB$'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - angle.imported-conformal-model-null-rotations
---

## formal
In $\Cl(1,3)$ with $e_{t}^{2} = +1$ and $e_{r}^{2} = e_{\theta}^{2} = e_{\varphi}^{2} = -1$, let $B = e_{t}e_{r}$ be the horizon's boost plane, the boost member of the singularity paper's curvature-selected pair.
\begin{enumerate}
\item[(i)] $B^{2} = +1$; the rotor $R = \cosh\eta + B\sinh\eta$ at $(\cosh\eta, \sinh\eta) = (\tfrac54, \tfrac34)$ satisfies $R\widetilde{R} = 1$ and acts on $(e_{t}, e_{r})$ by the boost of rapidity $2\eta$, the matrix $\begin{psmallmatrix} 17/8 & -15/8 \\ -15/8 & 17/8\end{psmallmatrix}$, fixing $e_{\theta}$ and $e_{\varphi}$; it rescales the null generators $e_{t} \pm e_{r}$ of the plane by $e^{\mp 2\eta} = \tfrac14, 4$.
\item[(ii)] At boost rapidity $2\eta = i\pi$, that is $\eta = i\pi/2$, the rotor is $iB$, with $(iB)\widetilde{(iB)} = B^{2} = 1$, and its action $x \mapsto BxB$ is $-1$ on the boost plane and $+1$ transverse to it: the reflection through the bifurcation surface. It commutes with the boost and squares to the identity.
\item[(iii)] In the completion $\Cl(2,4)$, for $a$ in the base, $T_{a} = 1 + \tfrac12\nInf a$ is an even element with inverse $1 - \tfrac12\nInf a$, fixes $\nInf$, is the null rotation $R_{u}$ of Fact \claimref{angle.imported-conformal-model-null-rotations} with $v = \nInf$ and $u = \tfrac12 a$, and carries $X(x)$ to $X(x + a)$. The base's boost rotor, read in the completion, fixes $\nO$ and $\nInf$ and carries $X(x)$ to $X(Rx\widetilde{R})$.
\end{enumerate}

## technical
In $\Cl(1,3)$ with $e_{t}^{2} = +1$ and the spatial squares $-1$, the horizon's boost plane $B = e_{t}e_{r}$ has $B^{2} = +1$. The rotor $R = \cosh\eta + B\sinh\eta$ boosts $(e_{t}, e_{r})$ by rapidity $2\eta$ and fixes the transverse directions; at $(\cosh\eta, \sinh\eta) = (\tfrac54, \tfrac34)$ it rescales the null generators $e_{t} \pm e_{r}$ by $\tfrac14$ and $4$. Continued to $\eta = i\pi/2$ the rotor becomes $iB$ and acts by $x \mapsto BxB$, which is $-1$ on the boost plane and $+1$ transverse to it: the reflection through the bifurcation surface, which commutes with the boost and squares to the identity.

In the completion $\Cl(2,4)$, with the conformal model's null vector $X(x)$ and its null rotations, the element $T_{a} = 1 + \tfrac12\nInf a$ for $a$ in the base is the null rotation fixing $\nInf$ with $u = \tfrac12 a$, and it carries $X(x)$ to $X(x + a)$: the translations are in the ascent. The base's boost rotor, read in the completion, fixes $\nO$ and $\nInf$ and carries $X(x)$ to $X(Rx\widetilde{R})$.

## lay
A horizon comes with two pieces of geometry: a reflection that swaps its two sides, and translations along it. This result shows that both are already present in the Clifford-algebra framework. Running the horizon's boost to an imaginary rapidity gives exactly the reflection, and the larger algebra reached by the ascent contains the translations as particular rotations. These are geometric facts only; they say nothing about which quantum state is selected.

## one-liner
The horizon's boost rotor at imaginary rapidity $i\pi$ is the reflection through the bifurcation surface, and the translations are the null rotations $T_{a} = 1 + \tfrac12\nInf a$ of the completion $\Cl(2,4)$.
