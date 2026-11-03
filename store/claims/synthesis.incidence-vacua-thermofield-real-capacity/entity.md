---
id: synthesis.incidence-vacua-thermofield-real-capacity
kind: claim
version: 5
title: No incidence vacuum is real; each incidence line is spanned by two thermofield doubles of the ascent mode with the boost qubit
status: proved
region: synthesis
subject: one-relation
tags:
- witt-index
- conformal-model
- entanglement
- two-readings
proposed_by:
  kind: ai
  session: colony-2026-10-22
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
  - one-relation.two-capacities-three-consequences@5
  - tower.witt-index-quantum-capacity@4
  - one-relation.imported-pure-spinors-incidence-chart@5
  - one-relation.spacetime-manifold-vacuum-lines@6
  - singularity.descended-form-state-independent@4
  - state-selection.partner-purification-are-canonical@4
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_real_states_read_real_capacity
- kind: check
  ref: check.py::check_incidence_lines_thermofield
lineage:
  motivated_by:
  - note.one-relation.two-residues-named-so-synthesis-can
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares where the proof uses them. Version 4 -> 5.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'check_real_states_read_real_capacity strengthened: four sample real states on Cl(2,4) (real on all 64 blades, omega(gh) = 0 and occupation 1/2 on the seven definite modes, null spaces conjugation-closed and totally isotropic of dimension 0, 2, 1, 0), the chiral vacuum (null space 3, not real), and floor((p+q)/2) <= min(p,q) iff |p - q| <= 1 for p + q <= 6; label and module docstring updated. Version 3 -> 4.'
  correction_pass:
    by: ai-colony-2026-10-22-toe
    date: '2026-10-22'
    open_problem: op.folded-state-selection-note
    note: 'Repointed the descended-form premise from the folded note''s copy (state-selection.descended-form-state-independent@1)
      to T05''s (singularity.descended-form-state-independent@2), which carries the zero-weight scope; (iii) now states
      that scope. After this, no entity outside the note uses the note''s same-title ids. Version 2 -> 3.'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'W503: lay and one-liner now state the condition u != 0 (respectively v != 0) for the thermofield-double reading.'
  open_problem: op.which-capacity
  note: Partial progress only. Computes how the incidence vacua split between the real and complex capacities; it does not connect them to the series' selected (descended) state of the boundary modes, so the open problem stays partial. Clause (v) bears on op.rule-2-sign conditionally on a reality premise. Restated after referee review (only the two spanning vacua are thermofield doubles).
---

## formal
Let $\Cl(2,4)$ act on its eight-dimensional Fock module, with ground generators $e_{1}$ ($e_{1}^{2} = 1$) and $e_{2}, e_{3}, e_{4}$ (squares $-1$), and ascent plane $e_{+}, e_{-}$ ($e_{\pm}^{2} = \pm 1$); give the module the Hermitian structure for which every generator is unitary, $g^{*} = g^{-1}$, which fixes the frame $e_{1}$ and the normalisation of the ascent pair. Put $\nO = \tfrac12(e_{+} + e_{-})$, $\ninf = e_{+} - e_{-}$, the ascent mode $a = \nO$, $a^{*} = \tfrac12\ninf$, $N = a^{*}a$. For a point $x = t e_{1} + r e_{2}$ (every point after a spatial rotation, which is unitary and fixes $N$) put $b = \tfrac12(e_{1} + e_{2})$, $b^{*} = \tfrac12(e_{1} - e_{2})$, the boost-qubit mode of the $(t,r)$ plane, $c = \tfrac12(e_{3} + ie_{4})$, the complex-only (spectator) mode, the null coordinates $u = t - r$, $v = t + r$, and $X(x) = \nO + x - \tfrac12 Q(x)\ninf$ with $Q(x) = uv$, as in Proposition \claimref{one-relation.spacetime-manifold-vacuum-lines}.
\begin{enumerate}
\item[(i)] \emph{(Real states fill only the real capacity.)} Call a state $\omega$ on $\Cl(p,q)_{\C}$ real if $\omega(y) \in \R$ for every $y \in \Cl(p,q)$. Then $\omega(gh) = 0$ for orthogonal generators $g, h$ of equal square, so every mode $\tfrac12(g + ih)$ of a definite block has occupation exactly $\tfrac12$; and $\{y \in V_{\C} : \omega(y^{*}y) = 0\}$ is the complexification of a real totally isotropic subspace, of dimension at most $\min(p,q)$. Hence a real state is the Fock vacuum of a maximal isotropic subspace of $V_{\C}$ only if $|p - q| \le 1$: no vacuum of the incidence chart of Fact \claimref{one-relation.imported-pure-spinors-incidence-chart} is a real state.
\item[(ii)] \emph{(The two distinguished vacua of a line.)} Let $\ket{0}_{\pm}$ be the vacua of $a$ and $b$ in the two chirality halves; they differ in the occupation of $c$. The incidence line $L_{x}$ is spanned by the two vacua of definite spectator occupation
\[
\Omega_{x} = (1 - u\,a^{*}b^{*})\ket{0}_{+}, \qquad \Psi_{x} = (b^{*} - v\,a^{*})\ket{0}_{-} .
\]
On each, the state of the $(a,b)$ pair is pure, the spectator is pure and carries all the non-reality required by (i) (value $\pm i$ on $e_{3}e_{4}$), and the state is real on the subalgebra generated by $e_{1}, e_{2}, e_{+}, e_{-}$. For $u \ne 0$, $\Omega_{x}$ is the thermofield double of the ascent mode's Gibbs state with $e^{-\beta} = u^{2}$, with partner the boost qubit $b$ (Theorem \claimref{state-selection.partner-purification-are-canonical}); for $v \ne 0$, $\Psi_{x}$ is likewise the thermofield double at $e^{-\beta} = v^{2}$, after a unitary on the partner. The inverse temperature is negative when $|u| > 1$ (respectively $|v| > 1$), the occupation then exceeding $\tfrac12$. At $u = 0$, $\Omega_{x}$ is the bare vacuum, not faithful on the ascent mode, and is no thermofield double (likewise $\Psi_{x}$ at $v = 0$).
\item[(iii)] \emph{(A general vacuum on the line.)} Every vacuum on $L_{x}$ has a diagonal ascent-mode marginal, of the descended Gibbs form when the ascent mode has nonzero weight (Theorem \claimref{singularity.descended-form-state-independent}; at zero weight a diagonal marginal is Gibbs only at occupation $\tfrac12$), with occupation $\langle N \rangle$ in the closed segment between $u^{2}/(1 + u^{2})$ and $v^{2}/(1 + v^{2})$, every value attained. A vacuum $\lambda\Omega_{x} + \mu\Psi_{x}$ with $\lambda\mu \ne 0$ entangles the $(a,b)$ pair with the spectator $c$: its $(a,b)$ state is mixed, and the ascent mode is purified by $b$ and $c$ jointly, not by the boost qubit alone.
\item[(iv)] \emph{(Pointwise compatibility.)} So the incidence-line structure admits, at the point $x$, a vacuum with thermal ascent marginal at every inverse temperature corresponding to the segment of (iii); $\beta = 2\pi$ is attained on $L_{x}$ exactly when $e^{-\pi}$ lies between $|u|$ and $|v|$, a condition that depends on the frame and scale fixed by the Hermitian structure, the dilation not being unitary for it. At the origin every vacuum on $L_{0}$ is the ascent vacuum. Nothing here connects these vacua to the selected (descended) state of the boundary modes.
\item[(v)] \emph{(The sign of an adjoined generator.)} Let two adjoined orthogonal generators $\varepsilon$, $\nu$ have $\varepsilon^{2} = -1$. Their plane is hyperbolic if and only if $\nu^{2} = +1$; if $\nu^{2} = -1$, every state real on the subalgebra of that plane gives its mode occupation exactly $\tfrac12$, by the argument of (i). A state real on the adjoined plane's subalgebra with a non-tracial ($\beta \ne 0$) marginal there therefore exists only for $\nu^{2} = +1$; this selects the sign only under the premise that the adjoined plane's state be real there, which is not derived.
\end{enumerate}

## technical
A state that takes real values on the real Clifford algebra can only hold modes made from real null vectors, so it can be pure on at most as many modes as the real capacity; on the modes that exist only after complexification it sits at occupation one half. The incidence vacua, which are pure on three complex modes, are therefore never real. Computing them at a point with null coordinates $u$ and $v$ shows how the line is built. It is spanned by two distinguished vacua, those in which the complex-only spectator mode has definite occupation: one is a two-mode squeezed state of the ascent mode with spacetime's boost qubit, with amplitude $u$, the other a single shared excitation with amplitude $v$. Each is pure on the two real modes, real there, and is the thermofield double of a Gibbs state of the ascent mode with Boltzmann factor $u^{2}$ or $v^{2}$ (negative temperature when the factor exceeds one), with the boost qubit as partner; the spectator carries all the non-reality. A general vacuum on the line still has a Gibbs-form ascent marginal, with occupation between the two endpoint values, but it entangles the real pair with the spectator, so its ascent mode is purified by the boost qubit and the spectator together. Whether a given inverse temperature, such as $2\pi$, occurs at a point depends on the frame and scale.

## lay
Two counts of quantum modes appear in the series: modes built from real light-like directions, and the larger number available once complex numbers are allowed. A state described by real numbers alone can only fill the first kind; on the extra mode it is always half full. The pure states that the series attaches to each point of spacetime, its vacua, use the extra mode, so none of them is of that real kind. Writing them out shows that each point's family of vacua is spanned by two special ones. In each of these, provided the point is not on a light ray through the origin, the added direction is entangled only with spacetime's own time-and-space direction and looks thermal on its own, the way half of a pure pair looks hot, while the extra complex mode sits in a fixed state. Mixtures of the two special vacua also look thermal on the added direction, but there the extra mode takes part in the entanglement.

## one-liner
Real states fill at most $\min(p,q)$ modes, so no incidence vacuum is real; at a point with null coordinates $u, v$ the incidence line is spanned by $(1 - u\,a^{*}b^{*})\ket{0}$ and $(b^{*} - v\,a^{*})\ket{0}$, the vacua of definite spectator occupation, which, provided $u \ne 0$ (respectively $v \ne 0$), are thermofield doubles of the ascent mode with the boost qubit at $e^{-\beta} = u^{2}, v^{2}$; other vacua on the line also involve the spectator.
