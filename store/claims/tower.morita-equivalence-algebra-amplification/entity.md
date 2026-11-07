---
id: tower.morita-equivalence-algebra-amplification
kind: claim
version: 2
title: Morita equivalence of an algebra and its amplification
status: imported
region: tower
subject: clifford-structure
tags: [classical-theorem, clifford-classification]
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
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
review: typed
imported_from:
- citation: T. Y. Lam, Lectures on Modules and Rings, Graduate Texts in Mathematics 189, Springer, New
    York (1999).
  key: Lam1999
  locator: \S\S 17--18
locators:
  paper: T03
  number: Fact 3.4
  label: fact:morita
  line: 262
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Decision item E8 (routine; no retirement): equivalent_to std-algebra.morita-amplification@1 added. This imported Fact (Lam) is clause (iii) of the proved std-algebra.morita-amplification; status stays imported (a derivation would be a status change, not needed).'
  env: fact
  typing:
    by: ai-typing-pass
    note: 'Imported classical fact with no derivation; levels only.'
equivalent_to:
- std-algebra.morita-amplification@1
---

## formal
For any unital ring $A$ and $m \geq 1$, the column module $A^m$ is a $\Mat_m(A)$-$A$-bimodule implementing an equivalence of module categories: $A$ and $\Mat_m(A)$ are Morita equivalent. \emph{Provenance:} classical Morita theory, \cite[\S\S 17--18]{Lam1999}.

## technical
For any unital ring $A$ and any $m \geq 1$, the column module $A^m$ is a $\Mat_m(A)$-$A$-bimodule implementing an equivalence between the categories of modules over $\Mat_m(A)$ and over $A$. Hence $A$ and its amplification $\Mat_m(A)$ are Morita equivalent; this is classical Morita theory.

## lay
Replacing an algebra by the algebra of square matrices with entries in it does not change its module theory: the two have equivalent categories of modules. This is a classical result imported from ring theory.

## one-liner
Every unital ring $A$ is Morita equivalent to the matrix ring $\Mat_m(A)$, via the column module $A^m$.
