---
id: dark-matter.imported-massless-graviton-production-rate
kind: claim
version: 3
title: 'Imported: the massless-graviton production rate'
status: imported
region: dark-matter
subject: dark-matter
tags: [quantum-gravity, matter-asymmetry]
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
- name: Claude Opus 5.5
  role: 'maintainer pass, reduced Planck mass letter at Leon''s decisions'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: 'flag at every level: the Fact imports a process of a quantised gravitational field, which the series does not hold; rate and coefficients unchanged'
  version: 3
  source: maintainer pass of 2026-11-10
review: typed
imported_from:
- citation: N. Bernal, M. Dutra, Y. Mambrini, K. Olive, M. Peloso, and M. Pierre, Spin-2 portal dark matter,
    Phys. Rev. D 97 (2018), 115020.
  key: Bernal2018
locators:
  paper: T14
  number: Fact A.1
  label: fact:alpha
  line: 1467
extraction:
  flags:
  - 'imports a process of a quantised gravitational field (exchange of a quantum of a spin-2 mediator), which the series does not hold; every result that uses it holds conditionally on the rate; open problem op.graviton-rate-as-classical-field-process'
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 2 -> 3, by Leon''s decision of 10 November 2026 (flag now, derive later). A flag paragraph is added at every level: the rate is computed in its source from the exchange of a quantum of a spin-2 field, the series holds no quantum of the gravitational field (conventions, section "Gravity and the graviton"), and the results that use the Fact rest on it conditionally. The rate, its coefficients and the provenance are unchanged, and no dependant is edited in this pass except the three predictions that carry a pointing sentence. The open problem op.graviton-rate-as-classical-field-process asks for the rate as a process of the classical gauge field sourced by matter, or a proof that it vanishes, and lists what rests on the Fact.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Decision item F14 (routine): the reduced Planck mass 2.435e18 GeV is written bar M_P = M_P/sqrt(8 pi) (quantity.reduced-planck-mass), not M_P, the letter of the non-reduced quantity.planck-mass (1.22e19 GeV), at every level; the provenance keeps Bernal et al.''s M_P with a note that the source writes it for the reduced mass. Notation; values unchanged.'
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported; levels only.
---

## formal
Dark matter produced from the Standard-Model plasma by massless graviton exchange has rate per volume
\[
R(T) \;=\; \frac{\alpha\,T^{8}}{\bar{M}_{P}^{4}}, \qquad \bar{M}_{P} = 2.435 \times 10^{18}\ \mathrm{GeV},
\]
the reduced Planck mass $\bar{M}_{P} = M_{P}/\sqrt{8\pi}$ ($M_{P}$ the non-reduced mass), with $\alpha = 1.9 \times 10^{-4}$, $1.1 \times 10^{-3}$, $2.3 \times 10^{-3}$ for one scalar, one fermion and one vector \emph{produced} species respectively, the sum over the Standard-Model bath being inside the coefficient, weighted as $4|\mathcal{M}^{0}|^{2} + 45|\mathcal{M}^{1/2}|^{2} + 12|\mathcal{M}^{1}|^{2}$ over its scalar, Weyl-fermion and vector degrees. \emph{Provenance:} \cite{Bernal2018}, Eq.~(31), $R^{0}(T) = (3997\pi^{3}/663552000)\,T^{8}/M_{P}^{4}$ for the scalar case (the source writes $M_{P}$ for the reduced mass $\bar{M}_{P}$), and Table I, the massless-graviton limit of that paper's massive spin-2 mediator. Imported at assembly level: whether the fermion coefficient is per Weyl or per Dirac species is carried as a bracket; the factor between counting particles and pairs, and the mean energy per quantum, are absorbed into a factor of at most $2^{1/4}$ on the temperature ratio below.

\emph{Flag (10 November 2026): a process the series does not hold.} In its source the rate is computed from the exchange of a quantum of a spin-2 field between the plasma and the produced species. The series holds no quantum of the gravitational field: gravity here is the classical gauge field of Gauge Theory Gravity (conventions, section ``Gravity and the graviton''). The Fact is therefore an import from outside the series' own content, and every result that uses it holds conditionally on the rate. It is not known whether the classical gauge field sourced by matter gives this rate, another rate or none; that is open problem op.graviton-rate-as-classical-field-process. No number above is changed by this flag.

## technical
Matter produced from the Standard-Model plasma by massless graviton exchange is created at a rate per volume $R(T) = \alpha\,T^{8}/\bar{M}_{P}^{4}$, with $\bar{M}_{P} = 2.435 \times 10^{18}$ GeV the reduced Planck mass. The coefficient is $\alpha = 1.9 \times 10^{-4}$, $1.1 \times 10^{-3}$ and $2.3 \times 10^{-3}$ for one produced scalar, fermion and vector species, the sum over the Standard-Model bath already inside it. The result is the massless limit of a massive spin-2 mediator calculation, imported at assembly level: whether the fermion coefficient is per Weyl or per Dirac species is carried as a bracket, and the particle-versus-pair factor and the mean energy per quantum are absorbed into a factor of at most $2^{1/4}$ on the temperature ratio. Flag: the source computes the rate from the exchange of a quantum of a spin-2 field, and the series holds no quantum of the gravitational field, which in it is the classical gauge field of Gauge Theory Gravity; results that use this rate hold conditionally on it, and deriving it as a process of the classical field sourced by matter, or showing that it vanishes, is open problem op.graviton-rate-as-classical-field-process.

## lay
Even matter that feels no force but gravity is produced in a hot early universe, because ordinary particles colliding can occasionally create it through gravity. This imported result gives the rate, which rises very steeply with temperature, for producing scalar, fermion and vector particles. It is the input that fixes how warm gravity alone can make the hidden worlds. A caution: the calculation it is taken from treats gravity as carried by particles, gravitons, and in this collection gravity is a classical field with no such particle. Whether the classical field produces matter at the same rate, at a different one or not at all has not been worked out, so everything in the collection that uses this rate holds only if the rate does.

## one-liner
Graviton exchange from the Standard-Model plasma produces a species at rate $\alpha T^{8}/\bar{M}_{P}^{4}$, with $\alpha$ of order $10^{-4}$ to $10^{-3}$ for scalars, fermions and vectors; flagged: the rate is imported from a calculation with a quantised gravitational field, which the series does not hold, so its users hold conditionally on it (open problem op.graviton-rate-as-classical-field-process).
