---
id: dark-matter.residue-soldered-invariant-not-algebraic-one
kind: claim
version: 3
title: The residue is a soldered invariant, not an algebraic one
status: proved
region: dark-matter
subject: clifford-structure
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
  - dark-matter.type-residue-what-each-tower-can@5
  - std-algebra.sylvester-inertia@1
  - primer.classification-real-clifford-algebras@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:thm:soldered
- kind: check
  ref: check.py::check_signature_is_read_off_the_generating_subspace
- kind: check
  ref: check.py::check_abstract_isomorphisms_not_soldered
- kind: check
  ref: check.py::check_this_world_and_r4_are_mat2_quaternions
locators:
  paper: T14
  number: Thm 3.5
  label: thm:soldered
  line: 195
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.sylvester-inertia, primer.classification-real-clifford-algebras where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Sylvester signature of v -> v^2 on V under basis changes (n <= 4); explicit abstract isomorphisms for residues 0~2, 7~3, 6~4 with different generating-subspace signatures; Cl(1,3) = Cl(0,4) = Mat_2(H) exhibited. Version 1 -> 2.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Kept the edge to the type-and-residue theorem, which supplies the invariants for (ii); Sylvester''s
      law is not a store claim, and P1 appears only in the closing gloss, not as a hypothesis, so it is
      not assumed. Levels pass: the lay now keeps ''at equal dimension''.'
---

## formal
Let $(A, V)$ denote a Clifford algebra together with its generating vector subspace $V \subset A$ (the soldering: $V$ is the image of the metric's tangent space, and $v^{2} = g(v,v)$ for $v \in V$). Then:
\begin{enumerate}
\item[(i)] any algebra isomorphism $(A, V) \to (A', V')$ carrying $V$ onto $V'$ preserves the signature $(p,q)$, hence the residue: the residue is an invariant of the soldered algebra;
\item[(ii)] as abstract algebras, residues $0$ and $2$, $3$ and $7$, and $4$ and $6$ are pairwise isomorphic at equal dimension, $\Cl(1,1) \cong \Cl(2,0)$, $\Cl(1,2) \cong \Cl(3,0)$, $\Cl(1,3) \cong \Cl(0,4) \cong \Mat(2, \mathbb{H})$; in particular this world's algebra and the $r = 4$ tower's are the same algebra, and no isomorphism between them carries vectors to vectors.
\end{enumerate}
So the tower charge is an invariant of the operator algebra soldered to the metric, not of the algebra: what forbids a portal in Section \ref{sec:count} is the one metric, P1.

## technical
Regard a Clifford algebra together with its generating vector subspace, $(A, V)$, as soldered to a metric: $V$ is the image of the tangent space and $Q(v) = g(v,v)$ for $v \in V$. An algebra isomorphism carrying $V$ onto $V'$ carries one quadratic form to the other, so by Sylvester's law it preserves the signature $(p,q)$ and hence the residue: the residue is an invariant of the soldered algebra.

As abstract algebras, however, residues $0$ and $2$, $3$ and $7$, and $4$ and $6$ coincide at equal dimension: $\Cl(1,1) \cong \Cl(2,0)$, $\Cl(1,2) \cong \Cl(3,0)$ and $\Cl(1,3) \cong \Cl(0,4) \cong \Mat(2,\HH)$, and no isomorphism between the members of a pair carries vectors to vectors. So this world's algebra and the $r = 4$ tower's are the same algebra, and the tower charge belongs to the algebra soldered to the metric, not to the algebra alone.

## lay
Each tower of possible matter is labelled by a number, its residue, which comes from how many directions are time-like and how many space-like. This result shows that the label only has meaning once the algebra is tied to the geometry of spacetime. As bare algebras, some different towers are exactly the same at the same dimension, for example our world's algebra and that of one dark tower. What tells them apart is which elements count as directions, and that is fixed by the metric.

## one-liner
The residue is preserved by every isomorphism carrying vectors to vectors, but not by abstract algebra isomorphisms, under which residues $0$ and $2$, $3$ and $7$, and $4$ and $6$ coincide at equal dimension.
