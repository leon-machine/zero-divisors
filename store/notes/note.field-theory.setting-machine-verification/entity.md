---
id: note.field-theory.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: quantum-fields
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
comments_on:
- field-theory.orientation-relocated
locators:
  paper: FT
  number: Setting
  section: Machine verification
  line: 307
---

## formal
Every proposition above is established by exact computation in real geometric algebra, with the series' shared library \texttt{GA.py} (Fraction coefficients; Gaussian rationals only for bookkeeping); no floating point is used. The derivation scripts and their independent review scripts are:

\begin{tabularx}{\textwidth}{@{}lXrr@{}}
\toprule
Run & Derivation script & Checks & Review checks\\
\midrule
\texttt{qft\_2026-10-15} & \texttt{verify\_QFT.py} & 80 & 64\\
\texttt{twistor\_ga\_2026-10-16} & \texttt{verify\_TWGA.py} & 55 & 50\\
\texttt{ga\_second\_quantisation\_2026-10-16} & \texttt{verify\_GA2Q.py} & 19 & 25\\
\texttt{ga\_interactions\_2026-10-16} & \texttt{verify\_INT.py} & 20 & 31\\
\texttt{ga\_bosons\_2026-10-16} & \texttt{verify\_BOS.py} & 23 & 30\\
\texttt{ga\_photon\_fock\_2026-10-16} & \texttt{verify\_PHO.py} & 22 & 41\\
\texttt{ga\_gravity\_source\_2026-10-16} & \texttt{verify\_GRV.py} & 12 & 12\\
\texttt{ga\_sm\_chirality\_2026-10-16} & \texttt{verify\_SMC.py} & 12 & 15\\
\midrule
Total & & 243 & 268\\
\bottomrule
\end{tabularx}

The consolidated runner \texttt{verify\_FT.py} runs the eight derivation scripts from their folders and reports each count; all pass. Each run's findings file lists the checks by class (proof-carrying, near-immediate, controls, imports), records the review's findings and the corrections applied, and states what the checks do not show. All counts above are from runs in exact arithmetic on 15 and 16 October 2026.

## technical
pending

## lay
pending

## one-liner
pending
