---
id: obj.transport.equivariance
kind: object
version: 1
title: Equivariance
status: defined
region: transport
subject: zero-divisors
tags: [rotors-and-stabilisers]
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
- obj.transport.extension-quadratic-spaces
locators:
  paper: T01
  number: Def 2.2
  label: def:equivariance
  line: 490
extraction:
  env: definition
  typing:
    by: ai-typing-pass
    note: 'Definition: levels only, no edge changes.'
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [transport.original-conjecture-refuted-below, transport.transport-principle, transport.transport-algorithm, transport.no-fourth-rule, transport.type-p-self-repairing, transport.cohomological-form-no-go, rungs.imported-totality-minimality-completion, rungs.fact-null-momenta-invite-one-rung, singularity.imported-no-c-number-repair, descent-lift.pairing-creator-under-transport-algorithm]
    added_about: []
    verdict: connected
    note: 'About from every statement that asserts or denies an equivariant element-level repair in the root paper sense; the base-unipotent equivariance of the wall theorems is a different notion and was not linked.'
---

## formal
Let $\mathbb{V}' \supseteq \mathbb{V}$ be an extension of quadratic spaces (Definition \claimref{obj.transport.extension-quadratic-spaces}) and $G$ a subgroup of $\Pin(p,q)$, acting on the null cone $\Ncone \subset \mathbb{V}$ by $\Ad$ (which preserves $\mathbb{V}$ and its null cone, being an isometry of $\mathbb{V}$) and on $\Cl(\mathbb{V}')$ by $\tau$ through the inclusion $\Cl(\mathbb{V}) \subseteq \Cl(\mathbb{V}')$. A map $\sigma : \Ncone \to \Cl(\mathbb{V}')$ is \emph{$G$-equivariant} if
\[
\sigma\bigl(\Ad_g(v)\bigr) \;=\; \tau_g\bigl(\sigma(v)\bigr) \qquad \text{for all } g \in G,\ v \in \Ncone .
\]

## technical
Given an extension $\mathbb{V}' \supseteq \mathbb{V}$ of quadratic spaces and a subgroup $G$ of $\Pin(p,q)$, the group acts on the null cone $\Ncone \subset \mathbb{V}$ by $\Ad$, which is an isometry of $\mathbb{V}$ and so preserves $\Ncone$, and acts on $\Cl(\mathbb{V}')$ by $\tau$ through the inclusion $\Cl(\mathbb{V}) \subseteq \Cl(\mathbb{V}')$. A map $\sigma : \Ncone \to \Cl(\mathbb{V}')$ is $G$-equivariant when $\sigma(\Ad_g(v)) = \tau_g(\sigma(v))$ for all $g \in G$ and all null $v$.

This is the sense in which a rule assigning an algebra element to each null vector is required to respect the symmetry of the geometry: transforming the input by $g$ transforms the output by the same $g$.

## lay
A rule that attaches something to each light-like direction is called equivariant if it does not depend on how the geometry is oriented. Moving the geometry by a symmetry and then applying the rule gives the same answer as applying the rule first and then moving the answer. The symmetries are those of the original space, acting also on the algebra of any enlargement of it.

## one-liner
A map from the null cone into the Clifford algebra of an extension is $G$-equivariant when it intertwines the action of $G \subseteq \Pin(p,q)$ on null vectors with its action on the algebra.
