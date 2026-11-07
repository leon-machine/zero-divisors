---
id: synthesis.real-structure-breaks-source-stabiliser-to-z2
kind: claim
version: 4
title: 'The real structure leaves a $\mathbb{Z}_{2}$ stabiliser and cannot give 207'
status: proved
region: synthesis
subject: generations
tags: [pairing-and-bogoliubov, flavour-and-mixing, no-go, representation-theory, needs-continuum]
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
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'consistency pass, sign slip in an intermediate expression of proof (ii) corrected'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - synthesis.light-pair-split-needs-broken-source-stabiliser@2
  - synthesis.coherent-face-vector-real-slices@2
  - families.rigidity-pairing-sector-one-event@4
  - synthesis.face-mass-form-unit-plus-gram@2
  - families.skeleton-rank-one-plus-ordering-shift@6
  - families.imported-squeezed-vacuum-bosonic-pairing@3
  - synthesis.light-cone-koide-is-quarter-turn@2
  - families.chart-computation-sign-twist-bracket-form@6
  - synthesis.channel-phase-invisible-to-axially-covariant-completions@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_normal_form_under_a_face_unitary
- kind: check
  ref: check.py::check_residual_stabiliser_is_z2
- kind: check
  ref: check.py::check_forced_eigenvector_and_free_block
- kind: check
  ref: check.py::check_cubic_family_word_has_no_residual_symmetry
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.one-open-problem-three-forms
  - synthesis.light-pair-split-needs-broken-source-stabiliser
  - synthesis.light-cone-koide-is-quarter-turn
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof (ii): the intermediate expression for the face action of I_4 R_n read conj(-I_4) I_4 R_n (-1)(-1), which is -R_n, against the correct end value R_n; it now reads conj(I_4^3 det R_n) I_4 R_n = conj(I_4) I_4 R_n = R_n (exact check in Cl(1,3) at a = 1 and a = 2/3: det(I_4 R_n) = I_4, N(I_4 R_n) = R_n, the old intermediate equals -R_n); the formal statement and the conclusion are unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The field unit in the channel and normal-form phases e^{i chi}, e^{i delta}, e^{i alpha}, e^{i phi}, in kappa = -i|kappa|, in the quarter-turns P_d - i P_s and P_s - i P_d, in the normal-form vector (1, a, ia) = c_R + i c_I, in the unitaries i R_n, i P_12 and diag(i, -i, 1), in m = c_R - i(1 + 2/lambda^2) c_I and in the check fields Q(i), Q(sqrt2, sqrt3)(i) became I_4, numbers (Fock amplitudes and unitary entries included) read in span{1, I_4} with the bar reversing I_4; the line C v, M_3(C) and the C-span of c_R, c_I are written over span{1, I_4}; no bare i remains. By Leon''s ruling R3 the face-space reading is stated once in R3''s words: numbers and the module''s complex structure in span{1, I_4}, the module read on the tower''s floors (notational).'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 2: the parenthetical "lowest in the source-built instances, not in general" (title, technical level, one-liner) and the closing observation of the formal statement are updated per synthesis.pair-singlet-mass-form-is-floor-plus-face-density (iii), which proves what was observed here: in every state built from the source, its conjugate and the invariant quartic word V (and every mixture of such), n is annihilated by the pair operator in its direction and sits at the floor 1 + <N>/4, the least eigenvalue of the mass form; a word in n itself still lifts it, so not in general. Cited in text only (that result uses this one). The mathematics proved here is unchanged.'
  open_problem: op.non-gaussian-completion
  note: >-
    The problem's first line of attack, decided for the two structures it names. The stored
    stabiliser result left open whether the real structure of face space, or a cubic family word,
    splits the light pair with no second free number. Here the pair (coherent source, real
    structure) is brought to a normal form by a face unitary: the structure becomes complex
    conjugation and the line of the source becomes that of (1, a, i a) with a = lambda/sqrt2, the
    same for every equivariant structure and every channel phase, up to a phase that depends on the
    structure and not on the channel phase. The residual symmetry is then a single reflection, which
    forces one exact eigenvector of the mass form and nothing else: exact six-mode Fock instances fill
    the whole five-dimensional commutant, tilt the heavy direction off the source, and move the split
    with the state. Where the forced eigenvector sits in the mass ordering is not fixed by the
    symmetry: it is the lowest in every instance built from the source, its conjugate and the
    invariant quartic word, and the top in an instance using a word in the forced direction itself.
    A cubic family word has only the monomial group, which fixes the source trivially. So for these
    two structures the split, and with it the 207, is a property of the selected non-Gaussian state,
    for which the series supplies no rule; the open problem is reformulated from "which structure"
    to "which state" for them. Bosonic face modes as in the skeleton theorem. Transport-absent.
---
## formal
Let $a_{iA}$ be the six bosonic face modes, $\hat\Omega_{k}$ the face operators, $H(\psi)$ the mass form of Theorem \claimref{families.skeleton-rank-one-plus-ordering-shift} in an arbitrary state (Proposition \claimref{synthesis.face-mass-form-unit-plus-gram}), $\hat\Omega(c)^{\dagger} = \sum_{k}\bar{c}_{k}\hat\Omega_{k}^{\dagger}$, and $N(U) = \overline{\det U}\,U$ the face action of the family unitary $U$, under which $H(\hat{U}\psi) = N H(\psi) N^{\dagger}$ (Proposition \claimref{synthesis.light-pair-split-needs-broken-source-stabiliser}(i)). Let $v = \kappa(u' + \lambda e^{I_4\chi}f_{+})$, $\lambda > 0$ (numbers, including Fock amplitudes and the entries of family unitaries, and the module's complex structure are read in $\mathrm{span}\{1, I_4\}$, the module read on the tower's floors, where $I_4$ commutes with the tower vectors, and the bar reverses $I_4$), be the coherent face vector of an antisymmetric pairing (Proposition \claimref{families.rigidity-pairing-sector-one-event}) and $\sigma = \sigma_{x,y} = (xP_{s} + yP_{d})\circ\overline{\phantom{v}}$, $|x| = |y| = 1$, any of the $S_{3}$-equivariant real structures of Proposition \claimref{synthesis.coherent-face-vector-real-slices}(i), among them the four $C$-compatible ones ($x, y = \pm1$) and the Lorentzian quarter-turn structure $\sigma_{-1,1}$ of Proposition \claimref{synthesis.light-cone-koide-is-quarter-turn}. Write $a = \lambda/\sqrt2$, so $a = 1$ at the Koide point $\lambda^{2} = 2$.
\begin{enumerate}
\item[(i)] \emph{(Normal form.)} There is a face unitary $M = F R_{\delta} Q^{\dagger}$ ($Q = x^{1/2}P_{s} + y^{1/2}P_{d}$ for a choice of square roots, the slice map of $\sigma$, for $\sigma_{-1,1}$ the quarter-turn $Q = P_{d} - I_4 P_{s}$; $R_{\delta}$ a rotation about the democratic axis; $F$ the orthonormal frame $u, d_{1}, d_{2}$) with $M\sigma M^{-1}$ complex conjugation and
\[
Mv \;=\; e^{I_4\alpha}\sqrt3\,|\kappa|\,(1,\ a,\ I_4 a).
\]
with $e^{I_4\alpha} = \overline{x^{1/2}}\,\kappa/|\kappa|$: the normal form is that of the line $\mathrm{span}\{1, I_4\}\,v$, and its phase depends on $\sigma$ (and on the choice of square root) but not on the channel phase $\chi$, which the rotation $R_{\delta}$ absorbs together with the slice phase $\delta$ ($\delta = \chi - \pi/2$ for $\sigma_{-1,1}$, $\delta = \chi$ for $\sigma_{-1,-1}$). The phase matters for completions with fixed coefficients (in $1 + \hat\Omega(v)^{\dagger} + \hat\Omega(\sigma v)^{\dagger}$ the two words acquire the relative phase $e^{-2I_4\alpha}$) and not for the symmetry statements below. Consequently every completion built from $\hat\Omega(v)^{\dagger}$, $\hat\Omega(\sigma v)^{\dagger}$ and $U(3)$-invariant words, or words defined in the normal frame, has a mass-form spectrum independent of $\chi$, in agreement with Proposition \claimref{synthesis.channel-phase-invisible-to-axially-covariant-completions}; $S_{3}$-invariant words that are not $U(3)$-invariant, written in the family frame, such as the cubic word of (iv), can see $\chi$.
\item[(ii)] \emph{(The residual stabiliser is $\mathbb{Z}_{2}$.)} In the frame of (i), with $c = (1, a, I_4 a) = c_{R} + I_4 c_{I}$, the unitaries commuting with conjugation and fixing $c$ are the real orthogonal matrices fixing $c_{R}$ and $c_{I}$, namely $\{1, R_{n}\}$ with $R_{n} = 1 - 2nn^{\mathsf T}/|n|^{2}$ the reflection in the plane of the source and $n = c_{R}\times c_{I} \propto (a, -1, 0)$; $R_{n} = N(I_4 R_{n})$ is in the face action, and at the Koide point it is the transposition of the two real axes. Its commutant has complex dimension $5$. Hence in every state invariant under $\hat{U}$, $U = I_4 R_{n}$, in particular every state built from $\hat\Omega(c)^{\dagger}$, $\hat\Omega(\bar{c})^{\dagger}$ and $U(3)$-invariant words, $n$ is an exact eigenvector of $H$, and $H$ is otherwise an arbitrary Hermitian form on the plane $n^{\perp} = \mathrm{span}\{c, m\}$, $m \propto c_{R} - I_4(1 + 2/\lambda^{2})\,c_{I}$. Carried back to the family coordinates, $n$ has real slice coordinates proportional to $a - \sqrt2\cos(\delta + 2\pi k/3)$, orthogonal to the projected vector $p_{k} \propto 1 + \lambda\cos(\delta + 2\pi k/3)$ of Proposition \claimref{synthesis.coherent-face-vector-real-slices}(iii); at the Koide point $n \propto 2u' - p$, the reflection of the Koide vector through the democratic axis, itself a Koide vector ($Q = \tfrac23$). The phase rotation $e^{I_4\phi}P_{c} + (1 - P_{c})$ fixes $c$ up to phase and does not commute with conjugation: the cut from the $SU(2)$ of the stored result to $\mathbb{Z}_{2}$ is the real structure's. The symmetry fixes the eigenvector $n$ and not its place in the mass ordering, which is an extra input of the state (see (iii)).
\item[(iii)] \emph{(The rest is the state's; computed, exact, at $a = 1$.)} Eleven states built from $\hat\Omega(c)^{\dagger}$, $\hat\Omega(\bar{c})^{\dagger}$ and $\hat{V} = \sum_{k}\hat\Omega_{k}^{\dagger}\hat\Omega_{k}$ are invariant under $\hat{U}$ and have $n$ as an exact eigenvector; the affine span of their mass forms is the whole five-dimensional commutant, so covariance imposes no further relation. The truncated single source $(1 + \hat\Omega(c)^{\dagger} + \tfrac12\hat\Omega(c)^{\dagger 2})\ket{0}$ keeps the source as an eigenvector and the pair degenerate; the two-word states tilt the heavy eigenvector off the source. In the real family $(1 + \hat\Omega(c)^{\dagger} + \hat\Omega(\bar{c})^{\dagger} + \beta\,\hat\Omega(c)^{\dagger}\hat\Omega(\bar{c})^{\dagger})\ket{0}$, $\beta \in \R$, which is invariant under the antiunitary implementing $\sigma$, the pair is degenerate at $\beta = 0$ (one real source, $2c_{R}$) and split with $\beta$-dependent values otherwise ($h_{n} = \tfrac{145}{77}$ at $\beta = 1$, $\tfrac{505}{257}$ at $\beta = 2$, $\tfrac{55}{32}$ at $\beta = -\tfrac12$). A Gaussian frozen vacuum invariant under that antiunitary has a real source and a degenerate pair.
\item[(iv)] \emph{(A cubic family word forces nothing.)} The word $\hat\Omega_{1}^{\dagger}\hat\Omega_{2}^{\dagger}\hat\Omega_{3}^{\dagger}$ is invariant exactly under the monomial unitaries whose $N$ has unit product of phases, and $|v_{k}|^{2} = |\kappa|^{2}(1 + \lambda^{2} + 2\lambda\cos(\chi + 2\pi k/3))$ are three distinct numbers unless two of the cosines coincide ($\chi \in \tfrac{\pi}{3}\mathbb{Z}$, which the physical phase is not), so the only monomial unitary fixing $v$ is the identity: a completion built from the source and the cubic word has no residual symmetry and its mass form is unconstrained.
\end{enumerate}
So the two second structures the open problem names act through covariance in opposite and equally insufficient ways: the real structure forces one eigenvector and leaves the split, and the position of that eigenvector in the ordering, to the state; the cubic word leaves everything to the state. For these two structures a split with no second free number needs a rule selecting the non-Gaussian frozen vacuum, which the series does not supply; and the channel phase, which encodes the $207$ in the projection reading, is invisible to the real-structure completions. Observation, computed here on the eleven states and on $150$ random instances in exploration, and proved for the whole class in Proposition \claimref{synthesis.pair-singlet-mass-form-is-floor-plus-face-density}(iii): in every state built from the source, its conjugate and $\hat{V}$ the forced eigenvector $n$ is annihilated by $\hat\Omega(n)$ and sits at the floor $1 + \langle\hat{N}\rangle/4$, the least eigenvalue of $H$ (strictly the lowest when the pair is split), while the $\mathbb{Z}_{2}$-invariant word $(\hat\Omega(n)^{\dagger})^{2}$ puts it on top ($h_{n} = \tfrac{1738}{199}$ in the instance checked); so even which family the forced eigenvector is remains the state's.

## technical
The stored stabiliser result says the electron and muon stay degenerate in any frozen vacuum that keeps the symmetry of its one source, and that a real structure on face space, already in the store, could break that symmetry. This result works out exactly what a real structure does. Any equivariant real structure, together with the coherent source of the families paper, can be rotated by a face unitary into a standard form: the structure becomes ordinary complex conjugation and the line of the source becomes that of the vector $(1, a, I_4 a)$ (numbers read in $\mathrm{span}\{1, I_4\}$) with $a = \lambda/\sqrt2$, equal to $1$ at the Koide point, up to a phase that depends on the structure and not on the channel phase. The channel phase does not survive, so no completion built from the source, its conjugate and $U(3)$-invariant words can see the phase that encodes the muon-to-electron ratio.

In the standard form the symmetry left is a single reflection, the swap of the two real axes at the Koide point. A reflection forces one eigenvector of the mass form, the normal $n$ to the source's real plane, and nothing more: the remaining two-by-two block is free. Exact Fock computations confirm it, filling the whole five-parameter family, tilting the heavy direction off the source, and moving the split as the state's coefficients move; whether the forced eigenvector is the lightest family is also the state's, the lowest in every state built from the source, its conjugate and the invariant quartic word (it sits at the floor of the mass form there, as a later result proves for that whole class), and the top in an instance built with a word in the forced direction itself. Carried back to the family coordinates, $n$ is the Koide vector with its doublet reversed, the reflection of the square-root-mass vector through the democratic axis. A cubic family word, the other candidate, is invariant only under permutations with phases, none of which fixes a source whose three components have distinct moduli, so it constrains nothing. The conclusion is a reformulation for these two structures: the ratio $207$ cannot come from the real structure or the cubic family word acting through symmetry; it must come from the choice of non-Gaussian state, for which the series has no rule.

## lay
The families paper leaves the electron and muon with equal masses, protected by a symmetry of the vacuum built from one preferred direction. One hoped-for cure was a notion of which directions in the family space count as real. This result shows what that notion can and cannot do. After a change of coordinates the preferred direction always looks the same, whichever version of reality is chosen and whatever the one free angle of the paper is, so that angle, which is where the muon-to-electron ratio would hide, is invisible. The symmetry that remains is a single mirror, and a mirror fixes only one thing: one definite direction in family space must be a mass eigenstate. Whether that state is the lightest, and how far apart the two light masses are, is not fixed at all; it depends on the detailed vacuum, and exact computations show every possibility is realised. A second candidate, a cubic combination of the three families, fixes even less. So for these two candidates the ratio of about 207 cannot be a consequence of symmetry; it would have to come from a rule choosing the vacuum, and no such rule is in the series.

## one-liner
Every $S_{3}$-equivariant real structure and the coherent source $\kappa(u' + \lambda e^{I_4\chi}f_{+})$ are carried by a face unitary to conjugation and the line of $(1, a, I_4 a)$, $a = \lambda/\sqrt2$, with a phase independent of $\chi$; the residual symmetry is the single reflection $R_{n}$, $n = c_{R}\times c_{I}$ (at the Koide point the reflection of the Koide vector through the democratic axis), which forces $n$ to be an exact eigenvector of the face mass form (at the floor, so the lowest, in every state built from the source, its conjugate and $\hat{V}$, not in general) and leaves a five-parameter block that exact Fock instances fill, while a cubic family word has no residual symmetry at all: the $207$ cannot come from the real structure or the cubic family word acting by covariance, only from the selected state.
