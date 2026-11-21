---
id: note.geometry-first.ladder-needs-halves-set-bit
kind: note
version: 1
title: The ladder needs halves to set a bit
status: example
subject: clifford-structure
proposed_by:
  kind: extraction
  session: notes-2026-11-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: idea, direction and review
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00a, deposited version
comments_on:
- synthesis.integer-clifford-algebras-contain-no-switch
locators:
  paper: T00a
  number: Ex F
  label: ex:halves
  line: 453
---

## formal
Send the two directions of $\Cl_{\Z}(1,1)$ to $e_{+}$ and $e_{-}$ of Example~\claimref{note.geometry-first.switch-two-two-tables}. The element $\alpha + \beta e_{1} + \gamma e_{2} + \delta e_{1}e_{2}$, with integer coefficients, becomes
\[
\begin{pmatrix} \alpha + \delta & \beta - \gamma \\ \beta + \gamma & \alpha - \delta \end{pmatrix} .
\]
The exchange $e_{+}$ is there, with $\beta = 1$. Setting the bit needs $\beta + \gamma = 1$ and $\beta - \gamma = 0$, so $\beta = \gamma = \tfrac12$; the test for on needs $\alpha = \tfrac12$ and $\delta = -\tfrac12$. Over the integers the ladder can exchange the two states but can neither set the bit nor test it. With halves it can do both, and $\tfrac12(e_{1} + e_{2})$, $\tfrac12(e_{1} - e_{2})$ is the switch of Theorem~\claimref{synthesis.integer-clifford-algebras-contain-no-switch}(iii).

## technical
pending

## lay
pending

## one-liner
pending
