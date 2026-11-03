---
id: obj.dark-matter.frozen-phase-operators
kind: object
version: 2
title: Frozen-phase operators
status: defined
region: dark-matter
subject: dark-matter
tags:
- superselection
- towers-by-residue
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
locators:
  paper: T14
  number: Def 3.6
  label: def:frozenops
  line: 208
extraction:
  env: definition
  context_refs:
  - dark-matter.residue-soldered-invariant-not-algebraic-one
  typing:
    by: ai-typing-pass
    note: Definition only; no edges changed, P1 and the soldered-residue theorem are named in the text
      but objects carry no premise edges.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - dark-matter.p1-single-frozen-point (motivated_by)
    added_dependants: []
    added_about: []
    verdict: connected
    note: Already used by about; lineage to P1, since the definition is stated as P1's operational reading.
lineage:
  motivated_by:
  - dark-matter.p1-single-frozen-point
---

## formal
Two things are fixed, and they are different. The one gravitational metric is shared by every tower (Premise \claimref{dark-matter.p1-single-frozen-point}); each tower $r$ has its own soldering $V_{r}$, the generating subspace of its own algebra $(A_{r}, V_{r})$, with $V_{6}$ the one metric's tangent space and the others the other towers' (Theorem \claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}). The \emph{frozen-phase sector decomposition} is the hypothesis that the frozen phase's state space is the direct sum over residues of sectors, the $r$-th a module over the soldered algebra $(A_{r}, V_{r})$, and that a \emph{frozen-phase local operator} is a section of one tower's soldered Clifford bundle: built, fibrewise, from that tower's soldering by Clifford multiplication and the connection it defines, with gravity entering every sector only through the shared metric's stress-energy coupling. This is the operational reading of Premise \claimref{dark-matter.p1-single-frozen-point}, stated as a hypothesis and carried as one.

## technical
Two structures are distinguished. The one gravitational metric is shared by every tower (premise P1), while each tower $r$ has its own soldering $V_{r}$, the generating subspace of its algebra $(A_{r}, V_{r})$, with $V_{6}$ the metric's tangent space. The frozen-phase sector decomposition is the hypothesis that the frozen phase's state space is a direct sum over residues of sectors, the $r$-th a module over $(A_{r}, V_{r})$. A frozen-phase local operator is a section of one tower's soldered Clifford bundle, built fibrewise from that tower's soldering by Clifford multiplication and the connection it defines, with gravity entering every sector only through the shared metric's stress-energy coupling. The definition is the operational reading of P1 and is carried as a hypothesis.

## lay
This definition says what counts as a physical operation in the universe's present, frozen phase. All towers share one gravitational geometry, but each has its own algebraic structure, and an allowed local operation is built from a single tower's structure. Towers then affect one another only through gravity. The paper states this as a hypothesis rather than deriving it.

## one-liner
The frozen-phase sector decomposition hypothesises a state space that is a direct sum of per-residue sectors, with local operators built from one tower's soldered Clifford bundle and gravity entering only through the shared metric.
