---
id: one-relation.imported-square-roots-real-clifford-algebras
kind: claim
version: 2
title: 'Imported: square roots of $-1$ in real Clifford algebras'
status: imported
region: one-relation
subject: clifford-structure
tags: [pseudoscalar-and-centre, classification, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, citation typos (author name, publisher)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: typed
imported_from:
- citation: E. Hitzer, R. Ablamowicz, and S. J. Sangwine, Square roots of $-1$ in real Clifford algebras,
    in Quaternion and Clifford Fourier Transforms and Wavelets, Birkhaeuser (2013) 123--153.
  key: HitzerAblamowiczSangwine2013
locators:
  paper: T16
  number: Fact 2.8
  label: fact:roots
  line: 534
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Citation typos: the second author is Ablamowicz (the technical level already spelled it so), and a lost backslash left Birkh"auser, written Birkhaeuser.'
  env: fact
  context_refs:
  - one-relation.odd-square-roots-chiral-phase
  typing:
    by: ai-typing-pass
    note: 'Imported fact, no derivation edges; the source marks it as context for, not a step of, the
      odd square-roots lemma. Levels pass: conditions already kept.'
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: 'Classical classification stated for orientation: the odd square-roots lemma proves the case it needs directly and cites this Fact as context, not as a step, and no store definition concerns it.'
---

## formal
The square roots of $-1$ in a real Clifford algebra $\Cl(p,q)$ are classified: they fall into finitely many conjugacy classes under the group of invertible elements, distinguished by the trace-like invariants of the algebra's matrix representation, and in $\Cl(1,3) \cong \Mat(2, \mathbb{H})$ every square root of $-1$ is conjugate to one of a short list. \emph{Provenance:} \cite{HitzerAblamowiczSangwine2013}. Lemma \claimref{one-relation.odd-square-roots-chiral-phase} below proves the odd case of $\Cl(1,3)$ directly, the general classification being context and not a step of the proof.

## technical
Imported from Hitzer, Ablamowicz and Sangwine: the square roots of $-1$ in a real Clifford algebra $\Cl(p,q)$ fall into finitely many conjugacy classes under the group of invertible elements, distinguished by trace-like invariants of the algebra's matrix representation, and in $\Cl(1,3) \cong \Mat(2,\HH)$ every square root of $-1$ is conjugate to one of a short list.

The source uses the general classification as context only; the odd case in $\Cl(1,3)$ that it needs is proved there directly.

## lay
Among ordinary numbers, minus one has no real square root, and the complex numbers give it two. In a Clifford algebra there can be many, and this result from the literature sorts them into finitely many classes, where two roots in the same class differ only by a change of viewpoint. In the algebra of spacetime there is just a short list of classes.

## one-liner
The square roots of $-1$ in a real Clifford algebra fall into finitely many conjugacy classes, a short list in $\Cl(1,3) \cong \Mat(2,\HH)$.
