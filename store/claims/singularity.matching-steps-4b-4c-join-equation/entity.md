---
id: singularity.matching-steps-4b-4c-join-equation
kind: claim
version: 7
title: 'The matching: Steps 4b and 4c join by equation'
status: proved
region: singularity
subject: thermality
tags: [modular-theory, hyperbolic-plane, rotors-and-stabilisers]
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
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 6
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'unit resolution pass, the phase flow written with the transverse unit J'
  version: 7
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - sheaf.localised-transport@6
  - sheaf.one-sided-completion@4
  - singularity.curvature-gauge-field-exact-shape-decoupling@5
  - singularity.degeneration-exactly@2
  - singularity.modular-structure-completed-pair@5
  - singularity.pseudo-inverse-identities-hyperbolic-atom@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:6.4
- kind: check
  ref: check.py::check_atom_on_the_physical_radial_plane
- kind: check
  ref: check.py::check_eigen_and_square_characterise_sigma
- kind: check
  ref: check.py::check_boost_flow_weights_and_orientation
- kind: check
  ref: check.py::check_degenerate_plane_at_r_zero_and_shared_direction
locators:
  paper: T05
  number: Cor 6.4
  label: cor:weld
  line: 1674
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U2: the phase flow Ad(e^{it sigma/2}) of the completed pair is written Ad(e^{J t sigma/2}) with J = e_2 e_3, the atom''s complex unit (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited as a mention); the formal level says that J, which equals the excluded dual I sigma_r as an element, is the flow''s scalar and not its bivector, so the characterisation of sigma is unchanged. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the phase flow Ad(e^{it sigma/2}) of the boundary pair is the complex phase whose real rotor flow is exp(lambda sigma/2); with I_4 in its place exp(I_4 t sigma/2) would be a rotor of the dual plane I sigma_r that the corollary excludes.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the CAR atom on the physical radial plane at every sampled radius (signature (1,1), physical null directions e0 +- e1), S(B) = -2B with B^2 = 1 characterising +-sigma_r, the boost weights of v and v*, and the rank-one degenerate weighted plane at r = 0 with k-sharp spacelike. Version 4 -> 5.'
  env: corollary
  context_refs:
  - sheaf.localised-transport
  - sheaf.one-sided-completion
  - sheaf.schwarzschild-degeneration-boundary-tame
  - singularity.degeneration-exactly
  - singularity.imported-one-sided-completion-singularity
  - singularity.plane-rate
  - singularity.pseudo-inverse-identities-hyperbolic-atom
  - singularity.transport-schwarzschild-fibre
  - singularity.why-calibration-cannot-be-internal
  unresolved_refs:
  - rem:evenledger
  - rem:frame
  - rem:weights
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.pseudo-inverse-identities-hyperbolic-atom
    - sheaf.one-sided-completion
    - sheaf.localised-transport
    - singularity.degeneration-exactly
    note: 'Removed the mechanical transport-algorithm edge; added the atom lemma (the hypothesis), the
      localisation theorem and corollary and the degeneration proposition (the ''one plane'' conclusion
      rests on them), leaving the scope caveats'' citations as context; the choice of which of the many
      cited results count as premises is a judgement call. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - singularity.pseudo-inverse-identities-hyperbolic-atom
    stated_role:
    - sheaf.localised-transport
    - sheaf.one-sided-completion
    - singularity.degeneration-exactly
    note: The proof covers only the equation pair; a closing sentence states the role of the three premises
      the statement's location clause uses (the localisation theorem cited there as T4 Thm 4.4 and Cor 4.5).
  source_formal: |-
    Realise the hyperbolic atom of Lemma \claimref{singularity.pseudo-inverse-identities-hyperbolic-atom} on the radial plane, $e_0 = \hat e_t$, $e_1 = \hat e_r$. Where this realisation lies must be stated, because it is available exactly where the ascent is not needed: at every $r > 0$ the physical radial plane has signature $(1,1)$ and carries a CAR pair inside $\Cl(1,3)$ with no ascent at all, but at $r = 0$ the radial plane itself degenerates, its radical the dying direction $k$ (corank one in the forced weighting, Remark \ref{rem:weights} and Fact \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(2); Proposition \claimref{singularity.degeneration-exactly}'s uniform rescaling degenerates the whole form), so no CAR pair supported on the radial plane survives there, even though the weighted module still contains hyperbolic planes (Fact \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(2): $V_1$ carries $\mathrm{diag}(m^2, -1, -1)$). On $E$ the atom is carried by $\operatorname{span}(k, \nO/2\nu)$, one leg the dying direction itself and one adjoined (Fact \claimref{singularity.imported-one-sided-completion-singularity}, Remark \ref{rem:evenledger}): the odd sector is not a pre-existing grading of $\Cl(1,3)$ precisely because one of its legs lies outside. Nor is the matching an identification of two coexisting copies, Fact \claimref{singularity.imported-one-sided-completion-singularity}'s pair existing exactly over $E$: the two constructions share the leg $k$. At every $r > 0$ the radial plane contains $k^{\sharp} = -\sqrt r\,\er$ (Proposition \claimref{singularity.transport-schwarzschild-fibre}(4)), the plane degenerates onto $\R k$ as $r \to 0$, and the completion re-attaches $\nO/2\nu$ to that same $k$. What is shared is the direction and the degeneration onto it, not a null leg of the atom: $k^{\sharp}$ is spacelike at every $r > 0$ while the atom's legs are null, and the $E$-atom's bivector $k \wedge \nO/2\nu$ is not $\sigma_r$. The identification of the modular bivector with the curvature-selected plane is therefore made at $r > 0$, where Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling} holds, and \emph{transported} to $E$ along the degeneration; that transport is the matching's residual step, stated as such rather than absorbed into the shared direction, and the two-level computations of Steps 4c through 6b concern the abstract atom, whichever realisation carries it. Then the modular bivector of Theorem \claimref{singularity.modular-structure-completed-pair},
    \[
    \sigma \;=\; v^*v - vv^* \;=\; e_0 e_1 ,
    \]
    spans the radial plane and satisfies the pair of equations
    \[
    S(\sigma) = -2\,\sigma, \qquad \sigma^2 = +1 ,
    \]
    and this pair characterises $\sigma$ up to sign among the unit frame bivectors: the eigenvalue equation confines $\sigma$ to $\{\sigma_r, I\sigma_r\}$ (Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}), and the square excludes the dual, for which $(I\sigma_r)^2 = -1$. The bivector whose rotor flow is Step 4c's modular flow is therefore the same object Step 4b's curvature distinguishes, identified by equation rather than by name; the residual sign is the orientation of the boost, the labelling of outgoing against ingoing, which is exactly the $\mathbb{Z}_2$ that Theorem \claimref{singularity.modular-structure-completed-pair}(2) attaches to the weights of $v$ and $v^*$. And by the localisation theorem \cite[Thm.~4.4, Cor.~4.5]{ButlerT4} the pair, hence the atom, hence $\sigma$, is at the degenerate radial direction, which is where Proposition \claimref{singularity.degeneration-exactly} located the division: the plane the curvature selects, the plane the completed pair lies in, and the plane through which division fails are one plane. One plane, not one locus: the curvature selects it at every $r > 0$, the calibration reads it at the horizon (Proposition \claimref{singularity.plane-rate}), the ladder inhabits it on $E$, and Proposition \claimref{singularity.why-calibration-cannot-be-internal} records that the calibration locus and the singular locus do not meet; what carries the identification across them is the frame-robustness of the plane (Remark \ref{rem:frame}) and the radius-independence of its selection, not a claim that the loci coincide.
  flow_note: 'both: the identification is of the generator sigma, which the rotor flow exp(lambda sigma/2)
    (T05 Thm 6.3, T08 Lem 4.2) and the phase flow e^{-i omega t} on the modes (T05 Thm 7.16, T07 Def 2.7),
    the Euclidean rotation of T05 Prop 7.21 share; Step 4c''s modular flow is the phase flow, sigma''s rotor
    flow continued to imaginary rapidity.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded; formal now name the flow (original formal in source_formal,
      proof in orig-proof-*.tex where changed; version bumped).'
---

## formal
Realise the hyperbolic atom of Lemma \claimref{singularity.pseudo-inverse-identities-hyperbolic-atom} on the radial plane, $e_0 = \hat e_t$, $e_1 = \hat e_r$. Where this realisation lies must be stated, because it is available exactly where the ascent is not needed: at every $r > 0$ the physical radial plane has signature $(1,1)$ and carries a CAR pair inside $\Cl(1,3)$ with no ascent at all, but at $r = 0$ the radial plane itself degenerates, its radical the dying direction $k$ (corank one in the forced weighting, Remark \ref{rem:weights} and Fact \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(2); Proposition \claimref{singularity.degeneration-exactly}'s uniform rescaling degenerates the whole form), so no CAR pair supported on the radial plane survives there, even though the weighted module still contains hyperbolic planes (Fact \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(2): $V_1$ carries $\mathrm{diag}(m^2, -1, -1)$). On $E$ the atom is carried by $\operatorname{span}(k, \nO/2\nu)$, one leg the dying direction itself and one adjoined (Fact \claimref{singularity.imported-one-sided-completion-singularity}, Remark \ref{rem:evenledger}): the odd sector is not a pre-existing grading of $\Cl(1,3)$ precisely because one of its legs lies outside. Nor is the matching an identification of two coexisting copies, Fact \claimref{singularity.imported-one-sided-completion-singularity}'s pair existing exactly over $E$: the two constructions share the leg $k$. At every $r > 0$ the radial plane contains $k^{\sharp} = -\sqrt r\,\er$ (Proposition \claimref{singularity.transport-schwarzschild-fibre}(4)), the plane degenerates onto $\R k$ as $r \to 0$, and the completion re-attaches $\nO/2\nu$ to that same $k$. What is shared is the direction and the degeneration onto it, not a null leg of the atom: $k^{\sharp}$ is spacelike at every $r > 0$ while the atom's legs are null, and the $E$-atom's bivector $k \wedge \nO/2\nu$ is not $\sigma_r$. The identification of the modular bivector with the curvature-selected plane is therefore made at $r > 0$, where Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling} holds, and \emph{transported} to $E$ along the degeneration; that transport is the matching's residual step, stated as such rather than absorbed into the shared direction, and the two-level computations of Steps 4c through 6b concern the abstract atom, whichever realisation carries it. Then the modular bivector of Theorem \claimref{singularity.modular-structure-completed-pair},
\[
\sigma \;=\; v^*v - vv^* \;=\; e_0 e_1 ,
\]
spans the radial plane and satisfies the pair of equations
\[
S(\sigma) = -2\,\sigma, \qquad \sigma^2 = +1 ,
\]
and this pair characterises $\sigma$ up to sign among the unit frame bivectors: the eigenvalue equation confines $\sigma$ to $\{\sigma_r, I\sigma_r\}$ (Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}), and the square excludes the dual, for which $(I\sigma_r)^2 = -1$. The bivector that generates Step 4c's modular flow, the phase flow $\operatorname{Ad}(e^{Jt\sigma/2})$, whose real rotor flow is $\exp(\lambda\sigma/2)$, is therefore the same object Step 4b's curvature distinguishes, identified by equation rather than by name (the flow's scalar unit is the atom's complex unit $J = e_{2}e_{3}$, which commutes with the atom, \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}; as an element $J$ equals the dual $I\sigma_r$, but it enters the flow as its scalar, not as its bivector, which is $\sigma$); the residual sign is the orientation of the boost, the labelling of outgoing against ingoing, which is exactly the $\mathbb{Z}_2$ that Theorem \claimref{singularity.modular-structure-completed-pair}(2) attaches to the weights of $v$ and $v^*$. And by the localisation theorem \cite[Thm.~4.4, Cor.~4.5]{ButlerT4} the pair, hence the atom, hence $\sigma$, is at the degenerate radial direction, which is where Proposition \claimref{singularity.degeneration-exactly} located the division: the plane the curvature selects, the plane the completed pair lies in, and the plane through which division fails are one plane. One plane, not one locus: the curvature selects it at every $r > 0$, the calibration reads it at the horizon (Proposition \claimref{singularity.plane-rate}), the ladder inhabits it on $E$, and Proposition \claimref{singularity.why-calibration-cannot-be-internal} records that the calibration locus and the singular locus do not meet; what carries the identification across them is the frame-robustness of the plane (Remark \ref{rem:frame}) and the radius-independence of its selection, not a claim that the loci coincide.

## technical
Realise the hyperbolic atom on the radial plane, $e_0 = \hat e_t$, $e_1 = \hat e_r$. The modular bivector of the completed pair is then $\sigma = v^*v - vv^* = e_0e_1$, which spans the radial plane and satisfies $S(\sigma) = -2\sigma$ and $\sigma^2 = +1$. Among the unit frame bivectors this pair of equations characterises $\sigma$ up to sign: the eigenvalue equation confines it to $\{\sigma_r, I\sigma_r\}$, and the square excludes the dual, $(I\sigma_r)^2 = -1$. The residual sign is the orientation of the boost, outgoing against ingoing. So the bivector generating the modular flow is the object the curvature distinguishes, identified by equation rather than by name.

Where the realisation lies is stated with care. At every $r > 0$ the radial plane has signature $(1,1)$ and carries a CAR pair with no ascent; at $r = 0$ it degenerates onto the dying direction $k$, and on the singular boundary the atom is carried by $\operatorname{span}(k, \nO/2\nu)$, one leg adjoined. The identification is made at $r > 0$ and transported to the boundary along the degeneration, a residual step stated as such. By the localisation theorem the completed pair sits at the degenerate radial direction, so the plane the curvature selects, the plane of the completed pair and the plane through which division fails are one plane, though not one locus.

## lay
Two separate steps of the argument each pick out a special plane: one from the curvature of the black hole, one from the internal clock of the quantum modes. This result shows they are the same plane, by checking that the clock's plane satisfies the two equations that single out the curvature's plane, up to a choice of orientation (outgoing or ingoing). The identification is made away from the singularity and carried to it along the way the geometry degenerates there, a step that is stated openly rather than absorbed.

## one-liner
The modular bivector of the completed pair, $\sigma = e_0e_1$, satisfies $S(\sigma) = -2\sigma$ and $\sigma^2 = +1$, which characterise the curvature-selected boost plane up to sign, so the modular flow and the curvature select the same plane, identified at $r > 0$ and transported to the singular boundary.
