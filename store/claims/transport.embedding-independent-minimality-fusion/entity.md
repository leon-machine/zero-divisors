---
id: transport.embedding-independent-minimality-fusion
kind: claim
version: 4
title: Embedding-independent minimality of the fusion
status: proved
region: transport
subject: completion
tags: [transport-algorithm, forcing-and-uniqueness]
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
derivations:
- name: main
  uses:
  - transport.classification-real-clifford-algebras@3
  - transport.corner-even-subalgebra@4
  - transport.rule-2-ideal-fusion-sharp-form@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_case_analysis_minimum
- kind: check
  ref: check.py::check_embedding_rules
- kind: check
  ref: check.py::check_equality_case_is_mat_2k_f
locators:
  paper: T01
  number: Thm 5.11
  label: thm:embmin
  line: 1258
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the case analysis of dim B enumerated, the embedding rules, and the fused algebra identified as Mat_2k(F). Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    added: [transport.classification-real-clifford-algebras]
    note: 'Added the classification, which the hypothesis uses for the split form Mat_k(F) + Mat_k(F) and the proof for the irreducible modules; kept the corner and fusion premises used in the final identification.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - transport.classification-real-clifford-algebras
---

## formal
Let $p - q \equiv 1 \pmod 4$, $A = \Cl(p,q) \cong \Mat_k(\mathbb{F}) \oplus \Mat_k(\mathbb{F})$ with $\mathbb{F} \in \{\R, \HH\}$, $f = \dim_\R \mathbb{F}$, so $\dim_\R A = 2k^2 f = 2^n$. Let $B$ be any \emph{simple} finite-dimensional real algebra admitting a unital algebra embedding $A \hookrightarrow B$. Then
\[
\dim_\R B \;\geq\; 2^{\,n+1},
\]
and equality holds if and only if $B \cong \Mat_{2k}(\mathbb{F}) \cong \Mat_2(\Cl^0(p,q))$: the fused algebra of Theorem \claimref{transport.rule-2-ideal-fusion-sharp-form} is the minimal simple environment of $A$ in the absolute sense, and it is the unique one of minimal dimension up to isomorphism.

## technical
Let $p - q \equiv 1 \pmod 4$, so that $A = \Cl(p,q) \cong \Mat_k(\mathbb{F}) \oplus \Mat_k(\mathbb{F})$ with $\mathbb{F} \in \{\R, \HH\}$ and $\dim_\R A = 2^n$. If $B$ is any simple finite-dimensional real algebra admitting a unital embedding $A \hookrightarrow B$, of whatever kind, then $\dim_\R B \geq 2^{n+1}$, with equality if and only if $B \cong \Mat_{2k}(\mathbb{F}) \cong \Mat_2(\Cl^0(p,q))$.

So the fused algebra of Rule 2 is the minimal simple environment of the split algebra in the absolute sense, not only among Clifford ascents, and it is the unique one of minimal dimension up to isomorphism.

## lay
When a Clifford algebra splits into two halves, the series repairs it by adding one direction, which fuses the halves into a single indivisible algebra twice the size. This result shows that no cleverer choice does better: any indivisible algebra containing the split one is at least twice its size. The fused algebra is, up to relabelling, the only one that achieves this.

## one-liner
For $p - q \equiv 1 \pmod 4$, every simple real algebra containing $\Cl(p,q)$ unitally has dimension at least $2^{n+1}$, with equality only for $\Mat_2(\Cl^0(p,q))$.
