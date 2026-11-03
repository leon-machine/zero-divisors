---
id: transport.type-p-self-repairing
kind: claim
version: 2
title: Type P is self-repairing
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
- obj.transport.equivariance
- obj.transport.extension-quadratic-spaces
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T01
  number: Prop 6.1
  label: prop:selfrepair
  line: 1361
extraction:
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'tautological proof, no edges Levels pass: conditions already kept.'
---

## formal
Let $A$ be any unital ring, $\mathcal{E}(A)$ its set of idempotents, and $A' \supseteq A$ any unital extension. The identity assignment
\[
\sigma : \mathcal{E}(A) \to A' , \qquad \sigma(e) = e,
\]
satisfies both von Neumann identities, $e\,\sigma(e)\,e = e$ and $\sigma(e)\,e\,\sigma(e) = \sigma(e)$, and is equivariant under \emph{every} ring automorphism of every extension: for any automorphism $\theta$ of $A'$ preserving $A$, $\sigma(\theta(e)) = \theta(\sigma(e))$ trivially. In the terminology of the taxonomy: the transport rule for type P is the identity, at signature increment $(0,0)$, and the repair is already present in the base algebra.

## technical
Let $A$ be any unital ring, $\mathcal{E}(A)$ its idempotents and $A' \supseteq A$ any unital extension. Taking each idempotent as its own partner, $\sigma(e) = e$, both von Neumann identities $e\,\sigma(e)\,e = e$ and $\sigma(e)\,e\,\sigma(e) = \sigma(e)$ hold because $e^3 = e$. The assignment commutes with every automorphism $\theta$ of $A'$ preserving $A$, since $\theta(e)$ is again an idempotent of $A$ and $\sigma$ is the identity.

In the obstruction taxonomy this says that the transport rule for type P, the non-central idempotents, is the identity at signature increment $(0,0)$: the repair is already present in the base algebra.

## lay
Some zero divisors are projection-like elements, ones that equal their own square. For these, the repair being sought is already available: each such element can serve as its own partner and satisfies the required identities. Because the rule is simply to take the element itself, it automatically respects every symmetry, so nothing needs to be added to the algebra.

## one-liner
In any unital ring the identity assignment $\sigma(e) = e$ on idempotents satisfies both von Neumann identities and is equivariant under every automorphism of every extension preserving the ring, so type P obstructions are repaired at signature increment $(0,0)$.
