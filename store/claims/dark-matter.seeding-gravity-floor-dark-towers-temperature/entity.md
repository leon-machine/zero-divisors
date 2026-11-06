---
id: dark-matter.seeding-gravity-floor-dark-towers-temperature
kind: claim
version: 4
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
review: typed
derivations:
- name: main
  uses:
  - dark-matter.ceiling-valued-inherited-success@5
  - dark-matter.imported-massless-graviton-production-rate@1
  - dark-matter.superselected-hence-dark-exactly-stable@5
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
By exact superselection the towers interact only through the shared metric (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}), so after the descent a dark tower can be heated only gravitationally; what the descent itself deposited in it (its charge, Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, with whatever energy the deposit carried) is a datum, not a computation. Let the descent reheat this tower to $T_{\mathrm{desc}}$ and let tower $r$, with $g_{d}$ light degrees of freedom that thermalise among themselves, be heated by graviton-mediated production from the visible plasma at rate per volume $\Gamma = c\,T^{8}/M_{P}^{4}$, with $c$ the sum of Fact \claimref{dark-matter.imported-massless-graviton-production-rate}'s per-species coefficients over the tower's light content. Then the produced comoving yield is
\[
Y \;=\; \frac{c\,T_{\mathrm{desc}}^{3}}{3\,\kappa_{s}M_{P}^{3}}, \qquad \kappa_{s} = \sqrt{\frac{\pi^{2}g_{*}}{90}}\;\frac{2\pi^{2}}{45}\,g_{s} \;=\; 145.3 \ \text{at } g_{*} = g_{s} = 100,
\]
its energy fraction at production is $4Y$, and the temperature ratio it alone would give is
\[
\xi_{\mathrm{floor}} \;=\; \Big(4Y\,\frac{g_{*}}{g_{d}}\Big)^{1/4} \;=\; 9.6 \times 10^{-4}\; c^{1/4}\Big(\frac{16}{g_{d}}\Big)^{1/4}\Big(\frac{T_{\mathrm{desc}}}{6 \times 10^{14}\ \mathrm{GeV}}\Big)^{3/4}
\]
for $g_{*} = g_{s} = 100$ at the reheating. This is a floor: the tower's bath cannot be colder, and it is hotter by whatever energy the deposit carried. The ratio thereafter evolves through the two sectors' separate entropy conservation, by
\[
\left(\frac{g_{d}^{\mathrm{seed}}}{g_{d}}\right)^{1/3}\left(\frac{g_{s}}{g_{s}^{\mathrm{seed}}}\right)^{1/3}
\]
at any later epoch. Two inputs are not fixed by the formula: $T_{\mathrm{desc}}$, the ceiling of Proposition \claimref{dark-matter.ceiling-valued-inherited-success} or below it, so that across that range the floor spans a factor $(3.5 \times 10^{11}/6 \times 10^{14})^{3/4}$, about $4 \times 10^{-3}$ ($3.75 \times 10^{-3}$), the body quoting the top and saying so; and the deposit's energy, which sets the actual ratio above the floor.

## technical
Since superselection leaves the shared metric as the only channel, a dark tower can be heated after the descent only gravitationally. If the descent reheats this tower to $T_{\mathrm{desc}}$ and tower $r$, with $g_{d}$ light degrees of freedom that thermalise among themselves, is heated by graviton-mediated production at rate $\Gamma = c\,T^{8}/M_{P}^{4}$, the comoving yield is $Y = c\,T_{\mathrm{desc}}^{3}/(3\kappa_{s}M_{P}^{3})$ with $\kappa_{s} = 145.3$ at $g_{*} = g_{s} = 100$. The temperature ratio this alone gives is
$\xi_{\mathrm{floor}} = (4Y g_{*}/g_{d})^{1/4} = 9.6 \times 10^{-4}\,c^{1/4}(16/g_{d})^{1/4}(T_{\mathrm{desc}}/6 \times 10^{14}\,\mathrm{GeV})^{3/4}$.

This is a floor: the tower is hotter by whatever energy the descent deposited. Thereafter the ratio evolves through the two sectors' separate entropy conservation, and across the range of reheating temperatures up to the ceiling the floor spans a factor of about $4 \times 10^{-3}$. The result is proved given the imported rate and the standard thermal history.

## lay
Even if the hidden sectors started completely cold, the hot ordinary matter of the early universe would warm them slightly through gravity, the only contact left between the sectors. Taking the standard rate for this gravitational production, and assuming each hidden sector's light particles share their heat among themselves, this result calculates that minimum warmth: about a thousandth of our temperature or less, depending on how hot the early universe became. The real temperature could be higher if the universe's birth heated the hidden sectors directly.

## one-liner
Gravitational production from the visible plasma, at the imported rate, puts a floor $\xi_{\mathrm{floor}} \propto c^{1/4}T_{\mathrm{desc}}^{3/4}$ on the temperature ratio of a dark tower whose light species thermalise among themselves, $9.6 \times 10^{-4}\,c^{1/4}(16/g_{d})^{1/4}$ at the ceiling reheating.
