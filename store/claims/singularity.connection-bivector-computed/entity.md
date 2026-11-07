---
id: singularity.connection-bivector-computed
kind: claim
version: 5
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
- name: Claude Opus 5.5
  role: GA rewrite (connection one-forms as the bivectors Omega(hb(gamma_c)))
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
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
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA: clause (2) now states the rotation-gauge field on the physical frame, omega(gamma_1) = -beta'' sigma_r, omega(gamma_2) = (beta gamma_0 + gamma_1) ^ gamma_2 / r, omega(gamma_3) = (beta gamma_0 + gamma_1) ^ gamma_3 / r + (cot theta / r) gamma_2 ^ gamma_3, omega(gamma_0) = 0, as the solution of the torsion equation hb^T(grad ^ f^a) = sum_b gamma^b ^ (omega(gamma_b) . gamma^a), the first structure equations read through hb^T; the one-forms stay as a labelled component reading; technical level and proof likewise. Equivalence checked exactly with lib/GA.py and lib/gtg.py in the maintainer scratch: at the six sample points of the check the bivectors assembled from the stored one-forms equal these closed forms and satisfy the GA structure equation (the opposite sign fails). Values unchanged. Orientation (reader R06): sigma_r = gamma_1 gamma_0 is stated beside the GA display.'
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
\item the torsion condition of \eqref{eq:gtgfield}, read on the physical frame, is $\hb^{T}(\nabla\wedge f^a) = \sum_b \gamma^b\wedge\bigl(\omega(\gamma_b)\cdot\gamma^a\bigr)$ for the background vector fields $f^a$ with $\hb^{T}(f^a) = \gamma^a$ (the coframe as background vectors: $f^0 = \nabla t$, $f^1 = \beta\nabla t + \nabla r$, $f^2 = r\nabla\vartheta$, $f^3 = r\sin\vartheta\,\nabla\varphi$), with $\omega(\gamma_b) := \Omega(\hb(\gamma_b))$; it is solved by the rotation-gauge field
\[
\omega(\gamma_0) = 0, \qquad
\omega(\gamma_1) = -\beta'\,\sigma_r, \qquad
\omega(\gamma_2) = \tfrac{1}{r}\,(\beta\gamma_0 + \gamma_1)\wedge\gamma_2, \qquad
\omega(\gamma_3) = \tfrac{1}{r}\,(\beta\gamma_0 + \gamma_1)\wedge\gamma_3 + \tfrac{\cot\vartheta}{r}\,\gamma_2\wedge\gamma_3,
\]
with $\sigma_r = \gamma_1\gamma_0$, the image of $e_re_t$ (the orientation of the dictionary, for which the surface gravity is $+1/4M$), verified by substitution: $\nabla\wedge f^0 = 0$, and with $\hb^{T}(\nabla r) = \gamma^1 - \beta\gamma^0$, $\hb^{T}(\nabla\wedge f^1) = \beta'\,\gamma^1\wedge\gamma^0$ and $\hb^{T}(\nabla\wedge f^2) = \tfrac1r(\gamma^1 - \beta\gamma^0)\wedge\gamma^2$, which are the right sides for the displayed $\omega$, the $\gamma_3$ leg being the round sphere's standard connection (in components, a labelled reading: these are the connection one-forms $\omega^1{}_0 = -\beta'\,\theta^1$, $\omega^2{}_0 = -\tfrac{\beta}{r}\,\theta^2$, $\omega^3{}_0 = -\tfrac{\beta}{r}\,\theta^3$, $\omega^2{}_1 = \tfrac{1}{r}\,\theta^2$, $\omega^3{}_1 = \tfrac{1}{r}\,\theta^3$, $\omega^3{}_2 = \tfrac{\cot\vartheta}{r}\,\theta^3$, solving the first structure equations $d\theta^a = -\omega^a{}_b\wedge\theta^b$ of the coframe);
\item evaluated on the background directions $\partial_t$, $\partial_r$ of the $(t,r)$ plane, the connection bivector is
\[
\Omega(\partial_t) \;=\; -\beta\beta'\,\sigma_r \;=\; \frac{M}{r^2}\,\sigma_r ,
\qquad
\Omega(\partial_r) \;=\; -\beta'\,\sigma_r \;=\; \frac{\beta}{2r}\,\sigma_r \;=\; \sqrt{\frac{M}{2r^3}}\;\sigma_r :
\]
the time-direction connection is the Newtonian field $M/r^2$, exactly and at every radius, and the radial-direction connection diverges as $r \to 0$ at the rate $r^{-3/2}$, the square root of the field-strength scale $M/r^3$.
\end{enumerate}

## technical
For the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$ on flat spacetime, with coframe the components of $\hb^{-1}$ and $\beta^2 = 2M/r$, all connection data is algebraic in $(r,\beta)$: $\beta' = -\beta/2r$ and $\beta\beta' = -M/r^2$, so every coefficient lies in $\mathbb{Q}(r)[\beta]$. The torsion condition of the gauge-theory field equations, read on the physical frame through the outermorphism $\hb^{T}$, is solved by the rotation-gauge field with $\Omega(\hb(\gamma_1)) = -\beta'\,\sigma_r$, $\Omega(\hb(\gamma_2)) = \tfrac1r(\beta\gamma_0 + \gamma_1)\wedge\gamma_2$, $\Omega(\hb(\gamma_3)) = \tfrac1r(\beta\gamma_0 + \gamma_1)\wedge\gamma_3 + \tfrac{\cot\vartheta}{r}\gamma_2\wedge\gamma_3$ and $\Omega(\hb(\gamma_0)) = 0$, each checked by substitution (in components, the connection one-forms of the coframe and the first structure equations).

On the background directions of the $(t,r)$ plane the connection bivector is $\Omega(\partial_t) = (M/r^2)\,\sigma_r$ and $\Omega(\partial_r) = \sqrt{M/2r^3}\,\sigma_r$, with $\sigma_r$ the unit radial boost bivector. The time-direction connection is exactly the Newtonian field at every radius, and the radial-direction connection diverges as $r^{-3/2}$ when $r \to 0$, the square root of the field-strength scale $M/r^3$.

## lay
In the gauge-theory description of gravity, the connection records how local frames boost and rotate from point to point. For a non-rotating black hole in this gauge it can be written down exactly. Along the time direction it equals Newton's gravitational field strength, mass over radius squared, at every radius; along the radial direction it grows without bound towards the centre, at the square root of the rate at which the field strength grows.

## one-liner
In the Painlev\'e-Gullstrand gauge the connection bivector is exactly $(M/r^2)\,\sigma_r$ along $\partial_t$ and $\sqrt{M/2r^3}\,\sigma_r$ along $\partial_r$.
