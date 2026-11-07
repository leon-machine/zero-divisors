---
id: synthesis.channel-phase-invisible-to-axially-covariant-completions
kind: claim
version: 3
title: 'The channel phase is invisible to axially covariant completions'
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.face-mass-form-unit-plus-gram@1
  - families.skeleton-rank-one-plus-ordering-shift@5
  - families.rigidity-pairing-sector-one-event@3
  - synthesis.coherent-face-vector-real-slices@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_axial_rotation_is_symmetry_of_real_structure_words
- kind: check
  ref: check.py::check_fock_rotation_covariance
lineage:
  motivated_by:
  - synthesis.coherent-face-vector-real-slices
  - families.koide-instrument
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The Fourier unit in zeta = e^{2 pi i/3}, the channel phase e^{i chi} and the axial phase e^{i theta} became I_4, numbers and family-vector components read in span{1, I_4}, and the eigenlines C u'', C f_+- are written as span{1, I_4} lines; no bare i remains. By Leon''s ruling R3 the face-space reading is stated once in R3''s words: numbers and the module''s complex structure in span{1, I_4}, the module read on the tower''s floors (notational).'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check entries synced with check.py: +1, -0 (added check_fock_rotation_covariance). Version 1 -> 2. stale module docstring (checks (a)-(d) not present) replaced by a description of what is run; added check_fock_rotation_covariance: psi[Rc] = R^ psi[c], H(R^ psi) = R H(psi) R^T, and invariance of sum_k (Omega_k^dag)^2 and sum_k Omega_k^dag Omega_k under the Fock rotation (16 cases).'
  open_problem: op.second-order-breaking
  note: >-
    Selection rule for the free phase of op.second-order-breaking (delta = 0.222, read as the
    channel phase chi of the coherent face vector in the real-slice reading). If the charged masses
    are read as eigenvalues of the face mass form, chi is invisible to every completion covariant
    under rotations about the democratic axis, which includes everything built from the source,
    its conjugate or any S3-equivariant real structure, and U(3)- or O(3)-invariant face words. The
    phase can enter only through structure that sees the family basis beyond those (the cyclic
    family shift survives), for instance a cubic family word. It also shows that the real-slice
    reading of the masses (where delta enters directly) and the eigenvalue reading are not
    interchangeable. Complements the stabiliser result filed for op.non-gaussian-completion in the
    same run. Bosonic face modes. Transport-absent.
---

## formal
Let $\hat\Omega_{k}$ and the mass form $H(\psi)$ be as in Theorem \claimref{families.skeleton-rank-one-plus-ordering-shift} and Proposition \claimref{synthesis.face-mass-form-unit-plus-gram}, $\hat\Omega(c)^{\dagger} = \sum_{k}\bar{c}_{k}\hat\Omega_{k}^{\dagger}$, and for a real orthogonal family matrix $R$ with $\det R = 1$ let $\hat{R}$ be the Fock unitary $a_{iA}^{\dagger} \mapsto \sum_{j}R_{ji}a_{jA}^{\dagger}$. Let $u' = (1,1,1)$, $f_{+} = (1, \zeta, \zeta^{-1})$, $\zeta = e^{2\pi I_4/3}$ (numbers, the components of family vectors and the module's complex structure are read in $\mathrm{span}\{1, I_4\}$, the module read on the tower's floors, where $I_4$ commutes with the tower vectors), and let $v(\chi) = \kappa(u' + \lambda e^{I_4\chi}f_{+})$ be the coherent face vector of an antisymmetric pairing (Proposition \claimref{families.rigidity-pairing-sector-one-event}), $\chi$ its channel phase.
\begin{enumerate}
\item[(i)] \emph{(Axial rotations move only the phase.)} A rotation $R$ about $u'$ commutes with the cyclic family shift, fixes $u'$, and multiplies $f_{+}$ by a phase $e^{I_4\theta}$: $Rv(\chi) = v(\chi + \theta)$. It commutes with complex conjugation and with every $S_{3}$-equivariant real structure $\sigma_{x,y}$ of Proposition \claimref{synthesis.coherent-face-vector-real-slices}, and $H(\hat{R}\psi) = RH(\psi)R^{\mathsf{T}}$.
\item[(ii)] \emph{(Invisibility.)} Let $\psi[c]$ be any state built from the vacuum by a fixed polynomial in $\hat\Omega(c)^{\dagger}$, $\hat\Omega(\bar{c})^{\dagger}$ or $\hat\Omega(\sigma_{x,y}c)^{\dagger}$ and in face words invariant under real rotations (such as $\sum_{k}\hat\Omega_{k}^{\dagger}\hat\Omega_{k}$ or $\sum_{k}(\hat\Omega_{k}^{\dagger})^{2}$), or evolved from the vacuum by a Hamiltonian built from these. Then $\psi[Rc] = \hat{R}\psi[c]$, so the spectrum of $H(\psi[v(\chi)])$ does not depend on $\chi$: the channel phase cannot set any ratio of mass-form eigenvalues.
\item[(iii)] \emph{(What can see it; computed, exact.)} The word $\sum_{k}(\hat\Omega_{k}^{\dagger})^{3}$, invariant under the cyclic family shift but not under rotations about $u'$, gives different characteristic polynomials of $H$ at $c$ and $Rc$ for rational rotations $R$ about $u'$, and equal ones at $c$ and its cyclic shift.
\end{enumerate}
So, if the charged masses are eigenvalues of the face mass form, the phase $\delta = 0.222$ of op.second-order-breaking (the channel phase in the real-slice reading of Proposition \claimref{synthesis.coherent-face-vector-real-slices}(iii)) can only be produced by an interaction that sees the family basis beyond rotation-invariant data, reducing the axial $SO(2)$ to the cyclic shift, under which $\chi$ matters modulo $2\pi/3$. In the real-slice reading the masses depend on $\delta$ directly; the two readings are therefore not interchangeable.

## technical
In the families paper the coherent face vector of every pairing is $\kappa(u' + \lambda e^{I_4\chi}f_{+})$ (numbers read in $\mathrm{span}\{1, I_4\}$): a democratic part, a Fourier doublet part of relative size $\lambda$ and a channel phase $\chi$, and in the real-slice reading of the charged spectrum $\chi$ is the Koide phase. Rotations of family space about the democratic axis fix $u'$ and multiply the Fourier vector $f_{+}$ by a phase, so they shift $\chi$ and nothing else. The mass form transforms covariantly under family rotations, and every construction that uses only the source, its complex conjugate or one of the store's $S_{3}$-equivariant real structures, plus rotation-invariant face words, commutes with these rotations. The eigenvalues of the mass form therefore cannot depend on $\chi$ for any such completion. The exact six-mode check confirms this for all four real structures and finds that a cubic family word, which sees the family basis, does respond to the rotation while still ignoring the cyclic shift. A completion that wants the observed phase to matter for the masses read as mass-form eigenvalues must contain structure of that kind.

## lay
In the framework the three charged lepton masses are tied to a single angle, measured at about $0.222$ radians, and the open problem is to derive it. This result shows a restriction on where it can come from. The angle describes how a certain internal vector sits relative to a fixed axis; turning the internal space around that axis changes only the angle. Any mechanism that treats all such turns alike, which covers every mechanism built from that internal vector, its mirror image, the framework's notions of which directions count as real, and rotation-invariant combinations, therefore produces masses that cannot depend on the angle at all. Only a mechanism that singles out the three generations as a definite set of directions, not just up to rotation, can make the angle matter; the framework's permutation symmetry of the generations is such a structure, and an example built from it does respond to the angle.

## one-liner
Rotations about the democratic axis shift only the channel phase $\chi$ of the coherent face vector and commute with every $S_{3}$-equivariant real structure, so any completion built from the source, its conjugate or a real structure and rotation-invariant face words has a mass-form spectrum independent of $\chi$; the phase $\delta = 0.222$ can matter only through family-basis structure such as a cubic family word.
