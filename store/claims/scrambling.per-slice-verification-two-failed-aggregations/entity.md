---
id: scrambling.per-slice-verification-two-failed-aggregations
kind: claim
version: 4
title: The per-slice verification, and the two failed aggregations
status: proved
region: scrambling
subject: entropy
tags: [mode-counting]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
about:
- obj.scrambling.stretched-singularity
derivations:
- name: main
  uses:
  - scrambling.integer-holographic-form-identification@2
  - scrambling.slice-volume-exactly-per-unit-killing@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:prop:n2
- kind: check
  ref: check.py::check_slice_check_scaling
- kind: check
  ref: check.py::check_operator_cell_aggregation_overshoot
- kind: check
  ref: check.py::check_fundamental_aggregation_breaks_scaling
locators:
  paper: T08
  number: Prop 5.7
  label: prop:n2
  line: 887
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: n^2 = 4 pi (2M)^(2/3), overshoot 16 pi, spheres per unit time (2M)^(1/3) and fundamental aggregation exponent 5/3. Version 3 -> 4.'
  env: proposition
  context_refs:
  - scrambling.slice-volume-exactly-per-unit-killing
  - scrambling.uniqueness-internal-scaling
  typing:
    by: ai-typing-pass
    added:
    - scrambling.slice-volume-exactly-per-unit-killing
    note: 'Kept the holographic corollary (clause 2) and added the slice-volume proposition, which supplies
      the spheres per unit Killing time in clause 3; the uniqueness proposition in context_refs was not
      added because clause 1 only compares the fuzzy count with its sphere-only case, a judgement call.
      Levels pass: the lay now keeps the formal''s either-or outcome for the open task, including the
      intrinsic-clock premise.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - scrambling.slice-volume-exactly-per-unit-killing
---

## formal
Let $n$ be the linear size of the slice's matrix algebra. Then:
\begin{enumerate}
\item \emph{(The slice check, exact in scaling.)} Matching the fuzzy operator dimension to the slice sphere's Planck-cell count sets $n^2 = 4\pi r_c^2 = 4\pi(2M)^{2/3}$ to leading order ($n$ is an integer matrix size and the right side transcendental; what the match fixes exactly is the $M^{2/3}$ scaling): the fuzzy count reproduces, from the matrix side, exactly the sphere-only case of Proposition \claimref{scrambling.uniqueness-internal-scaling}, its $M^{2/3}$ scaling. The fuzzy geometry and the metric geometry agree slice by slice.
\item \emph{(Operator-cell aggregation fails, by exactly the area coefficient.)} Counting one boundary-mode fermion per operator cell of the epoch volume is the $\nu = 1$ reading, which overshoots $N_{\mathrm{epoch}} = \SBH$ by exactly $16\pi$ (Corollary \claimref{scrambling.integer-holographic-form-identification}(3)): the required thinning is the horizon-area coefficient itself.
\item \emph{(Fundamental-per-slice aggregation breaks the scaling.)} Counting $n \propto M^{1/3}$ fundamentals per sphere and aggregating over the epoch's spheres (the slice volume of Proposition \claimref{scrambling.slice-volume-exactly-per-unit-killing} contains $8\pi M/4\pi r_c^2 = (2M)^{1/3}$ spheres per unit Killing time) gives
\[
N_{\mathrm{fund}} \;\propto\; M^{1/3}\cdot M^{1/3}\cdot \Delta t \;\propto\; M^{5/3} \quad (\Delta t \sim M),
\]
which breaks the area scaling altogether.
\end{enumerate}
Both direct aggregation rules fail, so the slice-to-epoch aggregation is the weighted completion's task: derive $N_{\mathrm{epoch}} = \SBH$, or refute the intrinsic-clock premise.

## technical
Let $n$ be the linear size of the slice's matrix algebra. Matching the fuzzy operator count to the slice sphere's Planck cells sets $n^2 = 4\pi r_c^2 = 4\pi(2M)^{2/3}$ at leading order, which fixes exactly the $M^{2/3}$ scaling of the sphere-only count: the fuzzy and metric geometries agree slice by slice.

The two direct ways of aggregating slices over an epoch both fail. One fermion per operator cell of the epoch volume is the $\nu = 1$ reading and overshoots $N_{\mathrm{epoch}} = \SBH$ by exactly $16\pi$. Counting $n \propto M^{1/3}$ fundamentals per sphere over the $(2M)^{1/3}$ spheres per unit Killing time gives $N_{\mathrm{fund}} \propto M^{5/3}$ for $\Delta t \sim M$, breaking the area scaling. The aggregation is left to the weighted completion, which must derive $N_{\mathrm{epoch}} = \SBH$ or refute the intrinsic-clock premise.

## lay
On each slice of the interior, the matrix picture of the modes and the ordinary geometric picture agree on how the number of cells grows with the black hole's mass. But the two obvious ways of adding the slices up over one thermal cycle both fail: one gives too many modes by a factor of $16\pi$, the other grows with the wrong power of the mass. The right way of adding up is left to the weighted completion, which must either reproduce the entropy count or refute the premise that the hole's own clock sets the cycle.

## one-liner
The fuzzy count $n^2 = 4\pi r_c^2$ matches each slice's $M^{2/3}$ scaling, but both direct aggregations over the epoch fail, one by $16\pi$ and one by breaking the area scaling.
