---
id: synthesis.principality-is-genericity
kind: claim
version: 1
title: Principality is genericity, not symmetry (invariance selects the zero map, indistinguishable blocks allow every rectangular type)
status: proved
region: synthesis
subject: programme
tags: [indifference, representation-theory, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
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
  - scrambling.imported-kostant-madore-partition-data@1
  - scrambling.boundary-mode-space-matrix@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_principal_is_the_unique_full_dimensional_orbit
- kind: check
  ref: check.py::check_indistinguishable_blocks_are_the_rectangular_types
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - scrambling.indifference-structural-premise-series
  - scrambling.principality-indifference-sphere
extraction:
  open_problem: pr.indifference
  note: >-
    Tests, on the one use of indifference that selects a structure from a finite list (the
    principal embedding of Theorem scrambling.principality-indifference-sphere), whether the
    selection is a consequence of symmetry plus a measure principle. Three readings are separated
    and each is decided exactly: invariance under conjugation, indistinguishability of blocks, and
    genericity for the invariant measure class on the nilpotent cone. Only genericity yields the
    principal embedding uniquely. The real Jordan form of nilpotent matrices and the
    Jacobson-Morozov correspondence between nilpotent elements and sl2 triples are classical
    (Jacobson 1951, Morozov 1942, Kostant 1959; cited from memory) and enter only through the
    imported Fact's classification by partitions. Transport-absent: representation theory of gl_n.
---

## formal
Let $\Mat_n$ be the matrix algebra of the boundary modes (Proposition \claimref{scrambling.boundary-mode-space-matrix}) and classify $\mathfrak{sl}_2$ structures on it by the partition $\lambda$ of $n$ (Fact \claimref{scrambling.imported-kostant-madore-partition-data}(i)), equivalently by the conjugacy class of the nilpotent element $e_\lambda$ of a standard triple; the zero map has $\lambda = (1^n)$, the principal embedding $\lambda = (n)$. Write $m_d$ for the number of parts of size $d$ and $\lambda^{T}$ for the conjugate partition.
\begin{enumerate}
\item[(i)] \emph{(Invariance.)} The conjugation orbit of $e_\lambda$ has dimension $n^2 - \sum_i (\lambda^{T}_i)^2$. It is a single point exactly for $\lambda = (1^n)$: the only $\mathfrak{sl}_2$ structure fixed pointwise by the symmetry of the matrix algebra ($\operatorname{Ad}_g \circ \phi = \phi$ for every invertible $g$) is the zero map. (Fixed only as a subalgebra, the principal image is also fixed at $n = 2$, where it is all of $\mathfrak{sl}_2$.)
\item[(ii)] \emph{(Indistinguishable blocks.)} The commutant of the image of a standard triple has dimension $\sum_d m_d^2$; it permutes the blocks of each size transitively, and blocks of different sizes are told apart by their dimension. So no block is distinguished from another exactly when $\lambda = (k^{n/k})$ is rectangular, $k \mid n$. For $n$ prime this leaves the principal embedding and the zero map; for composite $n$ every rectangular type, for example $(2,2)$ at $n = 4$.
\item[(iii)] \emph{(Genericity.)} The orbit dimension equals $n^2 - n$ exactly for $\lambda = (n)$ and is strictly smaller for every other $\lambda$. The nilpotent cone is the union of the finitely many orbits, so the principal orbit is open and dense in it, and for every measure on the cone absolutely continuous with respect to its conjugation-invariant measure class, the type is $(n)$ almost surely.
\end{enumerate}
So the selection of the principal embedding in Theorem \claimref{scrambling.principality-indifference-sphere} does not follow from symmetry: pointwise invariance selects the zero map, and the absence of distinguished blocks allows every rectangular type. It follows from indifference read as genericity: the structure that a choice with no preference lands on with probability one for the invariant measure class. In this use, what the indifference premise (Principle \claimref{scrambling.indifference-structural-premise-series}) adds beyond symmetry is that measure principle.

## technical
The series selects the principal embedding of $\mathfrak{sl}_2$ into the boundary modes' matrix algebra by its indifference premise: other embeddings carry uncaused partition data. This result tests that selection against three precise readings of indifference. Invariance under the matrix algebra's own symmetry selects only the zero map, the one structure fixed by conjugation. Requiring that no block be distinguished from another allows every rectangular partition $(k^{n/k})$, since the commutant permutes equal blocks; for $n$ prime this leaves only the principal embedding and the zero map. Only genericity singles out the principal embedding: its orbit is the unique one of full dimension $n^2 - n$ in the nilpotent cone, so a choice with no preference, made with any measure in the invariant class, lands on it with probability one. In this use, indifference is a measure principle added to symmetry.

## lay
The series picks one particular way for the symmetry of a sphere to act on the boundary modes, arguing that any other way would make arbitrary distinctions. This result asks which reading of "no arbitrary distinctions" actually makes that choice. Demanding full symmetry picks the trivial option where nothing acts at all. Demanding that no group of modes be singled out still allows several options when the number of modes can be split evenly. Only the reading "pick what a random choice gives almost surely" selects the series' option uniquely. So the premise is doing the work of a rule about probability, not just about symmetry.

## one-liner
Among $\mathfrak{sl}_2$ structures on $\Mat_n$, pointwise conjugation invariance selects the zero map, indistinguishable blocks allow every rectangular type $(k^{n/k})$, and only genericity (the unique full-dimensional orbit, $n^2 - n$) selects the principal embedding, so in this use indifference is a measure principle.
