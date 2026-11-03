---
id: dark-matter.imported-massless-graviton-production-rate
kind: claim
version: 1
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
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported; levels only.
---

## formal
Dark matter produced from the Standard-Model plasma by massless graviton exchange has rate per volume
\[
R(T) \;=\; \frac{\alpha\,T^{8}}{M_{P}^{4}}, \qquad M_{P} = 2.435 \times 10^{18}\ \mathrm{GeV},
\]
the reduced Planck mass, with $\alpha = 1.9 \times 10^{-4}$, $1.1 \times 10^{-3}$, $2.3 \times 10^{-3}$ for one scalar, one fermion and one vector \emph{produced} species respectively, the sum over the Standard-Model bath being inside the coefficient, weighted as $4|\mathcal{M}^{0}|^{2} + 45|\mathcal{M}^{1/2}|^{2} + 12|\mathcal{M}^{1}|^{2}$ over its scalar, Weyl-fermion and vector degrees. \emph{Provenance:} \cite{Bernal2018}, Eq.~(31), $R^{0}(T) = (3997\pi^{3}/663552000)\,T^{8}/M_{P}^{4}$ for the scalar case, and Table I, the massless-graviton limit of that paper's massive spin-2 mediator. Imported at assembly level: whether the fermion coefficient is per Weyl or per Dirac species is carried as a bracket; the factor between counting particles and pairs, and the mean energy per quantum, are absorbed into a factor of at most $2^{1/4}$ on the temperature ratio below.

## technical
Matter produced from the Standard-Model plasma by massless graviton exchange is created at a rate per volume $R(T) = \alpha\,T^{8}/M_{P}^{4}$, with $M_{P} = 2.435 \times 10^{18}$ GeV the reduced Planck mass. The coefficient is $\alpha = 1.9 \times 10^{-4}$, $1.1 \times 10^{-3}$ and $2.3 \times 10^{-3}$ for one produced scalar, fermion and vector species, the sum over the Standard-Model bath already inside it. The result is the massless limit of a massive spin-2 mediator calculation, imported at assembly level: whether the fermion coefficient is per Weyl or per Dirac species is carried as a bracket, and the particle-versus-pair factor and the mean energy per quantum are absorbed into a factor of at most $2^{1/4}$ on the temperature ratio.

## lay
Even matter that feels no force but gravity is produced in a hot early universe, because ordinary particles colliding can occasionally create it through gravity. This imported result gives the rate, which rises very steeply with temperature, for producing scalar, fermion and vector particles. It is the input that fixes how warm gravity alone can make the hidden worlds.

## one-liner
Graviton exchange from the Standard-Model plasma produces a species at rate $\alpha T^{8}/M_{P}^{4}$, with $\alpha$ of order $10^{-4}$ to $10^{-3}$ for scalars, fermions and vectors.
