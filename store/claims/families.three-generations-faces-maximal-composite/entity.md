---
id: families.three-generations-faces-maximal-composite
kind: claim
version: 3
title: Three generations as the faces of the maximal composite
status: conjectured
region: families
subject: generations
tags:
- face-identification
- conformal-spinors
- flavour-and-mixing
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
lineage:
  motivated_by:
  - families.imported-face-valued-bracket-quantum-numbers
  - families.imported-one-derived-generation-hypothesis-s
locators:
  paper: T13
  number: Conj 3.1
  label: conj:faces
  line: 613
extraction:
  maintainer_pass_faces:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, by Leon''s decision of 2026-11-01: a marked note at the end of the formal and technical levels restating the face identification as three composites with separate slots, since in one slot space under one gauge group at most one face is a weak doublet and the faces'' chirality halves span 28 (shared pair system) or 46 to 47 (separate pair modes) of the 48 states three generations need (synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group). The conjecture''s statement and status unchanged; no edge added.'
  env: conjecture
  context_refs:
  - families.imported-face-valued-bracket-quantum-numbers
  - families.imported-one-derived-generation-hypothesis-s
  typing:
    by: ai-typing-pass
    note: 'Conjecture left conjectured with its existing motivated_by (the face-valued bracket and the
      derived generation). Levels pass: the lay level now marks the three-twistor bound as observation
      level and keeps Hypothesis (S) for the lepton doublet; the one-liner states the bound it rests on.'
  source_title: Three generations as the faces of the maximal composite
  source_formal: 'The maximal composite is three twistors, a bound imported at observation level, and
    a massive matter unit is a two-twistor composite (Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}).
    Given the bound, there are $\binom{3}{2} = 3$ ways to choose which two twistors of the maximal system
    carry the mass, each choice supplying an identical copy of the fermion content of Fact \claimref{families.imported-one-derived-generation-hypothesis-s},
    its lepton doublet under Hypothesis (S). Conjecture: the three generations are the three two-twistor
    faces of the maximal three-twistor system. Corollary shape, at observation level: generation mixing
    is the overlap between distinct embeddings, a CKM-shaped structure with mixing angles set by the geometry
    of the faces.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: The maximal composite and its faces are now named by conformal spinors in all levels; the conjecture
      and its levels are unchanged.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: connected
    note: Already connected through the postulate families.hyp-face-identification, which the results
      relying on the face identification assume; no definition bears on it.
---

## formal
The maximal composite is three conformal spinors (twistors), a bound imported at observation level, and a massive matter unit is a two-spinor composite (Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}). Given the bound, there are $\binom{3}{2} = 3$ ways to choose which two spinors of the maximal system carry the mass, each choice supplying an identical copy of the fermion content of Fact \claimref{families.imported-one-derived-generation-hypothesis-s}, its lepton doublet under Hypothesis (S). Conjecture: the three generations are the three two-spinor faces of the maximal three-spinor system. Corollary shape, at observation level: generation mixing is the overlap between distinct embeddings, a CKM-shaped structure with mixing angles set by the geometry of the faces.

\emph{Note (the face identification restated, 2026-11-01).} The identification is restated as three composites with separate slots: each face is its own two-spinor composite, with its own slot and pair modes, and the three are not subspaces of one slot space. Read in one state space with shared slots the faces are not three generations under one gauge group (\claimref{synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group}): any Lie algebra acting linearly on the three slots leaves at most one face plane irreducible, so at most one face is a weak doublet, and the faces' chirality halves span $28$ states with one pair system shared by the faces, or $46$ to $47$ with separate pair modes, of the $48 = 3 \times 16$ that three generations need.

## technical
Given the imported bound that the maximal composite is three conformal spinors, and that a massive matter unit is a two-spinor composite, there are $\binom{3}{2} = 3$ ways to choose which two spinors of the maximal system carry the mass, each supplying an identical copy of one generation's fermion content, its lepton doublet under Hypothesis (S). The conjecture is that the three generations are these three two-spinor faces.

Its corollary shape, at observation level, is that generation mixing is the overlap between distinct embeddings, a CKM-shaped structure with mixing angles set by the geometry of the faces.

(Note, 2026-11-01: the identification is restated as three composites with separate slots; in one shared slot space at most one face is a weak doublet under one gauge group and the faces' chirality halves span at most $47$ of the $48$ states three generations need, \claimref{synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group}.)

## lay
Matter comes in three copies, or generations, of each kind of particle, with no accepted explanation for why there are three. This conjecture proposes that the number comes from counting: if the largest allowed composite has three building blocks (a bound the series holds only at observation level) and a massive particle uses two of them, there are exactly three ways to choose the pair. Each choice would be one generation, with its lepton doublet as identified under Hypothesis (S), and the way generations mix would come from how the choices overlap.

## one-liner
Conjecturally, given the observation-level bound that the maximal composite is three conformal spinors, the three generations are the three two-spinor faces of the maximal three-spinor composite, with generation mixing given by the overlaps between faces.
