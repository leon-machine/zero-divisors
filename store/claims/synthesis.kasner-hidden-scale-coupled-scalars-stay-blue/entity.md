---
id: synthesis.kasner-hidden-scale-coupled-scalars-stay-blue
kind: claim
version: 4
title: 'Scalars coupled to the hidden scale stay blue on a Kasner approach'
status: proved
region: synthesis
subject: dark-energy
tags: [kasner, no-go, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-five-fronts
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'GA rewrite (scalar kinetic term in GTG)'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - synthesis.kasner-approach-gives-horizon-exit-and-index-three@4
  - interior.kasner-form-interior@6
  - synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands@1
  - dark-tower-matter.five-dimensional-content@5
  - dark-tower-matter.five-dimensional-towers@4
  - synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue@3
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise@4
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.imported-bessel-reduction-and-small-argument-hankel-forms@2
  - synthesis.imported-kaluza-klein-ansatz@1
  - synthesis.imported-planck-2018-isocurvature-and-isotropy-bounds@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_reduction_weights
- kind: check
  ref: check.py::check_bessel_order
- kind: check
  ref: check.py::check_normalisation_and_index
- kind: check
  ref: check.py::check_equal_observed_exponents
- kind: check
  ref: check.py::check_every_point_has_a_blue_axis
- kind: check
  ref: check.py::check_stored_fields_blue
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.dating-descent
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The spectator scalar''s kinetic term is written -Q(hb^T(nabla phi))/2 with the volume factor sqrt|g_4| = det(hb_4)^{-1}, and the proof''s inverse-metric weight g^{tau tau} g^{jj} as Q(g^tau) Q(g^j) for the physical coframe g^mu = hb^T(e^mu) (the same scalars for a diagonal field), the components kept as labelled readings; F_{mu y} F^{mu y} stays (field-strength components, which the conventions allow); notation only.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R4 (scalar mode functions and Hankel Wronskians are written with the field theory''s unit, one reading with synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching and the other scalar-mode entities): the modes e^{I_4 k x^i}, the canonical normalisation tau^alpha(phi phi-dot* - phi* phi-dot) = I_4, the Hankel Wronskian -4 I_4/(pi s) and the product -4 I_4 q |N|^2/pi are written with I_4 (proof), numbers read in span{1, I_4}, exact since that span is the complex numbers; no bare i remains, so the declaration is removed.'
  open_problem: op.descent-state-and-spectrum
  note: >-
    Closes the scalar part of what the stored Kasner result lists as not covered: fields coupled to the
    size of the hidden direction. A scalar whose four-dimensional action carries b^lambda has Bessel order
    |lambda - 1||p_h|/(2(1 - p_i)) along a principal axis. For |lambda - 1| <= 2 no Kasner point, vacuum
    or stiff, isotropic or not, gives an index below 1 on all three observed axes, because that would need
    p_h > 1 or p_h < -1/2, outside the range of a single exponent; so these fields cannot be red in every
    direction, with no appeal to the isotropy of the record. With the observed exponents equal (vacuum: the
    two points (0,0,0;1) and (1/2,1/2,1/2;-1/2); the five-dimensional stiff segment between them) the order
    is at most |lambda - 1|/2 on every axis. The stored five-dimensional content (the towers' u(3) gauge
    field, their Dirac species, the hidden direction's diagonal field) and our four-dimensional fields give
    scalars with lambda = -1 (the Wilson-line component A_y) and 0 (fields confined to the observed
    directions, the Higgs among them); lambda = 1 is the generic bulk scalar zero mode (the store holds no
    five-dimensional scalar field). The Wilson-line scalar is the reddest, index exactly 1 at both vacuum
    points. The towers' u(3) vector zero modes (weight b on a vector) have order p/(1 - p) <= 1 on the
    segment, so their potentials have index at least 1 and their field strengths are bluer still. A red index
    within an epoch would need |lambda - 1| > 3, which nothing stored supplies, and even then the measured
    value would be a choice of the point on the segment. The interior of the segment is reached by
    five-dimensional stiff matter, the analogue of the stored four-dimensional stiff-matter theorem; the
    store holds no five-dimensional stiff source, so the vacuum ends are the only points the store itself
    reaches. The radion's own perturbation is the curvature perturbation of the Einstein-frame stiff
    contraction and has order 0 (argued, from memory: the pre-big-bang curvature spectrum). The metric's
    off-diagonal modes, the Kaluza-Klein vector (whose field strength is blue) and curvature couplings,
    of which only a fitted curvature coupling reaches the measured tilt, are treated in a result filed
    alongside, synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling; the conversion of
    these spectra into the curvature perturbation cannot lower the index for a local function of a Gaussian
    field, synthesis.local-conversion-cannot-redden-a-gaussian-spectator. The Dirac species
    are fermions, covered by the shot-noise bound. Transport-absent: standard mode analysis; the reduction
    weights are read in the Clifford algebra Cl(1,4). Imported as Facts: the Bessel reduction of
    y'' + ((1 - 2a)/x) y' + c^2 x^(2c - 2) y = 0 to order a/c and the small-argument form of the Hankel
    functions (synthesis.imported-bessel-reduction-and-small-argument-hankel-forms), the Kaluza-Klein ansatz
    (synthesis.imported-kaluza-klein-ansatz), and the record's statistical isotropy
    (synthesis.imported-planck-2018-isocurvature-and-isotropy-bounds). Cited from memory, a flagged citation
    (no five-dimensional stiff source is adopted): the five-dimensional stiff Kasner relations.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the Bessel reduction and small-argument Hankel forms, the Kaluza-Klein ansatz and the statistical isotropy of the record, cited from memory in version 1, now cite the imported Facts (uses edges added, claimrefs in the proof); the Planck parameters pin moved to version 2 (baryon and dark matter densities added there, not used here); the five-dimensional stiff Kasner relations stay a flagged citation; the pin to synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise moved to its version 2 (a pointer note added there). No clause changed.'
---

## formal
Let a gravitational field on flat spacetime have, near a wall at $\tau = 0$, the synchronous diagonal derived metric $d\tau^{2} - \sum_{j=1}^{3}\tau^{2p_{j}}(dx^{j})^{2} - \tau^{2p_{h}}dy^{2}$, with three observed directions and the hidden direction $y$ of Proposition \claimref{synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands}, scale $b = \tau^{p_{h}}$, and $p_{1} + p_{2} + p_{3} + p_{h} = 1$, $p_{1}^{2} + p_{2}^{2} + p_{3}^{2} + p_{h}^{2} \le 1$: the five-dimensional vacuum points (equality) and the points that five-dimensional stiff matter reaches (strict inequality; the analogue of Theorem \claimref{synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue} in five dimensions, standard and not in the store, which holds no five-dimensional stiff source). Let $\phi$ be a massless spectator scalar, constant along $y$, with four-dimensional action $\int d\tau\,d^{3}x\,\sqrt{|g_{4}|}\,b^{\lambda}\,(-\tfrac12 Q(\hb^{T}(\nabla\phi)))$, $g_{4}$ the derived metric on the observed directions and $\sqrt{|g_{4}|} = \det(\hb_{4})^{-1}$ its volume factor (in components $Q(\hb^{T}(\nabla\phi)) = g^{\mu\nu}\partial_{\mu}\phi\,\partial_{\nu}\phi$), and let $k$ lie along the principal axis $i$, $q = 1 - p_{i} > 0$, $s = k\tau^{q}/q$.
\begin{enumerate}
\item[(i)] \emph{(Order.)} The mode equation is $\ddot\phi + \alpha\dot\phi/\tau + k^{2}\tau^{-2p_{i}}\phi = 0$ with $\alpha = 1 + (\lambda - 1)p_{h}$; with $\phi = \tau^{(1-\alpha)/2}Z(s)$, $Z$ obeys Bessel's equation of order $\nu_{i} = |\lambda - 1|\,|p_{h}|/(2q)$. The order is $0$, the case of Theorem \claimref{synthesis.kasner-approach-gives-horizon-exit-and-index-three}, exactly when $(\lambda - 1)p_{h} = 0$.
\item[(ii)] \emph{(Spectrum within an epoch.)} The adiabatic normalisation of $\phi = N\tau^{(1-\alpha)/2}H^{(1)}_{\nu}(s)$ has $|N|^{2} = \pi/(4q)$, free of $k$, and for $\nu_{i} > 0$ the exited spectrum along the axis $i$ has index $n - 1 = 3 - 2\nu_{i}$.
\item[(iii)] \emph{(Some axis is blue.)} A single exponent of the ball lies in $[-\tfrac12, 1]$. If $|\lambda - 1| \le 2$ then $\nu_{i} \le |p_{h}|/(1 - p_{i})$, and $\nu_{i} > 1$ on all three observed axes would give $3|p_{h}| > 2 + p_{h}$, that is $p_{h} > 1$ or $p_{h} < -\tfrac12$. So at every point of the ball at least one observed axis that the modes leave has $\nu_{i} \le 1$ and index at least $1$.
\item[(iv)] \emph{(Equal observed exponents.)} With $p_{1} = p_{2} = p_{3} = p$ and $p_{h} = 1 - 3p$, the vacuum points are $p = 0$ and $p = \tfrac12$ only, the ball gives $0 \le p \le \tfrac12$, and there $|1 - 3p|/(1 - p) \le 1$, with equality only at the two vacuum points and zero at the static point $p = \tfrac13$. So $\nu \le |\lambda - 1|/2$ and $n - 1 \ge 3 - |\lambda - 1|$ on every axis. With unequal observed exponents and $(\lambda - 1)p_{h} \ne 0$ the order differs between axes.
\item[(v)] \emph{(The stored fields.)} In $\Cl(1,4)$ with frame $\tau^{p_{j}}e_{j}$, $\sqrt{|g_{5}|} = \sqrt{|g_{4}|}\,b$ and $Q(f_{y}) = -b^{2}$, so the component $A_{y}$ of the five-dimensional gauge field of Propositions \claimref{dark-tower-matter.five-dimensional-towers} and \claimref{dark-tower-matter.five-dimensional-content} has $\lambda = -1$, a field confined to the observed directions has $\lambda = 0$, and the zero mode of a massless five-dimensional scalar, a generic entry since the store holds no such field, has $\lambda = 1$. For these $|\lambda - 1| \le 2$, so (iii) holds at every point and, with equal observed exponents, $\nu \le 1$ and $n - 1 \ge 1$ on every axis: blue by at least $1.0351$, more than $246$ standard deviations from the measured $n_{s} - 1 = -0.0351 \pm 0.0042$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}). At both vacuum points $(\nu, n - 1)$ is $(1, 1)$ for $A_{y}$, $(\tfrac12, 2)$ for a confined field and $(0, \text{between } 2 \text{ and } 3)$ for a bulk zero mode. The towers' gauge vector zero modes, transverse components with weight $b$, have order $p/(1 - p) \le 1$ on the equal-exponent points, so the index of their potentials is at least $1$. A red index within an epoch needs $|\lambda - 1| > 3$, and then the index runs over $[3 - |\lambda - 1|, 3]$ along the segment, so the measured value would be a choice of $p$.
\end{enumerate}
Not covered: the metric's off-diagonal modes, curvature couplings off the vacuum points, the conversion of a spectator spectrum into the curvature perturbation, and couplings to fields the store does not hold (a dilaton with its own rate).

## technical
The stored Kasner result shows that a scalar feeling only the geometry gets a blue spectrum near a wall, because the volume grows exactly as proper time. Fields that also feel the size of a hidden direction, the case it leaves open, have a different friction term: if the four-dimensional action carries the hidden scale to the power $\lambda$, the mode equation is Bessel's of order $|\lambda - 1||p_{h}|/(2(1 - p_{i}))$ and the index is 3 minus twice that. Because a single Kasner exponent never leaves $[-\tfrac12, 1]$, a field with $|\lambda - 1| \le 2$ cannot have an index below 1 along all three observed axes at any Kasner point; and when the three observed exponents are equal (the two vacuum points, and the five-dimensional stiff segment between them, which no stored source reaches) every axis has index at least $3 - |\lambda - 1|$. Reducing the stored five-dimensional content in the Clifford algebra gives $\lambda = -1$ (the gauge field's component along the hidden direction) and $0$ (fields of our observed directions, such as the Higgs), with $\lambda = 1$ for a generic bulk scalar; the towers' gauge vectors are blue too. So no scalar the series supplies is red on a Kasner approach in every direction, and with isotropic observed exponents every one has index at least 1. A red tilt from this source would need a coupling with $|\lambda - 1|$ above 3 that nothing stored provides, and even then it would be a fit of the point on the segment.

## lay
In standard cosmology the slightly uneven ripples of the early universe come from a stage of rapid expansion. This framework lacks that stage, and earlier work found that the one place its geometry stretches ripples beyond the horizon, the violent squeezing near a singularity, gives far too much small-scale ripple for the simplest fields. This result checks the fields that also feel the size of a hidden extra direction, which could in principle behave differently. For every such field the framework contains, at least one visible direction always ends up with ripples strongly tilted toward small scales, so the ripples cannot have the measured tilt in every direction; and when the squeezing is the same in all visible directions, every direction is tilted the wrong way. So this route does not supply the measured ripples either.

## one-liner
On a Kasner approach with hidden scale $b = \tau^{p_{h}}$ and $\sum p = 1$, a scalar with action weight $b^{\lambda}$ has Bessel order $|\lambda - 1||p_{h}|/(2(1 - p_{i}))$ and index $3 - 2\nu$; for $|\lambda - 1| \le 2$ some observed axis has index at least $1$ at every point, and with equal observed exponents every axis does; the stored fields have $\lambda \in \{0, -1\}$ (and $1$ for a generic bulk scalar), the Wilson-line scalar $A_{y}$ at exactly $1$: no red tilt.
