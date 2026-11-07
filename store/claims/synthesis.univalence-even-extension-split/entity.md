---
id: synthesis.univalence-even-extension-split
kind: claim
version: 3
title: 'Univalence as the choice of the even extension'
status: proved
region: synthesis
subject: descent
tags: [univalence, superselection, car-algebra, thermal-premises]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.singularity.grading-parity-automorphism
derivations:
- name: main
  uses:
  - singularity.imported-univalence-superselection-rule@2
  - singularity.descended-form-state-independent@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_even_part_is_unique_even_extension
- kind: check
  ref: check.py::check_ladder_kms_admits_coherence
- kind: check
  ref: check.py::check_full_kms_forces_single_mode_evenness
- kind: check
  ref: check.py::check_cross_mode_odd_correlation_with_even_gibbs_marginals
- kind: check
  ref: check.py::check_graded_product_has_one_odd_factor_at_most
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.p-univalence
  - singularity.r-regularity-fixed-locus
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. The Killing flow Ad(e^{it omega N}) on the completed modes'' factor and its continuation alpha_{ip}: by U2 the unit is J = e_2 e_3 (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited as a mention): Ad(e^{J t omega_k N_k}), alpha_{Jp}, mode factor over span{1, J}. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the proof continues the Killing flow Ad(e^{it omega N}) on the complex mode factor Mat_2(C) to imaginary time (alpha_{ip}) for the KMS relation; the store does not tie that factor''s complex structure to I_4.'
  open_problem: pr.p-univalence
  note: >-
    Isolates what (P) adds beyond the observable clause of the imported superselection rule:
    nothing observable; it selects the even extension of the physical state on the even
    subalgebra. The imported Fact states both "the observable algebra is the even subalgebra"
    and "physical states are even"; the first is the Wick-Wightman-Wigner content, the second is
    (P) itself, so citing the import for (P) is a restatement, not a derivation. Clause (iii)
    uses a reading of (R) on the whole mode factor, which is stronger than (R) as stated (ladder
    pairs only); it is offered as the natural reading of "each single-mode marginal is KMS", and
    adopting it is a decision about the premise. By reading their statements, the consumers
    singularity.ascended-marginals-are-diagonal, singularity.rate-discharge-hypothesis-iii and
    synthesis.boundary-mode-thermal-entropy use (P) only through omega(v_k) = 0 at single modes,
    the part (iii) supplies; singularity.chains-state-class-stability defines its class as even
    states and so uses the cross-mode part as well (argued, not checked). Transport-convenient:
    the grading is the Clifford grading of the completed pair, the statements are about Z2-graded
    algebras. Complementary to synthesis.univalence-from-even-stationary-dynamics (filed alongside):
    that result derives (P) for joint Gibbs and stationary states of even generators, of which (iii)
    is the one-mode case; the counter-states of (ii) and (iv) are neither stationary for a
    nonzero-weight flow nor Gibbs, so the two results are consistent: (P) has no observable content
    beyond the even observables, and it follows from joint equilibrium.
---

## formal
Let $\Aa$ be the boundary-mode algebra of $N$ completed modes with parity automorphism $\alpha = \operatorname{Ad}(\Gamma)$ (Definition \claimref{obj.singularity.grading-parity-automorphism}), even part $\Aev$, odd part $\Aod$, and $E := \tfrac12(\mathrm{id} + \alpha)$. Write (R) for Premise \claimref{singularity.r-regularity-fixed-locus} and (P) for Premise \claimref{singularity.p-univalence}.
\begin{enumerate}
\item[(i)] \emph{(Even extension.)} For every state $\omega$ on $\Aa$, $\omega \circ E$ is an even state equal to $\omega$ on $\Aev$, and it is the only even state with that restriction. So the states of the even subalgebra, the observables of Fact \claimref{singularity.imported-univalence-superselection-rule}, correspond one to one to the even states of $\Aa$, and (P) says exactly that the state on $\Aa$ is the even extension of its restriction to the observables. No expectation value of an even element distinguishes $\omega$ from $\omega \circ E$; what (P) fixes are the odd expectation values, among them the off-diagonal entries $\omega(v_k)$ of the ascended single-mode marginals.
\item[(ii)] \emph{(R) as stated does not give (P).} At a mode of weight $\omega_k$, with $n = (e^{p\omega_k} + 1)^{-1}$ and $0 < c^2 \leq n(1 - n)$, the state $\varrho = \begin{psmallmatrix} 1 - n & c \\ c & n \end{psmallmatrix}$ of the mode factor satisfies the KMS relation of (R) for every pair in the ladder $\{v_k, v_k^{*}\}$, has the Gibbs state as its descended marginal, and has $\omega(v_k) = c \neq 0$.
\item[(iii)] \emph{(Full-factor KMS gives the single-mode part.)} If the marginal at mode $k$ satisfies the KMS relation of (R) for all pairs $a, b$ in the mode factor $\Mat_2(\C)$, it is the Gibbs state of $K_k$, so $\omega(v_k) = 0$; this holds at every weight, and at zero weight the relation is traciality and gives the marginal $\tfrac12$.
\item[(iv)] \emph{(The cross-mode part is not local.)} For $N \geq 2$, single-mode evenness at every mode does not imply (P): on two modes, $\varrho = \varrho_1 \otimes \varrho_2 + c\,(v_1 + v_1^{*})(1 - 2v_2^{*}v_2)$ in the Jordan-Wigner representation, with $\varrho_1, \varrho_2$ diagonal Gibbs states and $c \neq 0$ small, is a state whose two single-mode marginals are $\varrho_1$ and $\varrho_2$ and which gives the odd element $(v_1 + v_1^{*})(1 - 2v_2^{*}v_2)$ the value $4c$.
\item[(v)] \emph{(Graded products.)} If $\omega(xy) = \omega(x)\omega(y)$ for $x$ in the algebra of one set of modes and $y$ in that of a disjoint set, at most one of the two restrictions is non-even.
\end{enumerate}
So (P) is the conjunction of a single-mode part, $\omega(v_k) = 0$ at every $k$, which the full-factor reading of (R) supplies, and a cross-mode part, the vanishing of odd correlations across modes, which no single-mode condition supplies and which no even observable detects.

## technical
The univalence premise (P) asks every physical state of the boundary modes to be even. The superselection rule it is usually traced to says that only even elements are observable. These are different statements: every state on the even observables has exactly one even extension to the whole algebra, $\omega \circ E$, and agrees with every other extension on all observables, so (P) is the choice of that extension and has no consequence for any even observable. What (P) fixes are odd expectation values, including the off-diagonal entries of the single-mode marginals. Its single-mode part follows if the regularity premise (R) is read on the whole mode factor rather than on the ladder pairs alone: such a marginal is Gibbs, hence diagonal, at every weight. As stated, (R) admits coherent non-even marginals. The cross-mode part, no odd correlation between modes, follows from no single-mode condition, as a two-mode model shows. A product state across disjoint sets of modes can be non-even on one factor at most.

## lay
The series assumes that the physical states of the boundary modes never mix states with an even and an odd number of particles. A standard rule of quantum theory already says that such mixtures cannot be observed. This result shows the assumption adds nothing that any measurement could see. It is a choice of bookkeeping for quantities nobody can measure. Part of it follows if each mode is required to be thermal in the full sense. The rest, about correlations between different modes, does not follow from anything said about one mode at a time.

## one-liner
(P) is the choice of the even extension and changes no even observable; its single-mode part follows from (R) read on the whole mode factor (not from (R) as stated), and its cross-mode part from no single-mode condition.
