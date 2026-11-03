---
id: obj.tower.tower
kind: object
version: 1
title: The tower
status: defined
region: tower
subject: tower
tags: [hyperbolic-plane, ladder-pairs]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
review: typed
locators:
  paper: T03
  number: Def 2.2
  label: def:tower
  line: 185
extraction:
  env: definition
  typing:
    by: ai-typing-pass
    note: Definition; levels only.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - tower.algebraic-limit-even-charge
    - tower.car-limit-even-charge
    - tower.commuting-copies
    - tower.compatibility-connecting-maps-transported
    - tower.grade-twist-when-it-inner
    - tower.ladder-pairs-satisfy-car-vectors
    - tower.rigidity-clock-frozen
    - tower.structure-tower-c-norms
    - tower.witt-index-quantum-capacity
    - tower.fock-module-one-qubit-per-rung
    - tower.volume-elements-planes
    - q.tower.odd-charge
    - field-theory.ground-does-not-attach-modes
    - field-theory.how-close-tower-comes-ccr
    - field-theory.path-integral-inside-tower
    - odd-extensions.every-path-mirror-crosses-two-time
    added_about: []
    verdict: connected
    note: A definition cannot carry uses or assumes; the added links are about edges from the T03 results
      stated on the chain T_k, its planes and its transport charge, from the question on odd charge, and
      from the field-theory and odd-extension results that work with tower planes or the residue.
---

## formal
The \emph{tower} over $\Cl(p,q)$ is the chain of algebras $T_k := \Cl(p{+}k, q{+}k)$, $k \geq 0$, on the spaces $\R^{p,q} \perp H_1 \perp \cdots \perp H_k$ with $H_j = \operatorname{span}\{e_j, f_j\}$ orthogonal hyperbolic planes, together with the natural unital embeddings $\iota_k : T_k \hookrightarrow T_{k+1}$ induced by the inclusion of quadratic spaces. Write $v_j, w_j$ for the $j$-th null pair, $\omega_j := e_j f_j$ for the $j$-th plane's volume element, and $d := p - q \bmod 8$ for the \emph{transport charge}.

## technical
The tower over $\Cl(p,q)$ is the chain of algebras $T_k = \Cl(p+k, q+k)$, $k \geq 0$, built on $\R^{p,q} \perp H_1 \perp \cdots \perp H_k$, where each $H_j = \operatorname{span}\{e_j, f_j\}$ is a hyperbolic plane orthogonal to the others, together with the unital embeddings $\iota_k : T_k \hookrightarrow T_{k+1}$ induced by the inclusion of quadratic spaces.

Each plane carries a null pair $v_j, w_j$ and a volume element $\omega_j = e_j f_j$, and the transport charge of the tower is $d = p - q \bmod 8$.

## lay
The tower is the ladder of algebras obtained by repeatedly adding a pair of new directions, one of each sign, at right angles to everything before. Each algebra sits naturally inside the next. Each added pair can be recombined into two directions of zero length, and the difference between the numbers of the two kinds of direction, counted modulo eight, is the tower's charge.

## one-liner
The tower over $\Cl(p,q)$ is the chain $T_k = \Cl(p+k,q+k)$ obtained by adjoining orthogonal hyperbolic planes one at a time, with its natural embeddings, null pairs and transport charge $d = p - q \bmod 8$.
