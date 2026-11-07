---
id: three-routes.base-unipotents-their-action-candidates
kind: claim
version: 5
title: The base unipotents, and their action on candidates
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
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.three-routes.candidates-base-unipotents
derivations:
- name: main
  uses:
  - three-routes.imported-boundary-gram-ladder@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_unipotents_are_isometries_fixing_k
- kind: check
  ref: check.py::check_dual_action_translates_candidates
locators:
  paper: T05-three-routes
  number: Lem 3.2
  label: lem:unipotents
  line: 180
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Decision item E6 (routine; no retirement): equivalent_to sheaf.base-unipotents-wall@3 added. The same result as the sheaf entity, which is kept as the home.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for 27 lambdas at two masses, g_lambda is a G-isometry fixing k with the composition law, and its dual action translates candidates freely and transitively. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - three-routes.imported-boundary-gram-ladder
    note: 'Added the boundary Gram fact, since the isometry computation uses that k spans the radical
      of G; linked the candidates definition as about. Levels pass: conditions already kept.'
  env: lemma
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - three-routes.imported-boundary-gram-ladder
equivalent_to:
- sheaf.base-unipotents-wall@3
---

## formal
Each $g_\lambda$ is a $G$-isometry of $W$ at the boundary, fixes $k$, and $g_\lambda g_{\lambda'} = g_{\lambda + \lambda'}$. The dual action on vectors is $u \mapsto u - k(u)\,\lambda$; on candidates it is the translation $u \mapsto u - \lambda$, a free and transitive action of $(\ker k, +)$.

## technical
At a boundary point, let $W$ carry the degenerate Gram $G$ whose radical is spanned by $k$. For $\lambda \in \ker k$ the base unipotent is $g_\lambda(\alpha) = \alpha + \alpha(\lambda)k$. Each $g_\lambda$ preserves $G$, because every correction term contains a pairing $G(\cdot, k)$, which vanishes; it fixes $k$; and $g_\lambda g_{\lambda'} = g_{\lambda + \lambda'}$.

On vectors the dual action is $u \mapsto u - k(u)\,\lambda$. Restricted to candidates, the vectors with $k(u) = 1$, it is the translation $u \mapsto u - \lambda$, a free and transitive action of the additive group $(\ker k, +)$.

## lay
At the boundary the geometry is degenerate in one direction, and there is a family of simple transformations that leave the geometry and that direction unchanged. These transformations shift every candidate for the missing partner by a fixed amount. Any candidate can be reached from any other this way, and none is left in place.

## one-liner
The base unipotents are isometries of the degenerate boundary Gram that fix $k$, and they act on candidate values as free, transitive translations by $\ker k$.
