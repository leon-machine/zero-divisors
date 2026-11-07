---
id: synthesis.c1-c2-forms-forced-one-number
kind: claim
version: 3
title: 'The forms of (C1) and (C2) are forced, up to one number'
status: proved
region: synthesis
subject: entropy
tags: [entropy-premises, mode-counting, schwarzschild, forcing-and-uniqueness]
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
  - interior.kasner-form-interior@7
  - sheaf.weights-are-forced-are-kasner-exponents@5
  - sheaf.kasner-data-interior@3
  - scrambling.slice-volume-exactly-per-unit-killing@5
  - singularity.imported-induced-geometry-interior-slice@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_frame_curvature_multiples
- kind: check
  ref: check.py::check_forced_weights_reproduce_curvature
- kind: check
  ref: check.py::check_count_one_number
- kind: check
  ref: check.py::check_slice_isometries_transitive
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.c1-curvature-cutoff
  - singularity.c2-cell-density
  - scrambling.scheme-robustness-cutoff
  - scrambling.uniqueness-internal-scaling
  - pred.boundary-mode-density
extraction:
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the one-liner now says at leading order in r_c/2M, as clauses (ii) and (iv) of the formal statement do. Version 1 -> 2.'
  open_problem: pr.c1-c2-placement
  note: 'Reduces the two placement postulates to two hypotheses of form (an algebraic, mass-independent curvature criterion; an isometry-invariant density) plus one number. The shape of (C1) and the form of (C2) are derived from those hypotheses; the threshold of (C1) and the density of (C2) are not separately identifiable at leading order, so the registered density prediction is a prediction for their combination. The curvature and volume computations are classical Schwarzschild geometry and transport-absent; the transport content is clause (ii), that the forced weights of the completion reproduce the interior curvature exactly, so the level sets are those of the weighted blow-up. Nothing here fixes the remaining number.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Schwarzschild field on flat spacetime; algebraic curvature scalars as rotation-gauge-invariant polynomials in the components of the curvature operator R(B); the six frame sectional curvatures named as the eigenvalues of R(B) on the frame planes in the store''s sign (checked against the stored spectrum (M/2r^3)(B + 3 sigma_r B sigma_r)); induced metric from the derived metric. Clauses (i)-(iv) unchanged; proof given a pointer.'
---

## formal
Place the boundary modes of the Schwarzschild gravitational field on flat spacetime of mass $M$ (Planck units; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) on an interior slice $r = r_c(M)$, $0 < r_c < 2M$, with some density per unit volume induced by the derived metric, and consider rules of the following two kinds: an \emph{algebraic mass-independent placement}, which sets an algebraic (pointwise) curvature scalar (a polynomial in the components of the curvature operator $\mathcal{R}(B)$ on the bivectors of an orthonormal physical frame, invariant under rotation-gauge transformations) to a fixed value in Planck units; and an \emph{invariant density}, a measure on the slice invariant under its isometries.
\begin{enumerate}
\item[(i)] \emph{(The shape of (C1).)} In the synchronous form of the interior (Proposition \claimref{interior.kasner-form-interior}), the curvature operator $\mathcal{R}(B)$ is diagonal on the six frame planes $(\tau t, \tau\theta, \tau\varphi, t\theta, t\varphi, \theta\varphi)$, and their sectional curvatures, its eigenvalues there in the store's sign, are exactly $(2, -1, -1, -1, -1, 2) \times M/r^{3}$. Hence every algebraic curvature scalar is a function of the Weyl eigenvalue $w = 2M/r^{3}$ alone (the Kretschmann scalar is $48M^{2}/r^{6} = 12\,w^{2}$), and every algebraic mass-independent placement selects a member of the one-parameter family
\[
w = \lambda, \qquad r_c^{3} = 2M/\lambda, \qquad \lambda > 0 .
\]
Postulate \claimref{singularity.c1-curvature-cutoff} is the member $\lambda = 1$; the Kretschmann criterion $48M^{2}/r^{6} = 1$ is $\lambda = 12^{-1/2}$.
\item[(ii)] \emph{(The family is the family of the forced weights.)} The forced weights of the completion, the Kasner exponents $(p_1, p_2, p_3) = (-\tfrac13, \tfrac23, \tfrac23)$ (Theorem \claimref{sheaf.weights-are-forced-are-kasner-exponents}, Fact \claimref{sheaf.kasner-data-interior}), give the six frame curvatures $p_i(p_i - 1)/\tau^{2}$ and $p_ip_j/\tau^{2}$, which are $(2, -1, -1, -1, -1, 2) \times 2/(9\tau^{2})$, and on the leading proper time $\tau = \tfrac23\,r^{3/2}(2M)^{-1/2}$ one has $4/(9\tau^{2}) = 2M/r^{3}$ exactly. So the family of (i) is, at leading order in $r/2M$, the family of proper-time level sets of the weighted blow-up, $w = \lambda \iff \tau = \tfrac23\lambda^{-1/2}$; the unit-proper-time criterion is $\lambda = 4/9$.
\item[(iii)] \emph{(The form of (C2).)} The slice $r = r_c$ carries the induced metric $|f(r_c)|\,dt^{2} + r_c^{2}\,d\Omega^{2}$ of the derived metric (Fact \claimref{singularity.imported-induced-geometry-interior-slice}), whose isometry group contains $\R \times SO(3)$ (Killing-time translations and rotations) acting transitively. An invariant density is therefore a constant multiple $\nu$ of the induced volume, uniqueness of the invariant measure on a homogeneous space being standard (Haar-Weil, cited from memory): the form of Postulate \claimref{singularity.c2-cell-density}, $\nu$ modes per Planck cell uniformly over the slice, is the only invariant one.
\item[(iv)] \emph{(Two numbers enter as one.)} On the family of (i), with density $\nu$, the three-volume per unit Killing time is exactly
\[
4\pi r_c^{2}\sqrt{2M/r_c - 1} \;=\; 8\pi M\,\lambda^{-1/2}\sqrt{1 - r_c/2M}, \qquad \frac{r_c}{2M} = \lambda^{-1/3}(2M)^{-2/3},
\]
so the accrual rate is
\[
\frac{dN}{dt} \;=\; 8\pi\,\kappa_s\,M\,\bigl(1 + O(M^{-2/3})\bigr), \qquad \kappa_s := \nu\,\lambda^{-1/2} .
\]
At leading order in $r_c/2M$ the count depends on the threshold $\lambda$ of (C1) and the density $\nu$ of (C2) only through $\kappa_s$; $\lambda$ is separately visible only at relative order $(2M)^{-2/3}$. Among power-law slices $r_c = cM^{\alpha}$ the leading volume per unit Killing time scales as $M^{(1 + 3\alpha)/2}$, linear in $M$ exactly at $\alpha = 1/3$, the exponent of the family of (i) (this extends the three-scheme comparison of Proposition \claimref{scrambling.uniqueness-internal-scaling} to every exponent).
\end{enumerate}
Consequently, under an algebraic mass-independent placement and an invariant density, the slice and the uniform density are forced, and what (C1) and (C2) add is two numbers, $\lambda$ and $\nu$, which the leading count sees only as $\kappa_s$; the area-law condition with the counted epoch at the modular period, which the store states for $\nu$ at $\lambda = 1$ (Prediction \claimref{pred.boundary-mode-density}), is a condition on $\kappa_s$, $\kappa_s = 1/(16\pi\ln 2)$ in the capacity convention. The value of $\kappa_s$ is not derived here. Filed alongside, synthesis.exceptional-boundary-measure-one-calibration: the same reduction read on the exceptional set, whose constant is $\nu' = \nu\tau_c = \tfrac23\kappa_s$ for an eigenvalue threshold; the two area-law values agree ($\kappa_s = 1/(16\pi\ln 2)$ exactly when $\nu' = 1/(24\pi\ln 2)$).

## technical
Suppose the rule that places the boundary modes is algebraic and mass-independent: it sets some algebraic (pointwise) curvature scalar to a fixed value in Planck units. Criteria built from derivatives of the curvature are not covered: they involve $M$ and $r$ separately and select other, mass-dependent slices. For the Schwarzschild field on flat spacetime, in the interior's synchronous frame the curvature operator $\mathcal{R}(B)$ is diagonal on the six frame planes, with sectional curvatures exactly $2, -1, -1, -1, -1, 2$ times $M/r^{3}$, so every such scalar is a function of the Weyl eigenvalue $w = 2M/r^{3}$, and the rule picks a slice $r_c^{3} = 2M/\lambda$ for some constant $\lambda$. Postulate (C1) is $\lambda = 1$, the Kretschmann criterion $\lambda = 12^{-1/2}$, the unit-proper-time criterion $\lambda = 4/9$. The forced weights of the completion, the Kasner exponents $(-1/3, 2/3, 2/3)$, reproduce the same six curvatures as $p_i(p_i - 1)/\tau^{2}$ and $p_ip_j/\tau^{2}$, with $4/(9\tau^{2}) = 2M/r^{3}$, so these slices are the proper-time level sets of the weighted blow-up.

If the mode density is invariant under the slice's isometries (Killing-time translations and rotations, which act transitively), it is a constant multiple $\nu$ of the induced volume: this is the form of (C2).

On the family the slice volume per unit Killing time is exactly $8\pi M\lambda^{-1/2}\sqrt{1 - r_c/2M}$, so $dN/dt = 8\pi\nu\lambda^{-1/2}M$ at leading order. The threshold and the density enter only through $\kappa_s = \nu\lambda^{-1/2}$; the threshold alone shows up only in the correction $r_c/2M = \lambda^{-1/3}(2M)^{-2/3}$, about $10^{-25}$ for a solar mass. Power-law slices $r_c = cM^{\alpha}$ give a count linear in $M$ only at $\alpha = 1/3$. So the two placement postulates reduce to two hypotheses of form, which force the slice family and the uniform density, plus one calibration constant $\kappa_s$; the registered density prediction, $1/(16\pi\ln 2)$ in the capacity convention, is a prediction for $\kappa_s$, equal to $\nu$ only at $\lambda = 1$. The same reduction read on the exceptional set is filed alongside (synthesis.exceptional-boundary-measure-one-calibration), with constant $\nu' = \tfrac23\kappa_s$.

## lay
The series counts the quantum degrees of freedom of a black hole on a surface deep inside it, using two assumptions: where the surface is (where the strength of the gravitational field, its curvature, reaches the Planck value) and how densely the degrees of freedom sit on it (a fixed number per Planck-sized cell). This result shows how much of that is choice. If the rule for the surface uses only the strength of curvature at each point, read off without derivatives, it must pick a surface of one specific family, because inside a black hole every measure of curvature is a function of one number; and the same family is singled out by the stretching pattern the series' completion forces near the singularity. If the density treats every point of the surface alike, it must be uniform. What is left are two numbers, the curvature threshold and the density, and the count only ever sees one combination of them. So the two assumptions together carry one adjustable constant, which the area law then has to fix; it is not derived here.

## one-liner
An algebraic (pointwise) curvature criterion at a mass-independent value forces the slice family $r_c^{3} = 2M/\lambda$ (every frame curvature of the interior is exactly a multiple of $M/r^{3}$, matching the forced Kasner weights) and an isometry-invariant density forces (C2)'s uniform form; what remains of (C1) and (C2) is the threshold and the density, which the count sees, at leading order in $r_c/2M$, only as $\nu\lambda^{-1/2}$.
