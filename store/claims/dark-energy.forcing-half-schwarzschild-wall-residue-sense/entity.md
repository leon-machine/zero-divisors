---
id: dark-energy.forcing-half-schwarzschild-wall-residue-sense
kind: claim
version: 4
title: The forcing half at the Schwarzschild wall, in the residue sense
status: proved
region: dark-energy
subject: dark-energy
tags: [schwarzschild, kasner, curvature-and-field-equations, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-datum-kasner-wall@8
  - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching@5
  - sheaf.matching-connection-level@8
  - sheaf.matching-fibre@5
  - sheaf.weights-are-forced-are-kasner-exponents@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_simple_pole_with_kasner_residue
- kind: check
  ref: check.py::check_residues_satisfy_the_field_equations
- kind: check
  ref: check.py::check_residues_are_the_completion_weights
locators:
  paper: T10
  number: Asm 4.10
  label: asm:forcing
  line: 921
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Kasner gauge field on flat spacetime: simple pole of Omega with residue p_i e_i^e_0; Ricci-flat exactly on the Kasner circle among a grid of triples; unit-boost residue; weights (2/3)(-1/2,1,1) equal the exponents. Version 2 -> 3. Fix round: check_residues_are_the_completion_weights computes the weights (-1/2, 1, 1) from the Schwarzschild interior coframe and converts them to (-1/3, 2/3, 2/3) with the exact proper-time series. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - dark-energy.frozen-point-datum-kasner-wall
    - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
    - sheaf.matching-connection-level
    - sheaf.matching-fibre
    - sheaf.weights-are-forced-are-kasner-exponents
    note: 'Took as premises the results cited in the three steps; the cosmological-constant, counterterm
      and variable-exponent results discharge qualifications after the assembly and were left out as premises.
      Levels pass: lay and one-liner now say leading-order field equations and residue sense, and that
      the momentum constraints and non-diagonal class remain open.'
  env: assembly
  context_refs:
  - dark-energy.cosmological-constant-does-not-change-residue
  - dark-energy.frozen-point-datum-kasner-wall
  - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
  - dark-energy.variable-exponents-residue-pointwise-corrections-are
  - dark-energy.wall-counterterm
  - sheaf.matching-connection-level
  - sheaf.matching-fibre
  - sheaf.weights-are-forced-are-kasner-exponents
  outside_pilot_cites:
  - ButlerT4
  flags:
  - no proof environment found
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (light): the Schwarzschild singularity named as the singular locus r = 0 of the Schwarzschild field on flat spacetime, and the connection whose pole is computed as the rotation-gauge field. Steps 1-3 and the qualifications unchanged. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged.'
---

## formal
The steps, each with its provenance:
\begin{enumerate}
\item \emph{(The datum's pole.)} At the singular locus $r = 0$ of the Schwarzschild gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) the frozen-point datum is regular in the exceptional chart except for a simple pole of the connection in its Levi-Civita block, the rotation-gauge field $\Omega$, with tangential legs, residue $-\sum_i p_iB_i\otimes\hat e^i$ (the sign of the Definition): Proposition \claimref{dark-energy.frozen-point-datum-kasner-wall}(i) on the Kasner model, transported to Schwarzschild by Fact \claimref{dark-energy.imported-weighted-limit-schwarzschild-singularity-matching} (the geometry paper's weighted limit, values-level, with its $O(\tau^{2/3})$ corrections in the boost block and $O(\tau^{1/3})$ in the rotation block).
\item \emph{(The residues satisfy the wall's field equations.)} The exponents obey the Kasner relations, which are the leading-order field equations, and the second relation is the statement that the residue bivector is a unit boost: Proposition \claimref{dark-energy.frozen-point-datum-kasner-wall}(ii), \cite[Prop.~8.26(3)]{ButlerT4}.
\item \emph{(The residues are the completion's weights.)} The sheaf paper's completion at this wall is built on weights that are forced, once the dying direction is named, to equal the Kasner exponents: \cite[Thm.~8.16]{ButlerT4}; and its exceptional frame is the frame in which (1) holds: \cite[Thm.~8.27]{ButlerT4}.
\end{enumerate}
Consequently, at this wall, the field equations neither merely permit the completion nor demand it as a further condition: their own singular locus supplies the data the completion is built from. The pole of the dynamical connection is not removable (step 1), its residues are fixed by the equations (step 2), and those residues are the weights of the completion (step 3). This is the forcing half of Section \ref{sec:vacate} answered in the residue sense. Three qualifications are discharged below: the cosmological corrections leave the residue unchanged (Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue}); the divergent curvature-squared \emph{value} is removed by a local wall counterterm that does not change the equations (Proposition \claimref{dark-energy.wall-counterterm}); and the residue statement holds pointwise for variable exponents in the diagonal class (Lemma \claimref{dark-energy.variable-exponents-residue-pointwise-corrections-are}), with the momentum constraints and the non-diagonal class remaining as the dynamical half of the sheaf paper's connection-level matching \cite[Rem.~8.28]{ButlerT4}.

## technical
At the singular locus of the Schwarzschild field on flat spacetime the frozen-point datum is regular in the exceptional chart except for a simple pole of the connection's Levi-Civita block, the rotation-gauge field, with tangential legs, of residue $-\sum_i p_i B_i\otimes\hat e^i$ with $B_i = e_0\wedge e_i$: this is the Kasner computation, transported to Schwarzschild by the weighted limit at values level. The exponents obey the Kasner relations $\sum_i p_i = 1 = \sum_i p_i^2$, which are the leading-order field equations, and the second relation says that the residue bivector is a unit boost. The weights of the sheaf completion at this wall are forced to equal the Kasner exponents, and its exceptional frame is the frame in which the pole is computed.

Together: the pole is not removable, its residues are fixed by the field equations, and those residues are the weights of the completion. So at this wall the equations' own singular locus supplies the data the completion is built from, which answers the forcing question in the residue sense; the momentum constraints and the non-diagonal class remain as the dynamical half of the connection-level matching.

## lay
Near the central singularity of a black hole, Einstein's equations break down in a specific, structured way: one part of the gravitational field blows up like one over the time remaining, with coefficients that the leading-order equations themselves fix. Those coefficients turn out to be exactly the numbers on which the series' completion of the geometry at the singularity is built. So at this wall, in this residue sense, the equations do not merely tolerate the completion; they supply its ingredients. The dynamical half of the matching (the momentum constraints and the non-diagonal case) is left open.

## one-liner
At the Schwarzschild wall the leading-order field equations fix the residues of the connection's simple pole, and those residues are the forced weights of the sheaf completion, so in the residue sense the equations supply the completion's data, the momentum constraints and the non-diagonal class remaining open.
