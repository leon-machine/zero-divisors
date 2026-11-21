---
id: note.geometry-first.switch-two-two-tables
kind: note
version: 1
title: The switch as two-by-two tables
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
- synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane
locators:
  paper: T00a
  number: Ex E
  label: ex:tables
  line: 405
---

## formal
In the basis $s_{\mathrm{off}}, s_{\mathrm{on}}$, each column giving the image of a state,
\[
v = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \qquad
w = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad
vw = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}, \qquad
wv = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} .
\]
So $v^{2} = w^{2} = 0$ (setting twice gives nothing), $vw$ is the test for on and $wv$ the test for off, and $vw + wv = 1$. The sum and the difference are
\[
e_{+} = v + w = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
e_{-} = v - w = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},
\]
with $e_{+}^{2} = 1$ (exchanging the states twice changes nothing), $e_{-}^{2} = -1$, and $e_{+}e_{-} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$. No entry is a fraction.

## technical
pending

## lay
pending

## one-liner
pending
