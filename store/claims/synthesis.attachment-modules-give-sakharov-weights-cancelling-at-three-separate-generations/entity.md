---
id: synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations
kind: claim
version: 3
title: 'Sakharov weights on the attachment cancel at three separate generations'
status: proved
region: synthesis
subject: einstein
tags: [conformal-spinors, mode-counting, curvature-and-field-equations, no-go, undetermined-input, needs-continuum]
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
  role: pin to the slot-module result moved to its version 2 after the clause split; notation declaration
  version: 3
  source: maintainer pass 2026-11-07
review: draft
derivations:
- name: main
  uses:
  - field-theory.twistor-attachment@6
  - standard-model.connection-forced@4
  - synthesis.slot-module-light-ray-arrays-are-weyl-components@2
  - synthesis.imported-sakharov-induced-gravity-coefficients@1
  - synthesis.imported-luscher-mack-conformal-energy-on-the-einstein-static-field@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_module_character_polar_part
- kind: check
  ref: check.py::check_dictionary_reproduces_a1
- kind: check
  ref: check.py::check_smooth_cutoff_vacuum_energy
- kind: check
  ref: check.py::check_series_content_cancels
- kind: check
  ref: check.py::check_sharp_floor_cutoff_is_not_local
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.twistor-attachment
  - families.three-generations-faces-maximal-composite
  - synthesis.einstein-equations-from-c-loc-and-clausius
extraction:
  maintainer_pass_unit_rulings_close:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Mellin inversion of the wave trace written with the unit I_4 (1/(2 pi I_4)), numbers read in span{1, I_4}, under Leon''s ruling of one unit throughout; the outside_ga declaration is removed since no bare i remains.'
  open_problem: op.einstein-from-the-field-theory
  note: >-
    Outside idea tested: Sakharov's induced gravity, with the attachment's positive-energy modules as the vacuum
    and a cut-off on conformal energy (the floors read as energy cut-offs) as the regulator, in place of the
    spectral action of one Dirac operator. The cancellation is the standard Sakharov count
    N_{1/2} = 4 N_1 applied to the Standard-Model content with three right-handed neutrinos (Broda and
    Szanecki; Boyle and Turok find the same 48 = 4 x 12 from vacuum-energy and Weyl-anomaly conditions; with
    the heat-kernel density tr(E + R/6) and Tichy-Flanagan, the imported Fact
    synthesis.imported-sakharov-induced-gravity-coefficients; conformal energy as energy on the unit Einstein
    static field, the imported Fact synthesis.imported-luscher-mack-conformal-energy-on-the-einstein-static-field); new here is only that the attachment's
    modules reproduce the weights. The regulator needs the conformal energy, so it exists only on Weyl-flat
    fields (synthesis.attachment-transport-is-flat-only-where-weyl-vanishes) and depends on the
    conformal frame. The reading of the L^2 term as the induced Einstein-Hilbert term is argued. The count
    N_W = 16 N_g reads three generations as three composites with separate slots (synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group): faces of one slot space
    give at most 40 states, not 48). The ghost subtraction for the vector is the physical-helicity reading of the
    covariant gauge fixing (synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts),
    clause (iv)). The sharp-floor clause is consistent with the floor regulator's boost breaking (synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off). Transport-absent in
    mechanism; the attachment makes the dictionary convenient.
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3, at Leon''s decision of 7 November 2026 splitting the algebra of the canonical part on a null plane out of the light-ray and slot-module results (synthesis.canonical-part-of-a-spinor-on-a-null-plane): this result cites the slot-module result for its clause (ii), sixteen Weyl components per generation, which is not part of the algebra split out, so the uses edge stays and its pin moves from version 1 to 2 (statement unchanged). Statement, proof and checks unchanged. Notation: the one bare i, in the Mellin inversion, stays (declared, complex-analysis).'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01 importing the cited literature as Facts: uses edges to synthesis.imported-sakharov-induced-gravity-coefficients@1 (Broda-Szanecki, the density tr(E + R/6), Boyle-Turok, Tichy-Flanagan) and synthesis.imported-luscher-mack-conformal-energy-on-the-einstein-static-field@1, replacing the citations in the proof of (ii) and its Reading. Statement, proof and checks otherwise unchanged.'
---

## formal
Let the attachment's helicity-$s$ module (Proposition \claimref{field-theory.twistor-attachment}) have conformal energies $k = |s| + 1 + n$, $n \ge 0$, with multiplicity $(n+1)(n+2|s|+1) = k^{2} - s^{2}$, and let a cut-off $f$ on $[0,1]$ weight the energy $k$ at cut-off $L$ by $f(k/L)$. The cut-off uses the conformal energy, so it is defined only on fields where the attachment carries that energy (Weyl-flat fields) and depends on the conformal frame in which the energy is read.
\begin{enumerate}
\item[(i)] \emph{(Character; proved.)} $\chi_{s}(t) = \sum_{n}(n+1)(n+2|s|+1)\,e^{-tk} = e^{-t(|s|+1)}\bigl[2(1 - e^{-t})^{-3} + (2|s| - 1)(1 - e^{-t})^{-2}\bigr]$, and its polar part at $t = 0$ is $2t^{-3} - s^{2}t^{-1}$, with no $t^{-2}$ term.
\item[(ii)] \emph{(Dictionary; computed, with a cited identification.)} Read on the Einstein static field of unit radius, where the conformal energy is the energy and the scalar curvature is $R = 6$ (cited), the polar part gives per field $a_{1} = \tfrac13 c_{-1}R$, $c_{-1}$ the field's $t^{-1}$ coefficient: $0$ for a conformally coupled scalar, $-R/6$ for a two-component (Weyl) fermion, $-2R/3$ for a gauge vector counted by its two physical helicities. These equal the heat-kernel values $\mathrm{tr}(E + R/6)$ computed independently: with the Lichnerowicz term $E = -R/4$ (computed in $\Cl(4,0)$) for the fermion, and four components with $E = -\Ric$ less two ghost scalars for the vector. These are the standard Sakharov weights $N_{0}(1 - 6\xi) + N_{1/2} - 4N_{1}$ at $\xi = 1/6$.
\item[(iii)] \emph{(Smooth cut-offs; proved.)} If $f$ is of class $C^{3}$ with $f(1) = f'(1) = 0$, the regulated zero-point sum of one helicity state, $E_{s}(L) = \sum_{k < L}(k^{2} - s^{2})\,k\,f(k/L)$, is $L^{4}\int_{0}^{1}x^{3}f - s^{2}L^{2}\int_{0}^{1}xf + O(L)$. For $f = (1 - x^{2})^{m}$, $m = 2, 3$, and integer $L$ it is a Laurent polynomial in $L$ with no $L^{3}$ or $L$ term; for the exponential cut-off the regulated sum $-\chi_{s}'(t)$ has polar part $6t^{-4} - s^{2}t^{-2}$.
\item[(iv)] \emph{(The content; proved.)} For $N_{V}$ gauge vectors and $N_{W}$ Weyl fields (two helicity states each) and $N_{S}$ conformally coupled scalars, the weighted sum $\tfrac12\sum_{\mathrm{bosons}}E_{s} - \tfrac12\sum_{\mathrm{fermions}}E_{s}$ has $L^{2}$ coefficient $-(N_{V} - N_{W}/4)\int_{0}^{1}xf$, independent of $N_{S}$, and $L^{4}$ coefficient $\tfrac12(2N_{V} + N_{S} - 2N_{W})\int_{0}^{1}x^{3}f$. With the connection-forced gauge algebra $\su(3) \oplus \su(2) \oplus \uu(1)$, $N_{V} = 12$ (Theorem \claimref{standard-model.connection-forced}), and $N_{g}$ generations read as separate slot modules of sixteen Weyl components each, right-handed neutrino included (\claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}), $N_{W} = 16N_{g}$ and the $L^{2}$ coefficient is $-(12 - 4N_{g})\int_{0}^{1}xf$: zero if and only if $N_{g} = 3$, for every cut-off of (iii) and every number of conformal scalars. With fifteen Weyl components per generation (no right-handed neutrino) it is $-(12 - \tfrac{15}{4}N_{g})\int_{0}^{1}xf$, never zero ($-\tfrac18$ at $N_{g} = 3$, $f = (1 - x^{2})^{2}$). At $N_{g} = 3$ the $L^{4}$ coefficient vanishes only if $N_{S} = 72$.
\item[(v)] \emph{(Sharp floors; proved.)} A sharp cut-off at a floor ($f = 1$ below $L$, $L$ an integer) gives $L^{3}$ and $L$ terms whose coefficients depend on whether the energies are integers (bosons) or half-integers (fermions): $-\tfrac12L^{3}$ per scalar or vector state and none per fermion state. With $f(1) = 0$ but $f'(1) \neq 0$ ($f = 1 - x^{2}$) the odd powers vanish, but the $L^{2}$ coefficient differs from $-s^{2}\int_{0}^{1}xf$ by an edge term, $-\tfrac16$ for $s = 0, 1$ and $+\tfrac1{12}$ for $s = \tfrac12$, which does not cancel with the content of (iv).
\end{enumerate}
\emph{Reading (argued).} On the Einstein static field of radius $r$ with physical cut-off $\Lambda_{c} = L/r$ the regulated energy is $r^{-1}E(\Lambda_{c}r)$, with orders $\Lambda_{c}^{4}r^{3}$ (the volume), $\Lambda_{c}^{2}r$ and $r^{-1}$; $\Lambda_{c}^{3}r^{2}$ and $\Lambda_{c}$ match no local invariant. If the regulated effective action is local and covariant, the $\Lambda_{c}^{2}r$ order is the induced Einstein-Hilbert term; on this one field it cannot be told apart from frame-dependent terms such as the integral of the spatial curvature. Under that hypothesis, with three separate generations including right-handed neutrinos, conformally coupled scalars and a smooth cut-off, this regulator would induce no Newton coupling at leading order, and Sakharov's route on this vacuum does not supply $G$. Transport-absent in mechanism; the attachment makes the dictionary convenient.

## technical
Take the attachment's helicity-$s$ modules: energies $k = |s| + 1 + n$ with multiplicity $k^{2} - s^{2}$. Their conformal-energy character has polar part $2t^{-3} - s^{2}t^{-1}$. On the Einstein static field of unit radius this reproduces the standard one-loop curvature coefficients $a_{1}$: zero for a conformally coupled scalar, $-R/6$ for a Weyl fermion, $-2R/3$ for a gauge vector counted by its physical helicities. These are the Sakharov weights $N_{0}(1 - 6\xi) + N_{1/2} - 4N_{1}$ at $\xi = 1/6$, recomputed here with the Lichnerowicz term in geometric algebra.

The regulator is a cut-off on conformal energy. It is frame-dependent, and it is defined only on Weyl-flat fields, where the attachment carries that energy. For any such cut-off that vanishes with its slope at the edge, one helicity state's regulated zero-point energy is $L^{4}\int x^{3}f - s^{2}L^{2}\int xf + O(L)$. Weighting bosons and fermions oppositely, the $L^{2}$ coefficient is $-(N_{V} - N_{W}/4)\int xf$, whatever the number of conformal scalars. The connection-forced gauge algebra has $N_{V} = 12$. With generations read as separate slot modules of sixteen Weyl fields each, right-handed neutrino included, $N_{W} = 16N_{g}$, so the coefficient vanishes if and only if $N_{g} = 3$. This is the standard count $N_{1/2} = 4N_{1}$ for the Standard Model with three right-handed neutrinos; the same $48 = 4 \times 12$ appears in Boyle and Turok's cancellation of the vacuum energy and Weyl anomaly. Without right-handed neutrinos there is no cancellation. The quartic coefficient does not vanish.

A sharp cut-off at a floor adds $L^{3}$ and $L$ terms whose coefficients depend on whether the energies are integers or half-integers. A cut-off with a kink at the edge adds a statistics-dependent $L^{2}$ edge term. On the Einstein static field these odd powers match no local invariant.

Reading, argued: if the regulated action is local and covariant, the $L^{2}$ order is the induced Einstein-Hilbert term, and under the stated content this cut-off would induce no Newton coupling at leading order. Transport-absent in mechanism.

## lay
Sakharov suggested that gravity's strength might not be fundamental but induced by the quantum jitter of all the matter and force fields, the way a medium's stiffness comes from its atoms. This result tries that idea with the series' own particle states and a natural cut-off, the series' levels read as an energy limit. That cut-off only makes sense where the gravitational field has no tidal (Weyl) part, and it singles out one frame. Each kind of particle adds to the induced strength of gravity in proportion to the square of its spin, with force carriers and matter particles pulling in opposite directions. These weights are the standard ones, and the series' states reproduce them. With twelve force carriers and three separate families of sixteen matter states each, right-handed neutrinos included, the two cancel exactly. This is the standard count for the Standard Model with right-handed neutrinos, noticed in another form by Boyle and Turok. So under this cut-off the series' matter would induce no gravitational strength at leading order, if the leading term is read as gravity's, which is argued rather than proved. A sharp cut-off at the levels would also produce terms that no local law of gravity contains.

## one-liner
On the attachment's helicity modules, the $L^{2}$ coefficient of the zero-point energy under a smooth cut-off on conformal energy (frame-dependent, defined on Weyl-flat fields) is $-(N_{V} - N_{W}/4)$ times one moment of the cut-off, the standard Sakharov weights; with $N_{V} = 12$, sixteen Weyl fields (right-handed neutrino included) in each of $N_{g}$ separate generations and conformal scalars it vanishes exactly at $N_{g} = 3$, which read on the Einstein static field is the induced Einstein-Hilbert coefficient if the regulated action is local and covariant (argued); a sharp floor cut-off adds non-local terms.
