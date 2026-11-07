---
id: three-routes.change-transversal-canonical-isomorphism-completions
kind: claim
version: 6
title: Change of transversal is a canonical isomorphism of completions
status: proved
region: three-routes
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
  source: 'authorship disclosure of T05-three-routes, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 6
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - three-routes.imported-collar-data-coupling@1
  - three-routes.radical-gauge-closes-solve@5
  - std-algebra.functoriality@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_three_routes.py
  tags:
  - num:3.4
- kind: check
  ref: check.py::check_intertwiner_on_boundary_data
- kind: check
  ref: check.py::check_normalised_representative_is_choice_free
- kind: check
  ref: check.py::check_ladder_carried_to_ladder
locators:
  paper: T05-three-routes
  number: Thm 3.4
  label: thm:intertwiner
  line: 200
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Decision item E6 (routine; no retirement): specialises sheaf.transversal-independence-wall@4 added. The sheaf result is the general statement and the home; this one is its case.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.functoriality where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Phi^T h_u Phi = h_(u+v) on Schwarzschild boundary data at four masses with control, choice-freeness of the normalised representative, and ladder carried to ladder. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - three-routes.imported-collar-data-coupling
    - three-routes.radical-gauge-closes-solve
    note: 'Added the coupling fact and the radical-gauge lemma named in the statement, both used in the
      five pairing computations. Levels pass: conditions already kept.'
  env: theorem
  context_refs:
  - three-routes.imported-collar-data-coupling
  - three-routes.radical-gauge-closes-solve
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - three-routes.imported-collar-data-coupling
    - three-routes.radical-gauge-closes-solve
specialises:
- sheaf.transversal-independence-wall@4
---

## formal
Fix collar constants $\mu, \nu$ and let $h_u$ denote the ambient form built from the transversal $u$ (Fact \claimref{three-routes.imported-collar-data-coupling}). For $v \in \ker k$ let $\tilde v$ be as in Lemma \claimref{three-routes.radical-gauge-closes-solve}, and define the unipotent map $\Phi_v$ on $T = W \oplus \operatorname{span}(\nO, \nInf)$:
\[
\Phi_v\big|_W = \id, \qquad \Phi_v(\nO) = \nO + \nu\,\tilde v, \qquad \Phi_v(\nInf) = \nInf + \mu\,\tilde v .
\]
Then $h_u(\Phi_v x, \Phi_v y) = h_{u+v}(x, y)$ for all $x, y$: $\Phi_v$ is an isometry $(T, h_{u+v}) \to (T, h_u)$ restricting to the identity on $W$, fixing $k$, and inducing an isomorphism of the completed Clifford algebras that carries ladder to ladder. The completion is therefore independent of the collar transversal, canonically over the degenerate base.

## technical
Fix collar constants $\mu, \nu$ and write $h_u$ for the ambient form built from the transversal $u$. For $v \in \ker k$ take the normalised covector $\tilde v$ with $G(\alpha, \tilde v) = \alpha(v)$ for all $\alpha$ and $G(\tilde v, \tilde v) + 2\tilde v(u) = 0$, and define $\Phi_v$ on $T = W \oplus \operatorname{span}(\nO, \nInf)$ as the identity on $W$, with $\Phi_v(\nO) = \nO + \nu\,\tilde v$ and $\Phi_v(\nInf) = \nInf + \mu\,\tilde v$.

Then $h_u(\Phi_v x, \Phi_v y) = h_{u+v}(x, y)$ for all $x, y$, so $\Phi_v$ is an isometry from $(T, h_{u+v})$ to $(T, h_u)$ that is the identity on $W$, fixes $k$, and induces an isomorphism of the completed Clifford algebras carrying ladder to ladder. The completion is therefore independent of the collar transversal, canonically over the degenerate base.

## lay
Completing the degenerate geometry at the boundary needs an auxiliary choice of transverse direction. This result shows the choice does not matter: completions built from different choices are related by an explicit, canonical map that preserves all the structure, including the paired ladder directions. So the completion is one object, not a family depending on the choice.

## one-liner
Completions built from different collar transversals are identified by an explicit unipotent isometry that fixes $k$ and carries ladder to ladder, so the completion is canonically independent of the transversal.
