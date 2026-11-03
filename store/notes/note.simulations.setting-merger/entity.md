---
id: note.simulations.setting-merger
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
locators:
  paper: T14b
  number: Setting
  section: Initial conditions
  line: 361
  subsection: The merger
---

## formal
Modelled on the Bullet Cluster: a main cluster with $M_{200} = 1.5 \times 10^{15}\ \Msun$ and $c = 4$ ($60{,}000$ particles), and a subcluster with $1.5 \times 10^{14}\ \Msun$ and $c = 7$ ($20{,}000$ particles), separated by $2500$ kpc along $x$ with impact parameter $150$ kpc along $y$, closing at $1800$ km/s, in the centre-of-mass frame. The random-number seed is $7$ for every merger. The truncated masses are $2.29 \times 10^{15}$ and $1.97 \times 10^{14}\ \Msun$, so main-cluster particles carry $3.8 \times 10^{10}\ \Msun$ and subcluster particles $9.8 \times 10^{9}\ \Msun$. Every halo has baryons $0.1571$ of its mass (galaxies $0.020$, our gas $0.1371$) and dark matter $0.8429$, split by composition as in Table \ref{tab:comps}. The line of sight is $z$, perpendicular to the orbit.

\centering \begin{tabular}{@{}lllll@{}}
\toprule
Code & Mirror & 3D towers & 5D towers & Reading \\
\midrule
\texttt{cdm} & collisionless & collisionless & collisionless & reference \\
\texttt{rule} & gas $0.186$ & sheet fluid $0.497$ & collisionless $0.316$ & (W) \\
\texttt{mirror} & gas $0.186$ & collisionless & collisionless & (C) \\
\texttt{mixed} & gas $0.186$ & sheet fluid $0.316$ & collisionless $0.497$ & mixed count, (W) \\
\texttt{mixednm} & collisionless & sheet fluid $0.316$ & collisionless & mixed count, mirror settled \\
\texttt{rule1} & gas $0.186$ & one tower fluid $0.249$ & collisionless & one 3D tower collides \\
\texttt{rule1nm} & collisionless & one tower fluid $0.249$ & collisionless & as \texttt{rule1}, mirror settled \\
\bottomrule
\end{tabular}

\emph{Compositions run, as shares of the dark matter (\file{merger.py}). The orientation codes describe the sheets' normals: \texttt{random} (a random normal per particle), \texttt{perp} (all normals along the line of sight, perpendicular to the merger axis, so the axis lies in the sheets) and \texttt{par} (all normals along the merger axis). A run is named \emph{model\_orientation}; \texttt{mirror\_only} is model \texttt{mirror} with random normals, reading (C). Suffix \texttt{nm}: the mirror collisionless from the start; suffix \texttt{lo}: half resolution.}

The variants isolate one effect each. \texttt{mixed} is T14's mixed count with the mirror as gas. \texttt{mixednm} and \texttt{rule1nm} make the mirror collisionless from the start, so that only the sheet fluid collides and its effect is seen apart from the mirror gas's; \texttt{rule1} and \texttt{rule1nm} let only one of the two three-dimensional towers collide, halving the sheet fluid.

## technical
pending

## lay
pending

## one-liner
pending
