---
id: note.simulations.setting-colliding-share
kind: note
version: 1
title: The colliding share
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
- simulations.imported-bullet-cluster
- simulations.merger
locators:
  paper: T14b
  number: Setting
  section: Self-interaction within a sheet
  line: 228
  subsection: The colliding share
---

## formal
If collisional dark matter were held back in a merger as completely as the gas is, the share of the dark matter that collides would bound the subcluster's mass loss, whatever its cross-section. As a heuristic, then, by \eqref{eq:shares}:
\[
\text{(W): } f_{\mathrm{mirror}} + f_{3\mathrm{D}} = 68.3\%, \qquad
\text{(C): } f_{\mathrm{mirror}} = 18.6\%, \qquad
\text{mixed count: } 50.3\%,
\]
against a mass loss of at most $23$ percent (Fact \claimref{simulations.imported-bullet-cluster}). These are shares of the dark matter, as T14 counts them, so the bound is read as a bound on the subcluster's dark matter, its gas having been stripped in any case. Counted with the subcluster's own gas ($13.7$ percent of its mass: the baryon fraction $0.157$ less the $2$ percent in galaxies), the colliding fraction of its mass is $0.137 + 0.843\,f$, with $f$ the colliding share of the dark matter above: $71$ percent in (W), $29$ in (C) and $56$ in the mixed count, and on that count reading (C) is above the bound as well. T14 \cite[Rem.~7.10, Prop.~7.15(v)]{ButlerT14} counts the self-interacting fraction as the three-dimensional towers alone (about half) and tests the mirror's $18.6$ percent separately; for a bound on mass loss the two add. The simulations of Section \ref{sec:results} test the heuristic, and it holds only roughly in either direction: colliding matter that partly passes through is held back less than its share (\texttt{rule\_par}), while a halo that puffs loses more than its share from a fixed aperture (Observation \claimref{simulations.merger}). Figure \ref{fig:fraction} shows the comparison.

## technical
pending

## lay
pending

## one-liner
pending
