---
id: singularity.type-n-only-type-n
kind: claim
version: 5
title: Type N, and only type N
status: proved
region: singularity
subject: singularity
tags: [obstruction-types, schwarzschild, transport-algorithm]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - sheaf.localised-transport@6
  - sheaf.one-sided-completion@4
  - sheaf.one-sided-completion-singularity@4
  - sheaf.schwarzschild-degeneration-boundary-tame@6
  - singularity.degeneration-exactly@2
  - tower.rigidity-clock-frozen@5
  - transport.existence-classification-type-c@4
  - transport.existence-locus-type-n@5
  - transport.type-p-self-repairing@2
  - primer.classification-real-clifford-algebras@3
  - std-algebra.sta-matrix@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:3.1
- kind: check
  ref: check.py::check_no_type_c_and_quaternionic_matrix_form
- kind: check
  ref: check.py::check_type_n_at_the_singularity
- kind: check
  ref: check.py::check_type_p_present_and_self_repairing
- kind: check
  ref: check.py::check_tower_floors_have_no_type_c
locators:
  paper: T05
  number: Prop 3.1
  label: prop:typeN
  line: 1490
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites primer.classification-real-clifford-algebras, std-algebra.sta-matrix where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: no type C (residue 6, centre R, Cl(1,3) = Mat_2(H)), type N at r = 0, type P present and self-repairing, and no type C on the tower floors. Version 3 -> 4.'
  env: proposition
  context_refs:
  - tower.rigidity-clock-frozen
  typing:
    by: ai-typing-pass
    added:
    - tower.rigidity-clock-frozen
    note: 'Added the frozen-clock theorem because the statement''s clause that no floor develops a type-C
      obstruction rests on it; the type-N locus edge is kept but doubtful, since the proof cites it to
      describe the nondegenerate datum and contrast it with the degenerate case. Levels pass: conditions
      already kept.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - tower.rigidity-clock-frozen
---

## formal
The obstruction at $r = 0$ is type N in the taxonomy of \cite[\S 3]{ButlerT1}: an isotropic direction without a metric partner, in the degenerate sense in which the root paper hands such cases to the sheaf paper. Type C cannot occur: $\Cl(1,3)$ has $p - q = -2 \equiv 6 \pmod 8$, hence is central simple ($\cong \Mat_2(\HH)$), has no central idempotents, and offers ideal fusion nothing to fuse. Type P, which is present in $\Cl(1,3)$ as in every algebra of its size, demands no transport: its rule is the rule of no rule \cite[\S 6, Prop.~6.1]{ButlerT1}, so it neither licenses nor obstructs the ascent. The operative transport rule is Rule 1, the Witt completion, and by \cite[Thm.~3.6]{ButlerT3} no floor of the resulting tower ever develops a type-C obstruction either. This is the algorithm's Step 2 \cite[\S 8.1, Step 2]{ButlerT1}, with both diagnostic questions answered by computation.

## technical
The obstruction at $r = 0$ is of type N: the degenerating direction $\er$ is null for the limit form and lies in its radical, so it is an isotropic direction without a metric partner, in the degenerate sense that the root taxonomy hands to the sheaf framework, whose localisation theorem supplies the partner by completion on the exceptional set. Type C cannot occur: $\Cl(1,3)$ has $p - q = -2 \equiv 6 \pmod 8$, so it is central simple, $\Cl(1,3) \cong \Mat_2(\HH)$, with no central idempotents for ideal fusion to fuse.

Type P is present, as in every algebra of this size, but demands no transport: its rule is the identity assignment, so it neither licenses nor obstructs the ascent. The operative transport rule is the Witt completion, and no floor of the resulting tower ever develops a type-C obstruction.

## lay
At the centre of a non-rotating black hole one direction of the geometry collapses, and this result identifies which kind of algebraic obstruction that is in the series' classification. It is the kind caused by a direction with no partner to pair with. The other substantive kind, which would need the algebra to split into independent pieces, cannot occur for the algebra of spacetime, and a third kind is present but harmless. So the repair that applies is the one that supplies the missing partner by enlarging the algebra.

## one-liner
The obstruction at $r = 0$ is of type N only: type C is excluded because $\Cl(1,3) \cong \Mat_2(\HH)$ is central simple, and type P imposes no transport.
