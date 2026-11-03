---
id: dark-matter.ceiling-valued-inherited-success
kind: claim
version: 5
title: The ceiling valued, and an inherited success
status: proved
region: dark-matter
subject: neutrinos
tags: [hypothesis-u, seesaw-and-majorana, mass-generation]
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
derivations:
- name: main
  uses:
  - families.alignment-computed-thirteenth-refutation-democracy-one@4
  assumes:
  - dark-matter.hyp-u-equal-rank-one-eigenvalues@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:ceiling
- kind: check
  ref: check.py::check_rank_one_eigenvalue_and_seesaw_inversion
- kind: check
  ref: check.py::check_two_ends_of_the_range
- kind: check
  ref: check.py::check_ratio_of_the_ends
locators:
  paper: T14
  number: Prop 6.4
  label: prop:ceiling
  line: 595
extraction:
  env: proposition
  context_refs:
  - dark-matter.mirror-share-one-how-fragile
  - dark-matter.radiation-audit-what-theorem-closes-what
  - families.alignment-computed-thirteenth-refutation-democracy-one
  outside_pilot_cites:
  - ButlerT12
  typing:
    by: ai-typing-pass
    added:
    - families.alignment-computed-thirteenth-refutation-democracy-one
    - dark-matter.hyp-u-equal-rank-one-eigenvalues
    note: 'added the families alignment as a premise because Hypothesis (U) is stated about the per-sector
      rank-one eigenvalues that alignment supplies; the two context results (mirror share, radiation audit)
      depend on this one and were not added; Hypothesis (U) itself has no store postulate, so the conditionality
      is carried only in the text. Hypothesis pass: assumes dark-matter.hyp-u-equal-rank-one-eigenvalues
      added because the paper names Hypothesis (U) as a condition of this result. Levels pass: the lay
      said ''every family'', but (U) equates the sectors'' rank-one eigenvalues, not the families, so
      it now names the sectors and (U); the one-liner now says (U) is read at a common low scale, the
      reading the quoted range uses.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - families.alignment-computed-thirteenth-refutation-democracy-one
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the rank-one eigenvalue, the seesaw inversion, both ends of the range on the input brackets and at central values, and their ratio (m_t/m_b)^2. Version 3 -> 4. Check strengthened: the bracket ends of m_t^2/m_3, m_b^2/m_3 and their ratio pinned exactly; quoted windows moved to module level. Version 4 -> 5.'
---

## formal
The families paper's alignment gives, within each sector, one vacuum direction and hence one rank-one Dirac mass at leading order \cite[Prop.~4.3]{ButlerT13}; it never equates magnitudes across sectors. This paper adds its own hypothesis, attacked below: \emph{Hypothesis (U)}, that the rank-one eigenvalues of the different sectors coincide at the ceiling, so that the neutrino's Dirac eigenvalue $m_{D}$ there is the common leading-order value, which the top retains and the second-order breaking splits for the down-type and charged-lepton sectors. With $m_{3}$ the heaviest light neutrino mass, the seesaw $m_{3} = m_{D}^{2}/M_{R}$ then values the scale on which two results depend, in a range whose ends are the two readings of (U):
\[
\frac{m_{b}^{2}}{m_{3}} \;\approx\; 3.5 \times 10^{11}\ \mathrm{GeV} \;\lesssim\; M_{\mathrm{rung}} \;=\; M_{R} \;=\; \frac{m_{D}^{2}}{m_{3}} \;\lesssim\; \frac{m_{t}^{2}}{m_{3}} \;\approx\; 6 \times 10^{14}\ \mathrm{GeV},
\]
the upper end if the neutrino's Dirac mass is retained unbroken like the top's, the lower if it is split like the bottom's, with (U) read at a common low scale (read at the ceiling, the running of $m_{t}$ and $m_{b}$ lowers both ends by about an order of magnitude, a systematic the range does not include); the ends differ by $(m_{t}/m_{b})^{2} \approx 1.7 \times 10^{3}$, and which applies is a condensate-component question the families paper leaves open. Conditional on (U) and flagged so; (U) is used in two results, the $M$ of Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(ii) and the rung scale of Proposition \claimref{dark-matter.radiation-audit-what-theorem-closes-what}(4). The same hypothesis puts the bottom and tau masses equal at the ceiling; whether their running reproduces the observed ratio near three is imported from the Standard-Model paper's run \cite{ButlerT12} at assembly level, a check to be passed, not one passed here.

## technical
Within each sector the families alignment gives one vacuum direction and hence a single rank-one Dirac eigenvalue at leading order, but it never relates magnitudes across sectors. Hypothesis (U) adds that these rank-one eigenvalues coincide at the ceiling, so the neutrino's Dirac eigenvalue $m_{D}$ is the common value, which the top retains and second-order breaking splits for the down-type and charged-lepton sectors. With $m_{3}$ the heaviest light neutrino mass, the seesaw $m_{3} = m_{D}^{2}/M_{R}$ then values the rung scale, $\frac{m_{b}^{2}}{m_{3}} \approx 3.5 \times 10^{11}\ \mathrm{GeV} \lesssim M_{\mathrm{rung}} = M_{R} \lesssim \frac{m_{t}^{2}}{m_{3}} \approx 6 \times 10^{14}\ \mathrm{GeV}$.

The upper end is the reading in which the neutrino's Dirac mass is retained like the top's, the lower the one in which it is split like the bottom's; they differ by $(m_{t}/m_{b})^{2} \approx 1.7 \times 10^{3}$, and which applies is left open. Reading (U) at the ceiling rather than at a common low scale lowers both ends by about an order of magnitude, a systematic the range does not include. The result is conditional on (U), which two other results use (the mirror-share mass and the rung scale of the radiation audit). The same hypothesis puts the bottom and tau masses equal at the ceiling; whether running reproduces their observed ratio near three is imported from the Standard-Model paper's run as a check still to be passed.

## lay
If one assumes that the leading mass of every kind of matter particle (up-type quarks, down-type quarks, charged leptons and neutrinos) is the same at the highest energy the framework uses (Hypothesis (U)), the mass of the heaviest light neutrino fixes how heavy its hidden partner must be. The answer depends on whether the neutrino behaves like the top quark or like the bottom quark, so it comes as a range spanning about three orders of magnitude, far above any collider energy. Everything rests on that equal-mass assumption, which the paper states as a hypothesis and then attacks.

## one-liner
Under Hypothesis (U), read at a common low scale, the seesaw values the rung scale between $m_{b}^{2}/m_{3} \approx 3.5 \times 10^{11}$ GeV and $m_{t}^{2}/m_{3} \approx 6 \times 10^{14}$ GeV.
