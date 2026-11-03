---
id: singularity.what-event-returns-radiation
kind: claim
version: 5
title: What an event returns to the radiation
status: proved
region: singularity
subject: entropy
tags: [radiation-spectrum, entanglement]
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
  - singularity.eviction-window-thermal-product-radiation-entropy@7
  - singularity.purity-correlation-transfer-recovery@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:11.7
- kind: check
  ref: check.py::check_block_entropy_and_returned_information
- kind: check
  ref: check.py::check_evicted_qubit_correlated_with_radiation_not_partner
- kind: check
  ref: check.py::check_idealisation_returns_two_ln_two
locators:
  paper: T05
  number: Cor 11.7
  label: cor:mirror
  line: 2298
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: S(A) = h_k + sum h_j and I(A:R_<) = 2 sum h_j at every event of three runs, I(L_j:R_<) = 2 h_j with partner damping, and 2 ln 2 in the idealisation. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  env: corollary
  context_refs:
  - singularity.purity-correlation-transfer-recovery
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.purity-correlation-transfer-recovery
    note: 'Kept the eviction theorem, added the correlation-transfer proposition whose clause (2) gives
      the strict inequality for a single partner, and removed the transport-algorithm repair edge; the
      paper says this reproduces the Hayden-Preskill mirror behaviour, which is not an imported claim
      in the store, so no standard route. Levels pass: the lay now carries the eviction theorem''s hypotheses,
      as the technical and one-liner do.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    stated_role:
    - singularity.purity-correlation-transfer-recovery
---

## formal
At an emission event let $A$ be the block the event adds to the radiation, the new quantum $R_k$ together with the qubits $L_j$ evicted at that event, and $R_{<}$ the radiation already present. Then, under the hypotheses of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy},
\[
S(\rho_A) \;=\; h_k + \sum_{j\ \mathrm{evicted}} h_j , \qquad I(A{:}R_{<}) \;=\; 2\sum_{j\ \mathrm{evicted}} h_j :
\]
the new quantum arrives uncorrelated with the earlier radiation, and every evicted qubit arrives fully correlated with the earlier radiation as a whole, $I(L_j{:}R_{<}) = 2h_j$, the maximum a qubit of entropy $h_j$ can carry. That correlation is not, in general, with its own partner $R_j$ alone: the pair coherence is damped by the scrambling (Proposition \claimref{singularity.purity-correlation-transfer-recovery}(2)), so $I(L_j{:}R_j) < 2h_j$ once a gate has acted, and the remainder lies in the multi-qubit correlations of Proposition \claimref{singularity.purity-correlation-transfer-recovery}(3). In the maximally entangled idealisation with one eviction per event, $I(A{:}R_{<}) = 2\ln 2 = S(\rho_A)$: the block is returned to the radiation fully correlated, at the rate the capacity falls. This is the sense in which the rate model reproduces the mirror behaviour of \cite{HP2007}: the window returns information at the rate it loses capacity, by eviction, not by scrambling.

## technical
Under the hypotheses of the eviction theorem, let $A$ be the block an emission event adds to the radiation, the new quantum $R_k$ with the qubits $L_j$ evicted at that event, and $R_{<}$ the radiation already present. Then $S(\rho_A) = h_k + \sum_j h_j$ and $I(A{:}R_{<}) = 2\sum_j h_j$: the new quantum arrives uncorrelated with the earlier radiation and each evicted qubit arrives with $I(L_j{:}R_{<}) = 2h_j$, the maximum for its entropy.

Once a gate has acted, that correlation is not with the partner $R_j$ alone, $I(L_j{:}R_j) < 2h_j$, the remainder lying in multi-qubit correlations. In the maximally entangled idealisation with one eviction per event, $I(A{:}R_{<}) = 2\ln 2 = S(\rho_A)$.

## lay
Under the hypotheses of the evaporation model's eviction theorem, each time the model black hole emits, it releases a new quantum and may push out some interior partners. The new quantum carries no information about the earlier radiation, but each pushed-out partner is as correlated with the earlier radiation as it can be. So information comes back by eviction, at the rate the capacity shrinks, matching the known mirror-like behaviour of black holes rather than arising from scrambling.

## one-liner
Under the eviction-theorem hypotheses, an emission event returns $I(A{:}R_{<}) = 2\sum_j h_j$ to the radiation, all of it carried by the evicted qubits.
