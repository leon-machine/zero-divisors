---
id: synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation
kind: claim
version: 2
title: 'The triangle anomaly in the spacetime algebra, cancelling per generation'
status: proved
region: synthesis
subject: quantum-fields
tags: [chirality, hypercharge-and-anomalies, recovers-known-physics, pseudoscalar-and-centre]
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
  - synthesis.one-loop-qed-in-the-spacetime-algebra@2
  - synthesis.imported-one-loop-integrals-and-pauli-villars-regulators@1
  - synthesis.anomaly-freedom-forces-slot-content@3
  - synthesis.imported-adler-bell-jackiw-axial-anomaly@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_gamma5_trace_is_the_pseudoscalar_part
- kind: check
  ref: check.py::check_vector_ward_identity_integrand_by_integrand
- kind: check
  ref: check.py::check_two_point_terms_integrate_to_zero_under_the_regulator
- kind: check
  ref: check.py::check_axial_identity_integrand_by_integrand
- kind: check
  ref: check.py::check_regulator_term_gives_one_over_two_pi_squared
- kind: check
  ref: check.py::check_field_form_is_the_pseudoscalar_part_of_f_squared
- kind: check
  ref: check.py::check_chiral_projectors_collapse_to_one
- kind: check
  ref: check.py::check_anomaly_tensor_of_one_generation_vanishes_on_the_whole_gauge_algebra
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four
  - standard-model.imported-anomaly-coefficients
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s list of routine imports of 2026-11-02: a uses edge to the new Fact synthesis.imported-adler-bell-jackiw-axial-anomaly@1 (Adler 1969; Bell and Jackiw 1969), which replaces the citation from memory and against which the magnitude is compared; the regulator-free extension result accepted with it is cited by claimref (no uses edge: scheme independence is a consequence recorded, not a premise). Statement and check unchanged.'
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    The problem's chiral-loop line: the triangle anomaly computed in the series' formalism with a stated
    regulator, and its cancellation per generation from the stored content. The axial anomaly is standard
    (Adler 1969; Bell and Jackiw 1969: Fact synthesis.imported-adler-bell-jackiw-axial-anomaly; Peskin and Schroeder ch. 19, cited from memory), and so is its cancellation per generation; the
    content here is the derivation in the spacetime algebra with the unit outside the product: the trace with
    the chirality element is four times the pseudoscalar coefficient, the regulator term is independent of the
    loop momentum at the integrand level (so no surface term is needed), the coefficient depends on the
    regulators only through sum c_i = 0, and the field form is the bilinear form of the scalar <I4 F^2>_0, the
    pseudoscalar part of the square of the field-strength bivector. The vanishing of the anomaly sums on the
    stored generation is the stored classification (synthesis.anomaly-freedom-forces-slot-content), completed
    here to every component of the symmetric tensor on the gauge algebra; the triangle reads the import
    standard-model.imported-anomaly-coefficients as the loop it comes from. No Krein premise is needed: the
    triangle has no internal gauge line; the regulator fields of negative weight are those of the imported
    Pauli-Villars scheme. Clause (v) on the gauge-algebra tensor is the standard Bose-symmetrisation argument
    (argued). The gravitational statement of (vi) is the trace count tr Y = 0, the imported mixed coefficient, not a
    computed gauge-gravitational triangle. Scheme independence of the coefficient is not proved here; the
    regulator-free extension result
    (synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants,
    its clause (iii)) shows that every covariant extension conserving both vector currents has the same axial
    divergence, which makes this Pauli-Villars value scheme independent. Transport-absent: Clifford algebra and the unit convention; the pseudoscalar reading is
    convenient. Cross-links: cancellation per generation holds for every number of generations, so anomaly
    freedom does not fix the generation count.
---

## formal
Work in $\Cl(1,3)$ with the vectors $\gamma_{\mu}$ as Dirac matrices, the unit of the Feynman rules a coefficient outside the Clifford product (Proposition \claimref{synthesis.one-loop-qed-in-the-spacetime-algebra}(5)), and the chirality element of the matrix reading $\gamma_{5} = iI_{4}$ with $i$ that coefficient, so $\mathrm{Tr}\,X = 4\langle X\rangle_{0}$. Write $S(p) = (p + M)/(Q(p) - M^{2})$. For momenta $k_{1}$, $k_{2}$, $q = k_{1} + k_{2}$ let
\[
D_{1}(\ell) = \mathrm{Tr}[\gamma^{\mu}\gamma_{5}S(\ell)\gamma^{\nu}S(\ell - k_{1})\gamma^{\rho}S(\ell - q)], \quad D_{2}(\ell) = \mathrm{Tr}[\gamma^{\mu}\gamma_{5}S(\ell)\gamma^{\rho}S(\ell - k_{2})\gamma^{\nu}S(\ell - q)],
\]
$P_{1}$, $P_{2}$ the same with $\gamma^{\mu}\gamma_{5}$ replaced by $\gamma_{5}$, and regulate with the Pauli-Villars fields of Fact \claimref{synthesis.imported-one-loop-integrals-and-pauli-villars-regulators}(iii) on the fermion loop, weights $c_{i}$ with $\sum_{i}c_{i} = 0$ ($c_{0} = 1$, $M_{0} = m$), $T^{\mu\nu\rho} = \sum_{i}c_{i}\int\frac{d^{4}\ell}{(2\pi)^{4}}(D_{1} + D_{2})|_{M = M_{i}}$.
\begin{enumerate}
\item[(i)] (Trace.) $\mathrm{Tr}(\gamma_{5}abcd) = 4i\langle I_{4}abcd\rangle_{0} = -4i\lambda$, where $a\wedge b\wedge c\wedge d = \lambda I_{4}$; it is real up to the unit and totally antisymmetric.
\item[(ii)] (Vector Ward identities.) For every $\ell$ and mass, $k_{1\nu}(D_{1} + D_{2})(\ell) = B(\ell - k_{1}) - B(\ell)$ with $B(p) = \mathrm{Tr}[\gamma^{\mu}\gamma_{5}S(p)\gamma^{\rho}S(p - k_{2})]$, and likewise for $k_{2\rho}$. The pseudoscalar part of the numerator of $B$ does not depend on the mass and is odd about the centre of the loop, and $\sum_{i}c_{i}/((Q(\ell) - M_{i}^{2})(Q(\ell - k) - M_{i}^{2})) = O(|\ell|^{-6})$ exactly when $\sum_{i}c_{i} = 0$; so the regulated shift difference integrates to zero and $k_{1\nu}T^{\mu\nu\rho} = k_{2\rho}T^{\mu\nu\rho} = 0$.
\item[(iii)] (Axial divergence.) For every $\ell$, $q_{\mu}(D_{1} + D_{2}) = -2M(P_{1} + P_{2})$ plus four two-point terms of the kind in (ii), which integrate to zero under the regulators. The numerator of $P_{1}$ and of $P_{2}$ over its three denominators is $M \cdot 4i\langle I_{4}\gamma^{\nu}k_{1}\gamma^{\rho}k_{2}\rangle_{0}$, independent of $\ell$. With the imported integral $\int\frac{d^{4}\ell}{(2\pi)^{4}}(\ell^{2} - \Delta)^{-3} = -i/(32\pi^{2}\Delta)$ and $M_{i} \to \infty$ for $i \geq 1$, at $m = 0$
\[
q_{\mu}T^{\mu\nu\rho} = \frac{1}{2\pi^{2}}\langle I_{4}\gamma^{\nu}k_{1}\gamma^{\rho}k_{2}\rangle_{0},
\]
which depends on the regulators only through $\sum_{i \geq 1}c_{i} = -1$. In the index reading the right side is $\pm\tfrac{1}{2\pi^{2}}\epsilon^{\nu\rho\alpha\beta}k_{1\alpha}k_{2\beta}$, the sign fixed by the orientation convention of $\epsilon$.
\item[(iv)] (Field form.) For polarisations $a_{1}$, $a_{2}$, $\langle I_{4}a_{1}k_{1}a_{2}k_{2}\rangle_{0} = \langle I_{4}f_{1}f_{2}\rangle_{0}$ with the plane-wave field-strength bivectors $f_{j} = a_{j} \wedge k_{j}$, symmetric in the two photons; it is the bilinear form of $\langle I_{4}F^{2}\rangle_{0}$, and for $F = E + I_{4}B$ ($E$, $B$ relative vectors) $\langle I_{4}F^{2}\rangle_{0} = -2E\cdot B$.
\item[(v)] (Chiral fields.) With $P_{L,R} = \tfrac12(1 \mp \gamma_{5})$, $\mathrm{Tr}[\gamma^{\mu}P_{L}a\gamma^{\nu}P_{L}b\gamma^{\rho}P_{L}c] = \mathrm{Tr}[\gamma^{\mu}a\gamma^{\nu}b\gamma^{\rho}cP_{R}]$, half the vector trace plus half the $\gamma_{5}$ trace, so a Weyl loop carries half the Dirac axial term with the sign of its chirality. For left-handed Weyl fields in a representation of a gauge algebra the anomalous part of the three-current triangle is proportional to the symmetric tensor $d(X, Y, Z) = \mathrm{tr}(X\{Y, Z\})$. The projector identity is proved; the reduction to $d$ is argued (Bose symmetrisation, standard).
\item[(vi)] (One generation.) For the left-handed content $(1,1)_{0} \oplus (1,\bar 3)_{-2/3} \oplus (2,3)_{1/6} \oplus (2,1)_{-1/2} \oplus (1,1)_{1} \oplus (1,\bar 3)_{1/3}$ of Theorem \claimref{synthesis.anomaly-freedom-forces-slot-content} ($m = 1$), $d$ vanishes on the whole complexified gauge algebra $\mathfrak{sl}(3) \oplus \mathfrak{sl}(2) \oplus \C$ and $\mathrm{tr}\,X = 0$ for every $X$ (for the hypercharge this is $\mathrm{tr}\,Y = 0$, the imported mixed gravitational coefficient: a trace count, not a computed gauge-gravitational triangle); the cancellation is between fields (the quark doublet alone gives $\mathrm{tr}\,Y^{3} = \tfrac{1}{36}$) and holds generation by generation, for any number of generations.
\end{enumerate}

## technical
In the spacetime algebra the Dirac matrices are the vectors, the trace is four times the scalar part, and the chirality element of the matrix reading is $iI_{4}$ with the unit standing outside the product, as the stored one-loop result requires on massive lines. Then the trace of the chirality element with four vectors is four times the pseudoscalar coefficient of their product. For the triangle with one axial and two vector vertices, regulated by Pauli-Villars fermions with weights summing to zero, contracting a vector vertex with its momentum turns the integrand into a difference of two-point terms shifted by that momentum, and since the regulators make those terms fall off fast enough the difference integrates to zero: both vector currents are conserved. Contracting the axial vertex gives the mass term $-2M$ times the pseudoscalar triangle plus terms that integrate to zero. For each regulator the pseudoscalar triangle's numerator is $M$ times a constant, $4i\langle I_{4}\gamma^{\nu}k_{1}\gamma^{\rho}k_{2}\rangle_{0}$, with no loop-momentum dependence, so the regulator term tends to a finite limit as its mass grows: the axial divergence of the massless loop is $(1/(2\pi^{2}))\langle I_{4}\gamma^{\nu}k_{1}\gamma^{\rho}k_{2}\rangle_{0}$, depending on the regulators only through the sum of their weights. Contracted with polarisations this is the bilinear form of $\langle I_{4}F^{2}\rangle_{0} = -2E\cdot B$, the pseudoscalar part of the square of the field bivector. A chiral vertex collapses its projectors to one, so a Weyl loop carries half the Dirac anomaly with its chirality's sign, and a content of Weyl fields is anomalous through the symmetric tensor $\mathrm{tr}(X\{Y, Z\})$ (the standard reduction, argued here); for one stored generation that tensor vanishes on the whole gauge algebra, generation by generation, and the trace $\mathrm{tr}\,Y$ that enters the imported mixed gravitational condition is zero (a trace count, not a computed triangle). These are standard results (Adler; Bell and Jackiw, Fact \claimref{synthesis.imported-adler-bell-jackiw-axial-anomaly}); what is new is their form in the spacetime algebra. Every covariant extension conserving both vector currents gives the same axial divergence (\claimref{synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants}(iii), given the imported existence of such extensions), so the value does not depend on the Pauli-Villars scheme.

## lay
Some symmetries of classical fields fail once quantum effects are included; the classic case is the axial anomaly of a charged particle in an electromagnetic field, found in 1969. This result recomputes that anomaly in the series' own algebra of spacetime, using a standard method of taming the infinities. The anomaly comes out as the part of the squared electromagnetic field that measures how electric and magnetic fields line up, with the textbook strength. For a theory to be consistent, such anomalies must cancel between all the particles that feel a force; the result checks that they cancel within one generation of the series' particles, so the cancellation does not depend on how many generations there are.

## one-liner
Standard (Adler; Bell and Jackiw), re-derived in the spacetime algebra: with imported Pauli-Villars regulators the triangle keeps both vector Ward identities and has axial divergence $(1/(2\pi^{2}))\langle I_{4}\gamma^{\nu}k_{1}\gamma^{\rho}k_{2}\rangle_{0}$ per massless Dirac fermion, the bilinear form of $\langle I_{4}F^{2}\rangle_{0} = -2E\cdot B$, depending on the regulators only through $\sum c_{i} = 0$; for one stored generation the anomaly tensor vanishes on the whole gauge algebra.
