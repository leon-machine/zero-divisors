---
id: field-theory.elementary-photon-ga
kind: claim
version: 4
title: The elementary photon in GA
status: proved
region: field-theory
subject: quantum-fields
tags: [gauge-fields, pseudoscalar-and-centre, recovers-known-physics, scattering-amplitudes]
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
review: typed
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - field-theory.contact-interactions-tower@4
  - field-theory.imported-standard-field-theory@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_BOS.py
  tags:
  - id:E0
  - id:E1
  - id:E2.0
  - id:E2.1
  - id:E2.1c
  - id:E2.2
  - id:E2.3
  - id:E2.4
  - id:E3
  - id:E3g
  - id:E3b
  - id:E3c
  - id:E4
- kind: check
  ref: check.py::check_kinematics_and_conservation
- kind: check
  ref: check.py::check_helicity_eigen_relation
- kind: check
  ref: check.py::check_sesquilinear_and_helicity_sum
- kind: check
  ref: check.py::check_coulomb_gauge_equals_covariant
- kind: check
  ref: check.py::check_massive_vector_contact_limit
locators:
  paper: FT
  number: Prop 7.3
  label: prop:photon
  line: 201
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: kinematics and current conservation, the helicity eigen-relation, sesquilinearity and the helicity sum, Coulomb-gauge exchange equal to the covariant form, and the massive contact limit. Version 3 -> 4.'
  env: proposition
  context_refs:
  - field-theory.contact-interactions-tower
  typing:
    by: ai-typing-pass
    added:
    - field-theory.contact-interactions-tower
    - field-theory.imported-standard-field-theory
    note: 'Added the contact-interaction proposition, which clause (5) reduces to, and the standard field-theory
      fact for the Coulomb-gauge exchange of clause (4). No standard route: clauses (1) to (3) are geometric-algebra
      statements that standard physics does not supply in this form. Levels pass: levels written from
      scratch, keeping every condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - field-theory.imported-standard-field-theory
    - field-theory.contact-interactions-tower
---

## formal
With $i = I_4$ and complex coefficients on the left:
\begin{enumerate}
\item the polarisation $\epsilon_h = t_1 - hI_4t_2$ satisfies $B_q\cdot\epsilon_h = hI_4\epsilon_h$ for the rotation bivector $B_q$ about $q$, on and off the coordinate axes;
\item the geometric product of complex vectors is sesquilinear, $\proj(J\epsilon) = J\cdot\bar\epsilon$, because $I_4$ anticommutes with vectors;
\item the helicity sum $\tfrac12\sum_h\proj(J_A\epsilon_h)\proj(J_B\epsilon_{-h})$ is the transverse product $J_A^\perp\cdot J_B^\perp$;
\item Coulomb-gauge exchange (two time orderings and the instantaneous Coulomb term) equals the covariant $-e^2J_A\cdot J_B/t$, by current conservation;
\item massive vector exchange reduces to the contact term of Proposition \claimref{field-theory.contact-interactions-tower} with $G = e^2/M^2$.
\end{enumerate}

## technical
With $i = I_4$ and complex coefficients on the left, the polarisation $\epsilon_h = t_1 - hI_4t_2$ satisfies $B_q\cdot\epsilon_h = hI_4\epsilon_h$ for the rotation bivector $B_q$ about $q$, on and off the coordinate axes; the geometric product of complex vectors is sesquilinear, $\proj(J\epsilon) = J\cdot\bar\epsilon$, because $I_4$ anticommutes with vectors; and the helicity sum $\tfrac12\sum_h\proj(J_A\epsilon_h)\proj(J_B\epsilon_{-h})$ is the transverse product $J_A^\perp\cdot J_B^\perp$.

Coulomb-gauge exchange, two time orderings and the instantaneous Coulomb term, equals the covariant $-e^2J_A\cdot J_B/t$, given current conservation, and massive vector exchange reduces to the contact term with $G = e^2/M^2$.

## lay
Taking the photon as a fundamental field, its polarisations and helicities can be written in geometric algebra with the volume element as imaginary unit. With them, photon exchange between two currents reproduces the standard result, given that the currents are conserved, and a heavy force carrier reduces to the contact interaction.

## one-liner
With $i = I_4$ the photon's helicity polarisations and helicity sum are geometric-algebra objects, and Coulomb-gauge exchange gives $-e^2J_A\cdot J_B/t$, given current conservation.
