---
id: synthesis.koide-channel-phase-is-no-symmetry-angle
kind: claim
version: 2
title: 'In the $\sqrt{m}$ (circulant) reading of the projected coherent vector at the Koide depth, the measured muon-electron ratio (three standard deviations of $m_{\mu}$) fixes the channel phase to $\delta_{*} \in (0.22222204589, 0.22222204830)$, which is not $\tfrac29$, not a rational of denominator below $630131$ and, on its whole relabelling orbit, not a rational multiple of $\pi$ of denominator at most $4208$, so no phase fixed by a symmetry of order up to $4208$ (argued: such phases are rational multiples of $\pi$) and no rational of denominator below $630131$ supplies the $207$ at exact Koide'
status: proved
region: synthesis
subject: generations
tags: [flavour-and-mixing, no-go, confronted-with-data, needs-continuum]
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
  - synthesis.coherent-face-vector-real-slices@1
  - families.koide-nullity-condition-one-member-invariant@2
  - synthesis.real-structure-breaks-source-stabiliser-to-z2@2
  - families.classification-displaced-gaussian-class-solved-level@3
  - synthesis.light-cone-koide-is-quarter-turn@1
  proof: proof-main.tex
quantities:
- quantity.electron-mass@1
- quantity.muon-mass@1
checked_by:
- kind: check
  ref: check.py::check_phase_window_from_the_split
- kind: check
  ref: check.py::check_two_ninths_is_excluded
- kind: check
  ref: check.py::check_no_simple_rational_phase
- kind: check
  ref: check.py::check_no_symmetry_angle
- kind: check
  ref: check.py::check_elasticity_of_the_split
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.one-open-problem-three-forms
  - synthesis.channel-phase-invisible-to-axially-covariant-completions
extraction:
  open_problem: op.non-gaussian-completion
  note: 'Adversarial, on the number to be predicted. In the store the projected coherent face vector at the Koide depth is p_k = 1 + sqrt2 cos(delta + 2 pi k/3), with delta the channel phase (or the channel phase minus a quarter turn on the Lorentzian slice), so at exact Koide the 207 is one phase. This result fixes that phase from the measured m_mu/m_e alone (tau-independent) and tests the two kinds of value a selection rule could supply without a second free number: a small rational (the literature value 2/9, Brannen 2006, cited from memory) and a symmetry angle, a rational multiple of pi such as any finite stabiliser (the Z2 of the real structure, the S3, the quarter turn, the Z3 of the cubic word) supplies. Both are excluded. The phase 2/9 alone, with the depth left free, fits the data (computed in floating point in the proof text: the depth then misses Koide by about 1e-7 in Q, invisible to the tau mass); it is the joint exactness of Q = 2/3 and delta = 2/9 that the muon-electron ratio excludes, by more than 400 standard deviations. Also relevant to op.second-order-breaking, whose free phase delta = 0.222 is this phase. The result is conditional on the sqrt(m) (circulant) reading of the projected coherent vector; under the mass-squared reading of the mass form the channel phase does not enter the spectrum of source-built completions (synthesis.real-structure-breaks-source-stabiliser-to-z2), and which reading is primary is open. Consistent with the eigenvalue form of \claimref{synthesis.series-family-structures-give-no-lopsided-second-stage} (same p_k after k -> -k). Denominator bounds are properties of the three-sigma window, not of an exact number. Transport-absent (data and the stored parametrisation).'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: a marked note after the formal statement points to synthesis.koide-channel-phase-target-depends-on-mass-definition and to the provisional pole-mass dictionary (note in families.skeleton-rank-one-plus-ordering-shift): the stored window and bounds are pole-mass statements (claimrefs only, not edges, since the mass-definition result uses this one). No clause changed.'
---

## formal
Read the projected coherent face vector of Proposition \claimref{synthesis.coherent-face-vector-real-slices}(iii)-(iv) as the $\sqrt{m}$ vector (its circulant reading; the mass-squared reading of the mass form is a different dictionary, in which the channel phase does not enter the spectrum of source-built completions by Proposition \claimref{synthesis.real-structure-breaks-source-stabiliser-to-z2}). At the Koide depth $\lambda^{2} = 2$ it is, up to a common factor, $p_{k} = 1 + \sqrt2\cos(\delta + \tfrac{2\pi k}{3})$, $k = 0, 1, 2$, with $\delta$ the channel phase $\chi$ on the Euclidean slice and $\chi \mp \tfrac{\pi}{2}$ on the Lorentzian one; read as the $\sqrt{m}$ vector it satisfies the Koide relation (Proposition \claimref{families.koide-nullity-condition-one-member-invariant}). The relabellings of the three families and the sign of the doublet part act on $\delta$ through $\pm\delta + \tfrac{\pi}{3}\mathbb{Z}$, and $\chi - \delta \in \{0, \pm\tfrac{\pi}{2}\}$, so the channel phase lies on the orbit $\pm\delta + \tfrac{\pi}{6}\mathbb{Z}$. Let $r(\delta) = (p_{2}/p_{1})^{2}$ and let $r_{\mathrm{obs}} = m_{\mu}/m_{e}$ at the stored masses, taken in the window $(206.7682690, 206.7682969)$ (three stored standard deviations of $m_{\mu}$; for $m_{e}$, $10^{-9}$ MeV).
\begin{enumerate}
\item[(i)] \emph{(The phase target.)} In the fundamental domain $[0, \tfrac{\pi}{6}]$ of $\pm\delta + \tfrac{\pi}{3}\mathbb{Z}$ all three $p_{k}$ are positive exactly on $[0, \tfrac{\pi}{12})$, where $p_{1} < p_{2} < p_{0}$ for $\delta > 0$; there $r$ increases strictly from $1$ to $\infty$, and $r(\delta_{*}) = r_{\mathrm{obs}}$ gives $\delta_{*} \in (0.22222204589, 0.22222204830)$.
\item[(ii)] \emph{($\tfrac29$ is excluded at exact Koide.)} $r(\tfrac29) \in (206.7703, 206.7704)$, above the window by more than $400$ standard deviations of the measured ratio; so $\delta_{*} < \tfrac29 - 1.7 \times 10^{-7}$.
\item[(iii)] \emph{(No small rational.)} No rational with denominator below $630131$ lies in the window of (i) (a property of the three-standard-deviation window); $\tfrac{140029}{630131}$ is the first.
\item[(iv)] \emph{(No symmetry angle.)} No rational of denominator below $25249$ lies in the corresponding window for $\delta_{*}/\pi$; hence no point of the orbit $\pm\delta_{*} + \tfrac{\pi}{6}\mathbb{Z}$, and so neither the channel phase $\chi$ on either slice nor any relabelling of it, is $\tfrac{a}{b}\pi$ with $b \le 4208$ (again for the three-standard-deviation window).
\item[(v)] \emph{(Elasticity.)} $(\delta/r)\,dr/d\delta \in (12.4, 12.5)$ across the window: the split responds to the phase with elasticity about $12.5$, not the unit elasticity of the relabelling signature of Proposition \claimref{families.classification-displaced-gaussian-class-solved-level}.
\end{enumerate}
So at exact Koide the open problem's $207$ is the single number $\delta_{*}$, known to $2.4 \times 10^{-9}$. A phase fixed by a finite-order symmetry (a root-of-unity condition, the kind every stabiliser met in face space supplies: the $\mathbb{Z}_{2}$ of the real structure, the $S_{3}$, the doublet quarter-turn, the $\mathbb{Z}_{3}$ of the cubic family word) is a rational multiple of $\pi$ (argued, not proved), and such a phase is excluded by (iv) for symmetries of order up to $4208$; the celebrated value $\tfrac29$ is excluded jointly with exact Koide by (ii). A selection rule for the non-Gaussian frozen vacuum must therefore produce a transcendental-looking phase to about $10^{-9}$, or produce a Koide defect along with it.

\emph{Note (mass definition).} The window, the exclusion of $\tfrac29$ and the denominator bounds use the stored pole masses, which the store's provisional dictionary assigns to the face mass form (note in \claimref{families.skeleton-rank-one-plus-ordering-shift}); exact Koide at pole masses is then a premise of the reading. At common-scale running masses, first order in $\alpha$, the target phase lies between $0.22254$ and $0.22258$, moved from $\delta_{*}$ by more than $1800$ times the distance from $\delta_{*}$ to $\tfrac29$, and $m_{\mu}/m_{e}$ between $210.58$ and $210.89$ (Proposition \claimref{synthesis.koide-channel-phase-target-depends-on-mass-definition}).

## technical
Reading the projected coherent face vector as the vector of square roots of the charged-lepton masses (its circulant reading), these are, at the Koide depth, $1 + \sqrt2\cos(\delta + 2\pi k/3)$ with $\delta$ the channel phase of the coherent face source (up to a quarter turn, depending on which real slice is used). So, granted the Koide relation, the muon-to-electron ratio is a function of one phase. This result solves for that phase from the measured muon and electron masses alone, using certified interval arithmetic: $\delta_{*}$ lies between $0.22222204589$ and $0.22222204830$. It then tests the two kinds of value a rule could supply without a second free number. The often-quoted value $2/9$ gives a ratio of $206.7703$ against the measured $206.76828$: excluded by more than $400$ standard deviations when the Koide relation is exact; it is the combination of exact Koide with $2/9$ that fails. Within three standard deviations of the muon mass, no fraction with denominator below $630131$ fits the window, and no rational multiple of $\pi$ with denominator up to $4208$ fits it on any relabelling. Since a phase fixed by a symmetry of finite order is a rational multiple of $\pi$ (argued), this rules out phases produced by symmetries of order up to $4208$, including all the stabilisers met in face space so far. Under the other dictionary, where the eigenvalues of the mass form are the squared masses, the channel phase does not reach the spectrum at all, so the result is specific to the square-root reading. The split's relative response to the phase is certified between $12.4$ and $12.5$ times the phase's relative change, so a rule must fix the phase to within the window's width, $2.4 \times 10^{-9}$, to reproduce the ratio to its measured precision.

## lay
A famous formula ties the electron, muon and tau masses together. In one reading of this framework, where a vector built from the vacuum is read as the square roots of the three masses, the remaining information in the masses is a single angle once that formula is granted. This result pins that angle down from the measured electron and muon masses to nine decimal places and checks the two kinds of value a theory might naturally produce. It is not the simple fraction $2/9$ that has been proposed before (close, but measurably different if the formula is exact), not any other fraction with a small denominator, and not the kind of angle a symmetry of modest order would produce, which is a simple fraction of a half-turn. Whatever fixes the muon-to-electron mass ratio has to produce a number that looks like none of these.

## one-liner
With the projected coherent vector read as the $\sqrt{m}$ vector (the circulant reading) at the Koide depth, the measured $m_{\mu}/m_{e}$ at three standard deviations of $m_{\mu}$ fixes the channel phase to $\delta_{*} \in (0.22222204589, 0.22222204830)$; $\delta = \tfrac29$ gives $m_{\mu}/m_{e} \in (206.7703, 206.7704)$ and is excluded jointly with exact Koide, and within that window no rational of denominator below $630131$ and no rational multiple of $\pi$ of denominator at most $4208$ (on the whole relabelling orbit) fits, so neither such a rational nor a phase fixed by a symmetry of order up to $4208$ (argued: such phases are rational multiples of $\pi$) supplies the $207$ at exact Koide.
