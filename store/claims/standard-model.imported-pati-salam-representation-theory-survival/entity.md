---
id: standard-model.imported-pati-salam-representation-theory-survival
kind: claim
version: 1
title: 'Imported: Pati-Salam representation theory, and the survival hypothesis'
status: imported
region: standard-model
subject: standard-model
tags: [classical-theorem, representation-theory, gauge-fields]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
imported_from:
- citation: J. C. Pati and A. Salam, Lepton number as the fourth ``color'', Phys. Rev. D 10 (1974) 275--289.
  key: PatiSalam1974
- citation: R. Slansky, Group theory for unified model building, Phys. Rep. 79 (1981) 1--128.
  key: Slansky1981
- citation: 'S. Bertolini, L. Di Luzio and M. Malinsk''y, Intermediate mass scales in the non-supersymmetric
    $SO(10)$ grand unification: a reappraisal, Phys. Rev. D 80 (2009) 015013, arXiv:0903.4049.'
  key: BertoliniDiLuzioMalinsky2009
locators:
  paper: T12
  number: Fact 10.1
  label: fact:ps
  line: 1886
extraction:
  env: fact
  context_refs:
  - standard-model.majorana-element
  typing:
    by: ai-typing-pass
    note: 'Imported fact; levels only, no edges to review. Levels pass: conditions already kept.'
---

## formal
(a) $\mathfrak{so}(4) \oplus \mathfrak{so}(6) \cong \su(2) \oplus \su(2) \oplus \su(4)$. Under $\mathrm{Spin}(4) \times \mathrm{Spin}(6) \subset \mathrm{Spin}(10)$ the $210$, the grade-four part of the Clifford algebra of the ten, contains exactly one singlet; and the $126$ decomposes as $(6,1,1) \oplus (10,1,3) \oplus (\overline{10},3,1) \oplus (15,2,2)$ in the convention of Proposition \claimref{standard-model.majorana-element}, its electroweak doublets lying in the $(15,2,2)$. (b) In unification with an intermediate scale, the scalars light at each scale are those whose vevs break the symmetry there, together with those the mass relations require; nothing else is light (the extended survival hypothesis). \emph{Provenance:} \cite{PatiSalam1974, Slansky1981} for (a), standard representation theory; (b) is a premise of the model-building literature \cite{BertoliniDiLuzioMalinsky2009}, adopted at assembly level.

## technical
(a) $\so(4) \oplus \so(6) \cong \su(2) \oplus \su(2) \oplus \su(4)$. Under $\mathrm{Spin}(4) \times \mathrm{Spin}(6) \subset \mathrm{Spin}(10)$ the $210$, the grade-four part of the Clifford algebra of the ten, contains exactly one singlet, and $126 = (6,1,1) \oplus (10,1,3) \oplus (\overline{10},3,1) \oplus (15,2,2)$, with its electroweak doublets in the $(15,2,2)$.

(b) The extended survival hypothesis: in unification with an intermediate scale, the scalars light at each scale are those whose vevs break the symmetry there, together with those the mass relations require, and nothing else is light. Part (a) is standard representation theory; part (b) is a premise of the model-building literature, adopted at assembly level.

## lay
The Pati-Salam picture groups quarks and leptons together by treating lepton number as a fourth colour, and it sits inside a larger symmetry, $\mathrm{Spin}(10)$. The first part of this fact lists standard rules for how certain large families of $\mathrm{Spin}(10)$ states break up under Pati-Salam. The second part is a working assumption of model builders: at each energy, only the scalar fields that are needed there are light. Both are taken from the literature, the second as an assumption rather than a theorem.

## one-liner
Standard Pati-Salam branching rules, one singlet in the $210$ and the stated decomposition of the $126$, together with the extended survival hypothesis for light scalars.
