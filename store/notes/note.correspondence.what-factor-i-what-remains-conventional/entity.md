---
id: note.correspondence.what-factor-i-what-remains-conventional
kind: note
version: 3
title: "What the factor $I_6$ is, and what remains conventional"
status: remark
subject: conformal-spacetime
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
comments_on:
- correspondence.reality-conjugation-twistor-form-factor
locators:
  paper: T09
  number: Rem 4.6
  label: rem:factori
  line: 556
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 kept (already raised in this pass). Penrose''s i in omega = ix pi, the last bare i, now stands only in the existing extraction.source_formal (the source writes i for I_6, the complex unit of CS, U5); the text names I_6 as the factor Penrose writes as his imaginary unit. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (bridge): the note sets Penrose''s i in omega = ix pi beside the factor I_6 of omega = I_6 x pi that it derives, in its source''s notation.'
  source_title: "What the factor $i$ is, and what remains conventional"
  source_formal: |-
    The $i$ in $\omega = ix\pi$ is thus derived: it is the anti-Hermiticity that reality of the chart point forces on the map $A$ relative to the twistor form, and it can be moved but not removed (a phase change of $\kappa$ rotates $\Sigma$ and $\hat x$ together). It does not encode the Lorentzian signature: both $2\det\hat x$ and $-2\det\hat x$ have Lorentzian signature on Hermitian $\hat x$, and which of them is the Minkowski form $\eta$ of Section \ref{sec:setting} is the choice of spin-frame normalisation in \cite{PenroseRindler86}. That normalisation is the one convention left in the reality dictionary; the paper does not use it. The classical global statement, that the $\Sigma$-null lines of $\PT$ form the whole real conformal compactification $\mathbb{PN}$ and not only its affine chart, is a point of contact here and is not needed \cite{Penrose1967, PenroseRindler86}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Converted the factor $i$ of the incidence relation to $I_6$, the twistor form to the invariant Hermitian form, and the null twistors to the null part of \\PCS. The phase change of $\\kappa$ is kept with the Fock model's scalar."
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "the factor $i$ of $\\omega = ix\\pi$: the conformal spinors unit $I_6$, set by the earlier pass; it stays distinct from the field theory unit $I_4$"
---

## formal
The factor $I_6$ in $\omega = I_6\hat x\pi$, the complex unit of $\CS$ and the factor Penrose writes as his imaginary unit, is thus derived: it is the anti-Hermiticity that reality of the chart point forces on the map $A$ relative to the invariant Hermitian form $\Sigma$, and it can be moved but not removed (a phase change of $\kappa$ rotates $\Sigma$ and $\hat x$ together). It does not encode the Lorentzian signature: both $2\det\hat x$ and $-2\det\hat x$ have Lorentzian signature on Hermitian $\hat x$, and which of them is the Minkowski form $\eta$ of Section \ref{sec:setting} is the choice of spin-frame normalisation in \cite{PenroseRindler86}. That normalisation is the one convention left in the reality dictionary; the paper does not use it. The classical global statement, that the $\Sigma$-null lines of $\PCS$, which lie in its $\Sigma$-null part (Penrose's $\mathbb{PN}$), form the whole real conformal compactification and not only its affine chart, is a point of contact here and is not needed \cite{Penrose1967, PenroseRindler86}.

## technical
pending

## lay
pending

## one-liner
pending
