---
id: synthesis.killing-horizon-value-factor-is-the-generator-boost
kind: claim
version: 2
title: 'At a Killing horizon the value factor is the generator boost'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, rotors-and-stabilisers, car-algebra]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof of (iv): the PG rotation-gauge field solved from the torsion equation for general beta'
  version: 2
  source: maintainer pass 2026-11-07 (consistency, GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review (referee F1): two citations in (iv) corrected'
  version: 2
  source: maintainer pass 2026-11-07 (consistency, GTG review)
review: draft
about:
- obj.hawking.continuum-mode-space
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-gtg-dictionary@2
  - field-theory.second-quantisation@6
  - synthesis.null-vacuum-on-a-horizon-generator@1
  - singularity.plane-rate@4
  - transport.group-null-rotations@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_killing_bivector_shape_on_the_horizon
- kind: check
  ref: check.py::check_canonical_block_is_the_generator_boost
- kind: check
  ref: check.py::check_closed_form_and_frame_independence
- kind: check
  ref: check.py::check_pg_rotation_field_on_the_killing_line
- kind: check
  ref: check.py::check_value_factor_and_transport_compose_to_the_dilation
- kind: check
  ref: check.py::check_gtg_pg_torsion_equation_and_killing_line
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.boost-evolution-on-generators-is-one-unitary-group
  - note.decisions.two-boost-flows
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (fix round): synthesis.imported-gtg-dictionary repinned 1 -> 2 after reviewing its correction of the component reading in clause (iv) to R(g_mu ^ g_nu) = -R(e_mu ^ e_nu), agreeing with the store''s sign, with GA wording in (ii) and (iv); this result cites (ii) for the parallel spin frame (dU/dt = -Omega U/2), whose content is unchanged (only the component reading moved into a parenthesis), so the use holds as cited.'
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee F1 fixes 7.1 and 7.2 applied (citations): the physical frame vectors of the label directions are now stated as the field''s definition through the frame g_mu = hb^{-1}(e_mu) of Definition obj.synthesis.gtg-flat-spacetime-gauge-fields(a) (clause (d), cited before, is the derived metric), and the frame torsion equation is attributed to Definition (f), D ^ hb^T(a) = hb^T(grad ^ a) applied to a = f^a with D = sum_b gamma^b D_{hb(gamma_b)} (Fact synthesis.imported-gtg-dictionary(ii), cited before, is the Levi-Civita derivative and transport). Fixer check: D ^ gamma^a = sum_b gamma^b ^ (omega(gamma_b) . gamma^a) for constant gamma^a, so the displayed equation is (f) on the physical frame. Pins: synthesis.imported-gtg-dictionary 1 -> 2 (see maintainer_pass_pin_review), field-theory.second-quantisation 5 -> 6 (unit named, notation), transport.group-null-rotations 4 -> 5 (formal unchanged).'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Items A6 and D2 (DECISIONS, Leon''s answer 1). A6 (restatement): (iv) now says beta = +sqrt(1 - f) and that -H is the de Sitter value in this chart, which contains the past cosmological horizon (the expanding chart gives +H on the future one); (iii) says future and past horizons; proof (iv) likewise, with (K . D) K = beta(r_h) f''(r_h)/2 K. Evidence: check_gtg_pg_torsion_equation_and_killing_line computes (K . D) K exactly in the PG fields beta = +sqrt(2/r), +2r/3 and -2r/3 at their horizons: 1/4, -2/3 and +2/3. D2 (routine): the pins on synthesis.boost-evolution-on-generators-is-one-unitary-group@4, synthesis.affine-cell-boost-spreads-without-scrambling@3 and synthesis.positive-null-energy-gives-r-premises@7 replaced by synthesis.null-vacuum-on-a-horizon-generator@1, whose clause (i) (the weight-1/2 dilation, premise-free) is what (iii) used; the other two are now text mentions without an edge; check.py calls premise() on the new pin in the two functions that called the old ones, and runcheck passes.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Clause (iv) of the proof rewritten in Gauge Theory Gravity: for hb(a) = a - beta (a.e_t) e_r with beta(r) general, the coframe vectors f^a with hb^T(f^a) = gamma^a and the torsion equation hb^T(grad ^ f^a) = sum_b gamma^b ^ (omega(gamma_b) . gamma^a) on the constant physical frame, solved by omega(gamma_0) = 0, omega(gamma_1) = -beta'' sigma_r, omega(gamma_2) = (beta gamma_0 + gamma_1) ^ gamma_2 / r, omega(gamma_3) = (beta gamma_0 + gamma_1) ^ gamma_3 / r + (cot/r) gamma_2 ^ gamma_3, so Omega(e_t) = -beta beta'' sigma_r = (f''/2) sigma_r; the Cartan forms kept as a labelled reading with their old check. Clauses (i)-(iii) were already in GA (omega in the statement is a physical vector orthogonal to k and m, named the rotation one-form). Original proof kept as orig-proof-main.tex. New exact check check_gtg_pg_torsion_equation_and_killing_line (both sides of the torsion equation from the coframe jets at three points with independent rational beta, beta'', r and angle, agreement with the engine''s field, a perturbed radial coefficient failing, Omega(e_t) and K = hb^{-1}(e_t)). outside_ga withdrawn: no stand-in remains.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The result is stated for every rotation one-form omega of a frame along the horizon generators; the one-form is the frame connection evaluated on the generator, and the statement quantifies over it in that language.'
  open_problem: op.which-boost-flow-is-time
  note: >-
    The follow-up left by the problem's settlement: clause (vi) of
    synthesis.boost-evolution-on-generators-is-one-unitary-group states that at Killing horizons the value
    factor of the boost evolution is the frame boost along the generator only as argued where the field
    strength is nonzero. This derives it, for every Killing horizon with nonzero surface gravity, rotating ones
    included, and instantiates it exactly for the static spherically symmetric class (Schwarzschild, de Sitter,
    Schwarzschild-de Sitter) in Painleve-Gullstrand gauge. Transport-convenient: the value factor is the
    rotor of parallel transport along the Killing orbit relative to the Killing-dragged frame. Standard
    content (not new): the shape of the Killing bivector on a Killing horizon, the surface gravity times the
    binormal plus a null rotation built from the horizon's rotation one-form (the rotation one-form of
    isolated-horizon geometry, Ashtekar and coworkers, cited from memory), with the vanishing of the second
    fundamental form and the parallelism of the Killing bivector along the orbit (both proved in the text from
    the Killing antisymmetry), and the Painleve-Gullstrand connection forms (computed exactly in the check).
    What is new is short: the canonical projector annihilates the generator from the right,
    Lambda(m) k = 0, so it sees only the boost weight of that bivector, the rotation one-form drops out of the
    canonical block and no transverse rotation (helicity phase) occurs; with it, the identification argued in
    clause (vi) of the continuum result is derived. Excluded: degenerate (extremal) horizons, kappa = 0, and
    the bifurcation surface itself.
---
## formal
Work on flat spacetime with gravity the gauge fields $(\hb, \Omega)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with the store's signature. Let $K$ be a Killing vector field of $(\hb, \Omega)$ in the sense of Fact \claimref{synthesis.imported-gtg-dictionary}(vi), with Killing bivector $F_{K} = \tfrac12 D \wedge K$, so that $(A\cdot D)K = A\cdot F_{K}$, and let $\mathcal{H}$ be a Killing horizon of $K$: a null hypersurface on which $K$ is normal, $Q(K) = 0$, with surface gravity $\kappa \ne 0$, $(K\cdot D)K = \kappa K$. At a point of $\mathcal{H}$ off its bifurcation surface write $K = \phi\,k$ with $k$ the physical generator direction, let $m$ be the null vector with $\ip{k}{m} = 1$ in the plane of $k$ and the frame vector $\gamma_{0}$, and $\Lambda(a) = a\gamma_{0}/(2a_{0})$ (Proposition \claimref{field-theory.second-quantisation}(1)), so that $\Lambda(m)$ projects onto the canonical light-ray component of a spinor field on the generator's null plane and $\Lambda(k) = 1 - \Lambda(m)$ onto the constrained one (as in synthesis.boost-evolution-on-generators-is-one-unitary-group, clause (i)).
\begin{enumerate}
\item[(i)] \emph{(Shape of the Killing bivector.)} For all physical vectors $X, Y$ tangent to $\mathcal{H}$, $Y\cdot(X\cdot F_{K}) = 0$. The bivectors with this property are exactly $\mathrm{span}\{k\wedge m,\ k\wedge a,\ k\wedge b\}$ ($a, b$ spanning the plane orthogonal to $k$ and $m$), and the surface-gravity condition fixes the first coefficient: on $\mathcal{H}$
\[
F_{K} = -\kappa\,k\wedge m + k\wedge\omega, \qquad \omega \perp k, m ,
\]
with $\omega$ the horizon's rotation one-form (zero for the static spherically symmetric class). No transverse rotation $a\wedge b$ and no $m\wedge a$, $m\wedge b$ occur. $F_{K}^{2} = \kappa^{2}$, so $F_{K}/\kappa$ is the unit boost bivector of a plane through $k$.
\item[(ii)] \emph{(The value factor.)} $F_{K}$ is parallel along the orbits of $K$, and relative to frames parallel along a generator, a field invariant under the Killing flow has values $\psi(t) = R_{t}\psi(0)$ with $R_{t} = \exp(-tF_{K}/2) = \cosh\tfrac{\kappa t}{2} - \sinh\tfrac{\kappa t}{2}\,F_{K}/\kappa$, the flow advancing the generator's affine parameter as $u \mapsto e^{\kappa t}u$ ($R_{t}kR_{t}^{\sim} = e^{\kappa t}k$). Since $\Lambda(m)k = 0$ and $\Lambda(m)(k\wedge m) = -\Lambda(m)$,
\[
\Lambda(m)F_{K} = \kappa\,\Lambda(m), \qquad \Lambda(m)R_{t} = e^{-\kappa t/2}\Lambda(m), \qquad kR_{t} = e^{-\kappa t/2}k ,
\]
for every rotation one-form $\omega$: on the canonical component the value factor is exactly the boost $B_{\kappa t}$ of the generator plane (the boost of synthesis.boost-evolution-on-generators-is-one-unitary-group, clause (ii)), and the intrinsic canonical data $k\psi$ (which do not depend on the choice of $m$) scale the same way. The null-rotation part $k\wedge\omega$ maps the canonical range into the constrained one and never back.
\item[(iii)] \emph{(Composition.)} With the transport $u \mapsto e^{\kappa t}u$ the value factor $e^{-\kappa t/2}$ preserves the canonical delta kernel, so the Killing flow on the generators' continuum is the unitary dilation group $\alpha_{\kappa t}$, the weight-$\tfrac12$ dilation of Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(i), for either sign of $\kappa$ (future and past horizons), with no additional phase on the two chirality channels; the argued step of clause (vi) of synthesis.boost-evolution-on-generators-is-one-unitary-group holds as stated.
\item[(iv)] \emph{(The static spherically symmetric class.)} For $\hb(a) = a - \beta\,(a\cdot e_{t})\,e_{r}$ with $\beta = +\sqrt{1 - f}$ (Painleve-Gullstrand gauge), the rotation-gauge field along the Killing vector $K = \hb^{-1}(e_{t})$ is $\Omega(e_{t}) = -\beta\beta'\,\sigma_{r} = \tfrac{f'}{2}\sigma_{r}$, $\sigma_{r} = e_{r}e_{t}$, with no angular part, at every radius; at a horizon $f(r_{h}) = 0$ the $t$-line is a null generator with $k = e_{t} + \beta e_{r}$, $\sigma_{r} = k\wedge m$, $\omega = 0$ and $\kappa = f'(r_{h})/2$: $1/4M$ for Schwarzschild (the stored rate of Proposition \claimref{singularity.plane-rate}), $-H$ for de Sitter in this chart, which contains the past cosmological horizon (the expanding chart gives $+H$ on the future one), and $\tfrac27$, $-\tfrac{5}{28}$ for the Schwarzschild-de Sitter field with horizons at $r = 1, 2$ ($H^{2} = \tfrac17$, $M = \tfrac37$).
\end{enumerate}
So the boost time evolution of a Killing horizon's generators is one unitary dilation group in every field strength: its value factor is a theorem, not an identification, and rotation of the horizon does not change it on the canonical component.

## technical
The stored result on the continuum of a horizon's generators found that the boost time evolution is one unitary dilation: the boost rotor acts on the canonical component of the spinor field with weight $e^{-\lambda/2}$ and the same rotor moves the points of the generator, and only the product preserves the anticommutator. At a Killing horizon in a gravitational field of nonzero field strength the transport of the affine parameter was known, but that the factor on values is the boost of the generator plane was argued.

This proves it. On a Killing horizon the covariant derivative of the Killing vector, the Killing bivector, is antisymmetric (the Killing property) and, restricted to the horizon, symmetric (it is the derivative of a normal field of a hypersurface); so it vanishes on pairs of tangent vectors, which leaves only three bivectors: the boost of the generator plane, with coefficient fixed by the surface gravity, and two null rotations about the generator, whose coefficients form the horizon's rotation one-form. Relative to frames parallel along the generator, the Killing flow turns the field's values by the rotor generated by this bivector. The canonical projector annihilates the generator from the right, so it sees the boost with weight $e^{-\kappa t/2}$ and does not see the null rotations at all. Combined with the stretching of the affine parameter this is again the unitary dilation. The Painleve-Gullstrand form of the static fields gives the rotation-gauge field along the Killing line as $f'/2$ times the radial boost, $\kappa$ at the horizon with $\beta = +\sqrt{1 - f}$, computed exactly from the torsion equation.

## lay
On a black hole's horizon, or the horizon of an expanding universe, the flow of time slides each light ray along itself and, at the same time, turns the values of matter fields riding on it. An earlier result showed that these two effects together make one well-behaved time evolution, provided the turning is a particular stretch, the one that matches the sliding; that was shown where gravity is absent and only argued at real horizons. Here it is shown at every horizon of this type, including those of spinning holes: the spin adds a twist, but the twist touches only the part of the field that is not free data on the light ray, so the free part evolves exactly as before.

## one-liner
At every Killing horizon with nonzero surface gravity, off its bifurcation surface, whatever the field strength and with or without rotation, the Killing bivector is $-\kappa\,k\wedge m + k\wedge\omega$, so relative to parallel frames the Killing flow acts on the canonical light-ray component by the generator-plane boost with weight $e^{-\kappa t/2}$, the rotation one-form reaching only the constrained component: the value factor of the boost time evolution is derived, not argued.
