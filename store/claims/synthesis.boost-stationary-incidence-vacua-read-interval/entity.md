---
id: synthesis.boost-stationary-incidence-vacua-read-interval
kind: claim
version: 2
title: 'Boost-stationary incidence vacua read the Lorentz interval'
status: proved
region: synthesis
subject: one-relation
tags: [needs-continuum]
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
  - synthesis.incidence-vacua-thermofield-real-capacity@5
  - one-relation.spacetime-manifold-vacuum-lines@6
  - singularity.descended-form-state-independent@4
  - std-algebra.bivector-exponential@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_boost_maps_lines_and_fixes_ascent
- kind: check
  ref: check.py::check_boost_stationary_section
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.incidence-vacua-thermofield-real-capacity
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.bivector-exponential where the proof uses them. Version 1 -> 2.'
  open_problem: op.which-capacity
  note: Partial progress. Under the positive Hermitian structure g* = g^{-1} (not Spin(2,4)-invariant), imposes on the incidence vacua constancy of the ascent marginal along boost orbits, in analogy with the stationarity of the Unruh state (the boost is not unitary here, so this is not invariance under a unitary flow), and finds that it fixes the ascent marginal (e^{-beta} = |Q(x)|) and forces the complex-only spectator into the purification away from t = 0 and r = 0. Transport-convenient (conformal model and Fock module only; no transport input). It does not connect the incidence vacua to the selected (descended) state of the boundary modes. For the two spanning vacua alone beta = 2 pi sits on the null hyperplanes |u| = e^{-pi} or |v| = e^{-pi}; the boost-constant reading puts it on the hyperboloid |Q| = e^{-2 pi}, in the units and about the origin that the Hermitian structure fixes.
---

## formal
Use the setting of Theorem \claimref{synthesis.incidence-vacua-thermofield-real-capacity}: $\Cl(2,4)$ on its Fock module with the positive Hermitian structure $g^{*} = g^{-1}$ for every generator, which is not $\Spin(2,4)$-invariant (clause (iv) of that theorem: boosts, translations and dilations are not unitary for it, so the units and the origin are fixed by it; under the invariant twistor form of signature $(2,2)$ the lines of real points are null and carry no states, filed alongside, synthesis.twistor-form-states-only-off-the-real-slice), the ascent mode $a = \nO$ with $N = a^{*}a$, the boost qubit $b$, the spectator $c$, a point $x = t e_{1} + r e_{2}$ with $u = t - r$, $v = t + r$, $Q(x) = uv$, the incidence line $L_{x}$ (the kernel of $X(x)$ on one chirality half), and its spanning vacua $\Omega_{x} = (1 - u\,a^{*}b^{*})\ket{0}_{+}$, $\Psi_{x} = (b^{*} - v\,a^{*})\ket{0}_{-}$. Put $f(s) = s/(1+s)$ and let $S_{\lambda} = \exp(\lambda e_{1}e_{2}/2)$ be the boost of the $(t,r)$ plane.
\begin{enumerate}
\item[(i)] \emph{(Boosts move lines and fix the ascent mode.)} $S_{\lambda}$ commutes with $N$, is not unitary for the Hermitian structure, and $S_{\lambda}X(x)S_{\lambda}^{-1} = X(x_{\lambda})$, where $x_{\lambda}$ has null coordinates $e^{\lambda}u$ and $e^{-\lambda}v$; so $S_{\lambda}$ maps $L_{x}$ onto $L_{x_{\lambda}}$, and the ascent occupation is one observable along the whole boost orbit $\{x_{\lambda}\}$.
\item[(ii)] \emph{(Occupation on the line.)} For $\phi = \lambda_{1}\Omega_{x} + \mu\Psi_{x}$, $\langle N\rangle_{\phi} = \dfrac{|\lambda_{1}|^{2}u^{2} + |\mu|^{2}v^{2}}{|\lambda_{1}|^{2}(1 + u^{2}) + |\mu|^{2}(1 + v^{2})}$.
\item[(iii)] \emph{(Boost-constancy fixes the marginal.)} The intersection, over the boost orbit of $x$, of the occupation segments $[\min, \max]\{f(u_{\lambda}^{2}), f(v_{\lambda}^{2})\}$ is the single value $f(|Q(x)|)$. Hence a section $x \mapsto \phi_{x} \in L_{x}$ whose ascent marginal is constant along every boost orbit has, at every $x$, the Gibbs marginal with $e^{-\beta(x)} = |Q(x)|$ (the ascent vacuum on the light cone $Q = 0$); such sections exist.
\item[(iv)] \emph{(Boost-constancy uses the spectator.)} If $|u| \ne |v|$, the vacua on $L_{x}$ with $\langle N\rangle = f(|Q(x)|)$ are exactly $\lambda_{1}\Omega_{x} + \mu\Psi_{x}$ with $|\lambda_{1}|^{2}|u| = |\mu|^{2}|v|$; each has $\lambda_{1}\mu \ne 0$, so its $(a,b)$ state is mixed, of purity $(w_{1}^{2} + w_{2}^{2})/(w_{1} + w_{2})^{2}$ with $w_{1} = |v|(1 + u^{2})$, $w_{2} = |u|(1 + v^{2})$, and the ascent mode is purified by the boost qubit and the complex-only spectator jointly. Only at the points $|u| = |v|$ ($t = 0$ or $r = 0$), one on each orbit off the light cone, may a boost-constant section be pure on $(a,b)$.
\item[(v)] \emph{(Where $2\pi$ sits.)} On a boost-constant section $\beta(x) = -\ln|Q(x)|$, in the units and about the origin the Hermitian structure fixes, so $\beta = 2\pi$ holds exactly on the hyperboloid $|Q(x)| = e^{-2\pi}$, and no boost-constant section has the same $\beta$ on two orbits with different $|Q|$.
\end{enumerate}
So a reading of the incidence vacua whose ascent marginal is constant along boost orbits (in analogy with, not an instance of, the stationarity of the Unruh state, since the boost is not unitary here) reads both capacities at once: its thermal content sits on the real hyperbolic planes and its purification on the real pair together with the complex-only spectator. Its inverse temperature is a function of the Lorentz interval, not a constant rapidity period.

## technical
Under the positive Hermitian structure, for which the boost is not unitary, the boost of the $(t,r)$ plane commutes with the ascent number operator and carries each incidence line to the line of the boosted point, rescaling the null coordinates oppositely. Along a boost orbit the product $uv$ is fixed, so the occupation segment $[f(u^{2}), f(v^{2})]$ at each point always contains $f(|uv|)$, and it collapses to that value where $|u| = |v|$. A section whose ascent marginal is constant along the orbits therefore has ascent Boltzmann factor $|Q(x)|$, the Lorentz interval in the units and about the origin that the Hermitian structure fixes. The vacua achieving it superpose the two spanning thermofield doubles with weights $|\lambda_1|^2 |u| = |\mu|^2 |v|$, which entangles the real pair with the complex-only spectator except on $t = 0$ or $r = 0$. The inverse temperature $-\ln|Q|$ equals $2\pi$ on one hyperboloid only.

## lay
At each point of spacetime the series has a line of candidate vacuum states, and some of them look thermal to the extra mode of the conformal model. Asking that this thermal reading not change as one moves along the paths a uniformly accelerating observer follows picks out a definite family. Its temperature depends only on the spacetime interval from the origin, in the units and about the origin that the construction fixes, and it needs both kinds of mode the algebra has, the real ones and the one that exists only with complex numbers.

## one-liner
Under the positive Hermitian structure, incidence vacua with ascent marginal constant along boost orbits have ascent Boltzmann factor $|Q(x)|$ and, off $t = 0$ and $r = 0$, entangle the real pair with the complex-only spectator.
