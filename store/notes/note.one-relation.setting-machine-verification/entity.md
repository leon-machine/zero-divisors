---
id: note.one-relation.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: one-relation
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
comments_on:
- one-relation.two-presentations
- one-relation.two-capacities-three-consequences
- one-relation.overlap-table-sorted
- one-relation.vector-derivative-covariant-first-order-operator
locators:
  paper: T16
  number: Setting
  section: Machine verification
  line: 883
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
Every computational identity asserted in this paper at its own proof level has been verified in exact arithmetic by the script \texttt{verify\_T16.py} \cite{ButlerVerifyT16}, which imports the series' shared library \texttt{GA.py}: exact rationals, Gaussian rationals, the blade arithmetic for the frame computations, and exact linear algebra over the Gaussian rationals for the kernel computations. No floating point is used anywhere; one hundred and forty-six checks, all passing, in five parts, three of which have a second part. Every reference to the script in a proof above names a check in this list.

\emph{Part A: the two presentations.} The orthogonal relations of $\Cl(1,1)$ and, on the real null pair built from the same generators, the CAR of one mode; in $\Cl(1,3)_{\C}$ the real pair on the boost plane and the complex pair on the anisotropic kernel, all CAR relations exact, the change of basis of rank four over the Gaussian rationals, and the definiteness of the kernel ($Q(ae_{2} + be_{3}) = -(a^{2} + b^{2})$ on rational instances), which is why the real capacity is one and the complex two; in $\Cl(2,4)_{\C}$ two real pairs and one complex pair, all nine relation sets exact, and the kernel's definiteness again (real capacity two, complex three); and, for the paragraph in words after Proposition \claimref{one-relation.two-presentations}, the two occupation projectors $n_{-}n_{+} = \tfrac12(1+\sigma)$ and $n_{+}n_{-} = \tfrac12(1-\sigma)$ summing to one, the eigen-relations $\sigma n_{\pm} = \mp n_{\pm}$, and the three sign reversals of $(e_{0}, e_{1})$, of which the two single reversals swap the projectors and the double one fixes them.

\emph{Part B: capacity and overlap.} Arithmetic, recorded rather than tested, with one exception named: both capacities rise by exactly one under a $(1,1)$ ascent on the grid $p, q \leq 8$; the two capacity tables for the series' signatures ($1,1,2,3$ real and $1,2,3,4$ complex on $(1,1)$, $(1,3)$, $(2,4)$, $(3,5)$); the agreement locus $r_{\R} = r_{\C}$, proved in Proposition \claimref{one-relation.two-capacities-three-consequences} to be $|p - q| \leq 1$, illustrated on the grid by a biconditional check that could fail; and the two identities of Proposition \claimref{one-relation.overlap-table-sorted}(i).

\emph{Part C: the manifold of vacuum lines.} The null basis $n_{0}, n_{\infty}$ with $\ip{n_{0}}{n_{\infty}} = 1$; on six rational points with $Q(x)$ of every sign, $Q(X(x)) = 0$ computed from the inner product, $X(x)^{2} = 0$ in the algebra, $X(x) \neq 0$, and $Q(X) = Q(x)(1+2c) \neq 0$ for every other slot coefficient; the Fock model of $\Cl(2,4)_{\C}$ on $\Lambda^{\bullet}W$ built from wedge and contraction with all thirty-six anticommutators of the six ambient generators verified; for each point, $c(X(x))$ nilpotent with kernel of dimension four on the module and two on each chirality half; on each incidence line, two independent twistors and their sum each with a three-dimensional annihilator, pairwise distinct, each containing $X(x)$; across the fifteen pairs of points, distinct lines that meet exactly when the points are null-separated, and $\ip{X(x)}{X(y)} = -\tfrac12 Q(x-y)$ on every pair.

\emph{Part D: the laboratory.} The kernel of the covariance conditions for six rational rotors on the $64$-dimensional space of constant-coefficient first-order operators is two-dimensional and equals the span of $\gamma^{\mu}$ and $\gamma^{\mu}I$ (Lemma \claimref{one-relation.vector-derivative-covariant-first-order-operator}), with $I$ anticommuting with all four generators, $\gamma^{\mu}(a+bI) = (a-bI)\gamma^{\mu}$ on instances, $I^{2} = -1$ and $(a+bI)(a-bI) = a^{2} + b^{2}$ on instances; the boost plane squares to $+1$ and the spin plane to $-1$, the latter commuting with $\gamma_{0}$, and a rational rest-space rotation carries it to a distinct plane squaring to $-1$ and commuting with $\gamma_{0}$; the three algebraic facts of the Klein-Gordon square and $\{\gamma^{\mu}, \gamma^{\nu}\} = 2\eta^{\mu\nu}$ on all sixteen pairs; and the Pauli identity on nine rational vector pairs in $\Cl(3,0)$.

\emph{Part E: the measure.} The Dirac representation's relations and Hermiticity; twelve rational mass-shell momenta at $m = 5$ with both energy signs; two-dimensional solution kernels at each; the $528$-condition system whose kernel is one-dimensional and spanned by $\gamma^{\mu}$ (Lemma \claimref{one-relation.dirac-current-conserved-density}); the direct verification that $\gamma^{\mu}$ satisfies every condition; the density $\psi^{\dagger}\psi$ as a sum of squared moduli on instances; the weight space invariant under all transpositions of $n = 2, 3, 4, 5$ components is one-dimensional, while under the intransitive subgroups generated by one transposition, or by two disjoint ones, on four components it is three- or two-dimensional, one dimension per orbit, and under the transitive Klein four-group it is one-dimensional again, so the check discriminates invariance under a transitive orbit from invariance under some symmetry; and the fine-graining construction on three rational instances, exhibited rather than tested.

\emph{Part B, second part: the third constant.} The component counts of $\{Q > 0\}$ checked on sample points: on the nine signatures $(1,0)$, $(1,1)$, $(1,2)$, $(1,3)$, $(2,0)$, $(2,1)$, $(2,2)$, $(3,1)$, $(3,2)$ and on $(0,3)$, the classes of a union-find over rational sample points joined by exact segments with certified $Q$-minima are counted and compared with the $S^{p-1}$ count entered as a literal, two classes being certified distinct by the sign of the time coordinate, and the disjunction against $\min(p,q) = 1$ is checked on seven signatures up to $n = 5$ (Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}(iv)); the space of symmetric forms vanishing on the rational null vectors, of dimension one on every signature $(p,q)$ with $1 \leq p, q \leq 3$ (Fact \claimref{one-relation.imported-null-cone-determines-form-zeemans}); in $\Cl(1,1)$ the Witt pair, the boost bivector's square, the rotor at $\lambda = 4$ with $R\tilde{R} = 1$, its rescaling of the Witt pair, its boost of the frame with norms preserved, the velocity $\tfrac{15}{17}$, the null lines as the fixed lines, and the opposite sign's reversal (Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}(iii)); the exponent determinant $-2$, the independence of the base units from $\hbar$ and $G$ alone, and the three Planck monomials; the signature of $Q/c^{2}$ at finite $c$ and the rank-one limit (Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}(i)); and three pairwise distinct hyperbolic planes of $(1,3)$ with complements of one signature, the witnesses for Witt's extension theorem (Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}(ii), Fact \claimref{one-relation.imported-witts-extension-theorem}).

\emph{Part C, second part: the quadric.} On seeded random Gaussian-rational even states of four modes, the Cartan form $\mathcal{Q}$ against the purity test $M^{2} = -1$ on states off the quadric and on it (forty random states, forty with the quartic coefficient adjusted to $\mathrm{Pf}/\psi_{0}$, ten scaled Thouless states and a Slater determinant, both directions exercised), $\mathcal{Q} = 0$ as one condition on the quartic coefficient, the two witness states and the paired-block state, the chart $\psi_{0} = 0$ where $\mathcal{Q}$ reduces to the Pfaffian; the Thouless-Pfaffian identity on ten random antisymmetric $A$, its consequence $\mathcal{Q} = 0$ on every Thouless state, and the converse on the chart $\psi_{0} \neq 0$ on ten states built on the quadric with $\mathcal{Q}$ computed, against ten controls off it; the absence of a quartic term at $\nu = 3$; the tangent ranks $1 + \nu(\nu-1)/2$ of the vacuum orbit at $\nu = 2, 3, 4$, the orbit open at $\nu = 3$ and a hypersurface at $\nu = 4$ with a non-vacuum of orbit rank eight, and $\mathcal{Q}$ invariant under the pairing and hop rotations, the former moving the vacuum along the quadric and the latter fixing it (Remark \claimref{note.one-relation.where-exhaustiveness-first-fails-4-quadric}).

\emph{Part D, second part: the sharpening.} $I\sigma_{3} = \gamma_{2}\gamma_{1}$ and its inverse; the three right factors' squares (Lemma \claimref{one-relation.form-law-forced-square}); the identity $(v + Iw)^{2} = Q(v) + Q(w) - 2I(v \wedge w)$ on four samples, $C^{2} = -1$ at four values of $t$, the boost of $u$ and the rotor covariance of $C$, and the chiral phase's three properties (Lemma \claimref{one-relation.odd-square-roots-chiral-phase}); the four-dimensional commutant of $C$ with its basis, the pseudoscalar's exclusion, the hyperboloid condition on four instances, the bijection $J \mapsto CJ$ on both sheets with the sign computation, the two-dimensional joint stabiliser, and the realignment of the boosted datum (Lemma \claimref{one-relation.one-datum-not-two-imaginary-unit}); the one bit (Corollary \claimref{one-relation.arrow-frequency-are-one-bit-level}); the commutation, anticommutation and non-scalar cases of $\gamma_{0}J\gamma_{0}$ and the commutant of $\gamma_{0}$ (Proposition \claimref{one-relation.schr-odinger-slow-shadow}(3)); and the ideal picture, the idempotent, the four-dimensional $P\,\Cl\,P$ with its three imaginary units, and the right factors that do and do not preserve the ideal (Lemma \claimref{one-relation.one-datum-not-two-imaginary-unit}).

What the script does not check, and cannot: Witt's extension theorem (Fact \claimref{one-relation.imported-witts-extension-theorem}), for which it exhibits witnesses and which carries Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}(ii) and the uniqueness clause of Proposition \claimref{one-relation.two-capacities-three-consequences}(1); the deformation retraction behind the component counts of Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}(iv), which the script samples; the placement clauses of Proposition \claimref{one-relation.spacetime-manifold-vacuum-lines}(3)-(4), which say where each theory is located; the identification and reading clauses of Proposition \claimref{one-relation.overlap-table-sorted}; the $\hbar$ and $G$ identification, flagged in-text as the synthesis's weakest point; the identification of the Dirac mass parameter with the dictionary's mass beyond the Klein-Gordon square; the orientation identification and the unsourced-frame clause of Proposition \claimref{one-relation.schr-odinger-slow-shadow}(3); the standard nonrelativistic descent itself, imported; the envariance argument's continuity step, imported with its critique; the freedom counts of Proposition \claimref{one-relation.record-chain-votes-measurement-without-collapse}, which are imported counts; and everything conditional on Premises \claimref{one-relation.supervenience-stated-so-it-can-be} and \claimref{one-relation.recording-irreversible-stated-so-it-can}, which are premises and not computations. The paper marks each of these where it stands.

## technical
pending

## lay
pending

## one-liner
pending
