---
id: singularity.euclidean-rotor-where-it-lies
kind: claim
version: 5
title: The Euclidean rotor, and where it lies
status: proved
region: singularity
subject: thermality
tags: [rotors-and-stabilisers, hawking-temperature]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: 'unit resolution pass, the continuation written with the central unit I_5 of Cl(2,3)'
  version: 5
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - singularity.descent-parity-average@4
  - std-algebra.complexification-is-the-odd-extension@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.21
- kind: check
  ref: check.py::check_complexified_rotor_period_four_pi
- kind: check
  ref: check.py::check_module_form_and_conjugation_period
- kind: check
  ref: check.py::check_euclidean_rotation_is_no_real_rotor
locators:
  paper: T05
  number: Prop 7.21
  label: prop:euclid
  line: 1898
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the continuation''s unit acts on the complexified atom and on its points (clause (3) is stated for points and turns e_0 into the complex vector along e_1), so it must commute with every vector: it is the central unit I_5 = I_4 e of Cl(2,3) (std-algebra.complexification-is-the-odd-extension, cited and added as a pinned uses edge since the proof uses I_5 central with square -1). Lambda = I_5 theta, R_{I_5 theta}, I_5 sigma = e_2 e_3 e (not in Cl(1,3), so clause (3) holds exactly as stated) and diag(e^{-+I_5 theta/2}); the note on values keeps I_4 on even values and now says which unit acts where, and that the atom''s transverse unit J (U2) would give e^{I_4 theta/2}, not in conflict with clause (3) but a different unit. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the continuation''s i is the unit of the complexified atom Mat_2(C), and clause (3) distinguishes i sigma from I_4 sigma_r = e_2e_3, so i = I_4 would contradict it; the note on values already says how the field''s unit I_4 reads it. Declared complex-analysis.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 3 -> 4: a marked wording note after clause (3), at Leon''s optional item of 2026-11-01, that with the field theory''s unit i = I4 acting on values i sigma_r = e2e3 lies in Cl(1,3) and the continued boost on even values is the real rotor of that plane (synthesis.modular-period-on-values-is-the-dual-plane-turn); the stored statement holds for points and for the atom''s formal unit. Statement, proof and checks unchanged; no edge added.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the complexified rotor c + i sigma s (unitary, composition law, period 4 pi), its module form diag(e^{-i theta/2}, e^{i theta/2}) with conjugation period 2 pi and the parity at theta = pi, and that no real rotor gives the Euclidean rotation of the radial plane while R_{i theta} rotates (e0, i e1). Version 2 -> 3.'
  env: proposition
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: Removed the mechanical transport-algorithm edge, since the proof is rotor algebra plus the module
      form of sigma from the parity-average theorem, which is kept.
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$\lambda = i\theta$, $R_{i\theta}$, $i\sigma$, $\operatorname{diag}(e^{\mp i\theta/2})$: continuation
      to imaginary rapidity in the complexified atom $\Mat_2(\C)$ (analytic continuation, complex matrices);
      clause (3) itself distinguishes $i\sigma$ from the dual $I\sigma_r = e_2e_3$, so $i = I_4$ would contradict
      it'
  flow_note: 'both: it continues the rotor flow exp(lambda sigma/2) (T05 Thm 6.3, T08 Lem 4.2) to lambda
    = i theta and identifies the result, the unitary whose conjugation action is the phase flow e^{-i omega
    t} on the modes (T05 Thm 7.16, T07 Def 2.7), as the Euclidean rotation, realised by no real rotor of
    Cl(1,3).'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded.'
---

## formal
Let $\sigma = e_0e_1$ be the boost bivector of the hyperbolic atom in the radial plane, with $\sigma^{2} = +1$, and let $\Aa = \Cl(1,1) \oplus \Cl(1,1)I_{5} \cong \Mat_2(\C)$ be the mode algebra, the complexification of the atom $\Cl(1,1)$ of the radial plane by the central unit $I_{5} = I_{4}e$ of the odd extension $\Cl(2,3)$ of spacetime ($e$ orthogonal to spacetime, $Q(e) = +1$), which squares to $-1$ and commutes with $e_{0}$, $e_{1}$ and every other vector (Theorem \claimref{std-algebra.complexification-is-the-odd-extension}); numbers are read in $\mathrm{span}\{1, I_{5}\}$.
\begin{enumerate}
\item The boost rotor $R_\lambda = \exp(\lambda\sigma/2)$ continues to imaginary rapidity $\lambda = I_{5}\theta$ as $R_{I_{5}\theta} = \exp(I_{5}\theta\sigma/2) = \cos(\theta/2) + I_{5}\sigma\sin(\theta/2)$, a unitary of $\Aa$ whose generator $I_{5}\sigma$ squares to $-1$; $R_{2\pi I_{5}} = -1$ and $R_{4\pi I_{5}} = +1$, so the rotor has period $4\pi$ and its conjugation action period $2\pi$.
\item On the two-dimensional module on which $v, v^{*}$ act as ladder operators, $R_{I_{5}\theta} = \operatorname{diag}(e^{-I_{5}\theta/2}, e^{I_{5}\theta/2})$: a rotation through $2\pi$ multiplies every spinor by $-1$, while its conjugation action on $\Aa$ is the identity.
\item The generator $I_{5}\sigma = e_{2}e_{3}e$ is not an element of the real algebra $\Cl(1,3)$. The dual member of the curvature-selected pair, $I\sigma_r = e_0e_1e_2e_3\,e_0e_1 = e_2e_3$, is the \emph{angular} plane: its rotor $\exp(\theta I\sigma_r/2)$ fixes $e_0$, $e_1$ and $\sigma_r$ and rotates $e_2$ into $e_3$, a rotation along the bifurcation sphere, not around it. The Euclidean rotation around the bifurcation sphere is therefore realised by no real rotor of $\Cl(1,3)$, and in particular not by the curvature-selected pair $\{\sigma_r, I\sigma_r\}$; it is realised by the unitary $R_{I_{5}\theta}$ of the complexified radial plane.
\end{enumerate}

\emph{Note (the unit on values, 2026-11-01).} Clause (3) is stated for points, and for the central unit $I_{5}$ of the atom's complexification. Read instead with the field theory's unit $I_{4}$ acting on values, $I_{4}\sigma_{r} = I_{4}e_{0}e_{1} = e_{2}e_{3}$ does lie in $\Cl(1,3)$, and the boost rotor continued to imaginary rapidity is, on even values, the real rotor of that dual plane (\claimref{synthesis.modular-period-on-values-is-the-dual-plane-turn}); on points it is not, since $I_{4}$ anticommutes with vectors, so the stored statement holds for points. The two units act in different places, $I_{5}$ on the complexified atom and its points, $I_{4}$ on even values, and are not identified; nor is either the atom's transverse unit $J = e_{2}e_{3}$ of \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}, which commutes with $e_{0}$ and $e_{1}$ but not with $e_{2}$, $e_{3}$, and with which the continued rotor is $e^{J\theta\sigma/2} = e^{I_{4}\theta/2}$, no rotor of $\Cl(1,3)$.

## technical
Let $\sigma = e_0e_1$ be the boost bivector of the hyperbolic atom in the radial plane, with $\sigma^2 = +1$, and $\Aa = \Cl(1,1) \oplus \Cl(1,1)I_{5} \cong \Mat_2(\C)$ the mode algebra, the atom complexified by the central unit $I_{5} = I_{4}e$ of $\Cl(2,3)$, which commutes with every vector. Continuing the boost rotor $R_\lambda = \exp(\lambda\sigma/2)$ to imaginary rapidity gives $R_{I_{5}\theta} = \cos(\theta/2) + I_{5}\sigma\sin(\theta/2)$, a unitary of $\Aa$ whose generator $I_{5}\sigma$ squares to $-1$, with $R_{2\pi I_{5}} = -1$ and $R_{4\pi I_{5}} = +1$: the rotor has period $4\pi$ and its conjugation action period $2\pi$. On the ladder module $R_{I_{5}\theta} = \operatorname{diag}(e^{-I_{5}\theta/2}, e^{I_{5}\theta/2})$, so a rotation through $2\pi$ multiplies every spinor by $-1$ while acting trivially on $\Aa$.

The generator $I_{5}\sigma = e_{2}e_{3}e$ is not in the real algebra $\Cl(1,3)$. The dual member of the curvature-selected pair, $I\sigma_r = e_2e_3$, is the angular plane: its rotor fixes $e_0$, $e_1$ and $\sigma_r$ and turns $e_2$ into $e_3$, a rotation along the bifurcation sphere rather than around it. So the Euclidean rotation around the bifurcation sphere is realised by no real rotor of $\Cl(1,3)$, and in particular not by the pair $\{\sigma_r, I\sigma_r\}$, but by the unitary $R_{I_{5}\theta}$ of the complexified radial plane.

## lay
Thermal effects near a black hole are often explained by turning time into an angle, so that the horizon's boost becomes a rotation. This result locates that rotation precisely. It is not any real rotation available in the ordinary algebra of spacetime directions, and in particular not the rotation along the sphere that the curvature also picks out; it lives only in the complexified algebra of the radial plane, where one full turn flips the sign of every spinor.

## one-liner
The imaginary-rapidity continuation $R_{I_{5}\theta} = \cos(\theta/2) + I_{5}\sigma\sin(\theta/2)$ of the radial boost rotor has period $4\pi$, with conjugation period $2\pi$, and is realised by no real rotor of $\Cl(1,3)$, in particular not by the curvature-selected pair, whose dual member $I\sigma_r = e_2e_3$ rotates along the bifurcation sphere.
