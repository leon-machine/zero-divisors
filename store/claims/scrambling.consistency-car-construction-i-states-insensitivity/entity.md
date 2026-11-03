---
id: scrambling.consistency-car-construction-i-states-insensitivity
kind: claim
version: 5
title: Consistency with the CAR construction, and the I-state's insensitivity
status: proved
region: scrambling
subject: thermality
tags: [car-algebra, boundary-modes]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
derivations:
- name: main
  uses:
  - hawking.imported-quasi-free-states-car-algebra@2
  - scrambling.boundary-mode-space-matrix@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:prop:consistency
- kind: check
  ref: check.py::check_multiplet_scalar_flow_commutes_with_su2
- kind: check
  ref: check.py::check_bilinears_gl_n_and_matrix_units
- kind: check
  ref: check.py::check_quasi_free_symbol_g_of_h_invariant
locators:
  paper: T08
  number: Prop 5.6
  label: prop:consistency
  line: 879
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the multiplet-scalar h commutes with su(2) blocks, the bilinears satisfy the gl(n) relations and restrict to matrix units on Fock space, and the quasi-free state with symbol g(h) is invariant under Q(i) unitaries commuting with h (SU(2) and phase), with a non-degenerate control. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 4 -> 5.'
  env: proposition
  outside_pilot_cites:
  - ButlerT10
  - ButlerT7
  typing:
    by: ai-typing-pass
    note: 'Kept both premises (the quasi-free symbol Fact for (iii) and the boundary mode space for (ii));
      no edges changed. Levels pass: the lay level and one-liner now keep the assembly level of check
      (i) and the quasi-free qualifier of check (iii).'
---

## formal
Three checks, each at its level. (i) \emph{Assembly:} the near-horizon reduction delivers one field per $(\ell, m)$ with $m$-independent dynamics, so the modular flow acts as a scalar on each multiplet and centralises the $\mathfrak{su}(2)$: the sphere's symmetry commutes with the clock. (ii) \emph{Proved:} the mixed bilinears of Proposition \claimref{scrambling.boundary-mode-space-matrix} are ordinary gauge-invariant CAR bilinears of the observable algebra: no operator outside the algebra of the boundary modes themselves is invoked. (iii) \emph{Proved, within the quasi-free setting:} the I-state with multiplet-degenerate frequencies is invariant under every gauge Bogoliubov transformation of the complexified one-particle space commuting with the one-particle Hamiltonian, in particular under all embedded $SU(2)$ actions: for a quasi-free state whose symbol is a function of the one-particle Hamiltonian, $\Lambda = g(h)$, and a unitary $U$ on the one-particle space with $UhU^* = h$, the transformed state has symbol $U\Lambda U^* = Ug(h)U^* = g(h) = \Lambda$, the same state. The I-state is embedding-insensitive: it neither selects nor obstructs the sphere. This diagonality is the sphere's side of the orthogonality no-go carried by the action paper T10 \cite{ButlerT10}: the state is insensitive to space for the same reason the gravitational sector leaves no mark on it; the full development of that identity is that paper's task (shared between the two papers).

## technical
Three checks, each at its own level. (i) Assembly: the near-horizon reduction gives one field per $(\ell, m)$ with $m$-independent dynamics, so the modular flow acts as a scalar on each multiplet and commutes with the $\su(2)$ of the sphere. (ii) Proved: the mixed bilinears of the boundary mode space are ordinary gauge-invariant CAR bilinears of the observable algebra, so no operator outside the algebra of the boundary modes is invoked.

(iii) Proved within the quasi-free setting: for a quasi-free state whose symbol is a function of the one-particle Hamiltonian, $\Lambda = g(h)$, and a unitary $U$ on the one-particle space with $UhU^* = h$, the transformed symbol is $Ug(h)U^* = g(h) = \Lambda$, the same state. So the I-state with multiplet-degenerate frequencies is invariant under every gauge Bogoliubov transformation commuting with the one-particle Hamiltonian, in particular under every embedded $SU(2)$ action: it neither selects nor obstructs the sphere.

## lay
The construction of the black hole's boundary modes passes three consistency checks, each at its own level. At assembly level, below full proof, the rotational symmetry of the sphere commutes with the modes' internal clock. Proved: the quantities used are built only from the modes themselves. Proved within the quasi-free class of states: the thermal state used is unchanged by any symmetry that respects the mode energies, so that state is blind to how the sphere sits inside the construction; it neither picks it out nor rules it out.

## one-liner
At assembly level the sphere's symmetry commutes with the modular clock; the mixed bilinears are ordinary CAR bilinears of the boundary modes; and, within the quasi-free setting, the I-state, whose symbol is a function of the one-particle Hamiltonian, is invariant under every gauge Bogoliubov transformation commuting with it, including all embedded $SU(2)$ actions.
