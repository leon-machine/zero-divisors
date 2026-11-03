---
id: synthesis.imported-haag-local-normality
kind: claim
version: 1
title: 'Imported: the local normality principle of algebraic quantum field theory (Haag), and local quasi-equivalence in a gravitational background (Haag, Narnhofer and Stein 1984)'
status: imported
region: synthesis
subject: thermality
tags: [modular-theory, superselection, horizons, classical-theorem]
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
- citation: 'R. Haag, Local Quantum Physics: Fields, Particles, Algebras, 2nd edition, Springer, Berlin, 1996.'
  key: Haag1996
  doi: 10.1007/978-3-642-61458-3
- citation: 'R. Haag, H. Narnhofer and U. Stein, On quantum field theory in gravitational background, Commun. Math. Phys. 94 (1984), 219--238.'
  key: HaagNarnhoferStein1984
  doi: 10.1007/BF01209302
extraction:
  note: >-
    Imported so that the result on local normality at the bifurcation surface can pin the principle whose
    generator-algebra analogue it adopts. Checked: the bibliographic data of Haag, Narnhofer and Stein (authors,
    title, journal, volume 94, issue 2, pages 219-238, 1984, DOI) against a library record of the publisher's
    DOI; the bibliographic data of the second edition of Haag's book (Springer, 1996) against publisher and
    bookseller listings; and the content of clause (b), that Haag, Narnhofer and Stein state a principle of
    local definiteness one of whose conditions is local quasi-equivalence of physical states on the algebras of
    relatively compact open regions, against a secondary statement (R. Verch, arXiv:funct-an/9609004). Cited from
    memory, not checked against the sources: the wording of clause (a) in Haag's book, and that Haag, Narnhofer
    and Stein obtain the Hawking temperature from a condition on the scaling limit of the state at the horizon.
    The transfer of the principle to the CAR algebra of an interval of one horizon generator is not part of this
    Fact; it is the adopted analogue stated in the result that uses it.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created at Leon''s decision of 2026-10-31 to import Haag''s local normality as a Fact, so that synthesis.local-normality-at-the-edge-gives-the-null-ground-state cites it as a premise rather than from memory; partly verified (see note).'
---

## formal
Let $\mathcal{O} \mapsto \mathcal{A}(\mathcal{O})$ be the net of local algebras of a quantum field theory over the bounded (relatively compact, open) regions $\mathcal{O}$ of spacetime.
\begin{enumerate}
\item[(a)] (Local normality; Haag.) The physical states are required to be locally normal with respect to the vacuum: for every bounded region $\mathcal{O}$ the restriction of a physical state to $\mathcal{A}(\mathcal{O})$ is a normal state of the vacuum representation restricted to $\mathcal{A}(\mathcal{O})$, equivalently its GNS representation restricted to $\mathcal{A}(\mathcal{O})$ is quasi-equivalent to the vacuum representation restricted there. This is a principle of the theory, selecting the physical states, and not a theorem.
\item[(b)] (Local quasi-equivalence in a gravitational background; Haag, Narnhofer and Stein.) For a quantum field in a gravitational background, the principle of local definiteness includes local quasi-equivalence: for any two physical states $\omega_{1}$, $\omega_{2}$ and every relatively compact open region $\mathcal{O}$, the representations $\pi_{\omega_{1}}$ and $\pi_{\omega_{2}}$ restricted to $\mathcal{A}(\mathcal{O})$ are quasi-equivalent. With a condition on the short-distance scaling limit of the state at the horizon, the Hawking temperature of a Killing horizon follows from it.
\end{enumerate}
\emph{Provenance:} \cite{Haag1996, HaagNarnhoferStein1984}.

## technical
Algebraic quantum field theory assigns to each bounded region of spacetime an algebra of observables. Haag's local normality principle says which states are physical: in every bounded region a physical state must look like a density matrix in the vacuum's Hilbert space, so that no measurement confined to a bounded region separates it from the vacuum's sector. Haag, Narnhofer and Stein carried the requirement to quantum fields in a gravitational background, as local quasi-equivalence of any two physical states on the algebras of relatively compact regions, and, with a condition on the short-distance scaling limit of the state at a horizon, obtained the Hawking temperature from it. Both are taken from the literature; applying the principle to the algebra of an interval of one horizon generator, as the store does, is an analogue adopted there and not part of this Fact.

## lay
Quantum field theory needs a rule for which states are physically possible. The standard rule, due to Haag, is that in any limited region a possible state must be indistinguishable in kind from the vacuum: it may differ in detail, but it cannot belong to a separate, incompatible sector. Haag, Narnhofer and Stein used the same rule for fields around black holes, and with a condition on how the state looks at very short distances near the horizon they recovered the Hawking temperature. These are taken from the literature.

## one-liner
Physical states are locally normal to the vacuum, quasi-equivalent to it on the algebra of every bounded region (Haag); in a gravitational background any two physical states are locally quasi-equivalent, and with a short-distance scaling-limit condition at a horizon this gives the Hawking temperature (Haag, Narnhofer and Stein 1984).
