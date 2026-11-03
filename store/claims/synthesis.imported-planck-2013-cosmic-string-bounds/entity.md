---
id: synthesis.imported-planck-2013-cosmic-string-bounds
kind: claim
version: 1
title: 'Imported: Planck bounds on cosmic strings, $G\mu < 1.5 \times 10^{-7}$ ($f_{10} < 0.015$) for Nambu-Goto and $G\mu < 3.2 \times 10^{-7}$ ($f_{10} < 0.028$) for Abelian-Higgs strings (Planck 2013 XXV)'
status: imported
region: synthesis
subject: dark-energy
tags: [confronted-with-data, symmetry-breaking]
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
- citation: 'Planck Collaboration (P. A. R. Ade et al.), Planck 2013 results. XXV. Searches for cosmic strings and other topological defects, Astron. Astrophys. 571 (2014), A25; arXiv:1303.5085.'
  key: Planck2013XXV
  doi: 10.1051/0004-6361/201321621
extraction:
  note: >-
    Imported so that the defect bound of the Pati-Salam chain can pin the string bounds it cites
    from memory. The four numbers were checked on 2026-10-31 against the abstract of
    arXiv:1303.5085 (Nambu-Goto G mu/c^2 < 1.5e-7 and f_10 < 0.015 at 95 per cent confidence;
    Abelian-Higgs G mu/c^2 < 3.2e-7 and f_10 < 0.028), and the journal reference (A&A 571, A25,
    2014) against a bibliographic record. The DOI and the quadratic scaling of the string spectrum
    with G mu (how the bounds on G mu and on f_10 correspond) are cited from memory.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created by the maintainer pass of 2026-10-31 (literature cited from memory by an accepted result; Leon''s list of imports).'
---

## formal
Fitting the Planck 2013 temperature power spectrum with a $\Lambda$CDM model plus the power of a scaling cosmic-string network, whose angular power spectrum is proportional to $(G\mu)^{2}$ for a given string model, and writing $f_{10}$ for the strings' fraction of the temperature power at multipole $\ell = 10$:
\begin{enumerate}
\item[(i)] Nambu-Goto strings: $G\mu/c^{2} < 1.5 \times 10^{-7}$ and $f_{10} < 0.015$ at $95$ per cent confidence;
\item[(ii)] Abelian-Higgs field-theory strings: $G\mu/c^{2} < 3.2 \times 10^{-7}$ and $f_{10} < 0.028$.
\end{enumerate}
Since $f_{10}$ is quadratic in $G\mu$ for each model, a network of tension $G\mu$ supplies $f_{10} = \kappa\,(G\mu)^{2}$ with $\kappa$ the ratio of the paired bounds, $\kappa = 0.015/(1.5 \times 10^{-7})^{2}$ and $0.028/(3.2 \times 10^{-7})^{2}$. \emph{Provenance:} \cite{Planck2013XXV}.

## technical
Moving cosmic strings would imprint their own pattern on the cosmic microwave background, with a power proportional to the square of their tension. Fitting the Planck 2013 data allowing for such a contribution bounds the tension at $G\mu < 1.5 \times 10^{-7}$ for idealised Nambu-Goto strings and $3.2 \times 10^{-7}$ for field-theory Abelian-Higgs strings, with the strings supplying at most $1.5$ and $2.8$ per cent of the temperature power at $\ell = 10$. Because the power scales as the square of the tension, these pairs fix the fraction any lighter network would supply.

## lay
If the early universe had produced a network of cosmic strings, thin lines of trapped energy, they would have left a characteristic pattern in the cosmic microwave background. The Planck satellite found no such pattern and set an upper limit on how heavy such strings could be: they could account for at most a few per cent of the observed ripples.

## one-liner
Planck 2013: $G\mu < 1.5 \times 10^{-7}$ with $f_{10} < 0.015$ for Nambu-Goto strings and $G\mu < 3.2 \times 10^{-7}$ with $f_{10} < 0.028$ for Abelian-Higgs strings, the string power scaling as $(G\mu)^{2}$.
