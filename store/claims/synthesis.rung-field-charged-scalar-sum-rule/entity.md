---
id: synthesis.rung-field-charged-scalar-sum-rule
kind: claim
version: 2
title: For the rung field's D-term action with an added invariant $W(N)$ of the norm alone, the charged pair and the neutral mode obey the tree-level sum rule $(m_{\pm}^{2} - M_{W}^{2}) - (m_{h}^{2} - M_{Z}^{2}) = 2(m^{*}/N^{*})^{2}(W' - N^{*}W'')$; $W = \kappa N^{2}$, the only such $W$ of $N$ alone with no dimensionful constant and no dependence on the level, gives $m_{\pm}^{2} = M_{W}^{2} + m_{h}^{2} - M_{Z}^{2}$ at tree level, about $117$ GeV
status: proved
region: synthesis
subject: standard-model
tags: [symmetry-breaking, gauge-fields, undetermined-input, confronted-with-data]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
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
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@3
  - synthesis.rung-field-on-the-lift-locus@2
  proof: proof-main.tex
quantities:
- quantity.z-boson-mass@2
- quantity.weak-mixing-angle-mz@1
- quantity.top-quark-mass@1
- quantity.bottom-quark-mass@1
- quantity.higgs-boson-mass@1
checked_by:
- kind: check
  ref: check.py::check_charged_scalar_sum_rule
- kind: check
  ref: check.py::check_scale_free_invariant_gives_the_equal_shift
- kind: check
  ref: check.py::check_prediction_bracket_from_record_inputs
- kind: check
  ref: check.py::check_moment_map_invariant_breaks_the_equality
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus
  - synthesis.rung-unit-second-free-number
extraction:
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 2: the measured Higgs mass, an input of (iii), is now the stored quantity.higgs-boson-mass (PDG 2024, 125.20 +- 0.11 GeV, checked against the source) instead of a value cited from memory; the check reads it and certifies that it lies in the bracket [125, 125.4] GeV used, and the proof says so. The measured W mass of the proof''s aside (stored as quantity.w-boson-mass) and the minimal supersymmetric sum rule of the note (stored as synthesis.imported-mssm-charged-higgs-tree-sum-rule) are not premises of the statement and are not pinned. The Z mass is repinned to quantity.z-boson-mass@2 (PDG 2024, 91.1880 GeV), and the proof''s sin^2 theta_W M_Z^2 is recomputed (1922.65 GeV^2); the brackets are unchanged. Statement unchanged.'
  open_problem: op.rung-unit
  note: >-
    The problem's first line of attack (supply the second invariant W(N) and check the charged pair against
    charged-scalar searches), taken adversarially. The stored D-term result gives m_h^2 and m_pm^2 each in
    terms of W'(N*) and W''(N*); eliminating W'' on the boundary N*^2 = m*^2 + H^4 gives an exact tree-level
    sum rule whose defect is 2 (m*/N*)^2 (W' - N* W''), which vanishes exactly for W = kappa N^2 among
    functions of N (W' proportional to N). The equality is special to functions of N alone: the invariant
    kappa m^2 of the hypercharge moment map also adds no dimensionful constant and gives a nonzero defect
    (exact, checked), and a term built from the level xi already in the action leaves a defect of order v^2.
    Within functions of N with no dimensionful constant and no dependence on the level (constants built from H
    are suppressed by (H/v)^2), W = kappa N^2 gives at tree level m_pm^2 = M_W^2 + m_h^2 - M_Z^2, about
    117.5 GeV with the measured W mass (cited from memory) or 117.3 GeV with the tree relation and the stored
    sin^2 theta_W. The measured, loop-corrected m_h is inserted in a tree relation; loop corrections are not
    estimated. The value is below m_t - m_b, so t -> b H+ is open; whether the searches in top decays exclude
    it depends on the charged pair's fermion couplings, which the store does not fix (argued, from memory:
    with couplings of the size of the neutral rung coupling it would be excluded). Technique imported from the
    minimal supersymmetric tree sum rule m_pm^2 = m_A^2 + M_W^2 (memory); here no second neutral field exists,
    and m_h itself enters. Transport-absent in content (tree-level field theory on the stored lift locus).
---

## formal
In the setting of \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}: the rung field on the null-lift locus $L = \{Q(c) = -H^{2}\}$ with the Hermitian kinetic term, the potential $V = V_{D} + W(N)$ with $V_{D}$ the hypercharge D-term action at level $\xi$ and $W$ a function of the Hermitian norm $N$, a charge-preserving vacuum on the lift family at $(N^{*}, m^{*})$ with $N^{*2} = m^{*2} + H^{4}$, $M_{W}^{2} = \tfrac12 g^{2}N^{*}$ and $M_{Z}^{2} = \tfrac12(g^{2} + g'^{2})N^{*}$.
\begin{enumerate}
\item[(i)] \emph{(Sum rule, tree level.)} For $W$ a function of $N$ alone the two charged modes are degenerate, and
\[
(m_{\pm}^{2} - M_{W}^{2}) - (m_{h}^{2} - M_{Z}^{2}) = 2\Bigl(\frac{m^{*}}{N^{*}}\Bigr)^{2}\bigl(W'(N^{*}) - N^{*}W''(N^{*})\bigr).
\]
\item[(ii)] \emph{(Functions of $N$ alone.)} Among functions of $N$, the defect vanishes at every vacuum exactly when $W'(N) = 2\kappa N$, that is $W = \kappa N^{2}$ up to a constant, the only function of $N$ alone that adds no dimensionful constant and no dependence on the level; then $m_{\pm}^{2} - M_{W}^{2} = m_{h}^{2} - M_{Z}^{2} = 4\kappa N^{*}$ in every frame. A linear term $\mu N$ leaves the defect $2\mu(m^{*}/N^{*})^{2}$, of modulus below $2|\mu|$; a term built from the cosmological scale, $\mu = O(H^{2})$, shifts $m_{\pm}^{2}$ relative to $M_{W}^{2}$ by $O(H^{2}/N^{*})$. An invariant depending on the hypercharge moment map, such as $\kappa m^{2}$, also adds no dimensionful constant and breaks the equality: for $\kappa = \tfrac15$ with the level re-solved for criticality the defect is $-\tfrac{17}{10}$ at $\lambda^{*} = \tfrac12$ and $-\tfrac{164}{45}$ at $\lambda^{*} = 3$ (with $H^{2} = 1$, $g = \tfrac23$, $g' = \tfrac12$).
\item[(iii)] \emph{(Tree-level value from the record.)} With $W = \kappa N^{2}$ and the tree relation $M_{W}^{2} = (1 - \sin^{2}\theta_{W})M_{Z}^{2}$, at tree level $m_{\pm}^{2} = m_{h}^{2} - \sin^{2}\theta_{W}M_{Z}^{2}$; with the stored $M_{Z}$ and $\sin^{2}\theta_{W}(M_{Z})$ and $m_{h} \in [125, 125.4]$ GeV, $116 < m_{\pm} < 119$ GeV, below $m_{t} - m_{b}$ and above the kinematic pair threshold of $105$ GeV at the highest LEP energies.
\end{enumerate}

## technical
The stored D-term action for the rung field fixes the Higgs-like neutral mode at $M_{Z}$ and the charged pair at $M_{W}$ at tree level, so a second invariant is owed, and for an invariant $W(N)$ of the norm alone the stored formulas give both masses in terms of its first two derivatives at the vacuum. Eliminating them leaves one combination: at tree level the difference of the two shifts is $2(m^{*}/N^{*})^{2}(W' - N^{*}W'')$, which vanishes exactly for the quartic $W = \kappa N^{2}$, the only function of $N$ alone that adds no constant. Then the charged pair sits at $\sqrt{M_{W}^{2} + m_{h}^{2} - M_{Z}^{2}} \approx 117$ GeV at tree level, light enough to appear in top decays; whether present searches exclude it depends on its couplings to quarks, which the series has not derived. The equality is not forced by the absence of constants in general: an invariant depending on the hypercharge moment map, such as $\kappa m^{2}$, also adds no constant and breaks it. A charged mass away from the tree value measures either a scale in $W(N)$, a dependence on the moment map, or loop corrections.

## lay
The series' candidate for the Higgs field comes with a pair of electrically charged partners. A simple version of its energy function gives the wrong Higgs mass, so an extra term is needed; this result shows that, for an extra term that depends only on the field's overall size, the charged partners' mass and the Higgs mass are tied by one exact relation at lowest order. If the extra term depends only on the field's overall size and introduces no new energy scale, then at lowest order the charged partners weigh about 117 GeV, light enough to be produced in top-quark decays. Extra terms of other kinds, even without a new scale, move that value.

## one-liner
For the rung field's D-term action plus an invariant $W(N)$ of the norm alone, at tree level $(m_{\pm}^{2} - M_{W}^{2}) - (m_{h}^{2} - M_{Z}^{2}) = 2(m^{*}/N^{*})^{2}(W' - N^{*}W'')$, so $W = \kappa N^{2}$, the only function of $N$ alone that adds no constant, gives $m_{\pm}^{2} = M_{W}^{2} + m_{h}^{2} - M_{Z}^{2}$ at tree level, a charged pair near $117$ GeV open to top decays; an invariant depending on the hypercharge moment map, such as $\kappa m^{2}$, also adds no constant and breaks the equality.
