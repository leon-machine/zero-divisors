---
id: synthesis.kasner-curvature-wall-is-negative-weight-helicity
kind: claim
version: 1
title: 'The Kasner curvature wall is the negative-weight helicity'
status: proved
region: synthesis
subject: interior
tags: [kasner, curvature-and-field-equations, no-go]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
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
  - synthesis.nondiagonal-kasner-residue-weighted-shear@3
  - synthesis.bkl-bounces-no-framewise-invariant@2
  - synthesis.unit-boost-residue-needs-nonpositive-exponent@3
  - synthesis.imported-gtg-dictionary@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_frame_formula_and_helicities
- kind: check
  ref: check.py::check_support_identity
- kind: check
  ref: check.py::check_exponents_on_open_arc
- kind: check
  ref: check.py::check_bianchi_ii_vacuum_equations
- kind: check
  ref: check.py::check_liouville_bounce_is_bkl_law
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.nondiagonal-kasner-residue-weighted-shear
extraction:
  open_problem: op.forcing-half-beyond-diagonal
  note: >-
    Removes the subleading slice-curvature assumption of clause (iv) of
    synthesis.nondiagonal-kasner-residue-weighted-shear by computing exactly when it holds: the slices'
    scalar curvature, weighted by tau^2, is a sum of the squared helicities h_k^2 times tau^(4 p_k) and of
    weight-free terms times tau^(2 - 2 p_m), so on the open Kasner arc the only term that can grow is the
    helicity of the negative-weight covector. The curvature hypothesis of the forcing statement therefore holds exactly on the class in
    which that helicity vanishes fast enough (for a time-independent coframe: theta^1 ^ d theta^1 = 0), and
    fails (tau^2 times the Hamiltonian constraint diverges like tau^(4 p_1)) at every point where the
    limiting coframe has h_1 not zero; there, in the homogeneous model, the
    wall is the Bianchi II vacuum field, whose two limiting epochs are related exactly by the BKL transition
    law that synthesis.bkl-bounces-no-framewise-invariant takes as its model. Not new in substance: the
    dominant curvature wall of cosmological billiards is governed by the same structure coefficient
    (Damour, Henneaux and Nicolai 2003, cited from memory), the Bianchi II solution is Taub's (1951) and the
    Kasner map is the BKL one (cited from memory; both re-derived and checked here), and the ansatz (1.3) of
    Fournodavlos and Luk, Asymptotically Kasner-like singularities (arXiv:2003.13591), imposes
    omega_1 ^ d omega_1 = 0 on the covector of the smallest exponent (read from the arXiv text). What the
    entity adds to the store: the necessity of that condition for the residue-sense forcing half, in the
    store's setting, and the exact statement that its failure is a BKL bounce rather than a different
    residue. The orthonormal-frame curvature formula (Ellis and MacCallum form, cited from memory) is not
    used as a premise: the check confirms it against the coordinate Ricci scalar. The non-diagonal momentum
    constraints and the inhomogeneous bounce (whether generic data follow the BKL law) remain open.
    Complementary to the diagonal wall with a massless scalar (filed alongside,
    synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall): on the part of the scalar disk where
    every p_l is in (0,1) (nonempty: it contains (1/3,1/3,1/3)) every power in (i) decays and the helicity
    condition is vacuous; elsewhere in the disk a weight can be negative and the condition applies.
    Transport-absent: a statement about the field equations, bearing on the connection's residue.
---

## formal
Let a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) have derived metric $g = d\tau^{2} - \sum_{l}\tau^{2p_{l}}(\theta^{l})^{2}$ on $(0, \tau_{0})\times U$, as in \claimref{synthesis.nondiagonal-kasner-residue-weighted-shear}, with constant weights, $\sum_{l}p_{l} = 1$, and a coframe of the slices $\theta(\tau, x)$. Let $E_{l}$ be the frame vectors dual to $\theta^{l}$ at fixed $\tau$, with commutators $[E_{m}, E_{n}] = c_{mn}{}^{l}E_{l}$, and define the helicities $h_{k}$ by
\[
\theta^{k}\wedge d\theta^{k} \;=\; h_{k}\;\theta^{1}\wedge\theta^{2}\wedge\theta^{3}, \qquad h_{k} = -c_{ij}{}^{k} \quad ((i, j, k) \text{ cyclic}),
\]
so that $h_{k} = 0$ exactly when the commutator of the two other frame vectors has no $E_{k}$ component, the Frobenius condition for the plane field they span. Write $R^{(3)}$ for the scalar curvature of the slices' metric $\sum_{l}\tau^{2p_{l}}(\theta^{l})^{2}$, positive for the round sphere.
\begin{enumerate}
\item[(i)] \emph{(Exact, at every $\tau$.)}
\[
\tau^{2}R^{(3)} \;=\; -\tfrac12\sum_{k}h_{k}^{2}\,\tau^{4p_{k}} \;+\; \sum_{m}Q_{m}\,\tau^{2 - 2p_{m}},
\]
where each $Q_{m}(\tau, x)$ is a polynomial in the structure functions $c_{mn}{}^{l}$ of $\theta(\tau)$ and their first derivatives along the $E_{l}$, independent of the weights.
\item[(ii)] \emph{(The open Kasner arc.)} Let $p$ lie on the Kasner circle with $p_{1} < 0 < p_{2} \leq p_{3} < 1$ (every point of the circle other than the permutations of $(1, 0, 0)$, labelled so), and let $\theta(\tau)$ converge with its first two derivatives in $x$ as $\tau \to 0$. Then $\tau^{2}R^{(3)} = -\tfrac12 h_{1}^{2}\tau^{4p_{1}} + O(\tau^{\delta})$ with $\delta = \min(4p_{2}, 2 - 2p_{3}) > 0$. Hence $\tau^{2}R^{(3)} \to 0$ at $x$ if and only if $\tau^{2p_{1}}h_{1}(\tau, x) \to 0$; for a coframe independent of $\tau$, if and only if $\theta^{1}\wedge d\theta^{1} = 0$ at $x$. The helicities $h_{2}$, $h_{3}$ of the positive-weight covectors are unrestricted. Off the circle, on the part of the disk of a wall with a massless scalar ($\sum_{l}p_{l} = 1$, $\sum_{l}p_{l}^{2} < 1$) where every $p_{l}$ is in $(0, 1)$ (nonempty: it contains $(\tfrac13, \tfrac13, \tfrac13)$; elsewhere in the disk an exponent can be negative), every power in (i) is positive and $\tau^{2}R^{(3)} \to 0$ for every coframe converging in $C^{2}$: the helicity condition is vacuous there (filed alongside, synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall, which treats that diagonal scalar wall).
\item[(iii)] \emph{(The curvature hypothesis of the forcing statement.)} Suppose, in addition, that the coframe's shear meets the criterion of \claimref{synthesis.nondiagonal-kasner-residue-weighted-shear}(ii) with residue $P = \mathrm{diag}(p_{l})$ and $\tau\partial_{\tau}(\tau K) \to 0$. Then the $00$ component of the field equations $\mathcal{R}(a) = \Lambda a$ and the Hamiltonian constraint, at order $\tau^{-2}$ and for any $\Lambda$, hold if and only if $\tau^{2p_{1}}h_{1}(\tau, x) \to 0$. So the curvature hypothesis of \claimref{synthesis.nondiagonal-kasner-residue-weighted-shear}(iv) is equivalent, in this class, to that helicity condition, and at a point where the limiting coframe has $h_{1} \neq 0$ $\tau^{2}$ times the Hamiltonian constraint diverges like $\tau^{4p_{1}}$: no gravitational field obeying the field equations has a Kasner-like approach with these weights and this coframe there. The momentum constraints and the spatial components are not analysed; they can only add conditions.
\item[(iv)] \emph{(The active wall, homogeneous model.)} Let the derived metric be $N^{2}dT^{2} - \sum_{l}a_{l}(T)^{2}(\theta^{l})^{2}$ with $d\theta^{1} = \theta^{2}\wedge\theta^{3}$, $d\theta^{2} = d\theta^{3} = 0$ (Bianchi II, $h_{1} = 1$), $N = a_{1}a_{2}a_{3}$ and $\alpha_{l} = \log a_{l}$. The vacuum condition $\mathcal{R}(a) = 0$ holds if and only if $2\alpha_{1}'' = -a_{1}^{4}$, $2\alpha_{2}'' = 2\alpha_{3}'' = a_{1}^{4}$ and $4(\alpha_{1}'\alpha_{2}' + \alpha_{2}'\alpha_{3}' + \alpha_{3}'\alpha_{1}') = a_{1}^{4}$. Every solution is $\alpha_{1} = \tfrac12\log(2v) - \tfrac12\log\cosh(2v(T - T_{0}))$, $\alpha_{2}' = -\alpha_{1}' + B$, $\alpha_{3}' = -\alpha_{1}' + C$ with $v > 0$ and $BC = v^{2}$. Orient $T$ so that the volume grows; then as $T \to +\infty$ and $T \to -\infty$ the field tends to Kasner epochs $p$ and $p'$ (weights the normalised velocities), the later one has $p_{1} < 0$, the earlier one, towards the singularity, is
\[
p' \;=\; \Bigl(\frac{-p_{1}}{1 + 2p_{1}},\ \frac{p_{2} + 2p_{1}}{1 + 2p_{1}},\ \frac{p_{3} + 2p_{1}}{1 + 2p_{1}}\Bigr),
\]
the BKL transition law of \claimref{synthesis.bkl-bounces-no-framewise-invariant} ($u \mapsto u - 1$, or $u \mapsto 1/(u - 1)$ at the end of an era), and in $p'$ the nonpositive weight sits on a helicity-free axis, so by (ii) the earlier epoch's slice curvature is subleading.
\end{enumerate}
So, for Kasner-arc weights, the assumption of the non-diagonal residue-sense forcing statement is replaced by a condition on the coframe alone: the negative-weight covector must lose its helicity in the limit (at the rate of (ii)). This is necessary for any such approach; that solutions exist under it is not claimed here. Where that helicity does not vanish the wall is a curvature wall which, in the homogeneous model, reflects the weights by the BKL law instead of supplying a residue.

## technical
The stored non-diagonal forcing statement puts the residue of the rotation-gauge field's pole on the Kasner circle under an assumption it does not derive: that the slices' scalar curvature, times $\tau^{2}$, tends to zero. This result computes when that holds. Exactly, at each time, the weighted curvature splits into squared helicities $h_{k}^{2}$ of the coframe covectors, each multiplied by $\tau^{4p_{k}}$, and terms with the weight-free coefficients multiplied by $\tau^{2 - 2p_{m}}$; the helicity $h_{k}$ is the trivector $\theta^{k}\wedge d\theta^{k}$, which vanishes exactly when the two other frame vectors span an integrable plane field. On the Kasner circle away from the Taub points exactly one weight is negative, so the only term that can grow is the helicity of the negative-weight covector, as $\tau^{4p_{1}}$. With the residue on the circle the Hamiltonian constraint at leading order says that this weighted curvature must tend to zero, so the assumption is equivalent to the vanishing of that one helicity at a sufficient rate, a necessary condition that generic coframes violate; the remaining field equations (momentum constraints, spatial components) are not analysed and can only add conditions, and existence of solutions is not claimed. Where it fails, the homogeneous model is the Bianchi II gravitational field: its exact vacuum solution passes from one Kasner epoch to another, and the map between them, computed here, is exactly the BKL transition law that the store's bounce results take as their model. The ingredients are standard: the structure coefficient is the dominant curvature wall of cosmological billiards (Damour, Henneaux and Nicolai 2003), the Bianchi II solution is Taub's and the map is that of Belinski, Khalatnikov and Lifshitz (all cited from memory, all re-derived and checked here), and the Kasner-like vacuum solutions of Fournodavlos and Luk (2020) are built on an ansatz that imposes exactly the vanishing helicity of the smallest-exponent covector. What the result adds is that this condition is necessary for the forcing half, and that its failure produces a bounce, not a different residue.

## lay
Near a singularity of the Kasner kind, space stretches in two directions and is squeezed in the third. The series had shown that Einstein's equations supply the data its completion needs at such a wall, provided the curvature of space itself stays small compared with the stretching. This result says exactly when that proviso holds. Space can be twisted around each direction, and only the twist around the squeezed direction matters: if it is absent the proviso holds and the series' statement goes through; if it is present, it grows without bound, and in the simplest model the singularity then bounces into a new Kasner regime by the rule that drives the well-known chaotic approach to generic singularities.

## one-liner
For Kasner-like weights on the open circle, exactly $\tau^{2}R^{(3)} = -\tfrac12\sum_{k}h_{k}^{2}\tau^{4p_{k}} + \sum_{m}Q_{m}\tau^{2 - 2p_{m}}$ with $h_{k}$ the helicity $\theta^{k}\wedge d\theta^{k}$ of the coframe, so the curvature assumption of the non-diagonal forcing statement holds iff $\tau^{2p_{1}}h_{1} \to 0$ (for a time-independent coframe, iff $\theta^{1}\wedge d\theta^{1} = 0$; a necessary condition for any such approach), and where it does not the homogeneous wall is Bianchi II, whose bounce is exactly the BKL transition law.
