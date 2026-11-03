---
id: synthesis.de-sitter-temperature-frozen-point-norm
kind: claim
version: 5
title: The cosmological horizon's descent temperature is the frozen point's norm over 2 pi
status: proved
region: synthesis
subject: thermality
tags: [hawking-temperature, frozen-point, modular-theory, horizons]
proposed_by:
  kind: ai
  session: synthesis-bridges-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.cosmological-horizon-boundary-modes
derivations:
- name: main
  uses:
  - synthesis.cosmological-horizon-completed-pair@3
  - synthesis.de-sitter-static-boost-frozen-point@5
  - singularity.ascended-marginals-are-diagonal@5
  - singularity.descended-form-state-independent@4
  - singularity.kms-uniqueness-factor@4
  assumes:
  - singularity.p-univalence@2
  - synthesis.r-lambda-regularity-cosmological-horizon@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_de_sitter_temperature
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.modular-descent
  - singularity.rate-discharge-hypothesis-iii
  - singularity.euclidean-section-period
  - mass.de-sitter-scale-frozen-point
  - standard-model.what
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  flow_note: phase flow e^{-i omega_j t} on the modes (the T05 Thm 7.16 sense); the period is converted at the rate of the rotor flow exp(t B_Lambda / 2).
  premise_scope: (P) is T05's premise for its boundary modes and is applied here beyond that scope, to the cosmological horizon's modes; it is the univalence superselection rule (singularity.imported-univalence-superselection-rule), which holds for any Z2-graded field algebra. A separate (P_Lambda) would make the transplant explicit, as (R_Lambda) does for (R).
  candour_note: As in T05, the thermality is the KMS algebra of one CAR mode under a premise that stipulates KMS at the geometric period; what is new is that the cosmological horizon now has the mode algebra on which that premise can be stated, its rate is the frozen point's norm, and the mirror's pair is the same with the ladder reversed.
  conjecture_history: Proposed on 21 October 2026 as a conjecture, since the series built no boundary-mode algebra for the cosmological horizon and (R) was stated for the Schwarzschild modes only. At Leon's request the algebra was built (synthesis.cosmological-horizon-completed-pair, obj.synthesis.cosmological-horizon-boundary-modes) and (R) transplanted as the premise synthesis.r-lambda-regularity-cosmological-horizon; the conjecture's conditional is now a theorem under (P) and (R_Lambda). The conjectured statement is kept below as source_formal.
  source_formal: 'Conjecture. If the boundary modes of the cosmological horizon carry a completed pair in the boost plane of the bifurcation sphere satisfying hypotheses (i) to (iii) of Theorem singularity.modular-descent, and if premise (R) is transplanted to that horizon, then the descended state is thermal in static time at T_Lambda = kappa_Lambda / 2 pi = sqrt(<I,I>) / 2 pi, with (a) beta H = 2 pi, (b) the same temperature for this world and the mirror, (c) T_Lambda undetermined within the series exactly as Lambda is.'
---

## formal
Let $\Lambda = 3H^{2} > 0$ and fix a static observer. Assume (P) (Premise \claimref{singularity.p-univalence}) for the boundary modes of the cosmological horizon (Definition \claimref{obj.synthesis.cosmological-horizon-boundary-modes}) and (R$_{\Lambda}$) (Premise \claimref{synthesis.r-lambda-regularity-cosmological-horizon}). Then at every mode $j$ the marginal is the Gibbs state of $K_{j}$ at one and the same inverse temperature in static Killing time,
\[
\beta \;=\; \frac{2\pi}{\kappa_{\Lambda}} \;=\; \frac{2\pi}{\sqrt{Q(I_{\Lambda})}} , \qquad
T_{\Lambda} \;=\; \frac{\kappa_{\Lambda}}{2\pi} \;=\; \frac{\sqrt{Q(I_{\Lambda})}}{2\pi} \;=\; \frac{1}{2\pi}\sqrt{\frac{\Lambda}{3}} ,
\]
the Gibbons-Hawking temperature \cite{GibbonsHawking1977cosmo}, with occupancy $\omega(v_{j}^{*}v_{j}) = (e^{\beta\omega_{j}} + 1)^{-1} \in (0,1)$. Every marginal is faithful, so hypothesis (iii) of Theorem \claimref{singularity.modular-descent} holds at this horizon as a consequence, and the temperature is the same at every mode with no condition on the joint state. In Hubble-normalised time the inverse temperature is $\beta H = 2\pi$ exactly. What follows for the mirror and for the status of $T_{\Lambda}$ is Corollary \claimref{synthesis.de-sitter-temperature-mirror-and-status}.

## technical
The singularity paper derives the Hawking temperature from its boundary modes under two premises: physical states are even (P), and each mode is KMS at the period the smooth Euclidean section needs (R). The same argument now runs at the cosmological horizon, because that horizon has a completed pair supplied by the static observer's geometry and a boundary-mode algebra built from copies of it. Assume (P) for these modes and the transplanted premise (R$_{\Lambda}$). Then every mode is thermal at $T_{\Lambda} = \kappa_{\Lambda}/2\pi = \sqrt{\Lambda/3}/2\pi$, the Gibbons-Hawking temperature, with Fermi-Dirac occupancy, and the same temperature holds at every mode whatever the joint state. The surface gravity here is the square root of the frozen point's norm.

In Hubble units the inverse temperature is exactly $2\pi$. The mirror's horizon temperature, and the sense in which the temperature is undetermined, are a separate corollary.

## lay
A universe with a positive cosmological constant gives every observer a horizon, and by the standard argument that horizon glows at a definite, extremely low temperature. The series derives the black-hole version of that glow from its own algebra, given one smoothness assumption. With the horizon's quantum modes now built, the same derivation works here under the same kind of assumption and gives the standard value, set by the cosmological constant. The number that fixes it is the length of the series' frozen point, the same quantity that carries the cosmological constant. So the series recovers the temperature's form, and its size is set by the same number as the cosmological constant.

## one-liner
Under (P) and (R$_{\Lambda}$), every boundary mode of the cosmological horizon is thermal at $T_{\Lambda} = \sqrt{Q(I_{\Lambda})}/2\pi = \sqrt{\Lambda/3}/2\pi$, with $\beta H = 2\pi$.
