---
id: synthesis.imported-rank-completion-of-the-doubled-matrix-algebra
kind: claim
version: 1
title: 'Imported: von Neumann''s continuous regular ring'
status: imported
region: synthesis
subject: tower
tags: [classical-theorem, limits, idempotents]
proposed_by:
  kind: ai
  session: 2026-11-15-continuum-verdict
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-15-continuum-verdict
review: draft
imported_from:
- citation: 'K. R. Goodearl, Von Neumann Regular Rings, Pitman, London (1979); 2nd ed., Krieger, Malabar (1991).'
  key: Goodearl1979
  locator: 'Theorems 19.6, 19.7, 19.14, 20.8, Corollary 21.14, ch. 10'
- citation: 'K. R. Goodearl, Metrically complete regular rings, Trans. Amer. Math. Soc. 272 (1982), no. 1.'
  key: Goodearl1982
  locator: 'Theorems 2.3, 4.10, Corollary 4.3'
- citation: 'P. Ara and J. Claramunt, Uniqueness of the von Neumann continuous factor, arXiv:1705.04501 (2017).'
  key: AraClaramunt2017
- citation: 'K. R. Goodearl, Centers of regular self-injective rings, Pacific J. Math. 76 (1978), 381--395.'
  key: Goodearl1978
  locator: 'Theorem 2.8'
- citation: 'I. Halperin, Von Neumann''s manuscript on inductive limits of regular rings, Canad. J. Math. 20 (1968), 477--483.'
  key: Halperin1968
- citation: 'J. von Neumann, On regular rings, Proc. Natl. Acad. Sci. USA 22 (1936), 707--713.'
  key: vonNeumann1936
extraction:
  note: >-
    Imported on 15 November 2026 at Leon's direction, in place of importing the working note "The
    Never-Ending Transport and the Continuum" (draft 0.5), which re-proves parts of these results in
    the store's vocabulary and was judged classical by two cold reviews. HOW EACH STATEMENT WAS
    CHECKED (all on 15 November 2026, all second-hand; Goodearl's book and von Neumann's own texts
    were NOT opened). Against the text of Ara and Claramunt, arXiv:1705.04501: the definition of M_K;
    clause (a) with its citation of Goodearl's Theorem 19.6; simplicity of the completion exactly when
    the rank function is extreme (Theorem 19.14); that M_K is a continuous factor, meaning a simple,
    regular, right and left self-injective ring of type II_f (ch. 10); the unique rank function
    (Corollary 21.14); the range [0,1] (stated there to follow from ch. 10); clause (e), their main
    theorem, which they describe as generalising a result of von Neumann, citing Halperin 1968;
    clause (d), which they state as a consequence of their result and Theorem 2.8 of Goodearl 1978,
    for algebras satisfying the equivalent conditions of their Theorem 2.2, of which M_K is the
    first. Against the introduction and statements of Goodearl 1982: that a rank-complete regular
    ring is right and left self-injective (there cited to the book's Theorems 19.7 and 20.8) and
    unit-regular (Theorem 2.3 there), and the comparison of finitely generated projective modules by
    the values of the extreme pseudo-rank functions (Theorem 4.10 there). INFERENCES MADE HERE, not
    quoted from a source: the specialisation of Theorem 4.10 to the simple ring M_K with its one
    rank function (clause (c), first sentence); the passage from isomorphic principal right ideals
    to conjugate idempotents in a unit-regular ring, and from "xR embeds in yR" to x = s y t (clause
    (c), second sentence; both standard, and both proved directly for the switch tower in the working
    note, Lemma 8.6 and Theorem 8.9 of draft 0.5); and the application to the switch tower (last
    paragraph), which rests on clause (e) and the uniqueness clause of
    synthesis.size-of-an-element-of-the-switch-tower. NOT CHECKED: the page range of Goodearl 1982;
    the journal data of the published version of Ara and Claramunt (Canad. J. Math.); what von
    Neumann's own construction of the dimension function uses (an earlier draft of the working note
    made a claim about it that a referee judged probably false; none is made here). Elek's
    arXiv:1402.5499 states the same completed algebra over C to be a simple continuous algebra whose
    rank takes all values in the unit interval, which agrees with clause (b). No machine check is
    attached to an imported statement.
---

## formal
Let $K$ be a field, and $R_{K} = \varinjlim \mathrm{M}_{2^{n}}(K)$ the direct limit along the unital embeddings $a \mapsto \begin{psmallmatrix} a & 0 \\ 0 & a\end{psmallmatrix}$, with the rank function $N(a) = \operatorname{rank}(a)/2^{n}$ for $a \in \mathrm{M}_{2^{n}}(K)$, which is compatible with the embeddings. Let $\mathcal{M}_{K}$ be the completion of $R_{K}$ in the metric $N(a - b)$.
\begin{enumerate}
\item[(a)] \emph{(Completions are regular.)} The completion of a von Neumann regular ring with respect to a rank function is a regular ring, complete in the metric of the unique continuous extension of the rank function, which is again a rank function.
\item[(b)] \emph{(The continuous factor.)} $\mathcal{M}_{K}$ is a simple, unit-regular, right and left self-injective regular ring. It has exactly one rank function $\overline{N}$, and $\overline{N}$ takes every value in the real interval $[0,1]$.
\item[(c)] \emph{(Comparison.)} For finitely generated projective right $\mathcal{M}_{K}$-modules, $A$ is isomorphic to a submodule of $B$ exactly when the rank of $A$ is at most that of $B$, and $A \cong B$ exactly when the ranks are equal. In particular, for $x, y \in \mathcal{M}_{K}$: $x = s\,y\,t$ for some $s, t$ exactly when $\overline{N}(x) \le \overline{N}(y)$, and two idempotents of the same rank are conjugate by a unit.
\item[(d)] \emph{(The scalars are not extended.)} The centre of $\mathcal{M}_{K}$ is $K$.
\item[(e)] \emph{(Uniqueness.)} If $B$ is any ultramatricial $K$-algebra (a countable direct limit of finite products of matrix algebras over $K$) and $N'$ is a non-discrete extremal pseudo-rank function on $B$, the completion of $B$ with respect to $N'$ is isomorphic to $\mathcal{M}_{K}$ as a $K$-algebra.
\end{enumerate}
\emph{Application to the switch tower.} $T = \bigcup_{k}\Cl_{\Q}(k,k)$ is a union of matrix algebras $\mathrm{M}_{2^{k}}(\Q)$ (Theorem \claimref{synthesis.size-of-an-element-of-the-switch-tower}(i)), so it is ultramatricial, and its size $N$ is its only rank function (clause (vi) there), hence extremal, with values $j/2^{k}$ for all $k$, hence non-discrete. By (e) the completion of $T$ in the distance $N(a - b)$ is $\mathcal{M}_{\Q}$, and (a) to (d) hold for it. \emph{Provenance:} (a) \cite[Theorem 19.6]{Goodearl1979}; (b) \cite[Theorems 19.7, 19.14, 20.8, Corollary 21.14, ch.~10]{Goodearl1979}, \cite[Theorem 2.3]{Goodearl1982}; (c) \cite[Theorem 4.10]{Goodearl1982}; (d) \cite{AraClaramunt2017} with \cite[Theorem 2.8]{Goodearl1978}; (e) \cite{AraClaramunt2017}, generalising von Neumann \cite{Halperin1968}; the ring itself is von Neumann's \cite{vonNeumann1936}.

## technical
Take the $2 \times 2$ matrices, embed them diagonally in the $4 \times 4$, those in the $8 \times 8$, and so on, and measure each matrix by its rank divided by its size. Completing the union in the distance ``normalised rank of the difference'' gives von Neumann's continuous regular ring: every element has a pseudo-inverse, the ring is simple, the rank now takes every real value between $0$ and $1$ and is the only such function, elements are compared exactly by their ranks ($x$ factors through $y$ when its rank is no larger), idempotents of equal rank are conjugate, and the centre is still the base field. Any ultramatricial algebra completed in a non-discrete extremal rank gives the same ring. The series' tower of switches over $\Q$ is such an algebra, so its completion is this ring.

## lay
A classical construction, due to von Neumann: keep doubling a grid of numbers, measure each grid by the fraction of it that carries independent information, and fill in the limits. In the result every element can be divided by in a weakened sense, and the measure takes every value between zero and one. The tower of the Transport Papers, completed in the same way, is exactly this classical object.

## one-liner
The rank-metric completion $\mathcal{M}_{K}$ of $\varinjlim \mathrm{M}_{2^{n}}(K)$ is a simple, unit-regular, self-injective regular ring with a unique rank function of range $[0,1]$, comparison of elements by rank, centre $K$, and it is the completion of every ultramatricial $K$-algebra in a non-discrete extremal rank, the switch tower over $\Q$ included (von Neumann; Goodearl; Ara and Claramunt).
