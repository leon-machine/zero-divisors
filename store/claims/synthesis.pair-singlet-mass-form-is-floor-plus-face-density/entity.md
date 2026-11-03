---
id: synthesis.pair-singlet-mass-form-is-floor-plus-face-density
kind: claim
version: 1
title: On the span of face words the mass form is the floor $1 + \langle N\rangle/4$ plus a weighted face density, so the forced eigenvector is the lowest in every source-built state and, under the mass-squared reading of the mass form, the split is a population ratio of the selected state
status: proved
region: synthesis
subject: generations
tags: [pairing-and-bogoliubov, flavour-and-mixing, mass-generation, representation-theory]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
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
  - families.imported-squeezed-vacuum-bosonic-pairing@3
  - families.skeleton-rank-one-plus-ordering-shift@5
  - synthesis.face-mass-form-unit-plus-gram@1
  - synthesis.cumulants-at-fixed-second-moments-keep-the-floor@1
  - synthesis.real-structure-breaks-source-stabiliser-to-z2@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_face_word_monomial_algebra
- kind: check
  ref: check.py::check_mass_form_is_floor_plus_weighted_density
- kind: check
  ref: check.py::check_forced_eigenvector_is_lowest_in_source_built_states
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.one-open-problem-three-forms
  - synthesis.real-structure-breaks-source-stabiliser-to-z2
  - synthesis.cumulants-at-fixed-second-moments-keep-the-floor
extraction:
  open_problem: op.non-gaussian-completion
  note: >-
    Settles the problem's second line of attack (the ordering observation) and sharpens its first.
    The face pair operators and the family density close on the span of face-word monomials applied
    to the vacuum, which contains the Gaussian class and every completion built from face words and
    the invariant quartic word: the monomials are orthogonal with norm (D+1)! m!, each Omega_l acts as
    (D+1) times a derivative, and the family density is fixed by the face words. The mass form on that
    span is the floor (1 + <N>/4) times the unit plus a positive Gram matrix, so the floor is attained
    exactly in the face directions whose pair annihilator kills the state. In states built from the
    source and its conjugate the annihilator along the normal n of the source's real plane kills the
    state, so n is the lowest eigenvector, at the floor, strictly lowest exactly when the light pair is
    split: the observation recorded in the stored Z2 result is a theorem. The electron is then fixed by
    the mean pair number alone, and the muon and tau are the floor plus the two eigenvalues of the
    weighted face density on the source's plane, whose sum is fixed by the first two moments of the
    pair number. A selection rule for the frozen vacuum must therefore fix two numbers of the state:
    the second moment of the pair number relative to its mean and the population ratio of the two
    plane eigen-directions, which is the 207 under the mass-squared reading of the mass form. The Lie algebra spanned by the face
    operators, their adjoints and the density, and the reading of the Gaussian class as the orbit of
    the vacuum, are noted in the findings and not claimed here. A remark in the proof records that the only pure quasi-free states on the span are the Gaussian pairings, all with a degenerate light pair, so the completion lies outside the quasi-free class. Transport-absent: bosonic Fock algebra
    on the face modes.
---
## formal
Let $a_{iA}$ ($i = 1, 2, 3$, $A = 1, 2$) be the six bosonic face modes of Theorem \claimref{families.skeleton-rank-one-plus-ordering-shift} (Fact \claimref{families.imported-squeezed-vacuum-bosonic-pairing}), $\hat\Omega_{k} = \tfrac12\varepsilon_{kij}\varepsilon_{AB}a_{iA}a_{jB}$ the face operators, $\hat\Omega(y) = \sum_{k}y_{k}\hat\Omega_{k}$, $\hat\rho_{lk} = \sum_{A}a_{lA}^{\dagger}a_{kA}$ the family density, $\hat{N}$ the number operator, $\hat{V} = \sum_{k}\hat\Omega_{k}^{\dagger}\hat\Omega_{k}$, and $H_{kl} = \tfrac12\langle\hat\Omega_{k}^{\dagger}\hat\Omega_{l} + \hat\Omega_{l}\hat\Omega_{k}^{\dagger}\rangle$ the mass form in an arbitrary state (Proposition \claimref{synthesis.face-mass-form-unit-plus-gram}). Let $\mathcal{S}$ be the closed span of the face-word monomials $\hat\Omega^{\dagger m}\ket{0} = \prod_{k}(\hat\Omega_{k}^{\dagger})^{m_{k}}\ket{0}$, $m \in \mathbb{N}^{3}$, $D = |m|$ (on which $\hat{N} = 2D$).
\begin{enumerate}
\item[(i)] \emph{(Face-word algebra.)} The monomials are orthogonal, $\|\hat\Omega^{\dagger m}\ket{0}\|^{2} = (D + 1)!\,m_{1}!\,m_{2}!\,m_{3}!$, and
\[
\hat\Omega_{l}\hat\Omega^{\dagger m}\ket{0} = (D + 1)\,m_{l}\,\hat\Omega^{\dagger(m - e_{l})}\ket{0},\qquad
\hat\rho_{lk}\hat\Omega^{\dagger m}\ket{0} = D\,\delta_{kl}\,\hat\Omega^{\dagger m}\ket{0} - m_{l}\,\hat\Omega^{\dagger(m - e_{l} + e_{k})}\ket{0},
\]
so $\hat{V} = \hat{D}(\hat{D} + 1)$ on $\mathcal{S}$, $\hat{D} = \hat{N}/2$.
\item[(ii)] \emph{(Floor plus weighted density.)} For every state supported on $\mathcal{S}$, pure or mixed,
\[
H \;=\; \Bigl(1 + \frac{\langle\hat{N}\rangle}{4}\Bigr)\mathbb{1} + G, \qquad G_{kl} = \Bigl\langle\hat\Omega_{k}^{\dagger}\hat\Omega_{l}\,\frac{\hat{N} + 3}{\hat{N} + 2}\Bigr\rangle \ \ge 0,
\]
with $\bar{y}^{\mathsf T}Gy = 0$ exactly when $\hat\Omega(y)$ annihilates the state, and $\mathrm{tr}\,H = 3 + 3\langle\hat{D}\rangle + \langle\hat{D}^{2}\rangle$. So $H \ge (1 + \langle\hat{N}\rangle/4)\mathbb{1}$ on $\mathcal{S}$, the floor attained exactly on the face directions whose pair annihilator kills the state.
\item[(iii)] \emph{(Source-built states: the ordering.)} In the normal frame of Proposition \claimref{synthesis.real-structure-breaks-source-stabiliser-to-z2}, $c = (1, a, ia) = c_{R} + ic_{I}$, $a > 0$, $n = c_{R}\times c_{I}$, every state built from $\hat\Omega(c)^{\dagger}$, $\hat\Omega(\bar{c})^{\dagger}$ and $\hat{V}$ on the vacuum (and every mixture of such) satisfies $\hat\Omega(n)\psi = 0$, hence
\[
Hn = \Bigl(1 + \frac{\langle\hat{N}\rangle}{4}\Bigr)n ,
\]
the least eigenvalue of $H$; $n$ is strictly the lowest exactly when the light pair is split, and the two heavier eigenvalues sum to $2 + \tfrac52\langle\hat{D}\rangle + \langle\hat{D}^{2}\rangle$. The observation recorded in that result (the forced eigenvector lowest in the source-built instances) holds for the whole class, and a word in $n$ itself is what can lift $n$ off the floor.
\item[(iv)] \emph{(What a rule must fix.)} In a source-built state the lightest mass squared is fixed by the mean pair number alone, and the other two are the floor plus the eigenvalues $g_{\pm}$ of $G$ on $n^{\perp}$. Under the mass-squared reading, the measured charged-lepton masses require $g_{\mu}/g_{\tau} = (m_{\mu}^{2} - m_{e}^{2})/(m_{\tau}^{2} - m_{e}^{2}) \approx 3.536 \times 10^{-3}$ and $(\langle\hat{D}^{2}\rangle + \tfrac32\langle\hat{D}\rangle)/(1 + \tfrac12\langle\hat{D}\rangle) = (m_{\mu}^{2} + m_{\tau}^{2})/m_{e}^{2} - 2$, so for a state of one pair number $D \approx 6.07 \times 10^{6}$ (arithmetic on measured masses, not checked; a dictionary and not a prediction).
\end{enumerate}
So on the span of face words, which contains the Gaussian class $\exp(\hat\Omega(v)^{\dagger})\ket{0}$ and the completions built from face words and $\hat{V}$ in Proposition \claimref{synthesis.real-structure-breaks-source-stabiliser-to-z2}, the family splitting is the spectrum of a positive weighted density of face quanta above a floor set by the mean pair number; a rule selecting the non-Gaussian frozen vacuum must fix the pair-number moments and the population ratio of the two directions of the source's plane, and under the mass-squared reading the $207$ is that ratio.

## technical
The face operators remove an antisymmetric pair of quanta from two different families, one per face. Applied repeatedly to the vacuum their adjoints build a subspace on which the algebra is simple: the monomials are orthogonal with known norms, each annihilator acts as the pair number plus one times a derivative with respect to the corresponding word, and the family density is not independent of the words. Putting these into the stored formula for the mass form gives a closed expression valid in every state of that subspace: the unit times one plus a quarter of the mean number of quanta, plus a positive Gram matrix, the one-body density of the face quanta weighted by a factor between one and three halves. The floor is reached in a face direction exactly when the state is annihilated by the pair operator of that direction.

For the frozen vacua built from the coherent source and its conjugate, the two words lie in the complex span of the source's real plane, and the pair annihilator along the normal of that plane differentiates each of them to zero. So the normal is an exact eigenvector at the floor, and it is the lowest; it is strictly the lowest whenever the electron and muon are split, and tied with a second direction only when the state is a single source. This turns the ordering observed in the stored instances into a theorem for the whole class and identifies what lifts the forced direction: only a word that uses that direction itself. The same formula gives the sum of the two heavier eigenvalues in terms of the first two moments of the pair number. In this class the electron's mass is fixed by the mean pair number, and the muon and tau by how the face quanta populate the two directions of the source's plane; under the mass-squared reading the measured spectrum fixes that population ratio and the second moment of the pair number, and a selection rule must produce both.

## lay
In the families paper the three charged leptons get their masses from a vacuum full of correlated pairs of quanta, and the electron and muon come out equal unless the vacuum is of a more complicated, non-Gaussian kind. Earlier work showed that symmetry alone cannot fix the electron-to-muon ratio and noticed, in computed examples, that one particular direction always came out lightest. This result explains why, and does so for every vacuum of the relevant kind. The mass formula turns out to have a simple shape: a common floor, set only by how many pairs the vacuum holds on average, plus a term that counts how the pairs are spread over the family directions. The direction that always came out lightest is one that, by construction, never receives any pairs in these vacua, so it sits exactly on the floor. The other two masses then measure how the pairs are shared between the remaining two directions. Reading the formula's eigenvalues as squared masses, as the families paper does, the famous ratio of about 207 becomes a statement about how a frozen vacuum shares its pairs, and any rule that chooses the vacuum must get that sharing right.

## one-liner
On the span of face words the mass form is $H = (1 + \langle N\rangle/4)\mathbb{1} + \langle\hat\Omega_{k}^{\dagger}\hat\Omega_{l}(N + 3)/(N + 2)\rangle$, a floor plus a positive weighted face density, so in every state built from the source and its conjugate the normal $n$ of the source's real plane is the lowest eigenvector, at the floor, strictly when the pair is split; under the mass-squared reading of the mass form the $207$ is a population ratio of the selected state.
