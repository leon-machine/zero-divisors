---
id: hawking.helicity-lift-joints-itemised
kind: claim
version: 6
title: The helicity lift, with its joints itemised
status: proved
region: hawking
subject: thermality
tags: [conformal-spinors, ledger-audit]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
- name: Claude Opus 5.5
  role: restatement of Joint J3 to the narrowed premise, channel reduction assumed for spin 2 only
  version: 6
  source: maintainer pass of 2026-11-09
review: typed
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - hawking.imported-penrose-transform@3
  - hawking.imported-twistor-storey-ordering-shift@6
  - hawking.homogeneity-ordering-shift@6
  - hawking.imported-s-wave-bosonic-sector@6
  proof: proof-main.tex
  assumes:
  - hawking.joint-j3-s-wave-reduction@2
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_homogeneity_table
- kind: check
  ref: check.py::check_helicity_is_the_shifted_euler_charge
locators:
  paper: T07
  number: Asm 5.3
  label: asm:helicity
  line: 597
extraction:
  maintainer_pass_2026_11_09:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Version 5 -> 6. Joint J3 restated to match hawking.joint-j3-s-wave-reduction version 2 at the formal, technical, lay and one-liner levels and in the proof: the channel-reduction step is premise only for spin 2 (the graviton); for spins 0, 1/2 and 1 (the photon among them) it is derived at the horizon by synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional (cited in the text; no uses edge added); the current-boson identification and the partial-wave lift stay premise for every species. J1, J2, the homogeneity table and the check are unchanged; the assumes pin on J3 is left for the repin.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the homogeneity table h = -2s - 2 and q(id) = -(Upsilon + 2) on twistor monomials. Version 4 -> 5.'
  env: assembly
  context_refs:
  - hawking.homogeneity-ordering-shift
  - hawking.imported-penrose-transform
  - hawking.imported-s-wave-bosonic-sector
  - hawking.imported-twistor-storey-ordering-shift
  unresolved_refs:
  - rem:whichdynamics
  flags:
  - no proof environment found
  repair:
    notes:
    - 'assembly: no proof environment; the itemised statement is the derivation; non-theorem joint named
      as a postulate'
  typing:
    by: ai-typing-pass
    added:
    - hawking.imported-penrose-transform
    - hawking.imported-twistor-storey-ordering-shift
    - hawking.homogeneity-ordering-shift
    - hawking.imported-s-wave-bosonic-sector
    note: 'Added the premises of joints J1 and J2 (Penrose transform, twistor ordering shift, homogeneity
      proposition) and the s-wave bosonic sector whose current boson J3 lifts; the last is the least certain,
      since it enters through the modelling joint J3, already an assumes edge. Levels pass: conditions
      already kept.'
  source_title: 'The helicity lift, with its joints itemised'
  source_formal: |-
    Helicity is not additional structure imported into the framework: it is the eigenvalue of the distinguished $\mathfrak{u}(1)$ charge of the completion's twistor storey, and the four-dimensional mode space of each massless species has a canonical place in it. The joints, each with its provenance:
    \begin{enumerate}
    \item (\emph{Joint J1: the transform, classical.}) By Fact \claimref{hawking.imported-penrose-transform}, the helicity-$s$ mode space is the cohomology at homogeneity $-2s-2$; photon kinematics are at homogeneities $-4$ and $0$ ($s = \pm1$), graviton kinematics at $-6$ and $+2$ ($s = \pm2$).
    \item (\emph{Joint J2: the charge, proved in the series.}) The ordering shift is proved in the twistor paper (Fact \claimref{hawking.imported-twistor-storey-ordering-shift}), and Proposition \claimref{hawking.homogeneity-ordering-shift} derives the homogeneity $-2s-2$ from it: the classification parameter of Joint J1 is an internal charge of the completion, so the helicity ladder is part of the ascended kinematics rather than a phenomenological label.
    \item (\emph{Joint J3: the reduction, modelling.}) The current boson of the s-wave theory (Fact \claimref{hawking.imported-s-wave-bosonic-sector}) is the s-wave reduction of each such four-dimensional field, and the lift from the boundary modes to the field is the standard partial-wave reconstruction, each helicity sector identified through the transform of Joint J1: the near-horizon reduction of field theory on the Schwarzschild exterior identifies each $(\omega, \ell, m, s)$ channel with a two-dimensional mode, which is where Definition \claimref{obj.hawking.continuum-mode-space}'s modelling input enters, flagged as such in Remark \ref{rem:whichdynamics}.
    \end{enumerate}
    The composite statement is the conjunction of the three joints with the provenance displayed: J1 is classical, J2 is Fact \claimref{hawking.imported-twistor-storey-ordering-shift} together with Proposition \claimref{hawking.homogeneity-ordering-shift}, and J3 is the one modelling joint. The homogeneity table is checked by the script.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the twistor storey to the conformal storey ($\Cl(2,4)$ with its spinor space $\CS$) and the twistor cohomology to cohomology on $\PCS$, in every level and the proof. Kept the Penrose transform and Penrose homogeneity by name: Joint J1 is the classical holomorphic-cohomology statement, which TWGA does not recast beyond the spacetime kernels.'
---

## formal
Helicity is not additional structure imported into the framework: it is the eigenvalue of the distinguished $\mathfrak{u}(1)$ charge of the completion's conformal storey (the twistor storey: $\Cl(2,4)$ with its conformal spinor space $\CS$), and the four-dimensional mode space of each massless species has a canonical place in it. The joints, each with its provenance:
\begin{enumerate}
\item (\emph{Joint J1: the transform, classical.}) By Fact \claimref{hawking.imported-penrose-transform}, the helicity-$s$ mode space is the cohomology at homogeneity $-2s-2$; photon kinematics are at homogeneities $-4$ and $0$ ($s = \pm1$), graviton kinematics at $-6$ and $+2$ ($s = \pm2$).
\item (\emph{Joint J2: the charge, proved in the series.}) The ordering shift is proved in the correspondence paper (Fact \claimref{hawking.imported-twistor-storey-ordering-shift}), and Proposition \claimref{hawking.homogeneity-ordering-shift} derives the homogeneity $-2s-2$ from it: the classification parameter of Joint J1 is an internal charge of the completion, so the helicity ladder is part of the ascended kinematics rather than a phenomenological label.
\item (\emph{Joint J3: the reduction, modelling.}) The current boson of the s-wave theory (Fact \claimref{hawking.imported-s-wave-bosonic-sector}) is the s-wave reduction of each such four-dimensional field, and the lift from the boundary modes to the field is the standard partial-wave reconstruction, each helicity sector identified through the transform of Joint J1; and the near-horizon reduction of field theory on the Schwarzschild exterior identifies each $(\omega, \ell, m, s)$ channel with a two-dimensional mode, which is where Definition \claimref{obj.hawking.continuum-mode-space}'s modelling input enters, flagged as such in Remark \ref{rem:whichdynamics}. That channel reduction is premise only for the graviton (spin $2$); for the photon, and for scalar and Dirac fields, it is derived at the horizon (Theorem \claimref{synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional}). The current-boson identification and the lift stay premise for every species.
\end{enumerate}
The composite statement is the conjunction of the three joints with the provenance displayed: J1 is classical, J2 is Fact \claimref{hawking.imported-twistor-storey-ordering-shift} together with Proposition \claimref{hawking.homogeneity-ordering-shift}, and J3 is the one modelling joint. The homogeneity table is checked by the script.

## technical
Helicity is identified with the eigenvalue of the distinguished $\mathfrak{u}(1)$ charge of the completion's conformal storey, $\Cl(2,4)$ with its conformal spinor space $\CS$, through three joints. Joint J1 is classical: by the Penrose transform the helicity-$s$ mode space is the cohomology on the projective spinor space $\PCS$ at homogeneity $-2s-2$, so photons sit at homogeneities $-4$ and $0$ and gravitons at $-6$ and $+2$. Joint J2 is proved in the series: the symmetric-ordering shift of the conformal storey gives $q(\id) = -\hbar(\Upsilon + 2)$, which places helicity $s$ at homogeneity $-2s-2$.

Joint J3 is a modelling premise: the current boson of the s-wave theory is the s-wave reduction of each four-dimensional massless field, and the near-horizon reduction of field theory on the Schwarzschild exterior identifies each $(\omega, \ell, m, s)$ channel with a two-dimensional mode. The channel reduction is assumed only for the graviton: for the photon, and for scalar and Dirac fields, it is derived at the horizon in Gauge Theory Gravity (\claimref{synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional}); the identification of the current boson with these channels is assumed for every species. The composite statement is the conjunction of the three joints and holds under premise J3.

## lay
Massless particles such as photons and gravitons carry helicity, a measure of how they spin about their direction of motion. This result reads helicity as a charge already present at the framework's conformal level, the level whose spinors describe light rays, by combining a classical theorem of Penrose (his transform) with a calculation proved earlier in the series. Connecting it to the horizon modes relies on one modelling assumption: that the framework's horizon modes are the spherical-wave pieces of the four-dimensional fields. That the fields do break into such one-dimensional pieces near the horizon has been derived for light, and is still assumed for gravitational waves.

## one-liner
Under the modelling joint J3 (its channel reduction assumed for spin $2$ only, derived for lower spins), helicity is the eigenvalue of the conformal storey's distinguished $\mathfrak{u}(1)$ charge, with helicity $s$ at Penrose homogeneity $-2s-2$.
