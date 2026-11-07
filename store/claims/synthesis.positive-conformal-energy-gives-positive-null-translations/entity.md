---
id: synthesis.positive-conformal-energy-gives-positive-null-translations
kind: claim
version: 7
title: 'Positive conformal energy gives positive null translations'
status: proved
region: synthesis
subject: conformal-spacetime
tags: [conformal-spinors, thermal-premises, modular-theory, horizons, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 6
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 7
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.positive-energy-selects-rule-2-sign@4
  - mass.chart-form-spin-isomorphism@6
  - angle.imported-theorems-deliver-their-hypotheses@3
  - std-algebra.bivector-exponential@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_central_rotation_contains_time_translation
- kind: check
  ref: check.py::check_boost_orbit_reaches_null_translations
- kind: check
  ref: check.py::check_controls_spacelike_past_and_wedge_reflection
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - note.singularity.cost-r-dictionary
  - field-theory.twistor-attachment
  - synthesis.c-loc-local-horizon-premise
  - synthesis.point-spectrum-boost-admits-no-half-sided-translations
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6 -> 7. The self-adjoint generators -i d pi(Y) of an arbitrary unitary representation on a GNS Hilbert space: by U1 the scalars of an abstract complex Hilbert space are span{1, I_4}, so the generators are -I_4 d pi(Y) (the formal level and every occurrence in the proof), with a sentence fixing the scalars. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the hypothesis is an arbitrary continuous unitary representation of Spin+(2,4) on a GNS Hilbert space, and -i d pi(Y) is its self-adjoint generator; the store does not tie that space''s complex structure to I_4.'
  maintainer_pass_2:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.bivector-exponential where the proof uses them. Version 4 -> 5.'
  maintainer_pass:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge-independent wording: ''a gravitational field of nonvanishing field strength'' in place of ''a nonvanishing gravitational field'' (referee 4, 2026-10-24). Version 3 -> 4.'
  restatement_2026_10_24:
    by: ai-run-2026-10-24-crossovers
    date: '2026-10-24'
    note: 'Scope sentences restated in Gauge Theory Gravity at Leon''s request: Minkowski space is flat spacetime with vanishing gravitational field; the Schwarzschild exclusion is a property of the gauge field (field strength pure, nonzero Weyl, so no gauge makes it a pure dilation of the background), not of a curved spacetime; the de Sitter field is the pure dilation hb = sigma. Statements (i), (ii), the check and the title unchanged. Version 2 -> 3.'
  correction_2026_10_24:
    by: ai-run-2026-10-24-crossovers
    date: '2026-10-24'
    note: 'Clause (iii) narrowed: it said the affine translations along a de Sitter horizon are not conformal transformations of Minkowski space; they are (the result filed alongside), so the de Sitter case is reached and only Schwarzschild is not. The same sentence corrected in the proof, the technical level, the lay level and the one-liner. Statement (i) and (ii) and the check unchanged. Version 1 -> 2.'
  open_problem: op.derive-loc-and-r-loc
  note: >-
    Clause (R_loc) of the local-horizon premise, read on the continuum: a companion result filed alongside
    reduces (R_loc), (R) and (R_Lambda) to one ground-state condition for the null translations along a
    horizon's generators (positive generator, invariant state). This result supplies the positivity half of
    that condition from the series' own algebra: the stored remark on what (R) costs proposed restating (R) as
    positivity of energy for a generator the ascent installs, and here positivity of the conformal energy Z,
    the generator the ascent to Cl(2,4) singles out (the centre of the maximal compact subalgebra), is shown to
    force a nonnegative generator for every future translation, null ones included. The argument is the
    closed-cone limit along the dilation and boost orbits, each step an exact identity in Cl(2,4); the only
    analytic input is that the nonnegative generators of a unitary representation form a closed convex
    invariant cone (standard, cited from memory with its one-line proof). What remains of the local thermal
    condition is that the state be invariant under the translations (the vacuum), a state premise with no
    thermal content. Transport-absent apart from its Cl(2,4) form: it is the standard equivalence of positive conformal energy and the spectrum condition, written in the ascent's conformal model; its scope is Minkowski space.
    Literature cited from memory: Segal and Paneitz on invariant cones of generators (the cone property), and,
    for the remark only, that positive conformal energy implies the Poincare spectrum condition (Mack 1977,
    Luscher and Mack 1975), which this result proves inside the conformal model.
---

## formal
Work in $\Cl(2,4)$ with orthonormal $e_{0}$ ($e_{0}^{2} = 1$), $e_{1}, e_{2}, e_{3}$ (square $-1$), $\nu$ ($\nu^{2} = 1$) and $e_{-}$ ($e_{-}^{2} = -1$); put $\nInf = \nu + e_{-}$, $\nO = \tfrac12(\nu - e_{-})$, so $\ip{\nO}{\nInf} = 1$, and $X(x) = \nO + x - \tfrac12 Q(x)\nInf$ for $x \in \R^{1,3}$, the chart of Lemma \claimref{mass.chart-form-spin-isomorphism}. Let $Z = e_{0}\nu$, which spans the centre of the maximal compact subalgebra of $\so(2,4)$ (Proposition \claimref{synthesis.positive-energy-selects-rule-2-sign}(i)), and for $a \in \R^{1,3}$ let $P_{a} = \tfrac12 a\nInf$, so that $\exp(tP_{a}) = 1 + tP_{a}$ maps $X(x)$ to $X(x + ta)$. Let $\pi$ be a continuous unitary representation of $\mathrm{Spin}^{+}(2,4)$ (for a field, on the GNS space of its state, not on a one-particle space such as $L^{2}(\R, du)$, where the null momentum takes both signs), and $C_{\pi}$ the set of Lie algebra elements $Y$ with $-I_{4}\,d\pi(Y) \ge 0$, the Hilbert space's scalars read in $\mathrm{span}\{1, I_{4}\}$, the default scalar field of an abstract complex Hilbert space.
\begin{enumerate}
\item[(i)] \emph{(Orbit identities, exact.)} $Z^{2} = -1$ and $Z = P_{e_{0}} + e_{0}\nO$. For the dilation rotor $D_{\rho} = \tfrac12(\rho + \rho^{-1}) + \tfrac12(\rho - \rho^{-1})e_{-}\nu$, which maps $X(x)$ to $\rho^{-2}X(\rho^{2}x)$, $\rho^{-2}\,D_{\rho}Z\tilde D_{\rho} = P_{e_{0}} + \rho^{-4}e_{0}\nO$. For the boost rotor $B_{\rho} = \tfrac12(\rho + \rho^{-1}) + \tfrac12(\rho - \rho^{-1})e_{1}e_{0}$, $2\rho^{-2}\,B_{\rho}P_{e_{0}}\tilde B_{\rho} = P_{\ell} + \rho^{-4}P_{e_{0} - e_{1}}$ with $\ell = e_{0} + e_{1}$. Rotations fixing $e_{0}$ and $\nInf$ carry $P_{\ell}$ to $P_{e_{0} + \hat n}$ for every unit $\hat n$, and every $a$ in the closed forward cone is a nonnegative combination of two future null vectors. The $P_{a}$ commute.
\item[(ii)] \emph{(The cone.)} $C_{\pi}$ is a closed convex cone, invariant under the adjoint action. If $Z \in C_{\pi}$ (nonnegative conformal energy), then $P_{a} \in C_{\pi}$ for every $a$ in the closed forward cone: the joint spectrum of the translations lies in the closed forward cone, and for every future null $\ell$ the null translation $\exp(tP_{\ell})$ has a nonnegative generator. If $-Z \in C_{\pi}$, the same holds with the backward cone. A spacelike $P_{a}$ is conjugate to $-P_{a}$, so it lies in $C_{\pi}$ only if $d\pi(P_{a}) = 0$.
\item[(iii)] \emph{(The local horizons of Minkowski space.)} Hence, if $\pi$ acts on the GNS space of a state whose GNS vector is invariant under the translations (the vacuum of a field second-quantised over a positive-energy space), the null translations along the generators of every local Rindler horizon of Minkowski space have nonnegative generators and leave the state invariant: the state is a ground state for every such null translation, the positivity and invariance from which the result filed alongside, synthesis.positive-null-energy-gives-r-premises, derives joint KMS at rapidity period $2\pi$ on either side of the edge. No temperature, period or Euclidean section enters. Here Minkowski space is flat spacetime with vanishing gravitational field ($\hb = 1$, $\Omega = 0$; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). For the Schwarzschild gravitational field the background conformal transformations are not conformal symmetries of the field: its field strength is pure, nonzero Weyl, so no gauge makes it a pure dilation of the background (the result filed alongside, clause (vi)), and the positivity of the affine translations along its horizon's generators is not supplied by this result. For the de Sitter field $\hb = \sigma$, a pure dilation, they are: for $\Lambda > 0$ and $n$ null with $\ip{n}{I} = 0$, in the physical affine parameter whose physical tangent is $n$, the uniform translation is generated by a background null translation plus a background null special conformal transformation, which lies in $C_{\pi}$ by the orbit identities of (i) applied to $e_{0}\nO$; for conformally invariant fields this gives the positivity there (the result filed alongside, synthesis.de-sitter-horizon-translation-is-conformal-null-rotation).
\end{enumerate}

## technical
The series' boundary modes attach to spacetime through the conformal spinor space, whose one-particle spaces are positive-energy representations of the conformal group: the conformal energy is bounded below. The ascent to $\Cl(2,4)$ singles out one generator for that energy, the rotation $Z = e_{0}\nu$ of the plane of the two directions that square like time, which spans the centre of the maximal compact subalgebra. This result shows, by exact identities in $\Cl(2,4)$, that positivity of $Z$ in a unitary representation forces positivity of every future translation. Among these are the null translations along the generators of the local Rindler horizons of Minkowski space.

Conjugating $Z$ by the dilation and rescaling, the remainder $\rho^{-4}e_{0}\nO$ dies and the time translation $P_{e_{0}}$ is left. Conjugating that by a boost and rescaling leaves the null translation $P_{\ell}$. The generators with nonnegative spectrum in a unitary representation form a closed convex cone invariant under conjugation, so they contain every future translation once they contain $Z$. Spacelike translations are conjugate to their negatives and cannot lie in such a cone unless they act trivially. This is the standard equivalence of positive conformal energy and the spectrum condition (Segal; Mack 1977; L\"uscher and Mack 1975), proved here in the conformal model; it is transport-absent apart from its $\Cl(2,4)$ form.

The representation must act on the space where the state lives: for a field, the GNS (filled-sea) Fock space, on which the second-quantised generators are nonnegative when the one-particle ones are. It does not act on a one-particle space such as $L^{2}(\R, du)$ of a generator, where the null momentum takes both signs. For the vacuum of such a field the result supplies the positivity half of the ground-state condition used by the result filed alongside, synthesis.positive-null-energy-gives-r-premises. With it, (R$_{\mathrm{loc}}$) holds on the local Rindler horizons of Minkowski space in the continuum restatement given there. Its scope is flat spacetime with vanishing gravitational field. The result filed alongside, synthesis.de-sitter-horizon-translation-is-conformal-null-rotation, extends the positivity half to the cosmological horizons of the de Sitter gravitational field, a pure dilation of the flat background, for conformally invariant fields. For the Schwarzschild field, whose field strength is pure nonzero Weyl, the positivity of the affine null translations is part of the premise. For a gravitational field of nonvanishing field strength the local form of (R$_{\mathrm{loc}}$) needs the state to be, at leading order near the point, invariant under the local null translations, which is a condition on the state.

Remark (argued). The twistor attachment (Proposition \claimref{field-theory.twistor-attachment}) has conformal energies $|s| + 1 + n > 0$. That this energy is generated by $Z$ is the standard identification, which the stored rule-2 result argues and does not prove. That the series' boundary modes carry such a representation on their state's GNS space is likewise argued, not proved. Granting both, the attachment's fields satisfy the spectrum condition. They would then meet the hypotheses of the Bisognano-Wichmann theorem of Fact \claimref{angle.imported-theorems-deliver-their-hypotheses} if they are Wightman fields (temperedness, locality, finite-component fields), which is not shown here.

## lay
The series' quantum fields are built so that a particular kind of energy, the energy that goes with the symmetries of light cones, is never negative. This result shows, by exact algebra, that this one requirement forces the ordinary energy, and the momentum along every light ray of flat spacetime, to be non-negative too. It is a known result, here written in the series' own algebra. It matters for the temperature of horizons. A companion result shows that if the momentum along a horizon's light rays is non-negative and the fields are in their lowest-energy state, an observer on one side of the horizon sees them as thermal at exactly the right temperature. Put together, the small horizons of flat spacetime get their temperature from positivity of energy. On its own this result does not reach the horizons of black holes. A companion result shows that, for massless fields of the kind unchanged by rescaling distances, it does reach the horizon of a universe driven by a cosmological constant: in the series' language spacetime is flat everywhere, that universe's gravitational field only rescales lengths, and sliding along its horizon's light rays is one of the symmetries of light cones. A black hole's gravitational field also stretches and squeezes by different amounts in different directions, a tidal effect no change of description removes. That the series' modes carry this kind of energy is argued, not proved.

## one-liner
In $\Cl(2,4)$ the rescaled dilation orbit of the central rotation $Z = e_{0}\nu$ tends to the time translation, and the rescaled boost orbit of that tends to every future null translation. So in a unitary representation on a state's GNS space with nonnegative conformal energy, every future translation has a nonnegative generator, in particular the null translations of every local Rindler horizon of Minkowski space: the positivity half of the local-horizon ground-state condition, the standard equivalence proved in the conformal model. The Schwarzschild horizon is not reached (the de Sitter cosmological horizon is, by the result filed alongside), and that the series' modes carry such a representation is argued.
