---
id: descent-lift.classical-record-reproduces-descent-stores-nothing
kind: claim
version: 5
title: A classical record reproduces the descent and stores nothing
status: proved
region: descent-lift
subject: descent
tags: [descent-map, measurement-and-records, ladder-pairs]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
about:
- obj.descent-lift.lift
derivations:
- name: main
  uses:
  - descent-lift.lift-costs-one-rung-per-mode@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_two_rung_classical_record
- kind: check
  ref: check.py::check_one_rung_classical_record
locators:
  paper: T05-descent-lift
  number: Prop 5.3
  label: prop:stochastic
  line: 255
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the even-mixture record (two rungs) and the maximally mixed rung (one rung) induce the descent on every even matrix unit, with joint purity 1/2 against 1 for the lift and a parity-commuting one-rung output. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - descent-lift.lift-costs-one-rung-per-mode
    note: 'added the lift theorem, whose factorisation clause defines the coupling C that the statement
      reuses (''the same coupling''); the univalence remark in the proof is context, not a premise; no
      standard route, since ''reproduces'' here compares a classical record with the coherent lift, not
      with standard physics. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - descent-lift.lift-costs-one-rung-per-mode
---

## formal
With the record pair in the even mixture $\tfrac12(\ket{00}\bra{00} + \ket{11}\bra{11})$ and the same coupling $C$, the induced map on the pair is again the descent, but the joint output of a pure input has purity $\tfrac12$, against $1$ for the lift. One rung suffices for this: a single rung in the maximally mixed state $\tfrac12(\ket{0}\bra{0} + \ket{1}\bra{1})$, with the coupling $1 - 2P^{R}_{1}N_{0}$, also induces the descent, its joint output commuting with the total parity and again of purity $\tfrac12$. Two rungs are needed only for the coherent lift.

## technical
Prepare the record pair not in the paired state $\varphi$ but in the even mixture $\tfrac12(\ket{00}\bra{00} + \ket{11}\bra{11})$ and apply the same supplied-class coupling $C$. Since $C$ acts on the two record branches as $1$ and as $\G_{0}$, the induced map on the pair is $\tfrac12(\rho + \G_{0}\rho\G_{0})$, the descent, but the joint output of a pure input is an equal mixture of two orthogonal pure states, of purity $\tfrac12$ rather than the lift's $1$.

A single rung suffices for this classical version: in the maximally mixed state $\tfrac12(\ket{0}\bra{0} + \ket{1}\bra{1})$, with the coupling $1 - 2P^{R}_{1}N_{0}$, it again induces the descent, with a joint output that commutes with the total parity and again has purity $\tfrac12$. Two rungs are needed only for the coherent lift.

## lay
The descent that erases a pair's entanglement can also be produced by coupling the pair to a record that is itself a random classical coin. That has the same effect on the pair, but the combined system ends up in a mixed state, so the erased information is not stored anywhere recoverable. A single extra mode is enough for this classical version; the second one is needed only when the record must keep the information coherently.

## one-liner
A classically mixed record with the same coupling induces the descent on the pair but leaves the joint state at purity $\tfrac12$, and one rung suffices for this, while the coherent lift needs two.
