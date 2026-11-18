---
id: synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries
kind: claim
version: 3
title: 'The tube-point clause: invariance under the rotations commuting with the horizon''s boost'
status: postulate
region: synthesis
subject: one-relation
tags: [conformal-spinors, frozen-point, horizons]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, every imaginary unit resolved as a geometric-algebra pseudoscalar (unit principle)
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Fable 5.2
  role: 'restatement of the clause at Leon''s decision: invariance under the rotations commuting with the wedge''s boost, the boost generating a positive multiple of the horizon''s Killing flow; silent on black-hole fields'
  version: 3
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
amendments:
- version: 3
  kind: restatement
  defect: 'as worded (invariance under every symmetry commuting with the boost, the boost generating any symmetry of the field) the clause had no single reading: with the boost counted nothing is fixed in any field, the outcome depended on the gauge, and the sentence that it decides fields with one horizon was not computed for the Schwarzschild field, where no observer meets the condition'
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
lineage:
  motivated_by:
  - synthesis.de-sitter-field-fixes-the-observer-tube-point
  - synthesis.wick-rotated-boost-selects-observer-tube-point
  - synthesis.imported-de-sitter-invariant-hadamard-state-unique
  - synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent
extraction:
  maintainer_pass_2026_11_18_leads:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 2 -> 3. Restatement by Leon''s decision D3 of 18 November 2026 (the clause is a costed premise; status stays postulate): the clause now reads invariance under the rotations among the symmetries commuting with the wedge''s boost, the boost being a positive multiple of the horizon''s Killing flow, in a gauge adapted to that flow. The de Sitter selection stands on that reading. On the Schwarzschild exterior and on the static region of Schwarzschild-de Sitter no observer meets the condition (synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent, (iv) to (vi)); the clause is silent there and rho stays free. The sentence ''it decides fields with one horizon only'' and the further-premise sentence of the cost are replaced; refutation condition (b) now reads ''on a field where the clause decides'', since the clause is silent on the Schwarzschild field; (a) and (c) say ''rotations''. Title changed to match. The new result added to lineage. The version-2 wording of the clause: ''In a gravitational field (hb, Omega) on flat spacetime of which K generates a symmetry, m is invariant under every symmetry of the field that commutes with K, acting on tube points complex-linearly.'''
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the tube point m = x_perp + i rho u is written x_perp + I_7 rho u, with I_7 = I_6 e the central pseudoscalar of Cl(3,4) = Cl(2,4)_C, which commutes with every vector (std-algebra.complexification-is-the-odd-extension, cited as a mention); the clause, its cost and its refutation condition are unchanged, and the status stays postulate. No bare i remains, so the outside_ga declaration (complex-analysis, for i only) is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the i of the tube point m = x_perp + i rho u belongs to the complexified spacetime (forward tube), whose unit must commute with the vectors; declared (version and levels unchanged).'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: >-
      New costed clause, registered by Leon's decision of 2026-10-31 to adopt the selection rule argued in the
      reading of synthesis.de-sitter-field-fixes-the-observer-tube-point as a costed clause: taken as given, with
      its cost (the hypothesis gap from the de Sitter Hadamard uniqueness theorem to the series' CAR modes, and
      its reach, one-horizon fields only) and a refutation condition stated. It fixes rho^2 = 12/Lambda for
      Lambda > 0 and leaves rho free for Lambda <= 0. An assumes edge from the de Sitter tube-point result is
      added with it.
---

## formal
\emph{The tube-point clause (costed; restated 18 November 2026).} Let a state of the series' modes and a wedge with boost $K$ be given, with the compatible tube point $m = x_{\perp} + I_{7}\rho u$ over the wedge's bifurcation plane ($I_{7} = I_{6}e$ the central pseudoscalar of $\Cl(2,4)_{\C} = \Cl(3,4)$, which commutes with every vector, Theorem \claimref{std-algebra.complexification-is-the-odd-extension}) that the boost-KMS data and the ascent pair fix up to the scale $\rho$ (Theorem \claimref{synthesis.wick-rotated-boost-selects-observer-tube-point}). Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with a Killing horizon, in a gauge adapted to the horizon's flow: the flow of $K$ is the flow of a positive multiple of the horizon's Killing field, and the rotations among the symmetries of the field commuting with $K$ (those generating a compact group) act on tube points complex-linearly, by bivectors. Then $m$ is fixed by every rotation among the symmetries of the field that commute with $K$. Where no observer of the region has a compatible tube point meeting this condition the clause is silent: it selects no tube point, excludes no state, and leaves $\rho$ free.

The boost is not among the symmetries asked to fix $m$: neither $K$ nor any sum $aK + B$, with $a \neq 0$ and $B$ a bivector of the space orthogonal to the boost plane, fixes a compatible tube point, in any field (Theorem \claimref{synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent}, opening paragraph).

\emph{What it is for.} It is the selection rule of the reading of Theorem \claimref{synthesis.de-sitter-field-fixes-the-observer-tube-point}, adopted. In the de Sitter field ($\Lambda > 0$), in the gauge $\hb = \sigma$ in which $K$ generates the horizon's flow, the symmetries commuting with $K$ are $K$ and a transverse $\so(3)$, and the compatible tube points that the $\so(3)$ fixes are exactly one boost orbit, foot at the scale's centre and $\rho^{2} = 12/\Lambda$ (that theorem, (i) and (ii)); so the clause fixes $\rho$ there, and the frozen-point and surface-gravity candidates are one tube point when $\rho = 1/\kappa$ is read as the physical norm of the boost generator (in chart length $\rho_{\Lambda} = 2/\kappa$, the factor $2$ being the local scale $\sigma = 2$). In that field the condition is equivalent to the complexified Stelle-West vector $X(m)/\sigma(m) - \tfrac{3}{\Lambda}I_{\Lambda}$ being purely imaginary (that theorem, (vii)). For the pure-dilation fields with $\Lambda \le 0$ it fixes no tube point and $\rho$ stays free (that theorem, (vi)).

On the Schwarzschild exterior, and on the static region of the Schwarzschild-de Sitter field with $K$ the flow of either horizon, no observer meets the condition (Theorem \claimref{synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent}, (iv) to (vi)): in every gauge adapted to the horizon's flow the rotations are the $\so(3)$ of a de Sitter tractor, a compatible tube point is fixed exactly when its observer is a fixed point of the rotations, and the rotation orbits of the region are two-spheres. The clause is silent there and $\rho$ stays free. The candidates that coincide with the clause's selection in the de Sitter field are not part of the clause and do not coincide there: the maximal normalised norm and free fall select no observer of the Schwarzschild exterior at a finite distance, and in the Schwarzschild-de Sitter field with lapse $f = 1 - 2M/r - \tfrac{\Lambda}{3}r^{2}$ they select one radius, $r_{0}^{3} = 3M/\Lambda$, the same for both horizons, with one scale per horizon in the ratio $\kappa_{b}/\kappa_{c}$ ($\tfrac85$ at $\Lambda = M = \tfrac37$, horizons at $r = 1$ and $r = 2$), neither equal to the inverse surface gravity (that theorem, (v) and (vi)). They are not adopted. Where the clause decides, it ties the scale to $\Lambda$ and supplies no unit independent of it.

\emph{What it costs.} It is adopted, not derived from the series' structure. The argument for it runs through the uniqueness of the de Sitter-invariant Hadamard state of a massive scalar (Fact \claimref{synthesis.imported-de-sitter-invariant-hadamard-state-unique}): a state with the symmetry of the field, and a rule assigning tube points covariantly, return a point fixed by the rotations of the field commuting with the boost. The series' boundary modes are CAR fermions, outside that theorem's hypotheses, so the clause carries the hypothesis gap from that theorem to the series' modes. Its restriction to the rotations, and to a boost that generates the horizon's own Killing flow, is part of what is adopted (decision of 18 November 2026) and is not derived either. As first worded, with invariance asked under every symmetry commuting with $K$ and $K$ allowed to generate any symmetry of the field, the clause had no single reading: counted with the boost the condition is met in no field, the de Sitter field included, and its outcome depended on the gauge, since in a gauge twisted by a rotation that grows with the rapidity, where $K$ generates the horizon's flow plus a rotation, the observers on the rotation axis meet the condition at every scale, in the de Sitter field as on the black-hole fields (Theorem \claimref{synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent}, opening paragraph and (vii)). The de Sitter selection stands on the restated reading. On the Schwarzschild and Schwarzschild-de Sitter fields the clause fixes nothing, and the question whether a tube point is assigned per observer or per horizon is not reached; a scale there needs a further premise, which is open (op.which-capacity).

\emph{Refutation condition.} The clause is false if any of the following is established: (a) a state of the series' modes on a horizon of the de Sitter field, satisfying the series' other premises, whose compatible tube point is not fixed by the transverse $\so(3)$, for example one whose data fix $\rho^{2} \neq 12/\Lambda$; (b) a derivation from the series' premises of a rule fixing $\rho$ that disagrees with the clause on a field where the clause decides (of the fields computed, the de Sitter field); (c) a proof that the series' horizon states on the de Sitter field are not invariant under the rotations of the field commuting with the boost.

## technical
A state of the series reads its capacities at a point of the complexified spacetime, its tube point, which the state's thermal data on a wedge fix up to one scale $\rho$. This clause fixes the scale by symmetry: with the wedge's boost generating a positive multiple of the horizon's Killing flow, the tube point must be left in place by every rotation among the symmetries of the gravitational field that commute with the boost. In the de Sitter field those rotations are the rotations about the observer at the centre of the static patch, and the only tube points they fix sit at $\rho^{2} = 12/\Lambda$, where the frozen-point and surface-gravity candidates agree as physical lengths. For a vanishing or negative cosmological constant nothing is fixed. On the Schwarzschild exterior and on the static region of Schwarzschild-de Sitter, for either horizon, no observer meets the condition, because every observer there is carried around a sphere by the rotations; the clause is silent there and the scale stays free. The norm and free-fall candidates, which are not adopted, pick no observer at a finite distance on Schwarzschild and one radius, $r_{0}^{3} = 3M/\Lambda$, in Schwarzschild-de Sitter, with two scales in the ratio of the surface gravities, $8/5$ in the stored sample. The clause is a costed choice: its support is the uniqueness of the symmetric Hadamard state for a massive scalar, which the series' fermionic boundary modes do not satisfy as stated; its restriction to rotations and to the horizon's own flow is adopted with it, the clause as first worded (every symmetry commuting with the boost, the boost generating any symmetry of the field) having no single reading; and it fixes no scale where a black hole is present. It would be refuted by a series state on de Sitter whose tube point the rotations move, by a derived rule that disagrees with it where it decides, or by a proof that the series' horizon states lack the field's rotational symmetry.

## lay
Each observer in this framework is attached to a point of a complexified copy of spacetime, and the framework's thermal data fix that point except for one length. This assumption fixes the length by symmetry: taking the horizon's own time flow as the reference, the point must not move under the rotations of the gravitational field that leave that flow alone. In a universe with a positive cosmological constant that picks one length, the size set by the cosmological constant; with zero or negative cosmological constant it picks none. Around a black hole, alone or in an expanding universe, no observer meets the requirement, since the rotations carry every observer around a sphere; there the assumption says nothing and the length stays undetermined. It is adopted with these limits stated, and could be overturned by a calculation or derivation that disagrees with it where it does decide.

## one-liner
Costed clause, restated: with the wedge's boost generating a positive multiple of the horizon's Killing flow, a state's tube point is fixed by the rotations among the field's symmetries commuting with the boost; in de Sitter this fixes $\rho^{2} = 12/\Lambda$ (frozen-point and surface-gravity candidates one tube point as physical lengths), for $\Lambda \le 0$ it leaves $\rho$ free, on the Schwarzschild exterior and the static region of Schwarzschild-de Sitter no observer meets the condition, the clause is silent and $\rho$ stays free, and it carries the hypothesis gap from the massive-scalar Hadamard uniqueness theorem to the series' CAR modes.
