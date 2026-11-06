---
id: synthesis.imported-monopoles-second-homotopy-and-pati-salam-charge
kind: claim
version: 1
title: 'Imported: monopoles from the second homotopy group; the Pati-Salam charge'
status: imported
region: synthesis
subject: dark-matter
tags: [symmetry-breaking, gauge-fields, classical-theorem]
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
- citation: 'J. Preskill, Magnetic monopoles, Ann. Rev. Nucl. Part. Sci. 34 (1984), 461--530.'
  key: Preskill1984
- citation: 'G. Lazarides, M. Magg and Q. Shafi, Phase transitions and magnetic monopoles in SO(10), Phys. Lett. B 97 (1980), 87--92.'
  key: LazaridesMaggShafi1980
extraction:
  note: >-
    Imported as input (a) of synthesis.pati-salam-monopoles-bound-descent-history, which cites it
    from memory. The homotopy statement is the exact sequence of the fibration H -> G -> G/H with
    pi_2(G) = 0 for every Lie group and pi_1(G) = 0 for simply connected G, standard; the review cited is
    from memory. The two-Dirac-unit charge of the SU(4) x SU(2)_L x SU(2)_R monopole was checked on
    2026-10-26 against the abstract and Section II of arXiv:2503.18321 ("a topologically stable finite
    energy magnetic monopole that carries two quanta of Dirac magnetic charge, 4 pi/e"), which lists
    Lazarides, Magg and Shafi, Phys. Lett. B 97 (1980) 87, in its references (bibliographic data checked
    there; pages 87-92 from memory). The mass estimate M of order 4 pi v/g is from memory.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: monopole input (a), cited from memory by the Pati-Salam monopole result, to be imported as a Fact).'
---

## formal
Let a gauge theory with connected, simply connected compact group $G$ be broken by a Higgs field to a closed subgroup $H$ at scale $v$. The exact homotopy sequence of $H \to G \to G/H$, with $\pi_{2}(G) = 0$ and $\pi_{1}(G) = 0$, gives $\pi_{2}(G/H) \cong \pi_{1}(H)$, and every nontrivial class is carried by a finite-energy ('t Hooft-Polyakov) monopole, of mass of order $4\pi v/g$ for gauge coupling $g$; the monopoles of the classes that generate the group are stable. For $G = SU(4) \times SU(2)_{L} \times SU(2)_{R}$ broken to the Standard Model group (the unbroken $U(1)$ of electromagnetism lying inside $H$), $\pi_{1}(H)$ contains $\mathbb{Z}$, and the lightest monopole carries two Dirac units of magnetic charge, $4\pi/e$, together with a colour magnetic field. \emph{Provenance:} \cite{Preskill1984} (the homotopy classification, as remembered); \cite{LazaridesMaggShafi1980} (the Pati-Salam monopole).

## technical
Whether a symmetry breaking leaves magnetic monopoles is a topological question: with a simply connected unbroken-phase group, the monopole charges are the closed loops of the residual group $H$ that cannot be shrunk, $\pi_{1}(H)$. Every grand-unified breaking to the Standard Model group has $\pi_{1}(H) \supseteq \mathbb{Z}$, because electromagnetism's circle cannot be unwound, so it leaves stable superheavy monopoles. For the Pati-Salam group the lightest carries twice the Dirac charge. This is a topological result, stated for the gauge groups; the series uses it for its own Pati-Salam chain.

## lay
When the forces of a unified theory separate as the universe cools, knots in the fields can be left behind that behave as isolated magnetic poles. Topology says when this must happen; for the unification scheme the series uses, it must, and each pole carries twice the smallest magnetic charge Dirac allowed.

## one-liner
For simply connected $G$ broken to $H$, $\pi_{2}(G/H) \cong \pi_{1}(H)$ and each class carries a finite-energy monopole; Pati-Salam broken to the Standard Model leaves stable monopoles of two Dirac units (Lazarides, Magg and Shafi 1980).
