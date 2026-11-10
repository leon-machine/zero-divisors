---
id: synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3
kind: claim
version: 1
title: 'No rule P2 licenses gives the thickness of R3'
status: proved
region: synthesis
subject: dark-matter
tags: [dark-matter-ratio, counting-rules, undetermined-input, premises-p1-p5, indifference]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
review: draft
derivations:
- name: main
  uses:
  - dark-matter.total-function-thickness@5
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - dark-matter.stored-asymmetry-charge-not-number@9
  - dark-matter.parallel-boundary-mode-spaces-one-wall@5
  - dark-matter.no-coupling-rule-odd-towers-follows@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_every_other_premise_is_blind_to_the_thickness
- kind: check
  ref: check.py::check_family_reaches_every_ratio_above_one
- kind: check
  ref: check.py::check_own_cells_are_not_isometric_across_dimensions
- kind: check
  ref: check.py::check_licensed_shares_miss_r3
- kind: proof
  derivation: main
extraction:
  open_problem: op.thickness-deposit-rule
  note: >-
    Attack item 1, second half, of op.thickness-deposit-rule: prove that no rule P2 licenses gives R3, which the
    success clause accepts ("a proof that no rule P2 licenses gives it, leaving the ratio a fit"). Premise set at
    the pinned versions: the past cone of the unit-ball rule (F1 to F4, P2, P3, R1, R2, R3, the Chevalley, Witt
    and Morita imports) with P1, the costed single-ideal clause and the stored asymmetry. Two parts. First, an
    independence family: a separate counted thickness for the five-dimensional and the three-dimensional pairs,
    every premise except R3 unchanged, extending the stored diagonal family T(c). Second, the licensed rules: P2's
    text (it equates along symmetry orbits, never inequivalent components) read with the one extension the store
    already uses (equal filling per rung of the shared wall) gives cross-tower shares 1 or 1/epsilon only, and
    R3's five-dimensional share 8/(3 pi) is below one. This makes the argued finding of 31 October (a rule
    democratic in any common count gives share one or 1/epsilon) a proof under a stated definition of licensing.
    The coincidence problem of asymmetric dark matter is prior art for the 1/epsilon branch (for example
    D. E. Kaplan, M. A. Luty and K. M. Zurek, Phys. Rev. D 79 (2009) 115016, cited from memory; not a premise).
    Transport-absent: counting and the structure of P2; nothing uses transport. What is not claimed: that no
    future premise could fix the thickness (a deposit correlation length or an evaporation measurement, attack
    items 2 and 4, are untouched); anything about R2, beyond that R2 and R3 together are democracy in cells that
    P2 does not relate.
---

## formal
Let the five-dimensional towers' matter count through $\lambda$ cell radii of their extra direction and the three-dimensional towers' sheets be stacked $\mu$ cell radii apart ($\lambda, \mu > 0$, common within each reversal pair), with Premises \claimref{dark-matter.r1-equal-mass-per-quantum}, \claimref{dark-matter.r2-one-quantum-per-unit-ball} and the sourcing rule as stored; Premise \claimref{dark-matter.r3-one-cell-per-unshared-direction} is $\lambda = \mu = 1$.
\begin{enumerate}
\item[(i)] \emph{(Independence; proved.)} Every premise of the unit-ball relation other than R3 (F1 to F4, P1, P2, P3, R1, R2, the costed single-ideal clause and the imports) holds for every $(\lambda, \mu)$: R2's densities in each tower's own space, R1's common mass, every sector label the descent deposits (residues, orientability, the stored charge $\epsilon N$ of the oriented pair and zero for the odd towers) and P2's equalities along reversal orbits are the same for all of them. The dark-to-baryon ratio is
\[
T(\lambda, \mu) \;=\; 1 + \frac{8}{3\mu} + \frac{16\lambda}{3\pi},
\]
increasing in $\lambda$, decreasing in $\mu$, and taking every value above $1$; on the diagonal it is $T(c)$ of \claimref{dark-matter.total-function-thickness}, and $T(1,1) = (11\pi + 16)/3\pi$. As scoped, Premise \claimref{dark-matter.p2-indifference} reaches labels and not states, so it licenses no rule on fillings at all.
\item[(ii)] \emph{(The rules P2 licenses; proved, given the definition.)} Call a deposit rule licensed by P2 if every equality it imposes between fillings of two towers equates objects in one orbit of the symmetries of the deposited structure: members of one reversal orbit, or objects common to all towers, as the rungs of the one wall (\claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}) or the light rays of the common count $N$ (\claimref{dark-matter.stored-asymmetry-charge-not-number}); this is P2's text (it equates along symmetry orbits and never equates inequivalent components) with the extension under which the stored rule of equal filling per rung of the shared wall is licensed. A tower's own cells are balls of its own space, of dimension $2$, $3$ or $4$, and balls of different dimension are not isometric, so no licensed rule equates a three- or five-dimensional tower's filling per own cell with this tower's: R2 and R3 together are democracy in cells that P2 does not relate. A licensed cross-tower rule fills a common object equally in every tower, so each odd tower's share is $1$, or $1/\epsilon$ with $0 < \epsilon \le 1$ under the charge reading, where this tower's baryons are the asymmetric excess $\epsilon$ of the common count and the odd towers carry none. R3's five-dimensional share is $8/3\pi \in (\tfrac56, \tfrac89)$, below one, so no licensed rule gives it, for any $\epsilon$; equivalently the licensed thicknesses are $\lambda = 3\pi/8$ or $3\pi/8\epsilon$, both above $\tfrac98$, never $1$. (The three-dimensional share $\tfrac43$ would be $1/\epsilon$ only at $\epsilon = \tfrac34$.) An annihilation stage would multiply the odd shares by a survival fraction, a dynamical quantity the series cannot fix, having no coupling rule for the odd towers (\claimref{dark-matter.no-coupling-rule-odd-towers-follows}).
\item[(iii)] \emph{(Cost.)} The thickness is a recorded input, R3 stays a premise, and $5.364$ remains a fit; the three-dimensional fraction $8/(3\mu T)$, $49.7\%$ at R3, rests on it too.
\end{enumerate}

## technical
The unit-ball relation counts a five-dimensional tower's matter through one cell radius of its extra direction and stacks a three-dimensional tower's sheets one cell radius apart (R3). Let those two lengths be free, $\lambda$ and $\mu$ cell radii, equal within each mirror-related pair as P2 requires. Nothing else in the premises changes: the densities in each tower's own space, the common mass, and every sector label are the same, so every value of the dark-to-baryon ratio above one is reached by some pair, and R3's value is one point. Read P2 as allowing only equalities between objects that a symmetry relates: two members of a reversal pair, or objects all towers share, such as the rungs of the one wall or the light rays of the common count. A five-dimensional tower's cells are four-balls and ours are three-balls, which no symmetry relates, so P2 can only equate fillings of shared objects. That gives every odd tower the same count as ours (share one, total $5.000$) or, if our baryons are only the small asymmetric excess $\epsilon$ of the common count, share $1/\epsilon$, at least one. R3 needs the five-dimensional share $8/3\pi \approx 0.85$, below one, so no such rule gives it.

## lay
The series' fit of the amount of dark matter depends on how thick, in its own units, the matter of the five-dimensional and three-dimensional hidden worlds counts. The fit sets that thickness to one unit. This result shows that nothing else in the theory fixes it: any thickness is compatible with every other assumption, and gives a different total. The theory's indifference principle could only make different worlds fill shared objects equally, which gives each hidden world as much matter as ours or far more, never the slightly smaller share the fit needs for the five-dimensional worlds. So the observed ratio of dark to ordinary matter remains something the theory fits, not something it predicts.

## one-liner
With separate thicknesses $\lambda$, $\mu$ for the five- and three-dimensional towers every premise but R3 holds and $T = 1 + 8/3\mu + 16\lambda/3\pi$ takes every value above one; the rules P2 licenses (equal filling of shared objects) give odd shares $1$ or $1/\epsilon \ge 1$, while R3 needs $8/3\pi < 1$, so no licensed rule gives R3 and $5.364$ stays a fit.
