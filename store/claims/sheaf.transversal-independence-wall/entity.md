---
id: sheaf.transversal-independence-wall
kind: claim
version: 4
title: Transversal independence at the wall
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
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.solve-closed-radical-gauge@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:10.3
- kind: check
  ref: check.py::check_phi_is_unipotent_isometry_fixing_cotangent
- kind: check
  ref: check.py::check_intertwiners_compose
- kind: check
  ref: check.py::check_ladder_partner_and_parity_images
locators:
  paper: T04
  number: Thm 10.3
  label: thm:transversal
  line: 1364
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Phi_v^T h_u Phi_v = h_(u+v) with unipotence and control, the cocycle, and the images of k* and sigma in the exterior model. Version 3 -> 4.'
  env: theorem
  context_refs:
  - sheaf.solve-closed-radical-gauge
  typing:
    by: ai-typing-pass
    added: [sheaf.solve-closed-radical-gauge]
    note: "Added the radical-gauge solve, whose normalisation and linearity the isometry and cocycle checks use."
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.solve-closed-radical-gauge
---

## formal
Fix $\mu, \nu$ and write $h_u$ for the ambient form of Definition \claimref{obj.sheaf.collar-data-coupling} built from the transversal $u$. For $v \in \ker k$, with $\tilde v$ normalised as in Lemma \claimref{sheaf.solve-closed-radical-gauge}, the unipotent map
\[
\Phi_v\big|_{T^*M} = \id, \qquad \Phi_v(\nO) = \nO + \nu\tilde v, \qquad \Phi_v(\nInf) = \nInf + \mu\tilde v
\]
satisfies $h_u(\Phi_v x, \Phi_v y) = h_{u+v}(x, y)$: it is an isometry $(T, h_{u+v}) \to (T, h_u)$ restricting to the identity on $T^*M$, fixing $k$, inducing an isomorphism of the completed Clifford algebras that preserves the grading and is the identity on the degeneration subalgebra. Writing $\Phi^u_v$ for the map built on the base transversal $u$, the intertwiners compose: $\Phi^u_v \circ \Phi^{u+v}_w = \Phi^u_{v+w}$. The completion at the wall is therefore independent of the collar transversal, canonically: the completions built on all transversals are identified by one coherent system of isomorphisms. What that system preserves is the form, the grading and the degeneration subalgebra; it preserves neither the named frame nor the ladder pair, $\Phi_v(k^*) = k^* + \tfrac12\tilde v$ and $\Phi_v(\sigma) = \sigma + \tilde v k$ for the parity element $\sigma := k^*k - kk^*$, so the ladder partner of the completion built on $u + v$ is, seen in $(T, h_u)$, a different partner of the same $k$.

## technical
Fix $\mu, \nu$ and write $h_u$ for the ambient form built from the transversal $u$. For $v \in \ker k$, with $\tilde v$ the normalised solve, the unipotent map $\Phi_v$ that is the identity on $T^*M$ and sends $\nO \mapsto \nO + \nu\tilde v$, $\nInf \mapsto \nInf + \mu\tilde v$ satisfies $h_u(\Phi_v x, \Phi_v y) = h_{u+v}(x,y)$. It is an isometry fixing $k$, inducing a grading-preserving isomorphism of the completed Clifford algebras that is the identity on the degeneration subalgebra, and these maps compose coherently: $\Phi^u_v \circ \Phi^{u+v}_w = \Phi^u_{v+w}$.

So the completion at the wall is canonically independent of the collar transversal. The identifications preserve the form, the grading and the degeneration subalgebra, but not the named frame or the ladder pair: $\Phi_v(k^*) = k^* + \tfrac12\tilde v$, and the parity element $\sigma = k^*k - kk^*$ goes to $\sigma + \tilde v k$.

## lay
Building the repair of a degenerate wall requires choosing an auxiliary direction. This result shows that different choices give repairs which are identified with one another by explicit, mutually compatible maps. The overall structure therefore does not depend on the choice, although particular elements picked out inside it do.

## one-liner
Explicit unipotent isometries, composing coherently, identify the completions built on all collar transversals, preserving form, grading and degeneration subalgebra but not the ladder partner.
