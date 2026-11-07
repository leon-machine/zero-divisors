---
id: synthesis.positive-structure-is-twistor-form-at-imaginary-time
kind: claim
version: 5
title: 'The positive structure is the twistor form at imaginary time'
status: proved
region: synthesis
subject: one-relation
tags: [conformal-spinors, conformal-model, two-readings, modular-theory, witt-index]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, every imaginary unit resolved as a geometric-algebra pseudoscalar (unit principle)
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'consistency pass, a stale remark that a result is not yet in the store'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - synthesis.incidence-vacua-thermofield-real-capacity@6
  - one-relation.spacetime-manifold-vacuum-lines@6
  - correspondence.reality-conjugation-twistor-form-factor@8
  - correspondence.incidence-relation-chart@7
  - synthesis.twistor-form-states-only-off-the-real-slice@2
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_positive_structure_is_polarised_at_imaginary_time
- kind: check
  ref: check.py::check_sigma_is_the_twistor_form
- kind: check
  ref: check.py::check_tube_points_polarise_sigma
- kind: check
  ref: check.py::check_no_state_for_an_indefinite_form
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.twistor-form-states-only-off-the-real-slice
  - synthesis.boost-stationary-incidence-vacua-read-interval
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. The argued reading said synthesis.positive-null-energy-gives-r-premises is not yet in the store; it is now in the store, and the parenthesis names it without that remark; no change of content.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the complex unit of Cl(2,4)_C on the eight-dimensional Fock module, of the tube points m = x + iy and X(+-i e_1), of J = i e_1 e_+ and of the imaginary boost is written I_7 = I_6 e, the central pseudoscalar of Cl(3,4), which commutes with every vector (std-algebra.complexification-is-the-odd-extension, cited as a mention); the setting says I_7 acts on the module as its complex unit and that the result''s J is its own operator, not the conventions'' transverse bivector. One complex unit throughout, never identified with I_6. No bare i remains, so the outside_ga declaration (complex-analysis, for i only) is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the i of J = i e_1 e_+, of the points +-i e_1 and x + iy, and of the imaginary boost is the plain unit of Cl(2,4)_C and of the complexified chart, which must commute with the vectors; declared (version and levels unchanged).'
  maintainer_pass_2:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares where the proof uses them. Version 2 -> 3.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  open_problem: op.which-capacity
  note: >-
    The open problem says the answer turns on the Hermitian structure, positive or the invariant
    twistor form. This result shows the two are not rivals: the stored positive structure (every
    generator unitary) is the twistor form polarised by the incidence lines of the two conjugate
    imaginary points +-i e1 (imaginary time one in the units of the Witt pair), the positive
    structures compatible with the twistor form are exactly the polarisations at points of the
    forward tube, and only a positive structure carries states of the algebra at all. So the
    Hermitian structure question becomes the question of a point of the forward tube, and the
    stored syntheses under the positive structure are twistor-form statements read from the point
    i e1. Proved here: (i)-(v). Argued only (proof text, last paragraph): the reading for the
    capacities (the selected state, being a state, reads the twistor form through a tube point, a
    complex-capacity object, and its marginals at real points are the real-capacity thermofield
    doubles of the stored synthesis), and the reading of i e1 as the midpoint of the KMS half strip.
    The selected boundary-mode state is still not connected to the incidence chart, so the problem
    stays partial. Filed alongside: synthesis.positive-null-energy-gives-r-premises rests on the same half
    strip (clause (iii) of the twistor-form theorem) from the analytic side; the centre i e1 is the
    strip's midpoint and the positive time orientation here is the one of that claim's positive null energy
    (argued). Literature cited from memory, not used as a premise: the Krein-space notion of a
    fundamental decomposition, and the classical identification of the positive two-planes of
    twistor space with the forward tube (Penrose), here re-proved from the stored statements; the
    elementary positivity argument of (iv) is standard. Transport-convenient: the incidence lines
    and the Witt-pair normalisation are the series' own; (iv) is transport-absent linear algebra.
---

## formal
Let the eight-dimensional Fock module of $\Cl(2,4)$ of Theorem \claimref{synthesis.incidence-vacua-thermofield-real-capacity}, with ground generators $e_{1}$ ($e_{1}^{2} = 1$) and $e_{2}, e_{3}, e_{4}$ (squares $-1$) and ascent plane $e_{\pm}$ ($e_{\pm}^{2} = \pm 1$), carry that theorem's positive Hermitian structure $h$, for which every generator is unitary. Put $\nO = \tfrac12(e_{+} + e_{-})$, $\ninf = e_{+} - e_{-}$, $X(m) = \nO + m - \tfrac12 Q(m)\ninf$ for $m$ in the complexified span of $e_{1}, \dots, e_{4}$, whose complex unit is $I_{7} = I_{6}e$, the central pseudoscalar of $\Cl(2,4)_{\C} = \Cl(3,4)$ as in that theorem, which commutes with every vector and acts on the module as its complex unit (Theorem \claimref{std-algebra.complexification-is-the-odd-extension}; the symbol $J$ below is this result's own operator, not the transverse bivector of the conventions), and let $L(m) \subset \CS$ be the incidence line of $m$, the vacua of $X(m)$ in a chirality half (Proposition \claimref{one-relation.spacetime-manifold-vacuum-lines}). Put $J = I_{7}e_{1}e_{+}$ and $\Sigma(\psi, \varphi) = h(\psi, J\varphi)$.
\begin{enumerate}
\item[(i)] \emph{($\Sigma$ is the twistor form.)} The positive structure is unique up to a positive factor. $J^{2} = 1$, $J$ is $h$-Hermitian and even, and $\Sigma$ is Hermitian, $\Spin(2,4)$-invariant and of signature $(2,2)$ on each chirality half; on $\CS$ the $\Spin(2,4)$-invariant Hermitian forms are the real multiples of $\Sigma$. So $\Sigma$ is the twistor form of Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor} up to a nonzero real factor.
\item[(ii)] \emph{(The positive structure is $\Sigma$ polarised at $\pm I_{7}e_{1}$.)} $X(\pm I_{7}e_{1}) = e_{+}(1 \mp J)$. Hence $\CS = L(I_{7}e_{1}) \oplus L(-I_{7}e_{1})$, the two lines are $\Sigma$-orthogonal, and $h = \Sigma$ on $L(I_{7}e_{1})$, $h = -\Sigma$ on $L(-I_{7}e_{1})$: the positive structure is the twistor form polarised by the incidence lines of the conjugate imaginary points $\pm I_{7}e_{1}$, imaginary time one in the units of the Witt pair.
\item[(iii)] \emph{(The polarisations are the points of the forward tube.)} The $\Sigma$-adjoint of every real vector is minus itself, so $X(m)^{\sharp} = -X(\bar m)$ and $\Sigma(L(m), L(\bar m)) = 0$ for every complex point $m$. For $m = x + I_{7}y$ with $y$ timelike and $y^{1} > 0$, $L(m)$ is $\Sigma$-positive and $L(\bar m)$ is $\Sigma$-negative, so $h_{m} := \Sigma$ on $L(m)$, $-\Sigma$ on $L(\bar m)$, extended $\Sigma$-orthogonally, is a positive Hermitian form on $\CS$ with $h_{m}^{-1}\Sigma$ an involution. Conversely every positive Hermitian form $h'$ on $\CS$ for which $h'^{-1}\Sigma$ is an involution is $h_{m}$ for exactly one such $m$, with the time orientation for which the definite lines of Theorem \claimref{synthesis.twistor-form-states-only-off-the-real-slice}(ii) are positive along $+e_{1}$. The stored structure is $h = h_{I_{7}e_{1}}$.
\item[(iv)] \emph{(Only positive structures carry states.)} Let $s$ be a nondegenerate Hermitian form on a finite-dimensional complex space $V$ and $A \mapsto A^{\sharp}$ its adjoint on $\End(V)$. A linear functional $\omega$ on $\End(V)$ with $\omega(A^{\sharp}A) \ge 0$ for all $A$ and $\omega(1) = 1$ exists if and only if $s$ is definite. So neither $\End(\CS)$ nor the complexified Clifford algebra carries any state for the adjoint of $\Sigma$, and every state of either is a state for a positive Hermitian structure; no positive structure is preserved by a boost, since $(e_{1}e_{2})^{2} = 1$ gives $\exp(\tfrac{\theta}{2}e_{1}e_{2})$ the eigenvalues $e^{\pm\theta/2}$.
\item[(v)] \emph{(The centre is the midpoint of the positive half strip.)} Reading Theorem \claimref{synthesis.twistor-form-states-only-off-the-real-slice}(iii) at $\rho = 1$ with $e_{1}$ as time: along the imaginary boost $x(\theta) = \cos\theta\,e_{2} + I_{7}\sin\theta\,e_{1}$ of the real point $e_{2}$ the lines are $\Sigma$-positive for $0 < \theta < \pi$, and at $\theta = \pi/2$ the line is $L(I_{7}e_{1})$, the positive part of $h$; for the real point $\rho e_{2}$ the midpoint is $I_{7}\rho e_{1}$, the centre of $h$ exactly when $\rho = 1$.
\end{enumerate}

## technical
The open question was whether the selected state reads the positive Hermitian structure, under which every Clifford generator is unitary, or the conformally invariant twistor form, of signature (2,2). They turn out to be one structure. The positive structure equals the twistor form flipped in sign on one of two complementary planes, and those planes are the incidence lines of the complex points plus and minus the unit time vector times the complex unit. Every positive structure compatible with the twistor form arises in this way from exactly one complex point whose imaginary part is future timelike, a point of the forward tube (Penrose's classical identification of the positive two-planes of twistor space with the forward tube, re-proved here from the stored statements), and, by a standard Krein-space fact, an algebra whose adjoint comes from an indefinite form has no states at all. So a state must choose a point of the forward tube, and the stored positive structure is the choice of imaginary time one. That point is also the midpoint of the half strip on which an imaginary boost of the unit real point keeps the lines positive (the stored half-strip theorem at unit distance).

## lay
The framework had two candidate ways of measuring the size of quantum states at a point of spacetime: one that treats all directions alike but cannot give every state a positive size, and one that always gives positive sizes but picks out a direction of time and a unit of length. This result shows they are the same thing seen from two places. The positive one is the symmetric one viewed from a particular point of complexified spacetime, one unit along imaginary time, and every positive version of it comes from such a point. Since a quantum state needs positive sizes, a state has to choose such a point; the question of which measure the state uses becomes the question of which point it is viewed from.

## one-liner
The positive Hermitian structure $h$ (every generator unitary) is the twistor form $\Sigma = h(\cdot, I_{7}e_{1}e_{+}\cdot)$ polarised by the incidence lines of $\pm I_{7}e_{1}$; the positive structures compatible with $\Sigma$ are exactly its polarisations at points of the forward tube, and only positive structures carry states.
