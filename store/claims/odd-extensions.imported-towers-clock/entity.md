---
id: odd-extensions.imported-towers-clock
kind: claim
version: 5
title: 'Imported: the towers and the clock'
status: proved
region: odd-extensions
subject: tower
tags: [towers-by-residue, clifford-classification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - dark-matter.imported-eight-towers-mod-8-clock@4
  - tower.commuting-copies@5
  - tower.rigidity-clock-frozen@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_ascent_is_matrix_amplification_one_step
- kind: check
  ref: check.py::check_period_eight
- kind: check
  ref: check.py::check_eight_towers
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Fact 1.1
  label: fact:towers
  line: 407
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Decision item E9 (routine; no retirement): equivalent_to dark-matter.imported-eight-towers-mod-8-clock@4 added. It restates the dark-matter Fact, which is kept as the home.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Cl(p+1,q+1) = Mat_2(Cl(p,q)) by commuting copies and matrix units, Cl(8,0) = Cl(0,8) = Mat_16(R) and the shift by eight, and the eight towers. Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  env: fact
  context_refs:
  - dark-matter.imported-eight-towers-mod-8-clock
  - tower.commuting-copies
  - tower.rigidity-clock-frozen
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: The three uses are exactly the cited provenance and are kept; mod-8 periodicity is classical
      but no imported periodicity claim exists in the store, so no standard-route derivation was added.
equivalent_to:
- dark-matter.imported-eight-towers-mod-8-clock@4
---

## formal
The $(1,1)$ ascent $\Cl(p,q) \to \Cl(p+1,q+1) \cong \Mat(2, \Cl(p,q))$ preserves $p - q$; the real Clifford algebras are periodic modulo eight; the eight residues label eight parallel towers. \emph{Provenance:} \cite[Thms.~3.2 and 3.6]{ButlerT3}; \cite[Fact~2.5]{ButlerT14}.

## technical
The $(1,1)$ ascent $\Cl(p,q) \to \Cl(p+1,q+1) \cong \Mat(2, \Cl(p,q))$ adjoins a hyperbolic plane and so preserves $p - q$, and the real Clifford algebras are periodic modulo eight. The residue $p - q \bmod 8$ therefore labels eight parallel towers, each closed under the ascent.

In the store this fact restates the tower's commuting-copies and rigidity results and the corresponding dark-matter fact.

## lay
The series' completion step adds two directions of opposite sign, which turns the algebra into two-by-two matrices over itself and leaves the difference between the counts of the two kinds of direction unchanged. Real Clifford algebras repeat with period eight in that difference. So the algebras fall into eight separate towers, and climbing never moves between them.

## one-liner
The $(1,1)$ ascent preserves $p - q$ and real Clifford algebras are periodic modulo eight, so the eight residues label eight parallel towers.
