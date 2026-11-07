---
id: note.rule2.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'GA rewrite (declared: cites the imported gamma-matrix Fact by name)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- rule2.imported-gamma-matrices-odd-dimension
- rule2.imported-five-dimensional-chern-simons-shift
- rule2.imported-parity-anomaly
- rule2.imported-graphenes-two-valleys-doubling
locators:
  paper: T17-rule2
  number: Setting
  section: Machine verification
  line: 278
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Not rewritten: the only stand-in the language check finds is the cited id of the imported Fact on odd-dimensional gamma matrices, which the note lists among the physics the script does not check; declared outside_ga (bridge), as reader R11 proposed.'
outside_ga:
  kind: bridge
  why: 'the setting text names, by its id, the imported Fact on odd-dimensional gamma matrices, one of the physics Facts the script does not recompute; the script''s own checks are in exact Clifford arithmetic'
---

## formal
Every computational identity asserted in this note has been verified in exact rational arithmetic by the script \texttt{verify\_T17\_rule2.py}, which imports the series' shared library \texttt{GA.py}: its basis-blade Clifford engine, exact ranks, and exact congruence signatures; no floating point anywhere. Twenty-four checks, all passing, in six parts.

\emph{Part A: the extension theorem.} On every even-dimensional nondegenerate $(p,q)$ with $2 \leq p + q \leq 6$, the volume element of each one-dimensional extension is tested for centrality and its square computed: the spacelike extension is type C exactly when $p - q \equiv 2 \pmod 4$, the timelike one exactly when $p - q \equiv 0$, the other has complex type, and the residue sets are $\{2, 6\}$ and $\{0, 4\}$. The Lorentzian alternation with its complex-type complement in dimensions $3, 5, 7, 9, 11$, and the three named cases.

\emph{Part B: the even subalgebra.} The map $e_i \mapsto e_i\nu$ on $(1,3)$ and $(2,0)$ with both signs of $\nu^2$: relations, evenness, and the generated dimension $2^n$.

\emph{Part C: the Kaluza-Klein algebra.} Centrality and square of $\omega$, the idempotent identities, $\gamma^2 = -1$ and $\omega = \gamma e_4$; rank $16$ of $a \mapsto \varepsilon_\pm a$ on the blades of $\Cl(1,3)$ and of each ideal; $\varepsilon_\pm e_4 = \mp\varepsilon_\pm\gamma$; the reflection as $\hat{\cdot}\circ\Ad_{e_4}$, its action on $\omega$ and on $\varepsilon_\pm$.

\emph{Part D: the two fusions.} In $\Cl(2,4)$ and $\Cl(1,5)$: the sixteen matrix-unit products, the non-centrality of $\varepsilon_\pm$, the trivial centre; $\Ad_\nu$ and $\Ad_{\nu e_4}$ on every generator; $(\nu e_4)^2 = \pm 1$; the ladder relations of $(\nu, e_4)$ in $\Cl(2,4)$ and the signature $(0,2)$ in $\Cl(1,5)$; the residues; the Rule 1 projectors $ff^*$, $f^*f$ commuting with $\Cl(1,3)$ and the corner of dimension $16$.

\emph{Part E: the plane.} The same programme for $\Cl(2,1)$: the splitting, the ideal dimension $4$, $\varepsilon_\pm e_t = \mp\varepsilon_\pm e_xe_y$, both fusions with their matrix units, inner grade involution and inner reflection, $(\nu e_x)^2 = \mp 1$, the complex type of $\Cl(1,2)$ and of $\Cl(4,1)$, and the residues.

\emph{Part F: the square in general.} On the grid of Part A: the obstructed extension is type C, the opposite-sign repair is $\Cl(p{+}1,q{+}1)$ at the same residue with a hyperbolic adjoined plane carrying a ladder pair, the same-sign repair sits two residues away with a definite plane, and every repaired algebra has trivial centre.

What the script does not check: the physics imported as Facts \claimref{rule2.imported-gamma-matrices-odd-dimension}, \claimref{rule2.imported-five-dimensional-chern-simons-shift}, \claimref{rule2.imported-parity-anomaly}, and \claimref{rule2.imported-graphenes-two-valleys-doubling} (the note identifies structures, it does not recompute effective actions); the isomorphism $\Cl(1,3) \cong \Mat_2(\HH)$ and the rest of the classification table beyond the dimension counts and centres it computes (imported); the group-theoretic restriction of Remark \claimref{note.rule2.twistor-five-dimensional-spinor} (standard); and the eleven-dimensional module counts of Remark \claimref{note.rule2.eleven-dimensions-reality-spinors} beyond the split-versus-complex verdict of Part A.

## technical
pending

## lay
pending

## one-liner
pending
