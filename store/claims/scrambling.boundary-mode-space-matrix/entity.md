---
id: scrambling.boundary-mode-space-matrix
kind: claim
version: 4
title: The boundary mode space as matrix
status: proved
region: scrambling
subject: entropy
tags: [boundary-modes, idempotents]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.witt-basis-car@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:prop:matrix
- kind: check
  ref: check.py::check_gl_relations_on_fock_space
- kind: check
  ref: check.py::check_one_particle_restriction_is_onto
- kind: check
  ref: check.py::check_doubling_gives_gl_n_in_clifford_algebra
locators:
  paper: T08
  number: Prop 5.2
  label: prop:matrix
  line: 855
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-basis-car where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: gl(n) commutator table on the full 4-mode Fock space, one-particle restriction onto Mat_n (n = 3, 4, 5), and the doubling in Cl(n,n) giving gl(n) against so(n). Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - hawking.current-commutator-exactly-edge-split
    note: 'Removed the edge to the current-commutator result: the proof cites it only as the place the
      same bilinear computation was used for the currents, and derives the general-index commutator directly
      from the CAR; doubtful only if the maintainer reads that citation as the source of the identity.'
---

## formal
Let the boundary mode space carry $n$ completed pairs, $n$ counted after the completion's doubling (each mode with its adjoined partner). The gauge-invariant bilinears $E_{ij} := \psi_i^\dagger \psi_j$ satisfy $[E_{ij}, E_{kl}] = \delta_{jk}E_{il} - \delta_{li}E_{kj}$ (the $\mathfrak{gl}(n)$ relations, an instance of the CAR bilinear commutator), preserve the one-particle subspace, and restrict on it to the full matrix algebra: $E_{ij}|_{\text{one-particle}} = $ the matrix unit $e_{ij}$, so the associative algebra they generate restricts onto $\Mat_n$. The doubling the completion forces is exactly what turns a tower of modes into a matrix; and matrices can be spheres.

## technical
Take $n$ completed pairs on the boundary mode space, with mode operators $\psi_i$ obeying the canonical anticommutation relations. The gauge-invariant bilinears $E_{ij} = \psi_i^\dagger\psi_j$ satisfy the $\mathfrak{gl}(n)$ relations $[E_{ij}, E_{kl}] = \delta_{jk}E_{il} - \delta_{li}E_{kj}$, map the one-particle subspace to itself, and act there as the matrix units $e_{ij}$, so the algebra they generate restricts onto $\Mat_n$.

The doubling the completion forces, each mode with its adjoined partner, is what supplies the complex operators $\psi_i, \psi_i^\dagger$ and hence the matrix structure; real Clifford directions alone give only the orthogonal bilinears.

## lay
The black hole's boundary modes come in pairs, and the pairs can be combined into operations that move one quantum from one mode to another. On states holding a single quantum, these operations behave exactly like the entries of an $n \times n$ matrix. This matrix structure is what later lets a sphere emerge from the modes.

## one-liner
The bilinears $\psi_i^\dagger\psi_j$ of $n$ completed boundary-mode pairs obey the $\mathfrak{gl}(n)$ relations and restrict on the one-particle subspace onto the full matrix algebra $\Mat_n$.
