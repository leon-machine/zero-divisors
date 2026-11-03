---
id: note.simulations.setting-measurements-3
kind: note
version: 1
title: Measurements
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
  section: Measurements
  line: 393
---

## formal
\textbf{Quantities measured.} At that moment, projected along $z$ on a $10$ kpc grid smoothed by $25$ kpc:
\begin{itemize}
\item \emph{galaxy peak}: the maximum of the subcluster's galaxies within $150$ kpc of its centre;
\item \emph{lensing contrast}: projected total mass at the galaxy peak divided by the main cluster's azimuthal median at the same radius from its own peak; a value near $1$ means the subcluster has no separate lensing peak;
\item \emph{mass-peak offset}: the signed distance along the motion from the galaxy peak to the nearest local maximum of projected mass within $300$ kpc of it and more than $250$ kpc from the main cluster's peak, positive when the mass peak leads the galaxies; offsets below $10$ kpc are within one grid cell;
\item \emph{gas offset}: the distance along the motion from the galaxy peak to the maximum of our gas weighted by $m\rho$ (an X-ray proxy) within $450$ kpc of it and more than $200$ kpc from the main cluster's peak;
\item \emph{own mass}: the subcluster's own particles within $150$ kpc of its galaxy peak, relative to the same quantity in the CDM run at CDM's Bullet-like moment ($t = 1.12$; the half-resolution runs against \texttt{cdm\_lo} at $t = 1.10$);
\item \emph{galaxy concentration}: the subcluster's galaxy mass within $150$ kpc of its galaxy peak, relative to that within $150$ kpc of its centre at $t = 0$;
\item \emph{mass-to-light change}: total over galaxy mass within $150$ kpc apertures on the subcluster's galaxy peak and the main cluster's mass peak, $(M/L)_{\mathrm{sub}}/(M/L)_{\mathrm{main}}$, divided by the same ratio at $t = 0$.
\end{itemize}
Randall et al.\ measure the mass-to-light ratio itself; the division by its value at $t = 0$ removes the sampling offset of the initial conditions. Only $94$ to $100$ (subcluster) and $81$ (main cluster) galaxy particles fall in the two apertures, among about $4900$ and $3700$ particles in all, so at $t = 0$ the ratio is $1.086$ in reading (C) and $1.146$ in CDM rather than $1$ (\file{ml\_baseline.py}, from the fixed-seed initial conditions). The ratio at either epoch carries a Poisson error of about $15$ percent from those counts; the change, a ratio of two such, carries at least that and up to about $21$ percent, about twice to two and a half times the observational error ($0.07/0.84 = 8$ percent).

## technical
pending

## lay
pending

## one-liner
pending
