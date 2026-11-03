---
id: interior.imported-tractor-connection
kind: claim
version: 2
title: 'Imported: the tractor connection'
status: imported
region: interior
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
  source: authorship disclosure of T06, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: T. N. Bailey, M. G. Eastwood and A. R. Gover, Thomas's structure bundle for conformal, projective
    and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217.
  key: BEG1994
- citation: S. N. Curry and A. R. Gover, An introduction to conformal geometry and tractor calculus, with
    a view towards analysis on manifolds, in Asymptotic Analysis in General Relativity, London Mathematical
    Society Lecture Note Series 443, Cambridge University Press (2018), 86--170.
  key: CurryGover2018
  locator: \S 5
locators:
  paper: T06
  number: Fact 4.1
  label: fact:tractor
  line: 441
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the conformal class is that of the derived metric of a gravitational field on flat spacetime, on its invertible region, where the tractor bundle is trivialised in the scale g by the null pair and the physical vectors of Cl(2,4); the imported connection and its sign sentence are unchanged.'
  env: fact
  context_refs:
  - interior.sign-fixed-internally
  eqrefs: 2
  typing:
    by: ai-typing-pass
    note: 'Imported fact with no derivation, so the context reference to the internal sign lemma (which fixes a convention, not a premise of the import) is left unedged.'
---

## formal
Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) on its invertible region. The tractor bundle $\mathcal{T}$ of the conformal class $[g]$, trivialised in the scale $g$ by $\nInf$, the physical vectors and $\nO$ (the vectors $\sigma\nInf + \mu + \rho\nO$ of $\Cl(2,4)$), carries a canonical connection depending only on $[g]$, preserving the metric \eqref{eq:tractormetric}, whose expression in the scale $g$ is
\begin{equation}
\nabla_a(\sigma, \mu_b, \rho) \;=\; \bigl(\nabla_a\sigma - \mu_a,\;\; \nabla_a\mu_b + g_{ab}\,\rho - \Sch_{ab}\,\sigma,\;\; \nabla_a\rho + \Sch_a{}^{b}\mu_b\bigr),
\end{equation}
where $\nabla_a$ on $\mu$ is the covariant derivative $D$ of the gravitational field in the physical frame and $\Sch_{ab}$ is the Schouten tensor of $g$, the components of the Schouten map $\Sch(A) = \tfrac12\bigl(\mathcal{R}(A) - \tfrac16 A\,\mathcal{R}\bigr)$ of the field strength; in four dimensions $\Sch_{ab} = \tfrac12\bigl(\Ric_{ab} - \tfrac{R}{6}\,g_{ab}\bigr)$. \emph{Provenance:} Bailey-Eastwood-Gover \cite{BEG1994}; Curry-Gover \cite[\S 5]{CurryGover2018}. The display \eqref{eq:tractorconn} is their connection written in the curvature conventions of Section \ref{sec:setting}; the relative sign of the Schouten slots against those references is convention-dependent, and Lemma \claimref{interior.sign-fixed-internally} fixes it internally, so that no sign in this paper rests on a translation between conventions.

## technical
For a gravitational field on flat spacetime with derived metric $g$, the tractor bundle $\mathcal{T}$ of the conformal class $[g]$ is, on the invertible region, the vectors $\sigma\nInf + \mu + \rho\nO$ of $\Cl(2,4)$. It carries a canonical connection that depends only on $[g]$ and preserves the tractor metric. In the scale $g$ it reads $\nabla_a(\sigma,\mu_b,\rho) = \bigl(\nabla_a\sigma - \mu_a,\ \nabla_a\mu_b + g_{ab}\rho - \Sch_{ab}\sigma,\ \nabla_a\rho + \Sch_a{}^{b}\mu_b\bigr)$, with $\nabla$ on $\mu$ the gravitational covariant derivative, where in four dimensions the Schouten tensor is $\Sch_{ab} = \tfrac12\bigl(\Ric_{ab} - \tfrac{R}{6}g_{ab}\bigr)$, read from the field strength.

The connection is imported from the tractor-calculus literature. The relative sign of the Schouten slots against those references depends on curvature conventions, and it is fixed internally rather than by translating between conventions.

## lay
Gravity here is a pair of fields on flat spacetime, and what it determines, once lengths are allowed to be rescaled freely, is a conformal geometry. To it one can attach a larger bundle called the tractor bundle, whose fibres are the six-dimensional vectors of the series' conformal model, with a natural way of differentiating its sections. This imported result gives that derivative explicitly once a particular scale is chosen, in terms of the Schouten tensor, a rearranged form of the field strength. The derivative depends only on the conformal geometry and respects the bundle's own metric.

## one-liner
For a gravitational field on flat spacetime, the tractor bundle of its conformal class (the $\Cl(2,4)$ vectors $\sigma\nInf + \mu + \rho\nO$) carries a canonical metric-preserving connection, given in a chosen scale by an explicit formula involving the Schouten tensor.
