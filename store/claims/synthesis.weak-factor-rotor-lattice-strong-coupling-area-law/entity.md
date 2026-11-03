---
id: synthesis.weak-factor-rotor-lattice-strong-coupling-area-law
kind: claim
version: 2
title: In Wilson's lattice form, which needs no gauge fixing for any compact group, the weak factor of the derived gauge algebra has rotor links, its Haar gluing rule is $\int\langle XU\rangle_0\langle\widetilde{U}Y\rangle_0\,dU = \tfrac14\langle XY\rangle_0$, and every rectangular Wilson loop has leading strong-coupling coefficient $(\beta/4)^{A}$, the same area law as compact $U(1)$ with $(\beta/2)^{A}$
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, rotors-and-stabilisers, recovers-known-physics, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_bivectors_close_to_su2_and_product_matches_ga
- kind: check
  ref: check.py::check_finite_groups_reproduce_haar_moments
- kind: check
  ref: check.py::check_gluing_rule_and_gauge_variant_averages_vanish
- kind: check
  ref: check.py::check_closed_loops_gauge_invariant
- kind: check
  ref: check.py::check_strong_coupling_area_law_leading_coefficients
- kind: check
  ref: check.py::check_compact_u1_has_the_same_strong_coupling_area_law
- kind: check
  ref: check.py::check_scalar_part_of_exponential_is_cosine_series
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.composite-gauge-bosons-what-excluded
  - field-theory.fock-space-maxwell-modes
extraction:
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s list of imports of 2026-11-01: a uses edge to the imported Fact synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement@1 (Wilson 1974, Osterwalder-Seiler 1978, Elitzur 1975, beta = 4/g^2 for SU(2), the deconfined phase of compact U(1) by Guth and by Froehlich-Spencer), which replaces the citations from memory. Statement and check unchanged.'
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    The problem asks for the non-abelian fields quantised with a gauge fixing or an equivalent, and what
    the series says on confinement and asymptotic freedom. Wilson's lattice formulation is the equivalent
    for a compact group: link variables in the group, Haar measure, no gauge fixing. In geometric algebra
    the weak factor su(2) is the bivector algebra of Cl(3,0), links are rotors and the trace is the scalar
    part. Established exactly: the bivectors close to su(2) with a negative-definite trace form; the Haar
    moments on the unit three-sphere, reproduced by the 24 Hurwitz units through degree 5 and by the
    quaternion group through degree 3; the gluing rule and the vanishing of every gauge-variant link
    average on every basis pair (complete by bilinearity); gauge invariance of closed loops under rational
    vertex rotors; the leading strong-coupling coefficient (1/4)^A of every rectangular Wilson loop (proved
    by a tree gauge and a Haar-invariant change of variables, computed for 1x1, 2x1, 2x2), and (1/2)^A for
    compact U(1). Because compact U(1) has the same strong-coupling area law, the result says nothing about
    confinement in the continuum; that needs the continuum limit, which in turn needs asymptotic freedom,
    the sign of the one-loop coefficient, computed conditionally on the content and the doublet count in
    the result (synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces).
    That the lattice needs no gauge fixing is Wilson's standard result for every compact group. The literature (Wilson 1974 for the action
    and the strong-coupling expansion, Osterwalder-Seiler for reflection positivity and the full
    strong-coupling area law, Elitzur's theorem, beta = 4/g^2 for SU(2), the proved deconfinement of
    four-dimensional compact U(1) at weak coupling by Guth and by Froehlich and Spencer) is imported
    (synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement). Transport-absent: the series supplies the gauge algebra,
    and the unit i = I4 plays no part on the Euclidean lattice.
---

## formal
Represent the $\su(2)$ factor of $\su(2) \oplus \su(3) \oplus \uu(1)$ (Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}) by the bivectors $B_1 = g_2g_3$, $B_2 = g_3g_1$, $B_3 = g_1g_2$ of $\Cl(3,0)$, and its group by the rotors $U = u_0 + u_1B_1 + u_2B_2 + u_3B_3$, $U\widetilde{U} = 1$, with the normalised Haar measure $dU$ of the unit three-sphere. On a square lattice give each oriented link a rotor ($\widetilde{U}$ for the reversed link), let $U_p$ be the ordered product round a plaquette $p$, and take the weight $\prod_p\exp(\beta\langle U_p\rangle_0)$.
\begin{enumerate}
\item[(i)] The $B_k$ close under the commutator with $[B_1, B_2] = -2B_3$ and cyclically, and $\langle B_jB_k\rangle_0 = -\delta_{jk}$: a compact $\su(2)$.
\item[(ii)] $\int u^{\alpha}\,dU = \prod_k(\alpha_k - 1)!!\,/\,\prod_{j=0}^{|\alpha|/2 - 1}(4 + 2j)$ when every $\alpha_k$ is even, and $0$ otherwise.
\item[(iii)] For all $X$, $Y$ in the even subalgebra, $\int\langle XU\rangle_0\,dU = 0$ and $\int\langle XU\rangle_0\langle\widetilde{U}Y\rangle_0\,dU = \tfrac14\langle XY\rangle_0$.
\item[(iv)] Under $U_{xy} \mapsto g_xU_{xy}\widetilde{g_y}$ with rotors $g$ at the sites, $\langle U_C\rangle_0$ is invariant for every closed path $C$, so expectations of gauge-invariant observables need no gauge fixing.
\item[(v)] For an $R \times T$ rectangle $C$ of area $A = RT$, the term of order $\beta^{A}$ in $\langle\langle U_C\rangle_0\rangle$ from the $A$ plaquettes of the rectangle is $\int\langle U_C\rangle_0\prod_{p \subset C}\langle U_p\rangle_0 = (\tfrac14)^{A}$, so its leading strong-coupling coefficient is $(\beta/4)^{A}$, an area law.
\item[(vi)] For compact $U(1)$, with links $a + bB_3$, the gluing coefficient is $\tfrac12$ and the corresponding coefficient is $(\beta/2)^{A}$: the same area law.
\item[(vii)] For a bivector $B$ of $\Cl(3,0)$, $B^2 = -\|B\|^2$ with $\|B\|^2 = \sum_k b_k^2$, so $1 - \langle\exp B\rangle_0 = \tfrac12\|B\|^2 - \tfrac1{24}\|B\|^4 + \cdots$, the cosine series.
\end{enumerate}
So at finite lattice spacing the weak factor is a quantised gauge field with no gauge fixing and no ghosts, as in Wilson's formulation for every compact group; its strong-coupling area law is shared with compact $U(1)$, so it is not evidence of confinement in the continuum, whose existence needs asymptotic freedom.

## technical
Wilson's lattice formulation quantises any compact gauge group without gauge fixing (a standard result): link variables live in the group, the measure is Haar, and only gauge-invariant loops are observed. In geometric algebra the weak factor $\su(2)$ of the derived gauge algebra is the bivector algebra of $\Cl(3,0)$, its group the rotors, and the trace the scalar part. The Haar moments on the unit three-sphere are rational, and the averages that matter are reproduced exactly by the 24 Hurwitz units. Two rules carry the strong-coupling expansion: every gauge-variant link average vanishes, and integrating a link shared by two loops glues them with a factor $\tfrac14$, $\int\langle XU\rangle_0\langle\widetilde{U}Y\rangle_0\,dU = \tfrac14\langle XY\rangle_0$. With the weight $\exp(\beta\langle U_p\rangle_0)$ per plaquette, every rectangular Wilson loop of area $A$ then has leading coefficient $(\beta/4)^{A}$, an area law. Compact $U(1)$ gives $(\beta/2)^{A}$, so the area law at strong coupling is not specific to the non-abelian factor and says nothing about confinement in the continuum; four-dimensional compact $U(1)$ is known to deconfine at weak coupling. The plaquette action expands as the cosine series $\tfrac12\|B\|^2 - \tfrac1{24}\|B\|^4 + \cdots$ of the plaquette bivector.

## lay
The weak force's symmetry, which the series derives, can be put on a spacetime lattice in the form introduced by Wilson, with each link carrying a rotation of the spacetime algebra. As in Wilson's construction for any such symmetry, this quantises the field directly, with no need to fix a gauge. When the coupling is strong, at leading order of the strong-coupling expansion the energy of a pair of test charges grows with their separation, the signature of confinement. The same happens for the electromagnetic symmetry on the lattice, so this alone does not show that the weak or strong force confines in the real, continuum world; that question needs the behaviour of the coupling at short distances.

## one-liner
In Wilson's lattice form (no gauge fixing, standard for compact groups), with rotor links of $\Cl(3,0)$ for the derived $\su(2)$ and Haar measure, gauge-variant averages vanish, the gluing rule is $\int\langle XU\rangle_0\langle\widetilde{U}Y\rangle_0 = \tfrac14\langle XY\rangle_0$ and every rectangular Wilson loop has leading strong-coupling coefficient $(\beta/4)^{A}$, as compact $U(1)$ has $(\beta/2)^{A}$, so the lattice quantises the factor without gauge fixing but its area law says nothing about continuum confinement.
