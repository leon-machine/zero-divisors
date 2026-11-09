---
id: synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free
kind: claim
version: 1
title: 'The descent leaves the odd towers'' dimension free: a Bott-shifted second model'
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
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_bott_shift_splits_off_a_real_matrix_factor
- kind: check
  ref: check.py::check_tensor_split_is_an_isomorphism
- kind: check
  ref: check.py::check_eight_of_one_sign_is_real_sixteen_by_sixteen
- kind: check
  ref: check.py::check_type_data_read_by_every_stored_selector_are_invariant
- kind: check
  ref: check.py::check_descent_premises_hold_in_both_models
- kind: check
  ref: check.py::check_unit_ball_ratio_differs_between_models
- kind: check
  ref: check.py::check_w_admits_m_l_and_not_m_8
- kind: proof
  derivation: main
extraction:
  open_problem: op.window-p3
  note: >-
    Attack on the remaining clause of op.window-p3, the lowest causal representative: an independence proof, as the
    success clause allows ("show the descent leaves it free"). The method is a second model of every premise the
    window-sensitive results rest on, P3 excepted, at the pinned versions (the union of the past cones of the
    census, the unit-ball rule, the residue 0 and 4 results, the oriented-causal theorem, the flag bit and the
    invariant-form results): the foundation premises F1 to F4, P1, P2, the single-clock filter, the costed
    single-ideal clause, H1, R1 to R3, the series' indifference premise and the imported Facts (Chevalley's blade
    basis, Witt, Morita amplification, the Clifford structure and classification, the Fock representation, the
    anomaly coefficients, the inverse-square law, and imports that do not mention a tower's dimension). The second
    model moves the odd representatives by Bott's shift of eight directions of the majority sign. Prior art, cited
    from memory, not premises: R. Bott's periodicity and its algebraic form Cl(p+8,q) = Cl(p,q) (x) Mat(16,R)
    (M. F. Atiyah, R. Bott and A. Shapiro, Topology 3 (1964) suppl. 1, 3-38; P. Lounesto, Clifford Algebras and
    Spinors, Cambridge 2001); new here is the use of the shift as a second model of the descent's premises, the
    explicit geometric-algebra split with the reversion, and the costing of the window. The emptiness of residues 0
    and 4 is a separate costed clause and is not touched. Transport-absent: the result is Clifford classification
    and model theory of the premises; nothing uses transport. What is not claimed: that no future premise could
    fix the window; that (W) is false; anything about which window the descent actually used.
---

## formal
Call a signature $(p,q)$ causal if $\min(p,q) = 1$, and let $\beta$ add eight directions of the majority sign: $\beta(p,q) = (p+8,q)$ if $p > q$, $(p,q+8)$ if $q > p$. Let $M_{L}$ represent residues $6, 2, 1, 7, 3, 5$ by $(1,3), (3,1), (2,1), (1,2), (4,1), (1,4)$, the lowest causal member of each (the representatives Premise \claimref{dark-matter.p3-nearest-dimension-representatives} gives these residues), and let $M_{8}$ agree with $M_{L}$ except at the odd residues, where it takes $(10,1), (1,10), (12,1), (1,12)$; residues $0$ and $4$ are treated alike in both, by the costed single-ideal clause of Observation \claimref{dark-matter.status-rule}(vi).
\begin{enumerate}
\item[(i)] \emph{(The shift splits off a real matrix factor; proved, exact.)} For a causal $s = (p,q)$ of dimension $n$ let $\omega_{8}$ be the product of the eight added vectors of $\beta s$. Then $\omega_{8}^{2} = 1$, the elements $a_{i} = e_{i}\omega_{8}$ ($i \le n$) obey the relations of $\Cl(p,q)$, are fixed by reversion and commute with the eight added vectors, and $\Cl(\beta s) = A \otimes B$ with $A = \langle a_{i}\rangle \cong \Cl(p,q)$ and $B$ the algebra of the added vectors, $B \cong \Mat(16,\R)$, reversion acting factor by factor. $B$ has a primitive idempotent $f$ with $\widetilde{f} = f$ and $fBf = \R f$, so its reversion pairing on $Bf$ is symmetric. Hence $\Cl(\beta s) \cong \Mat(16, \Cl(s))$ with its reversion, every spinor ideal of $\Cl(\beta s)$ is an ideal of $\Cl(s)$ tensored with $\R^{16}$, and $s$ and $\beta s$ have the same residue, causality, dimension mod $8$, pseudoscalar square and centrality, Clifford type and reversion-pairing type.
\item[(ii)] \emph{(Both are models of the descent's premises; proved.)} $M_{L}$ and $M_{8}$ each satisfy every premise of the window-sensitive results other than P3: F1 to F4 (each representative's generators carry the sign bits), the eight-tower clock (each representative has its residue), the single-clock filter (all populated representatives are causal), Premise \claimref{dark-matter.p1-single-frozen-point} (one frozen point and one metric; its orientation clause acts on residues $2$ and $6$, which the models share, and the odd representatives have odd dimension in both, so neither has an orientable odd tower), Premise \claimref{dark-matter.p2-indifference} (each model is closed under reversal, since $\beta$ commutes with $(p,q) \mapsto (q,p)$), the costed clause, H1 and the constituent definitions (transported through (i)), the anomaly import (odd dimensions carry no local anomaly in either), and the inverse-square law (in neither model does a tower's unshared direction carry the one metric). Every stored structural selector (flag bit, chirality type, anomaly degree, pairing type) takes the same value on $s$ and $\beta s$ by (i). So nothing in the descent, P3 aside, separates $M_{L}$ from $M_{8}$, and since $\beta$ can be iterated there are infinitely many models: the lowest-causal clause of P3 is independent of the descent.
\item[(iii)] \emph{(The stored selector that does separate them.)} Premise (W) of \claimref{synthesis.frozen-point-complement-window-lowest-causal} admits every representative of $M_{L}$ and no odd representative of $M_{8}$, and up to dimension sixteen the lowest causal member is the only admitted causal member of each odd residue. (W) is not periodic along a residue and is not in the premise set; it was found with the fit known and is not adopted.
\item[(iv)] \emph{(Cost.)} With R1 to R3 read in their dimension-generic form (share $V_{3}/V_{D}$ for a space of dimension $D$, one cell radius per unshared direction), the dark-to-baryon ratio is $(11\pi + 16)/3\pi \in (5.36, 5.37)$ in $M_{L}$ and $1 + 320/\pi^{4} + 1920/\pi^{5} \in (10.5, 10.6)$ in $M_{8}$. The window is therefore a recorded input of the unit-ball relation, selected among the models by the observed ratio, and P3 stays as a costed premise; the results stored under P3 about the odd towers (their types, contents and cell counts) hold given P3 and do not follow from the descent.
\end{enumerate}

## technical
Every residue mod 8 has infinitely many causal signatures, spaced by eight dimensions along each sign: adding eight directions of the majority sign keeps exactly one time direction and the residue. In geometric algebra the shift is explicit: multiplying each old generator by the product of the eight new ones gives a copy of the old algebra that commutes with the new eight, and the new eight generate a sixteen by sixteen real matrix algebra, so the shifted algebra is the old one tensored with real matrices, reversion included. All the data the series uses to sort towers (residue, causality, whether the tower can carry the flag bit, real chirality, the parity relevant to anomalies, the type of the invariant pairing) are unchanged. So a second model of every premise of the descent other than P3 puts the odd towers at dimensions eleven and thirteen instead of three and five, keeping this world, its mirror and the costed treatment of residues 0 and 4. The descent cannot fix the lowest causal member; P3 does. The one stored hypothesis that would, premise (W), is not periodic and is not adopted. Cost: the dark-to-baryon ratio changes from 5.364 to about 10.56 between the two models, so the window is an input of the fit, chosen by the observed value.

## lay
The series sorts possible hidden worlds into eight families, and each family contains worlds of many different dimensions, each with a single time direction. To predict how much dark matter there is, the series picks the smallest such world in each family, by an assumption. This result shows the assumption cannot be derived from the rest of the theory: adding eight dimensions to the odd families' worlds changes nothing that any other assumption of the theory looks at, because the extra eight dimensions only multiply the algebra by a table of real numbers. The two versions predict different amounts of dark matter (about 5.4 and about 10.6 times the ordinary matter), so the choice of the smallest worlds is an input that the observed amount selects, not a prediction.

## one-liner
Adding eight directions of the majority sign splits off a $\Mat(16,\R)$ factor (reversion included) and fixes every selector the series uses, so a second model with the odd towers at $(10,1), (1,10), (12,1), (1,12)$ satisfies every premise of the descent except P3: the lowest-causal window is independent, P3 stays costed, and the unit-ball ratio becomes about $10.56$ instead of $5.364$.
