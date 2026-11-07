---
id: angle.imported-singularity-papers-state-selection
kind: claim
version: 11
title: 'Imported: the singularity paper''s state selection'
status: proved
region: angle
subject: thermality
tags: [hawking-temperature, modular-theory, undetermined-input]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-angle, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 11
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - singularity.euclidean-section-period@5
  - singularity.modular-descent@6
  - singularity.rate-rigidity-temperature-not-algebra-intrinsic@5
  - singularity.schmidt-forcing-proved-outright@5
  - singularity.class-relative-no-go-no-supplied@3
  - singularity.computed@4
  assumes:
  - singularity.l-boundary-mode-locality@2
  - singularity.q-joint-quasi-freeness-s-wave@3
  - singularity.r-regularity-fixed-locus@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_boost_invariant_cyclic_separating_states
- kind: check
  ref: check.py::check_marginal_is_gibbs_at_the_sample_point
- kind: check
  ref: check.py::check_intertwining_automorphisms_act_through_sign
- kind: check
  ref: check.py::check_surface_gravity_and_euclidean_period
- kind: check
  ref: check.py::check_kms_relations_fix_each_mode_marginal
- kind: check
  ref: check.py::check_supplied_class_ultralocal_and_sea_level_occupancies
locators:
  paper: T05-angle
  number: Fact 1.1
  label: fact:T5
  line: 116
outside_ga:
  kind: complex-analysis
  why: 'the phase flow Ad(e^{itK}) acts on the complex mode factor of the boundary-mode algebra, whose modes descend from the atom of the spacetime radial plane and anticommute with I_4 (conventions, known limits 1 and 2), as its defining object declares, so I_4 is not shown to be its unit'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the phase flow Ad(e^{itK}) acts on the complex mode factor of the boundary-mode algebra, whose modes descend from the atom of the spacetime radial plane and anticommute with I_4 (conventions, known limits 1 and 2), as its defining object declares, so I_4 is not shown to be its unit.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Label: the weights omega_k = kappa k with the sea at k = 0 stated here are the source paper''s convention, version 2 of premise (Q); version 3 of (Q) adopts kappa(k + 1/2), and only the n_0 = 1/2 line of this statement depends on the offset. Version 7 -> 8. Check entries synced with check.py: +2, -2 (added check_kms_relations_fix_each_mode_marginal, check_supplied_class_ultralocal_and_sea_level_occupancies; removed check_r_imposes_kms_mode_by_mode, check_supplied_class_ultralocal_and_s_wave_weights). Version 8 -> 9. Fix round: KMS check solves the KMS relations for a general functional (unique Gibbs marginal); ultralocality widened to all number monomials and parity sections with a hopping contrast; bilinear weights computed from the flow; (R) and the weights labelled as assumed premises. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 9 -> 10.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the boost-invariant cyclic separating states, the Gibbs marginal at 9/16, the sign-only action of intertwining automorphisms, kappa = 1/4M and the period, KMS per mode, ultralocality and the s-wave weights. Version 6 -> 7.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: STRUCTURE L3 and L8
    open_problem: op.small-findings
    note: 'L3: the Schmidt form now carries T05 Lem 7.2''s hypotheses (invariant up to phase, cyclic and separating), without which the product vectors |01>, |10> are also invariant; L8: the locality premise is named (L_E), as in singularity.l-boundary-mode-locality, not (L), which in T05 is the rate model''s two-sector postulate.'
  env: fact
  context_refs:
  - singularity.euclidean-section-period
  - singularity.modular-descent
  - singularity.rate-rigidity-temperature-not-algebra-intrinsic
  - singularity.schmidt-forcing-proved-outright
  - singularity.why-calibration-cannot-be-internal
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    removed:
    - singularity.why-calibration-cannot-be-internal
    added:
    - singularity.class-relative-no-go-no-supplied
    - singularity.computed
    note: 'Restating fact: added the supplied-class theorem (ultralocality) and the surface-gravity computation,
      which the fact restates; removed the calibration-locus proposition, cited in the provenance but
      not restated; the (L) assumes edge is left in place although ultralocality is a theorem, as assumes
      edges are a maintainer decision. Levels pass: named premises (L) and (Q), both in this entry''s
      assumes, in the technical, lay and one-liner, and named (R) in the lay.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - singularity.l-boundary-mode-locality
    - singularity.q-joint-quasi-freeness-s-wave
  source_formal: For the horizon pair, a boost-invariant state has the form $\cos\theta\,\ket{00} + \sin\theta\,\ket{11}$;
    its one-sided marginal is $\operatorname{diag}(\cos^{2}\theta, \sin^{2}\theta)$, the Gibbs state for
    the number operator at $\tan^{2}\theta = e^{-\beta\omega}$; the sample point $e^{-\omega/T} = \tfrac{9}{16}$
    has $(\cos\theta, \sin\theta) = (\tfrac45, \tfrac35)$. Every automorphism of the mode factor intertwining
    the boost flow acts on $\beta$ through $\{\pm 1\}$ only. The surface gravity is $\kappa = 1/4M$, the
    Euclidean section is smooth at the bifurcation sphere exactly for the period $2\pi/\kappa$, and (R)
    imposes KMS at that period mode by mode. The supplied class is ultralocal, and the s-wave array of Step
    4e has weights $\omega_{k} = \kappa k$ with its sea level at $k = 0$. \emph{Provenance:} \cite[Lem.~7.2,
    Thm.~7.3, Thm.~7.16, Prop.~7.18, Prem.~7.19, Prop.~7.25, Rem.~7.26, Prem.~7.30, Rem.~7.33, Prem.~8.1,
    Thm.~C.8, Rem.~C.9, Prop.~A.2]{ButlerT5}.
  flow_note: phase flow e^{-i omega t} on the modes (T05 Thm 7.16, T07 Def 2.7), the Euclidean rotation
    of T05 Prop 7.21. The sentence on automorphisms intertwining the flow restates T05 Thm 7.16, whose flow
    is Ad(e^{itK}); the boost-invariance of the pair state holds equally under the rotor flow, since both
    say the state commutes with K.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded; formal, proof main now name the flow (original formal
      in source_formal, proof in orig-proof-*.tex where changed; version bumped).'
---

## formal
For the horizon pair, a state vector that is invariant up to phase under the boost and cyclic and separating for the pair factor has the form $\cos\theta\,\ket{00} + \sin\theta\,\ket{11}$ with $\cos\theta\sin\theta \neq 0$; its one-sided marginal is $\operatorname{diag}(\cos^{2}\theta, \sin^{2}\theta)$, the Gibbs state for the number operator at $\tan^{2}\theta = e^{-\beta\omega}$; the sample point $e^{-\omega/T} = \tfrac{9}{16}$ has $(\cos\theta, \sin\theta) = (\tfrac45, \tfrac35)$. Every automorphism of the mode factor intertwining the boost's phase flow $\operatorname{Ad}(e^{itK})$ acts on $\beta$ through $\{\pm 1\}$ only. The surface gravity is $\kappa = 1/4M$, the Euclidean section is smooth at the bifurcation sphere exactly for the period $2\pi/\kappa$, and (R) imposes KMS at that period mode by mode. The supplied class is ultralocal, and the s-wave array of Step 4e has weights $\omega_{k} = \kappa k$ with its sea level at $k = 0$. \emph{Provenance:} \cite[Lem.~7.2, Thm.~7.3, Thm.~7.16, Prop.~7.18, Prem.~7.19, Prop.~7.25, Rem.~7.26, Prem.~7.30, Rem.~7.33, Prem.~8.1, Thm.~C.8, Rem.~C.9, Prop.~A.2]{ButlerT5}.

## technical
This entry restates the singularity paper's state selection for a horizon pair. A state vector of the pair that is boost invariant up to phase and cyclic and separating has the form $\cos\theta\,\ket{00} + \sin\theta\,\ket{11}$, and its one-sided marginal $\operatorname{diag}(\cos^{2}\theta, \sin^{2}\theta)$ is the Gibbs state for the number operator with $\tan^{2}\theta = e^{-\beta\omega}$; the sample point $e^{-\omega/T} = \tfrac{9}{16}$ corresponds to $(\cos\theta, \sin\theta) = (\tfrac45, \tfrac35)$. The algebra does not fix $\beta$: every automorphism of the mode factor that intertwines the boost flow acts on $\beta$ only through $\{\pm 1\}$.

The value comes from the geometry and a premise. The surface gravity is $\kappa = 1/4M$, the Euclidean section is smooth at the bifurcation sphere exactly for the period $2\pi/\kappa$, and premise (R) imposes KMS at that period mode by mode. The supplied class of boundary-mode generators, the number-diagonal class that the boundary-mode locality premise (L$_E$) admits, is ultralocal, and the s-wave array has weights $\omega_{k} = \kappa k$ with its sea level at $k = 0$, the convention of premise (Q).

## lay
For a pair of modes straddling a black hole horizon, the states that look the same under the horizon's boost form a one-parameter family, and each of them looks thermal from one side. The algebra alone cannot say which temperature is right; it is set by requiring the geometry to be smooth at the horizon, an assumption (premise (R)) that gives the Hawking value. This entry gathers those earlier results, together with two further premises it rests on: that the framework's own dynamics never moves particles between points (premise (L$_E$), boundary-mode locality), and that the modes are jointly in the simplest thermal state with evenly spaced energies (premise (Q)).

## one-liner
A boost-invariant, cyclic and separating horizon-pair state is a thermofield state whose temperature the algebra leaves free and premise (R) fixes at the Euclidean period $2\pi/\kappa$, with $\kappa = 1/4M$; premises (Q) and (L$_E$) supply the s-wave weights and the ultralocal generator class.
