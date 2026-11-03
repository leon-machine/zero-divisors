---
id: synthesis.twistor-form-states-only-off-the-real-slice
kind: claim
version: 1
title: Under the invariant twistor form, incidence lines of real points carry no states, and the lines along an imaginary boost are definite on each half strip, of opposite signs
status: proved
region: synthesis
subject: one-relation
tags: [conformal-spinors, conformal-model, two-readings, modular-theory, witt-index]
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
derivations:
- name: main
  uses:
  - correspondence.reality-conjugation-twistor-form-factor@6
  - correspondence.incidence-relation-chart@4
  - synthesis.incidence-vacua-thermofield-real-capacity@5
  - one-relation.two-capacities-three-consequences@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_restricted_form_is_imaginary_part
- kind: check
  ref: check.py::check_store_sigma_and_real_lines
- kind: check
  ref: check.py::check_imaginary_boost_half_strip
- kind: proof
  derivation: main
extraction:
  open_problem: op.which-capacity
  flow_note: phase; the imaginary boost of clause (iii) is the phase flow's geometric continuation, the rotor at imaginary rapidity (see synthesis.phase-flow-is-time-rotor-flow-kms-continuation).
  note: >-
    Carries out the redo of op.which-capacity with the store's own (2,2) reality conjugation in place
    of the positive Hermitian structure used by synthesis.incidence-vacua-thermofield-real-capacity,
    which is not Spin(2,4)-invariant (its clause (iv)). Under the invariant twistor form the incidence
    line of a real point is Sigma-null, a maximal isotropic plane of a form of Witt index two, and
    carries no positive state; positivity needs a complex point with timelike imaginary part. The
    content of (ii) is classical twistor theory (Penrose: lines of the positive or negative half of
    twistor space correspond to the forward or backward tube), cited from memory and re-proved here
    from the stored statements; it is transport-absent. What is new for the problem is the reading:
    the two Hermitian structures split the question. With the positive structure thermal content sits
    on real points and real planes (the stored synthesis); with the invariant structure real points
    are pure geometry (null lines) and states live on the complex continuation, exactly on the half
    strips of an imaginary boost, one positive and one negative, each half the rapidity period 2 pi;
    for the stored kappa and the continuation whose imaginary part points along +e0 = a2 the positive
    one is 0 < theta < pi (computed on the stored construction; reversing kappa or the time orientation
    exchanges them). ARGUED, not proved: this matches the geometric form of the KMS strip (the
    Bisognano-Wichmann picture), and it suggests that the
    selected state reads the complex capacity through the continuation while the incidence structure
    of real spacetime is a real-capacity (isotropic) statement for Sigma. The selected boundary-mode
    state is still not connected to these lines (a direct identification of the completion's pair
    with the chart's ascent pair fails: the completion's pair is (k, nO/(2 nu)) with k the dying
    direction, not ninf). Filed alongside, synthesis.boost-stationary-incidence-vacua-read-interval,
    which answers the same question under the positive Hermitian structure; the two do not conflict,
    and the present result shows that the only structure under which the boost is a symmetry gives no
    states on real points.
---

## formal
Let $\Sigma$ be the twistor form of Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor}, built from $\kappa = \Gamma c(b_{4})J$ with the phase fixed there, on $\CS = \Som\oplus\Spi$: Hermitian of signature $(2,2)$, with $\Som$ and $\Spi$ $\Sigma$-null and $\sigma: \Som\times\Spi \to \C$ its perfect pairing. Let $i$ be the complex unit of the Fock model and $e_{0}, \dots, e_{3}$ the orthonormal basis of the Minkowski complement of the Witt pair used there ($e_{0}$ timelike). For a point $m = x + iy$ of the complexified affine chart of Theorem \claimref{correspondence.incidence-relation-chart}, with $x, y$ real, let $\hat x$, $\hat y$ be the $\sigma$-Hermitian maps with $m(i\hat x) = x$, $m(i\hat y) = y$ (clause (5) of the Proposition), so that $m = m(A)$ with $A = i\hat x - \hat y$, and let $L = \{A\pi + \pi : \pi \in \Spi\}$ be its incidence line. Then:
\begin{enumerate}
\item[(i)] $\Sigma(A\pi + \pi, A\pi' + \pi') = -2\,\sigma(\hat y\pi, \pi')$ for all $\pi, \pi' \in \Spi$: the form $\Sigma$ restricted to the incidence line depends only on the imaginary part $y$, and its determinant in any basis of $L$ has the sign of $Q(y)$;
\item[(ii)] hence $L$ is $\Sigma$-null exactly when $y = 0$ (a real point), $\Sigma$-definite exactly when $Q(y) > 0$, of signature $(1,1)$ when $Q(y) < 0$, and of rank one when $y$ is null and nonzero; for the stored $\kappa$ the definite lines are positive exactly when $y$ has positive $e_{0}$-component, so the lines on which $\Sigma$ defines a state space are those of the complex points with imaginary part timelike and pointing along $+e_{0}$;
\item[(iii)] for the real point $x_{0} = \rho e_{1}$, $\rho > 0$, the boost of the $(e_{0}, e_{1})$ plane with imaginary rapidity $i\theta$ gives $x(\theta) = \rho\cos\theta\,e_{1} + i\rho\sin\theta\,e_{0}$; its line is $\Sigma$-definite of one sign for $0 < \theta < \pi$, of the opposite sign for $\pi < \theta < 2\pi$, and $\Sigma$-null at $\theta = 0$ and $\theta = \pi$, where $x(\pi) = -x_{0}$ is the reflected real point; the orbit has period $2\pi$.
\end{enumerate}
So under the $\mathrm{Spin}(2,4)$-invariant form the incidence lines of real points, maximal isotropic for a form of Witt index two, carry no positive state, and positivity is attained only off the real slice: along an imaginary boost, on exactly one of the half strips $0 < \theta < \pi$ and $\pi < \theta < 2\pi$, which one being fixed by the sign of $\kappa$ and the orientation of the continuation; for the stored $\kappa$ and imaginary part along $+e_{0}$ it is the first.

## technical
The positive Hermitian structure under which the incidence vacua were found to be thermofield doubles is not invariant under the conformal group. The store also has an invariant structure, the twistor form $\Sigma$ of signature $(2,2)$, under which the lines of real points are exactly the $\Sigma$-null lines. Restricting $\Sigma$ to the line of a complex point $x + iy$ gives $-2$ times the Hermitian form of the imaginary part $y$, whose determinant has the sign of $Q(y)$: null for real points, definite for timelike $y$, split for spacelike $y$, degenerate for null $y$. This is the classical correspondence between the halves of twistor space and the forward and backward tubes. Computed on the stored construction itself, the definite lines are positive when $y$ points along $+e_{0}$.

Along an imaginary boost of a point of the right wedge, $x(\theta) = \rho\cos\theta\,e_{1} + i\rho\sin\theta\,e_{0}$, the line is definite of opposite signs on the two half strips and null at $0$ and $\pi$, where the point is real again and reflected; for the stored $\kappa$ the restricted form is $2\rho\sin\theta$ times a fixed positive form, positive on $0 < \theta < \pi$. So with the invariant structure, real spacetime is pure geometry, a family of null lines saturating the form's isotropic dimension, and states exist only on the complex continuation, on one half strip of the rapidity period $2\pi$.

## lay
Earlier work found that, at each point of spacetime, the series' quantum vacua include thermal states, but it used a way of measuring states that does not respect the symmetries of spacetime. This result redoes the analysis with the measure that does respect them. Then every real point of spacetime corresponds to a family of vacua of zero norm, pure geometry with no states on it; genuine states appear only when the point is continued into complex values. Along that continuation the states exist for exactly half of one full turn. A suggested reading, not proved here, is that this half-turn matches the half period that appears in the imaginary-time treatment of Hawking's temperature.

## one-liner
Under the conformally invariant twistor form the incidence line of a point $x + iy$ carries $-2$ times the Hermitian form of $y$, so lines of real points are null and carry no states, definiteness needs timelike $y$, and along an imaginary boost the lines are definite of opposite signs on the two half strips, positive on $0 < \theta < \pi$ for the stored conjugation with imaginary part along $+e_{0}$.
