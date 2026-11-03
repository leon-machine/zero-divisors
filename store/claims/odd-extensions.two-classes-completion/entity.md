---
id: odd-extensions.two-classes-completion
kind: claim
version: 3
title: Two classes of completion
status: proved
region: odd-extensions
subject: completion
tags: [degenerate-algebras, hyperbolic-plane, classification, cosmological-constant]
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
about:
- obj.odd-extensions.single-extension
derivations:
- name: main
  uses:
  - odd-extensions.exceptional-algebra-residue-completion-both-sides@4
  - odd-extensions.imported-minimal-completion-degenerate-algebra-rule@5
  - odd-extensions.imported-tame-walls-exceptional-algebra-residue@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_second_class_complement_line_changes_type
- kind: check
  ref: check.py::check_first_class_cannot_be_two_sided
- kind: check
  ref: check.py::check_first_class_rank_two
locators:
  paper: T14a
  number: Cor 10.4
  label: cor:twowalls
  line: 764
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the second-class rank-one complement changing type, the first class degenerating for any constant complement, and the rank-two first-class completion. Version 2 -> 3.'
  env: corollary
  context_refs:
  - odd-extensions.imported-minimal-completion-degenerate-algebra-rule
  typing:
    by: ai-typing-pass
    added:
    - odd-extensions.imported-minimal-completion-degenerate-algebra-rule
    note: 'Added the minimal-completion Fact from context_refs because the statement derives the rank-two
      claim for the first class from it; E204 is inherited from the lambda-wall theorem, outside this
      list. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - odd-extensions.imported-minimal-completion-degenerate-algebra-rule
---

## formal
The sheaf paper's conservation theorem concerns completions with one exterior model: the same nondegenerate complement $K$ on both sides of the wall. For those, degeneracy is conserved and displaced to a shadow wall, and the ambient adjoins a hyperbolic plane to the whole bundle: rank two by Fact \claimref{odd-extensions.imported-minimal-completion-degenerate-algebra-rule}, and to the whole bundle because off the wall the bundle is nondegenerate and the standard complement must exist there. The $\Lambda$ family is completed by a construction of the other class: a family of hyperplanes in one fixed nondegenerate space, whose complement is a single line that changes type across the wall, rank one. Nothing prevents a spacetime wall from being completed in the second class as well, with a complement that is not standard; what the sheaf paper proves is that the first class cannot be made two-sided. The transport principle's founding move, resolving a nilpotent by a pair, is the first class, and the frozen point's passage from anti-de Sitter to de Sitter is the second, which is not a transport (Definition \claimref{obj.odd-extensions.single-extension}).

## technical
Completions across a wall come in two classes. In the first, the same nondegenerate complement $K$ sits on both sides of the wall; then degeneracy is conserved and displaced to a shadow wall, and the ambient adjoins a hyperbolic plane to the whole bundle, of rank two by the minimal completion result and over the whole bundle because the standard complement must exist where the bundle is nondegenerate.

In the second class a family of hyperplanes in one fixed nondegenerate space is completed by a single line that changes type across the wall, of rank one; the $\Lambda$ family is completed this way. Nothing prevents a spacetime wall from being completed in the second class with a non-standard complement; what is proved is that the first class cannot be made two-sided. Resolving a nilpotent by a pair is of the first class, while the frozen point's passage from anti-de Sitter to de Sitter is of the second and is not a transport in the single-extension sense.

## lay
There are two different ways to complete a space whose metric degenerates along a wall. One keeps the same extra piece on both sides and adds a pair of directions everywhere; the other places the whole family inside one fixed larger space and adds a single direction whose character flips across the wall. The series' basic repair of division by zero is of the first kind. The passage from anti-de Sitter to de Sitter at the frozen point is of the second kind, and so is not a transport in the series' sense.

## one-liner
Wall completions fall into a first class with one exterior model, which conserves degeneracy, adjoins a rank-two hyperbolic plane to the whole bundle and cannot be made two-sided, and a second, rank-one class with a single type-changing line, which completes the $\Lambda$ family and is not a transport.
