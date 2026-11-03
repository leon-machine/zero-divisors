---
id: dark-matter.direction-nesting-adds-algebra
kind: claim
version: 3
title: The direction a nesting adds, in the algebra
status: proved
region: dark-matter
subject: dark-matter
tags: [pseudoscalar-and-centre, towers-by-residue]
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
  - dark-matter.nesting@3
  - dark-matter.type-residue-what-each-tower-can@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_residue_five
- kind: check
  ref: check.py::check_residue_three
- kind: check
  ref: check.py::check_residue_seven
- kind: check
  ref: check.py::check_residue_one
locators:
  paper: T14
  number: Lem 7.11
  label: lem:fifth
  line: 876
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the four nestings in GA: centrality and squares of omega, P^2 = -1, the added direction as +-P^-1 omega or +-omega^-1 P, the central idempotents and the reflection. Version 2 -> 3.'
  env: lemma
  context_refs:
  - dark-matter.nesting
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.nesting
    note: 'Added the nesting proposition because the lemma is stated on its four slices and takes from
      it that each smaller algebra sits inside the larger. Levels pass: the lay level no longer says the
      lemma places particles on a side; it now says the sign names a side and that sourcing on that side
      is clause S.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.nesting
---

## formal
Write $P$ for the even world's pseudoscalar, the ordered product of its generators, and $\omega$ for the central volume element of the odd tower. In the four nestings of Proposition \claimref{dark-matter.nesting}(i):
\begin{enumerate}
\item[(i)] (Residue $5$, $\Cl(1,4) \supset \Cl(1,3)$.) $\omega = e_{0}e_{1}e_{2}e_{3}e_{4}$ is central with $\omega^{2} = +1$, $P = e_{0}e_{1}e_{2}e_{3}$ has $P^{2} = -1$, and the fifth direction is
\[
e_{4} \;=\; P^{-1}\omega .
\]
Reversing our orientation, $P \mapsto -P$ with $\omega$ fixed, reverses $e_{4}$. The central idempotents $\tfrac{1}{2}(1 \pm \omega)$ cut out the two simple components on which the two irreducible modules live (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(iv)), and $e_{4}$ acts on them as $\pm P^{-1}$. The reflection through our world, $x_{4} \mapsto -x_{4}$, fixes $P$ and sends $\omega \mapsto -\omega$: it exchanges the two components.
\item[(ii)] (Residue $3$, $\Cl(4,1) \supset \Cl(3,1)$.) The mirror's algebra is the slice $\{e_{0}, e_{1}, e_{2}, e_{4}\}$ with $P = e_{0}e_{1}e_{2}e_{4}$, $P^{2} = -1$; $\omega^{2} = -1$, one module; the added direction is $e_{3} = -P^{-1}\omega$, reversed by $P \mapsto -P$.
\item[(iii)] (Residue $7$, $\Cl(1,2) \subset \Cl(1,3)$.) $\omega = e_{0}e_{1}e_{2}$ is central in the slice with $\omega^{2} = -1$, and the direction the three-dimensional tower lacks is $e_{3} = \omega^{-1}P$.
\item[(iv)] (Residue $1$, $\Cl(2,1) \subset \Cl(3,1)$.) The slice is $\{e_{0}, e_{1}, e_{3}\}$, $\omega = e_{0}e_{1}e_{3}$ is central in it with $\omega^{2} = +1$, two modules, and the lacking direction is $e_{2} = -\omega^{-1}P$.
\end{enumerate}
These are identities: $\omega$ is the ordered product $P e_{4}$ (or $\omega_{3}e_{3}$), so each equation restates the ordering, and its sign under $P \mapsto -P$ is immediate. What they fix is the meaning of a side: given the even world's orientation, the sign of $\omega$ is the sign of the direction the nesting adds or removes. Where $\omega^{2} = +1$ (residues $5$ and $1$) that sign is a label a quantum carries, its simple component; where $\omega^{2} = -1$ (residues $3$ and $7$) $-\omega$ is the conjugate complex structure on the same real module, and the sign is a convention for the tower as a whole. The lemma supplies no half-space: that a quantum sources on the side its sign names is clause S.

## technical
In each nesting of an odd tower's algebra with an even world's, write $P$ for the even world's pseudoscalar and $\omega$ for the odd algebra's central volume element. For the five-dimensional tower over ours, $\Cl(1,4) \supset \Cl(1,3)$, $\omega = e_{0}e_{1}e_{2}e_{3}e_{4}$ with $\omega^{2} = +1$, $P^{2} = -1$, and the fifth direction is $e_{4} = P^{-1}\omega$. It reverses when our orientation does, acts as $\pm P^{-1}$ on the two simple components cut out by $\tfrac{1}{2}(1 \pm \omega)$, and the reflection through our world exchanges those components. The other nestings give $e_{3} = -P^{-1}\omega$ over the mirror ($\omega^{2} = -1$), $e_{3} = \omega^{-1}P$ for the three-dimensional tower in ours ($\omega^{2} = -1$) and $e_{2} = -\omega^{-1}P$ in the mirror ($\omega^{2} = +1$).

These are identities restating the order of the generators. What they fix is the meaning of a side: given the even world's orientation, the sign of $\omega$ is the sign of the direction the nesting adds or removes. Where $\omega^{2} = +1$ that sign is a label each quantum carries, its simple component; where $\omega^{2} = -1$ it is a convention for the tower as a whole. The lemma supplies no half-space; sourcing on the named side is a separate clause.

## lay
When a world with one more or one fewer dimension is nested against ours, the extra direction can be written in the algebra as a product of our volume element and the other world's. Reversing our orientation reverses that direction, so the sign of the other world's volume element names a side of our world. Whether a particle actually acts from the side its sign names is a separate clause (clause S), not part of this result. In some nestings each particle carries the sign; in others it is only a convention for the whole hidden world.

## one-liner
In each nesting the direction added or removed is the product of the even world's pseudoscalar and the odd tower's central volume element $\omega$, so the sign of $\omega$ names a side: a label per quantum where $\omega^{2} = +1$ and a whole-tower convention where $\omega^{2} = -1$.
