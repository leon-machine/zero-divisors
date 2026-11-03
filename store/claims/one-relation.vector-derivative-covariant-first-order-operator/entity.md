---
id: one-relation.vector-derivative-covariant-first-order-operator
kind: claim
version: 4
title: The vector derivative is the covariant first-order operator
status: proved
region: one-relation
subject: one-relation
tags: [forcing-and-uniqueness]
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
review: typed
about:
- obj.std-algebra.spacetime-algebra
- obj.std-algebra.rotor
derivations:
- name: main
  uses:
  - std-algebra.pseudoscalar-commutation@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T16.py
  tags:
  - label:lem:vectorderivative
- kind: check
  ref: check.py::check_covariant_operators_span_gamma_and_gamma_i
- kind: check
  ref: check.py::check_constant_factor_is_invertible
- kind: check
  ref: check.py::check_right_multiplication_is_outside_the_class
locators:
  paper: T16
  number: Lem 5.1
  label: lem:vectorderivative
  line: 741
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.pseudoscalar-commutation, obj.std-algebra.spacetime-algebra, obj.std-algebra.rotor where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the 384 x 64 covariance system for six rational rotors has a two-dimensional kernel spanned by gamma^mu and gamma^mu I; gamma^mu (a + bI) = (a - bI) gamma^mu and (a - bI)(a + bI) = a^2 + b^2; right multiplication by noncentral B is not a left multiplication. Version 1 -> 2. Sample inputs moved to module level; by-hand mismatch count (4, from the non-central gamma_0) asserted. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'No edges; the proof is self-contained. Levels pass: the lay level''s closing inference now
      stays within the constant-coefficient, left-multiplication class.'
---

## formal
Let $D = A^{\mu}\partial_{\mu}$ be a first-order operator with constant coefficients $A^{\mu} \in \Cl(1,3)$ acting by left multiplication on $\Cl(1,3)$-valued fields on Minkowski space (hence on every minimal left ideal), and suppose $D$ is covariant under the spin group: $D(R\,\psi\circ\Lambda_{R}^{-1}) = R\,(D\psi)\circ\Lambda_{R}^{-1}$ for every rotor $R \in \mathrm{Spin}^{+}(1,3)$, $\Lambda_{R}$ its vector transformation. Then $A^{\mu} = \gamma^{\mu}(a + bI)$ for real $a, b$, with $I = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$ the pseudoscalar: $D = (a - bI)\nabla$ for the vector derivative $\nabla = \gamma^{\mu}\partial_{\mu}$, and $a - bI$ is invertible whenever $(a,b) \neq (0,0)$. Among covariant constant-coefficient first-order operators acting by left multiplication, the vector derivative is unique up to an invertible constant factor. (Right multiplications are outside the class: $\psi \mapsto \nabla\psi\,B$ for constant $B$ is covariant, and is not of the form $A^{\mu}\partial_{\mu}$ acting on the left unless $B$ is central.)

## technical
Let $D = A^{\mu}\partial_{\mu}$ have constant coefficients $A^{\mu} \in \Cl(1,3)$ acting by left multiplication on $\Cl(1,3)$-valued fields on Minkowski space, and suppose it is covariant under every rotor of $\mathrm{Spin}^{+}(1,3)$. Then $A^{\mu} = \gamma^{\mu}(a + bI)$ with $a, b$ real, so $D = (a - bI)\nabla$ with $\nabla = \gamma^{\mu}\partial_{\mu}$, and $a - bI$ is invertible unless $a = b = 0$.

So within this class the vector derivative is unique up to an invertible constant factor. Right multiplications $\psi \mapsto \nabla\psi\, B$ are covariant but lie outside the class unless $B$ is central.

## lay
Relativity requires a law to look the same to all observers. Among the simplest kinds of first-order derivative operator in the spacetime algebra, only one meets that requirement, up to a constant multiple: the vector derivative. So, within that class, the operator in the electron's equation is not a free choice.

## one-liner
Every spin-covariant, constant-coefficient, first-order operator acting by left multiplication on $\Cl(1,3)$-valued fields is an invertible constant times the vector derivative $\nabla = \gamma^{\mu}\partial_{\mu}$.
