---
id: singularity.schmidt-forcing-proved-outright
kind: claim
version: 4
title: Schmidt forcing, proved outright
status: proved
region: singularity
subject: descent
tags: [entanglement, forcing-and-uniqueness]
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
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.2
- kind: check
  ref: check.py::check_invariance_forces_one_eigenspace
- kind: check
  ref: check.py::check_cyclic_separating_only_on_the_number_basis
- kind: check
  ref: check.py::check_phase_convention_gives_cos_sin
locators:
  paper: T05
  number: Lem 7.2
  label: lem:schmidt
  line: 1713
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: invariance up to phase forces one eigenspace of G over all 15 supports, cyclic and separating only on the number basis (determinant a^2 b^2), and the phase convention. Version 2 -> 3. Sample inputs moved to module level; the support count 2^4 - 1 = 15 is now asserted; no other change to what is tested. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'Removed the mechanical transport-algorithm edge: the proof is a spectral computation on the
      explicit generator G; the modular structure theorem is cited only to name G as the boost and was
      not added, so this lemma now has no premises. Levels pass: conditions already kept.'
  env: lemma
  context_refs:
  - singularity.modular-structure-completed-pair
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$e^{itG}$ on $\C^2 \otimes \C^2$: the doubled system''s Hilbert space in the cyclic-and-separating
      setting of modular theory (imported Hilbert space, matrix algebra over $\C$); doubtful, since $G$
      is built from number operators; $(i - j)$ is an index'
---

## formal
Realise the boost on the doubled system by the one-parameter unitary group $e^{i t G}$, $G = N \otimes 1 - 1 \otimes N$ (the pair carries the flow of Theorem \claimref{singularity.modular-structure-completed-pair}, the partner the mirrored flow). If a unit vector $\Omega \in \C^2 \otimes \C^2$ is invariant up to phase under this group and is cyclic and separating for the pair factor, then
\[
\Omega \;=\; \cos\theta\,|00\rangle + \sin\theta\,|11\rangle \qquad \text{with } \cos\theta\sin\theta \neq 0 ,
\]
up to a global phase and a phase convention on $|11\rangle$: the Schmidt basis is the number basis.

## technical
Let the boost act on the doubled mode $\C^2 \otimes \C^2$ by the unitary group $e^{itG}$ with $G = N \otimes 1 - 1 \otimes N$. If a unit vector $\Omega$ is invariant up to phase under this group and is cyclic and separating for the pair factor, then up to a global phase and a phase convention on $|11\rangle$, $\Omega = \cos\theta\,|00\rangle + \sin\theta\,|11\rangle$ with $\cos\theta\sin\theta \neq 0$.

Invariance up to phase makes $\Omega$ an eigenvector of $G$, which acts as $G|ij\rangle = (i - j)|ij\rangle$. The eigenvectors for $\pm 1$ are product vectors, which cannot be cyclic and separating, so $\Omega$ lies in the zero eigenspace spanned by $|00\rangle$ and $|11\rangle$, and both coefficients must be nonzero for the same reason. The Schmidt basis is therefore the number basis.

## lay
Take one mode together with its partner. If their joint state is unchanged by the boost, apart from an overall phase, and is genuinely entangled, then there is no freedom in which basis the entanglement uses: it must pair empty with empty and occupied with occupied. Only the balance between those two terms is left free.

## one-liner
A unit vector on the doubled mode that is boost invariant up to phase and cyclic and separating is $\cos\theta\,|00\rangle + \sin\theta\,|11\rangle$ with both coefficients nonzero, so its Schmidt basis is the number basis.
