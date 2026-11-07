---
id: std-algebra.square-roots-of-minus-one
kind: claim
version: 2
title: Square roots of -1
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- clifford-classification
- classification
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
derivations:
- name: main
  uses:
  - std-algebra.periodicity@1
  - std-algebra.complexification@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_spacetime_roots_all_conjugate_to_I
- kind: check
  ref: check.py::check_three_classes_in_pauli_algebra
- kind: check
  ref: check.py::check_existence_by_signature
locators:
  sources:
  - key: HitzerAblamowiczSangwine2013
    locator: the classification of square roots of -1
outside_ga:
  kind: other
  why: 'the classification is over the abstract matrix algebras Mat_m(C) and Mat_m(H): the eigenvalues +-i and the quaternion unit (through R_i) are scalars of those algebras, not elements of a Clifford algebra standing for a pseudoscalar'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the classification is over the abstract matrix algebras Mat_m(C) and Mat_m(H): the eigenvalues +-i and the quaternion unit (through R_i) are scalars of those algebras, not elements of a Clifford algebra standing for a pseudoscalar.'
  referee_fixes: '2026-10-26: D = H case: f is left (not right) multiplication by -i on coordinates (referee part 2, point 2).'
  by: algebra-core-2026-10-26
---

## formal
Let $A$ be a real algebra $\Mat_m(D)$, $D \in \{\R, \C, \HH\}$. The elements $f \in A$ with $f^{2} = -1$, up to conjugation $f \mapsto g f g^{-1}$ by invertible $g \in A$, are:
\begin{itemize}
\item $D = \R$: none if $m$ is odd; one class if $m$ is even;
\item $D = \C$: $m + 1$ classes, $f$ being conjugate to $\operatorname{diag}(\mathrm{i} 1_k, -\mathrm{i} 1_{m-k})$ for exactly one $k \in \{0, \dots, m\}$;
\item $D = \HH$: one class.
\end{itemize}
In $A \oplus A$ the classes are the pairs of classes. Consequently (\claimref{std-algebra.periodicity}) a nondegenerate $\Cl(p,q)$ contains a square root of $-1$ unless $(p, q) \in \{(0,0), (1,0)\}$; in $\Cl(1,3) \cong \Mat_2(\HH)$ every square root of $-1$, for example a unit spacelike vector or the pseudoscalar $I$, is conjugate to $I$; and in $\Cl(3,0) \cong \Mat_2(\C)$ there are three classes, those of $\omega$, $-\omega$ and $e_1e_2$, separated by $\langle f \omega^{-1} \rangle_0 \in \{1, -1, 0\}$.

## technical
How many essentially different square roots of $-1$ an algebra has depends only on its type. A real matrix algebra has them only in even size and then they are all alike; a complex matrix algebra has one class for each way of splitting the space into $+i$ and $-i$ eigenspaces; a quaternionic matrix algebra has exactly one class. Read through the classification of Clifford algebras this settles the question for every signature; the full classification for every $\Cl(p,q)$, with the centralisers, is in Hitzer, Ablamowicz and Sangwine.

## lay
Many elements of a Clifford algebra square to minus one and so behave like the imaginary unit. In some algebras they are all the same up to a change of viewpoint; in others they come in a few distinct kinds. In the algebra of space-time they are all alike.

## one-liner
Square roots of $-1$ in $\Mat_m(\R)$, $\Mat_m(\C)$, $\Mat_m(\HH)$ form $1$ (if $m$ even, else $0$), $m + 1$ and $1$ conjugacy classes; so in $\Cl(1,3)$ all are conjugate to $I$.
