---
id: transport.existence-locus-type-p
kind: claim
version: 6
title: Existence locus of type P
status: proved
region: transport
subject: zero-divisors
tags: [obstruction-types, idempotents]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.classification-real-clifford-algebras@3
  - transport.exceptional-division-algebras@3
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_noncentral_idempotent_exactly_off_the_five
- kind: check
  ref: check.py::check_idempotents_of_the_five_are_central
- kind: check
  ref: check.py::check_orthogonal_vector_pair_gives_type_p
locators:
  paper: T01
  number: Prop 3.8
  label: prop:typeP
  line: 630
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.orthogonal-anticommute where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: a non-central idempotent exists exactly off the five exceptional signatures for n <= 6 (matching k >= 2 in the d-table), idempotents of the five are central, and orthogonal vector pairs with a^2 b^2 < 0 give (1 + ab/|ab|)/2. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - transport.classification-real-clifford-algebras
    note: Added the classification of real Clifford algebras, which the proof invokes directly for the
      matrix-algebra case and for existence in every listed signature.
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - transport.classification-real-clifford-algebras
---

## formal
$\Cl(p,q)$ contains a non-central idempotent if and only if it is not a direct sum of division algebras, that is, if and only if
\[
(p,q) \;\notin\; \{(0,0),\ (0,1),\ (0,2),\ (1,0),\ (0,3)\} .
\]
In particular, for $n \geq 2$ with $(p,q) \notin \{(0,2), (0,3)\}$, type P is always present, and concretely: any invertible vector pair $a, b$ with $a \cdot b = 0$ and $a^2 b^2 = -1$ (one timelike and one spacelike factor) yields the non-central idempotent $\tfrac12(1 + u)$ with $u = ab$, since then $(ab)^2 = -a^2b^2 = +1$, and every unit blade $u$ with $u^2 = 1$, $u \neq \pm 1$, $u$ non-central yields one.

## technical
$\Cl(p,q)$ contains a non-central idempotent exactly when it is not a direct sum of division algebras, that is when $(p,q) \notin \{(0,0), (0,1), (0,2), (1,0), (0,3)\}$. In particular, for $n \geq 2$ with $(p,q) \notin \{(0,2), (0,3)\}$ type P is always present.

Concretely, orthogonal invertible vectors $a, b$ with $Q(a)Q(b) = -1$, one timelike and one spacelike, give $u = ab$ with $u^2 = -Q(a)Q(b) = 1$ and hence the non-central idempotent $\tfrac12(1 + u)$; more generally every non-central unit blade $u$ with $u^2 = 1$, $u \neq \pm 1$, yields one.

## lay
An element that equals its own square but does not commute with everything is a type-P obstruction. Such elements exist in every real Clifford algebra except five small ones built from the real numbers, the complex numbers and the quaternions. A simple recipe produces one from a space-like and a time-like direction at right angles.

## one-liner
A real Clifford algebra contains a non-central idempotent exactly when it is not a direct sum of division algebras, which excludes only five small signatures.
