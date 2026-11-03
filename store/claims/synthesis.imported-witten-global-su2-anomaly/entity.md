---
id: synthesis.imported-witten-global-su2-anomaly
kind: claim
version: 1
title: 'Imported: Witten''s global $SU(2)$ anomaly; a four-dimensional $SU(2)$ gauge theory with an odd number of left-handed fermion doublets (and no other representations) is inconsistent, so a consistent theory has an even number of them (Witten 1982)'
status: imported
region: synthesis
subject: standard-model
tags: [hypercharge-and-anomalies, gauge-fields, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-02
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'E. Witten, An SU(2) anomaly, Phys. Lett. B 117 (1982), no. 5, 324--328.'
  key: Witten1982
  doi: 10.1016/0370-2693(82)90728-6
extraction:
  note: >-
    Imported so that the result on the generation number can pin the evenness of the number of weak doublets
    instead of citing it from memory. Checked on 2 November 2026 against the publication record (Princeton
    University research portal): title, author, Phys. Lett. B 117, issue 5, pages 324--328, 18 November 1982,
    DOI 10.1016/0370-2693(82)90728-6, and the abstract: a new restriction on fermion quantum numbers in gauge
    theories; an SU(2) gauge theory with an odd number of left-handed fermion doublets (and no other
    representations) is mathematically inconsistent. The mechanism stated in the formal level (the sign of the
    fermion integral under the gauge transformation of the nontrivial class of pi_4(SU(2)) = Z_2, from the mod-two
    count of fermion zero modes) is cited from memory.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Created by the maintainer pass of 2 November 2026, by Leon''s list of routine imports (Witten 1982), for the result on the generation number.'
---

## formal
In four dimensions, an $SU(2)$ gauge theory whose fermions are an odd number of left-handed Weyl doublets, and no other representations, is mathematically inconsistent: since $\pi_{4}(SU(2)) = \mathbb{Z}_{2}$ there are gauge transformations not continuously connected to the identity, under which the fermion integral of one doublet changes sign, so with an odd number of doublets the partition function and every gauge-invariant expectation value vanish \cite{Witten1982}. A consistent theory of this kind has an even number of left-handed doublets.

## technical
Besides the perturbative (triangle) anomalies there is a global one for the weak isospin group: a single left-handed doublet, or any odd number of them, makes the theory ill defined, because a topologically nontrivial gauge transformation flips the sign of the fermion integral. Each Standard Model generation has four doublets (three colours of quark and one lepton), so the condition holds for any number of generations.

## lay
Witten found that a theory with the weak force acting on an odd number of left-handed particle pairs cannot be consistent, whatever else it contains. Each family of ordinary matter has four such pairs, so any number of families passes this test; it cannot be used to fix how many families there are.

## one-liner
An $SU(2)$ gauge theory with an odd number of left-handed fermion doublets is inconsistent ($\pi_{4}(SU(2)) = \mathbb{Z}_{2}$ flips the sign of the fermion integral), so the number of doublets must be even (Witten 1982).
