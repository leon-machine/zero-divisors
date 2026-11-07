---
id: synthesis.collar-kms-extension-three-flows
kind: claim
version: 2
title: 'Under a slice-product collar, the horizon''s KMS state does not give $6\pi$'
status: proved
region: synthesis
subject: thermality
tags: [modular-theory, schwarzschild, kasner, boundary-modes]
proposed_by:
  kind: ai
  session: colony-2026-10-22
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
review: draft
derivations:
- name: main
  uses:
  - singularity.modular-flow-boundary-modes-holonomy-universal@2
  - singularity.imported-interior-collar-kasner-form@6
  - singularity.kms-uniqueness-factor@5
  - singularity.imported-general-form@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_collar_rates_and_temperatures
- kind: check
  ref: check.py::check_product_kms_and_no_common_state
- kind: proof
  derivation: main
outside_ga:
  kind: complex-analysis
  why: 'the phase flows Ad(e^{it f(r_k) K_k}), K_k = sigma_k/2, act on the slices'' matrix-factor atoms, whose modes anticommute with I_4 (conventions, known limit 1), so I_4 is not their unit'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the phase flows Ad(e^{it f(r_k) K_k}), K_k = sigma_k/2, act on the slices'' matrix-factor atoms, whose modes anticommute with I_4 (conventions, known limit 1), so I_4 is not their unit.'
  open_problem: op.collar-kms-extension
  flow_note: phase; every flow here is the phase flow Ad(e^{itK}) of the stated rates (see synthesis.phase-flow-is-time-rotor-flow-kms-continuation).
  tension_with:
  - id: singularity.modular-flow-boundary-modes-holonomy-universal@1
    clause: (ii), the conditional sentence
    note: >-
      The stored sentence reads "if the KMS state of the boundary modes on the completed pair
      extends to a KMS state of the t-line holonomy flow on the collar, then its inverse temperature
      in Hubble-normalised time at the exceptional set is this beta_H = 6 pi". Under (C), with the
      t-line holonomy flow parametrised by Killing time (this claim's Killing flow), clause (ii)
      shows the extension exists and is unique and that its local Hubble-normalised inverse
      temperature diverges at the exceptional set, so the conditional fails. With the flow
      parametrised by the Hubble-normalised parameter, clause (iii) shows no extension exists, so
      the conditional is vacuous. The stored derivation holds the rapidity period at 2 pi on every
      slice, which is the rapidity-flow state of clause (iv), KMS for neither geometric flow. Not
      entered as a pinned contradicts link because this claim is conditional on (C), which the store
      does not hold; the maintainer should decide whether to amend the stored sentence.
  note: >-
    Decides op.collar-kms-extension only under the slice-product hypothesis (C), which the series does
    not supply (it constructs no collar algebra; note.singularity.where-spectrum-would-lie); the
    problem should become partial (decided under (C)), not resolved. The sphere holonomies (B2, B3)
    are outside (C) and remain open. status proved is to be read as proved under (C), which is a
    hypothesis of the statement. Under (C) the extension question splits by which holonomy flow is
    meant: along the Killing flow the horizon's KMS state extends uniquely and its local
    Hubble-normalised inverse temperature diverges at the exceptional set; no KMS state of the
    Hubble-normalised flow restricts to it; 6 pi is the Hubble-normalised inverse temperature at the
    exceptional set only as the local value of the slice-wise rapidity-2 pi state (KMS for neither
    geometric flow) or for a Hubble-KMS state that drops the horizon period. The KMS machinery is
    standard; the content is the series' rates.
---

## formal
Work in units $2M = 1$ on the collar of Fact \claimref{singularity.imported-interior-collar-kasner-form}, with $\kappa = \tfrac12$, $A = 1/r - 1$, and $\tau(r) = \int_{0}^{r}\sqrt{x/(1-x)}\,dx = \tfrac23 r^{3/2}S(r)$. By Proposition \claimref{singularity.modular-flow-boundary-modes-holonomy-universal} the $t$-line holonomy on the slice $r$ is the $B_{1}$ boost of that slice's completed pair, with rapidity rate $\rho(r) = 1/(2r^{2})$ per unit Killing time and, for $r < 1$, $\rho_{\mathrm{H}}(r) = \tau\,|A'|/(2\sqrt{A}) = \tfrac13 S(r)(1-r)^{-1/2}$ per unit Hubble-normalised parameter. Assume:
\begin{enumerate}
\item[(C)] for every finite set of slices $0 < r_{1} < \dots < r_{m} \le 1$ the collar algebra is the tensor product of the slices' matrix-factor atoms, each holonomy flow acting slice by slice as the phase flow $\operatorname{Ad}(e^{it f(r_{k})K_{k}})$ of its rate $f$, with $K_{k} = \sigma_{k}/2$; for the Hubble flow the slices satisfy $r_{m} < 1$, since $\rho_{\mathrm{H}}$ is not defined at the horizon.
\end{enumerate}
Call a flow with rate profile $f$ the Killing flow ($f = \rho$), the Hubble flow ($f = \rho_{\mathrm{H}}$, slices in $(0,1)$) or the rapidity flow ($f = 1$). Then:
\begin{enumerate}
\item[(i)] each flow has exactly one KMS state at each $\beta \neq 0$ on each admissible finite set of slices, the product of slice Gibbs states with rapidity periods $\beta f(r_{k})$; two flows have a common KMS state (at nonzero inverse temperatures) only if their profiles are proportional on the slices, and $\rho_{\mathrm{H}}/\rho = \tau\sqrt{r/(1-r)}$ is strictly increasing on $(0,1)$, so no state on two or more slices is KMS for two of the three flows;
\item[(ii)] the Killing-flow KMS state whose horizon slice has rapidity period $2\pi$ (inverse temperature $2\pi/\kappa$) has rapidity period $2\pi/r^{2}$ on the slice $r$ and, for $r < 1$, local Hubble-normalised inverse temperature $6\pi\sqrt{1-r}/(r^{2}S(r)) = 6\pi r^{-2}(1 - \tfrac45 r + O(r^{2}))$, which diverges at the exceptional set: the horizon's state extends uniquely along the Killing flow and tends to the ground state there;
\item[(iii)] every Hubble-flow KMS state at $\beta_{\mathrm{H}} > 0$ has rapidity period $\beta_{\mathrm{H}}\rho_{\mathrm{H}}(r) \to \infty$ as $r \to 1$, so none restricts, on slices approaching the horizon, to the horizon's state with period $2\pi$; the one at $\beta_{\mathrm{H}} = 6\pi$ has rapidity period $2\pi(1 + \tfrac45 r + O(r^{2}))$, tending to $2\pi$ only at the exceptional set;
\item[(iv)] the rapidity-flow KMS state at $\beta = 2\pi$ (period $2\pi$ on every slice) restricts to the horizon's state and has local Hubble-normalised inverse temperature $2\pi/\rho_{\mathrm{H}}(r) \to 6\pi$ and local Killing inverse temperature $4\pi r^{2}$; by (i) it is KMS for neither the Killing nor the Hubble flow.
\end{enumerate}
So under (C) the KMS state of the completed pair does not extend to a KMS state of the Hubble-normalised holonomy flow, and its extension along the Killing holonomy flow reads infinite inverse temperature at the exceptional set. The value $\beta_{\mathrm{H}} = 6\pi$ is the inverse temperature at the exceptional set only of a Hubble-KMS state with rapidity period $2\pi$ imposed there (not the horizon's state), or as the local value of the slice-wise state of (iv), which is KMS for neither geometric flow. In particular, under (C) the conditional sentence of Proposition \claimref{singularity.modular-flow-boundary-modes-holonomy-universal}(ii) fails when the $t$-line holonomy flow is parametrised by Killing time (by (ii)) and is vacuous when it is parametrised by the Hubble-normalised parameter (by (iii)); its value $6\pi$ belongs to the state of (iv). The failure is located in the profile $\rho_{\mathrm{H}}/\rho$, whose running $\tfrac45 r$ separates (iii) from (iv) at first order and whose divergence at the horizon excludes the Hubble flow there.

## technical
Assume the collar's boundary-mode algebra on any finite set of $t$-line slices is a tensor product of the slices' atoms, and let each holonomy flow act on each slice as the phase flow of its rate. Three rate profiles are natural: Killing time ($1/(2r^{2})$ in units $2M = 1$), the Hubble-normalised parameter ($\tfrac13 S(r)(1-r)^{-1/2} = \tfrac13 + \tfrac{4}{15}r + \cdots$, defined inside the horizon), and rapidity itself. Each flow has one KMS state per inverse temperature, a product of Gibbs states, and two flows share one only if their rate profiles are proportional, which no two of these are.

The horizon's state (rapidity period $2\pi$ at $r = 1$) extends uniquely along Killing time, with period $2\pi/r^{2}$: near the singularity it is frozen into the ground state, and its local Hubble-normalised inverse temperature diverges as $6\pi/r^{2}$. Every Hubble-KMS state is instead frozen near the horizon, where the Hubble rate diverges; the one at $\beta_{\mathrm{H}} = 6\pi$ has period $2\pi + \tfrac{8\pi}{5}r + \cdots$. The state with period $2\pi$ on every slice matches the horizon and has local Hubble inverse temperature tending to $6\pi$, but it is KMS for the rapidity flow, not for either geometric flow.

So the stored conditional that the extension would read $6\pi$ at the exceptional set fails under this hypothesis when the holonomy flow runs in Killing time: the extension exists but reads infinity. The $6\pi$ belongs to the state with period $2\pi$ on every slice, which is not the equilibrium state of either geometric flow.

## lay
Earlier work found that a natural clock at the black hole's central singularity would give a universal temperature, $6\pi$ in suitable units, if the thermal state at the horizon could be continued all the way in. Under the simplest assumption about how the interior's quantum modes fit together, this result shows that the horizon's state can be continued, but the continued state does not show $6\pi$ at the singularity: it becomes ever colder there. A state that does show $6\pi$ at the singularity is either not the horizon's state, or shows it only as a reading taken slice by slice for a state that is not in equilibrium for either of the interior's natural clocks.

## one-liner
Under a slice-product collar algebra the horizon's KMS state extends uniquely along the Killing holonomy flow but freezes at the exceptional set, no Hubble-normalised KMS state matches the horizon, and $6\pi$ survives only as the slice-by-slice value of a state that is KMS for neither geometric flow, so the stored $6\pi$ conditional fails on the Killing reading.
