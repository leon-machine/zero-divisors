# The Matter in the Dark Towers: Companion note to T14: what each tower is made of, built by the Standard-Model paper's construction in geometric algebra (regenerated from the store)

**Abstract.** The dark-matter paper T14 fixes how much matter each of five dark towers holds, not what that matter is. This note builds it with the Standard-Model paper's construction, in geometric algebra. A constituent is an element of the spin-irreducible even ideal of the tower's conformal algebra, and its scalars are the commutant of the spin action there. We prove that this field is the division algebra of the next residue: the reals in the three-dimensional towers, the complex numbers in this tower and the mirror, the quaternions in the five-dimensional towers. One identity of the reversion pairing then says where mass begins (two constituents in three and four dimensions, one in five); the momentum-preserving mixings are the field's unitary groups; and, under the series' identification premise and one transposition rule, the gauge algebras follow. The mirror carries the Standard Model again. Both three-dimensional towers carry the abelian $\so(2) \oplus \so(2)$: two copies of single-flavour electrodynamics in $2+1$ dimensions. Both five-dimensional towers carry $\uu(3)$, dark colour and one abelian charge, with vector-like quarks, leptons and a neutral singlet; with an external imaginary unit both would carry the Standard-Model algebra instead. The towers of each odd dimension differ only in discrete structure. Three consequences follow. The equal-mass premise of the unit-ball rule has no mechanism in any odd tower. A cold mirror is an unstated exception to T14's indifference premise. No configuration of the towers as built passes the cluster, radiation and mirror bounds together. The algebraic results are verified in exact arithmetic.

## What we assume

**Postulate 1 (P3: nearest-dimension representatives).** Each tower is represented at the dimension nearest four; where two are equally near (the odd residues, three and five), the lower one with a single time, else the higher. \emph{Support:} P1's one metric read as minimality. Structural premise; Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}(iii) records the other windows.

**Postulate 2 (R1: equal mass per quantum).** The quanta of every populated tower carry the same mass $m$.

**Postulate 3 (R2: one quantum per unit ball).** A populated tower whose space has $D$ dimensions ($2$, $3$ or $4$) holds one quantum per unit ball $\B^{D}$ of that space, in one unit of length common to all towers: every tower has the same Wigner-Seitz radius. The rule presupposes that all six towers are populated, which for the odd four is the inference of Observation \claimref{dark-matter.which-towers-are-populated}.

**Postulate 4 (R3: one cell per unshared direction).** In the sourcing rule, a tower's matter counts through exactly one cell radius of each direction its neighbour lacks, on one side: a five-dimensional tower's matter through one radius of its extra direction, and a three-dimensional tower's sheets stacked one radius apart along the direction it lacks. the section ``The thickness: a contact mechanism'' gives a mechanism that returns this value and costs it.

**Postulate 5 (Premise H1: a constituent's momentum).** A constituent has a spinor part $\psi$ in the tower's spinor ideal $S$ (Definition \claimref{obj.dark-tower-matter.ideals-fields-momentum}), carried by a map $T \to S$ that intertwines the action of the tower's spin group, so that the field of $T$ acts on $S$ through it; its momentum is the vector part of $\psi e_{t}\rev{\psi}$. In dimension four this is T12's Fact 2.1 in the even algebra; in dimensions three and five it is a premise.

**Postulate 6 (Premise H2: gauge algebras as hierarchy automorphisms).** The gauge algebra of a tower's matter is the automorphism algebra of its minimal massive hierarchy, constituent slots tensor pair slots, as T12's Theorem 4.1 identifies it in dimension four, at observation level \cite[Thm.~4.1, Prop.~4.3]{ButlerT12}.

**Postulate 7 (Hypothesis (S) carried to every tower).** The constituent slots are fermionic modes on the same footing as the pairs, so that the composite's state space is the exterior algebra of slot and pair modes \cite[Sec.~5]{ButlerT12}. Used only where stated.

**Postulate 8 (Premise U: the transposition rule).** (U1) A constituent is an element of the spin-irreducible even ideal of the conformal algebra, as T12 defines this tower's, and its field is the commutant of the spin action on it. (U2) The hierarchy's first factor counts constituents at mass onset, and its slot group is the momentum-preserving group of that many constituents; the pair group is the group of mixings of the ladder pairs that preserves their canonical relations and the field's positive norm, the unitary group over the pairs' scalars ($\R$, or $\C$ where a complex unit builds the pairs), as T12 takes $U(m) \times U(k)$ \cite[Thm.~4.1]{ButlerT12}. (U3) Every complex unit used to build a ladder pair is an element of the constituent's field that the real algebra supplies; no external imaginary unit is adjoined.

## Introduction



**setting  (Introduction).** The dark-matter paper T14 \cite{ButlerT14} derives eight parallel towers, one per residue $r = p - q \bmod 8$ of the real Clifford algebras, and finds that six can hold matter: this one ($r = 6$, signature $(1,3)$), its mirror ($r = 2$, $(3,1)$), two three-dimensional towers ($r = 1, 7$) and two five-dimensional towers ($r = 3, 5$). The towers touch only through the one shared metric. By its unit-ball rule the five dark towers hold, relative to our baryons, the shares $1$, $4/3$, $4/3$, $8/(3\pi)$ and $8/(3\pi)$, whose sum $(11\pi + 16)/(3\pi) = 5.364$ is the observed ratio of dark to visible matter. T14 proves the mirror a copy of this tower; for the four odd towers it says how much matter each holds and leaves open what that matter is.

This note answers that question by doing in each tower what the Standard-Model paper T12 \cite{ButlerT12} does in ours. T12's chain is: a constituent; the number of constituents at which mass begins; the mixings that preserve total momentum; the automorphisms of the smallest massive composite, identified with the gauge algebra; the content and its charges; then, with imported physics, hadrons, atoms and a stable relic. Every link is transposed here, and where the transposition meets an obstacle the resolution is taken from the way our tower resolves the same obstacle.

Everything is written in geometric algebra. A constituent is an element of a minimal left ideal of an even Clifford algebra; its momentum is the vector part of $\psi e_{t} \rev{\psi}$; its field of scalars is the corner algebra $f \Cl^{0} f$ with the adjoint $x^{\dagger} = e_{t}\rev{x}e_{t}^{-1}$. The mass laws are identities of the reversion pairing $\rev{\psi}_{1}\psi_{2}$.

**setting  (Prior art).** The real Clifford algebras, their periodicity and their spinor modules are classical (Cartan, Chevalley \cite{Chevalley1954}, Lounesto \cite{Lounesto2001}); the even-subalgebra isomorphisms $\Cl^{0}(p,q) \cong \Cl(p,q-1)$ and $\Cl^{0}(p,q) \cong \Cl^{0}(q,p)$ are standard \cite{Porteous1995, Lounesto2001}, and the division algebra of each even algebra can be read off the periodicity table. The spacetime-algebra current $j = \psi\gamma_{0}\rev{\psi}$ and its square $j^{2} = |\psi\rev{\psi}|^{2}$ are Hestenes's \cite{Hestenes1966, DoranLasenby2003}. Mirror matter and its cosmology have a long literature \cite{FootMirror2004, RouxCline2020}; the parity anomaly and topologically massive gauge fields in $2+1$ dimensions are Redlich's and Deser, Jackiw and Templeton's \cite{Redlich1984, DJT1982}; Polyakov confinement \cite{Polyakov1977}; five-dimensional gauge theory, its Chern-Simons terms and its strong-coupling scale are standard \cite{IMS1997, CLP2000}. The identification of a gauge algebra with the automorphisms of the minimal massive composite is T12's, and its global form and content are classical structure theory once that identification is made.

**setting  (Contribution).** \begin{enumerate}
\item The constituent's field in tower $r$ is the division algebra of residue $r + 1$, at the conformal and the tower level alike (Theorem \claimref{dark-tower-matter.constituents-field}, a corollary of the periodicity table): $\R$, $\C$, $\HH$ as the causal tower's dimension runs three, four, five. It is not the type T14 assigns by residue, which is the commutant of a different module (Remark \claimref{note.dark-tower-matter.t14s-types-are-different-commutant}).
\item One identity of the reversion pairing gives where mass begins: at two constituents in three and four dimensions, where the pairing is alternating, and at one in five, where it is not (Theorem \claimref{dark-tower-matter.where-mass-begins}). The momentum-preserving mixings are $O(n)$, $U(n)$, $Sp(n)$ (Theorem \claimref{dark-tower-matter.ladder}).
\item The third ladder pair of the five-dimensional towers needs a complex unit. At $r = 3$ the algebra supplies one, and every other quaternionic unit fails to commute with the pair structure; at $r = 5$ the units form a sphere (Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions}).
\item Under T12's identification premise and one transposition rule (Premise \claimref{dark-tower-matter.u-transposition-rule}): $\so(2) \oplus \so(2)$ in both three-dimensional towers, $\uu(3)$ in both five-dimensional towers ($\su(2) \oplus \su(3) \oplus \uu(1)$ in both if the pair unit is external), the Standard Model in the mirror (Theorem \claimref{dark-tower-matter.gauge-algebras} and, for the mirror, T14's copy theorem), with the content of Propositions \claimref{dark-tower-matter.three-dimensional-content} and \claimref{dark-tower-matter.five-dimensional-content}.
\item The towers of each odd dimension hold the same kind of matter (Corollary \claimref{dark-tower-matter.same-kind-matter}); the mirror's even algebras are this tower's under an explicit real isomorphism, which reverses the conformal pseudoscalar (Theorem \claimref{dark-tower-matter.mirror-algebra}).
\item The physics: the matter of each tower in halos (the section ``From content to matter''); the equal-mass premise R1 has no mechanism in the odd towers (Proposition \claimref{dark-tower-matter.r1-has-no-mechanism-odd-towers}); a cold mirror is an exception to P2 (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}); and the towers as built against the data (Observation \claimref{dark-tower-matter.towers-built}).
\end{enumerate}

the table accompanying \claimref{dark-tower-matter.imported-towers-their-types} and a figure of the original collect the result.

\centering  
\begin{tabular}{@{}llllll@{}}
\toprule
$r$ & tower & field & gauge algebra & elementary matter & in halos \\
\midrule
$6$ & $(1,3)$, ours & $\C$ & $\su(3) \oplus \su(2) \oplus \uu(1)$ & quarks, leptons & atoms, stars \\
$2$ & $(3,1)$, mirror & $\C$ & the same & a copy & dissipative gas \\
$1$ & $(2,1)$, sheets & $\R$ & $\so(2) \oplus \so(2)$ & cells $A$, $B$ & collisionless in one phase \\
$7$ & $(1,2)$, sheets & $\R$ & $\so(2) \oplus \so(2)$ & cells $A$, $B$ & collisionless in one phase \\
$3$ & $(4,1)$ & $\HH$ & $\uu(3)$\,$^{*}$ & $U, D, E, N$, vector-like & free fermions \\
$5$ & $(1,4)$ & $\HH$ & $\uu(3)$\,$^{*}$ & $U, D, E, N$, vector-like & free fermions \\
$0$ & $(2,2)$ & $\R$ & $\sll(2,\R) \oplus \sll(3,\R) \oplus \gl(1,\R)$ & none (no stable vacuum) & none \\
$4$ & $(4,0)$, $(0,4)$ & $\HH$ & (no time) & none & none \\
\bottomrule
\end{tabular}

\emph{The eight towers' matter. Fields: Theorem \claimref{dark-tower-matter.constituents-field}. Gauge algebras: Theorem \claimref{dark-tower-matter.gauge-algebras}, under H2 and Premise \claimref{dark-tower-matter.u-transposition-rule}; $^{*}$with an external pair unit, $\su(2) \oplus \su(3) \oplus \uu(1)$ in both (Remark \claimref{note.dark-tower-matter.branches-break-u-what-they-give}); $r = 0$: Remark \claimref{note.dark-tower-matter.kleinian-algebra}. Content: Propositions \claimref{dark-tower-matter.three-dimensional-content}, \claimref{dark-tower-matter.five-dimensional-content}. In halos: the section ``From content to matter''.}

## Setting, imports and premises



**setting  (Setting, imports and premises).** Throughout, a tower is $V = \R^{p,q}$ with an orthonormal basis $\{e_{a}\}$, $Q(e_{a}) = e_{a}^{2} = \pm 1$, and $\Cl(V) = \Cl(p,q)$ its Clifford algebra, with even subalgebra $\Cl^{0}(V)$, reversion $x \mapsto \rev{x}$, grade involution $x \mapsto \hat{x}$ and grade projection $\ip{\cdot}_{k}$. In a causal signature ($\min(p,q) = 1$) the \emph{time direction} $e_{t}$ is the one basis vector of the minority sign, as in T14's convention \cite[Prop.~3.1]{ButlerT14}, and $Q(e_{t}) = \pm 1$ accordingly. The tower's conformal algebra is $\Cl(\hatV)$ with $\hatV = V \oplus \R^{1,1}$, that is $\Cl(p+1, q+1)$. The pseudoscalar of an algebra of dimension $n$ is $\omega = e_{1}e_{2}\cdots e_{n}$, central when $n$ is odd, with $Q(\omega) = (-1)^{n(n-1)/2}(-1)^{q}$.

The objects that the twistor paper T9 \cite{ButlerT9} and T12 describe in twistor language are, here, the even ideals of the conformal algebra and their elements; this note uses only the latter.



**Theorem 9 (Imported: the towers and their residues).** The residue $r = p - q \bmod 8$ is constant along each tower of $(1,1)$ ascents. Under T14's Premise P3 the representatives are $(1,3)$ at $r = 6$, $(3,1)$ at $r = 2$, $(2,1)$ and $(1,2)$ at $r = 1, 7$, $(4,1)$ and $(1,4)$ at $r = 3, 5$, $(2,2)$ at $r = 0$ and $(4,0)$ or $(0,4)$ at $r = 4$; $r = 0$ and $r = 4$ are sterile. The odd residues carry no orientation bit and therefore no asymmetry. The towers interact only through the one metric (exact superselection). Sources: \cite[Prop.~3.1, Thm.~3.4, Thm.~3.10, Prop.~4.1]{ButlerT14}, \cite[Thm.~3.6]{ButlerT3}.

*Proof.* The residue $r = p - q \bmod 8$ is constant along each tower of $(1,1)$ ascents. Under T14's Premise P3 (\claimref{dark-matter.p3-nearest-dimension-representatives}) the representatives are $(1,3)$ at $r = 6$, $(3,1)$ at $r = 2$, $(2,1)$ and $(1,2)$ at $r = 1, 7$, $(4,1)$ and $(1,4)$ at $r = 3, 5$, $(2,2)$ at $r = 0$ and $(4,0)$ or $(0,4)$ at $r = 4$; $r = 0$ and $r = 4$ are sterile. The odd residues carry no orientation bit and therefore no asymmetry. The towers interact only through the one metric (exact superselection). Sources: \cite[Prop.~3.1, Thm.~3.4, Thm.~3.10, Prop.~4.1]{ButlerT14} (\claimref{dark-matter.superselected-hence-dark-exactly-stable}, \claimref{dark-matter.flag-bit-exists-exactly-tower-dimension}, \claimref{dark-matter.towers-are-residues-single-clock-filter}, \claimref{dark-matter.type-residue-what-each-tower-can}), \cite[Thm.~3.6]{ButlerT3} (\claimref{tower.rigidity-clock-frozen}).




**Fact (imported) 10 (Imported: the structure of real Clifford algebras).** (i) For $q \geq 1$, $\Cl^{0}(p,q) \cong \Cl(p,q-1)$, by $e_{a} \mapsto e_{a}e_{n}$ with $Q(e_{n}) = -1$; for $p \geq 1$, $\Cl^{0}(p,q) \cong \Cl(q, p-1)$. (ii) $\Cl(p,q)$ is a matrix algebra over $D \in \{\R, \C, \HH\}$, or a sum of two, with $D$ fixed by $p - q \bmod 8$: $\R$ at $0, 1, 2$; $\C$ at $3, 7$; $\HH$ at $4, 5, 6$. (iii) A minimal left ideal $Af$ of a simple or semisimple algebra $A$, $f$ a primitive idempotent, has commutant $\mathrm{End}_{A}(Af) \cong (fAf)^{\mathrm{op}}$, a division algebra (Schur), acting by right multiplication. Sources: \cite{Chevalley1954, Lounesto2001, LawsonMichelsohn1989}.

*Provenance:* C. Chevalley, The Algebraic Theory of Spinors, Columbia University Press (1954).; P. Lounesto, Clifford Algebras and Spinors, 2nd ed., Cambridge University Press (2001).; H. B. Lawson and M.-L. Michelsohn, Spin Geometry, Princeton University Press (1989)..



**Theorem 11 (Imported: our tower's Standard-Model chain).** In this tower: a single constituent has null momentum and two have the squared mass of T11's two-constituent formula \cite[Prop.~4.1]{ButlerT11}, \cite[Fact~2.1]{ButlerT12}; each constituent carries three ladder pairs \cite[Fact~2.2, Lem.~2.12]{ButlerT12}, the tower's rungs satisfying the canonical anticommutation relations \cite[Prop.~4.1]{ButlerT3}; the mixings of $n$ constituents preserving their total momentum and helicity form are $U(n)$ \cite[Prop.~3.1]{ButlerT12}; and the content, hypercharges, anomalies and Higgs representation are \cite[Thm.~4.1, Thm.~4.2, Prop.~5.3, Thm.~5.5, Prop.~9.22]{ButlerT12}.

*Proof.* In this tower: a single constituent has null momentum and two have the squared mass of T11's two-constituent formula \cite[Prop.~4.1]{ButlerT11} (\claimref{mass.mass-symplectic-area-two-twistor-formula}), \cite[Fact~2.1]{ButlerT12}; each constituent carries three ladder pairs \cite[Fact~2.2, Lem.~2.12]{ButlerT12} (\claimref{standard-model.pair-count-dimension}, \claimref{standard-model.imported-pair-systems-two-chirality-halves}), the tower's rungs satisfying the canonical anticommutation relations \cite[Prop.~4.1]{ButlerT3} (\claimref{tower.ladder-pairs-satisfy-car-vectors}); the mixings of $n$ constituents preserving their total momentum and helicity form are $U(n)$ \cite[Prop.~3.1]{ButlerT12} (\claimref{standard-model.internal-symmetry-ladder}); and the content, hypercharges, anomalies and Higgs representation are \cite[Thm.~4.1, Thm.~4.2, Prop.~5.3, Thm.~5.5, Prop.~9.22]{ButlerT12} (\claimref{standard-model.quarks-leptons-two-level-fermion-content}, \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}, \claimref{standard-model.global-form-quotient-determined}, \claimref{standard-model.ten-transported-ambient-space-doublets-are}, \claimref{standard-model.gauge-algebra-minimal-massive-composite}).




**Theorem 12 (Imported: the unit-ball shares).** T14's premises R1 (every quantum of every populated tower has the same mass $m$, numerically the nucleon's), R2 (one quantum per unit ball of each tower's own space, with a common Wigner-Seitz radius $d_{b}$) and R3 (a three-dimensional tower's sheets stacked one cell radius apart; a five-dimensional tower's matter counted through one radius of its extra direction) give shares $1$, $2 \times 4/3$, $2 \times 8/(3\pi)$ and the total $(11\pi + 16)/(3\pi)$ \cite[Prem.~7.2 to 7.4, Prop.~7.6]{ButlerT14}. As fractions of the dark matter: mirror $18.6$ percent, each three-dimensional tower $24.9$, each five-dimensional tower $15.8$.

*Proof.* T14's premises R1 (\claimref{dark-matter.r1-equal-mass-per-quantum}) (every quantum of every populated tower has the same mass $m$, numerically the nucleon's), R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball}) (one quantum per unit ball of each tower's own space, with a common Wigner-Seitz radius $d_{b}$) and R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}) (a three-dimensional tower's sheets stacked one cell radius apart; a five-dimensional tower's matter counted through one radius of its extra direction) give shares $1$, $2 \times 4/3$, $2 \times 8/(3\pi)$ and the total $(11\pi + 16)/(3\pi)$ \cite[Prem.~7.2 to 7.4, Prop.~7.6]{ButlerT14} (\claimref{dark-matter.unit-ball-rule}). As fractions of the dark matter: mirror $18.6$ percent, each three-dimensional tower $24.9$, each five-dimensional tower $15.8$.




**Fact (imported) 13 (Imported: the cluster merger simulations).** In the idealised Bullet-like merger runs of T14b \cite[Obs.~7.1, Table~3]{ButlerT14b}: (i) with only the mirror colliding ($18.6$ percent of the dark matter, as gas) the subcluster keeps a separate lensing peak on its galaxies and a mass-to-light change of $0.82$ against the observed $0.84 \pm 0.07$; (ii) with the mirror gas and one three-dimensional tower's share of colliding fluid ($43.5$ percent colliding) the subcluster dissolves, and with more it dissolves too; (iii) with the mirror collisionless and $24.9$ or $31.6$ percent of colliding fluid, the subcluster keeps a weaker peak but only $0.55$ or $0.44$ of its central mass: the colliding fluid alone costs about half of it. In (i) the subcluster's own mass is $0.57$ of the cold-dark-matter run's, but mass and light leave together and the mass-to-light change, the quantity the observational bound is inferred from, is consistent. No run lies between $18.6$ and $24.9$ percent colliding. The colliding components there are fluids.

*Provenance:* L. Butler, Simulating the Dark Towers: Methods, Assumptions and Tests of the Unit-Ball Composition, Transport Papers T14b (2026), Obs. 7.1, Table 3.

**setting  (Setting, imports and premises).** Four statements are carried as premises. H1 and H2 are this paper's names for two of T12's ingredients used off dimension four; Hypothesis (S) is T12's; U is this paper's transposition rule.

## Constituents, momentum and where mass begins





**Definition 14 (Ideals, fields and momentum).** Let $\hf$ be a primitive idempotent of $\Cl^{0}(\hatV)$, and in a causal tower let $f = \tfrac{1}{2}(1 + e_{t}e_{a})$ for a space direction $e_{a}$, which is a primitive idempotent of $\Cl^{0}(V)$ in dimensions three to five (Theorem \claimref{dark-tower-matter.constituents-field}); in the sterile towers $f$ is any primitive idempotent of $\Cl^{0}(V)$. The \emph{constituent ideal} is $T = \Cl^{0}(\hatV)\hf$ and the \emph{spinor ideal} is $S = \Cl^{0}(V)f$. Their \emph{fields} are the commutants $\F(T) = \mathrm{End}_{\Cl^{0}(\hatV)}(T)$ and $\F(S) = \mathrm{End}_{\Cl^{0}(V)}(S)$, the latter realised as right multiplication by the corner algebra $f\Cl^{0}(V)f$. In a causal tower the \emph{adjoint} is $x^{\dagger} = e_{t}\rev{x}e_{t}^{-1}$, and the \emph{momentum} of $\psi \in S$ is
\[
j(\psi) \;=\; \ip{\psi e_{t} \rev{\psi}}_{1}.
\]
The total momentum of constituents $\psi_{1}, \ldots, \psi_{n}$ is $P = \sum_{i} j(\psi_{i})$, and its \emph{squared mass} is $m^{2} = Q(e_{t})\,Q(P)$.

**setting  (Constituents, momentum and where mass begins).** The constructions are explicit: $e_{t}e_{a}$ squares to $+1$, and $\Cl^{0}(V)f$ has real dimension $2$, $4$, $8$ in dimensions three, four, five, which is minimal (Theorem \claimref{dark-tower-matter.constituents-field}); $\hf$ is a product of two or three commuting factors $\tfrac{1}{2}(1 + b)$ with $b$ an even blade of square $+1$. The script builds both by a search over commuting even blades (Part A).



**Theorem 15 (The constituent's field in each tower).** In tower $r$ the fields $\F(T)$ and $\F(S)$ are equal, and equal to the division algebra of residue $r + 1$:
\begin{center}\small
\begin{tabular}{@{}lccccccccc@{}}
\toprule
$r$ & $6$ & $2$ & $1$ & $7$ & $3$ & $5$ & $0$ & $4$ \\
tower & $(1,3)$ & $(3,1)$ & $(2,1)$ & $(1,2)$ & $(4,1)$ & $(1,4)$ & $(2,2)$ & $(4,0)$, $(0,4)$ \\
conformal & $(2,4)$ & $(4,2)$ & $(3,2)$ & $(2,3)$ & $(5,2)$ & $(2,5)$ & $(3,3)$ & $(5,1)$, $(1,5)$ \\
field & $\C$ & $\C$ & $\R$ & $\R$ & $\HH$ & $\HH$ & $\R$ & $\HH$ \\
$\dim_{\R} T$, $\dim_{\R} S$ & $8, 4$ & $8, 4$ & $4, 2$ & $4, 2$ & $16, 8$ & $16, 8$ & $4, 2$ & $8, 4$ \\
\bottomrule
\end{tabular}
\end{center}
In particular the field is not a function of the conformal pseudoscalar's square: $Q(\omega) = -1$ at $r = 7$ (field $\R$) and at $r = 3$ (field $\HH$).

*Proof.* \textit{The two even algebras.}\enspace By Fact \claimref{dark-tower-matter.imported-clifford-structure}(i),
\begin{align*}
\Cl^{0}(\hatV) &= \Cl^{0}(p+1, q+1) \cong \Cl(p+1, q), \\
\Cl^{0}(V) &= \Cl^{0}(p, q) \cong \Cl(p, q-1),
\end{align*}
and both have residue $(p+1) - q = p - (q-1) = r + 1$. The one tower with $q = 0$ is $(4,0)$: there $\Cl^{0}(4,0) \cong \Cl(0,3)$, of residue $-3 \equiv 5 = r + 1$, and $(0,4)$ gives the same algebra.



\emph{The commutant.}  By Fact \claimref{dark-tower-matter.imported-clifford-structure}(ii) each algebra is a matrix algebra over the division algebra $D(r+1)$, or a sum of two copies of one, and by Fact \claimref{dark-tower-matter.imported-clifford-structure}(iii) the commutant of a minimal left ideal is $D(r+1)$. Reading $D$ off for each tower:
\[
\begin{array}{c|cccccccc}
r & 6 & 2 & 1 & 7 & 3 & 5 & 0 & 4 \\
r + 1 & 7 & 3 & 2 & 0 & 4 & 6 & 1 & 5 \\ \hline
D(r+1) & \C & \C & \R & \R & \HH & \HH & \R & \HH
\end{array}
\]



\emph{Checks.}  The script computes every commutant from scratch on exact matrix representations of the ideals and classifies it (checks A1, A2), with the dimensions (A3) and the pseudoscalars (A4, A5).


**Remark  (T14's types are a different commutant).** T14's Theorem 3.4 assigns real type to $r = 0, 1, 2$ (two inequivalent modules at $r = 1$), complex type with an intrinsic $U(1)$ to $r = 3, 7$, and quaternionic type to $r = 4, 5, 6$ \cite[Thm.~3.4]{ButlerT14}. That is the commutant of the full Clifford algebra $\Cl(V)$ on its irreducible module; Theorem \claimref{dark-tower-matter.constituents-field} is the commutant of the spin action on the constituent ideal. Both are correct and they answer different questions. T14's intrinsic $U(1)$ at $r = 3$ and $r = 7$ is the central pseudoscalar, which reappears here as structure the tower carries beside its constituent field: at $r = 7$ as a unit joining two real constituents (Proposition \claimref{dark-tower-matter.residue-seven-unit}), at $r = 3$ as the unit $I_{7}$ inside the quaternions (Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions}).



**Theorem 16 (The adjoint and the norm of the field).** In a causal tower:
\begin{enumerate}
\item[(i)] $e_{K}e_{K}^{\dagger} = Q(e_{t})^{|K|}$ for every basis blade $e_{K}$, so $e_{K}e_{K}^{\dagger} = 1$ on every even blade and, for even $x$, $\ip{xx^{\dagger}}_{0}$ is the sum of the squares of $x$'s coordinates;
\item[(ii)] $f^{\dagger} = f$, and for $x \in f\Cl^{0}(V)f$,
\[
x^{\dagger}x \;=\; xx^{\dagger} \;=\; N(x)\,f, \qquad N(x) = 2\ip{xx^{\dagger}}_{0} \geq 0,
\]
with $N(x) = 0$ only at $x = 0$;
\item[(iii)] for $\psi \in S$ and $x \in f\Cl^{0}(V)f$,
\[
j(\psi x) \;=\; N(x)\, j(\psi).
\]
\end{enumerate}

*Proof.* \textit{(i) The blades.}\enspace Every direction other than $e_{t}$ has square $-Q(e_{t})$. There are two cases.

If $t \notin K$, moving $e_{t}$ through the $|K|$ vectors of $\rev{e_{K}}$ costs one sign each, and a blade times its reverse is the product of its squares:
\[
e_{K}^{\dagger} = e_{t}\rev{e_{K}}e_{t}^{-1} = (-1)^{|K|}\rev{e_{K}}, \qquad e_{K}\rev{e_{K}} = \bigl(-Q(e_{t})\bigr)^{|K|},
\]
so $e_{K}e_{K}^{\dagger} = (-1)^{|K|}\bigl(-Q(e_{t})\bigr)^{|K|} = Q(e_{t})^{|K|}$.

If $e_{K} = e_{t}e_{K'}$, then $\rev{e_{K}} = \rev{e_{K'}}e_{t}$, and
\begin{align*}
e_{K}^{\dagger} &= e_{t}\rev{e_{K'}} = (-1)^{|K'|}\,\rev{e_{K'}}\,e_{t}, \\
e_{K}e_{K}^{\dagger} &= (-1)^{|K'|}\,e_{t}\bigl(e_{K'}\rev{e_{K'}}\bigr)e_{t} = (-1)^{|K'|}\bigl(-Q(e_{t})\bigr)^{|K'|}\,Q(e_{t}) = Q(e_{t})^{|K|}.
\end{align*}
For $K \neq L$, $e_{K}e_{L}^{\dagger}$ is a multiple of $e_{K \triangle L}$, which has no scalar part. Hence for even $x = \sum_{K}x_{K}e_{K}$,
\[
\ip{xx^{\dagger}}_{0} \;=\; \sum_{K,L}x_{K}x_{L}\,\ip{e_{K}e_{L}^{\dagger}}_{0} \;=\; \sum_{K}x_{K}^{2} \qquad \text{(check B0)}.
\]



\emph{(ii) The corner and its conjugation.}  With $f = \tfrac{1}{2}(1 + e_{t}e_{a})$ and $\rev{(e_{t}e_{a})} = e_{a}e_{t}$,
\[
f^{\dagger} = \tfrac{1}{2}\bigl(1 + e_{t}\,e_{a}e_{t}\,e_{t}^{-1}\bigr) = \tfrac{1}{2}(1 + e_{t}e_{a}) = f.
\]
The corner $\F = f\Cl^{0}f$ is a division algebra $\R$, $\C$ or $\HH$ with unit $f$ (Fact \claimref{dark-tower-matter.imported-clifford-structure}(iii)). It is closed under $\dagger$, since $(fxf)^{\dagger} = fx^{\dagger}f$, and $\dagger$ is an anti-involution of it with $\ip{xx^{\dagger}}_{0} > 0$ for $x \neq 0$ by (i).

The standard conjugation is the only anti-involution with that positivity. Every other candidate has an element with $xx^{\dagger} = -f$, whose scalar part is $-\tfrac{1}{2}$:
\begin{itemize}
\item on $\C$ the other candidate is the identity, and a unit square root $x$ of $-f$ gives $xx^{\dagger} = xx = -f$;
\item on $\HH$ every other anti-involution is $x \mapsto u\bar{x}u^{-1}$ for a unit imaginary $u$, and a unit imaginary $v$ anticommuting with $u$ gives $v\,u\bar{v}u^{-1} = v^{2} = -f$.
\end{itemize}
So $\dagger$ is the standard conjugation, and
\[
x^{\dagger}x \;=\; xx^{\dagger} \;=\; N(x)\,f
\]
with $N$ the standard norm; the script verifies this as a polynomial identity in $x$'s coordinates (check B1). Taking scalar parts, with $\ip{f}_{0} = \tfrac{1}{2}$,
\[
\ip{xx^{\dagger}}_{0} \;=\; N(x)\,\ip{f}_{0} \;=\; \tfrac{1}{2}\,N(x),
\]
which is positive definite by (i), since $x$ is even (B3).



\emph{(iii) The norm law.}  By the definition of the adjoint, $e_{t}\rev{x} = x^{\dagger}e_{t}$, and $\psi f = \psi$ for $\psi \in S$. So
\begin{align*}
\psi x\,e_{t}\,\rev{(\psi x)} &= \psi\,\bigl(x e_{t}\rev{x}\bigr)\,\rev{\psi} \\
&= \psi\,\bigl(xx^{\dagger}\bigr)\,e_{t}\rev{\psi} \\
&= N(x)\,\psi f\,e_{t}\rev{\psi} \\
&= N(x)\,\psi e_{t}\rev{\psi},
\end{align*}
and the grade-one part is $j(\psi x) = N(x)\,j(\psi)$ (B2).




**Theorem 17 (Where mass begins in each causal tower).** Let $\psi, \psi_{1}, \psi_{2} \in S$ in a causal tower of dimension $n$.
\begin{enumerate}
\item[(i)] For $n = 3$ and $n = 4$ the reversion pairing is alternating, $\rev{\psi}\psi = 0$, every single constituent's momentum is null, and
\[
m^{2}\bigl(j(\psi_{1}) + j(\psi_{2})\bigr) \;=\; 2\,\ip{xx^{\dagger}}_{0}, \qquad x = \rev{\psi}_{1}\psi_{2}.
\]
Mass begins at two constituents; it vanishes exactly when $\rev{\psi}_{1}\psi_{2} = 0$.
\item[(ii)] For $n = 5$ the reversion pairing is not alternating, and
\[
m^{2}\bigl(j(\psi)\bigr) \;=\; \tfrac{1}{2}\,\ip{xx^{\dagger}}_{0}, \qquad x = \rev{\psi}\psi,
\]
which vanishes on a nonzero proper cone in $S$. Mass begins at one constituent.
\end{enumerate}
In every causal tower the total momentum of any number of constituents is timelike or null, never spacelike.

*Proof.* \textit{The pairing as a sandwich.}\enspace Write $\psi = \phi f$ with $\phi \in \Cl^{0}(V)$ and $f = \tfrac{1}{2}(1 + b)$, $b$ a bivector of square $+1$. Then $\rev{b} = -b$, so $\rev{f} = 1 - f$ and
\[
\rev{\psi}\psi \;=\; (1 - f)\;\rev{\phi}\phi\;f.
\]
The element $\rev{\phi}\phi$ is even and reversion-invariant, so it has grades $0$ and $4$ only:
\[
\rev{\phi}\phi = s + F, \qquad s = \ip{\rev{\phi}\phi}_{0}, \quad F = \ip{\rev{\phi}\phi}_{4}.
\]
Since $(1 - f)f = 0$, every part of $\rev{\phi}\phi$ that commutes with $b$ drops out of the sandwich:
\[
(1 - f)\,c\,f \;=\; c\,(1 - f)f \;=\; 0 \qquad \text{whenever } cb = bc.
\]



\emph{Dimensions three and four.}  In dimension three $F = 0$. In dimension four $F = uI$ is a multiple of the pseudoscalar, which commutes with every even element and in particular with $b$. In both cases all of $\rev{\phi}\phi$ commutes with $b$, so $\rev{\psi}\psi = 0$. This is the alternation in (i).



\emph{Dimension five.}  Here $F$ is a general four-vector, which need not commute with $b$, and $(1 - f)\,F f \neq 0$ for suitable $\phi$, so the pairing is not alternating.



\emph{The mass laws.}  The two displayed laws are identities between polynomials of degree four in the coordinates of $\psi_{1}, \psi_{2}$ (respectively $\psi$) on a basis of $S$. The script verifies them as polynomial identities over $\mathbb{Q}$, not on samples, in all six causal towers (checks B4, B5), together with the nullity of $j(\psi)$ in dimensions three and four (B4); it exhibits a nonzero $\psi$ with $\rev{\psi}\psi = 0$ in each five-dimensional tower (B6). The right-hand sides are nonnegative by Lemma \claimref{dark-tower-matter.adjoint-norm}(i), so each single momentum (and in dimensions three and four each pair sum) is timelike or null.



\emph{Any number of constituents.}  For every $\psi \in S$,
\begin{align*}
Q(e_{t})\,\bigl(j(\psi)\cdot e_{t}\bigr) &= Q(e_{t})\,\ip{\psi e_{t}\rev{\psi}\,e_{t}}_{0} \\
&= \ip{\psi\,e_{t}\rev{\psi}e_{t}^{-1}}_{0} \\
&= \ip{\psi\psi^{\dagger}}_{0} \;\geq\; 0 \qquad \text{(B7)}.
\end{align*}
So every constituent's momentum is causal and lies in the same closed half-space bounded by $e_{t}^{\perp}$, hence in the same half of the causal cone, and that half is closed under addition.


**Remark  (The four-dimensional case is T11's formula).** In this tower $x = \rev{\psi}_{1}\psi_{2}$ lies in the two-dimensional space $(1-f)\Cl^{0}f$, a copy of $\C$, and Theorem \claimref{dark-tower-matter.where-mass-begins}(i) is T11's two-constituent mass formula \cite[Prop.~4.1]{ButlerT11} written in the even algebra, the pairing $x$ playing the role of the bracket. In five dimensions the law is the Fierz identity $j^{2} = (\bar{\psi}\psi)^{2}$ of a single Dirac spinor; the geometric statement is that the four-vector part of $\rev{\phi}\phi$ survives the idempotent.



**Theorem 18 (The momentum-preserving mixings of constituents).** Let $\F = f\Cl^{0}(V)f$ act on $S$ on the right and on $S^{n}$ by $\psi'_{i} = \sum_{k}\psi_{k}U_{ki}$ for $U \in M_{n}(\F)$. Then $U$ preserves the total momentum of every $n$-tuple if and only if $UU^{\dagger} = 1$, where $(U^{\dagger})_{ik} = (U_{ki})^{\dagger}$. The momentum-preserving group is $O(n)$, $U(n)$ or $Sp(n)$ as $\F = \R$, $\C$, $\HH$: $O(n)$ in the three-dimensional towers, $U(n)$ in this tower and the mirror, $Sp(n)$ in the five-dimensional towers.

*Proof.* \textit{Unitary mixings preserve the momentum.}\enspace Using $e_{t}\rev{y} = y^{\dagger}e_{t}$ on each entry of $U$,
\begin{align*}
\sum_{i}\psi'_{i}e_{t}\rev{\psi'_{i}} &= \sum_{i}\sum_{k,l}\psi_{k}U_{ki}\,e_{t}\,\rev{U_{li}}\,\rev{\psi_{l}} \\
&= \sum_{k,l}\psi_{k}\Bigl(\sum_{i}U_{ki}U_{li}^{\dagger}\Bigr)e_{t}\rev{\psi_{l}}.
\end{align*}
If $UU^{\dagger} = 1$, that is $\sum_{i}U_{ki}U_{li}^{\dagger} = \delta_{kl}f$, the right-hand side is $\sum_{k}\psi_{k}e_{t}\rev{\psi_{k}}$.



\emph{Only unitary mixings do.}  Take $\psi_{k} = \psi a_{k}$ for one $\psi \in S$ with $j(\psi) \neq 0$ and a row $a = (a_{k}) \in \F^{n}$. Then $\psi'_{i} = \psi\,(aU)_{i}$, and Lemma \claimref{dark-tower-matter.adjoint-norm}(iii) gives the total momenta before and after as
\[
P = \Bigl(\sum_{k}N(a_{k})\Bigr)\,j(\psi), \qquad P' = \Bigl(\sum_{i}N\bigl((aU)_{i}\bigr)\Bigr)\,j(\psi).
\]
Their equality for every $a$ says that $U$ preserves the positive definite form $\sum_{k}N(a_{k})$ on $\F^{n}$, whose polarisation is the standard $\F$-Hermitian form; so $UU^{\dagger} = 1$.



\emph{The groups.}  The isometry groups of the standard forms over $\R$, $\C$, $\HH$ are $O(n)$, $U(n)$, $Sp(n)$, and Theorem \claimref{dark-tower-matter.constituents-field} assigns the fields. The script checks an $\F$-unitary mixing in every causal tower as a polynomial identity (C1) and exhibits a non-unitary mixing that changes the total momentum (C2).


## The ladder pairs and the complex unit



**setting  (The ladder pairs and the complex unit).** A \emph{ladder pair} is a pair $w, v$ of null vectors of the conformal space, $Q(w) = Q(v) = 0$, or of vectors dressed by a complex unit with $w^{2} = v^{2} = 0$, such that $wv + vw = 1$: the canonical anticommutation relations, one fermionic mode per pair \cite[Prop.~4.1]{ButlerT3}. Pairs built from real hyperbolic planes of $\hatV$ need no unit; their number is the real Witt index $\min(p,q) + 1$. The constituent's pair count is the complex Witt index $\lfloor (n+2)/2 \rfloor$ (T12's Lemma 2.12 in even dimension \cite[Lem.~2.12]{ButlerT12}; in odd dimension the same bound, with one generator left over).



**Theorem 19 (The ladder pairs of the causal towers).** \begin{enumerate}
\item[(i)] In the three-dimensional towers the real and complex Witt indices of $\hatV$ are both $2$: two real ladder pairs, and no unit is needed (check D1).
\item[(ii)] In this tower, the mirror and the five-dimensional towers the real Witt index is $2$ and the complex one $3$: the third pair needs a complex unit. In this tower and the mirror the field is $\C$ and the unit is fixed up to sign (Remark \claimref{note.dark-tower-matter.why-u}).
\end{enumerate}

*Proof.* In a causal tower $\min(p,q) = 1$, and $\hatV$ has signature $(p+1, q+1)$. Its Witt indices are
\[
\text{real: } \min(p+1, q+1) = 2, \qquad
\text{complex: } \Bigl\lfloor \frac{\dim\hatV}{2} \Bigr\rfloor =
\begin{cases} 2, & \dim\hatV = 5, \\ 3, & \dim\hatV = 6, 7. \end{cases}
\]
Check D1 builds the two real pairs of $\Cl(3,2)$ and $\Cl(2,3)$ on their modules and verifies the relations. In this tower and the mirror the field of (ii) is $\C$ by Theorem \claimref{dark-tower-matter.constituents-field}.




**Theorem 20 (The third pair's unit in five dimensions).** Work on the sixteen-dimensional irreducible module of the conformal algebra, which is the constituent ideal $T$ as a module of the spin group, with spin commutant $\HH$ (Theorem \claimref{dark-tower-matter.constituents-field}).
\begin{enumerate}
\item[(i)] ($r = 3$) The pseudoscalar $I_{7}$ of $\Cl(5,2)$ lies in $\HH$, squares to $-1$ and commutes with every vector. With it the third pair $\tfrac{1}{2}(e_{a} \pm I_{7}e_{b})$ joins two real pairs to give three pairs obeying the canonical relations, and their bilinears $I_{7}(v_{i}w_{i} - \tfrac{1}{2})$, $v_{i}w_{k} - v_{k}w_{i}$, $I_{7}(v_{i}w_{k} + v_{k}w_{i})$ span a Lie algebra $\uu(3)$ whose centraliser in $\HH$ is $\mathrm{span}\{1, I_{7}\}$.
\item[(ii)] ($r = 3$) Every unit $J \in \HH$ anticommuting with $I_{7}$ anticommutes with every vector, so it acts as the grade involution: it fixes the real pairs up to sign and sends $w_{3}$ to $-\bar{w}_{3}$, exchanging the third pair's creator and annihilator; $\uu(3)$ and $J$ generate a Lie algebra of dimension $30$, not the commuting sum $\su(2) \oplus \uu(3)$ of dimension $12$.
\item[(iii)] ($r = 5$) No element of $\HH$ outside $\R$ commutes with all of $\HH$, and $\omega$ squares to $+1$: the algebra supplies no canonical unit. Every unit $u \in \HH$ commutes with the vectors and builds a third pair, $w_{3} = \tfrac{1}{2}(e_{a} + ue_{b})$, $v_{3} = -\tfrac{1}{2}(e_{a} - ue_{b})$ with $Q(e_{a}) = Q(e_{b}) = -1$; the resulting $\uu(3)_{u}$ has centraliser $\mathrm{span}\{1, u\}$ in $\HH$, and a second unit anticommuting with $u$ generates dimension $30$ with it. Any two units are conjugate in $\HH$: $(1 - u'u)\,u = u'(1 - u'u)$ for $u' \neq -u$, and $u' = -u$ is reached by conjugation with any unit anticommuting with $u$. The choices form the sphere $Sp(1)/U(1) = S^{2}$.
\end{enumerate}

*Proof.* \textit{(i) The unit $I_{7}$.}\enspace $I_{7}$ is central in $\Cl(5,2)$ (odd dimension) with $Q(I_{7}) = -1$ (the section ``Setting, imports and premises''). Central elements commute with the spin action, so $I_{7} \in \HH$, the spin commutant of Theorem \claimref{dark-tower-matter.constituents-field}. Take $Q(e_{a}) = Q(e_{b}) = +1$ and
\[
w = \tfrac{1}{2}(e_{a} + I_{7}e_{b}), \qquad \bar{w} = \tfrac{1}{2}(e_{a} - I_{7}e_{b}).
\]
Since $I_{7}$ commutes with vectors and $e_{a}e_{b} = -e_{b}e_{a}$,
\begin{align*}
w^{2} &= \tfrac{1}{4}\bigl(Q(e_{a}) + I_{7}^{2}\,Q(e_{b})\bigr) = \tfrac{1}{4}(1 - 1) = 0, \\
w\bar{w} + \bar{w}w &= \tfrac{1}{2}\bigl(Q(e_{a}) - I_{7}^{2}\,Q(e_{b})\bigr) = \tfrac{1}{2}(1 + 1) = 1.
\end{align*}
The cross relations with the real pairs hold because distinct basis vectors anticommute and $I_{7}$ commutes with them (D3). Closure and the centraliser are computed (D4, D5).



\emph{(ii) A unit anticommuting with $I_{7}$.}  $J$ commutes with the even algebra (it lies in the spin commutant) and anticommutes with $I_{7}$. Every vector factors as $e = (eI_{7}^{-1})\,I_{7}$ with $eI_{7}^{-1}$ even, so
\[
JeJ^{-1} \;=\; (eI_{7}^{-1})\,\bigl(JI_{7}J^{-1}\bigr) \;=\; (eI_{7}^{-1})(-I_{7}) \;=\; -e \qquad \text{(D6)}.
\]
Hence $J(I_{7}e_{b})J^{-1} = I_{7}e_{b}$ and
\[
Jw_{3}J^{-1} \;=\; -\tfrac{1}{2}(e_{a} - I_{7}e_{b}) \;=\; -\bar{w}_{3},
\]
and the closure has dimension $30$ (D7).



\emph{(iii) The residue-five tower.}  The centre of $\HH$ is $\R$ and $Q(\omega) = +1$ (A4), so the algebra names no unit. The spin and Clifford commutants coincide on this module (D8), so every unit $u \in \HH$ commutes with the vectors. With $Q(e_{a}) = Q(e_{b}) = -1$ and $u^{2} = -1$,
\[
w_{3}v_{3} + v_{3}w_{3} \;=\; -\tfrac{1}{2}\bigl(Q(e_{a}) - u^{2}\,Q(e_{b})\bigr) \;=\; -\tfrac{1}{2}(-1 - 1) \;=\; 1 \qquad \text{(D9 to D11)}.
\]
For the conjugacy, with $u^{2} = u'^{2} = -1$,
\begin{align*}
(1 - u'u)\,u &= u - u'u^{2} = u + u', \\
u'\,(1 - u'u) &= u' - u'^{2}u = u' + u,
\end{align*}
so the two sides agree, and $1 - u'u = 0$ only at $u' = -u$ (D12).


**Remark  (The two readings of the unit).** Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions} is where the two five-dimensional towers part. At $r = 3$ the unit that builds the pairs is fixed by the algebra, and the quaternionic unit group of a single constituent, which preserves its momentum (Theorem \claimref{dark-tower-matter.ladder}), does not preserve the pair structure. At $r = 5$ every choice of unit is equivalent, and each choice cuts the quaternionic group to the circle it generates. Under U3 both towers therefore build their pairs with one complex unit; they differ in whether the algebra names it. With an external unit, which commutes with the whole quaternionic group, the group survives in both towers alike (Remark \claimref{note.dark-tower-matter.branches-break-u-what-they-give}).

## The gauge algebras





**Theorem 21 (The gauge algebras of the odd towers).** Under H2 and Premise \claimref{dark-tower-matter.u-transposition-rule}:
\begin{enumerate}
\item[(i)] (Three-dimensional towers, $r = 1, 7$.) Mass begins at two real constituents and each carries two real pairs, so the minimal massive hierarchy is $\R^{2} \otimes \R^{2}$. Its automorphisms $A \otimes B$ with $A, B \in O(2)$ form $(O(2) \times O(2))/\mathbb{Z}_{2}$, the kernel being $\{(1,1), (-1,-1)\}$; the gauge algebra is $\so(2) \oplus \so(2)$, abelian, of dimension $2$, and the identity component of the group is $U(1)_{+} \times U(1)_{-}$.
\item[(ii)] (Five-dimensional towers, $r = 3, 5$.) Mass begins at one constituent and its three pairs are complex with the unit of Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions}, so the hierarchy is $\C^{1} \otimes \C^{3}$. Its automorphisms form $(U(1) \times U(3))/U(1) \cong U(3)$; the gauge algebra is $\uu(3) = \su(3) \oplus \uu(1)$, of dimension $9$.
\end{enumerate}

*Proof.* \textit{(i) The two factors.}\enspace The constituent count is two (Theorem \claimref{dark-tower-matter.where-mass-begins}(i)) and the field is $\R$ (Theorem \claimref{dark-tower-matter.constituents-field}), so by U2 (\claimref{dark-tower-matter.u-transposition-rule}) the slot group is $O(2)$ (Theorem \claimref{dark-tower-matter.ladder}). The pairs are real (Proposition \claimref{dark-tower-matter.pairs}(i)), and by U2 their group is the orthogonal group of the real pair space, again $O(2)$.

The norm clause of U2 matters here. Without it, the pair mixings preserving the canonical relations alone would be $GL(2,\R)$, acting by $B$ on the $w_{i}$ and by $B^{-T}$ on the $v_{i}$. That is the mechanism of Remark \claimref{note.dark-tower-matter.kleinian-algebra}, where the sterile tower has no time direction and so no adjoint.



\emph{(i) The kernel.}  An automorphism of $\R^{2} \otimes \R^{2}$ respecting both factors is $A \otimes B$, and
\[
A \otimes B = 1 \quad\Longleftrightarrow\quad A = \lambda 1, \;\; B = \lambda^{-1}1,
\]
with $\lambda$ real and orthogonal, so $\lambda = \pm 1$. The kernel $\{(1,1), (-1,-1)\}$ is discrete, no generator is lost, and the algebra is $\so(2) \oplus \so(2)$ (the gauge algebra by \claimref{dark-tower-matter.h2-identification}; checks E1, E2).



\emph{(i) The charges.}  Write $s$ and $p$ for the weights of the slot and pair rotations. The element $(-1, -1)$ acts as $(-1)^{s + p}$, so the group's representations are those with $s + p$ even, on which
\[
q_{\pm} = \frac{s \pm p}{2}
\]
are the integral charges of $U(1)_{\pm}$ (F2).



\emph{(ii) The slot.}  The constituent count is one (Theorem \claimref{dark-tower-matter.where-mass-begins}(ii)). The slot group of one constituent is $Sp(1)$ (Theorem \claimref{dark-tower-matter.ladder}), acting on the spinor part through H1 (\claimref{dark-tower-matter.h1-momentum})'s identification of the two fields. The pair unit of Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions} lies in that field, and only the circle it generates commutes with the pair algebra, so the slot is one complex line with group $U(1)$.



\emph{(ii) The pairs and the kernel.}  By U2 the three complex pairs carry $U(3)$. The action $(\lambda, B) \mapsto \lambda B$ has the common scalar as its kernel, as in T12's proof of its Theorem 4.1, so the group is
\[
\frac{U(1) \times U(3)}{U(1)} \;\cong\; U(3)
\]
(E3; the control $\C^{2} \otimes \C^{3} \mapsto 12$ is E4).


**setting  (The gauge algebras).** In the mirror the algebra and global form are this tower's, $\su(2) \oplus \su(3) \oplus \uu(1)$ and $S(U(2) \times U(3))$: that is T14's copy theorem \cite[Thm.~4.3]{ButlerT14}, which Theorem \claimref{dark-tower-matter.mirror-algebra} below realises as an explicit isomorphism of the even algebras.

**Remark  (Branches that break U, and what they give).** Two transpositions reproduce this tower and break a clause of Premise \claimref{dark-tower-matter.u-transposition-rule}. (a) Counting the $r = 7$ constituent in the full Clifford module, where the central $\omega$ joins two real constituents into one complex element that is already massive (Theorem \claimref{dark-tower-matter.where-mass-begins}(i) for the two real parts), gives the hierarchy $\C^{1} \otimes \C^{2}$ and $\uu(2)$, with content a doublet of $Y = \tfrac{1}{2}$, a singlet of $Y = -1$ and a neutral singlet; it breaks U1, since $\omega$ is odd and does not act on the spin-irreducible ideal (Proposition \claimref{dark-tower-matter.residue-seven-unit}(ii)). (b) Building the five-dimensional third pair with an external $i$, which commutes with the quaternionic unit group, keeps that group as the slot group of the one constituent: the hierarchy is a quaternionic line tensor $\C^{3}$, with automorphisms $\su(2) \oplus \su(3) \oplus \uu(1)$ and global form $S(U(2) \times U(3))$, and vector-like content $(2,3)_{1/6}$, $(2,1)_{-1/2}$. It keeps U1 and U2 and breaks U3; it is T12's own practice of working in the complexification, carried to a tower whose field is $\HH$; and it is open at $r = 3$ and $r = 5$ on the same terms, so it does not separate them. Its $\su(2)$ acts on one constituent's quaternionic multiplicity, not on two constituents. Their arithmetic is in the supplementary scripts (\file{D3C}, \file{D5Q}; the section ``Machine verification''). Neither is a result of this paper.

## Content



**setting  (Content).** T12's lesson is that fermions are generators of the composite, not its states \cite[Rem.~5.2, Prop.~5.3]{ButlerT12}. The generators of a hierarchy $\F^{m} \otimes \F^{k}$ are its single slot-pair cells; Hypothesis (S) adds the constituent-level states.



**Theorem 22 (The three-dimensional towers' content).** In the towers $r = 1, 7$:
\begin{enumerate}
\item[(i)] The generators are the four cells of $\R^{2} \otimes \R^{2}$, of weights $(s, p) \in \{\pm 1\}^{2}$; as complex two-component fermions they are $A$, with $(q_{+}, q_{-}) = (1, 0)$, and $B$, with $(0, 1)$, and their conjugates. Each is charged under one factor only: the tower is two copies of single-flavour electrodynamics in $2+1$ dimensions, exchanged by the pair reflection $p \mapsto -p$.
\item[(ii)] Every weight of the exterior algebra of the cells has $s + p$ even; no state of the tensor state space has weight $(\pm 1, 0)$ or $(0, \pm 1)$.
\item[(iii)] Under (S) the constituent-level states have weight $(\pm 1, 0)$, off the lattice $s + p$ even: (S) and the global form of Theorem \claimref{dark-tower-matter.gauge-algebras}(i) are incompatible. Of the directions the transport adds, the rung directions carry $(\pm 1, 0)$ and the pair directions $(0, \pm 1)$, and both are excluded; the one neutral direction (the leftover generator of the odd conformal algebra) is allowed, and its value is a bare mass. The tower has no charged Higgs analogue.
\item[(iv)] There is no chirality: the odd-dimensional modules carry no Lorentz-invariant grading \cite[Prop.~3.9]{ButlerT14}. Gauge-invariant Dirac masses exist for $A$ and $B$ without any condensate, and there is no baryon-like composite: every gauge-neutral state has zero net number of each cell.
\end{enumerate}

*Proof.* \textit{(i)}\enspace The cells are single-occupation states. The charges $q_{\pm} = (s \pm p)/2$ of the $U(1)_{+} \times U(1)_{-}$ of Theorem \claimref{dark-tower-matter.gauge-algebras}(i) send
\[
(s, p) = (1, 1) \;\mapsto\; (q_{+}, q_{-}) = (1, 0), \qquad (1, -1) \;\mapsto\; (0, 1) \qquad \text{(F2)},
\]
and the pair reflection $p \mapsto -p$ exchanges them.



\emph{(ii)}  A product of cells adds weights, and each cell has $s + p \in \{-2, 0, 2\}$ (F1).



\emph{(iii)}  A constituent-level state occupies one slot mode and no pair mode, so its weight is $(\pm 1, 0)$, off the lattice $s + p$ even (Remark \claimref{note.dark-tower-matter.why-s-fails-three-dimensions-not}). The weights of the transported directions are computed in the supplementary script \file{D3R} (checks H5 to H9): rung directions $(\pm 1, 0)$, pair directions $(0, \pm 1)$, the leftover generator $(0,0)$.



\emph{(iv)}  This is the odd case of T14's Proposition \claimref{dark-matter.two-families-are-two-chiralities}. A mass term $\bar{A}A$ has weight zero, and a neutral product of cells pairs each cell with its conjugate.


**Remark  (The neutral row).** In a hierarchy $\C^{1} \otimes \C^{k}$ whose central generator acts by $k$ on the slot and $-1$ on each pair, the state with the slot and all $k$ pairs occupied has weight $k - k = 0$. The constituent-level generator of a one-constituent hierarchy is therefore neutral: the trace-free central generator of $\uu(1) \oplus \uu(k)$ on $\C^{1} \oplus \C^{k}$ is $(k\,i, -i\,1_{k})$ up to scale, and weights add. Arithmetic.



**Theorem 23 (The five-dimensional towers' content).** In the towers $r = 3, 5$, under (S) the state space $\Lambda^{\bullet}(\C^{1} \oplus \C^{3})$ has sixteen states. With $Y = s - k/3$ ($s$ the slot occupation, $k$ the number of occupied pairs), the complement $(s,k) \mapsto (1-s, 3-k)$ negates $Y$ and conjugates colour, so the sixteen are eight species-states and their conjugates, four vector-like Dirac species:
\begin{center}\small
\begin{tabular}{@{}lccl@{}}
\toprule
species & colour & $Y$ & states $(s,k)$ \\
\midrule
$U$ & $3$ & $2/3$ & $(1,1)$, conjugate $(0,2)$ \\
$D$ & $3$ & $-1/3$ & $(0,1)$, conjugate $(1,2)$ \\
$E$ & $1$ & $-1$ & $(0,3)$, conjugate $(1,0)$ \\
$N$ & $1$ & $0$ & $(0,0)$, $(1,3)$ \\
\bottomrule
\end{tabular}
\end{center}
These are the electric charges of one of our generations with the weak doublet removed. Through the section $B \mapsto ((\det B)^{-1}, B)$ the centre of $U(3)$ acts on $(s,k)$ by $\lambda^{k - 3s} = \lambda^{-3Y}$, so $3Y$ is an integer with $3Y + k \equiv 0 \pmod 3$, $k$ being the triality: the lattice of $U(3)$, satisfied automatically; the neutral species $N$ is the empty state and the full row of Remark \claimref{note.dark-tower-matter.neutral-row}. Without (S) the content is one Dirac colour triplet of $Y = 2/3$. There is no chirality and every species has a gauge-invariant bare mass.

*Proof.* The state space under (S) (\claimref{dark-tower-matter.hypothesis-s-slot-statistics}) has
\[
\dim \Lambda^{\bullet}\C^{4} \;=\; \sum_{s=0}^{1}\sum_{k=0}^{3}\binom{3}{k} \;=\; 2 \cdot 8 \;=\; 16
\]
states, the $\binom{3}{k}$ states at pair number $k$ forming the $1, 3, \bar{3}, 1$ of the $SU(3)$ of Theorem \claimref{dark-tower-matter.gauge-algebras}(ii). The complement negates $Y$:
\[
Y(1 - s, 3 - k) \;=\; (1 - s) - \frac{3 - k}{3} \;=\; -\Bigl(s - \frac{k}{3}\Bigr) \;=\; -Y(s, k),
\]
and the remaining weights are arithmetic (F3, F4). The masses are as in Proposition \claimref{dark-tower-matter.three-dimensional-content}(iv).


**Remark  (Why (S) fails in three dimensions, not five).** In both cases the slot-level states are charged under the kernel of the action on the hierarchy. In five dimensions the kernel is the common scalar $U(1)$, and the subgroup $S(U(1) \times U(3)) = \{((\det B)^{-1}, B)\}$ maps isomorphically onto the quotient $U(3)$: the exterior algebra of slot and pair modes is a representation of that section, as T12 uses $S(U(2) \times U(3))$ in four dimensions. In three dimensions the kernel $\{\pm(1,1)\}$ is discrete inside the torus $SO(2) \times SO(2)$, and no subgroup maps isomorphically onto the quotient, so the slot-level states are not representations of the global form. Under (S) the five-dimensional state space has a tenth abelian automorphism, the slot number, beyond the nine of $\uu(3)$; this paper takes it as a global symmetry, not gauged (a choice: T12 counts the corresponding extra generator in four dimensions and finds it anomaly-free, broken by the right-handed neutrino's Majorana mass \cite[Prop.~5.8]{ButlerT12}); here it is broken only by a mass term for $N$ off the pair unit's axis.



**Theorem 24 (Chern-Simons levels of the odd towers' content).** \begin{enumerate}
\item[(i)] In the three-dimensional towers each $U(1)_{\pm}$ couples to exactly one unit-charge two-component fermion, which shifts its Chern-Simons level by $\tfrac{1}{2}\mathrm{sign}(m)$ \cite{Redlich1984}; integrality of the effective level forces the bare levels into $\mathbb{Z} + \tfrac{1}{2}$. Parity is therefore broken by the gauge sector.
\item[(ii)] In the five-dimensional towers, in units $q' = 3Y$, the content of Proposition \claimref{dark-tower-matter.five-dimensional-content} has $\sum q'^{3} = -6$ and $\sum q' = 0$ (with multiplicities), and the induced abelian cubic Chern-Simons coefficient, $\tfrac{1}{2}\sum \mathrm{sign}(m)\,q'^{3}$, is integral for every choice of mass signs \cite{IMS1997}. The $SU(3)$ and mixed levels, which on $U(3)$ are tied to the abelian one, are not analysed here.
\end{enumerate}

*Proof.* \textit{(i)}\enspace With bare level $k$ and one unit-charge fermion of mass $m$ (Proposition \claimref{dark-tower-matter.three-dimensional-content}(i)), the effective level is, by Fact \claimref{rule2.imported-parity-anomaly},
\[
k_{\mathrm{eff}} \;=\; k + \tfrac{1}{2}\,\mathrm{sign}(m) \;\in\; \mathbb{Z} \quad\Longrightarrow\quad k \in \mathbb{Z} + \tfrac{1}{2} \qquad \text{(G1, G2)},
\]
and no half-integer is zero, so a parity-odd Chern-Simons term is always present.



\emph{(ii)}  In units $q' = 3Y$ the species of Proposition \claimref{dark-tower-matter.five-dimensional-content} carry $q' = 2, -1, -3, 0$ for $U, D, E, N$, with colour multiplicity $3$ for $U$ and $D$. So
\begin{align*}
\sum q'^{3} &= 3(2)^{3} + 3(-1)^{3} + (-3)^{3} + 0 = 24 - 3 - 27 = -6, \\
\sum q' &= 3(2) + 3(-1) + (-3) + 0 = 0 \qquad \text{(G3)}.
\end{align*}
In the induced coefficient $\tfrac{1}{2}\sum \mathrm{sign}(m)\,q'^{3}$ (Fact \claimref{rule2.imported-five-dimensional-chern-simons-shift}) the terms of $U$ and $N$ are the integers $\pm 12$ and $0$, and those of $D$ and $E$ are $\pm\tfrac{3}{2}$ and $\pm\tfrac{27}{2}$, whose sum is an integer for each choice of signs.


## The paired towers



**setting  (The paired towers).** T14's indifference premise P2 equates the data of the two members of each reversal pair, $\{2, 6\}$, $\{1, 7\}$ and $\{3, 5\}$ \cite[Prem.~2.2]{ButlerT14}. This section compares the members of the odd pairs as algebras.



**Theorem 25 (The central unit of the residue-seven tower).** \begin{enumerate}
\item[(i)] Along the residue-seven tower ($\Cl(2,3)$, $\Cl(3,4)$, $\Cl(4,5)$, \ldots) the pseudoscalar is central and squares to $-1$ at every rung; along the residue-one tower ($\Cl(3,2)$, $\Cl(4,3)$, \ldots) it is central and squares to $+1$.
\item[(ii)] At $r = 7$ the pseudoscalar $\omega$ is odd: it carries the even ideal into the odd one, so it does not act on the constituent ideal, and the grade involution reverses it.
\item[(iii)] On the Clifford module $\Cl(\hatV)\hf = T \oplus \omega T$, left multiplication by $c + s\omega$ ($c^{2} + s^{2} = 1$) commutes with the whole Clifford action and carries $X + \omega Y$ to $(cX - sY) + \omega(sX + cY)$: on a pair of real constituents it is the slot rotation of Theorem \claimref{dark-tower-matter.gauge-algebras}(i), here supplied by the algebra itself. Every cell carries charge $\pm 1$ under it. If the tower's action is built from operations that commute with the Clifford action, as T12's are, a Majorana-type mass (charge $2$) is then forbidden in the $r = 7$ tower whether or not the rotation is gauged; this last clause is at assembly level.
\end{enumerate}

*Proof.* \textit{(i)}\enspace By the formula of the section ``Setting, imports and premises'' (\claimref{primer.sign}), $Q(\omega) = (-1)^{n(n-1)/2}(-1)^{q}$. Each rung adds $(1,1)$ to the signature, so $n$ rises by two and $q$ by one, and the first exponent changes by
\[
\frac{(n+2)(n+1)}{2} - \frac{n(n-1)}{2} \;=\; 2n + 1,
\]
which is odd. The two sign changes cancel, so $Q(\omega)$ is constant along each tower and equal to its value at the first rung:
\[
Q(\omega_{2,3}) = (-1)^{10}(-1)^{3} = -1, \qquad Q(\omega_{3,2}) = (-1)^{10}(-1)^{2} = +1.
\]
Every rung has odd dimension, so $\omega$ is central (H1, H2; \claimref{std-algebra.pseudoscalar-commutation}).



\emph{(ii)}  $\omega$ is a product of five vectors (H3), so it is odd, left multiplication by it exchanges the even and odd parts, and $\hat{\omega} = (-1)^{5}\omega = -\omega$ (\claimref{std-algebra.involution-properties}).



\emph{(iii)}  $\omega$ is central with $\omega^{2} = -1$ (H4), so $c + s\omega$ commutes with the Clifford action, and for $X, Y \in T$
\[
(c + s\omega)(X + \omega Y) \;=\; cX + s\omega^{2}Y + \omega(sX + cY) \;=\; (cX - sY) + \omega(sX + cY).
\]




**Theorem 26 (Paired towers hold the same kind of matter).** Under H2 and Premise \claimref{dark-tower-matter.u-transposition-rule} the two towers of each odd dimension have the same constituent field, the same mass onset, the same gauge algebra and the same content. They differ only as follows.
\begin{center}\small
\begin{tabular}{@{}p{3.6cm}p{4.9cm}p{4.9cm}@{}}
\toprule
 & $r = 1$ & $r = 7$ \\
\midrule
slot rotation & a rotation of two modules of the same type & the algebra's central unit, exact at every rung \\
slot reflection & internal & exists only fused with orientation reversal \\
module types & two ($\omega = \pm 1$) & one \\
number-violating masses & forbidden once the slot rotation is gauged (H2) & forbidden by the algebra's unit, gauged or not \\
\midrule
 & $r = 3$ & $r = 5$ \\
\midrule
the pair unit & $I_{7}$, fixed by the algebra & a point of $S^{2}$, not fixed \\
reversion-type invariant form & one, Hermitian for $I_{7}$ & none \\
module types & one & two \\
\bottomrule
\end{tabular}
\end{center}

*Proof.* The shared rows are Theorems \claimref{dark-tower-matter.constituents-field}, \claimref{dark-tower-matter.where-mass-begins}, \claimref{dark-tower-matter.gauge-algebras} and Propositions \claimref{dark-tower-matter.three-dimensional-content}, \claimref{dark-tower-matter.five-dimensional-content}. The differing rows come from Proposition \claimref{dark-tower-matter.residue-seven-unit} and Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions}, except two that are computed in supplementary scripts: the slot-reflection row in \file{D3C} (Part I), and the invariant-form row in the referee script \file{CHECK\_ALG/check\_r3\_r5.py}.

The argument holds given \claimref{dark-tower-matter.u-transposition-rule}, which fixes the constituent field and the slot and pair groups, and \claimref{dark-tower-matter.h2-identification}, which identifies the gauge algebra with the automorphism algebra of the minimal massive hierarchy.


**Remark  (The $r = 5$ unit: datum or field).** If the unit $u$ of Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions}(iii) is a constant of the tower, every choice gives an isomorphic tower and nothing observable distinguishes it from $r = 3$; this is how this tower treats its own unit, which the algebra fixes up to sign. If $u$ varies over spacetime, the tower carries a sigma model on $S^{2}$ with two massless five-dimensional scalars, which moves the radiation bound of Proposition \claimref{dark-tower-matter.five-dimensional-towers}(iii) from $0.085$ to $0.084$. The series supplies no kinetic term for $u$; the first reading is this tower's.

## The mirror





**Theorem 27 (The mirror's even algebra as a real isomorphism).** \begin{enumerate}
\item[(i)] The linear map $e_{K} \mapsto (-1)^{|K|/2}e_{K}$ on even basis blades is an algebra isomorphism from the even algebra of a signature onto the even algebra of the reversed signature (every $Q(e_{a})$ negated); in particular $\Cl^{0}(3,1) \cong \Cl^{0}(1,3)$ and $\Cl^{0}(4,2) \cong \Cl^{0}(2,4)$.
\item[(ii)] It carries the mirror's pseudoscalar $I_{4}'$ to $+I_{4}$ and its conformal pseudoscalar $I_{6}'$ to $-I_{6}$.
\item[(iii)] The full algebras differ: $\Cl(1,3)$ has quaternionic irreducible modules and $\Cl(3,1)$ real ones.
\end{enumerate}

*Proof.* \textit{(i) The product rule.}\enspace Write $Q$ for the squares of the first signature and $Q' = -Q$ for those of the second. For even blades $e_{K}$, $e_{L}$,
\[
e_{K}e_{L} \;=\; \sigma \prod_{c \in K \cap L}Q(e_{c})\;e_{K \triangle L},
\]
with $\sigma$ the reordering sign, which does not depend on the squares; the same holds in the second algebra with $Q'$ in place of $Q$.



\emph{(i) The map respects it.}  Let $\varphi(e_{K}) = (-1)^{|K|/2}e_{K}$, and use $|K \triangle L| = |K| + |L| - 2|K \cap L|$ and $\prod_{c}Q'(e_{c}) = (-1)^{|K \cap L|}\prod_{c}Q(e_{c})$. Then
\begin{align*}
\varphi(e_{K}e_{L}) &= \sigma\prod_{c}Q(e_{c})\,(-1)^{|K \triangle L|/2}\,e_{K \triangle L}
= (-1)^{\frac{|K|+|L|}{2}}(-1)^{|K \cap L|}\,\sigma\prod_{c}Q(e_{c})\,e_{K \triangle L}, \\
\varphi(e_{K})\,\varphi(e_{L}) &= (-1)^{\frac{|K|+|L|}{2}}\,\sigma\prod_{c}Q'(e_{c})\,e_{K \triangle L}
= (-1)^{\frac{|K|+|L|}{2}}(-1)^{|K \cap L|}\,\sigma\prod_{c}Q(e_{c})\,e_{K \triangle L}.
\end{align*}
The two agree. The script checks every pair of basis blades in both cases (I1).



\emph{(ii)}  On the pseudoscalars,
\[
\varphi(I_{4}') = (-1)^{4/2}\,I_{4} = +I_{4}, \qquad \varphi(I_{6}') = (-1)^{6/2}\,I_{6} = -I_{6} \qquad \text{(I2)}.
\]



\emph{(iii)}  The commutants are $\HH$ and $\R$ (I3; Fact \claimref{dark-tower-matter.imported-clifford-structure}).


**setting  (The mirror).** So the mirror's constituents are complex, as ours are (Theorem \claimref{dark-tower-matter.constituents-field}): its real (Majorana) ground spinors do not make them real. The isomorphism sends the mirror's field unit $I_{4}'$ to ours and its conformal unit $I_{6}'$ to minus ours. If each tower's constituent unit is taken to be its own oriented conformal pseudoscalar, the mirror's constituent unit and field unit therefore have the opposite relative sign to ours, and the mirror is the parity image of this tower. That reading is interpretive and depends on the identification of the transported plane, which with one sign reversed would flip the sign of $I_{6}'$'s image. Nothing gravitational distinguishes the two.



**Theorem 28 (The mirror's temperature and premise P2).** T14 applies P2 along the reversal orbit to equate the ceiling coupling and the asymmetry per mode, both data of the descent \cite[Thm.~4.3(iv), (v)]{ButlerT14}. The energy the descent deposits per unit charge is a datum of the same kind, and P2 declares which of $2$, $6$ is visible to be indexical. Applied with the same reach, P2 gives $\xi = T'/T = 1$ and $\Delta\Neff = \tfrac{8}{7}(\tfrac{11}{4})^{4/3} + 3.044 = 7.45$ at recombination, excluded by a factor of about $25$. T14's mirror, cold from the gravitational floor upward \cite[Prop.~4.6, Prop.~A.2]{ButlerT14}, is therefore an exception to P2 that T14 neither states nor costs. Assembly level.

*Proof.* \textit{The reach of P2.}\enspace The equalities of T14's Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), (v) rest on P2's clause that a difference between two continuous data of one reversal orbit is an uncaused distinction. T14's Proposition A.2 (\claimref{dark-matter.seeding-gravity-floor-dark-towers-temperature}) calls what the descent deposited ``a datum, not a computation'', and T14's Proposition 4.6 (\claimref{dark-matter.stored-asymmetry-charge-not-number}) carries the mirror's temperature as such a datum, from the floor up to the $\Neff$ cap.



\emph{The number.}  At $\xi = 1$ the mirror is a full Standard-Model copy at the photon temperature. Its energy density is that of a photon, worth $\tfrac{8}{7}(\tfrac{11}{4})^{4/3}$ neutrino species, plus three neutrinos:
\[
\Delta\Neff \;=\; \underbrace{\tfrac{8}{7}\bigl(\tfrac{11}{4}\bigr)^{4/3}}_{\text{mirror photon}} \;+\; \underbrace{3.044}_{\text{mirror neutrinos}} \;=\; 4.40 + 3.044 \;=\; 7.45 \qquad \text{(K2)}.
\]




**Theorem 29 (The mirror's composition across its temperature range).** Decimal. Supplementary scripts: the mirror's (folder \file{MIR}, checks D1, D2 and E0 to E7) and the cosmology check's (folder \file{CHECK\_COS}). T14 carries $\xi$ from the gravitational floor ($2.8$ to $3.2 \times 10^{-4}$ at the top of the ceiling range) to the $\Neff$ cap ($0.448$), with a hot-deposit estimate near $4 \times 10^{-3}$.
\begin{enumerate}
\item[(i)] At the floor the mirror is charge-dominated and degenerate from the moment it is seeded: the Fermi energy its deposited baryon number must carry exceeds the floor's thermal deposit by $49$ to $84$, and at its weak freeze-out the quark chemical potential is $18$ to $23$ times its temperature. Beta equilibrium persists into the hadron phase, and for a copied lepton number $L \leq 0$ (our tower's sphaleron value $L/B = -51/28$, or zero) the mirror ends $96$ to $100$ percent neutrons. Its endpoint is cold, dense, neutron-rich matter; the composition after decay and capture needs a dense-matter network and is not computed here.
\item[(ii)] Between $\xi \approx 3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing T14's hot-deposit estimate, the mirror is helium ($Y' = 0.94$ to $1.00$).
\item[(iii)] Above that interval the helium fraction falls ($Y' = 0.85$ at $\xi = 0.1$) and towards the cap the mirror is hydrogen-rich ($Y' = 0.58$ at $\xi = 0.448$).
\end{enumerate}
T14 does not print a mirror $\eta'$ at freeze-out; its floor value $19$ to $26$ is the late-time ratio, and the thermal up-down ratio T14 assumes there is inconsistent with its own $\eta' > 1$.

*Proof.* Computed, as the source states, in the supplementary scripts \file{MIR} (checks D1, D2 and E0 to E7) and \file{CHECK\_COS}, across the range of the temperature ratio that \claimref{dark-matter.stored-asymmetry-charge-not-number} and \claimref{dark-matter.seeding-gravity-floor-dark-towers-temperature} supply, for the mirror that \claimref{dark-matter.mirror-tower-copy-one} makes a copy of this tower. The source gives no further proof text.




**Conjecture 30 (The mirror against the astrophysical record).** On every branch the mirror recombines early (at a visible temperature of $0.04$ to $3$ keV) and is cold dark matter for the microwave background and large-scale structure, and in galaxies it is a collisional gas that cools by bremsstrahlung in a few gigayears, settles partly and forms stars. Against the Gaia thin-disk bounds \cite{Widmark2021} and Roux and Cline's limit $\Omega_{b'} \lesssim 0.8\,\Omega_{b}$ \cite{RouxCline2020}, only the helium interval has room: there T14b's Galaxy models pass at the Sun only with helium-star feedback \cite[Obs.~9.1]{ButlerT14b}, and Roux and Cline's limit, which covers the whole helium interval, is exceeded by a factor $1.24$. Nothing in the construction lowers the mirror's share below $0.995$ or changes its microphysics without a further exception to P2: the copy is exact and the tension T14 records stands. Observation level, on imported galaxy modelling.

## From content to matter



**setting  (From content to matter).** This section uses imported physics, stated as such, and decimal estimates, labelled; every number is reproduced by Part K of the script or by the named supplementary check.



**Theorem 31 (The phases of the three-dimensional towers).** Imported: Polyakov confinement of a compact $U(1)$ with Maxwell dynamics \cite{Polyakov1977}; topological mass $e^{2}k/2\pi$ and the absence of confinement at nonzero Chern-Simons level \cite{DJT1982, AHPS1989}; flux attachment, with spin shifted by $q^{2}/2k$ \cite{Wilczek1982}. With the minimal bare level $|k| = \tfrac{1}{2}$ of Proposition \claimref{dark-tower-matter.anomalies}(i), each factor is in one of two phases, set by whether the cell's mass sign is aligned with its bare level:
\begin{enumerate}
\item[(C)] effective level $0$: Polyakov-confining; the cells bind into neutral onia that annihilate at full strength into a lighter channel;
\item[(T)] effective level $\pm 1$: topologically massive, the photon gapped at $e^{2}/2\pi$; the unit-charge lines are transparent and the cells become effectively neutral and, on the standard signs, spin $0$ (interpretive).
\end{enumerate}
In phase (T) with $e^{2} \gg m$ the cells are stable by their gauge charges (at $r = 7$ also by the algebra's central unit, Proposition \claimref{dark-tower-matter.residue-seven-unit}), and contact processes scale as $(m/e^{2})^{2}$. Assembly level. T14's Proposition 6.2 states that every compact $U(1)$ in three dimensions confines \cite[Prop.~6.2]{ButlerT14}; with the forced half-integral level that holds in phase (C) only. Both phases close T14's radiation channel: nothing light remains in phase (T), and even two massless $2+1$ dimensional photons at the photon temperature would give $\Delta\Neff$ of about $4 \times 10^{-3}$ on sheets (supplementary \file{CHECK\_COS}).

*Proof.* Follows from \claimref{dark-tower-matter.anomalies}(i) (the minimal bare level), \claimref{dark-tower-matter.three-dimensional-content} (the cells and their charges) and, for $r = 7$, \claimref{dark-tower-matter.residue-seven-unit}, together with the imported results the source names (Polyakov confinement; the topological mass and the absence of confinement at nonzero level, after Deser, Jackiw and Templeton and Affleck, Harvey, Palla and Semenoff; flux attachment, after Wilczek), as the source states. Those imported results are not in the store.




**Theorem 32 (Survival of sheet relics against annihilation).** Decimal. On a sheet the comoving number per unit area and the expansion rate both fall as $a^{-2}$ in radiation domination, so two-dimensional s-wave annihilation with $\sigma_{1}v = 2P/m$ ($P$ the absorption probability per encounter) depletes a symmetric population logarithmically, $1/N_{f} = 1/N_{0} + (2P/m)\ln(a_{f}/a_{i})/(a^{2}H)$. At R2's density a symmetric sheet relic keeps $99$ percent of its number only for $P \lesssim 2 \times 10^{-16}$; at $P = 1$ about $10^{-14}$ survives (K3). In phase (T) this needs $e^{2}/m > 7 \times 10^{7}$, which also makes the relic collisionless in clusters (threshold $5.9 \times 10^{6}$, from the in-sheet phase-shift bound $1.7 \times 10^{-7}$ of T14b's cluster computation \cite[Comp.~3.3, Prem.~2.12]{ButlerT14b}) (K4). Phase (C) fails R2 by itself.

*Proof.* Follows from R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball})'s density (\claimref{dark-tower-matter.imported-unit-ball-rule}), the phases (T) and (C) of \claimref{dark-tower-matter.three-dimensional-phases} and the in-sheet phase-shift bound of \claimref{simulations.cluster-bound-two-dimensions}, as the source states; the decimal estimates are those the source cites to its script (K3, K4).




**Theorem 33 (The five-dimensional towers in cosmology and halos).** Decimal, with imports as stated. With the fifth direction one cell radius deep and co-expanding (R3; \cite[Rem.~7.9, Rem.~7.14]{ButlerT14}):
\begin{enumerate}
\item[(i)] $LT$ runs from about $390$ (at $g_{s} = 106.75$) to $1170$ today: the Kaluza-Klein spacing is always below $T/120$, so the towers are five-dimensional at the visible temperature and at their matter's mass scale (K5); at T14's small dark temperatures the dark bath itself is only a few Kaluza-Klein levels deep.
\item[(ii)] Five-dimensional gauge theory is infrared free; reducing to four dimensions gives a confinement scale below $\pi/L$ by a factor smaller than $e^{-250}$ even at strong coupling (K7), and the $1/r^{2}$ potential binds nothing unless the theory is within a factor of about eight of strong coupling at the quark mass (supplementary \file{D5C}, H3; \cite{CLP2000}). There are no dark hadrons and no dark atoms.
\item[(iii)] With the Kaluza-Klein tower populated, $\Delta\Neff < 0.3$ needs $T_{D}/T_{\gamma} < 0.085$ for the nine vectors of $\uu(3)$ ($0.13$ for one photon), not the $0.46$ to $0.51$ of T14's zero-mode formula \cite[Prop.~6.3]{ButlerT14}; a sector decoupled at a GeV would give about $670$ (K6). T14's own temperature estimates meet the corrected bound by orders.
\item[(iv)] Two-body scattering is collisionless by geometry, $\sigma_{\mathrm{eff}}/m = \sigma_{5}/(Lm) < 10^{-8}\ \mathrm{cm^{2}\,g^{-1}}$ even for charged and coloured species (supplementary \file{D5C}, H9).
\item[(v)] With no boundary term in the series the gauge field's natural condition at the ends of the fifth direction keeps a four-dimensional zero mode, so beyond about a metre the charged species form a neutral dark plasma. Published plasma-instability limits \cite{SSS2024, PIC2024}, rescaled to a GeV, lie six to ten orders below the coupling a freeze-out relic needs and about two to five orders below a deposit at a natural five-dimensional coupling (supplementary \file{D5C}, Section 14, and \file{CHECK\_COS}). Whether such instabilities transfer bulk momentum in a merger is not established \cite{Lasenby2020}: an exposure, not an exclusion.
\item[(vi)] If the neutral species $N$ (Proposition \claimref{dark-tower-matter.five-dimensional-content}) carries R2's count as a deposit and the charged species annihilate at weak coupling, the tower carries no long-range charge and is collisionless whatever the zero modes do. Under Premise \claimref{dark-tower-matter.u-transposition-rule} this branch is open to both five-dimensional towers.
\end{enumerate}
The relic is a symmetric gas of free spin-$\tfrac{1}{2}$ dark quarks and leptons, or of $N$ alone. The lightest species is stable by fermion parity, the lightest quark and lepton by species numbers broken only at the rung scale.

*Proof.* Follows from \claimref{dark-tower-matter.gauge-algebras} (the nine vectors of $\uu(3)$) and \claimref{dark-tower-matter.five-dimensional-content} (the neutral species $N$), with the fifth direction fixed by premise R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}) and clause (vi) under Premise \claimref{dark-tower-matter.u-transposition-rule}, as the source states. The decimal estimates are those the source cites to its script (K5 to K7) and to the supplementary script \file{D5C}; the imported results it names (five-dimensional strong coupling, plasma-instability limits) are not in the store.




**Theorem 34 (R1 has no mechanism in the odd towers).** In this tower and the mirror a quantum's mass is a confinement scale, $m = c\Lambda$ \cite[Prop.~4.7]{ButlerT14}. In the three-dimensional towers the gauge algebra is abelian and the coupling dimensionful, so there is no dimensional transmutation and the cells' masses are bare parameters; the viable phase needs $m/e^{2} \lesssim 1.4 \times 10^{-8}$, which nothing in the content protects (no chirality; parity broken by the forced Chern-Simons level). In the five-dimensional towers nothing confines (Proposition \claimref{dark-tower-matter.five-dimensional-towers}(ii)) and the quanta are elementary with bare masses. So T14's R1, equal mass per quantum, has no mechanism for about $81$ percent of the dark matter and is a premise about bare masses there. Assembly level.

*Proof.* Follows from \claimref{dark-matter.mirror-share-one-how-fragile} ($m = c\Lambda$ in this tower and the mirror), \claimref{dark-tower-matter.gauge-algebras} (abelian in three dimensions), \claimref{dark-tower-matter.three-dimensional-content} (no chirality), \claimref{dark-tower-matter.anomalies} (the forced Chern-Simons level), \claimref{dark-tower-matter.survival-sheets} (the viable phase), \claimref{dark-tower-matter.five-dimensional-towers}(ii) and the shares of \claimref{dark-tower-matter.imported-unit-ball-rule}, as the source states.




**Theorem 35 (How the odd towers could be populated).** The odd towers carry no asymmetry (Fact \claimref{dark-tower-matter.imported-towers-their-types}). Their matter is therefore symmetric, and R2's density must be either a count deposited by the descent and protected from annihilation by kinematics or weakness (Propositions \claimref{dark-tower-matter.survival-sheets}, \claimref{dark-tower-matter.five-dimensional-towers}(vi)), or, in the five-dimensional towers, a weak-coupling freeze-out with the coupling tied to the deposit temperature. Neither is derived. Assembly level.

*Proof.* Follows from \claimref{dark-tower-matter.imported-towers-their-types} (no asymmetry in the odd towers), \claimref{dark-tower-matter.survival-sheets} and \claimref{dark-tower-matter.five-dimensional-towers}(vi), with R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball})'s density from \claimref{dark-tower-matter.imported-unit-ball-rule}, as the source states.


## The sterile towers





**Theorem 36 (The kinematics of the sterile towers).** \begin{enumerate}
\item[(i)] In $\R^{2,2}$ the orthogonal complement of every non-null vector is nondegenerate and indefinite, so every vector, of either sign of $Q$, is a sum of two null vectors $v = (\tfrac{1}{2}v + w) + (\tfrac{1}{2}v - w)$ with $w \perp v$, $Q(w) = -Q(v)/4$; and the null cone minus the origin is connected, so it has no invariant future half.
\item[(ii)] In $\R^{4,0}$ (and $\R^{0,4}$) the only null vector is zero: there is no massless constituent, no time and no evolution.
\end{enumerate}

*Proof.* \textit{(i) Sums of null vectors.}\enspace For non-null $v$, $v^{\perp}$ is three-dimensional, of signature $(1,2)$ if $Q(v) > 0$ and $(2,1)$ if $Q(v) < 0$, since the counts of \claimref{std-algebra.sylvester-inertia} add over $V = \R v \perp v^{\perp}$. Either way $Q$ is indefinite on it, so it takes the value $-Q(v)/4$ at some $w \perp v$, and then
\[
Q\bigl(\tfrac{1}{2}v \pm w\bigr) \;=\; \tfrac{1}{4}Q(v) + Q(w) \;=\; \tfrac{1}{4}Q(v) - \tfrac{1}{4}Q(v) \;=\; 0
\]
(J1, which also checks nondegeneracy and indefiniteness on random vectors, and J2, which exhibits sums of both signs).



\emph{(i) The cone is connected.}  In coordinates $(t_{1}, t_{2}; x_{1}, x_{2})$ with $Q = t_{1}^{2} + t_{2}^{2} - x_{1}^{2} - x_{2}^{2}$, the null cone minus the origin is
\[
\bigl\{\, |t| = |x| > 0 \,\bigr\} \;\cong\; S^{1} \times S^{1} \times \R_{>0},
\]
which is connected. In signature $(1,3)$ the same set has the two components $t_{0} > 0$ and $t_{0} < 0$. T16 proves the corresponding statement for the timelike sets \cite[Lem.~4.4]{ButlerT16}.



\emph{(ii)}  $Q$ is a sum of four squares, so $Q(v) = 0$ only at $v = 0$ (J3).


**Remark  (The Kleinian algebra).** At $r = 0$ the constituent field is $\R$ (Theorem \claimref{dark-tower-matter.constituents-field}), and $\Cl^{0}(2,2) \cong \Mat_{2}(\R) \oplus \Mat_{2}(\R)$ has two inequivalent spinor ideals. There is no time direction, so no adjoint and no norm clause: a momentum bilinear in one element of each ideal is preserved by acting with $U$ on the elements of the first ideal and $U^{-T}$ on those of the second, for every $U \in GL(n,\R)$ (supplementary \file{STE}, checks C4, C5). Under H2 with this slot group the gauge algebra is the split form $\sll(2,\R) \oplus \sll(3,\R) \oplus \gl(1,\R)$, of dimension $12$, whose simple factors have indefinite Killing forms, signatures $(2,1)$ and $(5,3)$ (E5): there is no positive gauge-kinetic energy. T14's ``Kleinian copy of the Standard Model'' \cite[Cor.~3.11]{ButlerT14} needs a compact weak factor, which does not preserve that bilinear. Assembly level.

**setting  (The sterile towers).** Both sterile towers are empty under T14's Premise P3, which is what the unit-ball rule's agreement with the observed ratio assumes: a populated $r = 0$ at share one would move the total to $6.36$, fifteen standard deviations from the observed $5.364 \pm 0.065$ \cite{Planck2018}.

## The dark sector as built, against the data





**Conjecture 37 (The dark towers as built, against the data).** \begin{center}\small
\begin{tabular}{@{}p{3.6cm}p{10.2cm}@{}}
\toprule
test & status \\
\midrule
$\Delta\Neff < 0.3$ & met on every branch except a hot mirror ($\xi = 1$, $7.45$) and a five-dimensional sector decoupled at a GeV (about $670$) \\
cluster mergers & passes in T14b's runs only if the mirror is the only colliding component (Fact \claimref{dark-tower-matter.imported-cluster-simulations}); that needs both three-dimensional towers in phase (T) at strong coupling with an unprotected light mass, and both five-dimensional towers collisionless (neutral-$N$ deposit, couplings weak near the unification scale, or ends the series does not supply). With zero modes and charged relics in both five-dimensional towers the colliding fraction would be $50.2$ percent, the fraction of T14b's failing mixed-count runs; with one, $34.4$ percent, above the $31.6$ percent run that already loses about half the subcluster's central mass. The extrapolation from fluids to a plasma is itself unproved \\
mirror bounds & marginal at best, in the helium interval with helium-star feedback, still $1.24$ above Roux and Cline; the helium interval itself needs an exception to P2 \\
R1 & a premise about bare masses in the odd towers; it holds only for the mirror \\
\bottomrule
\end{tabular}
\end{center}
No configuration of the five towers as built is compatible with every test at face value. The least exposed configuration needs four choices the series does not make (a P2 exception for the mirror's temperature, boosted mirror feedback, strong coupling with an unprotected light mass in the three-dimensional towers, and collisionless five-dimensional relics), and even with them it stays marginal, $1.24$ above Roux and Cline's limit. Observation level.

## What this note depends on, and what would refute it



**setting  (What this note depends on, and what would refute it).** \emph{Proved here, at proof level:} Theorem \claimref{dark-tower-matter.constituents-field}, Lemma \claimref{dark-tower-matter.adjoint-norm}, Theorems \claimref{dark-tower-matter.where-mass-begins}, \claimref{dark-tower-matter.ladder}, \claimref{dark-tower-matter.third-pairs-unit-five-dimensions} and \claimref{dark-tower-matter.mirror-algebra}, Proposition \claimref{dark-tower-matter.pairs}, Proposition \claimref{dark-tower-matter.residue-seven-unit}(i) to (iii) up to its last clause, Proposition \claimref{dark-tower-matter.sterile-kinematics}, and the algebra in Theorem \claimref{dark-tower-matter.gauge-algebras} and Propositions \claimref{dark-tower-matter.three-dimensional-content}, \claimref{dark-tower-matter.five-dimensional-content}, \claimref{dark-tower-matter.anomalies}.

\emph{Assembly, under named premises:} that the algebras of Theorem \claimref{dark-tower-matter.gauge-algebras} are gauge algebras (H2), that a constituent's momentum is $j$ of its spinor part off dimension four (H1), the constituent-level content (S), the transposition rule (U), and Propositions \claimref{dark-tower-matter.mirrors-temperature-p2}, \claimref{dark-tower-matter.three-dimensional-phases}, \claimref{dark-tower-matter.r1-has-no-mechanism-odd-towers}, \claimref{dark-tower-matter.population}, Remark \claimref{note.dark-tower-matter.kleinian-algebra}.

\emph{Decimal:} Computation \claimref{dark-tower-matter.mirrors-composition}, Propositions \claimref{dark-tower-matter.survival-sheets}, \claimref{dark-tower-matter.five-dimensional-towers}, Observation \claimref{dark-tower-matter.towers-built}.

\emph{Interpretive:} the mirror as parity image; the spin $0$ of the dressed three-dimensional cells.

\emph{What would refute the constructions.} A spin-irreducible constituent ideal whose spin commutant differs from Theorem \claimref{dark-tower-matter.constituents-field}'s; a nonzero element of $S$ in dimension three or four with $\rev{\psi}\psi \neq 0$; an element of $\HH$ outside $\mathrm{span}\{1, I_{7}\}$ at $r = 3$ commuting with the $I_{7}$-built pair algebra. Each is a finite computation the script performs.

\emph{What would refute the physics.} A thin dark disk or bulge component excluding a mirror of $0.995\,\Omega_{b}$ in the helium interval with helium-star feedback refutes T14's mirror; a demonstration that dark plasma instabilities transfer bulk momentum in cluster mergers, with gauge zero modes in the five-dimensional towers, refutes the composition unless their relic is the neutral species; a measured $\Delta\Neff$ excess attributable to a dark sector would place a five-dimensional tower above $0.085$ of the photon temperature, outside T14's estimates.

\emph{Successor problems.} (1) Whether the cold mirror is a stated exception to P2, and where in T14's interval $\xi$ lies. (2) A footing for R1 in the odd towers, or a replacement. (3) The boundary data of the five-dimensional towers' fifth direction (zero modes or not) and their population mechanism. (4) The three-dimensional phase and coupling. (5) Hypothesis (S) off dimension four, the same missing theorem as in this tower. (6) The family count in the odd towers, where the maximal-composite bound of T13 \cite[Conj.~3.1]{ButlerT13} does not transpose. (7) The $r = 5$ unit: datum or field. (8) Whether the five-dimensional pair unit is internal (U3) or external, which decides between $\uu(3)$ and the Standard-Model algebra in both towers. (9) The $SU(3)$ and mixed Chern-Simons levels of the five-dimensional content.

## Position in the series



**setting  (Position in the series).** This paper is T14c of the series, a companion to the dark-matter paper T14 \cite{ButlerT14}, downstream of its Theorem 3.4 (types by residue), Proposition 4.1 (superselection), Theorem 4.3 (the mirror copy), Theorem 3.10 (no orientation bit in odd dimension) and its unit-ball rule (Section 7). It runs the construction of the Standard-Model paper T12 \cite{ButlerT12} in each tower, using the mass formula of the mass paper T11 \cite{ButlerT11}, the rungs and canonical relations of the tower paper T3 \cite{ButlerT3}, and, for comparison only, the families of T13 \cite{ButlerT13} and the neutrino sector of T15 \cite{ButlerT15}. Its physical tests take the simulations of the companion note T14b \cite{ButlerT14b} as given; the companion note T14a \cite{ButlerT14a} is upstream of nothing here. The cone fact for signature $(2,2)$ is the foundations paper T16's \cite{ButlerT16}. The capstone T17 \cite{ButlerT17} records T14's predictions; the section ``What this note depends on, and what would refute it'' lists what this note adds to them.

## Machine verification



**setting  (Machine verification).** The script \file{verify\_T14c.py} \cite{ButlerVerifyT14c} imports the series library \file{GA.py} and checks the computational statements of Sections 3 to 10 in exact arithmetic: rational numbers, and a small polynomial ring over $\mathbb{Q}$ in which the identities of Lemma \claimref{dark-tower-matter.adjoint-norm} and Theorems \claimref{dark-tower-matter.where-mass-begins} and \claimref{dark-tower-matter.ladder} are verified as polynomial identities in the spinors' coordinates rather than on samples. Part K alone is decimal and labelled. Without the supplementary scripts it runs $57$ checks, all passing:

\begin{center} \begin{tabular}{@{}lll@{}}
\toprule
Part & statements & checks \\
\midrule
A & Theorem \claimref{dark-tower-matter.constituents-field} & A1 to A5 \\
B & Lemma \claimref{dark-tower-matter.adjoint-norm}, Theorem \claimref{dark-tower-matter.where-mass-begins} & B0 to B7 \\
C & Theorem \claimref{dark-tower-matter.ladder} & C1, C2 \\
D & Proposition \claimref{dark-tower-matter.pairs}, Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions} & D1a, D1b, D2 to D12 \\
E & Theorem \claimref{dark-tower-matter.gauge-algebras}, Remark \claimref{note.dark-tower-matter.kleinian-algebra} & E1 to E5 \\
F & Propositions \claimref{dark-tower-matter.three-dimensional-content}, \claimref{dark-tower-matter.five-dimensional-content} & F1 to F4 \\
G & Proposition \claimref{dark-tower-matter.anomalies} & G1 to G3 \\
H & Proposition \claimref{dark-tower-matter.residue-seven-unit} & H1 to H4 \\
I & Theorem \claimref{dark-tower-matter.mirror-algebra} & I1 to I3 \\
J & Proposition \claimref{dark-tower-matter.sterile-kinematics} & J1 to J3 \\
K & Propositions \claimref{dark-tower-matter.mirrors-temperature-p2}, \claimref{dark-tower-matter.survival-sheets}, \claimref{dark-tower-matter.five-dimensional-towers}; Fact \claimref{dark-tower-matter.imported-unit-ball-rule} (decimal) & K1 to K7 \\
\bottomrule
\end{tabular}
\end{center}

Part L runs the supplementary derivation scripts deposited with the paper in the folders \file{MIR}, \file{D3R}, \file{D3C}, \file{D5C}, \file{D5Q}, \file{STE} (one per tower: $24$, $61$, $78$, $86$, $106$ and $68$ checks) and two independent checks, \file{CHECK\_ALG} ($50$ exact checks) and \file{CHECK\_COS} (decimal), and requires each to be present and to run clean, twelve further checks ($69$ in all). The paper cites them for the decimal composition of the mirror (Computation \claimref{dark-tower-matter.mirrors-composition}), the five-dimensional binding, scattering and plasma estimates (Proposition \claimref{dark-tower-matter.five-dimensional-towers}), the invariant forms of Corollary \claimref{dark-tower-matter.same-kind-matter}, the branches of Remark \claimref{note.dark-tower-matter.branches-break-u-what-they-give}, the Kleinian ladder of Remark \claimref{note.dark-tower-matter.kleinian-algebra}, the transported weights of Proposition \claimref{dark-tower-matter.three-dimensional-content}(iii) and the sheet radiation of Proposition \claimref{dark-tower-matter.three-dimensional-phases}. What no script checks: the statement after Theorem \claimref{dark-tower-matter.gauge-algebras} about the mirror (T14's), the imported physics (Redlich's shift, Polyakov, topological mass, flux attachment, five-dimensional Chern-Simons quantisation, plasma instabilities) and the galaxy modelling of T14b.

## Results cited, not shown

**Fact (imported) 38 (The flag bit exists exactly at tower dimension $0 \bmod 4$).** Let a tower have dimension $n$ and conformal completion with ambient $V$ of dimension $n + 2$, and let $W, W' \subset V_{\C}$ be a Witt pair, the two halves of Definition \claimref{obj.dark-matter.witt-flag} taken coherently across the pairs, with pure spinors the null blade $f$ and the top state (Definition \claimref{obj.dark-matter.null-blades-fock-ideal-chirality}). Then the choice between $W$ and $W'$ is a discrete invariant of the connected conformal spin group, a \emph{bit}, if and only if $n \equiv 0 \pmod 4$ (ambient dimension $2m$ with $m$ odd), and the bit is the chirality of the pure spinor, that is, the parity of the Fock grade of the complementary half's pure spinor ($0$ for $f$, $m$ for the top state). (i) The odd residues are odd-dimensional for every signature in the class, so the ambient is odd-dimensional, the pseudoscalar central, an even versor carries $W$ to $W'$, and the spin algebra mixes the Fock grades: no bit, on any window. (ii) The even residues carry the bit exactly at tower dimension $0 \bmod 4$: under Premise \claimref{dark-matter.p3-nearest-dimension-representatives} all four are at dimension four and carry it; the causal representatives of the alternative windows of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}(iii), $(1,1)$ of $r = 0$ and $(1,5)$ of $r = 4$, do not. So the towers that can be oriented are the even residues $\{0, 2, 4, 6\}$ given P3, and the odd residues cannot be, given nothing.

*Provenance:* Transport Lab claim dark-matter.flag-bit-exists-exactly-tower-dimension, version 3 (T14 Thm 3.10).

**Fact (imported) 39 (The mirror share is one, and how fragile that is).** Write $m_{r} = c_{r}\Lambda_{r}$, with $\Lambda_{r}$ the confinement scale of tower $r$'s non-abelian sector and $c_{r}$ the constituent factor of its lightest charge-carrying composite.
\begin{enumerate}
\item[(i)] \emph{(The mirror.)} By Theorem \claimref{dark-matter.mirror-tower-copy-one}(iii), $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$ exactly, hence $f_{2} = 1$ under P4, which Theorem \claimref{dark-matter.mirror-tower-copy-one}(v) discharges for the mirror, an isomorphism of theories rather than a one-loop statement. As a ratio of mass densities it is a ratio of mean mass per baryon: ours is about $936.7$ MeV after helium, a mirror burnt entirely to helium (the completion limit of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}'s burning branch) gives $931.8$ MeV, so $f_{2}$ is $0.995$ in that limit and $1$ on the proton-only branch, a one-sided systematic of half a percent at assembly level. Caveat (T14c): the two branches bracket the share where the mirror is helium or protons; at the gravitational floor the mirror is degenerate and, for a copied lepton number $L \leq 0$, ends $96$ to $100$ percent neutrons, a composition neither branch describes, and it is helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$ (Computation \claimref{dark-tower-matter.mirrors-composition}); the half-percent bracket is established there and not at the floor.
\item[(ii)] \emph{(Fragility.)} The equality is unstable to any departure from the copy. Suppose the two towers shared a ceiling $M$ and coupling but differed in light content by $\Delta b$ over the running range, with $b_{6} \leq 11$; then at one loop
\[
\ln\frac{\Lambda_{2}}{\Lambda_{6}} \;\geq\; \frac{\Delta b}{b_{6} + \Delta b}\,\ln\frac{M}{\Lambda_{6}}.
\]
One Dirac flavour is $\Delta b = 2/3$, which with $\Lambda_{6} = 0.3$ GeV moves the mirror share by a factor between $4.89$ (bottom of the ceiling range, $b_{6} = 11$) and $21.4$ (top, $b_{6} = 7$), past the observed $5.364$ everywhere except at the bottom of the range on the most conservative branch. A coupling departure $\delta = \alpha_{2}(M)^{-1} - \alpha_{6}(M)^{-1}$ at the ceiling with identical content moves $\Lambda_{2}/\Lambda_{6}$ by $e^{-2\pi\delta/b}$, a factor $2.45$ per unit at $b = 7$, so the share stays within ten percent of one only for $|\delta| < 0.106$. So $f_{2} = 1$ is exact, P2-protected, and fragile.
\item[(iii)] \emph{(The odd towers.)} In three and five dimensions the gauge coupling is dimensionful and the confinement scale is set by the coupling itself ($\Lambda_{3} \sim g_{3}^{2}N$, $\Lambda_{5} \sim 1/g_{5}^{2}$), so nothing about $\Lambda_{1,7,3,5}$ follows without a rule the series does not derive (Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}); the unit-ball rule of the section ``The dark matter ratio: the unit-ball rule'' constrains that rule, as shares per unit of our volume, without supplying it.
\end{enumerate}
Level: (i) is Theorem \claimref{dark-matter.mirror-tower-copy-one}; (ii) is one-loop arithmetic under its stated assumptions, flagged; (iii) is a scope statement.

*Provenance:* Transport Lab claim dark-matter.mirror-share-one-how-fragile, version 6 (T14 Prop 4.7).

**Fact (imported) 40 (The mirror tower is a copy of this one).** Every item of Fact \claimref{dark-matter.imported-inputs-standard-model-chain} is invariant under the signature reversal $(p,q) \mapsto (q,p)$ that carries this tower's signature $(1,3)$ to the mirror's $(3,1)$ (the proof runs the list item by item; the tractor bundle over a $(3,1)$ conformal structure has ambient $\R^{4,2}$ and the same complexified fibre, Hypothesis (S) has no signature in it, and one-loop running depends on the content alone). Hence:
\begin{enumerate}
\item[(i)] the mirror tower's derived content is a copy of this tower's: gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$, the same global form, the same generation with the same hypercharges and the same chirality halves, including a massless mirror photon and mirror neutrinos;
\item[(ii)] the ground type (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}: $\R$ for the mirror, $\mathbb{H}$ for this tower) does not enter: the derivation uses the conformal spin group and its complex representations, never the tower's real Clifford module;
\item[(iii)] the mirror's light content, and therefore its $\beta$-functions at every scale, equal this tower's, so that with a common ceiling $M$ and a common coupling there its confinement scale and composite spectrum equal ours exactly, $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$, and under P4, which (v) discharges for the mirror, its tower factor is $f_{2} = 1$ up to the ratio of mean mass per baryon of the two sectors, which their nuclear histories set (one on the proton-only branch, $0.995$ on the burning branch, Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i)): $\Omega_{\mathrm{mirror}} = \Omega_{b}$ to half a percent;
\item[(iv)] the common coupling in (iii) is where this theorem applies P2 across towers: the reversal is the automorphism of the configuration along whose orbit Premise \claimref{dark-matter.p2-indifference} equates, so a coupling difference at the ceiling would be an uncaused distinction between the two members of one orbit, which the audit forbids; the odd towers, off that orbit relative to this one, get no such licence;
\item[(v)] the asymmetry per mode is equal in the two towers, $\epsilon_{2} = \epsilon_{6}$, by two routes, both carried: by the audit, as in (iv), a difference between two continuous data of one reversal orbit being an uncaused distinction; and, more weakly (isomorphic theories share the function, not thereby the value of a datum of theory plus initial condition), by inheritance, both towers being oriented by the one flag under Premise \claimref{dark-matter.p1-single-frozen-point}'s orientation clause. So Premise \claimref{dark-matter.p4-democracy-asymmetry-over-oriented-towers} is discharged for the mirror, and the share of one in (iii) rests on P1, P2 and the copy.
\end{enumerate}
This is mirror matter in the sense of the literature \cite{FootMirror2004}, derived rather than posited: the framework's $r = 2$ tower is a second Standard Model.

Caveat (T14c): applied with the reach used in (iv) and (v), Premise P2 also equates a third datum of the descent along the same orbit, the energy deposited per unit charge, and so gives $\xi = T'/T = 1$ and $\Delta\Neff = 7.45$ at recombination, which the record excludes (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}). The cold mirror the paper carries is therefore an exception to P2 that this theorem does not state; (i) to (iii) stand, and (iv) and (v) hold as equalities under P2 only alongside that exception.

*Provenance:* Transport Lab claim dark-matter.mirror-tower-copy-one, version 8 (T14 Thm 4.3).

**Fact (imported) 41 (Seeding by gravity: the floor on a dark tower's temperature).** By exact superselection the towers interact only through the shared metric (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}), so after the descent a dark tower can be heated only gravitationally; what the descent itself deposited in it (its charge, Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, with whatever energy the deposit carried) is a datum, not a computation. Let the descent reheat this tower to $T_{\mathrm{desc}}$ and let tower $r$, with $g_{d}$ light degrees of freedom that thermalise among themselves, be heated by graviton-mediated production from the visible plasma at rate per volume $\Gamma = c\,T^{8}/M_{P}^{4}$, with $c$ the sum of Fact \claimref{dark-matter.imported-massless-graviton-production-rate}'s per-species coefficients over the tower's light content. Then the produced comoving yield is
\[
Y \;=\; \frac{c\,T_{\mathrm{desc}}^{3}}{3\,\kappa_{s}M_{P}^{3}}, \qquad \kappa_{s} = \sqrt{\frac{\pi^{2}g_{*}}{90}}\;\frac{2\pi^{2}}{45}\,g_{s} \;=\; 145.3 \ \text{at } g_{*} = g_{s} = 100,
\]
its energy fraction at production is $4Y$, and the temperature ratio it alone would give is
\[
\xi_{\mathrm{floor}} \;=\; \Big(4Y\,\frac{g_{*}}{g_{d}}\Big)^{1/4} \;=\; 9.6 \times 10^{-4}\; c^{1/4}\Big(\frac{16}{g_{d}}\Big)^{1/4}\Big(\frac{T_{\mathrm{desc}}}{6 \times 10^{14}\ \mathrm{GeV}}\Big)^{3/4}
\]
for $g_{*} = g_{s} = 100$ at the reheating. This is a floor: the tower's bath cannot be colder, and it is hotter by whatever energy the deposit carried. The ratio thereafter evolves through the two sectors' separate entropy conservation, by
\[
\left(\frac{g_{d}^{\mathrm{seed}}}{g_{d}}\right)^{1/3}\left(\frac{g_{s}}{g_{s}^{\mathrm{seed}}}\right)^{1/3}
\]
at any later epoch. Two inputs are not fixed by the formula: $T_{\mathrm{desc}}$, the ceiling of Proposition \claimref{dark-matter.ceiling-valued-inherited-success} or below it, so that across that range the floor spans a factor $(3.5 \times 10^{11}/6 \times 10^{14})^{3/4}$, about $4 \times 10^{-3}$ ($3.75 \times 10^{-3}$), the body quoting the top and saying so; and the deposit's energy, which sets the actual ratio above the floor.

*Provenance:* Transport Lab claim dark-matter.seeding-gravity-floor-dark-towers-temperature, version 4 (T14 Prop A.2).

**Fact (imported) 42 (The stored asymmetry is a charge, not a number).** Under the classification of Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, with $\epsilon$ initial data of the descent, inherited rather than generated, and the number $N$ common to the towers under P1 ($N = M_{P}/H$, which fixes the boundary mode count, about $\pi N^{2}/\ln 2$, without being it: Observation \claimref{standard-model.largeness-number-universes-boundary-modes}; the argument uses only that $N$ is common):
\begin{enumerate}
\item[(i)] \emph{(Charge.)} The asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, fixed by the descent's data and independent of the tower's temperature; it is not a thermal number $n - \bar{n} \propto g\,\mu T^{2}$. So the mirror share $f_{2} = 1$ holds at any mirror temperature: a cold mirror carries the same baryon charge as this tower in the same number of baryons, with negligible mirror radiation.
\item[(ii)] \emph{(Origin.)} The charge is the descent's and cannot be produced afterwards: the one channel superselection leaves open, gravitational production from the visible plasma (the section ``Seeding by gravity, and why no coupling rule follows''), yields $1.8$ to $2.7 \times 10^{-15}$ mirror quanta per unit entropy at the ceiling reheating against the $8.7 \times 10^{-11}$ baryons per unit entropy that our baryon number requires, more than four orders too few even counting every produced quantum as a baryon. Black holes are a sink for $Q$, not a source (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}(iv), under P5): a mass-preserving rearrangement that erodes each tower's free baryon count and moves no share.
\item[(iii)] \emph{(Temperature.)} Taken as a free datum of the descent, which by Proposition \claimref{dark-tower-matter.mirrors-temperature-p2} is an exception to P2 (applied with the reach of Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), (v), P2 gives $\xi = 1$, which the record excludes), the mirror's temperature ratio $\xi = T'/T$ is bounded below by the gravitational floor, $\xi$ between $2.8$ and $3.2 \times 10^{-4}$ at the ceiling reheating (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(ii), the bracket the species-counting ambiguity; four parts in a thousand of this at the bottom of the ceiling range), and above by the $\Neff$ cap at $0.448$; a deposit of each unit of baryon number with energy of order the reheating temperature puts it at $\xi \approx 4 \times 10^{-3}$. The paper carries the whole interval. With $\eta = n_{B}/n_{\gamma} = 6.1 \times 10^{-10}$ here and equal baryon number,
\[
\eta' \;=\; \frac{\eta}{\xi^{3}}
\]
runs from $19$ to $26$ at the floor down to about $0.008$ at the hot deposit, crossing one at $\xi = \eta^{1/3} = 8.5 \times 10^{-4}$: at least $10^{7}$ times ours throughout, with $\Delta\Neff$ eight orders or more below the cap.
\item[(iv)] \emph{(The two readings.)} The thermal reading would give $f_{2} \sim \xi_{2}^{3}$ instead, at most $0.090$ under the $\Neff$ cap ($0.448^{3}$) and $10^{-7}$ or less anywhere in the interval; the two readings cannot both hold, and the paper's own classification decides for the charge.
\end{enumerate}
Level: the classification is Fact \claimref{dark-matter.imported-trichotomy-descents-data}'s; the incompatibility is arithmetic. The mirror's nucleosynthesis, which is not a copy of ours and on which the burning branch of Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i) and the composition caveat of refutation item 6 rest, follows the proof, at assembly level. Caveat (T14c): the proof's thermal up-down ratio at freeze-out fails at the floor, where the mirror is degenerate and, for a copied lepton number $L \leq 0$, ends $96$ to $100$ percent neutrons; it is helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing the hot-deposit estimate (Computation \claimref{dark-tower-matter.mirrors-composition}). The burning branch is therefore not the floor's composition.

*Provenance:* Transport Lab claim dark-matter.stored-asymmetry-charge-not-number, version 7 (T14 Prop 4.6).

**Fact (imported) 43 (Superselected, hence dark and exactly stable).** By Premise \claimref{dark-matter.p1-single-frozen-point} and the acoustic programme (Fact \claimref{dark-matter.imported-gravity-only-coupling}, the series' acoustic no-go, at its mixed level: within the s-wave current algebra, with the sphere step conditional on the Indifference premise and the thermal state on premise (Q)), matter in a neighbouring tower gravitates on this metric and does nothing else observable at first order: dark by structural necessity, at that level. Stability is then not suppressed but exact, in three steps, the first of which is proved given the sector decomposition of Definition \claimref{obj.dark-matter.frozen-phase-operators}.
\begin{enumerate}
\item The tower charge $r$ is superselected in the frozen phase: frozen-phase operators are built from the one soldering and preserve its signature (Theorem \claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}), so portal matrix elements between residues vanish identically away from walls.
\item The walls are unreachable: singular loci ascend within-tower, since the completion adjoins exactly $(1,1)$ and preserves the residue (Fact \claimref{dark-matter.imported-eight-towers-mod-8-clock}), while the mod-8 shadow walls that separate residues are displaced successively away from the physical region, by the wall-sequence theorem of the sheaf paper \cite[\S5]{ButlerT4}, under that theorem's hypotheses (a compact base and good couplings at every stage), carried here.
\item Therefore the only inter-tower event in the universe's history is the descent itself: the towers communicated once, at the origin, and have been in absolute mutual darkness but for weight ever since. The singular locus of a black hole is an inter-tower event for energy, as it already was for weight, and never for the residue of any quantum: energy crosses at the wall, the residue does not (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}).
\end{enumerate}
One residue is flagged at observation level: dark-tower matter crossing this tower's horizons carries superselected charge the four-dimensional boundary mode space cannot hold, which routes it into the tower-wise run of the singularity paper's ascend-then-descend structure \cite{ButlerT5}; the computation of that routing, with the mass range of its Gauss-law clause, is Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}.

*Provenance:* Transport Lab claim dark-matter.superselected-hence-dark-exactly-stable, version 5 (T14 Prop 4.1).

**Fact (imported) 44 (Towers are residues, and the single-clock filter).** The residue $r = p - q \pmod 8$ is invariant along every tower: the eight parallel towers are the eight residues, their parallelism derived rather than described. Call a signature $(p,q)$ \emph{causal} if $\min(p,q) = 1$: exactly one direction of the minority sign, the timelike one, whichever sign convention carries time. Labelling this world $(1,3)$, residue $6$, fixes the convention time $=$ plus, and the mirror residue $2$ reads $(3,1)$; under the opposite convention the two labels swap and the causal sort is unchanged, but every attribution of a Clifford type to a member of the reversal pair passes to the other member, since $\Cl(1,3) \cong \Mat(2,\mathbb{H})$ and $\Cl(3,1) \cong \Mat(4,\R)$ are not isomorphic. That attribution is fixed by a labelling convention Premise \claimref{dark-matter.p2-indifference} declares indexical, and is so read below. Then:
\begin{enumerate}
\item[(i)] \emph{(Census; proved.)} Every residue contains causal signatures once the dimension is free: the lowest are $(1,1)$ at $r = 0$, $(2,1)$ at $r = 1$, $(3,1)$ at $r = 2$, $(4,1)$ at $r = 3$, $(1,5)$ or $(5,1)$ at $r = 4$, $(1,4)$ at $r = 5$, $(1,3)$ at $r = 6$, $(1,2)$ at $r = 7$. The residue alone therefore sorts nothing; a representative must be chosen.
\item[(ii)] \emph{(The sort under P3; proved given the premise.)} Under Premise \claimref{dark-matter.p3-nearest-dimension-representatives} the representatives are $(1,3)$ at $r = 6$, this world; $(3,1)$ at $r = 2$, a mirror Minkowski with real (Majorana-type) spinors; $(2,2)$ at $r = 0$, two times; $(4,0)$ or $(0,4)$ at $r = 4$, none; $(2,1)$ and $(1,2)$ at $r = 1, 7$, three-dimensional; $(4,1)$ and $(1,4)$ at $r = 3, 5$, five-dimensional. Exactly two are sterile, $r = 0$ and $r = 4$ (a figure of the original), and they are the fixed points of the mirror map $r \mapsto -r$: under P3 the towers without a single time are the towers that are their own mirrors.
\item[(iii)] \emph{(Sensitivity; proved.)} The sterile set is a function of the window. With any dimension up to five allowed, only $r = 4$ is sterile ($(1,1)$ is a causal signature for $r = 0$); with dimensions three to six, only $r = 0$ ($(1,5)$ is one for $r = 4$); with the upper bound removed, nothing is ($(1,9)$ is one for $r = 0$ at ten); and the literal lowest-dimensional representative of every residue, with no lower bound, is definite for $r = 6$ itself, namely $(0,2)$: without a lower bound the criterion would sterilise this world.
\end{enumerate}
Six admit matter: this one and five dark. Which of the six the descent populated is a further question, answered for the mirror by P2 and for the odd towers only by the record (Observation \claimref{dark-matter.which-towers-are-populated}). Structural level given P3; the two-time exclusion at $r = 0$ imports the standard instability of two-time dynamics, flagged, and the flag does not remove it (Proposition \claimref{dark-matter.flag-insensitive-residue-no-flag-level}).

*Provenance:* Transport Lab claim dark-matter.towers-are-residues-single-clock-filter, version 5 (T14 Prop 3.1).

**Fact (imported) 45 (The two families are the two chiralities).** In even dimension $2m$:
\begin{enumerate}
\item[(i)] every maximal isotropic $U$ has a pure spinor, unique up to scale, and it is a chirality eigenstate; the pure spinor of $W$ is the null blade $f$ itself, of Fock grade zero, and the pure spinor of $W'$ is the top state $v_{1}\cdots v_{m}f$, of Fock grade $m$;
\item[(ii)] the chirality of $\psi_{U}$ is preserved by even versors (the spin group) and reversed by odd versors (reflections), so the \emph{family} of $U$, defined as the chirality of its pure spinor, is an invariant of the connected isometry group and not of the full one;
\item[(iii)] there are exactly two families, and a Witt pair $W$, $W'$ lies in opposite families if and only if $m$ is odd.
\end{enumerate}
In odd dimension $2m + 1$ there is one family: the connected isometry group acts transitively on maximal isotropic subspaces, and the spin algebra does not preserve the grade parity of $S$.

*Provenance:* Transport Lab claim dark-matter.two-families-are-two-chiralities, version 6 (T14 Prop 3.9).

**Fact (imported) 46 (Type by residue, and what each tower can carry intrinsically).** The type is a function of the residue alone: $D = \R$ with one irreducible module at $r = 0, 2$ and two at $r = 1$; $D = \C$ with one at $r = 3, 7$; $D = \mathbb{H}$ with one at $r = 4, 6$ and two at $r = 5$. Consequently, for the P3 representatives, in the labelling convention of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter} (under the opposite one every attribution to a named member of a pair $\{r, -r\}$ passes to the other):
\begin{enumerate}
\item[(i)] the mirror tower $r = 2$ has real (Majorana) spinors with intrinsic group $\mathbb{Z}_{2}$: no continuous charge commutes with its ground Clifford action, and in particular no $U(1)$ under which its ground spinors are charged; the fork tower $r = 0$, also real with one module, has the same intrinsic group $\mathbb{Z}_{2}$;
\item[(ii)] the residues $r = 3$ (five-dimensional) and $r = 7$ (three-dimensional) have complex spinors with intrinsic group exactly $U(1)$, a distinguished complex structure and hence exactly one intrinsic abelian charge each;
\item[(iii)] this world $r = 6$, and $r = 4, 5$, have quaternionic spinors with intrinsic group $Sp(1)$: a two-sphere of complex structures and no distinguished $U(1)$;
\item[(iv)] the odd residues $r = 1, 5$ have two inequivalent irreducible modules, distinguished by the sign of the central volume element, and $r = 3, 7$ one, the volume element acting as the complex unit.
\end{enumerate}
The intrinsic group is a lower bound on a tower's internal symmetry, not the whole of it: the rungs adjoin ladder pairs whose flags are complex structures (Remark \claimref{note.dark-matter.where-flag-defined-what-it-carries}), and the derived content of this tower's $U(1)$ is a rung-level object \cite{ButlerT12}. What the theorem fixes is what the ground algebra carries by itself.

*Provenance:* Transport Lab claim dark-matter.type-residue-what-each-tower-can, version 5 (T14 Thm 3.4).

**Fact (imported) 47 (The unit-ball rule).** Under R1 to R3, the share of a tower whose space has $D$ dimensions is $f = \tfrac{V_{3}}{V_{D}}$, and
\[
\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; V_{3}\sum_{\text{dark }r}\frac{1}{V_{D_{r}}}
\;=\; \frac{V_{3}}{V_{3}} + 2\,\frac{V_{3}}{V_{2}} + 2\,\frac{V_{3}}{V_{4}}
\;=\; 1 + \frac{8}{3} + \frac{16}{3\pi} \;=\; \frac{11\pi + 16}{3\pi} \;=\; 5.36432\ldots
\]
against the observed $5.364 \pm 0.065$. The agreement is built in, not predicted: the relation was found by solving for the observed value, and its clauses were chosen with it known, and the closed form is one of fourteen equally simple candidates within the error bar (Observation \claimref{dark-matter.status-rule}).

*Provenance:* Transport Lab claim dark-matter.unit-ball-rule, version 5 (T14 Prop 7.6).

**Fact (imported) 48 (Mass as symplectic area: the two-spinor formula).** On the real slice, where $\varepsilon^{A'B'}$ is the conjugate of $\varepsilon^{AB}$ and $\bar\pi$ the conjugate of $\pi$ (the conjugation reverses the complex unit $I_{6}$): a single conformal spinor (twistor) carries null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$ and is massless, and a system of two conformal spinors with momentum
\[
p_{AA'} = \pi^{1}_{A}\bar\pi^{1}_{A'} + \pi^{2}_{A}\bar\pi^{2}_{A'}
\]
has
\begin{equation}
m^{2} = p^{2} = 2\,\bigl|\br{\pi^{1}\pi^{2}}\bigr|^{2},
\end{equation}
the squared symplectic area between the two spinor parts. Aligned spinors (vanishing bracket) give a null composite, and mass grows with the misalignment.

*Provenance:* Transport Lab claim mass.mass-symplectic-area-two-twistor-formula, version 3 (T11 Prop 4.1).

**Fact (imported) 49 (The sign of $\omega^2$).** $\displaystyle \omega^2 = (-1)^{\tfrac{n(n-1)}{2}} (-1)^q = (-1)^{\tfrac{(p-q)(p-q-1)}{2}}$. In particular $\omega^2 = +1$ if and only if $p - q \equiv 0$ or $1 \pmod 4$.

*Provenance:* Transport Lab claim primer.sign, version 2 (T00 Lem 9.5).

**Fact (imported) 50 (Imported: the five-dimensional Chern-Simons shift).** A five-dimensional Dirac fermion of mass $m$ charged under a gauge field, integrated out, shifts the coefficient of the five-dimensional Chern-Simons term by $\tfrac12\sgn(m)$ (times the representation's cubic index for a non-abelian field); the sign is odd under the reflection of one spatial direction, so that the parity-violating term is present for a single species and absent for a pair whose contributions cancel. \emph{Provenance:} \cite{Witten1996, IMS1997}.

*Provenance:* E. Witten, Phase transitions in M-theory and F-theory, Nucl. Phys. B 471 (1996) 195--216.; K. Intriligator, D. R. Morrison, N. Seiberg, Five-dimensional supersymmetric gauge theories and degenerations of Calabi-Yau spaces, Nucl. Phys. B 497 (1997) 56--100..

**Fact (imported) 51 (Imported: the parity anomaly).** A single two-component Dirac fermion of mass $m$ in $2{+}1$ dimensions, coupled to a $U(1)$ gauge field, has an effective action containing a Chern-Simons term at level $\tfrac12\sgn(m)$ up to a sign that flips between the two inequivalent two-component representations; the term is odd under the reflection of one spatial axis, so a single species breaks parity, while two species, one in each representation with equal mass (equivalently the four-component fermion with its parity-invariant mass term), induce no net Chern-Simons term. \emph{Provenance:} \cite{NiemiSemenoff1983, Redlich1984, AGW1984}.

*Provenance:* A. J. Niemi, G. W. Semenoff, Axial-anomaly-induced fermion fractionization and effective gauge-theory actions in odd-dimensional space-times, Phys. Rev. Lett. 51 (1983) 2077--2080.; A. N. Redlich, Gauge noninvariance and parity nonconservation of three-dimensional fermions, Phys. Rev. Lett. 52 (1984) 18--21; Parity violation and gauge noninvariance of the effective gauge field action in three dimensions, Phys. Rev. D 29 (1984) 2366--2374.; L. Alvarez-Gaum'e, E. Witten, Gravitational anomalies, Nucl. Phys. B 234 (1984) 269--330..

**Fact (imported) 52 (The cluster bound in two dimensions).** For quanta of the nucleon mass at a relative speed of $3000$ km/s ($k = 0.0238\ \mathrm{fm^{-1}}$ in the centre-of-mass frame):
\begin{enumerate}
\item[(i)] a hard disk of radius $0.21$ fm has $\lambda = 13$ fm from the partial-wave sum and $14$ fm from the logarithmic form; of radius $10^{-11}$ fm, still $\lambda = 0.49$ fm;
\item[(ii)] the bound $\sigma_{\mathrm{eff}}/m < 1\ \cmg$ in a cluster core (isotropic spacing) requires $\lambda < 4.8 \times 10^{-12}$ fm;
\item[(iii)] by size alone that requires $a < 10^{-4.0 \times 10^{6}}$ fm; by interaction strength, an s-wave phase shift $\delta_{0} < 1.7 \times 10^{-7}$.
\end{enumerate}

*Provenance:* Transport Lab claim simulations.cluster-bound-two-dimensions, version 3 (T14b Comp 3.3).

**Fact (imported) 53 (The gauge algebra of the minimal massive composite).** The maximal hierarchy of three conformal spinors (the three-twistor hierarchy) $\C^{3} \otimes \C^{3}$ has automorphism algebra $\su(3) \oplus \su(3) \oplus \uu(1)$, of dimension seventeen, which is not the Standard Model's. The minimal massive one is: mass first exists at two constituents (Fact \claimref{mass.mass-symplectic-area-two-twistor-formula}), so matter's \emph{minimal massive} hierarchy is $\C^{2} \otimes \C^{3}$, two conformal spinors of three pairs each, and its automorphisms form $(U(2) \times U(3))/U(1)$, with Lie algebra
\begin{equation}
\su(2) \oplus \su(3) \oplus \uu(1),
\end{equation}
of dimension $4 + 9 - 1 = 12 = 3 + 8 + 1$: the Standard Model Lie algebra exactly. The global group is determined by Theorem \claimref{standard-model.global-form-quotient-determined}.

*Provenance:* Transport Lab claim standard-model.gauge-algebra-minimal-massive-composite, version 4 (T12 Thm 4.1).

**Fact (imported) 54 (The global form: the quotient determined).** The global gauge group of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} is determined exactly. The kernel of the $(U(2) \times U(3))$-action on $\C^{2} \otimes \C^{3}$ is $K = \{(\lambda I_{2}, \lambda^{-1} I_{3})\} \cong U(1)$, and
\begin{equation}
(U(2) \times U(3))/K \;\cong\; S(U(2) \times U(3)) \;\cong\; \bigl(SU(2) \times SU(3) \times U(1)\bigr)/\mathbb{Z}_{6}:
\end{equation}
the framework's group is the smallest of the Standard Model's global forms, the full $\mathbb{Z}_{6}$ quotient, not the naive product and not either intermediate quotient. Three consequences. (i) $S(U(2) \times U(3))$ is exactly the subgroup of $SU(5)$ preserving the splitting $\C^{5} = \C^{2} \oplus \C^{3}$, and none of the three proper covers $(SU(2) \times SU(3) \times U(1))/\Gamma$, $\Gamma \subsetneq \mathbb{Z}_{6}$, acts faithfully through it; so the framework's global form is the one that grand unification's embedding requires, and the trace ratio $3/8$ of the section ``Unification and the desert'' refers to the same normalisation from the other side. (ii) The representations of the group are confined to the $\mathbb{Z}_{6}$ charge lattice: on a representation of the covering product with colour triality $t \in \mathbb{Z}_{3}$, weak parity $\delta \in \mathbb{Z}_{2}$ (the class of the $SU(2)$ content: $1$ on a doublet, $0$ on a singlet or triplet) and abelian weight $q \in \mathbb{Z}$ (the integer such that the $U(1)$ factor $\lambda$ acts by $\lambda^{q}$), descent to the quotient holds if and only if $2t + 3\delta + q \equiv 0 \pmod 6$; writing $Y = q/6$ this is the condition that $t/3 + \delta/2 + Y$ be an integer. The content of Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency} lies on it (each of its representations is built as a representation of $S(U(2) \times U(3))$), and the lattice check is printed there. (iii) A structural stance, registered: the lattice forbids representations off it, so a confirmed discovery of, for example, a fractionally charged colour singlet would refute the identification of the gauge group with the automorphism group of minimal massive compositeness, a stance that current searches test \cite{PDG2024}. The stance inherits the conditionality of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s premise and is flagged at that level.

*Provenance:* Transport Lab claim standard-model.global-form-quotient-determined, version 3 (T12 Thm 4.2).

**Fact (imported) 55 (Hypercharge from the global form, pair counting, and consistency).** With $Y$ the hypercharge defined before Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}, and with Hypothesis (S) wherever a doublet at the level of one conformal spinor (a twistor-level doublet) enters:
\begin{enumerate}
\item (Under (S).) The one-handed listing keeps the states of even total mode number and conjugates the odd ones, or the reverse; the choice is the particle-antiparticle orientation. Write $(j, k)$ for the component of the five-mode state space with $j$ slot modes and $k$ pair modes occupied (mode counts, not the pair of representation dimensions used elsewhere in this paper, for which see the caption of a figure of the original). In the listing that keeps the quark doublet, the component $(1,1)$, as a particle, the lepton doublet is the full conformal spinor, the component $(1,3)$, $Y_{L} = -1/2$, and the empty conformal spinor, the component $(1,0)$, appears only as its conjugate (here both phrases name doublet components of the one-slot listing; the neutrino paper uses ``empty'' and ``filled conformal spinor'' for the grade-zero and grade-three singlets of the single-spinor sector, different objects, Proposition \claimref{neutrino.empty-twistor}). The $[SU(2)]^{2}U(1)$ anomaly coefficient of the two doublets, $3Y_{Q} + Y_{L}$ with the three the colour multiplicity, is then the identity $3 \cdot \tfrac16 - \tfrac12 = 0$; it would equal $1$ if the empty conformal spinor were listed as the particle instead, so the anomaly confirms the orientation the listing fixed. Pair counting fixes $|Y_{L}/Y_{Q}| = 3$; the parity fixes the sign.
\item (Unconditional as a computation on the Fock space of a single conformal spinor, like Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(3).) Listed by the handedness of (1), the sector of a single conformal spinor gives the singlet spectrum. Here $\CS = \Lambda^{\mathrm{even}}W$, the conformal spinor space, and $\CSm{} = \Lambda^{\mathrm{odd}}W$ are the two chirality halves (Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}), and the listing keeping the even grades and conjugating the odd ones gives
\[
(1)_{0} \;\oplus\; (\bar{3})_{-2/3} \;\oplus\; (\bar{3})_{+1/3} \;\oplus\; (1)_{+1},
\]
that is $\nu^{c}$, $u^{c}$, $d^{c}$, $e^{c}$ with hypercharges $0, -\tfrac23, +\tfrac13, +1$: the observed singlet spectrum, with the fourth singlet at hypercharge zero. (The listing by the opposite handedness is the conjugate of this one, the same spectrum in the opposite convention.) Under (S) the grade-$k$ states of a single conformal spinor are the $(0, k)$ components, the states with no slot mode and $k$ pair modes occupied (their content $\Lambda^{k}\C^{3}$ and weight $-2k$ match, and irreducibles are determined by content and weight), so their parity is the total parity and this listing is the same listing as in (1).
\item (Consistency, and uniqueness given the content; under (S) for the doublets.) With the content of (1) and (2), all four anomaly conditions of Fact \claimref{standard-model.imported-anomaly-coefficients} hold. Conversely, for the field content $Q = (2,3)$, $L = (2,1)$, $u^{c} = (1,\bar{3})$, $d^{c} = (1,\bar{3})$, $e^{c} = (1,1)$, all listed in one handedness, together with a fourth singlet of hypercharge zero or no fourth singlet, and $Y_{Q} = 1/6$ as the normalisation, the four conditions determine $Y_{L}$, $Y(e^{c})$ and $\{Y(u^{c}), Y(d^{c})\}$ uniquely, and the solution is the spectrum of (1) and (2). Both hypotheses are necessary: with a fourth singlet of unconstrained hypercharge the conditions admit a one-parameter family, and if the doublets were listed in the opposite handedness from the singlets the $[SU(3)]^{2}U(1)$ and cubic sums would be $-\tfrac23$ and $+\tfrac49$ rather than zero.
\end{enumerate}

*Provenance:* Transport Lab claim standard-model.hypercharge-global-form-pair-counting-consistency, version 5 (T12 Thm 5.5).

**Fact (imported) 56 (Imported: the pair systems and the two chirality halves).** Let $W$ be a maximal isotropic (three-dimensional) subspace of $V_{\C}$ with a dual isotropic complement. The complexified ascended algebra acts irreducibly on $\Lambda^{\bullet}W$, and its two chirality halves are $\CS = \Lambda^{\mathrm{even}}W$ and $\CSm = \Lambda^{\mathrm{odd}}W$, each of dimension four. Every nonzero conformal spinor (twistor) $u \in \CS$ is a pure spinor: it is the Fock vacuum of the system of three fermionic ladder pairs built on its own annihilator space $W_{u}$, every state of the module is generated from $u$ by those pair operators, and $\CS$ (respectively $\CSm$) is what the even (respectively odd) products generate. Conformal spinors are states of the pair algebra, not its operators. \emph{Provenance:} \cite[Thm.~3.1]{ButlerT9} for the Fock model and the chirality halves; \cite[Thm.~5.3]{ButlerT9} for the pure-spinor and Fock-vacuum statements; the tower paper \cite[Thms.~4.2, 4.3]{ButlerT3} for the iterated pair structure (one qubit per rung, Witt index as capacity) within which this sits.

*Provenance:* Transport Lab claim standard-model.imported-pair-systems-two-chirality-halves, version 5 (T12 Fact 2.2).

**Fact (imported) 57 (The internal symmetry ladder).** For a system of $n$ conformal spinors (an $n$-twistor system) $(Z^{1}, \ldots, Z^{n})$, the linear mixings $Z^{i} \mapsto U^{i}{}_{j} Z^{j}$ that preserve the total momentum $p_{AA'} = \sum_{i} \pi^{i}_{A}\bar\pi^{i}_{A'}$, built from the parts $\pi^{i}$ in the $E = +1$ eigenspace, and the total helicity form $\sum_{i} \bar{Z}^{i} \cdot Z^{i}$, the reversion form $h$ summed over the spinors, for every configuration form exactly the unitary group $U(n)$. The ladder therefore reads: one conformal spinor, massless, internal group $U(1)$; two, the first massive step, internal group $U(2)$, with Lie algebra $\su(2) \oplus \uu(1)$; three, internal group $U(3)$, with Lie algebra $\su(3) \oplus \uu(1)$. (The groups are $U(n)$ themselves, not products: the map $SU(n) \times U(1) \to U(n)$, $(a, \mu) \mapsto \mu a$, is onto, and its kernel is $\{(\mu^{-1}I_{n}, \mu) : \mu^{n} = 1\} \cong \mathbb{Z}_{n}$ by the determinant, so $U(n) = (SU(n) \times U(1))/\mathbb{Z}_{n}$; the distinction is treated in the section ``The gauge algebra and the global form''.)

*Provenance:* Transport Lab claim standard-model.internal-symmetry-ladder, version 3 (T12 Prop 3.1).

**Fact (imported) 58 (The pair count in dimension $n$).** Let the ambient space of the completion in spacetime dimension $n$ have signature $(2, n)$, so that $V_{\C}$ has dimension $n + 2$ and carries a nondegenerate symmetric bilinear form. If $n$ is even, a maximal totally isotropic subspace of $V_{\C}$ has dimension $(n+2)/2$, so the pair system of a conformal spinor (a twistor's pair system) has $(n+2)/2$ pairs; in dimension four it has three.

*Provenance:* Transport Lab claim standard-model.pair-count-dimension, version 3 (T12 Lem 2.12).

**Fact (imported) 59 (Quarks and leptons: the two-level fermion content).** Under $S(U(2) \times U(3))$, with $Y$ the hypercharge just defined:
\begin{enumerate}
\item (Unconditional.) The pair-level generators, the cells of the tensor state space, transform as $(2, 3)$ with abelian weight $q = 1$, so $Y = 1/6$: the quark doublet's representation. A single pair has one unit of hypercharge.
\item (Under Hypothesis (S).) The states with one slot mode occupied and the pair modes in an $SU(3)$-invariant configuration are $\C^{2} \otimes \Lambda^{0}W$, weight $3$ ($Y = +1/2$, total mode number one, odd), and $\C^{2} \otimes \Lambda^{3}W$, weight $-3$ ($Y = -1/2$, total mode number four, even); both transform as $(2, 1)$. Without (S) neither exists in the state space, whose only row-filling states form the quadruplet $(4,1)$ of weight $+3$.
\item (Unconditional as a computation on the Fock space of a single conformal spinor, with the pair-slot factor acting alone; that Fock space is not a subspace of the tensor state space, and under (S) it is the row $j = 0$.) In the sector of a single conformal spinor (the single-twistor sector) $\Lambda^{\bullet}W = \Lambda^{\bullet}\C^{3}$, the grade-$k$ states transform as $\Lambda^{k}\C^{3}$, that is as $1, 3, \bar{3}, 1$ for $k = 0, 1, 2, 3$, with weight $q = -2k$: $Y = 0, -1/3, -2/3, -1$.
\end{enumerate}
In particular, under (S), the fermion content of the composite at the particle handedness (Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}) is
\begin{equation}
(2,3)_{1/6} \oplus (2,1)_{-1/2},
\end{equation}
quark doublet plus lepton doublet, with colour neutrality of the lepton the statement that a state with its pair modes full is an $SU(3)$ singlet: a lepton is a complete conformal spinor, one slot with the pair system full, while a quark is one slot with one pair.

*Provenance:* Transport Lab claim standard-model.quarks-leptons-two-level-fermion-content, version 5 (T12 Prop 5.3).

**Fact (imported) 60 (The ten is the transported ambient space, and its doublets are the rungs).** Under $S(U(2) \times U(3))$ acting on the module, the ten decomposes as
\[
R_{2} \oplus \overline{R}_{2} \oplus W \oplus \overline{W} \;=\; (2,1)_{1/2} \oplus (2,1)_{-1/2} \oplus (1,3)_{-1/3} \oplus (1,\bar{3})_{1/3}:
\]
the rung creation vectors $v_{4}, v_{5}$ are a weak doublet of hypercharge $+\tfrac12$ with $2T_{3} = +1, -1$, the rung annihilation vectors $w_{4}, w_{5}$ the conjugate doublet of hypercharge $-\tfrac12$, and the pair vectors are colour triplets and antitriplets of hypercharge $\mp\tfrac13$, weak singlets. This is the $10$ of $\mathrm{Spin}(10)$ restricted as in Fact \claimref{standard-model.imported-spinor-bilinears}, realised as the transported ambient space itself: the Higgs doublet's representation is carried by the directions transport adjoined, and the colour-triplet partner's by the null directions the ground completion already had.

*Provenance:* Transport Lab claim standard-model.ten-transported-ambient-space-doublets-are, version 2 (T12 Prop 9.22).

**Fact (imported) 61 (The three involutions on each grade).** The grade involution is an automorphism, reversion and Clifford conjugation are anti-automorphisms; all three are involutions and they commute. On $\Cl^{k}$ they act by
\begin{equation}
\hat{x} = (-1)^{k} x, \qquad \tilde{x} = (-1)^{k(k-1)/2} x, \qquad \bar{x} = (-1)^{k(k+1)/2} x .
\end{equation}
\texttt{GA.grade\_inv} and \texttt{GA.reverse} implement the first two.

*Provenance:* Transport Lab claim std-algebra.involution-properties, version 1.

**Fact (imported) 62 (How the pseudoscalar commutes).** In $\Cl(p, q, r)$, $n = p + q + r$, with unit pseudoscalar $I$:
\begin{enumerate}
\item[(i)] $I X_k = (-1)^{k(n-1)} X_k I$ for $X_k \in \Cl^{k}$; so $I$ commutes with $\Cl^{+}$, and with $\Cl^{-}$ when $n$ is odd, while it anticommutes with $\Cl^{-}$ when $n$ is even. Equivalently $I X = X I$ for $n$ odd and $I X = \hat{X} I$ for $n$ even.
\item[(ii)] $I \tilde{I} = \prod_{i} Q(e_i)$, which is $(-1)^{q}$ when $r = 0$ and $0$ when $r > 0$.
\item[(iii)] $I^{2} = (-1)^{n(n-1)/2} (-1)^{q}$ when $r = 0$ (\claimref{primer.sign}), and $I^{2} = 0$ when $r > 0$: in a degenerate algebra the pseudoscalar is nilpotent.
\end{enumerate}

*Provenance:* Transport Lab claim std-algebra.pseudoscalar-commutation, version 1.

**Fact (imported) 63 (Orthogonal bases and the law of inertia).** Every real quadratic space $(V, Q)$ of dimension $n$ has an orthogonal basis $e_1, \dots, e_n$ with $Q(e_i) \in \{1, -1, 0\}$. The numbers $p$, $q$ and $r$ of basis vectors with $Q(e_i) = 1$, $-1$ and $0$ do not depend on the basis (Sylvester's law of inertia). Moreover $r = \dim \operatorname{rad} V$, and $p + q$ is the rank of any Gram matrix of $B$. Two real quadratic spaces are isometric if and only if they have the same $(p, q, r)$.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, AMS (2005)., the diagonalisation of forms and Sylvester's law of inertia (real case).

**Fact (imported) 64 (The ladder pairs satisfy the CAR, as vectors).** In $T_k$, the adjoined null pairs satisfy, exactly and at the level of vectors,
\[
v_i v_j + v_j v_i = 0, \qquad w_i w_j + w_j w_i = 0, \qquad v_i w_j + w_j v_i = \delta_{ij}\,,
\]
for all $1 \leq i, j \leq k$: a system of $k$ fermionic modes, with no normal-ordering, no completion, and no representation chosen. Adding a rung adds one mode and touches none of the existing relations.

*Provenance:* Transport Lab claim tower.ladder-pairs-satisfy-car-vectors, version 4 (T03 Prop 4.1).

**Fact (imported) 65 (Rigidity; the clock is frozen).** Along the tower: the transport charge $d = p - q \bmod 8$ is constant; the division-ring type, simplicity class, and centre of every floor equal those of the ground floor; every floor is Morita equivalent to the ground floor; and the obstruction taxonomy of \cite{ButlerT1} is floor-independent: in particular a type-C obstruction (a central idempotent) never arises by transport from a simple ground algebra, at any height. The physical tower is $\Cl(1{+}k, 3{+}k) \cong \Mat_{2^{k+1}}(\HH)$, frozen at clock position $6$. Bott periodicity manifests as immediate freeze, not eventual return.

*Provenance:* Transport Lab claim tower.rigidity-clock-frozen, version 5 (T03 Thm 3.6).

**Refutation 66 (The raw representation content matches the fermion table entry by entry).** Refuted. The corrected statement: The disagreements are composites; generators, not states, are the content, and the lepton lies one level higher, under the declared hypothesis of slot statistics.

**Refutation 67 (The hierarchy of three conformal spinors $\mathbb{C}^{3}\otimes\mathbb{C}^{3}$ carries the Standard Model).** The hierarchy of three conformal spinors (the three-twistor hierarchy) $\mathbb{C}^{3}\otimes\mathbb{C}^{3}$ carries the Standard Model

**Prediction 68 (Direct detection stays null).** Permanent direct-detection nulls: dark matter couples through gravity alone, at first order.

**Prediction 69 (No indirect dark-sector signals).** No indirect dark-sector signals: no decay products, since the tower charge is superselected, and annihilation products only at the rate of graviton exchange, suppressed by powers of $E/M_{P}$ on a charge-asymmetric relic.

**Prediction 70 (No fractionally charged colour singlet).** The $\mathbb{Z}_{6}$ charge lattice: no fractionally charged colour singlet exists.


