---
id: lepton.imported-free-sector-anomaly-conditions
kind: claim
version: 5
title: 'Imported: the free sector and the anomaly conditions'
status: proved
region: lepton
subject: standard-model
tags: [hypercharge-and-anomalies]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate reference key merged at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - lepton.imported-free-sector-anomaly-conditions-external@2
  - standard-model.imported-anomaly-coefficients@1
  - standard-model.quarks-leptons-two-level-fermion-content@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_free_sector_content
- kind: check
  ref: check.py::check_opposite_handedness_enters_conjugated
locators:
  paper: T12-lepton
  number: Fact 1.5
  label: fact:free
  line: 196
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Decision item D12 (routine): references.yaml held WeinbergQFT1 and WeinbergQFT2 as one book (Weinberg, QFT Vol. 2, 1996); the key is merged into WeinbergQFT2 and the citations of the formal level and the proof repointed (the source_formal and orig-proof-main.tex keep the paper''s key as history).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the free sector (1)_0 + (3)_{-1/3} + (3b)_{-2/3} + (1)_{-1} from exact characters, and conjugated opposite-handed fermions cancelling in all four anomaly sums. Version 3 -> 4.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the single-twistor sector to the sector of a single conformal spinor at every level and in the provenance proof; the Dirac module Sp and its complex structure are kept.'
  source_title: |-
    Imported: the free sector and the anomaly conditions
  source_formal: |-
    The single-twistor (massless, free) sector is $\Sp = \Lambda^{\bullet}W$ with the pair-slot factor acting as $\Lambda^{\bullet}(\lambda^{-2}b)$: its grade-$k$ states transform as $\Lambda^{k}\C^{3} = 1, 3, \bar{3}, 1$ with weight $-2k$, that is $(1)_{0}, (3)_{-1/3}, (\bar{3})_{-2/3}, (1)_{-1}$. For a gauge group with a $U(1)$ factor acting on Weyl fermions listed in one handedness, the four anomaly-cancellation conditions are those of \cite[Fact~2.7]{ButlerT12}; a fermion of the opposite handedness enters as its conjugate, with the conjugate representation and the opposite hypercharge. \emph{Provenance:} \cite[Prop.~5.3(3), Fact~2.7]{ButlerT12}; \cite[\S 22.4]{WeinbergQFT1}.
  typing:
    by: ai-typing-pass
    note: 'Kept the anomaly-coefficient import, the quark-lepton content result (free-sector clause) and
      the external Weinberg entry, all cited as provenance. Levels pass: lay and one-liner now keep the
      U(1)-factor hypothesis of the anomaly clause.'
  env: fact
  context_refs:
  - standard-model.imported-anomaly-coefficients
  - standard-model.quarks-leptons-two-level-fermion-content
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
The sector of a single conformal spinor (the single-twistor sector; massless, free) is $\Sp = \Lambda^{\bullet}W$ with the pair-slot factor acting as $\Lambda^{\bullet}(\lambda^{-2}b)$: its grade-$k$ states transform as $\Lambda^{k}\C^{3} = 1, 3, \bar{3}, 1$ with weight $-2k$, that is $(1)_{0}, (3)_{-1/3}, (\bar{3})_{-2/3}, (1)_{-1}$. For a gauge group with a $U(1)$ factor acting on Weyl fermions listed in one handedness, the four anomaly-cancellation conditions are those of \cite[Fact~2.7]{ButlerT12}; a fermion of the opposite handedness enters as its conjugate, with the conjugate representation and the opposite hypercharge. \emph{Provenance:} \cite[Prop.~5.3(3), Fact~2.7]{ButlerT12}; \cite[\S 22.4]{WeinbergQFT2}.

## technical
The sector of a single conformal spinor (massless, free), $\Sp = \Lambda^{\bullet}W$, with the pair-slot factor acting as $\Lambda^{\bullet}(\lambda^{-2}b)$, has grade-$k$ states $\Lambda^{k}\C^{3}$ of weight $-2k$, that is $(1)_{0}, (3)_{-1/3}, (\bar{3})_{-2/3}, (1)_{-1}$.

For a gauge group with a $U(1)$ factor acting on Weyl fermions listed in one handedness, the four anomaly-cancellation conditions are the series' standard ones; a fermion of the opposite handedness enters as its conjugate, with the conjugate representation and the opposite hypercharge.

## lay
A single free spinor state of the conformal algebra carries four kinds of state, with hypercharges zero, minus one third, minus two thirds and minus one. To check that a gauge theory with an abelian (hypercharge-type) factor, built on such particles, is consistent at the quantum level, one uses four standard anomaly sums over the particles, all listed with the same handedness. A particle of the other handedness is counted through its antiparticle.

## one-liner
The free sector of a single conformal spinor carries $(1)_{0}, (3)_{-1/3}, (\bar{3})_{-2/3}, (1)_{-1}$, and, for a gauge group with a $U(1)$ factor, the four anomaly conditions apply to fermions listed in one handedness, opposite-handed ones entering as conjugates.
