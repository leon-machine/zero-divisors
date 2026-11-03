---
id: correspondence.googly-localisation-quartic-order
kind: claim
version: 3
title: "Googly localisation at quartic order"
status: conjectured
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors, chirality, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
lineage:
  motivated_by:
  - correspondence.chirality-split-ordering-insensitivity-asd-sector
  - correspondence.imported-nonlinear-graviton
  - correspondence.ordering-filtration
locators:
  paper: T09
  number: Conj 6.11
  label: conj:googly
  line: 864
extraction:
  maintainer_pass:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only. Version 2 -> 3.'
  env: conjecture
  context_refs:
  - correspondence.chirality-split-ordering-insensitivity-asd-sector
  - correspondence.imported-nonlinear-graviton
  - correspondence.ordering-filtration
  typing:
    by: ai-typing-pass
    note: Conjecture with its existing motivated_by lineage kept; no edges.
  source_title: "Googly localisation at quartic order"
  source_formal: |-
    There is a palatial construction (a deformation of the holomorphic function algebra of twistor space within $\mathcal{P}$, in the programme of \cite{Penrose15}) with the following two parts. \emph{(a)} Anti-self-dual (nonlinear graviton) curvature data enters at the commutative level: the construction restricted to the ASD sector reduces, at order $\hbar^0$, to the deformed twistor spaces of Fact \claimref{correspondence.imported-nonlinear-graviton}, and its ASD data is insensitive to operator ordering, the consistency of which is Proposition \claimref{correspondence.chirality-split-ordering-insensitivity-asd-sector}(2). \emph{(b)} The self-dual, googly data is carried \emph{exactly} by the quartic-order ordering tensor of Lemma \claimref{correspondence.ordering-filtration}: the $\mathfrak{so}(2,4)$-valued discrepancy assignments $(M, N) \mapsto$ (reordering defect of $q(M)q(N)$-words in the deformed product), which by Lemma \claimref{correspondence.ordering-filtration}(3) lie precisely where curvature operators lie. In particular the googly information resides not in ordering ambiguities generically but at quartic order specifically.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space to the conformal spinor space and the deformed twistor spaces to deformed projective spinor spaces (Penrose's curved twistor spaces, named once). The palatial programme and the googly data keep their names as Penrose's; the conjecture itself is unchanged."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: 'Open conjecture whose supporting results are already its motivated_by lineage; nothing proved rests on it and no store definition concerns it.'
---

## formal
There is a palatial construction (a deformation of the holomorphic function algebra of the conformal spinor space $\CS$ (twistor space) within $\mathcal{P}$, in the programme of \cite{Penrose15}) with the following two parts. \emph{(a)} Anti-self-dual (nonlinear graviton) curvature data enters at the commutative level: the construction restricted to the ASD sector reduces, at order $\hbar^0$, to the deformed projective spinor spaces (Penrose's curved twistor spaces) of Fact \claimref{correspondence.imported-nonlinear-graviton}, and its ASD data is insensitive to operator ordering, the consistency of which is Proposition \claimref{correspondence.chirality-split-ordering-insensitivity-asd-sector}(2). \emph{(b)} The self-dual, googly data is carried \emph{exactly} by the quartic-order ordering tensor of Lemma \claimref{correspondence.ordering-filtration}: the $\mathfrak{so}(2,4)$-valued discrepancy assignments $(M, N) \mapsto$ (reordering defect of $q(M)q(N)$-words in the deformed product), which by Lemma \claimref{correspondence.ordering-filtration}(3) lie precisely where curvature operators lie. In particular the googly information resides not in ordering ambiguities generically but at quartic order specifically.

## technical
Conjecture. There is a palatial construction, a deformation of the holomorphic function algebra of the conformal spinor space inside the palatial algebra $\mathcal{P}$ in Penrose's programme, with two features. Restricted to the anti-self-dual sector it reduces at order $\hbar^0$ to the deformed projective spinor spaces of the nonlinear graviton, and its anti-self-dual data is insensitive to operator ordering, consistently with the proved ordering insensitivity of that sector.

The self-dual, googly data is carried exactly by the quartic-order ordering tensor: the $\mathfrak{so}(2,4)$-valued reordering defects of $q(M)q(N)$-words in the deformed product, which by the ordering filtration lie where curvature operators lie. So the googly information would reside at quartic order specifically, not in ordering ambiguities generically.

## lay
Penrose's nonlinear graviton captures one half of the gravitational field strength, the anti-self-dual Weyl half, through a curved version of the projective spinor space of the conformal algebra; the other half is called the googly data. This conjecture proposes that, in a noncommutative version of that construction (Penrose's palatial programme), the anti-self-dual half is untouched by questions of operator ordering, while the googly half is carried precisely by the ordering effects that first appear when four of its operators are multiplied. It is a proposal, not a proved result.

## one-liner
Conjecturally, a palatial deformation of the conformal spinor space carries anti-self-dual curvature at the commutative, ordering-insensitive level and the self-dual googly data exactly in the quartic-order ordering tensor.
