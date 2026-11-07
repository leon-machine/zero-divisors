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
  role: 'unit resolution pass, clauses (1) and (2) written with the transverse unit J, clause (3) with the central unit I_5 of Cl(2,3)'
  version: 5
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - singularity.descent-parity-average@5
  - synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom@1
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
    note: 'Unit principle U2 (the atom''s unit is J throughout, coordinator''s ruling of 7 November): clauses (1) and (2) are written with J = e_2 e_3, lambda = J theta, R_{J theta} = cos + J sigma sin with J sigma = I_4, diag(e^{-+J theta/2}) over span{1, J} (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited and added as a pinned uses edge, since the proof uses J central with square -1 and J* = -J). Clause (3) keeps the source''s formal unit i (U6): with J its first sentence would be false, J sigma = I_4 being an element of Cl(1,3); its conclusion that no real rotor of Cl(1,3) realises the Euclidean rotation also holds with J (R_{J theta} = e^{I_4 theta/2} is no rotor). The note says that the 2026-11-01 reading on values, exp(theta J/2), and the continued rotor on the mode operators, exp(theta I_4/2), concern different objects. Declaration kept, narrowed to clause (3). Revised at the coordinator''s ruling of 7 November: clause (3), its technical restatement and proof step (3) concern the continued rotor on spacetime vectors, so by U3 they are written with I_5 = I_4 e of Cl(2,3): R_{I_5 theta}, generator I_5 sigma = e_2 e_3 e not in Cl(1,3) (std-algebra.complexification-is-the-odd-extension, cited and added as a pinned uses edge); clause (3) now says that on the atom''s modes the unit is J and the continued flow is e^{I_4 theta/2}, a different object. Declaration removed: no bare i remains.'
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
Let $\sigma = e_0e_1$ be the boost bivector of the hyperbolic atom in the radial plane, with $\sigma^{2} = +1$, and let $\Aa = \Cl(1,1) \oplus \Cl(1,1)J \cong \Mat_2(\C)$ be the mode algebra, the complexification of the atom by its complex unit $J = e_{2}e_{3}$, which squares to $-1$ and commutes with $e_{0}$ and $e_{1}$ (Theorem \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}); numbers of the atom are read in $\mathrm{span}\{1, J\}$. Clause (3) concerns the continued rotor acting on spacetime vectors, so its unit is the one that commutes with every vector, the central unit $I_{5} = I_{4}e$ of the odd extension $\Cl(2,3)$ ($e$ orthogonal to spacetime, $Q(e) = +1$, Theorem \claimref{std-algebra.complexification-is-the-odd-extension}).
\begin{enumerate}
\item The boost rotor $R_\lambda = \exp(\lambda\sigma/2)$ continues to imaginary rapidity $\lambda = J\theta$ as $R_{J\theta} = \exp(J\theta\sigma/2) = \cos(\theta/2) + J\sigma\sin(\theta/2)$, a unitary of $\Aa$ whose generator $J\sigma = I_{4}$ squares to $-1$; $R_{2\pi J} = -1$ and $R_{4\pi J} = +1$, so the rotor has period $4\pi$ and its conjugation action period $2\pi$.
\item On the two-dimensional module on which $v, v^{*}$ act as ladder operators, $R_{J\theta} = \operatorname{diag}(e^{-J\theta/2}, e^{J\theta/2})$ over $\mathrm{span}\{1, J\}$: a rotation through $2\pi$ multiplies every spinor by $-1$, while its conjugation action on $\Aa$ is the identity.
\item On vectors the continued rotor is $R_{I_{5}\theta} = \cos(\theta/2) + I_{5}\sigma\sin(\theta/2)$, and its generator $I_{5}\sigma = e_{2}e_{3}e$ is not an element of the real algebra $\Cl(1,3)$. The dual member of the curvature-selected pair, $I\sigma_r = e_0e_1e_2e_3\,e_0e_1 = e_2e_3$, is the \emph{angular} plane: its rotor $\exp(\theta I\sigma_r/2)$ fixes $e_0$, $e_1$ and $\sigma_r$ and rotates $e_2$ into $e_3$, a rotation along the bifurcation sphere, not around it. The Euclidean rotation around the bifurcation sphere is therefore realised by no real rotor of $\Cl(1,3)$, and in particular not by the curvature-selected pair $\{\sigma_r, I\sigma_r\}$; it is realised by the unitary $R_{I_{5}\theta}$ of the complexified radial plane. On the atom's mode operators the unit is $J$ and the continued flow there is $R_{J\theta} = e^{I_{4}\theta/2}$ of (1), a different object.
\end{enumerate}

\emph{Note (the unit on values, 2026-11-01).} Clause (3) is stated for points, with the unit $I_{5}$ that commutes with every vector; with the atom's unit $J$ the generator of (1) is $J\sigma = I_{4}$, an element of $\Cl(1,3)$ that is not a bivector, so that $R_{J\theta} = e^{I_{4}\theta/2}$ is no rotor either. Read with the field theory's unit $I_{4}$ in place of that formal unit, acting on values, $I_{4}\sigma_{r} = I_{4}e_{0}e_{1} = e_{2}e_{3}$ does lie in $\Cl(1,3)$, and the boost rotor continued to imaginary rapidity is, on even values, the real rotor of that dual plane (\claimref{synthesis.modular-period-on-values-is-the-dual-plane-turn}); on points it is not, since $I_{4}$ anticommutes with vectors, so the stored statement holds for points. The two readings concern different objects and do not contradict each other: on values the continued rotor is $\exp(\theta J/2)$, whose conjugation is trivial on $\Aa$ ($J$ is central there), while on the atom's mode operators, with the unit $J$, it is $R_{J\theta} = \exp(\theta I_{4}/2)$ (as $JK = I_{4}/2$, \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}); $I_{4}$ and $J$ are not identified.

## technical
Let $\sigma = e_0e_1$ be the boost bivector of the hyperbolic atom in the radial plane, with $\sigma^2 = +1$, and $\Aa = \Cl(1,1) \oplus \Cl(1,1)J \cong \Mat_2(\C)$ the mode algebra, the atom complexified by its complex unit $J = e_{2}e_{3}$, which commutes with $e_{0}$ and $e_{1}$. Continuing the boost rotor $R_\lambda = \exp(\lambda\sigma/2)$ to imaginary rapidity $\lambda = J\theta$ gives $R_{J\theta} = \cos(\theta/2) + J\sigma\sin(\theta/2)$, a unitary of $\Aa$ whose generator $J\sigma = I_{4}$ squares to $-1$, with $R_{2\pi J} = -1$ and $R_{4\pi J} = +1$: the rotor has period $4\pi$ and its conjugation action period $2\pi$. On the ladder module $R_{J\theta} = \operatorname{diag}(e^{-J\theta/2}, e^{J\theta/2})$, so a rotation through $2\pi$ multiplies every spinor by $-1$ while acting trivially on $\Aa$.

On vectors the unit is the central unit $I_{5} = I_{4}e$ of $\Cl(2,3)$, which commutes with every vector, and the generator $I_{5}\sigma = e_{2}e_{3}e$ of the continued rotor $R_{I_{5}\theta}$ is not in the real algebra $\Cl(1,3)$ (on the atom's modes the unit is $J$ and the continued flow is $e^{I_{4}\theta/2}$, a different object). The dual member of the curvature-selected pair, $I\sigma_r = e_2e_3$, is the angular plane: its rotor fixes $e_0$, $e_1$ and $\sigma_r$ and turns $e_2$ into $e_3$, a rotation along the bifurcation sphere rather than around it. So the Euclidean rotation around the bifurcation sphere is realised by no real rotor of $\Cl(1,3)$, and in particular not by the pair $\{\sigma_r, I\sigma_r\}$, but by the unitary $R_{I_{5}\theta}$ of the complexified radial plane.

## lay
Thermal effects near a black hole are often explained by turning time into an angle, so that the horizon's boost becomes a rotation. This result locates that rotation precisely. It is not any real rotation available in the ordinary algebra of spacetime directions, and in particular not the rotation along the sphere that the curvature also picks out; it lives only in the complexified algebra of the radial plane, where one full turn flips the sign of every spinor.

## one-liner
The imaginary-rapidity continuation $R_{J\theta} = \cos(\theta/2) + J\sigma\sin(\theta/2)$ of the radial boost rotor, $J = e_{2}e_{3}$ the atom's complex unit, has period $4\pi$, with conjugation period $2\pi$, and is realised by no real rotor of $\Cl(1,3)$, in particular not by the curvature-selected pair, whose dual member $I\sigma_r = e_2e_3$ rotates along the bifurcation sphere.
