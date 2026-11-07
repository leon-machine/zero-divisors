---
id: synthesis.unit-boost-residue-needs-nonpositive-exponent
kind: claim
version: 4
title: 'A unit-boost Kasner residue needs a nonpositive exponent'
status: proved
region: synthesis
subject: interior
tags: [kasner, no-go]
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
  role: GA rewrite (Kasner-scalar field equations with the Ricci map and the physical gradient)
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-datum-kasner-wall@7
  - dark-energy.forcing-half-schwarzschild-wall-residue-sense@4
  - synthesis.diagonal-kasner-momentum-constraint@3
  assumes: []
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_residue_square_is_sum_of_squares
- kind: check
  ref: check.py::check_circle_has_nonpositive_entry
- kind: check
  ref: check.py::check_positive_exponents_not_unit
- kind: check
  ref: check.py::check_scalar_kasner_relations
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-energy.forcing-half-schwarzschild-wall-residue-sense
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Line element and index tensors to GA in (3): the ansatz is the synchronous gauge field hb^{-1}(e_0) = e_0, hb^{-1}(e_i) = tau^{p_i} e_i with its derived metric as a labelled reading, the kinetic term is Q(hb^T(grad phi))/2; in the proof the Ricci tensor becomes the Ricci map, the Einstein equation calR(a) = -8 pi G (T(a) - (d_b . T(b)) a/2), the scalar stress the map a -> (a . hat-grad phi) hat-grad phi with hat-grad phi = hb^T(grad phi) = (q/tau) e_0, and the wave equation D . hat-grad phi = 0; components stay as labelled readings. A notation change through the dictionary (R_ab = g_a . calR(g_b)); the Ricci map values are the ones checked exactly for dark-energy.frozen-point-datum-kasner-wall. Statement unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG sign (Leon 2026-10-23, referee GR1): B_w = sum_i p_i B_i is kept; the residue of the Kasner pole in the sign of the rotation-gauge field is -B_w, with the same square, so every clause is unchanged (DICTIONARY C10). Check unchanged apart from its docstring. Version 2 -> 3.'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the one-liner now says at leading order in tau for the Einstein-scalar clause, as the formal statement does, and separates it from the exact all-positive clause. Version 1 -> 2.'
  open_problem: op.forcing-half-beyond-diagonal
  note: >-
    An obstruction to extending the residue-sense forcing half, in its unit-boost form, beyond the
    vacuum Kasner class. The exact content is elementary: the residue bivector squares to the sum of
    squared exponents, which is 1 only on the Kasner circle, where some exponent is nonpositive; with
    all exponents positive, or with a massless scalar carrying a logarithmic rate, it is a boost of norm
    below one. The reason it matters is argued in the technical level with literature cited from memory:
    nonpositive exponents are the ones that trigger BKL bounces in generic vacuum data, and the
    matter that makes singularities quiescent (a massless scalar) does so by moving the exponents into
    the positive region, off the unit-boost circle. Transport-convenient: it concerns whether the
    completion's unit-boost weights can match the field equations' residues.
---

## formal
Let $p = (p_1, p_2, p_3) \in \R^3$ with $\sum_i p_i = 1$, and let $B_w = \sum_i p_i B_i$ with $B_i = e_0 e_i$ in $\Cl(1,3)$; the residue bivector of the Kasner pole (\claimref{dark-energy.frozen-point-datum-kasner-wall}(i)), in the sign of the rotation-gauge field, is $-B_w$, which has the same square, so each statement below about $B_w$ holds for the residue.
\begin{enumerate}
\item $B_w^2 = \sum_i p_i^2$. So $B_w$ is a unit boost if and only if $p$ lies on the Kasner circle, which is the second Kasner relation of \claimref{dark-energy.frozen-point-datum-kasner-wall}(ii).
\item On the Kasner circle some exponent is nonpositive, and an exponent vanishes only at the permutations of $(1,0,0)$. Equivalently, if every $p_i > 0$ then $B_w^2 = 1 - 2\sum_{i<j}p_ip_j < 1$.
\item On the synchronous diagonal Kasner field $\hb^{-1}(e_0) = e_0$, $\hb^{-1}(e_i) = \tau^{p_i}e_i$ on flat spacetime (derived metric, in components, $d\tau^2 - \sum_i \tau^{2p_i}(dx^i)^2$) coupled to a massless scalar $\phi = q\log\tau$, at leading order in $\tau$, the Einstein-scalar equations hold if and only if $\sum_i p_i = 1$ and $\sum_i p_i^2 = 1 - 8\pi G q^2$ (the scalar's kinetic term normalised as $\tfrac12 Q(\hb^{T}(\nabla\phi))$, in components $\tfrac12(\partial\phi)^2$), the wave equation then holding exactly. Hence $B_w^2 = 1 - 8\pi G q^2$: the residue is a unit boost exactly when the scalar carries no logarithmic rate.
\end{enumerate}
So the identification of step (2) of \claimref{dark-energy.forcing-half-schwarzschild-wall-residue-sense}, field equations at the wall equal to a unit-boost residue, holds only on vacuum walls, and every such wall has an exponent $p_i \leq 0$.

## technical
The residue-sense forcing half reads the leading field equations at a Kasner wall as the statement that the residue of the connection's pole is a unit boost, which is what makes it the completion's weight. This result shows how narrow that reading is. The ingredients are standard and not new: the Kasner relations and the fact that one exponent on the Kasner circle is nonpositive (Kasner 1921; Landau and Lifshitz, vol.~2), and the Kasner disk of a massless scalar, sum of squares $1 - 8\pi G q^2$ (Belinski and Khalatnikov 1973), all cited from memory. What is added is their bearing on the store's reading: the residue squares to the sum of the squared exponents, so it is a unit boost only on the vacuum circle, where an exponent is nonpositive, and with a scalar of nonzero log-rate it is a boost of norm below one. Read against the literature (cited from memory, not imported into the store): the nonpositive exponent is exactly what destabilises a Kasner regime in generic vacuum data (Belinski, Khalatnikov and Lifshitz; Ringström's theorem for Bianchi IX), so beyond special classes such as Fournodavlos and Luk's no limiting residue exists; and the massless scalar is what makes singularities quiescent (Andersson and Rendall, 2001), precisely by allowing all exponents positive, which by (2) cannot be a unit boost. So, argued from the literature and not proved here, a generic non-diagonal extension of the forcing half cannot keep the unit-boost form: either no residue exists, or it is not a unit boost. Filed alongside, synthesis.nondiagonal-kasner-residue-weighted-shear places the residues of the non-diagonal class on the Kasner circle under the hypothesis that the slices' curvature is subleading; by (2) such a residue has an exponent $\leq 0$, the case in which that hypothesis generically fails (argued).

## lay
Near a singularity of the Kasner type the geometry stretches in some directions and squeezes in others, at rates given by three exponents. The series showed that, in empty space, Einstein's equations make the singular part of the geometry a pure boost of unit size, and that this is exactly the input its completion needs. This result points out how special that is. The unit size requires one direction that does not stretch, which is also what makes empty-space singularities oscillate chaotically in general. Adding a simple kind of matter calms the oscillations, but then the boost is shorter than one. So the neat match the series found does not extend unchanged to generic singularities.

## one-liner
The Kasner residue bivector squares to $\sum_i p_i^2$, so it is a unit boost only on the vacuum Kasner circle, where some exponent is nonpositive; with all exponents positive it is a boost of norm squared below $1$, and with a massless scalar of log-rate $q$, at leading order in $\tau$, of norm squared $1 - 8\pi G q^2 < 1$.
