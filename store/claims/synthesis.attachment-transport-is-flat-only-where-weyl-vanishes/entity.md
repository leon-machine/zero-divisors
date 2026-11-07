---
id: synthesis.attachment-transport-is-flat-only-where-weyl-vanishes
kind: claim
version: 2
title: 'The attachment''s transport supplies a state only where Weyl vanishes'
status: proved
region: synthesis
subject: quantum-fields
tags: [conformal-spinors, tractors, gauge-fields, no-go]
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - synthesis.imported-gtg-dictionary@1
  - field-theory.twistor-attachment@6
  - synthesis.attachment-conformal-energy-is-generated-by-z@4
  - field-theory.where-each-lives@3
  - synthesis.imported-twistor-equation-integrability-petrov-n-or-o@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_samples_are_weyl_maps_of_each_petrov_type
- kind: check
  ref: check.py::check_schouten_drops_out_of_the_field_strength
- kind: check
  ref: check.py::check_parallel_conformal_spinors_by_petrov_type
- kind: check
  ref: check.py::check_cotton_block_only_cuts_the_type_n_kernel
- kind: check
  ref: check.py::check_no_conformal_energy_generator_commutes_with_weyl
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.twistor-attachment
  - field-theory.ground-does-not-attach-modes
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection
extraction:
  open_problem: op.qft-on-gtg-fields
  note: >-
    Answers the first attack line of op.qft-on-gtg-fields (attach the modes through the tractor transport
    beyond conformal flatness) negatively and names the datum. The attachment's one-particle structure is the
    conformal spinor space with its form h, the u(2,2) action and the grading Z; on a gravitational field the
    tractor gauge field transports conformal spinors with curvature its field strength, whose derivative-free
    part is minus the Weyl curvature (the stored tractor theorem, clause (iv)), so the Schouten map, hence the
    Ricci curvature and the matter, does not enter. The annihilated subspace has complex dimension 4, 2, 0 at
    type O, N and other points (the standard integrability condition Psi_ABCD omega^D = 0 of the twistor
    equation, reproduced in Cl(2,4)), and no conformal-energy generator commutes with a nonzero Weyl curvature.
    So the attachment's tractor transport constructs the one-particle space only on Weyl-flat regions;
    elsewhere it supplies no state, and a state (a positive-frequency choice) has to come from another
    construction; other constructions are not excluded (the field algebra itself exists on every globally
    hyperbolic field: the imported Fact synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field,
    cited, not used). The converse direction (W = 0 on a region makes the
    whole tractor field strength vanish) is proved in synthesis.twistor-flat-fields-give-nordstrom-not-einstein, clause (i), from the stored Weyl theorem. Transport-convenient. Literature: the integrability condition of the twistor equation and
    its restriction to Petrov types N and O (Penrose and Rindler vol. 2, Ch. 6; Gasperin and Pais,
    arXiv:2404.05883), the imported Fact synthesis.imported-twistor-equation-integrability-petrov-n-or-o; the
    Dirac CAR algebra on a gravitational field (Dimock 1982), the imported Fact
    synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field, cited in the proof's Reading and not
    used.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01 importing the cited literature as Facts: a uses edge to synthesis.imported-twistor-equation-integrability-petrov-n-or-o@1 replaces the citation of Penrose-Rindler and Gasperin-Pais in the proof of (ii); Dimock 1982 is now cited as the Fact synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field in the Reading, without a uses edge, since the result does not use it. Statement, proof and checks otherwise unchanged.'
  flags:
  - 'algebraic integrability only: the dimensions are those of the subspace annihilated by the curvature at a point, an upper bound for the parallel subspace; existence of the two type N parallel directions on a region is not claimed'
---

## formal
Let $(\hb, \Omega)$ be a torsion-free gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $\Omega_{T}$ its tractor gauge field and $F_{T}$ the field strength of $\Omega_{T}$ (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), and let a bivector of $\Cl(2,4)$ act on the conformal spinor space $\CS$ (Proposition \claimref{field-theory.where-each-lives}) by left multiplication, so that a $\CS$-valued field is parallel when $a\cdot\nabla\psi + \tfrac12\Omega_{T}(a)\psi = 0$ for every $a$, and a bivector field $X$ (an adjoint tractor) when $a\cdot\nabla X + \Omega_{T}(a)\times X = 0$. Write $\mathcal{W}$ for the Weyl curvature, an $I_{4}$-linear map on spacetime bivectors, and give each point the Petrov type of $\mathcal{W}$ there.
\begin{enumerate}
\item[(i)] \emph{(Ricci blindness; proved.)} $F_{T}(A\wedge B) = -\mathcal{W}(A\wedge B) + \nO\wedge C(A, B)$, with $C$ the Cotton term: the Schouten map, hence the Ricci curvature, enters only through $C$, which vanishes on every Einstein space (Ricci curvature proportional to the metric, $\Sch = \tfrac{\Lambda}{6}\id$); under Einstein's equations with matter it does not vanish in general.
\item[(ii)] \emph{(Parallel conformal spinors; proved.)} A parallel $\CS$-valued field is annihilated by every $F_{T}(A\wedge B)$ at every point. The subspace of $\CS$ annihilated by the Weyl bivectors has complex dimension $4$ at type O points, $2$ at type N points, where it is the subspace annihilated by left multiplication by the repeated principal null vector $k$, and $0$ at points of type I, II, D and III; a nonzero Cotton term can only reduce it. Where $F_{T} = 0$ on a simply connected region (in four dimensions this is the case exactly where $\mathcal{W} = 0$, by the twistor-flat result (\claimref{synthesis.twistor-flat-fields-give-nordstrom-not-einstein})) the parallel conformal spinors form a space of complex dimension $4$ carrying the attachment's $\mathfrak{u}(2,2)$ action, form $h$ and grading $Z$ unchanged.
\item[(iii)] \emph{(No conformal-energy generator; proved.)} The bivectors of $\Cl(2,4)$ commuting with every $F_{T}(A\wedge B)$, which contain every parallel adjoint tractor, span $15$ dimensions at type O points, $5$ at type N points and $1$ (the multiples of $E = e_{+}e_{-}$) at points of type I, II, D and III; at every point with $\mathcal{W} \neq 0$ each of them annihilates a null vector under the commutator product, while every nonzero multiple of a rotor conjugate of the attachment's conformal-energy generator $Z = e_{0}\nu$ (the grading of the massless, conformally invariant modules; for massive fields $Z$ is not a symmetry even where $\mathcal{W} = 0$) annihilates only a negative-definite $4$-plane. So no conformal-energy generator is parallel through a point where the Weyl curvature is nonzero.
\end{enumerate}
Hence the tractor transport carries the attachment's one-particle structure across a region only where $\mathcal{W} = 0$: on a general gravitational field the attachment's tractor transport does not construct the one-particle space and supplies no state (no choice of positive frequency); a state must come from another construction, which this result does not exclude.

## technical
The series attaches its modes to spacetime through the conformal spinor space: a four-dimensional complex space with an invariant form of signature $(2,2)$, the conformal algebra $\mathfrak{u}(2,2)$ acting on it, and the central rotation $Z$, whose grading gives the positive conformal energy. On a gravitational field the natural way to carry this space from point to point is the tractor gauge field, and the space survives transport only where that field's curvature annihilates it.

The curvature acting on conformal spinors is minus the Weyl curvature plus a Cotton term; the Ricci curvature, and with it the matter, drops out. Where the Weyl curvature vanishes the whole space is parallel (on such regions the Cotton term vanishes too, by the twistor-flat result (\claimref{synthesis.twistor-flat-fields-give-nordstrom-not-einstein})). Where it does not, the annihilated part has complex dimension $2$ at points of Petrov type N (the spinors killed by the repeated principal null vector) and $0$ at points of every other type, the standard integrability condition of the twistor equation reproduced in $\Cl(2,4)$. No conformal-energy generator commutes with a nonzero Weyl curvature either: everything that does annihilates a null vector, while such a generator annihilates only a negative-definite plane.

So off Weyl-flat regions the attachment's tractor transport gives no one-particle space and supplies no state, the choice of positive frequency; that choice has to come from another construction. The grading $Z$ concerns the massless, conformally invariant modules. The result is transport-convenient.

## lay
The series links its quantum modes to spacetime through a special four-dimensional space of spinors, which in flat space comes with a built-in notion of positive energy. In a gravitational field one has to carry that space from point to point, and gravity's tidal part, the Weyl curvature, twists it on the way. This result shows that the space survives only where that tidal part vanishes: at a point of one special radiation type half of it can survive, and at every other point none of it, and the built-in notion of positive energy is lost. So in a general gravitational field this way of attaching the modes does not fix the quantum state; the state has to be supplied in some other way.

## one-liner
On a gravitational field the attachment's conformal spinors can be parallel for the tractor gauge field only where the Weyl curvature vanishes (a two-dimensional subspace at type N points, none at types I, II, D, III), and no conformal-energy generator commutes with a nonzero Weyl curvature, so off Weyl-flat regions the tractor transport of the attachment supplies no state.
