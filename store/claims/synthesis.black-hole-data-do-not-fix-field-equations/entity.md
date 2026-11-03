---
id: synthesis.black-hole-data-do-not-fix-field-equations
kind: claim
version: 6
title: The series' black-hole thermodynamics holds unchanged in every Ricci-polynomial extension of Einstein's theory, so on its own it cannot yield Einstein's equations
status: proved
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, hawking-temperature, horizons, no-go, schwarzschild]
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
  - synthesis.quarter-from-temperature@1
  - scrambling.mode-count@2
  - singularity.rate-discharge-hypothesis-iii@4
  - synthesis.imported-wald-noether-charge-entropy@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_black_hole_data
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.quarter-from-temperature
extraction:
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the lay level now states hypothesis (W), Wald entropy, as a condition, as clause (ii) of the formal statement does. Version 2 -> 3.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: Wald''s entropy formula, cited from memory, is now the imported Fact synthesis.imported-wald-noether-charge-entropy, added to uses and cited in the statement, proof and check; (W), that this is the horizon entropy, stays the stated reading. The remark cites Jacobson 1995 as the imported Fact synthesis.imported-jacobson-clausius-1995 in text only (it is not a premise). Version 1 -> 2.'
  open_problem: ein.clausius-route
  note: >-
    Locates the step at which a Clausius derivation of Einstein's equations from the series fails. Every
    input the series has (the boundary modes' temperature under (P) and (R), the count under (C1) and (C2),
    Hawking's integral of dM/T) is a statement about stationary vacuum black holes, and those data are shared by
    a continuum of inequivalent theories. Jacobson's derivation (Fact synthesis.imported-jacobson-clausius-1995) escapes this because it imposes the Clausius relation on local Rindler horizons crossed by
    matter, where the Ricci tensor is nonzero; the series has no entropy statement there. Hypothesis (W) reads horizon entropy as Wald's Noether-charge entropy, whose formula is the imported Fact synthesis.imported-wald-noether-charge-entropy. That
    f = beta R_ab R^ab gives fourth-order field equations is K. S. Stelle, Phys. Rev. D 16 (1977) 953 (cited from
    memory). A decision for Leon, recorded in the findings: the Clausius route needs a new premise placing boundary
    modes, with a fixed density per Planck area, on every local Killing horizon (not only on the stretched
    singularity). Transport-absent.
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Lagrangians L_f are densities of a gravitational field on flat spacetime, f a polynomial in the Ricci map of the field strength, with field equations from varying hb with Omega the torsion-free field of hb (equivalently, varying the derived metric); Ricci-flat metrics are vacuum fields, Schwarzschild and Reissner-Nordstrom are the corresponding fields, and flat space is a region of vanishing field strength. Signature (-,+,+,+) kept as declared. Clauses (i) to (iv), the remark and their strength unchanged; proof given a pointer to the dictionary Fact. check_black_hole_data strengthened: kappa and horizon derived from f, Hawking integral computed and compared with A/4 at five masses, Wald (ii) for Einstein part and two quadratic monomials, RN horizon value computed; docstring names (iii) as untested. Version 4 -> 5. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 5 -> 6.'
---

## formal
Conventions: signature $(-,+,+,+)$ with the Ricci tensor positive on spheres (in the store's $(+,-,-,-)$ convention the signs of the mixed Ricci components below flip). For a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), let $L_{f} = (R - 2\Lambda)/16\pi G + f$ with $\Lambda = 0$, a Lagrangian density (with the weight $\det(\hb)^{-1}$), where $R$ is the scalar curvature and $f$ is a polynomial in the components of the Ricci tensor, the Ricci map of the field strength (indices contracted with the derived metric), every monomial of which has degree at least two in the Ricci tensor; its field equations are those obtained by varying $\hb$ with $\Omega$ the torsion-free field of $\hb$, equivalently by varying the derived metric; $f = 0$ is Einstein's theory.
\begin{enumerate}
\item[(i)] Every vacuum field (Ricci-flat derived metric, vanishing Ricci map) solves the field equations of every $L_{f}$. The Schwarzschild field is a vacuum field, with horizon locus $r = 2M$, surface gravity $1/4M$, interior and Kretschmann scalar $K = 48M^{2}/r^{6}$ independent of $f$; so the surface $2M/r^{3} = 1$ on which (C1) places the boundary modes is the curvature level $\sqrt{K/12} = 1$, and a region where the field strength vanishes has no such surface.
\item[(ii)] Assume (W): horizon entropy is Wald's Noether-charge entropy (Fact \claimref{synthesis.imported-wald-noether-charge-entropy}). Then the Schwarzschild horizon has entropy $A/4G$ under every $L_{f}$, since the Ricci-dependent part of the Wald functional vanishes where the Ricci tensor does.
\item[(iii)] Hence, without (W), every black-hole input of the series takes the same value under every $L_{f}$, since each is a statement about the geometry: the boundary modes' temperature $1/8\pi M$ under (P) and (R) (Theorem \claimref{singularity.rate-discharge-hypothesis-iii}), the count $N = 8\pi\nu M\,\Delta t$ under (C1) and (C2) (Theorem \claimref{scrambling.mode-count}), and Hawking's integral $S = \int dM/T = 4\pi M^{2} = A/4$ (Proposition \claimref{synthesis.quarter-from-temperature}). Their field equations with matter differ from Einstein's whenever $f \neq 0$ (for $f = \beta R_{ab}R^{ab}$ they are of fourth order), so no derivation that uses only these inputs, the Clausius relation along the Schwarzschild family included, can yield Einstein's equations. (W) adds only that Wald's entropy agrees, by (ii).
\item[(iv)] What separates the theories is a horizon with matter on it. At the horizon of the Reissner-Nordstr\"om field $R^{t}{}_{t} = R^{r}{}_{r} = -Q^{2}/r^{4} \neq 0$, and under (W) the term $f = \beta R_{ab}R^{ab}$ adds $4\pi\beta\,(R^{t}{}_{t} + R^{r}{}_{r})\,A$ to the entropy, which is nonzero there.
\end{enumerate}
\emph{Remark (not part of the proved statement).} Jacobson's derivation (Fact \claimref{synthesis.imported-jacobson-clausius-1995}) imposes the Clausius relation on local Rindler horizons crossed by a matter flux, at every point and null direction, where the Ricci tensor is nonzero. A survey of the store finds no entropy statement for such non-Killing local horizons: (R) concerns stationary Killing horizons, and (C1) puts the black hole's boundary modes only where the curvature reaches the Planck scale. The store does place boundary modes at sub-Planckian curvature on de Sitter's cosmological horizon, but that is again a Killing horizon, so the conclusion concerns local non-Killing horizons only. Filed alongside, synthesis.clausius-route-newton-constant-is-residue, which locates the same missing step on Jacobson's own route.

## technical
The series' thermodynamic inputs are all about stationary black holes in vacuum: the boundary modes' temperature, which (R) fixes at $1/8\pi M$; the count of boundary modes on the stretched singularity, which (C1) places where the curvature reaches the Planck scale; and Hawking's integral of $dM/T$, which gives a quarter of the area. Add to Einstein's Lagrangian any polynomial in the Ricci tensor of degree at least two. The Schwarzschild field still solves the new field equations, read as equations for the gravitational field on flat spacetime, because each new term vanishes with the Ricci tensor, and assuming Wald's entropy formula its horizon entropy is still a quarter of the area. So all of the series' inputs, and every relation among them, hold equally in a whole family of theories whose field equations with matter are not Einstein's. Einstein's equations cannot follow from them on their own. Jacobson's derivation avoids this by imposing the heat relation on small local horizons with matter flowing through them, where the Ricci tensor is not zero and the theories' entropies differ; the store has no entropy statement for such non-Killing local horizons: the black hole's modes sit where curvature is Planckian, and the de Sitter horizon's sit on a Killing horizon.

## lay
The series has three facts about black holes: their temperature, how many quantum modes they hold, and Hawking's argument that turns the temperature into an entropy. A whole family of theories of gravity, differing from Einstein's in how matter sources the gravitational field, has exactly the same black holes, with the same temperature and, if horizon entropy is given by the standard (Wald) rule, the same entropy. So those three facts, on their own, cannot single out Einstein's equations. The known derivation of Einstein's equations from thermodynamics works because it applies the heat law to tiny horizons that matter is flowing through. The series does not yet say what entropy such a horizon has, and that is the step it would need to supply.

## one-liner
Every Lagrangian $R/16\pi G + f(\mathrm{Ric})$ with $f$ at least quadratic in the Ricci tensor shares the Schwarzschild field, its temperature, its (C1) surface and (assuming Wald entropy) its entropy $A/4G$, so the series' black-hole inputs on their own cannot yield Einstein's equations; what would separate the theories is entropy on local horizons crossed by matter, where the Ricci tensor is nonzero.
