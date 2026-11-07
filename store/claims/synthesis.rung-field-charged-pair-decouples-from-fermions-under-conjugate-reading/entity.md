---
id: synthesis.rung-field-charged-pair-decouples-from-fermions-under-conjugate-reading
kind: claim
version: 4
title: 'The charged pair decouples from fermions under the per-sector reading'
status: proved
region: synthesis
subject: standard-model
tags: [symmetry-breaking, gauge-fields, confronted-with-data]
proposed_by:
  kind: ai
  session: 2026-11-01-weak-scale
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'consistency pass, Lie-algebra name written with its macro'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@4
  - synthesis.rung-field-on-the-lift-locus@3
  - standard-model.one-vev-vector-relations-breaking-pattern@7
  - standard-model.yukawa-pattern-two-rung-module@6
  - standard-model.imported-tower-commuting-copies-fock-module@5
  - synthesis.rung-field-charged-scalar-sum-rule@2
  - synthesis.imported-atlas-charged-higgs-top-decay-tau-nu-limits@1
  - synthesis.imported-long-lived-charged-particle-stau-limits@1
  - synthesis.imported-two-doublet-top-to-charged-higgs-width-ratio@1
  proof: proof-main.tex
quantities:
- quantity.top-quark-mass@1
- quantity.w-boson-mass@1
- quantity.cosmological-constant@1
- quantity.reduced-planck-constant-times-c@1
- quantity.inverse-fine-structure-mz@1
- quantity.weak-mixing-angle-mz@1
checked_by:
- kind: check
  ref: check.py::check_yukawa_readings_see_only_beta
- kind: check
  ref: check.py::check_charged_pair_coupling_is_cot_beta
- kind: check
  ref: check.py::check_w_h_charged_vertex
- kind: check
  ref: check.py::check_alpha_phase_breaks_only_the_lift_constraint
- kind: check
  ref: check.py::check_charged_plane_alpha_only_at_zero_h
- kind: check
  ref: check.py::check_top_decay_branching_negligible
- kind: check
  ref: check.py::check_no_tree_vertex_with_w_and_a_neutral_gauge_field
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-field-charged-scalar-sum-rule
  - synthesis.rung-unit-is-frame-boost
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'su(2)_R is written with the stored macro, $\su(2)_{R}$, at every level and in the proof; no mathematics changed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'In the proof the unit on the rung field is written as I_4, which commutes with the rung vectors (C read as span{1, I_4}): the generators (I_4/2) sigma_j and (I_4/2) 1, the rational phases 3/5 + (4/5) I_4 and 5/13 - (12/13) I_4 and the moment maps G(c, -I_4 T c); nothing stays.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: uses edges to the imported Facts on the ATLAS top-decay search, the long-lived stau limits and the two-doublet width ratio (all at version 1), which the statement and the proof''s reading cite; the ratio formula, earlier cited from memory, and the three search results now cite those Facts by claimref. Content unchanged.'
  open_problem: op.rung-unit
  note: >-
    The problem's first line of attack asks for the charged pair's fermion couplings and the comparison with
    charged-scalar searches in top decays. The stored per-sector reading takes down-type entries from M_c and
    up-type entries from M_{c*}; both use only the beta half of the rung vector (the w-coefficients of c and
    the v-coefficients of c*, which are conj(beta)). That reading is not su(2)_R covariant (its kernel, the
    alpha half, is not su(2)_R invariant); the c* reading stands for the su(2)_R-covariant completion, Y on c
    and Ytilde on c* as wholes, of which the per-sector reading is the leading mass reading. Every clause here
    is a statement about the per-sector reading. Under it the stored charged plane at the vacuum, alpha-dominated
    with beta-part H^2/lambda^2 times conj(a), gives couplings of one-doublet type (Phi_1 = alpha,
    Phi_2 = conj(beta), Phi_2^dag Phi_1 = Q(c) = -H^2) with tan(beta_2) = lambda^2/H^2 = e^{2 eta}, the rung
    unit's boost squared, for every W(N) and every level. Under the covariant completion the alpha half also
    carries Y and Ytilde, and the pair couples with the strength of the mass couplings. Transport-absent in
    technique (tree-level field theory on the stored lift locus); the suppression factor is the stored frame
    boost.
---

## formal
In the setting of \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}: the rung vector $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$ ($a = 4, 5$) on the null-lift locus $L = \{Q(c) = -H^{2}\}$, $Q(c) = \alpha^{\mathsf T}\beta$, $N$, $m$, the Hermitian form $G$, the slot-mixing generators $T_{j}$, $Y$, the lift family $c_{\lambda}$ ($\alpha = (H^{2}/\lambda, 0)$, $\beta = (-\lambda, 0)$, $\lambda = He^{\eta}$), and the per-sector Yukawa reading of \claimref{standard-model.one-vev-vector-relations-breaking-pattern} on the sixteen: the down-type and charged-lepton entries are those of $M_{c}$ on $(Q, d^{c})$ and $(L, e^{c})$, the up-type and Dirac-neutrino entries those of $M_{c^{*}}$ on $(Q, u^{c})$ and $(L, \nu^{c})$. This reading is not $\su(2)_{R}$ covariant; it is the leading mass reading of the covariant completion with one family matrix on $c$ and one on $c^{*}$, to which the clauses below do not apply. Let the vacuum be $c_{\lambda}$ with $\lambda^{2} > H^{2}$.
\begin{enumerate}
\item[(i)] \emph{(The per-sector readings see only $\beta$.)} Both readings vanish on every vector with $\beta = 0$ and are unchanged by any phase $\alpha \mapsto u\alpha$, $|u| = 1$; the sum of $|\text{entry}|^{2}$ over each of the two sectors is $8|\beta|^{2}$. Read through $c$ itself (not the series' reading) the up-type entries would see $\alpha$.
\item[(ii)] \emph{(Charged couplings under the per-sector reading.)} The physical charged plane at $c_{\lambda}$ is $\{\alpha' = a\,e_{5},\ \beta' = (H^{2}/\lambda^{2})\bar{a}\,e_{5}\}$, and for each of its directions $d$, in both sectors,
\[
\frac{\sum|\text{entries of } d|^{2}/N(d)}{\sum|\text{entries of } c_{\lambda}|^{2}/N(c_{\lambda})} = \Bigl(\frac{H^{2}}{\lambda^{2}}\Bigr)^{2} = e^{-4\eta}:
\]
in the two-doublet reading $\Phi_{1} = \alpha$, $\Phi_{2} = \bar{\beta}$, with $\Phi_{2}^{\dagger}\Phi_{1} = Q(c) = -H^{2}$, the pattern is that of one doublet coupling to every fermion, with $\tan\beta_{2} = |\Phi_{2}|/|\Phi_{1}| = \lambda^{2}/H^{2} = e^{2\eta}$, and the charged pair couples with $\cot\beta_{2}$ times the coupling of the neutral vev direction.
\item[(iii)] \emph{(Gauge vertex.)} For $j = 1, 2$ the vector $T_{j}(dc_{\lambda}/d\lambda)$ lies in the charged sector, and its squared $G$-projection on the physical charged plane is $4H^{4}\lambda^{4}/(\lambda^{4} - H^{4})^{2} = 1/\sinh^{2}2\eta$ times its squared projection on the eaten plane spanned by $T_{1}c_{\lambda}$, $T_{2}c_{\lambda}$.
\item[(iv)] \emph{(A phase on $\alpha$.)} The map $\alpha \mapsto u\alpha$ keeps $N$, $m$, $|Q|$, $\sum_{j}\mu_{j}^{2}$, $\mu_{Y}$ and $G$, commutes with every $T_{j}$ and $Y$, keeps both per-sector readings, and sends $Q$ to $uQ$: it keeps the kinetic term, the D-term action at every level, every added $W(N)$ and the per-sector Yukawa entries, and moves $L$ unless $H = 0$. At $H = 0$ the charged plane at $c_{\lambda}$ lies wholly in the $\alpha$ half.
\item[(v)] \emph{(Top decays.)} With the stored $m_{t}$, $M_{W}$, $\alpha^{-1}(M_{Z})$, $\sin^{2}\theta_{W}$, $\Lambda$ and $\hbar c$, $g^{2}H^{2}/(4M_{W}^{2}) < \cot\beta_{2} = H^{2}/\lambda^{2} < g^{2}H^{2}/(2M_{W}^{2})$ (with $H^{2} = \Lambda/3$ and the tree relation $M_{W}^{2} = \tfrac12 g^{2}N^{*}$), the lower end above $2.32 \times 10^{-89}$ and the upper end below $4.66 \times 10^{-89}$, and for $m_{\pm}^{2} \in [13702, 13803]$ GeV$^{2}$ (\claimref{synthesis.rung-field-charged-scalar-sum-rule}) the factor $K = (1 - x)^{2}/((1 - y)^{2}(1 + 2y))$, $x = m_{\pm}^{2}/m_{t}^{2}$, $y = M_{W}^{2}/m_{t}^{2}$, lies below $\tfrac12$, so $\Gamma(t \to bH^{+})/\Gamma(t \to bW^{+}) = K\cot^{2}\beta_{2} < 10^{-176}$ (the ratio formula of Fact \claimref{synthesis.imported-two-doublet-top-to-charged-higgs-width-ratio}).
\end{enumerate}

## technical
The rung field is two Higgs-like doublets tied by the lift constraint: $\alpha$ and the conjugate of $\beta$, with $\Phi_{2}^{\dagger}\Phi_{1} = -H^{2}$. The series reads down-type masses through $c$ and up-type masses through $c^{*}$. Taken sector by sector (down-type entries from $c$, up-type entries from $c^{*}$), both readings use only the $\beta$ half, so one doublet gives every fermion its mass; this per-sector reading is not $\su(2)_{R}$ covariant, and it is the leading mass reading of the covariant completion, which puts one family matrix on $c$ and one on $c^{*}$ as wholes. At the vacuum the $\beta$ half carries the weak scale $\lambda$ and the $\alpha$ half only $H^{2}/\lambda$, and the physical charged pair is almost entirely $\alpha$: its admixture of $\beta$ is $H^{2}/\lambda^{2} = e^{-2\eta}$, the rung unit's boost squared. Under the per-sector reading its couplings to quarks and leptons, and its vertex with the $W$ and the neutral mode, carry that factor, so $t \to bH^{+}$ is negligible; a phase on $\alpha$ alone keeps the kinetic term, the D-term action, every $W(N)$ and the per-sector entries, and is broken only by the constraint $Q(c) = -H^{2}$. Under the covariant completion the $\alpha$ half carries the same two family matrices, and the pair couples with the strength of the mass couplings.

## lay
The series' candidate for the Higgs field comes with a pair of electrically charged partners. This result works out how those partners couple to quarks and leptons when the masses are read sector by sector, down-type quarks from the field and up-type quarks from its conjugate, which is the series' leading reading of the masses. Under that reading they hardly couple at all: their coupling is smaller than the ordinary one by a factor set by the ratio of the cosmological scale to the weak scale, so top quarks essentially never decay into them. The reason is an almost exact symmetry that only the cosmological constant breaks, and the partners then cannot decay quickly into anything. A left-right symmetric completion of the same reading gives the partners couplings of ordinary strength instead, and then searches in top-quark decays apply.

## one-liner
Under the per-sector Yukawa reading (down-type from $c$, up-type from $c^{*}$; not $\su(2)_{R}$ covariant) every fermion coupling of the rung field is to its $\beta$ half, while the charged pair is its $\alpha$ half up to $H^{2}/\lambda^{2} = e^{-2\eta}$: a one-doublet coupling pattern with $\tan\beta_{2} = e^{2\eta}$, a phase on $\alpha$ broken only by $Q(c) = -H^{2}$, and $t \to bH^{+}$ below $10^{-176}$; under the covariant completion the pair couples with the strength of the mass couplings.
