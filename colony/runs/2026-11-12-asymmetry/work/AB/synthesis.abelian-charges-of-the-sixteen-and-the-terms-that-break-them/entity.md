---
id: synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them
kind: claim
version: 1
title: 'Abelian charges of the sixteen: only hypercharge survives every stored term'
status: proved
region: synthesis
subject: dark-matter
tags: [matter-asymmetry, hypercharge-and-anomalies, superselection]
proposed_by:
  kind: ai
  session: 2026-11-12-asymmetry
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-12-asymmetry
review: draft
derivations:
- name: main
  uses:
  - standard-model.hyp-s-slot-statistics@10
  - standard-model.automorphisms-preserve-slot-pair-split-are@7
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.majorana-element@7
  - standard-model.proton-decay-only-through-slot-pair@5
  - standard-model.imported-anomaly-coefficients@1
  - dark-tower-matter.mirrors-composition@3
  - dark-matter.superselected-hence-dark-exactly-stable@5
  - dark-matter.stored-asymmetry-charge-not-number@10
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_commutant_of_the_gauge_algebra_is_six_dimensional
- kind: check
  ref: check.py::check_dirac_majorana_and_mixing_conditions
- kind: check
  ref: check.py::check_mixed_coefficients_leave_hypercharge_only
- kind: check
  ref: check.py::check_equilibrium_generates_and_erases_baryon_number
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.stored-asymmetry-charge-not-number
  - synthesis.matter-asymmetry-registered-free-input
  - neutrino.r-descent-reheats-below-lower-heavy
extraction:
  open_problem: op.matter-asymmetry-origin
  note: >-
    Filed against the question which operator the stored asymmetry charge is. The algebra is the standard
    classification of the global charges of one family and is transport-absent; what is new for the store is
    that it is done over the whole commutant of the gauge algebra on the sixteen, so that the answer is about
    every abelian charge and not about a list of named ones, and that it is set against the three stored
    statements about the charge. The anomalous weak process itself, and the statement that it reaches
    equilibrium above the weak scale, are not stored Facts: they are literature (the anomaly of the baryon
    current, 't Hooft 1976; the equilibrium, Kuzmin, Rubakov and Shaposhnikov 1985; the coefficient 28/79,
    Harvey and Turner 1990), cited here from memory. The store already uses that equilibrium, in the check of
    dark-tower-matter.mirrors-composition. Clause (vi) is conditional on it and says so. Not done: rates, the
    freeze-out of any of the processes, the degenerate mirror plasma, three families beyond the multiplicity.
---

## formal
Under Hypothesis (S) (\claimref{standard-model.hyp-s-slot-statistics}) let the five modes be the pair modes $1, 2, 3$ and the slot modes $4, 5$, with creation operators $v_{a}$ and contractions $w_{a}$, $N_{a} = v_{a}w_{a}$, and let the sixteen be the even states of the five-mode module, with the species $Q$, $u^{c}$, $d^{c}$, $L$, $e^{c}$, $\nu^{c}$ and the charges $B - L$, $\chi$, $n_{B} = \tfrac14((B - L) + \chi)$, $n_{L} = \tfrac14(\chi - 3(B - L))$, $Y = T_{3R} + \tfrac12(B - L)$ of Propositions \claimref{standard-model.automorphisms-preserve-slot-pair-split-are} and \claimref{standard-model.proton-decay-only-through-slot-pair}. Let $\mathfrak{g} = \su(3) \oplus \su(2)_{L} \oplus \uu(1)_{Y}$, let $B$ be the invariant pairing of Lemma \claimref{standard-model.invariant-pairing-five-modes} and $T = v_{1}v_{2}v_{3}v_{4}v_{5}$ the Majorana element (\claimref{standard-model.majorana-element}).

A \emph{charge} is a pair $(X, h)$: an operator $X$ on the sixteen commuting with $\mathfrak{g}$, and a number $h$, the charge assigned to the slot creation operators $v_{4}, v_{5}$, the slot contractions $w_{4}, w_{5}$ carrying $-h$ (one doublet and its conjugate). A term $B(\psi, a\varphi)$ on the sixteen, $a$ an element of the algebra of charge $h_{a}$, \emph{conserves} $(X, h)$ if $B(X\psi, a\varphi) + B(\psi, aX\varphi) + h_{a}B(\psi, a\varphi) = 0$ for all $\psi, \varphi$ in the sixteen. A root vector $E$ \emph{carries} $X$ if $[X, E] = cE$ on the sixteen for a number $c$.
\begin{enumerate}
\item[(i)] \emph{(All the charges.)} The commutant of $\mathfrak{g}$ on the sixteen has dimension $6$: it is spanned by the projections on the six species, of dimensions $6, 3, 3, 2, 1, 1$. So a charge is seven numbers $(x_{Q}, x_{u}, x_{d}, x_{L}, x_{e}, x_{\nu}; h)$.
\item[(ii)] \emph{(Dirac terms.)} The charges conserved by every term $B(\psi, a\varphi)$ with $a$ a slot operator form a space of dimension $3$, with basis $Y$ (with $h = \tfrac12$), $n_{B}$ and $n_{L}$ (with $h = 0$). If the slot creation and contraction operators are given independent charges $h_{v}$, $h_{w}$ the space has dimension $4$, and the additional charge has colour coefficient $A_{3} = -2(h_{v} + h_{w}) \neq 0$ in the sense of (v). The unit of the module, $x = 1$ on all six species, is conserved exactly for $h_{v} = h_{w} = -2$: it is not a charge with one doublet and its conjugate, and with independent $h_{v}$, $h_{w}$ it is the additional charge up to the first three, with $A_{3} = A_{2} = 8$.
\item[(iii)] \emph{(The Majorana element.)} $B(\psi, T\varphi)$ conserves $(X, h)$ exactly when $x_{\nu} = 0$. Among the charges of (ii) these are $\mathrm{span}\{Y, n_{B}\}$: $n_{L}$ and $B - L$ are changed by two units and $n_{B}$ is not changed.
\item[(iv)] \emph{(The slot-pair root vectors.)} Each of the $24$ products $v_{a}v_{i}$, $v_{a}w_{i}$, $w_{a}v_{i}$, $w_{a}w_{i}$ ($a$ a pair mode, $i$ a slot mode) carries $Y$ and $B - L$. Among the charges of (ii), those carried by all $24$ are $\mathrm{span}\{Y, B - L\}$; $n_{B}$ is carried by none of them in the sense that $v_{1}v_{4}$ changes it by $\tfrac13$ on $\nu^{c}$ and by $-\tfrac23$ on a state of $Q$.
\item[(v)] \emph{(Mixed coefficients.)} Let $A_{2}(X) = \mathrm{tr}(4T_{3L}^{2}X)$ and $A_{3}(X) = \mathrm{tr}((N_{1} - N_{2})^{2}X)$ on the sixteen, the coefficients of the conditions $[SU(2)]^{2}U(1)$ and $[SU(3)]^{2}U(1)$ of Fact \claimref{standard-model.imported-anomaly-coefficients} for $X$ in place of $Y$, per family. Then $A_{2} = 6x_{Q} + 2x_{L}$ and $A_{3} = 4x_{Q} + 2x_{u} + 2x_{d}$; $A_{3}$ vanishes on the space of (ii); $A_{2}(Y) = A_{2}(B - L) = 0$ and $A_{2}(n_{B}) = A_{2}(n_{L}) = 2$. Among the charges of (ii), those with $A_{2} = 0$ are $\mathrm{span}\{Y, B - L\}$, and those with $A_{2} = 0$ that the Majorana element conserves are $\mathrm{span}\{Y\}$. Each of $Y$, $n_{B}$, $n_{L}$, $B - L$ has trace zero on the sixteen.
\item[(vi)] \emph{(Conditional: the equilibrium the store uses.)} Suppose the process with $A_{2} \neq 0$ acts and reaches the equilibrium whose conditions are those of the check of Computation \claimref{dark-tower-matter.mirrors-composition} (three families, one doublet), where the totals obey $B = \tfrac{28}{79}(B - L)$. Then the totals after it are a function of the total $B - L$ before it alone: initial totals $(B, L) = (0, -79)$ end with $B = 28$, and $(B, L) = (79, 79)$ end with $B = 0$.
\end{enumerate}
\emph{Reading (argued).} By (iii) to (v), no abelian charge of the sixteen other than hypercharge is conserved by every term the store holds or uses, and the charge the measured baryon density reads, $n_{B}$, is changed by two of them: the slot-pair root vectors, whose bosons are massive at the unification scale, and the process of (v), which the store uses at equilibrium. The stored statements about the asymmetry charge concern three different objects. The tower charge of Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable} is the residue $r$, constant on a tower's sector; its superselection forbids exchange between towers and implies nothing about a charge within a tower. Premise (R) of the neutrino paper protects the descent's $B - L$. Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number} speaks of baryon number. On (vi) these are reconciled only if the datum of the descent is the total $B - L$, of which the baryon number is the fraction $\tfrac{28}{79}$ in this tower, and then baryon number is generated from a state of zero baryon number, $(0, -79)$, and erased from a state with $B = L$, by a dynamics after the descent: the stored sentence that the charge cannot be produced afterwards holds for $B - L$ up to the Majorana element, not for baryon number. By the last sentence of (v) and of (ii), an excess that is the same on all sixteen states, the charge of the module's unit, carries no baryon number, no lepton number and no hypercharge, and is conserved by the Dirac terms only as the colour-anomalous fourth charge of (ii).

The algebra is standard and transport-absent. Not shown: any rate; that the process of (v) is in equilibrium at the descent's reheating temperature; the same coefficient in the mirror tower, whose plasma the cited Computation finds degenerate.

## technical
On the sixteen states of one family, every operator commuting with the Standard Model gauge algebra is a combination of the six species projections, so an abelian charge is six numbers, plus the charge of the slot doublet that enters the Dirac pairings. Requiring the Dirac pairings to conserve the charge leaves three: hypercharge, baryon number and lepton number. The Majorana element removes lepton number and $B - L$. The slot-pair generators, the ones that mediate proton decay, carry hypercharge and $B - L$ and nothing else. The mixed weak-isospin coefficient vanishes for hypercharge and $B - L$ and equals $2$ per family for baryon number and for lepton number. Hypercharge alone passes all the tests.

The equilibrium of the anomalous weak process, which the store uses for the lepton number copied to the mirror, makes the final baryon number $28/79$ of the initial $B - L$ whatever the initial baryon number was. So if that process acted after the descent, the inherited quantity is $B - L$, and baryon number is derived from it.

## lay
The series says the excess of matter over antimatter is a conserved charge planted at the beginning. This result asks which charge. Listing every candidate for one family of particles and testing each against every interaction the series holds, only hypercharge is conserved by all of them, and hypercharge cannot hold the excess. Baryon number, which is what the measured amount of ordinary matter counts, is changed by a known weak process that the series itself already uses. The quantity that process preserves is baryon number minus lepton number, and only the heavy-neutrino mass term changes that one. So what can be inherited is baryon minus lepton number, with the baryon number following from it by a fixed fraction, $28/79$.

## one-liner
On the sixteen, the commutant of the Standard Model algebra is six-dimensional; Dirac pairings conserve $\mathrm{span}\{Y, n_{B}, n_{L}\}$, the Majorana element leaves $\{Y, n_{B}\}$, the slot-pair root vectors and the mixed weak coefficient leave $\{Y, B - L\}$, so only $Y$ survives all; under the equilibrium the store uses, $B = \tfrac{28}{79}(B - L)$ and baryon number is not the conserved datum.
