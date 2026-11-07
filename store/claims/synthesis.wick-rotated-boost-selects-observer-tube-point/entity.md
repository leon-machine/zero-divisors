---
id: synthesis.wick-rotated-boost-selects-observer-tube-point
kind: claim
version: 2
title: 'The Wick-rotated boost selects the observer''s tube point'
status: proved
region: synthesis
subject: one-relation
tags: [conformal-spinors, conformal-model, two-readings, modular-theory, witt-index]
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
- name: Claude Opus 5.5
  role: notation pass, every imaginary unit resolved as a geometric-algebra pseudoscalar (unit principle)
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.positive-structure-is-twistor-form-at-imaginary-time@5
  - one-relation.spacetime-manifold-vacuum-lines@6
  - synthesis.twistor-form-states-only-off-the-real-slice@2
  - synthesis.incidence-vacua-thermofield-real-capacity@6
  - synthesis.boost-stationary-incidence-vacua-read-interval@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_wick_rotated_boost_unitary_exactly_over_the_bifurcation_plane
- kind: check
  ref: check.py::check_wick_rotation_is_antiperiodic_with_weights_one_half
- kind: check
  ref: check.py::check_quarter_turn_takes_tube_point_to_observer
- kind: check
  ref: check.py::check_observer_point_tracial_exactly_at_its_tube_point
- kind: check
  ref: check.py::check_ascent_pair_fixes_the_foot
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.positive-structure-is-twistor-form-at-imaginary-time
  - hawking.i-state
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the complex unit of the Wick rotation W_theta = exp(i theta K), of the tube points m = x_perp + i rho u, of h_{i e_1}, of the eigenvalues e^{+-i theta/2}, of the quarter turn, of J_m = i I_m and of the KMS continuation alpha_{i beta} of the boost automorphisms is written I_7 = I_6 e, the central pseudoscalar of Cl(3,4) = Cl(2,4)_C, which commutes with every vector (std-algebra.complexification-is-the-odd-extension, cited as a mention); the Wick rotation stays the complex continuation exp(I_7 theta K), not the real dual-plane rotation by I_4 K. The bivector I_m of the proof is a named unit bivector, not identified with I_7. No bare i remains, so the outside_ga declaration (complex-analysis, for i only) is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: W_theta = exp(i theta K) is the Wick rotation in Cl(2,4)_C, which maps the complex tube points to real ones; the dual-plane rotation exp(theta I_4 K) is a real rotation of span(e_3, e_4) and is a different operator, so i stays with the complex points; declared (version and levels unchanged).'
  open_problem: op.which-capacity
  note: >-
    Attack lines 2 and 3 of the open problem. The stored result reduced the Hermitian-structure
    question to the choice of a forward-tube point m (the positive structure h_m is the twistor
    form polarised at m). This result asks which tube points are compatible with a state that is KMS
    for the boost of one wedge, and answers it in three exact steps in the eight-dimensional module:
    (i) the Wick-rotated boost exp(i theta K) is h_m-unitary exactly when m = x_perp + i rho u lies over
    the bifurcation plane with imaginary part in the boost plane, which is also the fixed set of the
    wedge reflection m -> R(mbar); (iii) each such m is a quarter turn of the Wick-rotated boost from
    exactly one real point x(m) of the right wedge, rho the distance from the bifurcation plane and u
    the tangent of the boost orbit there, so stored h = h_{i e1} is the tube point of the unit observer
    e2; (iv) the ascent mode is boost invariant, so any boost-KMS functional gives it occupation 1/2,
    the ascent number operator is Hermitian for h_m exactly when the foot of m is the base point of
    the ascent pair, and among such tube points exactly m(x) makes every vacuum on the line of an
    observer x with that foot carry that occupation (the two thermofield doubles become Bell pairs of
    the ascent mode with the boost qubit); so the ascent pair fixes the foot and only the scale rho
    is left free. Proved: (i)-(iv). Argued only (proof text, reading): that the selected state
    (the I-state, KMS at the Hawking temperature) reads m(x) for its observer x; the capacity
    reading (complex capacity through the definite line L(m(x)), real capacity as one Bell pair at
    x); the scale rho = 1/kappa when the boost flow is normalised by the surface gravity; the
    weights +-1/2 of (ii) as the half-integer offset of (Q) in rapidity units; the ln 2 of the Bell
    pair as the KMS-forced trace of a zero-frequency mode. No common frame boost across planes is
    assumed. Modulo the boost the compatible set is an upper half space of pairs (x_perp, rho) on which
    dilations and transverse translations act transitively; the transverse translations move the
    ascent pair, so with the ascent pair given the foot is fixed and only rho stays free. Every
    capacity-type property is the same at every tube point (Spin(2,4) is transitive on the tube and
    commutes with the reality conjugation). Filed alongside, synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale
    gives the converse direction: with the boost, the positive structure at i rho e1 fixes the ray of
    the de Sitter tractor at Lambda = 12/rho^2, so the frozen point of positive Lambda, which lies in
    the ascent plane and commutes with K, singles out the point of the half space with foot zero and
    rho^2 = 12/Lambda (rho = 2/H in chart units); the argued rho = 1/kappa = 1/H agrees with it only
    when read with the local scale factor sigma = 2 there, a factor 2 in chart length. Literature cited
    from memory, not used as a premise: the Bisognano-Wichmann theorem (the wedge vacuum is KMS for
    the boost at rapidity period 2 pi, with modular conjugation the wedge reflection) and the
    Osterwalder-Schrader picture of the Euclidean rotation. Transport-convenient: the incidence
    lines, the ascent pair and the twistor-form polarisation are the series' own; (i) and (iii) are
    the finite-dimensional form of standard Euclidean geometry of the Rindler wedge.
---

## formal
Use the setting of Theorem \claimref{synthesis.positive-structure-is-twistor-form-at-imaginary-time}: the eight-dimensional Fock module of $\Cl(2,4)$ with ground generators $e_{1}$ ($e_{1}^{2} = 1$, the time direction) and $e_{2}, e_{3}, e_{4}$ (squares $-1$), ascent plane $e_{\pm}$, $\nO = \tfrac12(e_{+} + e_{-})$, $\ninf = e_{+} - e_{-}$, $X(m) = \nO + m - \tfrac12 Q(m)\ninf$, the incidence line $L(m)$ in a chirality half, the twistor form $\Sigma$, and for a forward-tube point $m$ the positive structure $h_{m}$, equal to $\Sigma$ on $L(m)$ and $-\Sigma$ on $L(\bar m)$, with $h_{I_{7}e_{1}} = h$; the complex unit is that theorem's $I_{7} = I_{6}e$, the central pseudoscalar of $\Cl(2,4)_{\C} = \Cl(3,4)$, which commutes with every vector (Theorem \claimref{std-algebra.complexification-is-the-odd-extension}). Let $K = \tfrac12 e_{1}e_{2}$ generate the boost $S_{\lambda} = \exp(\lambda K)$ of the $(e_{1}, e_{2})$ plane, which fixes $\nO$, $\ninf$ and the bifurcation plane $\operatorname{span}(e_{3}, e_{4})$, and let $W_{\theta} = \exp(I_{7}\theta K) = \cos\tfrac{\theta}{2} + I_{7}\sin\tfrac{\theta}{2}\,e_{1}e_{2}$ be its Wick rotation. Let $a = \nO$, $a^{*} = \tfrac12\ninf$, $N = a^{*}a$ be the ascent mode.
\begin{enumerate}
\item[(i)] \emph{(Wick-rotation compatibility.)} $W_{\theta}$ is $h_{m}$-unitary for every real $\theta$ if and only if $m = x_{\perp} + I_{7}\rho u$ with $x_{\perp} \in \operatorname{span}(e_{3}, e_{4})$, $\rho > 0$ and $u = \cosh\eta\,e_{1} + \sinh\eta\,e_{2}$ for some real $\eta$; equivalently, if and only if $m$ is fixed by the antiholomorphic wedge reflection $m \mapsto R(\bar m)$, where $R$ reverses $e_{1}$ and $e_{2}$ and fixes $e_{3}$, $e_{4}$. These compatible tube points form a four-dimensional family.
\item[(ii)] \emph{(Antiperiodicity.)} On each chirality half $e_{1}e_{2}$ has eigenvalues $+1$ and $-1$, each twice, so $W_{\theta}$ has eigenvalues $e^{\pm I_{7}\theta/2}$; $W_{2\pi} = -1$ and $W_{4\pi} = 1$.
\item[(iii)] \emph{(Quarter turn to the observer.)} For compatible $m = x_{\perp} + I_{7}\rho u$, $W_{\pi/2}X(m)W_{\pi/2}^{-1} = X(x(m))$ with $x(m) = x_{\perp} + \rho(\sinh\eta\,e_{1} + \cosh\eta\,e_{2})$, a real point of the right wedge. The map $m \mapsto x(m)$ is a bijection from the compatible tube points onto the right wedge $\{x_{\perp} + s : s \in \operatorname{span}(e_{1}, e_{2}),\ Q(s) < 0\}$ with positive $e_{2}$-component of $s$, commuting with the boosts $S_{\lambda}$, the dilations and the translations along the bifurcation plane. Its inverse sends a point $x$ of the wedge to $m(x) = x_{\perp} + I_{7}\rho(x)u(x)$, where $\rho(x)$ is the distance of $x$ from the bifurcation plane and $\rho(x)u(x)$ is the tangent at $x$ of the boost orbit through $x$. The stored structure $h = h_{I_{7}e_{1}}$ is the tube point of the unit observer $e_{2}$. Modulo the boosts the compatible family is the upper half space $\{(x_{\perp}, \rho) : \rho > 0\}$, on which the dilations and the translations along the bifurcation plane, all commuting with $K$, act transitively: the boost, its Wick rotation and the reflection single out a tube point only once an observer $x$, equivalently a scale $\rho$ and a foot $x_{\perp}$, is given; the translations do not fix the ascent pair, so (iv) fixes the foot.
\item[(iv)] \emph{(Single-atom compatibility with the boost-KMS state.)} For $c \in \operatorname{span}(e_{3}, e_{4})$ let $a_{c} = X(c)$, $a_{c}^{*} = \tfrac12\ninf$, $N_{c} = a_{c}^{*}a_{c}$ be the ascent mode based at the point $c$ of the bifurcation plane ($a_{0} = a$, $N_{0} = N$); $\{a_{c}, a_{c}^{*}\} = 1$. $a_{c}$ and $a_{c}^{*}$ are fixed by every boost $S_{\lambda}$, so any linear functional on the Clifford algebra satisfying the KMS condition for the boost automorphisms $\operatorname{Ad}S_{\lambda}$, at any inverse temperature, gives $\langle N_{c}\rangle = \tfrac12$. For a compatible $m$ with foot $x_{\perp}$, $N_{c}$ is $h_{m}$-Hermitian if and only if $x_{\perp} = c$. For such $m$ and a real point $x$ of the right wedge with foot $c$, every vacuum on $L(x)$ has $h_{m}$-occupation $\langle N_{c}\rangle = \tfrac12$ if and only if $m = m(x)$. Then the two vacua spanning $L(x)$, the translates of $\Omega$ and $\Psi$ of Theorem \claimref{synthesis.incidence-vacua-thermofield-real-capacity}, read with $h_{m(x)}$, are thermofield doubles at $\beta = 0$: the ascent mode is maximally entangled with the boost qubit. So for a given ascent pair the foot is fixed at its base point and the scale $\rho$ is the only datum left free.
\end{enumerate}

## technical
The previous result showed that a state on the conformal spinor module must choose a point of the forward tube, the choice fixing the positive Hermitian structure. Here the choice is tied to a wedge and its boost. The tube points whose positive structure makes the imaginary-rapidity (Wick-rotated) boost a unitary symmetry are exactly the complex points whose real part lies on the bifurcation plane and whose imaginary part is a future timelike vector of the boost plane; they are also the points fixed by the antiholomorphic wedge reflection, the geometric form of a modular conjugation. Each lies a quarter turn of the Wick-rotated boost from a single real point of the wedge: its imaginary part is the distance of that point from the bifurcation plane times the unit tangent of the boost orbit through it. The Wick-rotated boost has weights one half and changes sign at a full turn. Finally, an ascent mode based at a point of the bifurcation plane is invariant under the boost, so any state KMS for the boost gives it occupation one half. Its number operator is Hermitian for the positive structure only when the tube point stands over that base point, and for an observer standing over it, and only at the observer's own tube point, every vacuum of the incidence line has occupation one half, so the line is compatible with the boost-KMS state whichever vacuum is taken, and its thermofield doubles become maximally entangled pairs of the ascent mode with the boost qubit. So the ascent pair fixes the foot on the bifurcation plane; the scale, the distance from that plane, is the one datum the boost and KMS data leave free.

## lay
An earlier result showed that a quantum state at a point of this geometry has to pick a point of a complexified spacetime, and that this choice sets how sizes of states are measured. This result asks which point a state of the kind the series uses, thermal for the boost of one horizon wedge, would pick. The compatible points sit directly over the horizon's two-dimensional edge, displaced into imaginary time, and each corresponds to exactly one observer outside the horizon: rotating that observer a quarter turn in imaginary time lands on it, and how far into imaginary time it sits is the observer's distance from the horizon's edge. The mode in question is tied to one point of the edge. For an observer standing over that point, and only at that observer's own complex point, the description of the point as a line of possible vacuum states agrees in full with what thermality for the boost demands of the mode: it is exactly half filled, fully entangled with the boost's own qubit. So where along the edge is fixed; what remains free is how far from it.

## one-liner
The Wick-rotated boost $\exp(I_{7}\theta K)$ of a wedge is unitary for the positive structure $h_{m}$ exactly at the tube points $m = x_{\perp} + I_{7}\rho u$ over the bifurcation plane (the fixed points of the wedge reflection), each a quarter turn from the one real wedge point $x_{\perp} + \rho(\sinh\eta\,e_{1} + \cosh\eta\,e_{2})$; the boost-invariant ascent mode has occupation $\tfrac12$ in every boost-KMS state, and, for an observer whose foot is the ascent pair's base point, every vacuum on its incidence line has it exactly under its own tube point; the foot is fixed by the ascent pair and only the scale $\rho$ is left free by the boost data.
