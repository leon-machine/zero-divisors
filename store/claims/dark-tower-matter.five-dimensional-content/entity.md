---
id: dark-tower-matter.five-dimensional-content
kind: claim
version: 5
title: The five-dimensional towers' content
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [hypercharge-and-anomalies]
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
derivations:
- name: main
  uses:
  - dark-tower-matter.three-dimensional-content@4
  - dark-tower-matter.gauge-algebras@5
  assumes:
  - dark-tower-matter.hypothesis-s-slot-statistics@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:F3
  - id:F4
- kind: check
  ref: check.py::check_sixteen_states_four_species
- kind: check
  ref: check.py::check_centre_acts_by_minus_three_y
locators:
  paper: T14c
  number: Prop 6.3
  label: prop:content5
  line: 603
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: 16 states of Lambda(C^1 + C^3), complement pairing into U, D, E, N with the stated hypercharges, and the centre of U(3) acting by lambda^(-3Y). Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  env: proposition
  unresolved_refs:
  - lem:neutralrow
  typing:
    by: ai-typing-pass
    added:
    - dark-tower-matter.gauge-algebras
    - dark-tower-matter.hypothesis-s-slot-statistics
    note: 'Kept the three-dimensional content (the proof takes the masses from its clause (iv)); added
      the gauge algebras, whose hierarchy C^1 (x) C^3 and U(3) section the content is built on, and Hypothesis
      (S) as assumed, since the table holds under (S) (as the Standard-Model paper''s content proposition
      is typed); the neutral-row remark is a note and cannot be a premise. Levels pass: levels written
      from scratch, keeping every condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-tower-matter.gauge-algebras
    - dark-tower-matter.hypothesis-s-slot-statistics
---

## formal
In the towers $r = 3, 5$, under (S) the state space $\Lambda^{\bullet}(\C^{1} \oplus \C^{3})$ has sixteen states. With $Y = s - k/3$ ($s$ the slot occupation, $k$ the number of occupied pairs), the complement $(s,k) \mapsto (1-s, 3-k)$ negates $Y$ and conjugates colour, so the sixteen are eight species-states and their conjugates, four vector-like Dirac species:
\begin{center}\small
\begin{tabular}{@{}lccl@{}}
\toprule
species & colour & $Y$ & states $(s,k)$ \\
\midrule
$U$ & $3$ & $2/3$ & $(1,1)$, conjugate $(0,2)$ \\
$D$ & $3$ & $-1/3$ & $(0,1)$, conjugate $(1,2)$ \\
$E$ & $1$ & $-1$ & $(0,3)$, conjugate $(1,0)$ \\
$N$ & $1$ & $0$ & $(0,0)$, $(1,3)$ \\
\bottomrule
\end{tabular}
\end{center}
These are the electric charges of one of our generations with the weak doublet removed. Through the section $B \mapsto ((\det B)^{-1}, B)$ the centre of $U(3)$ acts on $(s,k)$ by $\lambda^{k - 3s} = \lambda^{-3Y}$, so $3Y$ is an integer with $3Y + k \equiv 0 \pmod 3$, $k$ being the triality: the lattice of $U(3)$, satisfied automatically; the neutral species $N$ is the empty state and the full row of Remark \ref{lem:neutralrow}. Without (S) the content is one Dirac colour triplet of $Y = 2/3$. There is no chirality and every species has a gauge-invariant bare mass.

## technical
In the towers $r = 3, 5$, under Hypothesis (S) the state space $\Lambda^\bullet(\C^1 \oplus \C^3)$ of the one slot and the three pairs has sixteen states. With $Y = s - k/3$ for slot occupation $s$ and pair number $k$, the complement $(s,k) \mapsto (1-s, 3-k)$ negates $Y$ and conjugates colour, giving four vector-like Dirac species: $U$ (colour $3$, $Y = 2/3$), $D$ ($3$, $-1/3$), $E$ ($1$, $-1$) and the neutral $N$ ($1$, $0$), the electric charges of one of our generations with the weak doublet removed.

Through the section $B \mapsto ((\det B)^{-1}, B)$ the centre of $U(3)$ acts by $\lambda^{-3Y}$, so $3Y$ is an integer with $3Y + k \equiv 0 \pmod 3$, satisfied automatically. Without (S) the content is one Dirac colour triplet of $Y = 2/3$. There is no chirality, and every species has a gauge-invariant bare mass.

## lay
Assuming the slot hypothesis, which treats a constituent's slot as a quantum mode like its pairs, a five-dimensional tower's matter comes in four kinds: two coloured quark-like species of charge two thirds and minus one third, a charged lepton-like species and a neutral one. These are the charges of one family of our matter with the weak-force partners missing. Without the hypothesis only one coloured species remains, and in either case each species can have a mass without any Higgs-like field.

## one-liner
Under (S) the five-dimensional towers carry four vector-like Dirac species $U, D, E, N$ with $Y = 2/3, -1/3, -1, 0$; without (S) they carry one colour triplet of $Y = 2/3$.
