---
id: hawking.kms-restricts-invariant-subalgebras
kind: claim
version: 3
title: KMS restricts to invariant subalgebras
status: proved
region: hawking
subject: descent
tags: [modular-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gibbs_state_is_kms_on_b
- kind: check
  ref: check.py::check_restriction_to_invariant_subalgebras
- kind: check
  ref: check.py::check_non_invariant_control
locators:
  paper: T07
  number: Lem 3.2
  label: lem:restrict
  line: 463
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: finite-dimensional core on Mat_4: the Gibbs state is KMS, four flow-invariant unital subalgebras are invariant under the continued flow and the restricted state satisfies the restricted KMS identity, with a non-invariant control. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: proved outright with no premises; the paper calls KMS theory standard only in its prior-art
      paragraph and no imported restriction lemma is in the store, so no standard route.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - hawking.imported-s-wave-bosonic-sector
    added_about: []
    verdict: connected
    note: The fact on the s-wave bosonic sector calls its KMS restriction step an instance of this lemma;
      the earlier pass left the edge out only because the lemma is stated after the fact, which creates
      no cycle.
---

## formal
If $\omega$ is $\alpha$-KMS at $\beta$ on $\mathfrak{B}$ and $\mathfrak{C} \subseteq \mathfrak{B}$ is a unital subalgebra with $\alpha_t(\mathfrak{C}) = \mathfrak{C}$, then $\omega|_{\mathfrak{C}}$ is KMS at $\beta$ for $\alpha|_{\mathfrak{C}}$.

## technical
Let $\omega$ be $\alpha$-KMS at $\beta$ on $\mathfrak{B}$ and let $\mathfrak{C}\subseteq\mathfrak{B}$ be a unital subalgebra with $\alpha_t(\mathfrak{C}) = \mathfrak{C}$. Then the restriction $\omega|_{\mathfrak{C}}$ is KMS at $\beta$ for $\alpha|_{\mathfrak{C}}$.

For $x, y\in\mathfrak{C}$ the correlation function $t\mapsto\omega(y\,\alpha_t(x))$ is the same whether computed in $\mathfrak{C}$ or in $\mathfrak{B}$, so its continuation to the strip and the KMS boundary identity carry over unchanged.

## lay
If a system is in thermal equilibrium and one looks only at a set of observables that the time evolution keeps within itself, those observables are also in equilibrium at the same temperature.

## one-liner
A KMS state restricts to a KMS state at the same inverse temperature on any unital subalgebra invariant under the dynamics.
