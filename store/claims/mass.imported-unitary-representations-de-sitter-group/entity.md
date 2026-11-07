---
id: mass.imported-unitary-representations-de-sitter-group
kind: claim
version: 5
title: 'Imported: the unitary representations of the de Sitter group'
status: imported
region: mass
subject: mass
tags: [classical-theorem, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
- name: Claude Opus 5.5
  role: notation pass, every imaginary unit resolved as a geometric-algebra pseudoscalar (unit principle)
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'maintainer pass, a series hypothesis moved out of the imported Fact at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
imported_from:
- citation: J. Dixmier, Repr'esentations int'egrables du groupe de De Sitter, Bull. Soc. Math. France
    89 (1961), 9--41.
  key: Dixmier1961
  locator: \S\S3--4
- citation: A. Higuchi, Symmetric tensor spherical harmonics on the $N$-sphere and their application to
    the de Sitter group $SO(N,1)$, J. Math. Phys. 28 (1987), 1553--1566.
  key: Higuchi1987
locators:
  paper: T11
  number: Fact 2.6
  label: fact:dixmier
  line: 434
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Decision item B6 (routine): the series-internal sentence that mass.casimir-form-join''s C_2(I_Lambda-perp) is ''in this same normalisation, with no shift'' moves out of this imported Fact (formal and technical): it is the normalisation hypothesis that synthesis.operator-join-casimir-shifts (iii) states and does not prove, and the Fact now says so and points there; Dixmier''s classification as imported is unchanged, status stays imported.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U4 with U1: the principal-series weight Delta = 3/2 + i nu is restated as 3/2 + I_4 nu, numbers and the scalars of the abstract representation spaces being read in span{1, I_4}; the source''s form moves to extraction.source_formal, and the formal level says the source writes i for I_4. No bare i remains, so the outside_ga declaration (imported, for i only) is removed; status stays imported.'
  source_formal: |-
    Among the unitary irreducible representations of $SO(1,4)$ carried by scalar fields, with the Casimir normalised so that it acts as $-m^{2}/H^{2}$ and $m^{2} = \Delta(3-\Delta)H^{2}$, are: the principal series, $m^{2} \ge \tfrac94 H^{2}$, parametrised by $\Delta = \tfrac32 + i\nu$ with $m^{2} = (\tfrac94 + \nu^{2})H^{2}$; the complementary series, $0 < m^{2} < \tfrac94 H^{2}$, with $\Delta$ real in $(0,3)$; and the massless point $m = 0$. No representation of the principal or complementary series has $m^{2} < 0$; the exceptional (discrete) series, which also contains scalar members at $\Delta = 3 + k$, $k = 1, 2, \dots$, with $m^{2} = -k(k+3)H^{2}$, is not used in this paper. \emph{Provenance:} the classification of the unitary representations is Dixmier's \cite[\S\S3--4]{Dixmier1961}; the $\Delta$-parametrisation and the mass formula for the scalar series of $SO(N,1)$ are the modern presentation, for which see \cite{Higuchi1987}. The Casimir normalisation here is the field-theoretic one on a scalar module. The de Sitter Casimir $C_{2}(I_{\Lambda}^{\perp})$ of Proposition \claimref{mass.casimir-form-join}, a quadratic form on the moment components of a composite, is in this same normalisation, with no shift between the two. What differs from the de Sitter mass is that Proposition's grip: by its clause (1) the grip equals the de Sitter mass plus $Q(I_{\Lambda}) = H^{2}$ times the composite's conformal Casimir $C_{2}(\Lambda^{2}\CS)$. Used to read Corollary \claimref{mass.weight-polynomial-two-series}, which proves the algebra of $-w(w+3)$ and imports the names of the series from here.
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Not rewritten: Delta = 3/2 + i nu is kept as Dixmier and Higuchi state it, and the entity declares outside_ga (imported); its dependants write the weight with I_4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'The series gloss now matches mass.casimir-form-join v4: the scalar-module Casimir and the composite de Sitter Casimir C_2(I_Lambda^perp) have the same normalisation (no shift by the conformal Casimir); the grip is the de Sitter mass plus H^2 times the conformal Casimir. The literature content (Dixmier, Higuchi) is unchanged. Version 1 -> 2.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'Delta = 3/2 + i nu: complex weight of an imported unitary representation of the de Sitter group (abstract Hilbert space, numbers)'
  env: fact
  context_refs:
  - mass.casimir-form-join
  - mass.weight-polynomial-two-series
  typing:
    by: ai-typing-pass
    note: Imported claim with no derivations; its context_refs are claims that use or compare with it,
      not premises, so no edges changed.
---

## formal
Among the unitary irreducible representations of $SO(1,4)$ carried by scalar fields, with the Casimir normalised so that it acts as $-m^{2}/H^{2}$ and $m^{2} = \Delta(3-\Delta)H^{2}$, are: the principal series, $m^{2} \ge \tfrac94 H^{2}$, parametrised by $\Delta = \tfrac32 + I_4\nu$ with $m^{2} = (\tfrac94 + \nu^{2})H^{2}$ (numbers, and the scalars of the representation spaces, are read in $\mathrm{span}\{1, I_4\}$, conventions U1; the source writes $i$ for $I_4$); the complementary series, $0 < m^{2} < \tfrac94 H^{2}$, with $\Delta$ real in $(0,3)$; and the massless point $m = 0$. No representation of the principal or complementary series has $m^{2} < 0$; the exceptional (discrete) series, which also contains scalar members at $\Delta = 3 + k$, $k = 1, 2, \dots$, with $m^{2} = -k(k+3)H^{2}$, is not used in this paper. \emph{Provenance:} the classification of the unitary representations is Dixmier's \cite[\S\S3--4]{Dixmier1961}; the $\Delta$-parametrisation and the mass formula for the scalar series of $SO(N,1)$ are the modern presentation, for which see \cite{Higuchi1987}. The Casimir normalisation here is the field-theoretic one on a scalar module. Whether the de Sitter Casimir $C_{2}(I_{\Lambda}^{\perp})$ of Proposition \claimref{mass.casimir-form-join}, a quadratic form on the moment components of a composite, is in this same normalisation is not part of this Fact: it is the normalisation hypothesis stated, and not proved, in Proposition \claimref{synthesis.operator-join-casimir-shifts}(iii). What that Proposition's split sets beside the de Sitter Casimir is its grip: by its clause (1) the grip equals the de Sitter mass plus $Q(I_{\Lambda}) = H^{2}$ times the composite's conformal Casimir $C_{2}(\Lambda^{2}\CS)$. Used to read Corollary \claimref{mass.weight-polynomial-two-series}, which proves the algebra of $-w(w+3)$ and imports the names of the series from here.

## technical
An imported classification. With the Casimir of $SO(1,4)$ normalised to act as $-m^{2}/H^{2}$ and $m^{2} = \Delta(3-\Delta)H^{2}$, the unitary irreducible representations carried by scalar fields include the principal series, $m^{2} \ge \tfrac94 H^{2}$, with $\Delta = \tfrac32 + I_4\nu$ in $\mathrm{span}\{1, I_4\}$ and $m^{2} = (\tfrac94 + \nu^{2})H^{2}$; the complementary series, $0 < m^{2} < \tfrac94 H^{2}$, with $\Delta$ real in $(0,3)$; and the massless point $m = 0$. Neither series contains a representation with $m^{2} < 0$.

The exceptional (discrete) series also has scalar members at $\Delta = 3 + k$, $k = 1, 2, \dots$, with $m^{2} = -k(k+3)H^{2}$, but it is not used. The Casimir here is the field-theoretic one on a scalar module. Whether the de Sitter Casimir of a composite, a quadratic form on its moment components, is in the same normalisation is not part of the imported classification; the operator-join results state it as a hypothesis. By the Casimir form's split, the composite's grip is its de Sitter reading plus $H^{2}$ times its conformal Casimir.

## lay
Quantum particles in a universe with a positive cosmological constant are classified by the symmetry group of de Sitter space. For scalar particles this classical result sorts the allowed masses into families: heavy particles above a threshold set by the expansion rate, light ones below it, and the massless case. None of the families used here allows a negative mass squared.

## one-liner
The scalar unitary representations of $SO(1,4)$, with $m^{2} = \Delta(3-\Delta)H^{2}$, comprise the principal series ($m^{2} \ge \tfrac94 H^{2}$), the complementary series ($0 < m^{2} < \tfrac94 H^{2}$) and the massless point, none with $m^{2} < 0$.
