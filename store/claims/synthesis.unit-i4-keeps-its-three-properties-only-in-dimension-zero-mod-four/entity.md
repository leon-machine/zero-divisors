---
id: synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four
kind: claim
version: 3
title: 'The unit $I_4$ keeps its properties only in dimension 0 mod 4'
status: proved
region: synthesis
subject: quantum-fields
tags: [pseudoscalar-and-centre, clifford-classification, chirality, no-go, classification]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the unit named as I_4 in place of ''i = I_4'' (wording)'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
review: draft
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  - primer.sign@3
  - std-algebra.pseudoscalar-commutation@1
  - synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_bivector_commutant_is_span_of_one_and_pseudoscalar
- kind: check
  ref: check.py::check_pseudoscalar_square_has_period_four
- kind: check
  ref: check.py::check_three_properties_only_when_dimension_is_zero_mod_four
- kind: check
  ref: check.py::check_four_dimensional_unit_inside_higher_dimensions
- kind: check
  ref: check.py::check_left_and_right_unit_differ_exactly_on_mixed_blades
- kind: check
  ref: check.py::check_tower_plane_generators_commute_with_the_unit
- kind: check
  ref: check.py::check_signature_dependence_of_the_odd_dimension_clauses
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.second-quantisation
  - field-theory.elementary-photon-ga
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit naming (DECISIONS H1, R06 item 1): ''with $i = I_4$'' identified a bare i with the unit, which the unit principle treats as a bare unit; the levels and proofs now name the unit (''with the unit $I_4$'', ''the field theory''s unit $I_4$''). Mechanical; no content change.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s list of imports of 2026-11-01: uses edges to the stored standard results primer.sign@2 (the square of the pseudoscalar) and std-algebra.pseudoscalar-commutation@1 (how it commutes), which carry the classification facts cited from memory (Lounesto, Porteous) in place of an import, and to the imported Fact synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5@1 (dimensional regularisation and the BMHV gamma_5), which replaces the citation of the regularisation literature from memory. Statement and check unchanged.'
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    The problem asks for one-loop quantities with a stated regulator, or the input the formalism lacks.
    Dimensional regularisation continues the Clifford algebra to D dimensions; this result asks what
    becomes of the series' imaginary unit there. In D = 4, I4 squares to -1, commutes with every bivector
    (so left multiplication by it commutes with the Lorentz rotors) and anticommutes with every vector (so
    left and right multiplication by it agree on even values). The classification facts are standard (the
    centre and the pseudoscalar square of a Clifford algebra; stored as primer.sign and
    std-algebra.pseudoscalar-commutation; Lounesto, Porteous); the
    content here is reading them as constraints on the unit. The bivector commutant of Cl(1, D-1) is
    span{1, I_D}; in the series' signature (1, D-1), I_D squares to -1 exactly for D = 0, 3 mod 4 (in the
    signature (D-1, 1) for D = 0, 1 mod 4); in both signatures all three properties hold together exactly
    for D = 0 mod 4, and in the signature (1, D-1) in D = 5, 6 not even the first two. The four-dimensional I4
    inside Cl(1, D-1) is the Breitenlohner-Maison-'t Hooft-Veltman gamma5 (anticommutes with the four,
    commutes with the extra generators; checked against arXiv:2004.14398, eq. 2.10): it anticommutes with
    the 4(D - 4) mixed bivectors. Right multiplication by I4 continues as a Lorentz-covariant unit but
    differs from left multiplication on the even blades with an odd number of four-dimensional indices.
    The tower's adjoined planes commute with I4 as the evanescent generators do. The continuation statement
    is proved for the integer-dimensional algebras only; for the formal non-integer dimension of dimensional
    regularisation it is the known gamma5 obstruction. Consequence (argued):
    vector-like loops can keep the unit as a right unit, as the standard scheme keeps an external i, so
    dimensional regularisation of one-loop QED needs no new input; for chiral couplings the series'
    identification of the unit with the element that anticommutes with vectors fails on the evanescent
    blades exactly as gamma5 does in that scheme, so chiral loops inherit its symmetry-restoring
    counterterms; four-dimensional regulators (Pauli-Villars, the lattice, Epstein-Glaser extension of
    distributions, and the tower's floors, which are not Lorentz covariant) need no continuation of the
    unit. The one-loop QED result (synthesis.one-loop-qed-in-the-spacetime-algebra) puts the
    unit outside the Clifford product on massive lines, which is the right unit of clause (v). The regularisation literature is imported
    (synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5). Transport-absent: Clifford algebra and the convention i = I4.
---

## formal
Let $\Cl(1, D-1)$ have orthogonal generators $g_0, \ldots, g_{D-1}$ with $Q(g_0) = 1$ and $Q(g_a) = -1$ for $a \ge 1$, $I_D = g_0g_1\cdots g_{D-1}$ and $I_4 = g_0g_1g_2g_3$, and write $\hat{x}$ for the grade involution. For $D = 4$ the unit $I_4$ of Definition \claimref{obj.field-theory.single-algebra-field} has three properties: (a) $I_4^2 = -1$; (b) $I_4$ commutes with every bivector, so left multiplication by it commutes with every rotor; (c) $I_4$ anticommutes with every vector, so $I_4x = \hat{x}I_4$ for all $x$ and left and right multiplication by $I_4$ agree on even elements.
\begin{enumerate}
\item[(i)] For $D \ge 3$ the elements of $\Cl(1, D-1)$ commuting with every bivector are exactly $\mathrm{span}\{1, I_D\}$.
\item[(ii)] In the signature $(1, D-1)$, $I_D^2 = (-1)^{D(D-1)/2 + D - 1}$, which is $-1$ exactly when $D \equiv 0$ or $3 \pmod 4$. (In the signature $(D-1, 1)$ it is $-1$ exactly when $D \equiv 0$ or $1 \pmod 4$.)
\item[(iii)] An element of $\Cl(1, D-1)$ with (a), (b) and (c) exists if and only if $D \equiv 0 \pmod 4$, and it is then $\pm I_D$; the same holds in $\Cl(D-1, 1)$. In the signature $(1, D-1)$, for $D = 5, 6$ no element has (a) and (b), and for $D = 7$ the only elements with (a) and (b), $\pm I_7$, commute with every vector. (In the signature $(D-1, 1)$, $\pm I_5$ have (a) and (b) and fail only (c).)
\item[(iv)] For $D > 4$, $I_4$ still has (a), anticommutes with $g_0, \ldots, g_3$, commutes with $g_4, \ldots, g_{D-1}$, and anticommutes with exactly the $4(D-4)$ mixed bivector blades $g_{\mu}g_{a}$ ($\mu \le 3 < a$), commuting with the others: left multiplication by $I_4$ does not commute with the rotors of the mixed planes.
\item[(v)] Right multiplication by $I_4$ squares to $-1$ and commutes with every left multiplication, rotors and vectors included. On an even blade, left and right multiplication by $I_4$ agree when the blade has an even number of indices in $\{0, 1, 2, 3\}$ and are opposite otherwise; for $D > 4$ they differ on $2^{D-2}$ of the $2^{D-1}$ even blades.
\item[(vi)] On the ground with one adjoined plane of Fact \claimref{field-theory.imported-tower-limit}, $I_4$ commutes with the plane's null generators $v$, $w$ and anticommutes with every $g_{\mu}v$ and $g_{\mu}w$.
\end{enumerate}
Clauses (i) to (iii) are standard classification facts about the centre and the pseudoscalar of a Clifford algebra (\claimref{primer.sign}, \claimref{std-algebra.pseudoscalar-commutation}), read here as constraints on the unit. So no algebra $\Cl(1, D-1)$ with $4 < D < 8$ keeps all three properties of the unit, and a continuation through the integer-dimensional algebras must give up (b), as the four-dimensional $I_4$ of (iv) does, or (c), as the right unit of (v) does.

## technical
In the spacetime algebra the series' imaginary unit $I_4$ squares to $-1$, commutes with every bivector, so with the Lorentz rotors acting on the left, and anticommutes with every vector, so that left and right multiplication by it agree on even field values. Dimensional regularisation continues the Clifford algebra in the dimension; in the integer-dimensional algebras $\Cl(1, D-1)$ the elements commuting with all bivectors are $\mathrm{span}\{1, I_D\}$, and $I_D^2 = (-1)^{D(D-1)/2 + D - 1}$ is $-1$ only for $D \equiv 0, 3 \pmod 4$ (standard classification facts, read here as constraints on the unit). So the three properties hold together exactly when $D \equiv 0 \pmod 4$, with $\pm I_D$ the only such elements, in this signature and in the mostly-plus one; in the series' signature $(1, D-1)$, for $D = 5, 6$ no element even squares to $-1$ and commutes with the rotors, while in the signature $(D-1, 1)$ the five-dimensional $\pm I_5$ do and fail only the anticommutation with vectors.

The two available continuations each give up one property. The four-dimensional $I_4$ inside $\Cl(1, D-1)$ squares to $-1$, anticommutes with the four original generators and commutes with the extra ones, which is the $\gamma_5$ of the Breitenlohner-Maison and 't Hooft-Veltman scheme; it anticommutes with the $4(D-4)$ mixed bivectors, so it is not covariant under rotations in the mixed planes. Right multiplication by $I_4$ commutes with every left action, so it is covariant, but it no longer anticommutes with vectors: it disagrees with left multiplication exactly on the even blades with an odd number of four-dimensional indices, $2^{D-2}$ of the $2^{D-1}$ even blades for $D > 4$. The tower's adjoined plane generators commute with $I_4$, as the extra generators of that scheme do. These statements concern the integer-dimensional algebras; for the formal non-integer dimension of the scheme the same split is the known $\gamma_5$ obstruction.

## lay
In this framework the imaginary number of quantum theory is the four-dimensional volume element of the spacetime algebra. The most common way of taming the infinities of quantum field theory pretends that spacetime has a slightly different number of dimensions. In the algebras of whole-number dimensions near four, this result shows that the volume element loses one of its three defining properties: it either stops respecting rotations that mix the old and new directions, or stops behaving oppositely to directions as it does in four dimensions. All three properties return only in dimensions four, eight, twelve and so on. The same split is the known difficulty with the chirality matrix in that method, here met by the imaginary unit itself.

## one-liner
In $\Cl(1, D-1)$, the series' signature, the bivector commutant is $\mathrm{span}\{1, I_D\}$ and $I_D^2 = -1$ only for $D \equiv 0, 3 \pmod 4$, so $I_4$'s three properties ($I_4^2 = -1$, commuting with rotors, anticommuting with vectors) hold together only for $D \equiv 0 \pmod 4$; for $D > 4$ the four-dimensional $I_4$ breaks covariance in the $4(D-4)$ mixed planes and the right unit $x \mapsto xI_4$ differs from the left on $2^{D-2}$ even blades.
