---
id: dark-matter.nesting
kind: claim
version: 3
title: The nesting
status: proved
region: dark-matter
subject: dark-matter
tags: [towers-by-residue]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.functoriality@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_slices_are_subalgebras
- kind: check
  ref: check.py::check_ball_sections
- kind: check
  ref: check.py::check_sphere_sections_and_measures
locators:
  paper: T14
  number: Prop 7.1
  label: prop:nesting
  line: 728
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.functoriality where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the slice relations in Cl(1,4), Cl(1,3), Cl(4,1), Cl(3,1), the ball and sphere sections on rational points, and the hat-box identity. Version 1 -> 2.'
  env: proposition
  unresolved_refs:
  - rem:forms
  typing:
    by: ai-typing-pass
    note: No edges; the result is direct computation.
---

## formal
Let $H' \subset \R^{4}$ be the hyperplane $x_{4} = 0$.
\begin{enumerate}
\item[(i)] (Algebra.) In $\Cl(1,4)$ the generators $e_{0}, \ldots, e_{3}$ satisfy the relations of $\Cl(1,3)$: this world's algebra is the slice of the residue-$5$ tower's algebra on which the fifth generator is dropped. In $\Cl(1,3)$ the generators $e_{0}, e_{1}, e_{2}$ satisfy those of $\Cl(1,2)$. The mirror chain is the same with the signatures reversed.
\item[(ii)] (Balls of space.) $\B^{4} \cap H' = \B^{3}$ and $\B^{3} \cap \{x_{3} = 0\} = \B^{2}$: our unit ball of space is the equatorial section of the five-dimensional tower's four-ball of space, and the three-dimensional tower's disc of space is the equatorial section of our ball.
\item[(iii)] (Spheres of spacetime.) In $\R^{6} \supset \R^{5} \supset \R^{4}$, $\Sph^{5} \cap \{x_{6} = 0\} = \Sph^{4}$ and $\Sph^{4} \cap \{x_{5} = 0\} = \Sph^{3}$: each world's spacetime sphere is the equator of the next world's. The balls of (ii) carry the space dimension $D$, the spheres of (iii) the spacetime dimension $n = D + 1$, and the hat-box identity of Remark \ref{rem:forms} links the measures of the two.
\end{enumerate}

## technical
Algebraically, in $\Cl(1,4)$ the generators $e_{0}, \ldots, e_{3}$ satisfy the relations of $\Cl(1,3)$, and in $\Cl(1,3)$ the generators $e_{0}, e_{1}, e_{2}$ satisfy those of $\Cl(1,2)$: this world's algebra is the slice of the five-dimensional tower's with the fifth generator dropped, and the three-dimensional tower's is a slice of ours, the mirror chain being the same with signatures reversed.

Geometrically, with $H'$ the hyperplane $x_{4} = 0$, $\B^{4} \cap H' = \B^{3}$ and $\B^{3} \cap \{x_{3} = 0\} = \B^{2}$, so each unit ball of space is the equatorial section of the next; and $\Sph^{5} \cap \{x_{6} = 0\} = \Sph^{4}$, $\Sph^{4} \cap \{x_{5} = 0\} = \Sph^{3}$, so each spacetime sphere is the equator of the next. The balls carry the space dimension $D$ and the spheres the spacetime dimension $n = D + 1$.

## lay
The hidden worlds fit inside one another like nested slices. Our world's algebra is what remains of a five-dimensional world's when one direction is dropped, and a three-dimensional world's is what remains of ours. The same holds for the geometry: our unit ball of space is the equator of the larger world's ball, and so on down the chain.

## one-liner
This world's algebra, unit ball of space and spacetime sphere are equatorial slices of the five-dimensional tower's, and the three-dimensional tower's are slices of ours, with the mirror chain the same under signature reversal.
