---
id: synthesis.reversion-pairing-vanishes-residues-zero-four
kind: claim
version: 1
title: 'The reversion pairing vanishes exactly at residues 0 and 4'
status: proved
region: synthesis
subject: dark-matter
tags: [towers-by-residue, dark-tower-premises, chirality, pseudoscalar-and-centre]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - dark-tower-matter.where-mass-begins@2
  - synthesis.lowest-causal-residues-zero-four-content@2
  - synthesis.oriented-causal-towers-mirror-pair-every-window@2
  - dark-matter.imported-eight-towers-mod-8-clock@4
  proof: proof-main.tex
about:
- obj.dark-tower-matter.ideals-fields-momentum
checked_by:
- kind: check
  ref: check.py::check_reversion_pairing_vanishes_residues_zero_four
- kind: proof
  derivation: main
extraction:
  open_problem: op.window-p3
  note: >-
    Adversarial and window-free test of the second clause of P3 (residues 0 and 4 empty), also
    bearing on op.thickness-deposit-rule attack (3). Parts (i) and (ii) are Clifford-algebra
    structure in every dimension (transport-absent); (iii) and (iv) are exact computations with
    T14c's own definitions. The statement takes no position on which reading of a massive
    composite the series adopts in dimension six; that is left open. The momentum figure 1/4 is
    recomputed here and is the one of synthesis.lowest-causal-residues-zero-four-content(iii),
    whose extension of H1 to dimensions two and six it inherits for part (iv) only.
---

## formal
Let a tower representative have signature $(p,q)$, $n = p + q$, residue $r = p - q \pmod 8$ and pseudoscalar $\omega$; call it causal when $\min(p,q) = 1$. Use the spinor ideal $S = \Cl^{0}(V)f$ and the momentum $j(\psi) = \ip{\psi e_{t}\rev{\psi}}_{1}$ of Definition \claimref{obj.dark-tower-matter.ideals-fields-momentum}, with the chiral factor $\tfrac12(1 \pm \omega)$ in $f$ in dimension six as in Proposition \claimref{synthesis.lowest-causal-residues-zero-four-content}. Then:
\begin{enumerate}
\item[(i)] \emph{(Every dimension; proved.)} The centre of $\Cl^{0}(V)$ is $\R$ for $n$ odd and $\R \oplus \R\omega$ for $n$ even. When $n$ is even and $\omega^{2} = +1$, $P_{\pm} = \tfrac12(1 \pm \omega)$ are central idempotents of $\Cl^{0}(V)$, and $\rev{P}_{\pm} = P_{\mp}$ exactly when $n \equiv 2 \pmod 4$; in that case $\rev{\psi}_{1}\psi_{2} = 0$ for all $\psi_{1}, \psi_{2} \in \Cl^{0}(V)P_{+}$ (and likewise for $P_{-}$), so the reversion pairing vanishes identically on any spinor ideal of one chirality. A causal signature satisfies these conditions exactly when $r \in \{0, 4\}$, the two residues fixed by the reversal $r \mapsto -r$, in every dimension: its causal members have $n \equiv 2 \pmod 4$, while the causal members of residues $2$ and $6$ have $n \equiv 0 \pmod 4$ and $\omega^{2} = -1$.
\item[(ii)] \emph{(Every dimension; proved.)} For a causal signature of any other residue $\Cl^{0}(V)$ is simple, and the reversion pairing on $S$ is not identically zero.
\item[(iii)] \emph{(Computed, exact.)} At the nine causal signatures of dimensions two to six, for both chiralities in dimensions two and six, the pairing vanishes on all of $S \times S$ exactly at $(1,1)$, $(1,5)$ and $(5,1)$.
\item[(iv)] \emph{(Computed, exact.)} Theorem \claimref{dark-tower-matter.where-mass-begins}(i) writes the mass of two constituents as $m^{2} = 2\ip{xx^{\dagger}}_{0}$ with $x = \rev{\psi}_{1}\psi_{2}$ at $n = 3, 4$ (reproduced here on basis pairs), and (ii) there writes the one-constituent mass at $n = 5$ through $x = \rev{\psi}\psi$: in every populated causal tower mass is a function of the reversion pairing. At $(1,5)$ and $(5,1)$ the pairing is zero while the momentum sum of two basis constituents has $m^{2} = \tfrac14$. The pair law therefore does not extend to dimension six, and the two readings of a massive composite (a nonvanishing pairing between constituents; a timelike total momentum) which coincide wherever the store proves them, separate exactly at residues $0$ and $4$.
\end{enumerate}
Consequently, with one spinor ideal per tower, the emptiness of residues $0$ and $4$ (the clause of Premise \claimref{dark-matter.p3-nearest-dimension-representatives} that the unit-ball fit needs) holds at every causal representative, in every dimension, under the pairing reading, and fails at residue $4$ under the momentum reading; the choice between the two readings in dimensions $n \equiv 2 \pmod 4$ is what that clause carries. The flag bit cannot carry it: residues $0$, $4$ and the odd residues all lack the bit, and the odd residues have a nonvanishing pairing. Taking the pairing reading is a costed clause, chosen with the fit known (the unit-ball value is itself a fit, Proposition \claimref{dark-matter.status-rule}). Filed alongside, synthesis.residues-zero-four-real-chirality-anomaly cites (i) as its lemma; under its hypothesis (G6), that a residue-$4$ tower's own gauge fields live on its six-dimensional space, its anomaly result closes the momentum reading's escape at residue $4$.

## technical
In a tower of even dimension whose pseudoscalar squares to $+1$, the projectors $\tfrac12(1 \pm \omega)$ split the even subalgebra into two chirality blocks. When the dimension is $2 \bmod 4$ the reversion turns $\omega$ into $-\omega$ and so exchanges the two blocks; then $\rev{\psi}_{1}\psi_{2}$ lands in the product of the two blocks, which is zero, for any two constituents of one chirality. Among the towers with one time direction this happens exactly at residues $0$ and $4$, the two residues fixed by the reversal, in every dimension; elsewhere the even subalgebra is simple and the pairing is not zero. An exact computation confirms it at the nine lowest causal signatures.

T14c's mass formulas in dimensions three, four and five express mass through this pairing. At $(1,5)$ and $(5,1)$ the pairing is identically zero, but the total momentum of two constituents still has $m^{2} = \tfrac14$. So "mass carried by the pairing" and "mass as a timelike total momentum" agree wherever the series has proved them and disagree exactly at residues $0$ and $4$. With one spinor ideal per tower, the first reading empties residues $0$ and $4$ in every window, and the second leaves residue $4$ massive; the clause of P3 that the dark-matter fit needs is this choice, made with the fit known, and the flag bit cannot make it. Filed alongside, the anomaly result for these residues closes the momentum reading's escape at residue $4$ under the hypothesis that that tower's own gauge fields live on its six dimensions.

## lay
The dark-matter paper needs two of its eight families of hidden worlds to be empty, and so far it has simply assumed that. This result finds that exactly those two families share a peculiar algebraic feature in every dimension: the quantity the series uses to pair two building blocks into a massive particle is identically zero there, while it is not zero in the six families that are supposed to hold matter. If mass is taken to come from that pairing, as in every case the series has proved (dimensions three to five), the two families are empty automatically; if instead mass is read off from the combined motion of the building blocks, one of them is not. The assumption is thereby turned into a precise choice between two definitions that agree everywhere else.

## one-liner
In every dimension the reversion pairing on a causal tower's spinor ideal vanishes identically exactly at the reversal-fixed residues 0 and 4, so T14c's pair law (mass through the pairing) and H1's total momentum, which agree in dimensions three to five, part company there: P3's emptiness clause becomes the choice between them.
