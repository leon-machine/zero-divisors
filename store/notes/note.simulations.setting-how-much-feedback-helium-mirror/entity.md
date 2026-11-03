---
id: note.simulations.setting-how-much-feedback-helium-mirror
kind: note
version: 1
title: How much feedback a helium mirror has
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
  section: The mirror in the Galaxy
  line: 564
  subsection: How much feedback a helium mirror has
---

## formal
A pure-helium star is a bare helium core. Helium stars collapse to iron cores from about $2.5\ \Msun$ \cite{Woosley2019}, form black holes above final masses of about $10$ to $12\ \Msun$ \cite{Woosley2019, Ertl2020}, and explode by pair instability from $64$ to $133\ \Msun$ \cite{HegerWoosley2002}. Taking $10^{50}$ erg from $2.5$ to $3\ \Msun$, $10^{51}$ erg from $3\ \Msun$ to the black-hole cut, none above it to $64\ \Msun$, and pair-instability energies rising from $10^{51}$ to $10^{53}$ erg, the energy per unit mass formed relative to ours ($1.08 \times 10^{49}$ erg/$\Msun$ for a Chabrier IMF \cite{Chabrier2003}, one core collapse per $93\ \Msun$) is given in Table \ref{tab:F}.
\centering \begin{tabular}{@{}lcccccc@{}}
\toprule
IMF shifted up in mass by & 1 & 3 & 5 & 7 & 10 & 30\\
\midrule
$F$, black holes above $12\ \Msun$ & 3.6 & 5.7 & 6.3 & 6.4 & 6.2 & 4.7\\
$F$, black holes above $30\ \Msun$ & 4.1 & 6.4 & 7.1 & 7.3 & 7.2 & 5.7\\
\bottomrule
\end{tabular}

\emph{The helium-star feedback factor $F$: supernova energy per unit stellar mass formed of a pure-helium population relative to ours, by the black-hole cut (rows) and the factor by which the IMF is shifted up in mass (columns); \file{imf\_table.py}.}

No shifted IMF exceeds $F \approx 7.3$. Our IMF's shape gives $3.6$ to $4.1$.

## technical
pending

## lay
pending

## one-liner
pending
