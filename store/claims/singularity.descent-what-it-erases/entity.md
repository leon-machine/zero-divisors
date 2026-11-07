---
id: singularity.descent-what-it-erases
kind: claim
version: 6
title: The descent, and what it erases
status: proved
region: singularity
subject: descent
tags:
- descent-map
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: 'GA rewrite (the matrix reading of the mode replaced by the CAR basis)'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - std-algebra.witt-basis-car@1
  - std-algebra.cl11-matrix@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:5.5
- kind: check
  ref: check.py::check_occupation_projector
- kind: check
  ref: check.py::check_pinching_keeps_diagonal_erases_coherences
locators:
  paper: T05
  number: Prop 5.5
  label: prop:descent
  line: 1565
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. The statement and proof now write the single-mode element as x = a vv* + b v + c v* + d v*v and the descent as x -> a vv* + d v*v, computed from the CAR (vv*, v, v*, v*v are matrix units in the mode algebra); the 2 x 2 matrices E_ij stay as a labelled reading. The matrix-unit table and the descent action were verified exactly with lib/GA.py in Cl(1,1) (v = (e0 + e1)/2, v* = (e0 - e1)/2). The citation of std-algebra.cl11-matrix is kept, for the matrix reading.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-basis-car, std-algebra.cl11-matrix where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: P = v* v idempotent with 1 - P = v v* in three realisations, and the pinching keeping the diagonal and erasing the coherences on all matrix units. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: proposition
  eqrefs: 3
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'no store references remain; the proof uses only the anticommutation relation, cited by equation;
      removed the mechanical repair edge to the transport algorithm: the section frames its results as
      a step of that algorithm, but the proof is a self-contained computation and does not use it as a
      premise'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  unit_note: 'The imaginary unit here stays a scalar i: this atom is built in the spacetime radial plane
    sigma = e0 e1, where the field theory''s unit I4 anticommutes with the mode operators, so the convention
    i = I4 (which needs a plane orthogonal to spacetime) does not apply. Recorded 21 October 2026; see
    store/conventions.md, known limit 1. Superseded on 7 November 2026 (version 6): no imaginary unit remains in
    this entity, and on this radial atom the unit principle''s unit is J = e2 e3 (conventions, U2).'
---

## formal
Set $P := v^* v$. Then $P^2 = P$, $1 - P = v v^*$, and every element of the mode algebra is $x = a\,vv^{*} + b\,v + c\,v^{*} + d\,v^{*}v$ for unique scalars $a, b, c, d$. With
\[
E(x) := P x P + (1{-}P)\,x\,(1{-}P), \qquad
E\bigl(a\,vv^{*} + b\,v + c\,v^{*} + d\,v^{*}v\bigr) = a\,vv^{*} + d\,v^{*}v .
\]
Descent retains the occupation data $a, d$ and erases the coherences $b, c$. (In the defining $2 \times 2$ representation, a labelled reading, $v = E_{12}$, $v^{*} = E_{21}$, $vv^{*} = E_{11}$, $P = E_{22} = \operatorname{diag}(0, 1)$, and $E$ sends the matrix with entries $a, b, c, d$ to $\operatorname{diag}(a, d)$.)

## technical
With $P := v^* v$, the anticommutation relation and $v^2 = (v^*)^2 = 0$ give $P^2 = P$ and $1 - P = v v^*$. Every element of the mode algebra is $x = a\,vv^{*} + b\,v + c\,v^{*} + d\,v^{*}v$.

The descent $E(x) := PxP + (1-P)\,x\,(1-P)$ sends $x$ to $a\,vv^{*} + d\,v^{*}v$: it retains the occupation data and erases the coherences $b, c$. In the defining $2 \times 2$ representation ($v = E_{12}$, $v^* = E_{21}$, $P = \operatorname{diag}(0,1)$) it keeps the diagonal of the matrix with entries $a, b, c, d$.

## lay
A single fermionic mode can be described by a two-by-two matrix. The descent keeps the two diagonal entries, which record whether the mode is empty or occupied, and discards the two off-diagonal entries, which record quantum coherence between those two possibilities.

## one-liner
The descent $E(x) = PxP + (1-P)x(1-P)$, with $P = v^* v$, keeps a mode's diagonal occupation data and erases its coherences.

