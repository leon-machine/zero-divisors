---
id: synthesis.koide-channel-phase-target-depends-on-mass-definition
kind: claim
version: 2
title: 'The Koide phase target depends on the mass definition'
status: proved
region: synthesis
subject: generations
tags: [flavour-and-mixing, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-five-fronts
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
  - synthesis.koide-channel-phase-is-no-symmetry-angle@2
  - synthesis.coherent-face-vector-real-slices@1
  - families.koide-nullity-condition-one-member-invariant@2
  - synthesis.imported-one-loop-qed-pole-mass-relation@1
  proof: proof-main.tex
quantities:
- quantity.electron-mass@1
- quantity.muon-mass@1
- quantity.tau-mass@1
- quantity.inverse-fine-structure-mz@1
checked_by:
- kind: check
  ref: check.py::check_first_order_factor_is_mu_free
- kind: check
  ref: check.py::check_common_scale_phase_band
- kind: check
  ref: check.py::check_shift_dwarfs_the_two_ninths_gap
- kind: check
  ref: check.py::check_koide_defect_at_common_scale
- kind: check
  ref: check.py::check_look_elsewhere_in_the_band
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.one-open-problem-three-forms
  - synthesis.koide-channel-phase-is-no-symmetry-angle
extraction:
  open_problem: op.non-gaussian-completion
  note: 'Adversarial, on the precision of the number to be predicted. The stored channel-phase window (2.4e-9 wide), the exclusion of 2/9 (1.7e-7 away) and the denominator bounds 630131 and 4208 all use pole masses. The running-stability observation (Sumino2009) is that Koide holds at pole masses to about 1e-5 while one QED loop changes it by about 1e-3 when written in running masses; this result quantifies what that does to the channel phase and to the 207. The one-loop pole to MSbar relation is imported as the Fact synthesis.imported-one-loop-qed-pole-mass-relation (in the form used by Sumino, arXiv:0903.3640, eq. 6); the value alpha(0) = 1/137.036 used in floating-point remarks is cited from memory, and the check brackets alpha between 1/138 and the stored alpha(M_Z), which covers every scale between the lepton masses and M_Z. Comparison: the running masses at M_Z of Xing, Zhang and Zhou 2008 (cited from memory: 0.48657, 102.718, 1746.24 MeV) give m_mu/m_e = 211.11, a Koide phase 0.22259 and Q - 2/3 = 1.26e-3 in floating point: just outside the first-order band, so higher orders (two-loop QED, electroweak running) move the common-scale target by about 1e-5. The alpha bracket [1/138, alpha(M_Z)] is a bracketing choice covering the couplings at the lepton masses and at M_Z, not a statement about the scheme of alpha in the fixed-order relation. The mass dictionary in force is pole masses (provisional choice); the result says what changes if it is revised. Also bears on op.second-order-breaking, whose free phase is this phase. Transport-absent (QED, data, the stored parametrisation).'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the one-loop QED pole to MS-bar relation now cites the imported Fact (uses edge added, claimrefs in the formal statement and the proof); the pin to synthesis.koide-channel-phase-is-no-symmetry-angle moved to its version 2 (a pointer to this result added there). Under the provisional pole-mass dictionary recorded in the families region (note in families.skeleton-rank-one-plus-ordering-shift, version 5), the stored targets stand as pole-mass statements. No clause changed.'
---

## formal
Read the projected coherent face vector as the $\sqrt{m}$ vector at the Koide depth, as in Proposition \claimref{synthesis.koide-channel-phase-is-no-symmetry-angle}, so that at exact Koide the ratio $r = m_{\mu}/m_{e}$ is $r(\delta) = (p_{2}/p_{1})^{2}$ with $p_{k} = 1 + \sqrt2\cos(\delta + \tfrac{2\pi k}{3})$, strictly increasing on $[0, \tfrac{\pi}{12})$. Take the one-loop QED relation between the pole mass and the $\overline{\mathrm{MS}}$ mass of a charged lepton, $m^{\mathrm{pole}} = \bar{m}(\mu)\bigl(1 + \tfrac{\alpha}{\pi}(1 + \tfrac34\ln(\mu^{2}/\bar{m}^{2}))\bigr)$ (Fact \claimref{synthesis.imported-one-loop-qed-pole-mass-relation}, the standard relation in the form of \cite{Sumino2009}), and write $\kappa = 3\alpha/(2\pi)$; the range of $\alpha$ below is a bracket covering its values at the lepton masses and at $M_{Z}$, not a scheme statement. To first order in $\alpha$:
\begin{enumerate}
\item[(i)] at a common scale $\mu$ the $\overline{\mathrm{MS}}$ masses are $m_{i}(1 + \kappa\ln m_{i})$ up to a common factor, so every ratio becomes $\bar{r} = r(1 + \kappa\ln r)$, independent of $\mu$; at each lepton's own scale $\mu = \bar{m}_{i}$ the ratios are the pole ratios;
\item[(ii)] for every $\alpha$ between $1/138$ and the stored $\alpha(M_{Z})$, with $m_{e}$, $m_{\mu}$ in the window of Proposition \claimref{synthesis.koide-channel-phase-is-no-symmetry-angle}, the common-scale ratio lies in $(210.58, 210.89)$ and the phase $\bar{\delta}$ with $r(\bar{\delta}) = \bar{r}$ lies in $(0.22254, 0.22258)$;
\item[(iii)] $\bar{\delta} - \delta_{*} > 3.1 \times 10^{-4}$, more than $1800$ times $\tfrac29 - \delta_{*}$, and $\delta_{*} < \tfrac29 < \bar{\delta}$;
\item[(iv)] at the common-scale masses Koide's quotient satisfies $Q - \tfrac23 \in (1.0 \times 10^{-3}, 1.3 \times 10^{-3})$, against $|Q - \tfrac23| < 10^{-5}$ at the stored pole masses;
\item[(v)] the least denominator of a rational in $(0.22254, 0.22258)$ is $319$, and that of a rational in the same band divided by $\pi$ is $367$, so within the band no point of the orbit $\pm\bar{\delta} + \tfrac{\pi}{6}\mathbb{Z}$ is $\tfrac{a}{b}\pi$ with $b \le 61$, against $b \le 4208$ at the pole masses.
\end{enumerate}
So the window $\delta_{*}$, the exclusion of $\tfrac29$ and the bounds $630131$ and $4208$ of Proposition \claimref{synthesis.koide-channel-phase-is-no-symmetry-angle} are properties of the pole-mass dictionary, under which they stand (the dictionary in force, provisionally). If a selection rule for the frozen vacuum fixes the face mass form at a scale above the lepton thresholds, its target is $\bar{\delta}$, in the first-order band of (ii), which one QED loop moves by more than $10^{5}$ widths of the pole window and which higher orders move by about $10^{-5}$; and a rule that gives exact Koide at a common scale is excluded at first order in $\alpha$ by the pole data, unless something cancels the logarithmic term (the running-stability problem of \cite{Sumino2009}) or the series' masses are pole masses by premise. Under the mass-squared reading of the face mass form, in which the channel phase does not enter the spectrum of source-built completions, only (i) and (iv) carry over: the shift of the mass ratios ($m_{\mu}/m_{e}$ about $210.6$ to $210.9$ at a common scale against $206.77$ at the pole) and the Koide defect.

## technical
In the $\sqrt{m}$ (circulant) reading, the stored phase target and its no-symmetry-angle bounds use pole masses. With the standard one-loop QED relation between pole and $\overline{\mathrm{MS}}$ masses, the only non-universal part at first order is $-\kappa\ln m_{i}$, $\kappa = 3\alpha/(2\pi)$, so ratios at a common scale are $\bar{r} = r(1 + \kappa\ln r)$ for every $\mu$. For $\alpha$ between $1/138$ and the stored $\alpha(M_{Z})$ this gives $m_{\mu}/m_{e} \in (210.58, 210.89)$ and, at exact Koide, $\bar{\delta} \in (0.22254, 0.22258)$, more than $3.1 \times 10^{-4}$ above $\delta_{*}$; $\tfrac29$ sits between them, $1800$ times closer to $\delta_{*}$ than the shift. Koide's $Q$ at those masses is off $\tfrac23$ by $(1.0, 1.3) \times 10^{-3}$, a hundred times its pole precision. In the common-scale band the least denominators are $319$ and $367$ (for $\delta/\pi$), so the symmetry-angle bound falls from $4208$ to $61$. Higher orders move the common-scale target by about $10^{-5}$. Under the mass-squared reading only the ratio shift and the Koide defect carry over. Everything is certified interval arithmetic: logarithms by the $\operatorname{atanh}$ series with its geometric remainder, $\pi$ by Machin's formula, sines and cosines by alternating Taylor polynomials.

## lay
The previous result pinned an angle, which encodes the muon-to-electron mass ratio in one reading of this framework (where a vector built from the vacuum is read as the square roots of the masses), to nine decimal places and showed it is not a simple fraction or a simple symmetry angle. But particle masses can be defined in more than one way: the physical mass of a free particle, or a mass that depends on the energy scale at which it is measured. The tiny electromagnetic corrections that relate these definitions shift the mass ratio by about two percent and the angle by about three parts in ten thousand, thousands of times more than the difference between the angle and the often-quoted value $2/9$. So the nine-decimal target, and the conclusion that no symmetry of order up to $4208$ supplies it, hold only if the framework's masses are the physical masses, which is the working choice for now. If the vacuum rule sets masses at a high energy scale, the target moves, it is known far less precisely, and the famous Koide formula itself fails there by about a tenth of a percent.

## one-liner
In the $\sqrt{m}$ (circulant) reading, at first order in $\alpha$, the one-loop QED relation between pole and $\overline{\mathrm{MS}}$ masses moves the Koide phase that reproduces $m_{\mu}/m_{e}$ at a common scale from $\delta_{*} \approx 0.2222220$ to $(0.22254, 0.22258)$ (more than $1800$ times the distance of $\tfrac29$) and puts Koide's $Q$ off $\tfrac23$ by $(1.0, 1.3) \times 10^{-3}$, so the stored nine-decimal target and its symmetry-angle bound $4208$ (which falls to $61$) are pole-mass statements; under the mass-squared reading only the ratio shift and the Koide defect carry over.
