---
id: transport.matrix-units-peirce-isomorphism
kind: claim
version: 3
title: Matrix units, and the Peirce isomorphism
status: proved
region: transport
subject: completion
tags: [idempotents]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
derivations:
- name: main
  uses:
  - transport.ascent-renders-grade-involution-inner@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:5.4
- kind: check
  ref: check.py::check_matrix_unit_relations
- kind: check
  ref: check.py::check_peirce_isomorphism
locators:
  paper: T01
  number: Lem 5.4
  label: lem:matrixunits
  line: 1165
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.matrix-units (specialises) where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the 2 x 2 matrix-unit relations for every p - q = 1 mod 4 with n <= 5 and both gamma, and the Peirce map (corner of dimension 2^(n-1), bijective, unital, multiplicative, with the displayed inverse). Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Kept the single premise; the paper calls this the standard matrix-units criterion (Lam), reproved for self-containment, but no imported claim for it is in the store, so no standard-route derivation was added.'
specialises:
- std-algebra.matrix-units@1
---

## formal
Let $\gamma = \pm 1$ and set
\[
E_{11} = \varepsilon_+, \qquad E_{22} = \varepsilon_-, \qquad E_{12} = \varepsilon_+ \nu, \qquad E_{21} = \gamma\, \varepsilon_- \nu .
\]
Then $E_{11} + E_{22} = 1$ and $E_{ij} E_{kl} = \delta_{jk} E_{il}$: a full $2 \times 2$ system of matrix units. Consequently
\[
B_\gamma \;\cong\; \Mat_2\bigl(E_{11} B_\gamma E_{11}\bigr), \qquad b \;\longmapsto\; \bigl(E_{1i}\, b\, E_{j1}\bigr)_{ij},
\]
an isomorphism of unital algebras with inverse $(c_{ij}) \mapsto \sum_{i,j} E_{i1} c_{ij} E_{1j}$.

## technical
With $Q(\nu) = \gamma = \pm 1$, set $E_{11} = \varepsilon_+$, $E_{22} = \varepsilon_-$, $E_{12} = \varepsilon_+ \nu$ and $E_{21} = \gamma\, \varepsilon_- \nu$. These satisfy $E_{11} + E_{22} = 1$ and $E_{ij} E_{kl} = \delta_{jk} E_{il}$, a full $2 \times 2$ system of matrix units in $B_\gamma$.

Consequently $b \mapsto (E_{1i}\, b\, E_{j1})_{ij}$ is an isomorphism of unital algebras $B_\gamma \cong \Mat_2(E_{11} B_\gamma E_{11})$, with inverse $(c_{ij}) \mapsto \sum_{i,j} E_{i1} c_{ij} E_{1j}$.

## lay
Inside the enlarged algebra, the two projectors that used to split the original algebra, together with the new direction, behave exactly like the four basic entries of a two-by-two matrix. It follows that the enlarged algebra is the same thing as two-by-two matrices whose entries come from one corner of it.

## one-liner
The projectors $\varepsilon_\pm$ and the adjoined generator $\nu$ form a full system of $2 \times 2$ matrix units, so $B_\gamma \cong \Mat_2(E_{11} B_\gamma E_{11})$.
