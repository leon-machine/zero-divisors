---
id: synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump
kind: claim
version: 1
title: Strict completions and the signature jump
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, obstruction-types, no-go, classification]
proposed_by:
  kind: ai
  session: 2026-11-18-navigate
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-navigate
review: draft
derivations:
- name: main
  uses:
  - sheaf.conservation-degeneracy-absolute-form@4
  - synthesis.wall-class-one-rung-obstruction@3
  - odd-extensions.imported-minimal-completion-degenerate-algebra-rule@5
  - std-algebra.periodicity@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_double_squares_to_a_positive_form_and_is_split
- kind: check
  ref: check.py::check_counter_models_for_each_tameness_clause
- kind: check
  ref: check.py::check_signature_jump_obstructs_with_matched_clocks
- kind: check
  ref: check.py::check_one_added_direction_and_the_corank_bound
lineage:
  motivated_by:
  - transport.obstructions-are-moved-never-destroyed
  - sheaf.wall-class
  - transport.no-transport-terminates
extraction:
  note: >-
    Filed against Conjecture 7.9 of the first paper (transport.obstructions-are-moved-never-destroyed, version 3),
    which is linked from the wall-class problem but is the subject of none of its attack items. The result
    decides the conjecture in its strict reading for every family, tame or not: it holds exactly where the
    signature of the family differs between exterior points, by the stored argument with the tameness hypotheses
    removed, and it fails otherwise, by the stored doubling, which is strict when the signature does not jump.
    Nothing here bears on the one-rung and rung-count questions of the wall-class problem. Decisions for the
    maintainer: the status of the conjecture (refuted as stated beyond the tame case, with its true part proved
    here), and whether its invariant clause is restated around the integer signature.
  open_problem: op.wall-class-invariant
---

## formal
Let $M$ be a connected manifold, $V \to M$ a real vector bundle of rank $n$ and $G$ a continuous symmetric bilinear form on $V$ (in the series, $V = T^{*}M$ and $G$ a cometric); let $\Sig \subset M$ be the closed set where $G$ is degenerate, and let $U$ be an open set containing $\Sig$ with $M \setminus U$ nonempty. A \emph{strict completion of $G$, standard outside $U$}, is a vector bundle $E \supset V$ with a continuous symmetric form $h$ such that on $M \setminus U$ one has $h = G \perp K$, with $K$ a nondegenerate form on a complement of $V$ whose signature is the same at every point of $M \setminus U$ (the reading of ``standard'' in Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}: one exterior model). No tameness hypothesis is made: the corank of $G$ on $\Sig$, the order of the degeneration and the shape of $\Sig$ are arbitrary.
\begin{enumerate}
\item[(1)] \emph{(Obstruction.)} If $\operatorname{sig} G$ takes two different values on $M \setminus U$, no strict completion standard outside $U$ is nondegenerate at every point of $M$. The set where a given one degenerates is closed, lies in $U$, and meets every path joining two points of $M \setminus U$ at which $\operatorname{sig} G$ differs.
\item[(2)] \emph{(Existence.)} If $\operatorname{sig} G$ is constant on $M \setminus U$, a strict completion standard outside $U$ and nondegenerate at every point of $M$ exists: for any bundle metric $A$ on $V$ and any continuous $\beta \colon M \to [0,1]$ that is positive on $\Sig$ and vanishes outside $U$, the form
\[
h_{D}(a \oplus a', c \oplus c') \;=\; G(a,c) - G(a',c') + \beta\bigl(A(a,c') + A(a',c)\bigr)
\]
on $V \oplus V$ has signature $(n,n)$ at every point of $M$ and equals $G \perp (-G)$ outside $U$. With $g$ the $A$-self-adjoint map of $G$ and $\hat h$ that of $h_{D}$ for $A \oplus A$, $\hat h^{2} = (g^{2} + \beta^{2}) \oplus (g^{2} + \beta^{2})$. This is the doubling of clause (2) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction}; what is added is that it is strict exactly when the signature of $G$ does not jump.
\item[(3)] \emph{(Dichotomy.)} Hence a strict completion standard outside $U$ and nondegenerate everywhere exists if and only if $\operatorname{sig} G$ is constant on $M \setminus U$. The obstruction is the function $\operatorname{sig} G$ on $M \setminus U$ modulo constants: an integer invariant of degree zero.
\item[(4)] \emph{(Each tameness clause fails without obstruction.)} On $M = \R$ with coordinate $x$, or $M = \R^{2}$ with coordinates $(x,y)$, and trivial bundles: (a) $G = x^{2}$ on a line, corank one on a smooth hypersurface, degenerating to second order ((T3) of \claimref{sheaf.tameness} fails); (b) $G = \operatorname{diag}(x, -x)$, first order with corank two ((T2) fails); (c) $G = x^{2} + y^{2}$ on a line, and $G = \begin{psmallmatrix} x & y \\ y & -x\end{psmallmatrix}$, degenerate at the origin only ((T1) fails). In each the signature is the same at every nondegenerate point, so by (2) each has a strict completion that is nondegenerate everywhere. For (a) one added direction suffices: $\begin{psmallmatrix} x^{2} & \beta \\ \beta & -1\end{psmallmatrix}$ has determinant $-(x^{2} + \beta^{2})$.
\item[(5)] \emph{(The clock does not measure it.)} $G = x\,\id$ on the trivial bundle of rank four over $\R$ has signature $(4,0)$ for $x > 0$ and $(0,4)$ for $x < 0$. The residues of $p - q$ modulo $8$ agree, and $\Cl(4,0) \cong \Cl(0,4) \cong \Mat_{2}(\HH)$ (\claimref{std-algebra.periodicity}), yet by (1) no strict completion is nondegenerate everywhere. Conversely a jump of the clock is a jump of the signature. So the invariant of (3) is the integer signature and not its residue modulo $8$; for a first-order degeneration of corank one the two agree, the jump being one eigenvalue and the residue changing by $2$.
\item[(6)] \emph{(What a completion costs.)} If $E \supset V$ carries a form $h$ restricting to $G$ on $V$ and nondegenerate at a point where $G$ has corank $r$, then $E$ has rank at least $n + r$ and $h$ has at least $r$ directions of each sign there (\claimref{odd-extensions.imported-minimal-completion-degenerate-algebra-rule}). The double of (2) has rank $2n$.
\end{enumerate}
\emph{Reading (Conjecture 7.9 of the first paper).} The conjecture, in its strict reading and for families outside the tame corank-one case, asserts that every completion nondegenerate of constant signature on one side degenerates on the other. By (1) that holds whenever the signature of the family differs between the sides, with no tameness assumed; by (4) it fails in each of the three ways tameness can fail when the signature does not differ; and by (5) the invariant it asks for is not built from the residues modulo $8$. With the exterior model free to change, nothing obstructs (the stored clause (2)), and the cost is counted in added directions, at least the corank by (6).

## technical
A strict completion is a form $h = G \perp K$ outside a neighbourhood $U$ of the degeneration set, with one signature of $K$ there. For any continuous family of symmetric forms on a connected base, tame or not:

(1) if the signature of $G$ differs between two exterior points, every strict completion degenerates somewhere in $U$, on a closed set separating the two points;

(2) if the signature of $G$ is constant on the exterior, the double $h_{D} = \begin{psmallmatrix} G & \beta \\ \beta & -G \end{psmallmatrix}$ (in a frame orthonormal for an auxiliary metric, $\beta$ positive on the degeneration set and zero outside $U$) is a strict completion of signature $(n,n)$, nondegenerate everywhere, because its square is $g^{2} + \beta^{2}$ on each copy.

So strict completions that are nondegenerate everywhere exist exactly when the signature does not jump. Counter-models to the conjectured general conservation, one for each tameness clause: $x^{2}$ (second order), $\operatorname{diag}(x,-x)$ (corank two), $x^{2} + y^{2}$ and $\begin{psmallmatrix} x & y \\ y & -x\end{psmallmatrix}$ (degeneration at a point). The invariant is the integer signature: $x\,\id$ in rank four jumps from $(4,0)$ to $(0,4)$, with equal residues modulo $8$ and isomorphic Clifford algebras, and is still obstructed.

A completion nondegenerate at a point of corank $r$ adds at least $r$ directions.

Ledger: transport-convenient. The argument is linear algebra and continuity; the transport rules enter only through the reading of the conjecture.

## lay
The first paper of the series conjectured that repairing a failure of division on one side of a boundary always pushes the failure to a new place on the other side, and that some invariant built from an eight-step clock measures this. That was proved for the simplest kind of boundary. This result settles the general case, and the answer is mixed.

If the geometry changes its signature across the boundary (a direction that was space-like becomes time-like, say), the conjecture is true for every kind of boundary: no repair that uses the same extra structure on both sides can work everywhere. If the signature is the same on both sides, the conjecture is false: there is an explicit repair that works everywhere, for every kind of degeneration. And the thing that decides between the two cases is the signature itself, a pair of whole numbers, not the eight-step clock: there is a boundary where the clock reads the same on both sides and the repair is still impossible.

## one-liner
For any continuous family of symmetric forms on a connected base, a completion $G \perp K$ with one exterior signature of $K$ that is nondegenerate everywhere exists if and only if the signature of $G$ does not jump; Conjecture 7.9 of the first paper therefore holds, without tameness, exactly where the signature jumps, fails otherwise ($x^{2}$, $\operatorname{diag}(x,-x)$, $x^{2}+y^{2}$), and its invariant is the integer signature, not the residue modulo $8$.
