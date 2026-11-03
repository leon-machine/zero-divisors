---
id: synthesis.imported-macro-monopole-flux-limit
kind: claim
version: 1
title: 'Imported: the MACRO final upper limit on the flux of magnetic monopoles, 1.4 x 10^-16 cm^-2 s^-1 sr^-1 at 90% confidence for 4 x 10^-5 < beta < 1 (MACRO Collaboration 2002)'
status: imported
region: synthesis
subject: dark-matter
tags: [confronted-with-data, symmetry-breaking]
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'M. Ambrosio et al. (MACRO Collaboration), Final results of magnetic monopole searches with the MACRO experiment, Eur. Phys. J. C 25 (2002), 511--522; arXiv:hep-ex/0207020.'
  key: MACRO2002
  doi: 10.1140/epjc/s2002-01046-9
extraction:
  note: >-
    Imported as input (d) of synthesis.pati-salam-monopoles-bound-descent-history, which cites it
    from memory. Checked on 2026-10-26 against the arXiv abstract of hep-ex/0207020 and the journal
    listing: title, collaboration, DOI 10.1140/epjc/s2002-01046-9, the use of all three sub-detectors,
    no candidates, the 90% confidence upper limit 1.4 x 10^-16 cm^-2 s^-1 sr^-1 over
    4 x 10^-5 < beta < 1, described as the first direct limit well below the Parker bound over the whole
    range where grand-unified monopoles are expected. The page range 511-522 and the first author are from
    memory. The abstract does not state the magnetic charge; the limit is read here for monopoles of one
    Dirac unit or more, as remembered.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: monopole input (d), cited from memory by the Pati-Salam monopole result, to be imported as a Fact).'
---

## formal
The MACRO experiment at Gran Sasso, using its scintillation counters, limited streamer tubes and nuclear track detectors separately and in combination, found no magnetic monopole candidate and set the 90\% confidence upper limit
\[
\mathcal{F} \;<\; 1.4 \times 10^{-16}\ \mathrm{cm}^{-2}\,\mathrm{s}^{-1}\,\mathrm{sr}^{-1}
\]
on the local flux of magnetic monopoles over the velocity range $4 \times 10^{-5} < \beta < 1$, below the Parker bound over the whole range where grand-unified monopoles are expected (read for magnetic charge of one Dirac unit or more, as remembered). \emph{Provenance:} \cite{MACRO2002}.

## technical
MACRO was a large underground detector built in part to look for magnetic monopoles from the early universe. Its final analysis found none and limited their flux through the Earth to below $1.4 \times 10^{-16}$ per square centimetre per second per steradian, for any speed from a few times $10^{-5}$ of light speed upwards. Converted to a number density with the monopoles' speed, at least the halo's virial speed for galactic monopoles, this bounds the monopole-to-entropy ratio today, the bound a causal grand-unified transition must meet.

## lay
A large underground experiment looked for magnetic poles left over from the early universe and found none. Its result limits how many can be passing through the Earth, and so how many the early universe can have made.

## one-liner
MACRO found no monopoles: the local flux is below $1.4 \times 10^{-16}$ cm$^{-2}$ s$^{-1}$ sr$^{-1}$ (90\% confidence) for $4 \times 10^{-5} < \beta < 1$ (MACRO Collaboration 2002).
