---
id: simulations.averaged-pair-operator
kind: claim
version: 5
title: The averaged pair operator
status: proved
region: simulations
subject: dark-matter
tags:
- halos-and-clusters
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.vector-squares@1
  - std-algebra.product-decomposition@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_conservation
- kind: check
  ref: check.py::check_parallel_normals_rejection
- kind: check
  ref: check.py::check_orthogonal_normals_and_idempotence
locators:
  paper: T14b
  number: Lem 4.1
  label: lem:projector
  line: 308
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares, std-algebra.product-decomposition where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: symmetry and pair conservation, the rejection for parallel normals in GA, and the eigenvalues and idempotence condition. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: Self-contained algebraic lemma; no edges, and the paper's citation of the standard symmetric
      SPH form is for the equations, not a statement that the lemma is recovered classically.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - simulations.s2-sheet-fluid (motivated_by)
    added_about: []
    verdict: standalone
    note: A lemma about the adopted pair rule that no proof uses; Premise S2 describes the rule by it,
      recorded as S2's lineage.
---

## formal
\begin{enumerate}
\item[(i)] $P_{ij} = P_{ji}$, and the contracted pair forces conserve momentum exactly and, in the equations before time integration and with the smoothing lengths held fixed within a step, total energy.
\item[(ii)] For parallel normals $\mathbf{n}_{i} = \mathbf{n}_{j} = \mathbf{n}$, $P_{ij}$ is the projection onto the sheet: in the geometric algebra of $\mathbb{R}^{3}$ it is the rejection $\mathbf{v} \mapsto (\mathbf{v}\wedge\mathbf{n})\,\mathbf{n}$, and it annihilates $\mathbf{n}$.
\item[(iii)] For orthogonal normals it keeps half of each normal component; its eigenvalues are then $1$, $\tfrac{1}{2}$, $\tfrac{1}{2}$, so it is idempotent only when $\mathbf{n}_{i} = \pm\mathbf{n}_{j}$.
\end{enumerate}

## technical
In the simulations the sheet fluid's pair forces are contracted with $P_{ij} = I - \tfrac{1}{2}(\mathbf{n}_{i}\mathbf{n}_{i}^{\mathsf T} + \mathbf{n}_{j}\mathbf{n}_{j}^{\mathsf T})$, the mean of the two particles' in-plane projectors. Since $P_{ij} = P_{ji}$ and the kernel gradient is antisymmetric, the contracted pair forces conserve momentum exactly and, in the equations before time integration and with the smoothing lengths held fixed within a step, total energy. For parallel normals with $Q(\mathbf{n}) = 1$, $P_{ij}$ is the rejection $\mathbf{v} \mapsto (\mathbf{v}\wedge\mathbf{n})\,\mathbf{n}$, the projection onto the sheet, and annihilates $\mathbf{n}$. For orthogonal normals its eigenvalues are $1, \tfrac{1}{2}, \tfrac{1}{2}$, keeping half of each normal component, and it is idempotent only when $\mathbf{n}_{i} = \pm\mathbf{n}_{j}$.

## lay
The simulations model three-dimensional dark matter as sheets that can only push along their own surface. Forces between two such particles are filtered through an averaged projection that keeps the part lying in the sheets. This result checks that the filter still conserves momentum and, within each step, energy, that it is an exact projection when the sheets are parallel, and that it is only a partial one when they are not.

## one-liner
The averaged pair operator $P_{ij}$ is symmetric, so the contracted forces conserve momentum and, step by step, energy; it is the sheet projection for parallel normals and is idempotent only when the normals agree up to sign.
