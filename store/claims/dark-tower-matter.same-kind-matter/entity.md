---
id: dark-tower-matter.same-kind-matter
kind: claim
version: 3
title: Paired towers hold the same kind of matter
status: proved
region: dark-tower-matter
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
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.constituents-field@2
  - dark-tower-matter.five-dimensional-content@5
  - dark-tower-matter.gauge-algebras@5
  - dark-tower-matter.residue-seven-unit@3
  - dark-tower-matter.third-pairs-unit-five-dimensions@5
  - dark-tower-matter.three-dimensional-content@4
  - dark-tower-matter.where-mass-begins@2
  assumes:
  - dark-tower-matter.u-transposition-rule@2
  - dark-tower-matter.h2-identification@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_module_types
- kind: check
  ref: check.py::check_slot_rotation_rows
- kind: check
  ref: check.py::check_pair_unit_rows
locators:
  paper: T14c
  number: Cor 7.2
  label: cor:samekind
  line: 690
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: module types at r = 1, 7, 3, 5, the central unit along the r = 7 tower and its rotation, and the pair-unit row at r = 3 and 5. Version 2 -> 3.'
  env: corollary
  typing:
    by: ai-typing-pass
    added:
    - dark-tower-matter.h2-identification
    note: 'Kept the seven results the proof names for the shared and differing rows and Premise U; added
      H2, named in the statement. Two rows come from supplementary scripts (D3C, CHECK_ALG) that the paper
      script reaches only through untagged Part L lines, so no legacy evidence was attached. Levels pass:
      levels written from scratch, keeping every condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - dark-tower-matter.u-transposition-rule
    - dark-tower-matter.h2-identification
    note: The proof assembles rows from cited results, so U and H2 are given a closing role sentence.
---

## formal
Under H2 and Premise \claimref{dark-tower-matter.u-transposition-rule} the two towers of each odd dimension have the same constituent field, the same mass onset, the same gauge algebra and the same content. They differ only as follows.
\begin{center}\small
\begin{tabular}{@{}p{3.6cm}p{4.9cm}p{4.9cm}@{}}
\toprule
 & $r = 1$ & $r = 7$ \\
\midrule
slot rotation & a rotation of two modules of the same type & the algebra's central unit, exact at every rung \\
slot reflection & internal & exists only fused with orientation reversal \\
module types & two ($\omega = \pm 1$) & one \\
number-violating masses & forbidden once the slot rotation is gauged (H2) & forbidden by the algebra's unit, gauged or not \\
\midrule
 & $r = 3$ & $r = 5$ \\
\midrule
the pair unit & $I_{7}$, fixed by the algebra & a point of $S^{2}$, not fixed \\
reversion-type invariant form & one, Hermitian for $I_{7}$ & none \\
module types & one & two \\
\bottomrule
\end{tabular}
\end{center}

## technical
Under H2 and Premise U the two towers of each odd dimension have the same constituent field, the same mass onset, the same gauge algebra and the same content, and differ only in discrete structure. At $r = 1$ the slot rotation rotates two modules of the same type, the slot reflection is internal, there are two module types ($\omega = \pm 1$), and number-violating masses are forbidden once the slot rotation is gauged; at $r = 7$ the rotation is the algebra's central unit, exact at every rung, the reflection exists only fused with orientation reversal, there is one module type, and such masses are forbidden by the unit, gauged or not.

At $r = 3$ the pair unit is $I_7$, fixed by the algebra, with one reversion-type invariant form, Hermitian for $I_7$, and one module type; at $r = 5$ the unit is a point of $S^2$, not fixed, with no such form and two module types.

## lay
Under the two premises that carry the Standard-Model construction to other towers, the two three-dimensional towers hold the same kind of matter as each other, and so do the two five-dimensional ones. What distinguishes the partners is only discrete structure, such as whether a needed square root of minus one is fixed by the algebra or freely chosen.

## one-liner
Under H2 and Premise U the paired odd towers share field, mass onset, gauge algebra and content, differing only in discrete structure such as whether the algebra fixes the pair unit.
