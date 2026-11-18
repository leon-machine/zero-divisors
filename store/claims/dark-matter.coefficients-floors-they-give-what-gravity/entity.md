---
id: dark-matter.coefficients-floors-they-give-what-gravity
kind: claim
version: 6
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
- name: Claude Fable 5.2
  role: 'restatement: every number recomputed with the derived production coefficients, the Dirac-or-Weyl bracket closed, the two bounds on the radiation at the floors weakened by a factor ten, and the energy convention behind the floors stated'
  version: 5
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'
- name: Claude Fable 5.2
  role: 'restatement at the maintainer''s decision of 18 November 2026: the floors take the mean energy per creation event computed in the seeding proposition; floors, the mirror''s baryon-to-photon ratio at the floor, the crossover coefficient, the floor at the rescue temperature and the radiation values recomputed; the convention qualifiers removed'
  version: 6
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
amendments:
- version: 6
  kind: restatement
  defect: 'the floors were evaluated at energy 3T per creation event, a convention; at the mean energy per event (7.889 T for the mirror''s content, 7.890 T for vectors) the mirror''s floor is 6.6e-4 and not 5.2e-4, the nine vectors'' 8.1e-4 and not 6.4e-4, the mirror''s baryon-to-photon ratio at the floor 2.1 and not 4.4, the crossover coefficient about 1.5 and not about 4, the radiation values at the floors 1.4e-12 and 1.7e-11 so that the bounds 1e-12 and 1e-11 fail, and the floor at the rescue temperature 5.4e-3, no longer equal to the hot-deposit value'
  evidence: check.py::check_mirror_floor_and_eta_prime
- version: 5
  kind: restatement
  defect: 'the floors, the yield, the shortfall and the radiation bounds were computed with the first published coefficients 1.9e-4, 1.1e-3, 2.3e-3, which are too small (by sixteen from the coupling, and with the 45 chiral fermions weighted as Dirac fermions or halved by hand); with the derived coefficients the mirror''s c is 0.568 and not 0.053 to 0.078, and the bounds below 1e-13 and below 1e-12 on the radiation at the floors no longer hold'
  evidence: check.py::check_mirror_floor_and_eta_prime
review: typed
derivations:
- name: main
  uses:
  - dark-matter.imported-massless-graviton-production-rate@4
  - dark-matter.mirror-tower-copy-one@11
  - dark-matter.open-channels-their-costs@7
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@6
  - synthesis.gravitational-pair-production-from-the-operator-source-at-first-order@2
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
  maintainer_pass_2026_11_18_energy:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 5 -> 6, at Leon''s decision of 18 November 2026, 14:04 (adopt the computed mean energy per creation event in the gravitational floor). From dark-matter.seeding-gravity-floor-dark-towers-temperature version 6 (repinned 5 -> 6): nine vectors'' floor 6.4e-4 -> 8.1e-4; mirror''s floor 5.2e-4 -> 6.6e-4 and eta'' at the floor 4.4 -> 2.1 (still above one); the coefficient at which eta'' = 1 at the floor about 4 (seven times the mirror''s) -> about 1.5 (1.54, 2.7 times the mirror''s); the floor at the rescue temperature 4e-3 -> 5.4e-3, which is 1.27 times the hot-deposit value 4.2e-3 and no longer equal to it (the equality held only with 3T per event on both sides); Delta N_eff at the floors 5.4e-13 (below 1e-12) -> 1.4e-12 (below 2e-12) and 6.5e-12 (below 1e-11) -> 1.7e-11 (below 2e-11). Unchanged, because they count events and quanta and not energy: the coefficients, the yield 1.95e-14, the shortfall 4.4e3 (2.2e3 against the quanta), the rescue temperature 9.9e15 GeV, the hot-deposit value and the bound 1e-8 there. Removed: the paragraph on the two energy counts (3T per event, 3T per quantum) and the sentences quoting a review''s computation of the mean energy; the numbers are now the stored ones. source_formal is the deposited statement and is left as it was. The series script verify_T14.py still evaluates the deposited paper''s formula.'
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 4 -> 5, at Leon''s decision of 18 November 2026 (restate the direct users of the corrected production rate). Every number that depends on the coefficients is recomputed with those of synthesis.gravitational-pair-production-from-the-operator-source-at-first-order, clause (v): nine vectors c 0.021 -> 0.2165 and floor 3.5e-4 -> 6.4e-4; mirror c 0.053 to 0.078 -> 0.568, floor 2.8 to 3.2e-4 -> 5.2e-4, eta'' 19 to 26 -> 4.4; yield 1.8 to 2.7e-15 -> 1.95e-14, shortfall 3 to 5e4 -> 4.4e3, rescue 31.9 to 36.2 -> 16.4 times the ceiling; the radiation bounds at the floors weakened from below 1e-13 and 1e-12 to below 1e-12 and 1e-11. The conditions on c (eta'' = 1 at about 4), the hot-deposit value 4e-3 and the bound 1e-8 are unchanged. The seeding proposition is repinned 4 -> 5 after its restatement of the same day (events of two quanta; formulas unchanged), and its other energy count is stated beside the values. The series script verify_T14.py still evaluates the first imported coefficients. source_formal is the deposited statement and is left as it was.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.imported-massless-graviton-production-rate repinned 1 -> 2 after reviewing the F14 change writing the rate with the reduced Planck mass bar M_P, the source''s M_P (any M_P here that is evaluated is 2.435e18 GeV, the reduced mass); the use here holds as cited. Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited.'
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
The production coefficients are those of Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(v) (Fact \claimref{dark-matter.imported-massless-graviton-production-rate} for the published values), under that theorem's hypothesis (OS), or on the standard account of the Fact: per creation event of two quanta, from a bath of the Standard Model's content with zero curvature couplings, $5789\pi^{3}/82944000 = 2.164 \times 10^{-3}$ for a real scalar, $16087\pi^{3}/82944000 = 6.014 \times 10^{-3}$ for a chiral fermion and $16087\pi^{3}/20736000 = 2.4055 \times 10^{-2}$ for a real massless vector. The floors are those of Proposition \claimref{dark-matter.seeding-gravity-floor-dark-towers-temperature}, $\xi_{\mathrm{floor}} = (\tfrac43(\bar{E}/T)\,Y g_{*}/g_{d})^{1/4}$ with the mean energy per creation event $\bar{E}$ computed there from the rate integral: $7.890\,T$ for vectors and $7.889\,T$ for a copy of the Standard Model's content.

(i) For a five-dimensional tower whose light content is the nine vectors of its $\mathfrak{u}(3)$, eight gluons and the abelian photon, $c = 9 \times 2.4055 \times 10^{-2} = 0.2165$, $g_{d} = 18$, and $\xi_{\mathrm{floor}} = 8.1 \times 10^{-4}$ at the ceiling reheating; whether those are its light species is part of the coupling question of Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}, and the value is the floor for that content, not for the tower.

(ii) For the mirror tower, whose content is the Standard Model's (Theorem \claimref{dark-matter.mirror-tower-copy-one}), the species sum over four real scalars, forty-five Weyl fermions and twelve vectors gives $c = 1519247\pi^{3}/82944000 = 0.568$, each of the forty-five being chiral and weighted once (the earlier bracket between counting the fermions per Dirac and per Weyl species is closed by the derived weights), with $g_{d} = 4 + 45 \times \tfrac{7}{4} + 24 = 106.75$, hence $\xi_{\mathrm{floor}} = 6.6 \times 10^{-4}$ and, with the charge reading of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, $\eta' = 2.1$ at the floor; $\eta'$ would fall below one at the floor only for a coefficient above about $1.5$ ($1.54$), which is $2.7$ times the mirror's.

(iii) The produced yield at the ceiling, $Y = 1.95 \times 10^{-14}$ creation events per unit entropy for the mirror, falls short of the $8.7 \times 10^{-11}$ baryons per unit entropy our baryon number requires by a factor of $4.4 \times 10^{3}$ (of $2.2 \times 10^{3}$ against the $2Y$ quanta); closing the gap would need $T_{\mathrm{desc}} = 9.9 \times 10^{15}$ GeV, $16.4$ times the ceiling, where the floor itself would be $5.4 \times 10^{-3}$, above the charge-domination crossover. That is $1.27$ times the hot-deposit value $4.2 \times 10^{-3}$ of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, and no longer equal to it: at that temperature gravity supplies one creation event per unit of baryon number, and an event carries $7.9\,T$ where the hot deposit takes $3T$ per unit of baryon number. The hot deposit's $3T$ is a stipulated figure of order the reheating temperature, not a computed mean, so the ratio $1.27$ records the two counts and carries no further weight. Gravity heats the dark towers; it does not populate them with charge, which is the descent's.

(iv) The mirror's contribution to $\Neff$, $7.447\,\xi^{4}$, is $1.4 \times 10^{-12}$ at the floor, below $2 \times 10^{-12}$, and below $10^{-8}$ at the hot deposit of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}; a nine-vector tower's, $2.202 \times 18\,\xi^{4}$ for eighteen light polarisations, the coefficient being half the two-polarisation $\Delta\Neff$ bracketed in Proposition \claimref{dark-matter.radiation-audit-what-theorem-closes-what}, is $1.7 \times 10^{-11}$ at its floor, below $2 \times 10^{-11}$. Both are far below any measurement.

## technical
The gravitational seeding floor, evaluated with the pair-production coefficients derived in the store (per creation event of two quanta: $2.164 \times 10^{-3}$ for a real scalar, $6.014 \times 10^{-3}$ for a chiral fermion, $2.4055 \times 10^{-2}$ for a real massless vector; under that derivation's hypothesis (OS), or on the standard account of the imported rate) and with the mean energy per creation event computed from the same rate integral (about $7.9\,T$), gives concrete floors. For a five-dimensional tower whose light content is the nine vectors of its $\mathfrak{u}(3)$, $c = 0.2165$, $g_{d} = 18$ and $\xi_{\mathrm{floor}} = 8.1 \times 10^{-4}$ at the ceiling reheating, a floor for that content and not for the tower. For the mirror, whose content is the Standard Model's, $c = 0.568$ with each of the forty-five chiral fermions weighted once (the earlier bracket between Dirac and Weyl counting is closed), $g_{d} = 106.75$, $\xi_{\mathrm{floor}} = 6.6 \times 10^{-4}$, and with the charge reading of the stored asymmetry $\eta' = 2.1$ at the floor, above one; it would fall below one only for a coefficient $2.7$ times the mirror's.

The yield produced at the ceiling, $Y = 1.95 \times 10^{-14}$ creation events per unit entropy for the mirror, falls short of the $8.7 \times 10^{-11}$ that our baryon number requires by a factor $4.4 \times 10^{3}$; closing the gap would need $T_{\mathrm{desc}}$ $16.4$ times the ceiling, where the floor would be $5.4 \times 10^{-3}$, $1.27$ times the hot-deposit value. Gravity heats the dark towers but does not populate them with charge. The mirror's $\Delta\Neff = 7.447\,\xi^{4}$ is $1.4 \times 10^{-12}$ at the floor, below $2 \times 10^{-12}$, and below $10^{-8}$ at the hot deposit, and the nine-vector tower's is $1.7 \times 10^{-11}$ at its floor, below $2 \times 10^{-11}$.

## lay
After the descent the hidden worlds can be warmed only through gravity, and this result puts numbers on that minimum warming, taking the descent to reheat at the ceiling temperature. For the mirror world, whose particles copy ours, the floor is about fifteen hundred times colder than ours; for a five-dimensional tower the figure assumes that its light particles are its nine force carriers, which is not settled. At the ceiling, gravity also falls short, by a few thousand times, of supplying the mirror world's matter, so that matter must have been set by the descent itself. These figures use the rate of gravitational production as the collection now derives it, which is larger than the published value used before, and the energy each act of production carries as worked out from that same calculation. At these temperatures the extra radiation the hidden worlds add is far too small to detect.

## one-liner
At the ceiling reheating, gravitational heating at the rate derived in the store, with the mean energy per creation event computed from it, gives temperature floors of $6.6 \times 10^{-4}$ for the mirror and, for that light content, $8.1 \times 10^{-4}$ for a nine-vector five-dimensional tower, but falls $4.4 \times 10^{3}$ short of the mirror's charge, so gravity heats the dark towers without populating them.
