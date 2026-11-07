---
id: synthesis.einstein-condition-is-infinity-vacuum-incidence
kind: claim
version: 4
title: 'The Einstein condition read as infinity-vacuum incidence'
status: proved
region: synthesis
subject: einstein
tags: [tractors, curvature-and-field-equations, pairing-and-bogoliubov, spinor-modules, null-directions]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - interior.imported-tractor-connection@2
  - interior.covariant-form-vacuum-equations@5
  - interior.metric-parallelism-trace-schouten-condition@6
  - one-relation.imported-pure-spinors-incidence-chart@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_classes
- kind: check
  ref: check.py::check_own_ray
- kind: check
  ref: check.py::check_fixed_vacuum
- kind: check
  ref: check.py::check_fock
- kind: check
  ref: check.py::check_real_direction
- kind: check
  ref: check.py::check_matter_and_bianchi
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - pairing.displacement-pairs-point-mode-vacuum-parallel
  - correspondence.one-statement-three-languages
  - one-relation.two-presentations
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: Clause (7) and the proof work with the Ricci, Schouten and stress tensors of the derived metric in components (l-flat tensor l-flat, g^{ab} T_{ab}, nabla^a Ric_ab) and with the complexified tangent and tractor spaces; the GTG field-equation form is stated beside them, and the complexifications T_x M (x) C and T_x (x) C have the units I_5 and I_7 by U3, not yet written in (reader R03).'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: g is the derived metric of a gravitational field on flat spacetime, the tractor connection its Cl(2,4) gauge field, tangent vectors physical vectors; the translation and its seven clauses unchanged. Checks untouched.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: ein.two-readings
  note: >-
    A translation, not a derivation. The standard equivalence used is: a four-metric is Einstein (Ric
    proportional to g) if and only if its Schouten tensor vanishes on null directions, P(l,l) = 0 for every
    null l (the null-null form used in Jacobson's derivation, cited from memory). This entity reads that
    equivalence, and the stored vacuum equations nabla I_g = (0, -P, 0), on the CAR side, through the Fock
    vacua whose annihilator contains the pure-scale tractor I_g (infinity vacua): the own-ray class of an
    infinity vacuum is -P(l,l). Every clause is linear algebra on stored premises plus the contracted Bianchi
    identity; no quantum principle is supplied that would force the classes to vanish, and the matter clause
    takes T as given. What the vacuum language adds as a reading: (a) the condition singling out Einstein
    metrics with arbitrary cosmological constant mentions no constant, which enters as an integration
    constant through the contracted Bianchi identity (as in unimodular gravity and Jacobson's null-null
    route); (b) point vacua obey the same own-ray incidence in every metric, kinematically; (c) one fixed
    infinity-vacuum field left unexcited forces pure null radiation. The classical twistor statement behind
    (5) (the infinity twistor is constant under local twistor transport iff the metric is Einstein) is
    Penrose's, cited from memory. The transport ledger is left to the build.
outside_ga:
  kind: other
  why: 'Clause (7) and the proof work with the Ricci, Schouten and stress tensors of the derived metric in components (l-flat tensor l-flat, g^{ab} T_{ab}, nabla^a Ric_ab) and with the complexified tangent and tractor spaces; the GTG field-equation form is stated beside them, and the complexifications T_x M (x) C and T_x (x) C have the units I_5 and I_7 by U3, not yet written in (reader R03).'
---

## formal
Let $g$ be the derived metric, of signature $(1,3)$, of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), write tractors in its splitting as $(\sigma, \mu_b, \rho)$, the vectors $\sigma\nInf + \mu + \rho\nO$ of $\Cl(2,4)$, with the connection of Fact \claimref{interior.imported-tractor-connection} (on flat spacetime the $\Cl(2,4)$ gauge field $\Omega_{T}$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), and let $I_g = (1, 0, 0)$ be the pure-scale tractor and $X = (0, 0, 1)$ the canonical tractor, so $Q(I_g) = Q(X) = 0$ and $\ip{X}{I_g} = 1$. Call a maximal totally isotropic subspace $W \subset \mathcal{T}_x \otimes \C$ (dimension three) an \emph{infinity vacuum} at $x$ if $I_g \in W$ and a \emph{point vacuum} if $X \in W$; maximal isotropic subspaces come in two families, and by Fact \claimref{one-relation.imported-pure-spinors-incidence-chart} the infinity (respectively point) vacua of the family attached to the conformal spinor space $\CS$ are the Fock vacua $u \in \CS$ with $c(I_g)u = 0$ (respectively $c(X)u = 0$); the other family is attached in the same way to the other half of the Fock module. For a field $W$ of such subspaces and $v \in T_xM$, a physical vector at $x$, the pairing classes of $W$ along $v$ are the values $\omega_v(w, w') := \ip{\nabla_v w}{w'}$ for $w, w' \in W$. The content is a translation of the standard equivalence ``$g$ is Einstein if and only if $\Sch(\ell,\ell) = 0$ for every null $\ell$'' into this language, not a derivation of it. Then:
\begin{enumerate}
\item \emph{(Shape.)} Every infinity vacuum is $W = \mathrm{span}(I_g, \ell, m)$ with $\ell, m$ in the $\mu$ slot spanning a totally null plane $A_W$ of $T_xM \otimes \C$; $A_W$ contains exactly one real null direction $\ell_W$, and every real null direction lies in exactly two infinity vacua. The same holds for point vacua with $X$ in place of $I_g$.
\item \emph{(Classes.)} For $w \in W$, $\omega_v(I_g, w) = -\Sch(v, w)$ for infinity vacua and $\omega_v(X, w) = g(v, w)$ for point vacua; both depend only on $W$ at $x$, not on its extension. For $W$ in the family of $\CS$, its Fock vacuum $u_W$ is annihilated by $c(\nabla_v I_g)$ if and only if $\omega_v(I_g, \cdot) = 0$ on $W$.
\item \emph{(Point vacua, in every metric.)} Every point vacuum has $\omega_{\ell_W}(X, \cdot) = 0$ on $W$: point vacua are unexcited along their own real null direction whatever $g$ is.
\item \emph{(Einstein with a free constant.)} The following are equivalent at $x$: (a) every infinity vacuum has $\omega_{\ell_W}(I_g, \ell_W) = 0$; (b) every infinity vacuum has $\omega_{\ell_W}(I_g, \cdot) = 0$ on $W$; (c) $\Sch = \tfrac{J}{4}\, g$ at $x$, that is $\Ric = \tfrac{R}{4}\, g$. If (c) holds on a connected region, $R$ is constant there (contracted Bianchi identity, Schur's argument in dimension four), and with $\Lambda := R/4$ the classes along a general direction are $\omega_v(I_g, w) = -\tfrac{\Lambda}{6}\, g(v, w)$.
\item \emph{(Ricci-flat.)} Every infinity vacuum has $\omega_v(I_g, \cdot) = 0$ on $W$ for every $v$ if and only if $\Sch = 0$, if and only if $\Ric = 0$, if and only if $\nabla I_g = 0$ (Theorem \claimref{interior.covariant-form-vacuum-equations}).
\item \emph{(One vacuum field: pure radiation.)} For a single infinity vacuum $W$ at $x$, $\omega_v(I_g, \cdot) = 0$ on $W$ for every $v$ if and only if $\Sch = c\, \ell_W^\flat \otimes \ell_W^\flat$ with $c$ real; then $J = 0$ and $\Ric = 2c\, \ell_W^\flat \otimes \ell_W^\flat$.
\item \emph{(Matter.)} For a real symmetric tensor $T$ at $x$ and a constant $G$, $\omega_{\ell_W}(I_g, \ell_W) = 4\pi G\, T(\ell_W, \ell_W)$ for every infinity vacuum if and only if $\Ric + 8\pi G\, T = h\, g$ at $x$ for some number $h$. If this holds on a connected region with $\nabla^a T_{ab} = 0$, then $h - 4\pi G\, g^{ab}T_{ab} =: \Lambda$ is constant there, and $\Ric + 8\pi G\,T = (\Lambda + 4\pi G\,g^{ab}T_{ab})\,g$ is the Einstein equation with source $T$ and cosmological constant $\Lambda$ in the store's curvature convention ($\Ric = \Lambda g$ for de Sitter space in signature $(1,3)$, so that $\Ric$ is minus the Ricci tensor of the convention in which the round sphere has positive Ricci curvature).
\end{enumerate}

## technical
This is a translation, not a derivation: the standard equivalence ``Einstein if and only if the Schouten tensor vanishes on null directions'' is rewritten in the language of Fock vacua. For a gravitational field on flat spacetime with derived metric $g$, the stored vacuum equations say $\nabla_a I_g = (0, -\Sch_{ab}, 0)$ for the tractor gauge field. On the CAR side, the null tractor $I_g$ is a nilpotent mode operator $c(I_g)$ whose kernel on the eight-dimensional Fock module is four-dimensional: it is spanned by the Fock vacua for which the infinity mode is an annihilator, the infinity vacua. Each infinity vacuum is $\mathrm{span}(I_g, \ell, m)$ with $\mathrm{span}(\ell, m)$ a totally null plane of the complexified tangent space, which contains exactly one real null direction (a signature argument), so infinity vacua are labelled by the celestial sphere, two per direction. The pairing classes of $I_g$ against the vacuum are $-\Sch(v, \cdot)$ on $W$, and they are exactly the single-mode excitation amplitudes of the vacuum by $c(\nabla_v I_g)$. The point vacua (those containing the canonical tractor $X$) have classes $g(v, \cdot)$, which vanish along the vacuum's own null direction in every metric: this is the twistor incidence relation, and it is kinematic. Asking the infinity vacua to obey the same incidence, unexcited along their own null generators, is equivalent to $\Sch = (J/4)g$, the Einstein condition with an undetermined constant; the contracted Bianchi identity then makes the constant constant. Asking them to be unexcited in every direction is Ricci-flatness, and the classes of an Einstein metric along a transverse direction are the universal amplitude $-(\Lambda/6)g(v, w)$. One infinity-vacuum field left unexcited in every direction forces $\Ric = 2c\,\ell\otimes\ell$, pure null radiation along its generator. The matter clause is pointwise algebra: equating the own-ray class with $4\pi G\,T(\ell, \ell)$ for every null $\ell$ is $\Ric + 8\pi G T = h g$ in the store's sign convention, which is the null-null content of the Einstein equations; under the null energy condition the own-ray class is non-negative. With a conserved $T$ on a connected region, the trace and the contracted Bianchi identity give $dh = 4\pi G\,d(g^{ab}T_{ab})$, so $h = \Lambda + 4\pi G\,g^{ab}T_{ab}$ with $\Lambda$ an integration constant. All of this is the Einstein condition rewritten in the vacuum language: nothing here supplies a quantum principle that forces the classes to vanish, nor a CAR-side definition of $T$. The exact checks verify the class formulas, the rank-nine own-ray system with kernel spanned by $g$, the one-vacuum kernel spanned by $\ell^\flat\otimes\ell^\flat$, the Fock-module annihilation criterion, the real-direction count on sample planes, and, for the matter clause, the own-ray classes of the store-convention Einstein tensor with a rational source together with the linear algebra of the Bianchi step.

## lay
A known way of stating Einstein's condition on empty space is that the curvature felt along every light ray has no part of a certain kind. This result translates that known statement into the series' language of quantum vacua; it does not derive it. In the series, every point of spacetime carries a small family of quantum vacuum states, and so does the point at infinity that a choice of scale singles out. Each such vacuum is attached to one light-ray direction. The vacua of an ordinary point are never disturbed when you move along their own light ray, in any spacetime: that is pure geometry. This result shows that asking the same of the vacua at infinity, that moving along their own light ray never disturbs them, is exactly Einstein's condition on the curvature, with the cosmological constant left free. Asking that they are never disturbed in any direction gives empty space with no cosmological constant, and asking it of one vacuum only gives a beam of pure radiation. With matter present, the disturbance along each light ray equals the matter's energy flowing along it exactly when Einstein's equations hold, the cosmological constant appearing as a free constant. These are equivalences: the result translates Einstein's condition into the language of vacua and does not explain why nature would impose it.

## one-liner
A translation, not a derivation: the standard equivalence ``Einstein if and only if $\Sch(\ell,\ell) = 0$ for all null $\ell$'' reads, through the Fock vacua annihilated by the pure-scale tractor, as ``every infinity vacuum is unexcited along its own light ray'' ($\Ric = (R/4)g$, $R$ then constant by the contracted Bianchi identity), with ``unexcited in every direction'' giving $\Ric = 0$, one unexcited vacuum giving $\Ric = 2c\,\ell\otimes\ell$, and, for a conserved source $T$, own-ray classes $4\pi G\,T(\ell,\ell)$ giving the Einstein equations with $\Lambda$ an integration constant; point vacua are unexcited along their own rays in every metric.
