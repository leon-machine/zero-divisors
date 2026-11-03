# Falling In: from the singularity to the Hawking temperature

**Abstract.** Each floor $\Cl(p{+}k, q{+}k)$ of the tower is canonically $\Mat_{2^k}(\Cl(p,q))$. Every floor shares the ground floor's charge, centre and obstruction taxonomy, so the physical tower is frozen at clock position $6$. Vectors realise at most $\min(p,q)$ fermionic mode pairs, the Witt index, which rises by exactly one at each rung. As $r \to 0$ the rescaled gauge map and metric converge to rank-one limits. The gauge-invariant curvature scalar $R_{abcd}R^{abcd} = 48M^2/r^6$ diverges at $r = 0$, so no gauge choice removes the degeneration. The obstruction is of type N only, since $\Cl(1,3) \cong \Mat_2(\HH)$ is central simple and type P imposes no transport. On the interior region the vacuum field equations hold exactly when the scale tractor of the physical metric is parallel. The entropy cost of any pinching is exactly a relative entropy, $\rel{\rho}{E(\rho)} \geq 0$. The descent is the parity average onto the even subalgebra. For a faithful single-mode state the partner is the commutant, so purity is an output. The curvature selects the boost plane, with rate $\kappa = 1/4M$ at the horizon. Under (P) and (R) each marginal is the Gibbs state at the Hawking temperature $T = 1/8\pi M$. The algebra alone does not fix that value. At the Hawking temperature the Fermi-Dirac quasi-free state is the only quasi-free state KMS for the boost dynamics. Under the linear s-wave weight assignment its current modes carry exactly the Bose-Einstein occupancy on the bilateral ladder, with an exponentially small finite-window correction.

This document follows one chain, from the algebra that repairs a failure of division, through the centre of a black hole, to the temperature and the radiation. After the premises, it opens with a single piece of general algebra and then builds the tower, because the results at the singularity draw on what the tower preserves and what it adds. The singularity section locates and classifies the degeneration, and a short section then recasts the vacuum equations in covariant form. The material is grouped by subject, so the cost of discarding information is measured before the descent that discards it is built, and the pair that carries each mode is examined on its own before the descent, parity and states are taken up together. The last section brings in the horizon, fixes the temperature, and assembles the Hawking state and its bosonic reading. Results used but not proved here are cited at the end with their provenance, followed by the prediction the framework registers.

## What we assume

**Postulate 1 ((P): univalence).** Physical states of the boundary modes are even: $\omega \circ \alpha = \omega$, equivalently $\omega$ annihilates the odd sector $\Aod$.

**Postulate 2 ((Q): joint quasi-freeness, with the s-wave weights at the half-integer offset).** In the stationary idealisation of the boundary modes, and for this step alone, the joint state of the mode array is taken to be the gauge-invariant quasi-free state with the marginal data that (P) and (R) (Premise \claimref{singularity.r-regularity-fixed-locus}) fix unconditionally (Theorem \claimref{singularity.rate-discharge-hypothesis-iii}, Corollary \claimref{singularity.chains-state-class-stability}): writing $\psi_k$ for the fermion modes of the array of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector}, its two-point function is $\langle \psi^\dagger_k \psi_l \rangle = \delta_{kl}\,n_k$, and every higher correlation function factorises by Wick's theorem, so that all connected correlators vanish and the joint state is KMS at $\beta = 2\pi/\kappa$ for the joint modular flow. The mode weights are evenly spaced with the array's sea level midway between two sites,
\[
\omega_k = \kappa\bigl(k + \tfrac12\bigr), \qquad k \in \Z ,
\]
so that no mode has zero weight, the weights are symmetric under the particle-hole relabelling $k \mapsto -1-k$, and the Killing flow at one modular period $2\pi/\kappa$ is the parity automorphism $\psi \mapsto -\psi$.

\emph{Why this offset.} The weights $\omega_k$ of Definition \claimref{obj.singularity.geometric-modular-condition-g} are fixed nowhere else in the framework: given (P), (R) and the quasi-free clause, an affine law $\omega_k = ck + d$ is what the currents' being normal modes of the boost flow requires, particle-hole symmetry leaves exactly two offset classes, $d = 0$ and $d = c/2$, and the slope is the value $\beta c = 2\pi$ (Theorem \claimref{synthesis.q-splits-maximum-entropy-affine-weights}(ii), (iv)). The class $d = c/2$ is adopted as a consequence of one reading, not as a bare premise: the array's modes are read as the discretised modes of the field theory's spinor fields on the horizon's light rays, $\psi(u) \mapsto e^{\kappa t/2}\psi(e^{\kappa t}u)$, of boost weight $\tfrac12$ (the weight at which the boost preserves the anticommutator), in the state that Premise \claimref{synthesis.n-plus-null-ground-state} (N$_{+}$) selects, a ground state for the affine null translations of the generators (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}). A field of boost weight $\tfrac12$ changes sign under a full turn of the regular Euclidean section, and $\kappa(k + \tfrac12)$ is the offset at which the array's Killing flow at one modular period carries that sign (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}). The reading is a decision, not a derivation: the Euclidean-period sign $R_{2\pi} = -1$ (Proposition \claimref{state-selection.where-fermi-dirac-comes}) holds in a KMS state of the array at either offset, so identifying the array's real-time recurrence at one period with it is part of the reading.

\emph{On the continuum.} The joint KMS part of this premise is not a separate assumption on the continuum mode space of a horizon's generators: there it follows from (N$_{+}$), whose null ground state restricts on either side of the edge to the continuum I-state at $\beta = 2\pi/\kappa$, jointly KMS and even (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(ii), (iii)). The stationary array statement here is its point-spectrum discretisation, on which (N$_{+}$) itself cannot be posed (part (iv) there). The quasi-free clause is a hypothesis of (N$_{+}$) as well, and (N$_{+}$) does not give the weight clause.

\emph{Consequences of the offset.} At these weights one array carries exactly $\tfrac12\ln 2$ at the Hawking temperature, given the classical theta-function identities, so under the entropy-matching hypothesis two arrays carry the capacity $\ln 2$ of one registered boundary mode with no zero-weight mode (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}(i), (iii)); the current sector of one array is one oscillator tower, one helicity channel, at either offset (Theorem \claimref{synthesis.array-ln2-is-zero-mode-doublet-one-tower}(ii), (iv)), so one registered mode then corresponds to two arrays and two helicity channels. Since every mode has nonzero weight, the gluing equation of Theorem \claimref{singularity.rate-discharge-hypothesis-iii} fixes $\beta$ at every mode of the array, and the zero-weight scopes of Theorems \claimref{singularity.descended-form-state-independent}, \claimref{singularity.universality-temperature-under-g} and \claimref{singularity.rate-discharge-hypothesis-iii} do not arise on it.

\emph{Version 2.} The source states the weight clause as $\omega_k = \kappa k$ with the sea level at $k = 0$, one mode of zero weight at which the gluing equation fixes $n_0 = \tfrac12$ but not $\beta$. Results computed under that offset refer to version 2.

**Postulate 3 ((R): regularity at the fixed locus).** For every mode $k$ and every pair $a, b$ of elements of its ladder $\{v_k, v_k^{*}\}$, the correlation function $F_{a,b}(t) := \omega\bigl(a\,\alpha_t(b)\bigr)$ of the Killing flow $\alpha_t = \operatorname{Ad}(e^{it\omega_k K_k})$, an entire function of $t$, continues in imaginary Killing time to a single-valued function on the regular Euclidean section of the Schwarzschild gravitational field on flat spacetime (Proposition \claimref{singularity.euclidean-section-period}; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}): its two orderings are the two sides of the cut, and they meet after one period,
\[
F_{a,b}\bigl(t + i\,p\bigr) \;=\; \omega\bigl(\alpha_t(b)\,a\bigr), \qquad p = \frac{2\pi}{\kappa} .
\]
In words: each single-mode marginal is KMS for the Killing flow at exactly the period the Euclidean section's smoothness at its tip dictates. The regularity is local, posed at the tip of the Euclidean section (a polar chart about the tip of the Wick-rotated flat background); for a state that is KMS for the Killing flow, this is also the period at which it is regular across the horizon locus in the Painlev\'e-Gullstrand chart.

\emph{Note (continuum restatement).} Posed on the continuum of the horizon's null generators (Definition \claimref{obj.hawking.continuum-mode-space}), the content of (R) for the eternal (Kruskal) hole follows from Premise \claimref{synthesis.n-plus-null-ground-state}: by Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(iii) the generators' modes are then jointly KMS for the Killing flow at $\beta = 8\pi M$. The wording above, on the ladders $\{v_{k}, v_{k}^{*}\}$ with a phase-acting flow, is a discretisation of that statement, recovered only for modes of vanishing Mellin width; (N$_{+}$) itself cannot be posed on point spectrum. A hole formed by collapse is not covered by (N$_{+}$), and (R) remains a premise. (The whole generator of the eternal horizon, which that case of (N$_{+}$) uses, lies beyond one flat chart; see that premise.)

## Clifford algebra structure

We begin with one piece of general algebra, which says what survives when an algebra is replaced by square matrices over it.

We state it for an arbitrary unital real algebra, since every floor of the tower will turn out to have this form.

**Theorem 4 (Matrix amplification: structural properties).** Let $A$ be a unital real algebra and $m \geq 1$. Then: (i) $Z(\Mat_m(A)) = Z(A)\cdot 1_m$; (ii) if $A$ is simple, so is $\Mat_m(A)$; (iii) $\Mat_m(\Mat_r(D)) \cong \Mat_{mr}(D)$ for any unital $D$; (iv) $\Mat_m(A_1 \oplus A_2) \cong \Mat_m(A_1) \oplus \Mat_m(A_2)$.

*Proof.* Parts (i) and (ii) are \claimref{std-algebra.morita-amplification}(i) and (ii); the computation runs as follows. (i) Let $z = (z_{ij})$ be central. The entries of $z E_{kl} = E_{kl} z$ are $(z E_{kl})_{ij} = z_{ik}\,\delta_{lj}$ and $(E_{kl} z)_{ij} = \delta_{ik}\, z_{lj}$; equality for all $i, j, k, l$ forces $z_{ik} = 0$ for $i \neq k$ and $z_{kk} = z_{ll}$, so $z = a \cdot 1_m$ with $a := z_{11}$, and commuting with $b \cdot 1_m$ for all $b \in A$ forces $a \in Z(A)$. The converse inclusion is clear. (ii) A nonzero two-sided ideal $I$ contains some $x$ with an entry $x_{kl} = a \neq 0$; then $E_{ik}\, x\, E_{lj} = a E_{ij} \in I$ for all $i, j$, so $I \supseteq \Mat_m(AaA) = \Mat_m(A)$, since $AaA = A$ by simplicity. (iii) and (iv) are regroupings of indices and entrywise splittings.


## Quantum capacity of the completion

This section builds the algebra of the completion one hyperbolic plane at a time and records what each step preserves and what it adds.

We start the tower with how one floor sits inside the next.

**Theorem 5 (The grade twist, and when it is inner).** Under the isomorphism of Theorem \claimref{tower.commuting-copies}, the tower embedding $\iota_k$ becomes the twisted diagonal $a \mapsto \operatorname{diag}(a, \hat a)$ of \cite[Thm.~7.1]{ButlerT1} (in the corner identification of Fact \claimref{transport.rule-1-morita-trivial}; in the twisted coordinates with $E_{11} = vw$ it reads $\operatorname{diag}(\hat a, a)$). If $p - q$ is even, $\Cl(p,q)$ is central simple over $\R$, the grade involution is an $\R$-algebra automorphism fixing the centre, and it is inner, implemented by the ground volume element $u$ (which anticommutes with vectors precisely when $n$ is even): $\hat a = u a u^{-1}$. Consequently $\operatorname{diag}(a, \hat a) = U \operatorname{diag}(a, a)\, U^{-1}$ with $U = \operatorname{diag}(1, u)$: the twist conjugates away at the level of the single step. (How the correction transports through the identifications of Theorem \claimref{tower.commuting-copies}, which is what the limit theorem needs, is Lemma \claimref{tower.compatibility-connecting-maps-transported}; the stagewise corrector is \emph{not} simply this $U$.) If $p - q$ is odd the grade involution acts nontrivially on the centre ($\R \oplus \R$ or $\C$) and is outer; no inner correction exists.

*Proof.* The matrix form of $\iota_k$ is Fact \claimref{transport.rule-1-morita-trivial} applied with base $T_k$: the new plane's ladder pair supplies the matrix units, and the base embeds as $a \mapsto \operatorname{diag}(a, \hat a)$, the grade involution taken in $T_k$. Note the parity is stable: $\dim$ of floor $k$ is $n + 2k$, of the same parity as $n$, so ``even charge'' is a property of the whole tower.

Even charge: $n$ even makes $\Cl(p,q)$ (and every floor) central simple over $\R$ (its centre is $\R$, \claimref{primer.centre}) \cite{Porteous1995, Lounesto2001}. The grade involution is an $\R$-algebra automorphism fixing the centre $\R$ pointwise, so its innerness is an instance of the Skolem-Noether theorem \cite{Pierce1982}; nothing need be imported, because the implementing element is exhibited directly: the volume element $u = x_1 \cdots x_n$ of an orthogonal generator frame satisfies $u x = (-1)^{n-1} x u = -xu$ for each generator $x$ (\claimref{std-algebra.pseudoscalar-commutation}) (move $x$ through $n$ letters, one coincidence), and $u^2 = \pm 1$ is invertible; so $\Ad_u(x) = u x u^{-1} = -x = \hat x$ on generators, and two automorphisms agreeing on generators agree. The displayed conjugation is then the block computation $U \operatorname{diag}(a,a)\, U^{-1} = \operatorname{diag}(a, u a u^{-1})$ with $U = \operatorname{diag}(1, u)$, invertible in $\Mat_2(T_k)$.

Odd charge: the centre of each floor is $\R \oplus \R$ ($d \equiv 1 \bmod 4$) or $\C$ ($d \equiv 3 \bmod 4$), generated by $1$ and the volume element $\omega$, which is odd (its length $n + 2k$ is odd) and is therefore sent by the grade involution to $-\omega$: the involution exchanges the two central idempotents $\tfrac12(1 \pm \omega)$, respectively conjugates the central complex structure. An inner automorphism fixes the centre pointwise; the grade involution does not, so it is outer, and no unitary correction of the diagonal exists.


Volume elements already appear in that twist, and the next result collects the identities they obey.

**Theorem 6 (Volume elements of the planes).** Let $\omega_j = e_j f_j$. Then $\omega_j^2 = 1$; $\omega_j$ anticommutes with $e_j$ and $f_j$; $\omega_j$ commutes with $e_i, f_i$ for $i \neq j$ and with every ground generator; and the $\omega_j$ commute pairwise. Hence $\Omega_k := \omega_1 \cdots \omega_k$ satisfies $\Omega_k^2 = 1$, commutes with all ground generators, and anticommutes with each $e_j, f_j$, $j \leq k$.

*Proof.* $\omega_j^2 = e_j f_j e_j f_j = -e_j^2 f_j^2 = -(1)(-1) = 1$, using $f_j e_j = -e_j f_j$ (\claimref{std-algebra.orthogonal-anticommute}). $\omega_j e_j = e_j f_j e_j = -e_j^2 f_j = -f_j$ while $e_j \omega_j = e_j e_j f_j = f_j$: they anticommute, and likewise for $f_j$. A ground generator or a generator of another plane anticommutes with both letters of $\omega_j$, hence commutes with their product. Pairwise commutation of the $\omega_j$ is the same parity count. The $\Omega_k$ statements follow: against $e_j$, exactly one factor ($\omega_j$) anticommutes.


We use those identities to view each floor as a product of two commuting pieces.

**Theorem 7 (Commuting copies).** Inside $T_k$, let $B_k$ be the subalgebra generated by the $2k$ plane generators $e_1, f_1, \dots, e_k, f_k$, and let $A_k$ be the subalgebra generated by the twisted base generators $x^{(k)} := x\,\omega_1 \omega_2 \cdots \omega_k$ for $x$ among the ground generators. Then: $B_k \cong \Cl(k,k) \cong \Mat_{2^k}(\R)$; $A_k \cong \Cl(p,q)$ via $x \mapsto x^{(k)}$ (the twisted generators satisfy the ground Clifford relations); $A_k$ and $B_k$ commute elementwise; and multiplication $A_k \otimes B_k \to T_k$ is an isomorphism of algebras,
\[
\Cl(p{+}k, q{+}k) \;\cong\; \Cl(p,q) \otimes \Mat_{2^k}(\R) \;=\; \Mat_{2^k}(\Cl(p,q)).
\]
The isomorphism is canonical given the ordered planes, and compatible with the tower embeddings up to the twist tracked in the section ``The CAR limit''.

*Proof.* \emph{$B_k \cong \Cl(k,k)$.} The $2k$ generators are orthonormal for the split form ($e_j^2 = 1$, $f_j^2 = -1$, pairwise orthogonal), so the universal property (\claimref{std-algebra.existence-uniqueness}) gives a surjection $\Cl(k,k) \to B_k$; it is injective because the $2^{2k}$ blades in the letters $e_1, f_1, \dots, e_k, f_k$ are part of the blade basis of $T_k$ (\claimref{std-algebra.blade-basis}), hence independent. \emph{$\Cl(k,k) \cong \Mat_{2^k}(\R)$} by induction using the series' own results: $\Cl(0,0) = \R$, and $\Cl(j{+}1,j{+}1) \cong \Mat_2(\Cl(j,j))$ is Fact \claimref{transport.rule-1-morita-trivial} with base $\Cl(j,j)$, the $(j{+}1)$-st plane carrying the outer index, so $\Cl(k,k) \cong \Mat_2(\Mat_2(\cdots)) = \Mat_{2^k}(\R)$.

\emph{$A_k \cong \Cl(p,q)$.} By Lemma \claimref{tower.volume-elements-planes}, $\Omega_k$ commutes with ground generators and $\Omega_k^2 = 1$, so for ground generators $x, y$:
\[
x^{(k)} y^{(k)} + y^{(k)} x^{(k)} = x \Omega_k y \Omega_k + y \Omega_k x \Omega_k = (xy + yx)\,\Omega_k^2 = 2B(x,y) .
\]
The universal property gives an algebra map $\Cl(p,q) \to A_k$, $x \mapsto x^{(k)}$; it sends the base blade $x_I$ to $x_I\,\Omega_k^{|I| \bmod 2}$, and these images are distinct nonzero blades (times a fixed invertible even element), hence independent: the map is an isomorphism onto $A_k$.

\emph{Commutation.} For a ground generator $x$ and any plane generator $g \in \{e_j, f_j\}$: $x$ anticommutes with $g$, and $\Omega_k$ anticommutes with $g$ (Lemma \claimref{tower.volume-elements-planes}), so $x^{(k)} g = x \Omega_k g = -x g \Omega_k = g x \Omega_k = g x^{(k)}$. Generators commute, hence the subalgebras do.

\emph{Multiplication is an isomorphism.} Commutation makes $A_k \otimes B_k \to T_k$ an algebra map. It is surjective: its image contains every plane generator, contains $\Omega_k \in B_k$, and therefore contains each ground generator $x = x^{(k)} \Omega_k$. Source and target both have dimension $2^n \cdot 2^{2k} = 2^{n + 2k}$, so a surjective linear map is an isomorphism. Finally $\Cl(p,q) \otimes \Mat_{2^k}(\R) = \Mat_{2^k}(\Cl(p,q))$. Canonicity: the construction used only the ordered orthogonal planes and their volume elements, no basis choices in the ground algebra. The compatibility with $\iota_k$ is Lemma \claimref{tower.grade-twist-when-it-inner} below: under these identifications $\iota_k$ is the twisted diagonal, the twist being conjugation by $\Omega$-data that the section ``The CAR limit'' tracks.


Since each floor is then a matrix algebra over the ground floor, the general facts about matrices tell us what stays fixed as the tower climbs.

**Theorem 8 (Rigidity; the clock is frozen).** Along the tower: the transport charge $d = p - q \bmod 8$ is constant; the division-ring type, simplicity class, and centre of every floor equal those of the ground floor; every floor is Morita equivalent to the ground floor; and the obstruction taxonomy of \cite{ButlerT1} is floor-independent: in particular a type-C obstruction (a central idempotent) never arises by transport from a simple ground algebra, at any height. The physical tower is $\Cl(1{+}k, 3{+}k) \cong \Mat_{2^{k+1}}(\HH)$, frozen at clock position $6$. Bott periodicity manifests as immediate freeze, not eventual return.

*Proof.* The charge is $(p{+}k) - (q{+}k) = p - q$, constant. All structural claims then follow from Theorem \claimref{tower.commuting-copies} and Lemma \claimref{tower.matrix-amplification-structural-properties}: centres agree by (i); if $A \cong \Mat_r(D)$ then $\Mat_{2^k}(A) \cong \Mat_{2^k r}(D)$ by (iii), the same division ring; simplicity propagates by (ii), and the block structure of a semisimple ground floor by (iv); and every floor is Morita equivalent to the ground floor by Fact \claimref{tower.morita-equivalence-algebra-amplification}. The taxonomy statement: by Fact \claimref{transport.existence-classification-type-c}, type C occurs exactly when the centre is $\R \oplus \R$; the centre is floor-independent by Lemma \claimref{tower.matrix-amplification-structural-properties}(i), so a simple ground floor (centre $\R$ or $\C$) propagates: no floor of its tower ever hosts a type-C obstruction. For the physical case, $\Cl(1,3) \cong \Mat_2(\HH)$ \cite{Porteous1995} (\claimref{std-algebra.sta-matrix}), so floor $k$ is $\Mat_{2^k}(\Mat_2(\HH)) = \Mat_{2^{k+1}}(\HH)$, and $1 - 3 \equiv 6 \pmod 8$.


Having seen what stays fixed, we turn to what each new floor adds.

**Theorem 9 (The ladder pairs satisfy the CAR, as vectors).** In $T_k$, the adjoined null pairs satisfy, exactly and at the level of vectors,
\[
v_i v_j + v_j v_i = 0, \qquad w_i w_j + w_j w_i = 0, \qquad v_i w_j + w_j v_i = \delta_{ij}\,,
\]
for all $1 \leq i, j \leq k$: a system of $k$ fermionic modes, with no normal-ordering, no completion, and no representation chosen. Adding a rung adds one mode and touches none of the existing relations.

*Proof.* Every displayed relation is an instance of the single Clifford relation $\alpha\beta + \beta\alpha = 2\langle\alpha, \beta\rangle$ on vectors (\claimref{std-algebra.vector-squares}), as for any Witt basis (\claimref{std-algebra.witt-basis-car}): the $v$'s are pairwise orthogonal null vectors ($\langle v_i, v_j \rangle = 0$ for $i \neq j$ since the planes are orthogonal, and $v_i^2 = 0$ since $v_i$ is null), likewise the $w$'s, and $\langle v_i, w_j \rangle = \tfrac12\delta_{ij}$ by the hyperbolic normalisation within each plane and orthogonality across planes. A new rung's vectors are orthogonal to all previous generators, so the old relations are untouched.


It is then natural to ask whether vectors can carry any more modes than these.

**Theorem 10 (Witt index is quantum capacity).** For any nondegenerate real quadratic space $(V, Q)$, the maximal number of pairwise-anticommuting fermionic mode pairs realisable by \emph{vectors} of $\Cl(V, Q)$ (families $(a_i, b_i)$ of vectors satisfying the displayed CAR of Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}) is exactly the Witt index $\min(p,q)$ of $Q$. Along the tower the Witt index is $\min(p,q) + k$: each rung raises the algebra's mode capacity by exactly one, and by no more.

*Proof.* \emph{Upper bound.} Let $(a_i, b_i)_{i \leq m}$ be vectors satisfying the CAR. Reading the relations through the Clifford relation on vectors (\claimref{std-algebra.vector-squares}): $\langle a_i, a_j \rangle = 0$ for all $i, j$ (including $i = j$), and $\langle a_i, b_j \rangle = \tfrac12 \delta_{ij}$. The span of the $a_i$ is therefore totally isotropic, and the $a_i$ are independent: a vanishing combination $\sum c_i a_i = 0$ pairs against $b_j$ to give $c_j/2 = 0$. So $m \leq$ the maximal totally isotropic dimension, which for a nondegenerate real form of signature $(p,q)$ is $\min(p,q)$: diagonalise, $V = P \perp N$ with $P$ positive definite of dimension $p$ and $N$ negative definite of dimension $q$; a totally isotropic $U$ meets $P$ trivially (a nonzero $v \in U \cap P$ would have $Q(v,v) > 0$ and $Q(v,v) = 0$ at once), so the projection $U \to N$ along $P$ is injective and $\dim U \leq q$; symmetrically $\dim U \leq p$; and $\min(p,q)$ is attained by the null spans of $\min(p,q)$ hyperbolic pairs (the classical bound, cf.\ \cite[Ch.~I]{Lam2005}).

\emph{Attainment.} Split off $\min(p,q)$ orthogonal hyperbolic planes from $(V, Q)$ (Witt decomposition, \claimref{std-algebra.witt-decomposition}) and take their normalised null pairs, as in Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}. Along the tower, the form of signature $(p{+}k, q{+}k)$ has Witt index $\min(p,q) + k$, and each rung contributes its own plane to the attaining family.


## The singularity: where division fails

With the completion in hand, we go to the centre of the black hole, locate the failure of division exactly, and classify the obstruction it presents.

We now leave the algebra and go to the centre of the black hole, where the classical field degenerates.

**Theorem 11 (The degeneration, exactly).** As $r \to 0$, exactly and with every identity holding at finite $\beta$:
\begin{enumerate}
\item (The map.) $\beta^{-1}\hb = \beta^{-1}\,\mathrm{id} - P$, so $\beta^{-1}\hb \to -P$: a rank-one map with image $\R\,\er$ and kernel $\et^{\perp} = \operatorname{span}(\er, e_\vartheta, e_\varphi)$.
\item (The metric.) $\beta^{-2} g(a,b) = -(a\cdot\et)(b\cdot\et) + \beta^{-1}\bigl[(a\cdot\et)(b\cdot\er) + (b\cdot\et)(a\cdot\er)\bigr] + \beta^{-2}(a \cdot b)$, so $\beta^{-2}g \to \hat g$ with
\[
\hat g(a,b) \;=\; -(a\cdot\et)(b\cdot\et) :
\]
a form of rank one and signature $(0,1,3)$, whose radical is $\et^{\perp}$, the kernel of the limit map.
\item (The null direction, located.) The folded direction $\er$ of Proposition \claimref{singularity.cones-fold} lies in the radical of $\hat g$ and is $\hat g$-null, while $g(\er,\er) = -1$ at every finite radius: the nullity of the degenerate direction is a property of the limit form, not of the flat background, and this is the exact content of the phrase ``degeneration through a null kernel direction''. It is the datum Step 2 uses.
\end{enumerate}

*Proof.* (1) and (2) are the displayed algebraic identities, which hold at every finite $\beta$ (expand $g(a,b) \;=\; \hb^{-1}(a) \cdot \hb^{-1}(b)$ with $\hb^{-1} = 1 + \beta P$ and divide); the limits are then immediate, and the rank, kernel, image and signature statements are finite linear algebra, checked exactly in the script (the signature by exact congruence diagonalisation). (3) $\hat g(\er, \er) = 0$ since $\er \cdot \et = 0$, and $\er$ lies in the radical computed in (2); $g(\er,\er) = \er^2 = -1$.


To see where the divergence sits, we compute the connection explicitly.

**Theorem 12 (The connection bivector, computed).** For the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$ of Fact \claimref{sheaf.gauge-field-cometric} on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), whose physical-vector map in components is the coframe $\theta^0 = dt, \qquad \theta^1 = dr + \beta\,dt, \qquad \theta^2 = r\,d\vartheta, \qquad \theta^3 = r\sin\vartheta\,d\varphi$, $\theta^a(v) = \gamma^a \cdot \hb^{-1}(v)$, write $\sigma_r$ for the unit radial boost bivector of that coframe (the sign convention is fixed once, in Remark \claimref{note.singularity.frame-made-explicit}; the verification script fixes it by computation). Then:
\begin{enumerate}
\item all connection data is algebraic in $(r, \beta)$: $\beta' = -\beta/2r$ and $\beta\beta' = -M/r^2$ exactly, so every coefficient below lies in the field $\mathbb{Q}(r)[\beta]$ with $\beta^2 = 2M/r$;
\item the torsion condition of $\mathcal{R}(a) - \tfrac12\, a\, \mathcal{R} \;=\; 8\pi\, T(a), \qquad D \wedge \hb(a) \;=\; \hb(\nabla \wedge a)$ is solved by the rotation-gauge field $\Omega$ whose components in this coframe are the connection one-forms
\[
\omega^1{}_0 = -\beta'\,\theta^1, \qquad
\omega^2{}_0 = -\tfrac{\beta}{r}\,\theta^2, \qquad
\omega^3{}_0 = -\tfrac{\beta}{r}\,\theta^3, \qquad
\omega^2{}_1 = \tfrac{1}{r}\,\theta^2, \qquad
\omega^3{}_1 = \tfrac{1}{r}\,\theta^3, \qquad
\omega^3{}_2 = \tfrac{\cot\vartheta}{r}\,\theta^3,
\]
verified by substitution in the first structure equations: $d\theta^0 = 0$ and $-\omega^0{}_1 \wedge \theta^1 = \beta'\,\theta^1 \wedge \theta^1 = 0$; $d\theta^1 = \beta'\,dr\wedge dt = \beta'\,\theta^1\wedge\theta^0 = -\,\omega^1{}_0\wedge\theta^0$; and $d\theta^2 = \tfrac1r\,dr\wedge\theta^2 = \tfrac1r(\theta^1 - \beta\theta^0)\wedge\theta^2 = -\,\omega^2{}_0\wedge\theta^0 - \omega^2{}_1\wedge\theta^1$, with the $\theta^3$ leg the round sphere's standard connection;
\item evaluated on the background directions $\partial_t$, $\partial_r$ of the $(t,r)$ plane, the connection bivector is
\[
\Omega(\partial_t) \;=\; -\beta\beta'\,\sigma_r \;=\; \frac{M}{r^2}\,\sigma_r ,
\qquad
\Omega(\partial_r) \;=\; -\beta'\,\sigma_r \;=\; \frac{\beta}{2r}\,\sigma_r \;=\; \sqrt{\frac{M}{2r^3}}\;\sigma_r :
\]
the time-direction connection is the Newtonian field $M/r^2$, exactly and at every radius, and the radial-direction connection diverges as $r \to 0$ at the rate $r^{-3/2}$, the square root of the field-strength scale $M/r^3$.
\end{enumerate}

*Proof.* The structure equations below are the torsion condition written in components of the coframe $\theta^a(v) = \gamma^a \cdot \hb^{-1}(v)$, and the one-forms $\omega^a{}_b$ are the components of the rotation-gauge field, so that evaluating them on a background direction gives $\Omega(a)$ (Fact \claimref{synthesis.imported-gtg-dictionary}(i) and (ii)). (1) $\beta = (2M)^{1/2} r^{-1/2}$ gives $\beta' = -\tfrac12 (2M)^{1/2} r^{-3/2} = -\beta/2r$ and $\beta\beta' = -\beta^2/2r = -M/r^2$. (2) The displayed substitutions, each one line; the coefficients of $\omega^2{}_0$ and $\omega^2{}_1$ are read off the decomposition $dr = \theta^1 - \beta\theta^0$, which is where the gauge field's off-diagonal character enters the connection. The script verifies the $\theta^0$, $\theta^1$ and $\theta^2$ structure equations as exact identities in $\mathbb{Q}(r)[\beta]$. (3) The frame duals of $\theta^0 = dt, \qquad \theta^1 = dr + \beta\,dt, \qquad \theta^2 = r\,d\vartheta, \qquad \theta^3 = r\sin\vartheta\,d\varphi$ satisfy $\partial_t = \hat e_0 + \beta\,\hat e_1$ and $\partial_r = \hat e_1$, so $\omega^1{}_0(\partial_t) = -\beta'\,\theta^1(\partial_t) = -\beta'\beta$ and $\omega^1{}_0(\partial_r) = -\beta'$; assembling into the bivector-valued $\Omega$ gives the display, and the numerical identities are (1).


With the connection known, the field equations and the curvature can be checked directly.

**Theorem 13 (The solution, and where the divergence lies).** The pair $(\hb, \Omega)$ of $\hb(a) \;=\; a - \beta\,(a \cdot \et)\,\er \;=\; (1 - \beta P)(a), \qquad \beta(r) = \sqrt{2M/r}, \qquad P(a) := (a \cdot \et)\,\er$ and Proposition \claimref{singularity.connection-bivector-computed} solves the vacuum field equations $\mathcal{R}(a) - \tfrac12\, a\, \mathcal{R} \;=\; 8\pi\, T(a), \qquad D \wedge \hb(a) \;=\; \hb(\nabla \wedge a)$ at every $r > 0$, and the divergence of the classical description resides in $\Omega$ and in the curvature, not in $\hb$:
\begin{enumerate}
\item (The radial curvature, from the gauge field alone.) On the radial plane both connection values are multiples of the single bivector $\sigma_r$, so the commutator term of the field strength the relation displayed with \claimref{singularity.imported-equivalence-einstein-equations} vanishes identically and nothing depends on $t$; hence, in two lines,
\[
\mathcal{R}(\partial_t \wedge \partial_r)
\;=\; \partial_t\,\Omega(\partial_r) - \partial_r\,\Omega(\partial_t) + \Omega(\partial_t)\times\Omega(\partial_r)
\;=\; -\,\partial_r\Bigl(\frac{M}{r^2}\Bigr)\sigma_r
\;=\; \frac{2M}{r^3}\,\sigma_r :
\]
the radial plane is an eigenplane of the curvature with eigenvalue of magnitude $2M/r^3$, derived without leaving the gauge formalism.
\item (Vacuum.) The full curvature operator is diagonal on the six frame planes with eigenvalues of magnitudes $(2M/r^3, M/r^3, M/r^3, M/r^3, M/r^3, 2M/r^3)$ and vanishing Ricci contraction: the mixed and angular planes are computed in the section ``The curvature operator, by the Cartan structure equations'' in the static chart, where the computation is shortest, and the two pictures agree on the invertible region by Fact \claimref{singularity.imported-equivalence-einstein-equations}. The shape this spectrum assembles into is Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}'s task.
\item (Unimodularity.) $\det \hb = 1$ exactly, at every radius, horizon included: $P$ is rank-one nilpotent, so $1 - \beta P$ is unipotent as a matrix. Likewise the $(t,r)$ block of the metric $g(a,b) \;=\; \hb^{-1}(a) \cdot \hb^{-1}(b)$ has determinant $-1$ at every radius. Nothing determinant-like degenerates at any $r > 0$: at finite radius the classical field is a volume-preserving shear, and the entire divergence of the approach is carried by the connection (Proposition \claimref{singularity.connection-bivector-computed}(3)) and by the curvature, both of which diverge, and by the metric components themselves, which diverge without a rescaled limit unless one is taken exactly as in Proposition \claimref{singularity.degeneration-exactly}.
\end{enumerate}

*Proof.* (1) The display, using Proposition \claimref{singularity.connection-bivector-computed}(3) and $-\,\partial_r(Mr^{-2}) = 2M/r^3$; the vanishing of the commutator is $\sigma_r \times \sigma_r = 0$. The script checks the identity $(\beta\beta')' = 2M/r^3$ in $\mathbb{Q}(r)[\beta]$, the vanishing of the angular wedge contribution, and the two-form computation itself. (2) the section ``The curvature operator, by the Cartan structure equations'', whose eigenvalues are verified as rational-function identities; vacuum is the vanishing of the Ricci contraction of that spectrum, equivalently Fact \claimref{singularity.imported-equivalence-einstein-equations} against the Ricci-flatness of Schwarzschild. (3) $\det(1 - \beta P) = 1$ for nilpotent $P$ (unipotent matrices have unit determinant; the script evaluates the determinant exactly at sample $\beta$ including the horizon), and the PG $(t,r)$ block $\bigl(\begin{smallmatrix} 1-\beta^2 & -\beta \\ -\beta & -1 \end{smallmatrix}\bigr)$ has determinant $-(1-\beta^2) - \beta^2 = -1$.


A divergence could in principle be an artefact of the gauge, so we ask whether any gauge choice removes it.

**Theorem 14 (Non-removability: the invariant argument).** The curvature scalar
\[
K \;:=\; R_{abcd}R^{abcd} \;=\; 4\Bigl(2\,\bigl(\tfrac{2M}{r^3}\bigr)^2 + 4\,\bigl(\tfrac{M}{r^3}\bigr)^2\Bigr) \;=\; \frac{48\,M^2}{r^6}
\;\longrightarrow\; \infty \quad (r \to 0),
\]
and $K$ is invariant under every gauge transformation of the theory, $r$-dependent transformations of arbitrary size included. Hence no gauge choice removes the degeneration at $r = 0$: the division-by-zero locus is a property of the solution, not of its presentation.

*Proof.* The middle equality evaluates $K$ from the eigenvalue spectrum of Proposition \claimref{singularity.solution-where-divergence-lies}(2) (each plane contributes four times its eigenvalue squared), and is verified as an exact rational-function identity in the script. Invariance: under the rotation-gauge law $\hb(a) \;\mapsto\; R\,\hb(a)\,\tilde R, \qquad \Omega(a) \;\mapsto\; R\,\Omega(a)\,\tilde R - 2\,(a\cdot\nabla R)\,\tilde R$ the curvature transforms by conjugation, $\mathcal{R}(B) \mapsto R\,\mathcal{R}(B)\tilde R$, which preserves every scalar contraction; under position-gauge displacements it transforms by pullback, which relocates but cannot alter the function's unbounded range on any neighbourhood of the singular locus. A divergent invariant cannot be transformed to a finite one.


We then follow the light cones inward to see the degeneration geometrically.

**Theorem 15 (The cones fold).** Track the null directions of the $(t,r)$ plane in the metric $g(a,b) \;=\; \hb^{-1}(a) \cdot \hb^{-1}(b)$, $g(a,a) = \hb^{-1}(a)^{2}$ with $\hb^{-1} = 1 + \beta P$: for $a = \et + \lambda\,\er$,
\[
\hb^{-1}(a) = \et + (\lambda + \beta)\,\er, \qquad g(a,a) = 1 - (\lambda + \beta)^2 ,
\]
so $a$ is $g$-null exactly when $\lambda = -\beta \pm 1$: the physical cone's two null directions are $\et + (-\beta \pm 1)\er$, the radial null curves $dr/dt = -\beta \pm 1$ of the Painlev\'e-Gullstrand line element of the section ``The metric of the gauge field, and its static form''. At the horizon ($\beta = 1$) they are $\lambda = 0$, the hovering ray, and $\lambda = -2$, an ingoing one. Normalising each by its $\er$-coefficient and letting $r \to 0$ (so $\beta \to \infty$),
\[
\tfrac{1}{-\beta \pm 1}\,\et + \er \;\longrightarrow\; \er :
\]
both branches of the light cone collapse onto the single direction $\er$, both tipping towards $-\er$, inward, on the way. Simultaneously $g(\et, \et) = 1 - \beta^2 \to -\infty$: no rescaling of the classical field stays finite and nondegenerate. The degeneration is through a null kernel direction in the exact sense of Proposition \claimref{singularity.degeneration-exactly}, and it is not removable by gauge choice (Proposition \claimref{singularity.non-removability-invariant-argument}).

*Proof.* The displayed computations, using $\et \cdot \er = 0$ to remove the cross term in $\hb^{-1}(a)^{2}$ (orthogonal vectors anticommute, \claimref{std-algebra.orthogonal-anticommute}) (note that it is $\hb^{-1}$, not $\hb$, that enters the metric: the $g$-null vectors are the $\hb$-images of the flat null vectors, $\hb(\et \pm \er) = \et + (\pm 1 - \beta)\er$); the limit is elementary. The two claims of the final sentence are the two propositions cited (\claimref{singularity.degeneration-exactly} and \claimref{singularity.non-removability-invariant-argument}), which are the exact forms this proposition's limits point at.


Knowing which direction folds, we can classify the obstruction.

**Theorem 16 (Type N, and only type N).** The obstruction at $r = 0$ is type N in the taxonomy of \cite[\S 3]{ButlerT1}: an isotropic direction without a metric partner, in the degenerate sense in which the root paper hands such cases to the sheaf paper. Type C cannot occur: $\Cl(1,3)$ has $p - q = -2 \equiv 6 \pmod 8$, hence is central simple ($\cong \Mat_2(\HH)$), has no central idempotents, and offers ideal fusion nothing to fuse. Type P, which is present in $\Cl(1,3)$ as in every algebra of its size, demands no transport: its rule is the rule of no rule \cite[\S 6, Prop.~6.1]{ButlerT1}, so it neither licenses nor obstructs the ascent. The operative transport rule is Rule 1, the Witt completion, and by \cite[Thm.~3.6]{ButlerT3} no floor of the resulting tower ever develops a type-C obstruction either. This is the algorithm's Step 2 \cite[\S 8.1, Step 2]{ButlerT1}, with both diagnostic questions answered by computation.

*Proof.* The degenerating direction is null for the limit form (Proposition \claimref{singularity.degeneration-exactly}(3)). This is the type-N datum of \cite[Def.~3.1, Prop.~3.3]{ButlerT1} (\claimref{transport.existence-locus-type-n}) in a degenerate setting that the root paper's taxonomy does not itself cover: there, type N is a null vector of a nondegenerate form, which acquires its annihilating idempotent through a hyperbolic partner, whereas here $\er$ lies in the radical of $\hat g$ and has no partner at all. The root paper is explicit that its algorithm assumes nondegeneracy and that the degenerate case is the sheaf paper's \cite[Rem.~4.15, Rem.~8.4]{ButlerT1}; the warrant for treating the radical direction as type N and applying Rule 1 fibrewise is therefore the localisation theorem of \cite[Thm.~4.4, Cor.~4.5]{ButlerT4} (\claimref{sheaf.one-sided-completion}, \claimref{sheaf.localised-transport}) in the Schwarzschild form \cite[Thms 8.7, 8.12]{ButlerT4} (\claimref{sheaf.schwarzschild-degeneration-boundary-tame}, \claimref{sheaf.one-sided-completion-singularity}), which Step 3 invokes, and which supplies the hyperbolic partner by completion exactly on $E$. The absence of type C is the classification: the mod-8 arithmetic and the classification $\Cl(1,3) \cong \Mat_2(\HH)$ are classical \cite{Porteous1995} (\claimref{primer.classification-real-clifford-algebras}, \claimref{std-algebra.sta-matrix}); the existence criterion for type C ($p - q \equiv 1 \bmod 4$) is \cite[Thm.~3.6]{ButlerT1} (\claimref{transport.existence-classification-type-c}), and $6 \not\equiv 1 \bmod 4$; the root paper's own worked signature for $\Cl(1,3)$ is \cite[Ex.~3.12]{ButlerT1}. That type P imposes nothing is \cite[Prop.~6.1]{ButlerT1} (\claimref{transport.type-p-self-repairing}): the identity assignment repairs every idempotent at cost zero. The tower statement is the frozen clock of T3 \cite{ButlerT3} (\claimref{tower.rigidity-clock-frozen}). The script checks the mod-8 datum and the centre; the type-N diagnosis itself is a citation, not a computation.


Having classified the obstruction, we return to the curvature and find its exact shape.

**Theorem 17 (The curvature of the gauge field: exact shape decoupling).** Let $\sigma_r$ be the unit bivector of the radial boost plane, and let $\Pi$ denote the projection of the six-dimensional bivector space onto $\operatorname{span}\{\sigma_r, I\sigma_r\}$, with $I$ the pseudoscalar. The radial plane is $\hb$-invariant,
\[
\hb(\et) \wedge \hb(\er) \;=\; (\et - \beta\er) \wedge \er \;=\; \et \wedge \er ,
\]
so the coordinate and physical radial planes coincide and $\sigma_r$ needs no chart to define. Then, exactly and at every radius,
\[
\mathcal{R}(B) \;=\; -\,\frac{M}{r^3}\,S(B), \qquad
S \;:=\; 1 - 3\Pi \;=\; -\tfrac12\bigl(B \mapsto B + 3\,\sigma_r B \sigma_r\bigr),
\]
in the sign convention of Proposition \claimref{singularity.solution-where-divergence-lies}(1) and of the Cartan computation of the section ``The Schwarzschild curvature and the surface gravity: the metric-picture cross-check'', which agree: $\mathcal{R}(\sigma_r) = +2M/r^{3}\,\sigma_r$ while $S(\sigma_r) = -2\sigma_r$ (only the eigenvalue ratio, the trace, and the identity of the distinguished plane pair enter the chain, and each is convention-free). The shape operator satisfies
\[
S^2 + S = 2 ,
\]
has spectrum $(-2, -2, 1, 1, 1, 1)$ with the doubled eigenvalue attained exactly on $\{\sigma_r, I\sigma_r\}$, and is trace-free on $\Lambda^2$, though that verifies an algebraic identity rather than field equations: $\tr(1 - 3\Pi) = 6 - 6 = 0$ holds automatically for any rank-two $\Pi$, and trace-freeness on $\Lambda^2$ is the vanishing of the scalar curvature, not Ricci flatness, which is carried by the solution of the section ``Step 1: locate the failure'' and not by this operator identity. The entire approach to the singularity is carried by the single scalar $M/r^3$.

*Proof.* Three parts, each machine-checked. \emph{The algebra of $S$.} For $B$ in the plane pair: $\sigma_r\,\sigma_r\,\sigma_r = \sigma_r$ since $\sigma_r^2 = 1$, and $\sigma_r (I\sigma_r)\sigma_r = I\sigma_r^3 = I\sigma_r$ since $I$ commutes with every even element (\claimref{std-algebra.pseudoscalar-commutation}); so $-\tfrac12(B + 3\sigma_r B\sigma_r) = -2B$ there. For each of the four mixed planes, $B$ shares exactly one index with the radial plane, hence anticommutes with $\sigma_r$ (\claimref{std-algebra.orthogonal-anticommute}): $\sigma_r B \sigma_r = -B\sigma_r^2 = -B$, giving $+B$. This is $1 - 3\Pi$; then $S^2 = 1 + 3\Pi$ (idempotency of $\Pi$) gives $S^2 + S = 2$, the spectrum is read off, and the trace is $2\cdot(-2) + 4\cdot 1 = 0$. \emph{The eigenvalues.} On the radial plane the eigenvalue comes from the gauge field alone: Proposition \claimref{singularity.solution-where-divergence-lies}(1) computed, in two lines and with the commutator term vanishing identically,
\[
\mathcal{R}(\partial_t \wedge \partial_r) \;=\; -\,\partial_r\Bigl(\frac{M}{r^2}\Bigr)\,\sigma_r \;=\; \frac{2M}{r^3}\,\sigma_r .
\]
The mixed and angular planes are computed in the section ``The curvature operator, by the Cartan structure equations'' by the Cartan structure equations in the static chart, giving $-M/r^3$ on the four mixed planes and the doubled value again on the angular dual; curvature is a pointwise invariant, and the two pictures agree on the invertible region by Fact \claimref{singularity.imported-equivalence-einstein-equations}. The eigenvalue ratio is $-2 : 1$, which is the ratio of $S$'s spectrum. \emph{Assembly.} An operator diagonal on the six planes with eigenvalues proportional to $(-2,-2,1,1,1,1)$ is $\pm(M/r^3)(1 - 3\Pi)$, and the sign is fixed by the radial plane: $\mathcal{R}(\sigma_r) = +2M/r^{3}\,\sigma_r$ against $S(\sigma_r) = -2\sigma_r$ gives the minus sign, and the mixed planes, $-M/r^{3}$ against $S = +1$, confirm it. The $\hb$-invariance display is one line of anticommutation ($\er \wedge \er = 0$). The script checks the conjugation table, the operator identities, the spectrum and trace, the eigenvalue ratio against the appendix's rational-function values, the sign of the identity on the radial and mixed planes, and the invariance display, blade-exactly.


## Einstein's equations in the completion

This short section recasts the vacuum field equations in covariant form on the interior region, using the tractor connection.

We next set the vacuum equations in covariant language, starting from two properties of the tractor connection.

**Theorem 18 (Metric parallelism, and the trace of the Schouten condition).** Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). (i) The connection \claimref{interior.imported-tractor-connection}, which on flat spacetime is the $\Cl(2,4)$ gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, preserves the tractor metric $\ip{(\sigma,\mu,\rho)}{(\sigma,\mu,\rho)} \;=\; g(\mu,\mu) \,+\, 2\sigma\rho$, the square $Q$ of $\Cl(2,4)$. (ii) If $\Sch_{ab} = c\, g_{ab}$ for a function $c$, that is $\Sch(A) = c\,A$ for the Schouten map of the field strength, then $c = \tfrac{R}{24}$ and $\Ric_{ab} = \tfrac{R}{4} g_{ab}$, that is $\mathcal{R}(A) = \tfrac14\mathcal{R}\,A$; in particular $\Sch_{ab} = 0$ if and only if $\Ric_{ab} = 0$.

*Proof.* Read in Gauge Theory Gravity: the metric $g$ below is the derived metric of the gravitational field $(\hb, \Omega)$ on flat spacetime, the manifold is the invertible region, and the tractor connection is the flat-space $\Cl(2,4)$ gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}; the index computation below is its reading in the splitting of $g$ (Fact \claimref{synthesis.imported-gtg-dictionary}).

(i) Along any direction $a$, with primes denoting the slots of \claimref{interior.imported-tractor-connection},
\[
\tfrac12\,\partial_a Q(T) \;=\; \sigma'\rho + \rho'\sigma + \mu^b\mu'_b
= (\nabla_a\sigma - \mu_a)\rho + (\nabla_a\rho + \Sch_a{}^b\mu_b)\sigma + \mu^b(\nabla_a\mu_b + g_{ab}\rho - \Sch_{ab}\sigma).
\]
The genuine derivative terms assemble to $\tfrac12\partial_a(2\sigma\rho + |\mu|^2)$; the remainder is $-\mu_a\rho + \mu_a \rho + \Sch_a{}^b\mu_b\sigma - \Sch_{ab}\mu^b\sigma = 0$, the two Schouten terms being one contraction written with the index raised on either side, so that no symmetry of $\Sch$ is needed.
(ii) Tracing $\Sch_{ab} = c\,g_{ab}$ gives $4c = \tfrac12(R - \tfrac{4R}{6}) = \tfrac{R}{6}$, so $c = \tfrac{R}{24}$; substituting back, $\Ric_{ab} = \tfrac{R}{6}g_{ab} + 2c\,g_{ab} = \tfrac{R}{4}g_{ab}$. If $c = 0$ then $R = 24c = 0$ and hence $\Ric = 0$; the converse is immediate.


These properties prepare the covariant form of the vacuum equations.

**Theorem 19 (Covariant form of the vacuum equations).** Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) on its invertible region $M^\circ$, and let $I_g := (1, 0, 0) = \nInf$ be the pure-scale section of $\mathcal{T}$ in the scale $g$. For the tractor connection, which in Gauge Theory Gravity is the $\Cl(2,4)$ rotation-gauge field $D^{T}_{a} = a \cdot \nabla + \Omega_{T}(a)\times$, $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$, acting on tractors $\sigma\nInf + \mu + \rho\nO$ (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), with slots in the splitting of $g$,
\[
\nabla_a I_g = \bigl(0,\; -\Sch_{ab},\; 0\bigr), \qquad\text{that is}\qquad D^{T}_{a}\nInf = -\Sch\bigl(\hb^{-1}(a)\bigr),
\]
so $I_g$ is parallel if and only if $\Sch = 0$, if and only if $g$ is Ricci-flat, if and only if (Fact \claimref{interior.imported-equivalence-einstein-equations}) the GTG vacuum field equations hold. Moreover $Q(I_g) = 0$: the section is null. Hence the vacuum field equations on $M^\circ$ are exactly equivalent to the parallelism of the scale tractor $I_g$ attached to $g$: the ideal point of the fibre quadric that the physical scale distinguishes is covariantly constant. (Existence of \emph{some} parallel null tractor is the strictly weaker, conformally invariant statement that $[g]$ is almost Ricci-flat: it carries an almost-Einstein scale which is Ricci-flat away from that scale's zero set, and the zero set may be non-empty. A non-constant rescaling $e^{2\omega}g$ already keeps the parallel section while losing the field equations.) The statement is covariant under the gauge transformations of $\mathcal{T}$, whose structure algebra is $\mathfrak{so}(2,4)$ acting through the bivectors of $\Cl(2,4)$.

*Proof.* Read in Gauge Theory Gravity: the metric $g$ below is the derived metric of the gravitational field $(\hb, \Omega)$ on flat spacetime, the manifold is the invertible region, and the tractor connection is the flat-space $\Cl(2,4)$ gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}; the index computation below is its reading in the splitting of $g$ (Fact \claimref{synthesis.imported-gtg-dictionary}).

Substitute $(\sigma, \mu, \rho) = (1, 0, 0)$ into \claimref{interior.imported-tractor-connection}: the first slot is $\nabla_a 1 - 0 = 0$; the second is $0 + g_{ab}\cdot 0 - \Sch_{ab}\cdot 1 = -\Sch_{ab}$; the third is $0 + \Sch_a{}^b \cdot 0 = 0$. So $\nabla I_g = 0$ iff $\Sch_{ab} = 0$ iff $\Ric = 0$ by Lemma \claimref{interior.metric-parallelism-trace-schouten-condition}(ii), and Fact \claimref{interior.imported-equivalence-einstein-equations} converts Ricci-flatness into the GTG field equations on the region of invertibility. The norm is $Q(I_g) = g(0,0) + 2 \cdot 1 \cdot 0 = 0$. Covariance is the statement that both sides of the equivalence are conditions on a section of an invariantly defined bundle with its canonical connection (Fact \claimref{interior.imported-tractor-connection}), the section itself determined by the given scale $g$: the splitting used to write the proof is scale-dependent; the bundle, the connection, and the parallelism condition on the given section are not.


## Entropy and information

Before the descent is built, we measure what it costs to discard coherences, in a form general enough to cover the descent when it arrives.

We now turn from geometry to information and ask exactly what is lost when coherences are discarded.

**Theorem 20 (The deficit theorem: the cost of descent, exactly).** Let $E$ be the pinching by any complete family of orthogonal projectors ($\EN$ included) and $\rho$ a density matrix. Then $E$ is idempotent, trace-preserving, and self-adjoint for the Hilbert-Schmidt pairing, and
\[
S\bigl(E(\rho)\bigr) - S(\rho) \;=\; \rel{\rho}{E(\rho)} \;\geq\; 0 ,
\]
with $S$ the von Neumann entropy and $D$ the relative entropy, and with equality if and only if $\rho = E(\rho)$. The level discrepancy of Step 6b is this quantity: not a slogan but a relative entropy, computed once and for all.

*Proof.* Idempotency and trace preservation are the orthogonality and completeness of the $\Pi_\varepsilon$. Self-adjointness: $\tr(E(a)\,b) = \sum_\varepsilon \tr(\Pi_\varepsilon a \Pi_\varepsilon b) = \sum_\varepsilon \tr(a\, \Pi_\varepsilon b \Pi_\varepsilon) = \tr(a\,E(b))$ by cyclicity of the trace. The key step: $E(\rho)$ commutes with every $\Pi_\varepsilon$, hence so does every function of it, hence $E\bigl(\log E(\rho)\bigr) = \log E(\rho)$; self-adjointness with $b = \log E(\rho)$ then gives
\[
\tr\bigl(\rho \log E(\rho)\bigr) \;=\; \tr\bigl(E(\rho) \log E(\rho)\bigr) ,
\]
whence $\rel{\rho}{E\rho} = \tr\rho\log\rho - \tr\rho\log E\rho = -S(\rho) + S(E\rho)$. Nonnegativity and the equality case are Klein's inequality, the single classical input of the theorem \cite[\S 11.3]{NielsenChuang}. The script verifies the structural clauses on a generic rational matrix and the key identity, in moment form $\tr\bigl(\rho\,(E\rho)^m\bigr) = \tr\bigl(E\rho\,(E\rho)^m\bigr)$, on the model's scrambled two-pair state, in exact arithmetic.


## Zero divisors and obstructions

This section looks closely at the smallest algebraic unit in which a zero divisor acquires a partner.

To see which pinching the completion calls for, we first look at the pair that gives a zero divisor its partner.

**Theorem 21 (Pseudo-inverse identities, and the hyperbolic atom).** From $v^2 = (v^*)^2 = 0, \qquad v v^* + v^* v = 1$ alone: $v v^* v = v$ and $v^* v v^* = v^*$, so each member of the pair is a von Neumann pseudo-inverse of the other, with no genuine inverse existing ($v$ is a zero divisor). The pair is realisable inside a single $(1,1)$ block: in $\Cl(1,1)$ with $e_0^2 = 1$, $e_1^2 = -1$, the vectors
\[
v = \tfrac12(e_0 + e_1), \qquad v^* = \tfrac12(e_0 - e_1)
\]
satisfy $v^2 = (v^*)^2 = 0, \qquad v v^* + v^* v = 1$ exactly. This block, the \emph{hyperbolic atom}, is the unique unit of transport that, at the level of elements, needs no ascent of its own \cite[Rem.~4.5]{ButlerT1}.

*Proof.* $v v^* v = v(1 - v v^*)^{\vphantom{*}} = v - v^2 v^* = v$ using $v^2 = (v^*)^2 = 0, \qquad v v^* + v^* v = 1$ and $v^2 = 0$; mirror for $v^*$. In the model: $v^2 = \tfrac14(e_0^2 + e_1^2) = \tfrac14(1 - 1) = 0$ (the cross terms cancel by anticommutation, \claimref{std-algebra.orthogonal-anticommute}), likewise $(v^*)^2 = 0$, and, by \claimref{std-algebra.vector-squares}, $v v^* + v^* v = 2\,(v \cdot v^*) = \tfrac12\bigl(e_0^2 - e_1^2\bigr) = \tfrac12(1 + 1) = 1$.


## Descent, parity and states

Here we define the map back down from the completion, identify it with the parity average, and follow what it implies for states and their thermal form.

The occupation projectors built from that pair define the way back down.

**Theorem 22 (The descent, and what it erases).** Set $P := v^* v$. Then $P^2 = P$, $1 - P = v v^*$, and in the defining $2 \times 2$ representation ($v = E_{12}$, $v^* = E_{21}$),
\[
P = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}, \qquad
E(x) := P x P + (1{-}P)\,x\,(1{-}P), \qquad
E\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a & 0 \\ 0 & d \end{pmatrix} .
\]
Descent retains the occupation data and erases the coherences $b, c$.

*Proof.* $P^2 = v^*(v v^*)v = v^*(1 - v^* v)v = v^* v - (v^*)^2 v^2 = P$, using $v^2 = (v^*)^2 = 0, \qquad v v^* + v^* v = 1$ (the CAR of a Witt pair, \claimref{std-algebra.witt-basis-car}) twice and $v^2 = (v^*)^2 = 0$; then $1 - P = vv^*$ is $v^2 = (v^*)^2 = 0, \qquad v v^* + v^* v = 1$ itself. In the defining representation (\claimref{std-algebra.cl11-matrix}) $v = E_{12}$, $v^*= E_{21}$ satisfy $v^2 = (v^*)^2 = 0, \qquad v v^* + v^* v = 1$ by matrix multiplication, $P = E_{22}$, and the displayed action of $E$ is the block computation $PxP + (1{-}P)x(1{-}P) = \operatorname{diag}(a, d)$.


That map has a second description, in terms of the parity of the mode.

**Theorem 23 (The descent is the parity average).** For every $x \in \Aa$,
\[
E(x) \;=\; \tfrac12\bigl(x + \alpha(x)\bigr) \;=\; \tfrac12\bigl(x + \sigma x \sigma\bigr) .
\]
Consequently $E$ is the group average over $\{\id, \alpha\}$, hence the unique conditional expectation of $\Aa$ onto its fixed-point algebra $\Aev$; its range is $\Aev$ and its kernel is exactly $\Aod$, the adjoined ladder sector; and $E$ preserves every state $\omega$ with $\omega \circ \alpha = \omega$.

*Proof.* In the defining representation $v = E_{12}$, $v^{*} = E_{21}$, so $P = E_{22}$ and $\sigma = 2P - 1 = \operatorname{diag}(-1, +1)$; then
\[
\alpha\begin{pmatrix} a & b \\ c & d \end{pmatrix}
= \begin{pmatrix} -1 & 0 \\ 0 & 1\end{pmatrix}\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} -1 & 0 \\ 0 & 1\end{pmatrix}
= \begin{pmatrix} a & -b \\ -c & d \end{pmatrix},
\]
so $\tfrac12(x + \alpha(x)) = \operatorname{diag}(a,d)$, which is the value of $E$ computed in Proposition \claimref{singularity.descent-what-it-erases}. The average of a finite group acting by automorphisms is a conditional expectation onto the fixed-point algebra. It is moreover the unique conditional expectation of $\Aa$ onto $\Aev$, by bimodularity: if $F$ is any conditional expectation onto $\Aev$, then for odd $x$, since $\sigma \in \Aev$ and $\sigma x \sigma = -x$, bimodularity gives $\sigma F(x) \sigma = F(\sigma x \sigma) = -F(x)$, while $F(x) \in \Aev$ is fixed by conjugation with $\sigma$, so $F(x) = -F(x) = 0$: every conditional expectation onto $\Aev$ annihilates the $(-1)$-eigenspace of $\alpha$, which is $\Aod = \operatorname{span}\{v, v^{*}\}$, and agrees with the identity on $\Aev$, hence equals $E$ on $\Aa = \Aev \oplus \Aod$. State preservation is $\omega(E(x)) = \tfrac12(\omega(x) + \omega(\alpha(x))) = \omega(x)$. The script verifies the identity, idempotence, the conditional-expectation property $E(axb) = aE(x)b$ for even $a, b$, and the range and kernel, on generic rational data.


Before asking where purity comes from, we set out the modular theory of a single matrix factor in full.

**Theorem 24 (Modular theory of a matrix factor, proved outright).** Let $H = \C^n \otimes \C^n$, let $M = \Mat_n(\C) \otimes 1$ act on the first factor, and let $\Omega = \sum_i \lambda_i\, |ii\rangle$ with all $\lambda_i > 0$ and $\sum \lambda_i^2 = 1$ (any cyclic separating vector of $M$ has this form in its Schmidt basis). Define the Tomita operator as the closure of $S : a\Omega \mapsto a^*\Omega$ ($a \in M$). Then its polar decomposition $S = J\Delta^{1/2}$ has
\[
\Delta = \rho \otimes \bar\rho^{\,-1}, \qquad \rho = \sum_i \lambda_i^2\,|i\rangle\langle i| , \qquad J\,|ij\rangle = |ji\rangle \ \text{(antilinearly)},
\]
and the modular flow on $M$ is $\sigma_t(a) = \rho^{it} a\, \rho^{-it}$. Moreover the state $\omega = \langle\Omega, \cdot\,\Omega\rangle$ satisfies the KMS identity $\omega(ab) = \omega(b\,\rho\,a\,\rho^{-1})$ for all $a, b \in M$.

*Proof.* Everything is finite-dimensional, so closures are automatic. On the matrix units $a = |i\rangle\langle j| \otimes 1$: $a\Omega = \lambda_j |ij\rangle$ and $a^*\Omega = \lambda_i |ji\rangle$, so $S$ is the antilinear map $|ij\rangle \mapsto (\lambda_i/\lambda_j)\,|ji\rangle$, and since the $a\Omega$ span $H$ ($\Omega$ is cyclic), this determines $S$. Define $\Delta |ij\rangle := (\lambda_i^2/\lambda_j^2)|ij\rangle$, which is exactly $(\rho \otimes \bar\rho^{\,-1})|ij\rangle$, positive and invertible, and let $J$ be the antilinear extension of $|ij\rangle \mapsto |ji\rangle$, which is antiunitary with $J^2 = 1$. Then $J\Delta^{1/2}|ij\rangle = (\lambda_i/\lambda_j) J|ij\rangle = (\lambda_i/\lambda_j)|ji\rangle = S|ij\rangle$ (the eigenvalues are real, so antilinearity causes no conjugation), and uniqueness of the polar decomposition gives the claim. The flow: $\Delta^{it}(b \otimes 1)\Delta^{-it} = (\rho^{it}\otimes\bar\rho^{-it})(b \otimes 1)(\rho^{-it}\otimes\bar\rho^{\,it}) = \rho^{it} b \rho^{-it} \otimes 1$, interior to $M$. KMS: the reduced density matrix of $\Omega$ on the first factor is $\rho$, so $\omega(x) = \tr(\rho x)$ for $x \in \Mat_n(\C)$, and $\omega(b\,\rho a \rho^{-1}) = \tr(\rho\, b\, \rho a \rho^{-1}) = \tr(\rho\, a b) = \omega(ab)$ by cyclicity of the trace.


That machinery now locates the partner of a mixed mode.

**Theorem 25 (Purity is an output: the partner is the commutant).** Let $\omega$ be a faithful state on the mode factor with $\varrho = \operatorname{diag}(\lambda_0^{2}, \lambda_1^{2})$, $\lambda_i > 0$. In its GNS representation: the space is $\C^{2}\otimes\C^{2}$ and the cyclic vector is $\Omega = \sum_i \lambda_i|ii\rangle$, cyclic and separating for $\pi(\Aa) = \Aa\otimes 1$; the commutant $\pi(\Aa)' = 1 \otimes \Aa$ is the partner copy and equals $J\pi(\Aa)J$; any two purifications of $\omega$ differ by a unitary on the purifying factor alone; and when $\omega$ is the Gibbs state at $\beta$, $\Omega$ is the thermofield double with $\tan\theta = e^{-\omega_k/2T}$, which is exactly the vector Lemma \claimref{singularity.schmidt-forcing-proved-outright} produces. Hypothesis (i) of Theorem \claimref{singularity.modular-descent}, the existence of the partner, and the thermofield form are therefore consequences of the one-sided state rather than independent choices.

*Proof.* The first two clauses are Lemma \claimref{singularity.modular-theory-matrix-factor-proved-outright} read in the direction of construction rather than of analysis: that lemma computes $\Delta = \rho\otimes\bar\rho^{-1}$ and $J|ij\rangle = |ji\rangle$ for this very $\Omega$ and establishes that $\Omega$ is cyclic and separating, the identification of the commutant being Tomita's theorem, whose finite-dimensional content is that lemma's polar decomposition. For the third: a purification of $\varrho$ has the $\lambda_i$ as its Schmidt coefficients, so it is $(1\otimes W)\Omega$ for an isometry $W$ between purifying spaces. For the fourth, substituting $\varrho = \operatorname{diag}(1, e^{-\omega_k/T})/Z$ gives $\lambda_1/\lambda_0 = e^{-\omega_k/2T} = \tan\theta$. The script instantiates the purification, the modular eigenvalues and the angle at the rational triple $(\tfrac35, \tfrac45)$.


Returning to the one-sided picture, we ask what any descended marginal must look like.

**Theorem 26 (The descended form is state independent).** Let $\varrho$ be the density matrix of \emph{any} state on the boundary mode space, and $\varrho_k$ its marginal at mode $k$. Then $E_k(\varrho_k)$ is diagonal in that mode's number basis, and therefore
\[
E_k(\varrho_k) \;=\; \frac{e^{-\beta_k \omega_k N_k}}{Z_k}
\]
for a unique $\beta_k \in [-\infty, +\infty]$, determined by $\beta_k\omega_k = \log\bigl(p_k/(1-p_k)\bigr)$ with $p_k$ the descended vacancy probability. (Stated for $\omega_k \neq 0$: at a zero-weight mode the right side is $\tfrac12\,\mathrm{id}$ for every $\beta_k$, so uniqueness always fails there, and existence fails unless $p_k = \tfrac12$.) The descended single-mode state is a Gibbs state of the boost generator $K_k$ whatever the ascended state was: no hypothesis on the state is used.

*Proof.* By Theorem \claimref{singularity.descent-parity-average} the range of $E_k$ is the even subalgebra, which in the number basis is the diagonal. A diagonal density matrix on a two-dimensional space is $\operatorname{diag}(p_k, 1 - p_k)$, and $\beta_k \mapsto (1 + e^{\beta_k\omega_k})^{-1}$ is a bijection from $\R$ onto $(0,1)$, so every such matrix with $0 < p_k < 1$ is the stated Gibbs matrix for exactly one $\beta_k$; the two boundary values are the limits $\beta_k = \pm\infty$.


We now ask what univalence says about the marginals before any descent.

**Theorem 27 (Ascended marginals are diagonal).** Let $\omega$ satisfy (P). Then $\omega(v_k) = \omega(v_k^{*}) = 0$ at every mode, so the ascended marginal $\varrho_k$ is diagonal in the number basis, coincides with $E_k(\varrho_k)$, and is by Theorem \claimref{singularity.descended-form-state-independent} the Gibbs state of $K_k$ at a unique $\beta_k$ for $\omega_k \neq 0$ (at a zero-weight mode diagonality still holds, and the Gibbs form requires $p_k = \tfrac12$, Theorem \claimref{singularity.descended-form-state-independent}'s parenthesis). Consequently partial trace and pinching coincide on every single-mode marginal, which is Proposition \claimref{singularity.pinching-against-partial-trace-scope-coincidence}(i) with hypothesis (ii) of Theorem \claimref{singularity.modular-descent} removed; and the parity protection lemma of the finite-mode model, Lemma \claimref{singularity.parity-protection}, is the special case of this theorem for the model's states, which are even because every configuration in their support has even total occupation.

*Proof.* $v_k$ and $v_k^{*}$ are odd, so $\alpha(v_k) = -v_k$ and (P, \claimref{singularity.p-univalence}) gives $\omega(v_k) = \omega(\alpha(v_k)) = -\omega(v_k)$, hence $\omega(v_k) = 0$, and likewise for $v_k^{*}$. The off-diagonal entries of $\varrho_k$ in the number basis are exactly $\omega(v_k)$ and $\omega(v_k^{*})$, those being the mode's two off-diagonal matrix units. Diagonality is the coincidence with $E_k(\varrho_k)$, and Theorem \claimref{singularity.descended-form-state-independent} supplies the Gibbs form. The argument uses no finiteness and holds verbatim on the CAR algebra over $E$. For the model: its states are supported on configurations with $R_k = L_k$ at every $k$, whose total occupation $2\sum_k b_k$ is even, and a state supported in a single parity sector is even. The script verifies both clauses, with a parity-mixed control whose marginal coherence is nonzero.


We go back to the completed pair to see which flow it carries and how that flow meets the descent.

**Theorem 28 (Modular structure of the completed pair).** Let $(v, v^*)$ satisfy $v^2 = (v^*)^2 = 0, \qquad v v^* + v^* v = 1$ and define $\sigma := v^* v - v v^*$. Then:
\begin{enumerate}
\item $\sigma^2 = 1$; and in the hyperbolic atom of Lemma \claimref{singularity.pseudo-inverse-identities-hyperbolic-atom}, $\sigma = e_0 e_1$ exactly, the unit boost bivector of the plane;
\item the rotor flow $R_\lambda = \exp(\lambda\sigma/2)$ acts by $v \mapsto e^{-\lambda} v$ and $v^* \mapsto e^{+\lambda} v^*$: the pair diagonalises the boost with opposite weights, the structure of outgoing and ingoing horizon modes;
\item the spectral projectors $\tfrac12(1 \pm \sigma)$ of the boost are identically the occupation projectors $v^* v$ and $v v^*$: the descent projectors of Proposition \claimref{singularity.descent-what-it-erases};
\item in the fermionic representation $\sigma = 2N - 1$: the generator of the geometric boost is, up to normalisation, the number operator, $K := \tfrac{\sigma}{2} = N - \tfrac12$;
\item $\mathrm{Spin}^+(1,1)$ is one-dimensional, so the boost flow is the \emph{only} one-parameter flow implemented by real rotors of the atom. The scope matters and is stated: the mode algebra $\Mat_2(\C)$ admits a three-parameter family of one-parameter unitary groups, and the uniqueness claimed is within the class the geometry supplies, real rotor flows of $\Cl(1,1)$; Proposition \claimref{singularity.euclidean-rotor-where-it-lies} later leaves that class deliberately, its Euclidean rotor being complex.
\end{enumerate}
One object, three readings: boost generator, number operator, generator of the descent projectors.

*Proof.* (1) $\sigma^2 = (v^*v)^2 + (vv^*)^2 - v^*v\,vv^* - vv^*\,v^*v = v^*v + vv^* - 0 - 0 = 1$, using idempotency (Proposition \claimref{singularity.descent-what-it-erases}) and $v^2 = (v^*)^2 = 0$ to remove the cross terms. In the atom (\claimref{singularity.pseudo-inverse-identities-hyperbolic-atom}): $v v^* = \tfrac14(e_0 + e_1)(e_0 - e_1) = \tfrac14(1 - e_0e_1 + e_1e_0 + 1) = \tfrac12(1 - e_0e_1)$, so $v^*v = 1 - vv^* = \tfrac12(1 + e_0e_1)$ and $\sigma = e_0 e_1$. (2) From $\sigma v = -v$ and $v\sigma = v$ (in the atom: $e_0e_1(e_0 + e_1) = -(e_1 + e_0)$ and $(e_0+e_1)e_0e_1 = e_1 + e_0$; abstractly from $v^2 = (v^*)^2 = 0, \qquad v v^* + v^* v = 1$), and $\sigma^2 = 1$ giving $e^{-\lambda\sigma} = \cosh\lambda - \sigma\sinh\lambda$:
\[
e^{\lambda\sigma/2}\,v\,e^{-\lambda\sigma/2} = v\,e^{-\lambda\sigma} = v\cosh\lambda - v\sigma\,\sinh\lambda = (\cosh\lambda - \sinh\lambda)\,v = e^{-\lambda}v ,
\]
using $v\sigma = v$ once; mirror-symmetrically for $v^*$. (3) is $v^*v = \tfrac12(1 + \sigma)$. (4) $N = v^*v$ counts occupation in the two-state module, and $\sigma = 2v^*v - 1$. (5) The rotor group of $\Cl(1,1)$ is generated by its single unit bivector.


With a flow singled out, we ask how far its thermal states on a single factor are unique.

**Theorem 29 (KMS uniqueness at a factor).** Let $\Aa$ be a matrix factor, $\alpha_t = \operatorname{Ad}(e^{itK})$ a flow and $\beta \neq 0$. A state $\omega = \tr(\varrho\,\cdot\,)$ is $(\alpha,\beta)$-KMS if and only if $\varrho = e^{-\beta K}/\tr e^{-\beta K}$. In particular there is exactly one KMS state for each $\beta$, and, for $K$ not a multiple of $1$, the KMS states of the flow form a line parametrised by $\beta$.

*Proof.* In finite dimensions the KMS condition reads $\omega(ab) = \omega\bigl(b\,\alpha_{i\beta}(a)\bigr) = \omega\bigl(b\,e^{-\beta K}a\,e^{\beta K}\bigr)$ for all $a, b$. Writing both sides as traces and using cyclicity, the left side is $\tr(b\varrho a)$ and the right side is $\tr\bigl(e^{\beta K}\varrho\, b\, e^{-\beta K} a\bigr)$, so for all $b$,
\[
b\,\bigl(\varrho\, e^{\beta K}\bigr) \;=\; \bigl(e^{\beta K}\varrho\bigr)\, b .
\]
Taking $b = 1$ gives $\varrho e^{\beta K} = e^{\beta K}\varrho$, so $\varrho$ commutes with $K$; the displayed identity then says that $\varrho\,e^{\beta K}$ commutes with everything, hence is central, hence scalar because $\Aa$ is a factor. So $\varrho \propto e^{-\beta K}$, and normalisation fixes the constant. The converse is the same computation read backwards. The script checks the identity on all sixteen matrix-unit pairs for $\varrho \propto \operatorname{diag}(1, \tfrac{16}{9})$ and exhibits a pair at which the tracial state fails it.


The same link between thermal and Gibbs states carries over to any finite-dimensional dynamics, which is the form the boundary windows will take.

**Theorem 30 (Gibbs states are KMS, and conversely, in finite dimensions).** Let $\mathfrak{B} = \End(\C^m)$, let $H$ be diagonal in the basis $(\xi_a)$ with eigenvalues $\lambda_a$, all distinct or not, let $\alpha_t = \mathrm{Ad}(e^{itH})$, and $\beta \in \R$. Then the Gibbs state $\omega_G(x) := \tr(e^{-\beta H}x)/\tr(e^{-\beta H})$ satisfies the KMS identity
\[
\omega_G(x\,y) \;=\; \omega_G\bigl(y\,\alpha_{i\beta}(x)\bigr), \qquad \alpha_{i\beta}(x) := e^{-\beta H}x\,e^{\beta H},
\]
for all $x, y$; and it is the \emph{unique} $\alpha$-KMS state at $\beta$ on $\mathfrak{B}$, degenerate spectrum included.

*Proof.* The identity is cyclicity of the trace:
\[
\omega_G\bigl(y\,\alpha_{i\beta}(x)\bigr) = \tr\bigl(e^{-\beta H}y\,e^{-\beta H}x\,e^{\beta H}\bigr)/Z = \tr\bigl(e^{-\beta H}xy\bigr)/Z = \omega_G(xy),
\]
the trailing $e^{\beta H}$ moved around the trace to cancel the inner factor. Conversely write $\omega(x) = \tr(\rho x)$ and evaluate the KMS identity on matrix units $x = E_{ab}$, $y = E_{cd}$: since $\alpha_{i\beta}(E_{ab}) = e^{-\beta(\lambda_a - \lambda_b)}E_{ab}$ and $\tr(\rho\,E_{ab}E_{cd}) = \delta_{bc}\,\rho_{da}$, the identity reads
\[
\delta_{bc}\,\rho_{da} \;=\; e^{-\beta(\lambda_a - \lambda_b)}\,\delta_{da}\,\rho_{bc}
\qquad \text{for all } a, b, c, d.
\]
Taking $c = b$ and $d = a$ gives $\rho_{aa} = e^{-\beta(\lambda_a - \lambda_b)}\rho_{bb}$: Gibbs ratios between all diagonal entries. Taking $c = b$ and $d \neq a$ gives $\rho_{da} = 0$ (the right side carries $\delta_{da} = 0$), for every pair $d \neq a$, degenerate eigenvalues included: $\rho$ is diagonal. So $\rho = e^{-\beta H}/Z$, and the KMS state is unique. The verification script performs the solve symbolically for the mode algebra $\Mat_2$ with $H = \omega N$ and confirms both clauses as identities of rational functions in the Boltzmann factor.


We turn to a further ingredient.

**Theorem 31 (KMS restricts to invariant subalgebras).** If $\omega$ is $\alpha$-KMS at $\beta$ on $\mathfrak{B}$ and $\mathfrak{C} \subseteq \mathfrak{B}$ is a unital subalgebra with $\alpha_t(\mathfrak{C}) = \mathfrak{C}$, then $\omega|_{\mathfrak{C}}$ is KMS at $\beta$ for $\alpha|_{\mathfrak{C}}$.

*Proof.* For $x, y \in \mathfrak{C}$ the correlation function $t \mapsto \omega(y\,\alpha_t(x))$ is computed entirely from elements of $\mathfrak{C}$ (invariance keeps $\alpha_t(x) \in \mathfrak{C}$), and is the same function of $t$ whether $x, y$ are regarded in $\mathfrak{C}$ or in $\mathfrak{B}$. Its continuation to the closed strip is unique (a function analytic on the strip and continuous on its closure is determined by its boundary restriction to the real line, by uniqueness of analytic continuation), so the strip function and the KMS boundary identity transfer verbatim from $\mathfrak{B}$ to $\mathfrak{C}$.


## Temperature and Hawking radiation

The last section brings in the geometry of the horizon, which sets the rate and with it the temperature, and then assembles the Hawking state and its bosonic reading.

We turn to a further ingredient.

**Theorem 32 ($\kappa = 1/4M$, computed).** For the Schwarzschild gravitational field of the section ``The metric of the gauge field, and its static form'' (the stored field $\hb = 1 - \beta P$ on flat spacetime, Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), the static Killing field $K = \hb^{-1}(e_t)$ has $Q(K) = f = 1 - 2M/r$, and the static observers, of velocity $v = K/\sqrt f$, have redshifted proper acceleration $\sqrt f\,\sqrt{-Q((v \cdot D)v)} = f'(r)/2$ at every $r > 2M$, so the surface gravity of the horizon locus $r = 2M$ is
\[
\kappa \;=\; \lim_{r \to 2M} \frac{f'(r)}{2} \;=\; \frac{1}{2}\cdot\frac{2M}{(2M)^2} \;=\; \frac{1}{4M} .
\]

*Proof.* The components below are those of the covariant derivative $D$ in the static frame, read through Fact \claimref{synthesis.imported-gtg-dictionary} (clauses (ii) and (vi)). The static observer has four-velocity $u = \xi/\sqrt f$ with $\xi = \partial_{t_s}$. Its acceleration $A^\mu = u^\nu \nabla_\nu u^\mu$ has the single component $A^r = \Gamma^r_{tt}\,(u^t)^2$, with $\Gamma^r_{tt} = -\tfrac12 g^{rr}\partial_r g_{tt} = -\tfrac12(-f)(f') = \tfrac12 f f'$ and $(u^t)^2 = 1/f$, so $A^r = f'/2$. Its proper magnitude is $\sqrt{-g_{rr}}\,|A^r| = f'/(2\sqrt f)$, and the redshifted magnitude is $\sqrt f \cdot f'/(2\sqrt f) = f'/2$, finite and radius-independent in its limit. By Fact \claimref{singularity.imported-surface-gravity-redshifted-acceleration}, $\kappa = f'(2M)/2 = 1/4M$. The conversion quoted in Proposition \claimref{singularity.plane-rate} follows: one period $2\pi$ of rapidity is $2\pi/\kappa = 8\pi M$ of Schwarzschild time.


We next see which plane the curvature singles out and how that surface gravity sets its rate.

**Theorem 33 (The plane and the rate).** The plane in which the completed pair lies is not chosen: the doubled eigenvalue of Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling} singles out the pair $\{\sigma_r, I\sigma_r\}$ invariantly at every radius, and its boost member $\sigma_r$, the member with square $+1$ up to the orientation sign, is at the horizon the boost plane of the Killing flow, with surface gravity
\[
\kappa = \frac{1}{4M} .
\]
The geometric normalisation this fixes: an interval of $2\pi$ in rapidity corresponds to $2\pi/\kappa = 8\pi M$ of Schwarzschild time. This single conversion factor is where the numerical value of the temperature enters the chain.

*Proof.* The selection is Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}; $(I\sigma_r)^2 = -1$ while $\sigma_r^2 = +1$ separates the pair's two members invariantly. The surface gravity is computed as the redshifted proper acceleration in the section ``The surface gravity'' (\claimref{singularity.computed}): $\kappa = \tfrac12 f'(r_h) = 1/4M$. The broader geometric development (the parallel ideal point, the weighted limit, the Kerr tests) remains the task of the series' geometry paper T6 \cite{ButlerT6}; nothing below uses more than what Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling} and the appendix prove.


With the rate in hand, the premises can now be brought to bear on every marginal.

**Theorem 34 (The rate, and the discharge of hypothesis (iii)).** Assume (P) and (R). Then at every mode $k$ the marginal is the Gibbs state of $K_k$ at the same inverse temperature,
\[
\beta_k \;=\; \beta \;=\; \frac{2\pi}{\kappa} \;=\; 8\pi M , \qquad T \;=\; \frac{\kappa}{2\pi} \;=\; \frac{1}{8\pi M} \;=\; \TH ,
\]
with occupancy $\omega(v_k^{*}v_k) = (e^{\beta\omega_k} + 1)^{-1} \in (0,1)$. In particular every marginal is faithful, hence cyclic and separating for its mode factor: hypothesis (iii) of Theorem \claimref{singularity.modular-descent} is a consequence of (R), not an assumption; and the temperature is the same at every mode without any condition on the joint state.

*Proof.* Fix a mode and drop its index. By (P, \claimref{singularity.p-univalence}) and Theorem \claimref{singularity.ascended-marginals-are-diagonal} the marginal is $\operatorname{diag}(1 - n, n)$ in the number basis with $n := \omega(v^{*}v) \in [0,1]$. The flow acts by $\alpha_t(v) = e^{-it\omega}v$ and $\alpha_t(v^{*}) = e^{it\omega}v^{*}$ (Theorem \claimref{singularity.modular-structure-completed-pair}(2) at imaginary rapidity, or directly from $Kv = v(K - 1)$). Take $a = v^{*}$, $b = v$: $F(t) = \omega(v^{*}\alpha_t(v)) = e^{-it\omega}n$, and $\omega(\alpha_t(v)v^{*}) = e^{-it\omega}\,\omega(vv^{*}) = e^{-it\omega}(1 - n)$. The gluing condition of (R, \claimref{singularity.r-regularity-fixed-locus}) reads $e^{p\omega}e^{-it\omega}n = e^{-it\omega}(1 - n)$, that is
\[
e^{p\omega}\,n \;=\; 1 - n \qquad\Longleftrightarrow\qquad n \;=\; \frac{1}{e^{p\omega} + 1} ,
\]
which is the Fermi-Dirac occupancy at inverse temperature $p$, strictly between $0$ and $1$ for every finite $p$ and $\omega > 0$. The pair $a = v$, $b = v^{*}$ gives the same equation with $n$ and $1 - n$ exchanged and $p\omega$ negated, hence the same solution; the pairs $a = b$ give $0 = 0$ on both sides since $v^{2} = 0$. So the marginal is $\operatorname{diag}(1, e^{-p\omega})/(1 + e^{-p\omega}) = e^{-p\omega K}/Z$, the Gibbs state of $K$ at $\beta = p = 2\pi/\kappa$ by Theorem \claimref{singularity.descended-form-state-independent}, and $T = 1/\beta = \kappa/2\pi$ is Proposition \claimref{singularity.plane-rate}'s conversion. Faithfulness is $0 < n < 1$: the Gibbs matrix has full rank, so the state is faithful on the mode factor, which for a matrix factor is cyclic and separating. The boundary cases $\beta = \infty$ (unoccupied, $n = 0$) and $\beta = 0$ (tracial, $n = \tfrac12$) fail the gluing condition at every finite nonzero $p$, for $\omega \neq 0$ (at a zero-weight mode the gluing itself degenerates to $n = \tfrac12$, Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}), so on the modes of nonzero weight (R) excludes them rather than presupposing their exclusion. Universality across modes needs no further input: each mode meets the same section with the same $\kappa$, which is constant over the bifurcation sphere (Proposition \claimref{singularity.computed} is radius-only, by spherical symmetry). The script verifies the gluing equation, its unique solution, and the failure of both boundary cases, on rational data.


A value has now been obtained, which leaves open where that value actually comes from.

**Theorem 35 (Rate rigidity: the temperature is not algebra intrinsic).** Let $\alpha_t = \operatorname{Ad}(e^{itK})$ be the boost flow of the single-mode algebra $\Aa$, let $\theta$ be a $*$-automorphism of $\Aa$, and let $\omega_\beta$ denote the $\beta$-KMS state of $\alpha$.
\begin{enumerate}
\item If $\theta$ commutes with the flow then it fixes every Gibbs state of $K$: $\omega_\beta \circ \theta = \omega_\beta$ for every $\beta$.
\item If $\theta$ reverses the flow, $\theta\circ\alpha_t = \alpha_{-t}\circ\theta$, then $\omega_\beta\circ\theta = \omega_{-\beta}$.
\item Under a constant reparametrisation of the flow, $\alpha_t \mapsto \alpha_{ct}$ with $c > 0$, the $\beta$-KMS state of $\alpha$ is the $(\beta/c)$-KMS state of the reparametrised flow: $\omega_\beta$ is unchanged and its inverse temperature is rescaled.
\item Hence no automorphism intertwining the flow carries $\omega_\beta$ to $\omega_{\beta'}$ for $|\beta'| \neq |\beta|$: $|\beta|$ is an invariant of the pair (state, parametrised flow), and the automorphism group acts on the line of KMS states with orbits $\{\beta, -\beta\}$, so that line carries no automorphism-theoretic structure beyond the orientation flip of (2). A condition that singles out one point of the line is therefore either a stipulation of the state itself or a reference to data outside the pair $(\Aa, \alpha)$; by (3), the value of $|\beta|$ is meaningful only relative to a parametrisation of the flow, and it is that parametrisation, the conversion of the flow parameter into geometric time, that the algebra does not supply.
\end{enumerate}

*Proof.* Every automorphism of a matrix factor is inner, $\theta = \operatorname{Ad}(U)$. (1) Commutation gives $Ue^{itK}U^{*} = c(t)e^{itK}$ with $|c(t)| = 1$; taking determinants, $c(t)^{2} = 1$, and $c$ is continuous with $c(0) = 1$, so $c \equiv 1$ and $U$ commutes with $K$. As $K = \operatorname{diag}(-\tfrac12, \tfrac12)$ is nondegenerate, $U$ is diagonal and $\operatorname{Ad}(U)$ fixes every diagonal matrix, in particular $e^{-\beta K}/Z$. (2) Flow reversal gives $UKU^{*} = -K$, so $U$ exchanges the spectral projectors of $K$ and $Ue^{-\beta K}U^{*} = e^{+\beta K}$. (3) The reparametrised flow is $\operatorname{Ad}(e^{it(cK)})$, generated by $cK$, and by Theorem \claimref{singularity.kms-uniqueness-factor} its $\beta'$-KMS state is $e^{-\beta' cK}/Z$, which equals $e^{-\beta K}/Z$ exactly when $\beta' = \beta/c$. (4) By Theorem \claimref{singularity.kms-uniqueness-factor} the KMS states are exactly the Gibbs states, and an automorphism intertwining the flow either commutes with it or reverses it (it conjugates $K$ to $\pm K$ up to a constant, the spectrum $\{-\tfrac12, \tfrac12\}$ of $K$ leaving no other option), so by (1) and (2) it acts on the parameter through $\{\pm 1\}$ only. That is the whole mathematical content of the clause; the sentence about what a selecting condition must refer to is its reading, and clause (3) is the reason the reading is exact: $\beta$ is the ratio of the state's modular parameter to the flow's parameter, and the second of these is a choice the algebra does not make. The script verifies clauses (1) to (3) on rational data.


Passing from single modes to the whole boundary algebra gives the state we are after.

**Theorem 36 (The I-state).** Consider the boundary-mode algebra with its boost dynamics (Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics}) at inverse temperature $\beta = 1/\TH = 2\pi/\kappa$.
\begin{enumerate}
\item \emph{(Existence, exactly on windows.)} The quasi-free state $\omega_I$ with the Fermi-Dirac symbol
\[
A_I \;=\; \bigl(1 + e^{\beta h}\bigr)^{-1}, \qquad\text{i.e.}\qquad n_j = \frac{1}{e^{\omega_j/\TH} + 1},
\]
restricts on every window to the Gibbs state of $H_F = \sum_{j \in F}\omega_j N_j$ and is KMS there, exactly (Lemma \claimref{hawking.gibbs-states-are-kms-conversely-finite}); it is the unique quasi-free extension of these window states, and it is $\tau$-KMS at $\beta$ on the full algebra by Fact \claimref{hawking.imported-kms-passes-inductive-limits}.
\item \emph{(Gauge invariance is forced.)} If a quasi-free state of $\mathfrak{A}$ is $\tau$-KMS at $\beta$, its pairing vanishes: the state is gauge-invariant automatically.
\item \emph{(The symbol is derived.)} Its symbol then satisfies the operator identity $A(1 + e^{-\beta h}) = e^{-\beta h}$, equivalently $A = e^{-\beta h}(1 - A)$, whence $A = A_I$: within the quasi-free class, the state whose modular clock is the geometry's clock is unique, and its two-point data are forced.
\end{enumerate}

*Proof.* (1) On a window $F$, the quasi-free state with diagonal symbol is the product state of Fact \claimref{hawking.imported-quasi-free-states-car-algebra} with $n_j = (1 + e^{\beta\omega_j})^{-1}$, which is exactly the Gibbs density matrix of $H_F$: $e^{-\beta H_F} = \bigotimes_j \mathrm{diag}(1, e^{-\beta\omega_j})$, normalised; the script builds the two sides independently and confirms the identity in exact arithmetic. Lemma \claimref{hawking.gibbs-states-are-kms-conversely-finite} gives the KMS identity on the window, exactly; the script verifies it on a three-mode window at rational Boltzmann factors, on a spanning set of pairs. The windows are nested with dense union and the dynamics preserves each, so Fact \claimref{hawking.imported-kms-passes-inductive-limits} passes the KMS property to $\mathfrak{A}$.
(2) Apply the KMS identity to the pair $x = a^\dagger(f)$, $y = a^\dagger(g)$, with $f, g$ supported in windows (so that $\alpha_{i\beta}(a^\dagger(f)) = a^\dagger(e^{-\beta h}f)$ is again a generator):
\[
P(f, g) \;=\; \omega\bigl(a^\dagger(f)\,a^\dagger(g)\bigr) \;=\; \omega\bigl(a^\dagger(g)\,a^\dagger(e^{-\beta h}f)\bigr) \;=\; P(g,\, e^{-\beta h}f).
\]
Antisymmetry of creation operators gives $P(f, g) = -P(g, f)$, so $P(g, (1 + e^{-\beta h})f) = 0$ for all $f, g$ in the dense span of the windows; $1 + e^{-\beta h}$ is bounded with bounded inverse and preserves that span, so $P = 0$.
(3) Apply the KMS identity to the pair $x = a^\dagger(f)$, $y = a(g)$:
\[
\omega\bigl(a^\dagger(f)\,a(g)\bigr) \;=\; \omega\bigl(a(g)\,a^\dagger(e^{-\beta h}f)\bigr)
\;=\; \ip{g}{e^{-\beta h}f} - \omega\bigl(a^\dagger(e^{-\beta h}f)\,a(g)\bigr),
\]
using the CAR $\{a(g), a^\dagger(f')\} = \ip{g}{f'}$. In symbols: $\ip{g}{Af} = \ip{g}{e^{-\beta h}f} - \ip{g}{Ae^{-\beta h}f}$ for all $f, g$ supported in windows, i.e.\ $A(1 + e^{-\beta h}) = e^{-\beta h}$ on the dense span, i.e.\ $A = e^{-\beta h}(1+e^{-\beta h})^{-1} = (1 + e^{\beta h})^{-1} = A_I$ (all four operators bounded, $h \ge 0$ here). By (2) and Fact \claimref{hawking.imported-quasi-free-states-car-algebra}, the state is determined by its two-point data, which are forced, so $\omega = \omega_I$. The mode-diagonal scalar identity $n = e^{-\beta\omega}(1-n)$, equivalently the detailed balance $n/(1-n) = e^{-\beta\omega}$, is checked by the script as an exact identity of rational functions.


We then pass from the fermion modes to their bosonic currents.

**Theorem 37 (The bosonisation bridge, s-wave sector).** Let $\{\psi_k, \psi^\dagger_k\}_{k \in \mathbb{Z}}$ be the boundary modes, as fermion operators on the filled-sea Fock space (the infinite filled-sea array whose algebraic model is the completed tower limit of \cite[Thm.~5.6]{ButlerT3}, cited for the structure; its provenance here is the s-wave aggregation declared above, not a tower, the mod-8 clock having stopped after one ascent), and define the currents $a_m := \sum_k :\psi^\dagger_k\,\psi_{k+m}:$ with $:\;:$ normal ordering at the sea level; with the sea filled below the level, $a_m$ annihilates the sea for $m > 0$ and $a_{-m} = a_m^{\dagger}$ creates particle-hole pairs. (The opposite index convention flips the sign of the central term; the verification script fixes the convention by computation.) Then:
\begin{enumerate}
\item (Current algebra.) $[a_m, a_n] = m\,\delta_{m+n,0}\,\id$ on the infinite array; on a finite window the commutator equals $m\,\delta_{m+n,0}\,\id$ plus an \emph{exactly identified} edge operator ($B_m - T_m - m$ in the proof's notation), supported on the bottom and top $m$ sites and vanishing on all bulk states: the number-conserving bilinears satisfy the canonical commutation relations of a free boson. A boson is a pair of the pair.
\item (KMS restriction.) Each bilinear $\psi^\dagger_k\psi_{k+m}$ carries a definite boost weight, fixed by the difference $\omega_{k+m} - \omega_k$ of its two modes' weights. Under (Q)'s weight clause, $\omega_k = \kappa k$, that difference is $\kappa m$ for every $k$, so each current $a_m$ is itself a weight vector and the current subalgebra is globally invariant under the modular flow of Theorem \claimref{singularity.modular-structure-completed-pair}; for weights that are not affine in $k$ the summands of $a_m$ rotate at different rates and the span of the currents need not be invariant, so this invariance uses (Q). Under (Q) the joint state is KMS for that flow, and a KMS state restricted to a flow-invariant subalgebra is KMS at the same temperature for the restricted flow. Without (Q) no joint KMS state is available: (R) is imposed on the marginals alone, and Theorem \claimref{singularity.exact-equilibrium-over-determines-boundary-modes} is the reason its joint form is rejected elsewhere in the chain.
\item (The Planck factor.) Under (Q), with the marginal occupancies $n_k = (e^{\beta\omega_k} + 1)^{-1} = (e^{\beta\kappa k} + 1)^{-1}$ at the premise's linear weights, the current occupancy is, exactly,
\[
\langle a_{-m} a_m \rangle \;=\; \sum_{k \in \mathbb{Z}} n_{k+m}\,(1 - n_k) \;=\; \frac{m}{e^{\beta\kappa m} - 1} \qquad (m > 0) ,
\]
with no vacuum piece in this convention ($a_m$ annihilates the sea): Bose-Einstein occupancy at exactly $\TH$. The Planck spectrum of the bosonic Hawking flux is derived, not conjectured, for the s-wave sector, in the equilibrium reading (Q) fixes; for a general member of the chain's state class the left side acquires the connected correlators (Q) sets to zero, and no exact spectrum is claimed.
\end{enumerate}
The single assembly-level ingredient in the section is the charge-zero Fock isomorphism (the charge-zero sector of the fermionic Fock space is canonically the bosonic Fock space, with fermions recovered as vertex operators), cited to \cite{PressleySegal1986} and used only for the completeness statement that the two descriptions are one algebra; parts (1)-(3) are proved outright.

*Proof.* (1) \emph{Finite window first, exactly.} On the window $W = \{-K, \dots, K-1\}$ set $a_m = \sum_{k \in S_m} \psi^\dagger_k \psi_{k+m}$ with $S_m = \{k : k, k+m \in W\}$; normal-ordering constants are scalars and drop out of every commutator, so they play no role here. The CAR give, for single bilinears,
\[
[\psi^\dagger_k \psi_{k+m},\; \psi^\dagger_l \psi_{l+n}] = \delta_{k+m,\,l}\,\psi^\dagger_k\psi_{l+n} - \delta_{l+n,\,k}\,\psi^\dagger_l\psi_{k+m} .
\]
For $n = -m$ ($m > 0$), summing over $k \in S_m$ and $l \in S_{-m}$ and writing $N_j = \psi^\dagger_j\psi_j$:
\[
[a_m, a_{-m}] \;=\; \sum_{k \in S_m} \bigl(N_k - N_{k+m}\bigr)
\;=\; \underbrace{\sum_{j=-K}^{-K+m-1} N_j}_{=:\,B_m} \;-\; \underbrace{\sum_{j=K-m}^{K-1} N_j}_{=:\,T_m} ,
\]
an \emph{exact operator identity}: the interior terms cancel in the telescoping sum and only the bottom and top $m$ sites survive. On any state that agrees with the filled sea on those edge sites, $B_m = m$ and $T_m = 0$, so $[a_m, a_{-m}] = m\,\id$ there; the edge operators are the entire finite-size correction, and they vanish on bulk states at every window size, not merely asymptotically. For $m + n \neq 0$ the same computation cancels all interior terms against each other and leaves an edge-supported remainder, zero on bulk states. The infinite array (modelled on the tower limit of \cite[Thm.~5.6]{ButlerT3}) has no edges, and the identities hold outright.

(2) A bilinear $\psi^\dagger_k\psi_{k+m}$ is an eigenvector of the modular flow with definite weight (both factors carry definite weight by Theorem \claimref{singularity.modular-structure-completed-pair}(2)), and its weight is fixed by the difference $\omega_{k+m} - \omega_k$. The current $a_m$ sums these bilinears over $k$, so it is an eigenvector exactly when that difference does not depend on $k$, that is when the weights are affine in $k$. This is where the weight clause of (Q, \claimref{singularity.q-joint-quasi-freeness-s-wave}) enters: with $\omega_k = \kappa k$ the difference is $\kappa m$ for every $k$, each $a_m$ is a weight vector, and the linear span of the currents is invariant. For weights not affine in $k$ the summands of $a_m$ rotate at different rates and the span need not be invariant. The restriction statement is definitional: if $(\omega, \sigma_t)$ is KMS at $\beta$ on an algebra and $A$ is a globally invariant subalgebra, the correlation functions of elements of $A$, their analytic continuations, and the KMS boundary identity are computed in $A$ exactly as in the ambient algebra.

(3) Under (Q, \claimref{singularity.q-joint-quasi-freeness-s-wave}), Wick's theorem gives $\langle a_{-m} a_m\rangle = \sum_{k} n_{k+m}(1 - n_k)$: the four-point functions factorise because (Q) sets every connected part to zero, which is exactly what a general member of the chain's state class denies. With the present convention the sum needs no vacuum subtraction: at $\beta \to \infty$ the summand $\mathbf{1}[k + m < 0]\,\mathbf{1}[k \geq 0]$ is empty for $m > 0$, consistent with $a_m$ annihilating the sea. Write $x := e^{-\beta\kappa} \in (0,1)$, $n_k = x^k/(1 + x^k)$, and
\[
g(k) := n_{k+m}(1 - n_k) = \frac{x^{k+m}}{(1 + x^{k+m})(1 + x^k)} \;\geq 0.
\]
The two-sided series $S := \sum_{k \in \mathbb{Z}} g(k)$ converges absolutely: $g(k) \leq x^{k+m}$ for $k \geq 0$ and $g(k) \leq x^{-k}$ for $k \leq -m$ (bound each Fermi factor by $1$ and the other by its numerator). Two exact pointwise identities finish the computation. \emph{Detailed balance:} $n_k(1 - n_{k+m}) = x^{-m}\, g(k)$, read off from the displayed formula by exchanging which factor keeps its numerator. \emph{Difference identity:} $g(k) - n_k(1 - n_{k+m}) = n_{k+m} - n_k$, by expanding both sides over the common denominator. Summing the difference identity over $\mathbb{Z}$ (all three series converge absolutely) and evaluating the telescoping middle sum by its partial sums,
\[
\sum_{k=-K}^{K} (n_{k+m} - n_k) \;=\; \sum_{j=K+1}^{K+m} n_j \;-\; \sum_{j=-K}^{-K+m-1} n_j \;\xrightarrow[K \to \infty]{}\; 0 - m = -m ,
\]
since $n_j \to 0$ as $j \to +\infty$ and $n_j \to 1$ as $j \to -\infty$. Therefore $S - x^{-m} S = -m$, i.e.
\[
S \;=\; \frac{m}{x^{-m} - 1} \;=\; \frac{m\,x^m}{1 - x^m} \;=\; \frac{m}{e^{\beta\kappa m} - 1} ,
\]
which is the assertion: Bose-Einstein occupancy, exactly, with the detailed-balance relation supplying the physical content. The deposited script verifies the two pointwise identities, the re-indexing, and the value against exact rational tail bounds; and, for (Q)'s role, that the Planck summand is the exact expectation $\langle n_{k+m}(1 - n_k)\rangle$ on the product member of the class while a correlated member with the same marginals shifts it by exactly the connected correlator.


We recall what is known about that bosonic sector, separating what holds unconditionally from what rests on the joint premise.

**Theorem 38 (Imported: the s-wave bosonic sector).** Two halves, at two levels. \emph{Unconditional:} on a window of the boundary mode space, the number-conserving bilinears (currents) satisfy the free-boson commutation relations exactly in the completed limit, with an exact finite-window operator identity whose deviation is a difference of edge operators; and the bilinear subalgebra is globally invariant under the modular boost. \emph{Conditional on T5's Premise (Q), joint quasi-freeness with the s-wave weights:} the restriction of the Fermi-Dirac KMS state to the bilinear subalgebra is KMS at the same temperature (an instance of Lemma \claimref{hawking.kms-restricts-invariant-subalgebras} below), giving the Bose-Einstein occupancy at $\TH$ for the s-wave sector; the linear weight assignment is the s-wave reduction's convention, adopted there as part of the premise. \emph{Provenance:} T5 \cite[Prem.~8.1, Thm.~8.2]{ButlerT5}; the correspondence itself is classical \cite{FrenkelKac1980}. The exact edge identity is reproved, in the form this paper needs, as Proposition \claimref{hawking.current-commutator-exactly-edge-split} below.

*Proof.* Two halves, at two levels. \emph{Unconditional:} on a window of the boundary mode space, the number-conserving bilinears (currents) satisfy the free-boson commutation relations exactly in the completed limit, with an exact finite-window operator identity whose deviation is a difference of edge operators; and the bilinear subalgebra is globally invariant under the modular boost. \emph{Conditional on T5's Premise (Q) (\claimref{singularity.q-joint-quasi-freeness-s-wave}), joint quasi-freeness with the s-wave weights:} the restriction of the Fermi-Dirac KMS state to the bilinear subalgebra is KMS at the same temperature (an instance of Lemma \claimref{hawking.kms-restricts-invariant-subalgebras} below), giving the Bose-Einstein occupancy at $\TH$ for the s-wave sector; the linear weight assignment is the s-wave reduction's convention, adopted there as part of the premise. \emph{Provenance:} T5 \cite[Prem.~8.1, Thm.~8.2]{ButlerT5} (\claimref{singularity.bosonisation-bridge-s-wave-sector}); the correspondence itself is classical \cite{FrenkelKac1980}. The exact edge identity is reproved, in the form this paper needs, as Proposition \claimref{hawking.current-commutator-exactly-edge-split} below.

This restates \claimref{hawking.imported-s-wave-bosonic-sector-external}.


The final result makes the bosonic occupancy exact and bounds the correction on a finite window.

**Theorem 39 (Bose-Einstein occupancy, with quantified window corrections).** Let the ladder carry the linear s-wave weight assignment (the convention T5's Premise (Q) adopts, a modelling input here as there; Fact \claimref{hawking.imported-s-wave-bosonic-sector}): level spacing $\epsilon$, sea at level $0$, I-state occupancies $n_k = (x^{-k} + 1)^{-1}$ with $x = e^{-\beta\epsilon} \in (0,1)$ the Boltzmann factor of the level spacing. Then:
\begin{enumerate}
\item \emph{(Detailed-balance identity.)} For every $k$ and $m \ge 1$, exactly,
\[
n_k - n_{k+m} \;=\; \bigl(x^{-m} - 1\bigr)\; n_{k+m}\,\bigl(1 - n_k\bigr).
\]
\item \emph{(The Planck factor, exactly, in the bilateral limit.)} Summing (1) over $k \in \Z$,
\[
\sum_{k \in \Z} n_{k+m}\,(1 - n_k) \;=\; \frac{m}{x^{-m} - 1} \;=\; \frac{m}{e^{\beta\epsilon m} - 1}:
\]
the current two-point function $\langle a_m^\dagger a_m\rangle_I = \sum_k n_{k+m}(1 - n_k)$ (a Wick computation) is exactly $m$ times the Bose-Einstein value at $\TH$, with no vacuum correction in this normalisation. The factor $m$ is the free-boson normalisation: on the bilateral ladder the currents are used only inside expectations, and $\langle [a_m, a_m^\dagger]\rangle_I = \sum_k (n_k - n_{k+m}) = m$, the telescoped left side of (1), matching the finite-window scalar of Proposition \claimref{hawking.current-commutator-exactly-edge-split}; the unit-normalised boson is $\hat a_m = a_m/\sqrt{m}$, whose occupancy $\langle \hat a_m^\dagger \hat a_m\rangle_I = 1/(e^{\beta\epsilon m} - 1)$ is the $n_-$ of the lift.
\item \emph{(Window tails.)} For the window $[-K, K]$ with the sea at the centre, i.e.\ the sum of (2) restricted to $k \in [-K, K-m]$ (both mode indices inside the window), the bilateral sum exceeds the window sum by a positive amount bounded by $2m\,x^{K - m}/(1 - x)$: exponentially small in the distance from the sea to the edges, in units of the level spacing.
\end{enumerate}

*Proof.* (1) With $u := x^{-k}$ and $w := x^{-m}$ (the I-state occupancies of \claimref{hawking.i-state} on the linear s-wave weights of \claimref{hawking.imported-s-wave-bosonic-sector}): $n_k - n_{k+m} = \tfrac{1}{u+1} - \tfrac{1}{uw+1} = \tfrac{u(w-1)}{(u+1)(uw+1)}$, and $(w-1)\,n_{k+m}(1-n_k) = (w-1)\cdot\tfrac{1}{uw+1}\cdot\tfrac{u}{u+1}$: identical. The script checks it as an identity of rational functions in the formal variable $u$ at several rational $w$.
(2) The terms $n_{k+m}(1 - n_k)$ decay like $x^{|k|}$ in both directions, so all sums converge absolutely and may be regrouped. Fix a residue class $k = r + jm$, $j \in \Z$: the class sum of the left side of (1) is $\lim_{j_0 \to \infty}\sum_{j=-j_0}^{j_0}\bigl(n_{r+jm} - n_{r+(j+1)m}\bigr) = \lim_{j_0 \to \infty}\bigl(n_{r-j_0 m} - n_{r+(j_0+1)m}\bigr) = 1 - 0$, the interior terms cancelling in adjacent pairs; there are $m$ residue classes, and dividing by $(x^{-m}-1)$ via (1) gives the display. The Wick computation: in the gauge-invariant quasi-free state, $\langle \psi^\dagger_{l+m}\psi_l\,\psi^\dagger_k\psi_{k+m}\rangle$ has vanishing disconnected part for $m \ge 1$ (the two-point function is mode-diagonal) and connected part $\delta_{kl}\,n_{k+m}(1 - n_k)$.
(3) Bound each term two ways, both valid for every integer index: $n_{k+m}(1-n_k) \le n_{k+m} \le x^{k+m}$ and $n_{k+m}(1-n_k) \le 1 - n_k \le x^{-k}$, since $n_j \le x^j$ and $1 - n_j \le x^{-j}$ are each the statement $1 \le 1 + x^{\pm j}$. The terms missing from the window sum are those with $k > K - m$ or $k < -K$, all positive, so the difference is positive and at most
\[
\sum_{k > K-m} x^{k+m} + \sum_{k < -K} x^{-k} \;=\; \frac{2\,x^{K+1}}{1-x} \;\le\; \frac{2m\,x^{K-m}}{1-x}.
\]
The script verifies instances of the bound exactly, and checks that the window sums at $K = 30$ and $K = 40$ agree with the closed form to within the proven tails, all in exact rational arithmetic.


## Results cited, not shown

**Fact (imported) 40 (Imported: KMS passes to inductive limits).** Let a C*-algebra be the closure of an increasing union of subalgebras, each globally invariant under a one-parameter dynamics, and let a state be KMS at $\beta$ on each subalgebra for the restricted dynamics. Then the state is KMS at $\beta$ on the whole algebra: the analytic-element requirement is checked on the dense union and passes to the closure. \emph{Provenance:} \cite[Prop.~5.3.25]{BratteliRobinson1997}.

*Provenance:* O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., Prop.~5.3.25.

**Fact (imported) 41 (Imported: quasi-free states of the CAR algebra).** For every operator $A$ on $\ell^2(J)$ with $0 \le A \le 1$ (the \emph{symbol}) there is a unique gauge-invariant state $\omega_A$ on $\mathfrak{A}$ with two-point function $\omega_A(a^\dagger(f)\,a(g)) = \ip{g}{Af}$ and all higher truncated functions zero (Wick determinants). More generally, a quasi-free state (all truncated functions beyond second order vanishing) is determined by its full two-point data, the symbol together with the pairing $P(f, g) := \omega(a^\dagger(f)\,a^\dagger(g))$, and gauge invariance is exactly $P = 0$. On a finite window with diagonal symbol this is the explicit product state $\bigotimes_j \rho_j$, $\rho_j = \mathrm{diag}(1 - n_j,\, n_j)$ in the occupation basis, which the script realises exactly. \emph{Provenance:} Araki \cite{Araki1971}; \cite[\S 5.2]{BratteliRobinson1997}.

*Provenance:* H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. RIMS Kyoto Univ. 6 (1971), 385--442.; O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., \S 5.2.

**Fact (imported) 42 (Imported: the s-wave bosonic sector (external ingredients)).** The results from outside the series on which \claimref{hawking.imported-s-wave-bosonic-sector} draws, as cited there: I. B. Frenkel and V. G. Kac, Basic representations of affine Lie algebras and dual resonance models, Invent. Math. 62 (1980), 23--66.

*Provenance:* I. B. Frenkel and V. G. Kac, Basic representations of affine Lie algebras and dual resonance models, Invent. Math. 62 (1980), 23--66..

**Fact (imported) 43 (Imported: equivalence with the Einstein equations).** On any region where $\hb$ is invertible, the GTG field equations for $(\hb, \Omega)$ are equivalent to the Einstein field equations for the metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$; in vacuum, to Ricci-flatness of $g$. \emph{Provenance:} Lasenby, Doran and Gull \cite[\S 4.3 and App.~C]{LDG1998}; textbook form \cite[Ch.~13-14]{DoranLasenby2003}.

*Provenance:* A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans. R. Soc. Lond. A 356 (1998), 487--582., \S 4 (\S 4.3, covariant forms of the field equations), App.~C; C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003)., Ch.~13-14.

**Fact (imported) 44 (Imported: the tractor connection).** Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) on its invertible region. The tractor bundle $\mathcal{T}$ of the conformal class $[g]$, trivialised in the scale $g$ by $\nInf$, the physical vectors and $\nO$ (the vectors $\sigma\nInf + \mu + \rho\nO$ of $\Cl(2,4)$), carries a canonical connection depending only on $[g]$, preserving the metric $\ip{(\sigma,\mu,\rho)}{(\sigma,\mu,\rho)} \;=\; g(\mu,\mu) \,+\, 2\sigma\rho$, whose expression in the scale $g$ is
\begin{equation}
\nabla_a(\sigma, \mu_b, \rho) \;=\; \bigl(\nabla_a\sigma - \mu_a,\;\; \nabla_a\mu_b + g_{ab}\,\rho - \Sch_{ab}\,\sigma,\;\; \nabla_a\rho + \Sch_a{}^{b}\mu_b\bigr),
\end{equation}
where $\nabla_a$ on $\mu$ is the covariant derivative $D$ of the gravitational field in the physical frame and $\Sch_{ab}$ is the Schouten tensor of $g$, the components of the Schouten map $\Sch(A) = \tfrac12\bigl(\mathcal{R}(A) - \tfrac16 A\,\mathcal{R}\bigr)$ of the field strength; in four dimensions $\Sch_{ab} = \tfrac12\bigl(\Ric_{ab} - \tfrac{R}{6}\,g_{ab}\bigr)$. \emph{Provenance:} Bailey-Eastwood-Gover \cite{BEG1994}; Curry-Gover \cite[\S 5]{CurryGover2018}. The display \claimref{interior.imported-tractor-connection} is their connection written in the curvature conventions of the section ``Setting and conventions''; the relative sign of the Schouten slots against those references is convention-dependent, and Lemma \claimref{interior.sign-fixed-internally} fixes it internally, so that no sign in this paper rests on a translation between conventions.

*Provenance:* T. N. Bailey, M. G. Eastwood and A. R. Gover, Thomas's structure bundle for conformal, projective and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217.; S. N. Curry and A. R. Gover, An introduction to conformal geometry and tractor calculus, with a view towards analysis on manifolds, in Asymptotic Analysis in General Relativity, London Mathematical Society Lecture Note Series 443, Cambridge University Press (2018), 86--170., \S 5.

**Fact (imported) 45 (The centre).** For $n \geq 1$, the centre of $\Cl(p,q)$ is $\R \cdot 1$ if $n$ is even, and $\R \cdot 1 \oplus \R \cdot \omega$ if $n$ is odd, where $\omega = e_1 e_2 \cdots e_n$ is the pseudoscalar.

*Provenance:* Transport Lab claim primer.centre, version 2 (T00 Lem 9.4).

**Fact (imported) 46 (Classification of the real Clifford algebras).** Let $d \equiv p - q \pmod 8$. Then $\Cl(p,q)$ is isomorphic, as a real associative algebra, to the entry of the table of the section ``The mod-8 classification'': $\Mat_k(\R)$ for $d \in \{0, 2\}$, $\Mat_k(\C)$ for $d \in \{3, 7\}$, $\Mat_k(\HH)$ for $d \in \{4, 6\}$, $\Mat_k(\R) \oplus \Mat_k(\R)$ for $d = 1$, and $\Mat_k(\HH) \oplus \Mat_k(\HH)$ for $d = 5$, with $k$ fixed in each case by $\dim_\R \Cl(p,q) = 2^n$. In particular $\Cl(p,q)$ is simple except when $p - q \equiv 1 \pmod 4$, where it is the direct sum of two isomorphic simple algebras.

*Provenance:* Transport Lab claim primer.classification-real-clifford-algebras, version 3 (T00 Thm 9.3).

**Fact (imported) 47 (Localised transport).** The subalgebra of $\shC$ generated by $T^*M$ is canonically isomorphic to $\shA$, globally, including over $\Sig$, because $h$ restricted to $T^*M$ equals $G$ identically by construction. Over $\Mo \cap \Mp$ the inclusion $\shA \subset \shC$ is fibrewise the conformal embedding $\Cl(p,q) \subset \Cl(p{+}1,q{+}1)$ of Rule 1 \cite{ButlerT1}. Over $\Sig$ the very same elements change ideal-theoretic character: a radical covector $k$ satisfies $k^2 = 0$ in both algebras, but the two-sided ideal it generates is square-zero in $A(x)$ (Theorem \claimref{sheaf.degeneration-sheaf}) and is the whole algebra in $C(x)$ (Proposition \claimref{sheaf.resolution-ideal-theoretically}), where $k$ acquires a partner $k^*$ built from the coupling, with $kk^* + k^*k = 1$ and $(k^*)^2 = 0$. The completion does not modify the degenerate algebra; it re-embeds it where its infinitesimals cease to be infinitesimal. In particular the localised ladder pair $(k, k^*)$ exists exactly over $\Sig$: the CAR structure of the series' operator-algebraic reading is supported on the singular locus.

*Provenance:* Transport Lab claim sheaf.localised-transport, version 5 (T04 Cor 4.5).

**Fact (imported) 48 (One-sided completion).** Assume (T1)-(T3), with signature $(p,q)$, $p \geq 1$, on the physical side $\Mp$, and assume the radical line bundle is trivial, $w_1(\shL) = 0$, so that collar data exist. Then there exists a smooth symmetric form $h$ on $T$ over $M$, equal to $G \perp H$ outside a collar of $\Sig$, which is nondegenerate of constant signature $(p{+}1, q{+}1)$ at every point of $\Mp$, including $\Sig$ itself. Consequently $\shC := \Cl(T, h)$ restricted to $\Mp$ is a locally free sheaf of algebras of constant rank $2^{n+2}$ whose every fibre is isomorphic to $\Cl(p{+}1, q{+}1)$; in the physical case, $\Cl(2,4) \cong \Mat_4(\HH)$.

*Provenance:* Transport Lab claim sheaf.one-sided-completion, version 4 (T04 Thm 4.4).

**Fact (imported) 49 (One-sided completion at the singularity).** Adjoin the trivial hyperbolic plane $(\nO, \nInf)$ to $\shW$ and couple it to the dying direction by the construction of Definition \claimref{obj.sheaf.collar-data-coupling}, taking the normalised transversal $u = \partial_t/m$ (so that $k(u) = 1$, as the definition requires), coupling constants satisfying $\mu\nu < 0$, and bump supported inside the horizon. Then the ambient form $h$ is nondegenerate of constant signature $(2,4)$ at every point of $\Mt$, the boundary $E$ included; the subalgebra generated by $\shW$ is canonically the degeneration sheaf; and the ladder pair
\[
k^* = \frac{\nO}{2\nu}, \qquad k k^* + k^* k = 1, \qquad k^2 = (k^*)^2 = 0
\]
exists exactly over $E$. The ascent $\Cl(1,3) \to \Cl(2,4)$, i.e.\ $\Mat_2(\HH) \to \Mat_4(\HH)$, is thereby performed at the Schwarzschild singularity, localised on $E \cong \R \times S^2$. Moreover no shadow wall forms anywhere in the manifold.

*Provenance:* Transport Lab claim sheaf.one-sided-completion-singularity, version 4 (T04 Thm 8.12).

**Fact (imported) 50 (The Schwarzschild degeneration is boundary-tame in $\shW$).** On the frame $(\rho, \dtPG, \mu_1, \mu_2)$ of $\shW$, the derived cometric $G(a,b) = \hb^{T}(a) \cdot \hb^{T}(b)$ of the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$ of Fact \claimref{sheaf.gauge-field-cometric} (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) has Gram matrix
\[
G(r) \;=\;
\begin{pmatrix}
m^2 - r & -m & 0 & 0\\
-m & 1 & 0 & 0\\
0 & 0 & -1 & 0\\
0 & 0 & 0 & -1
\end{pmatrix},
\]
with entries polynomial in $r$, hence extending smoothly to $E$. Moreover:
\begin{enumerate}
\item (nondegeneracy off the wall) $\det G = -r$, so $G$ is nondegenerate of signature $(1,3)$ at every $r > 0$, the horizon included;
\item (corank one) at $E$ the Gram has rank exactly three; the radical is the line spanned by
\[
k \;=\; \rho + m\,\dtPG ,
\]
and the $G$-orthogonal complement $V_1 = \langle \rho, \mu_1, \mu_2\rangle$ is nondegenerate, carrying the form $\mathrm{diag}(m^2, -1, -1)$ of signature $(1,2)$;
\item (first-order degeneration) $g_k := G(k,k) = -r$ \emph{exactly}, at every radius: the dying eigenvalue vanishes to precisely first order in the defining function $r$, with transversality datum $\delta(k \otimes k) = -\,dr|_E$, a nowhere-zero section of the $r$-conormal line $N^*_rE$ (Conventions);
\item (gauge robustness) the same module and the same radical are obtained from the Schwarzschild coordinate frame: the transition $\dtS = \dtPG + \tfrac{m}{m^2 - r}\rho$ is a smooth invertible change of $\shW$-frame at $E$, it diagonalises $G$, and $k = m\,\dtS + \tfrac{r}{r - m^2}\rho$, so that on $E$ the radical line is spanned by the Killing-time covector $\dtS$;
\item (the rain identity) $k = d\Phi$ with $\Phi = m t + \tfrac23 r^{3/2}$, and $k$ annihilates the infalling free-fall congruence (worldlines of $D$-parallel velocity) along the background direction $\partial_t - \beta\,\partial_r$ at \emph{every} radius: the dying direction is the conormal to the foliation ruled by the rain.
\end{enumerate}

*Provenance:* Transport Lab claim sheaf.schwarzschild-degeneration-boundary-tame, version 6 (T04 Thm 8.7).

**Fact (imported) 51 (Imported: equivalence with the Einstein equations).** On any region where $\hb$ is invertible, the GTG field equations $\mathcal{R}(a) - \tfrac12\, a\, \mathcal{R} \;=\; 8\pi\, T(a), \qquad D \wedge \hb(a) \;=\; \hb(\nabla \wedge a)$ for $(\hb, \Omega)$ are equivalent to the Einstein field equations for the metric $g(a,b) \;=\; \hb^{-1}(a) \cdot \hb^{-1}(b)$; in vacuum, to Ricci-flatness of $g$. Moreover the curvatures correspond, not only the equations: on the invertible region the GTG curvature bivector $\mathcal{R}(B)$, evaluated on the coordinate planes $g_\mu \wedge g_\nu$ of the frame $g_\mu = \hb^{-1}(e_\mu)$ and contracted with the reciprocal planes, reproduces the Riemann tensor $R_{\mu\nu}{}^{\rho\sigma}$ of $g$, so the curvature operator on bivectors, its spectrum, its eigenplanes and its scalar invariants are the same objects in the two pictures. \emph{Provenance:} Lasenby, Doran and Gull \cite[\S 4.3 and App.~C]{LDG1998}; textbook form, including the dictionary between $\mathcal{R}(B)$ and the Riemann tensor, \cite[Ch.~13-14]{DoranLasenby2003}. It is the second clause that licenses the assembly of Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}'s spectrum from the two formalisms.

*Provenance:* A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans. R. Soc. Lond. A 356 (1998), 487--582., \S 4 (\S 4.3, covariant forms of the field equations), App.~C; C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003)., Ch.~13-14.

**Fact (imported) 52 (Imported: surface gravity as redshifted acceleration).** Let $(\hb, \Omega)$ be a static gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with a static Killing horizon: a Killing field $K$, a physical vector field whose covariant derivative $A \mapsto A \cdot D K$ is antisymmetric in the flat product, and a locus of the background on which $Q(K) = 0$ and $K$ is normal to it. The surface gravity defined on the horizon locus by $(K \cdot D)K = \kappa\,K$ equals the limit, at the horizon locus, of the proper acceleration of static observers (velocity $v = K/\sqrt{Q(K)}$, acceleration $(v \cdot D)v$) multiplied by the redshift factor $\sqrt{Q(K)}$; $Q(K)$ is the derived-metric norm $g(\xi,\xi)$ of the Killing vector $\xi$ over which $K$ sits (Fact \claimref{synthesis.imported-gtg-dictionary}, clause (vi)). \emph{Provenance:} R.~M.~Wald, General Relativity, University of Chicago Press (1984), \S 12.5, read in Gauge Theory Gravity through the dictionary.

*Provenance:* R. M. Wald, General Relativity, University of Chicago Press (1984), §12.5.

**Fact (imported) 53 (The blade basis, degenerate forms included).** Let $e_1, \dots, e_n$ be any basis of $V$. The $2^{n}$ ordered products $e_I = e_{i_1} e_{i_2} \cdots e_{i_k}$, for $I = \{i_1 < \dots < i_k\} \subseteq \{1, \dots, n\}$ (with $e_{\emptyset} = 1$), form a basis of $\Cl(V, Q)$. Hence $\dim \Cl(V, Q) = 2^{n}$, the map $\iota : V \to \Cl(V, Q)$ is injective, and $\Cl(V, Q) \ne 0$. This holds for every real quadratic space, degenerate or not.

*Provenance:* Transport Lab claim std-algebra.blade-basis, version 1.

**Fact (imported) 54 (Cl(1,1) and Cl(2,0) are the real 2x2 matrices).** The Clifford algebra of any hyperbolic plane $H$ is isomorphic to $\Mat_2(\R)$: if $(u, w)$ is a hyperbolic pair spanning $H$, the assignment
\begin{equation}
u \mapsto \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad w \mapsto \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}
\end{equation}
extends to an isomorphism $\Cl(H) \to \Mat_2(\R)$, under which $uw$ and $wu$ are the complementary idempotents $\operatorname{diag}(1, 0)$ and $\operatorname{diag}(0, 1)$. In particular $\Cl(1,1) \cong \Mat_2(\R)$. Also $\Cl(2,0) \cong \Mat_2(\R)$, by $e_1 \mapsto \operatorname{diag}(1, -1)$, $e_2 \mapsto \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$.

*Provenance:* Transport Lab claim std-algebra.cl11-matrix, version 1.

**Fact (imported) 55 (The Clifford algebra exists and is unique).** For every real quadratic space $(V, Q)$ a Clifford algebra exists: $\Cl(V, Q) = T(V) / I_Q$, the tensor algebra modulo the two-sided ideal generated by $\{v \otimes v - Q(v)\,1 : v \in V\}$, with $\iota$ the inclusion of $V = T^{1}(V)$ followed by the quotient map. Any two Clifford algebras of $(V, Q)$ are isomorphic by a unique isomorphism compatible with the maps from $V$. Concretely, for any real symmetric Gram matrix $G$ on $\R^{n}$ (degenerate allowed), the operators $c(v) = v \wedge {} + \, \iota_{Gv}$ on the exterior algebra $\Lambda \R^{n}$ satisfy $c(v)^{2} = Q(v)$, and so give a representation $\Cl(V, Q) \to \operatorname{End} \Lambda V$. (That this representation is faithful is shown afterwards, in the blade basis result, by the triangularity of $x \mapsto x \cdot 1$.)

*Provenance:* Transport Lab claim std-algebra.existence-uniqueness, version 1.

**Fact (imported) 56 (An algebra and its matrix amplification).** Let $A$ be a unital real algebra and $m \ge 1$, and let $E_{ij}$ be the matrix units of $\Mat_m(A)$. Then:
\begin{enumerate}
\item[(i)] the centre of $\Mat_m(A)$ is $\{z \cdot 1_m : z \in \Zc(A)\}$;
\item[(ii)] the two-sided ideals of $\Mat_m(A)$ are exactly the $\Mat_m(I)$ with $I$ a two-sided ideal of $A$;
\item[(iii)] $M \mapsto M^{m}$ (columns, acted on by matrix multiplication) and $N \mapsto E_{11} N$ are mutually inverse equivalences between left $A$-modules and left $\Mat_m(A)$-modules, so $A$ and $\Mat_m(A)$ are Morita equivalent.
\end{enumerate}
With \claimref{std-algebra.matrix-units}: an algebra with a full $m \times m$ system of matrix units has the centre, the ideals and the modules of its corner.

*Provenance:* Transport Lab claim std-algebra.morita-amplification, version 1.

**Fact (imported) 57 (Orthogonal vectors anticommute).** For $u, v \in V$: $u v = -v u$ if and only if $B(u, v) = 0$. In an orthogonal basis $e_1, \dots, e_n$, $e_i e_j = -e_j e_i$ for $i \ne j$ and $e_i^{2} = Q(e_i)$, and the product of two basis blades is $e_I e_J = \pm \bigl(\prod_{i \in I \cap J} Q(e_i)\bigr)\, e_{I \triangle J}$, the sign being $(-1)$ to the number of pairs $(i, j) \in I \times J$ with $i > j$.

*Provenance:* Transport Lab claim std-algebra.orthogonal-anticommute, version 1.

**Fact (imported) 58 (How the pseudoscalar commutes).** In $\Cl(p, q, r)$, $n = p + q + r$, with unit pseudoscalar $I$:
\begin{enumerate}
\item[(i)] $I X_k = (-1)^{k(n-1)} X_k I$ for $X_k \in \Cl^{k}$; so $I$ commutes with $\Cl^{+}$, and with $\Cl^{-}$ when $n$ is odd, while it anticommutes with $\Cl^{-}$ when $n$ is even. Equivalently $I X = X I$ for $n$ odd and $I X = \hat{X} I$ for $n$ even.
\item[(ii)] $I \tilde{I} = \prod_{i} Q(e_i)$, which is $(-1)^{q}$ when $r = 0$ and $0$ when $r > 0$.
\item[(iii)] $I^{2} = (-1)^{n(n-1)/2} (-1)^{q}$ when $r = 0$ (\claimref{primer.sign}), and $I^{2} = 0$ when $r > 0$: in a degenerate algebra the pseudoscalar is nilpotent.
\end{enumerate}

*Provenance:* Transport Lab claim std-algebra.pseudoscalar-commutation, version 1.

**Fact (imported) 59 (The spacetime algebra as a matrix algebra, and the spacetime split).** (i) $\Cl(1,3) \cong \Mat_2(\HH)$: with quaternion units $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$, the assignment $\gamma_0 \mapsto \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$, $\gamma_k \mapsto \begin{psmallmatrix} 0 & \mathbf{q}_k \\ \mathbf{q}_k & 0 \end{psmallmatrix}$ extends to an isomorphism. (ii) As a labelled reading, the Dirac matrices $\gamma^{D}_0 = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$, $\gamma^{D}_k = \begin{psmallmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{psmallmatrix}$ ($2 \times 2$ blocks) give a faithful representation $\Cl(1,3) \to \Mat_4(\C)$ whose complex span is all of $\Mat_4(\C)$: $\C \otimes \Cl(1,3) \cong \Mat_4(\C)$. (iii) The relative vectors $\sigma_k = \gamma_k \gamma_0$ satisfy $\sigma_j \sigma_k + \sigma_k \sigma_j = 2\delta_{jk}$ and $\sigma_1 \sigma_2 \sigma_3 = I$, and generate the even subalgebra: $\Cl^{+}(1,3) \cong \Cl(3,0)$, so the spacetime pseudoscalar is the pseudoscalar of the observer's space.

*Provenance:* Transport Lab claim std-algebra.sta-matrix, version 1.

**Fact (imported) 60 (The product of two vectors).** In $\Cl(V, Q)$, for all $u, v \in V$,
\begin{equation}
v^{2} = Q(v), \qquad u v + v u = 2 B(u, v).
\end{equation}
In particular $u v = B(u, v) + \tfrac12(u v - v u)$, the sum of a scalar and an antisymmetric part.

*Provenance:* Transport Lab claim std-algebra.vector-squares, version 1.

**Fact (imported) 61 (Null pairs satisfy the canonical anticommutation relations).** Let $v_1, \dots, v_k, w_1, \dots, w_k \in V$ be a \emph{Witt basis} of their span: $B(v_i, v_j) = B(w_i, w_j) = 0$ and $B(v_i, w_j) = \tfrac12 \delta_{ij}$. Then in $\Cl(V, Q)$
\begin{equation}
v_i v_j + v_j v_i = 0, \qquad w_i w_j + w_j w_i = 0, \qquad v_i w_j + w_j v_i = \delta_{ij},
\end{equation}
the canonical anticommutation relations for $k$ modes (read $v_i$ as annihilators, $w_i$ as creators). The elements $N_i = w_i v_i$ are mutually commuting idempotents with $N_i + v_i w_i = 1$. In particular, for orthogonal hyperbolic planes $\operatorname{span}(e_i, e_{k+i})$ of $\R^{k,k}$, $v_i = \tfrac12(e_i + e_{k+i})$ and $w_i = \tfrac12(e_i - e_{k+i})$ form such a basis. The form need not be nondegenerate outside the span.

*Provenance:* Transport Lab claim std-algebra.witt-basis-car, version 1.

**Fact (imported) 62 (Hyperbolic pairs and the Witt decomposition).** Let $(V, Q)$ be a real quadratic space of signature $(p, q, r)$ and let $m = \min(p, q)$.
\begin{enumerate}
\item[(i)] If $P \subseteq V$ is a nondegenerate plane and $u \in P$ is a nonzero null vector, there is a unique $w \in P$ such that $(u, w)$ is a hyperbolic pair; $P$ is a hyperbolic plane.
\item[(ii)] (Witt decomposition) There is an orthogonal decomposition
\begin{equation}
V = H_1 \perp \dots \perp H_m \perp A \perp \operatorname{rad} V
\end{equation}
with each $H_i$ a hyperbolic plane and $A$ anisotropic ($Q(a) \ne 0$ for $a \ne 0$, hence definite, of signature $(p - m, q - m, 0)$).
\item[(iii)] If $(u_i, w_i)$ is a hyperbolic pair spanning $H_i$, then $N = \operatorname{span}(u_1, \dots, u_m) \oplus \operatorname{rad} V$ is a maximal totally null subspace, and every totally null subspace has dimension at most $m + r$.
\end{enumerate}

*Provenance:* Transport Lab claim std-algebra.witt-decomposition, version 1.

**Fact (imported) 63 (Morita equivalence of an algebra and its amplification).** For any unital ring $A$ and $m \geq 1$, the column module $A^m$ is a $\Mat_m(A)$-$A$-bimodule implementing an equivalence of module categories: $A$ and $\Mat_m(A)$ are Morita equivalent. \emph{Provenance:} classical Morita theory, \cite[\S\S 17--18]{Lam1999}.

*Provenance:* T. Y. Lam, Lectures on Modules and Rings, Graduate Texts in Mathematics 189, Springer, New York (1999)., \S\S 17--18.

**Fact (imported) 64 (Existence and classification of type C).** $\Cl(p,q)$ ($n \geq 1$) contains a nontrivial central idempotent if and only if
\[
p - q \equiv 1 \pmod 4 ,
\]
and in that case the nontrivial central idempotents are exactly the two elements
\[
\varepsilon_\pm = \tfrac12\,(1 \pm \omega),
\]
which are exchanged by the grade involution $\hat{\cdot}$ (an \emph{outer} automorphism of the split algebra; no inner automorphism exchanges them, centrality being conjugation-invariant), and satisfy $\varepsilon_+ \varepsilon_- = 0$ and $\varepsilon_+ + \varepsilon_- = 1$, and effect the splitting $\Cl(p,q) = \varepsilon_+ A \,\oplus\, \varepsilon_- A$ into the two simple ideals of Theorem \claimref{transport.classification-real-clifford-algebras}.

*Provenance:* Transport Lab claim transport.existence-classification-type-c, version 4 (T01 Thm 3.6).

**Fact (imported) 65 (Existence locus of type N).** $\Cl(p,q)$ contains a null vector if and only if the signature is mixed, $pq \neq 0$. In that case the null vectors form a cone of dimension $n - 1$, and every null vector is a two-sided zero divisor without left or right inverse in any unital algebra containing $\Cl(p,q)$.

*Provenance:* Transport Lab claim transport.existence-locus-type-n, version 5 (T01 Prop 3.3).

**Fact (imported) 66 (Rule 1 is Morita-trivial).** The elements
\[
E_{11} = ff^*, \qquad E_{22} = f^*f, \qquad E_{12} = f, \qquad E_{21} = f^*
\]
form a full $2 \times 2$ system of matrix units in $B$ ($E_{11} + E_{22} = 1$, $E_{ij}E_{kl} = \delta_{jk}E_{il}$); the corner is the base, $E_{11} B E_{11} = A\,ff^* \cong A$ via $a \mapsto a\,ff^*$; and therefore
\[
\Cl(p{+}1, q{+}1) \;\cong\; \Mat_2\bigl(\Cl(p,q)\bigr),
\]
under which the ascent embedding $A \hookrightarrow B$ becomes the twisted diagonal $a \mapsto \mathrm{diag}(a, \hat{a})$. In particular Rule 1 preserves the Morita class: the Wedderburn type, and with it the simplicity or splitness and the type-C diagnosis of the section ``A taxonomy of obstructions'', are the same for $B$ as for $A$, and the clock residue $d = p - q \pmod 8$ is fixed. (The \emph{presence} of types N and P is not preserved and could not be: Proposition \claimref{transport.no-transport-terminates} below shows every completion carries fresh obstructions of its own.) The adjoined ladder pair is, in the matrix description, exactly the off-diagonal matrix units, and the descent projectors $f^*f,\, ff^*$ are the diagonal ones.

*Provenance:* Transport Lab claim transport.rule-1-morita-trivial, version 5 (T01 Thm 7.1).

**Fact (imported) 67 (Type P is self-repairing).** Let $A$ be any unital ring, $\mathcal{E}(A)$ its set of idempotents, and $A' \supseteq A$ any unital extension. The identity assignment
\[
\sigma : \mathcal{E}(A) \to A' , \qquad \sigma(e) = e,
\]
satisfies both von Neumann identities, $e\,\sigma(e)\,e = e$ and $\sigma(e)\,e\,\sigma(e) = \sigma(e)$, and is equivariant under \emph{every} ring automorphism of every extension: for any automorphism $\theta$ of $A'$ preserving $A$, $\sigma(\theta(e)) = \theta(\sigma(e))$ trivially. In the terminology of the taxonomy: the transport rule for type P is the identity, at signature increment $(0,0)$, and the repair is already present in the base algebra.

*Provenance:* Transport Lab claim transport.type-p-self-repairing, version 2 (T01 Prop 6.1).

**Prediction 68 (The no-echo prediction, registered).** The framework's quantum structure lies at the stretched singularity, $r_c = (2M)^{1/3}$ in Planck units, by Postulate \claimref{singularity.c1-curvature-cutoff} (C1): deep inside the hole, at Planck curvature, and nowhere near the horizon, which remains exactly the smooth vacuum horizon of classical general relativity (the exterior dictionary is exact, \cite[Fact 2.1]{ButlerT6}). The registered prediction: post-merger ringdown is the Kerr quasinormal spectrum of general relativity with \emph{no} modification, and in particular no echo train at the Planck-structure delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$ (the delay at which near-horizon structure at Planck distance would reflect \cite{CardosoPani2017}), of order tens to hundreds of milliseconds for stellar-mass remnants ($35$ ms at $10\,M_\odot$, $0.1$ to $0.25$ s for remnants of $30$ to $70\,M_\odot$): within the sensitivity band of existing detectors. A single statistically confirmed echo train would refute the framework's localisation of quantum structure. The prediction is stated so that it can fail.

Every floor of the tower shares the ground floor's charge, centre and obstruction taxonomy, so the tower changes nothing structural. What it adds is exactly one vector-realised fermionic mode at each rung. At the centre of the black hole the degeneration is a property of the solution, not of its presentation. It is an obstruction of type N, so the repair is the completion that supplies the missing partner. Coming back down from the completion costs exactly a relative entropy. The curvature fixes the rate, so that $2\pi$ of rapidity corresponds to $8\pi M$ of Schwarzschild time. Under (P) and (R) every mode's marginal is the Gibbs state at the Hawking temperature, with no condition on the joint state. The I-state is the unique quasi-free state that is KMS for the boost dynamics at that temperature. Under the linear s-wave weight assignment its current modes carry exactly the Bose-Einstein occupancy on the bilateral ladder. Because the quantum structure sits deep inside the hole, the framework registers that post-merger ringdown is the unmodified Kerr quasinormal spectrum, with no echo train. What we assume is set out in a short list of premises. Univalence (P) requires every physical state of the boundary modes to be even under the grading, so odd elements have zero expectation value. Regularity (R) requires each single-mode marginal to be KMS for the Killing flow at the period $2\pi/\kappa$ dictated by smoothness of the Euclidean section. Joint quasi-freeness (Q) takes the joint state, in the stationary idealisation, to be the quasi-free state with those marginals, and assigns the mode weights $\omega_k = \kappa k$. The bosonic reading of the boundary currents rests on (Q), and without it no joint KMS state is available. The value of the temperature is meaningful only relative to a parametrisation of the flow, which the algebra does not supply.
