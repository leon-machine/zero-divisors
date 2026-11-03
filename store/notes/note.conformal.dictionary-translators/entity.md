---
id: note.conformal.dictionary-translators
kind: note
version: 1
title: The dictionary, and the translators
status: example
subject: completion
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T02, deposited version
comments_on:
- conformal.principal-case
- conformal.minimal-nondegenerate-completion
locators:
  paper: T02
  number: Ex 3.2
  label: ex:dictionary
  line: 225
---

## formal
Write $e_0$ for PGA's degenerate generator and $e_1, e_2, e_3$ for the Euclidean ones. The completion adjoins one dual direction; in CGA conventions, take the null pair $\nInf, \nO$ with $\nInf^2 = \nO^2 = 0$ and $\nInf \cdot \nO = -1$, and embed
\[
e_0 \longmapsto \nInf, \qquad e_i \longmapsto e_i .
\]
This is an isometric embedding of the degenerate form ($\nInf$ is null and orthogonal to the $e_i$), hence induces the algebra embedding of Theorem \claimref{conformal.minimal-nondegenerate-completion}; the adjoined partner is $\nO$. Under it, PGA's translator by a vector $t$,
\[
T_t \;=\; 1 + \tfrac12\, e_0\, t \qquad (t = t^i e_i),
\]
maps to $1 + \tfrac12 \nInf t$, which is precisely CGA's translator \cite{DFM2007}. The embedding is an algebra map, so all motor compositions, exponentials of PGA bivectors, and sandwich actions are carried verbatim; what CGA adds (versors built from $\nO$: inversions, dilations, transversions) is exactly the content of the adjoined direction. The plane at infinity of PGA becomes the point at infinity's null direction of CGA, which is the geometric form of the pairing $\lambda$ in the minimality proof: the direction that paired with nothing in PGA is the direction that must pair with something in any completion.

## technical
pending

## lay
pending

## one-liner
pending
