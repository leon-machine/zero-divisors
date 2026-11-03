---
id: note.primer.setting-machine-verification
kind: note
version: 1
title: Machine verification
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
- primer.splitting-along-hyperbolic-plane
- primer.twisted-adjoint-action
locators:
  paper: T00
  number: Setting
  section: Machine verification
  line: 585
---

## formal
Although this primer proves nothing new, its worked examples are computations, and the series' standard is that computations are machine-checked. The script \texttt{verify\_T00.py}, deposited alongside this paper, imports the series' shared exact-arithmetic library \texttt{GA.py} and verifies, in exact rational arithmetic with no floating point: the geometric-product identities of Example \claimref{note.primer.euclidean-plane}, including $(e_1e_2)^2 = -1$ and the complex-multiplication table of the even subalgebra; the dimension count $2^{n}$ for $n \leq 6$; the hyperbolic-pair identities of Example \claimref{note.primer.hyperbolic-plane}; the commutation rule $vx = \hat{x}v$ and the involution signs on all blades for $n \leq 5$; the reflection and rotor formulas of Section \ref{sec:rotors}, with the exact rational rotation of Example \claimref{note.primer.rotation-exactly} and the boost eigenvalue $(a-b)^{2}$ of Example \claimref{note.primer.boost-what-it-does-null-direction}; the pseudoscalar squares and centre dimensions behind the table of Section \ref{sec:clock}, exhaustively for $n \leq 6$; the conformal lift's nullity, metric faithfulness, and the total swap on the projective line, including $1/0 = \infty$; and the computational content of the toolkit: the splitting lemma's unique expansion and the injectivity of null multiplication (Lemma \claimref{primer.splitting-along-hyperbolic-plane}), and the twisted adjoint action's multiplicativity and reflection formula (Lemma \claimref{primer.twisted-adjoint-action}). Sixteen checks, all passing.

## technical
pending

## lay
pending

## one-liner
pending
