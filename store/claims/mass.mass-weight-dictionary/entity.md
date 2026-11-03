---
id: mass.mass-weight-dictionary
kind: claim
version: 4
title: The mass-weight dictionary
status: proved
region: mass
subject: mass
tags: [refutation, frozen-point, dictionaries, mass-generation]
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
review: typed
derivations:
- name: main
  uses:
  - mass.imported-frozen-point-tractor-connection@6
  - mass.imported-thomas-operator@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:thm:dictionary
- kind: check
  ref: check.py::check_mass_is_minus_w_w_plus_n_minus_one_times_norm
- kind: check
  ref: check.py::check_four_dimensions_in_lambda_and_frozen_point
locators:
  paper: T11
  number: Thm 3.1
  label: thm:dictionary
  line: 448
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Thomas tractor paired with the frozen point as Clifford vectors gives m^2 = -w(w+n-1) Q(I) on a 144-point grid and -w(w+3) Lambda/3 in n = 4. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: theorem
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added:
    - mass.imported-thomas-operator
    note: 'The proof pairs $I$ with the slots of $D\sigma$ and says it works from the two Facts, so the Thomas operator Fact was added; the paper notes agreement with the de Sitter mass formula but that import does not derive the coupling, so no standard-route was added here.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - mass.imported-thomas-operator
---

## formal
Let $\sigma$ be a density of conformal weight $w$ on a vacuum Einstein background with frozen point $I$, and impose the coupling
\[
I \cdot D\sigma = 0.
\]
Then, in the scale of $I$, $\sigma$ obeys the Klein-Gordon equation $(\Box + m^{2})\sigma = 0$ with
\begin{equation}
m^{2} = -\,w(w+n-1)\,Q(I), \qquad\text{in } n = 4:\quad m^{2} = -\,w(w+3)\,\frac{\Lambda}{3} = -\,w(w+3)\,H^{2}.
\end{equation}
The mass of a field is its conformal weight, read in the units the frozen point provides, and every mass in the theory is $\sqrt{\Lambda}$ times a factor fixed by the weight.

## technical
Let $\sigma$ be a density of conformal weight $w$ on a vacuum Einstein background with frozen point $I$, and impose $I \cdot D\sigma = 0$, with $D$ the Thomas operator. In the scale of $I$ this is the Klein-Gordon equation $(\Box + m^{2})\sigma = 0$ with $m^{2} = -w(w+n-1)Q(I)$, which in four dimensions reads $m^{2} = -w(w+3)\Lambda/3 = -w(w+3)H^{2}$.

So a field's mass is its conformal weight read in the units the frozen point supplies, and every mass in the theory is $\sqrt{\Lambda}$ times a factor fixed by the weight.

## lay
The framework has exactly one built-in scale, set by the cosmological constant. This theorem shows that a field coupled to that scale in the natural way behaves as a particle with a definite mass, fixed by a single number the field carries, its conformal weight. In that sense every mass is the cosmological scale multiplied by a number determined by the weight.

## one-liner
A density of weight $w$ with $I \cdot D\sigma = 0$ obeys the Klein-Gordon equation with $m^{2} = -w(w+3)H^{2}$ in four dimensions.
