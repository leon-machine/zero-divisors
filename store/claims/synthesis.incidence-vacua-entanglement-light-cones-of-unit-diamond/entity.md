---
id: synthesis.incidence-vacua-entanglement-light-cones-of-unit-diamond
kind: claim
version: 2
title: 'Incidence vacua are maximally entangled on the unit diamond''s light cones'
status: proved
region: synthesis
subject: conformal-spacetime
tags: [entanglement, conformal-model, modular-theory, spinor-modules, needs-continuum]
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
derivations:
- name: main
  uses:
  - synthesis.incidence-vacua-thermofield-real-capacity@6
  - state-selection.partner-purification-are-canonical@4
  - one-relation.spacetime-manifold-vacuum-lines@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_incidence_entanglement
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.incidence-vacua-thermofield-real-capacity
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Subject moved from thermality to conformal-spacetime (DECISIONS H12, xsubject-R02 item 6): its logical neighbours are in conformal-spacetime (I213). Not a substantive field; no version change.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  open_problem: ein.entanglement-equilibrium
  note: >-
    A cross-reading of Jacobson's entanglement-equilibrium setting (T. Jacobson, Phys. Rev. Lett. 116 (2016)
    201101, cited from memory), whose data at a point are a unit timelike vector and a small radius, the ball's
    causal diamond carrying the entanglement. In the incidence chart the Hermitian structure supplies one such
    datum: the frame e_1 and the unit radius; the entanglement of the two distinguished vacua is stationary
    exactly on the light cones of the diamond's tips and, on the slice t = 0, maximal exactly on the unit sphere.
    The same result is an obstruction for the target: the profile depends on the point only through u and v,
    there is one radius and one frame (boosts and dilations are not unitary), and no metric enters, so the
    variation at fixed volume from which Jacobson extracts the field equations has nothing to act on in the
    flat chart; a curved version would need the incidence vacua carried by transport. Transport-convenient.
---

## formal
In the setting of Theorem \claimref{synthesis.incidence-vacua-thermofield-real-capacity}: $\Cl(2,4)$ on its Fock module with every generator unitary, a point $x = te_{1} + re_{2}$ ($r \geq 0$ after a spatial rotation), $u = t - r$, $v = t + r$, and the distinguished vacua $\Omega_{x} = (1 - u\,a^{*}b^{*})\ket{0}_{+}$, $\Psi_{x} = (b^{*} - v\,a^{*})\ket{0}_{-}$ of the incidence line (Proposition \claimref{one-relation.spacetime-manifold-vacuum-lines}).
\begin{enumerate}
\item[(i)] \emph{(Profile.)} The entanglement entropy of the ascent mode with the boost qubit $b = b(x)$ is $S_{\Omega}(x) = s(u)$ in $\Omega_{x}$ and $S_{\Psi}(x) = s(v)$ in $\Psi_{x}$, where $s(w) = \ln(1 + w^{2}) - n\ln w^{2}$ and $n = w^{2}/(1 + w^{2})$ is the ascent occupation. The partner $b(x)$ is the boost-qubit mode of the $(t, r)$ plane through $x$, so it depends on the spatial direction of $x$: the profile compares entanglements with different partners at different points. Since each marginal is the Gibbs state of the fixed number operator $N$ at $e^{-\beta} = w^{2}$, the Gibbs identity for a one-parameter family of Gibbs states of one Hamiltonian gives $ds/dw = \beta\,dn/dw$, $\beta = -\ln w^{2}$; this is a property of such families, not of the incidence chart. So $s$ is stationary exactly at $w = 0$, where it vanishes, and at $w^{2} = 1$, where it is maximal, $s = \ln 2$; it increases with $|w|$ on $[0, 1]$ and decreases beyond.
\item[(ii)] \emph{(The light cones of the unit diamond.)} $\Omega_{x}$ is maximally entangled exactly on $\{|u| = 1\}$, the future light cones of $\pm e_{1}$, and $\Psi_{x}$ exactly on $\{|v| = 1\}$, their past light cones; only the union $\{|u| = 1\}\cup\{|v| = 1\}$ is the union of the light cones of the two events $\pm e_{1}$. These are the tips of the causal diamond of the unit ball $\{t = 0,\ r \leq 1\}$; on its null boundary $\Omega_{x}$ is maximally entangled on the past part ($u = -1$) and $\Psi_{x}$ on the future part ($v = 1$). On the slice $t = 0$ both entropies equal $s(r)$, zero at the centre, increasing to $\ln 2$ on the unit sphere $r = 1$, decreasing outside.
\item[(iii)] \emph{(Fixed by the Hermitian structure.)} Boosts of the $(t, r)$ plane rescale $u$ and $v$ oppositely and dilations rescale both, so neither preserves the maximal set; their generators $e_{1}e_{2}$ and $e_{+}e_{-}$ are self-adjoint for the Hermitian structure, so the groups they generate are not unitary. The diamond, its radius and its rest frame $e_{1}$ are therefore determined by the Hermitian structure, and the profile depends on $x$ only through $u$ and $v$.
\end{enumerate}

## technical
At each point of spacetime the series attaches a line of vacuum states, spanned by two distinguished ones in which the added ascent mode is entangled with spacetime's own boost qubit. That entanglement depends on the point only through the null coordinates: it is $s(u) = \ln(1 + u^{2}) - \frac{u^{2}}{1 + u^{2}}\ln u^{2}$ for one vacuum and $s(v)$ for the other. Because each marginal is a Gibbs state of one fixed number operator, it obeys the Gibbs identity $ds = \beta\,dn$, with $\beta = -\ln u^{2}$ the inverse temperature of the thermofield double, and it is maximal, one bit, exactly where $\beta = 0$: for the first vacuum on the future light cones, for the second on the past light cones, of the two events one unit of time before and after the origin. The partner mode changes with the spatial direction of the point. Those cones bound the causal diamond of the unit ball, and on the ball itself the entanglement grows from zero at the centre to its maximum on the bounding sphere. The unit of length and the time direction are fixed by the module's Hermitian structure, since boosts and dilations are not unitary for it. The picture echoes Jacobson's entanglement-equilibrium setting, a small ball in a chosen rest frame with its entanglement at the edge, but it has one size, one frame and no metric, so it cannot by itself yield field equations.

## lay
The series attaches to every point of spacetime a small family of quantum states. In the two special members of that family, an extra quantum mode is entangled with a mode that belongs to spacetime itself, by an amount that depends on where the point is. Working this out exactly, the entanglement is largest, one full bit, precisely on the light cones of two events, one unit of time before and after the origin. Those light cones are the edges of the region a signal can cross inside a ball of unit size, and across that ball the entanglement grows from nothing at the centre to its maximum at the edge. This echoes a known derivation of Einstein's equations from entanglement in small balls, but here the ball has one fixed size and orientation and no geometry can bend it, so the echo does not yet give those equations.

## one-liner
In the two distinguished incidence vacua the ascent-boost entanglement is $s(u) = \ln(1 + u^{2}) - \frac{u^{2}}{1 + u^{2}}\ln u^{2}$ and $s(v)$, maximal exactly on $|u| = 1$ and $|v| = 1$, which together are the light cones of $\pm e_{1}$, the tips of the unit causal diamond that the Hermitian structure fixes.
