---
id: synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike
kind: claim
version: 3
title: 'The Krein quartet''s induced-gravity weight depends on the regulator'
status: proved
region: synthesis
subject: einstein
tags: [gauge-fields, mode-counting, curvature-and-field-equations, no-go, undetermined-input, needs-continuum]
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
  role: pins to the slot-module and attachment results moved to their new versions after the clause split
  version: 3
  source: maintainer pass 2026-11-07
review: draft
derivations:
- name: main
  uses:
  - synthesis.imported-sakharov-induced-gravity-coefficients@2
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations@3
  - standard-model.connection-forced@4
  - synthesis.slot-module-light-ray-arrays-are-weyl-components@3
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@4
  - synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1
  - synthesis.imported-ikeda-taniguchi-spectra-of-the-hodge-laplacian-on-spheres@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_einstein_static_and_sphere_curvature_and_vector_density
- kind: check
  ref: check.py::check_quartet_cancels_level_by_level_on_the_einstein_static_field
- kind: check
  ref: check.py::check_gauge_fixed_operator_has_longitudinal_eigenvalue_over_alpha
- kind: check
  ref: check.py::check_four_sphere_spectra_reproduce_heat_kernel_densities
- kind: check
  ref: check.py::check_vector_weight_is_alpha_minus_five
- kind: check
  ref: check.py::check_series_content_induced_coefficient
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields
  - synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts
extraction:
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3, at Leon''s decision of 7 November 2026 splitting the algebra of the canonical part on a null plane out of the light-ray and slot-module results (synthesis.canonical-part-of-a-spinor-on-a-null-plane): this result cites the slot-module result for sixteen Weyl components per generation (its clause (ii)), which is not part of the algebra split out, so the uses edge stays; its pin moves from version 1 to 2 and the pin to the attachment result from 2 to 3 (both statements unchanged). Statement, proof and checks unchanged. Notation: no bare imaginary unit; nothing to declare.'
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decisions of 2 November 2026: an assumes edge to the Krein premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2, which clause (i) and the reading state as their hypothesis ((K1) for the zero-point sign of the negative-norm time component, (K4) in the reading); a uses edge to the new imported Fact synthesis.imported-ikeda-taniguchi-spectra-of-the-hodge-laplacian-on-spheres@1, which replaces the in-text citation from memory (and the entity''s own bibliography entry); the extraction note names synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form by id at its reviewed strength. Pin of synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum moved to @3 (dated note, spectrum unchanged). The check touches both new premises. Statement unchanged.'
  open_problem: op.einstein-from-the-field-theory
  note: >-
    Induced gravity beyond the cancelling content: the gauge sector with its Krein quartet (time or exact
    component, its partner, ghost, antighost) and the regulator. The stored count gives each gauge vector the
    weight -4 of its two helicities, which is the Feynman-gauge heat-kernel value. Here: under an energy
    cut-off on the Einstein static field the quartet's four members have the same frequencies and cancel level
    by level (one zero-energy mode left), so the two-helicity count is exact there; under a heat-kernel
    (proper-time) cut-off on the gauge-fixed operators of the Nakanishi-Lautrup family the longitudinal
    eigenvalues are the scalar ones divided by alpha while the ghosts' are not, and the vector's weight is
    alpha - 5 (Landau gauge -5), quartic weight 1 + alpha^2. With the content in force (12 vectors, 48 Weyl
    fields, two elementary doublets of curvature coupling xi_R) the induced coefficient is
    12(alpha - 1) + 8(1 - 6 xi_R) under the covariant cut-off and 8(1 - 6 xi_R) under the energy cut-off; the
    stored zero needs xi_R = 1/6 and alpha = 1 (or the energy cut-off). Under the Krein premise, clause (K1) is
    the Gupta-Bleuler value alpha = 1, so the stored count is the store's value; the result says that this is a
    property of the content together with the regulator and the gauge. Standard in kind (power divergences are
    gauge dependent); the weight alpha - 5 and the level-by-level cancellation on the Einstein static field are
    computed here. The curvature coupling is written xi_R because xi is the D-term level in the store.
    The coexact one-form spectra on S^3 and S^4 are those of the imported Fact
    synthesis.imported-ikeda-taniguchi-spectra-of-the-hodge-laplacian-on-spheres and enter only through the exact
    heat-kernel densities they reproduce. Clause (i) uses clause (K1) of the Krein premise for the
    zero-point sign of the negative-norm time component, and the reading uses (K4). The result
    synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form
    shows that the one-particle form -u.w of (K1) is the trace form of the twistor adjoint, while the quantisation
    of the unphysical modes with the indefinite form stays a premise; on all four polarisations that form is the
    alpha = 1 commutator, so under (KF) the gauge parameter on which the covariant-cut-off weight depends is
    alpha = 1. The weak-scale content here has two elementary doublets, while standard-model.chain runs
    with one doublet from M_Z to M_I; that tension between stored results is not resolved here. Euclidean
    computations (the four-sphere, heat kernels on closed Riemannian manifolds) are a reading of the local
    curvature-linear densities, outside the flat background. Transport-absent.
---

## formal
Let a gauge vector be gauge-fixed covariantly with parameter $\alpha > 0$ (the Nakanishi-Lautrup family; $\alpha = 1$ is the Gupta-Bleuler form of clause (K1) of Premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}), with its ghost and antighost, and call the \emph{weight} of a field its contribution to the induced Einstein-Hilbert coefficient in units of one minimally coupled real scalar (Fact \claimref{synthesis.imported-sakharov-induced-gravity-coefficients}(a), (b); a real scalar of curvature coupling $\xi_{R}$ has weight $1 - 6\xi_{R}$, a Weyl fermion $1$). The quartet is the time (or exact) component of the vector, its partner, the ghost and the antighost.
\begin{enumerate}
\item[(i)] \emph{(Energy cut-off on the Einstein static field; proved under the Krein premise, $\alpha = 1$.)} Under clause (K1) of the Krein premise, which fixes the zero-point energy of the negative-norm time component, on $\mathbb{R}\times S^{3}$ of unit radius in the Feynman gauge the time component, the exact part and the ghost pair all have frequencies $\sqrt{l(l+2)}$, with multiplicities $(l+1)^{2}$ ($l \ge 0$), $(l+1)^{2}$ ($l \ge 1$) and $2(l+1)^{2}$ of fermionic sign; the signed count vanishes at every $l \ge 1$ and is $-1$ at the zero frequency. So for every cut-off on energy the quartet contributes nothing to the zero-point sum, and the vector's weight is $-4$, that of its two helicities (the coexact one-forms, the attachment's helicity $\pm 1$ modules).
\item[(ii)] \emph{(Heat-kernel cut-off on the gauge-fixed operators; proved, in the Euclidean reading.)} On a closed Riemannian four-manifold (a Euclidean reading of the field equations, outside the flat background), with a proper-time cut-off on the gauge-fixed operator $P_{\alpha} = \delta d + \alpha^{-1}d\delta$ and on the ghost operator $\Delta_{0}$, the vector's weight is $\alpha - 5$ (transverse $-3$, longitudinal $\alpha$, ghosts $-2$) and its volume weight $1 + \alpha^{2}$; the two-helicity values $-4$ and $2$ hold only at $\alpha = 1$, and the Landau limit gives $-5$. On the unit four-sphere every term is computed exactly from the spectra.
\item[(iii)] \emph{(Gauge-invariant reading; proved.)} The parameter-free product $\det_{T}(\Delta_{1})^{-1/2}\det{}'(\Delta_{0})^{1/2}$ under one cut-off has weight $-4$.
\item[(iv)] \emph{(The series' content; computed.)} With the twelve vectors of the connection-forced algebra (Theorem \claimref{standard-model.connection-forced}), forty-eight Weyl fields (three separate slot modules of sixteen, \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}) and the two elementary doublets (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}) of curvature coupling $\xi_{R}$, the induced coefficient is $B = 8(1 - 6\xi_{R})$ minimal-scalar units under the energy cut-off and $B = 12(\alpha - 1) + 8(1 - 6\xi_{R})$ under the heat-kernel cut-off on the gauge-fixed operators: zero at $\xi_{R} = \tfrac16$ in the first case and at $\xi_{R} = \tfrac16$, $\alpha = 1$ in the second, $-12$ at $\xi_{R} = \tfrac16$ in the Landau gauge, and $8$ at $\xi_{R} = 0$, $\alpha = 1$.
\end{enumerate}
\emph{Reading (argued).} Under clause (K4) of the Krein premise the quartet has zero norm in the physical space (Fact \claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}); still, a power-divergent coefficient sees it unless the regulator treats its four members alike, so the induced Einstein-Hilbert coefficient of the series' content is fixed by its physical content only together with the regulator and, for a covariant cut-off, the gauge. Under the Krein premise ($\alpha = 1$) the vector weight is $-4$ and the stored cancellation (\claimref{synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations}) holds if the doublets are conformally coupled; schemes without a dimensionful cut-off induce no such term for massless fields (Fact \claimref{synthesis.imported-sakharov-induced-gravity-coefficients}(d)). Transport-absent.

## technical
Count each field's contribution to the induced Einstein-Hilbert coefficient in units of one minimally coupled scalar: a scalar of curvature coupling $\xi_{R}$ gives $1 - 6\xi_{R}$, a Weyl fermion $1$ (with the Lichnerowicz term computed in geometric algebra), and a gauge vector in the Feynman gauge with its ghosts $-4$, the value of its two helicities.

Under the Krein premise, for a covariantly gauge-fixed vector the unphysical quartet (time or longitudinal component, its partner, ghost and antighost) has zero norm in the physical space, but whether it drops from a power-divergent coefficient depends on the regulator. On the Einstein static field with a cut-off on energy, in the Feynman gauge, all four members have the same frequencies $\sqrt{l(l+2)}$ and their signed multiplicities cancel at every level, leaving one zero-energy mode: the quartet drops and only the two helicities count. With a covariant heat-kernel cut-off on the gauge-fixed operator of gauge parameter $\alpha$ (computed in the Euclidean reading), the longitudinal eigenvalues are the scalar ones divided by $\alpha$ while the ghosts' are not, and the vector's weight becomes $\alpha - 5$: $-4$ only at $\alpha = 1$, $-5$ in the Landau gauge. On the unit four-sphere every term is computed exactly from the spectra.

With the series' content (twelve vectors, forty-eight Weyl fields, two Higgs doublets of curvature coupling $\xi_{R}$) the induced coefficient is $8(1 - 6\xi_{R})$ under the energy cut-off and $12(\alpha - 1) + 8(1 - 6\xi_{R})$ under the covariant one. The stored cancellation needs conformal coupling and, for the covariant cut-off, $\alpha = 1$, the Gupta-Bleuler value of the Krein premise. Reading, argued: the coefficient is fixed by the content only together with the regulator and the gauge. Transport-absent.

## lay
Sakharov's idea is that the strength of gravity could be induced by the quantum jitter of all the other fields. Each kind of field adds or subtracts a definite amount, and an earlier result showed that the series' force carriers and matter particles cancel exactly, at least for one way of cutting off the jitter at short distances. Force carriers come with extra bookkeeping modes that describe nothing physical and are removed in the end. This result checks, under the series' premise for these modes (an indefinite inner product), whether they really drop out of the count. With a cut-off on energy they do, level by level. With a cut-off that treats space and time alike, they do only for one particular choice of the bookkeeping, and otherwise each force carrier shifts the count. So the cancellation depends on the cut-off and the bookkeeping, not only on which particles exist. The series' own choice of bookkeeping is the one that keeps the cancellation, provided the Higgs fields couple to curvature in the special conformal way.

## one-liner
Under the Gupta-Bleuler form of the Krein premise, the unphysical quartet of a gauge vector drops level by level from the induced Einstein-Hilbert coefficient under an energy cut-off on the Einstein static field, but under a heat-kernel cut-off on the gauge-fixed operators the vector's weight is $\alpha - 5$ ($-4$ only at the Gupta-Bleuler value $\alpha = 1$), so the series' content induces $12(\alpha - 1) + 8(1 - 6\xi_{R})$ minimal-scalar units under the covariant cut-off and $8(1 - 6\xi_{R})$ under the energy cut-off.
