---
id: tower.matrix-amplification-structural-properties
kind: claim
version: 3
title: 'Matrix amplification: structural properties'
status: proved
region: tower
subject: clifford-structure
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.morita-amplification@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_centre_of_matrix_algebra
- kind: check
  ref: check.py::check_matrix_algebra_over_simple_is_simple
- kind: check
  ref: check.py::check_block_flattening
- kind: check
  ref: check.py::check_matrices_over_direct_sum
locators:
  paper: T03
  number: Lem 3.3
  label: lem:amplification
  line: 254
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.morita-amplification where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: centre of Mat_m(A), simplicity of Mat_2(A) for simple A, block flattening, and matrices over a direct sum. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Self-contained computation with matrix units and no store references, so no edges.'
---

## formal
Let $A$ be a unital real algebra and $m \geq 1$. Then: (i) $Z(\Mat_m(A)) = Z(A)\cdot 1_m$; (ii) if $A$ is simple, so is $\Mat_m(A)$; (iii) $\Mat_m(\Mat_r(D)) \cong \Mat_{mr}(D)$ for any unital $D$; (iv) $\Mat_m(A_1 \oplus A_2) \cong \Mat_m(A_1) \oplus \Mat_m(A_2)$.

## technical
For a unital real algebra $A$ and $m \geq 1$, passing to $m \times m$ matrices over $A$ preserves the basic structure. The centre is $Z(\Mat_m(A)) = Z(A) \cdot 1_m$; $\Mat_m(A)$ is simple whenever $A$ is; nested matrix algebras regroup, $\Mat_m(\Mat_r(D)) \cong \Mat_{mr}(D)$ for any unital $D$; and amplification distributes over direct sums, $\Mat_m(A_1 \oplus A_2) \cong \Mat_m(A_1) \oplus \Mat_m(A_2)$.

The first two statements follow from computations with the matrix units $E_{kl}$; the last two are regroupings of indices.

## lay
Replacing an algebra by square matrices whose entries come from that algebra changes its size but not its essential character. The centre stays the same, simplicity is kept, matrices of matrices are just larger matrices, and a direct sum of algebras splits into a direct sum of matrix algebras.

## one-liner
Matrix amplification $A \mapsto \Mat_m(A)$ preserves the centre and simplicity, regroups nested matrix algebras, and distributes over direct sums.
