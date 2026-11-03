---
id: synthesis.imported-harrison-scott-mu-tau-reflection
kind: claim
version: 1
title: 'Imported: mu-tau reflection symmetry, |U_mu i| = |U_tau i| for every i, the exchange of mu and tau combined with CP, gives theta23 = pi/4 and delta = +-pi/2 in the standard parametrisation (Harrison and Scott 2002)'
status: imported
region: synthesis
subject: neutrinos
tags: [flavour-and-mixing, classical-theorem]
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
imported_from:
- citation: 'P. F. Harrison and W. G. Scott, mu-tau reflection symmetry in lepton mixing and neutrino oscillations, Phys. Lett. B 547 (2002), 219--228; arXiv:hep-ph/0210197.'
  key: HarrisonScott2002
  locator: 'eqs. (1) to (3), Section 2'
  doi: 10.1016/S0370-2693(02)02772-7
extraction:
  note: >-
    Imported so that synthesis.circulant-charged-leptons-excluded-with-real-neutrino-sectors can pin
    the pattern it names. Checked on 2026-11-01 against arXiv:hep-ph/0210197 (abstract page and
    PDF): title, authors, DOI; eq. (1), |U_mu i| = |U_tau i| exactly for i = 1, 2, 3 (strong mu-tau
    universality); Section 2, mu-tau reflection (eq. (2), with the vector u real) as the mu-tau
    exchange combined with CP on the whole leptonic sector, sufficient for eq. (1), and the
    parenthetic statement that eq. (1) corresponds to theta23 = pi/4 and delta = +-pi/2 in the
    standard parametrisation; eq. (3), |U_mu3| = ((1 - |U_e3|^2)/2)^(1/2). Their footnote attributes
    the circulant-basis case to an earlier paper, not checked. The journal volume and pages are from
    memory, consistent with the DOI.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of Harrison-Scott mu-tau reflection as a routine Fact, with a references entry).'
---

## formal
A lepton mixing matrix $U$ has strong $\mu$-$\tau$ universality when $|U_{\mu i}| = |U_{\tau i}|$ for $i = 1, 2, 3$. It holds when the theory is symmetric under $\mu$-$\tau$ reflection, the exchange of the $\mu$ and $\tau$ flavours combined with CP on the whole leptonic sector, and in the standard parametrisation it corresponds to $\theta_{23} = \pi/4$ and $\delta_{CP} = \pm\pi/2$ (with $s_{12}c_{12}s_{13}\cos\delta_{CP} = 0$ in general, so these values whenever $\theta_{13} \ne 0$); the third column then has $|U_{\mu 3}| = |U_{\tau 3}| = ((1 - |U_{e3}|^{2})/2)^{1/2}$. \emph{Provenance:} \cite{HarrisonScott2002} (eqs. (1) to (3), Section 2).

## technical
If the muon and tau neutrino flavours enter every mass eigenstate with equal weight, the atmospheric mixing angle is maximal and, unless the smallest angle vanishes, the leptonic CP phase is maximal too. Harrison and Scott identified the symmetry behind this pattern: exchanging the muon and tau flavours together with a CP conjugation.

## lay
Neutrino experiments find the muon and tau types mixed into the neutrino mass states in roughly equal amounts. A simple symmetry, swapping the two types while also swapping matter and antimatter, makes the amounts exactly equal and forces the matter-antimatter asymmetry of neutrino oscillations to be as large as it can be.

## one-liner
$|U_{\mu i}| = |U_{\tau i}|$ for all $i$ ($\mu$-$\tau$ reflection) means $\theta_{23} = \pi/4$ and $\delta_{CP} = \pm\pi/2$ for $\theta_{13} \ne 0$ (Harrison and Scott 2002).
