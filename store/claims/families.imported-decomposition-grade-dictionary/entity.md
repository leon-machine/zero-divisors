---
id: families.imported-decomposition-grade-dictionary
kind: claim
version: 1
title: 'Imported: the decomposition of $16 \otimes 16$ and the grade dictionary'
status: imported
region: families
subject: generations
tags: [classical-theorem, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
imported_from:
- citation: R. Slansky, Group theory for unified model building, Phys. Rep. 79 (1981) 1--128.
  key: Slansky1981
locators:
  paper: T13
  number: Fact 8.5
  label: fact:decomp
  line: 939
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported from the literature with no derivations; only the levels were written.
---

## formal
For the positive-chirality spinor $16$ of $\mathrm{Spin}(10)$, $16 \otimes 16 = 10 \oplus 120 \oplus 126$, the $10$ and the $126$ symmetric and the $120$ antisymmetric. In the Clifford algebra of the ten the odd grades carry the representations $1 \leftrightarrow 10$, $3 \leftrightarrow 120$ and $5 \leftrightarrow 126 \oplus \overline{126}$, the grade-five space splitting into its self-dual and anti-self-dual halves; of these only the self-dual half, the $126$, pairs the positive-chirality $16$ with itself, and the $\overline{126}$ acts as zero in any $\mathrm{Spin}(10)$-equivariant bilinear form on the $16$. \emph{Provenance:} \cite{Slansky1981}; standard representation theory, not proved in the series. The script checks purity of grade five and the symmetry and entries of the induced form, not the decomposition.

## technical
For the positive-chirality spinor $16$ of $\mathrm{Spin}(10)$, $16 \otimes 16 = 10 \oplus 120 \oplus 126$, with the $10$ and the $126$ symmetric and the $120$ antisymmetric. In the Clifford algebra of the ten the odd grades carry $1 \leftrightarrow 10$, $3 \leftrightarrow 120$ and $5 \leftrightarrow 126 \oplus \overline{126}$, the grade-five space splitting into its self-dual and anti-self-dual halves.

Only the self-dual half, the $126$, pairs the $16$ with itself; the $\overline{126}$ acts as zero in any $\mathrm{Spin}(10)$-equivariant bilinear form on the $16$. This is standard representation theory imported from the literature and not proved in the series.

## lay
When two copies of the sixteen-component matter multiplet of the unified symmetry group are combined, the result breaks into three standard pieces, of sizes ten, one hundred and twenty, and one hundred and twenty-six. Each piece corresponds to a definite grade of element in the underlying Clifford algebra: one, three or five. This lets one tell which piece an operator feeds simply by reading off its grade. The fact is textbook group theory taken from the literature.

## one-liner
For $\mathrm{Spin}(10)$, $16 \otimes 16 = 10 \oplus 120 \oplus 126$, the odd Clifford grades one, three and five carry the $10$, the $120$ and the $126 \oplus \overline{126}$, and only the $126$ pairs the $16$ with itself.
