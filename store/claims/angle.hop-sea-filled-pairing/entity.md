---
id: angle.hop-sea-filled-pairing
kind: claim
version: 4
title: The hop with the sea filled is the pairing
status: proved
region: angle
subject: thermality
tags: [pairing-and-bogoliubov, finite-models, entanglement]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-angle, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - angle.hop-across-cut@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_v_is_the_particle_hole_automorphism
- kind: check
  ref: check.py::check_image_state_and_pairing_generator
- kind: check
  ref: check.py::check_equal_frequency_boost_becomes_number_difference
locators:
  paper: T05-angle
  number: Prop 4.3
  label: prop:particlehole
  line: 193
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: V = (a1 + a1^dag) Gamma_0 as the particle-hole automorphism, the image state and pairing generator with their spectrum, and the boost conjugation. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'No edges: the thermofield pair of the singularity paper is named for comparison only; the proof
      is a direct computation with the stated operator V.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - angle.hop-across-cut
    added_dependants: []
    added_about: []
    verdict: connected
    note: The proposition conjugates the state and generator of the hop proposition, whose spectrum and
      unique ground state it carries over; the thermofield pair it names is matched by inspection, not imported.
---

## formal
Let $V = (a_{1} + a^{\dagger}_{1})\Gamma_{0}$ on the pair, with $\Gamma_{0} = (-1)^{N_{0}}$ and $\ket{11} = a^{\dagger}_{0}a^{\dagger}_{1}\ket{00}$. Then $V$ is unitary and Hermitian, $V^{2} = 1$, conjugation by $V$ fixes $a_{0}$ and exchanges $a_{1}$ with $a^{\dagger}_{1}$ (the particle-hole automorphism of the right mode), and:
\begin{enumerate}
\item[(i)] $V\psi = \tfrac45\ket{00} + \tfrac35\ket{11}$, exactly the singularity paper's thermofield pair at the sample point, an even state with the same left marginal $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$;
\item[(ii)] $VHV^{-1} = 7N_{0} - 12(a^{\dagger}_{0}a^{\dagger}_{1} + a_{1}a_{0})$, a pairing generator with the same spectrum, whose unique ground state is $V\psi$;
\item[(iii)] $V(N_{0} + N_{1} - 1)V^{-1} = N_{0} - N_{1}$: the equal-frequency boost of the hop form becomes the number-difference boost of the vacuum form.
\end{enumerate}

## technical
Let $V = (a_{1} + a^{\dagger}_{1})\Gamma_{0}$ on the pair, with $\Gamma_{0} = (-1)^{N_{0}}$ and $\ket{11} = a^{\dagger}_{0}a^{\dagger}_{1}\ket{00}$. It is unitary and Hermitian with $V^{2} = 1$, and conjugation by $V$ fixes $a_{0}$ and exchanges $a_{1}$ with $a^{\dagger}_{1}$: it is the particle-hole automorphism of the right mode. It carries the hop ground state $\psi = \tfrac35\ket{10} + \tfrac45\ket{01}$ to $V\psi = \tfrac45\ket{00} + \tfrac35\ket{11}$, the even thermofield pair at the sample point, with the same left marginal $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$.

The hop generator becomes a pairing generator, $VHV^{-1} = 7N_{0} - 12(a^{\dagger}_{0}a^{\dagger}_{1} + a_{1}a_{0})$, with the same spectrum and unique ground state $V\psi$, and the equal-frequency boost becomes the number-difference boost, $V(N_{0} + N_{1} - 1)V^{-1} = N_{0} - N_{1}$. Read with the right mode's occupation inverted, the hop is the pairing.

## lay
In the two-mode model, swap the roles of "particle" and "empty slot" on one side only. Under this swap a term that hops particles across the horizon becomes a term that creates or removes pairs, and the lowest-energy state of the hopping model becomes exactly the paired, thermal-looking state used in the earlier analysis of the singularity. The view from the other side does not change, so the two models describe the same correlation.

## one-liner
The particle-hole map on the right mode carries the hop generator and its ground state to a pairing generator and the thermofield pair $\tfrac45\ket{00} + \tfrac35\ket{11}$, with the same left marginal.
