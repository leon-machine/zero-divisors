---
id: synthesis.field-strength-heat-kernel-coefficients-of-the-dark-towers-fix-no-scale-ratio
kind: claim
version: 1
title: 'Spin-trace rule in dimensions three and five: heat-kernel numbers, running only in four'
status: proved
region: synthesis
subject: dark-matter
tags: [gauge-fields, running-and-unification, towers-by-residue, spinor-modules, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-11-09-bridges
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-bridges
review: draft
derivations:
- name: main
  uses:
  - synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces@3
  - synthesis.imported-heat-kernel-coefficients-and-background-field-gauge@2
  - synthesis.gauge-algebra-by-tower@1
  - dark-tower-matter.three-dimensional-content@4
  - dark-tower-matter.five-dimensional-content@5
  - dark-tower-matter.three-dimensional-phases@4
  - dark-matter.mirror-tower-copy-one@9
  - dark-matter.no-coupling-rule-odd-towers-follows@6
  - dark-tower-matter.r1-has-no-mechanism-odd-towers@3
  - dark-tower-matter.five-dimensional-towers@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_spin_weights_are_the_same_in_three_four_and_five_dimensions
- kind: check
  ref: check.py::check_rule_gives_d_minus_26_over_6_and_a_logarithm_only_in_four_dimensions
- kind: check
  ref: check.py::check_table_by_tower_on_the_stored_content
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces
  - synthesis.gauge-algebra-by-tower
extraction:
  open_problem: op.dark-tower-running
  note: >-
    First application of the stored spin-trace rule to the dark towers' gauge algebras. Setting (attack item 1 of
    the open problem): the store already treats the three-dimensional towers' abelian fields as dynamical in the
    tower's own dimension, with a dimensionful coupling and confinement decided by the Chern-Simons level, so the
    reading taken here is that each tower's gauge field is dynamical in its own dimension; the four-dimensional
    reading of the five-dimensional content is given beside it as arithmetic. What is established: the spin weights
    of the rule are the same in the towers' algebras of dimension three and five as in four, so the rule gives one
    field-strength heat-kernel coefficient per field in every dimension, (d - 26)/6 per unit Casimir for a vector
    with its ghosts and n_c/3 per unit index for a spinor of n_c components; the table of these numbers on the
    stored content; and that they are running coefficients in four dimensions only, because the stored Fact has a
    logarithm only there. In three and five dimensions they are heat-kernel numbers, not beta coefficients: their
    signs do not decide asymptotic freedom or confinement. That no scale ratio follows for the odd towers is in substance already stored
    (dark-matter.no-coupling-rule-odd-towers-follows, dark-tower-matter.r1-has-no-mechanism-odd-towers,
    dark-tower-matter.five-dimensional-towers clause (ii)); what this entity adds is the coefficient table and the
    extension of the spin weights. A second route to 'a logarithm only at d = 4' (argued, not a clause): the
    stored flat vacuum-polarisation kernel in dimension d has freedom degree d - 2, so in d = 3 the field-strength
    term has no freedom and the only local term of order one is the parity-odd level, and in d = 5 the freedom is
    one constant of mass dimension one. No scale ratio to the visible sector is filed for the
    odd towers: it needs the dimensionful coupling (no equal-coupling premise reaches the odd towers), the gauge-
    invariant bare masses (free) and, in five dimensions, a regulator or completion. The mirror tower's ratio is 1
    and is already stored. Consequences, stated and not forced: op.odd-towers and op.thickness-deposit-rule get no
    correlation length from one-loop running; in the three-dimensional towers the only stored scale is the
    coupling itself (the topological mass of the stored phases result). The zero of the vector coefficient at
    d = 26 is a known coincidence with the critical dimension of the bosonic string (cited from memory) and is
    given no meaning. Standard dimensional analysis in d = 5 (infrared free at weak coupling, not renormalisable)
    is cited from memory and is not a clause. Transport-absent apart from the content it is applied to.
---

## formal
Under H1, H2 and U (the towers' gauge algebras), (S) where stated, the covariant gauge and the indefinite-form premise of the stored rule, and reading each tower's gauge field as dynamical in its own dimension: let a tower of dimension $d \in \{3, 4, 5\}$ have the algebra $\Cl(p,q)$, $p + q = d$, of its signature ($\Cl(2,1)$, $\Cl(1,2)$; $\Cl(1,3)$, $\Cl(3,1)$; $\Cl(4,1)$, $\Cl(1,4)$), and for a bivector $F$ put $X = -2\langle F^{2}\rangle_{0}$ and, for a representation in which $F$ acts by $M(F)$, the spin weight $s = 4\,\mathrm{Re}\,\mathrm{tr}\,M(F)^{2}/X$ of \claimref{synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces}: $M(F)a = a\cdot F$ on vectors and $M(F)\psi = \tfrac12F\psi$ on a left ideal with $n_{c}$ complex components. The stored rule assigns to a field with $n$ components, statistics $\sigma$ and determinant weight $w$ the number $c = \tfrac13\sigma w(n + 6s)$ per unit index, the trace of the flat coefficient $\tfrac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu} + \tfrac12E^{2}$ of Fact \claimref{synthesis.imported-heat-kernel-coefficients-and-background-field-gauge}(i), which is stated in every dimension.
\begin{enumerate}
\item[(i)] \emph{(Spin weights; proved.)} In each of the six algebras $s = -4$ on vectors and $s = -n_{c}/2$ on a left ideal of $n_{c}$ complex components ($n_{c} = 2$ in dimension three, $4$ for a Dirac ideal in four and five). In $\Cl(2,1)$ the ideal's commutant is $\mathrm{span}\{P, w\}$ with $w^{2} = +P$ and contains no unit of square $-1$: there $n_{c}$ means half the real dimension, the complex unit being the $\so(2)$ charge and not an element of the tower's algebra; the weight, a real trace, is unaffected.
\item[(ii)] \emph{(The rule in dimension $d$; proved, given the Fact.)} A gauge vector with its ghosts has $c = \tfrac16(d - 24) - \tfrac13 = \tfrac16(d - 26)$ per unit adjoint Casimir, a spinor of $n_{c}$ components $c = n_{c}/3$ per unit index, a complex scalar $\tfrac13$: at $d = 4$ the stored $-\tfrac{11}{3}$, $\tfrac23$, $\tfrac43$; at $d = 3$, $-\tfrac{23}{6}$ and $\tfrac23$; at $d = 5$, $-\tfrac72$ and $\tfrac43$. In the expansion of the Fact this coefficient multiplies $t^{(4-d)/2}$: a logarithm of the cut-off at $d = 4$ only (clause (ii) of the Fact is stated there only), a term finite at short proper time at $d = 3$ and a power of the cut-off at $d = 5$; the squared coupling has mass dimension $4 - d$. So $c$ is a one-loop running coefficient at $d = 4$ and a heat-kernel number, with no regulator-independent meaning as a beta coefficient, at $d = 3$ and $5$. In three dimensions the determinant of the squared Dirac operator is the modulus of the fermion determinant only; its parity-odd phase is the induced Chern-Simons level that the stored phases result uses, and it is not part of $c$.
\item[(iii)] \emph{(The table on the stored content; computed.)} With the algebras of \claimref{synthesis.gauge-algebra-by-tower} and the content of \claimref{dark-tower-matter.three-dimensional-content} and \claimref{dark-tower-matter.five-dimensional-content}: in the three-dimensional towers each $\so(2)$ factor has $c = \tfrac23$ (one unit-charge two-component fermion, no vector term); in the five-dimensional towers the colour factor has $c = 3\cdot(-\tfrac72) + 2\cdot\tfrac43\cdot\tfrac12 = -\tfrac{55}{6}$ under (S) (triplets $U$, $D$) and $-\tfrac{59}{6}$ without (S), and the abelian factor $\tfrac43\sum\dim\cdot Y^{2} = \tfrac{32}{9}$ under (S) and $\tfrac{16}{9}$ without, in the normalisation $Y = s - k/3$ of the stored content. Read in four dimensions, one copy of the five-dimensional content has $b_{3} = -\tfrac{29}{3}$ under (S), the colour coefficient of one generation, and $-\tfrac{31}{3}$ without, against the stored $-7$ of the visible sector at three generations, which three copies of the (S) content would equal; the number of copies is not stored.
\item[(iv)] \emph{(What follows and what does not; argued, consistent with the stored obstructions, to which it adds the coefficients.)} This clause concerns the odd towers; the mirror tower's coefficients and scale are the visible ones, ratio $1$, under the common-ceiling premise (\claimref{dark-matter.mirror-tower-copy-one}(iii), (iv)), which does not reach the odd towers. The store already records that off $d = 4$ the coupling is dimensionful with no fixed length, that no coupling value is derived and that no premise equates couplings across to the odd towers (\claimref{dark-matter.no-coupling-rule-odd-towers-follows}); that the three-dimensional towers are abelian with a dimensionful coupling, no transmutation and bare masses, and that nothing confines in five dimensions (\claimref{dark-tower-matter.r1-has-no-mechanism-odd-towers}); and that the five-dimensional gauge theory is infrared free, its reduction to four dimensions with the fifth direction one cell radius deep giving a confinement scale below $\pi/L$ by more than $e^{-250}$ (\claimref{dark-tower-matter.five-dimensional-towers}(ii)). In the three-dimensional towers the stored phases are decided by the effective Chern-Simons level, not by the sign of $c$ (\claimref{dark-tower-matter.three-dimensional-phases}), and the only scales are the dimensionful coupling (the topological mass $e^{2}/2\pi$ of the stored phases) and the free bare masses. The numbers of (iii) are consistent with these: under a different hypothesis, a common dimensionless coupling $\alpha_{0}$ at a common scale with massless content, which no stored statement supplies, the four-dimensional reading would give at one loop $\ln(\Lambda_{5}/\Lambda_{\mathrm{vis}}) = (2\pi/\alpha_{0})(\tfrac17 - \tfrac{3}{29}) = (2\pi/\alpha_{0})\tfrac{8}{203}$; this is a different hypothesis from that of the stored reduction (under R3) and does not contradict its verdict. No scale ratio for an odd tower follows from the store.
\end{enumerate}

## technical
The series derives the one-loop running of the visible gauge couplings from traces of the squared spin generator in the spacetime algebra, and derives a gauge algebra and matter content for each dark tower, but had not put the two together. The spin traces turn out to be the same in the three- and five-dimensional towers' algebras as in four dimensions, so the same rule yields a number per field in every dimension; for a gauge vector with ghosts it is $(d - 26)/6$. That number governs logarithmic running only in four dimensions. In three dimensions the coupling carries a mass dimension and the stored analysis already decides confinement by a topological level; in five the coupling has inverse mass dimension and the one-loop term is a power of the cut-off. A table is given for the stored content, with the four-dimensional reading of the five-dimensional content beside it, and the inputs a confinement-scale ratio would need are listed: none is in the store except for the mirror tower, where the ratio is one.

## lay
The strong force gets stronger at long distances, which is why quarks are confined, and the series can compute that trend for our own sector from the algebra of spacetime. The dark sectors of the series live on towers of other dimensions with their own forces, so one can ask whether those forces confine too and at what scale. The same algebraic calculation goes through in three and five dimensions and gives definite numbers. But only in four dimensions do those numbers describe a force that changes slowly with distance; in three and five dimensions the strength of a force has a built-in length scale and the numbers do not settle the question. For the mirror copy of our own sector the answer is already known: it behaves exactly like ours. For the odd-dimensional towers, a confinement scale would need information the series does not contain.

## one-liner
The stored spin-trace rule has the same spin weights in the towers' algebras of dimension three, four and five, giving the field-strength heat-kernel coefficient $(d - 26)/6$ for a vector with ghosts and $n_{c}/3$ for a spinor, hence $\tfrac23$ per abelian factor in the three-dimensional towers and $-\tfrac{55}{6}$ (colour) and $\tfrac{32}{9}$ (abelian) in the five-dimensional ones under (S); these are running coefficients at $d = 4$ only, and no scale ratio for an odd tower follows (argued; the stored obstructions).
