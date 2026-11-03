---
id: families.koide-nullity-condition-one-member-invariant
kind: claim
version: 2
title: Koide as a nullity condition, for one member of the invariant family
status: proved
region: families
subject: generations
tags:
- flavour-and-mixing
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
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:nullity
- kind: check
  ref: check.py::check_singlet_doublet_decomposition
- kind: check
  ref: check.py::check_invariant_forms_two_parameter_family
- kind: check
  ref: check.py::check_nullity_chain
- kind: check
  ref: check.py::check_lepton_vector_null_to_three_parts_per_million
locators:
  paper: T13
  number: Prop 5.3
  label: prop:nullity
  line: 710
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: singlet plus doublet, the two-parameter invariant forms and their signatures, the nullity chain, and q(v_lepton) to 3 parts in 10^6. Version 1 -> 2.'
  env: proposition
  context_refs:
  - families.chart-computation-sign-twist-bracket-form
  typing:
    by: ai-typing-pass
    note: 'No edges: the proof is elementary and self-contained, and the chart citation is a comparison;
      Foot''s 45-degree reading (Foot1994) is the same geometry but is not in the store as an imported
      claim, so no standard route was added. Levels pass: conditions already kept.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - families.chart-computation-sign-twist-bracket-form (motivated_by)
    - families.koide-instrument (motivated_by)
    - families.selectivity-observation-level (motivated_by)
    added_about: []
    verdict: connected
    note: Elementary and self-contained; its identity Q = 1/(3 cos^2 theta) and the null reading are what
      the chart computation, the instrument and the selectivity observations build on, recorded as their
      lineage since those are not proofs.
---

## formal
Face space decomposes under $S_{3}$ as singlet $\oplus$ doublet, with invariant coordinates $s = v \cdot u$ and $d = v - su$. The $S_{3}$-invariant quadratic forms are exactly the two-parameter family $q_{\alpha,\beta}(v) = \alpha s^{2} - \beta|d|^{2}$. For $\alpha, \beta > 0$ each has signature $(1, 2)$, face space read through it is a three-dimensional Minkowski space with the democratic direction timelike, and the equal split $s^{2} = |d|^{2}$ is precisely the statement that the family vector is \emph{null} for the equal-coefficient member $q(v) = s^{2} - |d|^{2}$:
\[
Q_{\sqrt{m}} = \tfrac23 \;\iff\; \cos^{2}\theta = \tfrac12 \;\iff\; s^{2} = |d|^{2} \;\iff\; q(v) = 0 .
\]
Numerically, $q(v_{\mathrm{lepton}}) = 0.0062$ against $|v|^{2} = 1883$: null to $3 \times 10^{-6}$ relative (Figure \ref{fig:lightcone}). Foot's $45^{\circ}$ reading \cite{Foot1994} is the same geometry in Euclidean language. The member $q$ is a choice: for $\beta < 0$ the same family is Euclidean, and Proposition \claimref{families.chart-computation-sign-twist-bracket-form} shows that the form the bracket construction supplies is the Euclidean member, while $S_{3}$-invariance alone singles out no member at all, so the light-cone reading is not forced by the framework; it is recorded here as the reading under which the most precise unexplained relation in flavour physics becomes a nullity statement, in the vocabulary in which the series' founding definition is that being null is the definition of being a point.

## technical
Face space splits under $S_{3}$ into the democratic singlet and a doublet, with invariant coordinates $s = v \cdot u$ and $d = v - su$. Writing $Q(d)$ for the Euclidean square of the doublet part, the invariant quadratic forms are exactly $q_{\alpha,\beta}(v) = \alpha s^{2} - \beta\,Q(d)$; for $\alpha, \beta > 0$ each has signature $(1,2)$, making face space a three-dimensional Minkowski space with the democratic direction timelike.

Since the Koide ratio is $1/(3\cos^{2}\theta)$, the relation $Q_{\sqrt{m}} = \tfrac23$ is equivalent to $s^{2} = Q(d)$, that is to the family vector being null for the equal-coefficient member $q(v) = s^{2} - Q(d)$; the lepton vector is null to $3 \times 10^{-6}$ relative. The member is a choice: the bracket construction supplies the Euclidean member and $S_{3}$-invariance alone selects none, so the light-cone reading is recorded, not forced.

## lay
The three family masses can be arranged as a vector, which splits into an average part and a part describing how the masses differ. The Koide relation turns out to say that these two parts have the same size. If length is measured with the rules of special relativity instead of ordinary geometry, that is the statement that the vector lies on a light cone. The paper stresses that this way of measuring is a choice not forced by the framework, though the charged leptons satisfy the condition to a few parts in a million.

## one-liner
The Koide relation is equivalent to the family vector being null for the equal-coefficient member $s^{2} - Q(d)$ of the $S_{3}$-invariant quadratic forms, a member that is chosen rather than forced.
