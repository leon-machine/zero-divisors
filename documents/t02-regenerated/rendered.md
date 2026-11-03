# Projective Completes to Conformal (regenerated from the store)

**Abstract.** Projective geometric algebra $\Cl(3,0,1)$ and conformal geometric algebra $\Cl(4,1)$ are the two standard algebras of applied geometric computing, usually presented as independent modelling choices. This note proves that the second is the unique minimal nondegenerate completion of the first. For any real Clifford algebra $\Cl(p,q,r)$ of a degenerate form with nondegenerate part of signature $(p,q)$ and radical of dimension $r$, the minimal nondegenerate Clifford completion exists, has signature exactly $(p{+}r, q{+}r)$, and is unique up to an isometry fixing the original space pointwise: existence by adjoining the dual of the radical with the hyperbolic pairing, minimality because each radical direction must pair nontrivially into any completion, the signature forced by Witt splitting of the complement, and uniqueness by the Witt extension theorem. In particular $\Cl(3,0,1)$ completes minimally and uniquely to $\Cl(4,1)$. The completion converts the radical's nilpotent ideal into the unit ideal. No extension gives a radical element an inverse, since its square stays zero; what CGA supplies is a partner $\varphi$ for each radical direction $\rho$ with $\rho\varphi + \varphi\rho = 2$, so the division PGA lacks becomes total at the level of ideals, through the pairing and not through inverses. The embedding carries PGA's translators to CGA's translators verbatim. Every result is proved in full; the note situates the theorem in the series' transport-rule taxonomy and delimits what minimality promises. All computational identities are verified in exact rational arithmetic in an accompanying script.

## Introduction



**setting  (Introduction).** Two algebras dominate applied geometric algebra. Projective (plane-based) geometric algebra, $\mathrm{PGA} = \Cl(3,0,1)$, models Euclidean rigid motions with a degenerate metric whose null direction $e_0$ encodes the plane at infinity \cite{Gunn2017, Selig2005}. Conformal geometric algebra, $\mathrm{CGA} = \Cl(4,1)$, embeds Euclidean space on a null quadric and adds inversions and dilations to the versor group \cite{HLR2001, DFM2007}. The two are normally introduced as alternative modelling decisions with different trade-offs. This note proves a sharper statement: CGA is the \emph{unique minimal nondegenerate completion} of PGA. The relationship is a theorem, an instance of the general minimal-completion theorem for degenerate Clifford algebras, which this note states and proves in full (Theorem \claimref{conformal.minimal-nondegenerate-completion}), with the PGA case as its principal corollary (Corollary \claimref{conformal.principal-case}).

The theorem belongs to a series. The root paper \cite{ButlerT1} proved the transport principle, that the failure of division at null vectors of $\Cl(p,q)$ is repaired minimally and uniquely by one hyperbolic plane, $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$, and classified all zero-divisor obstructions and their transport rules; the sheaf paper \cite{ButlerT4} handled metrics that degenerate along a locus, where the radical generates a canonical square-zero ideal (the corank-one case), and proved that any nondegenerate completion converts that ideal into the unit ideal. The present note is the degenerate-algebra instance of the same programme: a radical of dimension $r$ requires exactly $r$ hyperbolic planes, and the minimal completion is unique. What is new here is the full rigor: the minimality argument is completed, the signature is forced by a Witt-splitting argument, and uniqueness is proved by the Witt extension theorem, none of which the applied literature states in this generality.

## The minimal completion theorem



**setting  (Setup).** Let $(W, B)$ be a real quadratic space of dimension $m$ with radical $R := \rad(B) = \{\rho : B(\rho, \cdot) = 0\}$ of dimension $r \geq 1$, and nondegenerate induced form of signature $(p,q)$ on $W/R$, so $m = p + q + r$; write $\Cl(p,q,r) := \Cl(W,B)$. The proofs import exactly two results, stated here with their provenance; everything else is proved in this note.



**Fact (imported) 1 (The blade basis persists under degeneracy (external ingredients)).** The results from outside the series on which \claimref{conformal.blade-basis-persists-under-degeneracy} draws, as cited there: C. Chevalley, The Algebraic Theory of Spinors and Clifford Algebras, Collected Works, Vol. 2, Springer, Berlin (1997).

*Provenance:* C. Chevalley, The Algebraic Theory of Spinors and Clifford Algebras, Collected Works, Vol. 2, Springer, Berlin (1997)..



**Theorem 2 (The blade basis persists under degeneracy).** Let $B$ be any symmetric bilinear form on a real space $W$ of dimension $m$, and let $e_1, \dots, e_m$ be any basis of $W$. Then the $2^m$ blades $e_I = e_{i_1} \cdots e_{i_k}$, $I = \{i_1 < \dots < i_k\}$, form a linear basis of $\Cl(W, B)$; in particular $\dim \Cl(W,B) = 2^m$ whether or not $B$ is degenerate. \emph{Provenance:} \cite[Lem.~2.6]{ButlerT4}; classical, \cite{Chevalley1997}.

*Proof.* Let $B$ be any symmetric bilinear form on a real space $W$ of dimension $m$, and let $e_1, \dots, e_m$ be any basis of $W$. Then the $2^m$ blades $e_I = e_{i_1} \cdots e_{i_k}$, $I = \{i_1 < \dots < i_k\}$, form a linear basis of $\Cl(W, B)$; in particular $\dim \Cl(W,B) = 2^m$ whether or not $B$ is degenerate. \emph{Provenance:} \cite[Lem.~2.6]{ButlerT4} (\claimref{sheaf.blade-basis-degenerate-forms-included}); classical, \cite{Chevalley1997} (\claimref{conformal.blade-basis-persists-under-degeneracy-external}).




**Fact (imported) 3 (The Witt extension theorem).** Over a field of characteristic not two, let $(\widetilde W_1, Q_1)$ and $(\widetilde W_2, Q_2)$ be isometric nondegenerate quadratic spaces and let $\sigma : S_1 \to S_2$ be an isometry between subspaces $S_i \subseteq \widetilde W_i$, the $S_i$ arbitrary and possibly degenerate. Then $\sigma$ extends to an isometry $\widetilde W_1 \to \widetilde W_2$. \emph{Provenance:} \cite[Ch.~I, Thm.~4.7]{Lam2005}.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, Graduate Studies in Mathematics 67, American Mathematical Society (2005)., Ch.~I, Thm.~4.7.

**setting  (Setup).** A \emph{completion} of $(W,B)$ is a quadratic space $(\widetilde W, Q)$ with $W \subseteq \widetilde W$ and $Q|_W = B$ and $Q$ nondegenerate; it is \emph{minimal} if no completion has smaller dimension. Every completion induces a unital algebra embedding $\Cl(W,B) \hookrightarrow \Cl(\widetilde W, Q)$: the inclusion of generators satisfies the Clifford relation, so the universal property gives the algebra map, and the map is injective because a basis of $W$ extends to a basis of $\widetilde W$, whereupon Fact \claimref{conformal.blade-basis-persists-under-degeneracy} sends the blades of $\Cl(W,B)$ to blades of $\Cl(\widetilde W, Q)$ in the extended basis, which are linearly independent.



**Theorem 4 (Minimal nondegenerate completion).** Let $(W,B)$ be as in the Setup: radical of dimension $r \geq 1$, nondegenerate part of signature $(p,q)$, $m = \dim W = p + q + r$. Then $(W,B)$ admits a completion, and:
\begin{enumerate}
\item every completion satisfies $\dim \widetilde W \geq m + r$;
\item completions of dimension exactly $m + r$ exist, and every such has signature $(p{+}r,\, q{+}r)$;
\item any two minimal completions are isometric by an isometry fixing $W$ pointwise.
\end{enumerate}
Consequently $\Cl(p,q,r)$ embeds in $\Cl(p{+}r, q{+}r)$, minimally so among the embeddings induced by completions (no completion of dimension below $m + r$ exists), and the minimal ambient algebra is unique up to an isomorphism fixing the image of $\Cl(p,q,r)$.

*Proof.* \emph{(1) The radical pairing.} Let $(\widetilde W, Q)$ be any completion. For $\rho \in R$ the functional $Q(\rho, \cdot)$ vanishes on all of $W$ (it equals $B(\rho, \cdot)$ there), hence descends to a functional on $\widetilde W / W$. This defines a linear map
\[
\lambda : R \longrightarrow (\widetilde W / W)^*, \qquad \lambda(\rho) := Q(\rho, \cdot) \bmod W .
\]
If $\lambda(\rho) = 0$ then $Q(\rho, \cdot)$ vanishes on $W$ and on representatives of $\widetilde W / W$, hence on $\widetilde W$, so $\rho = 0$ by nondegeneracy: $\lambda$ is injective, and $\dim(\widetilde W / W) \geq r$.

\emph{(2) Existence at the bound, and the forced signature.} Take $\widetilde W := W \oplus R^*$ and define $Q$ by: $Q|_W = B$; $Q(\rho, \varphi) = \varphi(\rho)$ for $\rho \in R$, $\varphi \in R^*$; $Q(\varphi, \varphi') = 0$ on $R^*$; and $Q(V_1, R^*) = 0$ for a fixed complement $V_1$ of $R$ in $W$. Nondegeneracy: if $v_1 + \rho + \varphi$ ($v_1 \in V_1$, $\rho \in R$, $\varphi \in R^*$) is $Q$-orthogonal to everything, then pairing against $R^*$ gives $\rho = 0$, against $R$ gives $\varphi = 0$, and against $V_1$ gives $v_1 = 0$ since $B|_{V_1}$ is nondegenerate (it is a complement of the radical). For the signature, choose a basis $\rho_1, \dots, \rho_r$ of $R$ with dual basis $\varphi_1, \dots, \varphi_r$: each $\operatorname{span}\{\rho_i, \varphi_i\}$ is a hyperbolic plane, the planes are mutually orthogonal and orthogonal to $V_1$, so $Q \cong B|_{V_1} \perp H^{\perp r}$ has signature $(p{+}r, q{+}r)$.

Now let $(\widetilde W, Q)$ be \emph{any} completion of dimension $m + r$. Then $V_1^{\perp}$ (orthocomplement in $\widetilde W$) is nondegenerate of dimension $(m{+}r) - (p{+}q) = 2r$, being the orthocomplement of a nondegenerate subspace, and it contains $R$ (radical vectors are $B$-orthogonal to $V_1$), which is totally isotropic of dimension $r$: half the dimension. We claim:
\begin{quote}
\emph{a nondegenerate quadratic space $(X, Q_X)$ of dimension $2s$ containing a totally isotropic subspace $U$ of dimension $s$ is isometric to $H^{\perp s}$.}
\end{quote}
The claim with $s = r$ gives $Q|_{V_1^\perp} \cong H^{\perp r}$ of signature $(r,r)$, and the total is $(p{+}r, q{+}r)$.

Proof of the claim, by induction on $s$, the case $s = 0$ being empty. Pick $u \in U$ nonzero; by nondegeneracy there is $y$ with $Q_X(u, y) = 1$, and $y' := y - \tfrac12 Q_X(y,y)\, u$ is null with $Q_X(u, y') = 1$ still, so $H_1 := \operatorname{span}\{u, y'\}$ is a hyperbolic plane and $X = H_1 \perp X_1$ with $X_1 := H_1^{\perp}$ nondegenerate of dimension $2s - 2$. For $u' \in U$ set $u'' := u' - Q_X(u', y')\, u$: then $u''$ pairs to zero with $u$ (both terms do, $U$ being isotropic) and with $y'$ (the correction cancels), so $u'' \in X_1$. The corrected vectors span a totally isotropic subspace of $X_1$, and the correction map $u' \mapsto u''$ is linear with kernel exactly $\R u$, so that subspace has dimension $s - 1$. Induction finishes the claim.

\emph{(3) Uniqueness.} Let $(\widetilde W_1, Q_1)$ and $(\widetilde W_2, Q_2)$ be minimal completions. By (2) they are isometric abstractly; more precisely, the identity $W \to W$ is an isometry between the subspaces $W \subseteq \widetilde W_1$ and $W \subseteq \widetilde W_2$ of two isometric nondegenerate spaces, and by Fact \claimref{conformal.witt-extension-theorem} it extends to an isometry $\widetilde W_1 \to \widetilde W_2$. Functoriality of $\Cl$ (\claimref{std-algebra.functoriality}) turns this isometry into an algebra isomorphism fixing the embedded copy of $\Cl(p,q,r)$ (an embedding by \claimref{conformal.blade-basis-persists-under-degeneracy}, the blades of a basis of $W$ being among the basis blades of $\widetilde W$).


**Remark  (What minimality promises, and what it does not).** The theorem is a statement about \emph{vector-level} completions: nondegenerate quadratic spaces extending $(W,B)$. It does not assert that $\Cl(p{+}r,q{+}r)$ is minimal among all associative algebras receiving $\Cl(p,q,r)$; that stronger, representation-independent statement is the subject of the sharpenings of \cite[\S4.6]{ButlerT1}, proved there for a nondegenerate base, where the completion adjoins a single hyperbolic plane, by conformal Gram methods. It also does not promise that individual degenerate \emph{elements} acquire inverses in the completion: they cannot, since a square-zero element is invertible in no unital extension \cite[Lem.~2.1]{ButlerT1}. What the completion delivers is stated ideal-theoretically in Proposition \claimref{conformal.nilpotent-ideal-becomes-unit-ideal}.



**Theorem 5 (The nilpotent ideal becomes the unit ideal).** Fix a basis $\rho_1, \dots, \rho_r$ of $R$. In $\Cl(p,q,r)$ the radical generates the two-sided ideal $J = \sum_i \Cl \cdot \rho_i$, with
\[
\dim J = 2^m - 2^{m-r}, \qquad J^{\,r+1} = 0, \qquad J^{\,r} \neq 0 ;
\]
in particular $J^2 = 0$ precisely when $r = 1$, the corank-one case established at sheaf level in \cite[Thm.~3.1]{ButlerT4}. In any completion, the image of the radical generates the \emph{unit} ideal of the ambient Clifford algebra, and each radical basis vector spans a hyperbolic plane with a partner vector of the completion.

*Proof.* \emph{The mechanics of radical letters.} Work in the blade basis (Fact \claimref{conformal.blade-basis-persists-under-degeneracy}) adapted to a decomposition $W = V_1 \oplus R$: each blade is $x_T\, \rho_S$ with $x_T$ a blade in a basis of $V_1$ and $\rho_S := \rho_{s_1} \cdots \rho_{s_j}$, $S = \{s_1 < \dots < s_j\}$. A radical letter $\rho$ satisfies $B(\rho, z) = 0$ for every vector $z$, so $\rho z = -z\rho$ with no scalar term: in any product of blades, radical letters reorder by pure anticommutation and contract with nothing, while a repeated radical letter makes the product zero ($\rho^2 = 0$). Hence
\[
(x_T\, \rho_S)(x_{T'}\, \rho_{S'}) \;=\;
\begin{cases}
0 & \text{if } S \cap S' \neq \emptyset, \\
\pm\, (x_T\, x_{T'})\; \rho_{S \cup S'} & \text{if } S \cap S' = \emptyset ,
\end{cases}
\]
where $x_T\, x_{T'}$ expands over blades of $V_1$ alone: radical letters accumulate and are never contracted away.

\emph{The ideal, and its dimension.} $\mathcal{S} := \operatorname{span}\{x_T \rho_S : S \neq \emptyset\}$ is a two-sided ideal by the display, and it equals $J$: every $x_T \rho_S$ with $s_1 \in S$ lies in $\Cl \cdot \rho_{s_1} \cdot \Cl$, and conversely every product $a \rho_i b$ expands into blades each retaining the letter $\rho_i$. Counting blades with $S \neq \emptyset$ gives $\dim J = 2^m - 2^{m-r}$.

\emph{Nilpotency, and its exact index.} By the display, a product of $j$ elements of $J$ lies in the span of blades carrying at least $j$ radical letters; only $r$ radical letters exist, so $J^{\,r+1} = 0$. In the other direction, $\rho_1 \cdots \rho_r$ is a product of $r$ elements of $J$ and is a basis blade, hence nonzero: $J^{\,r} \neq 0$. For $r \geq 2$ the nonzero blade $\rho_1 \rho_2 \in J^2$ shows the ideal is not square-zero.

\emph{The unit ideal in the completion.} Let $(\widetilde W, Q)$ be any completion and $\rho_i$ a radical basis vector. By nondegeneracy there is $\varphi_i \in \widetilde W$ with $Q(\rho_i, \varphi_i) = 1$, so the Clifford relation (\claimref{std-algebra.vector-squares}) gives $\rho_i \varphi_i + \varphi_i \rho_i = 2$, and $1 = \tfrac12(\rho_i \varphi_i + \varphi_i \rho_i)$ lies in the two-sided ideal generated by $\rho_i$ (both summands carry the factor $\rho_i$). Replacing $\varphi_i$ by $\varphi_i - \tfrac12 Q(\varphi_i, \varphi_i)\, \rho_i$ leaves $Q(\rho_i, \varphi_i) = 1$ (since $Q(\rho_i, \rho_i) = 0$) and makes $\varphi_i$ null, so $\operatorname{span}\{\rho_i, \varphi_i\}$ is a hyperbolic plane. This is the finite-dimensional instance of the resolution mechanism of \cite[Prop.~3.4]{ButlerT4}.


## PGA completes to CGA, exactly





**Theorem 6 (The principal case).** $\mathrm{PGA} = \Cl(3,0,1)$ has minimal nondegenerate completion $\Cl(4,1) = \mathrm{CGA}$, uniquely: the engineering community's two standard algebras are a degenerate algebra and its unique minimal completion. Likewise in the plane, $\Cl(2,0,1)$ completes minimally to $\Cl(3,1)$; and in general the $n$-dimensional Euclidean PGA $\Cl(n,0,1)$ completes minimally to the $n$-dimensional CGA $\Cl(n{+}1,1)$.

*Proof.* Theorem \claimref{conformal.minimal-nondegenerate-completion} with $(p,q,r) = (n,0,1)$.


**Example  (The dictionary, and the translators).** Write $e_0$ for PGA's degenerate generator and $e_1, e_2, e_3$ for the Euclidean ones. The completion adjoins one dual direction; in CGA conventions, take the null pair $\nInf, \nO$ with $\nInf^2 = \nO^2 = 0$ and $\nInf \cdot \nO = -1$, and embed
\[
e_0 \longmapsto \nInf, \qquad e_i \longmapsto e_i .
\]
This is an isometric embedding of the degenerate form ($\nInf$ is null and orthogonal to the $e_i$), hence induces the algebra embedding of Theorem \claimref{conformal.minimal-nondegenerate-completion}; the adjoined partner is $\nO$. Under it, PGA's translator by a vector $t$,
\[
T_t \;=\; 1 + \tfrac12\, e_0\, t \qquad (t = t^i e_i),
\]
maps to $1 + \tfrac12 \nInf t$, which is precisely CGA's translator \cite{DFM2007}. The embedding is an algebra map, so all motor compositions, exponentials of PGA bivectors, and sandwich actions are carried verbatim; what CGA adds (versors built from $\nO$: inversions, dilations, transversions) is exactly the content of the adjoined direction. The plane at infinity of PGA becomes the point at infinity's null direction of CGA, which is the geometric form of the pairing $\lambda$ in the minimality proof: the direction that paired with nothing in PGA is the direction that must pair with something in any completion.

**Remark  (Why PGA cannot be repaired in place).** A frequently asked question in the applied community is whether PGA's non-invertible elements (anything with a factor in the ideal $J$) could be given inverses by a clever convention. Proposition \claimref{conformal.nilpotent-ideal-becomes-unit-ideal} says what is possible and what is not: no extension makes a radical element invertible (its square is zero and stays zero), but the minimal completion makes the ideal it generates the whole algebra, so the obstruction is lifted at the level of ideals: what annihilated in PGA generates $1$ in CGA, through the identity $\rho\varphi + \varphi\rho = 2$ and not through an inverse of $\rho$. The repair is a transport, not an inverse: the same reading this series gives division by zero throughout \cite{ButlerT1}. And the minimality clause fixes the cost: exactly one hyperbolic plane per radical dimension.

**Remark  (Relation to the transport rules).** In the taxonomy of \cite{ButlerT1}, a radical direction is the degenerate limiting case of a type-N obstruction, and its transport rule is the Witt completion; the degenerate one-generator ascent (adjoining a null direction \emph{without} a partner) is exactly what building $\Cl(p,q,r{+}1)$ from $\Cl(p,q,r)$ does, and it leaves the form degenerate, so no such ascent is ever a completion: more nilpotence never repairs nilpotence, which is why the repair must adjoin partners, not more radical. For nondegenerate bases the same phenomenon is exhibited in \cite[Thm.~5.7]{ButlerT1}: there the null adjunction produces a square-zero thickening of the base, not a completion of it. At sheaf level the same structure appears as the degeneration sheaf's fibre over a singular locus \cite[Thm.~3.1]{ButlerT4}. The present note is the finite-dimensional, applied instance of those results.

## Position in the series



**setting  (Position in the series).** This paper is T2 of the series. It relies on two papers of the series. From the root paper T1 \cite{ButlerT1} it takes the element-level lemma that a square-zero element is invertible in no unital extension, the type-N reading of a radical direction and the taxonomy frame of Remark \claimref{note.conformal.relation-transport-rules}, and the representation-independent sharpenings whose scope Remark \claimref{note.conformal.what-minimality-promises-what-it-does} delimits. From the sheaf paper T4 \cite{ButlerT4} it takes the blade-basis lemma for degenerate forms (Fact \claimref{conformal.blade-basis-persists-under-degeneracy}), together with the corank-one square-zero ideal and resolution mechanism of which Proposition \claimref{conformal.nilpotent-ideal-becomes-unit-ideal} is the finite-dimensional, any-corank instance.

No later paper of the series depends on this note's theorems: it is the applied-audience presentation of results whose general versions are proved in T1 \cite{ButlerT1} and T4 \cite{ButlerT4}, and the status table of the capstone T17 \cite{ButlerT17} records it on that basis.

## Machine verification



**setting  (Machine verification).** Every computational identity in this note has been checked by computer, in exact rational arithmetic over the shared library's basis-blade Clifford product, which admits degenerate generators, in the manner of the verifications deposited with \cite{ButlerT1, ButlerT4}. The script \texttt{verify\_T02.py}, deposited with this note alongside the series' shared exact-arithmetic library \texttt{GA.py}, \cite{ButlerVerifyT02}, performs its checks and reports each: the radical ideal of $\Cl(3,0,1)$ (dimension $8$, all $64$ ideal products zero: the corank-one, square-zero case of Proposition \claimref{conformal.nilpotent-ideal-becomes-unit-ideal}); the nilpotency profile at corank two in $\Cl(2,1,2)$ (ideal dimension $24 = 2^5 - 2^3$, a nonzero product in $J^2$, $\dim J^2 = 8$, and $J^3 = 0$, per Proposition \claimref{conformal.nilpotent-ideal-becomes-unit-ideal}); the model completions' Gram matrices (nondegeneracy by exact rank, signatures $(4,1)$ and $(4,3)$ by exact congruence diagonalisation, per Theorem \claimref{conformal.minimal-nondegenerate-completion}(2)); the embedding $e_0 \mapsto \nInf$ (isometry of the degenerate form on all pairs, algebra map on all $16 \times 16$ blade products, injectivity by exact rank); the unit-ideal identity $\nInf \nO' + \nO' \nInf = 1$ for the normalised partner; the translator dictionary (PGA translator composition $T_s T_t = T_{s+t}$ and its verbatim image in $\Cl(4,1)$, including the sandwich action on a sample vector, checked to move the vector, so the check is not vacuous); and the radical-pairing injectivity instance of the minimality argument. No floating point is used anywhere; the script exits nonzero on any failure, and all checks pass.

## Results cited, not shown

**Fact (imported) 7 (Blade basis, degenerate forms included).** Let $B$ be any symmetric bilinear form on $W$, $\dim W = n$, and let $e_1, \dots, e_n$ be \emph{any} basis of $W$ (orthogonality is not assumed and may be unavailable smoothly in families). Then the $2^n$ blades $e_I = e_{i_1} \cdots e_{i_k}$, $I = \{i_1 < \dots < i_k\}$, form a linear basis of $\Cl(W, B)$. Moreover the structure constants of the algebra in this basis are polynomial in the entries $B(e_i, e_j)$.

*Provenance:* Transport Lab claim sheaf.blade-basis-degenerate-forms-included, version 4 (T04 Lem 2.6).

**Fact (imported) 8 (Isometries extend to algebra homomorphisms).** An isometry $f : (V, Q) \to (W, Q')$ extends to a unique unital algebra homomorphism $\Cl(f) : \Cl(V, Q) \to \Cl(W, Q')$ with $\Cl(f)(v) = f(v)$. It is injective when $f$ is, and $\Cl(g \circ f) = \Cl(g) \circ \Cl(f)$. In particular the orthogonal group $\mathrm{O}(V, Q)$ acts on $\Cl(V, Q)$ by automorphisms, and the inclusion of a subspace $U \subseteq V$ gives an embedding $\Cl(U, Q|_U) \hookrightarrow \Cl(V, Q)$.

*Provenance:* Transport Lab claim std-algebra.functoriality, version 1.

**Fact (imported) 9 (The product of two vectors).** In $\Cl(V, Q)$, for all $u, v \in V$,
\begin{equation}
v^{2} = Q(v), \qquad u v + v u = 2 B(u, v).
\end{equation}
In particular $u v = B(u, v) + \tfrac12(u v - v u)$, the sum of a scalar and an antisymmetric part.

*Provenance:* Transport Lab claim std-algebra.vector-squares, version 1.


