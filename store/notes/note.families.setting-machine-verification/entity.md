---
id: note.families.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: generations
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
- name: Claude Opus 5.5
  role: GA rewrite (cross products as the dual of the outer product)
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- families.koide-instrument
- families.skeleton-rank-one-plus-ordering-shift
- families.doublet-direction-module-georgi-jarlskog-clebsch
- families.imported-tree-relations-family-no-go
locators:
  paper: T13
  number: Setting
  section: Machine verification
  line: 970
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The channel cross products f_+ x f_- and u'' x f_+ are written as the duals of outer products, -I_f(f_+ ^ f_-) and -I_f(u'' ^ f_+), as in families.rigidity-pairing-sector-one-event (version 5). What stays: the matrix identity G G^dag = |a|^2 1 - abar a^T and the sparse exact matrices of Part F, which describe the script''s own computations (matrices as such).'
---

## formal
Every computational identity asserted in this paper at its own proof level has been verified in exact arithmetic by the script \texttt{verify\_T13.py} \cite{ButlerVerifyT13}, which imports the series' shared library \texttt{GA.py} and adds two small exact fields locally: the cyclotomic rationals $\mathbb{Q}(\zeta_{3})$ (via the minimal polynomial $\zeta^{2} + \zeta + 1 = 0$, with conjugation) and the quadratic ring $\mathbb{Z}[\sqrt{2}]$ with exact sign comparison; square roots of the measured masses are handled by exact rational interval arithmetic (integer square roots with certified brackets). No floating point is used anywhere except the RECORD lines of Part G, printed and not checked; seventy-three checks, all passing, organised in seven parts keyed to statement tags.

\emph{Part A: faces.} The $\binom{3}{2} = 3$ count, the pairwise single-slot intersections, and the transitivity of the $S_{3}$ action; the democratic texture $u'u'^{\mathsf{T}}$, $u' = (1,1,1)$, with rank one, trace three, and spectrum $(3, 0, 0)$ exactly.

\emph{Part B: condensation.} The fixed bracket \eqref{eq:gap} as a rational-function identity in formal $\Lambda$ at rational $\nu$ and $C$, with the sign of the dictionary against its opposite; the source expansion \eqref{eq:source} exactly on Gaussian-rational instances, with the $\bar b$-coefficient $\tfrac{\Lambda}{3}\Omega_{\omega}$ read off exactly; the thirteenth refutation's exponents formed from the stated inputs; the Cabibbo bracket $0.215^{2} < m_{d}/m_{s} < 0.235^{2}$ as exact inequalities.

\emph{Part C: the Koide numerics.} $Q_{m}$ bracketed in $(0.893, 0.894)$, the refutation; $Q_{\sqrt{m}}$ certified inside $(2/3 - 10^{-5},\, 2/3 + 10^{-5})$ by interval arithmetic on the pole masses; the nullity $q(v)$ certified positive, below $0.02$, and below $10^{-5}$ of $|v|^{2}$; the predicted tau mass bracketed in $(1776.9, 1777.0)$ MeV; the Euclidean identity $C(v) = |v|^{2} = \sum_{k}m_{k}$ on the lepton vector; the Fourier ratio $|\Gamma|^{2}/a^{2}$ bracketed inside $2 \pm 10^{-4}$; the angular determination of Observation \claimref{families.koide-instrument}, $\delta\theta = \tfrac12\,\delta Q/Q$ at $45^{\circ}$, bracketed inside $(1.6, 1.7) \times 10^{-6}$, and its resolution from $m_{\tau} \pm 0.09$ MeV bracketed inside $(3.7, 3.9) \times 10^{-6}$; $\cos^{2}\theta_{m} = 1/(3Q_{m})$ bracketed inside $(0.37303, 0.37304)$, whence $\theta_{m} = 52.35^{\circ}$; the singlet-doublet split, $s^{2}$ and $|d|^{2}$ both inside $(941.54, 941.56)$ with relative difference below $10^{-5}$; the phase $\delta$ through $\tan^{2}\delta = 3(\sqrt{m_{\mu}} - \sqrt{m_{e}})^{2}/(2\sqrt{m_{\tau}} - \sqrt{m_{e}} - \sqrt{m_{\mu}})^{2}$ bracketed so that $\delta \in (0.2215, 0.2225)$; and the hadronic estimate $(M_{P}^{2}H)^{1/3}$ bracketed inside $(4, 5) \times 10^{7}$ eV on the stated inputs.

\emph{Part D: the chart.} $C(f_{\pm}) = 0$ and $C(f_{+}, f_{-}) = 3$ in exact cyclotomic arithmetic; $C(af_{+} + bf_{-}) = 6ab$; the $\mathbf{3} \otimes \mathrm{sgn}$ twist on explicit arrays; the space of $S_{3}$-invariant symmetric forms on $\R^{3}$ computed as the kernel of the invariance constraints, of dimension exactly two, spanned by $\delta$ and the all-ones form; the Fourier bijection on explicit doublet vectors; and the $S_{2}$-point equivalence $Q = 2/3 \iff b^{2} = 2a^{2}$ on the explicit triple $(a+b, a-b/2, a-b/2)$, with $(a+b)/(a-b/2) = 4 + 3\sqrt{2}$ at $b = a\sqrt{2}$ in $\mathbb{Z}[\sqrt{2}]$.

\emph{Part E: the Gaussian theorems.} The closure identity $GG^{\dagger} = |a|^{2}\mathbb{1} - \bar{a}a^{\mathsf{T}}$ with its exact kernel and rank two on Gaussian-rational instances; the channels' dual outer products $-I_{f}(f_{+} \wedge f_{-}) = (\zeta^{2} - \zeta)(1,1,1)$ and $-I_{f}(u' \wedge f_{+}) = (\zeta^{2} - \zeta)f_{+}$ ($I_{f}$ the family pseudoscalar) with their Hermitian orthogonality; the Gaussian data $\hat\xi\hat\xi^{\dagger} = R \otimes \mathbb{1}$ at every point; the Wick evaluation of Theorem \claimref{families.skeleton-rank-one-plus-ordering-shift}, piece by piece and in total, against the closed form \eqref{eq:H}, in $\mathbb{Q}(\zeta_{3})$ at the rational hyperbolic points $(\tfrac34, \tfrac54)$ and $(\tfrac{12}{5}, \tfrac{13}{5})$, feeding ratios $0, \tfrac34, \tfrac43$ and channel phases $1, \zeta, \zeta^{2}$, with the coherent vector $2sc\,n$ and the rank-one normal-ordered form; the skeleton's trace and eigenvalue identities as rational-function identities in the depth; $\rho = 4 + 3\sqrt{2}$ as the exact root of $\rho^{2} - 8\rho - 2$; $(4+3\sqrt{2})^{4} = 2308 + 1632\sqrt{2}$ exactly; the crossing bracketed by exact sign evaluation in $\mathbb{Z}[\sqrt{2}]$ ($769.332 < x^{*} < 769.333$), the identity $(1+6x+6x^{2})/(1+x) = 6x + 1/(1+x)$ as a rational-function identity, and the displacement of $x^{*}$ from $K/6$ bracketed in $(2 \times 10^{-4}, 3 \times 10^{-4})$; the failure of the nominated canonical depth (the ratio function evaluated at $x = 1$ is $13/2$, and $K$ exceeds it by a factor above $700$ in exact $\mathbb{Z}[\sqrt{2}]$ sign arithmetic); and a monotonicity chain witnessing the single crossing.

\emph{Part F: the $126$ direction.} The module rebuilt as sparse exact matrices on $\Lambda^{\bullet}\C^{5}$: the CAR of five mode pairs, the sixteen even states with their species, the hypercharge and $B - L$ eigenvalues; the forty-five bivectors and the $\so(10)$-invariance of the pairing on all $45 \times 32 \times 32$ basis identities; the $10$ form of $w_{4}$ (symmetric, entries $\pm 1$ on $(L, e^{c})$, $(Q, d^{c})$); the form of $T_{\mathrm{GJ}}$ symmetric with entries exactly $-1$ on $(L, e^{c})$ and $\pm\tfrac13$ on $(Q, d^{c})$, sign-sensitively, the one-sided weighting antisymmetric, the ratio $3$; the $\Cl(5,5)$ orthonormal basis and the grade decomposition of $T_{\mathrm{GJ}}$ by the trace formula, pure grade five, with the grade-one part's form identically zero and the symmetric part of $Y_{T}$ equal to $Y_{5}$; the up-type direction $v_{4}(B - L)\chi$, its form symmetric with signed entries $+1$ and $\pm\tfrac13$ and the magnitude ratio $3$; the closed form $\tfrac43\,w_{4}(v_{5} \wedge w_{5})(\sum v_{i} \wedge w_{i})$ and the anticommutations behind it (Proposition \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}); and, as Fact \claimref{families.imported-tree-relations-family-no-go}'s content recomputed, the family no-go on an invertible rational family matrix without symmetry, the $10$ giving $M_{e}$ and $M_{d}$ with equal singular spectra for every sign of the entries while the $126$ direction gives spectra in the ratio $3$ on the same $F$, and the charge $Y(e^{c}) = 1$.

\emph{Part G: the covariance.} $\mathrm{Im}\,w = N\,(m/M_{P})$ as an exact identity of exponent triples in $(H, M_{P}, m)$; the weights $-1$ and $0$ of the two factors, computed by applying the substitution $H \to \kappa H$ with $M_{P}$ and $m$ fixed (the proposition's premise) to the monomials $N$ and $m/M_{P}$ built from the generators; the covariance condition on a power law $cN^{a}$ as an identity of monomials in $(N, \kappa)$, holding exactly at $a = 1$ and failing at $\tfrac13, \tfrac23, 2, -\tfrac13$; and the same at integer exponents on rational instances (Proposition \claimref{families.why-kinematic-attacks-had-fail}). The six logarithmic ratios are printed as RECORD lines.

What the script does not check, at the levels stated in the text: the scan-based clauses of Proposition \claimref{families.classification-displaced-gaussian-class-solved-level}(2)-(3), flagged as preliminary computation; the representation-theoretic steps stated as elementary in-proof, and the decomposition of $16 \otimes 16$ with its grade dictionary, imported as Fact \claimref{families.imported-decomposition-grade-dictionary}; the ordinary decimal roundings of quantities the script brackets; and the measured masses themselves \cite{PDG2024}, refreshed at submission.

## technical
pending

## lay
pending

## one-liner
pending
