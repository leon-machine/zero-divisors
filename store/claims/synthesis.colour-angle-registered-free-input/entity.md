---
id: synthesis.colour-angle-registered-free-input
kind: claim
version: 1
title: 'Premise: the physical colour angle is a registered free input'
status: postulate
region: synthesis
subject: standard-model
tags: [gauge-fields, undetermined-input]
proposed_by:
  kind: ai
  session: maintainer-2026-11-16
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction and decision
- name: Claude Fable 5.2
  role: drafting
  source: maintainer pass 2026-11-16 (anomaly)
review: draft
lineage:
  motivated_by:
  - synthesis.colour-angle-term-under-the-stored-maps-and-no-colour-anomalous-phase-of-the-rung-coupling
  - synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion
  - synthesis.imported-physical-colour-angle-and-its-shift-under-quark-rephasing
  - synthesis.imported-neutron-dipole-bound-and-its-conversion-to-the-colour-angle
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - synthesis.common-ceiling-coupling-premise
  - synthesis.matter-asymmetry-registered-free-input
  - synthesis.number-n-registered-free-input
  - synthesis.rung-unit-second-free-number
extraction:
  open_problem: op.strong-cp
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: >-
      New postulate, adopted by Leon's decision D1 of 16 November 2026: the physical colour angle, the
      coefficient of the colour four-form plus the phase of the quark mass determinant, is registered as a
      free input of the series with a refutation condition, in the format of
      synthesis.matter-asymmetry-registered-free-input, so that the premise register counts it. It rests on
      the two results accepted the same day (the colour angle term under the stored maps, and the phase of
      the quark mass determinant on the covariant completion) and on two Facts imported with it (the
      definition of the physical angle and its shift under a rephasing; the neutron dipole bound and its
      conversion). With it the open problem op.strong-cp is settled by its own success clause, on the
      branch "record it as a free input with a refutation condition". What is proved and what is argued is
      said in the formal level: that the series leaves the angle free is proved for the covariant rung
      coupling and for the stored maps examined, and argued for the store as a whole, since the lists of
      stored maps and of stored fields are not shown complete. Two premise questions that the two
      results raise are recorded as open and not decided: how the stored CPT conjugation acts on
      the gauge sector, and which identification of the two towers' orientations the common-ceiling
      coupling premise uses for the angle. The quarter-turn texture, on which the mass phase would be zero
      or a half turn at tree level, is stored as a conjecture
      (synthesis.exact-quarter-turn-texture-of-the-quark-stages) and is not adopted. No assumes edges are
      added.
---

## formal
\emph{Premise ($\bar\theta$), the physical colour angle as a registered input.} Let $\Theta(F)$ be the grade-four part of the colour field square, the characteristic four-form of the colour field strength read in the spacetime algebra (Theorem \claimref{synthesis.colour-angle-term-under-the-stored-maps-and-no-colour-anomalous-phase-of-the-rung-coupling}, setting and clause (i)), and let $\theta$ be the coefficient with which it enters the action, in the normalisation of Fact \claimref{synthesis.imported-physical-colour-angle-and-its-shift-under-quark-rephasing}(i), in which $\theta$ is an angle. Let $\theta_{M}$ be the mass phase, the $I_{4}$ phase of $\det M_{u}\det M_{d}$ for the quark mass matrices of the covariant completion (Theorem \claimref{synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion}). The \emph{physical colour angle} is
\[
\bar\theta = \theta + \theta_{M},
\]
defined modulo a whole turn; a rephasing of the quarks moves $\theta$ and $\theta_{M}$ by opposite amounts and leaves $\bar\theta$ (Fact \claimref{synthesis.imported-physical-colour-angle-and-its-shift-under-quark-rephasing}(ii), (iii)). The premise: \emph{$\bar\theta$ is a free number of the series.} It is not computed from the transport structure, from another premise of the register, or from a dynamics of the series, and it is not a function of $N$ (Premise \claimref{synthesis.number-n-registered-free-input}), of the D-term level $\xi G$ (Premise \claimref{synthesis.rung-unit-second-free-number}) or of the asymmetry $\epsilon$ (Premise \claimref{synthesis.matter-asymmetry-registered-free-input}). Its value is constrained by the record and not explained: near zero, the neutron dipole measurement and its conversion give $|\bar\theta|$ below about $2 \times 10^{-10}$, on the condition that the angle term is the only source of the neutron's dipole moment and with the conversion coefficient known to a factor of a few (Fact \claimref{synthesis.imported-neutron-dipole-bound-and-its-conversion-to-the-colour-angle}). That bound is linear in the angle near zero. A physical angle of a half turn also conserves CP in the Lagrangian, so the imported bound does not exclude it; whether it is excluded is a statement about the hadron spectrum that is model-dependent in the source read and is not imported (Fact \claimref{synthesis.imported-physical-colour-angle-and-its-shift-under-quark-rephasing}(iv)).

\emph{Why it is registered: what is proved and what is argued.} Three stored statements together say that the series does not fix $\bar\theta$. (1) \emph{The coefficient.} None of the stored maps examined fixes $\theta$: the stored CPT conjugation fixes $\Theta(F)$ in both of its conventions, on the hypothesis that it acts on the colour index by an automorphism or anti-automorphism of $\su(3)$, which the store does not state; the reversal to the mirror carries the term up to the sign of the identification of the two orientations; and the further stored maps listed there fix it (Theorem \claimref{synthesis.colour-angle-term-under-the-stored-maps-and-no-colour-anomalous-phase-of-the-rung-coupling}(i) to (iii), proved; its Reading (a), argued, over a named list of maps that is not a search of the store). (2) \emph{The mass phase.} Off the balanced frame the covariant completion is a bijection onto pairs of mass matrices, so $\theta_{M}$ takes every value at fixed masses and mixing: no stored statement about masses and mixing fixes it (Theorem \claimref{synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion}(i), proved). The readings on which the determinant is real are closed by stored data or are not available for the symmetric family matrices, except one texture that is not a stored structure (ibid.\ (iii), (iv); Conjecture \claimref{synthesis.exact-quarter-turn-texture-of-the-quark-stages}). (3) \emph{No relaxation.} On the covariant rung coupling with both family matrices invertible, and with no further field of the doublets' gauge charges and no further coloured fermion, every phase symmetry has colour coefficient $0$, so none shifts $\theta$; the neutral normal pair is massive and has no shift symmetry (Theorem \claimref{synthesis.colour-angle-term-under-the-stored-maps-and-no-colour-anomalous-phase-of-the-rung-coupling}(iv) to (viii), proved for that coupling). That no stored field relaxes the angle is argued from this over the rung field's components; the list of stored fields is not shown complete (its Reading (c)). So: that the stored structures leave $\bar\theta$ free is proved for the covariant rung coupling and for the maps examined, and argued for the store as a whole. The registration is the maintainer's decision of 16 November 2026 on that basis; it is a premise and is not derived.

\emph{Scope.} The premise registers one number, for this tower. Its relation to the mirror's angle is Premise \claimref{synthesis.common-ceiling-coupling-premise} read for the angle and the family matrices, not this premise: that premise equates the two towers' angles only up to the sign of the identification of the two orientations, $+$ for the stored reversal (Theorem \claimref{synthesis.colour-angle-term-under-the-stored-maps-and-no-colour-anomalous-phase-of-the-rung-coupling}(iii)), and which identification it is read with is an open item, not decided here. The angle is a parameter of the laws and not configuration data: the stored conjugation, which exchanges the two flag signs, fixes the term (on its hypothesis), so the angle is not exchanged with the flag and does not tell the two signs apart. It is not the only parity- and time-odd parameter of the stored laws: the up-down stage phase that the store selects from the data (\claimref{synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase}) is another, so the flag is not the one CP-odd datum (Reading (b) of the first Theorem, argued). The angle that Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}(ii) excludes, by the same bound, as a source of the matter asymmetry is this one; that clause left open an angle that relaxes or rolls, and, argued from (3), no field among the rung field's components supplies one.

\emph{What it does not give.} It does not say why the angle is small. It registers the sum only: $\theta$ and $\theta_{M}$ are not separately physical and neither is registered. It says nothing of the angle of the weak gauge field. It does not decide between a physical angle near zero and one near a half turn beyond what the record does. It does not answer how the stored CPT conjugation acts on the gauge sector, which Premise \claimref{dark-matter.premise-cpt-covariance} leaves premised and unstated.

\emph{Refutation condition.} The premise is false if a stored result fixes $\bar\theta$ from the series' premises, at zero or at any other value, with the mass phase included; if a stored field is shown to relax it, that is, a phase symmetry of the stored couplings with nonzero colour coefficient, which on the covariant rung coupling requires $\det(aY + b\tilde{Y})$ to be a single monomial $c\,a^{j}b^{n-j}$ with $2j \neq n$ (ibid.\ (v)), or a further field outside the hypothesis of (3); or if $\bar\theta$ is shown to be a function of another registered number. A result that fixes $\theta$ alone or $\theta_{M}$ alone does not meet the first condition: the tree-level texture of the conjecture cited above would fix $\theta_{M}$ at zero or a half turn and leave $\theta$, and so $\bar\theta$, free. A measured neutron dipole moment that fixes a nonzero value of the angle does not refute the premise; it measures the registered number.

## technical
The strong interaction admits a term whose coefficient is an angle, and the physical angle is that coefficient plus the phase of the determinant of the quark mass matrices; only the sum is physical, since a rephasing of the quarks moves one part into the other. The record bounds it near zero at about $2 \times 10^{-10}$ through the neutron's electric dipole moment. This premise registers the physical angle as a free input of the series, beside $N$, the D-term level and the matter asymmetry. The stored results support the registration in three parts. The stored maps that were examined, among them the series' CPT conjugation (on a hypothesis about its action on colour that the store does not state) and the reversal to the mirror, do not fix the coefficient. The covariant coupling of the rung field leaves the pair of quark mass matrices unconstrained, so the phase of the determinant is free at fixed masses and mixing. And that coupling, with both family matrices invertible, has no phase symmetry with a colour coefficient, so nothing among the rung field's components relaxes the angle as an axion would. The first and third are proved for the named maps and for that coupling and argued for the store as a whole. The premise is refuted by a stored derivation of the physical angle, by a stored field that relaxes it, or by showing it to be a function of another registered number. It does not explain the smallness of the angle, and it registers neither part of the sum separately. The mirror's angle equals this one only by the common-ceiling coupling premise, and then up to a sign that depends on how the two orientations are identified.

## lay
The strong force could treat matter and antimatter differently, by an amount set by one angle. Experiments on the neutron show that this angle is smaller than about one part in ten billion, and no one knows why. This framework does not explain it either. The results it holds show that its own symmetries, among those examined, do not force the angle to vanish, that its description of quark masses leaves the relevant phase free, and that the field which gives quarks their masses has no symmetry that would let the angle relax to zero. So the angle is recorded here as one of the basic numbers put in by hand, with its measured upper limit. The entry would be overturned if a calculation within the framework fixed the angle, or if a field were found in it that drives the angle to zero.

## one-liner
Premise ($\bar\theta$): the physical colour angle $\bar\theta = \theta + \theta_{M}$, the coefficient of the colour four-form plus the $I_{4}$ phase of $\det M_{u}\det M_{d}$, is a registered free input, not computed from the structure, from another premise or from a dynamics, and not a function of $N$, $\xi G$ or $\epsilon$; the record bounds it near zero at about $2 \times 10^{-10}$ (a half turn is not excluded by the imported bound); that the stored structures leave it free is proved for the covariant rung coupling and the maps examined and argued for the store; refuted by a stored result that fixes it with the mass phase included, by a stored field that relaxes it, or by showing it a function of another registered number.
