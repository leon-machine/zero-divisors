---
id: one-relation.imported-witts-extension-theorem
kind: claim
version: 3
title: 'Imported: Witt''s extension theorem'
status: imported
region: one-relation
subject: clifford-structure
tags: [witt-index, classical-theorem]
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
- name: Claude Opus 5.5
  role: 'consistency pass, citation typo (journal title)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: typed
imported_from:
- citation: E. Witt, Theorie der quadratischen Formen in beliebigen Koerpern, J. Reine Angew. Math. 176
    (1937) 31--44.
  key: Witt1937
- citation: T. Y. Lam, Introduction to Quadratic Forms over Fields, Graduate Studies in Mathematics 67,
    American Mathematical Society (2005).
  key: Lam2005
  locator: Ch.~I, \S4
locators:
  paper: T16
  number: Fact 2.11
  label: fact:witt
  line: 546
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Citation typo: a lost backslash left K"orpern; written Koerpern as in std-algebra.witt-extension.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-extension (equivalent_to) where the proof uses them. Version 1 -> 2.'
  env: fact
  context_refs:
  - one-relation.third-constant-conversion-constant-between-charts
  - one-relation.two-capacities-three-consequences
  typing:
    by: ai-typing-pass
    note: Imported classical theorem, no derivation edges.
equivalent_to:
- std-algebra.witt-extension@2
---

## formal
Let $(V, Q)$ be a nondegenerate quadratic space over a field of characteristic not two, and let $\sigma : U \to U'$ be an isometry between two subspaces of $V$ carrying the restricted forms. Then $\sigma$ extends to an isometry of $(V, Q)$. Consequently the isometry group $O(V, Q)$ acts transitively on the subspaces of any one isometry type, in particular on the hyperbolic planes, and in any two Witt decompositions $V = H \perp A$, $H$ hyperbolic of maximal dimension, the anisotropic parts $A$ are isometric (Witt's cancellation theorem). \emph{Provenance:} \cite{Witt1937}; \cite[Ch.~I, \S4]{Lam2005}. It is the whole content of Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}(ii) and of the uniqueness clause of Proposition \claimref{one-relation.two-capacities-three-consequences}(1); the script exhibits witnesses (hyperbolic planes of $(1,3)$ with isometric complements) and does not check the theorem.

## technical
Witt's extension theorem: in a nondegenerate quadratic space $(V,Q)$ over a field of characteristic not two, any isometry $\sigma : U \to U'$ between subspaces, for the restricted forms, extends to an isometry of all of $V$. Hence $\mathrm{O}(V,Q)$ acts transitively on the subspaces of any one isometry type, in particular on hyperbolic planes.

A consequence is Witt cancellation: in any two decompositions $V = H \perp A$ with $H$ hyperbolic of maximal dimension, the anisotropic parts $A$ are isometric.

## lay
Witt's theorem concerns a space with a fixed rule for measuring lengths. It says that any length-preserving match between two pieces of the space extends to a length-preserving symmetry of the whole space, so pieces that look alike from the inside are also indistinguishable from the outside. It is a classical result from the 1930s.

## one-liner
Over a field of characteristic not two, every isometry between subspaces of a nondegenerate quadratic space extends to the whole space, so the isometry group is transitive on subspaces of each isometry type.
