---
id: synthesis.imported-nielsen-olesen-string-tension
kind: claim
version: 1
title: 'Imported: the tension of a Nielsen-Olesen string is $\mu = 2\pi\epsilon(\beta)\eta^{2}$, with $\epsilon(1) = 1$ at the Bogomolny point and $\epsilon$ growing only logarithmically in $\beta$ (Nielsen and Olesen 1973; Bogomolny 1976)'
status: imported
region: synthesis
subject: dark-energy
tags: [symmetry-breaking, gauge-fields, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'H. B. Nielsen and P. Olesen, Vortex-line models for dual strings, Nucl. Phys. B 61 (1973), 45--61.'
  key: NielsenOlesen1973
  doi: 10.1016/0550-3213(73)90350-7
- citation: 'E. B. Bogomolny, The stability of classical solutions, Sov. J. Nucl. Phys. 24 (1976), 449--454.'
  key: Bogomolny1976
- citation: 'M. B. Hindmarsh and T. W. B. Kibble, Cosmic strings, Rep. Prog. Phys. 58 (1995), 477--562; arXiv:hep-ph/9411342.'
  key: HindmarshKibble1995
extraction:
  note: >-
    Imported so that the defect bound of the Pati-Salam chain can pin the tension it cites from
    memory (mu = 2 pi eps eta^2 with eps of order one). The Nielsen-Olesen reference (Nucl. Phys. B
    61, 45--61, 1973, and its DOI) was checked on 2026-10-31 against a bibliographic record. The
    Bogomolny value was rederived in the stated normalisation (|phi| -> eta, kinetic term |D phi|^2):
    the energy per unit length is bounded below by eta^2 times the gauge coupling times the flux
    2 pi n / e, that is 2 pi |n| eta^2, with equality at critical coupling. The large-beta growth
    eps ~ ln beta and the other citations are from memory; the normalisation of beta varies between
    sources and only its order of magnitude enters the citing result.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created by the maintainer pass of 2026-10-31 (literature cited from memory by an accepted result; Leon''s list of imports).'
---

## formal
In the Abelian Higgs model with complex scalar $\phi$, kinetic term $|D\phi|^{2}$, $D = \partial - ieA$, and potential $\tfrac{\lambda}{4}(|\phi|^{2} - \eta^{2})^{2}$, so that $|\phi| \to \eta$ in the vacuum, a straight static string of unit winding (the Nielsen-Olesen vortex) has energy per unit length
\[
\mu \;=\; 2\pi\,\epsilon(\beta)\,\eta^{2},
\]
with $\beta$ the squared ratio of the scalar to the vector mass. At the Bogomolny point $\beta = 1$ the bound $\mu \ge 2\pi|n|\eta^{2}$ for winding $n$ is saturated, so $\epsilon(1) = 1$; $\epsilon$ is increasing, of order one over a wide range, and grows like $\ln\beta$ for $\beta \gg 1$ (below $10$ for $\beta$ up to about $10^{4}$). The same holds, with $\eta$ the symmetry-breaking scale of the relevant scalar, for the strings of a non-Abelian breaking with $\pi_{1}(G/H) \neq 0$, up to factors of order one. \emph{Provenance:} \cite{NielsenOlesen1973}; \cite{Bogomolny1976}; \cite{HindmarshKibble1995}.

## technical
A gauge string, a tube of trapped magnetic flux in a Higgs vacuum, has a tension fixed by the symmetry-breaking scale: about $2\pi\eta^{2}$, exactly that at the special coupling where the scalar and vector masses are equal, and larger only by a slowly growing factor, roughly the logarithm of the mass ratio squared, otherwise. So the tension of any string of a breaking at scale $\eta$ is $G\mu \sim \eta^{2}/M_{\mathrm{Pl}}^{2}$ up to a factor of order one.

## lay
When a symmetry of the forces breaks, it can leave behind strings of trapped energy. Nielsen and Olesen found the basic example. How heavy such a string is per unit length is set almost entirely by the energy scale at which the symmetry broke: roughly that energy squared, times a number close to one.

## one-liner
A Nielsen-Olesen string of a breaking at scale $\eta$ has tension $\mu = 2\pi\epsilon\eta^{2}$, $\epsilon = 1$ at the Bogomolny point and of order one (growing like $\ln\beta$) otherwise (Nielsen and Olesen 1973; Bogomolny 1976).
