---
id: odd-extensions.twistor-algebra
kind: claim
version: 6
title: "The even conformal algebra is $\\Cl(2,3)$"
status: proved
region: odd-extensions
subject: conformal-spacetime
tags: [clifford-classification, grading-and-parity, pseudoscalar-and-centre]
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
  - odd-extensions.doubling-or-complexification@5
  - odd-extensions.four-extensions-oriented-pair@5
  - odd-extensions.imported-conformal-completion@5
  - std-algebra.pseudoscalar-commutation@1
  - primer.sign@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_even_subalgebra_is_cl23_cl41_and_mat4c
- kind: check
  ref: check.py::check_both_oriented_shadows_inside_even_subalgebra
- kind: check
  ref: check.py::check_conformal_spinors_are_the_module_of_the_even_subalgebra
- kind: check
  ref: check.py::check_signature_reversal_changes_the_centre
locators:
  paper: T14a
  number: Thm 4.1
  label: thm:rung
  line: 517
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.pseudoscalar-commutation, primer.sign where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Cl^0(2,4) generated as Cl(2,3) and Cl(4,1) and identified with Mat(4,C) by matrix units with omega_6 as complex unit, the two shadows, CS as its module, and the centres separating the reversed odd algebras. Version 3 -> 4. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 4 -> 5.'
  env: theorem
  context_refs:
  - odd-extensions.imported-conformal-completion
  - odd-extensions.imported-copy-theorem-soldered-residue
  typing:
    by: ai-typing-pass
    added:
    - odd-extensions.imported-conformal-completion
    note: 'The conformal-completion fact was added because the hypothesis and clause (iii) (twistor space
      as the module of the even subalgebra) rest on it; the copy-theorem fact was not added, since clause
      (iii) only lists that theorem''s inputs and does not use its conclusion. Levels pass: conditions
      already kept.'
  source_title: "The twistor algebra is $\\Cl(2,3)$"
  source_formal: |-
    Let $\Cl(2,4)$ be the ambient of this world's conformal completion (Fact \claimref{odd-extensions.imported-conformal-completion}). Then:
    \begin{enumerate}
    \item[(i)] $\Cl^{0}(2,4) \cong \Cl(2,3) \cong \Cl(4,1) \cong \Mat(4,\C)$, the two odd algebras being generated inside the even subalgebra by $e_{i}e_{6}$ for a spacelike $e_{6}$ and by $e_{i}e_{1}$ for a timelike $e_{1}$ respectively; the rung's volume element $\omega_{6}$ is even, squares to $-1$ and commutes with every even element, and is the complex unit of $\Mat(4,\C)$;
    \item[(ii)] inside $\Cl^{0}(2,4)$ both oriented shadows occur: the bivectors $e_{i}e_{6}$ for $i = 2, \ldots, 5$ generate a $\Cl(1,3)$ and the bivectors $e_{i}e_{1}$ for $i = 2, \ldots, 5$ generate a $\Cl(3,1)$;
    \item[(iii)] every input to the copy theorem (Fact \claimref{odd-extensions.imported-copy-theorem-soldered-residue}) is an object of $\Cl^{0}(2,4)$ or of its complexified modules, hence of the complexification in which $\Cl(1,3)$ and $\Cl(3,1)$ are two real forms of one algebra;
    \item[(iv)] signature reversal is not an isomorphism of the odd extensions: $\Cl(2,3) \not\cong \Cl(3,2)$ and $\Cl(1,4) \not\cong \Cl(4,1)$, the centre being $\C$ in $\Cl(2,3)$ and $\Cl(4,1)$ and $\R \oplus \R$ in $\Cl(3,2)$ and $\Cl(1,4)$.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Retitled (the algebra acting on the conformal spinor space, formerly the twistor algebra), glossed the rung's volume element as the conformal pseudoscalar $I_6$, and renamed twistor space in the proof and the lay level; the mathematics is unchanged."
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - odd-extensions.imported-conformal-completion
---

## formal
Let $\Cl(2,4)$ be the ambient of this world's conformal completion (Fact \claimref{odd-extensions.imported-conformal-completion}). Then:
\begin{enumerate}
\item[(i)] $\Cl^{0}(2,4) \cong \Cl(2,3) \cong \Cl(4,1) \cong \Mat(4,\C)$, the two odd algebras being generated inside the even subalgebra by $e_{i}e_{6}$ for a spacelike $e_{6}$ and by $e_{i}e_{1}$ for a timelike $e_{1}$ respectively; the rung's volume element $\omega_{6}$ (the conformal pseudoscalar, $I_6$ up to sign) is even, squares to $-1$ and commutes with every even element, and is the complex unit of $\Mat(4,\C)$;
\item[(ii)] inside $\Cl^{0}(2,4)$ both oriented shadows occur: the bivectors $e_{i}e_{6}$ for $i = 2, \ldots, 5$ generate a $\Cl(1,3)$ and the bivectors $e_{i}e_{1}$ for $i = 2, \ldots, 5$ generate a $\Cl(3,1)$;
\item[(iii)] every input to the copy theorem (Fact \claimref{odd-extensions.imported-copy-theorem-soldered-residue}) is an object of $\Cl^{0}(2,4)$ or of its complexified modules, hence of the complexification in which $\Cl(1,3)$ and $\Cl(3,1)$ are two real forms of one algebra;
\item[(iv)] signature reversal is not an isomorphism of the odd extensions: $\Cl(2,3) \not\cong \Cl(3,2)$ and $\Cl(1,4) \not\cong \Cl(4,1)$, the centre being $\C$ in $\Cl(2,3)$ and $\Cl(4,1)$ and $\R \oplus \R$ in $\Cl(3,2)$ and $\Cl(1,4)$.
\end{enumerate}

## technical
For the ambient $\Cl(2,4)$ of the conformal completion, the even subalgebra satisfies $\Cl^0(2,4) \cong \Cl(2,3) \cong \Cl(4,1) \cong \Mat(4, \C)$, generated by the $e_ie_6$ for a spacelike $e_6$ or by the $e_ie_1$ for a timelike $e_1$. The volume element $\omega_6$ is even, central there, satisfies $\omega_6^2 = -1$, and is the complex unit. Inside it the $e_ie_6$ ($i = 2, \dots, 5$) generate a $\Cl(1,3)$ and the $e_ie_1$ a $\Cl(3,1)$, so both oriented shadows occur, and every input of the copy theorem lives in $\Cl^0(2,4)$ or its complexified modules.

Signature reversal does not identify the odd extensions: $\Cl(2,3) \not\cong \Cl(3,2)$ and $\Cl(1,4) \not\cong \Cl(4,1)$, because the centre is $\C$ for $\Cl(2,3)$ and $\Cl(4,1)$ but $\R \oplus \R$ for $\Cl(3,2)$ and $\Cl(1,4)$.

## lay
The algebra that acts on the four-component spinors of the conformal algebra turns out to be a five-dimensional Clifford algebra of signature (2,3), which is the same as four-by-four complex matrices. Both orientations of the spacetime algebra sit inside it, which is why the copy theorem cannot tell this world from its mirror. The odd-dimensional algebras one step up do tell the two orientations apart, because their centres differ.

## one-liner
The even part of $\Cl(2,4)$ is $\Cl(2,3) \cong \Cl(4,1) \cong \Mat(4, \C)$ and contains both $\Cl(1,3)$ and $\Cl(3,1)$, while signature reversal does not identify the odd extensions.
