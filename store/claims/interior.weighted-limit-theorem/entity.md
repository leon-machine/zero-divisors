---
id: interior.weighted-limit-theorem
kind: claim
version: 5
title: Weighted limit theorem
status: proved
region: interior
subject: interior
tags: [schwarzschild, kasner, limits, frozen-point]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
derivations:
- name: main
  uses:
  - interior.boosts-generate-exactly-levi-factor@4
  - interior.covariant-form-vacuum-equations@5
  - interior.exact-parallelism-convergence-rate@5
  - interior.interior-connection-exactly@7
  - interior.kasner-form-interior@5
  - interior.metric-parallelism-trace-schouten-condition@6
  - interior.non-null-stabilisers-section-they-act@4
  - interior.scale-tractor-leaves-cone@7
  - interior.stabilisers-flat-model@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:5.6
- kind: check
  ref: check.py::check_connection_shape_and_rates
- kind: check
  ref: check.py::check_limiting_values_annihilate_scale_tractor
- kind: check
  ref: check.py::check_holonomy_algebra_is_levi_factor
- kind: check
  ref: check.py::check_transport_along_abelian_directions
locators:
  paper: T06
  number: Thm 5.6
  label: thm:weighted
  line: 682
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the interior connection shape and rates from the GTG gauge fields, the scale tractor annihilated by the limiting values, the holonomy Lambda^2 W as Levi factor or inside the reductive stabiliser, and the abelian transport directions. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the admissible metric is the derived metric of a gravitational field on flat spacetime, the Hubble-normalised Levi-Civita connection its rotation-gauge field on unit physical directions (Cartan sign, DICTIONARY C10) and the tractor connection its Cl(2,4) gauge field; content unchanged. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged.'
  typing:
    by: ai-typing-pass
    removed: [interior.schwarzschild-lines-exactly, interior.transport-level-convergence-along-tangential-curves]
    note: 'Removed the phi-line corollary and the tangential transport theorem, which the final clause and proof only point to as where the phi-line comparison is made; the Schwarzschild-de Sitter clause of item 4 is proved directly from the non-null stabiliser proposition, so that theorem was not added.'
  env: theorem
  context_refs:
  - interior.schwarzschild-de-sitter-weighted-limit
  eqrefs: 4
---

## formal
For the Schwarzschild interior, and more generally for every admissible metric in the sense of Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}, each read as the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}; the Levi-Civita connection being its rotation-gauge field $\Omega$ on unit physical directions, in the sign of that Definition, in which the Cartan forms of a Kasner field assemble to minus the weighted boosts, and the tractor connection its $\Cl(2,4)$ gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}):
\begin{enumerate}
\item the Hubble-normalised Levi-Civita and tractor connections, evaluated on unit tangential directions, extend continuously to the exceptional boundary; for Schwarzschild the correction is $O(\tau^{2/3})$ in the boost coefficients and $O(\tau^{1/3})$ in the rotation coefficients;
\item the parallel scale tractor $I_g$ of Theorems \claimref{interior.covariant-form-vacuum-equations} and \claimref{interior.scale-tractor-leaves-cone} extends to a parallel section of the boundary bundle of Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}: in the parallel trivialisation it is the constant section, and every limiting connection value annihilates it;
\item the limiting tangential connection is
\[
\widehat\Omega_0 \;=\; -\sum_{i=1}^3 p_i\, B_i \otimes \hat\theta^i ,
\]
the three boosts of the adapted frame weighted by minus the Kasner exponents, while every tractor coupling (the $\sigma$- and $\rho$-slot interchange terms of \eqref{eq:tractorconn}) and every rotation coefficient scales to zero;
\item consequently the limiting connection values lie in $\Lambda^2 W$, and the boundary holonomy algebra of Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible} is exactly $\Lambda^2 W \cong \mathfrak{so}(1,3)$: the two nilpotent summands $\nInf \wedge W$, $\nO \wedge W$ and the grading element $\nInf \wedge \nO$ receive no limiting value. For $\Lambda = 0$ the frozen point is null and this algebra is the Levi factor of its parabolic stabiliser (Proposition \claimref{interior.stabilisers-flat-model}), with no component in the shearing nilradical; for $\Lambda \neq 0$ the frozen point is non-null, its stabiliser is reductive with no nilradical (Proposition \claimref{interior.non-null-stabilisers-section-they-act}), and $\Lambda^2 W$ lies inside that stabiliser as a proper subalgebra (Theorem \claimref{interior.schwarzschild-de-sitter-weighted-limit}).
\end{enumerate}
For Schwarzschild the convergence holds at transport level along the abelian directions, exactly rather than by estimate, in two separate statements. Along the $t$- and $\theta$-coordinate lines the connection is a fixed bivector times a scalar, so the interior and Kasner-model transports commute, and their Hubble-normalised generators on the unit direction differ by $\tau\sigma_i - p_i = O(\tau^{2/3})$: over segments of fixed Hubble-normalised length the two transports differ by a boost of angle $O(\tau^{2/3}) \to 0$, with no Gronwall argument (over a fixed \emph{coordinate} segment the transports individually diverge, and no claim is made about their comparison). Along the $\tau$-geodesics the coordinate frame evolves diagonally, and its log-ratio against the Kasner model is $\int_0^\tau (\sigma_i - p_i/s)\,ds = O(\tau^{2/3}) \to 0$, one scale factor at a time. Along the $\varphi$-lines the connection on the coordinate vector carries the $\tau$-independent rotation $\cos\theta\,R_{23}$ beside a divergent boost, the two do not commute, and this theorem makes no transport-level claim there: the comparison over segments of fixed Hubble-normalised length, along the $\varphi$-lines and along every tangential curve of every admissible metric, is Theorem \claimref{interior.transport-level-convergence-along-tangential-curves} with Corollary \claimref{interior.schwarzschild-lines-exactly}; what remains open in general is the tangential regularity of the boundary data, the control of tangential derivatives of $E_\tau$, registered as a successor problem in Section \ref{sec:scope}.

## technical
For the Schwarzschild interior and every admissible metric, read as gravitational fields on flat spacetime, the Hubble-normalised rotation-gauge field and tractor gauge field on unit tangential directions extend continuously to the exceptional boundary (for Schwarzschild with corrections $O(\tau^{2/3})$ in the boosts and $O(\tau^{1/3})$ in the rotations); the parallel scale tractor $I_g$ extends as a parallel section of the boundary bundle; and the limiting tangential connection is $\widehat\Omega_0 = -\sum_i p_i\,B_i \otimes \hat\theta^i$, with every tractor coupling and rotation coefficient scaling to zero. The limiting values therefore generate exactly $\Lambda^2 W \cong \mathfrak{so}(1,3)$, with nothing in the two nilpotent summands or the grading element. For $\Lambda = 0$ this is the Levi factor of the parabolic stabiliser of the null frozen point; for $\Lambda \neq 0$ it is a proper subalgebra of the reductive stabiliser of the non-null one.

For Schwarzschild the convergence also holds exactly at transport level along the abelian directions: along the $t$- and $\theta$-lines, over segments of fixed Hubble-normalised length, the interior and model transports differ by a boost of angle $O(\tau^{2/3})$, and along the $\tau$-geodesics the frame's log-ratio against the model is $O(\tau^{2/3})$. This result makes no transport-level claim along the $\varphi$-lines or over segments of fixed coordinate length.

## lay
This is the central result about the approach to the singularity of a non-rotating black hole, and of a wider class of similar singularities. After rescaling by the natural clock, the rules for carrying directions settle to a clean limit at the singularity: three pure stretchings with the Kasner weights, and nothing else. These generate exactly the algebra of Lorentz transformations, while the parts of the larger symmetry that caused obstructions elsewhere in the series receive nothing.

## one-liner
For Schwarzschild and every admissible metric the Hubble-normalised connection tends to $-\sum_i p_i B_i \otimes \hat\theta^i$, the scale tractor extends as a parallel section, and the boundary holonomy algebra is exactly $\Lambda^2 W \cong \mathfrak{so}(1,3)$.
