---
id: note.simulations.setting-gravity
kind: note
version: 1
title: Gravity
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
  line: 260
  subsection: Gravity
---

## formal
Gravity is computed with a Barnes-Hut octree \cite{BarnesHut1986}. A node of side $\ell$ at distance $r$ from its centre of mass is opened if $\ell^{2} > \theta^{2}r^{2}$ or if the particle lies inside it, with $\theta = 0.7$. Forces use Plummer softening,
\[
\mathbf{a}_{i} \;=\; \sum_{j} G\,m_{j}\,\frac{\mathbf{r}_{j} - \mathbf{r}_{i}}{\bigl(|\mathbf{r}_{j} - \mathbf{r}_{i}|^{2} + \epsilon^{2}\bigr)^{3/2}},
\qquad \epsilon = 15\ \kpc ,
\]
with nodes standing in for the particles they contain.

## technical
pending

## lay
pending

## one-liner
pending
