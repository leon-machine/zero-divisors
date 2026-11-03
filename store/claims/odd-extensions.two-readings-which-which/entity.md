---
id: odd-extensions.two-readings-which-which
kind: claim
version: 2
title: The two readings, and which is which
status: proved
region: odd-extensions
subject: tower
tags: [frozen-point, towers-by-residue, undetermined-input]
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
review: typed
derivations:
- name: main
  uses:
  - odd-extensions.belongs-tower@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_one_algebra_two_solderings
- kind: check
  ref: check.py::check_stelle_west_vector_is_the_normal_of_fixed_norm
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Cor 7.2
  label: cor:readings
  line: 620
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: one algebra Cl(1,4) with soldered residues 6 and 5, and the Stelle-West vector as the normal of the de Sitter hyperboloid with Lambda Q(V) = -3. Version 1 -> 2.'
  env: corollary
  context_refs:
  - odd-extensions.four-extensions-are-four-odd-towers
  typing:
    by: ai-typing-pass
    note: 'Kept the one use; the reference to the four-odd-towers proposition is the statement being qualified,
      not a premise, so it was not added. Levels pass: the one-liner now keeps "if populated" for the
      five-dimensional dark towers.'
---

## formal
The two readings of $\Cl(1,4)$ that occur in the series are two solderings of one algebra, and the series' definition of the residue assigns them to different towers. The fifth direction of the frozen point's algebra is not a spacetime direction and never was: it is the Stelle-West vector, the normal to the de Sitter hyperboloid, with fixed norm $\ell = \sqrt{3/\Lambda}$, and its algebra is this tower's. The five-dimensional dark towers, if populated, are soldered to a fifth tangent direction that the frozen point does not supply, whose size $L$ remains the datum the series does not fix. Proposition \claimref{odd-extensions.four-extensions-are-four-odd-towers} therefore holds as a statement about algebras, and only about algebras.

## technical
The two readings of $\Cl(1,4)$ that occur in the series are two solderings of one algebra, and the residue, read from the soldered space, assigns them to different towers. The fifth direction of the frozen point's algebra is the Stelle-West vector, the normal to the de Sitter hyperboloid with fixed norm $\ell = \sqrt{3/\Lambda}$; it is not a spacetime direction, and that algebra belongs to this tower.

The five-dimensional dark towers, if populated, are soldered to a fifth tangent direction that the frozen point does not supply, of a size $L$ the series does not fix. The identification of the four single extensions with the four odd towers therefore holds for algebras, and only for algebras.

## lay
The same five-dimensional algebra turns up twice in the series with two different meanings. In one, the fifth direction is the fixed radius direction of de Sitter space, which belongs to our world; in the other it is a genuine extra direction of a hypothetical dark sector, whose size the series leaves open. Matching the single extensions to dark towers is therefore a statement about the algebras alone.

## one-liner
The two readings of $\Cl(1,4)$ are two solderings of one algebra: the frozen point's, whose fifth direction is the Stelle-West vector, lies in this tower, and the five-dimensional dark towers', if populated, soldered to an unfixed fifth tangent direction, lie in another.
