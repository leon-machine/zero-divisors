---
id: synthesis.locality-of-the-attached-free-fields-fixes-their-statistics
kind: claim
version: 5
title: 'Locality fixes the statistics of the attached free fields'
status: proved
region: synthesis
subject: quantum-fields
tags: [car-algebra, conformal-spinors, no-go, recovers-known-physics]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'GA rewrite (metric components as frame products)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - field-theory.second-quantisation@5
  - field-theory.fock-space-maxwell-modes@4
  - field-theory.twistor-attachment@6
  - field-theory.imported-tower-limit@3
  - field-theory.imported-statistics-no-go-palatial-algebra@2
  - field-theory.no-canonical-commutation-relations-tower@3
  - field-theory.how-close-tower-comes-ccr@4
  - synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_polarisation_sums_have_degree_two_s
- kind: check
  ref: check.py::check_locality_selects_the_statistics
- kind: check
  ref: check.py::check_storeys_carry_opposite_brackets
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.imported-standard-field-theory
  - field-theory.twistor-attachment
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The metric components of the polarisation algebra are written as products of the spacetime algebra''s frame vectors, g_{mu mu} = Q(gamma_mu) and g_{mu nu} = gamma_mu . gamma_nu (the same numbers; for the propagator, -gamma_mu . gamma_nu/k^2 is the component reading of a -> -a/k^2); the remaining indices are components on the frame gamma_mu, the algebra''s own vectors; notation only.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The i0 prescription of the imported two-point function in the proof is written in scalar form with the field theory''s unit I_4, which the entity already uses for D_+ = int d mu e^{-I_4 k.xi} (U1; one unit per entity): -1/(4 pi^2 (Q(xi) - I_4 0 xi_0)), as the Fact now states it. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The plane-wave phases of the free fields and of the two-point function, the momentum substitution P(I_4 d) and the overall factor -I_4^d/(4 pi^2) now use the field theory''s unit I_4 (numbers read in span{1, I_4}); the i0 of the imported boundary value -1/(4 pi^2 (Q(xi) - i0 xi_0)) stays, a boundary-value prescription quoted from the Fact.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s list of imports of 2026-11-01: a uses edge to the imported Fact synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem@1 (the massless two-point function D+ with its spacelike evenness, and Pauli''s free-field argument), which replaces the citations from memory; the pin of field-theory.twistor-attachment moves to @6, which now carries a marked note citing this result for the free fields. Statement and check unchanged.'
  open_problem: op.qft-structural-inputs
  note: >-
    The problem's attack line "spin-statistics from the tower's CAR limit and the palatial storey's CCR together
    with the attachment", done by Pauli's free-field argument (Pauli 1940, standard; imported in
    synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem) on the
    series' own polarisation sums. What it trades: for the free fields the store has (scalar, spinor, photon),
    the twistor attachment's sentence "a CAR lift is local exactly when 2s is odd", which rested on the imported
    Jost-point theorem, now follows from locality with positive norm, the stored sums and the massless two-point function. What it
    does not do: it assumes locality (microcausality) and positive energy; it is not the general Wightman
    theorem; interacting fields are untouched. Consequences: an elementary local rung scalar must be a palatial
    (CCR) field, and the tower's odd rung vectors cannot be its quanta as a local CAR field. The sign (-1)^{2s} is
    also the value factor of the boost rotor continued over one modular period; a derivation from modular
    covariance is a different route with a different premise (locality with positive norm here, modular covariance there; synthesis.modular-period-on-values-is-the-dual-plane-turn. With an indefinite form the conclusion reverses for c = -1, the Faddeev-Popov case (synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts). The massless two-point function
    (normalisation and spacelike evenness) is imported in the same Fact; only f = 1/Q and its evenness enter the check.
    Transport-convenient: the sums and storeys are the series' objects; the locality argument is standard. Kill
    conditions registered before computing (spinor sum of even degree, photon sum of odd degree, the photon's
    P(d)(1/Q) vanishing at spacelike points) did not fire.
---

## formal
Let $f(\xi) = 1/Q(\xi)$, and take the massless two-point function $D_{+}$, which on the open spacelike set equals $-f/(4\pi^{2})$ and is even under $\xi \to -\xi$ (standard; Fact \claimref{synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem}(i)). For an attached free field with particle and antiparticle parts carrying a polarisation sum $P$, a polynomial in $k$ homogeneous of degree $d$, with weights $1$ and $c \neq 0$ ($c > 0$ when the field's Fock space has a positive norm), and with bracket sign $\eta = +1$ (CAR, anticommutator) or $-1$ (CCR, commutator):
\begin{enumerate}
\item The stored fields' sums are $P = 1$ (scalar, $d = 0$), $P(k) = k\gamma_{0} = 2k_{0}\Lambda(k)$ with $\Lambda$ the projector of Proposition \claimref{field-theory.second-quantisation} ($d = 1$), and for the Riemann-Silberstein photon of Proposition \claimref{field-theory.fock-space-maxwell-modes}, on bivectors $A$, $B$, $P(k)[A, B] = \sum_{\epsilon}\langle A(k \wedge \epsilon)\rangle_{0}\langle B(k \wedge \epsilon)\rangle_{0}$ over transverse $\epsilon$, which on the null cone equals the quadratic $-\langle A(k \wedge \gamma_{0})\rangle_{0}\langle B(k \wedge \gamma_{0})\rangle_{0} + \sum_{i}\langle A(k \wedge \gamma_{i})\rangle_{0}\langle B(k \wedge \gamma_{i})\rangle_{0}$ ($d = 2$). So $d = 2s$ and $P(-k) = (-1)^{2s}P(k)$.
\item At spacelike $\xi$ the bracket equals $-\tfrac{I_{4}^{d}}{4\pi^{2}}\bigl(1 + \eta c(-1)^{d}\bigr)P(\partial)f(\xi)$, and $P(\partial)f$ is nonzero there for each of the three sums ($-2\xi\gamma_{0}/Q(\xi)^{2}$ for the spinor). Hence, with positive norm ($c > 0$), the field is local exactly when $c = 1$ and $\eta = -(-1)^{2s}$; with an indefinite (Krein) form and $c = -1$ it is local exactly when $\eta = (-1)^{2s}$, so an anticommuting scalar is then local (the Faddeev-Popov ghost case).
\item The tower plane ($Q(v) = Q(w) = 0$, $\{v, w\} = 1$, Fact \claimref{field-theory.imported-tower-limit}) has $\eta = +1$; the palatial pair on polynomials has $\eta = -1$. So, with positive norm, a CAR (tower) lift is local only for the spinor and a CCR (palatial) lift only for the scalar and the photon; with Proposition \claimref{field-theory.no-canonical-commutation-relations-tower}, an elementary local scalar of positive norm, such as a quantised rung field, is palatial.
\end{enumerate}

## technical
Given the massless two-point function, equal at spacelike separation to $-1/(4\pi^{2}Q(\xi))$ and even (standard), Pauli's free-field argument runs on the series' own polarisation sums. The sums of the stored fields have degree $d = 2s$: $1$ for a scalar, $k\gamma_{0} = 2k_{0}\Lambda(k)$ for the spinor, and the photon's bivector sum, a quadratic in $k$ on the null cone. With weights $1$ and $c$ on particle and antiparticle parts and bracket sign $\eta$, the bracket at spacelike $\xi$ is a nonzero multiple of $(1 + \eta c(-1)^{d})P(\partial)(1/Q)$, and $P(\partial)(1/Q) \neq 0$; so in a positive-norm space ($c > 0$) the field is local exactly when $c = 1$ and $\eta = -(-1)^{2s}$.

The tower's CAR has $\eta = +1$ and the palatial CCR $\eta = -1$, so with positive norm the tower carries local spinor fields and the palatial storey local scalar and photon fields, and an elementary local rung scalar of positive norm is palatial. The positive norm is needed: with an indefinite (Krein) form, $c = -1$, the condition becomes $\eta = (-1)^{2s}$ and a CAR scalar is local, as the Faddeev-Popov ghosts of covariant gauge fixing are. For these free fields the result can stand in for the Jost-point import, traded for locality with positive norm; modular covariance is an alternative premise for the same sign.

## lay
Particles that make up matter obey an exclusion rule, while particles of force and the Higgs do not, and which rule a particle obeys is tied to its spin. Here that tie is derived for the series' simplest fields from one requirement, together with the usual rule that quantum states have positive probabilities: measurements at points too far apart for light to connect must not disturb each other. The series stores exclusion-rule modes in one part of its algebra and the other kind in another; the requirement allows half-integer spin only in the first and whole-number spin only in the second, so an elementary Higgs field would have to be built in the second. Without positive probabilities the rule fails, which is why the bookkeeping fields used to fix gauges can break it.

## one-liner
Given the massless two-point function and positive norm ($c > 0$), locality of the series' attached free fields fixes their statistics: the stored polarisation sums have degree $2s$, so the tower's CAR carries only local spinor fields and the palatial CCR only local scalar and photon fields, an elementary rung scalar of positive norm being palatial; with an indefinite form a CAR scalar is local, as ghosts are.
