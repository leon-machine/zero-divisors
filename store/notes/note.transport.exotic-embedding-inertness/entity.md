---
id: note.transport.exotic-embedding-inertness
kind: note
version: 2
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
comments_on:
- transport.classification-real-clifford-algebras
- transport.representation-independent-minimality-completion
locators:
  paper: T01
  number: Ex 4.20
  label: ex:exotic
  line: 999
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3 with U5: the complex entries of the standard embedding of H in Mat_2(C) (diag(i, -i) and the like) are written with I_5, the central pseudoscalar of Cl(2,3), which is the complex unit of its type Mat_4(C) (std-algebra.complexification-is-the-odd-extension, cited as a mention); Hamilton''s i, j, k are named units and stay. No bare imaginary unit remains, so the outside_ga declaration (bridge, for i only) is removed. Version kept at 2, already bumped in this pass.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (bridge): the standard embedding of H in Mat_2(C) is written with complex matrices (diag(i, -i) and the like), the matrix form of the classification Cl(2,3) = Mat_4(C) in which the note states the embedding.'
---

## formal
$\Cl(1,3) \cong \Mat_2(\HH)$ embeds unitally in $\Cl(2,3) \cong \Mat_4(\C)$, an algebra of \emph{half} the dimension of the completion $\Cl(2,4)$: the standard unital embedding $\HH \hookrightarrow \Mat_2(\C)$ ($1, i, j, k$, Hamilton's units, mapped to $I$, $\mathrm{diag}(I_5, -I_5)$, $\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$, $\begin{psmallmatrix}0&I_5\\I_5&0\end{psmallmatrix}$, the matrix entries read in $\mathrm{span}\{1, I_5\}$, the centre of $\Cl(2,3)$, whose pseudoscalar $I_5$ is its complex unit, Theorem \claimref{std-algebra.complexification-is-the-odd-extension}) applied entrywise gives $\Mat_2(\HH) \hookrightarrow \Mat_4(\C)$, and $\Cl(2,3)$ has type $\Mat_4(\C)$ by Theorem \claimref{transport.classification-real-clifford-algebras} ($d \equiv 7$). The embedding is genuine; it is also inert: the ambient quadratic space of $\Cl(2,3)$ is five-dimensional, and by Theorem \claimref{transport.representation-independent-minimality-completion} no normalised conformal chart of four-dimensional spacetime exists on its quadric. The algebra is big enough to contain $\Cl(1,3)$ and too small to resolve it: what a resolution needs is not space for the \emph{elements} but space for the \emph{points}, and points cost two dimensions in the exact balance $(+1,+1)$.

## technical
pending

## lay
pending

## one-liner
pending
