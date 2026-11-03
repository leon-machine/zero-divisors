---
id: note.simulations.setting-what-expect
kind: note
version: 1
title: What to expect
status: setting
subject: dark-matter
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
comments_on:
- simulations.mirror-galaxy
locators:
  paper: T14b
  number: Setting
  section: Running the code
  line: 813
  subsection: What to expect
---

## formal
Initial conditions are reproduced bit for bit: regenerated with the fixed seeds, all $26$ merger and assembly initial-conditions files match the SHA-256 checksums of the runs reported here, deposited as \file{outputs/ic\_sha256.txt}; from \file{work/sims},
{ \begin{verbatim}
sha256sum -c ../../outputs/ic_sha256.txt
\end{verbatim}}
\noindent checks them. The evolved runs are reproduced statistically, not bit for bit, since the OpenMP threads sum forces in a varying order and the time steps change with the snapshot spacing (Section \ref{sec:films}); the film re-runs show the size of the differences. The Galaxy model, the $F$ table, the mass-to-light baseline and the printed tables of Section \ref{sec:sidm} are deterministic and are reproduced exactly. The compiler's warnings about unused return values of \texttt{fread} are harmless.

## technical
pending

## lay
pending

## one-liner
pending
