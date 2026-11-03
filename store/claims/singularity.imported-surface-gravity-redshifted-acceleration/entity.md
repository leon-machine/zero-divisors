---
id: singularity.imported-surface-gravity-redshifted-acceleration
kind: claim
version: 2
title: 'Imported: surface gravity as redshifted acceleration'
status: imported
region: singularity
subject: thermality
tags: [classical-theorem, hawking-temperature, horizons]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: R. M. Wald, General Relativity, University of Chicago Press (1984)
  locator: §12.5
locators:
  paper: T05
  number: Fact A.1
  label: fact:kappa
  line: 2579
extraction:
  env: fact
  flags:
  - citation taken from inline provenance (no \cite)
  typing:
    by: ai-typing-pass
    note: imported fact with no derivation; the statement cites Wald in its provenance clause although
      the extraction flagged it as uncited
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Killing field, the horizon locus, the surface gravity (K.D)K = kappa K and the static observers are written with the covariant derivative D of the gravitational field on flat spacetime; the redshift factor is sqrt(Q(K)). Wald''s content unchanged.'
---

## formal
Let $(\hb, \Omega)$ be a static gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with a static Killing horizon: a Killing field $K$, a physical vector field whose covariant derivative $A \mapsto A \cdot D K$ is antisymmetric in the flat product, and a locus of the background on which $Q(K) = 0$ and $K$ is normal to it. The surface gravity defined on the horizon locus by $(K \cdot D)K = \kappa\,K$ equals the limit, at the horizon locus, of the proper acceleration of static observers (velocity $v = K/\sqrt{Q(K)}$, acceleration $(v \cdot D)v$) multiplied by the redshift factor $\sqrt{Q(K)}$; $Q(K)$ is the derived-metric norm $g(\xi,\xi)$ of the Killing vector $\xi$ over which $K$ sits (Fact \claimref{synthesis.imported-gtg-dictionary}, clause (vi)). \emph{Provenance:} R.~M.~Wald, General Relativity, University of Chicago Press (1984), \S 12.5, read in Gauge Theory Gravity through the dictionary.

## technical
For a static Killing horizon of a gravitational field on flat spacetime, with Killing field $K$, the surface gravity $\kappa$, defined on the horizon locus by $(K \cdot D)K = \kappa\,K$, equals the horizon limit of the proper acceleration $(v \cdot D)v$ of static observers, $v = K/\sqrt{Q(K)}$, multiplied by the redshift factor $\sqrt{Q(K)}$.

This is a standard textbook result, imported without proof; it is Wald's statement read through the dictionary between Gauge Theory Gravity and the language of the derived metric.

## lay
Surface gravity is the number that measures the strength of gravity at a black hole's horizon. Take the acceleration an observer needs to hover at a fixed position, correct it for the gravitational redshift, and follow it down to the horizon. This standard result says that the limit reached there is the surface gravity.

## one-liner
For a static Killing horizon, the surface gravity, $(K \cdot D)K = \kappa K$ on the horizon locus, equals the horizon limit of the redshift-weighted proper acceleration of static observers.
