---
id: sheaf.log-obstruction
kind: claim
version: 4
title: The log obstruction
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
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_chain_rule_formulas
- kind: check
  ref: check.py::check_algebra_and_stability
- kind: check
  ref: check.py::check_log_is_a_jordan_block
locators:
  paper: T04
  number: Lem 9.7
  label: lem:logobstruction
  line: 1234
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: both chain-rule formulas derived from the exponential series in x with log coefficients, the algebra and its stability, and the Jordan-block form of tau^e log tau under tau d/dtau. Version 2 -> 3. Sample inputs moved to module level; no change to what is tested. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'No edges: the proof is the chain rule plus a self-contained exponent-raising argument. Levels
      pass: conditions already kept.'
---

## formal
For $e$ smooth on $E$,
\[
\tau\partial_\tau\,\tau^{e(x)} \;=\; e(x)\,\tau^{e(x)},
\qquad
\partial_x\,\tau^{e(x)} \;=\; e'(x)\,\tau^{e(x)}\log\tau .
\]
Consequently $\mathcal{A}$ is a commutative algebra stable under $\tau\partial_\tau$; it is stable under tangential vector fields if and only if every exponent is locally constant; and the obstruction is genuine: if $e'(x_0) \neq 0$ then $\tau^{e(x)}\log\tau$ does not lie in $\mathcal{A}$ near $(x_0,0)$.

## technical
For a smooth exponent $e$, $\tau\partial_\tau\, \tau^{e(x)} = e(x)\,\tau^{e(x)}$ and $\partial_x\, \tau^{e(x)} = e'(x)\,\tau^{e(x)}\log\tau$. So the variable-order algebra $\mathcal{A}$ is a commutative algebra stable under $\tau\partial_\tau$, but it is stable under tangential vector fields only if every exponent is locally constant.

The obstruction is genuine: if $e'(x_0) \neq 0$ then $\tau^{e(x)}\log\tau$ does not lie in $\mathcal{A}$ near $(x_0,0)$. The proof supposes an expansion in an admissible family of powers, removes the negative powers one at a time, and reaches the contradiction that $\log\tau$ would be bounded near $\tau = 0$.

## lay
Powers of the distance to a boundary, with the power varying from point to point, behave well when one differentiates towards the boundary. Differentiating along the boundary instead produces a logarithm, and that logarithm cannot be rewritten in terms of such powers. So the algebra of these powers is closed under all derivatives only when the powers are locally constant.

## one-liner
Tangential derivatives of $\tau^{e(x)}$ produce $e'(x)\,\tau^{e(x)}\log\tau$, which lies outside the variable-order algebra wherever $e' \neq 0$, so the algebra is stable under tangential fields only for locally constant exponents.
