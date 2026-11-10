---
id: synthesis.curved-field-vacuum-polarisation-freedom-is-five-local-covariant-constants-of-which-one-is-transverse
kind: claim
version: 1
title: 'Given imported local covariance, curved vacuum-polarisation extensions differ by 5 terms'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, curvature-and-field-equations, recovers-known-physics, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-10-phase3
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase3
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-local-covariance-with-scaling-of-time-ordered-products@1
  - synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products@2
  - synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants@4
  - synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_invariant_local_terms_of_dimension_two_for_two_vector_slots
- kind: check
  ref: check.py::check_divergence_of_the_field_strength_is_laplacian_minus_gradient_divergence_plus_ricci
- kind: check
  ref: check.py::check_ward_identity_leaves_one_constant_times_the_divergence_of_the_field_strength
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
extraction:
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    Works on attack item 3 of op.qft-loops-and-renormalisation (the reduction of the 15 local terms per index pair
    to a constant using the imported local covariance with scaling). It addresses the last sentence of clause (iv)
    of the cited curved-field kernel result, "that the Ward identity on the field then leaves the single constant
    Z_3 is argued and not derived". What the imported Fact supplies, exactly: its clause (iii) turns the
    coefficient functions of the point into constant-coefficient polynomials in the curvature operator, its
    covariant derivatives and the mass, and fixes their dimension at 2 - j. What is derived here from that form:
    the list of terms (five constants) and the effect of transversality on it (one constant, the divergence of
    the field strength). What this does NOT close, so that clause (iv) of the cited result stays argued as a
    whole: (a) the degree of divergence 2 on the field rests on the imported scaling-degree rules and is argued
    there; it is a hypothesis here; (b) the existence of a transverse local covariant extension on a
    gravitational field is not proved (clause (iv) below is argued and names the missing input); (c) the imported
    Fact is cited from memory, is sourced for a scalar field, and its use for the current of the Dirac field is
    the less well sourced part; (d) the kernel of the cited result is the trace form of the parametrix, not a
    state's current two-point function. Not needed for this count, contrary to the cited result's own note: the
    first Hadamard transport equation (it enters only the coefficients at degree four, not the degree of
    divergence). The protraction identity is a hypothesis here as in the cited result; it enters only the count
    of curvature terms (two instead of three). Without it, on symmetric maps, a third invariant appears, and for
    general maps six: both computed. Checked on the web on 10 November 2026 (arXiv abstract pages, through a
    text-extraction tool): Hollands and Wald, arXiv:gr-qc/0103074 (uniqueness of local covariant Wick polynomials
    and time-ordered products up to finitely many parameters, the Minkowski ones plus couplings to curvature;
    existence of the time-ordered products deferred) and arXiv:gr-qc/0111108 (existence; a scaling expansion as
    polynomials in the curvature times Lorentz-invariant distributions), both for a scalar field; J. Zahn,
    The renormalized locally covariant Dirac field, arXiv:1210.4031 (Wick powers and time-ordered products of
    the locally covariant Dirac field in gauge backgrounds, the current conserved, the remaining freedom
    characterised), which is the literature's source for the Dirac case and is not imported in the store. Prior
    art, from memory: that the transverse local term of the photon on a curved background is the divergence of
    the field strength, and that curvature couplings of the photon induced at one loop are finite (Drummond and
    Hathrell 1980), is standard. The five constants are the five quadratic local actions of dimension four in the
    vector field A, namely (D ^ A)^2, (D.A)^2, m^2 A^2, calR A^2 and A.calR(A), and that gauge invariance leaves
    the first is standard power counting; nothing here is new quantum field theory. What is specific here is the
    exact count in the series' algebra and the role of the protraction identity in it. Zahn, arXiv:1311.7661
    (perturbative agreement for the charged Dirac field in a gauge background), read at abstract level only, is the
    other literature source for the missing existence input; whether either paper states the classification for the
    current two-point function on a gravitational, as opposed to gauge, background was not verified. The entity
    status proved covers clauses (i) to (iii) as conditional statements; clause (iv) is argued. Sibling, intended
    citation: the protraction identity derived from vanishing torsion, which is to replace hypothesis (PI).
    Transport-absent.
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a smooth gravitational field on four-dimensional flat spacetime with vanishing torsion (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $D = \hb^{T}(\partial_{a})D_{a}$ its covariant vector derivative, $\mathcal{R}$ its curvature operator, $\mathcal{R}(b) = \partial_{a}\cdot\mathcal{R}(a\wedge b)$ the Ricci vector and $\mathcal{R}_{0} = \partial_{a}\cdot\mathcal{R}(a)$ the scalar. The result is conditional on Fact \claimref{synthesis.imported-local-covariance-with-scaling-of-time-ordered-products}, which is cited from memory; its sources treat the time-ordered products of a scalar field, and its use for the current of the Dirac field is part of the import. It concerns the difference of two extensions and does not show that a transverse one exists. The stored kernel it refers to is the trace form of the parametrix, not a state's current two-point function. Hypothesis (PI), as in Theorem \claimref{synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four}: the protraction identity $\partial_{a}\wedge\mathcal{R}(a\wedge b) = 0$, the first Bianchi identity of a torsion-free field (classical). For a physical vector field $A$ write
\[
K_{1}A = \nabla^{2}A, \qquad K_{2}A = D\,(D\cdot A), \qquad K_{3}A = m^{2}A, \qquad K_{4}A = \mathcal{R}_{0}\,A, \qquad K_{5}A = \mathcal{R}(A),
\]
with $\nabla^{2}A = \sum_{k} Q(\gamma_{k})\bigl[(\gamma_{k}\cdot D)(\gamma_{k}\cdot D)A - ((\gamma_{k}\cdot D)\gamma_{k})\cdot D\,A\bigr]$ the rough Laplacian on an orthonormal physical frame $\{\gamma_{k}\}$. A \emph{local term for two vector slots of degree of divergence $2$} is a kernel $(a, x; b, x') \mapsto a\cdot K_{x}\bigl(b\,\delta(x, x')\bigr)$ with $K$ a differential operator of order at most $2$ on physical vector fields of the form that Fact \claimref{synthesis.imported-local-covariance-with-scaling-of-time-ordered-products}(iii) gives to the difference of two extensions that are local and covariant with almost homogeneous scaling: the coefficient of the derivatives of order $j$ is a polynomial with constant coefficients in $\mathcal{R}$, its covariant derivatives and the mass $m$, of dimension $2 - j$, covariant under the rotation gauge.
\begin{enumerate}
\item[(i)] \emph{(The list; proved given the form of the cited Fact and (PI), the dimensions of the invariant spaces by exact rank. That the coefficients are rotor-invariant tensors of the slots is the proof's reading of ``local and covariant'' in the Fact.)} Every such term is $K = \sum_{i=1}^{5}c_{i}K_{i}$ with real constants $c_{i}$: five constants in place of the $15$ coefficient functions of the point per index pair of clause (iv) of the cited theorem. The count: no Lorentz-invariant tensor has three vector slots, so there is no term $m\,D$; with four vector slots there are four invariants, two symmetric in the derivative pair ($K_{1}$, $K_{2}$ up to lower order) and two antisymmetric, which multiply commutators of covariant derivatives and are curvature terms without derivatives; the invariant bilinear forms in $(a, b)$ that are linear in a map of bivectors number $6$ for all maps, $3$ on symmetric maps, $2$ on maps obeying (PI), namely $a\cdot\mathcal{R}(b)$ and $(a\cdot b)\,\mathcal{R}_{0}$, and $0$ on maps that also have vanishing Ricci vector. So the Weyl part of the curvature operator cannot occur in the difference of two extensions, and no parity-odd term occurs although invariance is imposed for the connected group only.
\item[(ii)] \emph{(Transversality; proved.)} On every torsion-free field, $D\wedge D\chi = 0$ for scalar fields $\chi$ and
\[
D\cdot(D\wedge A) = \nabla^{2}A - D\,(D\cdot A) + \mathcal{R}(A)
\]
in the store's sign of the curvature operator. The condition $K(D\chi) = 0$ for every scalar $\chi$, on every torsion-free field and for every mass, holds exactly when $(c_{1}, c_{2}, c_{3}, c_{4}, c_{5}) = c\,(1, -1, 0, 0, 1)$, that is
\[
K A = c\;D\cdot(D\wedge A),
\]
the divergence of the field strength of $A$. On the flat field this is $c\,(\nabla^{2}A - \nabla(\nabla\cdot A))$, the transverse term $c\,T(\delta)$ of clause (iii) of Theorem \claimref{synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants} up to the sign convention of $T$: the constant $Z_{3}$. A photon mass term ($c_{3}$) and the terms $c_{4}$, $c_{5}$ do not occur in the difference of two transverse extensions; the Ricci term occurs only inside $D\cdot(D\wedge A)$, the Maxwell operator of the field, where it is the minimal coupling. Nothing is said here about the finite dependence of the kernel itself on the curvature.
\item[(iii)] \emph{(What this gives for the stored clause; proved given the two imported Facts and the hypothesis that the degree of divergence is $2$.)} Assume, as argued in clause (iv) of the cited curved-field theorem from Fact \claimref{synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products}(ii) and (vi), that the time-ordered one-loop vacuum-polarisation kernel on the field has degree of divergence $2$. If transverse local covariant extensions exist, then any two extensions of it that are local and covariant with almost homogeneous scaling and transverse in one slot differ by $c\,a\cdot D\cdot(D\wedge(b\,\delta))$ with one real constant $c$, the same on every torsion-free field: the freedom is the flat $Z_{3}$, and the coefficient of the Ricci term relative to the Laplacian is fixed.
\item[(iv)] \emph{(Existence of a transverse extension; argued, not proved.)} Suppose in addition that the failure of transversality of a local covariant extension, the map $\chi \mapsto \bar\Pi(D\chi)$, is itself a local term of the form of the cited Fact with dimension $3$, and that the kernel is symmetric under exchange of its two slots; neither is part of the stored Facts. The candidates are $D(D\cdot D\chi)$, $m^{2}D\chi$, $\mathcal{R}_{0}D\chi$, $\mathcal{R}(D\chi)$ and $(D\mathcal{R}_{0})\chi$. The first four are $K_{2}$ to $K_{5}$ applied to $D\chi$ and are removed by subtracting local terms of (i); the fifth gives a double divergence $\int\chi\,(D\mathcal{R}_{0})\cdot D\psi$ that is not symmetric in $(\chi, \psi)$ and is excluded by the symmetry. Under these two suppositions a transverse local covariant extension exists. What is missing in the store is a statement that the divergence of a local covariant time-ordered product of currents is of this local form (the literature's Ward identity or principle of perturbative agreement on a gravitational field; Zahn, arXiv:1210.4031 and arXiv:1311.7661, for the charged Dirac field in gauge backgrounds, read at the level of the abstracts only). Clause (iv) of the cited curved-field theorem therefore stays argued.
\end{enumerate}

## technical
The stored curved-field result found that, at each point, the vacuum polarisation on a gravitational field has the same fifteen undetermined local terms per pair of indices as on flat spacetime, but with coefficients that could vary from point to point, and it cited the imported local-covariance Fact for their reduction to constants without carrying the reduction out. This result carries it out, conditionally. The Fact is cited from memory and its sources prove it for a scalar field; its use for the electron's current is part of the import. The Fact says each coefficient is a constant-coefficient polynomial in the curvature operator, its derivatives and the mass, of a fixed dimension, and the construction is covariant under local rotations; so each coefficient is a Lorentz-invariant tensor, and the invariant tensors can be counted exactly as the common kernel of the Lorentz generators acting through the algebra. With two derivatives there are two terms, the rough Laplacian and the gradient of the divergence; with one derivative none, because no invariant has three vector slots; with no derivative the mass squared, and two terms linear in the curvature, the Ricci map and the scalar curvature, the Weyl part admitting no invariant. The count of curvature terms uses the protraction identity: on symmetric maps without it there is a third invariant. That is five constants. Requiring that two extensions both obey the Ward identity makes their difference annihilate gradients. For a torsion-free field the curl of a gradient vanishes and the divergence of the field strength equals the Laplacian minus the gradient of the divergence plus the Ricci map, in the store's sign; an exact computation on a sample field shows the four other directions fail independently, so the transverse terms are the multiples of the divergence of the field strength. Given the imported Facts and the flat degree of divergence, if transverse local covariant extensions exist, two of them differ by the one constant of flat spacetime, which multiplies the Maxwell operator of the field; its Ricci term is the minimal coupling, and no independent coupling to curvature is free. Whether a transverse local covariant extension exists on a gravitational field is not proved here; it is argued under two further suppositions that the store does not hold, so the argued clause of the stored curved-field result stays argued.

## lay
The effect by which a photon briefly becomes an electron and positron pair has an infinite part that a rule must fix, and the rule leaves some quantities free. On flat spacetime the free quantities reduce to one number, which is absorbed into the measured electric charge. On a gravitational field the collection had shown only that the free quantities are of the same kind at each point, and had relied on a theorem from the literature, taken as an imported fact and quoted from memory, to say they are the same everywhere. This result works out what that theorem leaves, given that imported theorem and assuming gravity without the twisting that spinning matter would source. The answer is five numbers: two that already exist on flat spacetime, a possible photon mass, and two couplings of the photon to curvature. Demanding that electric charge be conserved, for both of two competing rules, removes four of them. If two charge-conserving rules exist, they differ only by the single number of flat spacetime; that number multiplies the ordinary wave operator of light on the gravitational field, and no separate coupling of light to curvature is left free. The theorem relied on was proved for a simpler kind of field than the electron's. The tidal part of gravity, the only part present in empty space, cannot appear among the free quantities at all. The result does not show that a charge-conserving rule exists on a gravitational field; that is argued under extra assumptions and is known in the literature, not derived here, so the open point in the collection's earlier result stays open.

## one-liner
Given the imported local-covariance Fact (imported, cited from memory, sourced for scalar fields), the protraction identity and degree of divergence $2$, on a torsion-free gravitational field two local covariant extensions of the one-loop vacuum polarisation differ by $c_{1}\nabla^{2} + c_{2}D(D\cdot) + c_{3}m^{2} + c_{4}\mathcal{R}_{0} + c_{5}\mathcal{R}(\cdot)$ (five constants, no Weyl term), and if both are transverse by $c\,D\cdot(D\wedge A) = c\,(\nabla^{2}A - D(D\cdot A) + \mathcal{R}(A))$, the flat constant $Z_{3}$ (proved given those inputs); whether a transverse local covariant extension exists is argued only, so the stored clause stays argued.
