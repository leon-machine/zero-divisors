---
id: synthesis.signed-directions-and-the-integer-clifford-algebra
kind: claim
version: 2
title: The group of signed directions and its integer Clifford algebra
status: proved
region: synthesis
subject: clifford-structure
tags: [clifford-classification, grading-and-parity, pseudoscalar-and-centre, forcing-and-uniqueness, classical-theorem]
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
- obj.std-algebra.clifford-algebra
founded_on:
- synthesis.premise-superposition-over-the-integers@2
lineage:
  motivated_by:
  - synthesis.blade-square-signs-f2-quadratic-form
derivations:
- name: main
  uses: []
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_the_sign_bit_is_forced
- kind: check
  ref: check.py::check_existence_by_the_bilinear_cocycle
- kind: check
  ref: check.py::check_radical_and_gauss_sums_over_the_integers
- kind: check
  ref: check.py::check_normal_form_table_squares_commutators
- kind: check
  ref: check.py::check_centre_and_extraspecial
- kind: check
  ref: check.py::check_integer_algebra_free_and_contraction
- kind: check
  ref: check.py::check_universal_property_and_base_change
- kind: check
  ref: check.py::check_classification_by_gauss_sum
- kind: proof
  derivation: main
locators:
  paper: T00a
  number: Thm 4.1
  label: thm:bitclifford
  line: 209
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.premise-superposition-over-the-integers: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  note: >-
    From Leon's working document "From the Bit to the Numbers" (7 November 2026), Steps 2 and 3,
    re-proved and re-checked here; not an attack on an open problem. The hypotheses (F2) and (F3) of
    the statement are the content of the premises filed alongside as postulates (the bit, minimal
    non-commutativity, superposition over the integers); a proposal cannot cite a proposal, so they
    are stated inside the theorem, which is therefore unconditional, and the assumes edges from this
    result to those postulates are left to the maintainer. Ledger: transport-absent; the content is
    classical group and ring theory, restated in the series' language. Overlap with Theorem
    synthesis.blade-square-signs-f2-quadratic-form, which is not refiled: its clauses (i) to (iv) (the
    sign from symmetry, the quadratic form, its radical, the Gauss-sum values) are re-derived here over
    the integers in a few lines and named as comparisons; it is linked by lineage and not by a uses
    edge, because its past cone runs through the real classification, Sylvester's law, periodicity and
    the Fact below, none of which this integer result needs. New to the store (all classical,
    restated): the existence of a group of signed directions for every sign vector (a bilinear
    2-cocycle), the group-theoretic premise form with the order clause forced for n >= 2 and independent for
    n = 1; the centre (extraspecial for n even), with the central involutions (the reading "c is the
    unique non-trivial central square root of 1" holds exactly when n is even or the pseudoscalar
    squares to c); the classification of the groups by q; the integer algebra Z[G]/(c + 1) free with
    the blade basis, the contraction rule v^2 = Q(v) as a theorem, and the universal property over
    every commutative ring; and the isomorphism classification by the Gauss sum. Relation to the
    former imported Fact synthesis.imported-real-clifford-algebras-as-twisted-group-algebras-and-the-arf-invariant (retired
    on 7 November 2026 in favour of this result and synthesis.blade-square-signs-f2-quadratic-form):
    its clause (a) is derived here (clauses (v) and (vii), over every commutative ring, not only R);
    its clause (b) is derived for the Clifford twisting functions, which is the part the classification
    of real Clifford algebras uses (clause (viii), over every ordered field and over Z), but not for
    general bilinear twisting functions; its clause (c) is clause (iv) of that theorem (the Gauss-sum values are re-derived here, clause (viii); the identification of the signs with the real, complex and quaternionic types is not). The
    maintainer decides what happens to the Fact. Prior art, cited from memory and not used in the
    proofs: the vee groups of Salingaros (J. Math. Phys. 22 (1981), 23 (1982), 25 (1984)); extraspecial
    2-groups and their classification by quadratic forms over F_2 (Gorenstein, Finite Groups;
    Quillen, Math. Ann. 194 (1971)); Arf's classification of quadratic forms over F_2 (Arf 1941); the
    Clifford algebra of a quadratic module over a commutative ring and its universal property
    (Bass, Amer. J. Math. 96 (1974); Knus, Quadratic and Hermitian Forms over Rings (1991));
    Ovsienko arXiv:1601.07664 and Elduque and Rodrigo-Escudero arXiv:1801.07002 (the Fact above).
    Related store item, not refiled: for (p, q) = (1, 1) the integer algebra of clause (v) is the
    orthogonal order of the remark note.one-relation.two-presentations-differ-over-the-integers,
    of index 4 in the integer matrix ring and without idempotents other than 0 and 1, so the bit
    ladder over Z yields that order and not the null-pair order Mat_2(Z).
---

## formal
Let $n \ge 1$. A \emph{group of signed directions} is a group $G$ with elements $e_{1}, \dots, e_{n}$ and $c$ such that
\begin{enumerate}
\item[(F2)] $c$ is central; $G/\langle c\rangle$ is elementary abelian of order $2^{n}$ with basis the images of $e_{1}, \dots, e_{n}$, so that $S \mapsto e_{S}\langle c\rangle$ identifies $\mathbb{F}_{2}^{n}$ (subsets of $\{1, \dots, n\}$ under symmetric difference $S \triangle T$) with $G/\langle c\rangle$, where $e_{S}$ is the increasing product of the $e_{i}$, $i \in S$; distinct directions do not commute, $c \ne 1$ and $e_{i}e_{j} = c\,e_{j}e_{i}$ for $i \ne j$; and $c^{2} = 1$.
\end{enumerate}
Then $e_{i}^{2} \in \langle c\rangle$; write $e_{i}^{2} = c^{s_{i}}$ with $s_{i} \in \{0, 1\}$, $N = \{i : s_{i} = 1\}$, $q = |N|$, $p = n - q$, and $Q(x) = \sum_{i \notin N} x_{i}^{2} - \sum_{i \in N} x_{i}^{2}$. Let
\begin{enumerate}
\item[(F3)] $A = \Z[G]/(c + 1)$, the integral group ring of $G$ modulo the two-sided ideal generated by $c + 1$.
\end{enumerate}
\begin{enumerate}
\item[(i)] \emph{(The sign.)} For $n \ge 2$ the clause $c^{2} = 1$ follows from the others; for $n = 1$ it is independent of them: the cyclic group of order $2m$ generated by $e_{1}$, with $c = e_{1}^{2}$, satisfies the other clauses for every $m \ge 2$ and has $c^{2} = 1$ only for $m = 2$. For every sign vector $(s_{1}, \dots, s_{n})$ a group of signed directions exists: $\{0, 1\} \times \mathbb{F}_{2}^{n}$ with $(a, S)(b, T) = (a + b + f(S,T) \bmod 2,\ S \triangle T)$, $f$ as in (ii), $c = (1, \emptyset)$, $e_{i} = (0, \{i\})$; it is unique up to an isomorphism fixing $c$ and the $e_{i}$. Every element of $G$ is $c^{a}e_{S}$ for exactly one $a \in \{0, 1\}$ and $S$, so $|G| = 2^{n+1}$, and $G$ is presented by the generators $e_{1}, \dots, e_{n}, c$ and the relations: $c$ central, $c^{2} = 1$, $e_{i}^{2} = c^{s_{i}}$, $e_{i}e_{j} = c\,e_{j}e_{i}$ ($i \ne j$).
\item[(ii)] \emph{(Squares and commutators.)} $e_{S}e_{T} = c^{f(S,T)}e_{S \triangle T}$ with $f(S,T) = |\{(i, j) \in S \times T : i > j\}| + |S \cap T \cap N|$. Every square and every commutator of $G$ lies in $\{1, c\}$; for $g \in \{e_{S}, c\,e_{S}\}$ and $h \in \{e_{T}, c\,e_{T}\}$, $g^{2} = c^{q(S)}$ and $gh = c^{b(S,T)}hg$ with
\[
q(S) = \binom{|S|}{2} + |S \cap N|, \qquad b(S,T) = |S|\,|T| + |S \cap T| \pmod 2,
\]
a quadratic form over $\mathbb{F}_{2}$ and its polar form (the same forms as in Theorem \claimref{synthesis.blade-square-signs-f2-quadratic-form}). For $n \ge 2$, $c$ is the only element other than $1$ that is a square or a commutator.
\item[(iii)] \emph{(The centre.)} The radical of $b$ is $\{\emptyset\}$ for $n$ even and $\{\emptyset, \{1, \dots, n\}\}$ for $n$ odd, and the centre of $G$ is $\{1, c\}$ for $n$ even and $\{1, c, e_{1 \cdots n}, c\,e_{1 \cdots n}\}$ for $n$ odd, $e_{1 \cdots n} = e_{1}e_{2}\cdots e_{n}$. So for $n$ even the centre, the commutator subgroup and the subgroup generated by the squares coincide and have order $2$: $G$ is an extraspecial $2$-group of order $2^{1+n}$. The element $c$ is the only central element of order $2$ when $n$ is even or $e_{1 \cdots n}^{2} = c$; when $n$ is odd and $e_{1 \cdots n}^{2} = 1$ (exactly when $p - q \equiv 1 \bmod 4$), $e_{1 \cdots n}$ and $c\,e_{1 \cdots n}$ are central of order $2$ as well.
\item[(iv)] \emph{(The groups are classified by $q$.)} Two groups of signed directions with the same $n$ are isomorphic by an isomorphism carrying $c$ to $c'$ if and only if their forms are equivalent, $q' \circ \phi = q$ for a linear bijection $\phi$ of $\mathbb{F}_{2}^{n}$. For $n \ge 2$ every isomorphism carries $c$ to $c'$.
\item[(v)] \emph{(The integer algebra.)} The ideal $(c + 1)$ is $\bigoplus_{S}\Z\,(1 + c)e_{S}$, and $A$ is a free $\Z$-module with basis the images of the $e_{S}$, written $e_{S}$ again; $c$ maps to $-1$ and $e_{S}e_{T} = (-1)^{f(S,T)}e_{S \triangle T}$, so $A$ has rank $2^{n}$ and integral structure constants.
\item[(vi)] \emph{(The contraction rule as a theorem.)} For $v = \sum_{i} a_{i}e_{i}$ with $a_{i} \in \Z$, $v^{2} = \sum_{i} a_{i}^{2}e_{i}^{2} = Q(v)$.
\item[(vii)] \emph{(The universal property.)} Let $R$ be a commutative ring, $A_{R} = R \otimes_{\Z} A = R[G]/(c + 1)$, free over $R$ with basis the $e_{S}$, and $\iota : R^{n} \to A_{R}$, $x \mapsto \sum_{i} x_{i}e_{i}$. For every associative unital $R$-algebra $B$ and $R$-linear $f : R^{n} \to B$ with $f(x)^{2} = Q(x)\,1$ for all $x$, there is exactly one unital $R$-algebra homomorphism $F : A_{R} \to B$ with $F \circ \iota = f$. So $(A_{R}, \iota)$ is the Clifford algebra $\Cl_{R}(p,q)$ of the quadratic module $(R^{n}, Q)$, isomorphic to the tensor algebra of $R^{n}$ modulo $x \otimes x - Q(x)$, with $\iota$ injective and the blade basis over every $R$; $A = \Cl_{\Z}(p,q)$; and for $R = \R$, $(A_{\R}, \iota)$ is the Clifford algebra $\Cl(p,q)$ of Definition \claimref{obj.std-algebra.clifford-algebra}, the $e_{S}$ its blades. If $2 = 0$ in $R$, $A_{R}$ is the commutative group algebra $R[\mathbb{F}_{2}^{n}]$ of the configurations.
\item[(viii)] \emph{(Isomorphism classes.)} For signatures $(p,q)$ and $(p',q')$ with $p + q = p' + q' = n$ the following are equivalent: (a) $q_{(p,q)}$ and $q_{(p',q')}$ are equivalent over $\mathbb{F}_{2}$; (b) their groups of signed directions are isomorphic by an isomorphism carrying $c$ to $c'$; (c) $\Cl_{R}(p,q) \cong \Cl_{R}(p',q')$ for every commutative ring $R$; (d) $\Cl_{R}(p,q) \cong \Cl_{R}(p',q')$ as $R$-algebras for one commutative ring $R$ that maps unitally to an ordered field ($\Z$, $\Q$ and $\R$ among them); (e) the Gauss sums $\sum_{S}(-1)^{q(S)}$ agree. With $j = e_{1}$ in $\Cl_{\Z}(0,1)$, $\sum_{S}(-1)^{q(S)} = \langle (1 - j)(1 + j)^{p}(1 - j)^{q}\rangle_{0}$, which is $2^{n/2}$, $-2^{n/2}$, $2^{(n+1)/2}$, $-2^{(n+1)/2}$, $0$ for $p - q$ congruent modulo $8$ to $0$ or $2$, $4$ or $6$, $1$, $5$, $3$ or $7$ (the values of Theorem \claimref{synthesis.blade-square-signs-f2-quadratic-form}); so (e) holds exactly when $p - q$ and $p' - q'$ lie in the same one of these classes. The Gauss sum is the signature of the trace form $(x, y) \mapsto 2^{-n}\Tr(L_{xy}) = \langle xy\rangle_{0}$ ($L_{z}$ left multiplication), which is diagonal on the blades with entries $e_{S}^{2}$.
\end{enumerate}

## technical
Take a group generated by $n$ directions and one central bit $c \ne 1$ such that dividing out the bit leaves the configurations $\mathbb{F}_{2}^{n}$, with any two distinct directions commuting up to $c$. Reading the relation for a pair both ways forces $c^{2} = 1$ once there are two directions; with one direction the order of $c$ is a separate choice. The group then has $2^{n+1}$ elements $\pm e_{S}$, every square and commutator is $1$ or $c$, and the squaring map is the quadratic form over $\mathbb{F}_{2}$ already stored for the blades, with polar form the commutator form. For even $n$ the centre is just $\{1, c\}$, which makes the group extraspecial; for odd $n$ the volume element joins the centre, and it is a second central involution when it squares to $1$, so $c$ is singled out as the commutator bit rather than as the only central involution. Groups of this kind are classified by their quadratic forms.

Adding integer superpositions with $c$ acting as $-1$, the ring $\Z[G]/(c + 1)$ is free of rank $2^{n}$ on the blades, and the cross terms of a vector's square cancel because $e_{i}e_{j} + e_{j}e_{i} = (c + 1)e_{j}e_{i}$ maps to $0$: the rule $v^{2} = Q(v)$, usually the defining axiom, is a theorem, and no division by $2$ is needed. The ring has the universal property of the Clifford algebra of the diagonal form $\langle \pm 1, \dots, \pm 1\rangle$ over the integers and, after extending the coefficients, over every commutative ring, so it is $\Cl_{\Z}(p,q)$ and over the reals it is the store's $\Cl(p,q)$; in characteristic $2$ the sign is invisible and the algebra collapses to the commutative group algebra of the configurations. Two signatures of the same dimension give isomorphic algebras, over the integers, the rationals or the reals alike, exactly when their quadratic forms over $\mathbb{F}_{2}$ are equivalent, and that happens exactly when the Gauss sums agree, the Gauss sum being the signature of the algebra's trace form.

## lay
Start with a handful of independent yes-or-no distinctions and allow them to depend on the order in which they are made, by the smallest possible amount: one extra bit that flips when two distinctions are swapped. That bit has to behave like a minus sign, and every combination of distinctions then squares to plus or minus one. Allowing whole-number combinations of these distinctions produces, with no further assumption, the whole-number form of the algebra of directions used throughout the series, which becomes that algebra once the coefficients are extended, with the rule that a direction times itself gives its squared length coming out as a consequence rather than being assumed. Which version of the algebra one gets is decided entirely by a yes-or-no table of the signs.

## one-liner
A group $G$ of $n$ directions extended centrally by one bit $c \ne 1$ with $e_{i}e_{j} = c\,e_{j}e_{i}$ has $c^{2} = 1$ (forced for $n \ge 2$), squares and commutators in $\{1, c\}$ given by the $\mathbb{F}_{2}$ form $q$, centre $\{1, c\}$ for even $n$ (extraspecial); $\Z[G]/(c + 1)$ is free on the blades, satisfies $v^{2} = Q(v)$ and is $\Cl_{\Z}(p,q)$ by its universal property over every commutative ring, and signatures give isomorphic algebras exactly when the Gauss sums of $q$ agree.
