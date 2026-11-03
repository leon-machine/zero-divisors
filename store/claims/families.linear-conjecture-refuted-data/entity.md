---
id: families.linear-conjecture-refuted-data
kind: claim
version: 3
title: The linear conjecture, refuted by data
status: proved
region: families
subject: generations
tags: [refutation, flavour-and-mixing, confronted-with-data]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.alignment-computed-thirteenth-refutation-democracy-one@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:linearkill
- kind: check
  ref: check.py::check_equal_split_means_two_thirds
- kind: check
  ref: check.py::check_linear_coordinate_refuted
- kind: check
  ref: check.py::check_sqrt_coordinate_passes
- kind: check
  ref: check.py::check_tau_mass_prediction
locators:
  paper: T13
  number: Prop 5.1
  label: prop:linearkill
  line: 694
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the equal split giving 2/3, Q_m and theta_m refuted, Q_sqrt(m) passing, and the tau mass prediction, by exact interval arithmetic. Version 1 -> 2. Value fix (Leon 2026-10-23): Q_sqrt(m) = 0.6666645 (certified in [0.66666445, 0.66666455), as in the proof), for the earlier 0.666661 (formal, technical and one-liner). Check strengthened: tau prediction bounds asserted to round to 1776.97 and the pull to 0.4 (brackets kept); Koide identity sample points moved to module level. Version 2 -> 3.'
  env: proposition
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'The alignment edge is the premise of the rank-one repair argument and was kept; the Koide relation
      itself is an empirical fact (Koide1982) evaluated on data, so no standard route applies. Levels
      pass: the lay level now keeps the equal singlet-doublet split behind the prediction $Q_{m} = 2/3$;
      the one-liner keeps that split and the flagged assumption for the heavy family.'
---

## formal
The natural conjecture, that the physical masses are linear in the face-space perturbation ($v_{k} = m_{k}$), predicts, under an equal singlet-doublet split, $Q_{m} = 2/3$. The data decide: $Q_{m} = 0.8936$ ($\theta_{m} = 52.4^{\circ}$), refuted at the first decimal. The refutation points at a repair, because the conjecture contradicts Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one}'s own structure: the light masses do not exist at first order (the leading form is rank one), so they cannot be linear in the perturbation; they arise at second order, and masses quadratic in the linear object mean the linear object is measured by $\sqrt{m}$ for the light pair. That argument covers the light pair only; the heavy family's mass is first order in the same form, and putting $\sqrt{m_{\tau}}$ on the same footing as $\sqrt{m_{e}}$ and $\sqrt{m_{\mu}}$ is a further assumption, made here and flagged. In the $\sqrt{m}$ coordinate the data decide again:
\begin{equation}
Q_{\sqrt{m}} \;=\; \frac{\sum_{k} m_{k}}{\bigl(\sum_{k}\sqrt{m_{k}}\bigr)^{2}} \;=\; 0.6666645,
\end{equation}
equal to $2/3$ to two parts in $10^{6}$ (three parts in $10^{6}$ relative), within the experimental uncertainty (dominated by the tau mass; read as a prediction, the relation fixes $m_{\tau} = 1776.97$ MeV against the measured $1776.93 \pm 0.09$, agreement at half a standard deviation). Equation \eqref{eq:koide} is the Koide relation \cite{Koide1982}, a forty-year-old empirical fact and no discovery of this paper; the framework's contribution is a candidate reason the linear object is $\sqrt{m}$ (the second-order structure just cited, with its gap) and the geometric reading that follows. Both numerical evaluations are reproduced by the script as exact rational arithmetic on the stated mass values, with the refutation and the pass as strict inequalities.

## technical
If the masses themselves were the face-space coordinates, an equal singlet-doublet split would give $Q_{m} = \sum m_{k}^{2}/(\sum m_{k})^{2} = \tfrac23$; the data give $Q_{m} = 0.8936$, refuting this at the first decimal. Because the leading mass form is rank one, the light masses arise only at second order, so for the light pair the linear object is $\sqrt{m}$; extending this to the heavy family is a further assumption, flagged as such.

In the $\sqrt{m}$ coordinate $Q_{\sqrt{m}} = \sum_{k} m_{k} / (\sum_{k} \sqrt{m_{k}})^{2} = 0.6666645$, equal to $\tfrac23$ within the experimental uncertainty; read as a prediction it gives $m_{\tau} = 1776.97$ MeV against the measured $1776.93 \pm 0.09$. This is the Koide relation, an empirical fact long predating the paper; the contribution here is a candidate reason for the $\sqrt{m}$ coordinate, with its gap.

## lay
A first guess, that the three charged-lepton masses themselves satisfy a simple balance condition, which they would if the masses were the basic coordinates and the split between the families were even, fails clearly against the data. The paper's own structure suggests why: the two lighter masses appear only at second order, so the natural quantities are their square roots. Using the square roots, the same condition holds to a few parts in a million. This is the Koide relation, known since the early 1980s; what the paper adds is a possible reason for using square roots, with an acknowledged gap for the heaviest lepton.

## one-liner
The linear conjecture, which under an equal singlet-doublet split gives $Q_{m} = \tfrac23$, is refuted by the data at $0.8936$, while in the $\sqrt{m}$ coordinate, suggested for the light pair by the rank-one leading form and assumed for the heavy family, the Koide relation $Q_{\sqrt{m}} = 0.6666645$ holds within experimental uncertainty.
