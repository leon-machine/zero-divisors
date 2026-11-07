---
id: singularity.stretched-singularity-count
kind: claim
version: 7
title: The stretched singularity, and the count
status: proved
region: singularity
subject: entropy
tags: [mode-counting, schwarzschild, boundary-modes]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  uses:
  - singularity.imported-induced-geometry-interior-slice@2
  - singularity.modular-descent@6
  assumes:
  - singularity.c1-curvature-cutoff@4
  - singularity.c2-cell-density@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:10.6
- kind: check
  ref: check.py::check_induced_metric_on_the_slice
- kind: check
  ref: check.py::check_slice_volume_identities
- kind: check
  ref: check.py::check_mode_rate_keeps_hawking_time
- kind: check
  ref: check.py::check_fixed_cutoff_radius_fails
locators:
  paper: T05
  number: Prop 10.6
  label: prop:count
  line: 2165
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the induced slice metric blade-exact in Cl(1,3), the slice volume and rate identities along the (C1) locus, kappa from f'', and the fixed-radius control. Version 5 -> 6. Check strengthened: horizon r = 2M pinned and sample volumes matched to the exact (2M)^2 (1 - r_c/2M) in place of loose bounds; sample radii moved to module level. Version 6 -> 7.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the slice is the background surface r = r_c of the Painleve-Gullstrand gauge field with the induced metric read from hb^{-1}; the count unchanged. Proof prefixed.'
  env: proposition
  context_refs:
  - singularity.assembled-page-curve-up-typicality
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.c1-curvature-cutoff
    - singularity.c2-cell-density
    note: 'Kept the slice geometry and modular descent (which supplies 8 pi M = 1/T_H), added the postulates
      (C1) and (C2) the statement assumes, and removed the transport-algorithm repair edge as framing.
      Levels pass: lay now names (C1) and (C2) and the leading-order, large-mass qualifier.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - singularity.c2-cell-density
---

## formal
Assume (C1) and (C2). For the Schwarzschild field in the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$, $\beta = \sqrt{2M/r}$, of Fact \claimref{sheaf.gauge-field-cometric}, the three-volume of the background slice $r = r_c$ per unit Killing time, from the metric induced by $\hb^{-1}$ (Fact \claimref{singularity.imported-induced-geometry-interior-slice}), is
\[
4\pi\,r_c^{2}\sqrt{|f(r_c)|} \;=\; 4\pi\sqrt{2M}\,r_c^{3/2}\sqrt{1 - \tfrac{r_c}{2M}} \;=\; 8\pi M\sqrt{1 - \tfrac{r_c}{2M}} \;=\; 8\pi M\,\bigl(1 + O(M^{-2/3})\bigr) ,
\]
using $r_c^{3} = 2M$: the cutoff radius conspires with the anisotropic stretch to leave \emph{linear} mass dependence at leading order, special to this cutoff (a mass-independent cutoff radius gives $M^{1/2}$ and can never reach the area law). With $\nu$ fermionic modes per Planck cell, and writing $N_{\mathrm{6a}}$ for the number of boundary modes (the notation Steps 6b and Fact \claimref{singularity.assembled-page-curve-up-typicality} use for this section's count),
\[
\frac{dN_{\mathrm{6a}}}{dt} \;=\; 8\pi\nu M\sqrt{1 - \tfrac{r_c}{2M}} \;=\; \frac{\nu}{\TH}\sqrt{1 - \tfrac{r_c}{2M}} :
\]
the stretched singularity registers $\nu$ modes per Hawking period up to the correction factor $\sqrt{1 - r_c/2M}$, which tends to $1$ as $M \to \infty$ in Planck units ($r_c/2M = (2M)^{-2/3}$). It keeps time with the horizon's own clock.

## technical
Assume (C1) and (C2). From the geometry the Painlev\'e-Gullstrand gauge field induces on the background slice $r = r_c$, its three-volume per unit Killing time is $4\pi r_c^2\sqrt{|f(r_c)|} = 8\pi M\sqrt{1 - r_c/2M} = 8\pi M\bigl(1 + O(M^{-2/3})\bigr)$, using $r_c^3 = 2M$: linear in the mass at leading order, which is special to this cutoff.

With $\nu$ modes per Planck cell, $dN_{\mathrm{6a}}/dt = 8\pi\nu M\sqrt{1 - r_c/2M} = (\nu/\TH)\sqrt{1 - r_c/2M}$, using $8\pi M = 1/\TH$ from modular descent: $\nu$ modes per Hawking period, up to a correction factor that tends to $1$ at large $M$.

## lay
Assume premise (C1), that the quantum modes are counted on a surface inside the black hole where curvature reaches the Planck scale, and premise (C2), that they are packed at a fixed number per Planck-sized cell. For a large black hole the volume of that surface grows with outside clock time at a rate proportional to the mass, at leading order, a coincidence special to this choice of surface. As a result, the surface gains modes at a steady rate set by the black hole's Hawking temperature.

## one-liner
Under (C1) and (C2), the stretched singularity's volume per unit Killing time is $8\pi M$ at leading order, so it gains about $\nu/\TH$ modes per unit time.
