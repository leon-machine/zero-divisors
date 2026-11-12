---
id: standard-model.imported-sectors-superselection-mirror-copy
kind: claim
version: 4
title: 'Imported: sectors, superselection, and the mirror copy'
status: proved
region: standard-model
subject: dark-matter
tags: [superselection, mirror-sector]
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
- name: Claude Opus 5.5
  role: consistency pass, premise named as the single frozen point
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.dark-matter.frozen-phase-operators
derivations:
- name: main
  uses:
  - dark-matter.mirror-tower-copy-one@11
  - dark-matter.superselected-hence-dark-exactly-stable@5
  - dark-matter.towers-are-residues-single-clock-filter@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_towers_are_residues_and_mirror_is_another
- kind: check
  ref: check.py::check_even_subalgebras_of_reversal_pair_agree
locators:
  paper: T12
  number: Fact 8.2
  label: fact:towers
  line: 1286
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Every level and the proof called the premise of T14 Prop 4.1 the single-clock premise; that proposition (dark-matter.superselected-hence-dark-exactly-stable) assumes P1, the single frozen point, while the single clock is the filter of the census. Naming fix.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Rule 1 keeps the residue (Morita step), this world and the mirror in different towers (corners H and R), and equal even-subalgebra types for the reversal pair. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    note: 'All three uses (towers as residues, superselection, the mirror copy theorem) match the cited
      provenance and were kept; the sector decomposition is already in about. Levels pass: the lay level
      and one-liner now state the single-clock premise and the sector decomposition the imported results
      are conditional on.'
  env: fact
  context_refs:
  - dark-matter.mirror-tower-copy-one
  - dark-matter.superselected-hence-dark-exactly-stable
  - dark-matter.towers-are-residues-single-clock-filter
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
The eight towers are the residues of the shadow dimension mod $8$ \cite[Prop.~3.1]{ButlerT14}, this world's tower one of them and the mirror tower another. Under the sector decomposition of \cite[Def.~3.6]{ButlerT14}, every frozen-phase local operator is a section of one tower's soldered bundle and acts within that tower's sector; the tower charge is superselected, the shadow walls separating residues are unreachable, and matter in another tower gravitates on the shared metric and does nothing else: the only inter-tower coupling is gravitational, and the only inter-tower event is the descent \cite[Prop.~4.1]{ButlerT14}. The mirror tower's derived content is a copy of this one's, with the same gauge algebra, global form, generation, hypercharges and chirality halves, hence the same $\beta$-functions at every scale \cite[Thm.~4.3(i),(iii)]{ButlerT14}. \emph{Provenance:} T14, at the levels declared there; Proposition 4.1 rests on the single-frozen-point premise P1 and the sector decomposition, and everything below that uses it is conditional on the same.

## technical
The eight towers are the residues of the shadow dimension mod $8$, this world's tower one of them and the mirror tower another. Under the sector decomposition every frozen-phase local operator is a section of one tower's soldered bundle and acts within that tower's sector; the tower charge is superselected and the shadow walls between residues are unreachable, so matter in another tower only gravitates on the shared metric, and the only inter-tower event is the descent.

The mirror tower's derived content is a copy of ours, with the same gauge algebra, global form, generation, hypercharges and chirality halves, hence the same $\beta$-functions at every scale. The fact is imported from the dark-matter paper at the levels declared there, and is conditional on the single-frozen-point premise P1 and the sector decomposition.

## lay
Under the dark-matter paper's single-frozen-point premise and its decomposition into sectors, the framework splits matter into eight separate sectors that can exchange nothing except gravity. One of them is ours, and another is a mirror copy with the same particles and forces. Because the forces are the same, their strengths change with energy in exactly the same way in both sectors. All of this is carried over from that paper at the levels it declares there.

## one-liner
Conditional on the single-frozen-point premise P1 and the sector decomposition, the eight towers are superselected sectors coupled only through gravity, and the mirror tower's content copies ours, with the same $\beta$-functions at every scale.
