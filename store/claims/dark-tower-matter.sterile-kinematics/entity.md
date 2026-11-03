---
id: dark-tower-matter.sterile-kinematics
kind: claim
version: 4
title: The kinematics of the sterile towers
status: proved
region: dark-tower-matter
subject: dark-matter
tags:
- null-directions
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - std-algebra.sylvester-inertia@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:J1
  - id:J2
  - id:J3
- kind: check
  ref: check.py::check_sums_of_null_vectors
- kind: check
  ref: check.py::check_null_cone_connected
- kind: check
  ref: check.py::check_definite_has_no_null_vector
locators:
  paper: T14c
  number: Prop 10.1
  label: prop:sterile
  line: 845
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.sylvester-inertia where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for every non-null integer vector in a box of R^(2,2): complement signature by sign of Q and an explicit null decomposition; a loop of null vectors from n to -n, (1,3) control; definite (4,0), (0,4) have no null vector. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - one-relation.third-constant-conversion-constant-between-charts
    note: 'Removed the foundations paper''s speed lemma: the proof proves the connectedness of the (2,2)
      null cone directly and cites that lemma only as the corresponding statement for timelike sets (the
      referee flagged the locator as being about different sets), so it is a comparison, not a premise.
      Levels pass: levels written from scratch, keeping every condition and level qualifier of the formal
      statement.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - dark-tower-matter.imported-towers-their-types (motivated_by)
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Elementary signature facts proved directly and cited by nothing later (T14c is the last paper
      to treat the sterile towers); linked by lineage to the towers fact that identifies the sterile representatives
      as (2,2) and (4,0).
lineage:
  motivated_by:
  - dark-tower-matter.imported-towers-their-types
---

## formal
\begin{enumerate}
\item[(i)] In $\R^{2,2}$ the orthogonal complement of every non-null vector is nondegenerate and indefinite, so every vector, of either sign of $Q$, is a sum of two null vectors $v = (\tfrac{1}{2}v + w) + (\tfrac{1}{2}v - w)$ with $w \perp v$, $Q(w) = -Q(v)/4$; and the null cone minus the origin is connected, so it has no invariant future half.
\item[(ii)] In $\R^{4,0}$ (and $\R^{0,4}$) the only null vector is zero: there is no massless constituent, no time and no evolution.
\end{enumerate}

## technical
In $\R^{2,2}$ the orthogonal complement of every non-null vector is nondegenerate and indefinite, so every vector of either sign of $Q$ is a sum of two null vectors, $v = (\tfrac12 v + w) + (\tfrac12 v - w)$ with $w \perp v$ and $Q(w) = -Q(v)/4$; and the null cone minus the origin, $S^1 \times S^1 \times \R_{>0}$, is connected, so it has no invariant future half. In $\R^{4,0}$ and $\R^{0,4}$ the only null vector is zero: there is no massless constituent, no time and no evolution.

## lay
The two sterile towers cannot hold ordinary matter. In the one with two time and two space directions, massless pieces can add up to anything, and there is no consistent distinction between future and past. In the one with no time direction at all, nothing can be massless and nothing evolves.

## one-liner
In signature $(2,2)$ every vector is a sum of two null vectors and the null cone has no future half, while in $(4,0)$ and $(0,4)$ the only null vector is zero.
