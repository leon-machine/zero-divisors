---
id: synthesis.imported-kay-wald-uniqueness-and-no-go
kind: claim
version: 1
title: 'Imported: on a spacetime with a bifurcate Killing horizon there is at most one stationary quasi-free Hadamard state, KMS at the Hawking temperature on a wedge; none exists on extended Schwarzschild-de Sitter, and on Kerr none is argued (Kay and Wald 1991, with Kay and Lupo 2016)'
status: imported
region: synthesis
subject: thermality
tags: [horizons, hawking-temperature, no-go, classical-theorem]
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
- citation: 'B. S. Kay and R. M. Wald, Theorems on the uniqueness and thermal properties of stationary, nonsingular, quasifree states on spacetimes with a bifurcate Killing horizon, Phys. Rep. 207 (1991), 49--136.'
  key: KayWald1991
- citation: 'B. S. Kay and U. Lupo, Non-existence of isometry-invariant Hadamard states for a Kruskal black hole in a box and for massless fields on 1+1 Minkowski spacetime with a uniformly accelerating mirror, Class. Quantum Grav. 33 (2016), 215001; arXiv:1502.06582.'
  key: KayLupo2016
  locator: 'App. B; footnotes 2 and 4'
  doi: 10.1088/0264-9381/33/21/215001
- citation: 'B. S. Kay, Quantum field theory in curved spacetime (2nd edition), in Encyclopedia of Mathematical Physics, 2nd edition (2024); arXiv:2308.14517.'
  key: Kay2023
  doi: 10.1016/B978-0-323-95703-8.00085-9
extraction:
  note: >-
    Imported so that the result on the microlocal condition on a horizon generator and the scope note of
    (N+) can pin the Kay-Wald theorems and their limits instead of citing them from memory; it states more
    precisely, with the no-go results, the Kay-Wald entry of the bundle angle.imported-theorems-deliver-their-hypotheses.
    Checked on 2026-11-01: the bibliographic data of Kay and Wald (title, Phys. Rep. 207, pages 49-136, 1991)
    against the abstract and bibliography of arXiv:1502.06582; the statement of (a) against its footnote 2
    (for a linear scalar field on a globally hyperbolic spacetime with a one-parameter isometry group and a
    bifurcate Killing horizon, at most one state invariant under the isometries and Hadamard, proved by Kay
    and Wald for quasi-free states with vanishing one-point function and with a global form of the Hadamard
    condition) and against Kay's review arXiv:2308.14517 (uniqueness on Kruskal attributed to Kay and Wald
    1991 combined with Kay 1993, J. Math. Phys. 34 (1993) 4519, which is cited from memory; the restriction
    of the state to one wedge is KMS at the Hawking temperature); clause (b) against the review ("a similar
    no-go result" for spacetimes with bifurcate Killing horizons, such as Schwarzschild-de Sitter, which
    include triple wedges; for Kerr "it was argued", from superradiance, with the remark that the argument
    may not extend to Dirac fields) and against footnotes 2 and 4 of Kay and Lupo (which list Kerr and
    Schwarzschild-de Sitter as proved cases and give, for Schwarzschild-de Sitter, the argument that the two
    horizons' Hawking temperatures differ); the store follows the review in calling the Kerr case argued.
    Clause (c) against the abstract of arXiv:1502.06582 (it "points out the existence of, and partially
    fills, a gap in the proofs" of Kay and Wald), its footnote 1 (filled for the spacetimes it names) and the
    review ("identified and corrected in Appendix B"); the DOI of Kay and Lupo against the arXiv record; the
    review's title, edition and DOI against its arXiv record. Cited from memory, not checked: the journal of
    Kay and Lupo as Class. Quantum Grav. with volume 33 and article number 215001 (consistent with the DOI)
    and the year of the review's book.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decision of 2026-11-01 approving Kay-Wald 1991 and Kay-Lupo 2016 as routine imports, so that synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state and the scope note of synthesis.n-plus-null-ground-state cite them as a Fact; partly verified (see note).'
  flags:
  - 'beyond one flat chart: the bifurcate Killing horizon with its bifurcation surface, the Kruskal extension and the triple wedges of extended Schwarzschild-de Sitter'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is globally hyperbolic and carries a one-parameter group of isometries whose Killing field has a bifurcate Killing horizon of surface gravity $\kappa$, and let Hadamard be as in Fact \claimref{synthesis.imported-microlocal-hadamard-condition}, for the linear scalar field.
\begin{enumerate}
\item[(a)] (Uniqueness and thermality; Kay and Wald.) There is at most one quasi-free state with vanishing one-point function that is invariant under the isometries and satisfies the Hadamard condition (in Kay and Wald's global form, on a neighbourhood of the horizon); if it exists, its restriction to one wedge is a KMS state for the Killing flow at the Hawking temperature $\kappa/2\pi$. On the Kruskal extension of Schwarzschild such a state exists, and with a later theorem of Kay (1993) it is the unique state invariant under the Schwarzschild isometry group whose two-point function has Hadamard form (as Kay's review states).
\item[(b)] (No-go results.) For spacetimes with bifurcate Killing horizons that include triple wedges, such as the extended Schwarzschild-de Sitter field, no such state exists (Kay and Wald; the two horizons' Hawking temperatures differ). For the Klein-Gordon field on the extended Kerr field, Kay and Wald argued from superradiance that no isometry-invariant Hadamard state exists; the argument may not extend to Dirac fields, which have no superradiance.
\item[(c)] (A gap in the proofs.) A gap in the proofs of Kay and Wald was identified and filled by Kay and Lupo (Appendix B; partially, in the words of their abstract, and for the spacetimes they name).
\end{enumerate}
\emph{Beyond one flat chart.} The bifurcate Killing horizon with its bifurcation surface, the Kruskal extension and the triple wedges are global, read on several charts of flat spacetime, each with its own gravitational field. \emph{Provenance:} \cite{KayWald1991}; \cite[App.~B]{KayLupo2016}; \cite[Sec.~7]{Kay2023}.

## technical
Kay and Wald proved the rigorous form of the statement that a black hole in equilibrium has the Hawking temperature: on a spacetime whose Killing flow has a bifurcate horizon, a stationary state of a free scalar field that is regular (Hadamard) across the horizon is unique, and on each side of the horizon it is thermal at the Hawking temperature. They also showed its limits. When the spacetime has two horizons at different temperatures, as a black hole in a universe with a positive cosmological constant (Schwarzschild-de Sitter) does, no such state exists; for a spinning hole (Kerr) they argued from superradiance that none exists for the scalar field. Kay and Lupo later found and filled a gap in the original proofs.

## lay
A black hole that has always existed in equilibrium has a unique smooth quantum state around it, and that state has the Hawking temperature: this is the precise form of Hawking's result, due to Kay and Wald. The same theorem says that in a universe with a positive cosmological constant, where the black hole's horizon and the universe's horizon have different temperatures, no such equilibrium state exists, and for a spinning hole they argued the same. These are taken from the literature.

## one-liner
On a spacetime with a bifurcate Killing horizon there is at most one stationary quasi-free Hadamard state, KMS at $\kappa/2\pi$ on a wedge (Kay and Wald 1991); none exists on extended Schwarzschild-de Sitter, and on Kerr none is argued for the scalar field; a gap in the proofs was filled by Kay and Lupo (2016, App. B).
