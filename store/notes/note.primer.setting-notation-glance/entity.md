---
id: note.primer.setting-notation-glance
kind: note
version: 1
title: Notation at a glance
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
comments_on:
- primer.twisted-adjoint-action
locators:
  paper: T00
  number: Setting
  section: Notation at a glance
  line: 535
---

## formal
Every symbol below is introduced somewhere in this primer or in T1, but a reader should not have to search for the introduction. This table collects the symbols in one place. The section column names where the symbol is first explained; symbols marked T1 belong to that paper's own constructions and are listed here so that the whole series can be read with one table at hand.

\begin{center}
 \begin{tabular}{cl>{ \arraybackslash}p{7.0cm}c}
\toprule
Symbol & Name & What it means & Where \\
\midrule
$Q(v)$ & quadratic form & the squared length the geometry assigns to $v$; the algebra's one rule is $v^2 = Q(v)$ & \S\ref{sec:product} \\
$a \cdot b$ & inner product & the symmetric part of the product, $\tfrac12(ab + ba)$; $a \cdot b = 0$ says $a$ and $b$ are orthogonal & \S\ref{sec:product} \\
$a \wedge b$ & outer product & the antisymmetric part, $\tfrac12(ab - ba)$; the oriented plane spanned by $a$ and $b$ & \S\ref{sec:product} \\
$\Cl(p,q)$ & Clifford algebra & the algebra of a space with $p$ directions of square $+1$ and $q$ of square $-1$ & \S\ref{sec:signature} \\
$\Cl(\mathbb{V}, Q)$ & the same, by space & the algebra named by the specific space rather than its signature; the form used when $Q$ may be degenerate & \S\ref{sec:product} \\
$\omega$ & pseudoscalar & the top blade $e_1 e_2 \cdots e_n$, the oriented volume of the whole space & \S\ref{sec:blades} \\
$\hat{x}$ & grade involution & the sign $(-1)^k$ on grade $k$: fixes even grades, negates odd ones & \S\ref{sec:involutions} \\
$\tilde{x}$ & reversion & reverses the order of factors in any product of vectors; sign $(-1)^{k(k-1)/2}$ on grade $k$ & \S\ref{sec:involutions} \\
$\perp$ & orthogonal sum & $\mathbb{V} = A \perp B$: the space splits into two parts, every vector of one orthogonal to every vector of the other; $W^{\perp}$ is the set of vectors orthogonal to all of $W$ & \S\ref{sec:toolkit} \\
$\oplus$ & direct sum & an algebra falling into two independent blocks, multiplied componentwise; the two blocks annihilate each other & \S\ref{sec:clock} \\
$\cong$ & isomorphic & the same structure under a renaming of elements & \S\ref{sec:clock} \\
$\Mat_k(\mathbb{F})$ & matrix algebra & the $k \times k$ matrices with entries in $\mathbb{F}$ & \S\ref{sec:clock} \\
$\R,\ \C,\ \HH$ & the three fields & the real numbers, the complex numbers, and the quaternions & \S\ref{sec:clock} \\
$\Pin,\ \Spin,\ \Spin^0$ & the versor groups & normalised versors; their even part; its identity component & \S\ref{sec:rotors} \\
$\Ad_g,\ \tau_g$ & the twisted actions & how a versor $g$ moves vectors ($\Ad$) and general elements ($\tau$) & Lem.\ \claimref{primer.twisted-adjoint-action} \\
$n_0,\ n_\infty$ & origin and infinity & the null pair of the conformal model, representing the origin and the point at infinity & \S\ref{sec:conformal} \\
$X(x)$ & conformal lift & the null vector in the enlarged space that represents the point $x$ of $\mathbb{V}$ & \S\ref{sec:conformal} \\
$p - q \bmod 8$ & clock residue & the number that decides which entry of the classification table an algebra is & \S\ref{sec:clock} \\
$e^2 = e$ & idempotent & a projection; apart from $0$ and $1$, always a zero divisor & T1 \\
$v\sigma v = v$ & pseudo-inverse & the standard weakened substitute for an inverse when none exists & T1 \\
\bottomrule
\end{tabular}
\end{center}

## technical
pending

## lay
pending

## one-liner
pending
