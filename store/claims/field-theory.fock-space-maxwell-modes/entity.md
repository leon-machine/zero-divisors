---
id: field-theory.fock-space-maxwell-modes
kind: claim
version: 5
title: The Fock space and the Maxwell modes
status: proved
region: field-theory
subject: quantum-fields
tags: [gauge-fields, pseudoscalar-and-centre, chirality]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the unit named as I_4 in place of ''i = I_4'' (wording)'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_PHO.py
  tags:
  - id:F1.1
  - id:F1.2
  - id:M1
  - id:M2a
  - id:M2b
  - id:M2c
  - id:M2d
  - id:M2e
  - id:M3.1
  - id:M3.2
- kind: check
  ref: check.py::check_bargmann_fock_ccr_and_adjoint
- kind: check
  ref: check.py::check_one_complex_mode_per_null_momentum
- kind: check
  ref: check.py::check_positive_frequency_is_positive_helicity
- kind: check
  ref: check.py::check_riemann_silberstein_field
locators:
  paper: FT
  number: Prop 8.1
  label: prop:fock
  line: 217
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit naming (DECISIONS H1, R06 item 1): ''with $i = I_4$'' identified a bare i with the unit, which the unit principle treats as a bare unit; the levels and proofs now name the unit (''with the unit $I_4$'', ''the field theory''s unit $I_4$''). Mechanical; no content change.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Bargmann-Fock CCR and adjoint, one I4-complex mode per null momentum, positive frequency as positive helicity for photons and all massless even spinors, and the Riemann-Silberstein form. Version 2 -> 3. Check strengthened: sample inputs moved to module level; the norm of each sample state is now required real as well as positive. Version 3 -> 4.'
  env: proposition
  context_refs:
  - field-theory.imported-statistics-no-go-palatial-algebra
  typing:
    by: ai-typing-pass
    note: 'No edges: the CCR are checked directly on polynomials (F1.1, F1.2), and the statement itself
      says the relation to the palatial algebra of the statistics fact is an analogy, not a construction,
      so that fact (context ref) was not added as a premise. Levels pass: levels written from scratch,
      keeping every condition and level qualifier of the formal statement.'
---

## formal
\begin{enumerate}
\item On polynomials with $\mathrm{span}\{1, I_4\}$ coefficients, $a_m = \partial/\partial z_m$ and $a_m^* = z_m$ satisfy the CCR exactly, and $a_m^*$ is the adjoint of $a_m$ for $\ip{z^n}{z^{n'}} = n!\,\delta$. This is the representation of Fact \claimref{field-theory.imported-statistics-no-go-palatial-algebra}, with variables indexed by photon modes; the relation to the palatial algebra itself is an analogy, not a construction.
\item For null $k$ the bivectors $f$ with $kf = 0$ form a real two-dimensional, $I_4$-stable space: one $I_4$-complex mode per momentum.
\item The positive-frequency mode $f\exp(-I_4k\cdot x)$ has helicity $+1$. Every massless even spinor, of either chirality, has the left-$I_4$ rotation phase of helicity $+\tfrac12$. So with the unit $I_4$, positive frequency is positive helicity for every massless even field.
\item With the unit $I_4$ the field operator is the Riemann-Silberstein form $F = \sum N\,2X\,[\exp(-I_4k\cdot x)\,a_+ + \exp(+I_4k\cdot x)\,a_-^*]$: helicity $+1$ annihilated, helicity $-1$ created.
\end{enumerate}

## technical
On polynomials with $\mathrm{span}\{1, I_4\}$ coefficients, $a_m = \partial/\partial z_m$ and $a_m^* = z_m$ satisfy the CCR exactly, and $a_m^*$ is the adjoint of $a_m$ for $\ip{z^n}{z^{n'}} = n!\,\delta$: the polynomial representation of the palatial algebra, with variables indexed by photon modes, the relation to the palatial algebra itself being an analogy, not a construction. For null $k$ the bivectors $f$ with $kf = 0$ form a real two-dimensional $I_4$-stable space, one $I_4$-complex mode per momentum.

The positive-frequency mode $f\exp(-I_4k\cdot x)$ has helicity $+1$, and every massless even spinor of either chirality has the left-$I_4$ rotation phase of helicity $+\tfrac12$; so with the unit $I_4$ positive frequency is positive helicity for every massless even field, and the field operator is the Riemann-Silberstein form $F = \sum N\,2X\,[\exp(-I_4k\cdot x)\,a_+ + \exp(+I_4k\cdot x)\,a_-^*]$, which annihilates helicity $+1$ and creates helicity $-1$.

## lay
The photon's quantum states are built on polynomials, the standard representation of boson operators, with the spacetime volume element as imaginary unit. Each photon momentum then carries one complex mode, and with this choice of unit positive frequency coincides with positive helicity for every massless field, so the field operator destroys one helicity and creates the other.

## one-liner
With the unit $I_4$ the photon's Fock space is the polynomial CCR representation with one $I_4$-complex mode per null momentum, and positive frequency is positive helicity for every massless even field.
