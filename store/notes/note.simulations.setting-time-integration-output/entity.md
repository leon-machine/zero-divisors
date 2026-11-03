---
id: note.simulations.setting-time-integration-output
kind: note
version: 1
title: Time integration and output
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
- simulations.merger
locators:
  paper: T14b
  number: Setting
  section: The simulation code
  line: 332
  subsection: Time integration and output
---

## formal
All particles share one time step,
\[
\Delta t = \min\Bigl(\Delta t_{\max},\ \min_{i}\tfrac{1}{4}\sqrt{\epsilon/|\mathbf{a}_{i}|},\ \min_{i\in\text{fluid}}\tfrac{1}{4}h_{i}/v_{\mathrm{sig},i}\Bigr),\qquad
v_{\mathrm{sig},i} = \max\Bigl(2c_{i},\ \max_{j}\bigl(c_{i} + c_{j} - 3w_{ij}\bigr)\Bigr),
\]
with $\Delta t_{\max} = 0.002$, the inner maximum over approaching pairs, and $w_{ij} = \mathbf{v}_{ij}\cdot\mathbf{r}_{ij}/r_{ij}$, negative on approach. The integrator is kick-drift-kick leapfrog, with the step shortened to land on each output time. Snapshots record positions, velocities, masses, internal energies, densities, smoothing lengths, types and halo labels. A merger run takes $15$ to $60$ minutes on two cores.

## technical
pending

## lay
pending

## one-liner
pending
