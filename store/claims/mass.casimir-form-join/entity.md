---
id: mass.casimir-form-join
kind: claim
version: 7
title: The Casimir form of the join
status: proved
region: mass
subject: mass
tags: [frozen-point, representation-theory, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 7
  source: maintainer pass 2026-11-07 (GA units)
review: typed
about:
- obj.mass.grip-mass-composite
derivations:
- name: main
  uses:
  - mass.chart-form-spin-isomorphism@5
  - mass.exact-join@8
  - mass.imported-flat-model-twistor-chart-infinity@7
  - mass.invariant-forms-simple-lie-algebra@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:prop:casimir
- kind: check
  ref: check.py::check_grip_norm_is_difference_of_casimirs
- kind: check
  ref: check.py::check_grip_norm_casimirs_negative_lambda_and_one_spinor
- kind: check
  ref: check.py::check_conformal_casimir_is_trace_form
- kind: check
  ref: check.py::check_de_sitter_casimir_closed_form
locators:
  paper: T11
  number: Prop 5.7
  label: prop:casimir
  line: 766
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The chart''s complex unit, which the proof''s convention line already read as I_6 but wrote i, is now written I_6: on the moment element''s spinor values on the right (W -> sum Z (Zbar . W) I_6), on numbers (traces) read in span{1, I_6}; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Q(P) = Q(I)(C2 - C2(I-perp)) at three non-null I for 1 to 3 spinors, C2(Lambda^2 CS) = tr h^2 - (tr h)^2/4, and the closed de Sitter Casimir for two spinors. Version 5 -> 6.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'the moment element M = i sum Z (Zbar . ): its i is the chart''s complex unit, set to I6 by the earlier GA pass (twistor unit, kept distinct from I4)'
  env: proposition
  context_refs:
  - mass.imported-unitary-representations-de-sitter-group
  eqrefs: 3
  typing:
    by: ai-typing-pass
    added:
    - mass.exact-join
    note: 'Part (3) combines (1) and (2) with the exact join''s mass formula, so the exact join was added; the E301 cycle with the invariant-forms lemma is broken on the lemma''s side, and the de Sitter representation Fact is a normalisation comparison only.'
  source_title: 'The Casimir form of the join'
  source_formal: |-
    Fix a composite $Z^{1}, \dots, Z^{N}$ with Hermitian Gram matrix $h_{il} = \bar{Z}^{i}\cdot Z^{l}$. For a nondegenerate subspace $W$ of the ambient space with basis $(e_{\alpha})$ and inverse Gram matrix $(g^{\alpha\beta})$, put $M_{\alpha\beta} := M_{e_{\alpha}\wedge e_{\beta}}$ and $C_{2}(W) := \tfrac12\, g^{\alpha\alpha'}g^{\beta\beta'}M_{\alpha\beta}M_{\alpha'\beta'}$, the quadratic Casimir of the rotations of $W$ evaluated on the composite; $C_{2}(\Lambda^{2}\T)$ is the conformal Casimir $C_{2}(\mathfrak{so}(2,4))$ of the composite, and for the frozen point $C_{2}(I_{\Lambda}^{\perp})$ is its de Sitter Casimir $C_{2}(\mathfrak{so}(1,4))$, both as quadratic forms on the moment components (this normalisation differs from the scalar-module one of Fact \claimref{mass.imported-unitary-representations-de-sitter-group} by the conformal Casimir, as (1) shows). Let $I$ be a nonzero non-null ambient vector and $P = M(I)$ the grip of Definition \claimref{obj.mass.grip-mass-composite}. Then:
    \begin{enumerate}
    \item $\ip{P}{P} = \ip{I}{I}\,\bigl(C_{2}(\Lambda^{2}\T) - C_{2}(I^{\perp})\bigr)$;
    \item $C_{2}(\Lambda^{2}\T) = \tr(h^{2}) - \tfrac14(\tr h)^{2}$, for any number of constituents;
    \item hence, for two twistors, $I = I_{\Lambda}$ and $\Lambda \neq 0$, the de Sitter Casimir of the composite is
    \[
    C_{2}(I_{\Lambda}^{\perp}) = \tfrac14(\tr h)^{2} + C - \frac{6\,|B_{\Lambda}|^{2}}{\Lambda}.
    \]
    \end{enumerate}
  correction:
    by: ai-correction
    date: '2026-10-22'
    note: 'Removed the stipulation that the moment normalisation of C_2(I^perp) differs from the scalar-module one by the conformal Casimir. A normalisation is an overall scale, not an additive shift by another Casimir; the scale is fixed by C_2(Lambda^2 CS) = tr h^2 - (1/4)(tr h)^2. Quantised on one conformal spinor of helicity s, C_2(Lambda^2 CS) and C_2(I_Lambda^perp) are 3(s^2 - 1) and 2(s^2 - 1) in units of hbar^2, the standard conformal and de Sitter Casimirs, with no shift (synthesis.operator-join-casimir-shifts, awaiting review). Under the old stipulation the conformally invariant scalar (homogeneity -2) would have m^2 = -H^2, which is no unitary scalar representation of SO(1,4) by the cited Fact and contradicts mass.mass-weight-dictionary (2H^2 at w = -1). Clauses (1)-(3) and the proof are unchanged; the statement now says that the grip equals the de Sitter mass plus <I,I> C_2(Lambda^2 CS).'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Twistor space \T is now the conformal spinor space \CS throughout (Casimir C_2(Lambda^2 CS), sl(CS)), the constituents are conformal spinors, and the proof''s chart halves \Sc, \Sc'' are written \Som, \Spi; a convention line reads the moment element''s i as I6. The computation is unchanged.'
---

## formal
Fix a composite $Z^{1}, \dots, Z^{N}$ of conformal spinors with Hermitian Gram matrix $h_{il} = \bar{Z}^{i}\cdot Z^{l}$. For a nondegenerate subspace $W$ of the ambient space with basis $(e_{\alpha})$ and inverse Gram matrix $(g^{\alpha\beta})$, put $M_{\alpha\beta} := M_{e_{\alpha}\wedge e_{\beta}}$ and $C_{2}(W) := \tfrac12\, g^{\alpha\alpha'}g^{\beta\beta'}M_{\alpha\beta}M_{\alpha'\beta'}$, the quadratic Casimir of the rotations of $W$ evaluated on the composite; $C_{2}(\Lambda^{2}\CS)$ is the conformal Casimir $C_{2}(\mathfrak{so}(2,4))$ of the composite, and for the frozen point $C_{2}(I_{\Lambda}^{\perp})$ is its de Sitter Casimir $C_{2}(\mathfrak{so}(1,4))$, both as quadratic forms on the moment components; in this normalisation $C_{2}(I_{\Lambda}^{\perp})$ is the de Sitter Casimir of the scalar-module convention of Fact \claimref{mass.imported-unitary-representations-de-sitter-group} (acting as $-m^{2}/H^{2}$). Let $I$ be a nonzero non-null ambient vector and $P = M(I)$ the grip of Definition \claimref{obj.mass.grip-mass-composite}. Then:
\begin{enumerate}
\item $Q(P) = Q(I)\,\bigl(C_{2}(\Lambda^{2}\CS) - C_{2}(I^{\perp})\bigr)$;
\item $C_{2}(\Lambda^{2}\CS) = \tr(h^{2}) - \tfrac14(\tr h)^{2}$, for any number of constituents;
\item hence, for two conformal spinors, $I = I_{\Lambda}$ and $\Lambda \neq 0$, the de Sitter Casimir of the composite is
\[
C_{2}(I_{\Lambda}^{\perp}) = \tfrac14(\tr h)^{2} + C - \frac{6\,|B_{\Lambda}|^{2}}{\Lambda}.
\]
\end{enumerate}
Consequently (1) says that the grip $Q(P)$ equals the de Sitter mass $-Q(I)\,C_{2}(I^{\perp})$ plus $Q(I)\,C_{2}(\Lambda^{2}\CS)$, and the two coincide only where the conformal Casimir vanishes.

## technical
For a composite with Hermitian Gram matrix $h$ and a nondegenerate subspace $W$ of the ambient space, $C_{2}(W)$ is the quadratic Casimir of the rotations of $W$ evaluated on the composite's moment components. For a nonzero non-null ambient vector $I$ with grip $P = M(I)$, the grip's length splits the conformal Casimir: $Q(P) = Q(I)\bigl(C_{2}(\Lambda^{2}\CS) - C_{2}(I^{\perp})\bigr)$, and the conformal Casimir is $C_{2}(\Lambda^{2}\CS) = \tr(h^{2}) - \tfrac14(\tr h)^{2}$ for any number of constituents.

For two conformal spinors, $I = I_{\Lambda}$ and $\Lambda \neq 0$, the de Sitter Casimir of the composite is $C_{2}(I_{\Lambda}^{\perp}) = \tfrac14(\tr h)^{2} + C - 6|B_{\Lambda}|^{2}/\Lambda$. These Casimirs are quadratic forms on moment components, and in this normalisation $C_{2}(I_{\Lambda}^{\perp})$ is the de Sitter Casimir of the scalar-module convention, acting as $-m^{2}/H^{2}$. So the grip equals the de Sitter mass plus $Q(I)$ times the conformal Casimir, and the two coincide only where the conformal Casimir vanishes, as on the massless locus, where $h = 0$.

## lay
The mass of a composite can be read in the language of symmetry. A composite carries charges under the whole conformal group and under the smaller de Sitter group picked out by the cosmological constant. Its mass squared is proportional to the difference between the two corresponding Casimir invariants: the part of its conformal charge that the cosmological scale breaks. This mass is not in general the mass read from the de Sitter symmetry alone: the two differ by the composite's conformal invariant times the cosmological scale, and agree only where that invariant vanishes.

## one-liner
The squared grip of a composite is $Q(I)$ times the conformal Casimir minus the Casimir of $I^{\perp}$, with $C_{2}(\Lambda^{2}\CS) = \tr(h^{2}) - \tfrac14(\tr h)^{2}$; it equals the de Sitter mass $-Q(I)C_{2}(I^{\perp})$ only where the conformal Casimir vanishes.
