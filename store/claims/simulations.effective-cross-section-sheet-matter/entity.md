---
id: simulations.effective-cross-section-sheet-matter
kind: claim
version: 3
title: The effective cross-section of sheet matter
status: proved
region: simulations
subject: dark-matter
tags: [halos-and-clusters]
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
  assumes:
  - dark-matter.r3-one-cell-per-unshared-direction@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_number_density_by_counting
- kind: check
  ref: check.py::check_collision_rate_equivalence
- kind: check
  ref: check.py::check_spacing_bounds_under_compression
locators:
  paper: T14b
  number: Prop 3.1
  label: prop:sigmaeff
  line: 164
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: n3 = n2/s by counting lattice quanta, sigma_eff = lambda s from equal collision rates, and the spacing bounds under compression. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    note: 'Kept the R3 assumption, which the proof invokes for the mean sheet spacing; the result is a
      direct rate identity with no standard-route claim in the paper. Levels pass: the lay level now names
      premise R3 for the sheet spacing.'
  env: proposition
---

## formal
Let the sheets carry $n_{2}$ quanta per unit area, be stacked a distance $s$ apart, and let each quantum have in-sheet cross-section $\lambda$. Then the collision rate of a quantum moving at speed $v$ equals that of a three-dimensional gas of number density $n_{3} = n_{2}/s$ with cross-section
\[
\sigma_{\mathrm{eff}} \;=\; \lambda\, s ,
\qquad\text{so}\qquad
\frac{\sigma_{\mathrm{eff}}}{m} \;=\; \frac{\lambda s}{m}.
\]
In a halo region of overdensity $\Delta$ at redshift $z$ the spacing lies between $d_{b}\Delta^{-1}/(1+z)$ (all compression along the normal) and $d_{b}/(1+z)$ (all compression in the plane), and is $s = d_{b}\Delta^{-1/3}/(1+z)$ for isotropic compression.

## technical
A quantum of a three-dimensional tower moves in a two-dimensional sheet and collides only with quanta of its own sheet, so its cross-section is a length $\lambda$. If the sheets carry $n_{2}$ quanta per unit area and are stacked a distance $s$ apart, the in-sheet collision rate is $n_{2}\lambda v = (n_{2}/s)(\lambda s)v$, the rate in a three-dimensional gas of density $n_{3} = n_{2}/s$ with $\sigma_{\mathrm{eff}} = \lambda s$, so $\sigma_{\mathrm{eff}}/m = \lambda s/m$.

Under premise R3 the sheets are a cell radius $d_{b}$ apart in the mean, comoving. In a region of overdensity $\Delta$ at redshift $z$ the spacing is $d_{b}\Delta^{-1}/(1+z)$ if all the compression is along the normal, $d_{b}/(1+z)$ if it is all in the plane, and $d_{b}\Delta^{-1/3}/(1+z)$ for isotropic compression.

## lay
Matter that lives on stacked sheets collides only within its own sheet. Seen from three dimensions, its collisions look like those of an ordinary gas whose effective target area is the in-sheet target length multiplied by the spacing between sheets. Under premise R3, that the sheets lie on average one cell radius apart, how far apart they are in a galaxy cluster depends on how the cluster has squeezed them.

## one-liner
Sheet matter with in-sheet cross-section $\lambda$ on sheets a distance $s$ apart collides like a three-dimensional gas with $\sigma_{\mathrm{eff}} = \lambda s$, the spacing set by the region's compression under premise R3.
