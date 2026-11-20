---
id: synthesis.premise-the-bit
kind: claim
version: 2
title: 'Premise (F1): the bit'
status: postulate
region: synthesis
subject: clifford-structure
tags: [grading-and-parity]
proposed_by:
  kind: ai
  session: 2026-11-07-bit-root
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-bit-root
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 2
  source: run 2026-11-08-foundation-layer
review: draft
foundation: true
lineage:
  motivated_by:
  - synthesis.blade-square-signs-f2-quadratic-form
locators:
  paper: T00a
  number: Premise (F1)
  line: 119
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Marked as a foundation postulate. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  env: premise
  note: >-
    The source document calls this primitive (B); the store names the four foundation postulates F1 to F4. From Leon's working document "From the Bit to the Numbers" (7 November 2026), Steps 0 and 1:
    the first of the four chosen primitives of the foundation (the bit, minimal non-commutativity,
    superposition, completion), with the independence of Step 1 included as the document says
    ("the bit, repeated"). Proposed as a root premise of the series' algebra; no stored entity
    assumes it, and whether the existing algebra is re-rooted on it through assumes edges is a
    decision for Leon. The counting of configurations by grade is a consequence, stated for
    orientation. Prior art, from memory: G. Spencer-Brown, Laws of Form (1969), the law of crossing (to cross
    twice is not to cross), which is the analogue of 1 + 1 = 0; his other law, calling, is idempotent
    (Boolean, 1 + 1 = 1), so only crossing, not Laws of Form as a whole, matches F_2.
---

## formal
\emph{Premise (F1), the bit.} The foundation takes as primitive a single distinction with two states, written $0$ (nothing) and $1$ (something), combined by comparison: making a distinction and making it again returns to nothing, $1 + 1 = 0$. With the product $1 \cdot 1 = 1$ (both made) and $0$ otherwise, the states form the two-element field $\mathbb{F}_{2}$. Distinctions are independent: for $n \ge 0$ distinctions a configuration is the set $S \subseteq \{1, \dots, n\}$ of those made, and configurations combine by comparison, the symmetric difference $S \triangle T$. So the configurations form the vector space $\mathbb{F}_{2}^{n}$, with $2^{n}$ elements, $\binom{n}{k}$ of them containing $k$ distinctions.

\emph{Status and cost.} A chosen primitive of the foundation, mathematical and not physical: it posits a structure, the two-element field and its finite powers, and asserts nothing about the world. Nothing beneath it is available to derive it from. What it does not contain: a sign ($1 = -1$ in $\mathbb{F}_{2}$, so a distinction cannot be told from its reversal), an order between distinctions (comparison is commutative), and any magnitude or geometry; the sign and the order enter with the premise of minimal non-commutativity, superposition with the premise of superposition over the integers. No observation bears on it; what can fail is the reading that the algebra of physics is built on it, which is argued and not proved.

## technical
The root of the series' algebra is a single distinction: two states, $0$ and $1$, combined by comparison, so that $1 + 1 = 0$; with the product it is the field $\mathbb{F}_{2}$. Repeating it independently $n$ times, a configuration is the set of distinctions made, and configurations combine by symmetric difference, giving $\mathbb{F}_{2}^{n}$: $2^{n}$ configurations, graded by how many distinctions they contain, which is the counting of the blades of a geometric algebra before any geometry. The premise is mathematical, a choice of starting structure. It carries no sign, since $1 = -1$ in $\mathbb{F}_{2}$, no order and no geometry; those come from the later premises.

## lay
This is the starting assumption of the whole construction, and it is a choice about mathematics, not a claim about nature: the simplest possible difference, something versus nothing, where doing the same thing twice undoes it. Many such differences, independent of one another, give a collection of on-off patterns. These patterns already have the shape of the algebra of directions used throughout the series, but none of its geometry yet: no sign, no order and no lengths.

## one-liner
Premise (F1): the foundation's primitive is one distinction, the two-element field $\mathbb{F}_{2}$ ($1 + 1 = 0$), repeated independently, so the configurations of $n$ distinctions are $\mathbb{F}_{2}^{n}$ under symmetric difference; a mathematical choice with no sign, order or geometry.
