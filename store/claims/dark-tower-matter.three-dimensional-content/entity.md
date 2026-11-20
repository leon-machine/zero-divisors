---
id: dark-tower-matter.three-dimensional-content
kind: claim
version: 4
title: The three-dimensional towers' content
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [hypercharge-and-anomalies, chirality]
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
  - dark-tower-matter.gauge-algebras@5
  - dark-matter.two-families-are-two-chiralities@7
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:F1
  - id:F2
- kind: check
  ref: check.py::check_cells_and_charges
- kind: check
  ref: check.py::check_exterior_weights_on_lattice
- kind: check
  ref: check.py::check_no_chirality_and_neutral_states
locators:
  paper: T14c
  number: Prop 6.1
  label: prop:content3
  line: 540
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: cell weights computed over Q(i), charges q_+-, exterior-algebra weights on the lattice s + p even, no anticommuting element in Cl(1,2), Cl(2,1), neutral states have zero net cell numbers. Version 3 -> 4.'
  env: proposition
  context_refs:
  - dark-matter.two-families-are-two-chiralities
  - dark-tower-matter.gauge-algebras
  unresolved_refs:
  - rem:S35
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.two-families-are-two-chiralities
    - dark-tower-matter.gauge-algebras
    note: 'Added the gauge algebras (the global form and charges the content is read under; context ref)
      and the dark-matter paper''s families proposition, whose odd case clause (iv) is. Hypothesis (S)
      was not made an assumption: clause (iii) shows (S) is incompatible with the global form here, so
      the result does not hold under (S). The remark on (S) is a note; the transported directions'' weights
      come from the supplementary script D3R. Levels pass: levels written from scratch, keeping every
      condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-tower-matter.gauge-algebras
---

## formal
In the towers $r = 1, 7$:
\begin{enumerate}
\item[(i)] The generators are the four cells of $\R^{2} \otimes \R^{2}$, of weights $(s, p) \in \{\pm 1\}^{2}$; as complex two-component fermions they are $A$, with $(q_{+}, q_{-}) = (1, 0)$, and $B$, with $(0, 1)$, and their conjugates. Each is charged under one factor only: the tower is two copies of single-flavour electrodynamics in $2+1$ dimensions, exchanged by the pair reflection $p \mapsto -p$.
\item[(ii)] Every weight of the exterior algebra of the cells has $s + p$ even; no state of the tensor state space has weight $(\pm 1, 0)$ or $(0, \pm 1)$.
\item[(iii)] Under (S) the constituent-level states have weight $(\pm 1, 0)$, off the lattice $s + p$ even: (S) and the global form of Theorem \claimref{dark-tower-matter.gauge-algebras}(i) are incompatible. Of the directions the transport adds, the rung directions carry $(\pm 1, 0)$ and the pair directions $(0, \pm 1)$, and both are excluded; the one neutral direction (the leftover generator of the odd conformal algebra) is allowed, and its value is a bare mass. The tower has no charged Higgs analogue.
\item[(iv)] There is no chirality: the odd-dimensional modules carry no Lorentz-invariant grading \cite[Prop.~3.9]{ButlerT14}. Gauge-invariant Dirac masses exist for $A$ and $B$ without any condensate, and there is no baryon-like composite: every gauge-neutral state has zero net number of each cell.
\end{enumerate}

## technical
In the towers $r = 1, 7$ the generators are the four cells of $\R^2 \otimes \R^2$, of weights $(s,p) \in \{\pm 1\}^2$; as complex two-component fermions they are $A$, with $(q_+, q_-) = (1, 0)$, $B$, with $(0, 1)$, and their conjugates, so the tower is two copies of single-flavour electrodynamics in $2+1$ dimensions, exchanged by $p \mapsto -p$. Every weight of the exterior algebra of the cells has $s + p$ even.

Under (S) the constituent-level states have weight $(\pm 1, 0)$, off that lattice, so (S) and the global form are incompatible; of the directions the transport adds only the one neutral direction is allowed, its value a bare mass, and there is no charged Higgs analogue. There is no chirality: gauge-invariant Dirac masses exist for $A$ and $B$ without any condensate, and every gauge-neutral state has zero net number of each cell, so there is no baryon-like composite.

## lay
Each three-dimensional tower contains two kinds of charged particle, each feeling only one of its two forces, so the tower is like two separate copies of electromagnetism on a sheet. Assuming the slot hypothesis would add states that do not fit the towers' symmetry, so here the hypothesis and the symmetry are incompatible. The particles can have masses without a Higgs-like field, and there are no proton-like bound states.

## one-liner
The three-dimensional towers carry two species $A$, $B$, each charged under one $U(1)$, with no chirality, gauge-invariant Dirac masses and no baryon-like composite, and under (S) the constituent-level states fall off the charge lattice.
