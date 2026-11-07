---
id: synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation
kind: claim
version: 3
title: 'CPT conjugation as the pseudoscalar rotor times complex conjugation'
status: proved
region: synthesis
subject: clifford-structure
tags: [matter-asymmetry, witt-index, no-go]
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
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.dark-matter.witt-flag
- obj.std-algebra.rotor
- obj.std-algebra.conformal-algebra
derivations:
- name: main
  uses:
  - dark-matter.two-families-are-two-chiralities@6
  - singularity.euclidean-rotor-where-it-lies@4
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - std-algebra.involution-properties@1
  - std-algebra.bivector-exponential@2
  - std-algebra.pseudoscalar-commutation@1
  assumes: []
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_anti_automorphism_and_rotor
- kind: check
  ref: check.py::check_conjugate_flag_other_family
- kind: check
  ref: check.py::check_real_linear_swap_reverses_action
- kind: check
  ref: check.py::check_C_antilinear_automorphism
- kind: check
  ref: check.py::check_reading_convention
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.premise-cpt-covariance
  - dark-matter.orientation-arrow-seventeenth-refutation
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: Cl(2,4) (x) C is Cl(3,4) with complex unit I_7 = I_6 e, the central pseudoscalar of the odd extension (std-algebra.complexification-is-the-odd-extension, cited as a mention), and kappa is the automorphism e -> -e (I_7 -> -I_7); the Witt flag w_k = e_{2k-2} - I_7 e_{2k-1}, the eigenvalues I_6 N = I_7 N and I_6 Nbar = -I_7 Nbar (checked in GA.py in the maintainer''s scratch: I_7 central, Gram diag(4, -4, -4)), the complex structure J = +-I_7 and the I_7 component of the exchanged e_0 are written with I_7. The entity says once that I_7 is the complex unit and I_6 the real pseudoscalar acting with eigenvalue +-I_7; they are not identified. No bare i remains, so the outside_ga declaration (other, for i only) is removed. Version kept at 3, already bumped in this pass.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the result is about complex conjugation kappa on Cl(2,4) (x) C and the Witt flag in C^6 spanned by e_{2k-2} - i e_{2k-1}; that i must commute with every vector, and I_6 psi_W = +-i psi_W compares I_6 with it.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.involution-properties, std-algebra.bivector-exponential, std-algebra.pseudoscalar-commutation where the proof uses them. Version 1 -> 2.'
  open_problem: pr.cpt-and-intrinsic-clock
  note: >-
    Settles the type of the stored CPT conjugation. As worded (grade involution, reversal, flag
    conjugate) it is an anti-automorphism of the Clifford algebra, not an automorphism. On the
    conformal ambient its vector part is a rotor of the identity component. With the field-action
    convention stated in the formal level (an anti-automorphism acts on vectors directly and on
    connections through the Lie algebra automorphism it induces, so curvature is carried by that
    automorphism), the only part that is not a constant gauge rotation is the flag conjugate, and it
    preserves the frozen point's action only if it is antilinear (complex conjugation). Under that
    convention the premise's description "a real linear automorphism, not the antiunitary operator"
    has the type the wrong way round. Applying the anti-automorphism instead to the Clifford integrand
    as a whole inverts both sign statements, so the conclusion is convention-dependent and the
    convention is part of the statement. The algebra is transport-absent (standard facts about
    Cl(2,4) and pure spinors); it is used to pin a series premise. Clause (5) proves the premise's
    action clause, in this convention, for the frozen point's action and for every functional of real
    tensor fields invariant under constant SO_0(2,4); spinor fields, fermionic and internal gauge
    sectors stay premised. The rewording of dark-matter.premise-cpt-covariance is a decision for the
    maintainer.
---

## formal
Let $\R^{2,4}$ carry the conformal ambient metric, $\Cl(2,4)$ its Clifford algebra with $e_0^2 = e_1^2 = 1$ and $e_2^2 = \dots = e_5^2 = -1$, $I_6 = e_0 e_1 \cdots e_5$ its unit pseudoscalar, and $\Cl(2,4) \otimes \C = \Cl(3,4) = \Cl(2,4) \oplus \Cl(2,4)I_7$ its complexification, whose complex unit is the central pseudoscalar $I_7 = I_6e$ of the odd extension ($e$ orthogonal to $\R^{2,4}$, $Q(e) = +1$; Theorem \claimref{std-algebra.complexification-is-the-odd-extension}); $\kappa$ is complex conjugation, the automorphism induced by $e \mapsto -e$, which fixes $\Cl(2,4)$ and sends $I_7$ to $-I_7$. $I_7$ is the complex unit throughout; $I_6$ is the real pseudoscalar of $\Cl(2,4)$, which acts on pure spinors with eigenvalues $\pm I_7$, and the two are not identified. Let $W \subset \C^6 = \R^{2,4} \oplus I_7\R^{2,4}$ be a maximal isotropic subspace with $W \cap \overline W = 0$ (the generic Witt flag of Definition \claimref{obj.dark-matter.witt-flag}), and $\psi_W$ its pure spinor.
\begin{enumerate}
\item The composite of grade involution and reversal is an anti-automorphism of $\Cl(2,4)$, not an automorphism, and acts on vectors as $-1$. Grade involution equals $\mathrm{Ad}(I_6)$, and $I_6 = (e_0e_1)(e_2e_3)(e_4e_5)$ is a rotor of the identity component: each factor squares to $-1$ and is $\exp(\pi B_k/2)$, and $I_6 \widetilde{I_6} = 1$. So the vector action $-1$ lies in $SO_0(2,4)$. In $\Cl(1,3)$, by contrast, $I_4\widetilde{I_4} = -1$.
\item $W$ is the $+I_7$ eigenspace of an orthogonal complex structure $J$ on $\R^{2,4}$, $W \oplus \overline W = \C^6$, and $I_6\psi_{W} = \pm I_7\,\psi_{W}$, $I_6 \psi_{\overline W} = \mp I_7\,\psi_{\overline W}$. So $\overline W$ lies in the other family, and complex conjugation is a flag conjugate. In $\Cl(3,3)$, $I_6^2 = +1$ and conjugation preserves the family.
\item Every real-linear isometry $g$ of $\R^{2,4}$ with $g(W) = \overline W$ has $\det g = -1$, so that $\epsilon(gI, gV, gF, gF) = -\epsilon(I, V, F, F)$ for vectors $I, V$ and bivectors $F$, $g$ acting on bivectors by its outermorphism. The complex-linear Witt exchange $v_k \leftrightarrow w_k$ does not preserve $\R^{2,4}$.
\item $C := \mathrm{Ad}(I_6) \circ \kappa$ is an antilinear involutive automorphism of $\Cl(2,4) \otimes \C$ that is $-1$ on $\R^{2,4}$, fixes the metric, $\epsilon$ and $I_6$, and carries $\psi_W$ to a multiple of $\psi_{\overline W}$. With the flag conjugate realised by $\kappa$, the stored composite $\phi$ (grade involution, reversal, flag conjugate) is reversal composed with $C$: an antilinear anti-automorphism. No realisation of the flag conjugate on $\R^{2,4}$ is both real-linear and orientation-preserving.
\item \emph{Convention.} A (possibly anti-) automorphism $\phi$ acts on fields as a symmetry: on a vector field by its vector part, and on a connection $A$ through the Lie algebra automorphism it induces, $A \mapsto -\phi(A)$ when $\phi$ is an anti-automorphism, so that curvature transforms by the same automorphism; for the stored composite this is the action of $C$. In this convention every action functional of real tensor (multivector) fields on which $C$ acts through its vector part, invariant under constant $SO_0(2,4)$ transformations, in particular the frozen point's $Q(I)^{-1}\int \epsilon(I, V, F, F)$ (\claimref{dark-energy.frozen-point-makes-stelle-west-vector}), satisfies $S \circ \phi = S$, while with any real-linear flag conjugate in place of $\kappa$ the same action changes sign. Spinor fields are not covered. If instead $\phi$ is applied to the Clifford integrand $IVFF$ as a whole and the top-grade coefficient taken, both sign statements invert (with $\kappa$ the integrand changes sign, with a real-linear flag conjugate it is preserved), so the conclusion of (5) depends on the convention.
\end{enumerate}

## technical
The seventeenth refutation rests on CPT conjugation, stored as the composite of grade involution, reversal and the flag conjugate $v_k \leftrightarrow w_k$ and described as a real linear automorphism that is not the antiunitary CPT operator of quantum field theory. This result fixes the type. Reversal makes the composite an anti-automorphism. On the conformal ambient its vector part, $-1$, is the action of the pseudoscalar $I_6$, which is a product of three commuting rotations by $\pi$ and so lies in the identity component: unlike in $\Cl(1,3)$, where total reflection needs complexification, here it is a real gauge rotation. What is left is the flag conjugate. For a generic flag $W$ the complex conjugate $\overline W$ is complementary and lies in the other family, because $I_6^2 = -1$ makes chirality an imaginary eigenvalue, so complex conjugation exchanges the families while fixing every real structure. Any real-linear exchange of the families has determinant $-1$ and reverses the frozen point's MacDowell-Mansouri integrand. So, when the conjugation acts on fields as a symmetry (vectors by its vector part, connections through the induced Lie algebra automorphism), the conjugation that leaves the action invariant, as the refutation needs, is antilinear on the complexified ambient and on the Fock module, of Wigner's antiunitary type (argued). Applying the anti-automorphism to the Clifford integrand as a whole inverts the sign statements, so this convention is part of the result. In it the premise's action clause holds for the frozen point's action and for every functional of real tensor fields invariant under constant conformal rotations; spinor fields, the fermionic and the internal gauge sectors remain premised.

## lay
The argument that the universe's matter-antimatter orientation is a free choice relies on a symmetry that swaps matter with antimatter and reverses space and time. The series described this symmetry as an ordinary linear operation, unlike the one used in quantum field theory. This result checks the algebra exactly and finds the opposite. In the six-dimensional space the series works in, the space-and-time reversal part is just a rotation, a symmetry the theory already has. The matter-antimatter swap is the genuinely new part, and acting on the fields in the usual way, it leaves the gravitational action unchanged only if it acts by complex conjugation, the same kind of operation quantum field theory uses. Done as an ordinary linear swap, it would flip the sign of the gravitational action.

## one-liner
On the conformal ambient the stored CPT conjugation is an anti-automorphism whose vector part is the rotor $I_6$ of the identity component; acting on fields (vectors directly, connections through the induced automorphism), its flag conjugate preserves the frozen point's action only when realised by complex conjugation, so the conjugation is antilinear, of Wigner's type (argued).
