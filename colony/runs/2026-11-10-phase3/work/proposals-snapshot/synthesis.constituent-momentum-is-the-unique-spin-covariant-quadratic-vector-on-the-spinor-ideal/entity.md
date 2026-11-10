---
id: synthesis.constituent-momentum-is-the-unique-spin-covariant-quadratic-vector-on-the-spinor-ideal
kind: claim
version: 1
title: 'Causal towers of dimension 3 to 5: j the only covariant quadratic vector of a constituent'
status: proved
region: synthesis
subject: dark-matter
tags: [dark-tower-premises, spinor-modules, mass-generation]
proposed_by:
  kind: ai
  session: 2026-11-10-phase3
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase3
review: draft
about:
- obj.dark-tower-matter.ideals-fields-momentum
derivations:
- name: main
  uses:
  - dark-tower-matter.constituents-field@2
  - dark-tower-matter.where-mass-begins@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_one_spin_covariant_quadratic_vector_in_each_causal_tower
- kind: check
  ref: check.py::check_vector_projection_is_vacuous_in_three_and_four_dimensions_and_not_in_five
- kind: check
  ref: check.py::check_five_dimensional_mass_is_the_square_of_the_dropped_central_part
- kind: check
  ref: check.py::check_invariant_quadratic_scalars_none_in_three_and_four_dimensions_one_in_five
- kind: check
  ref: check.py::check_two_constituents_admit_cross_terms_so_additivity_is_not_forced
- kind: check
  ref: check.py::check_cross_block_has_the_dimension_of_the_field_so_two_constituents_give_three_four_six
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-tower-matter.h1-momentum
extraction:
  open_problem: op.odd-towers
  note: >-
    Premise reduction of the dark-matter postulates, item H1 (dark-tower-matter.h1-momentum, version 1): which part
    of the premise is a choice. The result is a statement about the stored definition of the momentum
    (obj.dark-tower-matter.ideals-fields-momentum) in the six causal towers of dimension three, four and five; it
    does not use H1 and H1 is not in its past cone (the two premises used, the constituents' field and the mass
    onset, have no postulate in theirs). What is proved: clauses (i) to (iv), by exact rank computations and
    polynomial identities over the six towers. What is argued: clause (v), the reading for H1, which rests on a
    reading of the three stored results that assume H1 (dark-tower-matter.gauge-algebras,
    synthesis.gauge-algebra-by-tower, synthesis.lowest-causal-residues-zero-four-content) and is not an audit of
    their proofs; the last of these extends H1 to dimensions two and six, which this result does not cover. Not
    claimed: that H1 can be retired (the existence of the spinor part, quadraticity, covariance and additivity
    over constituents stay assumed); anything in the sterile towers or outside dimensions three to five; that
    the title's "only" means more than "up to a real factor" and one constituent (the title has no room for
    the phrases; every level states them). Related stored result, named for comparison and not
    used: synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion classifies the spin-invariant
    bilinear forms on a spinor ideal with values in the corner algebra; clause (ii)'s count of invariant quadratic
    scalars agrees with it, and that result has H1 in its past cone, so it is not a premise here. Prior art,
    cited from memory and not a premise: that the symmetric square of a spinor representation contains the vector
    representation once in these dimensions is textbook representation theory of Clifford algebras (the symmetry
    types of spinor bilinears; for example A. Van Proeyen, Tools for supersymmetry, hep-th/9910030; cited from memory, the section not verified);
    no novelty is claimed beyond placing it on the series' spinor ideals and reading it against H1.
    Transport-absent: representation theory of the towers' even algebras; nothing uses transport.
---

## formal
Let $V$ be a causal tower of dimension $n \in \{3, 4, 5\}$, that is $\R^{2,1}$, $\R^{1,2}$, $\R^{1,3}$, $\R^{3,1}$, $\R^{4,1}$ or $\R^{1,4}$, with $e_{t}$, $f$, the spinor ideal $S = \Cl^{0}(V)f$ and the momentum $j(\psi) = \langle \psi e_{t}\rev{\psi}\rangle_{1}$ of Definition \claimref{obj.dark-tower-matter.ideals-fields-momentum}. The bivectors $B$ of $\Cl(V)$ act on $S$ by $\psi \mapsto B\psi$ and on $V$ by $v \mapsto Bv - vB$. Covariance here is under the Lie algebra of bivectors, hence under the connected group the rotors generate; no reflection is imposed, the bivectors act on $S$ from the left only (the right action of the field of $S$ is not imposed), and $\beta$ below is real-bilinear. Call a map $\mu : S \to V$ a \emph{spin-covariant quadratic vector} if $\mu(\psi) = \beta(\psi, \psi)$ for a symmetric $\R$-bilinear $\beta : S \times S \to V$ with
\[
\beta(B\psi, \phi) + \beta(\psi, B\phi) \;=\; B\,\beta(\psi, \phi) - \beta(\psi, \phi)\,B
\]
for every bivector $B$ and all $\psi, \phi \in S$; and call a quadratic form $S \to \R$ \emph{spin-invariant} if its symmetric bilinear form satisfies the same equation with right-hand side zero.
\begin{enumerate}
\item[(i)] \emph{(Uniqueness for one constituent; proved, by an exact rank computation in each of the six towers.)} The spin-covariant quadratic vectors on $S$ form a real line, spanned by $j$: $j$ is the only one up to a real factor. That the symmetric square of a spinor module contains the vector once in these dimensions is classical spinor algebra; what is done here is to place it on the series' spinor ideals.
\item[(ii)] \emph{(The projection; proved.)} For $n = 3$ and $n = 4$, $\psi e_{t}\rev{\psi}$ is a vector for every $\psi \in S$, so the projection $\langle\,\cdot\,\rangle_{1}$ in $j$ removes nothing, and $S$ carries no nonzero spin-invariant quadratic form. For $n = 5$,
\[
\psi e_{t}\rev{\psi} \;=\; j(\psi) + s(\psi)\,I,
\]
with $I$ the pseudoscalar of $\Cl(V)$, which is central, and $s$ a nonzero quadratic form on $S$; the spin-invariant quadratic forms on $S$ are the real multiples of $s$. These counts (none for $n = 3, 4$, one line for $n = 5$) agree with \claimref{synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion}(iii), which is not used here.
\item[(iii)] \emph{(Mass in dimension five; proved.)} For $n = 5$ and every $\psi \in S$, with $y = \psi e_{t}\rev{\psi}$,
\[
y^{2} = 2\,s(\psi)\,I\,y, \qquad Q(j(\psi)) = s(\psi)^{2}\,I^{2}, \qquad m^{2}\bigl(j(\psi)\bigr) = Q(e_{t})\,Q(j(\psi)) = s(\psi)^{2},
\]
and $2\,s(\psi)^{2} = \langle x x^{\dagger}\rangle_{0}$ for $x = \rev{\psi}\psi$, the single-constituent law of Theorem \claimref{dark-tower-matter.where-mass-begins}(ii), of which this clause is a restatement in terms of $s$. So in the five-dimensional towers the mass of one constituent is the square of the central part that the projection in $j$ removes, and the constituent is massless exactly where $s(\psi) = 0$.
\item[(iv)] \emph{(What covariance does not fix; proved in the six towers.)} The spin-covariant real bilinear maps $S \times S \to V$, with no symmetry imposed, form a space of dimension $1$, $2$, $4$ for $n = 3, 4, 5$, the real dimension of the field of $S$ (Theorem \claimref{dark-tower-matter.constituents-field}). On $S \oplus S$, two constituents, a spin-covariant quadratic vector is a multiple of $j(\psi_{1})$, a multiple of $j(\psi_{2})$ and such a bilinear map of $(\psi_{1}, \psi_{2})$, so the space has dimension $3$, $4$, $6$, larger than the plane spanned by the two single momenta (for $n = 3, 4$ also computed directly on $S \oplus S$). The total momentum $j(\psi_{1}) + j(\psi_{2})$ of the Definition is one point of it. The cross terms are odd under $\psi_{2} \mapsto -\psi_{2}$ and the two single momenta are even, so covariance together with invariance under a change of sign of one constituent leaves $a\,j(\psi_{1}) + b\,j(\psi_{2})$: that momenta add is then the absence of a cross term together with equal weights $a = b$, clauses of the Definition that covariance does not supply.
\item[(v)] \emph{(Reading for Premise H1; argued.)} In dimensions three and five the momentum clause of Premise \claimref{dark-tower-matter.h1-momentum} is, by (i), equivalent to the weaker statement that a constituent's momentum is a nonzero spin-covariant (connected group) real-quadratic function of its spinor part with values in $V$, together with a real factor: a positive factor multiplies every mass of the tower by one constant and a negative one exchanges the two time orientations. The formula is therefore not an independent choice. What remains assumed in H1 is that a constituent has a spinor part in $S$ (the intertwining map), that its momentum is quadratic in that part and covariant, and, from the Definition, that momenta add. In dimension three the premise's formula has the form of the four-dimensional one with nothing removed; in dimension five it removes the central part $s\,I$, which by (iii) carries the whole single-constituent mass.
\end{enumerate}

## technical
Premise H1 of the dark-tower paper takes a constituent's momentum, in the towers of dimension three and five, to be the vector part of $\psi e_{t}\rev{\psi}$ for its spinor part $\psi$, as in dimension four. This result asks how much of that is a choice, in the six causal towers of dimension three to five. Requiring only that the momentum be a vector depending quadratically on $\psi$ and transforming with it under the spin algebra leaves, by an exact computation in each tower, a single candidate up to a real factor, and it is the premise's $j$; covariance is under the connected spin group only (no reflections) and the dependence is real-quadratic. This is a standard fact of spinor algebra, placed here on the series' ideals. In dimensions three and four the product $\psi e_{t}\rev{\psi}$ is already a vector, so the projection removes nothing. In dimension five it has a second part, a multiple $s$ of the central pseudoscalar; $s$ is the only spin-invariant quadratic form on the spinor ideal (in agreement with the stored classification of invariant forms, which is not used), and the squared mass of a single constituent equals $s^{2}$, which restates the stored single-constituent mass law. For two constituents covariance allows cross terms beside the two single momenta, as many as the real dimension of the ideal's field, so the covariant quadratic vectors of two constituents form spaces of dimension three, four and six in dimensions three, four and five; requiring also invariance under a change of sign of one constituent removes the cross terms and leaves the two weights, so the additivity of momenta is a separate clause. Under these conditions the formula of H1 is forced once momentum is assumed quadratic and covariant; the existence of the spinor part, quadraticity, covariance and additivity remain assumed.

## lay
One of the assumptions behind the series' account of matter in the hidden worlds of three and five dimensions is a formula for the momentum of a basic constituent, copied from our four-dimensional world. This result shows that, in the six such worlds with one time direction, the formula is not a free choice: if momentum is to be an arrow in spacetime built from two copies of the constituent's internal state, and to turn when the state is turned, there is only one such formula up to an overall factor. Here "turn" means continuous rotations and boosts only, not mirror reflections, and this is a standard fact about spinors, placed here in the series' algebra. In five dimensions the same construction also produces a single extra number, and the mass of a lone constituent is exactly the square of that number. What is still assumed is that constituents have such an internal state at all, that momentum is built from two copies of it, and that the momenta of several constituents simply add: for two constituents the same requirement allows extra mixed terms, in three, four and five dimensions alike, so it does not single out the plain sum.

## one-liner
In the causal towers of dimension three to five the quadratic vectors of one constituent on the spinor ideal that are covariant under the connected spin group (real-quadratic, no reflections) form one real line, spanned by H1's momentum $j$, a classical fact placed on the series' ideals; $\psi e_{t}\rev{\psi}$ is a pure vector in dimensions three and four and $j + sI$ in dimension five, where the single-constituent mass is $s^{2}$; for two constituents the covariant spaces have dimension $3$, $4$, $6$, so, assuming a spinor part and momentum quadratic and covariant, H1's formula is forced up to a real factor while additivity is not.
