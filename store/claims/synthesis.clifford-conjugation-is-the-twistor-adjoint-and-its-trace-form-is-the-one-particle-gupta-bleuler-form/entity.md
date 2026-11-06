---
id: synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form
kind: claim
version: 1
title: 'Clifford conjugation as twistor adjoint and the Gupta-Bleuler form'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, conformal-spinors, representation-theory, car-algebra, dictionaries]
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
  - synthesis.positive-structure-is-twistor-form-at-imaginary-time@3
  - field-theory.fock-space-maxwell-modes@4
  - field-theory.imported-tower-limit@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_twistor_adjoint_is_clifford_conjugation
- kind: check
  ref: check.py::check_trace_form_on_vectors_is_gupta_bleuler
- kind: check
  ref: check.py::check_krein_trace_form_is_conformally_invariant_and_positive_one_is_not
- kind: check
  ref: check.py::check_invariant_forms_on_polarisations_are_multiples_of_the_metric
- kind: check
  ref: check.py::check_fock_form_over_the_trace_form_is_the_stored_krein_form
- kind: check
  ref: check.py::check_ghost_twist_is_a_mode_parity_as_j_is
- kind: check
  ref: check.py::check_scalar_part_of_clifford_conjugate_is_minus_the_metric_in_any_signature
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields
  - synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts
  - synthesis.positive-structure-is-twistor-form-at-imaginary-time
extraction:
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Bears on whether the indefinite form of the Krein premise (KF) can be derived from the series' structures.
    Answer: its one-particle form can be identified, not derived. The adjoint of the twistor form on the conformal
    spinor module is Clifford conjugation of Cl(2,4), independent of the twistor form's real factor, and its
    normalised trace form on vectors is minus the metric. That identity, the scalar part of conj(a) b equal to
    -a.b, holds in every Clifford algebra with no module and no twistor form, so the one-particle Gupta-Bleuler
    form is the store's metric with its sign reversed; the sign that makes the spatial polarisations positive
    comes from the store's signature, and the normalisation is a convention. What the twistor form adds is the
    involution J, which relates this form to the positive structure's trace form, the Euclidean form of the time
    e1 used for the stored photon, and whose second quantisation is the stored fundamental symmetry (-1)^{n0}.
    Every Lorentz-invariant Hermitian form on the polarisations is a real multiple of -u.w (Schur, computed). The
    Fock space over this one-particle form gives [a(u), a(w)^dagger] = -u.w on all four polarisations, the
    Feynman-gauge (alpha = 1) realisation of (K1); covariant gauges with alpha != 1 use the dipole (B-field) state
    space, which is not a Fock space over a one-particle form and is not described here. The ghost twist of (K2)
    is the parity of one mode, as J is up to sign (computed; this distinguishes nothing, since every mode-parity
    twist is of this kind). Not derived: that the polarisation and ghost state spaces carry the indefinite form
    rather than a positive one (the content of (K1) and (K2) as a premise), (K3) and (K4). Standard throughout;
    transport-absent. Formerly filed as synthesis.gupta-bleuler-form-is-the-trace-form-of-the-twistor-adjoint.
---

## formal
Units and signature of the store. Let $\CS$ be the eight-dimensional conformal spinor module of $\Cl(2,4)$ with the generators $e_{1}$ ($e_{1}^{2} = 1$, the time), $e_{2}, e_{3}, e_{4}$ (squares $-1$) and the ascent plane $e_{\pm}$ ($e_{\pm}^{2} = \pm 1$), the positive Hermitian structure $h$ for which every generator is unitary, $J = ie_{1}e_{+}$ and the twistor form $\Sigma(\psi, \varphi) = h(\psi, J\varphi)$ of Theorem \claimref{synthesis.positive-structure-is-twistor-form-at-imaginary-time}. Write $A^{\dagger}$ and $A^{\sharp}$ for the adjoints of an operator $A$ on $\CS$ for $h$ and for $\Sigma$, $\bar A$ for Clifford conjugation (the anti-automorphism with $\bar a = -a$ on vectors, extended antilinearly to complex combinations), and $\tau(A) = \tfrac18\operatorname{tr}A$. Polarisation vectors $u, w$ are vectors of the span of $e_{1}, \dots, e_{4}$, with $u\cdot w$ the store's metric, $Q(e_{1}) = 1$.
\begin{enumerate}
\item[(i)] \emph{(The twistor adjoint is Clifford conjugation; proved.)} $A^{\sharp} = JA^{\dagger}J$; for every $A$ in $\Cl(2,4)$ acting on $\CS$, $A^{\sharp} = \bar A$, so $B^{\sharp} = (-1)^{k(k+1)/2}B$ for a blade $B$ of grade $k$; and $A^{\sharp}$ is unchanged when $\Sigma$ is replaced by $\lambda\Sigma$, $\lambda$ real and nonzero.
\item[(ii)] \emph{(Its trace form on vectors is minus the metric; proved.)} For real vectors $a, b$ of $\Cl(2,4)$, $\tau(a^{\sharp}b) = \langle\bar ab\rangle_{0} = -a\cdot b$, of signature $(4, 2)$; the identity $\langle\bar ab\rangle_{0} = -a\cdot b$ holds in every Clifford algebra, with no module and no twistor form. $\tau(a^{\dagger}b)$ is the Euclidean form in which the six generators are orthonormal. The two are related by $J$: $\tau(a^{\sharp}b) = \tau(a^{\dagger}JbJ)$, where $b \mapsto JbJ$ reverses $e_{1}$ and $e_{+}$ and fixes $e_{2}, e_{3}, e_{4}, e_{-}$. On polarisation vectors the first is the one-particle Gupta-Bleuler form $-u\cdot w$, negative on $e_{1}$ and positive on $e_{2}, e_{3}, e_{4}$ (the sign from the store's signature, the normalisation by the choice of $\tau$); the second is the Euclidean form of the time $e_{1}$; and $J$ acts as $u \mapsto -e_{1}ue_{1}$.
\item[(iii)] \emph{(Invariance; proved.)} $\tau(a^{\sharp}b)$ is invariant under every rotor of $\Cl(2,4)$; the positive form $\tau(a^{\dagger}b)$ is not invariant under the boost $\tfrac54 + \tfrac34e_{1}e_{2}$, which takes $e_{1}$ to a vector of positive norm $\tfrac{257}{32}$.
\item[(iv)] \emph{(Uniqueness; proved.)} The real bilinear forms on the polarisation space invariant under the six Lorentz bivectors form a one-dimensional space spanned by the metric. Hence every Lorentz-invariant Hermitian form on the complex polarisations is a real multiple of $-u\cdot w$, and none is definite.
\item[(v)] \emph{(Second quantisation; proved.)} On the polynomials in $z_{0}, \dots, z_{3}$ with the form $\langle z^{\alpha}, z^{\beta}\rangle = \alpha!\,\delta_{\alpha\beta}$ (Proposition \claimref{field-theory.fock-space-maxwell-modes}), the bosonic Fock form over the one-particle form $\tau(u^{\sharp}w)$ is $\langle z^{\alpha}, (-1)^{n_{0}}z^{\beta}\rangle$, and for it the adjoint of $a_{\mu} = \partial/\partial z_{\mu}$ is $-g_{\mu\mu}z_{\mu}$, so $[a(u), a(w)^{\dagger}] = -u\cdot w$ on all four polarisations: the Feynman-gauge ($\alpha = 1$) realisation of the form in clause (K1) of Premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}, with fundamental symmetry the second quantisation of $b \mapsto JbJ$. Covariant gauges with $\alpha \neq 1$ use the dipole state space with an auxiliary field, not a Fock space over a one-particle form, and are not described here.
\item[(vi)] \emph{(The ghost twist; computed.)} $J = 2n_{c} - 1$, with $n_{c}$ the number operator of the mode $c = \tfrac12(e_{1} + ie_{+})$; on a floor of two tower modes $b, d$ (Fact \claimref{field-theory.imported-tower-limit}) the ghost twist $S = 1 - (b^{*} - d^{*})(b - d)$ of (K2) is $1 - 2n_{-}$, the parity of the mode $(b - d)/\sqrt2$. Both twists are parities of one mode; every fundamental symmetry of this kind on a fermion floor has that form, so this does not single out (K2).
\end{enumerate}
\emph{Reading (argued).} The one-particle form of (K1) is minus the store's metric, the trace form of Clifford conjugation in any Clifford algebra; the twistor form supplies the involution $J$ that relates it to the positive polarisation form, so the frame that the positive form singles out is the attachment's imaginary time point. Clause (K1) as a premise, that the polarisation and ghost state spaces carry the indefinite form, is not derived, and neither are (K2) to (K4). The covariant and the positive forms are both present in the attachment, as in Theorem \claimref{synthesis.positive-structure-is-twistor-form-at-imaginary-time}(iv), where the covariant form is the one on the whole space and states exist only for positive structures. Standard; transport-absent.

## technical
The Krein premise of the series' gauge-field theory gives the polarisations of a gauge field the indefinite Gupta-Bleuler form, minus the Minkowski metric. This result places that form among the series' structures. The adjoint of the twistor form on the conformal spinor module of Cl(2,4) is Clifford conjugation, the anti-automorphism that negates every vector, whatever the real factor of the twistor form; its normalised trace form on vectors is minus the metric. That last identity holds in every Clifford algebra, so the one-particle Gupta-Bleuler form is simply the series' metric with its sign reversed, and the twistor form adds the involution J, which relates it to the positive structure's trace form, the Euclidean form of the time used for the stored photon, and whose second quantisation is the stored fundamental symmetry (-1)^{n_0}. Every Lorentz-invariant Hermitian form on the polarisations is a multiple of this one (computed). The Fock space over it is the Feynman-gauge realisation; other covariant gauges need a dipole state space and are not covered. The ghost twist is, like J, the parity of one fermion mode, which every such twist is. Nothing here derives that the unphysical modes must carry the indefinite form, the regulator fields, or positivity of the physical space. Standard; transport-absent.

## lay
The indefinite "length" used to quantise force fields covariantly gives the time direction negative length and the space directions positive length. This is the series' own spacetime metric with its sign reversed. The result shows that the conformal spinors of the series carry the same rule, and that the ordinary positive length used for light corresponds to choosing a time direction. It does not show that the series must use the indefinite length for its unphysical states; that remains an assumption.

## one-liner
Clifford conjugation, the twistor adjoint on the conformal spinors, has trace form $-a\cdot b$ on vectors (as in every Clifford algebra); on polarisations this is the one-particle Gupta-Bleuler form of (K1), unique up to a real factor among Lorentz-invariant forms, with fundamental symmetry the second quantisation of $J$ and Fock space the Feynman-gauge realisation; restates, does not derive, (K1); (K2) to (K4) do not follow; transport-absent.
