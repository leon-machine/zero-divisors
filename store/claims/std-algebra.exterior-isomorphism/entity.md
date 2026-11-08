---
id: std-algebra.exterior-isomorphism
kind: claim
version: 2
title: The outer product is the exterior algebra
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- classical-theorem
- degenerate-algebras
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'maintainer pass, citation of the retired imported Fact repointed to its derivation in geometric algebra'
  version: 2
  source: run 2026-11-07-bit-root
review: typed
trust: ai-proposed
about:
- obj.std-algebra.outer-product
derivations:
- name: main
  uses:
  - std-algebra.blade-basis@1
  - std-algebra.grade-decomposition@2
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.existence-uniqueness@1
  - synthesis.completion-recovers-the-real-clifford-algebras@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_outer_product_is_exterior
locators:
  sources:
  - key: Chevalley1954
    locator: Ch. II (the Clifford algebra of a quadratic space)
  - key: Lounesto2001
    locator: Ch. 22 (Chevalley's construction)
  - key: Lounesto2001
    locator: Ch. 3 (bivectors and the exterior algebra)
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 7 November 2026: the imported Fact std-algebra.sylvester-inertia is retired, replaced by synthesis.completion-recovers-the-real-clifford-algebras, whose clause (iii) derives Sylvester's law of inertia in geometric algebra over any Euclidean field, the reals included; the citation and edge now point there. The check's premise() call names the new result; nothing else changed.
  by: algebra-core-2026-10-26
---

## formal
The outer product makes $\Cl(V, Q)$ an associative unital graded algebra, and there is a unique algebra isomorphism
\begin{equation}
\Phi : (\Lambda V, \wedge) \longrightarrow (\Cl(V, Q), \wedge), \qquad \Phi(v) = v,
\end{equation}
which maps $\Lambda^{k} V$ onto $\Cl^{k}$. For vectors, $v_1 \wedge \dots \wedge v_k = [v_1, \dots, v_k]$, the antisymmetrised product, and $v \wedge v = 0$. $\Phi^{-1}$ is the symbol map $x \mapsto x \cdot 1$ of the exterior model of \claimref{std-algebra.existence-uniqueness}. In an orthogonal basis, $e_I \wedge e_J$ is $e_I e_J$ when $I \cap J = \emptyset$ and $0$ otherwise. The outer product does not depend on $Q$: as a graded algebra, $(\Cl(V, Q), \wedge)$ is the same for every quadratic form on $V$, degenerate ones included.

## technical
With the outer product alone, the Clifford algebra is the exterior (Grassmann) algebra of $V$: the identity on vectors extends to an isomorphism of graded algebras, the outer product of vectors is their antisymmetrised geometric product, and it ignores the quadratic form entirely. The inverse isomorphism is the symbol map of the exterior model. In an orthogonal basis, the outer product of two blades is their geometric product if they share no index and zero otherwise.

## lay
If you keep only the "new directions" part of every product, you get the older algebra of oriented areas and volumes invented by Grassmann, and the length rule disappears from it completely. The Clifford product adds the length rule back on top of this.

## one-liner
$(\Cl(V, Q), \wedge) \cong (\Lambda V, \wedge)$ as graded algebras, by the identity on $V$; $v_1 \wedge \dots \wedge v_k = [v_1, \dots, v_k]$ and $\wedge$ does not depend on $Q$.
