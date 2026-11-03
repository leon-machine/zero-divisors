---
id: note.transport.exotic-embedding-inertness
kind: note
version: 1
title: An exotic embedding, and its inertness
status: example
subject: clifford-structure
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.classification-real-clifford-algebras
- transport.representation-independent-minimality-completion
locators:
  paper: T01
  number: Ex 4.20
  label: ex:exotic
  line: 999
---

## formal
$\Cl(1,3) \cong \Mat_2(\HH)$ embeds unitally in $\Cl(2,3) \cong \Mat_4(\C)$, an algebra of \emph{half} the dimension of the completion $\Cl(2,4)$: the standard unital embedding $\HH \hookrightarrow \Mat_2(\C)$ ($1, i, j, k$ mapped to $I$, $\mathrm{diag}(i, -i)$, $\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$, $\begin{psmallmatrix}0&i\\i&0\end{psmallmatrix}$) applied entrywise gives $\Mat_2(\HH) \hookrightarrow \Mat_4(\C)$, and $\Cl(2,3)$ has type $\Mat_4(\C)$ by Theorem \claimref{transport.classification-real-clifford-algebras} ($d \equiv 7$). The embedding is genuine; it is also inert: the ambient quadratic space of $\Cl(2,3)$ is five-dimensional, and by Theorem \claimref{transport.representation-independent-minimality-completion} no normalised conformal chart of four-dimensional spacetime exists on its quadric. The algebra is big enough to contain $\Cl(1,3)$ and too small to resolve it: what a resolution needs is not space for the \emph{elements} but space for the \emph{points}, and points cost two dimensions in the exact balance $(+1,+1)$.

## technical
pending

## lay
pending

## one-liner
pending
