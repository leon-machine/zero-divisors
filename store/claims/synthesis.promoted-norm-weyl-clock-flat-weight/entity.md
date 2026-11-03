---
id: synthesis.promoted-norm-weyl-clock-flat-weight
kind: claim
version: 6
title: For the frozen-point action the Euclidean action of an Einstein instanton at matching $\Lambda$ is $(\ell^{2}/64\pi G)\int|W|^{2}$, and the time conjugate to the promoted norm advances by the Weyl-squared integral in vacuum and by the Euler-density excess $E - 8\Lambda^{2}/3$ with matter, so it runs on every FLRW cosmology with dust or radiation
status: proved
region: synthesis
subject: dark-energy
tags: [cosmological-constant, the-number-n, frozen-point, curvature-and-field-equations, kasner, no-go]
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
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@3
  - dark-energy.imported-henneaux-teitelboim-promotion@5
  - dark-energy.under-action-written-norm-parameter-laws@4
  - synthesis.de-sitter-entropy-pi-n-squared@5
  - dark-energy.frozen-point-datum-kasner-wall@7
  - synthesis.imported-chern-gauss-bonnet@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_normalisation
- kind: check
  ref: check.py::check_gauss_bonnet_cross
- kind: check
  ref: check.py::check_pointwise_einstein_identity
- kind: check
  ref: check.py::check_instanton_actions
- kind: check
  ref: check.py::check_conjugate_time_density
- kind: check
  ref: check.py::check_clock_frozen_conformally_flat_and_kasner
- kind: check
  ref: check.py::check_matter_flrw_density
- kind: check
  ref: check.py::check_matter_density_frame_independent
- kind: check
  ref: check.py::check_lorentzian_decomposition_with_source
- kind: proof
  derivation: main
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 5 -> 6. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: the Chern-Gauss-Bonnet theorem, cited from memory in (ii), is now the imported Fact synthesis.imported-chern-gauss-bonnet, added to uses and cited in the proof and check. The Miskovic-Olea identity is recorded as the imported Fact synthesis.imported-miskovic-olea-identity and cited in text as prior work; it is not a premise (the de Sitter identity is proved here), so it is not in uses. Version 1 -> 2.'
  open_problem: op.henneaux-teitelboim-promotion
  note: >-
    Decision input for the promotion, computed on the series' own action rather than on the
    Einstein-Hilbert action the unimodular literature uses. Two consequences: the cosmic time the
    promotion introduces registers, in vacuum, Weyl curvature only (it stands still on de Sitter
    space and diverges at a Kasner wall), and with matter the excess of the Euler density over its
    de Sitter value (it runs on every FLRW cosmology with dust or radiation); and the semiclassical
    weight of the action supplies no factor favouring small Lambda (the Gauss-Bonnet term cancels
    the Baum-Hawking factor exp(pi N^2) exactly), so a measure over Lambda must come from elsewhere.
    The mathematics is standard (Chern-Gauss-Bonnet, the imported Fact synthesis.imported-chern-gauss-bonnet; Einstein instantons) and transport-absent;
    the instanton identity of (ii) is known for the Euler-regularised (MacDowell-Mansouri) action
    in the anti-de Sitter case (Miskovic and Olea, the imported Fact synthesis.imported-miskovic-olea-identity, cited as prior
    work and not as a premise; on-shell equivalence to conformal gravity); what is new here is its reading for the promoted norm and the
    cancellation of the Baum-Hawking factor. Complementary to the phase-space count filed alongside,
    synthesis.promoted-norm-one-global-pair, which promotes the norm of I rather than l^2; the two
    conjugate times differ by the factor g'. Companion filed alongside: synthesis.einstein-route-makes-n-initial-data
    (N is initial data on the Clausius route with no promotion; the promotion adds this clock). The Euclidean continuation of
    the functional and the no-boundary reading in (iv) are stated as hypotheses, not derived.
  correction:
    by: ai-correction
    date: '2026-10-23'
    session: 2026-10-23-toe
    note: 'Version 3 said the conjugate time stands still on every FLRW cosmology. FLRW with matter
      is not a solution of the vacuum functional, and with matter coupled the step from the density
      k(E - 24/u^2) to k|W|^2 fails twice: the trace of the frame equation is the matter trace, not
      zero, and the trace-free Ricci part does not vanish, so F is not W. Clause (iii) now gives the
      general density, clause (iv) is restricted to vacuum (where conformally flat means locally de
      Sitter), and clause (v) computes the density with matter: on flat FLRW with a perfect fluid it
      is (4/3)k[Lambda(rho - 3p) - rho(rho + 3p)] in units 8 pi G = 1, nonzero for radiation and for
      dust away from 8 pi G rho = Lambda. Clauses (i), (ii) and the reading under (H) are unchanged.'
  flags:
  - 'beyond one flat chart: the closed Einstein instantons S^4, S^2 x S^2, CP^2 and their Euler characteristic'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (MIXED): the functional is that of a gravitational field on the Wick-rotated flat background; |W|^2 read from the Weyl part of the curvature operator; vol = det(hb)^{-1} d^4x; locally de Sitter as W = 0; FLRW as the comoving-gauge field. The closed Einstein instantons of (ii) and (H) (S^4, S^2 x S^2, CP^2, chi) carry the Section 14 flag and a flags entry; the clock density of (iii)-(v) is local. Clauses (i)-(v) and the reading unchanged; proof given a pointer.'
---

## formal
\emph{Setting.} Take the MacDowell-Mansouri functional of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west} for a gravitational field $(\hb, \Omega)$ on the Wick-rotated, Euclidean, flat background (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), in Euclidean signature, $S = k\,\ell^{2}\int\epsilon_{abcd}F^{ab}\wedge F^{cd}$ with Lorentz block $F^{ab} = R^{ab} - \ell^{-2}e^{a}\wedge e^{b}$ (the Euclidean form of the de Sitter branch, for which the round $\Sph^{4}$ of radius $\ell$ has $F = 0$), torsion zero, $\Lambda = 3/\ell^{2} > 0$, and $N^{2} = \ell^{2}/G = 3/(G\Lambda)$, the number of Proposition \claimref{synthesis.de-sitter-entropy-pi-n-squared}. Write $W$ for the Weyl tensor, the trace-free part $\mathcal{W}$ of the curvature operator, and $|W|^{2} = W_{abcd}W^{abcd} = 2\langle\mathcal{W}(a \wedge b)\,\mathcal{W}(\partial_b \wedge \partial_a)\rangle$; $\mathrm{vol}$ is $\det(\hb)^{-1}d^{4}x$.
\begin{enumerate}
\item[(i)] \emph{(Normalisation.)} Matching the Einstein-Cartan term to the Euclidean Einstein-Hilbert action $-\tfrac{1}{16\pi G}\int R$ fixes $k = 1/(64\pi G)$; the cosmological term is then exactly $\tfrac{2\Lambda}{16\pi G}\int\mathrm{vol}$ with $\Lambda = 3/\ell^{2}$, and the Gauss-Bonnet coefficient is $\ell^{2}/(64\pi G) = 3/(64\pi G\Lambda)$.
\item[(ii)] \emph{(Instanton actions.)} On every Einstein metric with $\Ric = \Lambda g$ the integrand is pointwise $\epsilon_{abcd}F^{ab}\wedge F^{cd} = |W|^{2}\,\mathrm{vol}$, the volume and curvature terms cancelling identically. Hence on every closed Einstein $4$-manifold $M$
\[
I_{\mathrm{MM}}[M] \;=\; \frac{\ell^{2}}{64\pi G}\int_{M}|W|^{2}\,\mathrm{vol} \;=\; I_{\mathrm{EH}}[M] + \frac{\chi(M)}{2}\,\pi N^{2} \;\ge\; 0,
\]
with equality exactly when the Weyl part vanishes on $M$ (locally conformally flat derived metric). For the round $\Sph^{4}$, $\Sph^{2}\times\Sph^{2}$ and $\mathbb{CP}^{2}$: $I_{\mathrm{MM}} = 0$, $\tfrac43\pi N^{2}$, $\tfrac34\pi N^{2}$, against $I_{\mathrm{EH}} = -\pi N^{2}$, $-\tfrac23\pi N^{2}$, $-\tfrac34\pi N^{2}$.
\item[(iii)] \emph{(The conjugate time.)} Under the promotion of Fact \claimref{dark-energy.imported-henneaux-teitelboim-promotion}, with the norm mode of Proposition \claimref{dark-energy.under-action-written-norm-parameter-laws} as the multiplier field, and with \emph{the norm} meaning $u = \ell^{2} = -Q(V)$, the variable conjugate to $u$ advances between two slices by the integral over the region between them of the density $k\bigl(E - 24u^{-2}\bigr)\mathrm{vol}$, $E$ the Gauss-Bonnet integrand, which is the derivative of the Lagrangian in $u$ at fixed frame and connection. On every torsion-free vacuum solution this is $k|W|^{2}\mathrm{vol}$. For any other choice $g(u)$ of the promoted variable (for instance $\Lambda = 3/u$, or the norm $Q(I) = \Lambda/3$) the conjugate variable advances by the same integral divided by $g'(u)$, so for $\Lambda$ by $-3/\Lambda^{2}$ times that; there is a conjugate time for each choice of variable, all proportional on each solution. The value does not depend on which frame normalisation is held fixed as the norm varies: the two choices differ by a multiple of the trace of the full frame equation (with the matter term when matter is present), which vanishes on shell.
\item[(iv)] \emph{(Vacuum: where it runs.)} On solutions of the functional as written (vacuum), the conjugate time does not advance on any region where the Weyl part of the field strength vanishes, and such a region is locally the de Sitter field (Einstein with $\mathcal{W} = 0$ is constant curvature), the de Sitter slicings of FLRW form included. Near a Kasner wall with $p_{1}p_{2}p_{3} \neq 0$ (Proposition \claimref{dark-energy.frozen-point-datum-kasner-wall}) its density is $k$ times the Kretschmann density at leading order, $\tfrac{64}{27}\,k\,\tau^{-3}$ for the Schwarzschild exponents, so it diverges as $\tau^{-2}$ toward the wall.
\item[(v)] \emph{(With matter.)} Add a matter action that depends on the frame only through the metric and on matter fields, and not on $u$ or on the connection (hypothesis (Mat)), with torsion zero. The density is still $k(E - 24u^{-2})\mathrm{vol}$. In Lorentzian signature $(3,1)$, with the curvature convention in which de Sitter space has $R_{abcd} = H^{2}(g_{ac}g_{bd} - g_{ad}g_{bc})$, on every solution, where $\Ric - \tfrac12 s\,g + \Lambda g = 8\pi G\,T$ holds, with $t = g^{ab}T_{ab}$ and $T^{\mathrm{tf}}$ the trace-free part of $T$,
\[
E - \tfrac83\Lambda^{2} \;=\; |W|^{2} - 2(8\pi G)^{2}|T^{\mathrm{tf}}|^{2} - \tfrac43\Lambda\,(8\pi G\,t) + \tfrac16(8\pi G\,t)^{2}.
\]
On the flat FLRW gravitational field on flat spacetime ($\hb^{-1}(e_t) = e_t$, $\hb^{-1}(e_i) = a(t)\,e_i$) with a perfect fluid of density $\rho$ and pressure $p$, writing $\tilde\rho = 8\pi G\rho$ and $\tilde p = 8\pi G p$,
\[
E - \tfrac83\Lambda^{2} \;=\; \tfrac43\bigl[\Lambda(\tilde\rho - 3\tilde p) - \tilde\rho(\tilde\rho + 3\tilde p)\bigr],
\]
which is $-\tfrac83\tilde\rho^{2}$ for radiation and $\tfrac43\tilde\rho(\Lambda - \tilde\rho)$ for dust, vanishing for dust only at $8\pi G\rho = \Lambda$. So the conjugate time advances on every FLRW cosmology with radiation or dust; standing still is a property of vacuum. Where $W = 0$, $(3k/\Lambda^{2})(E - \tfrac83\Lambda^{2}) = -t/(2\Lambda) + O(G)$; the time conjugate to $\Lambda$ advances by $(3k/\Lambda^{2})\int(E - \tfrac83\Lambda^{2})\mathrm{vol}$ up to the overall sign set by the signature convention of the action, so to first order in $G$ it counts, for dust, $\rho/(2\Lambda)$ per unit four-volume: rest mass times proper time over $2\Lambda$.
\end{enumerate}
\emph{Reading, conditional on the no-boundary hypothesis (H).} (H) If the relative weight of the values of the promoted $\Lambda$ is the semiclassical factor $e^{-I}$ of closed Einstein instantons, then by (ii) the round $\Sph^{4}$ contributes weight $1$ at every $\Lambda$ and every other Einstein instanton contributes less, the less the smaller $\Lambda$; the factor $e^{\pi N^{2}}$ of the Einstein-Hilbert argument for small $\Lambda$ is cancelled exactly by the Gauss-Bonnet term. Under (H) the series' action therefore supplies no factor favouring small $\Lambda$, and a measure over the promoted $\Lambda$ has to be supplied as a datum of its own.

\emph{Beyond one flat chart.} The closed Einstein four-manifolds of (ii) and of the reading (H) ($\Sph^{4}$, $\Sph^{2}\times\Sph^{2}$, $\mathbb{CP}^{2}$, with their Euler characteristic $\chi(M)$) are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region are in GTG, and the closed instantons are read on the manifold assembled from the derived metric's charts.

## technical
The frozen-point action is the MacDowell-Mansouri form: Einstein-Hilbert plus a cosmological term plus a Gauss-Bonnet term whose coefficient is fixed at $\ell^{2}/(64\pi G)$. On any Einstein space the three combine into the Weyl-squared integral times that coefficient, so the Euclidean action of an Einstein instanton is non-negative and vanishes exactly for those with vanishing Weyl part, the round four-sphere among them; by Gauss-Bonnet it equals the Einstein-Hilbert value plus half the Euler characteristic times $\pi N^{2}$. The instanton identity itself is known for the Euler-regularised form of this action in the anti-de Sitter case (Miskovic and Olea, Fact \claimref{synthesis.imported-miskovic-olea-identity}, where the action is on shell equivalent to conformal gravity); what is new here is its reading for the promoted norm and the exact cancellation of the Baum-Hawking factor. If the norm $\ell^{2}$ (or any function of it, which only rescales the result by a derivative) is promoted to a multiplier field as Henneaux and Teitelboim do for $\Lambda$, its conjugate cosmic time is the derivative of the action in the norm, the integral of $k(E - 24\ell^{-4})$ with $E$ the Gauss-Bonnet integrand. On vacuum solutions this is the Weyl-squared integral: it stands still on de Sitter space and diverges at a Kasner wall. With matter coupled through the metric it is not: the trace and the trace-free part of the stress tensor enter, and on a flat FLRW universe with a perfect fluid the density is $\tfrac43 k[\Lambda(\tilde\rho - 3\tilde p) - \tilde\rho(\tilde\rho + 3\tilde p)]$ with $\tilde\rho = 8\pi G\rho$, $\tilde p = 8\pi G p$; it is negative throughout a radiation era, changes sign for dust at $8\pi G\rho = \Lambda$, and to first order in matter the time conjugate to $\Lambda$ counts rest mass times proper time over $2\Lambda$. The clock therefore runs on every universe with dust or radiation; it stands still only in vacuum. It is not monotone (it reverses sign for dust at $8\pi G\rho = \Lambda$), so it is a record of the history, not a time coordinate ordering it. The clock depends on which action is promoted: for the Einstein-Hilbert action it counts four-volume over $8\pi G$, for the series' action the Euler-density excess, which to first order in matter is $\rho/(2\rho_{\Lambda})$ times the four-volume clock, $\rho_{\Lambda} = \Lambda/8\pi G$; the companion result filed alongside, synthesis.einstein-route-makes-n-initial-data, shows that on the Clausius route alone $\Lambda$ is an integration constant and $N$ initial data with no promotion, so what the promotion adds over that route is this clock and the Liouville density. Assuming the no-boundary weighting, the series' action gives every value of $\Lambda$ weight one through the four-sphere and penalises the others, so it contains nothing that favours a small $\Lambda$: the standard Baum-Hawking factor comes from the Einstein-Hilbert action and is cancelled here. Its closed Einstein instantons and their Euler characteristic are global: no single gravitational field on flat spacetime carries them, so that part is read on several charts of flat spacetime (charts of Euclidean $\R^{4}$), each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations; the clock's density is local and lives on a flat chart. Because the clock's advance on a history depends on the solution (in vacuum it is the Weyl-squared integral; with matter it is dominated by the matter's stress), a density over $\Lambda$ that assumes equal ranges of the conjugate time for every $\Lambda$ (as in the phase-space count filed alongside, synthesis.promoted-norm-one-global-pair) carries that assumption as an extra input.

## lay
The framework's action for gravity differs from Einstein's by a term that only depends on the overall shape of space. One proposal for the cosmological constant is to make it a quantity that can differ between possible universes, paired with a cosmic clock. The first part of this result, the value of the action on these spaces, is already known in the literature on this form of the action; what is added is what it means for that proposal. It computes what the clock is for the framework's action: in empty space it only ticks where space is tidally distorted, so it stands still in a universe holding nothing but the cosmological constant, and near the crushing singularity inside a black hole it runs without bound. In a universe with matter and radiation, like ours, it does tick: fastest in the hot early universe, reversing direction once matter has thinned to the density of the cosmological constant. It also shows that, if one weighs possible universes in the usual way, this action gives no preference to a small cosmological constant, unlike Einstein's action; any explanation of the small observed value would have to come from somewhere else.

## one-liner
For the frozen-point (MacDowell-Mansouri) action the Euclidean action of an Einstein instanton is $(\ell^{2}/64\pi G)\int|W|^{2} = I_{\mathrm{EH}} + \tfrac{\chi}{2}\pi N^{2} \ge 0$, (an identity known for this action), and under the Henneaux-Teitelboim promotion the time conjugate to the norm $\ell^{2}$ (any function of it, up to $g'$) advances by the Weyl-squared integral in vacuum, so it stands still on de Sitter space, and by the Euler-density excess $E - 8\Lambda^{2}/3$ with matter, so it runs on every FLRW cosmology with dust or radiation; if the no-boundary weight is used, the action favours no small $\Lambda$.
