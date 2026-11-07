---
id: synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection
kind: claim
version: 2
title: 'Imported: the twisted modular reflection of the chiral Fermi field'
status: imported
region: synthesis
subject: thermality
tags: [modular-theory, car-algebra, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-06
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: unit pass, every imaginary unit resolved to the geometric-algebra unit it stands for
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
imported_from:
- citation: 'R. Brunetti, D. Guido and R. Longo, Modular structure and duality in conformal quantum field theory, Commun. Math. Phys. 156 (1993), 201--219; arXiv:funct-an/9302008.'
  key: BGL1993
  locator: 'the algebraic Bisognano-Wichmann theorem for conformal nets (modular groups of wedge, interval and double-cone algebras geometric) and Haag duality; abstract checked; the circle-net form of clause (a) cited from memory'
  doi: 10.1007/BF02096738
- citation: 'H. Baumgaertel, M. Jurke and F. Lledo, Twisted duality of the CAR-algebra, J. Math. Phys. 43 (2002), 4158--4179; arXiv:math-ph/0204029.'
  key: BJL2002
  locator: 'twisted duality M(q)'' = Z M(q^perp) Z* for the self-dual CAR algebra in any Fock representation, and an explicit formula for the graph of the modular operator, applied to free fermionic nets; abstract checked'
  doi: 10.1063/1.1483376
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2 (U4). Restated with the unit of the Hilbert spaces written as I_4 (U1, abstract complex Hilbert spaces and the continuum mode space of the line): the Klein twist Z = (1 + I_4 Theta)/(1 + I_4) and the momentum P = I_4 d/du; the antiunitary conjugations stay as operators. The source writes i for I_4; its form is kept in source_formal. Status stays imported; declaration removed. Statement content unchanged.'
  source_formal: |-
    \begin{enumerate}
    \item[(a)] (Bisognano-Wichmann for conformal nets; Brunetti, Guido and Longo.) For a local net of von Neumann algebras on the circle, covariant under the M\"obius group with positive energy and with a unique invariant vacuum $\Omega$, the modular group of the algebra of an interval $I$ with respect to $\Omega$ is the one-parameter M\"obius subgroup fixing the endpoints of $I$, with the modular parameter rescaled by $2\pi$, and the modular conjugation implements the M\"obius reflection fixing the endpoints of $I$, mapping the algebra of $I$ onto that of its complement (Haag duality). On the line, for the half-line $(a, \infty)$, the modular group is the dilation about $a$ and the conjugation implements $u \mapsto 2a - u$.
    \item[(b)] (Twisted duality; Baumgaertel, Jurke and Lledo.) For the self-dual CAR algebra over a Hilbert space with antiunitary involution, in any Fock representation, and a closed subspace $q$ invariant under the involution, the von Neumann algebras satisfy $\mathcal{M}(q)' = Z\mathcal{M}(q^{\perp})Z^{*}$, with $Z = (1 + i\Theta)/(1 + i)$ the Klein twist built from the grading $\Theta$; the graph of the modular operator has an explicit form, which applies to free fermionic nets.
    \item[(c)] (The field-level form for the chiral Fermi field.) For the free chiral Fermi field $\psi$ on the line, $\CAR(L^{2}(\R)\otimes K)$, in its vacuum, the gauge-invariant quasi-free state with symbol $\chi_{(-\infty, 0)}(P)\otimes\id_{K}$, $P = i\,d/du$, the modular conjugation $J_{a}$ of the algebra of the half-line $(a, \infty)$ acts on the fields as the Klein-twisted charge-conjugating reflection about $a$: $J_{a}\psi(f)J_{a} = c'\,Z\psi^{*}(f\circ r_{a})Z^{*}$ for $f$ supported in $(a, \infty)$, $r_{a}(u) = 2a - u$, with a constant phase $c'$ independent of $f$ and $a$. It is the second quantisation, twisted by $Z$, of the one-particle modular conjugation, as in (a) for local nets; the value of $c'$ depends on the conventions and is not part of this Fact.
    \end{enumerate}
    \emph{Provenance:} \cite{BGL1993}; \cite{BJL2002}; clause (c) and the circle form of (a) cited from memory.

    The source writes $i$ for $I_{4}$.
  note: >-
    Imported so that the results on modular conjugations on a horizon generator pin the field-level action of
    the vacuum's half-line modular conjugations, which the Fact angle.imported-theorems-deliver-their-hypotheses
    does not state (it gives the modular groups, and for wedges the conjugation as CPT composed with a rotation,
    acting on spacetime). Checked on 6 November 2026: the bibliographic data of both papers (journal, volume,
    issue, pages, DOI) against the Crossref records; the abstract of arXiv:funct-an/9302008 (an algebraic
    Bisognano-Wichmann theorem for conformal quantum field theory, from a result of Borchers: the modular group
    of a wedge algebra is the rescaled pure Lorentz transformations preserving it, with a geometric description
    for double cones, essential duality and Haag duality, and a PCT symmetry for every conformal theory in even
    spacetime dimension); and the abstract of arXiv:math-ph/0204029 (twisted duality for the self-dual CAR
    algebra in any Fock representation, M(q)' = Z M(q^perp) Z*, proved through a Halmos decomposition, modular
    theory and Kato's theory of pairs of projections, with an explicit formula for the graph of the modular
    operator for free fermionic nets). Cited from memory, not checked against the sources: the circle-net
    (Moebius-covariant) form of clause (a), and clause (c), the field-level action of the conjugation on the
    chiral Fermi field, which is the fermionic counterpart of (a) obtained by second quantisation of the
    one-particle modular objects. The value of the constant phase in (c) depends on conventions and is not part
    of this Fact.
  maintainer_pass:
    by: maintainer-2026-11-06
    date: '2026-11-06'
    note: 'Created so that synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state (converse, clause (v)) and synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i (the vacuum''s half-line conjugations) cite the field-level modular conjugation as a Fact rather than from memory; partly verified (see note).'
---

## formal
Numbers are read in $\mathrm{span}\{1, I_{4}\}$, the unit of every Hilbert space here (U1; on the line it is the unit of the continuum mode space). The modular conjugations $J_{a}$ are antiunitary operators, not units.
\begin{enumerate}
\item[(a)] (Bisognano-Wichmann for conformal nets; Brunetti, Guido and Longo.) For a local net of von Neumann algebras on the circle, covariant under the M\"obius group with positive energy and with a unique invariant vacuum $\Omega$, the modular group of the algebra of an interval $I$ with respect to $\Omega$ is the one-parameter M\"obius subgroup fixing the endpoints of $I$, with the modular parameter rescaled by $2\pi$, and the modular conjugation implements the M\"obius reflection fixing the endpoints of $I$, mapping the algebra of $I$ onto that of its complement (Haag duality). On the line, for the half-line $(a, \infty)$, the modular group is the dilation about $a$ and the conjugation implements $u \mapsto 2a - u$.
\item[(b)] (Twisted duality; Baumgaertel, Jurke and Lledo.) For the self-dual CAR algebra over a Hilbert space with antiunitary involution, in any Fock representation, and a closed subspace $q$ invariant under the involution, the von Neumann algebras satisfy $\mathcal{M}(q)' = Z\mathcal{M}(q^{\perp})Z^{*}$, with $Z = (1 + I_{4}\Theta)/(1 + I_{4})$ the Klein twist built from the grading $\Theta$; the graph of the modular operator has an explicit form, which applies to free fermionic nets.
\item[(c)] (The field-level form for the chiral Fermi field.) For the free chiral Fermi field $\psi$ on the line, $\CAR(L^{2}(\R)\otimes K)$, in its vacuum, the gauge-invariant quasi-free state with symbol $\chi_{(-\infty, 0)}(P)\otimes\id_{K}$, $P = I_{4}\,d/du$, the modular conjugation $J_{a}$ of the algebra of the half-line $(a, \infty)$ acts on the fields as the Klein-twisted charge-conjugating reflection about $a$: $J_{a}\psi(f)J_{a} = c'\,Z\psi^{*}(f\circ r_{a})Z^{*}$ for $f$ supported in $(a, \infty)$, $r_{a}(u) = 2a - u$, with a constant phase $c'$ independent of $f$ and $a$. It is the second quantisation, twisted by $Z$, of the one-particle modular conjugation, as in (a) for local nets; the value of $c'$ depends on the conventions and is not part of this Fact.
\end{enumerate}
\emph{Provenance:} \cite{BGL1993}; \cite{BJL2002}; clause (c) and the circle form of (a) cited from memory.

## technical
For conformal quantum field theories Brunetti, Guido and Longo proved the Bisognano-Wichmann property algebraically: the modular flow that the vacuum defines on the algebra of an interval (or a half-line, or a wedge) is the geometric flow of the conformal group fixing that region, and the modular conjugation acts as the matching reflection, which gives Haag duality. For fermions locality is replaced by twisted locality, and Baumgaertel, Jurke and Lledo proved the corresponding twisted duality for the free fermion (CAR) algebra: the commutant of a region's algebra is the twisted algebra of the complementary region. For the free chiral Fermi field on a line in its vacuum the two combine into the field-level statement used in the store: the modular conjugation of a half-line acts on the fields as the reflection about the cut combined with charge conjugation and the Klein twist, with a constant phase whose value is a matter of convention.

## lay
In quantum field theory the vacuum attaches to each region a mathematical reflection. For theories with conformal symmetry it is known that this reflection is the ordinary mirror reflection of the region; for free fermions moving along a line it acts on the fields themselves as the mirror image through the cut, with particles exchanged for antiparticles and a fixed sign twist for fermions. The results are taken from the literature.

## one-liner
For Moebius-covariant nets the vacuum's modular group of an interval or half-line is the geometric flow fixing it and its modular conjugation the matching reflection (Brunetti, Guido and Longo 1993); the free CAR algebra has twisted duality $\mathcal{M}(q)' = Z\mathcal{M}(q^{\perp})Z^{*}$ (Baumgaertel, Jurke and Lledo 2002); for the chiral Fermi field in its vacuum the half-line conjugation acts on the fields as the Klein-twisted charge-conjugating reflection about the cut, up to a constant phase.
