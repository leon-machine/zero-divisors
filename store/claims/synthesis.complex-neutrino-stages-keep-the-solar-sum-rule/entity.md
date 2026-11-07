---
id: synthesis.complex-neutrino-stages-keep-the-solar-sum-rule
kind: claim
version: 3
title: 'Complex neutrino stages keep the solar sum rule'
status: proved
region: synthesis
subject: neutrinos
tags: [flavour-and-mixing, symmetry-breaking, no-go]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - neutrino.breaking-relation@3
  - synthesis.solar-angle-light-plane-sum-rule@1
  - synthesis.one-type-second-stages-are-twins@2
  - synthesis.series-family-structures-give-no-lopsided-second-stage@3
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix@3
  - standard-model.imported-clebsch-structure-seesaw@1
  - synthesis.imported-takagi-factorisation@1
  - synthesis.imported-nufit-6-oscillation-parameter-ranges@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_equal_modulus_stages_reduce_to_the_symmetric_block
- kind: check
  ref: check.py::check_tilt_and_ratio_in_s_and_u
- kind: check
  ref: check.py::check_tilt_maximum_on_the_level_set
- kind: check
  ref: check.py::check_bound_against_data_for_complex_neutrino_stages
- kind: check
  ref: check.py::check_symmetric_couplings_give_one_type_stages
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.series-family-structures-give-no-lopsided-second-stage
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix
  - synthesis.conjugate-reading-up-down-split-is-t3r-odd-or-cp-odd
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The complex second-stage parameter x = t e^{I_4 varphi} and the phases of the lightest states in the proof are written with I_4 (numbers read in span{1, I_4}); the grid index i in s = i/300 is an index and stays.'
  open_problem: op.second-order-breaking
  note: >-
    Decides the problem's fourth line of attack (the solar-angle bound for a complex neutrino
    coefficient) for every neutrino stage of one type in modulus, |x| = |y| in the light-plane block,
    and asks whether the second family matrix of the su(2)_R-covariant completion (Y on c, Yt on c*,
    1 November) is the lopsided S2-odd second stage the solar sum rule requires. The stored rule
    covered real textures and, with a real neutrino coefficient, complex charged stages; for a complex
    neutrino coefficient the light neutrino states are the Takagi vectors of B B^T, which are not a
    function of the moduli. Here: every |x| = |y| block reduces by a diagonal unitary to the symmetric
    one; the tilt and the mass ratio depend on s = |x|^2/k^2 and u = cos^2(arg x) only; on a level
    set of m1/m2 the tilt decreases from its value at u = 0; the maximum is tan^2 theta_nu =
    sqrt(rho)(1 + sqrt(rho))/(1 - sqrt(rho)), so a phase raises the neutrino tilt by the factor
    (1 + sqrt(rho))/(1 - sqrt(rho)) over the real value sqrt(rho), from 17.5 to 19.3 degrees at
    rho = 1/100. That is not enough: the solar angle stays below 23.3 degrees. A numerical sweep over
    phases (numpy, exploration only) gave the same maximum. Clause (iii) decides the complex-neutrino
    case that synthesis.series-family-structures-give-no-lopsided-second-stage (iv), (v) left to a numerical
    observation; clause (i) is the Lemma-order complex analogue of the real, all-orders twin identity
    synthesis.one-type-second-stages-are-twins. The 10s on c and c* are symmetric in the family index,
    so the P12-odd stage they give in each sector is symmetric and one type in modulus; a 126 enters
    only with a P12-even f, since an odd f also puts an odd part into M_R = v_R f, outside the setting
    (an exploration with an odd light-plane block in the inverse of M_R reached about 28 degrees). The
    covariant completion with 10s therefore fails the solar angle under (H) at this order and meets the
    one-type hypothesis of the Cabibbo result
    (synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase); the covariant completion supplies a second family matrix and a CP phase, not the
    lopsidedness, which still needs an antisymmetric (120) and a symmetric odd part in one sector. The
    Takagi factorisation of complex symmetric matrices (Horn and Johnson, Matrix Analysis, Corollary 4.4.4)
    and the NuFIT 6.0 ranges are imported as the Facts synthesis.imported-takagi-factorisation and
    synthesis.imported-nufit-6-oscillation-parameter-ranges. Transport-absent: two-by-two linear algebra on the family index.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the Takagi factorisation and the NuFIT 6.0 ranges now cite imported Facts (uses edges added, claimrefs in the formal statement and the proof); the pin to synthesis.series-family-structures-give-no-lopsided-second-stage moved to its version 2, which adds a pointer to this result. No clause changed.'
---
## formal
Work at the $S_{3} \to S_{2}$ direction with the textures and the order of Proposition \claimref{synthesis.solar-angle-light-plane-sum-rule}, each second stage $X_{s}$ odd under $P_{12}$ and allowed complex as in Proposition \claimref{synthesis.series-family-structures-give-no-lopsided-second-stage}: in the basis $(\hat{b}_{e}, \hat{b}_{o})$ of the light plane the compression is $B_{s} = \bigl[\begin{smallmatrix} k & x_{s}\\ y_{s} & 0\end{smallmatrix}\bigr]$, $k = 2/3$, and at the Lemma's order (Lemma \claimref{neutrino.breaking-relation}) the light neutrino mass matrix on the light plane is a complex multiple of $N = B_{\nu}B_{\nu}^{\mathsf T}$, so the light neutrino states are the Takagi vectors of $N$ (the eigenvectors of $NN^{\dagger}$, Fact \claimref{synthesis.imported-takagi-factorisation}) and $\rho = m_{1}/m_{2} = \sigma_{2}(N)/\sigma_{1}(N)$. Let $\theta_{\nu}$ be the angle of the lightest neutrino state from $\hat{b}_{o}$.
\begin{enumerate}
\item[(i)] \emph{(Reduction.)} If $|x| = |y|$, put $D = \mathrm{diag}(1, x/y)$. Then $DND = N_{s} = \bigl[\begin{smallmatrix} k^{2} + x^{2} & kx\\ kx & x^{2}\end{smallmatrix}\bigr]$, the block of the symmetric stage $y = x$, so $N$ and $N_{s}$ have the same singular values and Takagi vectors whose components agree in modulus. Every complex stage with $|x| = |y|$ (symmetric, antisymmetric, Hermitian, any multiple of the sign line) has the same $\theta_{\nu}$ and $\rho$ as the symmetric stage with the same $x$. This is the Lemma-order complex analogue of the real twin identity of Proposition \claimref{synthesis.one-type-second-stages-are-twins}.
\item[(ii)] \emph{(Tilt and ratio.)} For $N_{s}$, with $s = |x|^{2}/k^{2}$ and $u = \cos^{2}(\arg x)$,
\[
\tan^{2}2\theta_{\nu} = \frac{4s(1 + 4su + 4s^{2}u)}{(1 + 2s(2u - 1))^{2}}, \qquad \rho + \frac{1}{\rho} = \frac{1 + 4su + 2s^{2}}{s^{2}},
\]
whenever $1 + 2s(2u - 1) > 0$.
\item[(iii)] \emph{(The maximum over phases.)} For $\rho_{0} < 3 - 2\sqrt2$ and every complex $x$ with $\rho \le \rho_{0}$,
\[
\tan^{2}\theta_{\nu} \;\le\; \frac{\sqrt{\rho_{0}}\,(1 + \sqrt{\rho_{0}})}{1 - \sqrt{\rho_{0}}},
\]
with equality exactly at $\rho = \rho_{0}$ and $u = 0$ (a purely imaginary relative coefficient $x/k$). For a real coefficient ($u = 1$) the stored value is $\tan^{2}\theta_{\nu} = \sqrt{\rho}$, so a phase raises the tilt by the factor $(1 + \sqrt{\rho_{0}})/(1 - \sqrt{\rho_{0}})$ and no more. At $\rho_{0} = 1/100$: $\tan^{2}2\theta_{\nu} \le 3960/6241$, $\tan^{2}\theta_{\nu} \le 11/90$, $\theta_{\nu} < 19.3^{\circ}$ (against $17.5^{\circ}$ real), attained at $s = 10/99$, $u = 0$. This decides the complex neutrino coefficient left open in Proposition \claimref{synthesis.series-family-structures-give-no-lopsided-second-stage}, for stages with $|x_{\nu}| = |y_{\nu}|$.
\item[(iv)] \emph{(The sum rule for complex stages.)} With any complex charged stage with $|x_{e}| = |y_{e}|$ and any complex neutrino stage with $|x_{\nu}| = |y_{\nu}|$, $|U_{e1}| \ge \cos(\theta_{e} + \theta_{\nu})$ with $\tan^{2}\theta_{e} = m_{e}/m_{\mu}$, so
\[
\Delta \;\le\; \arctan\sqrt{m_{e}/m_{\mu}} \;+\; \arctan\sqrt{\frac{\sqrt{\rho}\,(1 + \sqrt{\rho})}{1 - \sqrt{\rho}}} .
\]
If $m_{1}/m_{2} \le 0.01$ (the inequality of Premise (H), taken as a hypothesis of this clause), $\Delta < 23.3^{\circ}$ and $|U_{e1}|^{2} > 0.844$, against $|U_{e1}|^{2} \le (1 - 0.275)(1 - 0.02023) < 0.711$ at the three-sigma edges of the NuFIT 6.0 global fit (union of its four columns; Fact \claimref{synthesis.imported-nufit-6-oscillation-parameter-ranges}). The restriction to a real neutrino coefficient in Proposition \claimref{synthesis.series-family-structures-give-no-lopsided-second-stage}(iv) and (v) is removed.
\item[(v)] \emph{(The $10$ couplings.)} If the $P_{12}$-odd second stage of each sector comes from $10$ couplings, which are symmetric in the family index (among them the coupling $Y$ to $c$ and $\tilde{Y}$ to $c^{*}$ of Theorem \claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}, entering $M_{e}$ and $\mD$ as in Fact \claimref{standard-model.imported-clebsch-structure-seesaw}, with any complex vevs and coefficients; a $126$ only with $P_{12}$-even $f$, which adds nothing to the odd stage), then $y_{s} = x_{s}$ in each sector, and by (iv), if $m_{1}/m_{2} \le 0.01$, the measured solar angle is not reached at the Lemma's order. So the second family matrix of the $\su(2)_{R}$-covariant completion, and the phases it carries, are not the lopsided $S_{2}$-odd stage; $|y_{s}| \ne |x_{s}|$ needs a family-antisymmetric coupling (the $120$) together with a symmetric odd part in one sector. A $P_{12}$-odd $126$ coupling $f$ also puts an odd part into $M_{R} = v_{R}f$, outside the setting, and is not covered.
\end{enumerate}
Scope: the Lemma's order of Proposition \claimref{synthesis.solar-angle-light-plane-sum-rule}, a second stage that is $P_{12}$-odd, and $M_{R}$ as there; lopsided stages ($|x| \ne |y|$) with a complex neutrino coefficient are not treated.

## technical
The stored solar sum rule says that, at the $S_{3} \to S_{2}$ direction and the breaking lemma's order, a second stage of one type in each sector keeps the solar angle below about twenty-two degrees if $m_{1}/m_{2} \le 0.01$. It was proved for real textures, and extended to complex charged-lepton stages with a real neutrino coefficient, because the charged light state depends only on the moduli of the light-plane entries. With a complex neutrino coefficient that argument fails: the light neutrinos diagonalise the complex symmetric matrix $B B^{\mathsf T}$, and its Takagi vectors depend on the phase.

Here the complex case is decided for every neutrino stage whose two light-plane entries have equal modulus. A diagonal unitary brings each such block to the symmetric one, and for that block the tilt of the light neutrino and the mass ratio are explicit functions of $s = |x|^{2}/k^{2}$ and $u = \cos^{2}(\arg x)$. Along a curve of fixed mass ratio the tilt decreases as $u$ grows, so it is largest for a purely imaginary relative coefficient, where $\tan^{2}\theta_{\nu} = \sqrt{\rho}(1 + \sqrt{\rho})/(1 - \sqrt{\rho})$, against $\sqrt{\rho}$ for real coefficients. At $\rho = 1/100$ that raises the neutrino tilt from $17.5$ to $19.3$ degrees, and the solar angle bound from $21.6$ to $23.3$ degrees, still far below the $32$ to $36$ degrees the data need.

This answers whether the second family matrix of the $\su(2)_{R}$-covariant completion, the coupling of the sixteen to the conjugate rung field, is the lopsided second stage. It is not, at the breaking lemma's order: a $10$ coupling is symmetric in the family index on $c$ as on $c^{*}$, so the exchange-odd stage each sector receives is symmetric and of one type in modulus, and the bound holds whatever the complex couplings and vevs. A $126$ is covered only if its family matrix is exchange-even, since an exchange-odd part would also enter the Majorana matrix $M_{R} = v_{R}f$, which the result holds fixed. The completion adds a second family matrix and CP phases; the lopsidedness the solar angle needs still requires an antisymmetric coupling (the $120$) alongside a symmetric odd part in one sector.

## lay
The theory explains the three generations of matter through a symmetry broken in two stages, and the large solar mixing angle of neutrinos asks for a particular second stage, one that treats left- and right-handed states unequally. An earlier result showed that a second stage of the simple kind keeps that angle below about 22 degrees when the lightest neutrino is much lighter than the next, but it left open what complex phases in the neutrino sector could do. This result settles that, at the order of approximation the earlier result used: a phase can raise the bound, by an exact factor, but only to about 23 degrees, against the measured value of about 33. The recently found second coupling of matter to the theory's Higgs-like field, which gives up-type and down-type particles separate patterns, is of the simple kind, so it cannot provide the stage; the needed ingredient is still a coupling that is antisymmetric between generations, acting together with a symmetric one.

## one-liner
For a light-plane neutrino block with $|x| = |y|$ and any complex coefficient, $\tan^{2}\theta_{\nu} \le \sqrt{\rho}(1 + \sqrt{\rho})/(1 - \sqrt{\rho})$ ($11/90$ at $\rho = 1/100$, attained at a purely imaginary coefficient), so at the breaking lemma's order, if $m_{1}/m_{2} \le 0.01$, the solar angle stays below $23.3^{\circ}$ for all one-type complex stages, and the family-symmetric $10$ couplings to $c$ and $c^{*}$ cannot supply the lopsided second stage.
