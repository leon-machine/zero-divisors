---
id: note.angle.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: thermality
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-angle, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: consistency pass, the imaginary rapidity's unit written as I_5
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- angle.imported-singularity-papers-state-selection
- angle.imported-theorems-deliver-their-hypotheses
- angle.within-supplied-class-spectrum-condition-selects
- angle.value-parameter-dynamics
locators:
  paper: T05-angle
  number: Setting
  section: Machine verification
  line: 240
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Two bare imaginary units missed by the detector, (iB) and the endpoint iB, are written I_5 B with I_5 = I_4 e the central unit of Cl(2,3), as in angle.wedge-reflection-translations-are-ascent (ii), whose twisted action is the wedge reflection only for a unit commuting with every vector.'
---

## formal
Every computational identity asserted in this note has been verified in exact arithmetic by the script \texttt{verify\_T05\_angle.py} \cite{ButlerVerifyT05angle}, which imports the series' shared library \texttt{GA.py}: its blade engine for the geometric parts and its Gaussian rationals for the Fock parts. The reduced state of a subsystem is computed as the restriction of the joint state to the subsystem's algebra, the fermionic reduced state, so that no tensor-product identification is needed. No floating point is used anywhere; the script exits nonzero on any failure. Eighteen checks, all passing, in six parts. The pre-registration is deposited beside the script \cite{ButlerPreregT05angle}.

\emph{Part A: the boost plane.} $B = e_{t}e_{r}$ is a bivector of square $+1$; the rotor at $(\tfrac54, \tfrac34)$ has $R\widetilde{R} = 1$ and the stated boost matrix on $(e_{t}, e_{r})$, fixing the transverse vectors; $x \mapsto BxB$ is $-1$ on the plane and $+1$ transverse, with $B\widetilde{B} = -1$ so that $(I_{5}B)\widetilde{(I_{5}B)} = 1$, $I_{5} = I_{4}e$ the central unit of the odd extension $\Cl(2,3)$ (\claimref{std-algebra.complexification-is-the-odd-extension}); the reflection commutes with the boost and is an involution on vectors; the boost rescales $e_{t} + e_{r}$ by $\tfrac14$ and $e_{t} - e_{r}$ by $4$.

\emph{Part B: the translations.} $\nO$, $\nInf$ null with $\nO\cdot\nInf = -1$; $X(x)$ null and $X(x)\cdot X(y) = -\tfrac12 Q(x - y)$ on rational points; $T_{a}$ even, with the stated inverse, fixing $\nInf$, of the null-rotation form with $u = \tfrac12 a$ orthogonal to $\nInf$; $T_{a}X(x)T_{a}^{-1} = X(x + a)$ and $T_{a}X(x - a)T_{a}^{-1} = X(x)$; the base's boost rotor fixes $\nO$ and $\nInf$ and commutes with the lift.

\emph{Part C: the supplied class.} Random rational diagonal generators on two and three modes with every cut: diagonal in the number basis; for each unique ground state (at least three such draws asserted), a number state with rank-one idempotent marginals on both sides, an eigenvector of every $N_{k}$, and, for a single-mode side, no Gibbs parameter; the degenerate generator $(N_{0} - N_{1})^{2}$ with ground space $\operatorname{span}\{\ket{00}, \ket{11}\}$ annihilating both the thermofield pair and $\ket{00}$.

\emph{Part D: the hop.} $H$ Hermitian; the one-particle block $\begin{psmallmatrix} 7 & -12 \\ -12 & 0\end{psmallmatrix}$; the eigenvector $\tfrac35\ket{10} + \tfrac45\ket{01}$ at $-9$; sector energies $0$ and $7$ with no off-diagonal entries; trace and determinant giving $16$ and $-9$; the ground state odd, of norm one, with both marginals of rank two, the left $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$ at $q = \tfrac{9}{16}$ and the right $\operatorname{diag}(\tfrac{9}{25}, \tfrac{16}{25})$; an eigenvector of $N_{0} + N_{1}$ and not of $N_{0} - N_{1}$.

\emph{Part E: the particle-hole map.} $V$ unitary, Hermitian, an involution, fixing $a_{0}$ and exchanging $a_{1}$ with $a^{\dagger}_{1}$; $V\psi = \tfrac45\ket{00} + \tfrac35\ket{11}$, even, with left marginal $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$; $VHV^{-1}$ equal to the pairing generator entry by entry, with $V\psi$ its eigenvector at $-9$; $V(N_{0} + N_{1} - 1)V^{-1} = N_{0} - N_{1}$; in $\Cl(2,2)$ the reflection $e_{4} \mapsto -e_{4}$ is an automorphism (random elements) fixing $f_{1}$ and carrying $f_{2}$ to $f_{2}^{*}$ and the hop to the pairing.

\emph{Part F: the parameter.} At the seven rational points, with $tcs > 0$, the hop generator with $\varepsilon/t = (s^{2} - c^{2})/(cs)$ has $c\ket{10} + s\ket{01}$ as an eigenvector at $-tc/s$, the three gaps equal to $ts/c + tc/s$, $tc/s$ and $ts/c$ and positive, and left marginal Gibbs at $q = c^{2}/s^{2}$.

What the script does not check: Facts \claimref{angle.imported-singularity-papers-state-selection} to \claimref{angle.imported-theorems-deliver-their-hypotheses} (imports); the general-$\nu$ clause of Proposition \claimref{angle.within-supplied-class-spectrum-condition-selects}(i) beyond $\nu = 3$ (the proof is a statement about diagonal matrices); the uniqueness clause of Proposition \claimref{angle.value-parameter-dynamics} beyond the seven points (the proof is the two-by-two computation); the Gibbs clause of Proposition \claimref{angle.within-supplied-class-spectrum-condition-selects}(i) for sides of more than one mode (the rank argument); and the continuation to imaginary rapidity in Proposition \claimref{angle.wedge-reflection-translations-are-ascent}(ii), of which the script checks the endpoint $I_{5}B$ and its action.

## technical
pending

## lay
pending

## one-liner
pending
