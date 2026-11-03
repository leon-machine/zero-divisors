---
id: note.transport.setting-null-vectors-zero-divisors-hyperbolic-2
kind: note
version: 1
title: Null vectors, zero divisors, and hyperbolic planes
status: setting
subject: zero-divisors
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.noinverse
- transport.totality
locators:
  paper: T01
  number: Setting
  section: Setting, and the classical facts the proofs use
  line: 462
  subsection: Null vectors, zero divisors, and hyperbolic planes
---

## formal
Null vectors are moreover two-sided zero divisors. The obstruction they pose is packaged in the reciprocal map
\[
\rho : \mathbb{V} \setminus \{Q = 0\} \to \mathbb{V}, \qquad \rho(x) = x / Q(x),
\]
which is partial exactly on $\{Q = 0\}$, the null cone together with the origin. Both failure modes are resolved by the same completion (Theorem \claimref{transport.totality}); only the null cone poses the element-level question of Section \ref{sec:nogo}, the pseudo-inverse condition being vacuous at the origin.

Null vectors come in pairs. If $v$ is null and $Q$ is nondegenerate, there is a vector $a$ with $v \cdot a \neq 0$; rescaling so that $v \cdot a = \tfrac12$ and setting $w = a - Q(a)\,v$ gives
\[
Q(w) = Q(a) - 2\,Q(a)\,(v \cdot a) = 0, \qquad v \cdot w = v \cdot a = \tfrac12 :
\]
a \emph{hyperbolic pair} $(v, w)$. The plane $H = \mathrm{span}\{v, w\}$ is a \emph{hyperbolic plane}: its Gram matrix on $(v,w)$ has determinant $-\tfrac14$, so $H$ is nondegenerate of signature $(1,1)$, and conversely every two-dimensional nondegenerate space containing a null vector is isometric to $H$ \cite{Lam2005}. Inside the Clifford algebra a hyperbolic pair satisfies
\begin{equation}
v^2 = w^2 = 0, \qquad vw + wv = 1, \qquad \text{hence} \quad vwv = (1 - wv)v = v .
\end{equation}
The last identity says $w$ is a \emph{pseudo-inverse} of $v$ in the sense of von Neumann: division by $v$ cannot be undone exactly, but $w$ undoes it up to the defect of $v$. This is the weakened form of inversion around which Section \ref{sec:nogo} revolves.

## technical
pending

## lay
pending

## one-liner
pending
