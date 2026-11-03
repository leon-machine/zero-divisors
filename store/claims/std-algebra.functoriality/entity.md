---
id: std-algebra.functoriality
kind: claim
version: 1
title: Isometries extend to algebra homomorphisms
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- rotors-and-stabilisers
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  - std-algebra.blade-basis@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_isometry_extends_multiplicatively
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
  - key: Chevalley1954
    locator: Ch. II (the Clifford algebra of a quadratic space)
extraction:
  by: algebra-core-2026-10-26
---

## formal
An isometry $f : (V, Q) \to (W, Q')$ extends to a unique unital algebra homomorphism $\Cl(f) : \Cl(V, Q) \to \Cl(W, Q')$ with $\Cl(f)(v) = f(v)$. It is injective when $f$ is, and $\Cl(g \circ f) = \Cl(g) \circ \Cl(f)$. In particular the orthogonal group $\mathrm{O}(V, Q)$ acts on $\Cl(V, Q)$ by automorphisms, and the inclusion of a subspace $U \subseteq V$ gives an embedding $\Cl(U, Q|_U) \hookrightarrow \Cl(V, Q)$.

## technical
Any length-preserving linear map between quadratic spaces extends to exactly one homomorphism of their Clifford algebras, and composition is respected. An injective isometry gives an injective homomorphism. So symmetries of the space act on the algebra, and the algebra of a subspace sits inside the algebra of the whole space.

## lay
If a map of arrows preserves square lengths, it automatically extends to a map of the whole algebra that respects multiplication. Symmetries of space therefore act on everything built from arrows.

## one-liner
An isometry $f$ extends uniquely to an algebra homomorphism $\Cl(f)$, injective when $f$ is; $\mathrm{O}(V, Q)$ acts by automorphisms.
