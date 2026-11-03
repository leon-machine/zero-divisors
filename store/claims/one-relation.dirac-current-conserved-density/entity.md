---
id: one-relation.dirac-current-conserved-density
kind: claim
version: 2
title: The Dirac current is the conserved density
status: proved
region: one-relation
subject: one-relation
tags: [forcing-and-uniqueness, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T16.py
  tags:
  - label:lem:current
- kind: check
  ref: check.py::check_representation
- kind: check
  ref: check.py::check_conserved_currents_are_one_dimensional
- kind: check
  ref: check.py::check_dirac_current_is_conserved
- kind: check
  ref: check.py::check_density_is_sum_of_squared_moduli
locators:
  paper: T16
  number: Lem 6.1
  label: lem:current
  line: 805
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Dirac representation over Q(i); 528 conservation conditions from twelve mass-shell momenta are all satisfied by gamma^mu and have rank 63 modulo the prime 1000003 (= 3 mod 4), so the conserved currents form a one-dimensional space; conservation on all sample pairs; J^0 = psi^dagger psi. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'No edges; the lemma is itself standard Dirac theory proved directly, and no imported standard Dirac-current claim exists in the store for a standard-route derivation.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$(i\gamma^\mu\partial_\mu - m)\psi = 0$ and the plane waves $u\,e^{-ip\cdot x}$: Dirac theory in
      a $\Mat(4, \C)$ matrix representation, $i$ next to $\gamma^\mu$ (gamma matrices as complex matrices);
      converting would need the Hestenes form, which the statement only cites. Doubtful for the plane waves'
---

## formal
Let $\psi$ range over solutions of the Dirac equation $(i\gamma^{\mu}\partial_{\mu} - m)\psi = 0$ with $m > 0$, in a matrix representation with $\{\gamma^{\mu}, \gamma^{\nu}\} = 2\eta^{\mu\nu}$, $\gamma^{0}$ Hermitian and $\gamma^{k}$ anti-Hermitian, and let $\bar{\psi} = \psi^{\dagger}\gamma^{0}$. Among the constant sesquilinear currents $J^{\mu}_{\Gamma} = \bar{\psi}\,\Gamma^{\mu}\psi$, $\Gamma^{\mu} \in \Mat(4, \C)$ constant, those conserved on every solution ($\partial_{\mu}J^{\mu}_{\Gamma} = 0$) form the one-dimensional space spanned by $\Gamma^{\mu} = \gamma^{\mu}$. The density of that current, $J^{0} = \bar{\psi}\gamma^{0}\psi = \psi^{\dagger}\psi$, is a sum of squared moduli, positive and zero only on the zero state.

## technical
For solutions of the Dirac equation $(i\gamma^{\mu}\partial_{\mu} - m)\psi = 0$ with $m > 0$, consider the constant sesquilinear currents $J^{\mu}_{\Gamma} = \bar{\psi}\Gamma^{\mu}\psi$. Those conserved on every solution form a one-dimensional space, spanned by $\Gamma^{\mu} = \gamma^{\mu}$. Its density $J^{0} = \psi^{\dagger}\psi$ is a sum of squared moduli, positive and vanishing only on the zero state.

Conservation on every solution reduces to the linear condition $(p - p')_{\mu}\bar{u}\Gamma^{\mu}v = 0$ over mass-shell plane waves; $\gamma^{\mu}$ satisfies it, and an exact finite sample of momenta already cuts the solution space down to one dimension.

## lay
The Dirac equation describes the electron relativistically. Among all the simple candidate currents one can build from its solutions, only one is conserved for every solution, the standard Dirac current. Its time component, the density, is always positive and is zero only when there is no wave at all.

## one-liner
Among constant sesquilinear currents, the Dirac current $\bar{\psi}\gamma^{\mu}\psi$ is the unique conserved one up to scale, with positive density $\psi^{\dagger}\psi$.
