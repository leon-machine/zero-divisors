---
id: note.simulations.setting-cooling
kind: note
version: 1
title: Cooling
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
  line: 529
  subsection: Cooling
---

## formal
Collisional-ionisation-equilibrium cooling for hydrogen and helium uses the rates of Katz, Weinberg and Hernquist \cite{KWH1996}, plus one term they omit, which matters only without hydrogen: collisional excitation of neutral helium from its ground state, with an effective collision strength of $0.15$; varied by a factor of three either way it changes the pure-helium curve only between about $2 \times 10^{4}$ and $10^{5}$ K and leaves the floor and the cooling times at the virial temperatures used unchanged. The metal-free curve reproduces Sutherland and Dopita's \cite{SutherlandDopita1993} ($\log\Lambda_{N} = -22.26$, $-23.25$, $-23.01$ at $10^{5}$, $10^{6}$, $10^{7}$ K, normalised to $n_{H}^{2}$). Metals add the Tozzi-Norman fit for $0.3\,Z_{\odot}$ \cite{TozziNorman2001}, converted from their $n_{e}n_{i}$ normalisation to $n_{H}^{2}$ by the factor $0.704/0.578$ that \file{cooling.py} uses ($0.704 = (X + Y/2)(X + Y/6)$, which counts the helium ions as $Y/6$; $0.578 = X^{2}$ for $X = 0.76$; for a fully ionised plasma of that $X$, $n_{e}n_{i} = 0.722\,(\rho/m_{p})^{2}$, which would change the metal term by $3$ percent and no conclusion), scaled linearly in $Z$ and, for a helium plasma, by electrons per gram. At equal density and equal virial velocity:
\begin{itemize}
\item metal-free helium cools $12$ to $94$ times more slowly than our metal-enriched gas at $V = 100$ to $200$ km/s, the Milky Way's hot halo;
\item $4$ to $6$ times more slowly if the mirror has enriched itself to the same metallicity;
\item as fast as ours in small early halos ($V \approx 30$ km/s), where He$^{+}$ line cooling dominates.
\end{itemize}
The residual hydrogen holds a cooling floor near $10^{4}$ K.

## technical
pending

## lay
pending

## one-liner
pending
