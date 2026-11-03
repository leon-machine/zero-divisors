---
id: scrambling.imported-time-plane-modular-data
kind: claim
version: 1
title: 'Imported: time and the plane from modular data'
status: imported
region: scrambling
subject: descent
tags: [classical-theorem, modular-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
imported_from:
- citation: J. J. Bisognano and E. H. Wichmann, On the duality condition for quantum fields, J. Math.
    Phys. 17 (1976), 303--321.
  key: BisognanoWichmann1976
- citation: H.-W. Wiesbrock, Half-sided modular inclusions of von Neumann algebras, Commun. Math. Phys.
    157 (1993), 83--92.
  key: Wiesbrock1993
locators:
  paper: T08
  number: Fact 5.1
  label: fact:modular2d
  line: 851
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: external import; no edges to review
---

## formal
The modular flow of a wedge algebra in the vacuum implements the boost: the timelike direction is recoverable from modular data (Bisognano-Wichmann). One half-sided modular inclusion recovers the two-dimensional conformal structure (Wiesbrock). \emph{Provenance:} \cite{BisognanoWichmann1976} (the duality theorem) and \cite{Wiesbrock1993} (the main theorem); both at assembly level for the present use.

## technical
For the algebra of a wedge in the vacuum, the modular flow implements the boost that preserves the wedge (Bisognano and Wichmann), so the timelike direction can be recovered from modular data alone. A single half-sided modular inclusion of von Neumann algebras recovers the two-dimensional conformal structure (Wiesbrock). Both results are used here at the level of the assembled algebras.

## lay
In quantum field theory, the vacuum restricted to a wedge-shaped region of spacetime comes with an intrinsic time evolution, and a classic theorem shows that it is exactly the boost preserving the wedge. So the direction of time can be read off from the algebra and the state alone. A related theorem recovers the whole two-dimensional plane of time and one space direction from a particular nesting of two algebras.

## one-liner
Imported: the modular flow of a wedge algebra in the vacuum is the boost (Bisognano-Wichmann), and one half-sided modular inclusion recovers the two-dimensional conformal structure (Wiesbrock).
