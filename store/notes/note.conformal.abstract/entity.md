---
id: note.conformal.abstract
kind: note
version: 2
title: Abstract
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T02, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, comments_on link at Leon''s decisions'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
comments_on:
- conformal.blade-basis-persists-under-degeneracy
- conformal.minimal-nondegenerate-completion
locators:
  paper: T02
  number: Abstract
  section: Abstract
  line: 120
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Decision item D11 (routine): comments_on link added to conformal.minimal-nondegenerate-completion, the abstract''s subject. Paper text unchanged.'
---

## formal
Projective geometric algebra $\Cl(3,0,1)$ and conformal geometric algebra $\Cl(4,1)$ are the two standard algebras of applied geometric computing, usually presented as independent modelling choices. This note proves that the second is the unique minimal nondegenerate completion of the first. For any real Clifford algebra $\Cl(p,q,r)$ of a degenerate form with nondegenerate part of signature $(p,q)$ and radical of dimension $r$, the minimal nondegenerate Clifford completion exists, has signature exactly $(p{+}r, q{+}r)$, and is unique up to an isometry fixing the original space pointwise: existence by adjoining the dual of the radical with the hyperbolic pairing, minimality because each radical direction must pair nontrivially into any completion, the signature forced by Witt splitting of the complement, and uniqueness by the Witt extension theorem. In particular $\Cl(3,0,1)$ completes minimally and uniquely to $\Cl(4,1)$. The completion converts the radical's nilpotent ideal into the unit ideal. No extension gives a radical element an inverse, since its square stays zero; what CGA supplies is a partner $\varphi$ for each radical direction $\rho$ with $\rho\varphi + \varphi\rho = 2$, so the division PGA lacks becomes total at the level of ideals, through the pairing and not through inverses. The embedding carries PGA's translators to CGA's translators verbatim. Every result is proved in full; the note situates the theorem in the series' transport-rule taxonomy and delimits what minimality promises. All computational identities are verified in exact rational arithmetic in an accompanying script.

## technical
pending

## lay
pending

## one-liner
pending
