---
id: synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free
kind: claim
version: 1
title: 'The five-dimensional towers'' dimension is free; Premise U fixes the three-dimensional ones'
status: proved
region: synthesis
subject: dark-matter
tags: [towers-by-residue, clifford-classification, undetermined-input, dark-matter-ratio, premises-p1-p5]
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
  - dark-matter.imported-eight-towers-mod-8-clock@4
  - tower.morita-equivalence-algebra-amplification@2
  - dark-tower-matter.imported-clifford-structure@1
  - synthesis.oriented-causal-towers-mirror-pair-every-window@2
  - synthesis.residues-zero-four-real-chirality-anomaly@4
  - synthesis.frozen-point-complement-window-lowest-causal@2
  - synthesis.gauge-algebra-by-tower@1
  - dark-tower-matter.constituents-field@2
  - dark-tower-matter.residue-seven-unit@3
  assumes:
  - dark-tower-matter.u-transposition-rule@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_bott_shift_splits_off_a_real_matrix_factor
- kind: check
  ref: check.py::check_tensor_split_is_an_isomorphism
- kind: check
  ref: check.py::check_eight_of_one_sign_is_real_sixteen_by_sixteen
- kind: check
  ref: check.py::check_type_data_invariant_and_pair_count_not
- kind: check
  ref: check.py::check_descent_premises_hold_in_both_models
- kind: check
  ref: check.py::check_premise_u_admits_the_shift_only_at_residues_three_and_five
- kind: check
  ref: check.py::check_unit_ball_ratio_differs_between_models
- kind: check
  ref: check.py::check_w_admits_m_l_and_not_m_8
- kind: proof
  derivation: main
extraction:
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Leon approved the assumes edge named at acceptance: Premise U (dark-tower-matter.u-transposition-rule@2), used directly in clause (iii), is now assumed; statement unchanged.'
  open_problem: op.window-p3
  note: >-
    Attack on the remaining clause of op.window-p3, the lowest causal representative, by a second model of every
    premise the window-sensitive results rest on, P3 excepted, at the pinned versions (the union of the past cones
    of the census, the unit-ball rule, the residue 0 and 4 results, the oriented-causal theorem, the flag bit, the
    invariant-form results and the odd towers' content and gauge algebras): the foundation premises F1 to F4, P1,
    P2, the single-clock filter, the costed single-ideal clause, H1, H2, Premise U, Hypothesis (S), R1 to R3, the
    series' indifference premise, and the postulates reached through the stored dark-matter and boundary-mode
    results (T14's (U) on rank-one eigenvalues, P4, P5, CPT covariance, the flag as datum, the interface premise
    (I), (P), (Q), (R), the rate inputs (L, U), the slot-module and common-ceiling premises, tameness), with the
    imported Facts (Chevalley's blade basis, Witt, Morita amplification, the Clifford structure and
    classification, the Fock representation, the anomaly coefficients, the inverse-square law, and imports that
    do not mention a tower's dimension). The model moves residues 3 and 5 by Bott's shift of eight directions of
    the majority sign. At residues 1 and 7 the same shift breaks Premise U (U3): the constituent field is R in
    every causal member there and the stored pair count exceeds the real Witt index above dimension three, so U
    admits only the lowest member; this clause is the result at residues 1 and 7, not an independence. Prior art,
    cited from memory, not premises: R. Bott's periodicity and its algebraic form Cl(p+8,q) = Cl(p,q) (x) Mat(16,R)
    (M. F. Atiyah, R. Bott and A. Shapiro, Topology 3 (1964) suppl. 1, 3-38; P. Lounesto, Clifford Algebras and
    Spinors, Cambridge 2001); new here are the use of the shift as a second model of the descent's premises, the
    explicit geometric-algebra split with the reversion, the U3 computation along residues 1 and 7, and the
    costing of the window. The emptiness of residues 0 and 4 is a separate costed clause and is not touched.
    Transport-absent: Clifford classification and model theory of the premises; nothing uses
    transport. What is not claimed: that no future premise could fix the five-dimensional window; that (W) is
    false; anything about which window the descent used.
---

## formal
Call a signature $(p,q)$ causal if $\min(p,q) = 1$, and let $\beta$ add eight directions of the majority sign: $\beta(p,q) = (p+8,q)$ if $p > q$, $(p,q+8)$ if $q > p$. Let $M_{L}$ represent residues $6, 2, 1, 7, 3, 5$ by $(1,3), (3,1), (2,1), (1,2), (4,1), (1,4)$, the lowest causal member of each (the representatives Premise \claimref{dark-matter.p3-nearest-dimension-representatives} gives these residues), and let $M_{8}$ agree with $M_{L}$ except at residues $3$ and $5$, where it takes $(12,1)$ and $(1,12)$; residues $0$ and $4$ are treated alike in both, by the costed single-ideal clause of Observation \claimref{dark-matter.status-rule}(vi).
\begin{enumerate}
\item[(i)] \emph{(The shift splits off a real matrix factor; proved, exact.)} For a causal $s = (p,q)$ of dimension $n$ let $\omega_{8}$ be the product of the eight added vectors of $\beta s$. Then $\omega_{8}^{2} = 1$, the elements $a_{i} = e_{i}\omega_{8}$ ($i \le n$) obey the relations of $\Cl(p,q)$, are fixed by reversion and commute with the eight added vectors, and $\Cl(\beta s) = A \otimes B$ with $A = \langle a_{i}\rangle \cong \Cl(p,q)$ and $B$ the algebra of the added vectors, $B \cong \Mat(16,\R)$, reversion acting factor by factor; $B$ has a primitive idempotent $f$ with $\widetilde{f} = f$ and $fBf = \R f$, so its reversion pairing on $Bf$ is symmetric. Hence $\Cl(\beta s) \cong \Mat(16, \Cl(s))$ with its reversion, and $s$, $\beta s$ have the same residue, causality, dimension mod $8$, pseudoscalar square and centrality, Clifford type, constituent field and reversion-pairing type. Not invariant: the complex Witt index $\lfloor(n+2)/2\rfloor$ of the conformal space $\hatV$, the stored number of ladder pairs, rises by $4$, and with it the content the gauge-algebra rule computes.
\item[(ii)] \emph{(Residues $3$ and $5$: both are models of the descent's premises; proved.)} $M_{L}$ and $M_{8}$ each satisfy every premise of the window-sensitive results other than P3: F1 to F4, the eight-tower clock, the single-clock filter, Premise \claimref{dark-matter.p1-single-frozen-point} (one frozen point and one metric; its orientation clause acts on residues $2$ and $6$, shared by the models, and no odd tower is oriented in either), Premise \claimref{dark-matter.p2-indifference} (each model is closed under reversal), the costed clause, H1, H2 and Hypothesis (S) (stated for every signature), Premise \claimref{dark-tower-matter.u-transposition-rule} (U) (at $(12,1)$ and $(1,12)$ the field is $\HH$, which supplies the unit for the five pairs beyond the two real ones), the anomaly import (odd dimensions carry no local anomaly), the inverse-square law (no tower's unshared direction carries the one metric), R1 and R3 in their dimension-generic form, and R2 in its dimension-generic reading (its stated list of dimensions $2$, $3$, $4$ is P3's window, which $M_{8}$ leaves); the remaining postulates of the cone do not mention a tower's dimension beyond $n \bmod 4$, which $\beta$ preserves. So nothing in the descent, P3 aside, fixes the five-dimensional towers' dimension; $\beta$ can be iterated, giving a model with those towers at dimension $5 + 8k$ for every $k \ge 0$.
\item[(iii)] \emph{(Residues $1$ and $7$: Premise U fixes the window; proved, given U.)} Along residues $1$ and $7$ the constituent field is $\R$ in every causal member (\claimref{dark-tower-matter.constituents-field}, invariant under $\beta$ by (i)), the real Witt index of $\hatV$ is $2$ and the stored pair count is $\lfloor(n+2)/2\rfloor$ (\claimref{synthesis.gauge-algebra-by-tower}), which exceeds $2$ for $n > 3$. U3 requires the unit that builds each further pair to lie in the field, which $\R$ cannot supply; the conformal pseudoscalar along residue $7$ is central of square $-1$ but odd and does not act on the constituent ideal (\claimref{dark-tower-matter.residue-seven-unit}). So U admits only $(2,1)$ and $(1,2)$: at residues $1$ and $7$ the lowest-causal clause of P3 follows from Premise U, and P3 is not needed there.
\item[(iv)] \emph{(The stored selector that separates the models.)} Premise (W) of \claimref{synthesis.frozen-point-complement-window-lowest-causal} admits every representative of $M_{L}$ and neither shifted representative of $M_{8}$; up to dimension sixteen the lowest causal member is the only admitted causal member of each odd residue. (W) is not in the premise set; it was found with the fit known and is not adopted.
\item[(v)] \emph{(Cost.)} With R1 to R3 read in their dimension-generic form (share $V_{3}/V_{D}$ for a space of dimension $D$, one cell radius per unshared direction), the dark-to-baryon ratio is $(11\pi + 16)/3\pi \in (5.36, 5.37)$ in $M_{L}$ and $1 + 8/3 + 1920/\pi^{5} \in (9.9, 10.0)$ in $M_{8}$. The five-dimensional towers' dimension is therefore a recorded input of the unit-ball relation, selected among the models by the observed ratio, and P3 stays a costed premise for residues $3$ and $5$; the results stored under P3 about the five-dimensional towers' content hold given P3.
\end{enumerate}

## technical
Every residue mod 8 has infinitely many causal signatures, spaced by eight dimensions along each sign. Multiplying each old generator by the product of eight new ones of the majority sign gives a copy of the old algebra that commutes with the new eight, which generate a sixteen by sixteen real matrix algebra; so the shifted algebra is the old one tensored with real matrices, reversion included, and residue, causality, flag bit, real chirality, anomaly parity, pairing type and the constituents' field are unchanged. The number of ladder pairs, the complex Witt index of the conformal space, is not unchanged: it grows by four. At residues 3 and 5 that does no harm, since the constituents' field is the quaternions, which supply the unit each extra pair needs; a second model of every premise other than P3 puts the five-dimensional towers at dimension thirteen, keeping everything else, and the dark-to-baryon ratio becomes about 9.94 instead of 5.364. At residues 1 and 7 the field is real in every causal member, so Premise U, which forbids an outside imaginary unit, admits only the three-dimensional member: there the window follows from U. The one stored hypothesis that would fix the five-dimensional window, premise (W), is not periodic and is not adopted.

## lay
The series sorts possible hidden worlds into eight families, each containing worlds of many different dimensions with a single time direction, and to predict the amount of dark matter it picks the smallest world in each family by an assumption. For the two families whose smallest worlds are three-dimensional, another assumption of the theory, that no imaginary unit may be brought in from outside, already rules out every larger world: there the choice is derived. For the two families whose smallest worlds are five-dimensional it is not: adding eight dimensions changes nothing that any other assumption looks at, and gives a different amount of dark matter (about 9.9 instead of 5.4 times the ordinary matter). So for those families the choice of the smallest world is an input that the observed amount selects, not a prediction.

## one-liner
Adding eight directions of the majority sign splits off a $\Mat(16,\R)$ factor (reversion included); at residues $3$, $5$ a second model with the towers at $(12,1)$, $(1,12)$ satisfies every premise except P3, Premise U included (field $\HH$), so that window is an input (ratio about $9.94$ instead of $5.364$), while at residues $1$, $7$ the field is $\R$ in every causal member and U admits only $(2,1)$, $(1,2)$.
