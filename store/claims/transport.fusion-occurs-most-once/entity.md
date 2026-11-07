---
id: transport.fusion-occurs-most-once
kind: claim
version: 5
title: Fusion occurs at most once
status: proved
region: transport
subject: completion
tags: [transport-algorithm, obstruction-types, towers-by-residue]
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
- obj.transport.transport
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.classification-real-clifford-algebras@3
  - transport.existence-classification-type-c@4
  - transport.rule-1-morita-trivial@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:7.4
- kind: check
  ref: check.py::check_residues_and_type_c_sites
- kind: check
  ref: check.py::check_histories_fuse_at_most_once
- kind: check
  ref: check.py::check_rule_one_amplification_and_lineage
locators:
  paper: T01
  number: Prop 7.4
  label: prop:parks
  line: 1495
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: type C computed exactly at d = 1 mod 4 for n <= 10, Rule 2 residue moves, every transport history of length <= 6 fusing at most once, and Rule 1 as matrix amplification with the physical lineage at residue 6. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - transport.classification-real-clifford-algebras
    note: 'Added the classification for the closing clause on Cl(1,3) (simple, quaternionic type at residue
      6); kept Rule 1 Morita triviality and the type-C existence locus, both used in the proof. Levels
      pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - transport.classification-real-clifford-algebras
---

## formal
Call a \emph{transport history} any finite sequence of algebras beginning at a nondegenerate $\Cl(p,q)$, each obtained from its predecessor by Rule 1 (the $(1,1)$ ascent) or, when the predecessor carries type C, by Rule 2 (ideal fusion). Then along any transport history:
\begin{enumerate}
\item the clock residue $d \bmod 8$ is constant under Rule 1 (Theorem \claimref{transport.rule-1-morita-trivial}) and moves by $\pm 1$ under Rule 2;
\item type C is present exactly at $d \equiv 1 \pmod 4$, i.e.\ at residues $1$ and $5$ (Theorem \claimref{transport.existence-classification-type-c}), and Rule 2 maps these to residues in $\{0, 2\}$ and $\{4, 6\}$ respectively, none of which is $\equiv 1 \pmod 4$;
\item hence Rule 2 can be applied at most once in any transport history, and after it (or from the start, if $d \not\equiv 1 \pmod 4$) every subsequent algebra in the history has the same Wedderburn type: the state machine takes at most one step on the mod-8 clock, and then remains fixed.
\end{enumerate}
In particular the physical lineage is stationary from the start: $\Cl(1,3)$ has $d \equiv 6$, is simple, never demands Rule 2, and every Rule-1 ascent $\Cl(1{+}k, 3{+}k) \cong \Mat_{2^k}(\Cl(1,3))$ remains at residue $6$, quaternionic type.

## technical
A transport history is a finite chain of algebras starting at a nondegenerate $\Cl(p,q)$, each step being Rule 1, the $(1,1)$ ascent, or, when the current algebra carries type C, Rule 2, ideal fusion. Rule 1 leaves the clock residue $d \bmod 8$ unchanged and Rule 2 moves it by $\pm 1$. Type C occurs exactly at $d \equiv 1 \pmod 4$, that is at residues $1$ and $5$, and Rule 2 sends these into $\{0, 2\}$ and $\{4, 6\}$, none of which is $\equiv 1 \pmod 4$.

Hence Rule 2 is applied at most once in any history, and after it, or from the start if $d \not\equiv 1 \pmod 4$, every later algebra has the same Wedderburn type. The physical case $\Cl(1,3)$ has $d \equiv 6$, is simple and never calls for Rule 2, and its Rule 1 ascents $\Cl(1{+}k, 3{+}k) \cong \Mat_{2^k}(\Cl(1,3))$ stay at residue $6$, of quaternionic type.

## lay
Each Clifford algebra sits at one of eight positions on a clock. One repair rule never moves the hand; the other moves it by one step, is only used at the two positions where the algebra is split, and always lands where no split occurs. So the second rule can be used at most once, after which nothing structural changes. The algebra of spacetime starts at a position that never needs the second rule.

## one-liner
Along any transport history Rule 1 fixes the mod-8 residue and Rule 2 leaves the type-C residues for good, so fusion happens at most once and the Wedderburn type is then fixed.
