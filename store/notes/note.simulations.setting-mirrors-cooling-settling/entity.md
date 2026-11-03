---
id: note.simulations.setting-mirrors-cooling-settling
kind: note
version: 1
title: The mirror's cooling and settling
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
  line: 324
  subsection: The mirror's cooling and settling
---

## formal
Bremsstrahlung from a fully ionised helium plasma, with Gaunt factor $1.2$ and $Z^{2} = 4$, gives $du/dt = -A\rho\sqrt{u}$ for a constant $A$. At fixed density this has the exact solution
\[
\sqrt{u(t + \Delta t)} \;=\; \sqrt{u(t)} - \tfrac{1}{2}A\rho\,\Delta t ,
\]
which the code applies after each step. When $u$ falls below $3u_{\mathrm{floor}}$ (for the helium plasma, $\mu = 4/3$, about $6.7 \times 10^{4}$ K) the particle becomes type $5$ and is collisionless from then on (Premise S3).

## technical
pending

## lay
pending

## one-liner
pending
