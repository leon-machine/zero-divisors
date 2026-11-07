---
id: neutrino.imported-mass-bracket-quantum-numbers
kind: claim
version: 5
title: 'Imported: the mass bracket and its quantum numbers'
status: proved
region: neutrino
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
  source: authorship disclosure of T15, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.imported-face-valued-bracket-quantum-numbers@5
  - mass.mass-symplectic-area-two-twistor-formula@3
  - neutrino.imported-derived-content-singlets@8
  - standard-model.internal-symmetry-ladder@4
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
- kind: check
  ref: check.py::check_single_spinor_sector_hypercharge
locators:
  paper: T15
  number: Fact 2.2
  label: fact:bracket
  line: 558
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: neutrino.imported-derived-content-singlets repinned 7 -> 8 after reviewing its G3 restatement (Hypothesis (S) is now derived in the store from the slot-module premise, where it was called open; the derived content is unchanged); the use here holds as cited.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: m^2 = 2|<pi1 pi2>|^2, the det(U) law, the single-spinor hypercharges -k/3, and the bracket''s Y = 1/2 + 1/2 = 1 singlet quantum numbers on the five-mode module. Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  env: fact
  context_refs:
  - families.imported-face-valued-bracket-quantum-numbers
  - mass.mass-symplectic-area-two-twistor-formula
  - neutrino.imported-derived-content-singlets
  - standard-model.internal-symmetry-ladder
  - standard-model.mass-bracket-charged-singlet
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - neutrino.imported-derived-content-singlets
    note: 'The quantum numbers are stated with the hypercharge and Hypothesis (S) states of the derived-content
      Fact, so that context_ref was added; the remaining uses are the cited sources and are kept. Levels
      pass: the lay level said the bracket has the charges of the right-handed electron, a sign error
      (that field has $Y = -1$), and now says $e^{c}$ with $Y = +1$; it also gains Hypothesis (S), the
      flat-space qualifier and the observation-level status of the order-parameter reading, and the one-liner
      gains (S).'
  source_title: 'Imported: the mass bracket and its quantum numbers'
  source_formal: |-
    A massive matter unit is a two-twistor composite whose flat mass is the bracket, $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ at $\Lambda = 0$. The bracket transforms by $\det(U)$ under the internal $U(2)$, and under the global form with the hypercharge of Fact \claimref{neutrino.imported-derived-content-singlets} the bracket of two twistors, each the vacuum of its pair system, transforms as $(1,1)$ with $Y = +1$: the quantum numbers of $e^{c}$, and not those of a weak doublet. The constituents there are slot-occupying states (that paper's $(1,0)$ components, which exist in its state space under Hypothesis (S), each of hypercharge $+\tfrac12$, so that the $+1$ is their sum; the slot arithmetic $\lambda^{3}$ per slot is unconditional in the global form), not the slot-free grade-zero state this paper calls the empty twistor; the bracket is defined on such twistors, is computed there only for that case, is not defined for an excited composite, and says nothing, either way, about a bilinear of two grade-zero states. The relation between this object and the Standard Model's order parameter is not settled in the series, and the reading of the bracket as an order parameter is recorded at observation level only. \emph{Provenance:} \cite[Props.~3.1-3.2]{ButlerT12}; \cite[Prop.~4.1]{ButlerT11}; the form of this Fact is the families paper's \cite[Fact~2.1]{ButlerT13}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The constituents, the bracket''s domain and the empty state are now named by conformal spinors in all levels and the restated proof; the paper''s name ''empty twistor'' is kept once as an aside, since a Proposition of that name is cited elsewhere.'
---

## formal
A massive matter unit is a composite of two conformal spinors (twistors) whose flat mass is the bracket, $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ at $\Lambda = 0$. The bracket transforms by $\det(U)$ under the internal $U(2)$, and under the global form with the hypercharge of Fact \claimref{neutrino.imported-derived-content-singlets} the bracket of two conformal spinors, each the vacuum of its pair system, transforms as $(1,1)$ with $Y = +1$: the quantum numbers of $e^{c}$, and not those of a weak doublet. The constituents there are slot-occupying states (that paper's $(1,0)$ components, which exist in its state space under Hypothesis (S), each of hypercharge $+\tfrac12$, so that the $+1$ is their sum; the slot arithmetic $\lambda^{3}$ per slot is unconditional in the global form), not the slot-free grade-zero state, the empty conformal spinor (this paper's empty twistor); the bracket is defined on such conformal spinors, is computed there only for that case, is not defined for an excited composite, and says nothing, either way, about a bilinear of two grade-zero states. The relation between this object and the Standard Model's order parameter is not settled in the series, and the reading of the bracket as an order parameter is recorded at observation level only. \emph{Provenance:} \cite[Props.~3.1-3.2]{ButlerT12}; \cite[Prop.~4.1]{ButlerT11}; the form of this Fact is the families paper's \cite[Fact~2.1]{ButlerT13}.

## technical
A massive matter unit is a composite of two conformal spinors with flat mass $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ at $\Lambda = 0$. The bracket transforms by $\det(U)$ under the internal $U(2)$, and under the global form with the series' hypercharge the bracket of two conformal spinors, each the vacuum of its pair system, transforms as $(1,1)$ with $Y = +1$: the quantum numbers of $e^{c}$, not those of a weak doublet.

The constituents are slot-occupying states, each of hypercharge $+\tfrac12$, which exist under Hypothesis (S); they are not the slot-free grade-zero empty conformal spinor. The bracket is computed only for that case, is not defined for an excited composite, and says nothing about a bilinear of two grade-zero states. Its relation to the Standard Model's order parameter is not settled, and reading it as an order parameter is an observation only.

## lay
In flat space the mass of a particle made of two conformal spinors is carried by one complex number, the bracket. Under the framework's symmetries it has the charges of $e^{c}$, the charge-conjugate partner of the right-handed electron, with hypercharge $+1$, rather than those of the Higgs doublet. This holds for constituents that occupy slots, states which exist under Hypothesis (S), and this version states exactly which constituent states the result covers, so that it is not stretched to states where the bracket is not defined. Reading the bracket as the Standard Model's order parameter is an observation only.

## one-liner
The bracket of two vacuum conformal spinors transforms by $\det(U)$ and has the $e^{c}$ quantum numbers $(1,1)$ with $Y = +1$, for slot-occupying constituents only, which exist under Hypothesis (S).
