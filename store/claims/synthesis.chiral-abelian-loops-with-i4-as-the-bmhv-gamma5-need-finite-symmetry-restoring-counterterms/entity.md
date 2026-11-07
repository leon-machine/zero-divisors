---
id: synthesis.chiral-abelian-loops-with-i4-as-the-bmhv-gamma5-need-finite-symmetry-restoring-counterterms
kind: claim
version: 3
title: 'Chiral abelian loops in BMHV need finite symmetry-restoring counterterms'
status: proved
region: synthesis
subject: quantum-fields
tags: [chirality, gauge-fields, recovers-known-physics, pseudoscalar-and-centre]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.field-theory.single-algebra-field
imported_from:
- citation: 'H. Belusca-Maito, A. Ilakovac, M. Madjor-Bozinovic and D. Stoeckinger, Dimensional regularization and Breitenlohner-Maison/''t Hooft-Veltman scheme for gamma_5 applied to chiral YM theories: full one-loop counterterm and RGE structure, J. High Energy Phys. 08 (2020), 024, arXiv:2004.14398.'
  key: BeluscaMaito2020
  doi: 10.1007/JHEP08(2020)024
- citation: 'H. Belusca-Maito, A. Ilakovac, P. Kuehler, M. Madjor-Bozinovic and D. Stoeckinger, Two-loop application of the Breitenlohner-Maison/''t Hooft-Veltman scheme with non-anticommuting gamma_5: full renormalization and symmetry-restoring counterterms in an abelian chiral gauge theory, J. High Energy Phys. 11 (2021), 159, arXiv:2109.11042, equations (6.4) and (6.5).'
  key: BeluscaMaito2021
  doi: 10.1007/JHEP11(2021)159
derivations:
- name: main
  uses:
  - synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four@2
  - synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5@2
  - synthesis.imported-one-loop-integrals-and-pauli-villars-regulators@2
  - synthesis.anomaly-freedom-forces-slot-content@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_projectors_remove_the_evanescent_momentum
- kind: check
  ref: check.py::check_bubble_contraction_is_a_polynomial_in_the_dimension
- kind: check
  ref: check.py::check_four_point_contraction_is_a_polynomial_in_the_dimension
- kind: check
  ref: check.py::check_pole_times_evanescent_factor
- kind: check
  ref: check.py::check_counterterm_coefficients
- kind: check
  ref: check.py::check_one_generation_sums
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'gamma_5 = i I_4 is now the chirality x -> I_4 x I_4 (the left I_4 the BMHV element inside the product, the right one the unit); the Feynman-rule units, the loop prefactors and the values of the master integrals use the field theory''s unit I_4, numbers read in span{1, I_4} and collected outside the product; no bare i remains.'
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s list of routine imports of 2026-11-02: the dimensional-regularisation Fact repinned at @2, whose clause (iv) holds the radial integral and the D-dimensional symmetric integration that were cited from memory, and whose clause (v) holds Belusca-Maito et al. 2021; the citation of that paper''s eq. (6.4) corrected (the paper imposes Tr Y_R^3 = 0, so its eq. (6.4) has no anomaly term; the triangle''s non-removable part in this scheme is the anomaly, proportional to sum Y^3, by the standard argument); the triangle and regulator-free results accepted with it are now named by id in the note and by claimref in the proof (no uses edges). Statement and check unchanged.'
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    The problem's chiral-loop line asks whether the right unit and the evanescent blades give the
    symmetry-restoring counterterms of chiral gauge theories or the series needs a further input. The stored
    unit result showed (argued) that chiral loops inherit them; this computes them for the abelian factor at
    one loop, in the spacetime algebra. The values are standard (Belusca-Maito et al. 2021, eq. (6.5), checked
    against the arXiv text on 2 November 2026; recomputed here, not copied); the content is the route: the
    four-dimensional I4 inside Cl(1, D-1) is the BMHV gamma5, the unit stays outside the product, and the
    projectors delete the evanescent loop momentum, so every breaking term is the evanescent remainder of the
    vector-like contraction, computed exactly as a polynomial in the integer dimension. The continuation in D,
    the D-dimensional symmetric integration l^a l^b -> g^{ab} l^2/D and the Gamma-function master integrals are
    the scheme; the dimensional-regularisation Fact contains the continuation and, from its version 2, the radial
    integral and the D-dimensional symmetric integration (its clause (iv); Peskin and Schroeder, eqs. (A.44) to
    (A.47), give the same in Minkowski form). The one-loop BMHV counterterm structure is standard
    (Belusca-Maito et al. 2020 for chiral Yang-Mills theories; 2021 for the abelian case). Answer to the attack line: no further input beyond the
    scheme; the counterterms are those of the standard scheme. Not covered: the fermion self-energy and vertex
    counterterms (gauge-parameter dependent), the non-abelian factors, and the triangle in this scheme, whose non-removable part is the anomaly, proportional to sum Y^3
    (standard; Belusca-Maito et al. 2021 impose Tr Y_R^3 = 0, so their eq. (6.4) has no such term); the anomaly
    coefficient itself is computed with Pauli-Villars in the triangle result
    (synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation),
    and its independence of the scheme is clause (iii) of the regulator-free extension result
    (synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants).
    The statement that the counterterms never cancel between fields holds in the purely chiral formulation, where
    every field carries the vertex gbar P; a vector-like pair given a D-dimensional vector vertex has no such breaking.
    Transport-absent: Clifford algebra and the unit convention.
---

## formal
In $\Cl(1, D-1)$ (integer $D \geq 4$, signature $(1, D-1)$) call components along $\gamma_{0}, \ldots, \gamma_{3}$ barred and the rest (evanescent) hatted, $k = \bar k + \hat k$. Take the unit of the Feynman rules as the right unit $x \mapsto xI_{4}$, a coefficient outside the product (numbers read in $\mathrm{span}\{1, I_{4}\}$), and the chirality $\gamma_{5}$ as $x \mapsto I_{4}xI_{4}$: on the left $I_{4} = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$ inside the product, the Breitenlohner-Maison-'t Hooft-Veltman element (Theorem \claimref{synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four}(iv); Fact \claimref{synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5}), and on the right the unit; $P_{R,L} = \tfrac12(1 \pm \gamma_{5})$, and the trace $4\langle X\rangle_{0}$. A massless fermion of charge $Y$ couples to an abelian gauge field through the vertex $\bar\gamma^{\mu}P_{R}$ (or $\bar\gamma^{\mu}P_{L}$) with the full propagator numerator $k$; external momenta are four-dimensional. In the purely chiral formulation every field of the content couples this way.
\begin{enumerate}
\item[(i)] (The projectors delete the evanescent momentum.) $\bar\gamma^{\mu}P_{R}k\bar\gamma^{\nu}P_{R} = \bar\gamma^{\mu}\bar k\bar\gamma^{\nu}P_{R}$, the same with $P_{L}$, so around a closed loop of chiral vertices every propagator numerator is replaced by its barred part; $\hat k$ enters only through traces with zero scalar part.
\item[(ii)] (Two-point contraction.) After $\ell^{a}\ell^{b} \to g^{ab}Q(\ell)/D$, the $\ell\ell$ part of the normalised numerator is $-\bar g^{\mu\nu}$ for the chiral loop and $\tfrac{2 - D}{2}\bar g^{\mu\nu}$ for half the vector-like Dirac loop, for $D = 4, \ldots, 8$; the difference is $\tfrac{D-4}{2}\bar g^{\mu\nu}$.
\item[(iii)] (Four-point contraction.) After $\ell^{a}\ell^{b}\ell^{c}\ell^{d} \to S^{abcd}Q(\ell)^{2}/(D(D+2))$, $S^{abcd} = g^{ab}g^{cd} + g^{ac}g^{bd} + g^{ad}g^{bc}$, the $\ell^{4}$ part summed over the six orderings of the photons is $0$ for the chiral loop (its $\gamma_{5}$ part included) and $(D-4)(D-2)S^{\mu\nu\rho\sigma}$ for half the vector-like loop, for $D = 4, \ldots, 7$.
\item[(iv)] (Breaking and counterterms.) Under dimensional regularisation (imported), the chiral loops equal the gauge-invariant half Dirac loops plus the local finite terms
\[
\Pi_{\mathrm{break}}^{\mu\nu} = -\frac{e^{2}Y^{2}}{48\pi^{2}}\,Q(\bar q)\,\bar g^{\mu\nu}, \qquad \Gamma_{\mathrm{break}}^{\mu\nu\rho\sigma} = -\frac{e^{4}Y^{4}}{24\pi^{2}}\,S^{\mu\nu\rho\sigma},
\]
the first not transverse. They are cancelled by the finite counterterms
\[
S_{\mathrm{fct}} = \frac{1}{16\pi^{2}}\int\Bigl[-\frac{e^{2}}{6}\sum Y^{2}\,\bar A_{\mu}\bar\partial^{2}\bar A^{\mu} + \frac{e^{4}}{12}\sum Y^{4}\,(\bar A^{2})^{2}\Bigr],
\]
the sums over the chiral fields, the published values \cite{BeluscaMaito2020, BeluscaMaito2021} recomputed (standard). In the purely chiral formulation both sums are positive, so these counterterms never cancel between fields (a vector-like pair given a $D$-dimensional vector vertex has no such breaking); for the left-handed content of one generation of Theorem \claimref{synthesis.anomaly-freedom-forces-slot-content} ($m = 1$), $\sum Y^{2} = \tfrac{10}{3}$ and $\sum Y^{4} = \tfrac{95}{54}$, while $\sum Y^{3} = 0$.
\end{enumerate}
Clauses (i) to (iii) are exact algebra in the integer-dimensional algebras; (iv) is computed given the scheme and its master integrals (Fact \claimref{synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5}(iv)).

## technical
Dimensional regularisation continues the Clifford algebra to $D$ dimensions; the stored unit result identifies the four-dimensional $I_{4}$ inside $\Cl(1, D-1)$ with the chirality element of the standard consistent scheme, which anticommutes with the four original directions and commutes with the extra ones. With the unit kept outside the product, the chiral projectors at the vertices of a loop delete the evanescent part of every internal momentum. The loop of a chiral abelian field is then the gauge-invariant half of a Dirac loop minus the evanescent remainder of the vector-like contraction, which this result computes exactly as a polynomial in the integer dimension: $(D-4)/2$ for the photon two-point function and $(D-4)(D-2)$ for the four-point function. Multiplied by the poles of the dimensionally continued integrals these give finite local terms that break the Ward identity: a non-transverse photon term $-(e^{2}Y^{2}/(48\pi^{2}))Q(\bar q)\bar g^{\mu\nu}$ and a four-photon contact term. The finite counterterms that restore the symmetry are $\frac{1}{16\pi^{2}}[-\frac{e^{2}}{6}\sum Y^{2}\bar A\cdot\bar\partial^{2}\bar A + \frac{e^{4}}{12}\sum Y^{4}(\bar A^{2})^{2}]$, the published values. These are the standard values. Unlike the anomaly, when every field carries a chiral vertex they never cancel between fields; for one generation of the series' content the sums are $10/3$ and $95/54$.

## lay
Calculations of quantum corrections often pretend that spacetime has a slightly different number of dimensions. In that method the four-dimensional volume element, which elsewhere in the series supplies the imaginary number of quantum theory, plays the role of the standard chirality element, which is not defined beyond four dimensions; the imaginary number itself stays outside the products. This result works out what that costs for particles that feel a force only in one handedness: the calculation breaks the force's symmetry by small, definite amounts, which have to be removed by hand with two correction terms. Their sizes come out equal to the published ones, and when every particle is treated as one-handed they add up rather than cancel over the particles of a generation, unlike the anomaly.

## one-liner
With $I_{4}$ as the BMHV chirality element and the unit outside the product, the projectors delete the evanescent loop momentum, and a massless chiral abelian field breaks the photon Ward identities by $-(e^{2}Y^{2}/(48\pi^{2}))Q(\bar q)\bar g^{\mu\nu}$ and $-(e^{4}Y^{4}/(24\pi^{2}))S^{\mu\nu\rho\sigma}$, cancelled by the standard counterterms $\frac{1}{16\pi^{2}}[-\frac{e^{2}}{6}\sum Y^{2}\bar A\cdot\bar\partial^{2}\bar A + \frac{e^{4}}{12}\sum Y^{4}(\bar A^{2})^{2}]$, recomputed; in the purely chiral formulation they never cancel between fields.
