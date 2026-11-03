---
id: synthesis.imported-local-quasi-equivalence-of-hadamard-states
kind: claim
version: 1
title: 'Imported: quasi-free Hadamard states are locally quasi-equivalent, for the Klein-Gordon field (Verch 1994) and for the Dirac field (D''Antoni and Hollands 2006)'
status: imported
region: synthesis
subject: thermality
tags: [superselection, car-algebra, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'R. Verch, Local definiteness, primarity and quasiequivalence of quasifree Hadamard quantum states in curved spacetime, Commun. Math. Phys. 160 (1994), 507--536.'
  key: Verch1994
  doi: 10.1007/BF02173427
- citation: 'C. D''Antoni and S. Hollands, Nuclearity, local quasiequivalence and split property for Dirac quantum fields in curved spacetime, Commun. Math. Phys. 261 (2006), 133--159; arXiv:math-ph/0106028.'
  key: DAntoniHollands2006
  locator: 'Thms. III.1, III.2'
  doi: 10.1007/s00220-005-1398-2
extraction:
  note: >-
    Imported so that the result on the microlocal condition on a horizon generator can pin the bulk theorems
    that turn local quasi-equivalence from a principle into a consequence of the Hadamard condition, instead of
    citing them from memory. Checked on 2026-11-01: Verch 1994 against the publisher's record of DOI
    10.1007/BF02173427 (title, author, journal, volume 160, pages 507-536, year; the abstract: the quantised
    Klein-Gordon field in its Weyl-algebra form, the GNS representations of quasi-free Hadamard states are
    locally quasi-equivalent in every globally hyperbolic spacetime, with local primarity and local
    definiteness on ultrastatic spacetimes, where the local von Neumann algebras of sufficiently small regions
    are type III_1 factors); the same theorem as stated in B. S. Kay's review arXiv:2308.14517 (on the
    algebra of any bounded open region the folia of the quasi-free Hadamard states coincide). D'Antoni and
    Hollands against the arXiv text of math-ph/0106028 (title, authors, abstract, Definition II.1 of the
    Hadamard condition by the wave front set, Theorem III.1: the GNS representations of any two quasi-free
    Hadamard states of the Dirac field are quasi-equivalent on the field algebra of any open relatively
    compact region; Theorem III.2: local unitary equivalence, with type III_1 local algebras; the split
    property in the representation of any quasi-free Hadamard state) and the DOI against the arXiv record.
    Cited from memory, not checked: the journal volume, year and pages of D'Antoni and Hollands (Commun. Math.
    Phys. 261 (2006) 133-159).
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decision of 2026-11-01 approving Verch 1994 and D''Antoni-Hollands 2006 as routine imports, so that synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state cites them as a Fact; partly verified (see note).'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is globally hyperbolic, read on several charts where its global structure needs them, and let a quasi-free state be Hadamard as in Fact \claimref{synthesis.imported-microlocal-hadamard-condition}.
\begin{enumerate}
\item[(a)] (Verch; the Klein-Gordon field.) The GNS representations of any two quasi-free Hadamard states of the Weyl algebra of the Klein-Gordon field are locally quasi-equivalent: their restrictions to the algebra of any open relatively compact region are quasi-equivalent. On ultrastatic spacetimes they are moreover locally primary and locally definite, and the local von Neumann algebras of sufficiently small regions are factors of type III$_{1}$.
\item[(b)] (D'Antoni and Hollands; the Dirac field.) The GNS representations of any two quasi-free Hadamard states of the free Dirac field are quasi-equivalent on the field algebra $\mathfrak{F}(\mathcal{O})$ of any open relatively compact region $\mathcal{O}$ (Theorem III.1); the local quasi-equivalence is a local unitary equivalence, and the local von Neumann algebras are factors of type III$_{1}$ (Theorem III.2). The split property holds in the representation of any quasi-free Hadamard state.
\end{enumerate}
So for these free fields the local quasi-equivalence of physical states, which Fact \claimref{synthesis.imported-haag-local-normality}(b) states as a principle, is a theorem once the physical states are taken to be the quasi-free Hadamard states. \emph{Provenance:} \cite{Verch1994}; \cite[Thms.~III.1, III.2]{DAntoniHollands2006}.

## technical
Two states of a quantum field are locally quasi-equivalent if, on every bounded region, each is a density matrix in the other's Hilbert space: no measurement confined to the region can separate their sectors. In algebraic quantum field theory this is usually imposed as a principle on physical states. Verch proved it as a theorem for the free scalar field in any globally hyperbolic background, for all quasi-free states satisfying the Hadamard condition; D'Antoni and Hollands proved the same for the free Dirac field, with local unitary equivalence and type III$_{1}$ local algebras. So, for free fields, being Hadamard implies local normality to every other Hadamard state, the vacuum-like ones included.

## lay
Quantum field theory needs a rule for which states are physically possible, and a standard one says that in any limited region a possible state must be of the same kind as the vacuum. For the simplest fields in a gravitational field, Verch for particles without spin and D'Antoni and Hollands for electrons showed that this rule is not an extra assumption: it follows from the short-distance requirement that states resemble empty space up close. These are taken from the literature.

## one-liner
Any two quasi-free Hadamard states are locally quasi-equivalent on the algebra of every open relatively compact region, for the Klein-Gordon field (Verch 1994) and for the Dirac field, there with local unitary equivalence and type III$_{1}$ local algebras (D'Antoni and Hollands 2006).
