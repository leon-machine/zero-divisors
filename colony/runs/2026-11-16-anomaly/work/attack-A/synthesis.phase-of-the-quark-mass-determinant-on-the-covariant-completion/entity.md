---
id: synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion
kind: claim
version: 1
title: 'The phase of the quark mass determinant on the covariant completion'
status: proved
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, mass-generation, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-11-16-anomaly
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-16-anomaly
review: draft
derivations:
- name: main
  uses:
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix@4
  - synthesis.imported-left-right-bidoublet-two-yukawa-couplings@3
  - synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog@1
  - synthesis.imported-jarlskog-commutator-identity@2
  - synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase@4
  - synthesis.solar-angle-light-plane-sum-rule@1
  - synthesis.one-type-second-stages-are-twins@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_completion_is_a_bijection_off_the_balanced_frame
- kind: check
  ref: check.py::check_readings_with_a_real_determinant
- kind: check
  ref: check.py::check_stage_determinant_formula
- kind: check
  ref: check.py::check_quarter_turn_stage_gives_a_real_determinant
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix
  - synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase
  - neutrino.real-breaking-assumption
extraction:
  open_problem: op.strong-cp
  note: >-
    Second attack item of op.strong-cp (the mass phase). The answer to "does the stored quark structure fix the
    phase of the determinant" is no, by a proved statement: off the balanced frame the covariant completion is a
    bijection onto pairs of mass matrices, so it constrains the pair no more than the Standard Model does.
    Clauses (iii) and (iv) list the readings on which the determinant is real and say what closes each. One of
    them is not closed by stored data and is a half result in the open problem's own sense: on one-type
    symmetric stages with real first stages and the up-down phase carried by one sector, the determinant is
    real exactly at the quarter turn that the stored Cabibbo result selects; its sign is the sign of a product
    of two coefficients that nothing stored fixes, it is a tree-level statement about a texture and not the
    consequence of a symmetry of the coupled theory, and it says nothing about the coefficient of the colour
    four-form. Not claimed: that the physical angle vanishes on any reading; anything beyond tree level; the
    statement that a half turn is excluded by the hadron spectrum (literature, from memory, not checked).
    The relation of the determinant phase to the physical angle (the angle is the coefficient of the colour
    four-form shifted by this phase, and a rephasing of the families moves both) is the statement of the open
    problem and of the literature; it is not derived here. Standard and transport-absent: the freedom of the
    determinant phase, and Hermitian mass matrices from a generalised parity in left-right models (Mohapatra and
    Senjanovic 1978; Beg and Tsao 1978, cited from memory). New for the store: the bijection on the stored
    completion, the exact stage determinant, and the link between a real determinant and the quarter turn.
---

## formal
Scalars of family matrices are read in $\mathrm{span}\{1, I_{4}\}$, $^{*}$ is $I_{4} \mapsto -I_{4}$ on entries, $^{\dagger}$ its composite with the transpose, and a \emph{unit} is $z = e^{I_{4}\gamma}$, as in Fact \claimref{synthesis.imported-jarlskog-commutator-identity}. On a charge-preserving point of the rung field, with rung-$4$ components $\alpha$, $\beta$ and family matrices $Y$, $\tilde{Y}$ of size $N \times N$, the covariant completion (\claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}; in the chart of Fact \claimref{synthesis.imported-left-right-bidoublet-two-yukawa-couplings}) has
\[
M_{u} = \alpha Y + \bar{\beta}\tilde{Y}, \qquad M_{d} = \beta Y + \bar{\alpha}\tilde{Y}, \qquad m(c) = \tfrac12(|\alpha|^{2} - |\beta|^{2}) .
\]
Let $H_{q} = M_{q}M_{q}^{\dagger}$, $D = \det[H_{u}, H_{d}]$ and
\[
\Theta = \det M_{u}\,\det M_{d} = |\Theta|\,e^{I_{4}\theta_{M}} ,
\]
so that $\theta_{M}$ is the phase of the determinant of the quark mass matrices, the \emph{mass phase}.
\begin{enumerate}
\item[(i)] \emph{(The completion does not constrain the pair.)} If $m(c) \neq 0$, the map $(Y, \tilde{Y}) \mapsto (M_{u}, M_{d})$ is a bijection of pairs of $N \times N$ matrices, with inverse
\[
Y = \frac{\bar{\alpha}M_{u} - \bar{\beta}M_{d}}{2m(c)}, \qquad \tilde{Y} = \frac{\alpha M_{d} - \beta M_{u}}{2m(c)},
\]
and it maps pairs of symmetric matrices onto pairs of symmetric matrices. Hence for every unit $z$ the pair $(zM_{u}, M_{d})$ is realised at the same point of the rung field by family matrices of the same kind; it has the same $H_{u}$, $H_{d}$, so the same masses, the same mixing matrix and the same $D$, and $\Theta$ is multiplied by $z^{N}$. So $\theta_{M}$ is a function of the stored data $(\alpha, \beta, Y, \tilde{Y})$, namely the phase of $\det(\alpha Y + \bar{\beta}\tilde{Y})\det(\beta Y + \bar{\alpha}\tilde{Y})$, that takes every value at fixed masses and mixing: no stored statement about masses and mixing fixes it. On the balanced frame, $m(c) = 0$, $M_{d} = (\beta/\alpha)M_{u}$, $D = 0$ and $\Theta = (\beta/\alpha)^{N}(\det M_{u})^{2}$.
\item[(ii)] \emph{(What moves it.)} $\Theta$ is unchanged by the hypercharge phase $\alpha \mapsto z\alpha$, $\beta \mapsto \bar{z}\beta$ of the rung field, and is changed by the common phase $\alpha, \beta \mapsto z\alpha, z\beta$ at fixed family matrices. The exchange $(Y, \tilde{Y}) \mapsto (\tilde{Y}^{*}, Y^{*})$ sends $(M_{u}, M_{d})$ to $(M_{d}^{*}, M_{u}^{*})$ and $\Theta$ to $\Theta^{*}$.
\item[(iii)] \emph{(Three readings with a real determinant, and what each costs.)} (a) \emph{Real.} If $\alpha$, $\beta$, $Y$, $\tilde{Y}$ are real, $\Theta$ is real, of either sign, and $D = 0$: by the cited Fact the Jarlskog invariant vanishes. (b) \emph{Self-conjugate coupling.} If $\tilde{Y} = Y^{*}$, the coupling $Yc + \tilde{Y}c^{*}$ being fixed by the conjugation, then in every frame $M_{d} = M_{u}^{*}$, $\Theta = |\det M_{u}|^{2} \ge 0$, so $\theta_{M} = 0$, and $D \neq 0$ generically; but $H_{d} = H_{u}^{*}$, so the up and down mass spectra are equal. (c) \emph{Hermitian.} If $Y$ and $\tilde{Y}$ are Hermitian and $\alpha$, $\beta$ real, then $M_{u}$, $M_{d}$ are Hermitian, $\Theta$ is real, $D \neq 0$ generically and the spectra are unequal: the parity mechanism of left-right models. A matrix that is Hermitian and symmetric is real, so for the symmetric family matrices of a $10$ this reading is (a).
\item[(iv)] \emph{(Stages.)} Let $M_{q} = c_{q}\bigl(\J + \delta_{q}(E + X_{q})\bigr)$, $q = u, d$, with $\J$ the matrix of ones, $E = e_{3}e_{3}^{\mathsf{T}}$ and $X_{q}$ odd under the exchange $P_{12}$ of the first two families, the textures of \claimref{synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase}. An odd $X$ has entries $X_{11} = -X_{22} = p$, $X_{12} = -X_{21} = q$, $X_{13} = -X_{23} = r$, $X_{31} = -X_{32} = s$, and exactly
\[
\det\bigl(\J + \delta(E + X)\bigr) = -3\delta^{2}xy + \delta^{3}(q^{2} - p^{2}), \qquad xy = \tfrac13(p - q - 2s)(p + q - 2r),
\]
with $x$, $y$ the off-diagonal entries of the light-plane block $\bigl[\begin{smallmatrix} 2/3 & x \\ y & 0\end{smallmatrix}\bigr]$ of \claimref{synthesis.solar-angle-light-plane-sum-rule}(i). For one-type symmetric stages $X_{q} = t_{q}S_{q}$, $S_{q}$ real symmetric with entries $p_{q}$, $r_{q}$, and $c_{q}$, $\delta_{q} > 0$ real,
\[
\Theta = (c_{u}c_{d})^{3}(\delta_{u}\delta_{d})^{2}\,(t_{u}t_{d})^{2}\,R, \qquad R = \prod_{q}\bigl((p_{q} - 2r_{q})^{2} + \delta_{q}p_{q}^{2}\bigr) > 0 .
\]
So $\theta_{M} = 2(\arg t_{u} + \arg t_{d})$, plus a half turn if $c_{u}c_{d} < 0$, while the up-down phase $\phi$ of the cited result is $\pm(\arg t_{u} - \arg t_{d})$ modulo a half turn: the two are independent. If one coefficient is real, $\Theta$ is $\operatorname{sgn}(c_{u}c_{d})\,e^{\pm2I_{4}\phi}$ times a positive number, so $\cos\theta_{M} = \operatorname{sgn}(c_{u}c_{d})(2\cos^{2}\phi - 1)$ and
\[
\Theta \text{ is real} \iff \cos\phi \in \{0, \pm1\} .
\]
The cited result excludes $\cos\phi = \pm1$ and selects $|\cos\phi| < \tfrac12$; on that range $|\cos\theta_{M}| > \tfrac12$, the mass phase is within a sixth of a turn of $0$ or of a half turn, and it is $0$ or a half turn exactly at the quarter turn $\cos\phi = 0$: $\theta_{M} = 0$ for $c_{u}c_{d} < 0$ and a half turn for $c_{u}c_{d} > 0$. At the quarter turn, with $t_{d}$ real and $t_{u} = I_{4}\tau$, $\tau$ real: $M_{d}^{*} = M_{d}$ and $P_{12}M_{u}^{*}P_{12} = M_{u}$, the up matrix is the twin $M_{h}P_{12}$ of a Hermitian matrix $M_{h}$ in the sense of \claimref{synthesis.one-type-second-stages-are-twins}, $D \neq 0$ generically and the spectra are unequal. With both coefficients real, or both a quarter turn, one conjugation fixes both matrices and $D = 0$, as \claimref{synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog}(iii) requires. Two complex coefficients give a real $\Theta$ when $\arg t_{u} + \arg t_{d}$ is a multiple of a quarter turn, for instance opposite eighth turns.
\end{enumerate}
\emph{Reading (argued).} The series does not fix the mass phase. By (i) the stored completion leaves the pair of quark mass matrices as free as two arbitrary symmetric matrices, so nothing short of an added premise on $Y$, $\tilde{Y}$ and the frame can fix $\theta_{M}$. Of the premises in the store: the adjoint reading of the action clause of \claimref{dark-matter.premise-cpt-covariance} is satisfied by every $(Y, \tilde{Y})$ and constrains nothing; the real-breaking assumption (\claimref{neutrino.real-breaking-assumption}), stated for the lepton matrices, would if extended to the quark matrices be reading (a), which the store's nonzero Jarlskog invariant and its exclusion of $\cos\phi = \pm1$ close; reading (b) is closed by the top and bottom masses; reading (c) is not available for symmetric family matrices. What stays open is the reading of (iv): a real vacuum with real first stages in both sectors, a real second stage in one sector and a second stage at an exact quarter turn in the other. On it the determinant is real with a nonzero Jarlskog invariant, and the stored Cabibbo relation holds with no free phase, $|V_{us}|^{2} = (x + y)/((1 + x)(1 + y))$, which the stored windows of the mass ratios allow and do not yet test. That is half a result in the sense of the open problem, and it is less than it looks: it is a property of a texture at tree level, the two sectors being fixed by two different conjugations, which is not a symmetry of the coupled theory (a common one gives $D = 0$), so nothing stored protects it against corrections; its sign, zero angle or half turn, is the sign of $-c_{u}c_{d}$, which nothing stored fixes; and it says nothing about the coefficient of the colour four-form, to which $\theta_{M}$ is only added. A physical angle below $10^{-10}$ would need on this reading, besides a vanishing coefficient, $|\cos\phi|$ of the same order, that is, a reason for the exact quarter turn.

## technical
The stored quark masses come from two family matrices and two components of the rung field. Solving for the family matrices shows that, away from the balanced frame, every pair of mass matrices arises from exactly one pair of family matrices. The structure therefore fixes nothing about the pair, and in particular one may turn the up matrix by any phase without changing a single mass or mixing angle while the determinant's phase turns freely. The phase of the determinant, which adds to the strong CP angle, is a free number of the stored structure.

The determinant is real on four readings. Real matrices: but then there is no CP violation in the quark mixing, against the data and against the store's own Cabibbo result. A coupling equal to its own conjugate: then the up and down quarks have equal masses. Hermitian matrices, the classical left-right solution: but the family matrices of a $10$ are symmetric, and symmetric Hermitian matrices are real. The fourth survives: with the democratic textures the store uses, the determinant of a sector is an explicit square of its second-stage coefficient, so the determinant's phase is twice the sum of the two sectors' phases while the Cabibbo phase is their difference. If one sector is real, the determinant is real exactly when the Cabibbo phase is a quarter turn, the value the data select. The up matrix is then a Hermitian matrix composed with the exchange of the first two families.

This does not solve the strong CP problem: the bare angle is untouched, the sign (zero or a half turn) is open, and the pattern is not a symmetry, so loop corrections are not controlled.

## lay
One number of particle physics, the strong CP angle, is measured to be zero to ten decimal places, and no one knows why. Part of it comes from the quark masses: a phase attached to the product of all of them. This result asks whether the series' description of quark masses fixes that phase. It does not: the description is exactly as flexible as the Standard Model's. There is one suggestive pattern. If all the ingredients are real except one, and that one is turned by exactly a quarter turn, the phase vanishes or equals a half turn, and the quarter turn is the value that the measured mixing of the first two quark families already asks for. But the pattern is not enforced by any symmetry of the series, and it leaves the other part of the angle untouched.

## one-liner
For $m(c) \neq 0$ the covariant completion $(Y, \tilde{Y}) \mapsto (M_{u}, M_{d})$ is a bijection, so the phase $\theta_{M}$ of $\det M_{u}\det M_{d}$ is free at fixed masses and mixing; it vanishes for real matrices ($D = 0$), for $\tilde{Y} = Y^{*}$ (equal up and down spectra) and for Hermitian matrices (real when symmetric); on one-type symmetric stages $\Theta = (c_{u}c_{d})^{3}(\delta_{u}\delta_{d})^{2}(t_{u}t_{d})^{2}R$, $R > 0$, so with one sector real $\Theta$ is real exactly when the stored up-down phase is a quarter turn ($D \neq 0$, sign $-\operatorname{sgn}(c_{u}c_{d})$): a tree-level texture, not a symmetry, and silent on the bare angle.
