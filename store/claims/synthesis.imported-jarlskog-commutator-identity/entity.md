---
id: synthesis.imported-jarlskog-commutator-identity
kind: claim
version: 1
title: 'Imported: the determinant of the commutator of the quark mass squares is $2iJ$ times the six mass-squared differences (Jarlskog 1985)'
status: imported
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, classical-theorem]
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
- citation: 'C. Jarlskog, Commutator of the quark mass matrices in the standard electroweak model and a measure of maximal CP nonconservation, Phys. Rev. Lett. 55 (1985), 1039--1042.'
  key: Jarlskog1985
  doi: 10.1103/PhysRevLett.55.1039
- citation: S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024) 030001.
  key: PDG2024
  locator: 'Review 12, CKM quark-mixing matrix, Sec. 12.4 (definition of J)'
  doi: 10.1103/PhysRevD.110.030001
extraction:
  note: >-
    Imported for the up/down mixing results (synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing
    and synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns), which cite the identity from
    memory. Checked on 2026-10-26: the title, journal, volume, first page and year of Jarlskog 1985
    against the APS abstract page (the last page, 1042, is from memory); the definition and sign
    convention of J against the PDG 2024 CKM review, Sec. 12.4. The identity itself, with the sign
    and normalisation stated here, was verified by an exact computation over the Gaussian rationals:
    an exactly unitary V (Cayley transform of a Hermitian matrix with Gaussian-rational entries),
    H_u = diag(1, 5, 17), H_d = V diag(2, 3, 11) V^dag, gives det[H_u, H_d] = 2iJ F_u F_d exactly,
    with J = Im(V_us V_cb V_ub^* V_cs^*) equal to Im(V_ud V_cs V_us^* V_cd^*). The abstract of the
    source does not state the determinant form; it is attributed to the paper from memory. The bare
    i is the complex unit of the mass matrices' entries (an imported complex vector space), not I_4.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass of 2026-10-26 (Leon accepted the up/down mixing results and asked for this import); verified by an exact computation, bibliographic data checked.'
---

## formal
Let $H_{u}$, $H_{d}$ be $3 \times 3$ Hermitian matrices with eigenvalues $m_{u}^{2} < m_{c}^{2} < m_{t}^{2}$ and $m_{d}^{2} < m_{s}^{2} < m_{b}^{2}$, $H_{q} = U_{q}\,\mathrm{diag}(\cdot)\,U_{q}^{\dagger}$ with $U_{q}$ unitary, and $V = U_{u}^{\dagger}U_{d}$ (rows $u, c, t$, columns $d, s, b$). Let $J$ be defined by $\mathrm{Im}[V_{ij}V_{kl}V_{il}^{*}V_{kj}^{*}] = J\sum_{m,n}\epsilon_{ikm}\epsilon_{jln}$, so that $J = \mathrm{Im}(V_{us}V_{cb}V_{ub}^{*}V_{cs}^{*})$; it does not depend on the phases of the columns of $U_{u}$ and $U_{d}$. Then
\[
\det[H_{u}, H_{d}] = 2iJ\,F_{u}F_{d},\qquad F_{u} = (m_{t}^{2} - m_{c}^{2})(m_{t}^{2} - m_{u}^{2})(m_{c}^{2} - m_{u}^{2}),\quad F_{d} = (m_{b}^{2} - m_{s}^{2})(m_{b}^{2} - m_{d}^{2})(m_{s}^{2} - m_{d}^{2}).
\]
In particular, with nondegenerate masses in each sector, $J = 0$ if and only if $\det[H_{u}, H_{d}] = 0$; a common eigenvector of $H_{u}$ and $H_{d}$ gives $\det[H_{u}, H_{d}] = 0$ and so $J = 0$. \emph{Provenance:} \cite{Jarlskog1985}; the definition of $J$ as in \cite{PDG2024}.

## technical
Quark mixing violates the symmetry between matter and antimatter through one number, the Jarlskog invariant $J$, read from the mixing matrix as the imaginary part of a product of four of its entries. Jarlskog showed that it can be read from the mass matrices directly, without diagonalising them: the determinant of the commutator of the up-type and down-type mass squares equals $2iJ$ times the product of all six mass-squared differences within the two sectors. So, when no two masses in a sector are equal, CP violation in quark mixing is absent exactly when that determinant vanishes, and in particular whenever the two mass squares share an eigenvector.

## lay
The way quarks of different families mix carries one number that measures how much nature distinguishes matter from antimatter in this sector. This standard identity shows that the number can be computed straight from the quark mass matrices, from how far the up-type and down-type matrices fail to commute. If they share even one common direction, the number is zero.

## one-liner
$\det[H_{u}, H_{d}] = 2iJ\,(m_{t}^{2} - m_{c}^{2})(m_{t}^{2} - m_{u}^{2})(m_{c}^{2} - m_{u}^{2})(m_{b}^{2} - m_{s}^{2})(m_{b}^{2} - m_{d}^{2})(m_{s}^{2} - m_{d}^{2})$ with $J = \mathrm{Im}(V_{us}V_{cb}V_{ub}^{*}V_{cs}^{*})$, so $J = 0$ when the mass squares share an eigenvector (Jarlskog 1985).
