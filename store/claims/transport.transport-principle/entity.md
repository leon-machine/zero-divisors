---
id: transport.transport-principle
kind: claim
version: 4
title: Transport principle
status: proved
region: transport
subject: completion
tags: [obstruction-types, transport-algorithm, forcing-and-uniqueness, classification]
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
- obj.transport.transport
- obj.transport.obstruction-types
- obj.transport.equivariance
- obj.transport.extension-quadratic-spaces
derivations:
- name: main
  uses:
  - transport.cohomological-form-no-go@4
  - transport.embedding-independent-minimality-fusion@4
  - transport.exhaustiveness-every-zero-divisor-annihilated-idempotent@3
  - transport.minimality@4
  - transport.no-fourth-rule@4
  - transport.no-go-level-elements@4
  - transport.one-generator-minimal-minimal-completions-classified@5
  - transport.representation-independent-minimality-completion@4
  - transport.rule-2-ideal-fusion-sharp-form@4
  - transport.totality@3
  - transport.type-p-self-repairing@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_isotropic_vector_repaired_on_points
- kind: check
  ref: check.py::check_central_idempotent_repaired_one_dimension_up
- kind: check
  ref: check.py::check_non_central_idempotent_is_its_own_repair
- kind: check
  ref: check.py::check_trichotomy_exhaustive_on_samples
locators:
  paper: T01
  number: Principle 8.2
  label: pri:transport
  line: 1568
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the three cases (point repair at null vectors with the (+1,+1) plane, fusion one dimension up, idempotents as their own repair) and exhaustiveness on samples. Version 2 -> 3. check_central_idempotent_repaired_one_dimension_up: tautological dimension assert replaced by a computed isomorphism of the nu^2 = +1 and -1 completions (nu -> w nu, rank of words); minimality wording removed from the docstring. Version 3 -> 4.'
  env: principle
  flags:
  - 'summary principle: derivation is its cited theorems'
  typing:
    by: ai-typing-pass
    note: 'Kept all eleven cited theorems, since the principle is the conjunction of the results it names.'
---

## formal
Division fails in a real Clifford algebra of nondegenerate form in exactly three ways, and each carries a forced minimal repair.
\begin{itemize}
\item \emph{At an isotropic vector} the repair is impossible for the element and total for the point. No equivariant element-level repair exists in the Clifford algebra of any extension (Theorems \claimref{transport.no-go-level-elements}, \claimref{transport.cohomological-form-no-go}); the reciprocal nevertheless extends totally, continuously and uniquely on the space of points, in a completion whose increment $(+1,+1)$ is forced both as a lift and as an ambient quadric (Theorems \claimref{transport.totality}, \claimref{transport.minimality}, \claimref{transport.representation-independent-minimality-completion}).
\item \emph{At a central idempotent} the repair is available at the level of elements, one dimension up: the adjoined generator renders the grade involution inner, the ideals fuse, and the completion is unique up to isomorphism and minimal among all simple real algebras (Theorems \claimref{transport.rule-2-ideal-fusion-sharp-form}, \claimref{transport.one-generator-minimal-minimal-completions-classified}, \claimref{transport.embedding-independent-minimality-fusion}).
\item \emph{At a non-central idempotent} no repair is needed: the element is its own (Proposition \claimref{transport.type-p-self-repairing}).
\end{itemize}
The trichotomy is exhaustive (Theorem \claimref{transport.exhaustiveness-every-zero-divisor-annihilated-idempotent}), so there is no fourth case (Corollary \claimref{transport.no-fourth-rule}); in each case the cost is independent of how the algebra is represented, and is exactly what the obstruction requires. \emph{Complete the space when the obstruction is a direction, the algebra when it is a splitting, and nothing when the element is already its own repair.}

## technical
In a real Clifford algebra of nondegenerate form, division fails in exactly three ways, each with a forced minimal repair. At an isotropic vector, $Q(v) = 0$, no equivariant element-level repair exists in the Clifford algebra of any extension, yet the reciprocal extends totally, continuously and uniquely on the space of points, in a completion whose increment $(+1,+1)$ is forced both as a lift and as an ambient quadric. At a central idempotent, one adjoined generator renders the grade involution inner and fuses the ideals, and the completion is unique up to isomorphism and minimal among all simple real algebras. At a non-central idempotent no repair is needed: the element is its own.

The trichotomy is exhaustive, so there is no fourth case, and in each case the cost does not depend on how the algebra is represented. In short: complete the space when the obstruction is a direction, the algebra when it is a splitting, and nothing when the element is already its own repair.

## lay
Division can go wrong in a Clifford algebra in exactly three ways. For a light-like direction the element itself cannot be fixed, but adding one extra pair of dimensions repairs the space of points; for an algebra split into two halves, adding one dimension fuses them; for an ordinary projection, nothing needs fixing. Each repair is the smallest possible, and the list is complete.

## one-liner
Division in a nondegenerate real Clifford algebra fails in exactly three ways, at an isotropic vector, a central idempotent or a non-central idempotent, and each has a forced minimal repair: complete the space, complete the algebra, or do nothing.
