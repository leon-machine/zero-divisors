---
id: note.geometry-first.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-11-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: idea, direction and review
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00a, deposited version
comments_on:
- synthesis.signed-directions-and-the-integer-clifford-algebra
- synthesis.completion-recovers-the-real-clifford-algebras
- synthesis.frobenius-and-universality-in-clifford-algebras
- synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane
locators:
  paper: T00a
  number: Setting
  section: Machine verification
  line: 599
---

## formal
The computations of this note are checked by the script \texttt{verify\_T00a.py}, deposited alongside it, which imports the series' shared exact-arithmetic library \texttt{GA.py} and works in exact rational arithmetic, with no floating point anywhere. A model of premise (F2) is built for every signature with $n \leq 4$, which shows the premise is consistent, and the formulas of Theorem \ref{thm:bitsign} for squares and commutators are compared with it; the blade product and the one rule of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} are compared with \texttt{GA.py}. For the completion step the script checks the inequalities of the square-root argument and the independence of $(p,q,r)$ from the order of rejection (Theorem \claimref{synthesis.completion-recovers-the-real-clifford-algebras}), the reduction of Lemma \ref{lem:bitpoly}(b) on known examples, the square-root formula and the real coefficients of $g_{t}$ (Theorem \ref{thm:bitroots}), and the relations used in Theorem \claimref{synthesis.frobenius-and-universality-in-clifford-algebras}. The identities of Theorem \claimref{synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane}, the case analysis of Proposition \claimref{synthesis.switch-planes-on-a-two-state-space} over the rationals, Theorem \claimref{synthesis.integer-clifford-algebras-contain-no-switch} and the index of Remark \claimref{note.synthesis.two-orders-of-construction-ladder-and-switch} are checked on finite ranges of integers, the mod-$2$ identity exhaustively for $n \leq 3$. Proposition \ref{prop:pinching} is checked on the plain and the signed register for $n \leq 3$ over the integers, including the index of part (iv), with the statements that depend on the ring (the injectivity in (iv) and the two claims of Remark \ref{rem:joined}) checked over $\Z/2$, $\Z/3$, $\Z/4$ and $\Z/6$ for $n \leq 2$; its part (v) in $\Cl(n,n)$ for $n \leq 3$ with \texttt{GA.py}, and its part (vi) against \texttt{GA.py} for every choice of signs with $n \leq 3$. These searches support the proofs and do not replace them; the limiting arguments that use completeness are proved, not computed. The claims about the switch and their conditions of failure were registered before any of them was run (\texttt{preregistration\_bit\_switch.md}, deposited with this note); Proposition \ref{prop:pinching} was not registered in advance. Not checked by machine, their proofs being short and structural: the universal properties of Theorems~\claimref{synthesis.signed-directions-and-the-integer-clifford-algebra}(iii) and~\claimref{synthesis.completion-recovers-the-real-clifford-algebras}(iv), Lemma~\ref{lem:bitpoly}(a), Theorem~\ref{thm:bitroots}(iv), and the trace argument for bosons. Fifty-three checks for the results. The worked examples are checked by the same script, each as printed: the table of Example~\ref{ex:twobits} against Theorem~\ref{thm:bitsign}(iii), the squares and inverse of Examples~\ref{ex:onerule} and~\ref{ex:half}, the roots and Hamilton's relations of Example~\ref{ex:roots}, the tables of Examples~\ref{ex:tables} and~\ref{ex:halves} (with the uniqueness of the halves), and the pinching of Example~\ref{ex:pinch}; eight checks. Sixty-one checks in all, all passing.

## technical
pending

## lay
pending

## one-liner
pending
