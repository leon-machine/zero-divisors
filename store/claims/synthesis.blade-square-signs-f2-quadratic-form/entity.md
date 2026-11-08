---
id: synthesis.blade-square-signs-f2-quadratic-form
kind: claim
version: 3
title: Blade square signs as a quadratic form over the two-element field
status: proved
region: synthesis
subject: clifford-structure
tags: [clifford-classification, grading-and-parity, hyperbolic-plane, classical-theorem]
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
- name: Claude Opus 5.5
  role: 'maintainer pass, the derivation citing the retired imported Fact removed'
  version: 3
  source: run 2026-11-07-bit-root
review: draft
derivations:
- name: main
  uses:
  - std-algebra.orthogonal-anticommute@1
  - transport.classification-real-clifford-algebras@3
  - primer.sign@2
  - tower.commuting-copies@5
  - tower.rigidity-clock-frozen@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_symmetry_forces_the_sign
- kind: check
  ref: check.py::check_blade_signs_are_a_quadratic_form
- kind: check
  ref: check.py::check_radical_gauss_sum_and_type
- kind: check
  ref: check.py::check_ascent_adds_a_hyperbolic_plane
- kind: check
  ref: check.py::check_anisotropic_plane_exchanges_p_and_q
- kind: proof
  derivation: main
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: >-
      Version 2 -> 3. Leon's decision of 7 November 2026: the imported Fact
      synthesis.imported-real-clifford-algebras-as-twisted-group-algebras-and-the-arf-invariant is retired, replaced by
      synthesis.signed-directions-and-the-integer-clifford-algebra, which derives its clause (a) over every commutative ring and its
      clause (b) for the Clifford twisting functions; clause (c) is clause (iv) here. The standard-route derivation that cited the
      Fact is removed (derivation main is self-contained and unchanged); the literature stays as prior art in this note.
  note: >-
    From Leon's working document "Scalars and the Continuum: Review and Extensions" (6 November
    2026), items on the directional skeleton and on the sign from symmetry, re-proved and re-checked
    here; not an attack on an open problem. Ledger: clauses (i) to (iv) are transport-absent, a
    reformulation of the classification of real Clifford algebras by a quadratic form over the
    two-element field; clause (v) is transport-convenient, the (1,1) ascent read as adding a form of
    Arf invariant 0, which is the division-ring part of the stored rigidity theorem in this language.
    Classical, restated: clauses (ii) to (iv) are stated and proved in V. Ovsienko, "Real Clifford
    algebras and quadratic forms over F_2: two old problems become one", arXiv:1601.07664 (Cl(p,q) as a
    twisted group algebra of F_2^n; isomorphism iff the F_2 forms are equivalent; the Arf invariant
    separates real from quaternionic), and in A. Elduque and A. Rodrigo-Escudero, "Clifford algebras as
    twisted group algebras and the Arf invariant", Adv. Appl. Clifford Algebras (2018),
    arXiv:1801.07002 (checked against the arXiv texts; formerly pinned as an imported Fact, now retired); the Gauss sum
    sum_S e_S^2 is the signature of the trace form x -> <x^2>_0, which is +k, 0, -2k on Mat_k(R),
    Mat_k(C), Mat_k(H). Clause (v) is Theorem tower.commuting-copies at one plane read in F_2 language,
    with the type statement that of Theorem tower.rigidity-clock-frozen. Clause (i) is a two-line
    classical observation, kept as a remark. Cited from memory and not used in the proof: Salingaros's finite groups of Clifford algebras
    (J. Math. Phys. 22 (1981), 23 (1982), 25 (1984)); Lounesto, Clifford Algebras and Spinors (2001);
    the Arf invariant (Arf 1941) and its additivity on orthogonal sums; the classification of central
    extensions of an elementary abelian 2-group by a group of order two through quadratic forms
    (as in Quillen, Math. Ann. 194 (1971)); and the Frobenius-Schur indicator reading of (iv), which
    the proof does not need since it defines the Arf invariant by the sign of the Gauss sum.
  maintainer_pass:
    by: maintainer-2026-11-06
    date: '2026-11-06'
    note: 'Version 1 -> 2: a standard-route derivation added, citing the new Fact synthesis.imported-real-clifford-algebras-as-twisted-group-algebras-and-the-arf-invariant (Ovsienko; Elduque and Rodrigo-Escudero), so that the prior art of clauses (ii) to (iv) is pinned as a Fact rather than named in the note; statement, main proof and check unchanged.'
---

## formal
Let $\Cl(p,q)$, $n = p + q \ge 1$, have orthonormal generators $e_{1}, \dots, e_{n}$, with $Q(e_{i}) = +1$ for $i \le p$ and $Q(e_{i}) = -1$ for $i$ in $N = \{p + 1, \dots, n\}$, and for $S \subseteq \{1, \dots, n\}$ let $e_{S}$ be the increasing product of the $e_{i}$, $i \in S$. Identify the subsets with $\mathbb{F}_{2}^{n}$, addition being the symmetric difference $S \triangle T$.
\begin{enumerate}
\item[(i)] \emph{(The sign from symmetry.)} Let $x_{1}, \dots, x_{n}$, $n \ge 2$, be elements of an algebra over a field $k$ with $x_{i}x_{j} = c\,x_{j}x_{i}$ for all $i \ne j$, for one $c \in k$, and $x_{1}x_{2} \ne 0$. Then $c^{2} = 1$. Moreover, if only the single relation $x_{1}x_{2} = c\,x_{2}x_{1}$ is imposed ($c \ne 0$), then $x_{1}^{2}x_{2} = c^{2}x_{2}x_{1}^{2}$, so wherever $x_{2}x_{1}^{2} \ne 0$ the square $x_{1}^{2}$ commutes with $x_{2}$ exactly when $c^{2} = 1$. Over a field of characteristic other than $2$, with $c \ne 1$ this gives $c = -1$: the symmetry of the relation and the centrality of the squares each force $c \in \{1, -1\}$.
\item[(ii)] \emph{(The quadratic form.)} $e_{S}^{2} = (-1)^{q(S)}$ with $q(S) = \binom{|S|}{2} + |S \cap N| \bmod 2$, and $e_{S}e_{T} = \pm e_{S \triangle T}$. The map $q : \mathbb{F}_{2}^{n} \to \mathbb{F}_{2}$ is a quadratic form whose polar form
\[
b(S,T) = q(S \triangle T) + q(S) + q(T) = |S|\,|T| + |S \cap T| \bmod 2
\]
is $1$ exactly when $e_{S}$ and $e_{T}$ anticommute. So the group $\{\pm e_{S}\}$ is a central extension of $\mathbb{F}_{2}^{n}$ by $\{\pm 1\}$ with commutator form $b$ and squaring map $q$.
\item[(iii)] \emph{(The radical.)} The radical of $b$ is $\{\emptyset\}$ for $n$ even and $\{\emptyset, \{1, \dots, n\}\}$ for $n$ odd, and $q(\{1, \dots, n\}) = 1$ exactly when the pseudoscalar squares to $-1$.
\item[(iv)] \emph{(The Gauss sum and the type.)} For any $j$ with $j^{2} = -1$ (a unit bivector of a Euclidean plane, say),
\[
\sum_{S} e_{S}^{2} \;=\; \sum_{S}(-1)^{q(S)} \;=\; \big\langle (1 - j)(1 + j)^{p}(1 - j)^{q} \big\rangle_{0},
\]
and its value is $2^{n/2}$ for $p - q \equiv 0, 2$, $-2^{n/2}$ for $p - q \equiv 4, 6$, $2^{(n+1)/2}$ for $p - q \equiv 1$, $-2^{(n+1)/2}$ for $p - q \equiv 5$ and $0$ for $p - q \equiv 3, 7 \pmod 8$. Define the Arf invariant of a quadratic form $q'$ with nondegenerate polar form on $\mathbb{F}_{2}^{m}$ by $\sum (-1)^{q'} = (-1)^{\mathrm{Arf}(q')}\,2^{m/2}$. For $n$ even, $\mathrm{Arf}(q) = 0$ exactly when $\Cl(p,q)$ is a real matrix algebra ($p - q \equiv 0, 2 \bmod 8$) and $\mathrm{Arf}(q) = 1$ exactly when it is a quaternionic one ($p - q \equiv 4, 6$). For $n$ odd, $q$ is nonzero on the radical exactly in the complex case ($p - q \equiv 3, 7$); otherwise $q$ descends to the quotient by the radical, whose Arf invariant is $0$ for a sum of two real matrix algebras ($p - q \equiv 1$) and $1$ for a sum of two quaternionic ones ($p - q \equiv 5$). So the parity of $n$, the value of $q$ on the radical and the Arf invariant determine the type in the classification.
\item[(v)] \emph{(The ascent.)} Add one hyperbolic plane spanned by $e, f$ with $Q(e) = 1$, $Q(f) = -1$, put $\omega = ef$, and take the twisted generators $x_{i}\omega$ of the commuting-copies isomorphism (Theorem \claimref{tower.commuting-copies}). For $A \subseteq \{1, \dots, n\}$ and $B \subseteq \{e, f\}$ the product of the $x_{i}\omega$, $i \in A$, with the blade $e_{B}$ is $\pm$ a blade of $\Cl(p{+}1, q{+}1)$, and $(A, B) \mapsto$ its index set is a linear bijection $\mathbb{F}_{2}^{n} \oplus \mathbb{F}_{2}^{2} \to \mathbb{F}_{2}^{n+2}$ carrying $q_{(p,q)} \perp q_{(1,1)}$ to $q_{(p+1,q+1)}$. The form $q_{(1,1)}$ has Arf invariant $0$, so the $(1,1)$ ascent leaves the Gauss sum's sign, the Arf invariant and the type unchanged (the division-ring clause of Theorem \claimref{tower.rigidity-clock-frozen}); the anisotropic plane $(0,2)$, whose Clifford algebra is the quaternions, has $q = 1$ on its three nonzero elements and Arf invariant $1$; adding it is not an orthogonal sum with the ground form, since the twist by its volume element, of square $-1$, exchanges $p$ and $q$: $\Cl(p, q{+}2)$ carries $q_{(q,p)} \perp q_{(0,2)}$.
\end{enumerate}

## technical
The signs of the squares of the basis blades of a real Clifford algebra form a quadratic form over the two-element field: index the blades by subsets of the generators, so that multiplying blades adds their index sets by symmetric difference, and record a $1$ when the blade squares to $-1$. The associated bilinear form records exactly which pairs of blades anticommute, so the finite group of signed blades is the central extension that this form describes. The form's own invariants recover the classification. In even dimension the anticommutation form is nondegenerate and the Arf invariant, read off from the sign of the Gauss sum $\sum_{S} e_{S}^{2}$, is $0$ for the real matrix algebras ($p - q \equiv 0, 2 \bmod 8$) and $1$ for the quaternionic ones ($p - q \equiv 4, 6$). In odd dimension the radical is spanned by the pseudoscalar: if it squares to $-1$ the algebra is complex, and otherwise the Arf invariant of the quotient separates two real from two quaternionic matrix algebras. The Gauss sum is the scalar part of $(1 - j)(1 + j)^{p}(1 - j)^{q}$ with $j^{2} = -1$, which gives the whole table at once.

Two small structural facts sit underneath. A single commutation coefficient shared by all pairs of directions must satisfy $c^{2} = 1$, because the relation must read the same with the two directions exchanged; and, with only one relation imposed, the same condition $c^{2} = 1$ is what makes the square of a direction central. Either way $c \in \{1, -1\}$, and $c = -1$ needs the separate input $c \ne 1$. These are classical: the classification by the quadratic form is in Ovsienko and in Elduque and Rodrigo-Escudero, and is restated here. In the language of the series, adding a hyperbolic plane, the $(1,1)$ increment of the transport ascent, adds an orthogonal summand of Arf invariant $0$ once the ground generators are twisted by the plane's volume element, so the type never changes up the tower, while the anisotropic plane $(0,2)$, whose algebra is the quaternions, carries Arf invariant $1$; adding it is not an orthogonal sum with the ground form, since the twist by its volume element, of square $-1$, exchanges $p$ and $q$: $\Cl(p, q{+}2)$ carries $q_{(q,p)} \perp q_{(0,2)}$.

## lay
Every product of basic directions in these algebras squares either to plus one or to minus one. Writing down which ones give minus one produces a simple yes-or-no table, and that table already knows which kind of number system the whole algebra is built on: ordinary real numbers, complex numbers or quaternions. Adding a pair of directions of opposite type, the basic step the series uses to repair division, never changes that answer; adding two directions that both square to minus one is different, because it also swaps the roles of the existing positive and negative directions.

## one-liner
The signs $e_{S}^{2} = (-1)^{q(S)}$ of the blades of $\Cl(p,q)$ form a quadratic form over $\mathbb{F}_{2}$ whose polar form is anticommutation; its Gauss sum $\sum_{S} e_{S}^{2} = \langle (1 - j)(1 + j)^{p}(1 - j)^{q}\rangle_{0}$, the value of $q$ on the radical and its Arf invariant give the real, complex or quaternionic type, and the $(1,1)$ ascent adds a summand of Arf invariant $0$.
