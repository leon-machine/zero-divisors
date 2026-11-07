---
id: hawking.greybody-inheritance-under-interface-premise
kind: claim
version: 6
title: Greybody inheritance, under the interface premise
status: proved
region: hawking
subject: thermality
tags: [radiation-spectrum, recovers-known-physics]
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
review: typed
derivations:
- name: main
  uses:
  - hawking.imported-exterior-exactly-general-relativity@3
  - hawking.i-state-continuum@5
  - hawking.imported-s-wave-bosonic-sector@6
  - hawking.imported-modular-descent-premises-geometric-normalisation@7
  proof: proof-main.tex
  assumes:
  - hawking.premise-i-interface-identification@1
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_fermionic_occupancy_is_upper_sign
- kind: check
  ref: check.py::check_bosonic_occupancy_is_lower_sign
- kind: check
  ref: check.py::check_hawking_temperature_coefficient
locators:
  paper: T07
  number: Asm 5.4
  label: asm:greybody
  line: 609
extraction:
  maintainer_pass:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 5 -> 6. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: joint (ii): the fermionic occupancy n_+ from the window symbol, the bosonic n_- from the current sums, their relation, and the T_H coefficient. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  env: assembly
  context_refs:
  - hawking.i-state-continuum
  - hawking.imported-exterior-exactly-general-relativity
  - hawking.imported-modular-descent-premises-geometric-normalisation
  - hawking.imported-s-wave-bosonic-sector
  flags:
  - no proof environment found
  repair:
    notes:
    - 'assembly: no proof environment; the itemised statement is the derivation; non-theorem joint named
      as a postulate'
  typing:
    by: ai-typing-pass
    added:
    - hawking.imported-exterior-exactly-general-relativity
    - hawking.i-state-continuum
    - hawking.imported-s-wave-bosonic-sector
    - hawking.imported-modular-descent-premises-geometric-normalisation
    note: 'Added the four joints the assembly names as premises (exterior exactness, continuum I-state,
      (Q)-conditional bosonic sector, geometric normalisation); the paper says the flux equals Hawking''s,
      but Hawking''s and Page''s results are not in the store as imported claims, so no standard-route
      derivation was added. Levels pass: lay now names premises (I) and (Q).'
---

## formal
\emph{Premise (I), the interface identification:} the horizon-sector state feeds the exterior modes in the standard way, i.e.\ the occupancy of each near-horizon channel is carried to the corresponding asymptotic channel by the exterior propagation. This is the same assumption every derivation of Hawking flux makes, from \cite{Hawking1975} onward, and it is this assembly's one non-theorem joint. Under (I), the emitted flux in each channel $(\omega, \ell, m, s)$ equals (with $\mathcal{N}$ the count of emitted quanta)
\[
\frac{d\mathcal{N}}{dt\,d\omega} \;=\; \frac{1}{2\pi}\,\Gamma_{s\ell m}(\omega)\; n_\pm(\omega), \qquad
n_\pm(\omega) = \frac{1}{e^{\omega/\TH} \pm 1}
\]
(the upper sign for the fermionic species, the lower for the bosonic sector), with $\Gamma_{s\ell m}$ the classical transmission coefficient through the Regge-Wheeler or Teukolsky barrier. The joints: (i) the barriers and their transmission coefficients are properties of the exterior metric, and by Fact \claimref{hawking.imported-exterior-exactly-general-relativity} the framework's exterior description \emph{is} classical general relativity on the invertible region, exactly and not asymptotically, so $\Gamma_{s\ell m}$ is inherited verbatim, mode by mode \cite{ReggeWheeler1957, Teukolsky1973}; (ii) the occupancies at the horizon are Theorem \claimref{hawking.i-state-continuum} for the fermionic species and Fact \claimref{hawking.imported-s-wave-bosonic-sector}'s (Q)-conditional half for the bosonic sector, both at exactly $\TH$ with the temperature's coefficient fixed geometrically (Fact \claimref{hawking.imported-modular-descent-premises-geometric-normalisation}); (iii) given (I), the displayed formula is the definition of filtered thermal flux: the framework's flux prediction equals Hawking's \cite{Hawking1975, Page1976}, greybody structure included.

## technical
Under premise (I), that the occupancy of each near-horizon channel is carried by the exterior propagation to the corresponding asymptotic channel, the emitted flux in each channel $(\omega, \ell, m, s)$ is $d\mathcal{N}/(dt\,d\omega) = \tfrac{1}{2\pi}\Gamma_{s\ell m}(\omega)\,n_{\pm}(\omega)$ with $n_{\pm}(\omega) = 1/(e^{\omega/\TH} \pm 1)$, the upper sign for fermionic species and the lower for the bosonic sector, and $\Gamma_{s\ell m}$ the classical transmission coefficient through the Regge-Wheeler or Teukolsky barrier.

The joints: the transmission coefficients are inherited verbatim, because the framework's exterior description is classical general relativity on the invertible region; the horizon occupancies are the continuum I-state for the fermions and, conditional on premise (Q), the bosonic sector, both at $\TH$ with the coefficient of the temperature fixed geometrically; and, given (I), the displayed formula is the definition of filtered thermal flux, so the framework's flux prediction equals Hawking's, greybody structure included.

## lay
Radiation leaving a black hole is thermal at the horizon, but part of it is scattered back by the black hole's gravitational field outside the horizon, so what reaches a distant observer is filtered. This result combines the framework's thermal horizon state with the ordinary general-relativistic filtering, under the interface premise (I), that what is emitted near the horizon is carried outward in the standard way. For the boson-like part it also relies on a further premise, (Q), about the joint state of the modes. The outcome is the usual Hawking spectrum, including its filtering factors.

## one-liner
Under the interface premise (I), and premise (Q) for the bosonic sector, the framework's emitted flux in each channel is $\tfrac{1}{2\pi}\Gamma_{s\ell m}(\omega)\,n_{\pm}(\omega)$ at $\TH$, Hawking's greybody-filtered spectrum.
