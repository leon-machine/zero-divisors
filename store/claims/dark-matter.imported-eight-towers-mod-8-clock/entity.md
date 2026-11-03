---
id: dark-matter.imported-eight-towers-mod-8-clock
kind: claim
version: 4
title: 'Imported: the eight towers and the mod-8 clock'
status: proved
region: dark-matter
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
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - tower.commuting-copies@5
  - tower.rigidity-clock-frozen@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_ascent_is_matrix_amplification_one_step
- kind: check
  ref: check.py::check_ascent_is_matrix_amplification_two_steps
- kind: check
  ref: check.py::check_period_eight
- kind: check
  ref: check.py::check_eight_towers
- kind: proof
  derivation: main
locators:
  paper: T14
  number: Fact 2.5
  label: fact:towers
  line: 112
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Cl(p+k,q+k) = Mat_{2^k}(Cl(p,q)) by commuting copies and matrix units for k = 1, 2, Cl(8,0) = Cl(0,8) = Mat_16(R) and the shift by eight, and the eight towers. Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  env: fact
  context_refs:
  - tower.commuting-copies
  - tower.rigidity-clock-frozen
  outside_pilot_cites:
  - ButlerT1
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: Both uses (commuting copies, rigidity) match the cited tower theorems and are kept; the paper
      attributes the matrix isomorphism to Bott, but no imported Bott-periodicity claim exists in the
      store, so no standard-route derivation was added.
---

## formal
The (1,1) ascent preserves $p - q$ and $\Cl(p+k, q+k) \cong \Mat(2^{k}, \Cl(p,q))$ (Bott), so the eight residues label eight parallel towers. \emph{Provenance:} \cite[Thms.~3.2, 3.6, Rem.~3.7]{ButlerT3}, \cite[\S7]{ButlerT1}.

## technical
The $(1,1)$ ascent $\Cl(p,q) \to \Cl(p+1,q+1)$ adjoins one hyperbolic plane, so it leaves $p - q$ unchanged, and iterating it gives $\Cl(p+k, q+k) \cong \Mat(2^{k}, \Cl(p,q))$, the Bott-type matrix doubling. The residue $p - q \bmod 8$ is therefore constant along each chain of ascents, and the eight residues label eight parallel towers.

In the store this fact restates the commuting-copies theorem and the rigidity of the clock along the tower.

## lay
Climbing the ladder of algebras by adding one plus-square direction and one minus-square direction never changes the difference between the two counts. Each step replaces the algebra by two-by-two matrices with entries in the old one, so nothing essential changes. The possible starting points therefore sort into eight separate towers, according to that difference counted modulo eight.

## one-liner
The $(1,1)$ ascent preserves $p - q$ with $\Cl(p+k,q+k) \cong \Mat(2^{k}, \Cl(p,q))$, so the eight residues of $p - q$ modulo eight label eight parallel towers.
