---
id: note.simulations.setting-running-2
kind: note
version: 1
title: Running
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
  line: 799
  subsection: Running
---

## formal
\textbf{Single runs by hand.} Compile \file{tpsim} and copy it into the stage folder, then run from there:
{ \begin{verbatim}
mkdir -p work/bin work/sims
gcc -O3 -fopenmp -o work/bin/tpsim code/tpsim.c -lm
cp work/bin/tpsim work/sims/
cd work/sims
python ../../code/merger.py mirror random mirror_only
python ../../code/halo.py rule random rule_random_s2 4000 2.0 23
python ../../code/analyze3.py cdm mirror_only
\end{verbatim}}
\file{merger.py} takes a model, a sheet orientation and a run name, then optionally the particle numbers of the two clusters (default $60{,}000$ and $20{,}000$) and an end time (capped at $1.3$). The models are \texttt{cdm}, \texttt{rule}, \texttt{mixed}, \texttt{mixednm}, \texttt{rule1}, \texttt{rule1nm} and \texttt{mirror} (Table \ref{tab:comps}); the orientations are \texttt{random}, \texttt{perp} and \texttt{par}. \file{halo.py} takes a model, \texttt{random}, a run name, then particles per progenitor, end time and seed; the note's runs used $4000$, $2.0$ and seeds $11$ and $23$ (the defaults are $5000$, $2.5$ and $11$). \file{analyze3.py} measures the named merger runs and should be given \texttt{cdm} first, since own mass is relative to it. \file{tpsim} itself takes the initial-conditions file, an output prefix, the end time, the snapshot interval, the softening, the opening angle $\theta$, the cooling coefficient $A$, the energy floor, and optionally $\Delta t_{\max}$ and $h_{\min}$; the scripts pass $0.02$ (mergers) or $0.5$ (assembly), $15$, $0.7$, \texttt{ics.cooling\_A()}, \texttt{ics.u\_of\_T(1e4)}, $0.002$ and $10$.

## technical
pending

## lay
pending

## one-liner
pending
