---
id: note.neutrino.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: neutrinos
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
comments_on:
- neutrino.rank-one-seesaw-ordering-sum-double
- neutrino.breaking-relation
- neutrino.imported-indifference-faces-democratic-alignment-rank
- neutrino.mixing-none-leading-order
locators:
  paper: T15
  number: Setting
  section: Machine verification
  line: 777
---

## formal
Every computational identity asserted in this paper at its own proof level, with the exceptions listed at the end, has been verified in exact arithmetic by the script \texttt{verify\_T15.py} \cite{ButlerVerifyT15}, which imports the series' shared library \texttt{GA.py}: exact rationals, Gaussian rationals with exact linear algebra, and certified rational interval arithmetic (integer square roots with proved brackets) for the measured splittings, the mixing angles, the top and bottom masses, the equilibrium mass, and the physical constants. No floating point is used anywhere. Every observational input behind a quoted number enters as a bracket, printed in the text where the input is used, so a refresh changes the inputs and not the logic; the light charged-fermion masses ($e, \mu, \tau, u, c$) enter at their central values, used for one-significant-figure ratios except $m_{\mu}/m_{\tau}$, whose three figures calibrate $\delta_{c}$ and which the script ties to those masses; and $M_{U}$ enters at the two values the text names, $2 \times 10^{16}$ GeV (the ratios) and $7 \times 10^{14}$ GeV (the factor $1.16$-$1.19$); the Pati-Salam chain's values enter as the brackets $v_{R} \in (4.1, 4.2) \times 10^{10}$ GeV and $M_{I} \in (1.9, 2.0) \times 10^{10}$ GeV, with $M_{U} = 3.36 \times 10^{16}$ GeV and $m_{t}(M_{I}) = 92$ GeV, as the Standard-Model paper records them.

\emph{Part A: the empty twistor.} The graded dimensions $1, 3, 3, 1$ of $\Lambda^{\bullet}\C^{3}$ with its two singlets; the hypercharge per grade under the weight rule, with $Y = 0$ at grade zero and $Y = -1$ at grade three; the four anomaly sums on the derived spectrum; the closed-form solution set $(a, 2a - f, f - 4a, -3a, 6a - f, f)$ satisfying all four sums for several $(a, f)$; the reduction of the cubic sum to $18a(8a^{2} + bc - 6af + f^{2})$ under the linear conditions; the linear decomposition of the closed form into $6Y$ and $(B - L) - 2Y$, which is the two-dimensional span; the family $Y + t(B - L)$ at $t = 1, -1, 2, \tfrac57$ with $Y_{N} = t$, the vanishing of all four sums on $B - L$, and the two mixed cubic coefficients zero; the collapse to the unique solution at $Y_{N} = 0$; the four sums recomputed over an explicit five-state spectrum with the singlet deleted, equal to the six-state sums at $Y_{N} = 0$ and unequal at $Y_{N} \neq 0$; the ray $B - L$ anomaly-free with $Y_{N}/Y_{Q} = 3$ and outside the family; and the $\mathbb{Z}_{6}$ condition as a function over the whole derived content, with an off-lattice hypercharge failing it.

\emph{Part B: the seesaw.} The $\Lambda$-term neutrino's extent $l/\LH = 2^{1/4}$ exactly for $p = m$, and $l \in (1.3, 1.5) \times 10^{20}$ m for $p = 100$ GeV from $\Lambda \in (1.0, 1.2) \times 10^{-52}$ m$^{-2}$; the Casimir $C \in (1.6, 2.0) \times 10^{63}$; the neutral-bilinear census over all twenty-one pairs; the block elimination identity assembled on rational instances and the scalar small eigenvalue certified within $m_{D}^{4}/M_{R}^{3}$ of $-m_{D}^{2}/M_{R}$; the $S_{3}$ lemma (characterisation on positive and negative instances over all six permutations, the spectrum, the determinant with both singular loci, the inverse against the adjugate, the projector form); the block decomposition of Proposition \claimref{neutrino.rank-one-seesaw-ordering-sum-double}(0), the identity $\J M_{R}^{-1}\J = 3M_{3}^{-1}\J$ and the light matrix on several $(\alpha, \beta, d)$; rank preservation for a rank-one $\mD$ across non-$S_{3}$-invariant invertible $M_{R}$; the shared heavy eigenvector $u'$; the exact identity of Lemma \claimref{neutrino.breaking-relation} on rational instances; the light matrix diagonalised exactly at the $S_{3} \to S_{2}$ direction, with $m_{2}/m_{3} \in (0.168, 0.172)$ at $\delta = 0.286$, $M_{3}/\alpha = 66$ (an instance chosen to land on the measured ratio, not a test of it), the charged-sector calibration $\delta_{c} = 0.286$ from $m_{\mu}/m_{\tau}$ by exact singular values (the target tied to the script's own lepton masses), the leading-order $\delta' = 0.024$ against the diagonalised $1/66$, the non-monotonicity of the exact ratio in $M_{3}/\alpha$ (its value at $176$ exceeding those at $66$ and at $500$, and the second root's existence between them), the small-$\delta$ convergence to the $\lambda_{A} = \tfrac49$ formula, and the compression eigenvalues $\lambda_{A} = \tfrac49$, $\lambda'_{A} = 0$; the inverted ratio $m_{1}/m_{2} > 0.98$; the floor inside $(0.0580, 0.0593)$ eV, the sum at $m_{1} = 0.1, 1, 3, 10$ meV, the value at $m_{1} = 8.7$ meV ($m_{1}$ of order $m_{2}$) above $0.07$ eV, the crossing of the $0.064$ eV bound between $3.5$ and $4.6$ meV, the inverted floor inside $(0.097, 0.102)$ eV, and $m_{2}/m_{3} \in (0.16, 0.18)$; the $0.052$ eV bound below the floor; the two double-beta values from the angle and splitting brackets, their shift below $0.1$ meV at $m_{1} = 0.1$ meV, and the four sign patterns at $m_{1} = 1$ meV spanning $0.6$-$4.6$ meV; the valuation of $M_{3}$ at both ends of Hypothesis (U) from the quark-mass brackets, $(m_{t}/m_{b})^{2} \in (1.6, 1.8) \times 10^{3}$, the two unification ratios at $2 \times 10^{16}$ GeV and the factor $1.16$-$1.19$ at $7 \times 10^{14}$ GeV; the charged-sector ratios $m_{\mu}/m_{\tau}$, $m_{e}/m_{\mu}$, $m_{u}/m_{c}$ from the record; the mixing requirement $|U_{\tau 3}|^{2} \in (0.39, 0.55)$; and $\alpha$ at both ends of (U) on the branch; on the Pati-Salam branch, $\sqrt{m_{3}v_{R}}$ inside $(1.42, 1.46)$ GeV, which is the requirement's coefficient $1.44$, the coupling a top-like $m_{D}$ would need inside $(3900, 4200)$, and the ordering $\alpha_{\mathrm{bottom}} < M_{I} < \alpha_{\mathrm{top}}$ with $M_{U}$ above $M_{3}$ at both ends.

\emph{Part C: leptogenesis.} The alignment result in two exact eigenbases of $u'^{\perp}$ over the Gaussian rationals for complex $y$; the resonant ratio for the degenerate pair independent of $\delta$ while the $N_{u'}$ ratio scales as $\delta^{2}$; the washout strength $K \in (43, 48)$ from bracketed $m_{3}$ and $m_{*}$; and the interference term with a complex breaking phase, zero at $0$ and $\pi$ and nonzero off them.

What the script does not check, imported or premised at the cited levels: the measurements themselves \cite{PDG2024, NuFIT2024, DESI2025, HouWangZhaoZhang2026, T2KNOvA2025, KamLANDZen2023, LEGEND2021}, including the $0.064$, $0.052$, $0.057$, $0.092$ and $0.111$ eV bounds and the double-beta limit and projection, which are quoted; the standard Boltzmann treatment behind $m_{*}$ and the order-$10^{-7}$ asymmetry a successful leptogenesis needs; the dimensional analysis of Fact \ref{fact:join}, which is read from T11's conventions; the application of the indifference instrument to $M_{R}$ and the extension of the Gram-square reading to it, at the level Fact \claimref{neutrino.imported-indifference-faces-democratic-alignment-rank} holds them; the extension of face-valuedness to the $LN$ bracket; the two remainders in Lemma \claimref{neutrino.breaking-relation}, $O(\delta)$ and $O(\delta^{2}M_{3}/\alpha)$, which are argued in the proof and instanced, not certified in general; the tilt estimates and the degree conversion of Observation \claimref{neutrino.mixing-none-leading-order}; the flavour-independence reading of Proposition \claimref{neutrino.leptogenesis-suppressed-alignment-reheating-premise-new}(3); and Premises (M), (H) and (R) and the branch of Remark \claimref{note.neutrino.branch-m-3}, which are premises.

## technical
pending

## lay
pending

## one-liner
pending
