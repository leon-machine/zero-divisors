---
id: obj.std-algebra.even-subalgebra
kind: object
version: 1
title: Even and odd parts
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- grading-and-parity
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
- obj.std-algebra.grade-projection
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
$\Cl^{+}(V, Q) = \bigoplus_{k \text{ even}} \Cl^{k}$ and $\Cl^{-}(V, Q) = \bigoplus_{k \text{ odd}} \Cl^{k}$. $\Cl^{+}$ is the \emph{even subalgebra}; its elements are \emph{even}, those of $\Cl^{-}$ \emph{odd}. They are the $+1$ and $-1$ eigenspaces of the grade involution.

## technical
The even part collects the even grades (scalars, bivectors, four-vectors, ...), the odd part the odd grades. The even part is closed under multiplication and is called the even subalgebra.

## lay
Elements built from an even number of arrows form a smaller algebra of their own, the even subalgebra. It is where rotations live.

## one-liner
$\Cl^{+}$ (even grades) and $\Cl^{-}$ (odd grades) are the $\pm 1$ eigenspaces of the grade involution; $\Cl^{+}$ is the even subalgebra.
