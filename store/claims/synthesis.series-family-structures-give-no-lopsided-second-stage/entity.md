---
id: synthesis.series-family-structures-give-no-lopsided-second-stage
kind: claim
version: 3
title: 'The series'' family structures give no lopsided second stage'
status: proved
region: synthesis
subject: neutrinos
tags: [flavour-and-mixing, symmetry-breaking, no-go, representation-theory]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - neutrino.breaking-relation@3
  - synthesis.residual-s2-fixes-120-family-form@1
  - synthesis.coherent-face-vector-real-slices@1
  - synthesis.solar-angle-light-plane-sum-rule@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_odd_part_of_series_structures_is_the_sign_line
- kind: check
  ref: check.py::check_koide_circulant_puts_the_channel_phase_on_the_sign_line
- kind: check
  ref: check.py::check_light_plane_compression_is_one_type_in_modulus
- kind: check
  ref: check.py::check_complex_one_type_light_angle_and_overlap
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns
  - synthesis.one-type-second-stages-are-twins
  - synthesis.no-120-excludes-hierarchical-second-stage
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The circulant phase e^{I_4 delta} and the channel-phase coefficient I_4 (lambda/2) sin delta are written with I_4 in the formal level and the proof (numbers, and C, read in span{1, I_4}); nothing stays. To clear W222 the proof of (i) writes the cross-product matrix of u-prime as the contraction Av = v . (I_e u-prime) with the bivector dual to u-prime, I_e = e1 e2 e3 the family-space pseudoscalar, and its sign law through the automorphism sending I_e to det P I_e; same matrix, same argument.'
  open_problem: op.second-order-breaking
  note: >-
    Answers the question the stored decoupling result left: the second stage must be odd under the
    residual S2; is there such a stage among the series' own family structures? The structures are the
    unit, the democratic matrix, the S3 to S2 direction e3 e3^T, the residual-S2 120 form u' ^ s, and the
    cyclic shift that appears when the Koide vector is read as the spectrum of a circulant. Their
    complex span has exactly one S2-odd line, the cross-product matrix of u', which is the sign
    representation of S3 (once in the family matrices, antisymmetric, odd under every transposition);
    in the circulant reading the channel phase is its coefficient, so the 207 sits on that line and
    breaks S3 to Z3. That line is one type in modulus for every complex coefficient, and so are all
    symmetric, antisymmetric and Hermitian odd stages; the stored solar sum rule, proved for real
    textures, is extended here to complex charged-lepton stages, where only the moduli of the
    light-plane entries enter. So no stage built from the series' structures reaches the solar angle
    under Premise (H) at the breaking lemma's order with a real neutrino coefficient; a complex
    neutrino coefficient is recorded numerically only. The required stage needs a symmetric odd part,
    a standard-representation component the series does not contain, with a non-Hermitian relative
    phase. Transport-absent: finite-group representation theory on the family index.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: a marked pointer note after the formal clauses sends the sentence on complex neutrino coefficients ("makes no statement there") to synthesis.complex-neutrino-stages-keep-the-solar-sum-rule, which decides the one-type-in-modulus case (claimref only, not an edge, since that result uses this one). No clause changed.'
---
## formal
Work at the $S_{3} \to S_{2}$ direction with the textures and the order of Proposition \claimref{synthesis.solar-angle-light-plane-sum-rule}: $M_{e} = c(\J + \delta_{c}(E + X_{e}))$, $\mD = d(\J + \delta(E + X_{\nu}))$, $M_{R} = \alpha\Pi + M_{3}\J/3$, $E = e_{3}e_{3}^{\mathsf T}$, $P_{12}$ the exchange of $e_{1}, e_{2}$, each $X_{s}$ odd under $P_{12}$, now allowed complex. Call the series' family structures $\mathbb{1}$, $\J$, $\Pi$, $E$ (Lemma \claimref{neutrino.breaking-relation}), $u'\wedge s$ (Proposition \claimref{synthesis.residual-s2-fixes-120-family-form}) and the cyclic shift $S$, $Se_{j} = e_{j+1}$, with $S^{\mathsf T}$. Let $A$ be the matrix of $v \mapsto u'\times v$.
\begin{enumerate}
\item[(i)] \emph{(One odd line.)} The $P_{12}$-odd part of the complex span of the series' family structures is $\C A$, with $A = S - S^{\mathsf T}$ and $S + S^{\mathsf T} = \J - \mathbb{1}$. $A$ spans the sign representation of $S_{3}$, $PAP^{\mathsf T} = \mathrm{sgn}(P)A$, which occurs exactly once among the $3 \times 3$ family matrices; it is antisymmetric, fixed by the $3$-cycles and odd under every transposition. Without the shift, which enters only through the circulant reading of (ii) and is not a premise of the store, the $P_{12}$-odd part of the span of $\mathbb{1}$, $\J$, $\Pi$, $E$ and $u'\wedge s$ is zero.
\item[(ii)] \emph{(The channel phase on that line, circulant reading.)} The circulant (numbers, and $\C$, are read in $\mathrm{span}\{1, I_{4}\}$) $C = \mathbb{1} + \tfrac{\lambda}{2}(e^{I_{4}\delta}S + e^{-I_{4}\delta}S^{\mathsf T}) = (1 - \tfrac{\lambda}{2}\cos\delta)\mathbb{1} + \tfrac{\lambda}{2}\cos\delta\,\J + I_{4}\tfrac{\lambda}{2}\sin\delta\,A$ has eigenvalues $1 + \lambda\cos(\delta - 2\pi k/3)$ on the Fourier vectors $f_{k}$, the components of the projected Koide vector of Proposition \claimref{synthesis.coherent-face-vector-real-slices}(iii) up to scale and labelling. So if the face family lines are read as the Fourier lines of a flavour basis, the channel phase is the coefficient of the sign line, odd under every residual $S_{2}$, and it breaks $S_{3}$ to $\mathbb{Z}_{3}$.
\item[(iii)] \emph{(Moduli.)} In the compression $B_{s} = \bigl[\begin{smallmatrix} 2/3 & x_{s}\\ y_{s} & 0\end{smallmatrix}\bigr]$ of that proposition, a symmetric odd $X$ gives $y = x$, an antisymmetric one $y = -x$, a Hermitian one $y = \bar{x}$, and $X = \gamma A$ gives $x = \sqrt3\gamma = -y$ for every complex $\gamma$; in all of these $|x| = |y|$.
\item[(iv)] \emph{(Sum rule for complex charged stages.)} For $B = \bigl[\begin{smallmatrix} k & x\\ y & 0\end{smallmatrix}\bigr]$ with $k > 0$ and complex $x, y$, the light left singular vector depends only on $k$, $|x|$, $|y|$, and for $|x| = |y|$ it makes the angle $\theta$ with $\tan^{2}\theta = \sigma_{2}/\sigma_{1}$ with the odd axis. Hence, with any complex charged stage with $|x_{e}| = |y_{e}|$ and a real one-type neutrino stage, $|U_{e1}| \ge \cos(\theta_{e} + \theta_{\nu})$ and the sum rule $\Delta \le \arctan\sqrt{m_{e}/m_{\mu}} + \arctan(m_{1}/m_{2})^{1/4}$ holds; under the inequality of Premise (H), taken as a hypothesis of this clause, $\Delta < 21.6^{\circ}$, excluding the measured solar angle.
\item[(v)] \emph{(Consequence.)} No second stage built linearly from the series' family structures, in the charged sector with any complex coefficient and in the neutrino sector with a real one, reaches the measured solar angle under (H) at the breaking lemma's order. The stage the data need has $|y| \ne |x|$ in some sector: an $S_{2}$-odd symmetric part (a standard-representation component) together with an antisymmetric part at a non-Hermitian relative phase, which the series' structures do not supply; products such as $AE = (1,-1,0)\,e_{3}^{\mathsf T}$ would.
\end{enumerate}
For a complex neutrino coefficient the light neutrino angle is not a function of the moduli, and the result makes no statement there. \emph{Note (pointer).} For neutrino stages of one type in modulus ($|x| = |y|$ in the light-plane block), which is what the 10 couplings of the $\su(2)_{R}$-covariant completion supply, the complex case is decided in Proposition \claimref{synthesis.complex-neutrino-stages-keep-the-solar-sum-rule}: a phase raises the neutrino tilt at most by the factor $(1 + \sqrt{\rho})/(1 - \sqrt{\rho})$, to $\tan^{2}\theta_{\nu} = \tfrac{11}{90}$ (about $19.3^{\circ}$) at $\rho = \tfrac{1}{100}$, and the solar angle stays below $23.3^{\circ}$ under (H) at the breaking lemma's order; stages with $|x| \ne |y|$ remain outside both results.

## technical
The stored decoupling result says the second stage of the family breaking must be odd under the exchange of the first two families. This result asks whether the series' own family structures contain such a stage. They are few: the unit, the democratic matrix, the breaking direction, the one antisymmetric form allowed at the first stage, and the cyclic shift that appears when the Koide vector is written as the spectrum of a circulant matrix. All but the shift are even. The shift contributes one odd line, the cross-product matrix of the democratic vector, which is the sign representation of the permutation group: antisymmetric, unchanged by cyclic relabellings and reversed by every exchange. In the circulant reading of the Koide parametrisation the channel phase, the number that encodes the muon-to-electron ratio, is exactly the coefficient of this line, so the phase is an odd stage for every choice of residual exchange and breaks the permutations down to the cyclic ones.

That line cannot be the second stage the solar angle needs. The stored sum rule bounds the solar angle for one-type stages on real textures; here the bound is extended to complex charged-lepton stages, because the light state's angle depends only on the moduli of the two off-diagonal entries of the light-plane block, and symmetric, antisymmetric and Hermitian stages all give entries of equal modulus. Since the series' line is antisymmetric, any multiple of it is one type, and under the hierarchical premise, with a real neutrino coefficient and at the breaking lemma's order, the solar angle stays below about twenty-two degrees. The stage the data ask for needs a symmetric odd part as well, at a relative phase that is not Hermitian; the series' structures do not contain one, though products of them do.

## lay
The theory explains the three generations of matter through a symmetry among them that is broken in stages, and the measured mixing angles of neutrinos require a particular kind of second stage, one that treats the first two generations oppositely. This result looks through the theory's own building blocks for such a stage and finds exactly one: a twisting pattern that is reversed by swapping any two generations. When the electron, muon and tau square-root masses are read as the spectrum of a cyclic matrix, it is also where the theory's one free angle, the number behind the muon being about 207 times heavier than the electron, lives. But this pattern is of the wrong shape to produce the large solar mixing angle: the bound on that angle holds for it, even with complex phases in the charged-lepton part (the neutrino part with complex phases is only explored numerically). So, if the second stage is hierarchical in the sense the theory assumes, the stage the data require is not among the theory's existing structures.

## one-liner
The series' family structures ($\mathbb{1}$, $\J$, $E$, $u'\wedge s$ and the circulant shift) have a single $S_{2}$-odd line, the sign representation $u'\times$, on which the Koide channel phase sits in the $\sqrt{m}$ (circulant) reading of the projected coherent vector; every multiple of it, and every symmetric, antisymmetric or Hermitian odd stage, is one type in modulus, and the solar sum rule holds for complex charged stages, so at the breaking lemma's order no stage built linearly from the series' structures reaches the solar angle under (H) with a real neutrino coefficient.
