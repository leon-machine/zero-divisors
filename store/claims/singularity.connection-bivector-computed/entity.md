---
id: singularity.connection-bivector-computed
kind: claim
version: 4
title: The connection bivector, computed
status: proved
region: singularity
subject: singularity
tags: [schwarzschild]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:2.3
- kind: check
  ref: check.py::check_beta_identities_in_q_r_beta
- kind: check
  ref: check.py::check_stated_connection_solves_torsion_uniquely
- kind: check
  ref: check.py::check_connection_on_radial_plane
locators:
  paper: T05
  number: Prop 2.3
  label: prop:omega
  line: 1351
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: beta'' = -beta/2r and beta beta'' = -M/r^2 in Q(r)[beta], the stated Omega as the unique torsion-free solution in GA at six points, and Omega(e_t) = (M/r^2) sigma_r, Omega(e_r) = (beta/2r) sigma_r. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: proposition
  unresolved_refs:
  - rem:frame
  eqrefs: 3
  typing:
    by: ai-typing-pass
    note: 'no store references in the statement or proof; the only reference is an unresolved remark fixing a sign convention, which is not a premise'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the coframe is the physical-vector map hb^{-1} of the PG gauge field hb = 1 - beta P in components; the connection one-forms are the components of the rotation-gauge field Omega solving the torsion condition; the coordinate directions d_t, d_r are the background directions on which Omega(a) is evaluated; curvature scale becomes field-strength scale. Values unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
For the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$ of Fact \claimref{sheaf.gauge-field-cometric} on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), whose physical-vector map in components is the coframe \eqref{eq:pgcoframe}, $\theta^a(v) = \gamma^a \cdot \hb^{-1}(v)$, write $\sigma_r$ for the unit radial boost bivector of that coframe (the sign convention is fixed once, in Remark \ref{rem:frame}; the verification script fixes it by computation). Then:
\begin{enumerate}
\item all connection data is algebraic in $(r, \beta)$: $\beta' = -\beta/2r$ and $\beta\beta' = -M/r^2$ exactly, so every coefficient below lies in the field $\mathbb{Q}(r)[\beta]$ with $\beta^2 = 2M/r$;
\item the torsion condition of \eqref{eq:gtgfield} is solved by the rotation-gauge field $\Omega$ whose components in this coframe are the connection one-forms
\[
\omega^1{}_0 = -\beta'\,\theta^1, \qquad
\omega^2{}_0 = -\tfrac{\beta}{r}\,\theta^2, \qquad
\omega^3{}_0 = -\tfrac{\beta}{r}\,\theta^3, \qquad
\omega^2{}_1 = \tfrac{1}{r}\,\theta^2, \qquad
\omega^3{}_1 = \tfrac{1}{r}\,\theta^3, \qquad
\omega^3{}_2 = \tfrac{\cot\vartheta}{r}\,\theta^3,
\]
verified by substitution in the first structure equations: $d\theta^0 = 0$ and $-\omega^0{}_1 \wedge \theta^1 = \beta'\,\theta^1 \wedge \theta^1 = 0$; $d\theta^1 = \beta'\,dr\wedge dt = \beta'\,\theta^1\wedge\theta^0 = -\,\omega^1{}_0\wedge\theta^0$; and $d\theta^2 = \tfrac1r\,dr\wedge\theta^2 = \tfrac1r(\theta^1 - \beta\theta^0)\wedge\theta^2 = -\,\omega^2{}_0\wedge\theta^0 - \omega^2{}_1\wedge\theta^1$, with the $\theta^3$ leg the round sphere's standard connection;
\item evaluated on the background directions $\partial_t$, $\partial_r$ of the $(t,r)$ plane, the connection bivector is
\[
\Omega(\partial_t) \;=\; -\beta\beta'\,\sigma_r \;=\; \frac{M}{r^2}\,\sigma_r ,
\qquad
\Omega(\partial_r) \;=\; -\beta'\,\sigma_r \;=\; \frac{\beta}{2r}\,\sigma_r \;=\; \sqrt{\frac{M}{2r^3}}\;\sigma_r :
\]
the time-direction connection is the Newtonian field $M/r^2$, exactly and at every radius, and the radial-direction connection diverges as $r \to 0$ at the rate $r^{-3/2}$, the square root of the field-strength scale $M/r^3$.
\end{enumerate}

## technical
For the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$ on flat spacetime, with coframe the components of $\hb^{-1}$ and $\beta^2 = 2M/r$, all connection data is algebraic in $(r,\beta)$: $\beta' = -\beta/2r$ and $\beta\beta' = -M/r^2$, so every coefficient lies in $\mathbb{Q}(r)[\beta]$. The torsion condition of the gauge-theory field equations is solved by the rotation-gauge field with explicit connection one-forms as components, for example $\omega^1{}_0 = -\beta'\,\theta^1$, $\omega^2{}_0 = -(\beta/r)\,\theta^2$ and $\omega^2{}_1 = \theta^2/r$, each checked by substitution in the first structure equations.

On the background directions of the $(t,r)$ plane the connection bivector is $\Omega(\partial_t) = (M/r^2)\,\sigma_r$ and $\Omega(\partial_r) = \sqrt{M/2r^3}\,\sigma_r$, with $\sigma_r$ the unit radial boost bivector. The time-direction connection is exactly the Newtonian field at every radius, and the radial-direction connection diverges as $r^{-3/2}$ when $r \to 0$, the square root of the field-strength scale $M/r^3$.

## lay
In the gauge-theory description of gravity, the connection records how local frames boost and rotate from point to point. For a non-rotating black hole in this gauge it can be written down exactly. Along the time direction it equals Newton's gravitational field strength, mass over radius squared, at every radius; along the radial direction it grows without bound towards the centre, at the square root of the rate at which the field strength grows.

## one-liner
In the Painlev\'e-Gullstrand gauge the connection bivector is exactly $(M/r^2)\,\sigma_r$ along $\partial_t$ and $\sqrt{M/2r^3}\,\sigma_r$ along $\partial_r$.
