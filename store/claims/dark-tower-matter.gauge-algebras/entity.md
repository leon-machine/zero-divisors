---
id: dark-tower-matter.gauge-algebras
kind: claim
version: 5
title: The gauge algebras of the odd towers
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [gauge-fields]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.constituents-field@2
  - dark-tower-matter.ladder@2
  - dark-tower-matter.pairs@3
  - dark-tower-matter.third-pairs-unit-five-dimensions@5
  - dark-tower-matter.where-mass-begins@2
  assumes:
  - dark-tower-matter.u-transposition-rule@4
  - dark-tower-matter.h2-identification@1
  - dark-tower-matter.h1-momentum@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:E1
  - id:E2
  - id:E3
  - id:E4
  - id:F2
- kind: check
  ref: check.py::check_three_dimensional_algebra_is_so2_plus_so2
- kind: check
  ref: check.py::check_three_dimensional_global_form
- kind: check
  ref: check.py::check_five_dimensional_algebra_is_u3
locators:
  paper: T14c
  number: Thm 5.1
  label: thm:algebras
  line: 467
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: so(2) + so(2) abelian with kernel {(1,1), (-1,-1)}, the U(1)_+ x U(1)_- lattice, and u(3) from C^1 (x) C^3 (dimension 9, derived 8, centre 1) with controls 12 and 7. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  env: theorem
  unresolved_refs:
  - rem:kleinian
  typing:
    by: ai-typing-pass
    added:
    - dark-tower-matter.h1-momentum
    - dark-tower-matter.h2-identification
    note: 'Kept all five cited results and Premise U; added H2, named in the statement, and H1, which
      the proof of (ii) invokes to identify the field of the conformal constituent with the field acting
      on its spinor part. Levels pass: levels written from scratch, keeping every condition and level
      qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-tower-matter.u-transposition-rule
    - dark-tower-matter.h2-identification
---

## formal
Under H2 and Premise \claimref{dark-tower-matter.u-transposition-rule}:
\begin{enumerate}
\item[(i)] (Three-dimensional towers, $r = 1, 7$.) Mass begins at two real constituents and each carries two real pairs, so the minimal massive hierarchy is $\R^{2} \otimes \R^{2}$. Its automorphisms $A \otimes B$ with $A, B \in O(2)$ form $(O(2) \times O(2))/\mathbb{Z}_{2}$, the kernel being $\{(1,1), (-1,-1)\}$; the gauge algebra is $\so(2) \oplus \so(2)$, abelian, of dimension $2$, and the identity component of the group is $U(1)_{+} \times U(1)_{-}$.
\item[(ii)] (Five-dimensional towers, $r = 3, 5$.) Mass begins at one constituent and its three pairs are complex with the unit of Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions}, so the hierarchy is $\C^{1} \otimes \C^{3}$. Its automorphisms form $(U(1) \times U(3))/U(1) \cong U(3)$; the gauge algebra is $\uu(3) = \su(3) \oplus \uu(1)$, of dimension $9$.
\end{enumerate}

## technical
Under H2 (the gauge algebra is the automorphism algebra of the minimal massive hierarchy) and Premise U: in the three-dimensional towers $r = 1, 7$ mass begins at two real constituents of two real pairs, so the hierarchy is $\R^2 \otimes \R^2$. Its automorphisms $A \otimes B$ with $A, B \in O(2)$ form $(O(2) \times O(2))/\mathbb{Z}_2$, the kernel being $\{(1,1), (-1,-1)\}$: the gauge algebra is the abelian $\so(2) \oplus \so(2)$, of dimension two, with identity component $U(1)_+ \times U(1)_-$.

In the five-dimensional towers $r = 3, 5$ mass begins at one constituent whose three pairs are complex, with the unit that builds the third pair, so the hierarchy is $\C^1 \otimes \C^3$. Its automorphisms form $(U(1) \times U(3))/U(1) \cong U(3)$, and the gauge algebra is $\uu(3) = \su(3) \oplus \uu(1)$, of dimension nine.

## lay
Assuming that a tower's forces are the symmetries of its smallest composite that can have mass, as in the Standard-Model paper, and a rule for carrying that construction to other towers, this theorem finds the forces of the odd towers. The three-dimensional towers get two independent forces like electromagnetism. The five-dimensional towers get a colour force like our strong force together with one force like electromagnetism, nine force carriers in all.

## one-liner
Under H2 and Premise U the gauge algebra is the abelian $\so(2) \oplus \so(2)$ in the three-dimensional towers and $\uu(3) = \su(3) \oplus \uu(1)$ in the five-dimensional towers.
