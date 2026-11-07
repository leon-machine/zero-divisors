---
id: synthesis.exceptional-boundary-measure-one-calibration
kind: claim
version: 2
title: 'Counting on the exceptional set, with the slice dropped'
status: proved
region: synthesis
subject: entropy
tags: [mode-counting, boundary-modes, schwarzschild, entropy-premises]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.kasner-form-interior@6
  - singularity.imported-interior-collar-kasner-form@6
  - scrambling.slice-volume-exactly-per-unit-killing@4
  - interior.imported-schwarzschild-curvature-spectrum@7
  - singularity.stretched-singularity-count@7
  - singularity.area-law-test@5
  - singularity.modular-descent@8
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_kasner_defining_function
- kind: check
  ref: check.py::check_measure_limit
- kind: check
  ref: check.py::check_threshold_to_proper_time
- kind: check
  ref: check.py::check_store_count_recovered
- kind: check
  ref: check.py::check_calibration
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.c1-curvature-cutoff
  - singularity.c2-cell-density
  - pred.boundary-mode-density
extraction:
  open_problem: pr.c1-c2-placement
  note: 'A corollary of the reduction of (C1) and (C2) to one calibration constant kappa_s = nu lambda^(-1/2) (filed alongside, synthesis.c1-c2-forms-forced-one-number). The exceptional set of the weighted blow-up carries a measure fixed by the metric, the limit of slice volume over proper time to the singularity, finite because the forced weights (the Kasner exponents) sum to one; at leading order the stretched-singularity count equals a density nu'' = (2/3) kappa_s per Planck area of that measure, so the slice of (C1) can be dropped for the leading count. The Kasner computation is classical GR (transport-convenient); the series content is that the counted modes are attributed to the exceptional set whose weights are forced. The area law fixes nu'', so the area-law test calibrates it rather than testing (C1) independently.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Schwarzschild field on flat spacetime inside its horizon locus, in its synchronous gauge with derived metric ds^2; the unit timelike gradient written Q(hb^T(nabla tau)) = 1; the measure fixed by the derived metric. Clauses (i)-(iv) unchanged; proof given a pointer.'
---

## formal
Work with the Schwarzschild gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) inside its horizon locus, in the synchronous gauge of Lemma \claimref{interior.kasner-form-interior}, whose derived metric is $ds^{2} = d\tau^{2} - A\,dt^{2} - r^{2}d\Omega^{2}$, $A = 2M/r - 1$, with $\tau$ the proper time to the singularity, and write $x := r/2M$. Let $E = \{\tau = 0\}\times\mathbb{R}_{t}\times S^{2}$ be the exceptional set of the weighted blow-up (Fact \claimref{singularity.imported-interior-collar-kasner-form}), whose weights are the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$.
\begin{enumerate}
\item[(i)] \emph{(Defining function.)} $\tau$ is the unique function of $r$ that vanishes on $E$ and has unit timelike physical gradient, $Q(\hb^{T}(\nabla\tau)) = A\,(d\tau/dr)^{2} = 1$; $\tau = \tfrac{2}{3}r^{3/2}(2M)^{-1/2}\,T(x)$ with $T(x) = \sum_{k} \tfrac{3}{2k+3}\binom{2k}{k}4^{-k}x^{k} = 1 + \tfrac{3}{10}x + O(x^{2})$.
\item[(ii)] \emph{(The measure.)} The three-volume per unit Killing time of the slice at proper time $\tau$ is $V(\tau) = 4\pi r^{2}\sqrt{A} = 12\pi M\,\tau\,\bigl(1 - \tfrac45 x + O(x^{2})\bigr)$, so
\[
\mu_{E} \;:=\; \lim_{\tau\to 0}\frac{V(\tau)}{\tau} \;=\; 12\pi M \quad\text{per unit Killing time}\qquad (3M\,dt\,d\Omega),
\]
finite and nonzero because the weights sum to one ($V \propto \tau^{p_{1}+p_{2}+p_{3}}$, $p_{1}+p_{2}+p_{3} = 1$). It is a measure on $E$ of the dimension of an area, fixed by the derived metric with no free constant, by (i).
\item[(iii)] \emph{(The count on $E$, at leading order.)} An eigenvalue threshold $2M/r^{3} = \lambda$ is the slice $\tau_{c} = \tfrac23\lambda^{-1/2}\bigl(1 + O(x_{c})\bigr)$, since $(2M/r^{3})\tau^{2} = \tfrac49 T(x)^{2}$. Under (C1) and (C2) the count of Proposition \claimref{singularity.stretched-singularity-count} is $dN/dt = \nu V(\tau_{c}) = \nu\tau_{c}\mu_{E}\sqrt{1-x_{c}}/T(x_{c})$, which at the slice of (C1) ($\lambda = 1$) is exactly $8\pi\nu M\sqrt{1 - x_{c}}$. Hence, at leading order in $x_{c} = (2M)^{-2/3}$, $dN/dt = \nu'\mu_{E}$ with
\[
\nu' \;:=\; \nu\,\tau_{c} \;=\; \tfrac23\,\kappa_{s}, \qquad \kappa_{s} := \nu\lambda^{-1/2},
\]
the single constant to which (C1) and (C2) reduce at leading order (filed alongside, synthesis.c1-c2-forms-forced-one-number). So, for the count at leading order, (C1) and (C2) can be replaced by the single premise (C2$'$): the boundary modes are carried by $E$ itself with $\nu'$ fermionic modes per Planck area of $\mu_{E}$; the two give the same leading count, and differ at relative order $x_{c}$ (first coefficient $-\tfrac12$ on the (C1) slice, none for $\mu_{E}$), corrections that belong to the slice.
\item[(iv)] \emph{(The number.)} With the counted epoch at the modular period $8\pi M$, the area law $N\ln 2 = \SBH$ of Proposition \claimref{singularity.area-law-test} holds at leading order if and only if $\nu'\ln 2 = 1/(24\pi)$, equivalently $\kappa_{s}\ln 2 = 1/(16\pi)$, the registered density at $\lambda = 1$ (Prediction \claimref{pred.boundary-mode-density}).
\end{enumerate}

## technical
Inside the horizon locus of the Schwarzschild field on flat spacetime, measure time by $\tau$, the proper time left before the singularity; it is the unique radial function vanishing at the singularity with unit-speed gradient. Near the singularity the $t$-direction stretches as $\tau^{-1/3}$ and the spheres shrink as $\tau^{2/3}$, the Kasner exponents that the weighted blow-up forces, and since they sum to one the three-volume per unit Killing time of the slice at $\tau$ is $12\pi M\,\tau$ at leading order. Dividing by $\tau$ and letting $\tau \to 0$ gives a finite measure $\mu_E = 12\pi M$ per unit Killing time on the exceptional set itself, of the dimension of an area, with no free constant.

An eigenvalue threshold $\lambda$ is the proper-time slice $\tau_c = \tfrac23\lambda^{-1/2}$ at leading order, so under (C1) and (C2) the leading count is $\nu'\mu_E$ with $\nu' = \nu\tau_c = \tfrac23\kappa_s$, where $\kappa_s = \nu\lambda^{-1/2}$ is the one constant to which the two postulates reduce. At leading order, then, the slice can be dropped: counting $\nu'$ modes per Planck area of $\mu_E$ on the exceptional set gives the same count. The area law with the modular epoch fixes $\nu'\ln 2 = 1/(24\pi)$, that is $\kappa_s\ln 2 = 1/(16\pi)$.

## lay
The singularity paper places the black hole's quantum modes on a surface inside the hole where the strength of the gravitational field, its curvature, reaches the Planck value, and packs them at a fixed number per Planck-sized cell. For a large hole, and to leading order, those two assumptions only ever appear multiplied together. This result adds a geometric reason why the surface itself can be dropped. Near the singularity one direction of space stretches while two shrink, at rates whose exponents add up to one, so the volume of a slice near the singularity is proportional to the time left before reaching it. Dividing out that time gives a natural size for the singularity's own boundary, an area, with nothing left to choose. Counting a fixed number of modes per Planck area of that boundary gives the same leading count as the two assumptions together. That one number is not derived; matching the black hole entropy fixes it.

## one-liner
At leading order, and under (C1) and (C2), the count is $\nu'$ modes per Planck area of the measure $\mu_E = \lim V/\tau = 12\pi M$ per unit Killing time that the Kasner exponents (summing to one) put on the exceptional set, with $\nu' = \nu\tau_c = \tfrac23\kappa_s$; the slice can be dropped, and the area law fixes $\nu'\ln 2 = 1/24\pi$.
