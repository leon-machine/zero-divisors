---
id: synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy
kind: claim
version: 2
title: 'The tower''s pairing gap at fixed charges is twice the quasiparticle energy'
status: proved
region: synthesis
subject: quantum-fields
tags: [pairing-and-bogoliubov, symmetry-breaking, mass-generation, recovers-known-physics, confronted-with-data]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - field-theory.composite-scalars-mean-field-level@4
  - field-theory.imported-tower-limit@3
  - field-theory.how-close-tower-comes-ccr@4
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@4
  - synthesis.imported-quasi-spin-pairing-and-top-condensation@1
  proof: proof-main.tex
quantities:
- quantity.higgs-boson-mass@1
- quantity.top-quark-mass@1
- quantity.z-boson-mass@2
checked_by:
- kind: check
  ref: check.py::check_closed_spectrum_on_floors
- kind: check
  ref: check.py::check_gap_at_fixed_charges_is_g_nb
- kind: check
  ref: check.py::check_mean_field_two_quasiparticle_energy
- kind: check
  ref: check.py::check_constituent_bound_against_record
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.composite-scalars-mean-field-level
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus
extraction:
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s list of imports of 2026-11-01: a uses edge to the imported Fact synthesis.imported-quasi-spin-pairing-and-top-condensation@1 (Kerman''s quasi-spin solution, the Nambu-Jona-Lasinio relation m_sigma = 2m as an analogy, Bardeen-Hill-Lindner and arXiv:1906.09579), which replaces the citations from memory; the pin of synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus moves to @3 (a marked note added there, content unchanged). Statement and check unchanged.'
  open_problem: op.qft-bosons-and-the-rung-field
  note: >-
    The problem's second line of attack (fluctuations of the tower's composite scalars beyond mean field),
    taken from outside the series: top condensation (Bardeen, Hill and Lindner) and the Nambu relation
    m_sigma = 2m of the Nambu-Jona-Lasinio model. The stored pairing element H_4 is the degenerate
    (single-shell) pairing model; its exact spectrum is the quasi-spin (seniority) spectrum (Kerman 1961,
    imported in synthesis.imported-quasi-spin-pairing-and-top-condensation), certified here exactly on all sectors of the n_b = 2, 3 floors at eight (K, G). At equal numbers
    the first excitation above the band breaks a pair and costs exactly G n_b, which is twice the mean-field
    quasiparticle energy E = G n_b/2: the pair-breaking (two-quasiparticle) threshold, 2E >= 2 Delta, equal to
    2 Delta on the shell K = 0. The uniform scalar channel does not reach it on a floor, so its relation to
    Nambu's m_sigma = 2m is an analogy (argued). Outside comparison (imported, the same Fact;
    arXiv 1906.09579): in the one-doublet top-condensation model the large-N_c relation is m_chi = 2 m_t,
    about sqrt(2) m_t with gauge and Higgs corrections, both too large for 125 GeV; the same paper gets a light
    composite Higgs from two condensates (mostly b-bbar with a top admixture), the several-species case. The record comparison is
    conditional on reading the rung field's neutral mode as lying at or above this threshold; the rung field is a
    doublet, the composite a single complex scalar, so the reading is a test, not a construction. Standard
    content re-derived in the formalism; transport-absent.
---

## formal
Let $H_{4} = \sum_{b}K(n_{a} + n_{c}) - G\,P^{*}P$, $P = \sum_{b}w_{a}w_{c}$, be the pairing element of Proposition \claimref{field-theory.composite-scalars-mean-field-level}(2) on a floor with $n_{b}$ blocks, $K \ge 0$, $G > 0$, acting on the Fock space of its $2n_{b}$ tower modes (the tower planes generate the CAR, Fact \claimref{field-theory.imported-tower-limit}).
\begin{enumerate}
\item[(i)] \emph{(Closed spectrum.)} $H_{4}$ conserves $N_{a}$ and $N_{c}$. In the sector $(N_{a}, N_{c})$ its eigenvalues are exactly the numbers $K(2p + s_{a} + s_{c}) - G(j + j_{z})(j - j_{z} + 1)$, where $s_{a}$ blocks hold $a$ alone, $s_{c}$ blocks hold $c$ alone, $p = N_{a} - s_{a} = N_{c} - s_{c}$ pairs occupy the remaining $\Omega = n_{b} - s_{a} - s_{c}$ blocks, $j_{z} = p - \Omega/2$, and $j \in \{\Omega/2, \Omega/2 - 1, \dots\}$ with $j \ge |j_{z}|$. The stored pair band $2Kn - Gn(n_{b} - n + 1)$ is $s_{a} = s_{c} = 0$, $j = n_{b}/2$, and is the lowest level of the sector $N_{a} = N_{c} = n$.
\item[(ii)] \emph{(Gap at fixed numbers.)} For $N_{a} = N_{c} = n$ with $0 < n < n_{b}$, the next level lies exactly $Gn_{b}$ above the band level, for every $K$ and $n$: breaking one pair, or lowering the quasi-spin by one, costs $Gn_{b}$, and no level lies between. This level is the pair-breaking (two-quasiparticle) threshold; the uniform scalar channel $P + P^{*}$ moves only along the band and does not reach it.
\item[(iii)] \emph{(Twice the quasiparticle energy.)} Above the threshold $G > 2K/n_{b}$ the one-shell mean-field energy $n_{b}(K - E) + \Delta^{2}/G$, $E^{2} = K^{2} + \Delta^{2}$, is stationary and convex exactly at $E = Gn_{b}/2$, the gap equation, so the exact gap of (ii) is $Gn_{b} = 2E = 2\sqrt{K^{2} + \Delta^{2}}$ with $\Delta$ the mean-field fermion mass: the pair-breaking threshold sits at twice the quasiparticle energy, at least $2\Delta$, and at exactly $2\Delta$ when $K = 0$, the floor analogue of Nambu's relation $m_{\sigma} = 2m$.
\item[(iv)] \emph{(Reading the rung field as such a composite.)} If the rung field's neutral mode is read as a tower composite of one fermion species of mean-field mass $m_{f} = \Delta$, lying at or above the pair-breaking threshold, then $m_{h} \ge 2m_{f}$ at this level. With the measured $m_{h}$ this needs $m_{f} < 63$ GeV, and with the tree value $m_{h} = M_{Z}$ of the D-term action (Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}) $m_{f} < 46$ GeV; both exclude the top quark as sole constituent at this level (one species, single shell), since $2m_{t}$ exceeds both. Composites of several species, or mixing between condensates, are not excluded.
\end{enumerate}

## technical
The stored composite scalars of the tower are built at mean field. Beyond mean field the pairing element on a floor is the degenerate pairing model, whose exact spectrum is the quasi-spin spectrum: in each sector of fixed numbers $N_{a}, N_{c}$ the levels are $K(2p + s) - G(j + j_{z})(j - j_{z} + 1)$, with $s$ singly occupied blocks, $p$ pairs on the others, quasi-spin $j$ and projection $j_{z}$. At equal numbers the band of the stored result is the lowest level and the next lies exactly $Gn_{b}$ above it: the pair-breaking (two-quasiparticle) threshold, which the uniform scalar channel does not reach on a floor.

The mean-field gap equation puts the quasiparticle energy at $E = Gn_{b}/2$, so the exact gap is $2E = 2\sqrt{K^{2} + \Delta^{2}}$, at least twice the fermion mass $\Delta$: by analogy, the floor form of Nambu's relation $m_{\sigma} = 2m$. If the Higgs boson is read as a composite of one species lying at or above this threshold, that species must be lighter than $m_{h}/2$, about $63$ GeV, or $M_{Z}/2$ at the tree level of the D-term action, which excludes the top quark as sole constituent at this level (one species, single shell). Light composites from several condensates, as in two-condensate models of top and bottom pairing, are not covered.

## lay
In this framework a scalar particle can arise as a bound pair of fermions, but so far only in an averaged approximation. This result solves the underlying model exactly on finite pieces of it. The lowest way to disturb the paired state without changing the particle numbers is to break one pair, and that costs exactly twice the energy of one dressed fermion, as the averaged treatment predicts.

By analogy with the known relation for such models, a composite scalar of this kind would weigh at least twice its constituents. If the Higgs boson were such a pair of a single kind of fermion, those fermions would have to be lighter than half its mass, about 63 GeV. The top quark is far heavier, so in this simple setting the Higgs cannot be a pair of top quarks alone, in line with the known difficulty of top-quark condensation; pairs mixing several kinds of fermion are not ruled out.

## one-liner
Beyond mean field the tower's pairing element has the closed quasi-spin spectrum on every floor, and at fixed numbers its first excitation, the pair-breaking threshold, lies exactly $Gn_{b} = 2E = 2\sqrt{K^{2} + \Delta^{2}}$ above the pair band; by analogy with Nambu's relation, a rung field read as a one-species composite at or above that threshold excludes the top quark as sole constituent at this level.
