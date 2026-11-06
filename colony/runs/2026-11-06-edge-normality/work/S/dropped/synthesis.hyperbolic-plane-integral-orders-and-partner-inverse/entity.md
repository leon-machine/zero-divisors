---
id: synthesis.hyperbolic-plane-integral-orders-and-partner-inverse
kind: claim
version: 1
title: Integral orders of the hyperbolic plane and the Witt partner as generalised inverse
status: proved
region: synthesis
subject: clifford-structure
tags: [hyperbolic-plane, two-readings, idempotents, degenerate-algebras]
proposed_by:
  kind: ai
  session: 2026-11-06-edge-normality
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-06-edge-normality
review: draft
derivations:
- name: main
  uses:
  - std-algebra.witt-basis-car@1
  - std-algebra.cl11-matrix@1
  - one-relation.two-presentations@4
  - transport.regularity-localises-zero-divisors-idempotents@2
  - std-algebra.radical-ideal-and-quotient@1
  - conformal.minimal-nondegenerate-completion@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_witt_order_is_the_integer_matrices
- kind: check
  ref: check.py::check_orthogonal_order_has_index_four_and_no_idempotents
- kind: check
  ref: check.py::check_partner_is_a_generalised_inverse
- kind: check
  ref: check.py::check_derivative_through_the_partner
- kind: check
  ref: check.py::check_radical_vector_has_no_generalised_inverse
- kind: proof
  derivation: main
extraction:
  note: >-
    From Leon's working document "Scalars and the Continuum: Review and Extensions" (6 November
    2026), items on the integral orders of the (1,1) plane and on the Witt partner as a generalised
    inverse, re-proved and re-checked here; not an attack on an open problem. What is new against the
    store is (i), (ii) and (iv): the two presentations of Proposition one-relation.two-presentations
    generate the same algebra over any ring containing 1/2 but different orders over the integers,
    and only the Witt one contains idempotents; and the partner turns the null difference of a
    function into its derivative times an integral idempotent. Clause (iii) restates in claim form
    what the store holds as T01's remark that the null partner is the Moore-Penrose pseudoinverse
    (note.transport.setting-hyperbolic-atom-matrix-algebra-moore) and as clause (ii) of
    descent-lift.pairing-creator-under-transport-algorithm; (v) is a one-line consequence of the
    stored radical-ideal result. Ledger: transport-convenient. The Witt pair is the ascent's
    hyperbolic pair, and the integral statements say that the null presentation, not the orthogonal
    one, is the one defined over the integers; nothing here needs the completion beyond that reading.
    Cited from memory and not used in the proof: the Clifford algebra of a hyperbolic quadratic
    module over a commutative ring is the endomorphism ring of the exterior algebra of a Lagrangian
    (Bass, Amer. J. Math. 96 (1974); Knus, Quadratic and Hermitian Forms over Rings (1991)), and the
    integer matrices are a maximal order in the rational ones (Reiner, Maximal Orders).
---

## formal
In $\Cl(1,1)$ let $e_{+}, e_{-}$ be orthonormal with $Q(e_{+}) = 1$, $Q(e_{-}) = -1$, and $a = \tfrac12(e_{+} + e_{-})$, $a' = \tfrac12(e_{+} - e_{-})$, so $a^{2} = a'^{2} = 0$ and $aa' + a'a = 1$. Let $\Lambda_{W}$ be the $\Z$-span of all products of $a, a'$ and $\Lambda_{O}$ the $\Z$-span of all products of $e_{+}, e_{-}$.
\begin{enumerate}
\item[(i)] \emph{(The Witt order.)} $\Lambda_{W} = \Z \oplus \Z a \oplus \Z a' \oplus \Z aa'$, and $x = \alpha\,aa' + \beta\,a + \gamma\,a' + \delta\,a'a \mapsto \begin{psmallmatrix} \alpha & \beta \\ \gamma & \delta \end{psmallmatrix}$ is a ring isomorphism of $\Lambda_{W}$ onto $\Mat_{2}(\Z)$, with $a, a'$ the off-diagonal matrix units and $aa'$, $a'a$ integral orthogonal idempotents summing to $1$.
\item[(ii)] \emph{(The orthogonal order.)} $\Lambda_{O} = \Z \oplus \Z e_{+} \oplus \Z e_{-} \oplus \Z e_{+}e_{-}$ is a subring of $\Lambda_{W}$ of index $4$, consisting of the matrices with $\alpha \equiv \delta$ and $\beta \equiv \gamma \bmod 2$, and $2\Lambda_{W} \subset \Lambda_{O}$, so $\Lambda_{O}[\tfrac12] = \Lambda_{W}[\tfrac12]$. Every element of $\Lambda_{O}$ has integer scalar part, every idempotent of $\Cl(1,1)$ other than $0, 1$ has scalar part $\tfrac12$, and so $\Lambda_{O}$ contains no idempotent other than $0$ and $1$; the idempotents $\tfrac12(1 \pm e_{+})$ of the orthogonal reading need $\tfrac12$. On the vector lattices, $Q(xa + ya') = xy$ on $\Z a + \Z a'$, whose polar form $Q(u + v) - Q(u) - Q(v)$ is unimodular (the hyperbolic quadratic module), while $Q(xe_{+} + ye_{-}) = x^{2} - y^{2}$ on the index-$2$ sublattice $\Z e_{+} + \Z e_{-}$, whose polar form has determinant $-4$ and whose bilinear form, half the polar form, is integral and unimodular: the two presentations of the one relation are the same over $\Z[\tfrac12]$ and differ over $\Z$ as a unimodular quadratic form and a unimodular bilinear form.
\item[(iii)] \emph{(The partner as generalised inverse.)} For every Witt pair $n, m$ of a Clifford algebra ($n^{2} = m^{2} = 0$, $nm + mn = 1$), $nmn = n$ and $mnm = m$, and $mn$, $nm$ are complementary idempotents. In $\Cl(1,1)$, for the anti-automorphism $\dagger$ (reversion composed with $e_{-} \mapsto -e_{-}$), which exchanges $a$ and $a'$, the idempotents $aa'$ and $a'a$ are self-adjoint, so $a'$ is the Moore-Penrose inverse of $a$ for $\dagger$.
\item[(iv)] \emph{(The derivative through the partner.)} For a polynomial $f$ with rational coefficients and a rational $x$, $f(x + n) = f(x) + f'(x)\,n$, and
\[
m\,\big(f(x + n) - f(x)\big) = f'(x)\,P, \qquad P = mn,
\]
and the same for a rational function regular at $x$. For $f$ with integer coefficients, $x \in \Z$ and $(n, m) = (a, a')$, both sides lie in $\Lambda_{W}$: dividing the null difference by the null step through its partner returns the derivative times the integral idempotent $P$ in place of $1$.
\item[(v)] \emph{(No inverse before the ascent.)} In $\Cl(p,q,r)$ with $r \ge 1$ every vector $\rho$ of the radical satisfies $\rho\,x\,\rho = 0$ for every $x$, so $\rho$ has no generalised inverse and $\Cl(p,q,r)$ is not von Neumann regular; in its minimal completion, which is nondegenerate and so regular, $\rho$ becomes a null vector with a partner, and (iv) is the image of the dual-number expansion $f(x + \rho) = f(x) + f'(x)\rho$ under $\rho \mapsto n$.
\end{enumerate}

## technical
The hyperbolic plane can be presented by a null pair $a, a'$ with $aa' + a'a = 1$ or by an orthonormal pair $e_{\pm}$ with $e_{\pm}^{2} = \pm 1$, and over the rationals these give the same algebra, the $2 \times 2$ matrices. Over the integers they do not. The integer combinations of products of the null pair are exactly the integer matrices, with the null vectors as the off-diagonal matrix units and $aa'$, $a'a$ as integral idempotents. The integer combinations of products of the orthonormal pair form a subring of index $4$ with no idempotents at all, since its elements have integer scalar parts and every nontrivial idempotent of the plane has scalar part one half. Twice the null order lies inside the orthogonal one, so the two agree once $\tfrac12$ is allowed: the difference is that between a quadratic form, $Q(xa + ya') = xy$, and a bilinear one, $x^{2} - y^{2}$, which over the integers are two different unimodular lattices.

The partner of a null vector is its generalised inverse, $nmn = n$, and for the adjoint that exchanges the pair it is the Moore-Penrose inverse, as the store already records for the hyperbolic atom. Used on a difference it gives a derivative without any degenerate direction: $m(f(x + n) - f(x)) = f'(x)\,mn$, the derivative multiplied by an idempotent instead of by $1$, with everything integral when $f$ and $x$ are. Before the ascent this is impossible: a radical vector of a degenerate algebra kills every sandwich $\rho x \rho$, so it has no generalised inverse, and it gains one only when the minimal completion pairs it with a partner.

## lay
The flat plane with one time-like and one space-like direction can be described with two directions of opposite sign or with two light-like directions. With fractions allowed both descriptions build the same structure. With only whole numbers they do not: the light-like description builds all whole-number $2 \times 2$ matrices, including the elements that act as projections, while the other builds a smaller ring with no projections at all, because those need a factor of one half. The light-like partner of a light-like direction also acts as its best available inverse, and using it to divide a small light-like change of a function by the size of the step gives the function's derivative, multiplied by a projection.

## one-liner
The null pair $a, a'$ of the hyperbolic plane generates $\Mat_{2}(\Z)$ with integral idempotents $aa'$, $a'a$, while the orthonormal pair generates an index-$4$ suborder with no idempotents, the two agreeing over $\Z[\tfrac12]$; the partner is the generalised inverse of its null vector, $nmn = n$, and gives $m(f(x + n) - f(x)) = f'(x)\,mn$, which a radical vector, with $\rho x \rho = 0$, cannot.
