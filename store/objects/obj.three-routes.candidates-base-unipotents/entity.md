---
id: obj.three-routes.candidates-base-unipotents
kind: object
version: 2
title: Candidates, and the base unipotents
status: defined
region: three-routes
subject: singularity
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
review: typed
about:
- obj.sheaf.collar-data-coupling
locators:
  paper: T05-three-routes
  number: Def 3.1
  label: def:candidates
  line: 176
extraction:
  typing:
    by: ai-typing-pass
    note: 'definition only: the coupling construction it mentions is context, so no edges were added.'
  env: definition
  context_refs:
  - three-routes.imported-collar-data-coupling
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [sheaf.base-unipotents-wall, sheaf.no-equivariant-value-wall, singularity.imported-no-equivariant-value-wall]
    added_about: [obj.sheaf.collar-data-coupling]
    verdict: connected
    note: 'Judgement call: the T4 lemma and theorem and the T5 Fact that define and use the same candidate values and base unipotents were linked by about, though the definition is the three-routes restatement.'
---

## formal
A \emph{candidate value} for the dying direction $k$ is a transversal: a vector $u$ with $k(u) = 1$, exactly the datum a classical reciprocal of $k$ would supply and exactly the datum the coupling construction consumes (Fact \claimref{three-routes.imported-collar-data-coupling}). The candidates form an affine space over $\ker k := \{v : k(v) = 0\}$, of dimension three. For $\lambda \in \ker k$ define the \emph{base unipotent} $g_\lambda : W \to W$, $g_\lambda(\alpha) := \alpha + \alpha(\lambda)\,k$.

## technical
At a boundary point where the covector $k$ spans the radical of the degenerate form on $W$, a candidate value for $k$ is a transversal: a vector $u$ with $k(u) = 1$. This is exactly the datum a classical reciprocal of $k$ would supply and exactly the datum the coupling construction consumes. The candidates form an affine space of dimension three over $\ker k = \{v : k(v) = 0\}$.

For each $\lambda \in \ker k$ the base unipotent is the map $g_\lambda : W \to W$, $g_\lambda(\alpha) = \alpha + \alpha(\lambda)\,k$, which shears covectors along the dying direction $k$.

## lay
When a direction in the geometry degenerates, an ordinary inverse would supply a partner vector that pairs with it to give one. Any vector with that property counts as a candidate, and there is a whole three-dimensional family of them, any two differing by a vector the dying direction does not see. For each such difference vector there is a base unipotent, a simple shear that adds a multiple of the dying direction.

## one-liner
A candidate value for the dying direction $k$ is a vector $u$ with $k(u) = 1$, and for each $\lambda \in \ker k$ the base unipotent is $g_\lambda(\alpha) = \alpha + \alpha(\lambda)\,k$.
