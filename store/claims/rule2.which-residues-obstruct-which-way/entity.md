---
id: rule2.which-residues-obstruct-which-way
kind: claim
version: 6
title: Which residues obstruct which way
status: proved
region: rule2
subject: zero-divisors
tags: [obstruction-types, towers-by-residue]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - rule2.where-obstruction-sits-commuting-square@6
  - transport.rule-1-morita-trivial@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T17_rule2.py
  tags:
  - label:cor:residues
- kind: check
  ref: check.py::check_even_residue_table
- kind: check
  ref: check.py::check_physical_lineage_and_mirror
locators:
  paper: T17-rule2
  number: Cor 2.3
  label: cor:residues
  line: 167
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: type C of both extensions over every even (p,q) with p + q <= 8 (residue sets {2, 6} and {0, 4}), the residue-6 lineage and mirror residue 2 with Mat_2 repairs by matrix units and corners. Version 5 -> 6.'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A10 follow-up: the mirror-residue sentence now says spacelike means square -1 and points at synthesis.mirror-extensions-causal-convention (in T14 causal convention the obstruction at residue 2 is a second time); mathematics unchanged.'
  source_formal: "The even residues whose spacelike extension is type C are $\\{2, 6\\}$; those whose timelike extension is type C are $\\{0, 4\\}$. In particular every even residue has exactly one obstructing one-dimensional extension. The physical lineage sits at residue $6$ and its Rule 1 ascents never leave it (Fact \\claimref{transport.rule-1-morita-trivial}); by Theorem \\claimref{rule2.where-obstruction-sits-commuting-square} it leaves residue $6$ only through a spacelike Kaluza-Klein direction, into the obstruction at residue $5$, and the opposite-sign repair returns it to $6$ as $\\Mat_2$ of where it started. The same holds at the mirror residue $2$."
  env: corollary
  context_refs:
  - transport.rule-1-morita-trivial
  typing:
    by: ai-typing-pass
    added:
    - transport.rule-1-morita-trivial
    note: 'Added the Rule 1 Morita result, which the statement cites for residue preservation of Rule
      1 ascents; this claim restates transport.which-residues-obstruct-which-way from the root paper and
      could be marked equivalent to it. Linked equivalent_to transport.which-residues-obstruct-which-way:
      the companion note restates it.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - transport.rule-1-morita-trivial
equivalent_to:
- transport.which-residues-obstruct-which-way@6
---

## formal
The even residues whose spacelike extension is type C are $\{2, 6\}$; those whose timelike extension is type C are $\{0, 4\}$. In particular every even residue has exactly one obstructing one-dimensional extension. The physical lineage sits at residue $6$ and its Rule 1 ascents never leave it (Fact \claimref{transport.rule-1-morita-trivial}); by Theorem \claimref{rule2.where-obstruction-sits-commuting-square} it leaves residue $6$ only through a spacelike Kaluza-Klein direction, into the obstruction at residue $5$, and the opposite-sign repair returns it to $6$ as $\Mat_2$ of where it started. The same holds at the mirror residue $2$, with spacelike read as square $-1$ in both towers: in T14's causal convention, where the mirror's time is its minus sign, that extension is the mirror's second time, and the mirror's own Kaluza-Klein direction gives the unobstructed $\Cl(4,1)$ (Proposition \claimref{synthesis.mirror-extensions-causal-convention}).

## technical
For an even-dimensional $\Cl(p,q)$ with residue $d = p - q \bmod 8$, the spacelike one-dimensional extension carries the type-C obstruction exactly when $d \in \{2, 6\}$ and the timelike one exactly when $d \in \{0, 4\}$, so every even residue has exactly one obstructing one-dimensional extension. Using that Rule 1 ascents preserve the residue, the physical lineage at $d = 6$ leaves residue $6$ only through a spacelike Kaluza-Klein direction, into the type-C obstruction at residue $5$.

The Rule 2 repair of that obstruction by a generator of the opposite sign returns it to residue $6$ as $\Mat_2$ of the algebra it started from. The mirror residue $2$ behaves in the same way when spacelike means square $-1$; in T14's causal convention that obstructing extension is the mirror's second time, not its Kaluza-Klein direction.

## lay
Clifford algebras repeat in a cycle of eight, so each one has a residue from 0 to 7. For the even residues, adding one new space direction breaks the algebra into two pieces exactly at residues 2 and 6, and adding one new time direction does so exactly at 0 and 4. The physical case sits at residue 6: its only exit is an extra space direction, and repairing that break with a direction of the opposite kind brings it back to residue 6 as two-by-two matrices over where it began.

## one-liner
The spacelike extension of an even residue is type C exactly at residues $2$ and $6$ and the timelike one exactly at $0$ and $4$, so the physical residue $6$ is left only through a spacelike direction and regained by the opposite-sign repair.
