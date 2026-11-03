---
id: correspondence.clifford-side-ordering-shift
kind: claim
version: 3
title: The Clifford side of the ordering shift
status: proved
region: correspondence
subject: conformal-spacetime
tags: [hyperbolic-plane, ladder-pairs, two-readings]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.spin-representation@6
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:prop:rent
- kind: check
  ref: check.py::check_grading_element_of_the_plane
- kind: check
  ref: check.py::check_boost_generator_is_number_minus_half
- kind: check
  ref: check.py::check_mixed_null_pair
locators:
  paper: T09
  number: Prop 5.6
  label: prop:rent
  line: 716
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for every Witt pair and scaling and a mode-mixing pair, E = v ^ v* is the grading element and rho(E) = (1/2) c(v) c(v*) - 1/2 = N - 1/2. Version 1 -> 2.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - correspondence.local-twistor-transport-ascended-spinor-connection
    note: 'Removed the local-twistor edge (E301): the proof only points forward to where these eigenvalues
      are used, so it is not a premise.'
---

## formal
Let $(v, v^*)$ be a null pair of $V$ with $\ip{v}{v^*} = 1$ (an adjoined ladder pair), and let $E := v\wedge v^* \in \mathfrak{so}(2,4)$ be the grading element of the corresponding hyperbolic plane. In the Fock model, the spinor action of $E$ is
\[
\rho(E) \;=\; \tfrac12\,c(v)\,c(v^*) - \tfrac12 \;=\; N - \tfrac12 ,
\]
where $N$ is the occupation number operator of the mode created by $v$ (eigenvalue $1$ on states containing that mode, $0$ otherwise). The generator of the adjoined plane's boost is the mode's number operator shifted by one half.

## technical
Take a null pair $(v, v^*)$ of $V$ with $\ip{v}{v^*} = 1$, an adjoined ladder pair, and let $E = v\wedge v^*$ be the grading element of its hyperbolic plane in $\mathfrak{so}(2,4)$. In the Fock model its spinor action is $\rho(E) = \tfrac12 c(v)c(v^*) - \tfrac12 = N - \tfrac12$, where $N$ is the occupation number of the mode created by $v$, equal to $1$ on states containing that mode and $0$ otherwise.

So the boost generator of the adjoined plane is the mode's number operator shifted by one half.

## lay
Each extra pair of directions added by the completion behaves like a single fermionic mode, which can be empty or occupied. The symmetry that stretches this pair of directions acts on spinors as the number of particles in that mode minus one half. The leftover half is a fixed offset, one half per mode.

## one-liner
In the Fock model the grading element of an adjoined null pair acts on spinors as $N - \tfrac12$, with $N$ the occupation number of the corresponding mode.
