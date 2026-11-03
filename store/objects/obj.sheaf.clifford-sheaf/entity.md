---
id: obj.sheaf.clifford-sheaf
kind: object
version: 1
title: The Clifford sheaf
status: defined
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
locators:
  paper: T04
  number: Def 2.7
  label: def:cliffordsheaf
  line: 443
extraction:
  env: definition
  context_refs:
  - sheaf.blade-basis-degenerate-forms-included
  typing:
    by: ai-typing-pass
    note: "Object: levels only."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [dark-energy.imported-walls-sphere-theorem, sheaf.degeneration-sheaf, sheaf.localised-transport, sheaf.wall-fibre-black-hole]
    added_about: []
    verdict: connected
    note: 'About from the statements written in the sheaf Cl(T*M, G); the completed sheaf of the three-routes note is a different object and was not linked.'
---

## formal
For a cometric $G$ on $M$, the \emph{Clifford sheaf} $\shA = \Cl(T^*M, G)$ is the sheaf of $\mathcal{O}_M$-algebras ($\mathcal{O}_M$ the sheaf of smooth real functions) whose local sections are smooth sections of the bundle of algebras $\coprod_{x} \Cl(T^*_xM, G_x)$, with the local trivialisations induced by blade frames: a local frame $e_1, \dots, e_n$ of $T^*M$ induces the fibrewise blade bases $\{e_I(x)\}$ of Lemma \claimref{sheaf.blade-basis-degenerate-forms-included}.

## technical
Given a cometric $G$ on $M$, possibly degenerate, the Clifford sheaf $\shA = \Cl(T^*M, G)$ is the sheaf of $\mathcal{O}_M$-algebras whose local sections are smooth sections of the bundle of fibre algebras $\Cl(T^*_xM, G_x)$. Smoothness is defined through blade frames: a local frame $e_1, \dots, e_n$ of $T^*M$ gives at each point the blade basis $\{e_I(x)\}$, which is a basis whether or not $G_x$ is degenerate, and these bases supply the local trivialisations.

## lay
At each point of a space one can build a Clifford algebra, an algebra of directions, from the way the geometry measures covectors. The Clifford sheaf gathers all of these algebras into one smoothly varying object over the whole space. Because the basis used to glue them together works even where the measurement degenerates, the construction does not stop where the geometry fails.

## one-liner
The Clifford sheaf of a cometric $G$ is the sheaf of smooth sections of the fibrewise Clifford algebras $\Cl(T^*_xM, G_x)$, trivialised by blade frames.
