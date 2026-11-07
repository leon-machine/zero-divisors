---
id: one-relation.arrow-frequency-are-one-bit-level
kind: claim
version: 4
title: The arrow and the frequency are one bit, at $\Cl(1,3)$ level
status: proved
region: one-relation
subject: one-relation
tags: [matter-asymmetry]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
about:
- obj.std-algebra.spacetime-algebra
derivations:
- name: main
  uses:
  - one-relation.imported-flag-arrow-superselection@7
  - one-relation.one-datum-not-two-imaginary-unit@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_reversing_j_reverses_gamma0
- kind: check
  ref: check.py::check_pi_rotation_flipping_j_flips_c
- kind: check
  ref: check.py::check_frame_and_unit_transform_together
locators:
  paper: T16
  number: Cor 5.7
  label: cor:onebit
  line: 795
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites obj.std-algebra.spacetime-algebra where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: with C = I gamma_3 fixed, J -> -J sends gamma_0 = CJ to -gamma_0 on both sheets, and the pi-rotations about axes of the spin plane flip J, fix gamma_0 and flip C. Version 2 -> 3.'
  env: corollary
  typing:
    by: ai-typing-pass
    added:
    - one-relation.one-datum-not-two-imaginary-unit
    note: 'Added the one-datum lemma, whose map gamma_0 = CJ the corollary''s identity acts on; kept the
      flag Fact as the source of the bit''s reading, though it may be only a comparison. Levels pass:
      lay now says the bit itself still rests on Hypothesis (S).'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - one-relation.one-datum-not-two-imaginary-unit
---

## formal
With $C$ fixed, $J \mapsto -J$ forces $\gamma_{0} \mapsto -\gamma_{0}$, since $C(-J) = -(CJ)$; the rest rotation by $\pi$ about an axis in the spin plane flips $J$ while fixing $\gamma_{0}$, but it also flips $C$, so it is not a symmetry of the fixed law. Hence, given the law, the frequency sign, particle against antiparticle, and the direction of the frame's time are one bit and not two. This is the identification Fact \claimref{one-relation.imported-flag-arrow-superselection} imports under Hypothesis (S), in this paper a one-line identity in $\Cl(1,3)$; it does not source the bit, which (S) still does, but it proves that the two readings of the bit cannot come apart, which the dark-matter paper asserts as ``spent once, read twice''.

## technical
Given the law $\nabla\psi = m\psi C$ with $C$ fixed, the imaginary unit $J$ and the rest-frame vector are tied by $\gamma_{0} = CJ$, so linearity gives $C(-J) = -(CJ)$: reversing the imaginary unit reverses the direction of the frame's time. The rest rotation by $\pi$ about an axis in the spin plane flips $J$ while fixing $\gamma_{0}$, but it also flips $C$, so it is not a symmetry of the fixed law.

Hence, given the law, the frequency sign (particle against antiparticle) and the direction of the frame's time are one bit, not two. This proves that the two readings of the bit cannot come apart; it does not source the bit, which still rests on Hypothesis (S) as the imported flag fact records.

## lay
In the relativistic electron equation, the sign that separates particles from antiparticles and the direction in which a laboratory's time runs look like two separate choices. Once the form of the law is fixed, flipping one forces the other to flip, so they are a single yes-or-no choice. This does not explain where that choice comes from, which still rests on Hypothesis (S); it only shows that its two readings always agree.

## one-liner
Given the fixed Dirac-Hestenes law, the frequency sign and the direction of the rest frame's time are a single bit, since $C(-J) = -(CJ)$.
