---
id: synthesis.completion-recovers-the-real-clifford-algebras
kind: claim
version: 2
title: "Completion recovers the real Clifford algebras; Sylvester's law of inertia in GA"
status: proved
region: synthesis
subject: clifford-structure
tags: [clifford-classification, degenerate-algebras, needs-continuum, classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-07-bit-root
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-bit-root
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 2
  source: run 2026-11-08-foundation-layer
review: draft
about:
- obj.std-algebra.quadratic-space
- obj.std-algebra.clifford-algebra
founded_on:
- synthesis.continuum-completion-premise@2
derivations:
- name: main
  uses:
  - std-algebra.polarisation@2
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.blade-basis@1
  - std-algebra.functoriality@1
  - std-algebra.existence-uniqueness@1
  - conformal.minimal-nondegenerate-completion@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_complete_field_square_root_step
- kind: check
  ref: check.py::check_orthogonal_basis_by_rejection
- kind: check
  ref: check.py::check_inertia_is_basis_independent
- kind: check
  ref: check.py::check_base_change_and_degenerate_embedding
- kind: check
  ref: check.py::check_square_classes_survive_over_the_rationals
- kind: proof
  derivation: main
locators:
  paper: T00a
  number: Thm 6.1
  label: thm:bitinertia
  line: 279
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  note: >-
    From Leon's working document "From the Bit to the Numbers" (7 November 2026), Step 5 (the
    continuum) and its item "Only signs survive in R", proved and checked here; not an attack on an
    open problem. This is the bridge from the ladder's rational Clifford algebras to the store's real
    ones. Clauses (i), (iv) and (vi) are its content under premise (F4) (filed alongside as
    synthesis.continuum-completion-premise; the rational algebras it starts from are those of
    synthesis.division-gives-the-rationals and synthesis.signed-directions-and-the-integer-clifford-algebra); the result is stated for an arbitrary ordered field F so that it does not depend on
    that premise as an edge, and the maintainer may add an assumes edge to it for clause (iv) at
    acceptance. Derived here, not imported: clauses (ii) and (iii) prove, over any Euclidean ordered
    field, what the former imported Fact std-algebra.sylvester-inertia stated for the reals (it is retired in favour of this result; orthogonal bases
    squaring to 1, -1, 0; the invariance of (p, q, r) with r the dimension of the radical; isometry
    exactly when the triples agree; that p + q is the rank of a Gram matrix follows from r = n - rank);
    Leon retired the Fact on 7 November 2026 and its dependants now cite clause (iii). Correction to the source document: its "Only signs
    survive in R" holds already over any Euclidean field (every positive element a square), which is
    far smaller than R and need not be complete; completeness is used for the square roots only through
    clause (i), and otherwise for limits (the exponential of a bivector, the angle pi), roots of real
    polynomials of odd degree and Frobenius' theorem (for which a real closed field suffices). The rational examples in (v) are the source's
    "with squares 2 and 3 it has none". Ledger: transport-absent (classical quadratic-form theory
    restated in geometric algebra). Prior art, cited from memory and not used in the proof: Sylvester
    (1852); Lam, Introduction to Quadratic Forms over Fields (2005), on Euclidean fields and square
    classes; the Hasse-Minkowski theorem, which classifies rational forms by their real and p-adic
    invariants (the primes a rational direction carries).
---

## formal
Let $F$ be an ordered field. A quadratic space over $F$ is a finite-dimensional $F$-vector space $V$ with $Q(\lambda v) = \lambda^{2}Q(v)$ and polar form $B(u, v) = \tfrac12(Q(u + v) - Q(u) - Q(v))$ bilinear (as in \claimref{obj.std-algebra.quadratic-space}, with $F$ for $\R$); its Clifford algebra is defined by the universal property of \claimref{obj.std-algebra.clifford-algebra} over $F$, in which $uv + vu = 2B(u,v)$. $F$ is \emph{Euclidean} if every positive element is a square. $\Cl_{F}(p,q,r)$ is the Clifford algebra of $F^{n}$, $n = p + q + r$, with an orthogonal basis of $p$, $q$, $r$ vectors of squares $1$, $-1$, $0$.
\begin{enumerate}
\item[(i)] \emph{(Completeness gives square roots.)} If $F$ is complete (every nonempty subset bounded above has a least upper bound), then $F$ is Euclidean.
\item[(ii)] \emph{(Orthogonal bases by rejection.)} Every quadratic space over $F$ has a basis $u_{1}, \dots, u_{n}$ of mutually anticommuting vectors, $u_{i}u_{j} = -u_{j}u_{i}$ for $i \ne j$, obtained by repeated rejection $x \mapsto x - B(x, u)\,u^{-1}$ from vectors $u$ with $Q(u) \ne 0$. If $F$ is Euclidean, the basis can be chosen with $Q(e_{i}) \in \{1, -1, 0\}$, by $e_{i} = u_{i}/\sqrt{|Q(u_{i})|}$ where $Q(u_{i}) \ne 0$.
\item[(iii)] \emph{(Sylvester's law of inertia.)} For any ordered $F$, the numbers $p$, $q$, $r$ of vectors with $Q > 0$, $Q < 0$, $Q = 0$ in an anticommuting basis do not depend on the basis: $r = \dim \operatorname{rad} V$, and $p$ (respectively $q$) is the largest dimension of a subspace on which $Q$ is positive (negative) definite. If $F$ is Euclidean, two quadratic spaces are isometric if and only if they have the same $(p, q, r)$, and then $\Cl(V, Q) \cong \Cl_{F}(p,q,r)$.
\item[(iv)] \emph{(The completion recovers the store's algebra.)} Let $\Cl_{\Q}(p,q,r)$ be the $\Q$-span of the blades with the blade product of Proposition \claimref{std-algebra.orthogonal-anticommute} (structure constants $0$, $\pm 1$). If $\R$ is a complete ordered field, as premise (F4) takes it, then $e_{S} \mapsto e_{S}$ extends to an isomorphism $\Cl_{\Q}(p,q,r) \otimes_{\Q} \R \cong \Cl(p,q,r)$, and for every real quadratic space $\Cl(V, Q) \cong \Cl_{\Q}(p,q,r) \otimes_{\Q} \R$ with $(p, q, r)$ its inertia; through $r$ added hyperbolic planes it embeds in the nondegenerate $\Cl_{\Q}(p{+}r,q{+}r) \otimes_{\Q} \R$, the radical generators going to null vectors $e'_{k} + f'_{k}$ (Theorem \claimref{conformal.minimal-nondegenerate-completion}). So every real Clifford algebra of the store is, up to isomorphism, a rational Clifford algebra of a $\pm 1$ form, or a subalgebra of one, extended by scalars.
\item[(v)] \emph{(Over $\Q$ square classes remain.)} Over $\Q$, (ii) holds without the normalisation and the invariance of $(p, q, r)$ in (iii) holds, but the isometry criterion fails: $Q(\lambda u) = \lambda^{2}Q(u)$ fixes $Q(u)$ only up to a nonzero rational square. The line with $e^{2} = 2$ is not isometric to the line with $e^{2} = \pm 1$; its Clifford algebra, with $x\bar{x} = a^{2} - 2b^{2}$ for $x = a + be$, has no zero divisors, while $\Cl_{\Q}(1,0)$ has $(1 + e_{1})(1 - e_{1}) = 0$. The plane with $e_{1}^{2} = 2$, $e_{2}^{2} = 3$ has $x\bar{x} = a^{2} - 2b^{2} - 3c^{2} + 6d^{2}$ for $x = a + be_{1} + ce_{2} + de_{1}e_{2}$, which has no nontrivial rational zero, so its Clifford algebra is a division ring, while $\Cl_{\Q}(2,0)$ has zero divisors. Over any Euclidean field they become $\Cl(1,0)$ and $\Cl(2,0)$.
\item[(vi)] \emph{(What is used.)} Clauses (ii) to (iv) use of the coefficient field only that it is ordered and, for the normalisation, Euclidean. Completeness enters (iv) only through (i).
\end{enumerate}

## technical
Assuming the coefficients are completed to a complete ordered field (premise (F4)), the real Clifford algebras of the store are recovered from the ladder's rational ones. Completeness gives square roots of positive numbers; with them every quadratic space, degenerate or not, has a basis of mutually anticommuting vectors squaring to $1$, $-1$ or $0$, found by rejecting each vector from those already chosen, and the three counts are invariants: the number of null vectors is the dimension of the radical, and the number of positive ones is the largest dimension on which the form is positive definite (Sylvester's law of inertia, derived here in geometric algebra). The blade product has structure constants $0$ and $\pm 1$, so every real Clifford algebra is a rational one extended by scalars, and a degenerate one sits inside a nondegenerate one through null vectors of added hyperbolic planes. What is used is less than completeness: the diagonalisation to signs holds over any ordered field in which positive elements are squares. Over the rationals it fails in a definite way: a direction squaring to $2$ cannot be rescaled to square $1$, and the plane with squares $2$ and $3$ has no zero divisors over $\Q$, unlike the Euclidean plane. Completeness itself is what limits need, such as the exponential of a bivector and the angle $\pi$, not the signs.

## lay
If the number line is taken to have no gaps, every way of measuring lengths and times in a flat space can be rescaled until each basic direction counts as plus one, minus one or zero, and how many of each there are does not depend on the directions chosen. This holds as soon as positive numbers have square roots, which needs much less than the full number line. With fractions alone it fails: a direction whose square is $2$ cannot be rescaled to square $1$, and some planes then behave differently, for example having no elements that multiply to zero. Under that assumption, all the algebras the store uses are the ones built earlier from whole numbers and fractions, extended to real coefficients.

## one-liner
If the coefficients form a complete ordered field (premise (F4)), every real quadratic space has an anticommuting basis of squares $1, -1, 0$ with invariant counts (Sylvester, derived in GA; Euclidean suffices) and every real Clifford algebra is $\Cl_{\Q}(p,q,r) \otimes \R$, inside $\Cl_{\Q}(p{+}r,q{+}r) \otimes \R$; over $\Q$ square classes remain ($\langle 2, 3\rangle$ is a division algebra).
