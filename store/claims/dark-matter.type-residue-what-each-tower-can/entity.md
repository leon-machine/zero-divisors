---
id: dark-matter.type-residue-what-each-tower-can
kind: claim
version: 5
title: Type by residue, and what each tower can carry intrinsically
status: proved
region: dark-matter
subject: dark-matter
tags:
- towers-by-residue
- clifford-classification
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
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.imported-eight-towers-mod-8-clock@4
  - dark-matter.towers-are-residues-single-clock-filter@5
  proof: proof-main.tex
- name: standard-route
  uses:
  - rule2.imported-classification-centre-type-c-external@1
  proof: proof-standard-route.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:thm:types
- kind: check
  ref: check.py::check_type_table_on_p3_representatives
- kind: check
  ref: check.py::check_type_is_a_residue_invariant
- kind: check
  ref: check.py::check_intrinsic_groups
- kind: check
  ref: check.py::check_volume_element_on_the_odd_residues
locators:
  paper: T14
  number: Thm 3.4
  label: thm:types
  line: 176
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: D and component count from a certified primitive idempotent (trace-form signature of f Cl f) on the P3 representatives and all 20 signatures with n <= 5, intrinsic groups and the volume element at the odd residues. Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  env: theorem
  context_refs:
  - dark-matter.towers-are-residues-single-clock-filter
  unresolved_refs:
  - rem:flaglives
  outside_pilot_cites:
  - ButlerT12
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.towers-are-residues-single-clock-filter
    note: 'Added the residue census as a premise because clauses (i) to (iii) are stated for its P3 representatives
      in its labelling convention; standard route uses the store''s ABS and Lounesto import, while the
      source names Cartan and Bott for the classical table. Levels pass: the lay level now keeps the P3-representative
      and labelling-convention qualifiers on the tower-by-tower attributions.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.towers-are-residues-single-clock-filter
about:
- obj.dark-matter.spinor-module-type
---

## formal
The type is a function of the residue alone: $D = \R$ with one irreducible module at $r = 0, 2$ and two at $r = 1$; $D = \C$ with one at $r = 3, 7$; $D = \mathbb{H}$ with one at $r = 4, 6$ and two at $r = 5$. Consequently, for the P3 representatives, in the labelling convention of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter} (under the opposite one every attribution to a named member of a pair $\{r, -r\}$ passes to the other):
\begin{enumerate}
\item[(i)] the mirror tower $r = 2$ has real (Majorana) spinors with intrinsic group $\mathbb{Z}_{2}$: no continuous charge commutes with its ground Clifford action, and in particular no $U(1)$ under which its ground spinors are charged; the fork tower $r = 0$, also real with one module, has the same intrinsic group $\mathbb{Z}_{2}$;
\item[(ii)] the residues $r = 3$ (five-dimensional) and $r = 7$ (three-dimensional) have complex spinors with intrinsic group exactly $U(1)$, a distinguished complex structure and hence exactly one intrinsic abelian charge each;
\item[(iii)] this world $r = 6$, and $r = 4, 5$, have quaternionic spinors with intrinsic group $Sp(1)$: a two-sphere of complex structures and no distinguished $U(1)$;
\item[(iv)] the odd residues $r = 1, 5$ have two inequivalent irreducible modules, distinguished by the sign of the central volume element, and $r = 3, 7$ one, the volume element acting as the complex unit.
\end{enumerate}
The intrinsic group is a lower bound on a tower's internal symmetry, not the whole of it: the rungs adjoin ladder pairs whose flags are complex structures (Remark \ref{rem:flaglives}), and the derived content of this tower's $U(1)$ is a rung-level object \cite{ButlerT12}. What the theorem fixes is what the ground algebra carries by itself.

## technical
For an irreducible real module of $\Cl(p,q)$, the commutant $D$ and the number of inequivalent irreducible modules depend only on the residue $r = p - q \pmod 8$, because $\Cl(p+1,q+1) \cong \Mat(2, \Cl(p,q))$ preserves both: $D = \R$ at $r = 0, 2$ (one module) and $r = 1$ (two); $D = \C$ at $r = 3, 7$ (one); $D = \HH$ at $r = 4, 6$ (one) and $r = 5$ (two). The intrinsic group is the unit group of $D$: $\Z_{2}$, $U(1)$ or $Sp(1)$.

For the P3 representatives, in the labelling convention in which this world is $(1,3)$, the mirror $r = 2$ and the fork $r = 0$ have real spinors with intrinsic group $\Z_{2}$, so no continuous charge commutes with their ground Clifford action; $r = 3$ and $r = 7$ have complex spinors and exactly one intrinsic abelian charge each; this world and $r = 4, 5$ are quaternionic, with $Sp(1)$ and no distinguished $U(1)$. At $r = 1, 5$ the two modules differ by the sign of the central volume element, which at $r = 3, 7$ acts as the complex unit. Under the opposite convention the attributions within each pair $\{r, -r\}$ swap. The intrinsic group bounds a tower's internal symmetry from below; it is not the whole of it.

## lay
Each tower's basic algebra decides what kind of numbers its matter states naturally use: real numbers, complex numbers or quaternions. That choice depends only on the tower's label, and it fixes which continuous symmetries a tower carries before any further structure is added. For the representatives the paper uses, and in its labelling convention (the opposite convention swaps the two members of each mirror pair), the mirror tower comes out with real spinors and no built-in continuous charge, two of the odd towers with exactly one built-in charge each, and our own world with quaternionic spinors.

## one-liner
A tower's spinor type (real, complex or quaternionic, with one or two modules) is a function of its residue alone, and it fixes the intrinsic symmetry group, $\Z_{2}$, $U(1)$ or $Sp(1)$, that each tower's ground algebra carries.
