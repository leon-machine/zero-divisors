---
id: pred.gravity-entangles-standard-phase
kind: prediction
version: 3
title: Gravity entangles two masses by the standard phase
status: live
subject: one-relation
tags: [live-prediction, quantum-gravity, entanglement]
region: quantum-gravity
proposed_by:
  kind: human
  author: leon (registration); entered by the build
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude (model not recorded)
  role: mathematics and drafting
- name: Claude Fable 5.2
  role: 'scope sentence: the prediction is about the phase only, with no claim about a mediator or a quantised gravitational field; observation row'
  version: 2
  source: maintainer pass of 2026-11-10
- name: Claude Fable 5.2
  role: 'basis linked to the operator Newtonian coupling, which derives the phase and its sign; the reading and premises stay outside the store; prediction unchanged'
  version: 3
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
review: draft
kill_condition:
  threshold: A null result at a sensitivity that resolves the standard phase on the experiment's geometry,
    with coherence kept for the duration, refutes the element reading together with premises P-i to P-vi
  data_source: gravity-mediated entanglement experiments (BMV type)
  registered: 2026-10-09; reading chosen 2026-10-12 (third addendum)
observations:
- date: 2026-11
  dataset: Mass in spatial superposition; proposals for gravity-mediated entanglement
  result: 'Status unchanged: no experiment has observed gravity-mediated entanglement, and the kill condition
    is neither met nor probed. The largest mass shown in spatial superposition is a sodium nanoparticle
    of more than 7,000 atoms, above 170,000 Da (macroscopicity 15.5), many orders below the milligram
    scale at which gravity between small masses has been measured classically. Current work is design
    and theory: a chip-based magnetic levitation and superposition scheme for nanodiamonds of 1e-19 to
    1e-15 kg (numerical simulation only), and a mass-independent scheme with two Stern-Gerlach interferometers
    (analytical). Whether a classical gravitational interaction with quantised matter could itself produce
    entanglement is disputed in print (Nature 646, 813 (2025), and a reply attributing the entanglement
    there to diffusion of particles between the objects); the stored prediction concerns the phase only
    and takes no side.'
  verdict: pending
  source: Pedalino et al., arXiv:2507.21211 (2025); Xiang et al., arXiv:2601.06608 (2026); Braccini, Serafini
    and Bose, arXiv:2602.19306 (2026); Gundhi, Infantino and Bassi, arXiv:2604.19696 (2026)
- date: 2026-10
  dataset: Tabletop gravity between small masses
  result: 'No experiment has reached gravity-mediated entanglement. The newest step is classical: Newtonian
    gravity measured between two 7.6 mg plates with a miniature torsion pendulum. Milligram quantum-regime
    proposals remain projections.'
  verdict: pending
  source: An et al., Nature Communications (2026); Bonaldi et al., arXiv:2607.18351 (2026)
- date: 2026-10
  dataset: gravity-mediated entanglement experiments
  result: No experiment has yet reached the standard phase.
  verdict: pending
  source: QG_entanglement_prediction_registration.md
locators:
  paper: QG notes
  number: registration 2026-10-09, third addendum
  label: ''
extraction:
  maintainer_pass_2026_11_18_basis:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 2 -> 3. The basis derivation now uses field-theory.operator-newtonian-coupling, the stored proposition that derives the registered phase with its sign from a coupling built from commuting conserved numbers and that already carried a supports link to this prediction. The element reading and premises P-i to P-vi, under which that coupling is the gravitational one, remain a working note outside the store, and no premise is added for them (the operator source is kept as a local hypothesis of the results that use it, decision of 18 November 2026). One sentence of the technical level reworded to say so. The prediction, its status and its kill condition are unchanged.'
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2: a scope sentence at every level says the prediction concerns the phase only, makes no claim about a mediator and is not a test of a quantised gravitational field, which the series does not hold (the conventions state the position); observation row of 2026-11 added from four arXiv abstracts read on the web on 2026-11-10, status unchanged. The prediction and its kill condition are unchanged.'
  env: registration
  source: 'Project: claude/QG_entanglement_prediction_registration.md'
  flags:
  - 'basis linked in part: the phase is derived in the store from the operator coupling; the element reading and premises P-i to P-vi rest on the working note "Value or Element", which is not a series paper'
  typing:
    by: ai-levels-pass
    note: 'Levels pass: wrote the technical and lay levels, which were pending, keeping the element reading
      and premises P-i to P-vi, and added both conditions to the one-liner, which had dropped them.'
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: 'Rests on the element reading and premises P-i to P-vi of a working note outside the store; the operator Newtonian coupling already supports it, and no store definition concerns the element reading.'
derivations:
- name: basis
  uses:
  - field-theory.operator-newtonian-coupling@4
---

## formal
Gravity entangles two masses, each held in a superposition of two places, by the standard phase $\Phi = (G m_A m_B/\hbar)\int (1/r_{11} + 1/r_{22} - 1/r_{12} - 1/r_{21})\,dt$, under the element reading and premises P-i to P-vi.

\emph{Scope.} The prediction concerns the phase only. It makes no claim about a mediator and is not a test of a quantised gravitational field: the series holds none, gravity here being the classical gauge field of Gauge Theory Gravity with the masses the field theory's fermions. An observed entanglement by the standard phase would agree with this prediction and with every account that gives that phase; only a null result at resolving sensitivity bears on it.

## technical
Registered prediction (registered 2026-10-09; reading chosen 2026-10-12, third addendum). Under the element reading of the frozen-point connection's equations, and under premises P-i to P-vi, held fixed before any result (P-ii is unitary evolution), two masses $m_A$ and $m_B$, each held in a superposition of two places, become entangled by the standard phase
$$\Phi = \frac{G m_A m_B}{\hbar}\int \left(\frac{1}{r_{11}} + \frac{1}{r_{22}} - \frac{1}{r_{12}} - \frac{1}{r_{21}}\right)dt,$$
with $r_{ij}$ the distance between branch $i$ of the first mass and branch $j$ of the second.

The prediction was first registered under the other reading of the same equations, the value reading (a single grade-two connection with real coefficients), as no entanglement; choosing the element reading inverted it. A null result at a sensitivity that resolves the standard phase on the experiment's geometry, with coherence kept for the duration, refutes the element reading together with P-i to P-vi. The phase and its sign are derived in the store from a coupling built from commuting conserved numbers (Proposition \claimref{field-theory.operator-newtonian-coupling}); the element reading and the premises, under which that coupling is the gravitational one, are a working note, not a series paper, and are not stored premises.

The prediction concerns the phase only. It makes no claim about a mediator and is not a test of a quantised gravitational field: the series holds none, gravity here being the classical gauge field of Gauge Theory Gravity with the masses the field theory's fermions. An observed entanglement by the standard phase would agree with this prediction and with every account that gives that phase; only a null result at resolving sensitivity bears on it.

## lay
Take two small masses and put each into a superposition of being in two places at once. This prediction says that, under one of the two readings the framework's equations allow (the element reading, chosen on 12 October 2026) and six premises fixed in advance (P-i to P-vi, one of them that quantum evolution stays unitary), gravity between the masses entangles them by exactly the standard amount, the phase that Newtonian gravity gives in ordinary quantum mechanics. Under the other reading the framework had predicted no entanglement at all. Tabletop experiments have not yet reached this sensitivity; a clear null result at the needed sensitivity, with the superpositions kept coherent throughout, would refute the chosen reading together with its premises. The prediction is about the size of the effect only. It says nothing about what carries gravity between the masses and is not a test of whether gravity comes in quanta: in this framework gravity is a classical field, and seeing the effect would not show otherwise.

## one-liner
Under the element reading and premises P-i to P-vi, gravity entangles two superposed masses by the standard phase; a statement about the phase only, with no claim about a mediator or a quantised gravitational field.
