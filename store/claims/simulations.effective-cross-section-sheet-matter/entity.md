---
id: simulations.effective-cross-section-sheet-matter
kind: claim
version: 4
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
- name: Claude Fable 5.2
  role: 'the mean sheet spacing named as the particle model''s length; R1 and R2 assumed'
  version: 4
  source: maintainer pass of 2026-11-19
amendments:
- version: 4
  kind: restatement
  defect: 'the statement put the mean sheet spacing at this world''s baryon spacing on R3 alone; R3''s unit is the length of Premise E, which is the baryon spacing only under R1 and R2'
review: typed
derivations:
- name: main
  assumes:
  - dark-matter.r1-equal-mass-per-quantum@1
  - dark-matter.r2-one-quantum-per-unit-ball@3
  - dark-matter.r3-one-cell-per-unshared-direction@3
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
  maintainer_pass_2026_11_19:
    by: maintainer-2026-11-19
    date: '2026-11-19'
    note: 'Version 3 -> 4. Leon''s decision of 19 November 2026 (R3''s unit is the length of Premise E): the mean sheet spacing was put at this world''s baryon spacing on R3 alone. Assumes edges to R1 and R2 are added, since that value is the particle model''s, and a marked note says so. The rate identity is unchanged.'
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
In a halo region of overdensity $\Delta$ at redshift $z$ the spacing lies between $d_{b}\Delta^{-1}/(1+z)$ (all compression along the normal) and $d_{b}/(1+z)$ (all compression in the plane), and is $s = d_{b}\Delta^{-1/3}/(1+z)$ for isotropic compression. Here $d_{b}$ is the mean comoving spacing of the sheets, which R3 sets at one unit. \emph{Note (19 November 2026).} R3's unit is the length of Premise E (\claimref{dark-matter.e-equal-mass-per-unit-ball}); it is this world's baryon spacing $d_{b}$ in the particle model, R1 and R2, assumed here for that value. The identity $\sigma_{\mathrm{eff}} = \lambda s$ needs neither.

## technical
A quantum of a three-dimensional tower moves in a two-dimensional sheet and collides only with quanta of its own sheet, so its cross-section is a length $\lambda$. If the sheets carry $n_{2}$ quanta per unit area and are stacked a distance $s$ apart, the in-sheet collision rate is $n_{2}\lambda v = (n_{2}/s)(\lambda s)v$, the rate in a three-dimensional gas of density $n_{3} = n_{2}/s$ with $\sigma_{\mathrm{eff}} = \lambda s$, so $\sigma_{\mathrm{eff}}/m = \lambda s/m$.

Under premise R3 the sheets are one unit apart in the mean, comoving, and in the particle model (R1 and R2) that unit is the cell radius $d_{b}$, this world's baryon spacing. In a region of overdensity $\Delta$ at redshift $z$ the spacing is $d_{b}\Delta^{-1}/(1+z)$ if all the compression is along the normal, $d_{b}/(1+z)$ if it is all in the plane, and $d_{b}\Delta^{-1/3}/(1+z)$ for isotropic compression.

## lay
Matter that lives on stacked sheets collides only within its own sheet. Seen from three dimensions, its collisions look like those of an ordinary gas whose effective target area is the in-sheet target length multiplied by the spacing between sheets. Under premise R3, that the sheets lie on average one unit of length apart (the particle spacing, in the particle picture assumed here), how far apart they are in a galaxy cluster depends on how the cluster has squeezed them.

## one-liner
Sheet matter with in-sheet cross-section $\lambda$ on sheets a distance $s$ apart collides like a three-dimensional gas with $\sigma_{\mathrm{eff}} = \lambda s$, the spacing set by the region's compression under premise R3, with the particle model's length.
