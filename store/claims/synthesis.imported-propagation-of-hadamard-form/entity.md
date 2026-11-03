---
id: synthesis.imported-propagation-of-hadamard-form
kind: claim
version: 1
title: 'Imported: the Hadamard form of a two-point function in a neighbourhood of one Cauchy surface propagates to the whole spacetime (Fulling, Sweeny and Wald 1978)'
status: imported
region: synthesis
subject: thermality
tags: [horizons, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'S. A. Fulling, M. Sweeny and R. M. Wald, Singularity structure of the two-point function in quantum field theory in curved spacetime, Commun. Math. Phys. 63 (1978), 257--264.'
  key: FullingSweenyWald1978
  doi: 10.1007/BF01196934
extraction:
  note: >-
    Imported so that the result on the microlocal condition on a horizon generator can pin the propagation
    step it cites, instead of citing it from memory. Checked on 2026-11-01 against the publisher's record of
    DOI 10.1007/BF01196934: title, authors, journal, volume 63, pages 257-264, year 1978, and the abstract (for
    the scalar field, if the anticommutator function G(x, x') has the Hadamard singularity structure in an
    open neighbourhood of a Cauchy surface it has it everywhere, "Cauchy evolution preserves the Hadamard
    singularity structure"; for a spacetime flat below a Cauchy surface the "in" vacuum is of Hadamard form
    everywhere). The micro-local proof of the same preservation is in Radzikowski 1996 (abstract checked, see
    synthesis.imported-microlocal-hadamard-condition). The Dirac-field analogue is not part of this Fact
    (not checked).
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decision of 2026-11-01 approving Fulling-Sweeny-Wald 1978 as a routine import, so that synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state cites it as a Fact; checked against the publisher''s record (see note).'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is globally hyperbolic, and let $G(x, x')$ be the anticommutator (symmetrised two-point) function of a state of the free scalar field. If $G$ has the Hadamard singularity structure in an open neighbourhood of one Cauchy surface, it has the Hadamard singularity structure everywhere: Cauchy evolution preserves the Hadamard form. In particular, for a gravitational field whose field strength vanishes below some Cauchy surface, the "in" vacuum is of Hadamard form everywhere. A micro-local proof of the preservation, by propagation of singularities, is in Radzikowski's work (Fact \claimref{synthesis.imported-microlocal-hadamard-condition}(a)). \emph{Provenance:} \cite{FullingSweenyWald1978}.

## technical
Fulling, Sweeny and Wald showed that the short-distance requirement on physical states of a free scalar field, the Hadamard form of the two-point function, does not have to be imposed everywhere: if it holds near one instant of time (an open neighbourhood of a Cauchy surface), the field equation carries it to the whole spacetime. So a field that starts in the vacuum of a flat region, before a star collapses for example, stays Hadamard throughout. Radzikowski later gave the same result a micro-local proof. The Dirac-field analogue is not part of this Fact.

## lay
If a quantum field looks like empty space up close at one moment, the laws of motion keep it that way at every later and earlier moment. Fulling, Sweeny and Wald proved this for the simplest fields in a gravitational field, so the requirement only has to be checked once, for instance before a black hole forms. This is taken from the literature.

## one-liner
For the free scalar field, a two-point function of Hadamard form in a neighbourhood of one Cauchy surface is of Hadamard form everywhere: Cauchy evolution preserves the Hadamard form (Fulling, Sweeny and Wald 1978).
