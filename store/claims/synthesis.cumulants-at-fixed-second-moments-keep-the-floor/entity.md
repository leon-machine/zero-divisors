---
id: synthesis.cumulants-at-fixed-second-moments-keep-the-floor
kind: claim
version: 1
title: Higher cumulants added at the skeleton's second moments cannot lower the light floor
status: proved
region: synthesis
subject: generations
tags: [pairing-and-bogoliubov, no-go, mass-generation]
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
  - families.koide-class-crossing-fit-conclusion@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_number_gram_is_family_density
- kind: check
  ref: check.py::check_floor_at_fixed_second_moments
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.one-open-problem-three-forms
  - synthesis.face-mass-form-unit-plus-gram
extraction:
  open_problem: op.non-gaussian-completion
  note: Constructive route on op.non-gaussian-completion, testing the problem's own first attack (add the lowest non-Gaussian cumulant to the frozen vacuum with the skeleton held fixed). Read in the mass-squared reading of the mass form (the skeleton theorem's clause 2). Lepton masses as quoted in the store (PDG 2024, m_tau = 1776.93 +- 0.09 MeV). Complements, filed alongside, synthesis.light-pair-split-needs-broken-source-stabiliser (a split needs a second face-space structure breaking the source's stabiliser), which says when the pair can split; this says how large the change must be at fixed second moments.
---

## formal
Let $\hat\Omega_{k}$ and $H(\psi)$ be the face operators and mass form of Theorem \claimref{families.skeleton-rank-one-plus-ordering-shift}, with the decomposition $H = \mathbb{1} + \bar\omega\omega^{\mathsf{T}} + K + 2\mathcal{N}$ of Proposition \claimref{synthesis.face-mass-form-unit-plus-gram}(iii), and let $\rho_{kl} = \sum_{A}\langle a_{kA}^{\dagger}a_{lA}\rangle$ be the one-body family density, $n = \tr\rho$ the mean number of face quanta.
\begin{enumerate}
\item[(i)] (The number Gram is the family density.) $\Theta_{k}\Theta_{l} = \tfrac14\bigl(\delta_{kl}\mathbb{1} - e_{l}e_{k}^{\mathsf{T}} \otimes \mathbb{1}\bigr)$ on the six modes, so in every state $2\mathcal{N} = \tfrac12(n\mathbb{1} - \rho^{\mathsf{T}})$. Hence $H \ge \mathbb{1} + \tfrac12(n\mathbb{1} - \rho^{\mathsf{T}})$ and the lightest family has $\lambda_{\min}(H) \ge 1 + \tfrac12(n - \rho_{\max})$, $\rho_{\max}$ the largest eigenvalue of $\rho$: half the population outside the most occupied family direction. In the skeleton $n = 4x$ and $\rho^{\mathsf{T}} = 2x(\mathbb{1} - P_{[\bar v]})$, and the light floor $\cosh^{2}r = 1 + x$ is this bound with equality.
\item[(ii)] (The floor survives every cumulant.) Let $\psi$ be any state, Gaussian or not, whose one- and two-point functions $\langle a_{p}\rangle$, $\langle a_{p}a_{q}\rangle$, $\langle a_{p}^{\dagger}a_{q}\rangle$ are those of the skeleton at depth $x$. Then $\omega$ and $\mathcal{N}$ are the skeleton's, and
\[
H(\psi) \;=\; (1 + x)\,\mathbb{1} \;+\; (5x + 4x^{2})\,P_{[\bar v]} \;+\; K(\psi), \qquad K(\psi) \ge 0,
\]
so $H(\psi) \ge \cosh^{2}r\,\mathbb{1}$: no family lies below the skeleton's floor, and connected cumulants of any order can only raise masses. The Gaussian value $K = 2x^{2}P_{[\bar v]}$ is one point of the cone $K \ge 0$.
\item[(iii)] (What reaching the data then costs.) Reading $H$'s eigenvalues as masses squared (the skeleton theorem's reading), reproducing $(m_{e}, m_{\mu}, m_{\tau})$ with second moments held at the Koide depth $x^{*} = 769.3325$ (Proposition \claimref{families.koide-class-crossing-fit-conclusion}) needs $\lambda_{\tau} \ge (m_{\tau}/m_{e})^{2}(1 + x^{*}) > 9.31 \times 10^{9}$, against the skeleton's $1 + 6x^{*} + 6x^{*2} < 3.56 \times 10^{6}$, so by Weyl's inequality the largest eigenvalue of $K$ must exceed $\lambda_{\tau} - (1 + 6x^{*} + 4x^{*2})$, more than $7{,}860$ times the Gaussian $2x^{*2}$; and since $\lambda_{\mu} \ge (m_{\mu}/m_{e})^{2}(1 + x^{*})$, the second eigenvalue of $K$, zero in the skeleton, must exceed $\lambda_{\mu} - (1 + 6x^{*} + 4x^{*2}) > 3.05 \times 10^{7}$: the connected Gram matrix must acquire rank two at that size.
\end{enumerate}
So the problem's first route, adding the lowest non-Gaussian cumulant to the frozen vacuum with the skeleton held fixed, cannot reach the charged-lepton spectrum as a correction: the electron cannot be brought below the floor, which is a second-moment quantity (by (i), the population outside the dominant family direction), and the muon and tau must be raised by connected fluctuations thousands of times the Gaussian ones. A completion must instead change the second moments, concentrating the face quanta in the electron's family direction, which within the displaced-Gaussian class with free means is the relabelling of Proposition \claimref{families.classification-displaced-gaussian-class-solved-level}(3); the non-Gaussian structure is needed to cause that concentration, not to add on top of it.

## technical
The mass form of the face modes splits into the unit, the outer square of the coherent vector, a connected Gram matrix $K$ and a number Gram matrix $\mathcal{N}$. This result first identifies $2\mathcal{N}$ exactly: it is $\tfrac12(n\mathbb{1} - \rho^{\mathsf{T}})$, built from the one-body family density $\rho$ alone. So every family's mass squared is at least one plus half the number of quanta sitting outside that family's direction, and the lightest at least one plus half the population outside the most occupied direction. The skeleton's light floor $\cosh^{2}r$ is exactly this bound: its two light directions each hold $2x$ quanta, the heavy one none.

Second, fix the first and second moments at the skeleton's and add any higher connected cumulants. The coherent vector and the number Gram, both second-moment objects, stay put, and only $K$ moves, within the cone of positive semidefinite matrices. So the mass form never drops below $\cosh^{2}r$ times the unit: higher cumulants only raise masses.

With the masses read as square roots of the eigenvalues, the electron would then sit at least at the floor, and the measured ratios force the tau's eigenvalue above $9.3 \times 10^{9}$ at the Koide depth, about $2{,}600$ times the skeleton's, with the connected Gram matrix's top eigenvalue nearly eight thousand times its Gaussian size and a second eigenvalue above $3 \times 10^{7}$ where the skeleton has none. Adding the lowest cumulant is therefore not a perturbative route to the $207$; a completion has to move the second moments, putting the quanta in the electron's direction.

## lay
In the series the three charged-lepton families get their masses from a frozen quantum state of six modes, and the simplest (Gaussian) version of that state makes the electron and the muon exactly equally heavy. The open problem asks whether adding a small non-Gaussian ingredient could split them by the observed factor of about 207. This result shows that it cannot do so as a small correction. The lighter pair's common mass in the Gaussian state is fixed by how many quanta sit in the other family directions, and any extra non-Gaussian ingredient that leaves those numbers alone can only make every family heavier, never lighter. Reaching the real masses would then need the extra ingredient to be thousands of times larger than the Gaussian part. What has to change instead is where the quanta sit: almost all of them must be in the electron's direction, and the non-Gaussian structure would have to explain why.

## one-liner
The number part of the face mass form is $\tfrac12(n\mathbb{1} - \rho^{\mathsf{T}})$ (one-body family density), the skeleton floor $\cosh^{2}r$ saturates the bound it gives, and any state with the skeleton's second moments has $H \ge \cosh^{2}r\,\mathbb{1}$: cumulants only raise masses, so reaching $m_{\mu}/m_{e} = 207$ at the Koide depth needs the connected Gram matrix's top eigenvalue about $7{,}900$ times the Gaussian one and a new second eigenvalue above $3 \times 10^{7}$.
