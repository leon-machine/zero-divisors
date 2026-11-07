---
id: three-routes.no-equivariant-value-boundary
kind: claim
version: 4
title: No equivariant value at the boundary
status: proved
region: three-routes
subject: walls
tags: [no-go]
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
  version: 4
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.three-routes.candidates-base-unipotents
derivations:
- name: main
  uses:
  - three-routes.base-unipotents-their-action-candidates@5
  - three-routes.change-transversal-canonical-isomorphism-completions@6
  - three-routes.imported-collar-data-coupling@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_three_routes.py
  tags:
  - num:3.5
- kind: check
  ref: check.py::check_theta_is_automorphism_of_completed_structure
- kind: check
  ref: check.py::check_dual_action_is_free_translation
locators:
  paper: T05-three-routes
  number: Thm 3.5
  label: thm:nogo
  line: 212
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Decision item E6 (routine; no retirement): specialises sheaf.no-equivariant-value-wall@5 added. The sheaf result is the general statement and the home; this one is its case.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: theta is an automorphism of (T,h_u) restricting to g_lambda and fixing k, with dual action a free translation of candidates, on Schwarzschild boundary data. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    added:
    - three-routes.change-transversal-canonical-isomorphism-completions
    - three-routes.imported-collar-data-coupling
    note: 'Added the intertwiner theorem, whose inverse is a factor of the automorphism, and the coupling
      fact used in the isometry computation; the later transcription of this result at the wall was not
      added, since it restates this theorem rather than supporting it. Levels pass: conditions already
      kept.'
  env: theorem
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - three-routes.change-transversal-canonical-isomorphism-completions
    - three-routes.imported-collar-data-coupling
specialises:
- sheaf.no-equivariant-value-wall@5
---

## formal
For each base unipotent $g_\lambda$ let $\hat g_\lambda := g_\lambda \oplus \id$ on $T$. Then
\[
\theta_\lambda \;:=\; \hat g_\lambda \circ \Phi_\lambda^{-1}
\]
is an automorphism of the fixed completed structure $(T, h_u)$, restricting to $g_\lambda$ on $W$ and fixing $k$; its induced dual action on candidate values is the translation $u' \mapsto u' - \lambda$. Consequently any assignment of a classical partner value at the boundary that is natural under automorphisms of the completed structure would be a fixed point of a free translation action of $(\ker k, +)$ on the candidates, and none exists: \emph{no equivariant classical value repairs the dying direction at $\Sig$ itself}.

## technical
For a base unipotent $g_\lambda$, $\lambda \in \ker k$, set $\hat g_\lambda = g_\lambda \oplus \id$ on $T$. It is an isometry from $(T, h_{u+\lambda})$ to $(T, h_u)$, and composing with the inverse intertwiner gives $\theta_\lambda = \hat g_\lambda \circ \Phi_\lambda^{-1}$, an automorphism of the fixed completed structure $(T, h_u)$ that restricts to $g_\lambda$ on $W$ and fixes $k$.

Its dual action on candidate values is the translation $u' \mapsto u' - \lambda$. A classical partner value assigned naturally under automorphisms of the completed structure would have to satisfy $\hat u = \hat u - \lambda$ for every $\lambda \in \ker k$, which fails for $\lambda \neq 0$. So no equivariant classical value repairs the dying direction at $\Sig$ itself.

## lay
At the black-hole boundary one direction has lost its partner, and one could try to supply a definite classical replacement. The completed structure has symmetries that move every candidate replacement, so a choice respecting those symmetries would have to stay put while being moved. That is impossible, so no such classical repair exists at the boundary itself.

## one-liner
Automorphisms of the completed structure translate candidate values freely by $\ker k$, so no automorphism-equivariant classical value repairs the dying direction at $\Sig$.
