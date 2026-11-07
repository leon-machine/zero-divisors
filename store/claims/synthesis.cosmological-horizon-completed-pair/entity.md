---
id: synthesis.cosmological-horizon-completed-pair
kind: claim
version: 4
title: The cosmological horizon's completed pair
status: proved
region: synthesis
subject: thermality
tags: [ladder-pairs, horizons, frozen-point, conformal-model]
proposed_by:
  kind: ai
  session: de-sitter-temperature-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof of the curvature step: the dilation field, Omega from the torsion equation, calR = (Lambda/3) id'
  version: 4
  source: maintainer pass 2026-11-07 (consistency, GTG proofs)
review: draft
derivations:
- name: main
  uses:
  - synthesis.de-sitter-static-boost-frozen-point@6
  - mass.de-sitter-scale-frozen-point@6
  - dark-energy.imported-frozen-point-geometry@7
  - singularity.pseudo-inverse-identities-hyperbolic-atom@4
  - singularity.modular-structure-completed-pair@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_completed_pair
- kind: check
  ref: check.py::check_gtg_dilation_field_curvature_selects_no_plane
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.plane-rate
  - singularity.why-calibration-cannot-be-internal
  - standard-model.what
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): dark-energy.imported-frozen-point-geometry repinned 6 -> 7 after reviewing its restatement (the sentence naming the tractor gauge-field theorem moved to a text-only remark); the parts cited here (parallel frozen point, Q(I) = Lambda/3, the stabilisers, the scale-g display and the Schouten tensor) are unchanged, and the use here holds as cited.'
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee F1: ACCEPT, no fix asked. Pin synthesis.de-sitter-static-boost-frozen-point 5 -> 6 (formal unchanged byte for byte: notation only).'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Item H5 (notation, routine): formal (iii) and proof Step 3 name the unit of the phase, span{1, hat-I} with hat-I the central unit of the boundary-mode object (unit principle U3), and the bar as its conjugate. No content change; evidence: the uniqueness computation of Step 3 is unchanged (|a| = 1/2 for either unit).'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Step 1 of the proof rewritten in Gauge Theory Gravity: the de Sitter field of the scale as the dilation hb^{-1}(a) = a/sigma; the torsion equation hb^T(grad ^ f^a) = sum_b gamma^b ^ (omega(gamma_b) . gamma^a) solved by omega(A) = grad sigma ^ A, so Omega(a) = -(Lambda/(6 sigma)) x ^ a; the field strength computed in GA to R(a ^ b) = -(Lambda/3) sigma^-2 a ^ b, hence calR(B) = (Lambda/3) B, Schouten (Lambda/6) id, Weyl zero; the Christoffel computation and the -Lambda/3 of the round-sphere-positive convention kept as a labelled reading (C11). Steps 2-5 were already in Cl(2,4) and are unchanged. Original proof kept as orig-proof-main.tex. New exact check check_gtg_dilation_field_curvature_selects_no_plane (Omega solved from torsion at nine rational points, its closed form, calR = (Lambda/3) id, Ricci map Lambda a, Weyl operator zero, riem_o = -(Lambda/3)(g_ac g_bd - g_ad g_bc)). outside_ga withdrawn: no stand-in remains in the proof''s main line.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The proof''s curvature check computes the Riemann tensor of the derived metric from its Christoffel symbols in components; the GTG statement is in the formal level.'
  maintainer_pass:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 2 -> 3.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  flow_note: rotor flow exp(t B_Lambda / 2) = exp(kappa_Lambda t u / 2), which rescales the pair (the T05 Thm 6.3 sense), the flow of minus the Killing field X . B_Lambda.
  note: Built at Leon's request (21 October 2026) to supply the boundary-mode algebra that the de Sitter temperature conjecture lacked. The Schwarzschild chain selects the pair's plane by curvature and localises its modes at the singular boundary; at the cosmological horizon curvature selects nothing, the static observer selects the plane, and the pair's two null vectors are the observer's endpoints on conformal infinity.
---

## formal
Let $\Lambda = 3H^{2} > 0$. In the conventions of Lemma \claimref{mass.de-sitter-scale-frozen-point} ($\ip{\nO}{\nInf} = 1$, $X(x) = \nO + x - \tfrac12 Q(x)\,\nInf$), let $I_{\Lambda} = \nInf + \tfrac{\Lambda}{6}\nO$ be the frozen point, $\sigma(x) = \ip{X(x)}{I_{\Lambda}} = 1 - \Lambda Q(x)/12$ the scale, so that $g = \sigma^{-2}\eta$, and $B_{\Lambda} = e_{0}W = H u$ the static Killing generator of the observer at $x = 0$, with $W = \nInf - \tfrac{\Lambda}{6}\nO$, $e_{W} = W/H$, $u = e_{0}e_{W}$ and surface gravity $\kappa_{\Lambda} = H$ (Proposition \claimref{synthesis.de-sitter-static-boost-frozen-point}). Let $S_{\Lambda} = \{x_{0} = 0,\ Q(x) = -12/\Lambda\}$ be the bifurcation sphere and $\Pi_{\Lambda} = \mathrm{span}\{e_{0}, e_{W}\}$ the plane of $B_{\Lambda}$.
\begin{enumerate}
\item[(i)] \emph{Curvature selects no plane.} The curvature of $g$ is constant: on bivectors it is a multiple of the identity ($\Lambda/3$ in the convention of Fact \claimref{dark-energy.imported-frozen-point-geometry}, $P = (\Lambda/6)g$; $-\Lambda/3$ for $R^{a}{}_{bcd} = \partial_{c}\Gamma^{a}_{db} - \cdots$ in signature $(+,-,-,-)$), so every plane is an eigenplane with the one eigenvalue, and nothing singles out a plane as the doubled eigenvalue singles out the pair $\{\sigma_{r}, I\sigma_{r}\}$ at Schwarzschild. The plane of the pair is fixed by the static observer, through $B_{\Lambda}$.
\item[(ii)] \emph{One ambient plane.} At every $s \in S_{\Lambda}$ the differential of $X/\sigma$ maps $(T_{s}M, g)$ isometrically onto $X(s)^{\perp} \cap I_{\Lambda}^{\perp}$, carrying the time direction to $\tfrac12 e_{0}$ and the radial direction $s$ to $(3/\Lambda)W$. Hence the normal plane of $S_{\Lambda}$ at every one of its points is the same ambient plane $\Pi_{\Lambda} \subset I_{\Lambda}^{\perp}$; and $\sigma = 2$ on $S_{\Lambda}$.
\item[(iii)] \emph{The completed pair.} $\Pi_{\Lambda}$ has signature $(1,1)$, $Q(e_{0}) = 1$ and $Q(e_{W}) = -1$, a hyperbolic atom in the sense of Lemma \claimref{singularity.pseudo-inverse-identities-hyperbolic-atom}. The vectors
\[
v_{\Lambda} \;=\; \tfrac12\,(e_{0} + e_{W}), \qquad v_{\Lambda}^{*} \;=\; \tfrac12\,(e_{0} - e_{W})
\]
satisfy $Q(v_{\Lambda}) = Q(v_{\Lambda}^{*}) = 0$, $v_{\Lambda}v_{\Lambda}^{*} + v_{\Lambda}^{*}v_{\Lambda} = 1$ and $v_{\Lambda}^{*}v_{\Lambda} - v_{\Lambda}v_{\Lambda}^{*} = u = B_{\Lambda}/\kappa_{\Lambda}$, and up to a phase (a unit number of $\mathrm{span}\{1, \hat{I}\}$, $\hat{I}$ the central unit of the boundary-mode algebra of obj.synthesis.cosmological-horizon-boundary-modes, $\bar a$ its conjugate) they are the only such pair of vectors of $\Pi_{\Lambda}$ with $v^{*}$ the frame adjoint of $v$ ($e_{0}^{*} = e_{0}$, $e_{W}^{*} = -e_{W}$). By Theorem \claimref{singularity.modular-structure-completed-pair}, with its $\sigma$ equal to $u$: the static Killing flow $\exp(tB_{\Lambda}/2)$ (the flow of $-\xi$, $\xi = X\cdot B_{\Lambda}$ being past-directed at the observer) is the pair's rotor flow at rapidity $\lambda = \kappa_{\Lambda}t$, acting by $v_{\Lambda} \mapsto e^{-\kappa_{\Lambda}t}v_{\Lambda}$ and $v_{\Lambda}^{*} \mapsto e^{\kappa_{\Lambda}t}v_{\Lambda}^{*}$, and for $t > 0$ it carries the observer to the future (the origin to $x = \tfrac{2}{H}\tanh(Ht/2)\,e_{0}$); the boost's spectral projectors are the occupation projectors, and $K := u/2 = N - \tfrac12$.
\item[(iv)] \emph{Anchored at conformal infinity.} $v_{\Lambda}$ and $v_{\Lambda}^{*}$ are orthogonal to $I_{\Lambda}$, and as points of the conformal model
\[
v_{\Lambda} \;=\; -\frac{H}{4}\,X\Bigl(-\frac{2}{H}\,e_{0}\Bigr), \qquad v_{\Lambda}^{*} \;=\; \frac{H}{4}\,X\Bigl(\frac{2}{H}\,e_{0}\Bigr),
\]
the past and future endpoints $i^{-}$ and $i^{+}$ of the static observer's worldline, at $x = \mp\sqrt{12/\Lambda}\,e_{0}$, where $\sigma = 0$: conformal infinity, the locus on which the physical read-out $g = \sigma^{-2}\eta$ fails, and there the Killing flow's two fixed points off the bifurcation sphere. The ladder of the cosmological horizon lies where the scale $\sigma$ is not invertible; the bifurcation sphere, where the Euclidean period is read, is regular.
\item[(v)] \emph{Existence, and the mirror.} A real pair exists exactly when $\Lambda > 0$: for $\Lambda = 0$ the plane of $B_{0} = e_{0}\nInf$ is degenerate, and for $\Lambda < 0$ the plane of $B_{\Lambda}$ is definite and has no real null vectors (its complexification carries a CAR pair generated by a rotation, not a boost). Under reversal of the ambient form ($Q \mapsto -Q$, the signature $(4,2)$ of the mirror), $\Pi_{\Lambda}$ is again a $(1,1)$ plane, $B_{\Lambda}^{2} = \kappa_{\Lambda}^{2}$ is unchanged, and the pair whose occupation boost is $u$ is $w = \tfrac12(e_{0} - e_{W})$, $w^{*} = -\tfrac12(e_{0} + e_{W})$: the same two rays with the ladder reversed, the annihilator at $i^{+}$ and the creator at $i^{-}$, and the flow contracting $w$ at the same rate $\kappa_{\Lambda}$.
\end{enumerate}

## technical
Take a positive cosmological constant $\Lambda = 3H^{2}$ and the static observer at the origin of the flat conformal chart, whose time is generated by the bivector $B_{\Lambda} = H e_{0}e_{W}$ in the plane of $e_{0}$ and the unit Stelle-West direction $e_{W}$. At Schwarzschild the plane of the completed pair is chosen by the curvature, whose doubled eigenvalue picks out the radial plane. De Sitter space has constant curvature, so the curvature picks out nothing, and the plane comes instead from the observer's Killing flow.

That plane is a single plane of the six-dimensional ambient space, orthogonal to the frozen point. It is the normal plane of the bifurcation sphere at every point of the sphere: the tangent-space embedding sends the time direction to $e_{0}/2$ and the radial direction to a multiple of $W$. It has signature $(1,1)$, so it is a hyperbolic atom. Its null vectors $v_{\Lambda} = \tfrac12(e_{0} + e_{W})$ and $v_{\Lambda}^{*} = \tfrac12(e_{0} - e_{W})$ satisfy the canonical anticommutation relations, and their occupation boost $v^{*}v - vv^{*}$ is the unit static boost. Up to a phase this is the only such pair in the plane. The static flow in Killing time $t$ is the pair's boost at rapidity $Ht$: it shrinks $v_{\Lambda}$ by $e^{-Ht}$ and grows $v_{\Lambda}^{*}$ by $e^{Ht}$, the structure the singularity paper proves for its own pair.

As points of the conformal model the two null vectors are the observer's past and future endpoints on conformal infinity, $x = \mp\sqrt{12/\Lambda}\,e_{0}$, where the scale $\sigma$ vanishes and the physical metric $\sigma^{-2}\eta$ cannot be read out. So the horizon's ladder sits where $\sigma$ is not invertible, while the bifurcation sphere ($\sigma = 2$), where the temperature's period is read, is regular, as at Schwarzschild. A real pair exists only for $\Lambda > 0$. In the mirror, where the ambient form is reversed, it exists with the same rate, and the ladder runs the other way: the annihilator sits at $i^{+}$ and the creator at $i^{-}$.

## lay
In a universe with a positive cosmological constant, every observer has a horizon, a sphere beyond which signals can never reach them. For black holes the series builds a pair of quantum modes, a creation and an annihilation operator, out of the geometry, and derives the hole's temperature from them. This result builds the matching pair for the cosmological horizon. For a black hole the shape of the curvature picks out the plane the pair lives in. In this universe the curvature is the same in every direction, so it picks out nothing, and the plane comes from the observer's own clock. The pair turns out to be two points at the edge of the conformal picture of the universe: where the observer's history begins and where it ends. There, infinitely far away, the picture no longer gives physical distances. The observer's clock squeezes one of them and stretches the other at a rate set by the cosmological constant. The mirror world gets the same pair with the two roles swapped.

## one-liner
At a positive cosmological constant, the static observer's boost plane is the horizon's completed pair: its null vectors $v_{\Lambda}, v_{\Lambda}^{*}$ are the observer's endpoints $i^{\mp}$ on conformal infinity, its occupation boost is the static boost, and Killing time acts at rapidity $\kappa_{\Lambda} = \sqrt{\Lambda/3}$.
