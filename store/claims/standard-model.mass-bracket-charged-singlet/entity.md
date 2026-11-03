---
id: standard-model.mass-bracket-charged-singlet
kind: claim
version: 4
title: The mass bracket is a charged singlet
status: proved
region: standard-model
subject: mass
tags: [hypercharge-and-anomalies, mass-generation, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - mass.mass-symplectic-area-two-twistor-formula@3
  - standard-model.global-form-quotient-determined@3
  - standard-model.imported-pair-systems-two-chirality-halves@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:prop:singlet
- kind: check
  ref: check.py::check_bracket_transforms_by_determinant
- kind: check
  ref: check.py::check_modulus_is_mass_phase_is_gauge
- kind: check
  ref: check.py::check_hypercharge_weight_six_singlet
locators:
  paper: T12
  number: Prop 3.2
  label: prop:singlet
  line: 951
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the bracket transforms by det U under 12 exact unitaries, modulus the mass and phase gauge, and abelian weight 6 (Y = +1) as an SU(2) x SU(3) singlet. Version 3 -> 4. Uses edge added (2026-10-23): standard-model.global-form-quotient-determined, whose parametrisation (lambda^3 a, lambda^-2 b) and hypercharge Y = q/6 the proof uses for Y = 6/6 = 1, now cited there.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Kept both edges, each cited in the proof; the global form and hypercharge sections the statement
      uses are cited only as sections, without a store label. Levels pass: lay said ''right-handed electron''
      (hypercharge -1); it now says e^c with hypercharge +1, as the formal does, and keeps the global-form
      condition.'
  source_title: 'The mass bracket is a charged singlet'
  source_formal: |-
    Under the $U(2)$ of the two-twistor step, the mass bracket transforms by the determinant:
    \[
    \br{\pi^{1}\pi^{2}} \mapsto \det(U) \cdot \br{\pi^{1}\pi^{2}}.
    \]
    It is therefore an $SU(2)$ singlet carrying charge one under the determinant character (charge two under the scalar phase $e^{i\theta}\,\id$, whose determinant is $e^{2i\theta}$): its modulus is the mass (Fact \claimref{mass.mass-symplectic-area-two-twistor-formula}), its phase is pure gauge under the $U(1)$, and it vanishes exactly on the massless locus. Under the global form of Section \ref{sec:algebra}, with the hypercharge of Section \ref{sec:content}, the bracket of two twistors, each the vacuum of its pair system, transforms as $(1, 1)$ with abelian weight $6$, hypercharge $Y = +1$: the quantum numbers of $e^{c}$, and not those of a weak doublet. (The bracket is defined on twistors; what it would be for an excited composite depends on the state space, and is not defined here.)
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The constituents and slots are now conformal spinors, and the scalar phase of the U(2) is written with the complex unit I6 of CS (e^{I6 theta}); the slot factor Lambda^2 C^2 and the Gaussian-rational checks are kept as written.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - mass.mass-symplectic-area-two-twistor-formula
    note: 'The proof and statement already cited the premise, but under the nonexistent id mass.mass-symplectic-area-two-spinor-formula; the id is corrected to the premise in uses, in the proof and in the formal statement.'
---

## formal
Under the $U(2)$ of the two-spinor step (two conformal spinors, mixed by their slot index), the mass bracket transforms by the determinant:
\[
\br{\pi^{1}\pi^{2}} \mapsto \det(U) \cdot \br{\pi^{1}\pi^{2}}.
\]
It is therefore an $SU(2)$ singlet carrying charge one under the determinant character (charge two under the scalar phase $e^{I_{6}\theta}\,\id$, whose determinant is $e^{2I_{6}\theta}$, with $I_{6}$ the complex unit of $\CS$): its modulus is the mass (Fact \claimref{mass.mass-symplectic-area-two-twistor-formula}), its phase is pure gauge under the $U(1)$, and it vanishes exactly on the massless locus. Under the global form of Section \ref{sec:algebra}, with the hypercharge of Section \ref{sec:content}, the bracket of two conformal spinors, each the vacuum of its pair system, transforms as $(1, 1)$ with abelian weight $6$, hypercharge $Y = +1$: the quantum numbers of $e^{c}$, and not those of a weak doublet. (The bracket is defined on conformal spinors; what it would be for an excited composite depends on the state space, and is not defined here.)

## technical
The mass bracket $\br{\pi^{1}\pi^{2}} = \det(\pi^{i}_{A})$ is the determinant of the spinor parts over the slot index, so a mixing $U$ in the $U(2)$ of the two-spinor step multiplies it by $\det(U)$. It is an $SU(2)$ singlet of charge one under the determinant character (charge two under the scalar phase $e^{I_{6}\theta}\,\id$, $I_{6}$ the complex unit); its modulus is the mass, its phase is pure gauge under the $U(1)$, and it vanishes exactly on the massless locus.

Under the paper's global form and hypercharge, the bracket of two conformal spinors, each the vacuum of its pair system, transforms as $(1, 1)$ with abelian weight $6$, so hypercharge $Y = +1$: the quantum numbers of $e^{c}$, not of a weak doublet. The bracket is defined on conformal spinors; for an excited composite it is not defined here.

## lay
For two conformal spinors, the series' mass is the size of a single complex number, the mass bracket. This result works out how that number changes under the internal symmetries of a system of two conformal spinors. It is unchanged by the $SU(2)$ part and only picks up a phase from the $U(1)$ part, so, with the paper's global form and hypercharge, it carries the charges of the conjugate electron field $e^{c}$, a weak singlet of hypercharge $+1$, rather than those of a weak doublet such as the Higgs.

## one-liner
The mass bracket transforms by $\det(U)$ under the two-spinor $U(2)$, making it an $SU(2)$ singlet of hypercharge $+1$ with the quantum numbers of $e^{c}$, not of a weak doublet.
