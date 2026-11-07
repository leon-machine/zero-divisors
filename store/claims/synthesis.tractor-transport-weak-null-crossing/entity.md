---
id: synthesis.tractor-transport-weak-null-crossing
kind: claim
version: 5
title: 'Tractor transport across a weak null crossing'
status: proved
region: synthesis
subject: interior
tags: [tractors, horizons, kerr, limits, null-directions]
proposed_by:
  kind: ai
  session: colony-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: the transport equation derived from the Cl(2,4) gauge field Omega_T in a D-parallel frame, E and N_v as bivector actions and facts (a) to (c) as Cl(2,4) identities; slot route kept as a labelled reading'
  version: 5
  source: maintainer pass 2026-11-07 (GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review fixes (referee F3): uses edges to the tractor gauge-field theorem and the GTG dictionary; stale pin reviewed'
  version: 5
  source: maintainer pass 2026-11-07 (GTG review fixes)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.imported-tractor-connection@3
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - synthesis.imported-gtg-dictionary@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_general_removal
- kind: check
  ref: check.py::check_null_and_radial_frames
- kind: check
  ref: check.py::check_model_profile
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gtg_tractor_transport_in_cl24
lineage:
  motivated_by:
  - interior.filtration-cauchy-horizon-read-literature
  - interior.imported-mass-inflation-stability
extraction:
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Blind referee F3: accept with one link fix. Applied (10a): the GTG proof writes the transport equation with Omega_T(x) = Omega(x) - ninf ^ gamma + n0 ^ p from Theorem synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection (proved) and reads the parallel frame, the D-parallel velocity and the Schouten map through Fact synthesis.imported-gtg-dictionary (ii), (iii), (v) (imported); both were cited for these steps and missing from uses, now added at versions 1 and 2. No text or check change (the referee recomputed the transport generator, facts (a) to (c), Q-preservation and the gauge identity symbolically in Cl(2,4); two mutations of check_gtg_tractor_transport_in_cl24 fail).'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Stale pin reviewed (fix round, 2026-11-07): interior.imported-tractor-connection 2 -> 3 states the connection first as the Cl(2,4) gauge field D^T of Theorem synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection and names the store curvature convention of its display (the slot display unchanged): notation (N); repinned.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'GTG proof made the main proof: tractors as Cl(2,4) vectors V = sigma ninf + mu + rho n0, transport D^T_{x''} V = 0 with Omega_T(x'') = Omega(x'') - ninf ^ gamma'' + n0 ^ P(gamma''), the Omega(x'') term absorbed by the D-parallel frame, so x'' = A x with E = (ninf ^ gamma'') . and N_v = -(n0 ^ v) . (the statement''s maps); facts (a) N_v N_w V = -sigma (v . w) n0, (b) N_n E N_n = nu N_n, (c) N_n N_R N_n = 0 computed in Cl(2,4); (4) from the Schouten map P(a) = (calR(a) - calR a/6)/2. The analysis (Volterra, Riccati, Wronskian) is unchanged scalar mathematics; the slot form is kept as a labelled reading. New check check_gtg_tractor_transport_in_cl24 (generator against E + N_p and the slot formulas, (a)-(c), metric preservation, the gauge identity, P = (Lambda/6) id); runcheck 4/4, check4 clean on a proposals copy. outside_ga removed: the regularity hypotheses are statements about the rotation-gauge field and the Schouten map along the worldline, and no stand-in remains. Statement, status, links unchanged.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The result is about the regularity of the Christoffel symbols and the Schouten tensor of the derived metric across a weak null singularity (their local square-integrability), properties of components as such.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: tractor wording completed (the transport is that of the Cl(2,4) gauge field of the gravitational field, read in the splitting of the derived metric; the soldering part is the physical frame hb^{-1}(a)); content unchanged.'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Note only: the sign of P_VV in the literature reading is now the store convention, P_VV = -4 pi (d_V phi)^2 (it was the sphere-positive sign), so focusing matter has S <= 0. The formal clauses, proof and checks depend only on |S| and a fixed sign and are unchanged. Version 1 -> 2.'
  open_problem: op.cauchy-horizon-transport
  note: >-
    Tests the heuristic that tractor transport fails at the L^2 threshold of the Christoffel symbols.
    Finding: under the stated hypotheses the threshold for transport is L^1, not L^2; the Schouten
    divergence along a crossing geodesic is removed by a change of splitting along the curve, induced by
    a scale whose logarithm along the curve is log y with y a solution of a Jacobi-type equation; y is
    continuous and positive under the Tipler-type double-integral condition (finite tidal deformation, as
    in Ori's import (iii)); what survives is a one-parameter ambiguity in the nilradical. Whether the known
    Cauchy-horizon solutions satisfy the hypotheses is open. Reading of the imports (argued, not part of
    the proof): in spherical symmetry with a Maxwell field and a massless scalar field, along radial
    causal geodesics the singular part of the Schouten tensor is P_VV dV dV with P_VV = -4 pi (d_V phi)^2
    in the store's curvature convention (Ric = Lambda g for de Sitter in (+,-,-,-), so Ric_VV = -8 pi
    T_VV with T_VV = (d_V phi)^2 in units G = 1; the sphere-positive convention has the opposite sign),
    so focusing matter has S <= 0 and |S| is proportional to (d_V phi)^2 (Maxwell contributes nothing
    to R_VV), the covector dV is parallel up to a continuous factor, and the
    theorem would apply if the remaining components are integrable along the geodesic (d_U phi bounded,
    d_V phi integrable), if the Schouten tensor has no part concentrated on the horizon, and if Levi-Civita
    transport extends continuously; none of this is confirmed against Luk-Oh, whose non-L^2 Christoffels
    do not by themselves give a parallel frame. Generic non-L^2 of d_V phi (to be confirmed as their
    mechanism) is exactly S not integrable, the divergent branch (3). For the vacuum perturbations of Kerr
    (Dafermos-Luk) the Schouten tensor vanishes and clause (4) reduces the tractor question to the
    Levi-Civita one. Non-geodesic and non-radial curves are not covered.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement of the non-tractor language: the causal geodesic is a causal worldline of D-parallel velocity of a gravitational field (hb, Omega) on flat spacetime, the metric is its derived metric, Levi-Civita transport is D-transport, Christoffel symbols are connection components, Ric = Lambda g becomes R(a) = Lambda a; the tractor connection, splitting and nilradical are left in their own language for the lead. Clauses (1)-(4) unchanged; check unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with derived metric $g$, and let $\gamma : [s_0, s_1] \to M$ be a causal worldline of $D$-parallel velocity (a causal geodesic of $g$) with affine parameter $s$, crossing at $s_c \in (s_0, s_1)$ a hypersurface across which the derived metric is continuous, smooth on either side, with no part of the Schouten tensor concentrated on the hypersurface (along $\gamma$, $\Sch(\gamma',\cdot)$ is the locally integrable function given by its values off $s_c$, with no surface layer at $s_c$), and suppose $D$-transport (the Levi-Civita transport of $g$) along $\gamma$ extends continuously across $s_c$, so that a $D$-parallel physical frame along $\gamma$ exists on $[s_0, s_1]$. Write the tractor transport along $\gamma$, the transport of the $\Cl(2,4)$ gauge field $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, in the splitting of the scale $g$ (Fact \claimref{interior.imported-tractor-connection}), in that frame, as $x' = A x$ with $A = E_{\gamma'} + N_{\Sch(\gamma',\cdot)}$, where $E_{\gamma'}$ is the soldering part (the term $-\nInf \wedge \hb^{-1}(x')$, $x'$ the background tangent) and, for a covector $v$, $N_v$ is the nilpotent map $(\sigma, \mu, \rho) \mapsto (0,\, \sigma v,\, -\ip{v}{\mu})$ of the nilradical $\mathfrak g_1$. Suppose
\[
\Sch(\gamma', \cdot) \;=\; S\,\nu\,n + R ,
\]
with $n$ a parallel null covector along $\gamma$, $\nu := n(\gamma') \neq 0$ (constant), $S$ a scalar function and $R$ a covector field with integrable components on $[s_0, s_1]$, and assume the Tipler-type condition $\int_{s_0}^{s_1} |s - s_c|\,|S(s)|\,ds < \infty$. Then:
\begin{enumerate}
\item \emph{(Removal.)} The equation $y'' = \nu^2 S\, y$ has solutions $y$ on $[s_0, s_c)$ and on $(s_c, s_1]$, continuous and positive on $[s_0, s_1]$, with $y'$ integrable (shrinking $[s_0,s_1]$ about $s_c$ if necessary). For any such $y$ put $f := y'/(\nu y)$. In the variables $\hat x := (1 - f N_n)\,x$ the transport equation reads
\[
\hat x' \;=\; \bigl(E_{\gamma'} + N_R + f\,[E_{\gamma'}, N_n]\bigr)\,\hat x ,
\]
whose coefficient is integrable; so the transport across $s_c$ exists and is unique for each such $y$.
\item \emph{(The ambiguity is exactly one nilpotent direction.)} Two such solutions $y_1, y_2$ give transports across $s_c$ that differ by the insertion, at $s_c$, of $\exp(c N_n)$ for a real $c$, and every $c \in \R$ occurs. The transport through the crossing is therefore defined exactly modulo the one-parameter subgroup $\exp(\R N_n)$ of the nilradical attached to the conormal $n$.
\item \emph{(Divergence in the metric's scale.)} If $S$ has a fixed sign near $s_c$ and is not integrable on a side of $s_c$, then $f$ is unbounded there, and in the splitting of $g$ (or of any scale differing from it by a bounded change of splitting) a parallel tractor has bounded components up to $s_c$ only if $\sigma(s_c) = 0$ and $\ip{n}{\mu(s_c)} = 0$: the divergence is in the $\mathfrak g_1$ slot along $n$. If instead $S$ is integrable, $A$ itself is integrable, the transport across is unique, and it is the one given by the solutions $y$ whose derivative is continuous at $s_c$.
\item \emph{(Einstein sides.)} If $\mathcal{R}(a) = \Lambda a$ on both sides (for the derived metric $\Ric = \Lambda g$), then $\Sch = \tfrac12(\Ric - \tfrac{R}{6}g) = \tfrac{\Lambda}{6} g$ by the four-dimensional Schouten formula of Fact \claimref{interior.imported-tractor-connection}, $S = 0$, and tractor transport across $s_c$ exists and is unique exactly when $D$-transport does.
\end{enumerate}

## technical
The question was whether the tractor connection can be integrated along causal curves through a perturbed Cauchy horizon, where the derived metric of the gravitational field is continuous but its Christoffel symbols, the connection components, are not square-integrable and the Schouten tensor blows up. The answer is a sharp form of "it fails in a nilpotent slot". Along a crossing geodesic, suppose the non-integrable part of the Schouten term is a rank-one null piece $S\nu n$ along a parallel null covector $n$ (the conormal of the crossed null hypersurface), and that $S$ obeys a Tipler-type double-integral condition. A change of splitting along $\gamma$ by the nilpotent element $f N_n$ (the one induced by a scale whose logarithm along $\gamma$ is $\log y$), with $f$ the logarithmic derivative of a solution of the Jacobi-type equation $y'' = \nu^2 S y$, removes the singular piece exactly: the transformed coefficient is integrable, so the transport across the crossing exists. The solution $y$ is continuous but its derivative diverges at the crossing, and continuing it across involves one free constant; that constant changes the transport by an element of the one-parameter group $\exp(\R N_n)$, and by nothing else. In the metric's own splitting the components blow up in exactly that direction. The hypotheses (continuous Levi-Civita transport, a rank-one null divergence along a parallel covector, the Tipler-type bound, no surface layer) are not yet confirmed for the known perturbed Cauchy-horizon solutions, whose Christoffel symbols fail to be square-integrable; that failure alone does not supply a parallel frame. In vacuum (or with a cosmological constant) the Schouten tensor is a multiple of the metric, there is no singular piece, and the tractor transport problem is that of $D$-transport.

The exact checks verify the gauge identity for fixed rational frames, causal tangents and null conormals, the two explicit frames (a null generator and a radial timelike crossing), and an explicit profile with $|S| \sim |s - s_c|^{-3/2}$, non-integrable while $|s - s_c||S|$ is integrable.

## lay
Inside charged and rotating black holes there is an inner horizon where infalling radiation piles up. The gravitational field stays continuous there, but its rates of change blow up. The programme's main tool for carrying structure along a path, the tractor transport, contains one more derivative than ordinary parallel transport, so one might expect it to fail outright. This result shows it survives along a path, provided three conditions hold there: ordinary parallel transport passes the horizon, the blow-up is concentrated in a single null direction, and it is of the weak kind that leaves infalling objects with finite tidal stretching. Then, after a suitable change of description along the path, the transport goes through. Whether the known models of perturbed inner horizons meet these conditions is not yet confirmed. What is lost is a single number, a one-parameter freedom in how the transport continues past the horizon, and it sits exactly in the nilpotent part of the symmetry algebra where the series expected the damage to be.

## one-liner
Along a causal free-fall worldline with continuous $D$-transport crossing a hypersurface where the Schouten divergence is a null rank-one piece along a parallel covector with finite Tipler integral and no surface layer, tractor transport exists after a change of splitting given by a Jacobi equation and is defined exactly modulo $\exp(\R N_n)$, a one-parameter subgroup of the nilradical; it diverges in that slot in the metric's own scale.
