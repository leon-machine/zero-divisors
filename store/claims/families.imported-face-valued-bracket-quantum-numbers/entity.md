---
id: families.imported-face-valued-bracket-quantum-numbers
kind: claim
version: 5
title: 'Imported: the face-valued bracket and its quantum numbers'
status: proved
region: families
subject: mass
tags: [hypercharge-and-anomalies, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - mass.mass-symplectic-area-two-twistor-formula@3
  - standard-model.internal-symmetry-ladder@3
  - standard-model.mass-bracket-charged-singlet@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_two_spinor_mass_is_twice_squared_bracket
- kind: check
  ref: check.py::check_bracket_transforms_by_the_determinant
- kind: check
  ref: check.py::check_bracket_carries_the_quantum_numbers_of_ec
locators:
  paper: T13
  number: Fact 2.1
  label: fact:bracket
  line: 577
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: m^2 = 2|<pi1 pi2>|^2 for Gaussian-rational spinors, the det(U) law under unitary mixing, and the (1,1), Y = +1 quantum numbers of the bracket on the five-mode module. Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  env: fact
  context_refs:
  - mass.mass-symplectic-area-two-twistor-formula
  - standard-model.gauge-algebra-minimal-massive-composite
  - standard-model.internal-symmetry-ladder
  - standard-model.mass-bracket-charged-singlet
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.gauge-algebra-minimal-massive-composite
    note: 'The gauge-algebra theorem is named only as presupposing the three-twistor bound, not as a source
      of this Fact; the bound itself comes from a remark of the Standard-Model paper that is not in the
      store. Levels pass: corrected the lay level''s sign error (the bracket carries the quantum numbers
      of $e^{c}$, hypercharge $+1$, not of the right-handed electron, hypercharge $-1$; review item 4),
      added the flat-space qualifier and kept the observation level of the order-parameter reading.'
  source_title: 'Imported: the face-valued bracket and its quantum numbers'
  source_formal: |-
    A massive matter unit is a two-twistor composite whose flat mass is the bracket, $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ at $\Lambda = 0$. A fundamental matter unit is built of up to three twistors, each the vacuum of three pairs; the three-twistor composite is the maximal one, and the Standard-Model paper states the bound at observation level, which is the level it has here. The mass bracket transforms by $\det(U)$ under the internal $U(2)$, an $SU(2)$ singlet with charge one under the determinant character, its modulus the mass and its phase pure gauge. Under the global form $S(U(2) \times U(3))$ with the hypercharge of the Standard-Model paper it transforms as $(1,1)$ with $Y = +1$: the quantum numbers of $e^{c}$, and not those of a weak doublet. The relation between this object and the Standard Model's order parameter, an $SU(2)$ doublet of hypercharge one half, is not settled in the series, and the reading of the bracket as an order parameter is recorded at observation level only. \emph{Provenance:} \cite[Prop.~4.1]{ButlerT11}; \cite[Rem.~3.3]{ButlerT12} for the three-twistor bound, at the observation level that remark declares (Thm.~4.1 there presupposes it in naming the maximal hierarchy); \cite[Props.~3.1-3.2]{ButlerT12} for the transformation law and the quantum numbers, with the level of the order-parameter sentence as stated there.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The matter units are now composites of conformal spinors (two-spinor composite, three-spinor bound) in the statement and its restated proof; the paper''s three-twistor bound is now called the three-spinor bound, with its T12 citation unchanged.'
---

## formal
A massive matter unit is a composite of two conformal spinors (twistors) whose flat mass is the bracket, $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ at $\Lambda = 0$. A fundamental matter unit is built of up to three conformal spinors, each the vacuum of three pairs; the three-spinor composite is the maximal one, and the Standard-Model paper states the bound at observation level, which is the level it has here. The mass bracket transforms by $\det(U)$ under the internal $U(2)$, an $SU(2)$ singlet with charge one under the determinant character, its modulus the mass and its phase pure gauge. Under the global form $S(U(2) \times U(3))$ with the hypercharge of the Standard-Model paper it transforms as $(1,1)$ with $Y = +1$: the quantum numbers of $e^{c}$, and not those of a weak doublet. The relation between this object and the Standard Model's order parameter, an $SU(2)$ doublet of hypercharge one half, is not settled in the series, and the reading of the bracket as an order parameter is recorded at observation level only. \emph{Provenance:} \cite[Prop.~4.1]{ButlerT11}; \cite[Rem.~3.3]{ButlerT12} for the three-spinor bound, at the observation level that remark declares (Thm.~4.1 there presupposes it in naming the maximal hierarchy); \cite[Props.~3.1-3.2]{ButlerT12} for the transformation law and the quantum numbers, with the level of the order-parameter sentence as stated there.

## technical
A massive matter unit is a two-spinor composite with flat mass $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ at $\Lambda = 0$; a fundamental unit has up to three conformal spinors, each the vacuum of three pairs, and the three-spinor bound holds at observation level only. Under the internal $U(2)$ the bracket transforms by $\det(U)$: it is an $SU(2)$ singlet of charge one under the determinant character, with modulus the mass and phase pure gauge.

Under the global form $S(U(2) \times U(3))$ with the series' hypercharge, the bracket transforms as $(1,1)$ with $Y = +1$, the quantum numbers of $e^{c}$ and not those of a weak doublet. Its relation to the Standard Model's order parameter, an $SU(2)$ doublet of hypercharge one half, is not settled, and reading the bracket as an order parameter is an observation only.

## lay
In this framework a particle with mass is built from two conformal spinors, and its mass in flat space is carried by one complex number, the bracket. This result records how that number behaves under the framework's internal symmetries: it has the charges of $e^{c}$, the conjugate of the right-handed electron, with hypercharge $+1$, not those of the Higgs doublet of the Standard Model. Whether it nonetheless plays a role like the Higgs field is left open, and that reading is held at observation level only.

## one-liner
The mass bracket transforms by $\det(U)$ under the internal $U(2)$ and carries the quantum numbers $(1,1)$ with $Y = +1$ of $e^{c}$, not those of a weak doublet.
