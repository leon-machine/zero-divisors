---
id: note.conformal.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: completion
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T02, deposited version
comments_on:
- conformal.nilpotent-ideal-becomes-unit-ideal
- conformal.minimal-nondegenerate-completion
locators:
  paper: T02
  number: Setting
  section: Machine verification
  line: 251
---

## formal
Every computational identity in this note has been checked by computer, in exact rational arithmetic over the shared library's basis-blade Clifford product, which admits degenerate generators, in the manner of the verifications deposited with \cite{ButlerT1, ButlerT4}. The script \texttt{verify\_T02.py}, deposited with this note alongside the series' shared exact-arithmetic library \texttt{GA.py}, \cite{ButlerVerifyT02}, performs its checks and reports each: the radical ideal of $\Cl(3,0,1)$ (dimension $8$, all $64$ ideal products zero: the corank-one, square-zero case of Proposition \claimref{conformal.nilpotent-ideal-becomes-unit-ideal}); the nilpotency profile at corank two in $\Cl(2,1,2)$ (ideal dimension $24 = 2^5 - 2^3$, a nonzero product in $J^2$, $\dim J^2 = 8$, and $J^3 = 0$, per Proposition \claimref{conformal.nilpotent-ideal-becomes-unit-ideal}); the model completions' Gram matrices (nondegeneracy by exact rank, signatures $(4,1)$ and $(4,3)$ by exact congruence diagonalisation, per Theorem \claimref{conformal.minimal-nondegenerate-completion}(2)); the embedding $e_0 \mapsto \nInf$ (isometry of the degenerate form on all pairs, algebra map on all $16 \times 16$ blade products, injectivity by exact rank); the unit-ideal identity $\nInf \nO' + \nO' \nInf = 1$ for the normalised partner; the translator dictionary (PGA translator composition $T_s T_t = T_{s+t}$ and its verbatim image in $\Cl(4,1)$, including the sandwich action on a sample vector, checked to move the vector, so the check is not vacuous); and the radical-pairing injectivity instance of the minimality argument. No floating point is used anywhere; the script exits nonzero on any failure, and all checks pass.

## technical
pending

## lay
pending

## one-liner
pending
