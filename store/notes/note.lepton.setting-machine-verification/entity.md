---
id: note.lepton.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: standard-model
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
comments_on:
- lepton.content-constituent-space
- lepton.self-conjugacy-forces-determinant-one-group
- lepton.what-self-conjugacy-says-about-thirteenth
- lepton.unit-action-cell-action
locators:
  paper: T12-lepton
  number: Setting
  section: Machine verification
  line: 314
---

## formal
Every computational identity asserted here is verified in exact arithmetic by the deposited script \cite{ButlerVerifyT12L}, \texttt{verify\_T12\_lepton.py}, which imports the series' shared library \texttt{GA.py}: seventeen checks, all passing, no floating point. They are: the hypercharge generator built as an exact matrix on each $\Con_{k}$ with weight $3 - 2k$, and the lattice residues (Proposition \claimref{lepton.content-constituent-space}(1), (4)); the $SU(3)$ contents of the halves and the dual weights $-(3-2k) = 3 - 2(3-k)$ (Proposition \claimref{lepton.content-constituent-space}(2), (3)); the $K$-weights $1 - k$, the dual $K$-weights $k - 1$, their disagreement at matching content, and the biconditional of Proposition \claimref{lepton.self-conjugacy-forces-determinant-one-group} on five subgroups $G$ encoded by their trivial central characters, the $k = 0$ test alone passing on $SU(2) \times U(3)$ while $k = 1$ decides; the twist by $(\det A)^{m}$, its weights under $\mathsf{y}$ and $K$, the values $Y_{L} = -\tfrac52, \tfrac32$ at $m = \mp 2$, and the closure of the shifted weight multiset under negation only at $m = 0$; the twelve components of the five-mode ledger with their duals, exactly one (the vacuum) self-dual and none of the constituents' duals present (Observation \claimref{lepton.what-self-conjugacy-says-about-thirteenth}); the ranks of the $SU(2)$-orbits of single-row states under the cell action ($k + 1$ for $k = 1, 2, 3$, computed in the wedge basis of $\Lambda^{k}\C^{6}$) and under the unit action ($2$), the cell weights $k$, and the full spans as ranks, $6, 9, 4$ against $6, 6, 2$ (Proposition \claimref{lepton.unit-action-cell-action}); the $(2,1)$ at weight $-3$ inside $(2,3) \otimes (3,\bar{3})$ as a dimension identity (Remark \claimref{note.lepton.operator-route-why-it-not-one}); and the two anomaly lists, $(0, 0, 0, 0)$ and $(\tfrac23, 0, 0, -\tfrac49)$, with the two lists conjugate in their free parts (Proposition \claimref{lepton.relative-handedness-slotted-free-sectors}). What the script does not check: the Facts, verified in their own papers' scripts; and the readings of Remark \claimref{note.lepton.what-was-assumed}, Observation \claimref{lepton.what-self-conjugacy-says-about-thirteenth} and Remark \claimref{note.lepton.what-kind-fact-relative-handedness}, which are not computations.

## technical
pending

## lay
pending

## one-liner
pending
