---
id: note.simulations.setting-films
kind: note
version: 1
title: The films
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
  section: The films
  line: 492
---

## formal
Both films are rendered from simulation snapshots by \file{render\_lib.py} \cite{ButlerSuppT14b}. Each layer is a projected map along the line of sight on a grid of $300$ cells across the field, smoothed by a Gaussian of $18$ kpc (gas) or $25$ kpc (total mass), placed on a log scale, and added in its own colour onto a dark ground: galaxies as individual points, our gas weighted by $m\rho\sqrt{u}$ (a bremsstrahlung proxy for the X-ray map), mirror gas, and total projected mass as contours (what lensing measures). In Film 1 the sheet fluid is drawn as solid green contours rather than a fill, since a green fill screen-blended over the pink gas reads as white. The colour scales are fixed from one snapshot and shared by every panel, so brightness can be compared across panels.

The films use the same initial conditions as the runs of Table \ref{tab:merger}, re-run with snapshots every $0.01$ time units ($9.8$ Myr). They reproduce the Bullet-moment measurements of Table \ref{tab:merger} within run-to-run noise (contrast $4.48$ against $4.74$ for (C), $0.92$ against $0.95$ for (W), $7.27$ against $7.50$ for CDM; mass-to-light change $0.79$ against $0.82$ for (C)), the differences coming from the shifted time steps.

## technical
pending

## lay
pending

## one-liner
pending
