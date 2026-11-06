---
id: synthesis.imported-wands-duality-of-perturbation-spectra
kind: claim
version: 1
title: 'Imported: duality of perturbation spectra (Wands 1999)'
status: imported
region: synthesis
subject: dark-energy
tags: [classical-theorem, kasner]
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
- citation: 'D. Wands, Duality invariance of cosmological perturbation spectra, Phys. Rev. D 60 (1999), 023507; arXiv:gr-qc/9809062.'
  key: Wands1999
  locator: 'eqs. (2)-(5), (9), (10)'
  doi: 10.1103/PhysRevD.60.023507
extraction:
  note: >-
    Imported because the duality decides which contractions could mimic an inflationary spectrum in
    op.descent-state-and-spectrum (the stored Kasner index 3 sits at the self-dual point, and the
    dual of the measured tilt is a near-dust contraction). Checked on 2026-11-01 against
    arXiv:gr-qc/9809062 (abstract page and PDF): title, author, DOI, the mode equation u_k'' + (k^2
    + mu^2) u_k = 0 with mu^2 = -a''/a (eq. (2)), a = a_0 (eta/eta_0)^((1 - 2 nu)/2) with nu = 3/2 +
    1/(p - 1) for a proportional to t^p (eqs. (3), (4)), mu^2 = -(nu^2 - 1/4)/eta^2 (eq. (5)), the
    spectrum proportional to (-k eta)^(3 - 2|nu|) (eq. (9)), the transformation p -> (1 - 2p)/(2 -
    3p), equivalently nu -> -nu (eq. (10)), its fixed points p = 1/3 and p = 1, and the abstract's
    pair of exponential expansion and a collapse with a proportional to (-t)^(2/3). The index form n
    - 1 = 3 - 2|nu| is read off eq. (9); the journal reference is inferred from the DOI; the
    relation p = 2/(3(1 + w)) for a fluid of constant w is standard and cited from memory.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of Wands'' duality as a routine Fact).'
---

## formal
Let a spatially flat FLRW universe be the gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is $a^{2}(\eta)(d\eta^{2} - d\mathbf{x}^{2})$, with power-law scale factor $a \propto |t|^{p}$ in cosmic time, equivalently $a \propto |\eta|^{(1 - 2\nu)/2}$ with $\nu = \tfrac32 + \tfrac{1}{p - 1}$. For a massless minimally coupled scalar $\delta\phi$ the variable $u = a\,\delta\phi$ obeys $u_{k}'' + (k^{2} - a''/a)u_{k} = 0$ with $a''/a = (\nu^{2} - \tfrac14)/\eta^{2}$, and from the vacuum at early times the spectrum of $\delta\phi$ outside the Hubble length is $\mathcal{P}_{\delta\phi} \propto (-k\eta)^{3 - 2|\nu|}$, so $n - 1 = 3 - 2|\nu|$. This depends on $\nu$ only through $|\nu|$, so it is invariant under $\nu \to -\nu$, that is $p \to \tilde{p} = (1 - 2p)/(2 - 3p)$. The fixed points are $p = \tfrac13$ ($\nu = 0$, the stiff fluid, where the spectrum is $k^{3}$ up to a logarithm) and $p = 1$; exponential expansion ($|\nu| = \tfrac32$) and the collapse $a \propto (-t)^{2/3}$ ($\nu = -\tfrac32$) both give a scale-invariant spectrum. For a fluid of constant equation of state $w$, $p = 2/(3(1 + w))$. \emph{Provenance:} \cite{Wands1999} (eqs. (2) to (5), (9), (10)).

## technical
In conformal time the mode equation of a massless field on a power-law background has an effective mass $-a''/a$ that is the same for two different power laws, one expanding and one contracting. They therefore give the same spectrum of field fluctuations. Exponential inflation and a collapsing universe dominated by pressureless matter both give a scale-invariant spectrum; the stiff fluid ($w = 1$, $a \propto t^{1/3}$) is its own dual and gives the steepest blue spectrum, $k^{3}$ up to a logarithm. A small red tilt requires a background slightly away from one of the two scale-invariant cases on either side of the duality.

## lay
Wands noticed in 1998 that a universe that expands very fast and a universe that slowly collapses can imprint exactly the same pattern of ripples on a light field. This duality pairs every expanding history with a contracting one; a universe filled with the stiffest possible matter is paired with itself.

## one-liner
On $a \propto |t|^{p}$ a massless field exits with $n - 1 = 3 - 2|\nu|$, $\nu = \tfrac32 + 1/(p - 1)$, invariant under $p \to (1 - 2p)/(2 - 3p)$; $p = \tfrac13$ (stiff) is self-dual, and de Sitter is dual to the collapse $a \propto (-t)^{2/3}$ (Wands 1999).
