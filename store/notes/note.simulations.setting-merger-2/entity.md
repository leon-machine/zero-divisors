---
id: note.simulations.setting-merger-2
kind: note
version: 1
title: The merger
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
- simulations.merger
- simulations.imported-bullet-cluster
locators:
  paper: T14b
  number: Setting
  section: 'Results: mergers and halos'
  line: 411
  subsection: The merger
---

## formal
Table \ref{tab:merger} gives every merger run; Figure \ref{fig:merger} plots the three measurements that the observation constrains for the five main runs.

\centering  
\begin{tabular}{@{}lrrrrrr@{}}
\toprule
Run & sep.\ (kpc) & max sep.\ (kpc) & contrast & offset (kpc) & own / CDM & $M/L$ change \\
\midrule
\texttt{cdm} & 742 & 1083 & 7.50 & $-5$ & 1.00 & 0.87 \\
\texttt{cdm\_lo} & 723 & 1090 & 7.13 & $-45$ & 1.00 & 0.91 \\
\texttt{rule\_random} & 584 & 625 & 0.95 & $+15$ & 0.10 & dissolved \\
\texttt{rule\_random\_lo} & 514 & 526 & 0.90 & $-5$ & 0.08 & dissolved \\
\texttt{rule\_perp} & 376 & 501 & 0.81 & $+185$ & 0.12 & dissolved \\
\texttt{rule\_par} & 720 & 829 & 3.24 & $-15$ & 0.48 & 0.68 \\
\texttt{mirror\_only} & 729 & 835 & 4.74 & $-5$ & 0.57 & 0.82 \\
\texttt{mixed\_random} & 460 & 579 & 1.11 & $-15$ & 0.27 & dissolved \\
\texttt{mixed\_perp} & 542 & 600 & 1.26 & $-5$ & 0.16 & dissolved \\
\texttt{mixednm\_random} & 730 & 792 & 2.69 & $-25$ & 0.44 & 0.61 \\
\texttt{mixednm\_perp} & 711 & 759 & 1.83 & $-95$ & 0.30 & 0.67 \\
\texttt{rule1\_random} & 486 & 493 & 1.47 & $-25$ & 0.23 & dissolved \\
\texttt{rule1nm\_random} & 723 & 846 & 3.78 & $+25$ & 0.55 & 1.18 \\
\midrule
observed & 720 & & separate peak & 42\rlap{$^{\dagger}$} & & $0.84 \pm 0.07$\rlap{$^{*}$} \\
\bottomrule
\end{tabular}

\emph{The Bullet-like merger (Section \ref{sec:measure}): separation at the Bullet-like moment, maximum separation after closest approach up to $t = 1.3$ (the CDM run was followed to $1.5$; the runs at $1083$ to $1090$ and $759$ to $846$ kpc are still separating at $1.3$), lensing contrast, signed mass-peak offset from the galaxies (positive: the mass peak leads; below $10$ kpc is within one grid cell), the subcluster's own mass within $150$ kpc of its galaxies relative to CDM's, and the mass-to-light change since $t = 0$ (sampling error $15$ to $21$ percent). The own-mass column has no observed counterpart: Randall et al.'s $23$ percent bound on mass loss is inferred from the mass-to-light ratio, not from the mass inside a fixed aperture. Where the contrast is near or below $1$ there is no separate subcluster peak, and the offset (\texttt{rule\_perp}'s $+185$) locates the nearest mass maximum, not a subcluster's. ``Dissolved'': the subcluster no longer has a galaxy concentration, so the ratio does not measure what the observation measures. Each run is one realisation. Observed values from Fact \claimref{simulations.imported-bullet-cluster}; $^{\dagger}$the subcluster's lensing peak, within $1\sigma$ of its galaxy centroid, which is known to $22$ kpc; $^{*}$the observed value is the ratio itself, not a change.}

## technical
pending

## lay
pending

## one-liner
pending
