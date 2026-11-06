---
id: dark-matter.coefficients-floors-they-give-what-gravity
kind: claim
version: 4
title: The coefficients, the floors they give, and what gravity cannot supply
status: proved
region: dark-matter
subject: dark-matter
tags: [matter-asymmetry, mirror-sector, quantum-gravity, needs-continuum]
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
  - dark-matter.imported-massless-graviton-production-rate@1
  - dark-matter.mirror-tower-copy-one@8
  - dark-matter.open-channels-their-costs@5
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:coefficients
- kind: check
  ref: check.py::check_nine_vector_floor
- kind: check
  ref: check.py::check_mirror_floor_and_eta_prime
- kind: check
  ref: check.py::check_yield_shortfall_and_rescue
- kind: check
  ref: check.py::check_neff_contributions
locators:
  paper: T14
  number: Prop A.3
  label: prop:coefficients
  line: 1503
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: species coefficients c, g_d = 106.75, floor brackets for the nine-vector and mirror contents, eta'' at the floor, the yield shortfall and rescue temperature (floor equal to the hot deposit there), and the N_eff contributions, all as exact power brackets with pi by Machin. Version 3 -> 4. Wording fix (Leon 2026-10-23): (iii) gives the exact range, 31.9 to 36.2 times the ceiling, for the earlier thirty-two to thirty-six (formal and technical).'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES L2
    open_problem: op.small-findings
    note: 'Recomputed exactly from the stored formulas of dark-matter.seeding-gravity-floor-dark-towers-temperature: the shortfall 3.2 to 4.8 x 10^4 inverts Y proportional to T^3 to a factor 31.8 to 36.4, so thirty-two to thirty-six times the ceiling (1.9 to 2.2 x 10^16 GeV unchanged). The eta-prime bracket 19 to 26 is correct with the unrounded floors 2.87 and 3.16 x 10^-4 and is left as it is.'
  source_formal: '(i) For a five-dimensional tower whose light content is the nine vectors of its $\mathfrak{u}(3)$, eight gluons and the abelian photon, $c = 9 \times 2.3 \times 10^{-3} = 0.021$, $g_{d} = 18$, and $\xi_{\mathrm{floor}} = 3.5 \times 10^{-4}$ at the ceiling reheating; whether those are its light species is part of the coupling question of Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}, and the value is the floor for that content, not for the tower.

(ii) For the mirror tower, whose content is the Standard Model''s (Theorem \claimref{dark-matter.mirror-tower-copy-one}), the species sum over four real scalars, forty-five Weyl fermions and twelve vectors gives $c = 0.053$ counting the fermions as $22.5$ Dirac species and $0.078$ counting them singly, with $g_{d} = 4 + 45 \times \tfrac{7}{4} + 24 = 106.75$, hence $\xi_{\mathrm{floor}}$ between $2.8$ and $3.2 \times 10^{-4}$ and, with the charge reading of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, $\eta''$ between $19$ and $26$ at the floor; the bracket is the counting ambiguity and is carried as such, and $\eta''$ would fall below one at the floor only for a coefficient above about $4$.

(iii) The produced yield at the ceiling, $Y = 1.8$ to $2.7 \times 10^{-15}$ per unit entropy for the mirror, falls short of the $8.7 \times 10^{-11}$ baryons per unit entropy our baryon number requires by a factor of $3$ to $5 \times 10^{4}$; closing the gap would need $T_{\mathrm{desc}}$ between $1.9$ and $2.2 \times 10^{16}$ GeV, thirty to thirty-six times the ceiling, where the floor itself would be $4 \times 10^{-3}$, above the charge-domination crossover and equal to the hot-deposit value of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, as it must be (the same energy per unit of baryon number either way). Gravity heats the dark towers; it does not populate them with charge, which is the descent''s.

(iv) The mirror''s contribution to $\Neff$, $7.447\,\xi^{4}$, is below $10^{-13}$ at the floor and below $10^{-8}$ at the hot deposit of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}; a nine-vector tower''s, $2.202 \times 18\,\xi^{4}$ for eighteen light polarisations, the coefficient being half the two-polarisation $\Delta\Neff$ bracketed in Proposition \claimref{dark-matter.radiation-audit-what-theorem-closes-what}, is below $10^{-12}$ at its floor.'
  env: proposition
  context_refs:
  - dark-matter.mirror-tower-copy-one
  - dark-matter.no-coupling-rule-odd-towers-follows
  - dark-matter.radiation-audit-what-theorem-closes-what
  - dark-matter.stored-asymmetry-charge-not-number
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.mirror-tower-copy-one
    note: 'Added the mirror-copy theorem because clause (ii) takes the mirror''s light content from it;
      kept the seeding-floor edge as a real premise, so the reported E301 cycle must be broken on the
      seeding claim, whose edge back here only cites these coefficients for a script evaluation (not my
      entity); the stored-asymmetry charge reading in (ii) is a real premise but was not added because
      that claim already uses this one. Levels pass: lay rewritten and one-liner amended to keep the ceiling
      reheating, the content-not-tower scope of the nine-vector floor, and the fact that the radiation
      bound holds at the floor and hot deposit.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.mirror-tower-copy-one
---

## formal
(i) For a five-dimensional tower whose light content is the nine vectors of its $\mathfrak{u}(3)$, eight gluons and the abelian photon, $c = 9 \times 2.3 \times 10^{-3} = 0.021$, $g_{d} = 18$, and $\xi_{\mathrm{floor}} = 3.5 \times 10^{-4}$ at the ceiling reheating; whether those are its light species is part of the coupling question of Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}, and the value is the floor for that content, not for the tower.

(ii) For the mirror tower, whose content is the Standard Model's (Theorem \claimref{dark-matter.mirror-tower-copy-one}), the species sum over four real scalars, forty-five Weyl fermions and twelve vectors gives $c = 0.053$ counting the fermions as $22.5$ Dirac species and $0.078$ counting them singly, with $g_{d} = 4 + 45 \times \tfrac{7}{4} + 24 = 106.75$, hence $\xi_{\mathrm{floor}}$ between $2.8$ and $3.2 \times 10^{-4}$ and, with the charge reading of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, $\eta'$ between $19$ and $26$ at the floor; the bracket is the counting ambiguity and is carried as such, and $\eta'$ would fall below one at the floor only for a coefficient above about $4$.

(iii) The produced yield at the ceiling, $Y = 1.8$ to $2.7 \times 10^{-15}$ per unit entropy for the mirror, falls short of the $8.7 \times 10^{-11}$ baryons per unit entropy our baryon number requires by a factor of $3$ to $5 \times 10^{4}$; closing the gap would need $T_{\mathrm{desc}}$ between $1.9$ and $2.2 \times 10^{16}$ GeV, $31.9$ to $36.2$ times the ceiling, where the floor itself would be $4 \times 10^{-3}$, above the charge-domination crossover and equal to the hot-deposit value of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, as it must be (the same energy per unit of baryon number either way). Gravity heats the dark towers; it does not populate them with charge, which is the descent's.

(iv) The mirror's contribution to $\Neff$, $7.447\,\xi^{4}$, is below $10^{-13}$ at the floor and below $10^{-8}$ at the hot deposit of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}; a nine-vector tower's, $2.202 \times 18\,\xi^{4}$ for eighteen light polarisations, the coefficient being half the two-polarisation $\Delta\Neff$ bracketed in Proposition \claimref{dark-matter.radiation-audit-what-theorem-closes-what}, is below $10^{-12}$ at its floor.

## technical
The gravitational seeding floor, evaluated with the imported graviton-exchange production coefficients, gives concrete floors. For a five-dimensional tower whose light content is the nine vectors of its $\mathfrak{u}(3)$, $c = 0.021$, $g_{d} = 18$ and $\xi_{\mathrm{floor}} = 3.5 \times 10^{-4}$ at the ceiling reheating, a floor for that content and not for the tower. For the mirror, whose content is the Standard Model's, $c$ is $0.053$ or $0.078$ as the fermions are counted per Dirac or per Weyl species, $g_{d} = 106.75$, $\xi_{\mathrm{floor}}$ lies between $2.8$ and $3.2 \times 10^{-4}$, and with the charge reading of the stored asymmetry $\eta'$ is $19$ to $26$ at the floor.

The yield produced at the ceiling, $Y = 1.8$ to $2.7 \times 10^{-15}$ per unit entropy for the mirror, falls short of the $8.7 \times 10^{-11}$ that our baryon number requires by a factor $3$ to $5 \times 10^{4}$; closing the gap would need $T_{\mathrm{desc}}$ $31.9$ to $36.2$ times the ceiling. Gravity heats the dark towers but does not populate them with charge. The mirror's $\Delta\Neff = 7.447\,\xi^{4}$ is below $10^{-13}$ at the floor and below $10^{-8}$ at the hot deposit, and the nine-vector tower's is below $10^{-12}$ at its floor.

## lay
After the descent the hidden worlds can be warmed only through gravity, and this result puts numbers on that minimum warming, taking the descent to reheat at the ceiling temperature. For the mirror world, whose particles copy ours, the floor is a few thousand times colder than ours; for a five-dimensional tower the figure assumes that its light particles are its nine force carriers, which is not settled. At the ceiling, gravity also falls short, by tens of thousands of times, of supplying the mirror world's matter, so that matter must have been set by the descent itself. At these temperatures the extra radiation the hidden worlds add is far too small to detect.

## one-liner
At the ceiling reheating, graviton-mediated heating gives temperature floors of a few times $10^{-4}$ for the mirror and, for that light content, a nine-vector five-dimensional tower, but falls $3$ to $5 \times 10^{4}$ short of the mirror's charge, so gravity heats the dark towers without populating them.
