---
id: obj.dark-tower-matter.ideals-fields-momentum
kind: object
version: 1
title: Ideals, fields and momentum
status: defined
region: dark-tower-matter
subject: dark-matter
tags:
- idempotents
- spinor-modules
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
locators:
  paper: T14c
  number: Def 3.1
  label: def:ideals
  line: 243
extraction:
  env: definition
  context_refs:
  - dark-tower-matter.constituents-field
  typing:
    by: ai-typing-pass
    note: 'Definition; no edges. Levels pass: levels written from scratch, keeping every condition and
      level qualifier of the formal statement.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - dark-tower-matter.u-transposition-rule (about)
    added_about: []
    verdict: connected
    note: Added about from Premise U, whose clauses use the constituent ideal, its field and momentum
      preservation.
---

## formal
Let $\hf$ be a primitive idempotent of $\Cl^{0}(\hatV)$, and in a causal tower let $f = \tfrac{1}{2}(1 + e_{t}e_{a})$ for a space direction $e_{a}$, which is a primitive idempotent of $\Cl^{0}(V)$ in dimensions three to five (Theorem \claimref{dark-tower-matter.constituents-field}); in the sterile towers $f$ is any primitive idempotent of $\Cl^{0}(V)$. The \emph{constituent ideal} is $T = \Cl^{0}(\hatV)\hf$ and the \emph{spinor ideal} is $S = \Cl^{0}(V)f$. Their \emph{fields} are the commutants $\F(T) = \mathrm{End}_{\Cl^{0}(\hatV)}(T)$ and $\F(S) = \mathrm{End}_{\Cl^{0}(V)}(S)$, the latter realised as right multiplication by the corner algebra $f\Cl^{0}(V)f$. In a causal tower the \emph{adjoint} is $x^{\dagger} = e_{t}\rev{x}e_{t}^{-1}$, and the \emph{momentum} of $\psi \in S$ is
\[
j(\psi) \;=\; \ip{\psi e_{t} \rev{\psi}}_{1}.
\]
The total momentum of constituents $\psi_{1}, \ldots, \psi_{n}$ is $P = \sum_{i} j(\psi_{i})$, and its \emph{squared mass} is $m^{2} = Q(e_{t})\,Q(P)$.

## technical
With $\hf$ a primitive idempotent of $\Cl^0(\hatV)$ and, in a causal tower, $f = \tfrac12(1 + e_te_a)$ for a space direction $e_a$ (any primitive idempotent of $\Cl^0(V)$ in the sterile towers), the constituent ideal is $T = \Cl^0(\hatV)\hf$ and the spinor ideal is $S = \Cl^0(V)f$. Their fields are the commutants $\F(T)$ and $\F(S)$, the latter realised as right multiplication by the corner algebra $f\Cl^0(V)f$.

In a causal tower the adjoint is $x^\dagger = e_t\rev{x}e_t^{-1}$, the momentum of $\psi \in S$ is $j(\psi) = \langle \psi e_t\rev{\psi}\rangle_1$, and constituents $\psi_1, \ldots, \psi_n$ have total momentum $P = \sum_i j(\psi_i)$ and squared mass $m^2 = Q(e_t)\,Q(P)$.

## lay
This definition fixes the basic objects of the dark-tower note. A constituent lives in a minimal piece of an even Clifford algebra, of the tower's conformal algebra or of the tower itself, and its numbers are the operations that commute with the algebra's action there. Its momentum is a vector built from the spinor and the time direction, and the mass of a collection comes from the length of its total momentum.

## one-liner
Defines the constituent ideal $T$, the spinor ideal $S$, their fields, the adjoint $e_t\rev{x}e_t^{-1}$, the momentum $j(\psi) = \langle \psi e_t\rev{\psi}\rangle_1$ and the squared mass $Q(e_t)\,Q(P)$.
