---
id: note.simulations.setting-halos
kind: note
version: 1
title: Halos
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
  section: Initial conditions
  line: 345
  subsection: Halos
---

## formal
A halo of mass $M_{200}$ and concentration $c$ is a Hernquist sphere of the same mass inside $r_{200}$, with the scale length that matches the Navarro-Frenk-White inner profile \cite{Hernquist1990, NFW1997, SpringelDiMatteoHernquist2005}:
\[
r_{200} = \Bigl(\frac{GM_{200}}{100H_{0}^{2}}\Bigr)^{1/3},\qquad
a = \frac{r_{200}}{c}\sqrt{2\Bigl[\ln(1 + c) - \frac{c}{1 + c}\Bigr]},\qquad
M_{H} = M_{200}\Bigl(1 + \frac{a}{r_{200}}\Bigr)^{2},
\]
with $H_{0} = 70$ km/s/Mpc; the first is the radius inside which the mean density is $200$ times critical, and the last makes the Hernquist enclosed mass $M_{H}r^{2}/(r + a)^{2}$ equal $M_{200}$ at $r_{200}$. The sphere is truncated at $15a$, keeping $225/256$ of $M_{H}$. Positions are drawn from the enclosed-mass profile; each particle is then assigned a species at random in proportion to the species' mass fraction (Premise S5).

Collisionless particles take speeds from the isotropic Hernquist distribution function $f(E)$ \cite{Hernquist1990} by rejection sampling up to the escape speed, with random directions. Fluid particles start at rest with $u = \sigma_{r}^{2}/(\gamma - 1)$, so that $P = \rho\sigma_{r}^{2}$ and the gas is in hydrostatic equilibrium with the isotropic Jeans dispersion
\[
\sigma_{r}^{2}(r) = \frac{GM_{H}}{12a}\Bigl[12x(1 + x)^{3}\ln\frac{1 + x}{x} - \frac{x}{1 + x}\bigl(25 + 52x + 42x^{2} + 12x^{3}\bigr)\Bigr], \qquad x = r/a ,
\]
which solves $d(\rho\sigma_{r}^{2})/dr = -\rho\,GM(r)/r^{2}$ for the Hernquist density. The sheet fluid has no pressure along its normal, so it also carries a Gaussian velocity of dispersion $\sigma_{r}$ along the normal.

## technical
pending

## lay
pending

## one-liner
pending
