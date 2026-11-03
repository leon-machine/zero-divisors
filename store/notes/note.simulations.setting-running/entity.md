---
id: note.simulations.setting-running
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
  line: 766
  subsection: Running
---

## formal
From the top folder:
{ \begin{verbatim}
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python code/reproduce.py figures --deposited   # the note's figures from outputs/
python code/reproduce.py all --quick           # check the whole chain on small runs
python code/reproduce.py all                   # the note's runs, half a day to a day
python code/reproduce.py compare               # regenerated against deposited
\end{verbatim}}
The first run of \file{reproduce.py} redraws the eight figures from the deposited results in a few seconds; with the library versions above and the Computer Modern font they are identical, pixel for pixel, to the note's, and with other versions the data are the same and the typography may differ. The \texttt{--quick} option runs three small mergers ($4000$ particles), two small cluster assemblies and coarse films, and one disk scale of the Galaxy model, so that every stage can be checked in about half an hour; its numbers are not the note's, and it works in \file{work\_quick/}, so it never occupies the folders of the full runs. The \texttt{figures} stage draws from \file{work/outputs/}, takes any result not regenerated there from the deposited \file{outputs/}, and says which it used for each file. Stages can be run one at a time, in the order of Table \ref{tab:stages}; each needs only the ones before it, and \texttt{--threads} sets the number of OpenMP threads for \file{tpsim} (default $2$, as in the note). A merger run that has finished is skipped if the stage is started again.

\centering \begin{tabular}{@{}l>{ \arraybackslash}p{0.48\textwidth}>{ \arraybackslash}p{0.24\textwidth}@{}}
\toprule
Stage & What it runs & Time on 2 cores \\
\midrule
\texttt{build} & compiles \file{tpsim.c} & seconds \\
\texttt{tests} & the two code tests of Section \ref{sec:code}, at full size even with \texttt{--quick} & $5$ to $10$ min \\
\texttt{mergers} & the $13$ merger runs of Table \ref{tab:merger} to $t = 1.3$ & $15$ to $60$ min each (CDM fastest, reading (W) slowest) \\
\texttt{halos} & the $13$ assembly runs ($4000$ particles per progenitor, $t = 2.0$, seeds $11$ and $23$) & $5$ to $25$ min each \\
\texttt{measure} & \file{analyze3.py}, \file{halo\_measure.py}, \file{proj\_ell.py}, \file{pk.py} & minutes \\
\texttt{films} & three re-runs with snapshots every $0.01$, then both films & $15$ to $60$ min per run, plus a few minutes' rendering \\
\texttt{galaxy} & both disk scales of the Galaxy model, the pass counts, the $F$ table (Table \ref{tab:F}) & about $25$ min \\
\texttt{small} & \file{sheet\_sidm.py}, \file{scatter2d.py}, \file{mirror\_cosmo.py}, \file{imf\_feedback.py}, \file{ml\_baseline.py} & under a minute \\
\texttt{figures} & \file{make\_figs.py} on \file{work/outputs/} & seconds \\
\texttt{compare} & prints regenerated against deposited numbers & seconds \\
\bottomrule
\end{tabular}

\emph{The stages of \file{reproduce.py}.}

## technical
pending

## lay
pending

## one-liner
pending
