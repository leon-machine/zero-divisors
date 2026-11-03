---
id: note.simulations.setting-which-files-do-what
kind: note
version: 1
title: Which files do what
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
  line: 717
  subsection: Which files do what
---

## formal
Table \ref{tab:files} lists every file in the supplement's \file{code/} folder against the result it produces. Five files are libraries, imported by the others and not run on their own: \file{ics.py} (initial conditions and snapshot input and output, used by every simulation script), \file{render\_lib.py} (the films' maps), and \file{cooling.py}, \file{fastcool2.py} and \file{sam2.py} (the Galaxy model). \file{merger.py}, \file{analyze3.py} and \file{halo\_measure.py} are run and also imported. The verification script \file{verify\_T14b.py} sits at the suite's top level beside \file{GA.py}, which it imports.

\centering \begin{tabular}{@{}>{ \arraybackslash}p{0.3\textwidth}>{ \arraybackslash}p{0.36\textwidth}>{ \arraybackslash}p{0.26\textwidth}@{}}
\toprule
Result in the note & Files & Writes \\
\midrule
Self-interaction (Section \ref{sec:sidm}, Table \ref{tab:sidm}, Figure \ref{fig:sigma}) & \file{sheet\_sidm.py}, \file{scatter2d.py} & printed tables \\
The simulation code (Section \ref{sec:code}) & \file{tpsim.c}; \file{ics.py}; \file{tpsim\_tests.py} for the two code tests & snapshots, test output \\
The merger (Table \ref{tab:merger}, Figure \ref{fig:merger}) & \file{merger.py} (runs \file{tpsim}), \file{analyze3.py}; \file{ml\_baseline.py} for the mass-to-light ratio at $t = 0$ & \file{runs/<tag>/}, \file{summary3.json}, \file{ml\_baseline.json} \\
Cluster assembly (Table \ref{tab:halo}, Figure \ref{fig:halo}) & \file{halo.py} (runs \file{tpsim}), \file{halo\_measure.py}, \file{proj\_ell.py}; \file{pk.py} for the power spectrum & \file{halos/<tag>/}, \file{proj\_ell.json}, \file{pk\_output.txt}, \file{pk\_ratio.json} \\
The films and Figure \ref{fig:retention} & \file{compact.py}, \file{remeasure.py}, \file{merger\_movie.py}, \file{bullet\_moment.py}; \file{render\_lib.py} & frames, \file{track.json}, the two films \\
Mirror composition (Section \ref{sec:galaxy}) & \file{mirror\_cosmo.py} & printed table \\
Galaxy model (Observation \claimref{simulations.mirror-galaxy}, Figure \ref{fig:galaxy}) & \file{chem\_test2.py}, \file{verdict.py}; \file{sam2.py}, \file{cooling.py}, \file{fastcool2.py} & \file{chem2\_*.json}, pass counts \\
The factor $F$ (Section \ref{sec:galaxy}) & \file{imf\_table.py}; \file{imf\_feedback.py} for the energy brackets & printed tables \\
All figures & \file{make\_figs.py} & \file{T14b\_fig\_*.pdf} \\
All of the above, in order & \file{reproduce.py} & \file{work/} \\
\bottomrule
\end{tabular}

\emph{The files in \file{code/} and what each produces.}

## technical
pending

## lay
pending

## one-liner
pending
