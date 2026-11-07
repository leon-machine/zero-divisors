---
id: simulations.cluster-bound-two-dimensions
kind: claim
version: 4
title: The cluster bound in two dimensions
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
- name: Claude Opus 5.5
  role: consistency pass, premise R3 named where the core spacing uses it
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - simulations.effective-cross-section-sheet-matter@3
  - simulations.imported-low-energy-scattering-two-dimensions@1
  assumes:
  - dark-matter.r1-equal-mass-per-quantum@1
  - dark-matter.r2-one-quantum-per-unit-ball@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_wave_number
- kind: check
  ref: check.py::check_hard_disk_lengths
- kind: check
  ref: check.py::check_cluster_bound_on_lambda
- kind: check
  ref: check.py::check_size_and_phase_shift_limits
locators:
  paper: T14b
  number: Comp 3.3
  label: prop:scatter
  line: 199
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The lay level, the one-liner and the proof attributed the core spacing to R1 and R2 only; the sheets'' spacing is R3''s, reached through simulations.effective-cross-section-sheet-matter, which assumes it (the technical level already said R1 to R3). Wording and citation; no edge changed.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the wave number, the hard-disk lengths by partial waves and the logarithmic form, the bound on lambda, and the size and phase-shift limits, by exact interval arithmetic. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    added:
    - simulations.effective-cross-section-sheet-matter
    - simulations.imported-low-energy-scattering-two-dimensions
    - dark-matter.r1-equal-mass-per-quantum
    - dark-matter.r2-one-quantum-per-unit-ball
    note: 'No proof environment: the paper''s ''How it is computed'' paragraph says (i) is the two-dimensional
      scattering fact evaluated and (ii) is the effective cross-section proposition solved for lambda,
      so those are the uses; R1 and R2 are assumed because the 3.5 cm core spacing is computed from them
      (R3 enters through the proposition); the cluster bound value itself is treated as a hypothesis of
      the statement, not a premise. Levels pass: the lay level and one-liner now name premises R1 and
      R2, which fix the core spacing, and the lay level keeps the nucleon-mass assumption.'
  env: computation
  flags:
  - no proof environment found
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - dark-matter.r1-equal-mass-per-quantum
    - dark-matter.r2-one-quantum-per-unit-ball
    note: The proof is a pointer to two cited results, so R1 and R2 are given a closing role sentence (the
      core spacing, as the typing note records).
---

## formal
For quanta of the nucleon mass at a relative speed of $3000$ km/s ($k = 0.0238\ \mathrm{fm^{-1}}$ in the centre-of-mass frame):
\begin{enumerate}
\item[(i)] a hard disk of radius $0.21$ fm has $\lambda = 13$ fm from the partial-wave sum and $14$ fm from the logarithmic form; of radius $10^{-11}$ fm, still $\lambda = 0.49$ fm;
\item[(ii)] the bound $\sigma_{\mathrm{eff}}/m < 1\ \cmg$ in a cluster core (isotropic spacing) requires $\lambda < 4.8 \times 10^{-12}$ fm;
\item[(iii)] by size alone that requires $a < 10^{-4.0 \times 10^{6}}$ fm; by interaction strength, an s-wave phase shift $\delta_{0} < 1.7 \times 10^{-7}$.
\end{enumerate}

## technical
Take quanta of the nucleon mass colliding at a relative speed of $3000$ km/s, so that $k = 0.0238\ \mathrm{fm^{-1}}$ in the centre-of-mass frame. In two dimensions the cross-section is a length, $\lambda = (4/k)\sum_{m}\sin^{2}\delta_{m}$. For a hard disk of radius $0.21$ fm it is $13$ fm from the partial-wave sum ($14$ fm from the logarithmic form), and even a disk of radius $10^{-11}$ fm gives $\lambda = 0.49$ fm, because at small $ka$ the radius enters only through $\lambda \approx \pi^{2}/\bigl(k(\ln(ka/2) + \gamma_{E})^{2}\bigr)$.

With $\sigma_{\mathrm{eff}} = \lambda s$ at the isotropic spacing of a cluster core, the bound $\sigma_{\mathrm{eff}}/m < 1\ \cmg$ requires $\lambda < 4.8 \times 10^{-12}$ fm. By size alone this needs $a < 10^{-4.0 \times 10^{6}}$ fm; through the interaction strength it needs an s-wave phase shift $\delta_{0} < 1.7 \times 10^{-7}$. These are numerical evaluations, with the spacing fixed by premises R1 to R3.

## lay
Matter confined to thin sheets scatters as if it lived in two dimensions, where a particle's target size is a length rather than an area. At the speeds of colliding galaxy clusters even an absurdly small particle presents a sizeable target, because its size enters only through a logarithm. Taking the quanta to have the nucleon's mass, with the spacing in a cluster core fixed by the paper's counting premises R1 to R3, to meet the observed limit on dark-matter collisions there the particles would have to be smaller than any physical scale, or barely interact at all.

## one-liner
For nucleon-mass sheet quanta at cluster speeds, assuming premises R1 to R3 for the core spacing, the cluster bound of $1\ \cmg$ needs an in-sheet cross-section below $4.8 \times 10^{-12}$ fm, which requires either an impossibly small size or an s-wave phase shift below $1.7 \times 10^{-7}$.
