---
id: simulations.confinement-scale-does-not-matter
kind: claim
version: 4
title: The confinement scale does not matter
status: proved
region: simulations
subject: dark-matter
tags: [halos-and-clusters, confronted-with-data]
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
  - simulations.cluster-bound-two-dimensions@4
  - simulations.effective-cross-section-sheet-matter@4
  - simulations.imported-low-energy-scattering-two-dimensions@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_tiny_composite_still_scatters
- kind: check
  ref: check.py::check_still_a_fluid
- kind: check
  ref: check.py::check_size_enters_only_through_the_log
- kind: check
  ref: check.py::check_phase_shift_limits
locators:
  paper: T14b
  number: Cor 3.4
  label: cor:confinement
  line: 210
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: lambda at a = 1e-30 fm, the cross-section floor, the logarithmic dependence on size, and the two phase-shift limits. Version 2 -> 3. Check strengthened: at a = 1e-100 fm, ln(ka/2) = -234.7 and lambda/lambda_max = 1.6e9 are pinned (by hand) in place of the looser inequalities they imply. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - simulations.effective-cross-section-sheet-matter
    - simulations.imported-low-energy-scattering-two-dimensions
    note: 'The proof relies on the sigma_eff table (computed from the effective cross-section proposition)
      and applies the two-dimensional logarithmic form directly at a = 1e-30 fm, so both were added; Premise
      C is what the corollary motivates, not a premise of it, and the Bullet Cluster bound is used only
      as the comparison value, so neither was added. Levels pass: conditions already kept.'
  env: corollary
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - simulations.effective-cross-section-sheet-matter
    - simulations.imported-low-energy-scattering-two-dimensions
---

## formal
Any self-interaction of composite strength makes the three-dimensional towers' matter a fluid in clusters, whatever the size of a composite. The cluster bound is met only if the quanta barely interact: an in-sheet phase shift below about $2 \times 10^{-7}$ (isotropic compression in a core; about $4 \times 10^{-6}$ for compression normal to the sheets), which is Premise C.

## technical
Sheet matter with an in-sheet cross-section of composite size, $\lambda \ge 0.21$ fm, has $\sigma_{\mathrm{eff}}/m \ge 9.5 \times 10^{7}\ \cmg$ in every cluster region and compression, far above the cluster bounds, so on cluster scales it is a fluid. Shrinking the composite does not help: the radius enters only through $\lambda \approx \pi^{2}/\{k[\ln(ka/2) + \gamma_{E}]^{2}\}$, so even $a = 10^{-30}$ fm leaves $\lambda \approx 0.08$ fm and $\sigma_{\mathrm{eff}}/m \ge 3 \times 10^{7}\ \cmg$.

The bound can be met only if the quanta barely interact: an in-sheet s-wave phase shift below about $2 \times 10^{-7}$ for isotropic compression in a core, or about $4 \times 10^{-6}$ for compression normal to the sheets, since $\lambda \propto \sin^{2}\delta_{0}$ and the allowed $\lambda$ scales as $1/s$. That condition is Premise C.

## lay
However small the composite particles of the sheet-bound dark sectors are, if they interact with the strength typical of composite particles they collide so often in galaxy clusters that they behave as a fluid. Cluster observations rule that out. The only way out is for the particles to barely interact at all, which is a separate assumption that the particles' size cannot supply.

## one-liner
Any self-interaction of composite strength makes the three-dimensional towers' matter a fluid in clusters whatever the composite's size; the cluster bound needs an in-sheet phase shift below about $2 \times 10^{-7}$ (isotropic compression) or $4 \times 10^{-6}$ (normal compression).
