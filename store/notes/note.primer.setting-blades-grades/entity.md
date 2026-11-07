---
id: note.primer.setting-blades-grades
kind: note
version: 2
title: Blades and grades
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
- name: Claude Opus 5.5
  role: 'consistency pass, stale count of where the degenerate dimension count is used'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- primer.commutation-rule
locators:
  paper: T00
  number: Setting
  section: Blades and grades
  line: 287
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Stale wording: the degenerate 2^n count is used by T1 twice (splitting lemma, null-generator ascent) and throughout T2 and T4 (std-algebra.blade-basis and its restatements), not exactly once.'
---

## formal
Fix an orthogonal basis $e_1, \dots, e_n$ of $\mathbb{V}$. Because orthogonal vectors anticommute and each $e_i^{2}$ is a scalar, any product of basis vectors can be reordered and reduced until each index appears at most once. The surviving products
\[
1, \quad e_i, \quad e_i e_j \ (i<j), \quad e_i e_j e_k \ (i<j<k), \quad \dots, \quad e_1 e_2 \cdots e_n
\]
are the \emph{basis blades}, and they form a linear basis of the algebra: one blade for each subset of the indices, hence
\[
\dim \Cl(\mathbb{V}, Q) \;=\; 2^{n} .
\]
This count holds even when $Q$ is degenerate \cite{Chevalley1997}, a fact T1 needs in an essential step (the splitting lemma, \claimref{primer.splitting-along-hyperbolic-plane}) and for its null-generator ascent, and that the degenerate algebras of T2 and T4 rest on throughout (\claimref{std-algebra.blade-basis}).

A blade built from $k$ distinct vectors has \emph{grade} $k$, and the grades are exactly the objects Section \ref{sec:product} built: scalars are grade 0, vectors grade 1, the bivectors grade 2, the trivectors grade 3, and so on up to the single top blade $\omega = e_1 e_2 \cdots e_n$, the \emph{pseudoscalar}, which represents the oriented volume of the whole space and is the top element that section's dependence argument located. Grade is basis-independent \cite{Porteous1995}, so the algebra splits into graded pieces, one for each dimension of geometric object it can represent: points of measure, directions, planes, volumes, and so on up to the space itself. The geometric product moves between the grades; the inner and outer products of Section \ref{sec:product} are its grade-lowering and grade-raising parts.

## technical
pending

## lay
pending

## one-liner
pending
