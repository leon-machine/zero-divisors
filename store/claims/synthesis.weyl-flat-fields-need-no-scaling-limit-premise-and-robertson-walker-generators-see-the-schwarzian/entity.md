---
id: synthesis.weyl-flat-fields-need-no-scaling-limit-premise-and-robertson-walker-generators-see-the-schwarzian
kind: claim
version: 4
title: 'On a globally hyperbolic Weyl-flat region of a gravitational field every quasi-free Hadamard state of the massless Dirac field has the flat massless vacuum as its scaling limit and, with the comoving transverse labels, the generator microlocal condition in the physical affine parameter, so the local form of (N$_{+}$), at the leading order at which local Rindler horizons are defined, holds there for the massless field without the scaling-limit premise; on a Robertson-Walker field the conformal vacuum differs on every null generator from the null vacuum of the physical affine parameter by the Schwarzian kernel of $S = 2a''''/a - 4(a''/a)^{2}$ (conformal time), which vanishes identically exactly on de Sitter and flat fields'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, car-algebra, null-directions, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-deposit-state
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.hawking.continuum-mode-space
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes@3
  - synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state@4
  - synthesis.local-normality-at-the-edge-gives-the-null-ground-state@2
  - synthesis.positive-null-energy-gives-r-premises@4
  - field-theory.second-quantisation@5
  - synthesis.imported-gtg-dictionary@1
  - synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_conformal_null_geodesics_keep_their_covectors
- kind: check
  ref: check.py::check_schwarzian_of_the_physical_affine_parameter
- kind: check
  ref: check.py::check_schwarzian_vanishes_exactly_on_de_sitter_and_flat
- kind: check
  ref: check.py::check_pulled_back_vacuum_differs_by_the_schwarzian_kernel
- kind: check
  ref: check.py::check_conformal_factor_scales_to_local_inertial_coordinates
- kind: check
  ref: check.py::check_leading_term_in_the_physical_parameter
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.hadamard-scaling-limit-premise
  - synthesis.attachment-transport-is-flat-only-where-weyl-vanishes
  - synthesis.de-sitter-horizon-translation-is-conformal-null-rotation
extraction:
  open_problem: op.deposit-state-is-hadamard
  note: >-
    Step (3) of op.deposit-state-is-hadamard on the Weyl-flat part of the chain. Clause (i) is the
    standard scaling-limit property of Hadamard states of free fields together with the standard
    conformal covariance of the massless Dirac field; this entity is where the store proves the
    conformal-covariance lemma (null geodesics and their covectors, wave-front sets) used by the
    deposit result(synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite). The new content is (ii) and (iii). The adopted premise (HS),
    synthesis.hadamard-scaling-limit-premise, asserts the vacuum-like scaling limit of Hadamard states at
    points of nonzero field strength. On a Weyl-flat field (nonzero Ricci part allowed, as on the
    descended Robertson-Walker field) it is a theorem for the massless Dirac field: conformal covariance
    carries the stored flat-field restriction result over, and on a generator, once the comoving
    transverse labels are fixed as the multiplicity space, the CAR gives weight one half in the physical
    affine parameter, so the only change is a smooth Schwarzian kernel. So, for the massless Dirac field
    and at the leading order at which (HS) defines local Rindler horizons, (HS) is needed only where the
    Weyl curvature is nonzero; for massive fields it stays a premise on Weyl-flat fields too. That is the
    region where the attachment's transport supplies no state (synthesis.attachment-transport-is-flat-only-where-weyl-vanishes): the two results
    bound the same region from both sides. With a Hadamard deposit on the descent slice (the thermal
    deposit over the conformal vacuum is one) the local form of (N+) holds at every point of every local
    Rindler horizon of the Weyl-flat descent region (a descent of radiation type, a stated hypothesis) with
    no premise beyond the deposit. The ground-state
    clause is a different matter: on a Robertson-Walker field the conformal vacuum is the ground state of
    the physical affine translations on a null generator exactly when 1/a is linear in conformal time
    (de Sitter, or flat), which makes exact on every generator the de Sitter statement of
    synthesis.de-sitter-horizon-translation-is-conformal-null-rotation, and fails on a radiation- or
    matter-dominated field (S = -4/t^2, -12/t^2). Transport-absent (standard conformal covariance and
    Schwarzian calculus, re-derived); its use is to bound where (HS) is needed. Local conformal flatness
    of four-dimensional fields with vanishing Weyl tensor and conformal covariance of the massless Dirac
    field with weight 3/2 are the imported Fact synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness.
    Literature cited from memory: the Schwarzian and
    Moebius invariance of the weight-1/2 vacuum kernel (standard, as in the stored collapse result);
    the inversion rule for the Schwarzian, S of the inverse map = -S/(Psi')^2 (standard, computed here).
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01 (deposit-state imports): a uses edge to the imported Fact on conformal covariance and local conformal flatness replaces the citations from memory in the set-up of the proof and in the note; the pin to the microlocal Fact moves to its version 2 (the scalar smooth-difference statement, not used here). Statement, proof steps and checks otherwise unchanged.'
  maintainer_pass_hs_scaling:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 2 -> 3, at Leon''s decisions of 2 November 2026: a marked note in the formal and technical levels records that clause (i) is subsumed by synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field (the bulk scaling limit at every point of every globally hyperbolic field, any mass), that (ii) and (iii) stand, and that the premise (HS) has been restated (version 3). Statement, proof and checks unchanged; no edge added.'
  flags:
  - 'massless Dirac field only: for a massive field the conformal map does not apply; the Weyl-flat massive case is covered by the scaling-limit theorem (HS), version 4, not by this result'
  - 'local conformal chart: the Weyl-flat region is written as hb(b) = b/phi(x) in a gauge; global conformal flatness is not assumed'
  - 'transverse labels: the generator continuum mode space uses the conformal chart''s comoving transverse labels; the physical area element a^2 d^2y changes along an expanding generator, and weight one half in the physical affine parameter follows from the CAR once the comoving labels are chosen'
  - 'local Rindler horizons: the chart''s null planes through a point agree with the local Rindler horizons there (expansion-free at the point) at the leading order, tangent at the point, at which (HS) and (C_loc) define them, not beyond it'
  - 'globally hyperbolic region U assumed (or a globally hyperbolic neighbourhood of each point), so that the Hadamard Facts apply on it'
  maintainer_pass_hs_bound:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 3 -> 4, at Leon''s decisions of 2 November 2026 (Hadamard scaling bound): (HS), synthesis.hadamard-scaling-limit-premise, is now a theorem (version 4); a marked sentence (formal, technical) and a flag record that the Weyl-curved and massive cases are covered by that theorem; the results here stand as a separate route on Weyl-flat regions. What this entity asserts is unchanged.'
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose Weyl curvature vanishes on an open region $U$, globally hyperbolic for the derived metric, written on $U$ in a gauge where $\hb(b) = b/\varphi(x)$ with $\varphi$ smooth and positive (derived metric $\varphi^{2}$ times the flat one, Fact \claimref{synthesis.imported-gtg-dictionary}), and let $\psi$ be the massless Dirac field (Proposition \claimref{field-theory.second-quantisation}). Hadamard is as in Fact \claimref{synthesis.imported-microlocal-hadamard-condition}; generators, the continuum mode space with the chart's comoving transverse labels $K = L^{2}(\R^{2}, d^{2}y)\otimes V_{\Lambda}$, the null vacuum and the generator microlocal condition are as in Theorems \claimref{synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes} and \claimref{synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state}.
\begin{enumerate}
\item[(i)] \emph{(Conformal transfer and bulk scaling limit; standard, re-derived.)} The flat null lines with $d\tilde\lambda = \varphi^{2}d\lambda$ are the affine null geodesics of the derived metric and carry the flat covectors, so a state of $\psi = \varphi^{-3/2}\chi$ is Hadamard exactly when the corresponding state of the flat field $\chi$ is. For every gauge-invariant quasi-free Hadamard state $\omega$ and every $x_{0} \in U$, the scaling limit of $\omega$ at $x_{0}$ (weight $\tfrac32$ per leg) is the flat massless vacuum in the local inertial coordinates $\varphi(x_{0})(x - x_{0})$.
\item[(ii)] \emph{(Generators; proved.)} On every null generator in $U$ the physical affine parameter $\tilde\lambda$ satisfies $d\tilde\lambda = \varphi^{2}d\lambda$, $\lambda$ the flat one. With the comoving transverse labels fixed as the multiplicity space (the physical area element $\varphi^{2}d^{2}y$ changes along an expanding generator), the CAR makes the generator field carry weight $\tfrac12$ in $\tilde\lambda$, and the restriction of $\omega$ satisfies the generator microlocal condition in $\tilde\lambda$. Hence the local form of (N$_{+}$) holds at every point of every null plane of the chart in $U$, for every such state, with no further premise. The chart's null planes through $x_{0}$ agree with the local Rindler horizons at $x_{0}$ (expansion-free there) at the leading order, tangent at $x_{0}$, at which the scaling-limit premise (HS) and (C$_{\mathrm{loc}}$) define them; at that order the conclusion of (HS) is, on Weyl-flat regions, a theorem for the massless Dirac field.
\item[(iii)] \emph{(Robertson-Walker generators; proved and computed.)} For $\varphi = a(t)$, $t = x\cdot e_{0}$, the restriction of the conformal vacuum to a null generator, read in $\tilde\lambda = \Psi(\lambda)$ with $\Psi' = a^{2}$, is the null vacuum of $\tilde\lambda$ plus the Schwarzian kernel of $\Phi = \Psi^{-1}$, whose leading term is $\tfrac{i}{2\pi}\cdot\tfrac{1}{12}S_{\Phi}\,(u - v)$ with $S_{\Phi} = -S/a^{4}$, where
\[
S = S_{\Psi} = \frac{\Psi'''}{\Psi'} - \frac32\Bigl(\frac{\Psi''}{\Psi'}\Bigr)^{2} = \frac{2a''}{a} - 4\Bigl(\frac{a'}{a}\Bigr)^{2} = -2a\Bigl(\frac1a\Bigr)'' ,
\]
derivatives in conformal time, $a$ at the point. $S$ vanishes on an interval exactly when $1/a$ is linear in $t$ there: de Sitter ($a = -1/(Ht)$) or the flat field. For $a = t^{n}$, $S = -2n(n + 1)/t^{2}$: radiation $-4/t^{2}$, matter $-12/t^{2}$. So the conformal vacuum is the ground state of the physical affine translations on every null generator exactly on de Sitter and flat fields (the ground-state clause of Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(i) in $\tilde\lambda$); on a radiation- or matter-dominated field it satisfies only the local form.
\end{enumerate}
\emph{Note (2 November).} Clause (i) is subsumed by Theorem \claimref{synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field}: every gauge-invariant quasi-free Hadamard state of the Dirac field, of every mass, has the flat massless vacuum as its scaling limit at every point of every globally hyperbolic gravitational field, whatever the Weyl curvature (standard, Sahlmann and Verch, re-derived). The conformal-covariance part of (i), which (ii) and the deposit result use, and clauses (ii) and (iii) stand: the generator statement (ii) is not given by that theorem. The premise (HS), \claimref{synthesis.hadamard-scaling-limit-premise}, has since been restated (version 3) as a statement about the Hadamard parametrix restricted to horizon generators; "the conclusion of (HS)" in (ii) is the scaling limit on the generators, the clause (b) of its version 2. The statements above are unchanged. \emph{(Added 2 November, later.)} (HS) is now a theorem (version 4 of \claimref{synthesis.hadamard-scaling-limit-premise}): its conclusion holds at every point of every local Rindler horizon, for every mass and whatever the Weyl curvature; this result stands as a separate route on Weyl-flat regions and does not use it.

## technical
The adopted scaling-limit premise (HS) says that at a point of a gravitational field with nonzero field strength a Hadamard state of the Dirac field looks, at short distances, like the flat field's massless vacuum, also on the null generators through the point. This result proves that statement for the massless Dirac field wherever the Weyl part of the field strength vanishes, on a globally hyperbolic region, including the Robertson-Walker fields of cosmology.

There the field is conformally flat and the massless Dirac field is conformally covariant, so a Hadamard state is carried to a flat-field Hadamard state, whose scaling limit is the vacuum (standard). On a null generator the physical affine parameter differs from the flat one by the factor $a^{2}$; with the comoving transverse labels as multiplicity space, the canonical anticommutator makes the generator field transform with weight one half, so the vacuum kernel changes only by a smooth Schwarzian term and the generator condition, hence the local form of (N$_{+}$), holds, at the leading order at which local Rindler horizons are defined. So, for the massless Dirac field, (HS) was needed only where the Weyl curvature is nonzero, and for massive fields everywhere. (HS) has since been proved in general, Weyl-curved and massive cases included; this result is a separate route on Weyl-flat regions.

Since 2 November the bulk scaling limit holds at every point of every globally hyperbolic gravitational field, for every mass, by a separate theorem, so the first part of this result is subsumed; the generator statement and the Robertson-Walker computation stand.

On a Robertson-Walker field the Schwarzian is $2a''/a - 4(a'/a)^{2}$ in conformal time, and the remainder in the physical affine parameter has leading coefficient $-S/a^{4}$ over twelve. It vanishes exactly for de Sitter and flat fields, where the conformal vacuum is the ground state for the physical affine translations on every null generator; on radiation- or matter-dominated fields it is not, and only the local form holds. Transport-absent.

## lay
The series assumes that, very close up, the quantum field always looks like empty flat space, even where gravity is present. This result proves that assumption, for massless spin-one-half particles, wherever space-time is a rescaled copy of flat space, which includes the uniform expanding universe of cosmology. So, for those particles, the assumption is only needed where gravity distorts shapes, as near a black hole; for particles with mass it is still an assumption. It also finds that the universe's natural empty state counts as the lowest-energy state along light rays only if the expansion is of the accelerating de Sitter kind, not during the radiation era.

## one-liner
On a globally hyperbolic Weyl-flat region every quasi-free Hadamard state of the massless Dirac field has the flat massless vacuum as its scaling limit and, with comoving transverse labels, the generator microlocal condition in the physical affine parameter, so for the massless field the local form of (N$_{+}$) (at the leading order defining local Rindler horizons) needs no scaling-limit premise there; on a Robertson-Walker field the conformal vacuum differs on null generators from the physical null vacuum by a Schwarzian kernel with $S = 2a''/a - 4(a'/a)^{2}$ (leading coefficient $-S/12a^{4}$ in the physical parameter), zero exactly on de Sitter and flat fields (radiation $-4/t^{2}$).
