---
id: hawking.imported-penrose-transform
kind: claim
version: 2
title: 'Imported: the Penrose transform'
status: imported
region: hawking
subject: thermality
tags: [classical-theorem, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
imported_from:
- citation: R. Penrose, Solutions of the zero-rest-mass equations, J. Math. Phys. 10 (1969), 38--39.
  key: Penrose1969
- citation: M. G. Eastwood, R. Penrose and R. O. Wells, Cohomology and massless fields, Commun. Math.
    Phys. 78 (1981), 305--351.
  key: EPW1981
locators:
  paper: T07
  number: Fact 5.1
  label: fact:penrose
  line: 571
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported literature result; no edges to review.
  source_title: 'Imported: the Penrose transform'
  source_formal: |-
    Massless free fields of helicity $s$ on (suitably convex regions of complexified) Minkowski space are in natural isomorphism with the first cohomology of the corresponding twistor-space region with coefficients in $\mathcal{O}(-2s-2)$: the homogeneity $-2s-2$ classifies the helicity-$s$ field. \emph{Provenance:} Penrose \cite{Penrose1969}; the sheaf-cohomological form \cite{EPW1981}.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the twistor-space region to a region of $\CS$ and named the complex unit of complexified Minkowski space as $I_4$. The transform itself is kept as the imported holomorphic sheaf-cohomology statement; its spacetime-algebra kernels (TWGA E2) are not added, since they are not part of the cited result.'
---

## formal
Massless free fields of helicity $s$ on (suitably convex regions of complexified) Minkowski space (complexified with the unit $I_4$, points $u + I_4 w$) are in natural isomorphism with the first cohomology of the corresponding region of the conformal spinor space $\CS$ (twistor space) with coefficients in $\mathcal{O}(-2s-2)$: the homogeneity $-2s-2$ classifies the helicity-$s$ field. \emph{Provenance:} Penrose \cite{Penrose1969}; the sheaf-cohomological form \cite{EPW1981}.

## technical
The Penrose transform identifies the massless free fields of helicity $s$ on suitably convex regions of complexified Minkowski space, the complex unit being $I_4$, with the first sheaf cohomology of the corresponding region of the conformal spinor space, with coefficients in $\mathcal{O}(-2s-2)$. The homogeneity $-2s-2$ therefore classifies the helicity-$s$ field.

## lay
A classical result of Penrose says that every massless field, such as light or gravitational waves, can be encoded as a geometric object on the space of spinors of conformal geometry. The encoding depends on the field's helicity only through a single integer describing how that object scales.

## one-liner
Massless free fields of helicity $s$ correspond naturally to first cohomology on regions of the conformal spinor space with coefficients in $\mathcal{O}(-2s-2)$.
