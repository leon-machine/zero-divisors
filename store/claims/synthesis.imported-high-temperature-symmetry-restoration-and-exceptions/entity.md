---
id: synthesis.imported-high-temperature-symmetry-restoration-and-exceptions
kind: claim
version: 1
title: 'Imported: thermal corrections generically restore a spontaneously broken gauge symmetry above a temperature of order its scale, with exceptions when scalar cross-couplings are negative, including a range of minimal SU(5) (Kirzhnits and Linde 1972, Dolan and Jackiw 1974, Weinberg 1974, Dvali, Melfo and Senjanovic 1995)'
status: imported
region: synthesis
subject: dark-matter
tags: [symmetry-breaking, classical-theorem]
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
- citation: 'D. A. Kirzhnits and A. D. Linde, Macroscopic consequences of the Weinberg model, Phys. Lett. B 42 (1972), 471--474.'
  key: KirzhnitsLinde1972
- citation: 'L. Dolan and R. Jackiw, Symmetry behavior at finite temperature, Phys. Rev. D 9 (1974), 3320--3341.'
  key: DolanJackiw1974
- citation: 'S. Weinberg, Gauge and global symmetries at high temperature, Phys. Rev. D 9 (1974), 3357--3378.'
  key: Weinberg1974
- citation: 'G. Dvali, A. Melfo and G. Senjanovic, Is there a monopole problem?, Phys. Rev. Lett. 75 (1995), 4559--4562; arXiv:hep-ph/9507230.'
  key: DvaliMelfoSenjanovic1995
  doi: 10.1103/PhysRevLett.75.4559
extraction:
  note: >-
    Imported as input (e) of synthesis.pati-salam-monopoles-bound-descent-history, which cites it
    from memory. Checked on 2026-10-26: Dvali, Melfo and Senjanovic against the arXiv abstract of
    hep-ph/9507230 (high-temperature behaviour of minimal SU(5); ranges of the Higgs potential's
    parameters in which the symmetry stays broken at high temperature, so the monopole-producing
    transition is avoided, and thermal monopole production suppressed); Weinberg 1974 (volume and pages)
    and Dolan and Jackiw 1974 (volume and pages) against the reference list of arXiv:hep-ph/9801313,
    which credits Weinberg with the observation that multi-scalar models can show more breaking at
    higher temperature. The one-loop form of the thermal mass, the generic restoration statement and
    Kirzhnits and Linde 1972 are cited from memory.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: monopole input (e), cited from memory by the Pati-Salam monopole result, to be imported as a Fact).'
---

## formal
In a gauge theory with scalar fields $\phi_{a}$ at temperature $T$ well above the masses, the one-loop thermal correction to the effective potential adds $\tfrac12 c_{ab}T^{2}\phi_{a}\phi_{b}$, with $c_{ab}$ set by the gauge, Yukawa and quartic couplings. When every eigenvalue of $c$ is positive (as for a single scalar, or for positive cross-couplings) the broken symmetry is restored above a critical temperature of order its breaking scale. With several scalars, negative cross-couplings can make an eigenvalue of $c$ negative while the zero-temperature potential stays bounded below, and then a symmetry broken at $T = 0$ stays broken at high temperature, or a symmetric one breaks (symmetry non-restoration, inverse breaking). In minimal SU(5) a range of the Higgs potential's parameters keeps the grand-unified symmetry broken at high temperature, so the transition that would produce monopoles does not occur. \emph{Provenance:} \cite{KirzhnitsLinde1972}, \cite{DolanJackiw1974}, \cite{Weinberg1974} (restoration and its exceptions); \cite{DvaliMelfoSenjanovic1995} (the SU(5) range and the monopole problem).

## technical
Heating usually undoes symmetry breaking: the thermal bath gives the Higgs fields a positive mass squared proportional to the temperature squared, which wins over the negative one that breaks the symmetry, so above a critical temperature the symmetric phase returns and the broken phase forms again on cooling. Weinberg observed that this is not universal: with several scalar fields and negative cross-couplings the thermal mass can be negative in some direction, and the symmetry stays broken however hot the bath. Dvali, Melfo and Senjanovic found such a range in minimal SU(5) and noted that it removes the transition that would make monopoles. Whether the series' Pati-Salam breaking is restored at high temperature therefore depends on its scalar couplings.

## lay
A hot enough universe usually restores the symmetries that are broken today, so they must break again as it cools, making magnetic poles. In some theories, with the right kind of interactions between the Higgs fields, heat does not restore the symmetry, and the problem is avoided.

## one-liner
Thermal masses $\tfrac12 c_{ab}T^{2}\phi_{a}\phi_{b}$ generically restore a broken gauge symmetry at high temperature; with negative scalar cross-couplings it can stay broken, as in a range of minimal SU(5), avoiding monopole production (Kirzhnits-Linde, Dolan-Jackiw, Weinberg; Dvali-Melfo-Senjanovic).
