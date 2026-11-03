---
id: note.simulations.setting-sheet-fluid
kind: note
version: 1
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
comments_on:
- simulations.averaged-pair-operator
locators:
  paper: T14b
  number: Setting
  section: The simulation code
  line: 300
  subsection: The sheet fluid
---

## formal
Premise S2 is implemented by contracting both the kernel gradient and the separation vector of every pair of sheet-fluid particles with an averaged pair operator before they enter the equations above. With $\mathbf{n}_{i}$ and $\mathbf{n}_{j}$ the unit normals of the two particles' sheets,
\begin{equation}
P_{ij} \;=\; I - \tfrac{1}{2}\bigl(\mathbf{n}_{i}\mathbf{n}_{i}^{\mathsf T} + \mathbf{n}_{j}\mathbf{n}_{j}^{\mathsf T}\bigr),
\qquad
\mathbf{g}_{ij} \mapsto P_{ij}\mathbf{g}_{ij}, \quad \mathbf{r}_{ij} \mapsto P_{ij}\mathbf{r}_{ij}.
\end{equation}
$P_{ij}$ is the mean of the two in-plane projectors $I - \mathbf{n}_{i}\mathbf{n}_{i}^{\mathsf T}$ and $I - \mathbf{n}_{j}\mathbf{n}_{j}^{\mathsf T}$. When all normals are parallel it is the projection onto the common sheet, nothing acts along the normal except gravity, and motion along it is ballistic; for differently oriented normals it is not a projection and keeps part of each normal component (Lemma \claimref{simulations.averaged-pair-operator}(iii)). Each particle's normal is fixed at its initial value, random per particle or common to all (Section \ref{sec:ics}).

## technical
pending

## lay
pending

## one-liner
pending
