---
id: synthesis.light-pair-split-needs-broken-source-stabiliser
kind: claim
version: 1
title: Frozen vacua invariant under the stabiliser of their source keep the light pair degenerate at every order of cumulants; a split must break that stabiliser
status: proved
region: synthesis
subject: generations
tags: [pairing-and-bogoliubov, flavour-and-mixing]
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
  - synthesis.face-mass-form-unit-plus-gram@1
  - families.skeleton-rank-one-plus-ordering-shift@5
  - families.imported-squeezed-vacuum-bosonic-pairing@3
  - synthesis.coherent-face-vector-real-slices@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_covariance
- kind: check
  ref: check.py::check_stabiliser_invariant_states_degenerate
- kind: check
  ref: check.py::check_breaking_controls
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.one-open-problem-three-forms
  - families.classification-displaced-gaussian-class-solved-level
extraction:
  open_problem: op.non-gaussian-completion
  note: >-
    Adversarial route on op.non-gaussian-completion. The problem's first attack line (add the
    lowest non-Gaussian cumulant with the skeleton fixed) is refuted for every completion whose
    frozen vacuum keeps the symmetry of its one source: the obstruction to splitting the light pair
    is the stabiliser of the source in the family U(3), not Gaussianity, and Schur's lemma keeps
    the pair degenerate at every order of cumulants. Non-Gaussianity is therefore neither the
    obstruction nor the cure. What a completion needs is a second face-space structure; the store
    already has one, the real structure of face space, and exact instances show that words using it
    split the pair from a complex source alone. This narrows the problem; it does not derive 207 and
    says nothing about whether a real-structure completion avoids a second free number. The
    magnitude side (what fixed second moments allow) is the result filed alongside,
    synthesis.cumulants-at-fixed-second-moments-keep-the-floor. Bosonic face
    modes as in the skeleton theorem. Transport-absent.
---

## formal
Let $a_{iA}$ ($i = 1,2,3$ a family, $A = 1,2$ a slot) be the six bosonic face modes, $\hat\Omega_{k}$ the face operators and $H(\psi)$ the mass form of Theorem \claimref{families.skeleton-rank-one-plus-ordering-shift}, evaluated in an arbitrary state $\psi$ as in Proposition \claimref{synthesis.face-mass-form-unit-plus-gram}, and put $\hat\Omega(c)^{\dagger} = \sum_{k}\bar{c}_{k}\hat\Omega_{k}^{\dagger}$ for $c \in \C^{3}$. For $U \in U(3)$ let $\hat{U}$ be the Fock unitary with $\hat{U}a_{iA}^{\dagger}\hat{U}^{\dagger} = \sum_{j}U_{ji}a_{jA}^{\dagger}$, and $N(U) = \overline{\det U}\,U$.
\begin{enumerate}
\item[(i)] \emph{(Covariance.)} For every state, $H(\hat{U}\psi) = N(U)\,H(\psi)\,N(U)^{\dagger}$, and $\hat{U}\hat\Omega(c)^{\dagger}\hat{U}^{\dagger} = \hat\Omega(N(U)c)^{\dagger}$.
\item[(ii)] \emph{(The stabiliser keeps the pair degenerate.)} Fix $c \neq 0$ and let $G_{c} = \{U : N(U)c = c\}$, which contains every $U$ fixing $c$ with $\det U = 1$ and so acts on $c^{\perp}$ as $SU(2)$. If $\hat{U}\psi = \psi$ for all $U \in G_{c}$, or only for two elements whose $N(U)$ have commutant $\mathrm{span}\{P_{c}, 1 - P_{c}\}$, then $H(\psi) = h_{c}P_{c} + h_{\perp}(1 - P_{c})$: $c$ is an eigenvector and the light pair is exactly degenerate. This holds for every such state, Gaussian or not, whatever its cumulants. It covers every state obtained from the vacuum by a polynomial in $\hat\Omega(c)^{\dagger}$ and $U(3)$-invariant face words such as $\hat{V} = \sum_{k}\hat\Omega_{k}^{\dagger}\hat\Omega_{k}$, and every state evolved from the vacuum by a Hamiltonian built from $\hat\Omega(c)$, $\hat\Omega(c)^{\dagger}$ and such words: one source and covariant interactions never split the pair.
\item[(iii)] \emph{(Non-Gaussian instances; computed, exact.)} $(1 + (\hat\Omega_{3}^{\dagger})^{3})\ket{0}$ and $(\hat\Omega_{3}^{\dagger} + \tfrac13\hat{V}(\hat\Omega_{3}^{\dagger})^{2} + 2i\,\hat\Omega_{3}^{\dagger}\hat{V}(\hat\Omega_{3}^{\dagger})^{2})\ket{0}$ are invariant under $G_{e_{3}}$, have a nonzero ordered truncated four-point function $\langle a_{11}^{\dagger}a_{22}^{\dagger}a_{11}a_{22}\rangle^{T}$, so are not Gaussian (Wick's theorem, Fact \claimref{families.imported-squeezed-vacuum-bosonic-pairing}), and have exactly degenerate light pairs with $h_{e_{3}} \neq h_{\perp}$; so does a state built from $\hat\Omega(c)^{\dagger}$ and $\hat{V}$ on a complex $c$.
\item[(iv)] \emph{(Breaking it; computed, exact.)} Adding $(\hat\Omega_{1}^{\dagger})^{2}\ket{0}$ to the first state of (iii) splits the pair. Words that also use the complex-conjugate face vector, $\ket{0} + \hat\Omega(c)^{\dagger}\ket{0} + \tfrac23\hat\Omega(c)^{\dagger}\hat\Omega(\bar{c})^{\dagger}\ket{0}$, which are covariant under real orthogonal $U$ only, split the pair for a complex $c$, generic or isotropic ($\sum_{k}c_{k}^{2} = 0$), and leave it degenerate for real $c$; the same words with $\hat\Omega(c)^{\dagger}$ in place of $\hat\Omega(\bar{c})^{\dagger}$ leave it degenerate.
\end{enumerate}
So the light-pair degeneracy of the skeleton is a symmetry statement about the source, not a property of the Gaussian class: a completion that splits the pair must carry a second face-space structure breaking $G_{c}$. A real structure on face space is one already in the store, and by Proposition \claimref{synthesis.coherent-face-vector-real-slices}(ii) the coherent vector of every antisymmetric pairing with $\lambda > 0$ is not real up to phase under any $S_{3}$-equivariant real structure, which is the situation in which (iv) splits the pair. Whether a completion of that kind produces $m_{\mu}/m_{e}$ with no second free number is not decided here.

## technical
The families paper's Gaussian freezing leaves the electron and muon exactly degenerate, and the registered open problem asks for a non-Gaussian frozen vacuum that splits them. This result shows the degeneracy has a different cause, for every completion whose frozen vacuum keeps the symmetry of its one source. Family rotations act on the face operators through $N(U) = \overline{\det U}\,U$, and the mass form transforms covariantly, $H \mapsto NHN^{\dagger}$, in every state. A frozen vacuum built from one face vector $c$ (the source) and family-covariant operations is invariant under the rotations fixing $c$, which act on the two directions orthogonal to $c$ as $SU(2)$; by Schur's lemma the mass form is then a single number on that plane. That is true at every order of cumulants.

Exact six-mode Fock computations confirm it: invariant states with nonzero connected four-point functions have exactly degenerate light pairs, including states built with the covariant quartic word $\sum_{k}\hat\Omega_{k}^{\dagger}\hat\Omega_{k}$. Breaking the stabiliser splits the pair, and the store already supplies a way to do it: words that use the complex conjugate of the source, covariant only under real rotations, split the pair as soon as the source is not real up to phase, which every pairing with $\lambda > 0$ satisfies. The open problem therefore becomes: which second face-space structure, and whether it brings a free number.

## lay
In the families paper, the electron and muon come out with exactly equal masses whenever the vacuum is of the simplest, Gaussian, type, and the paper's proposed way out was to use a more complicated vacuum. This result shows that complexity alone cannot work for any vacuum that keeps a certain symmetry. The equality is protected by that symmetry: the vacuum is built from a single preferred direction, and any rotation of the other two directions that leaves that one alone also leaves the vacuum alone. As long as that remains true, however complicated the vacuum, the two lighter particles stay equal. Exact computations confirm it. To separate them, some second ingredient must spoil the symmetry. One candidate already exists in the framework, a notion of which directions count as real, and with it the separation does appear in examples. Whether it gives the right ratio, about 207, is still open.

## one-liner
The face mass form is covariant, $H(\hat{U}\psi) = N H N^{\dagger}$ with $N = \overline{\det U}\,U$, so any state invariant under the stabiliser of its one source has an exactly degenerate light pair at every order of cumulants; splitting $m_{e}$ from $m_{\mu}$ needs a second face-space structure breaking that stabiliser, such as the real structure, not non-Gaussianity.
