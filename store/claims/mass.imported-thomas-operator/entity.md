---
id: mass.imported-thomas-operator
kind: claim
version: 2
title: 'Imported: the Thomas operator'
status: imported
region: mass
subject: einstein
tags: [classical-theorem, tractors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
imported_from:
- citation: T. Y. Thomas, On conformal geometry, Proc. Natl. Acad. Sci. USA 12 (1926), 352--359.
  key: Thomas1926
- citation: T. N. Bailey, M. G. Eastwood, and A. R. Gover, Thomas's structure bundle for conformal, projective
    and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217.
  key: BEG1994
- citation: A. R. Gover, Almost Einstein and Poincar'e-Einstein manifolds in Riemannian signature, J.
    Geom. Phys. 60 (2010), 182--204.
  key: Gover2010
locators:
  paper: T11
  number: Fact 2.2
  label: fact:thomas
  line: 414
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the scale g is the derived metric of a gravitational field on flat spacetime, the tractors are the Cl(2,4) vectors and the Einstein condition is the parallelism of the scale tractor for the tractor gauge field; content unchanged.'
  typing:
    by: ai-typing-pass
    note: Imported claim; the context_refs are consistency checks within the paper, not premises, so no
      derivation was added.
  env: fact
  context_refs:
  - mass.de-sitter-scale-frozen-point
  - mass.imported-frozen-point-tractor-connection
  - mass.weight-polynomial-two-series
  eqrefs: 1
---

## formal
Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with tractors the vectors $\sigma\nInf + \mu + \rho\nO$ of $\Cl(2,4)$. On a density $\sigma$ of conformal weight $w$ the Thomas operator $D$ produces the tractor
\[
D\sigma = \bigl(\, w(n+2w-2)\,\sigma,\;\; (n+2w-2)\,\nabla_{a}\sigma,\;\; -(\Box\sigma - wJ\sigma)\,\bigr)
\]
in the splitting of a scale $g$, and $D\sigma$ is conformally invariant as a weight-$(w-1)$ tractor field. For $w = 1$ and a scale $\sigma$, $\tfrac1n D\sigma$ is the scale tractor of $\sigma$, whose parallelism, for the tractor gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, is the Einstein condition of Fact \claimref{mass.imported-frozen-point-tractor-connection}. \emph{Provenance:} Thomas's prolongation \cite{Thomas1926}, in the form of \cite{BEG1994}; see also \cite{Gover2010}. The sign of the $J$-term follows the sign of the Schouten tensor in the connection, and within the convention of \eqref{eq:tractorconn} it is the one displayed: at $w = 1$ on the constant density $1$ of an Einstein scale the display returns $(1, 0, J/4) = (1, 0, \Lambda/6)$, the frozen point of Fact \claimref{mass.imported-frozen-point-tractor-connection}, a consistency the paper's own computations confirm (Lemma \claimref{mass.de-sitter-scale-frozen-point}(1), Corollary \claimref{mass.weight-polynomial-two-series}(2)). No translation between conventions is used.

## technical
On a density $\sigma$ of conformal weight $w$ the Thomas operator gives, in the splitting of a scale $g$, $D\sigma = (w(n+2w-2)\sigma,\ (n+2w-2)\nabla_a\sigma,\ -(\Box\sigma - wJ\sigma))$, a conformally invariant tractor field of weight $w - 1$. For $w = 1$ and a scale $\sigma$, $\tfrac1n D\sigma$ is the scale tractor of $\sigma$, whose parallelism is the Einstein condition.

The sign of the $J$-term follows the sign of the Schouten tensor in the series' connection: at $w = 1$ on the constant density $1$ of an Einstein scale it returns $(1, 0, \Lambda/6)$, the frozen point. Imported from Thomas, in the form of Bailey, Eastwood and Gover.

## lay
The Thomas operator is a standard tool of conformal geometry that turns a scale-dependent quantity into an object that does not depend on the choice of scale. Applied to a choice of scale itself, it produces the scale tractor, and an Einstein scale gives the frozen point. This classical construction is imported in the sign convention the series uses.

## one-liner
The Thomas operator sends a weight-$w$ density to a conformally invariant tractor, and at $w = 1$ it produces the scale tractor, which is the frozen point for an Einstein scale.
