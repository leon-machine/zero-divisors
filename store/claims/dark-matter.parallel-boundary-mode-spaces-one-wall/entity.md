---
id: dark-matter.parallel-boundary-mode-spaces-one-wall
kind: claim
version: 5
title: 'Parallel boundary mode spaces at one wall: the infall computation'
status: proved
region: dark-matter
subject: dark-matter
tags: [boundary-modes, radiation-spectrum]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
about:
- obj.dark-matter.frozen-phase-operators
derivations:
- name: main
  uses:
  - dark-matter.imported-eight-towers-mod-8-clock@4
  - dark-matter.imported-schwinger-discharge-charged-hole@1
  - dark-matter.superselected-hence-dark-exactly-stable@5
  - hawking.greybody-inheritance-under-interface-premise@6
  assumes:
  - dark-matter.p1-single-frozen-point@1
  - dark-matter.p5-boundary-modes-hold-entropy-not@1
  - singularity.rate-models-kinematic-inputs-l-u@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:infall
- kind: check
  ref: check.py::check_information_is_cheap
- kind: check
  ref: check.py::check_schwinger_discharge_and_crossover
- kind: check
  ref: check.py::check_charge_is_expensive
locators:
  paper: T14
  number: Prop 6.5
  label: prop:infall
  line: 607
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: S_BH(solar) against the progenitor entropy; Schwinger Q_c, its ratio to extremal and the 1.3e5 solar-mass crossover; T_H(solar), m_p/T_H and the return fraction, exact with pi by Machin. Version 3 -> 4. Check strengthened: T_H, m_p/T_H, the most baryons emitted and the return fraction pinned to seven figures, which pins the 8 pi normalisation. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    removed:
    - dark-matter.stored-asymmetry-charge-not-number
    added:
    - hawking.greybody-inheritance-under-interface-premise
    - dark-matter.p1-single-frozen-point
    - dark-matter.p5-boundary-modes-hold-entropy-not
    note: 'Removed the stored-asymmetry edge, which the proof cites only to say this result is consistent
      with its no-production clause; added the greybody assembly that clause (i) runs tower by tower,
      and P1 and P5 as assumptions, since (i) is P1 and (iv) is P5. Levels pass: lay rewritten to keep
      P1, P5, the interface premise, the exhaustiveness premise and the observation level of the burst;
      technical and one-liner now carry the interface and exhaustiveness premises.'
  env: proposition
  outside_pilot_cites:
  - ButlerT5
  - ButlerT7
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - hawking.greybody-inheritance-under-interface-premise
---

## formal
Matter of any tower crossing this tower's horizon meets the shared singular locus, which degenerates every tower's algebra, so each tower ascends its own ladder there, parallel boundary mode spaces at one wall. The fate of what fell in, for all towers and holes (clause (iii) limited in mass):

(i) \emph{Energy:} its rest energy joins the one metric (P1) and is returned democratically as Hawking radiation into every populated tower, in proportion to each tower's light degrees of freedom once the temperature exceeds their gaps, because barriers, transmission coefficients and occupancies belong to the exterior metric, which does not record which tower the mass came from; this is P1 with Definition \claimref{obj.dark-matter.frozen-phase-operators} and the Hawking paper's greybody assembly under its interface premise, run tower by tower \cite[Assembly~5.4]{ButlerT7}. (ii) \emph{Information:} it ascends its own tower's boundary mode space and returns in its own tower's channel, at little entropy cost: a solar-mass hole's Bekenstein entropy is of order $10^{77}$ against its progenitor's $10^{58}$, so the singularity paper's deficit theorem and Page curve are untouched, tower by tower. (iii) \emph{Gauss-law charges,} for holes below about $1.3 \times 10^{5}$ solar masses, are returned per tower by that tower's own discharge (Fact \claimref{dark-matter.imported-schwinger-discharge-charged-hole}), at a cost of order the charge times the lightest charged mass, negligible against $M$; above that mass discharge does not limit the charge, and whether a supermassive hole returns it is left open here; no other clause uses (iii).

(iv) \emph{Global charges} are not returned in any tower, ours included (P5): information is returned at little cost because Hawking quanta are soft, and charge would cost the hole's mass to return because its lightest carrier is a GeV proton against a nanokelvin $T_{\mathrm{H}}$. (v) \emph{No remnant:} the singularity paper's exhaustiveness clause, imported as Fact \claimref{singularity.rate-models-kinematic-inputs-l-u} at its level there, a premise.

The late-stage evaporation therefore dims the visible final burst by the ratio of the total light degrees of freedom to the visible ones, of order the tower count if the towers are comparable, a minor prediction for primordial-black-hole burst searches at observation level, unconditional on the charge regime since it follows from (i) alone. The charge-saturated case is clearest: a hole formed from mirror matter alone has $Q_{2}m_{2} = M$, and it does not return its charge, exactly as no astrophysical hole of this tower returns ours. The ascend-then-descend structure at the degenerate locus is imported from the singularity paper \cite{ButlerT5}.

## technical
Matter of any tower crossing a horizon meets the one shared singular locus, where every tower's algebra degenerates and ascends its own ladder, giving parallel boundary mode spaces at one wall. Under P1 and the Hawking paper's greybody assembly under its interface premise, run tower by tower, (i) the rest energy joins the metric and is re-emitted democratically as Hawking radiation into every populated tower, in proportion to its light degrees of freedom; (ii) information returns in its own tower's channel at little entropy cost, since $S_{\mathrm{BH}} \sim 10^{77}$ for a solar mass against a progenitor's $10^{58}$; (iii) Gauss-law charges are returned by discharge for holes below about $1.3 \times 10^{5}$ solar masses, and above that the question is left open.

Under P5, (iv) global charges are returned in no tower, since the lightest carrier is a GeV proton against a nanokelvin $T_{\mathrm{H}}$; and (v) there is no remnant, by the imported exhaustiveness premise. A consequence at observation level, from (i) alone, is that the final burst of an evaporating hole is dimmed by the ratio of total to visible light degrees of freedom.

## lay
Matter from any hidden sector that falls into a black hole ends up at the same place inside. This result follows what becomes of it, on stated premises: that all sectors share one gravitational field (P1), that the Hawking paper's interface premise about how emitted radiation reaches distant observers holds, that the hole's boundary modes give back information but not conserved particle counts (P5), and the imported premise that nothing is left over at the end. Under these, its energy comes back as Hawking radiation shared among all the sectors, its information comes back within its own sector, and its count of particles such as protons is not returned. A side effect, at the level of observation, is that the last flash of a tiny evaporating black hole would be fainter than expected, because part of it goes into the hidden sectors.

## one-liner
Under P1, P5, the interface premise and the imported exhaustiveness premise, what any tower drops into a black hole returns its energy democratically to all towers and its information to its own, but not its global charges, and leaves no remnant.
