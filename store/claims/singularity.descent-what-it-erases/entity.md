---
id: singularity.descent-what-it-erases
kind: claim
version: 5
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
    store/conventions.md, known limit 1.'
---

## formal
Set $P := v^* v$. Then $P^2 = P$, $1 - P = v v^*$, and in the defining $2 \times 2$ representation ($v = E_{12}$, $v^* = E_{21}$),
\[
P = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}, \qquad
E(x) := P x P + (1{-}P)\,x\,(1{-}P), \qquad
E\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a & 0 \\ 0 & d \end{pmatrix} .
\]
Descent retains the occupation data and erases the coherences $b, c$.

## technical
With $P := v^* v$, the anticommutation relation and $v^2 = (v^*)^2 = 0$ give $P^2 = P$ and $1 - P = v v^*$. In the defining $2 \times 2$ representation, $v = E_{12}$ and $v^* = E_{21}$, so $P = \operatorname{diag}(0,1)$.

The descent $E(x) := PxP + (1-P)\,x\,(1-P)$ sends the matrix with entries $a, b, c, d$ to $\operatorname{diag}(a, d)$: it retains the occupation data and erases the coherences $b, c$.

## lay
A single fermionic mode can be described by a two-by-two matrix. The descent keeps the two diagonal entries, which record whether the mode is empty or occupied, and discards the two off-diagonal entries, which record quantum coherence between those two possibilities.

## one-liner
The descent $E(x) = PxP + (1-P)x(1-P)$, with $P = v^* v$, keeps a mode's diagonal occupation data and erases its coherences.

