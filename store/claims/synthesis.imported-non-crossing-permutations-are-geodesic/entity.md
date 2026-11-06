---
id: synthesis.imported-non-crossing-permutations-are-geodesic
kind: claim
version: 1
title: 'Imported: non-crossing permutations as geodesics (Biane)'
status: imported
region: synthesis
subject: entropy
tags: [finite-models, classical-theorem]
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
- citation: 'P. Biane, Some properties of crossings and partitions, Discrete Math. 175 (1997), 41--53.'
  key: Biane1997
- citation: 'A. Nica and R. Speicher, Lectures on the Combinatorics of Free Probability, London Mathematical Society Lecture Note Series 335, Cambridge University Press (2006), Lecture 23.'
  key: NicaSpeicher2006
- citation: 'J. A. Mingo and A. Nica, Annular noncrossing permutations and partitions, and second-order asymptotics for random matrices, Int. Math. Res. Not. 2004, no. 28, 1413--1460; arXiv:math/0303312.'
  key: MingoNica2004
extraction:
  note: >-
    Imported for the replica-saddle count of eviction, whose proof (ii) cites the characterisation
    of the permutations attaining the genus bound as "classical, Biane; from memory". The attribution
    to Biane of the geodesic description (#(tau) + #(tau^-1 gamma) = n + 1 for the non-crossing
    permutations, his Section 1.3) was checked on 2026-10-31 against Mingo and Nica,
    arXiv:math/0303312, Section 2.10. Biane's bibliographic data, the lecture number in Nica and
    Speicher, and the journal data of Mingo and Nica are cited from memory. The counts 1, 2, 5, 14,
    42, 132, 429 for n up to 7 are confirmed by enumeration in the eviction result's check.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created by the maintainer pass of 2026-10-31 (literature cited from memory by an accepted result; Leon''s list of imports).'
---

## formal
For $\sigma \in S_{n}$ let $\#(\sigma)$ be its number of cycles and $|\sigma| = n - \#(\sigma)$ the least number of transpositions whose product is $\sigma$, and let $\eta = (1\,2\,\cdots\,n)$. Since $|\cdot|$ is the word length for the generating set of all transpositions, $|\sigma| + |\sigma^{-1}\eta| \ge |\eta| = n - 1$, that is
\[
\#(\sigma) + \#(\sigma^{-1}\eta) \;\le\; n + 1 .
\]
Equality holds exactly when $\sigma$ lies on a geodesic from the identity to $\eta$ in the Cayley graph of $S_{n}$ for the transpositions; these are exactly the permutations whose cycles, each written in increasing order, form a non-crossing partition of $\{1, \dots, n\}$, and $\sigma \mapsto$ (its cycle partition) is a bijection from them onto the non-crossing partitions. Their number is the Catalan number $C_{n} = \frac{1}{n + 1}\binom{2n}{n}$. \emph{Provenance:} \cite[Section 1.3]{Biane1997}; \cite[Lecture 23]{NicaSpeicher2006}; \cite[Section 2.10]{MingoNica2004}.

## technical
Counting a permutation's distance from the identity by the transpositions it needs, the full cycle on $n$ letters is $n - 1$ steps away, and a permutation together with its complement relative to that cycle can never take fewer steps in total. The ones that take exactly that many sit on a shortest path, and they are precisely the permutations whose cycles do not cross when the letters are placed around a circle. There are a Catalan number of them. In random-matrix and replica calculations these are the planar, leading terms.

## lay
Among all ways of shuffling $n$ objects, a special family, the ones whose loops can be drawn around a circle without crossing, plays a leading role whenever large random systems are averaged. This standard result of combinatorics identifies them as the shuffles that lie on a shortest route to the full cyclic shuffle, and counts them by the Catalan numbers $1, 2, 5, 14, \dots$.

## one-liner
$\#(\sigma) + \#(\sigma^{-1}\eta) \le n + 1$ on $S_{n}$, with equality exactly for the $C_{n}$ non-crossing permutations, the geodesics from the identity to the full cycle (Biane 1997).
