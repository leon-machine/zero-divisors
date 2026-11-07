---
id: note.descent-lift.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: descent
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: consistency pass, bare imaginary unit written as I_4
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- descent-lift.imported-pinching-one-way-door
- descent-lift.imported-thouless-states-witt-vacua
- descent-lift.lift-costs-one-rung-per-mode
- descent-lift.imported-stinespring-kraus-choi
locators:
  paper: T05-descent-lift
  number: Setting
  section: Machine verification
  line: 316
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: "The Part D description wrote the Hermitian quartic element with a bare i; it is now I_4, the unit the stored proposition descent-lift.within-supplied-dynamics-descent-has-no uses (it commutes with the rung mode operators and with N_0), a pure notation change."
---

## formal
Every computational identity asserted in this note has been verified in exact arithmetic by the script \texttt{verify\_T05\_dilation.py} \cite{ButlerVerifyT05dilation}, which imports the series' shared library \texttt{GA.py}: its Gaussian rationals and its exact ranks. Irrational normalisations are avoided by working with unnormalised isometries, $W^{\dagger}W = 2^{\nu-1}$, and unnormalised record states; the reduced state of a subsystem is computed as the restriction of the joint state to the subsystem's algebra, with the operators $\ket{Y}\bra{X}_{S}$ built from the system's ladder operators, and the tensor-product partial trace is used only as a cross-check on even records. No floating point is used anywhere; the script exits nonzero on any failure. Thirty-four checks, all passing, in eight parts. The two pre-registrations are deposited beside the script \cite{ButlerPreregT05dilation, ButlerPreregT05pairing}.

\emph{Part A: the channel.} The product of the two parity averages equals the joint-number-diagonal pinching on all sixteen matrix units of the pair and is idempotent on a random matrix; on the even sector it equals $\tfrac12(\rho + \G_{0}\rho\G_{0}) = \tfrac12(\rho + \G_{1}\rho\G_{1})$, with Choi rank $2$ there and $4$ on the full space; the descent of the thermofield pair is $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$ with coherence $\tfrac{12}{25}$ removed; on one mode the even sector is the vacuum line and the descent is the identity on it.

\emph{Part B: the record.} The even sector of $k$ rungs has $2^{k-1}$ basis states for $k \leq 4$; Stinespring's one-rung map and the occupation copy both induce the descent on the even sector and both fail evenness, the first producing a parity-mixed joint state from the vacuum, the second an odd joint state from $\ket{11}$.

\emph{Part C: the lift of the pair.} $W = 1 \otimes \ket{00} + \G_{0} \otimes \ket{11}$ is even, has $W^{\dagger}W = 2$ with $W\ket{00} \perp W\ket{11}$, and induces $2\EN$ on the even sector's matrix units; the tensor-product partial trace agrees with the algebraic restriction on the lifted states; $C = 1 - 2P^{R}_{11}N_{0}$ is diagonal, equals $1 - \tfrac14(1-\G_{0})(1-\G_{2})(1-\G_{3})$, commutes with every $N_{k}$ and the total parity, squares to $1$; and $W = C(\,\cdot \otimes \varphi)$ on both even basis states and on the pair.

\emph{Part D: the preparation.} $\varphi$ is even and a Witt vacuum with Thouless amplitude $1$; the hops, the annihilation and the Cartan elements annihilate the record vacuum while the pair creation carries it to $\ket{11}$; the rational pairing rotor is unitary, even, and carries $\ket{00}$ to $\tfrac35\ket{00} + \tfrac45\ket{11}$; ten number-conserving generators commute with the total number, and the enumeration of joint basis states at the required number and parity leaves only the record vacuum for both even system states; a beam splitter between the pair and a rung at $(\tfrac35, \tfrac45)$ moves weight $\tfrac{16}{25}$ out of $\ket{11}$; the system pairing $1 + (a^{\dagger}_{0}a^{\dagger}_{1} - a_{1}a_{0})$, conjugated by the two system-record swaps and followed by $C$, is an even map inducing $2\EN$ on the even sector; the annihilation $a_{2}a_{3}$ kills the record vacuum while its Hermitian completion $a_{2}a_{3} + a^{\dagger}_{3}a^{\dagger}_{2}$ carries it to $\ket{11}$; the quartic element $I_{4}N_{0}(a^{\dagger}_{2}a^{\dagger}_{3} - a_{3}a_{2})$ is Hermitian, even, kills the joint vacuum and fails to commute with the total number, and its rotation at $\pi/2$, entered in closed form, is a unitary, even map carrying $\psi \otimes \ket{00}$ to the two-rung occupation copy, which is even, induces $\EN$, and equals $W$ in the record basis $\ket{00} \pm \ket{11}$.

\emph{Part E: the stored coherence.} The lifted pair is pure and even; its pair marginal is the classical shared bit and equals the descent; the marginal of each of the two modes is $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$; the record marginal has trace $1$ and determinant $\tfrac{144}{625}$; the lifted state equals $c\ket{00}\ket{+} + s\ket{11}\ket{-}$; the partial-lift factors $1, \tfrac{7}{25}, 0, -\tfrac{7}{25}$ at $A = 0, \tfrac34, 1, \tfrac43$.

\emph{Part F: the classical records.} The even mixture on the record pair with the coupling $C$ induces the descent exactly and leaves the joint output at purity $\tfrac12$; a single rung in the maximally mixed state with the coupling $1 - 2P^{R}_{1}N_{0}$ does the same, its joint output commuting with the total parity.

\emph{Part G: three modes.} On the even sector of three modes the pinching has Choi rank $4$; the even sector of three rungs has dimension $4$ and of two rungs $2$; the four record states are even and orthonormal (each pair checked); $W$ is even with $W^{\dagger}W = 4$ and induces $4\EN$ on the sixteen even matrix units; the record preparation is an even Witt vacuum with all three amplitudes $1$.

\emph{Part H: the pairing creator under the transport algorithm.} In $\Cl(2,2)$ over the rationals: $n = f_{1}^{*}f_{2}^{*}$ is nonzero, pure grade $2$, square zero, the centre is the scalars, $f_{2}^{*}f_{2}$ and $f_{1}^{*}f_{1}$ are non-central idempotents with $n\,f_{2}^{*}f_{2} = 0$ and $f_{1}f_{1}^{*}n = 0$, and the annihilating idempotents $f_{2}f_{2}^{*}$ and $f_{1}^{*}f_{1}$ are $wv$ and $vw$ for the grade-one null pairs $(f_{2}^{*}, f_{2})$ and $(f_{1}^{*}, f_{1})$ with $vw + wv = 1$; the Fock adjoint is an anti-automorphism exchanging $f_{k}$ and $f_{k}^{*}$, and $n^{\dagger} = f_{2}f_{1}$ satisfies the four Penrose equations with $n$ and kills $P_{00}$; $f \wedge f^{*}$ squares to $\tfrac14$ and commutes with the number operator; the reflection $e_{4} \mapsto -e_{4}$ is an automorphism carrying $h$ to $n$, $X_{h}$ to $X_{p}$, $P_{00}$ to $P_{01}$, $P_{\mathrm{odd}}$ to $P_{\mathrm{even}}$ and the hop rotor to the pairing rotor; $X_{p} = \tfrac12(e_{1}e_{2} + e_{3}e_{4})$ and $X_{h} = \tfrac12(e_{1}e_{2} - e_{3}e_{4})$, $X_{p}^{2} = -P_{\mathrm{even}}$, $X_{h}^{2} = -P_{\mathrm{odd}}$, $X^{3} = -X$, both closed-form exponentials at $(\tfrac35, \tfrac45)$ are even with $R\widetilde{R} = 1 = RR^{\dagger}$, the pairing rotor carries $P_{00}$ to $\tfrac35P_{00} + \tfrac45 nP_{00}$ and the hop rotor fixes it; $nn^{\dagger} + n^{\dagger}n = P_{\mathrm{even}}$ with $P_{\mathrm{even}} + P_{\mathrm{odd}} = 1$; and the pinching of either rung erases $n, h, X_{p}, X_{h}$ and fixes $\sigma_{1}, \sigma_{2}, \sigma_{1}\sigma_{2}$.

What the script does not check: Facts \claimref{descent-lift.imported-pinching-one-way-door} to \claimref{descent-lift.imported-thouless-states-witt-vacua} (imports); clauses (i) to (iii) of Theorem \claimref{descent-lift.lift-costs-one-rung-per-mode} beyond $\nu = 2, 3$ and clauses (iv) and (v) beyond $\nu = 2$ (the proofs are by counting and by Fact \claimref{descent-lift.imported-stinespring-kraus-choi}); the coefficient argument in the proof of Proposition \claimref{descent-lift.within-supplied-dynamics-descent-has-no}, of which the script checks one annihilation and the one quartic exception; and, in Proposition \claimref{descent-lift.pairing-creator-under-transport-algorithm}, the imported taxonomy of Fact \claimref{descent-lift.imported-taxonomy-type-p-rule-algorithm} and the identity $XP = X$, which follows from $X^{3} = -X$.

## technical
pending

## lay
pending

## one-liner
pending
