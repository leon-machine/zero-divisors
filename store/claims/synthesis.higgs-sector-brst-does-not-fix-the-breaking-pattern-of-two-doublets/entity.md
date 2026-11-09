---
id: synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets
kind: claim
version: 1
title: 'Higgs-sector BRST does not fix the breaking pattern of two doublets'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, symmetry-breaking, no-go, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
review: draft
derivations:
- name: main
  uses:
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent@3
  - synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta@4
  - synthesis.rung-field-on-the-lift-locus@5
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@6
  - synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_generators_form_the_electroweak_algebra_on_two_doublets
- kind: check
  ref: check.py::check_potential_is_gauge_invariant
- kind: check
  ref: check.py::check_free_brst_symmetry_needs_a_stationary_vacuum
- kind: check
  ref: check.py::check_goldstone_rank_is_three_exactly_on_aligned_doublets
- kind: check
  ref: check.py::check_one_coupling_sign_decides_the_pattern
- kind: check
  ref: check.py::check_lift_locus_rank_three_exactly_on_the_boundary
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta
extraction:
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Cross-reference: the intended citations of the sibling field-level BRST result (its (ii) for nilpotency, its (iv), (v) for the gauge-fixed masses) are now plain cross-references to its stored id (extraction note only); statement unchanged.'
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Attack on the item "Higgs-sector BRST: the field-level differential with the Goldstone and doublet terms
    (s phi), and the breaking pattern derived from the series' scalar sector instead of the aligned vacuum taken as
    input" of op.qft-non-abelian-gauge-fields, from the adversarial side: what the BRST structure needs of the
    vacuum, and whether it can supply the breaking pattern. The stored quartet result
    (synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta (v))
    takes the two doublets' neutral aligned vacuum as input and computes rank three. Found: the full scalar
    differential needs no condition on the vacuum, but its free part, the one the quartet construction quantises, is
    a symmetry of the quadratic action only at a stationary point of the potential; the Goldstone rank of two doublets
    is 0, 3 or 4, with 3 exactly for aligned doublets; and two gauge-invariant quartics differing in the sign of one
    coupling have their global minima on the neutral pattern and on a charge-breaking one, with the BRST structure
    consistent in both. So the breaking pattern is an output of the potential, not of the BRST construction. On the
    rung field's lift locus the rank is 3 exactly on the charge-preserving boundary of the stored orbit space and 4
    inside, never 0, and the stored D-term vacuum lies on the boundary: there the potential does derive the pattern;
    this clause is a corollary of stored clauses (synthesis.rung-field-on-the-lift-locus (1), where the stabiliser is
    trivial or a circle, and synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus (1), (2)), restated
    in doublet language. Doublets are even elements of Cl(3,0) on e0, e1, e2 in the realisation of the stored bivector
    form of the gauge algebra (weak T_a = e12/2, e20/2, e01/2 on the left, hypercharge y phi e12 on the right, y = 1/2),
    the same realisation as
    synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge; as real representations a doublet of
    hypercharge 1/2 and one of -1/2 are the same, so the statements hold for the series' pair. Cross-reference: the nilpotency of s on the scalar sector
    for every vacuum is (ii) of synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge, and the
    't Hooft-gauge mixing cancellation and the equality of vector, Goldstone and ghost masses used in (iii) are its
    (iv), (v); here both are given in one line each, with the BRST symmetry of the gauge-fixed action from Fact
    synthesis.imported-brst-kugo-ojima-strocchi-and-gribov (i). Prior art, cited from memory and not used: the
    Chevalley-Eilenberg form of BRST nilpotency for a matter representation (C. Becchi, A. Rouet and R. Stora,
    Ann. Phys. 98 (1976) 287; I. V. Tyutin, 1975); the R_xi gauges (K. Fujikawa, B. W. Lee and A. I. Sanda, Phys.
    Rev. D 6 (1972) 2923); charge-breaking minima of two-doublet potentials and their exclusion when a neutral
    minimum exists (P. M. Ferreira, R. Santos and A. Barroso, Phys. Lett. B 603 (2004) 219; I. P. Ivanov, Phys.
    Rev. D 75 (2007) 035001). The counter-model pair of (iii) is that classical two-doublet fact (the sign of the
    coupling of the alignment invariant decides between neutral and charge-breaking minima), given here in
    geometric-algebra form with exact minima; the rank statement (ii) is standard. New for the store: the
    stationarity condition (i) for the free BRST of the stored quartet construction, and the reading that the BRST
    construction is consistent for either pattern.
    What is not claimed: which pattern the series' own potential selects beyond the D-term case (the stored
    theorem leaves the global minimum with an added invariant open), the interacting BRST charge, or anything
    non-perturbative. Transport-absent.
---

## formal
Realise the gauge algebra of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} by bivectors as in \claimref{synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent}, the weak factor being $T_{1}, T_{2}, T_{3} = \tfrac12e_{12}, \tfrac12e_{20}, \tfrac12e_{01}$ in $\Cl(3,0)$ on $e_{0}, e_{1}, e_{2}$, and read each of two doublets as an even element $\phi = \phi^{0} + \phi^{1}e_{12} + \phi^{2}e_{02} + \phi^{3}e_{01}$, with $\rho(T_{a})\phi = T_{a}\phi$, colour acting by $0$ and hypercharge by $\rho(Y)\phi = y\,\phi e_{12}$, $y = \tfrac12$, and with the real form $\langle\phi, \psi\rangle = \langle\widetilde{\phi}\psi\rangle_{0}$. (As real representations a doublet of hypercharge $\tfrac12$ and one of hypercharge $-\tfrac12$ coincide, so this covers the two doublets of Theorem \claimref{synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta}(v); no statement below depends on the value of $y \ne 0$.) For $\Phi = (\phi_{1}, \phi_{2})$ put $N_{k} = \langle\widetilde{\phi}_{k}\phi_{k}\rangle_{0}$, $\psi = \widetilde{\phi}_{1}\phi_{2}$, $K = \langle\psi\rangle_{0}^{2} + \langle\psi\widetilde{e_{12}}\rangle_{0}^{2}$ and $K' = \langle\psi\widetilde{e_{02}}\rangle_{0}^{2} + \langle\psi\widetilde{e_{01}}\rangle_{0}^{2}$. Extend the stored differential by $s\Phi = -g\rho(c)\Phi$; for a constant vacuum $v$ write $\Phi = v + h$ and split $s = s_{0} + s_{1}$ by field degree ($s_{0}h = -g\rho(c)v$, $s_{0}A = \nabla c$, $s_{0}c = 0$), and let $S = S_{1} + S_{2} + \dots$ be the 't Hooft-Feynman gauge-fixed action (canonical normalisation $-\tfrac14\kappa_{ab}F^{a}_{\mu\nu}F^{b\,\mu\nu}$) with a gauge-invariant polynomial potential $V$, split by degree in the fields.
\begin{enumerate}
\item[(i)] \emph{(The vacuum condition.)} $\rho$ is a representation of $\su(2) \oplus \uu(1)$ by maps antisymmetric for the real form, with no nonzero invariant vector on the eight components; so $s^{2}\Phi = 0$ for every $\Phi$ and every $v$, and the full differential needs no condition on the vacuum. Its free part $s_{0}$ is nilpotent and is a symmetry of the quadratic action $S_{2}$ exactly when $\rho(X)\nabla V(v) = 0$ for every $X$, that is, for two doublets, exactly when $v$ is a stationary point of $V$; off a stationary point $s_{0}S_{2} = -s_{1}S_{1} = g\langle\nabla V(v), \rho(c)h\rangle \ne 0$.
\item[(ii)] \emph{(Goldstone rank.)} $K + K' = N_{1}N_{2}$, and $N_{k}$, $K$, $K'$ are gauge invariant. The Goldstone map $X \mapsto \rho(X)\Phi$ has rank $0$ at $\Phi = 0$, rank $3$ exactly when $\Phi \ne 0$ and $K' = 0$ (the two doublets aligned, $\phi_{2} = \phi_{1}z$ or $\phi_{1} = \phi_{2}z$ with $z \in \mathrm{span}\{1, e_{12}\}$), leaving one unbroken $\uu(1)$, and rank $4$ otherwise, breaking the whole electroweak factor.
\item[(iii)] \emph{(The pattern is not a BRST output.)} With $V_{\kappa, w} = (N_{1} + N_{2} - w)^{2} + (N_{1} - N_{2})^{2} + \kappa K$: $V_{-1, 3/2} = \tfrac34(N_{1} + N_{2} - 2)^{2} + \tfrac54(N_{1} - N_{2})^{2} - \tfrac34 + K'$, so its global minima are exactly the aligned pairs with $N_{1} = N_{2} = 1$ (rank $3$: nine massless and three massive vectors, five physical scalars, the stored count); $V_{1, 2} \ge 0$ with equality exactly when $N_{1} = N_{2} = 1$ and $K = 0$ (rank $4$, for example $\Phi = (1, e_{02})$: eight massless and four massive vectors, four physical scalars). Both minima are stationary, so by (i) the free BRST symmetry holds in both models; the gauge-fixed action is BRST invariant in both (Fact \claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}(i)), and in the 't Hooft-Feynman gauge the vector-Goldstone mixing is a total derivative and each massive vector, its Goldstone mode and its ghosts share one mass, at either rank, so the quartet positivity of the stored theorem applies to each massive vector of the diagonalised mass matrix. The two models differ only in the sign of the coefficient of $K$: the breaking pattern is decided by the potential and not by the BRST construction. (This is the classical two-doublet fact that the sign of the alignment coupling decides between neutral and charge-breaking minima, in geometric-algebra form.)
\item[(iv)] \emph{(The lift locus; a corollary of stored clauses.)} In the setting of Theorems \claimref{synthesis.rung-field-on-the-lift-locus} and \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}, put $\phi_{1} = \alpha$ and $\phi_{2} = \bar{\beta}$, read in $\Cl(3,0)^{+}$ by $(z_{1}, z_{2}) \mapsto z_{1} + e_{01}z_{2}$ with $\mathrm{span}\{1, I_{4}\}$ read as $\mathrm{span}\{1, e_{12}\}$ acting on the right; then the slot $U(2)$ acts on both as on a doublet, the span$\{1, e_{12}\}$ part of $\widetilde{\phi}_{2}\phi_{1}$ is $\phi_{2}^{\dagger}\phi_{1} = \alpha^{\mathsf T}\beta = Q(c)$, and $\mathsf{N}^{2} - m^{2} = N_{1}N_{2}$. On the null-lift locus $Q(c) = -H^{2}$, so $K = H^{4}$ and $N_{1}N_{2} = H^{4} + K' \ge H^{4}$: the Goldstone rank is $3$ exactly on the boundary $\mathsf{N}^{2} - m^{2} = H^{4}$, the charge-preserving orbits, and $4$ in the interior, and never $0$, so the rung field on the locus has no unbroken electroweak phase; the D-term vacuum of the stored theorem lies on the boundary. This restates, in doublet language, the stabilisers of the lift-locus theorem (1) (a circle on the boundary orbits, trivial inside) and the D-term theorem (1), (2).
\end{enumerate}

## technical
The scalar part of the BRST differential, the gauge transformation of the two doublets with the gauge parameter replaced by the ghost, squares to zero for every field value: it only needs the doublets to carry a representation of the gauge algebra, so no condition on the vacuum enters there. A condition does enter one step later. The stored positivity result quantises the free theory about a vacuum, with its free BRST charge, and that free charge is a symmetry of the free action only if the vacuum is a stationary point of the potential: off such a point the linear term of the potential spoils the invariance of the quadratic action, because the doublets carry no invariant direction. The second finding is that the BRST construction cannot choose the breaking pattern. Two doublets break the electroweak factor to the photon's $\uu(1)$ exactly when they are aligned, and break it completely otherwise. Two simple gauge-invariant potentials, differing only in the sign of the term measuring alignment, have their lowest points on the neutral pattern (three massive vectors) and on a charge-breaking one (four massive vectors, a massive photon), and the BRST machinery, gauge fixing and positivity of physical states work equally in both. So the neutral pattern must come from the potential. On the rung field's constrained surface, the two doublets have a fixed nonzero inner product, so they always break the symmetry, the photon is massless exactly on the boundary of the orbit space found earlier, and the stored D-term potential puts its vacuum on that boundary.

## lay
The Higgs field gives the W and Z bosons their mass while leaving the photon massless. The series has two Higgs-like fields, and earlier work assumed the way they settle leaves the photon massless, then checked that the quantum bookkeeping of the forces (the BRST method, which removes unphysical states) works. This result asks whether that bookkeeping could itself force the photon to stay massless. It cannot: the bookkeeping works just as well when the fields settle in a way that gives the photon a mass, as an explicit pair of examples shows, differing only in the sign of one number in the energy of the fields. It does demand that the fields sit at a balanced point of their energy. So which pattern nature picks has to come from the energy of the fields; on the constrained version of the series' field with its simplest energy, it does pick the massless photon.

## one-liner
The scalar BRST differential $s\Phi = -g\rho(c)\Phi$ of two doublets (even elements of $\Cl(3,0)$) is nilpotent at every vacuum, but its free part is a symmetry of the quadratic action only at a stationary point; the Goldstone rank is $3$ exactly for aligned doublets and $4$ otherwise, and two quartics differing in the sign of one coupling have neutral and charge-breaking global minima with the BRST structure intact in both, so the pattern is fixed by the potential, not by BRST; on the rung lift locus the rank is $3$ exactly on the charge-preserving boundary and never $0$ (a restatement of stored clauses).
