---
id: singularity.deficit-theorem-cost-descent-exactly
kind: claim
version: 4
title: 'The deficit theorem: the cost of descent, exactly'
status: proved
region: singularity
subject: entropy
tags: [descent-map]
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
about:
- obj.singularity.multi-mode-descent
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:9.3
- kind: check
  ref: check.py::check_pinching_structure
- kind: check
  ref: check.py::check_key_lemma_moment_form
- kind: check
  ref: check.py::check_entropy_identity_exact
locators:
  paper: T05
  number: Thm 9.3
  label: thm:deficit
  line: 2085
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: four projector families (idempotent, trace preserving, HS self-adjoint), the key lemma in moment form, and S(E rho) - S(rho) = D(rho||E rho) as formal logarithms with D > 0. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'Removed the mechanically added transport-algorithm edge: the theorem is a general identity
      for pinchings with no store premises; its only outside input is Klein''s inequality, cited to the
      literature and not an imported claim in the store.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
---

## formal
Let $E$ be the pinching by any complete family of orthogonal projectors ($\EN$ included) and $\rho$ a density matrix. Then $E$ is idempotent, trace-preserving, and self-adjoint for the Hilbert-Schmidt pairing, and
\[
S\bigl(E(\rho)\bigr) - S(\rho) \;=\; \rel{\rho}{E(\rho)} \;\geq\; 0 ,
\]
with $S$ the von Neumann entropy and $D$ the relative entropy, and with equality if and only if $\rho = E(\rho)$. The level discrepancy of Step 6b is this quantity: not a slogan but a relative entropy, computed once and for all.

## technical
Let $E$ be the pinching by a complete family of orthogonal projectors, the multi-mode descent $\EN$ included. Then $E$ is idempotent, trace-preserving and self-adjoint for the Hilbert-Schmidt pairing, and for every density matrix $\rho$ the entropy increase under $E$ is exactly a relative entropy: $S(E(\rho)) - S(\rho) = \rel{\rho}{E(\rho)} \geq 0$, with equality if and only if $\rho = E(\rho)$.

The level discrepancy of the chain is this quantity, so the cost of descent is an exact relative entropy rather than a qualitative statement.

## lay
Descent here means discarding the parts of a quantum state that link different sectors, keeping only the blocks along the diagonal. The theorem says the entropy gained by doing so equals a standard measure of how distinguishable the original state is from its descended version. The gain is never negative, and it is zero only when there was nothing to discard.

## one-liner
For any pinching $E$ and density matrix $\rho$, $S(E(\rho)) - S(\rho) = \rel{\rho}{E(\rho)} \geq 0$, with equality exactly when $\rho = E(\rho)$.
