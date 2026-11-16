---
id: synthesis.colour-angle-fixed-by-no-stored-conjugation-and-relaxed-by-no-stored-field
kind: claim
version: 1
title: 'The colour angle: fixed by no stored conjugation, relaxed by no stored field'
status: proved
region: synthesis
subject: standard-model
tags: [gauge-fields, hypercharge-and-anomalies, undetermined-input, no-go]
proposed_by:
  kind: ai
  session: 2026-11-16-anomaly
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-16-anomaly
review: draft
derivations:
- name: main
  uses:
  - synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation@4
  - synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation@5
  - dark-matter.mirror-tower-copy-one@11
  - synthesis.imported-chern-weil-and-chern-simons-forms@1
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix@4
  - synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them@1
  - synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element@1
  - standard-model.invariant-pairing-five-modes@5
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@6
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@5
  - synthesis.rung-field-on-the-lift-locus@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_four_form_of_a_field_square_in_the_spacetime_algebra
- kind: check
  ref: check.py::check_stored_conjugation_fixes_even_elements_and_reflections_reverse_the_six_form
- kind: check
  ref: check.py::check_signature_reversal_carries_the_four_form_with_its_sign
- kind: check
  ref: check.py::check_colour_form_is_invariant_under_automorphisms
- kind: check
  ref: check.py::check_invertible_pair_admits_no_phase_symmetry_with_a_colour_coefficient
- kind: check
  ref: check.py::check_counter_models_with_a_colour_coefficient_have_monomial_determinant
- kind: check
  ref: check.py::check_conjugate_coupling_removes_the_fourth_charge_and_keeps_a_quarter_turn_of_the_unit
- kind: check
  ref: check.py::check_axial_phase_is_a_symmetry_of_the_stored_potential_and_unbroken_on_the_cone
- kind: check
  ref: check.py::check_determinant_phase_of_the_normal_pair_and_mass_product_of_a_monomial
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.premise-cpt-covariance
  - dark-matter.premise-flag-as-datum
  - synthesis.common-ceiling-coupling-premise
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase
extraction:
  open_problem: op.strong-cp
  note: >-
    Filed against the first and third attack items of the strong CP problem (the angle term under the flag
    reversal, the stored CPT conjugation and the reversal to the mirror; a stored field with a shift symmetry),
    and against the last attack item of op.matter-asymmetry-origin (the relaxing angle). The outcome is
    negative on both: no stored premise moves the term, and no stored coupling has a phase symmetry with a
    colour coefficient. The algebra is standard and transport-absent: that the conjugation of charge, parity
    and time together fixes the angle term, and that a two-doublet model in which both doublets couple to
    both quark types has no Peccei-Quinn symmetry, are textbook. What is new for the store is that the stored
    conjugation, which is not the CPT operator of quantum field theory, is shown to fix the term in its own
    convention; that the absence of the symmetry is proved for the stored covariant coupling with family
    matrices, with the exact condition (both family matrices invertible) and the counter-models when it
    fails; and that the stored fourth Dirac charge is identified as the unit of the module, cut down by the
    conjugate coupling to the order-four pseudoscalar of the ten Majoranas. Literature used and not stored as
    Facts, each cited from memory unless marked checked: the physical angle is the bare angle plus the phase
    of the determinant of the quark mass matrices, and a phase rotation with colour coefficient shifts the
    angle ('t Hooft 1976; Fujikawa 1979); the neutron dipole measurement (Abel et al. 2020, Phys. Rev. Lett.
    124, 081803, checked at source: (0.0 +- 1.1 +- 0.2) x 10^-26 e cm) and its conversion (Dragos et al.
    2021, Phys. Rev. C 103, 015202, checked at source: d_n = -0.00152(71) theta e fm, |theta| < 1.98 x 10^-10
    at 90 percent; Bhattacharya et al. 2021, Phys. Rev. D 103, 114507, checked: no reliable lattice value
    yet, |d_n| below about 0.01 theta e fm); the topological susceptibility of the colour vacuum, near
    (75 MeV)^4; the exclusion of an axion with decay constant at the weak scale (Review of Particle Physics,
    Axions and other similar particles, 2021 revision, checked: the standard and variant axions were
    quickly excluded, limits in the Listings; the measurements, from memory, are the kaon decay to a pion and
    an unseen particle, radiative quarkonium decays and beam dumps). Not done: the phase of the determinant
    on the stored family structures; any loop correction; a completeness proof for the list of stored fields.
---

## formal
Work in the spacetime algebra $\Cl(1,3)$ with vectors $\gamma_{\mu}$ and unit pseudoscalar $I_{4}$; numbers are read in $\mathrm{span}\{1, I_{4}\}$ and $\bar{z}$ is $I_{4} \mapsto -I_{4}$. Let the colour field strength be $F = \sum_{a}F^{a}T_{a}$, with $F^{a}$ bivector fields and $T_{a}$ a basis of $\su(3)$, let $\kappa_{ab} = \tr(T_{a}T_{b})$ be the trace form, and put
\[
\Theta(F) = \sum_{a,b}\kappa_{ab}\,\langle F^{a}F^{b}\rangle_{4} ,
\]
the grade-four part of the colour field square: the characteristic four-form of Fact \claimref{synthesis.imported-chern-weil-and-chern-simons-forms} for the trace form, read in the algebra. The \emph{angle term} is $\theta$ times the coefficient of $I_{4}$ in $\Theta(F)$; its normalisation is not used.

For $n$ families let $\Phi_{1} = \alpha$ and $\Phi_{2} = \bar\beta$ be the two doublets of the complexified rung field $c = \alpha\cdot v + \beta\cdot w$ of Theorem \claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}; they transform alike under the slot $U(2)$, and the maps of the rung summand that commute with the gauge group and keep $\mathsf{N}(c)$ are $\Phi \mapsto g\Phi$, $g \in U(2)$. The covariant coupling of that Theorem is, on the neutral components,
\[
M_{u} = \Phi_{1}Y + \Phi_{2}\tilde{Y}, \qquad M_{d} = \bar\Phi_{2}Y + \bar\Phi_{1}\tilde{Y},
\]
with $n \times n$ family matrices $Y$, $\tilde{Y}$. A \emph{phase symmetry} is a one-parameter group acting on the quark doublets, the up-type and the down-type singlets by unitary family rotations with generators $K_{Q}$, $K_{u}$, $K_{d}$, and on $\Phi$ by $e^{tK_{\Phi}}$, all anti-Hermitian, such that $K_{Q}^{\mathsf T}M_{u} + M_{u}K_{u} + \delta M_{u} = 0$ and $K_{Q}^{\mathsf T}M_{d} + M_{d}K_{d} + \delta M_{d} = 0$ for every $\Phi$, where $\delta$ is the derivative along $K_{\Phi}$. Its \emph{colour coefficient} is the real number $a_{3} = I_{4}^{-1}(2\tr K_{Q} + \tr K_{u} + \tr K_{d})$; for one family and diagonal generators $2a_{3}$ is the coefficient $A_{3}$ of Theorem \claimref{synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them}(v). Write $I_{4}q_{1}$, $I_{4}q_{2}$ for the diagonal entries of $K_{\Phi}$ and $p(a, b) = \det(aY + b\tilde{Y})$.
\begin{enumerate}
\item[(i)] \emph{(The term.)} $\tfrac12\langle F^{a}F^{b} + F^{b}F^{a}\rangle_{4} = F^{a}\wedge F^{b}$, and for $F = E + I_{4}B$ with $E = \sum_{i}E_{i}\gamma_{i}\gamma_{0}$, $B = \sum_{i}B_{i}\gamma_{i}\gamma_{0}$, $\langle F^{2}\rangle_{4} = 2\bigl(\sum_{i}E_{i}B_{i}\bigr)I_{4}$, the pseudoscalar part of the field square of Theorem \claimref{synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation}(iv). Reversal and the grade involution fix $\Theta(F)$. If $g$ is a linear isometry of the vectors acting on bivectors by its outermorphism, $\Theta(gF) = \det(g)\,\Theta(F)$.
\item[(ii)] \emph{(The stored conjugation fixes it.)} The conjugation $C = \mathrm{Ad}(I_{6})\circ\kappa$ of Theorem \claimref{synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation} acts on fields, in the convention of its clause (5), by its vector part $-1$ on $\R^{2,4}$ and on the colour index by an automorphism of $\su(3)$. The vector part has determinant $+1$, its outermorphism is the grade involution $\mathrm{Ad}(I_{6})$, which fixes every even element, and every automorphism of $\su(3)$ preserves the trace form. Hence $\Theta(CF) = \Theta(F)$, in the spacetime algebra and for every four-form of $\Cl(2,4)$ built from two bivector fields. A real-linear flag conjugate has determinant $-1$ (clause (3) there); it reverses $I_{6}$, and it reverses $\Theta$ when it preserves the four-space that carries $F$ and reverses its orientation.
\item[(iii)] \emph{(Signature reversal carries it with its sign.)} Let $\gamma'_{\mu}$ generate the algebra of the reversed signature, $Q(\gamma'_{\mu}) = -Q(\gamma_{\mu})$. The map $\gamma_{\mu}\gamma_{\nu} \mapsto -\gamma'_{\mu}\gamma'_{\nu}$ extends to an isomorphism $\sigma$ of the even subalgebras with $\sigma(I_{4}) = I'_{4}$, so $\Theta'(\sigma F) = \sigma(\Theta(F))$ has the same coefficient on $I'_{4}$ as $\Theta(F)$ has on $I_{4}$. The identification without the sign is not multiplicative, and gives the same four-form.
\item[(iv)] \emph{(No colour coefficient on the covariant coupling.)} If $\det Y \neq 0$, every phase symmetry has $a_{3} = -n(q_{1} - q_{2})$. If also $\det\tilde{Y} \neq 0$, every phase symmetry has $q_{1} = q_{2}$ and $a_{3} = 0$. At the family point of the cone ($\alpha = 0$) $\det M_{d} = \beta^{n}\det Y$ and $\det M_{u} = \bar\beta^{n}\det\tilde{Y}$, so both determinants are nonzero exactly when no quark is massless there; on the lift family $(|\beta|^{2} - |\alpha|^{2})\tilde{Y} = \beta M_{u} - \alpha M_{d}$ and $(|\beta|^{2} - |\alpha|^{2})Y = \bar\beta M_{d} - \bar\alpha M_{u}$, so both are invertible when $|\alpha/\beta|$ is smaller than the ratio of the least singular value of each mass matrix to the greatest of the other.
\item[(v)] \emph{(When a colour coefficient is possible.)} Suppose $p$ is not identically zero and a phase symmetry has $a_{3} \neq 0$. Then $K_{\Phi}$ is diagonal, $p(a, b) = c\,a^{j}b^{n-j}$ for one $j$ with $2j \neq n$, and $a_{3} = -(2j - n)(q_{1} - q_{2})$. In that case, on a charge-preserving point of the lift locus, where $\alpha\beta = -H^{2}$, the product of the $2n$ quark masses is $|c|^{2}H^{2n}$, and at the family point of the cone a quark is massless. The condition is met with $a_{3} \neq 0$ by $\tilde{Y} = 0$, by $Y = 1$ with $\tilde{Y}$ nilpotent, and by the family split $Y = \mathrm{diag}(1, 1, 0)$, $\tilde{Y} = \mathrm{diag}(0, 0, 1)$ ($j = 2$, $a_{3} = -(q_{1} - q_{2})$).
\item[(vi)] \emph{(One family, in the stored module.)} In the five-mode module of the cited charge list, give the coefficients $\alpha$ of the slot creation operators and $\beta$ of the slot contractions independent charges $h_{v}$, $h_{w}$. The terms $B(\psi, c\varphi)$ conserve a four-dimensional space of charges, the fourth having $A_{3} = -2(h_{v} + h_{w})$ (clause (ii) there). The terms $B(\psi, c^{*}\varphi)$, in which $v$ carries $\bar\beta$ and $w$ carries $\bar\alpha$, add the conditions that force $h_{v} + h_{w} = 0$: the charges conserved by both are $\mathrm{span}\{Y, n_{B}, n_{L}\}$, and $A_{3}$ vanishes on them. The unit of the module with $h_{v} = h_{w} = -2$ is conserved by the coupling to $c$ and has charge $4$ on every term of the coupling to $c^{*}$, so of the group it generates exactly the quarter turns survive. The quarter turn acts on the sixteen by the unit $I_{4}$ and on the slot coefficients by $-1$: it is the pseudoscalar $\omega$ of the ten Majoranas of Theorem \claimref{synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element}(ii), up to its inverse. Its colour coefficient is $A_{3} = 8$.
\item[(vii)] \emph{(The scalar sector.)} The axial phase $\alpha \mapsto e^{I_{4}\phi}\alpha$, $\beta \mapsto e^{I_{4}\phi}\beta$ (so $q_{1} - q_{2} = 2$ per unit of $\phi$) fixes $\mathsf{N}$, $m$, $|Q|$ and the D-term potential of Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}, hence $V_{D} + W(\mathsf{N}) + k_{10}|Q|^{2}$ for every function $W$, and the cone $Q = 0$; it multiplies $Q$ by $e^{2I_{4}\phi}$, so it moves the terms with $k_{4}, \dots, k_{9}$ of Theorem \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}(3) and the lift locus $Q = -H^{2}$. At the family point of the cone, $\alpha = 0$, the axial phase composed with the inverse hypercharge rotation fixes the point and turns $\alpha$ by $e^{2I_{4}\phi}$: the two directions of the normal pair are one $I_{4}$-complex field carrying this unbroken phase, which is the equality $m_{H} = m_{A}$ at $k_{8} = k_{9} = 0$ of clause (2) there. No direction of the field is massless there except the gauge orbit.
\item[(viii)] \emph{(The normal pair moves the phase of the determinant.)} At the family point of the cone, to first order in the normal pair $\alpha_{1}$,
\[
\delta\log\det M_{u} = \frac{\alpha_{1}}{\bar\beta_{1}}\tr(\tilde{Y}^{-1}Y), \qquad \delta\log\det M_{d} = \frac{\bar\alpha_{1}}{\beta_{1}}\tr(Y^{-1}\tilde{Y}),
\]
so the $I_{4}$ part of $\log\det(M_{u}M_{d})$ has nonzero gradient along the normal pair unless $\tr(\tilde{Y}^{-1}Y)$ is the conjugate of $\tr(Y^{-1}\tilde{Y})$.
\end{enumerate}
\emph{Reading (argued).} Two literature statements are used here and are not stored Facts, both cited from memory: the physical angle is $\bar\theta = \theta + $ the $I_{4}$ phase of $\det(M_{u}M_{d})$, and a phase rotation with colour coefficient $a_{3}$ through an angle $\phi$ shifts $\theta$ by $a_{3}\phi$. (a) \emph{What each premise says about the bare angle.} Premise \claimref{dark-matter.premise-cpt-covariance} holds for every value of $\theta$, by (ii): it says nothing about it. On the family terms the premise takes the adjoint reading, which fixes the sum of each term and its adjoint and so the mass phase; on the entrywise reading, which is not premised, $C$ would fix the angle term and reverse the mass phase, and the clause would then require that phase to be $0$ or a half turn together with $J = 0$, which the stored $J$ excludes. Premise \claimref{dark-matter.premise-flag-as-datum} makes the two flag signs configurations of one functional with one angle, and $C$, which exchanges them, fixes the term: nothing is forced, and the term does not tell the two signs apart, so it is no refutation of that premise. By (iii) the mirror tower's functional is the copy with the same sign, and Premise \claimref{synthesis.common-ceiling-coupling-premise}, which equates every coupling of the copied theory at the ceiling, equates the two towers' angles; it relates them and fixes neither. The only maps that reverse the term reverse an orientation; none is premised to be a symmetry, and a real-linear flag conjugate reverses the frozen point's action with it. So the series does not fix the bare angle. (b) \emph{One datum or several.} The flag is configuration data; the up-down stage phase that the store selects from the data (\claimref{synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase}) is a parameter of the family terms, which $C$ in the adjoint reading does not move. So the stored laws carry a parity- and time-odd parameter of their own, and the angle would be another: the flag is not the only such datum. (c) \emph{Nothing relaxes the angle.} By (iv) and (v), with the stored coupling and no massless quark, no phase symmetry of the doublets or the families shifts the angle; by (vi) the charge that would have done so, with $\tilde{Y}$ absent, is the unit of the module, and what is left of it is $\omega$, which shifts the angle by $\tfrac12 A_{3}\cdot\tfrac{\pi}{2} = 2\pi$ per family and so constrains nothing; by (vii) the potential's axial phase symmetry is broken by the Yukawa terms and by $H^{2}$, and where it holds it is unbroken at the vacuum of the cone, so there is no light neutral odd scalar; by (viii) the normal pair does couple linearly to the angle term through the mass phase, as a massive field with no shift symmetry: with the stored masses of that pair near $3$ TeV on the working branch and a topological susceptibility near $(75\ \mathrm{MeV})^{4}$ (literature), its displacement lowers $\bar\theta$ by a relative part of order $10^{-13}$, an order-of-magnitude estimate. So the angle that the fifteenth refutation left open (\claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}(ii)), one that relaxes or rolls, has no carrier among the stored fields examined: the rung field's eight components. That this list of stored scalar fields is complete is argued, not proved. (d) \emph{The second invariant.} The conclusion is the same for every $W(\mathsf{N})$, so the strong CP question puts no condition on $W$. (e) Had $\tilde{Y}$ been absent, the axial phase would have been a symmetry with colour coefficient $-2n$ broken at the weak scale, and its neutral odd scalar an axion with decay constant at the weak scale, which is excluded (literature, checked at the review cited in the note); the stored requirement $m_{t} \neq m_{b}$ already needs $\tilde{Y}$.

Not shown: the phase of the determinant on any stored family structure; loop corrections; the angle of the weak field.

## technical
The colour angle multiplies the grade-four part of the colour field square, $2\,E\cdot B\,I_{4}$ per colour component. An isometry of the vectors multiplies it by its determinant. The stored CPT conjugation acts on fields by the vector map $-1$ of the six-dimensional ambient, of determinant $+1$, and by an automorphism of the colour algebra, so it fixes the term; a real-linear flag conjugate, of determinant $-1$, reverses it and reverses the frozen point's action too. The even algebras of the two signatures are isomorphic by a map that sends $I_{4}$ to $I'_{4}$, so the mirror's term is the copy with the same sign. Hence the CPT premise, the flag premise and the copy theorem leave the bare angle free, and the common-ceiling-coupling premise only equates the two towers' angles.

For the covariant coupling $Y$ on $c$ and $\tilde{Y}$ on $c^{*}$ with $n$ families, traces of the four invariance conditions give $2\tr K_{Q} + \tr K_{u} + \tr K_{d} = 0$ and equal doublet weights as soon as $Y$ and $\tilde{Y}$ are invertible, which holds when no quark is massless at the cone's vacuum. In general a nonzero colour coefficient needs $\det(aY + b\tilde{Y})$ to be a single monomial $c\,a^{j}b^{n-j}$ with $2j \neq n$, and then the product of the quark masses on the lift locus is $|c|^{2}H^{2n}$. For one family the charge removed by the conjugate coupling is the unit of the module, of which the quarter turn, the pseudoscalar of the ten Majoranas, survives. The potential's axial phase symmetry holds for $V_{D} + W(\mathsf{N}) + k_{10}|Q|^{2}$ with any $W$ and is unbroken at the cone's vacuum, where the normal pair is its charged field; the normal pair moves the phase of the mass determinant at first order but is massive. No stored field examined relaxes the angle, and $W$ is not constrained.

## lay
The strong force allows a term whose strength is an angle, and measurements of the neutron show that angle to be smaller than about one part in ten billion. This result asks two things of the series. First, whether any of its symmetries forces the angle to vanish: the series' own version of the combined reversal of charge, space and time leaves the term unchanged, the mirror world carries the same term with the same sign, and the only operations that would flip it are mirror reflections, which the series does not take to be symmetries. So nothing fixes it. Second, whether any field of the series could make the angle relax to zero, as an axion would: the field that gives quarks their masses couples in two ways at once, and the two together leave no symmetry of the required kind, provided no quark is massless. The heavy neutral partner of the Higgs field does feel the angle, but it is far too heavy to move it. The series therefore neither sets the angle nor relaxes it.

## one-liner
The grade-four part of the colour field square is fixed by the stored CPT conjugation (vector part of determinant $+1$, an automorphism on the colour index), reversed only by orientation-reversing maps, and carried to the mirror with its sign; on the covariant coupling $Y$ on $c$, $\tilde{Y}$ on $c^{*}$ with both invertible every phase symmetry has colour coefficient $0$ (a nonzero one needs $\det(aY + b\tilde{Y}) = c\,a^{j}b^{n-j}$, $2j \neq n$), the charge removed is the unit of the module, cut to $\omega$, and the normal pair is massive: no stored premise fixes the angle and no stored field relaxes it.
