---
id: synthesis.mass-squared-reading-needs-millions-of-face-pairs
kind: claim
version: 2
title: 'The mass-squared reading needs millions of face pairs'
status: proved
region: synthesis
subject: generations
tags: [flavour-and-mixing, no-go, confronted-with-data]
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
  - synthesis.pair-singlet-mass-form-is-floor-plus-face-density@1
  - synthesis.koide-channel-phase-target-depends-on-mass-definition@2
  - synthesis.imported-one-loop-qed-pole-mass-relation@1
  proof: proof-main.tex
quantities:
- quantity.electron-mass@1
- quantity.muon-mass@1
- quantity.tau-mass@1
checked_by:
- kind: check
  ref: check.py::check_ratio_bound_on_the_span_of_face_words
- kind: check
  ref: check.py::check_extreme_point_function_is_increasing
- kind: check
  ref: check.py::check_threshold_from_the_stored_masses
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.pair-singlet-mass-form-is-floor-plus-face-density
  - synthesis.cumulants-at-fixed-second-moments-keep-the-floor
extraction:
  open_problem: op.non-gaussian-completion
  note: 'The problem asks for a selection rule for the non-Gaussian frozen vacuum with no fitted number and for its pair-number moments. The stored floor-plus-density result gives, for source-built states, the dictionary (<D^2> + 3<D>/2)/(1 + <D>/2) = (m_mu^2 + m_tau^2)/m_e^2 - 2 and the one-pair-number value D about 6.07e6 as unchecked arithmetic. This result makes it an inequality for every state on the span of face words, pure or mixed and not only source-built, and turns it into a support condition: since the floor bounds the least eigenvalue from below and the trace is fixed by the first two pair-number moments, the ratio is a ratio of two linear functionals of the pair-number distribution, maximised at a point mass, where it equals 2D + 1 + 2/(D + 2), increasing in D. With the stored masses at three standard deviations, every state supported on D <= 6065573 falls short. A rule with no fitted number must therefore produce a pair number of order (m_tau/m_e)^2/2 from structure: for instance (arithmetic, not checked) a geometric pair-number distribution of mean n has the ratio (2 + 7n/2 + 2n^2)/(1 + n/2), about 4n, so it needs n about 3.03e6. In the linear reading (eigenvalues of H as masses, not the stored primary reading) the same bound gives (m_mu + m_tau)/m_e <= 2K + 1 + 2/(K + 2) and needs K of about 1840 (arithmetic, not checked). The integer threshold is a pole-mass statement; at common-scale MS-bar masses (one-loop QED, alpha between 1/138 and alpha(M_Z)) the ratio is about 1.283e7 to 1.288e7 and the threshold about 6.41 to 6.44 million (floating-point estimate, not checked here, with the one-loop relation of synthesis.imported-one-loop-qed-pole-mass-relation; the mass-definition dependence is the subject of synthesis.koide-channel-phase-target-depends-on-mass-definition, now a premise). Transport-absent.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the mention of synthesis.koide-channel-phase-target-depends-on-mass-definition, a claimref in text in version 1, is now a uses edge (pinned at its version 2; acyclic, since that result does not reach this one), and the one-loop QED relation used in the floating-point remark cites its imported Fact. No clause changed.'
---

## formal
Let $\mathcal{S}$ be the span of face-word monomials and $H = (1 + \tfrac12\langle\hat{D}\rangle)\mathbb{1} + G$, $G \ge 0$, $\mathrm{tr}\,H = 3 + 3\langle\hat{D}\rangle + \langle\hat{D}^{2}\rangle$, the mass form of a state on $\mathcal{S}$ as in Proposition \claimref{synthesis.pair-singlet-mass-form-is-floor-plus-face-density}, with eigenvalues $\lambda_{1} \le \lambda_{2} \le \lambda_{3}$.
\begin{enumerate}
\item[(i)] For every state on $\mathcal{S}$, pure or mixed,
\[
\frac{\lambda_{2} + \lambda_{3}}{\lambda_{1}} \;\le\; \frac{2 + \tfrac52\langle\hat{D}\rangle + \langle\hat{D}^{2}\rangle}{1 + \tfrac12\langle\hat{D}\rangle},
\]
with equality exactly when $\lambda_{1}$ is the floor $1 + \tfrac12\langle\hat{D}\rangle$ (as in every source-built state, loc. cit. (iii)).
\item[(ii)] If the state is supported on pair numbers $D \le K$, then $(\lambda_{2} + \lambda_{3})/\lambda_{1} \le 2K + 1 + \tfrac{2}{K + 2}$, with equality for the word $\hat\Omega_{1}^{\dagger K}\ket{0}$.
\item[(iii)] Under the mass-squared reading, $(\lambda_{2} + \lambda_{3})/\lambda_{1} = (m_{\mu}^{2} + m_{\tau}^{2})/m_{e}^{2}$, which the stored pole masses place in $(12131147, 12138498)$ at three standard deviations (the face mass form gives pole masses under the dictionary the store adopts provisionally; at common-scale running masses the ratio is larger, \claimref{synthesis.koide-channel-phase-target-depends-on-mass-definition}, for the mass definition). So every state on $\mathcal{S}$ supported on $D \le 6065573$ is excluded, and the frozen vacuum must give positive weight to pair numbers $D \ge 6065574$; equivalently its moments must satisfy $\langle\hat{D}^{2}\rangle + \tfrac52\langle\hat{D}\rangle + 2 > 12131147\,(1 + \tfrac12\langle\hat{D}\rangle)$.
\end{enumerate}
So a selection rule for the non-Gaussian frozen vacuum that introduces no fitted number must, under the mass-squared reading, produce a pair-number scale of order $(m_{\tau}/m_{e})^{2}/2$ from structure; a rule confined to pair numbers below about six million cannot supply the charged-lepton masses on the span of face words, whatever state it selects there.

## technical
On the span of face words the stored result writes the mass form as a floor $1 + \langle D\rangle/2$ times the identity plus a positive matrix, with trace $3 + 3\langle D\rangle + \langle D^{2}\rangle$, where $D$ is the number of face pairs. Since the least eigenvalue is at least the floor and the trace is fixed, the sum of the two heavier eigenvalues over the lightest is at most $(2 + \tfrac52\langle D\rangle + \langle D^{2}\rangle)/(1 + \tfrac12\langle D\rangle)$, for every state there, not only those built from the source. This is a ratio of two averages over the pair-number distribution, so over states supported on $D \le K$ it is largest at a single pair number $K$, where it equals $2K + 1 + 2/(K + 2)$. Reading the eigenvalues as squared pole masses, the measured $(m_{\mu}^{2} + m_{\tau}^{2})/m_{e}^{2}$ is about $1.213 \times 10^{7}$, so the selected vacuum must put weight on pair numbers of at least $6065574$; at common-scale running masses the threshold is larger, an estimated $6.4$ million at first order in $\alpha$. A rule without a fitted number has to generate a number of that size.

## lay
In one reading of the theory, the three charged-lepton masses squared are the three levels of a matrix built from the vacuum, and the vacuum is described by how many pairs of certain quanta it holds. This result shows that the ratio of the heavy levels to the light one can never exceed about twice the largest number of pairs present. Since the tau is about 3477 times heavier than the electron (at the pole masses), the squared ratio is about twelve million, so the vacuum must contain states with at least about six million pairs; with the masses defined at a common energy scale instead, the number rises to about 6.4 million. Whatever rule picks the vacuum has to produce a number that large from the theory's structure, without it being put in by hand.

## one-liner
Under the mass-squared reading, every state on the span of face words has $(\lambda_{2} + \lambda_{3})/\lambda_{1} \le (2 + \tfrac52\langle D\rangle + \langle D^{2}\rangle)/(1 + \tfrac12\langle D\rangle) \le 2K + 1 + 2/(K + 2)$ for support on $D \le K$, so the measured $(m_{\mu}^{2} + m_{\tau}^{2})/m_{e}^{2} \approx 1.213 \times 10^{7}$ at the pole masses needs a frozen vacuum with weight at pair numbers $D \ge 6065574$ (an estimated $6.4$ million at common-scale running masses).
