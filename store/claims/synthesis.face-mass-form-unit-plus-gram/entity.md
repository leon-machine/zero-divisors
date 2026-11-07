---
id: synthesis.face-mass-form-unit-plus-gram
kind: claim
version: 2
title: In every state the face mass form is at least the unit, the excess an explicit Gram matrix
status: proved
region: synthesis
subject: generations
tags: [pairing-and-bogoliubov, flavour-and-mixing]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - families.skeleton-rank-one-plus-ordering-shift@6
  - families.imported-squeezed-vacuum-bosonic-pairing@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_theta_normalisation
- kind: check
  ref: check.py::check_unit_plus_gram
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.skeleton-rank-one-plus-ordering-shift
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No bare i: the coefficient space C^3 of the source vector c is written span{1, I_4}^3, numbers read in span{1, I_4}; nothing stays. By Leon''s ruling R3 the face-space reading is stated once in R3''s words: numbers and the module''s complex structure in span{1, I_4}, the module read on the tower''s floors (notational).'
  open_problem: op.non-gaussian-completion
  note: Generalises clauses (1)-(2) of the skeleton theorem from the Gaussian class to every state of the six bosonic face modes, so it is the frame inside which any non-Gaussian completion must split the light pair. Its content is the state-independent lower bound H >= 1 and the explicit vectors that realise W; that H - 1 is a Gram matrix is automatic for any positive semidefinite matrix, so it does not by itself answer op.gram-square-and-face-space, which asks for the Yukawa form as the square of a face-space map. It uses only the canonical commutation relations of the bosonic modes; with fermionic (CAR) modes the face operators vanish identically, because the fermionic bracket is symmetric in the family pair, so the statement has no fermionic counterpart. Symmetric ordering being equivariant, the ordering constants alone cannot break S2, which (ii) makes explicit. Transport-absent.
---

## formal
Let $a_{p}$, $p = (i, A)$, be the six bosonic modes of the face algebra, $\Theta_{k} = \tfrac12(E_{k} \otimes \varepsilon)$ and $\hat\Omega_{k} = \sum_{pq}\Theta_{k}[p,q]\,a_{p}a_{q}$ as in Theorem \claimref{families.skeleton-rank-one-plus-ordering-shift}, and for any state $\psi$ (normalised, with finite fourth moments) let $H_{kl} = \tfrac12\langle\hat\Omega_{k}^{\dagger}\hat\Omega_{l} + \hat\Omega_{l}\hat\Omega_{k}^{\dagger}\rangle$ be that theorem's mass form. For $c \in \mathrm{span}\{1, I_4\}^{3}$ (numbers and the module's complex structure are read in $\mathrm{span}\{1, I_4\}$, the module read on the tower's floors, where $I_4$ commutes with the tower vectors) put $\Theta(c) = \sum_{k}c_{k}\Theta_{k}$ and $\hat\Omega(c) = \sum_{k}c_{k}\hat\Omega_{k}$. Then, for every state, Gaussian or not,
\[
H \;=\; \mathbb{1} \;+\; W^{\dagger}W, \qquad W c \;=\; \bigl(\hat\Omega(c)\psi,\ \sqrt2\,(\Theta(c)a)\psi\bigr) \in \mathcal{F} \oplus \mathcal{F}^{6},
\]
a linear map from face space. For a mixed state $\sum_{i}p_{i}|\psi_{i}\rangle\langle\psi_{i}|$ the same holds with $W^{\dagger}W$ replaced by $\sum_{i}p_{i}W_{i}^{\dagger}W_{i}$, again the unit plus a positive semidefinite (Gram) matrix. Explicitly $H_{kl} = \delta_{kl} + \langle\hat\Omega_{k}^{\dagger}\hat\Omega_{l}\rangle + 2\langle a^{\dagger}\Theta_{k}\Theta_{l}a\rangle$. Consequently:
\begin{enumerate}
\item[(i)] $H \ge \mathbb{1}$: every family's eigenvalue is at least the bare ordering floor $1$, with equality along $c$ exactly when $\hat\Omega(c)\psi = 0$ and $(\Theta(c)a)\psi = 0$.
\item[(ii)] The floor is the identity, invariant under every unitary of face space; all family dependence of $H$, and in particular every splitting of the light pair, lies in $H - \mathbb{1} = W^{\dagger}W$, the Gram matrix of the explicit state vectors $\hat\Omega_{k}\psi$ and $(\Theta_{k}a)\psi$. (That $H - \mathbb{1}$ admits some Gram representation follows from (i) alone; the content here is the bound and the realising vectors.)
\item[(iii)] Splitting the normal-ordered part by the coherent vector $\omega_{k} = \langle\hat\Omega_{k}\rangle$, $W^{\dagger}W = \bar\omega\omega^{\mathsf{T}} + K + 2\mathcal{N}$ with $K_{kl} = \langle(\hat\Omega_{k} - \omega_{k})^{\dagger}(\hat\Omega_{l} - \omega_{l})\rangle$ and $\mathcal{N}_{kl} = \langle a^{\dagger}\Theta_{k}\Theta_{l}a\rangle$, each a Gram matrix: the rank-one outer square of the source plus a connected Gram part plus a number Gram part. In the Gaussian class $K = 2x^{2}P_{[\bar v]}$ and $2\mathcal{N} = x(\mathbb{1} + P_{[\bar v]})$, both along the coherent ray or family-blind, which is why the light pair stays degenerate there.
\end{enumerate}

## technical
The families paper's mass form, the symmetrised second moment of the three face operators, was evaluated in closed form only for Gaussian frozen vacua. This result treats every state of the six bosonic face modes. The canonical commutation relations split the symmetrised form into a constant unit matrix, the bare ordering floor, plus the Gram matrix of a linear map from face space into (two copies of) Fock space: one component is the face operator applied to the state, the other the pair operator's one-mode part.

So every family's mass-squared in these units is at least one in every state; the floor is identical for the three families and cannot distinguish them; and all family structure, including any splitting of the electron and muon, sits in the excess over the unit, the Gram matrix of explicit state vectors (any positive semidefinite excess has some Gram form; what is new is the bound and these vectors). That Gram square decomposes further into the outer square of the coherent vector (the democratic source term), a connected part and a number part; in the Gaussian class the last two are aligned with the coherent ray or family-blind, which is the mechanism behind the exact light-pair degeneracy there.

## lay
In the families paper the masses of the three generations come from how the vacuum fluctuates in three directions of an internal space. That paper computed this only for the simplest class of vacua, the Gaussian ones, where two generations come out exactly equal. This result looks at every possible vacuum and shows the mass pattern always has the same two-part shape: a fixed baseline, equal for all three generations, plus a part built as the square of something the vacuum determines. So any proposal to separate the electron from the muon has to do it entirely through that second part; the baseline can never help.

## one-liner
For every state of the six bosonic face modes the mass form is $H = \mathbb{1} + W^{\dagger}W$ with $W$ a state-dependent linear map from face space, so $H \ge \mathbb{1}$ in every state and every family splitting lies in the excess $W^{\dagger}W$.
