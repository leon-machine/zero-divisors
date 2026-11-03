---
id: transport.classification-idempotent-orbits
kind: claim
version: 5
title: Classification of idempotent orbits
status: proved
region: transport
subject: clifford-structure
tags: [idempotents, classification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.classification-real-clifford-algebras@3
  - transport.units-span@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:6.4
- kind: check
  ref: check.py::check_orbits_are_rank_classes
- kind: check
  ref: check.py::check_complement_conjugate_iff_balanced
- kind: check
  ref: check.py::check_central_iff_singleton_orbit
locators:
  paper: T01
  number: Thm 6.4
  label: thm:orbits
  line: 1389
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: conjugacy of idempotents iff equal rank data by solving g e = e'' g in Mat_2(R), Mat_4(R), Mat_2(C), Mat_2(H) and Mat_2(R) + Mat_2(R); complements conjugate iff balanced; central iff fixed by all blade units. Version 3 -> 4. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 4 -> 5.'
  env: theorem
  context_refs:
  - transport.classification-real-clifford-algebras
  typing:
    by: ai-typing-pass
    added:
    - transport.classification-real-clifford-algebras
    note: 'Added the classification theorem, cited in the statement''s hypothesis and named in context_refs;
      version bumped to 2 for the derivation change, so transport.pair-canonical-label-bit''s pin @1 is
      now stale. Levels pass: the lay now keeps the nondegeneracy hypothesis and the split-case rank pairs.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - transport.classification-real-clifford-algebras
---

## formal
Let $A = \Cl(p,q)$, nondegenerate, so that $A \cong \Mat_m(D)$ or $\Mat_m(D) \oplus \Mat_m(D)$ with $D \in \{\R, \C, \HH\}$ (Theorem \claimref{transport.classification-real-clifford-algebras}), acting on the free right $D$-module $V = D^m$ (or on the pair of them). Define the \emph{rank} of an idempotent as $\dim_D$ of its image (a rank pair, in the split case). Then:
\begin{enumerate}
\item Two idempotents are conjugate under the inner automorphism group of $A$ if and only if they have the same rank data. In the simple case the idempotents of rank $r$, $0 < r < m$, form a single conjugacy orbit; in the split case inner automorphisms act componentwise and the orbits are indexed by rank pairs.
\item $e$ and $1 - e$ are conjugate if and only if $\mathrm{rank}\, e = m - \mathrm{rank}\, e$ (componentwise, in the split case): the labelling of a complementary pair is gauge exactly when the pair is balanced, and is canonically ordered by rank otherwise.
\item An idempotent is central if and only if its conjugation orbit is a singleton. The taxonomy's P/C boundary is therefore orbit-theoretic: type C comprises the idempotents that conjugation cannot move at all, type P those it moves through a full rank class.
\end{enumerate}

## technical
Let $A = \Cl(p,q)$ be nondegenerate, so that by the classification $A \cong \Mat_m(D)$ or $\Mat_m(D) \oplus \Mat_m(D)$ with $D \in \{\R, \C, \HH\}$, acting on $D^m$ (or a pair of copies). The rank of an idempotent is the $D$-dimension of its image, a rank pair in the split case. Two idempotents are conjugate under inner automorphisms if and only if they have the same rank data; in particular $e$ and $1 - e$ are conjugate if and only if $\mathrm{rank}\,e = m - \mathrm{rank}\,e$, componentwise in the split case.

An idempotent is central if and only if its conjugation orbit is a single point. This makes the boundary between obstruction types P and C orbit-theoretic: type C idempotents are those conjugation cannot move, type P those it moves through a full rank class.

## lay
Idempotents are elements equal to their own square, like projections onto a subspace. This result sorts them in any nondegenerate real Clifford algebra: two are related by an internal change of viewpoint exactly when they project onto subspaces of the same size (in each of the two blocks, when the algebra splits into two). The ones that no such change can move at all are exactly the ones that commute with everything, and this is how the series separates two of its types of obstruction.

## one-liner
Idempotents of a nondegenerate real Clifford algebra are conjugate exactly when their rank data agree, and an idempotent is central exactly when its conjugation orbit is a point.
