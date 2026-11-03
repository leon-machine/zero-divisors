---
id: correspondence.ordering-filtration
kind: claim
version: 3
title: "The ordering filtration"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors]
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
  uses:
  - correspondence.symmetrised-quadratics-palatial-algebra@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_quadratic_ambiguities_are_central
- kind: check
  ref: check.py::check_cubic_ambiguities_are_linear
- kind: check
  ref: check.py::check_quartic_ambiguities_and_balanced_mixed
- kind: check
  ref: check.py::check_balanced_discrepancy_is_q_of_commutator
locators:
  paper: T09
  number: Lem 6.7
  label: lem:quartic
  line: 823
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: normal ordering in the palatial algebra with formal hbar: degree <= 2 discrepancies central (4 of 45), degree 3 linear (32 of 120), degree 4 hbar-quadratic plus hbar^2 scalar with mixed balanced parts equal to q(M) up to centre (58 of 100), and [q(M), q(N)] = hbar q([M, N]). Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: Kept the single edge to the symmetrised-quadratics lemma, which the proof uses directly.
  source_title: "The ordering filtration"
  source_formal: |-
    Grade $\mathcal{P}$ by total degree in the generators. Then:
    \begin{enumerate}
    \item any two orderings of a monomial of degree $\le 2$ differ by an element of $\hbar\,\C$: quadratic ordering ambiguities are central scalars and carry no tensorial information;
    \item any two orderings of a monomial of degree $4$ differ by $\hbar\,(\text{a quadratic}) + \hbar^2\,\C$; for a \emph{balanced} monomial (two $Z$'s and two $\bar Z$'s) the quadratic is a mixed one, i.e.\ of the form $q(M) + \hbar\C$ with $M \in \mathfrak{gl}(\T)$, and the ordering discrepancy of a product $q(M)q(N)$ of symmetrised quadratics taken in the two orders is $[q(M), q(N)] = \hbar\,q([M,N])$: balanced quartic ordering ambiguities are valued, through $q$, in $\mathfrak{gl}(\T)$, which contains the conformal algebra $\mathfrak{so}(2,4)_\C \cong \mathfrak{sl}(\T)$;
    \item quartic order is the \emph{first} at which an ordering ambiguity can be $\mathfrak{gl}(\T)$-valued.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space to the conformal spinor space \\CS in all levels and the proof; Penrose's palatial algebra keeps its name, and the lay level describes it without the word twistor."
---

## formal
Grade $\mathcal{P}$ by total degree in the generators. Then:
\begin{enumerate}
\item any two orderings of a monomial of degree $\le 2$ differ by an element of $\hbar\,\C$: quadratic ordering ambiguities are central scalars and carry no tensorial information;
\item any two orderings of a monomial of degree $4$ differ by $\hbar\,(\text{a quadratic}) + \hbar^2\,\C$; for a \emph{balanced} monomial (two $Z$'s and two $\bar Z$'s) the quadratic is a mixed one, i.e.\ of the form $q(M) + \hbar\C$ with $M \in \mathfrak{gl}(\CS)$, and the ordering discrepancy of a product $q(M)q(N)$ of symmetrised quadratics taken in the two orders is $[q(M), q(N)] = \hbar\,q([M,N])$: balanced quartic ordering ambiguities are valued, through $q$, in $\mathfrak{gl}(\CS)$, with $\CS$ the conformal spinor space (twistor space), which contains the conformal algebra $\mathfrak{so}(2,4)_\C \cong \mathfrak{sl}(\CS)$;
\item quartic order is the \emph{first} at which an ordering ambiguity can be $\mathfrak{gl}(\CS)$-valued.
\end{enumerate}

## technical
Grade the palatial algebra $\mathcal{P}$ by total degree in the generators $Z^\alpha$, $\bar Z_\beta$. Two orderings of a monomial of degree at most two differ by an element of $\hbar\,\C$, a central scalar with no tensorial content. Two orderings of a degree-four monomial differ by $\hbar$ times a quadratic plus an element of $\hbar^2\C$; for a balanced monomial, with two $Z$s and two $\bar Z$s, the quadratic is $q(M) + \hbar\C$ with $M \in \mathfrak{gl}(\CS)$, and the discrepancy of $q(M)q(N)$ taken in the two orders is $[q(M), q(N)] = \hbar\,q([M,N])$.

So balanced quartic ordering ambiguities are valued, through $q$, in $\mathfrak{gl}(\CS)$, which contains the conformal algebra $\mathfrak{so}(2,4)_\C \cong \mathfrak{sl}(\CS)$, and quartic order is the first at which an ordering ambiguity can be $\mathfrak{gl}(\CS)$-valued.

## lay
In Penrose's palatial algebra, a noncommutative algebra of operators built on the conformal spinor coordinates, changing the order in which operators are multiplied can change the answer. For products of one or two operators the change is only a fixed number and carries no geometric information. Products of four operators are the first where the change can be a matrix-valued quantity of the same type as the conformal symmetries of spacetime.

## one-liner
In the palatial algebra, ordering ambiguities are central scalars up to quadratic order, and balanced quartic monomials are the first whose ordering ambiguities are valued in $\mathfrak{gl}(\CS)$, which contains the conformal algebra.
