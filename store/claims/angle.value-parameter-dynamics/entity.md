---
id: angle.value-parameter-dynamics
kind: claim
version: 4
title: The value is a parameter of the dynamics
status: proved
region: angle
subject: thermality
tags: [finite-models, undetermined-input]
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
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_ground_state_eigenvalue_and_marginal
- kind: check
  ref: check.py::check_gap_identities_and_sign_condition
- kind: check
  ref: check.py::check_gibbs_parameter_fixed_by_ratio_and_sign_of_t
lineage:
  motivated_by:
  - angle.hop-across-cut
locators:
  paper: T05-angle
  number: Prop 4.5
  label: prop:parameter
  line: 210
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Statement corrected: the Gibbs parameter is fixed by eps/t together with the sign of t (eps/t alone fixes it only for t > 0; (4/5,3/5) at t = 60 and (3/5,-4/5) at t = -60 share eps/t = -7/12 with q = 16/9 and 9/16); proof: the root with the sign of t. Also own exact check added: ground state, eigenvalue, gaps and marginal at the seven sample points, the gap identities, and the determination of q by eps/t with the sign of t. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'No edges: the proof is a self-contained finite computation; the link to rate rigidity is made
      only in a following remark.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Self-contained finite computation generalising the hop example (recorded as lineage, since its
      proof does not use that example); it closes the note's line of argument and only the remark on where
      2 pi lives draws on it.
---

## formal
For every rational point $(c, s)$ of the unit circle with $cs \neq 0$ and every rational $t$ with $tcs > 0$, the hop generator $H = \varepsilon N_{0} - t(a^{\dagger}_{0}a_{1} + a^{\dagger}_{1}a_{0})$ with $\varepsilon/t = (s^{2} - c^{2})/(cs)$ has $c\ket{10} + s\ket{01}$ as its unique ground state, with eigenvalue $-tc/s$, and left marginal Gibbs for $N_{0}$ at $q = c^{2}/s^{2}$. The Gibbs parameter of the marginal, and with it $\beta\omega = -\log q$, is determined by the ratio $\varepsilon/t$ of the couplings together with the sign of $t$ (by the ratio alone for $t > 0$): $c/s$ is the root of $r^{2} + (\varepsilon/t)r - 1 = 0$ with the sign of $t$.

## technical
Take the two-mode hop generator $H = \varepsilon N_{0} - t(a^{\dagger}_{0}a_{1} + a^{\dagger}_{1}a_{0})$, a rational point $(c, s)$ of the unit circle with $cs \neq 0$, and a rational $t$ with $tcs > 0$. Choosing $\varepsilon/t = (s^{2} - c^{2})/(cs)$ makes $c\ket{10} + s\ket{01}$ the unique ground state, with eigenvalue $-tc/s$, and its left marginal is Gibbs for $N_{0}$ at $q = c^{2}/s^{2}$.

So the Gibbs parameter of the marginal, and with it $\beta\omega = -\log q$, is fixed by the coupling ratio $\varepsilon/t$ together with the sign of $t$. A hop can select an entangled ground state with a finite $\beta$, but the value of $\beta$ is set by the couplings.

## lay
In the two-mode model with a hopping term, the lowest-energy state can be made to look thermal from one side at any of a whole family of temperatures. Which temperature appears is set by the ratio of the two strengths in the generator and the sign of the hopping strength. So the finite model shows that a hop can produce a thermal-looking state, but by itself it does not fix one particular temperature.

## one-liner
For the two-mode hop generator the Gibbs parameter of the ground state's left marginal is $q = c^{2}/s^{2}$, set by the coupling ratio $\varepsilon/t$ and the sign of $t$, for every rational point $(c, s)$ of the circle with $cs \neq 0$.
