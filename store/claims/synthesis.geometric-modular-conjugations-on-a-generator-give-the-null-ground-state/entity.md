---
id: synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state
kind: claim
version: 4
title: 'Field-level geometric modular conjugations on a generator give the null ground state'
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
- name: Claude Opus 5.5
  role: premises repointed to the premise-free results split out of the null-energy and collapse results
  version: 3
  source: maintainer pass 2026-11-07
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.hawking.continuum-mode-space
imported_from:
- citation: 'K. Loewner, Ueber monotone Matrixfunktionen, Math. Z. 38 (1934), 177--216.'
  key: Loewner1934
  locator: 'a real function on an open interval is operator monotone (all Loewner matrices positive) if and only if it extends to a Pick function analytic across the interval; now Fact synthesis.imported-loewner-theorem-and-yafaev-hankel-sign-criterion (a), bibliographic data checked, statement cited from memory'
- citation: 'D. R. Yafaev, Criteria for Hankel operators to be sign-definite, Anal. PDE 8 (2015); arXiv:1303.4040.'
  key: Yafaev2015
  locator: 'Theorem 4.7 of the arXiv version (Theorem 4.9 of the journal version, Anal. PDE 8 (2015), 183--221), the Laplace representation of the kernel of a nonnegative Hankel operator; now Fact synthesis.imported-loewner-theorem-and-yafaev-hankel-sign-criterion (b); an alternative to Loewner in Step 5'
- citation: 'D. Buchholz, M. Florig and S. J. Summers, An algebraic characterization of vacuum states in Minkowski space. II. Continuity aspects, Lett. Math. Phys. 49 (1999), 337--350; arXiv:math-ph/9909003.'
  key: BFS1999
  locator: 'Condition of Geometric Modular Action (a)-(d), Modular Stability Condition, Prop. 3.5 (translations from the modular conjugations) and Prop. 3.6 (spectrum condition up to sign, from CGMA together with modular stability); the remark that CGMA alone does not give a ground state; read on arXiv; now Fact synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability'
- citation: 'D. Buchholz and S. J. Summers, An algebraic characterization of vacuum states in Minkowski space, Commun. Math. Phys. 155 (1993), 449--458.'
  key: BS1993
  locator: 'origin of the condition of geometric modular action (last section), as cited in BFS1999; the paper itself not read'
- citation: 'R. Brunetti, D. Guido and R. Longo, Modular structure and duality in conformal quantum field theory, Commun. Math. Phys. 156 (1993), 201--219.'
  key: BGL1993
  locator: 'geometric modular action (Bisognano-Wichmann) for half-line and interval algebras of Moebius-covariant nets; now Fact synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection (a), (c), abstract checked, the field-level form cited from memory'
- citation: 'H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. Res. Inst. Math. Sci. 6 (1970/71), 385--442.'
  key: Araki1970
  locator: 'purity criterion: a gauge-invariant quasi-free state is pure if and only if its symbol is a projection; only the direction pure implies projection is used (Step 2); now clause (d) of Fact synthesis.imported-powers-stormer-takesaki-disjointness, checked secondhand'
- citation: 'H. Baumgaertel, M. Jurke and F. Lledo, Twisted duality of the CAR-algebra, J. Math. Phys. 43 (2002), 4158--4179.'
  key: BJL2002
  locator: 'modular objects of the twisted (fermionic) second quantisation of a standard subspace, the Klein twist Z; now Fact synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection (b), (c), abstract checked, the field-level form cited from memory'
derivations:
- name: main
  uses:
  - synthesis.null-vacuum-on-a-horizon-generator@1
  - synthesis.imported-powers-stormer-takesaki-disjointness@3
  - synthesis.imported-loewner-theorem-and-yafaev-hankel-sign-criterion@1
  - synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection@1
  - synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability@1
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
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R2 (7 November 2026) the generator''s mode space carries the field theory''s unit I_4 throughout: P = I_4 d/du, the null-vacuum kernel (I_4/2 pi)(u - v + I_4 0)^{-1}, the Klein twist Z = (1 + I_4 Theta)/(1 + I_4), the twisted reflection positivity -I_4 eta omega(B(x)B(rho_a x)), the modular group Delta_a^{I_4 t} and the continuation to rapidity I_4 pi, the Fourier and Laplace kernels and the Pick-function continuation (numbers read in span{1, I_4}, Im the I_4-coefficient), and the checked phase (3 + 4 I_4)/5. Nothing stays; the earlier declaration is removed.'
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3, at Leon''s decision of 7 November 2026: it cited synthesis.positive-null-energy-gives-r-premises only for its (i) (the null vacuum, its kernel and ground-state property), which is now synthesis.null-vacuum-on-a-horizon-generator (ii); the uses edge, the claimrefs and the checks'' premise calls are repointed to it, so this result no longer inherits Premise (N+) through them. Statement, proof argument and checks otherwise unchanged; no assumes edge added or removed; notation as the sweep left it.'
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
    the sign eta of the reflection relative to the Klein twist built with the field algebra's imaginary unit;
    it is not fixed by the series (the orientation of i relative to time is an open datum that (N+) assumes),
    so eta = -1 is a named assumption here. The net-level failure (local gauge transforms of the vacuum, the
    Fermi seas) is the companion result synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i, cited, not reproved.
    Compared with the stored KMS form, this result trades the modular group for the class assumption
    (gauge-invariant quasi-free states).
    Transport-absent. Literature, each now a Fact: Loewner's theorem and Yafaev's Hankel criterion
    (synthesis.imported-loewner-theorem-and-yafaev-hankel-sign-criterion; Loewner's statement from memory), Araki's purity criterion
    (synthesis.imported-powers-stormer-takesaki-disjointness (d), checked secondhand), Buchholz-Florig-Summers (synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability,
    checked on arXiv), and the field-level twisted reflection of the chiral Fermi field, Brunetti-Guido-Longo and
    Baumgaertel-Jurke-Lledo, for the converse (synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection (c), cited there from memory); the
    Fact angle.imported-theorems-deliver-their-hypotheses gives only the modular group.
  maintainer_pass:
    by: maintainer-2026-11-06
    date: '2026-11-06'
    note: 'Version 1 -> 2: the derivation now pins the imported Facts it uses (Loewner and Yafaev, the field-level modular conjugation of the chiral Fermi field, Buchholz-Florig-Summers, and the purity criterion added as clause (d) of the Powers-Stormer Fact, now at version 3), the text cites them with claimref, and the companion net-level result is cross-referenced with claimref; statement, proof and check unchanged.'
  flags:
  - 'converse imported: that the null vacuum satisfies the hypothesis at every cut is the field-level Bisognano-Wichmann property of the chiral Fermi field, Fact synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection (c), cited there from memory; the one-particle identity it needs is argued by analytic continuation of the boost to rapidity i pi'
  - 'purity criterion (Araki 1970): the direction used, pure implies projection symbol, is clause (d) of Fact synthesis.imported-powers-stormer-takesaki-disjointness (version 3), checked there secondhand'
  - 'the sign eta is not a convention: it is the orientation of the imaginary unit relative to the time orientation, an open datum that (N+) assumes; eta = -1 is a named assumption of the equivalence with (N+)'
  - 'K with internal multiplicity: the reflection is assumed to act trivially on K up to the sign eta; for a general self-adjoint unitary V on K the analysis is not done'
---

## formal
Units $\hbar = c = 1$. On one generator, affine parameter $u \in \R$, let $\CAR(h)$, $h = L^{2}(\R, du)\otimes K$, be the continuum mode space (Definition \claimref{obj.hawking.continuum-mode-space}), $h_{a} = L^{2}((a, \infty))\otimes K$, $\rho_{a}f(u) = f(2a - u)$ the reflection about the cut $a$, $P = I_{4}\,d/du$ (the complex unit of $h$ is the field theory's unit $I_{4}$; numbers, analytic continuations included, are read in $\mathrm{span}\{1, I_{4}\}$, with $\mathrm{Im}$ the $I_{4}$-coefficient), $B(f) = \psi(f) + \psi^{*}(f)$, and $\omega$ a gauge-invariant quasi-free state with symbol $T$, $\omega(\psi^{*}(v)\psi(u)) = T(u, v)$; the null vacuum $\omega_{0}$ has $T_{0} = \chi_{(-\infty, 0)}(P)\otimes\id_{K}$, kernel $\tfrac{I_{4}}{2\pi}(u - v + I_{4}0)^{-1}$, the state of Premise \claimref{synthesis.n-plus-null-ground-state} (Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii)). In the GNS representation $(\pi, \mathcal{H}, \Omega)$ let $\Theta$ implement the grading, $Z = (1 + I_{4}\Theta)/(1 + I_{4})$ the Klein twist, $\mathcal{R}_{a} = \pi(\CAR(h_{a}))''$ and $\mathcal{R}_{a}^{c} = \pi(\CAR(h_{a}^{c}))''$. For $\eta \in \{1, -1\}$, $\omega$ satisfies \emph{CGMA$_{\eta}$ at the cut $a$} if $\Omega$ is cyclic and separating for $\mathcal{R}_{a}$ and its modular conjugation $J_{a}$ acts as the twisted charge-conjugating reflection about $a$:
\[ J_{a}\,\pi(\psi(f))\,J_{a} = \eta\,Z\,\pi(\psi^{*}(\rho_{a}f))\,Z^{*}\qquad (f \in h_{a}). \]
The hypothesis names $J_{a}$ only: no modular group, no KMS condition, no temperature, no stationarity. Let $A \subset \R$ be a set of cuts whose differences generate a dense subgroup of $\R$ (three cuts $0, 1, c$ with $c$ irrational suffice).
\begin{enumerate}
\item[(i)] \emph{(One cut: purity; proved, given Powers-Stormer and the purity criterion.)} CGMA$_{\eta}$ at one cut gives twisted Haag duality $\mathcal{R}_{a}' = Z\mathcal{R}_{a}^{c}Z^{*}$ there, and then $\omega$ is pure, so $T$ is a projection (Araki's criterion, direction pure implies projection, Fact \claimref{synthesis.imported-powers-stormer-takesaki-disjointness}(d) \cite{Araki1970}). No state KMS for the affine translations, and no stationary half-thermal product other than $\omega_{0}$, satisfies CGMA$_{\eta}$ at any cut.
\item[(ii)] \emph{(Dense cuts: stationarity and charge symmetry; proved.)} The invariance $\omega\circ\mathrm{Ad}(Z^{*}J_{a}) = \overline{\omega}$ alone gives $\rho_{a}(1 - T)\rho_{a} = T$; at the cuts of $A$ this makes $T = \theta(P)$ translation invariant with $\theta(-p) = 1 - \theta(p)$.
\item[(iii)] \emph{(Positivity is a Loewner condition; proved, given Loewner's theorem, Fact \claimref{synthesis.imported-loewner-theorem-and-yafaev-hankel-sign-criterion}(a).)} At a cut, the natural-cone positivity $\ip{B(x)\Omega}{J_{a}B(x)\Omega} \ge 0$, $x \in h_{a}$, is the twisted reflection positivity $-I_{4}\eta\,\omega(B(x)B(\rho_{a}x)) \ge 0$, and for $T = \theta(P)$ as in (ii) it says that the kernels $\int_{0}^{\infty}\ip{\xi}{w(p)\zeta}\,p(a + b)/((a^{2} + p^{2})(b^{2} + p^{2}))\,dp$, $w(p) = -\eta(1 - 2\theta(p))$, are positive; for each unit $\xi$ this is the Loewner kernel of $H_{\xi}(a) = -\int_{0}^{\infty}\ip{\xi}{w(p)\xi}\big(\tfrac{p}{a^{2} + p^{2}} - \tfrac{p}{1 + p^{2}}\big)dp$, whose Pick continuation has $\mathrm{Im}\,H_{\xi}(I_{4}y + 0) = \tfrac{\pi}{2}\ip{\xi}{w(y)\xi}$. Hence $w(p) \ge 0$ for almost every $p > 0$. For the null vacuum $H(a) = \ln a$.
\item[(iv)] \emph{(The ground-state clause; proved.)} If $\omega$ satisfies CGMA$_{\eta}$ at every cut of $A$, then $\omega = \omega_{0}$ when $\eta = -1$, and $\omega$ is its time reverse, symbol $\chi_{(0, \infty)}(P)\otimes\id_{K}$ (the ground state for the reversed translations), when $\eta = +1$. Stationarity, positivity of the null translations and the period $2\pi$ of the geometric modular group are outputs. The sign $\eta$ is not a convention: it records the orientation of the imaginary unit of the field algebra relative to the time orientation, a datum the series does not fix and (N$_{+}$) assumes; the equivalence with (N$_{+}$) below holds under the named assumption $\eta = -1$.
\item[(v)] \emph{(Converse; imported from memory.)} $\omega_{0}$ satisfies CGMA$_{-1}$ at every cut, and its time reverse CGMA$_{+1}$. The modular group (the boost about $a$ at rapidity $-2\pi t$) is supplied by the pinned Fact \claimref{angle.imported-theorems-deliver-their-hypotheses} and the KMS property of $\omega_{0}$ about every point (Theorem \claimref{synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state}(ii)); the field-level action of $J_{a}$ as the twisted charge-conjugating reflection is not in that Fact; it is Fact \claimref{synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection}(c) \cite{BGL1993, BJL2002}, cited there from memory, with the one-particle identity argued by analytic continuation. So for gauge-invariant quasi-free states on one generator, given this converse and the assumption $\eta = -1$, (N$_{+}$) is equivalent to CGMA$_{-1}$ at the cuts of $A$, and to CGMA$_{-1}$ at every cut.
\item[(vi)] \emph{(Sharpness.)} (a) Two cuts do not suffice (proved): a local gauge transform $\omega_{0}\circ\gamma_{g}$ with $g$ unimodular, symmetric about $0$ and $1$ and of period $2$ satisfies CGMA$_{-1}$ at every integer cut and is not stationary. (b) Without purity (argued): the translation-KMS states satisfy (ii) and the positivity (iii) at every cut (Loewner function $\psi(\beta a/2\pi + \tfrac12)$, a Pick function) and fail only (i). (c) Positivity is not implied by (ii) (proved): the pure, translation-invariant, charge-symmetric state with occupied set $(-\infty, -2)\cup(0, 2)$ has an indefinite form ($-\tfrac35$ on $e^{-u}$, $\tfrac{3}{20}$ on $e^{-4u}$), although its kernel differs from $\omega_{0}$'s by the entire function $-\tfrac{I_{4}}{\pi}(1 - \cos 2s)/s$, so it is generator-Hadamard at every point, and it is locally normal to $\omega_{0}$ on every bounded interval: the compressed symbol difference is a difference of positive trace-class operators, so the Powers-Stormer inequality and criterion (Fact \claimref{synthesis.imported-powers-stormer-takesaki-disjointness}(a), (c)) give local quasi-equivalence.
\end{enumerate}
The hypothesis is posed on the fields, not only on the local algebras: the net-level form $J_{a}\mathcal{R}_{I}J_{a} = Z\mathcal{R}_{\rho_{a}I}Z^{*}$ is kept by every local gauge transform of $\omega_{0}$, the translation-invariant Fermi-level states $\chi_{(-\infty, k)}(P)$ included, which violate the charge symmetry of (ii) for $k \ne 0$ (the companion result on net-level modular data, \claimref{synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i}, proves the net-level identity; Step 8(d) only applies it); in Minkowski space too, geometric modular action of the net alone does not give positive energy (Fact \claimref{synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability}(e) \cite{BFS1999}).
Status: (i) to (iv) and (vi)(a), (c) proved, with exact checks of the Loewner identity, the vacuum's form and its sign, the charge-symmetry condition on the listed symbols, the swapped-band values and the two-cut counter-model; (iii) rests on Loewner's theorem (Fact \claimref{synthesis.imported-loewner-theorem-and-yafaev-hankel-sign-criterion}, the statement cited from memory; Yafaev's Hankel criterion, in the same Fact, gives the same step); (i) also rests on Araki's purity criterion (Fact \claimref{synthesis.imported-powers-stormer-takesaki-disjointness}(d)); (v) imported (Fact \claimref{synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection}(c), cited there from memory), the Fact \claimref{angle.imported-theorems-deliver-their-hypotheses} giving only the modular group; (vi)(b) argued. Transport-absent.

## technical
The series assumes (N$_{+}$): the modes on a horizon's light rays are in their ground state for sliding along the rays. Earlier results reached this only with a stationarity assumption, or from thermality about every point (a condition on a modular flow and its temperature). This result uses a weaker-looking ingredient of modular theory, at a price: unlike the stored thermality theorem, which assumes nothing about the class of the state, it assumes the state gauge-invariant and quasi-free, so it trades the modular group for the class assumption. It uses only the modular conjugation $J$ of the algebra of the modes beyond each cut of a light ray, required to act on the fields as the reflection about the cut combined with charge conjugation, with a sign $\eta$. This is the generator form of the condition of geometric modular action of Buchholz and Summers, posed on the fields rather than only on the local algebras. Within gauge-invariant quasi-free states it gives (N$_{+}$) for $\eta = -1$ and the time-reversed vacuum for $\eta = +1$; the sign is the orientation of the imaginary unit relative to time, which the series does not fix, so $\eta = -1$ is an assumption, not a convention, from three cuts at incommensurable distances, with no stationarity, no temperature and no modular group assumed. Each part of the hypothesis does one job. That $J$ maps the algebra beyond the cut onto the twisted algebra before it (twisted Haag duality) forces the state to be pure; every thermal state fails here. That $J$ fixes the state vector and acts as a reflection makes the state invariant under products of reflections, which are translations, and symmetric under charge conjugation. That $J$ is a modular conjugation makes a reflection-positivity form nonnegative; on exponentials its Gram kernel is a Loewner kernel, so the form is positive exactly when a certain function is operator monotone, and the boundary values of its Pick continuation on the imaginary axis are the occupation numbers: they must not exceed one half at positive momentum, which for a pure state is the Hardy polarisation, the null vacuum. The temperature $1/2\pi$ and the boost as modular flow then follow from the stored results. The sharpness examples show the hypothesis cannot be thinned: two commensurable cuts admit gauge-twisted non-stationary vacua; the positivity part alone admits all translation-thermal states; a pure stationary charge-symmetric state with one momentum band swapped is locally the vacuum everywhere and fails only the positivity; and the algebra-level form admits the Fermi-level states (the companion result on net-level modular data, \claimref{synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i}). The result restates (N$_{+}$) as a modular principle on the generator; it does not derive it from a principle the series already holds, and it is transport-absent.

## lay
The series assumes that the quantum modes running along a horizon's light rays are in their lowest-energy state. Earlier results could justify this only for states that do not change in time, or by asking the modes to look warm from every point along the ray. This result replaces both with a condition that mentions neither time evolution nor temperature: cutting a light ray at a point, the mathematical mirror that quantum theory attaches to the part of the ray beyond the cut must be the ordinary mirror image through the cut, with particles exchanged for antiparticles. Asking this at three cuts spaced at incommensurable distances forces the modes into their lowest-energy state, or into its time-reversed image, which a sign in the mirror distinguishes; which sign is right is not settled by anything else in the series and is assumed. The different parts of the condition rule out, in turn, warm states, states that change along the ray, and states that are cold but wrongly filled. The result holds for the simplest class of states (those fixed by their two-point correlations), and the condition is a reformulation of the assumption in the language of modern quantum field theory, not a derivation of it from something the series already assumes.

## one-liner
For gauge-invariant quasi-free states on a horizon generator, requiring (at the field level) the modular conjugation of the algebra beyond each of three cuts at incommensurable distances to act on the fields as the twisted charge-conjugating reflection about the cut, with sign $\eta$, gives (N$_{+}$) for $\eta = -1$ (an assumed sign: the orientation of the unit $I_{4}$ relative to time is an open datum) and its time reverse for $\eta = +1$, with no stationarity, temperature or modular group assumed: twisted Haag duality forces purity, the reflections give stationarity and charge symmetry, and the natural-cone positivity is a Loewner condition whose boundary values are the occupation numbers; two cuts, or the positivity without purity, do not suffice.
