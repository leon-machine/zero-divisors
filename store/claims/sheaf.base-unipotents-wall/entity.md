---
id: sheaf.base-unipotents-wall
kind: claim
version: 3
title: Base unipotents at the wall
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
- obj.three-routes.candidates-base-unipotents
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_unipotents_are_isometries_fixing_k
- kind: check
  ref: check.py::check_composition_and_translation_action
locators:
  paper: T04
  number: Lem 10.1
  label: lem:wallunipotents
  line: 1348
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: g_lambda isometric and fixing k on a GA wall fibre and the Schwarzschild wall, the composition law, and the translation action on transversals. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: "Self-contained lemma with no premises; no edges changed."
---

## formal
For $\lambda \in \ker k := \{v : k(v) = 0\}$ define $g_\lambda(\alpha) := \alpha + \alpha(\lambda)\,k$ on $T^*M$ at the wall point. Then $g_\lambda$ is a $G$-isometry, fixes $k$, and $g_\lambda g_{\lambda'} = g_{\lambda+\lambda'}$; the dual action on vectors is $u' \mapsto u' - k(u')\lambda$, hence on transversals ($k(u') = 1$) the translation $u' \mapsto u' - \lambda$, a free and transitive action of $(\ker k, +)$.

## technical
At a wall point let $k$ span the radical of $G$ on $T^*M$. For each vector $\lambda$ with $k(\lambda) = 0$, the map $g_\lambda(\alpha) = \alpha + \alpha(\lambda)\,k$ is a $G$-isometry fixing $k$, and $g_\lambda g_{\lambda'} = g_{\lambda+\lambda'}$. Dually it acts on vectors by $u' \mapsto u' - k(u')\lambda$, so on transversals, the vectors with $k(u') = 1$, it is the translation $u' \mapsto u' - \lambda$, and $(\ker k, +)$ acts on them freely and transitively.

## lay
At a point of the wall the geometry cannot see the dying direction, and this gives it extra symmetries: shears that add a multiple of the dying direction to any covector. These shears combine like ordinary addition. Acting on the directions that cross the wall, they move any one crossing direction to any other in exactly one way.

## one-liner
At a wall point the shears $g_\lambda(\alpha) = \alpha + \alpha(\lambda)\,k$, $\lambda \in \ker k$, are $G$-isometries fixing $k$ that act on transversals as a free and transitive group of translations.
