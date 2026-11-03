---
id: sheaf.stability-reduction-strict-diagonal-case
kind: claim
version: 4
title: 'Stability: reduction to the strict-diagonal case'
status: proved
region: sheaf
subject: walls
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.sheaf.variable-order-algebra-strict-diagonal-data
- obj.sheaf.relatively-admissible-perturbation
derivations:
- name: main
  uses:
  - sheaf.boundary-units-invert@2
  - sheaf.variable-weight-boundary-tameness-completion-forced@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_congruence_to_diagonal_data
- kind: check
  ref: check.py::check_conclusions_hold_verbatim
locators:
  paper: T04
  number: Thm 9.5
  label: thm:stability
  line: 1214
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: at the u = 2 Kasner point, a unit congruence that is the identity on E reduces an admissible perturbation to diagonal data with units c_i (1 + O(w)), and the corank, first-order dying eigenvalue and (2,4) completion survive. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Kept both edges: unit inversion for the pivots and the variable-weight theorem whose conclusions
      are transferred. Levels pass: conditions already kept.'
---

## formal
For every relatively admissible $\Xi_\bullet$, the perturbed pair $(\shW, G + \Xi_\bullet)$ is congruent, by a transition in $GL_4(\mathcal{A})$ which is the identity on the exceptional boundary, to diagonal data over $\mathcal{A}$ with the \emph{same} exponents and perturbed unit entries $c_i' = c_i(1 + O(\tau^\delta))$, boundary units of $\mathcal{A}$ in the sense of Lemma \claimref{sheaf.boundary-units-invert} (smoothness of the units is not preserved, membership in $\mathcal{A}$ is). Consequently every conclusion of Theorem \claimref{sheaf.variable-weight-boundary-tameness-completion-forced} holds verbatim for the perturbed data: the same module, corank one with the same radical, dying eigenvalue of exactly first order in $\varrho$ with the unperturbed leading unit, the $(2,4)$ completion with no shadow wall, and the same pointwise-forced weights.

## technical
Perturb strict diagonal data by a relatively admissible error $\Xi_\bullet$. Then $(\shW, G + \Xi_\bullet)$ is congruent, by a transition in $GL_4(\mathcal{A})$ that is the identity on the exceptional boundary, to diagonal data over $\mathcal{A}$ with the same exponents and unit entries $c_i' = c_i(1 + O(\tau^\delta))$; these are boundary units of $\mathcal{A}$, though not necessarily smooth.

The proof diagonalises the nondegenerate block by symmetric Gaussian elimination with invertible pivots, then removes the dying-slot cross terms, leaving the Schur complement $\tilde d = -\varrho c_1 (1 + O(\tau^\delta))$. Since the variable-weight theorem used only that the units are positive boundary units, all its conclusions hold verbatim: the same module, corank one with the same radical, a first-order dying eigenvalue with the unperturbed leading unit, the $(2,4)$ completion with no shadow wall, and the same forced weights.

## lay
The results for the anisotropic singularity were first proved for an idealised, perfectly diagonal geometry. This result shows that perturbations of the admissible size can be undone by a change of frame, leaving data of the same idealised form. So every conclusion of the idealised case survives such perturbations unchanged.

## one-liner
Every relatively admissible perturbation of strict diagonal data is congruent to diagonal data with the same exponents and perturbed boundary units, so all conclusions of the variable-weight theorem hold verbatim.
