---
id: synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state
kind: claim
version: 1
title: 'Geometric modular conjugations on a generator give the null ground state'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, modular-theory, car-algebra, forcing-and-uniqueness, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-06-edge-normality
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-06-edge-normality
review: draft
about:
- obj.hawking.continuum-mode-space
outside_ga:
  kind: complex-analysis
  why: 'the proof is Fourier and Pick-function analysis on L^2 of a null line (Laplace transforms of half-line test functions, Loewner''s theorem, boundary values of Cauchy-type integrals) for operators on a complex Hilbert space; the fields are CAR operators and the modular objects antiunitaries there; the checks use Gaussian rationals (GA.QI) and exact signatures (GA.congruence_signature)'
imported_from:
- citation: 'K. Loewner, Ueber monotone Matrixfunktionen, Math. Z. 38 (1934), 177--216.'
  key: Loewner1934
  locator: 'a real function on an open interval is operator monotone (all Loewner matrices positive) if and only if it extends to a Pick function analytic across the interval; cited from memory, statement standard, page data not checked'
- citation: 'D. R. Yafaev, Criteria for Hankel operators to be sign-definite, Anal. PDE 8 (2015); arXiv:1303.4040.'
  key: Yafaev2015
  locator: 'Theorem 4.7, the Laplace representation of the kernel of a nonnegative Hankel operator; abstract and theorem number read on arXiv, journal pages not checked; an alternative to Loewner in Step 5'
- citation: 'D. Buchholz, M. Florig and S. J. Summers, An algebraic characterization of vacuum states in Minkowski space. II. Continuity aspects, Lett. Math. Phys. 49 (1999), 337--350; arXiv:math-ph/9909003.'
  key: BFS1999
  locator: 'Condition of Geometric Modular Action (a)-(d), Modular Stability Condition, Prop. 3.5 (translations from the modular conjugations) and Prop. 3.6 (spectrum condition up to sign, from CGMA together with modular stability); the remark that CGMA alone does not give a ground state; read on arXiv'
- citation: 'D. Buchholz and S. J. Summers, An algebraic characterization of vacuum states in Minkowski space, Commun. Math. Phys. 155 (1993), 449--458.'
  key: BS1993
  locator: 'origin of the condition of geometric modular action (last section), as cited in BFS1999; the paper itself not read'
- citation: 'R. Brunetti, D. Guido and R. Longo, Modular structure and duality in conformal quantum field theory, Commun. Math. Phys. 156 (1993), 201--219.'
  key: BGL1993
  locator: 'geometric modular action (Bisognano-Wichmann) for half-line and interval algebras of Moebius-covariant nets; cited from memory'
- citation: 'H. Baumgaertel, M. Jurke and F. Lledo, Twisted duality of the CAR-algebra, J. Math. Phys. 43 (2002), 4158--4179.'
  key: BJL2002
  locator: 'modular objects of the twisted (fermionic) second quantisation of a standard subspace, the Klein twist Z; cited from memory'
derivations:
- name: main
  uses:
  - synthesis.positive-null-energy-gives-r-premises@4
  - synthesis.imported-powers-stormer-takesaki-disjointness@2
  - synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state@2
  - angle.imported-theorems-deliver-their-hypotheses@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_the_form_is_a_loewner_kernel
- kind: check
  ref: check.py::check_the_vacuum_form_is_positive_and_fixes_the_sign
- kind: check
  ref: check.py::check_charge_symmetry_and_the_states_it_admits
- kind: check
  ref: check.py::check_the_swapped_band_state_breaks_the_positivity
- kind: check
  ref: check.py::check_two_cuts_do_not_give_stationarity
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state
  - synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics
extraction:
  open_problem: op.r-premises-external
  note: >-
    Answers the problem's request for a stationarity-free form of (N+) at the level of a principle with no
    temperature and no modular group in it: on one generator, for gauge-invariant quasi-free states, the
    condition of geometric modular action posed elementwise on the modular conjugations of the half-line
    algebras (J_a acts as the twisted charge-conjugating reflection about a, with a sign eta) at three cuts
    with incommensurable distances is equivalent to (N+) for eta = -1 and to its time reverse for eta = +1.
    The proof splits CGMA into three parts and shows what each does: twisted Haag duality at one cut forces
    purity (this is where every thermal state is excluded); invariance of the state under the reflections
    gives stationarity and charge symmetry; the natural-cone positivity of J is a null-line reflection
    positivity whose Gram kernel is a Loewner kernel, and Loewner's theorem with a boundary-value argument
    turns it into the sign of the occupation, hence the Hardy polarisation. The period 2 pi and the
    geometric modular group (the stored KMS form, synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state)
    are outputs. Candid status: this is a restatement of (N+) as a modular principle, not a derivation from a
    principle the series already adopts; the series adopts no premise on modular conjugations (see
    synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics,
    where the same kind of premise, modular P1CT symmetry, gives interacting spin-statistics under the
    spectrum condition; here, on a generator, the elementwise form supplies the spectrum condition). The
    elementwise form is needed: the net-level form of Buchholz and Summers is satisfied by every local-gauge
    transform of the vacuum, including the translation-invariant Fermi-level states, matching the Minkowski
    statement that geometric modular action alone does not give positive energy. The orientation sign is
    the sign eta of the reflection relative to the Klein twist built with the field algebra's imaginary unit.
    Transport-absent. Literature: Loewner's theorem cited from memory (Yafaev's Hankel criterion, read on
    arXiv, gives the same step); Buchholz-Florig-Summers read on arXiv; the converse (Bisognano-Wichmann for
    the chiral Fermi field, twisted second quantisation) cited from memory.
  flags:
  - 'converse imported: that the null vacuum satisfies the hypothesis at every cut is the Bisognano-Wichmann property of the chiral Fermi field, cited from memory; the one-particle identity it needs is argued by analytic continuation of the boost to rapidity i pi'
  - 'K with internal multiplicity: the reflection is assumed to act trivially on K up to the sign eta; for a general self-adjoint unitary V on K the analysis is not done'
---

## formal
Units $\hbar = c = 1$. On one generator, affine parameter $u \in \R$, let $\CAR(h)$, $h = L^{2}(\R, du)\otimes K$, be the continuum mode space (Definition \claimref{obj.hawking.continuum-mode-space}), $h_{a} = L^{2}((a, \infty))\otimes K$, $\rho_{a}f(u) = f(2a - u)$ the reflection about the cut $a$, $P = i\,d/du$, $B(f) = \psi(f) + \psi^{*}(f)$, and $\omega$ a gauge-invariant quasi-free state with symbol $T$, $\omega(\psi^{*}(v)\psi(u)) = T(u, v)$; the null vacuum $\omega_{0}$ has $T_{0} = \chi_{(-\infty, 0)}(P)\otimes\id_{K}$, kernel $\tfrac{i}{2\pi}(u - v + i0)^{-1}$, the state of Premise \claimref{synthesis.n-plus-null-ground-state} (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(i)). In the GNS representation $(\pi, \mathcal{H}, \Omega)$ let $\Theta$ implement the grading, $Z = (1 + i\Theta)/(1 + i)$ the Klein twist, $\mathcal{R}_{a} = \pi(\CAR(h_{a}))''$ and $\mathcal{R}_{a}^{c} = \pi(\CAR(h_{a}^{c}))''$. For $\eta \in \{1, -1\}$, $\omega$ satisfies \emph{CGMA$_{\eta}$ at the cut $a$} if $\Omega$ is cyclic and separating for $\mathcal{R}_{a}$ and its modular conjugation $J_{a}$ acts as the twisted charge-conjugating reflection about $a$:
\[ J_{a}\,\pi(\psi(f))\,J_{a} = \eta\,Z\,\pi(\psi^{*}(\rho_{a}f))\,Z^{*}\qquad (f \in h_{a}). \]
The hypothesis names $J_{a}$ only: no modular group, no KMS condition, no temperature, no stationarity. Let $A \subset \R$ be a set of cuts whose differences generate a dense subgroup of $\R$ (three cuts $0, 1, c$ with $c$ irrational suffice).
\begin{enumerate}
\item[(i)] \emph{(One cut: purity; proved, given Powers-Stormer.)} CGMA$_{\eta}$ at one cut gives twisted Haag duality $\mathcal{R}_{a}' = Z\mathcal{R}_{a}^{c}Z^{*}$ there, and then $\omega$ is pure: $T$ is a projection. No state KMS for the affine translations, and no stationary half-thermal product other than $\omega_{0}$, satisfies CGMA$_{\eta}$ at any cut.
\item[(ii)] \emph{(Dense cuts: stationarity and charge symmetry; proved.)} The invariance $\omega\circ\mathrm{Ad}(Z^{*}J_{a}) = \overline{\omega}$ alone gives $\rho_{a}(1 - T)\rho_{a} = T$; at the cuts of $A$ this makes $T = \theta(P)$ translation invariant with $\theta(-p) = 1 - \theta(p)$.
\item[(iii)] \emph{(Positivity is a Loewner condition; proved, given Loewner's theorem.)} At a cut, the natural-cone positivity $\ip{B(x)\Omega}{J_{a}B(x)\Omega} \ge 0$, $x \in h_{a}$, is the twisted reflection positivity $-i\eta\,\omega(B(x)B(\rho_{a}x)) \ge 0$, and for $T = \theta(P)$ as in (ii) it says that the kernels $\int_{0}^{\infty}\ip{\xi}{w(p)\zeta}\,p(a + b)/((a^{2} + p^{2})(b^{2} + p^{2}))\,dp$, $w(p) = -\eta(1 - 2\theta(p))$, are positive; for each unit $\xi$ this is the Loewner kernel of $H_{\xi}(a) = -\int_{0}^{\infty}\ip{\xi}{w(p)\xi}\big(\tfrac{p}{a^{2} + p^{2}} - \tfrac{p}{1 + p^{2}}\big)dp$, whose Pick continuation has $\mathrm{Im}\,H_{\xi}(iy + 0) = \tfrac{\pi}{2}\ip{\xi}{w(y)\xi}$. Hence $w(p) \ge 0$ for almost every $p > 0$. For the null vacuum $H(a) = \ln a$.
\item[(iv)] \emph{(The ground-state clause; proved.)} If $\omega$ satisfies CGMA$_{\eta}$ at every cut of $A$, then $\omega = \omega_{0}$ when $\eta = -1$, and $\omega$ is its time reverse, symbol $\chi_{(0, \infty)}(P)\otimes\id_{K}$ (the ground state for the reversed translations), when $\eta = +1$. Stationarity, positivity of the null translations and the period $2\pi$ of the geometric modular group are outputs.
\item[(v)] \emph{(Converse; imported.)} $\omega_{0}$ satisfies CGMA$_{-1}$ at every cut, and its time reverse CGMA$_{+1}$ (Bisognano-Wichmann for the chiral Fermi field, Fact \claimref{angle.imported-theorems-deliver-their-hypotheses}, with the KMS property of $\omega_{0}$ about every point, Theorem \claimref{synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state}(ii)). So for gauge-invariant quasi-free states on one generator, (N$_{+}$) is equivalent to CGMA$_{-1}$ at the cuts of $A$, and to CGMA$_{-1}$ at every cut.
\item[(vi)] \emph{(Sharpness.)} (a) Two cuts do not suffice (proved): a local gauge transform $\omega_{0}\circ\gamma_{g}$ with $g$ unimodular, symmetric about $0$ and $1$ and of period $2$ satisfies CGMA$_{-1}$ at every integer cut and is not stationary. (b) Without purity (argued): the translation-KMS states satisfy (ii) and the positivity (iii) at every cut (Loewner function $\psi(\beta a/2\pi + \tfrac12)$, a Pick function) and fail only (i). (c) Positivity is not implied by (ii) (proved): the pure, translation-invariant, charge-symmetric state with occupied set $(-\infty, -2)\cup(0, 2)$ has an indefinite form ($-\tfrac35$ on $e^{-u}$, $\tfrac{3}{20}$ on $e^{-4u}$), although its kernel differs from $\omega_{0}$'s by the entire function $-\tfrac{i}{\pi}(1 - \cos 2s)/s$, so it is locally normal to $\omega_{0}$ and generator-Hadamard at every point.
\end{enumerate}
The hypothesis is posed on the fields, not only on the local algebras: the net-level form $J_{a}\mathcal{R}_{I}J_{a} = Z\mathcal{R}_{\rho_{a}I}Z^{*}$ is kept by every local gauge transform of $\omega_{0}$, the translation-invariant Fermi-level states $\chi_{(-\infty, k)}(P)$ included, which violate the charge symmetry of (ii) for $k \ne 0$ (proof, Step 8(d)); in Minkowski space too, geometric modular action of the net alone does not give positive energy \cite{BFS1999}.
Status: (i) to (iv) and (vi)(a), (c) proved, with exact checks of the Loewner identity, the vacuum's form and its sign, the charge-symmetry condition on the listed symbols, the swapped-band values and the two-cut counter-model; (iii) rests on Loewner's theorem (cited from memory; Yafaev's Hankel criterion gives the same step); (v) imported; (vi)(b) argued. Transport-absent.

## technical
The series assumes (N$_{+}$): the modes on a horizon's light rays are in their ground state for sliding along the rays. Earlier results reached this only with a stationarity assumption, or from thermality about every point (a condition on a modular flow and its temperature). This result uses a weaker-looking ingredient of modular theory: only the modular conjugation $J$ of the algebra of the modes beyond each cut of a light ray, required to act on the fields as the reflection about the cut combined with charge conjugation, with a sign $\eta$. This is the generator form of the condition of geometric modular action of Buchholz and Summers, posed on the fields rather than only on the local algebras. Within gauge-invariant quasi-free states it gives (N$_{+}$) for $\eta = -1$ and the time-reversed vacuum for $\eta = +1$, from three cuts at incommensurable distances, with no stationarity, no temperature and no modular group assumed. Each part of the hypothesis does one job. That $J$ maps the algebra beyond the cut onto the twisted algebra before it (twisted Haag duality) forces the state to be pure; every thermal state fails here. That $J$ fixes the state vector and acts as a reflection makes the state invariant under products of reflections, which are translations, and symmetric under charge conjugation. That $J$ is a modular conjugation makes a reflection-positivity form nonnegative; on exponentials its Gram kernel is a Loewner kernel, so the form is positive exactly when a certain function is operator monotone, and the boundary values of its Pick continuation on the imaginary axis are the occupation numbers: they must not exceed one half at positive momentum, which for a pure state is the Hardy polarisation, the null vacuum. The temperature $1/2\pi$ and the boost as modular flow then follow from the stored results. The sharpness examples show the hypothesis cannot be thinned: two commensurable cuts admit gauge-twisted non-stationary vacua; the positivity part alone admits all translation-thermal states; a pure stationary charge-symmetric state with one momentum band swapped is locally the vacuum everywhere and fails only the positivity; and the algebra-level form admits the Fermi-level states. The result restates (N$_{+}$) as a modular principle on the generator; it does not derive it from a principle the series already holds, and it is transport-absent.

## lay
The series assumes that the quantum modes running along a horizon's light rays are in their lowest-energy state. Earlier results could justify this only for states that do not change in time, or by asking the modes to look warm from every point along the ray. This result replaces both with a condition that mentions neither time evolution nor temperature: cutting a light ray at a point, the mathematical mirror that quantum theory attaches to the part of the ray beyond the cut must be the ordinary mirror image through the cut, with particles exchanged for antiparticles. Asking this at three cuts spaced at incommensurable distances forces the modes into their lowest-energy state, or into its time-reversed image, which a sign in the mirror distinguishes. The different parts of the condition rule out, in turn, warm states, states that change along the ray, and states that are cold but wrongly filled. The condition is a reformulation of the assumption in the language of modern quantum field theory, not a derivation of it from something the series already assumes.

## one-liner
For gauge-invariant quasi-free states on a horizon generator, requiring the modular conjugation of the algebra beyond each of three cuts at incommensurable distances to act on the fields as the twisted charge-conjugating reflection about the cut, with sign $\eta$, gives (N$_{+}$) for $\eta = -1$ and its time reverse for $\eta = +1$, with no stationarity, temperature or modular group assumed: twisted Haag duality forces purity, the reflections give stationarity and charge symmetry, and the natural-cone positivity is a Loewner condition whose boundary values are the occupation numbers; two cuts, or the positivity without purity, do not suffice.
