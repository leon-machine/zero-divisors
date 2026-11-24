---
id: dark-matter.seeding-gravity-floor-dark-towers-temperature
kind: claim
version: 6
title: 'Seeding by gravity: the floor on a dark tower''s temperature'
status: proved
region: dark-matter
subject: dark-matter
tags: [matter-asymmetry, quantum-gravity, needs-continuum]
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
  role: 'restatement: the rate is cited from the result that derives it, with its hypothesis; the rate counts creation events of two quanta, so the yield is of events and the energy convention behind the floor is stated; formulas unchanged'
  version: 5
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'
- name: Claude Fable 5.2
  role: 'restatement at the maintainer''s decision of 18 November 2026: the floor is defined with the mean energy per creation event, computed from the rate integral and checked here, in place of the convention of 3T per event; prefactor 9.6e-4 -> 1.23e-3'
  version: 6
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
amendments:
- version: 6
  kind: restatement
  defect: 'the floor took energy 3T per creation event (energy fraction 4Y), a convention not derived from the rate; in the rate integral each incoming leg is weighted by E^3 times its occupation, so an event carries 8 zeta(5)/zeta(4) T to (60/7) zeta(5)/zeta(4) T, 7.87 T to 7.89 T for the Standard Model''s bath, the energy fraction is (4/3)(E/T) Y, about 10.5 Y, and the stated prefactor 9.6e-4 was low by a factor 1.27'
  evidence: check.py::check_mean_energy_per_event
- version: 5
  kind: restatement
  defect: 'the statement took the rate and its per-species coefficients from the imported Fact alone, whose first published value was too small, and did not say whether the rate counts quanta or creation events of two quanta, on which the energy fraction 4Y behind the floor depends by a factor two'
  evidence: check.py::check_floor_prefactor_and_scaling
review: typed
derivations:
- name: main
  uses:
  - dark-matter.ceiling-valued-inherited-success@5
  - dark-matter.imported-massless-graviton-production-rate@5
  - dark-matter.superselected-hence-dark-exactly-stable@5
  - synthesis.gravitational-pair-production-from-the-operator-source-at-first-order@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:gravseed
- kind: check
  ref: check.py::check_boltzmann_yield
- kind: check
  ref: check.py::check_kappa_and_convention
- kind: check
  ref: check.py::check_mean_energy_per_event
- kind: check
  ref: check.py::check_floor_prefactor_and_scaling
- kind: check
  ref: check.py::check_ceiling_range_factor
- kind: check
  ref: check.py::check_later_evolution_of_the_ratio
locators:
  paper: T14
  number: Prop A.2
  label: prop:gravseed
  line: 1475
extraction:
  maintainer_pass_2026_11_18_energy:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 5 -> 6, at Leon''s decision of 18 November 2026, 14:04 (adopt the computed mean energy per creation event in place of the stored convention of 3T per event). The floor is now xi_floor = ((4/3)(E/T) Y g*/g_d)^(1/4) with E the mean energy per event: each incoming leg of the rate integral of clause (v) of the pair-production theorem is weighted by E^3 times its occupation, mean 4 zeta(5)/zeta(4) T (Bose) or (30/7) zeta(5)/zeta(4) T (Fermi); weighted by the Bose and Fermi parts of the rate, E = 7.873 T (real scalar), 7.890 T (chiral fermion or vector), 7.889 T (a copy of the bath) for the bath (4, 45, 12). Prefactor 9.6e-4 -> 1.23e-3 (between 1.225 and 1.226e-3 for those contents). Removed: the counts 4Y (3T per event) and 8Y (3T per quantum), the factor 2^(1/4), and the sentence saying the mean was computed in a review and not by this proposition''s check; the mean is now proved and checked here (check_mean_energy_per_event, zeta(5) bracketed by a partial sum with exact tail bounds). The yield Y, kappa_s, the scaling in c, g_d and T_desc, the ceiling-range factor and the later evolution are unchanged. The export xi8_bracket now takes the bracket of E/T as its third argument. The series script verify_T14.py still evaluates the deposited paper''s formula (3T per event, 9.6e-4, and the first imported coefficients).'
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 4 -> 5, at Leon''s decision of 18 November 2026 (restate the direct users of the corrected production rate). The rate is now cited from synthesis.gravitational-pair-production-from-the-operator-source-at-first-order, clause (v), with the imported Fact kept for the published values; the rate counts creation events of two quanta, so Y is the yield of events, and the floor keeps the stored energy convention (3T per event, energy fraction 4Y), with the two-quanta count (8Y, a factor 2^(1/4) on the ratio) stated beside it. No formula and no number of the statement changed. The series script verify_T14.py still evaluates the floor at the first imported coefficients.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.imported-massless-graviton-production-rate repinned 1 -> 2 after reviewing the F14 change writing the rate with the reduced Planck mass bar M_P, the source''s M_P (any M_P here that is evaluated is 2.435e18 GeV, the reduced mass); the use here holds as cited.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Boltzmann yield c T^3/(3 kappa_s M_P^3) with Riemann brackets, kappa_s in (145.25, 145.30), the 9.6e-4 prefactor and exact scaling, the ceiling-range factor and the entropy evolution of the ratio. Version 2 -> 3. Wording fix (Leon 2026-10-23): the ceiling-range factor (3.5e11/6e14)^(3/4) is stated as about 4 x 10^-3 (3.75 x 10^-3) rather than equal to 4 x 10^-3 (formal). Check strengthened: kappa_s, the convention factor 1.66 and the floor prefactor pinned to seven figures; scaling samples moved to module level. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    removed:
    - dark-matter.coefficients-floors-they-give-what-gravity
    added:
    - dark-matter.ceiling-valued-inherited-success
    - dark-matter.imported-massless-graviton-production-rate
    - dark-matter.superselected-hence-dark-exactly-stable
    note: 'Broke the E301 cycle here: the edge to the coefficients proposition only marks that the script
      evaluates this formula at those coefficients, which the general floor does not use; added the imported
      graviton production rate (the result is proved given it), superselection (only gravitational heating)
      and the ceiling valuation (the range of the reheating temperature); the stored-asymmetry deposit
      is context and already depends on this claim. Levels pass: lay and one-liner now keep the imported
      production rate and the thermalisation assumption; the one-liner''s bare 10^{-3} became the formula''s
      normalised value.'
  env: proposition
  context_refs:
  - dark-matter.ceiling-valued-inherited-success
  - dark-matter.imported-massless-graviton-production-rate
  - dark-matter.stored-asymmetry-charge-not-number
  - dark-matter.superselected-hence-dark-exactly-stable
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.ceiling-valued-inherited-success
    - dark-matter.imported-massless-graviton-production-rate
    - dark-matter.superselected-hence-dark-exactly-stable
---

## formal
By exact superselection the towers interact only through the shared metric (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}), so after the descent a dark tower can be heated only gravitationally; what the descent itself deposited in it (its charge, Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, with whatever energy the deposit carried) is a datum, not a computation. Let the descent reheat this tower to $T_{\mathrm{desc}}$ and let tower $r$, with $g_{d}$ light degrees of freedom that thermalise among themselves, be heated by gravitational pair production from the visible plasma at the rate per volume $\Gamma = c\,T^{8}/M_{P}^{4}$ of Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(v) (Fact \claimref{dark-matter.imported-massless-graviton-production-rate} for the published values), under that theorem's hypothesis (OS), or on the standard account of the Fact, with $c$ the sum of the theorem's per-species coefficients over the tower's light content and $\Gamma$ counting creation events, each of two quanta. Then the produced comoving yield of events is
\[
Y \;=\; \frac{c\,T_{\mathrm{desc}}^{3}}{3\,\kappa_{s}M_{P}^{3}}, \qquad \kappa_{s} = \sqrt{\frac{\pi^{2}g_{*}}{90}}\;\frac{2\pi^{2}}{45}\,g_{s} \;=\; 145.3 \ \text{at } g_{*} = g_{s} = 100,
\]
and the number of quanta per unit entropy is $2Y$.

\emph{(The mean energy per event.)} A creation event puts into the tower the energy $E_{1} + E_{2}$ of the incoming pair. In the rate integral of clause (v) of that theorem the angular weight of every channel is a constant times $s^{2} = 4E_{1}^{2}E_{2}^{2}(1 - \cos\theta_{12})^{2}$, so each incoming leg is weighted by $E^{3}$ times its occupation, independently of the other leg, and the mean energy of a leg is
\[
\frac{\Gamma(5)\,\zeta(5)}{\Gamma(4)\,\zeta(4)}\,T \;=\; \frac{4\,\zeta(5)}{\zeta(4)}\,T \;\approx\; 3.832\,T \ \ \text{(Bose)}, \qquad
\frac{\tfrac{15}{16}\cdot 24\,\zeta(5)}{\tfrac{7}{8}\cdot 6\,\zeta(4)}\,T \;=\; \frac{30\,\zeta(5)}{7\,\zeta(4)}\,T \;\approx\; 4.106\,T \ \ \text{(Fermi)},
\]
with $\zeta(4) = \pi^{4}/90$ and $1.0369277 < \zeta(5) < 1.0369278$. An event from a Bose pair therefore carries $8\,\zeta(5)/\zeta(4)\,T \approx 7.664\,T$ on average and an event from a Fermi pair $(60/7)\,\zeta(5)/\zeta(4)\,T \approx 8.212\,T$. For a produced species $j$ the mean energy per event $\bar{E}$ weights these two by the Bose and Fermi parts of $\alpha_{j}$ in clause (v), which are proportional to $\bigl(c_{j}(N_{s} + 12N_{v}) + 5\tau_{j}\sum_{i}\tau_{i}\bigr)/225$ and to $49\,c_{j}N_{w}/4800$; for a tower the parts are summed over its light content. So $7.66 < \bar{E}/T < 8.22$ for every bath and every content, and for a bath of the Standard Model's content $(N_{s}, N_{w}, N_{v}) = (4, 45, 12)$ with zero curvature couplings
\[
\bar{E} \;=\; 7.873\,T \ \text{(a real scalar)}, \qquad 7.890\,T \ \text{(a chiral fermion, or a real massless vector, or any number of them)}, \qquad 7.889\,T \ \text{(a copy of that content)}.
\]

\emph{(The floor.)} With $s/\rho = 4/(3T)$ at $g_{*} = g_{s}$ the energy fraction at production is $\tfrac43(\bar{E}/T)\,Y$, between $10.49\,Y$ and $10.52\,Y$ for those contents, and the temperature ratio it alone would give is
\[
\xi_{\mathrm{floor}} \;=\; \Big(\tfrac43\,\frac{\bar{E}}{T}\,Y\,\frac{g_{*}}{g_{d}}\Big)^{1/4} \;=\; 1.23 \times 10^{-3}\; c^{1/4}\Big(\frac{16}{g_{d}}\Big)^{1/4}\Big(\frac{T_{\mathrm{desc}}}{6 \times 10^{14}\ \mathrm{GeV}}\Big)^{3/4}
\]
for $g_{*} = g_{s} = 100$ at the reheating. The prefactor depends on the produced content only through $\bar{E}^{1/4}$: it lies between $1.225$ and $1.226 \times 10^{-3}$ for each of the contents above, and between $1.21$ and $1.24 \times 10^{-3}$ for any bath and content. This is a floor: the tower's bath cannot be colder, and it is hotter by whatever energy the deposit carried. The ratio thereafter evolves through the two sectors' separate entropy conservation, by
\[
\left(\frac{g_{d}^{\mathrm{seed}}}{g_{d}}\right)^{1/3}\left(\frac{g_{s}}{g_{s}^{\mathrm{seed}}}\right)^{1/3}
\]
at any later epoch. Two inputs are not fixed by the formula: $T_{\mathrm{desc}}$, the ceiling of Proposition \claimref{dark-matter.ceiling-valued-inherited-success} or below it, so that across that range the floor spans a factor $(3.5 \times 10^{11}/6 \times 10^{14})^{3/4}$, about $4 \times 10^{-3}$ ($3.75 \times 10^{-3}$), the body quoting the top and saying so; and the deposit's energy, which sets the actual ratio above the floor.

## technical
Since superselection leaves the shared metric as the only channel, a dark tower can be heated after the descent only gravitationally. If the descent reheats this tower to $T_{\mathrm{desc}}$ and tower $r$, with $g_{d}$ light degrees of freedom that thermalise among themselves, is heated by gravitational pair production at the rate $\Gamma = c\,T^{8}/M_{P}^{4}$ derived in the store (creation events of two quanta each; under that derivation's hypothesis (OS), or on the standard account of the imported rate), the comoving yield of events is $Y = c\,T_{\mathrm{desc}}^{3}/(3\kappa_{s}M_{P}^{3})$ with $\kappa_{s} = 145.3$ at $g_{*} = g_{s} = 100$. Each event carries the energy of its incoming pair. The rate integral weights each incoming leg by $E^{3}$ times its occupation, so a leg carries $4\zeta(5)/\zeta(4)\,T \approx 3.83\,T$ if it is a boson and $(30/7)\zeta(5)/\zeta(4)\,T \approx 4.11\,T$ if it is a fermion, and the mean energy per event $\bar{E}$ lies between $7.66\,T$ and $8.22\,T$; for the Standard Model's bath it is $7.873\,T$ for a produced real scalar, $7.890\,T$ for a chiral fermion or a vector and $7.889\,T$ for a copy of the bath's content. The energy fraction is $\tfrac43(\bar{E}/T)\,Y$, about $10.5\,Y$, and the temperature ratio this alone gives is
$\xi_{\mathrm{floor}} = (\tfrac43(\bar{E}/T)\,Y g_{*}/g_{d})^{1/4} = 1.23 \times 10^{-3}\,c^{1/4}(16/g_{d})^{1/4}(T_{\mathrm{desc}}/6 \times 10^{14}\,\mathrm{GeV})^{3/4}$, the prefactor between $1.225$ and $1.226 \times 10^{-3}$ for those contents.

This is a floor: the tower is hotter by whatever energy the descent deposited. Thereafter the ratio evolves through the two sectors' separate entropy conservation, and across the range of reheating temperatures up to the ceiling the floor spans a factor of about $4 \times 10^{-3}$. The result is proved given the rate and the standard thermal history.

## lay
Even if the hidden sectors started completely cold, the hot ordinary matter of the early universe would warm them slightly through gravity, the only contact left between the sectors. Taking the rate of this gravitational production as the collection now derives it, working out from the same calculation how much energy each act of production carries (close to eight times the temperature, more than a typical particle of the hot matter carries, because energetic collisions produce more readily), and assuming each hidden sector's light particles share their heat among themselves, this result calculates that minimum warmth: about a thousandth of our temperature or less, depending on how hot the early universe became. The real temperature could be higher if the universe's birth heated the hidden sectors directly.

## one-liner
Gravitational pair production from the visible plasma, at the rate derived in the store (coefficient $c$, counting events of two quanta, each carrying a mean energy of about $7.9\,T$ computed from the rate integral), puts a floor $\xi_{\mathrm{floor}} \propto c^{1/4}T_{\mathrm{desc}}^{3/4}$ on the temperature ratio of a dark tower whose light species thermalise among themselves, $1.23 \times 10^{-3}\,c^{1/4}(16/g_{d})^{1/4}$ at the ceiling reheating.
