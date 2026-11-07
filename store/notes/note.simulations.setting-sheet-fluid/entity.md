---
id: note.simulations.setting-sheet-fluid
kind: note
version: 2
title: The sheet fluid
status: setting
subject: dark-matter
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
- name: Claude Opus 5.5
  role: consistency pass, the averaged pair operator written as a linear map of vectors
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- simulations.averaged-pair-operator
locators:
  paper: T14b
  number: Setting
  section: The simulation code
  line: 300
  subsection: The sheet fluid
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The matrix form with an identity matrix I (the pseudoscalar''s symbol) and outer products n n^T is written as the linear map v -> v - ((v.n_i)n_i + (v.n_j)n_j)/2, the in-plane projectors as the rejections of the Lemma; pure notation, as in simulations.averaged-pair-operator.'
---

## formal
Premise S2 is implemented by contracting both the kernel gradient and the separation vector of every pair of sheet-fluid particles with an averaged pair operator before they enter the equations above. With $\mathbf{n}_{i}$ and $\mathbf{n}_{j}$ the unit normals of the two particles' sheets,
\begin{equation}
P_{ij}(\mathbf{v}) \;=\; \mathbf{v} - \tfrac{1}{2}\bigl((\mathbf{v}\cdot\mathbf{n}_{i})\mathbf{n}_{i} + (\mathbf{v}\cdot\mathbf{n}_{j})\mathbf{n}_{j}\bigr),
\qquad
\mathbf{g}_{ij} \mapsto P_{ij}\mathbf{g}_{ij}, \quad \mathbf{r}_{ij} \mapsto P_{ij}\mathbf{r}_{ij}.
\end{equation}
$P_{ij}$ is the mean of the two in-plane projectors, the rejections $\mathbf{v} \mapsto (\mathbf{v}\wedge\mathbf{n}_{i})\,\mathbf{n}_{i}$ and $\mathbf{v} \mapsto (\mathbf{v}\wedge\mathbf{n}_{j})\,\mathbf{n}_{j}$ (Lemma \claimref{simulations.averaged-pair-operator}(ii)). When all normals are parallel it is the projection onto the common sheet, nothing acts along the normal except gravity, and motion along it is ballistic; for differently oriented normals it is not a projection and keeps part of each normal component (Lemma \claimref{simulations.averaged-pair-operator}(iii)). Each particle's normal is fixed at its initial value, random per particle or common to all (Section \ref{sec:ics}).

## technical
pending

## lay
pending

## one-liner
pending
