---
id: synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump
kind: claim
version: 1
title: 'Completions of degenerating forms: signature jump, eigenbundle class, transfer'
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
- kind: check
  ref: check.py::check_constant_model_for_corank_two_and_the_twisted_eigenline
- kind: check
  ref: check.py::check_clifford_multiplication_families_and_the_added_generator
lineage:
  motivated_by:
  - transport.obstructions-are-moved-never-destroyed
  - sheaf.wall-class
  - transport.no-transport-terminates
extraction:
  note: >-
    Clauses (1) and (2) are the stored signature count and the stored doubling with the tameness hypotheses
    removed; what is new is the two readings kept apart, the transfer clause, the obstruction of degree one, the
    counter-models, the rank-four example and the Clifford families. Filed against Conjecture 7.9 of the first paper (transport.obstructions-are-moved-never-destroyed, version 3),
    which is linked from the wall-class problem but is the subject of none of its attack items. Two readings of
    ``one exterior model'' are kept apart: the stored one (any nondegenerate K of one signature) and a stricter one
    (a fixed form K_0). Under the first the signature jump is the whole obstruction. Under the second there is
    more: the class of the family's eigenbundles on the exterior, shown here in degree one. What holds in every
    case is the transfer clause, which is the conjecture's ``moved, never destroyed'' as a theorem. The statement
    that the degeneration of Clifford multiplication on the minimal module is not removable for every m = 1, 2,
    3, 5 modulo 8 (beyond the proved m = 1, 2) is the real Bott periodicity through the construction of Atiyah, Bott and Shapiro, cited from
    memory, not derived and not used in any proved clause. Nothing here bears on the one-rung and rung-count
    questions of the wall-class problem for tame walls. Decisions for the maintainer: the status of the
    conjecture and its restatement; a successor problem (derive the classification of the eigenbundle class of
    isolated degenerations in the store's own terms).
  open_problem: op.wall-class-invariant
---

## formal
Let $M$ be a connected manifold, $V \to M$ a real vector bundle of rank $n$ and $G$ a continuous symmetric bilinear form on $V$ (in the series, $V = T^{*}M$ and $G$ a cometric); let $\Sig \subset M$ be the closed set where $G$ is degenerate, and $U$ an open set containing $\Sig$ with $M \setminus U$ nonempty. No tameness hypothesis is made. A \emph{completion standard outside $U$} is a bundle $E \supset V$ with a continuous symmetric form $h$ equal on $M \setminus U$ to $G \perp K$, $K$ a nondegenerate form on a complement of $V$. It is \emph{strict} if $\operatorname{sig} K$ is the same at every point of $M \setminus U$ (the stored reading of ``standard'', Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}), and a \emph{model completion} if moreover the complement is a product $M \times W_{0}$ and $K$ is one fixed form $K_{0}$ on $W_{0}$. For a nondegenerate form and an auxiliary bundle metric write $(\cdot)_{+}$, $(\cdot)_{-}$ for its positive and negative eigenbundles.
\begin{enumerate}
\item[(1)] \emph{(Signature jump.)} If $\operatorname{sig} G$ takes two values on $M \setminus U$, no strict completion standard outside $U$ is nondegenerate at every point of $M$; the set where one degenerates is closed, lies in $U$, and meets every path joining two points of $M \setminus U$ at which $\operatorname{sig} G$ differs. Where in $U$ it lies is not determined by the family: the undeformed $G \perp K$ degenerates on $\Sig$ itself, and for $G = x$ on a line over $\R$ the completions $\begin{psmallmatrix} x & \beta \\ \beta & 1\end{psmallmatrix}$ and $\begin{psmallmatrix} x & \beta \\ \beta & -1\end{psmallmatrix}$ degenerate where $x = \beta^{2}$ and where $x = -\beta^{2}$, on one side or the other according to the sign of $K$.
\item[(2)] \emph{(The double.)} For any bundle metric $A$ on $V$ and any continuous $\beta \colon M \to [0,1]$ positive on $\Sig$ and zero outside $U$, the form $h_{D}(a \oplus a', c \oplus c') = G(a,c) - G(a',c') + \beta\bigl(A(a,c') + A(a',c)\bigr)$ on $V \oplus V$ has signature $(n,n)$ at every point of $M$ and equals $G \perp (-G)$ outside $U$. With $g$ the $A$-self-adjoint map of $G$, the map of $h_{D}$ is $g\,\varepsilon_{1} + \beta\,\varepsilon_{2}$, where $\varepsilon_{1}$ changes the sign of the second copy and $\varepsilon_{2}$ exchanges the copies, two anticommuting maps of square one that commute with $g$, so its square is $g^{2} + \beta^{2}$: the double adjoins to the family one generator anticommuting with it. This is the form of clause (2) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction}, with no tameness.
\item[(3)] \emph{(Strict completions: a dichotomy.)} A strict completion standard outside $U$ and nondegenerate everywhere exists if and only if $\operatorname{sig} G$ is constant on $M \setminus U$: the double is strict exactly then, its $K$ being $-G$.
\item[(4)] \emph{(Transfer.)} Let $h$ be any completion standard outside $U$ and nondegenerate at every point of $M$. Then $h_{\pm}$ are vector bundles over all of $M$, and on $M \setminus U$ they are isomorphic to $G_{\pm} \oplus K_{\pm}$. So the bundles $G_{\pm} \oplus K_{\pm}$ on $M \setminus U$ extend over $M$; if $M$ is contractible they are trivial, $\operatorname{sig} G + \operatorname{sig} K$ is constant, and $w_{1}(K_{\pm}) = w_{1}(G_{\pm})$. Whatever class the eigenbundles of the degenerating family carry on the exterior, relative to $M$, the complement carries its opposite: the obstruction is moved into the adjoined part, not removed. This is a necessary condition on a completion; that the class is the whole obstruction is shown here only for strict completions, in (3).
\item[(5)] \emph{(Model completions: an obstruction of degree one.)} On $M = \R^{2}$ let $G = \begin{psmallmatrix} x & y \\ y & -x\end{psmallmatrix}$, degenerate at the origin only, of signature $(1,1)$ elsewhere, so that (3) gives strict completions. For bounded $U$, no model completion standard outside $U$, with any $W_{0}$ and any $K_{0}$, is nondegenerate everywhere: on a circle around the origin the line $G_{+}$ is spanned at angle $\theta$ by $(\cos\tfrac\theta2, \sin\tfrac\theta2)$ and returns to its negative, so $G_{+} \oplus (K_{0})_{+}$ is not orientable there and cannot be the restriction of a bundle on the plane. The double's $K = -G$ has $K_{+} = G_{-}$, twisted in the same way, as (4) requires.
\item[(6)] \emph{(Each tameness clause fails without obstruction, even for model completions.)} (a) $G = x^{2}$ on a line over $\R$ ((T3) of \claimref{sheaf.tameness} fails): $\begin{psmallmatrix} x^{2} & \beta \\ \beta & -1\end{psmallmatrix}$ has determinant $-(x^{2} + \beta^{2})$. (b) $G = \operatorname{diag}(x,-x)$ over $\R$ ((T2) fails): with $K_{0} = \operatorname{diag}(1,-1)$ and coupling $\beta\begin{psmallmatrix} 1 & 1 \\ 1 & -1\end{psmallmatrix}$ the determinant is $x^{2} + 4\beta^{4}$. (c) $G = x^{2} + y^{2}$ on a line over $\R^{2}$ ((T1) fails): $K_{0} = -1$ as in (a). Each is a model completion of signature $(1,1)$ or $(2,2)$, nondegenerate everywhere.
\item[(7)] \emph{(The clock does not measure the jump.)} $G = x\,\id$ on the trivial bundle of rank four over $\R$ has signature $(4,0)$ for $x > 0$ and $(0,4)$ for $x < 0$: equal residues of $p - q$ modulo $8$ and isomorphic Clifford algebras, $\Cl(4,0) \cong \Cl(0,4)$ (\claimref{std-algebra.periodicity}), yet (1) applies. For a first-order degeneration of corank one the jump is one eigenvalue and the residue changes by $2$.
\item[(8)] \emph{(Multiplication by the position vector.)} Let $E_{1}, \dots, E_{m}$ be symmetric anticommuting maps of square one on $\R^{d}$ (a module of $\Cl(m,0)$) and $g(x) = \sum_{i}x_{i}E_{i}$ over $M = \R^{m}$. Then $g(x)^{2} = Q(x)$: the family degenerates exactly where the vector $x$ is a zero divisor, here at the origin, with corank $d$. If the module carries one more such map $E_{m+1}$, anticommuting with the others, then $g + \beta E_{m+1}$ is nondegenerate everywhere on the same bundle: the degeneration is removed with no added direction, by a form that does not restrict to $G$ inside $U$ (a completion that does needs rank $2d$ at the origin, by (9)). On the module of least dimension this holds for $m = 4$ (computed) and, by the dimensions of the classification, for $m \equiv 0, 4, 6, 7 \pmod 8$; for $m = 1, 2, 3$ no such map exists (computed), and for $m = 1$ and $m = 2$ on the least module no model completion standard outside a bounded $U$ is nondegenerate everywhere, by (1) and (5), the family of (5) being the case $m = 2$.
\item[(9)] \emph{(Cost.)} If $h$ restricts to $G$ on $V$ and is nondegenerate at a point where $G$ has corank $r$, then $E$ has rank at least $n + r$ (\claimref{odd-extensions.imported-minimal-completion-degenerate-algebra-rule}), and if the nondegenerate part of $G$ there has signature $(p,q)$, $h$ has at least $p + r$ positive and $q + r$ negative directions.
\end{enumerate}
\emph{Reading (Conjecture 7.9 of the first paper).} As a statement about every degenerating family the conjecture is false: in (6) each way in which tameness can fail occurs with a completion, of one fixed exterior model, that is nondegenerate everywhere. Where the signature jumps, its conclusion that no completion of one exterior signature is nondegenerate everywhere is true with no tameness (1); its further clause, that the degeneration reappears on a displaced locus on the other side, is not: by (1) the place is not fixed by the family. What is true of every family is (4): a completion that is nondegenerate everywhere carries on its complement the opposite of the class of the family's eigenbundles, so the obstruction is moved. That class is an obstruction, and in the strict reading, where it is the signature, the only one. Its part of degree zero is the integer signature, not a residue modulo $8$ (7); it has parts of higher degree, of which (5) is the first. For an isolated degeneration in codimension $m$ the pattern of (8), removable for $m \equiv 0, 4, 6, 7$ and not for $m = 1, 2$, is periodic in $m$ with period eight on the removable side by the classification; that on the least module it is not removable by a model completion for every $m \equiv 1, 2, 3, 5 \pmod 8$, beyond the cases $m = 1, 2$ proved here, is the periodicity theorem of Bott in the form of Atiyah, Bott and Shapiro (cited from memory, not derived here, not used above). In that sense the clock of the conjecture is found in the codimension of the locus, not in the residues of the two sides.

## technical
For a continuous family $G$ of symmetric forms on a connected base, tame or not, and completions $h = G \perp K$ outside a neighbourhood $U$ of the degeneration set:

(1) if the signature of $G$ jumps between exterior points, no completion with one exterior signature of $K$ is nondegenerate everywhere (where it degenerates depends on $K$);

(2), (3) if it does not jump, the double $g\varepsilon_{1} + \beta\varepsilon_{2}$ is one, of signature $(n,n)$, its square being $g^{2} + \beta^{2}$; the double adjoins one generator anticommuting with the family;

(4) in every completion that is nondegenerate everywhere, the complement's eigenbundles carry, on the exterior, the opposite of the class of the family's eigenbundles relative to the base (transfer);

(5) with a fixed exterior form $K_{0}$ there are further obstructions: $\begin{psmallmatrix} x & y \\ y & -x\end{psmallmatrix}$, whose positive eigenline is twisted around the origin, has no such completion;

(6) $x^{2}$, $\operatorname{diag}(x,-x)$ and $x^{2}+y^{2}$ have completions with a fixed exterior form, one for each tameness clause;

(7) $x\,\id$ in rank four jumps from $(4,0)$ to $(0,4)$ with equal residues modulo $8$ and is obstructed;

(8) multiplication by the position vector on a module of $\Cl(m,0)$ degenerates at the zero divisor $x = 0$ and is repaired on the same module when the module carries one more anticommuting generator: on the least module for $m \equiv 0, 4, 6, 7 \pmod 8$, not for $m = 1, 2, 3$.

Ledger: transport-convenient throughout. (1) to (7) and (9) are linear algebra and continuity. (8) is standard Clifford-module theory (prior art: Atiyah, Bott and Shapiro 1964, for least modules and their extension), read on the series' own object: the family is division by a vector and its repair the adjunction of a generator.

## lay
The first paper of the series conjectured that repairing a failure of division on one side of a boundary always pushes the failure to a new place on the other side, and that an invariant built from an eight-step clock measures this. That was proved for the simplest kind of boundary. This result decides it for the notion of repair the series had stored, and shows what takes its place beyond that.

As first stated, the conjecture is false: there are degenerations of each kind the simple case excludes that can be repaired everywhere, using the same extra structure on all sides. Where the geometry changes its signature across the boundary, no repair using extra structure of one signature works everywhere, for every kind of boundary; where the failure then reappears is not fixed, and can be on either side. And one part of it is true always, in a sharper form than was conjectured: any repair that works everywhere must carry, in the structure it adds, the mirror image of the twist that the degenerating geometry had. The obstruction is not removed. It is moved into what was added.

The invariant is that twist. Its simplest part is the signature itself, a pair of whole numbers, and not the eight-step clock: there is a boundary where the clock reads the same on both sides and the repair is still impossible. But there are subtler parts, which appear when the degeneration happens at a point and not across a wall. For the most natural example, multiplication by a position vector, which fails exactly where the vector cannot be divided by, whether the failure can be repaired on the smallest space the multiplication acts on, without adding anything (by a repair that changes the multiplication near the point), depends on the number of dimensions with a period of eight. The repairable half of that pattern is proved here; the other half is a classical theorem, cited and not proved here. The clock is there after all, in the dimension of the place where division fails.

## one-liner
For any continuous family of symmetric forms: a completion with one exterior signature that is nondegenerate everywhere exists iff the signature does not jump (the double, which adjoins one anticommuting generator); every such completion carries on its complement the opposite of the family's eigenbundle class (transfer); with a fixed exterior form there are further obstructions ($\begin{psmallmatrix} x & y \\ y & -x\end{psmallmatrix}$, twisted eigenline); so Conjecture 7.9 fails as stated ($x^{2}$, $\operatorname{diag}(x,-x)$, $x^{2}+y^{2}$), holds where the signature jumps, and the eigenbundle class is an obstruction, the integer signature being its part of degree zero.
