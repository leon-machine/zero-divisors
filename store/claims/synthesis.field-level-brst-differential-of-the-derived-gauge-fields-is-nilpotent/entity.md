---
id: synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent
kind: claim
version: 2
title: 'For the gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$ of the minimal massive composite, realised up to isomorphism by bivectors of $\Cl(9,0)$, the field-level BRST differential of the Lie-algebra-valued vector potential, $sA = \nabla c + g[A, c]$ (the covariant derivative of the ghost) with $sc = -\tfrac{g}{2}[c, c]$, squares to zero on all fields and their derivatives for every coupling, needs the Jacobi identity, the factor $\tfrac12$ and the covariant term, transforms the bivector field strength covariantly, and makes the Yang-Mills density plus an exact gauge-fixing term with the Faddeev-Popov operator invariant'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, recovers-known-physics, rotors-and-stabilisers]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_gauge_algebra_as_bivectors
- kind: check
  ref: check.py::check_brst_differential_is_nilpotent
- kind: check
  ref: check.py::check_nilpotency_needs_jacobi_the_half_and_the_covariant_term
- kind: check
  ref: check.py::check_field_strength_is_covariant
- kind: check
  ref: check.py::check_yang_mills_density_is_invariant_on_the_weak_block
- kind: check
  ref: check.py::check_gauge_fixing_term_is_exact_with_the_faddeev_popov_operator
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, maintainer pass of 2026-11-02: the Gribov result accepted with it is now cited by claimref at the formal level and by id in this note (no uses edge: a statement of scope, not a premise). Statement and check unchanged.'
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Answers the first attack line of the problem (the interacting field-level BRST charge, with the ghost's
    covariant derivative acting on the gauge field) at the level of the differential on local fields. The stored
    result has the free charge at one null momentum and the constraint charge on the matter representation; here
    the differential acts on the full jet algebra of the interacting non-abelian fields, with the gauge algebra
    su(2) + su(3) + u(1) of the minimal massive composite realised, up to isomorphism, by bivectors of Cl(9,0) (the
    weak factor by the rotor generators on e0, e1, e2, as on the stored rotor lattice; colour by the traceless
    bivectors of the e3..e8 block commuting with a complex structure J; the u(1) by J/2). This realisation is
    isomorphic to, not identical with, the stored one on C^2 x C^3, and it does not fix the hypercharge embedding;
    the pure gauge differential sees only the isomorphism class. Standard (Becchi, Rouet,
    Stora; Tyutin; the frame imported in synthesis.imported-brst-kugo-ojima-strocchi-and-gribov), recomputed
    exactly; what is new is the realisation in the series' algebra with the bivector field strength
    F = nabla^A + (g/2)[A^A] and the explicit failure of nilpotency without the Jacobi identity, the factor 1/2
    or the covariant term. The differential has rational coefficients and no imaginary unit, so it commutes with
    i = I4 and needs neither a central unit nor an inner product: positivity of the state space is a separate
    question (the Krein-form premise and the quartet mechanism). Not addressed: the Goldstone and doublet terms of
    the differential (s phi for the two doublets); the operator charge of the interacting theory on a state space
    (which needs renormalisation and the Slavnov-Taylor identities); anomalies; the Gribov ambiguity, which makes the
    construction perturbative (the lattice result
    synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law).
    Transport-absent.
---

## formal
Fields at a point and all their derivatives generate the jet algebra: $A^{a}_{\mu}$ and $B^{a}$ even, the ghosts $c^{a}$ and antighosts $\bar c^{a}$ odd (generators of a Grassmann algebra, the Clifford algebra of a form that vanishes), the coupling $g$ and gauge parameter $\xi$ even constants; $\partial_\mu$ acts by shifting the jet index. The gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$ of the minimal massive composite, Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} has basis $T_a$ with $[T_a, T_b] = f_{ab}{}^{c}T_c$. The vector potential is $A = T_a A^{a}$, $A^{a} = A^{a}_{\mu}\gamma^{\mu}$ a vector field of the spacetime algebra, $\nabla = \gamma^{\mu}\partial_\mu$, and the field strength is the bivector $F^{a} = \nabla\wedge A^{a} + \tfrac{g}{2}f_{bc}{}^{a}A^{b}\wedge A^{c}$. The BRST differential $s$ is the odd derivation, acting from the left and commuting with every $\partial_\mu$, with
\[
sA^{a} = \nabla c^{a} + g f_{bc}{}^{a}A^{b}c^{c}, \qquad sc^{a} = -\tfrac{g}{2}f_{bc}{}^{a}c^{b}c^{c}, \qquad s\bar c^{a} = B^{a}, \qquad sB^{a} = 0 .
\]
\begin{enumerate}
\item[(i)] \emph{(The algebra as bivectors; computed.)} The twelve bivectors $T_{1,2,3} = \tfrac12 e_{12}, \tfrac12 e_{20}, \tfrac12 e_{01}$ on $e_0, e_1, e_2$, the eight traceless bivectors of the $e_3, \dots, e_8$ block commuting with $J = e_{34} + e_{56} + e_{78}$, and $T_{12} = \tfrac12 J$, in $\Cl(9,0)$, close under the commutator into $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$: $58$ nonzero rational structure constants, $J$ spanning the centre, a derived algebra $[\mathfrak{g}, \mathfrak{g}]$ of dimension $11$, a positive-definite ad-invariant form $\kappa_{ab} = -\langle T_aT_b\rangle_0$, and an eight-dimensional block whose adjoint representation has one-dimensional commutant. This realisation is isomorphic to, not identical with, the realisation on $\C^{2} \otimes \C^{3}$ of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}, and it does not fix how the $\mathfrak{u}(1)$ (hypercharge) acts on matter; the pure gauge differential depends only on the isomorphism class.
\item[(ii)] \emph{(Nilpotency; proved.)} For any Lie algebra, $s^2 = 0$ on the whole jet algebra, for every $g$. The check confirms $s^2 = 0$ exactly on all $300$ generators $A^{a}_{\mu}$, $c^{a}$ with at most one derivative for the algebra of (i), as polynomials in $g$.
\item[(iii)] \emph{(What nilpotency needs; computed.)} Replacing $\tfrac{g}{2}$ by $2g$ in $sc$ leaves $s^2c = 0$ but gives $s^2A^{a}_{\mu} = 3(D_\mu Y)^{a}$ with $Y = sc$ the correct ghost variation (in general the residual is $(2h - 1)D_\mu Y$ for $sc = -hg[c, c]$); dropping the term $gf_{bc}{}^{a}A^{b}c^{c}$ gives $s^2A^{a}_{\mu} = \partial_\mu(sc^{a})$, nonzero on the $44$ components of the eleven non-abelian generators; shifting one antisymmetric pair of $\mathfrak{su}(3)$ structure constants (so that the Jacobi identity fails) gives $s^2 \neq 0$ on $30$ of the $60$ underived generators.
\item[(iv)] \emph{(Covariance and invariance; proved.)} $sF^{a} = g f_{bc}{}^{a}F^{b}c^{c}$, so for every ad-invariant $\kappa$ the scalar and pseudoscalar densities $\kappa_{ab}\langle F^{a}F^{b}\rangle_0$ and $\kappa_{ab}\langle F^{a}F^{b}\rangle_4$ are $s$-invariant. The check confirms the first identity for all twelve components, the ad-invariance of $\kappa$ and its failure for a perturbed $\kappa$, and the invariance of both densities on the $\mathfrak{su}(2) \oplus \mathfrak{u}(1)$ block exactly, with a perturbed $\kappa$ breaking the scalar one.
\item[(v)] \emph{(Gauge fixing; proved.)} With $\Psi = \kappa_{ab}\bar c^{a}(\nabla\cdot A^{b} + \tfrac{\xi}{2}B^{b})$,
\[
s\Psi = \kappa_{ab}\big(B^{a}\,\nabla\cdot A^{b} + \tfrac{\xi}{2}B^{a}B^{b} - \bar c^{a}\,\nabla\cdot(Dc)^{b}\big), \qquad (Dc)^{b} = \nabla c^{b} + g f_{cd}{}^{b}A^{c}c^{d},
\]
so $\kappa_{ab}\langle F^{a}F^{b}\rangle_0 + s\Psi$, the Yang-Mills density with a covariant gauge fixing and the Faddeev-Popov operator $\nabla\cdot D$, is $s$-invariant; the check confirms the expansion and $s(s\Psi) = 0$ for the full algebra.
\end{enumerate}
\emph{Reading.} The non-abelian gauge fields of $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$ admit the standard covariant BRST gauge fixing at the level of local fields: the ghost's covariant derivative is forced (iii), and the differential is nilpotent for every coupling. The differential involves no imaginary unit and no inner product, so it is compatible with $i = I_4$ and is independent of the Krein-form premise (KF); that premise and the quartet mechanism concern the state space, not the differential. Standard (Fact \claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}(i)); transport-absent. Not addressed: the Goldstone and doublet terms of the differential, the operator charge of the interacting theory, its renormalisation, anomalies and the Gribov ambiguity, which confines the construction to perturbation theory (Fact \claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}(iv); the lattice computation \claimref{synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law}).

## technical
The problem asks for the interacting BRST charge of the gluons and the W and Z, in which the ghost's covariant derivative acts on the gauge field. At the level of local fields this is a differential on the algebra generated by the fields and their derivatives. Here the gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$ of the minimal massive composite is written, up to isomorphism, by bivectors of $\Cl(9,0)$: the weak factor as half the bivectors on $e_0, e_1, e_2$ (the rotor generators already used on the stored lattice), colour as the eight traceless bivectors of the $e_3, \dots, e_8$ block that commute with a complex structure $J$, and the $\mathfrak{u}(1)$ as $J/2$. This is isomorphic to the stored realisation on $\C^{2} \otimes \C^{3}$, not identical with it, and it does not fix the hypercharge embedding, which the pure gauge differential does not see; with matter or Goldstone fields it would matter. The structure constants are rational and exact, and the commutant test identifies the eight-dimensional block as simple, hence $\mathfrak{su}(3)$.

The vector potential is a Lie-algebra-valued vector field of the spacetime algebra and its field strength is the bivector $F = \nabla\wedge A + \tfrac{g}{2}[A\wedge A]$. The differential acts as a gauge transformation with the ghost as parameter, $sA = Dc$, and on the ghost as $sc = -\tfrac{g}{2}[c, c]$. Squaring to zero on the ghost is the Jacobi identity; on the vector potential it needs, in addition, the factor $\tfrac12$ and the covariant term, and the exact computation shows each failing when altered. Because $s$ commutes with derivatives, nilpotency on the underived fields gives it on every derivative; the check confirms it directly up to first derivatives (300 generators), as a polynomial identity in the coupling.

The field strength transforms covariantly, so both invariant densities, the Yang-Mills scalar $\langle FF\rangle_0$ and the pseudoscalar $\langle FF\rangle_4$, are BRST invariant for any ad-invariant form. A gauge-fixing fermion $\Psi$ adds the exact term $s\Psi$, which contains the covariant gauge condition, the Gaussian weight $\tfrac{\xi}{2}B^2$ and the Faddeev-Popov term $-\bar c\,\nabla\cdot Dc$; invariance of the sum is then nilpotency. All of this is standard BRST, recomputed in the series' algebra; nothing in it comes from transport. The Goldstone and doublet terms of the differential are not included, and the construction is perturbative (Gribov copies, Fact \claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}(iv)). The differential has rational coefficients, so the unit $i = I_4$ never enters, and it needs no inner product; positivity of the physical states is a statement about the state space (the Krein-form premise and the quartet mechanism), which this result does not touch.

## lay
To describe the strong and weak forces as quantum fields in a way that respects relativity, one adds fictitious ghost fields and a bookkeeping operation that must give zero when applied twice. This result writes that operation for the full set of the series' force fields (without the Higgs fields' part), with the force fields' symmetry written as plane elements of a Clifford algebra, and checks exactly that it gives zero twice, for any strength of the force. It also shows that each ingredient is needed: removing the term in which the ghost feels the force field, or changing a factor of one half, spoils it. The usual energy of the force fields and the usual way of fixing the gauge pass the test. Nothing here is new physics; it confirms that the series' algebra carries the standard construction.

## one-liner
With the gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$ of the minimal massive composite realised up to isomorphism by bivectors of $\Cl(9,0)$ ($\mathfrak{su}(2)$ on $e_0, e_1, e_2$, $\mathfrak{su}(3)$ in the $e_3, \dots, e_8$ block commuting with a complex structure $J$, $\mathfrak{u}(1)$ as $J/2$; hypercharge embedding not fixed), the BRST differential $sA = \nabla c + g[A, c]$, $sc = -\tfrac{g}{2}[c, c]$ squares to zero on all fields and derivatives for every $g$, fails without the Jacobi identity, the $\tfrac12$ or the covariant term, transforms $F = \nabla\wedge A + \tfrac{g}{2}[A\wedge A]$ covariantly, and leaves $\langle FF\rangle_0 + s\Psi$ invariant with the Faddeev-Popov operator $\nabla\cdot D$; standard, transport-absent.
