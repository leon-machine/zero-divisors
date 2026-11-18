---
id: synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation
kind: claim
version: 1
title: 'Lattice model: a field slaved to an operator source, and the free part'
status: proved
region: synthesis
subject: quantum-fields
tags: [quantum-gravity, entanglement, finite-models, no-go]
proposed_by:
  kind: ai
  session: 2026-11-18-navigate
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-navigate
review: draft
outside_ga:
  kind: other
  why: the free field of the model obeys canonical commutation relations, which no finite Clifford algebra holds (the stored statistics result); only the matter factor of the model is an element of the algebra
derivations:
- name: main
  uses:
  - synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane@1
  - field-theory.operator-newtonian-coupling@4
  - synthesis.locality-of-the-attached-free-fields-fixes-their-statistics@5
  - field-theory.no-canonical-commutation-relations-tower@3
  - synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_matter_factor_is_nonzero_when_paths_source_differently
- kind: check
  ref: check.py::check_free_field_keeps_its_form_and_the_response_is_minus_the_commutator
- kind: check
  ref: check.py::check_slaved_field_does_not_commute_at_spacelike_separation
- kind: check
  ref: check.py::check_free_part_restores_commutation_at_spacelike_separation
- kind: check
  ref: check.py::check_einstein_map_kernels_at_non_null_and_null_momentum
lineage:
  motivated_by:
  - pred.gravity-entangles-standard-phase
  - pred.no-gravitational-settling
  - dark-matter.imported-massless-graviton-production-rate
extraction:
  open_problem: op.graviton-rate-as-classical-field-process
  note: >-
    Carries into the store, as a model result, two steps of the working notes of 12 October 2026 behind the
    registered entanglement prediction (the radiated-record step, claim 5.1, and the radiative-sector step,
    claim R1; both were refereed then, and the registration's third addendum restated its premise (P-v) on
    their strength: "with retardation, a field with no free part fails microcausality, so the full theory needs
    a radiative sector with quantum states"). The store did not hold them, and its conventions since 10 November
    state that the gravitational gauge field has no quantum. Restated after review: the condition that fails in
    the model is commutation of the field with later matter observables at spacelike separation, which the store
    does not state (its locality theorem is about a free field's own bracket, which the slaved field satisfies);
    the extension of the element reading beyond the static limit is supplied here, not stored; and an
    instantaneous field fails the same test. The model is a scalar field on a lattice in one space dimension
    with no gauge constraint and no spin two; the transfer to the gravitational gauge field is argued, by the
    standard argument (Yang and Feldman 1950; Peierls 1952; for gravity Belenchia et al. 2018 and Danielson,
    Satishchandran and Wald 2022, as cited in those notes and not re-read in this run). Decisions for the
    maintainer: whether the series asks its gravitational field to commute with matter observables at spacelike
    separation, and if so which of the element reading and the convention of no quantum it restates; an open
    problem for the field at null momentum; the burst baseline of the dimmed-burst result, which follows that
    choice.
---

## formal
\emph{The model.} Matter is one quantum on two paths: the algebra of a completed pair $\Cl(1,1)$, $e_{1}^{2} = 1$, $e_{2}^{2} = -1$, with $v = \tfrac12(e_{1} + e_{2})$, $w = \tfrac12(e_{1} - e_{2})$, $Q(v) = Q(w) = 0$, $vw + wv = 1$ (\claimref{synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane}), path projectors $P_{1} = vw$, $P_{2} = wv$, and a source operator $J = c_{1}P_{1} + c_{2}P_{2}$ built from the commuting path numbers, as the gravitational source is in the stored static coupling (\claimref{field-theory.operator-newtonian-coupling}). After the source has acted the paths are recombined by the unit $U = p + q\,e_{2}$, $p^{2} + q^{2} = 1$, and the quantum is detected at the event $(0, t_{d})$ by $O = U^{-1}P_{1}U$. The field is a scalar on the sites $n \in \Z$ at integer times with an exact light cone, $\phi_{n}(t+1) = \phi_{n+1}(t) + \phi_{n-1}(t) - \phi_{n}(t-1)$, coupled at site $0$ at the times $t' \in \{0, \dots, 5\}$ through $g\,J\,\phi_{0}(t')$; $t_{d} = 8$. Let $G(n,t;t')$ be the retarded response at $(n,t)$ to a unit source at $(0,t')$ and $\Delta(n,t;t')$ the commutator function of the free field, $[\phi^{0}_{n}(t), \phi^{0}_{0}(t')] = I_{4}\,\Delta$ with the unit written as in the field theory. An event is spacelike to the detection when $|n| > |t - t_{d}|$. Everything in (1) to (4) is a statement about this model.
\begin{enumerate}
\item[(1)] \emph{(Matter factor; proved.)} $[J, O] = (c_{1} - c_{2})\,p\,q\,e_{2}$: nonzero exactly when the two paths source the field differently and the recombiner mixes them.
\item[(2)] \emph{(Slaved field; proved.)} If the field has no free part, $\phi_{n}(t) = g\,J\sum_{t'}G(n,t;t')$ is an element of the matter algebra, and $[\phi_{n}(t), O] = g\,[J, O]\sum_{t'}G(n,t;t')$ exactly. The sum is nonzero at $172$ of the $502$ events of the grid $|n| \le 18$, $0 \le t \le 18$ that are spacelike to the detection, among them events at the detection time itself. All values of this field are multiples of $J$ and commute with one another: the field's bracket with itself vanishes everywhere, and what fails is its commutation with the matter's later observable. A field equal to $gJ$ times any function of the event, an instantaneous one included, fails in the same way wherever the function is nonzero; the retarded rule does not cure it.
\item[(3)] \emph{(Kubo; proved.)} $G(n,t;t') = -\Delta(n,t;t')$ for $t > t'$ and $G = 0$ for $t \le t'$.
\item[(4)] \emph{(Free part; proved to first order in $g$.)} If the field is $\phi = \phi^{0} - g\,J\sum_{t'}G$ with $\phi^{0}$ a free field with the canonical commutator, and the matter evolves under the same coupling, then to first order $[\phi_{n}(t), O] = -g\,[J, O]\sum_{t'}\bigl(G + \Delta\bigr)(n,t;t')$, and by (3) the sum is $\sum_{t' \ge t}\Delta$: it vanishes at all $502$ spacelike events, is supported in the past cones of the source events, and is nonzero at timelike events. The free part alone fails to commute with $O$, as the slaved part does; it is their sum that commutes.
\item[(5)] \emph{(Where a free part of the gravitational gauge field can sit; computed.)} For the first-order curvature map $\mathcal{R}_{k}[h](B) = -\tfrac12\,k \wedge h(B \cdot k)$ of Theorem \claimref{synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel}, the Einstein map on symmetric maps has kernel of dimension four, the displacements, at every non-null $k$, and of dimension six at every nonzero null $k$ (computed at four and two momenta; the rank depends only on whether $k$ is timelike, spacelike or null). So a solution of the first-order field equation without source, modulo displacements, exists only at null momentum, with two components; the retarded, advanced and symmetric rules differ by such solutions. A free part with the commutators of (4) is canonical, and no floor of the tower holds canonical commutation relations (\claimref{field-theory.no-canonical-commutation-relations-tower}).
\end{enumerate}
\emph{Reading (argued).} The stored locality theorem (\claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}) asks that a free field's bracket with itself vanish at spacelike separation; the slaved field of (2) satisfies that trivially. The condition that fails in (2) is a different one, commutation of the field with the later observables of its source at spacelike separation, which excludes signalling and which the store does not state. If the series asks it of its gravitational gauge field, and if the element reading behind Prediction \claimref{pred.gravity-entangles-standard-phase} is extended beyond the static limit of the stored coupling with the field a function of the matter's commuting numbers and nothing else (an extension made here, not stored; the convention that the field has no quantum is read as allowing nothing else), then by the standard argument, of which (2) to (4) are the mechanism in a scalar model, the condition fails, and it is restored by a free part with canonical commutators in the two components of (5). The model has one space dimension, no gauge constraint and no spin two; for a gauge field the instantaneous part is fixed by a constraint and the observables that commute are dressed ones, which the model does not represent. The registered phase does not use the condition and is not affected. The model does not say which position the series should take, nor whether a limit on localisation makes the failure unobservable.

## technical
One quantum on two paths sources a lattice field with an exact light cone through $J = c_{1}P_{1} + c_{2}P_{2}$, is recombined, and is detected by $O$. All coefficients are integers and rationals.

If the field has no free part it is $gJ\sum G$, and its commutator with the detection, $g[J,O]\sum G$, is nonzero at $172$ of $502$ spacelike events. Its bracket with itself vanishes; what fails is commutation with the matter's later observable, and an instantaneous slaved field fails likewise.

If the field has a free part with canonical commutators, the matter's evolution under the same coupling adds $-g[J,O]\sum\Delta$, and since the retarded response is minus the commutator function (Kubo), the total vanishes at every spacelike event, to first order.

For the gravitational gauge field a free part can sit only at null momentum, in two components (Einstein-map kernels four and six).

The reading for gravity is argued: if the series requires its gravitational field to commute with matter observables at spacelike separation, the element reading extended beyond the static limit with a field that has no variable of its own does not meet it; the store states neither that requirement nor that extension.

Ledger: transport-absent. Standard physics (the Yang-Feldman and Peierls structure; for gravity the argument of Belenchia et al. and of Danielson, Satishchandran and Wald), carried into the store from the working notes of 12 October 2026.

## lay
The series predicts that gravity entangles two masses. That prediction treats the gravitational field of a mass as fixed by where the mass is, even when the mass is in two places at once. The series also says that the gravitational field has no quanta of its own.

This result is a small exact model of what follows if both are taken at face value everywhere. A field that only ever repeats what its source did ends up carrying information about which path the source took. It then fails to commute with a later measurement of the source at places no signal from that measurement can reach, which in principle allows signalling. In the model the failure goes away if the field has an independent part of its own with quantum behaviour, the role gravitons play in the standard account.

The model is a toy: one dimension of space, a simple field, none of the special features of gravity. It shows the mechanism, not a theorem about gravity. Nothing here changes the predicted entanglement. But the series has not said whether it requires its gravitational field to pass this test, and if it does, it has a choice to make between its two statements.

## one-liner
In an exact lattice scalar model, a field slaved to an operator source ($J = c_{1}P_{1} + c_{2}P_{2}$ on two paths) fails to commute with the source's later detection at $172$ of $502$ spacelike events, and a free part with canonical commutators restores commutation at all of them to first order (retarded response equals minus the commutator function); argued from this: if the series requires such commutation of its gravitational field, the element reading extended beyond the static limit with a field that has no variable of its own does not meet it.
