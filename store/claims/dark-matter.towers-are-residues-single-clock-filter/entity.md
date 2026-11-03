---
id: dark-matter.towers-are-residues-single-clock-filter
kind: claim
version: 5
title: Towers are residues, and the single-clock filter
status: proved
region: dark-matter
subject: dark-matter
tags: [towers-by-residue, classification]
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
derivations:
- name: main
  uses:
  - dark-matter.imported-eight-towers-mod-8-clock@4
  assumes:
  - dark-matter.p2-indifference@2
  - dark-matter.p3-nearest-dimension-representatives@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:residues
- kind: check
  ref: check.py::check_towers_are_the_eight_residues
- kind: check
  ref: check.py::check_reversal_convention_and_types
- kind: check
  ref: check.py::check_census_lowest_causal
- kind: check
  ref: check.py::check_sort_under_p3
- kind: check
  ref: check.py::check_window_sensitivity
locators:
  paper: T14
  number: Prop 3.1
  label: prop:residues
  line: 150
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: eight towers as residue classes, reversal and the Cl(1,3)/Cl(3,1) types, the lowest causal census, the P3 sort with sterile {0, 4} and the window sensitivity. Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  env: proposition
  context_refs:
  - dark-matter.flag-insensitive-residue-no-flag-level
  - dark-matter.which-towers-are-populated
  typing:
    by: ai-typing-pass
    note: 'Kept the clock import and P2, P3; the two context references (flag-insensitivity and the population
      observation) are cited as comment and further question, not as premises, so not added. Levels pass:
      the lay now names P3 and P2 and the imported two-time instability behind the r = 0 exclusion; the
      one-liner names P2, P3 and the import.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - dark-matter.p2-indifference
    note: P2 enters only through the labelling convention of the statement, which no step of the proof argues,
      so its role is stated in a closing sentence.
---

## formal
The residue $r = p - q \pmod 8$ is invariant along every tower: the eight parallel towers are the eight residues, their parallelism derived rather than described. Call a signature $(p,q)$ \emph{causal} if $\min(p,q) = 1$: exactly one direction of the minority sign, the timelike one, whichever sign convention carries time. Labelling this world $(1,3)$, residue $6$, fixes the convention time $=$ plus, and the mirror residue $2$ reads $(3,1)$; under the opposite convention the two labels swap and the causal sort is unchanged, but every attribution of a Clifford type to a member of the reversal pair passes to the other member, since $\Cl(1,3) \cong \Mat(2,\mathbb{H})$ and $\Cl(3,1) \cong \Mat(4,\R)$ are not isomorphic. That attribution is fixed by a labelling convention Premise \claimref{dark-matter.p2-indifference} declares indexical, and is so read below. Then:
\begin{enumerate}
\item[(i)] \emph{(Census; proved.)} Every residue contains causal signatures once the dimension is free: the lowest are $(1,1)$ at $r = 0$, $(2,1)$ at $r = 1$, $(3,1)$ at $r = 2$, $(4,1)$ at $r = 3$, $(1,5)$ or $(5,1)$ at $r = 4$, $(1,4)$ at $r = 5$, $(1,3)$ at $r = 6$, $(1,2)$ at $r = 7$. The residue alone therefore sorts nothing; a representative must be chosen.
\item[(ii)] \emph{(The sort under P3; proved given the premise.)} Under Premise \claimref{dark-matter.p3-nearest-dimension-representatives} the representatives are $(1,3)$ at $r = 6$, this world; $(3,1)$ at $r = 2$, a mirror Minkowski with real (Majorana-type) spinors; $(2,2)$ at $r = 0$, two times; $(4,0)$ or $(0,4)$ at $r = 4$, none; $(2,1)$ and $(1,2)$ at $r = 1, 7$, three-dimensional; $(4,1)$ and $(1,4)$ at $r = 3, 5$, five-dimensional. Exactly two are sterile, $r = 0$ and $r = 4$ (Figure \ref{fig:clock}), and they are the fixed points of the mirror map $r \mapsto -r$: under P3 the towers without a single time are the towers that are their own mirrors.
\item[(iii)] \emph{(Sensitivity; proved.)} The sterile set is a function of the window. With any dimension up to five allowed, only $r = 4$ is sterile ($(1,1)$ is a causal signature for $r = 0$); with dimensions three to six, only $r = 0$ ($(1,5)$ is one for $r = 4$); with the upper bound removed, nothing is ($(1,9)$ is one for $r = 0$ at ten); and the literal lowest-dimensional representative of every residue, with no lower bound, is definite for $r = 6$ itself, namely $(0,2)$: without a lower bound the criterion would sterilise this world.
\end{enumerate}
Six admit matter: this one and five dark. Which of the six the descent populated is a further question, answered for the mirror by P2 and for the odd towers only by the record (Observation \claimref{dark-matter.which-towers-are-populated}). Structural level given P3; the two-time exclusion at $r = 0$ imports the standard instability of two-time dynamics, flagged, and the flag does not remove it (Proposition \claimref{dark-matter.flag-insensitive-residue-no-flag-level}).

## technical
The $(1,1)$ ascent adjoins one positive and one negative direction, so the residue $r = p - q \pmod 8$ is constant along every tower and the eight parallel towers are the eight residues. Call $(p,q)$ causal if $\min(p,q) = 1$. Since $(1,s)$ has residue $1 - s$, every residue contains causal signatures once the dimension is free, so the residue alone sorts nothing and a representative must be chosen. Under premise P3 (nearest-dimension representatives) the representatives are $(1,3)$ at $r = 6$, $(3,1)$ at $r = 2$, $(2,2)$ at $r = 0$, $(4,0)$ or $(0,4)$ at $r = 4$, $(2,1)$ and $(1,2)$ at $r = 1, 7$, and $(4,1)$ and $(1,4)$ at $r = 3, 5$. Exactly $r = 0$ and $r = 4$ are sterile, and they are the fixed points of the mirror map $r \mapsto -r$.

Which member of the reversal pair $\{6, 2\}$ is this world depends on the sign convention for time, and the convention matters for types because $\Cl(1,3) \cong \Mat(2,\HH)$ and $\Cl(3,1) \cong \Mat(4,\R)$ are not isomorphic; premise P2 declares the convention indexical. The sterile set is a function of the dimension window: other windows sterilise only $r = 4$, only $r = 0$, or nothing, and with no lower bound the criterion would sterilise this world's residue. Six towers admit matter, this one and five dark; the exclusion of $r = 0$ imports the standard instability of two-time dynamics.

## lay
Clifford algebras repeat with period eight, and the paper reads the eight repeating families as eight parallel towers, each labelled by a number from 0 to 7. If the dimension may vary freely, every label can host a world with exactly one direction of time, so a premise is needed to pick one representative per label. Taking the dimension nearest four (premise P3), two labels are left without a single time direction, one with none and one with two, the latter excluded by importing the standard instability of two-time physics; the other six can hold matter: our world and five dark ones. Which member of a mirror pair is called our world depends on a sign convention for time that premise P2 declares to carry no physics.

## one-liner
The residue $p - q \pmod 8$ is invariant along each tower, and under the nearest-dimension premise P3, with P2 reading the time-sign label as indexical, exactly the residues $0$ and $4$ lack a single time direction, leaving six towers that admit matter (the two-time exclusion imports the standard instability).
