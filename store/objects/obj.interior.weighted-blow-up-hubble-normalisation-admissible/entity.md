---
id: obj.interior.weighted-blow-up-hubble-normalisation-admissible
kind: object
version: 2
title: Weighted blow-up, Hubble normalisation, and the admissible class
status: defined
region: interior
subject: interior
tags: [kasner, limits]
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
- obj.synthesis.gtg-flat-spacetime-gauge-fields
locators:
  paper: T06
  number: Def 5.5
  label: def:blowup
  line: 674
extraction:
  typing:
    by: ai-typing-pass
    note: 'Definition; levels typed, no edges.'
  env: definition
  context_refs:
  - interior.exact-parallelism-convergence-rate
  - interior.interior-connection-exactly
  - interior.kasner-form-interior
  - interior.transport-level-convergence-along-tangential-curves
  - interior.weighted-limit-theorem
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [interior.schwarzschild-de-sitter-weighted-limit, interior.schwarzschild-lines-exactly]
    added_about: []
    verdict: connected
    note: 'Added the Schwarzschild-de Sitter limit and the exact-lines corollary, both stated in Hubble-normalised data; the T5 modular-flow rate that is Hubble-normalised in passing was not linked.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: admissibility is defined for a gravitational field (hb, Omega) on the collar in a synchronous gauge (Einstein: R(a) = Lambda a in the store sign, which is Ric = Lambda g for the derived metric), with the connection the rotation-gauge field in a D-parallel physical frame; a synchronous metric is called admissible when it is the derived metric of an admissible field, so dependants reading admissible metric are unchanged. Conditions, constants and boundary objects unchanged. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged.'
---

## formal
Blow up the interior along the singular locus by adjoining the exceptional boundary $\{\tau = 0\}$ to the collar $(0,\tau_0] \times \mathcal{B}$, $\mathcal{B} := \R_t \times S^2$, \emph{with direction-dependent weights} $(p_1, p_2, p_3)$: the boundary is probed by the rescaled (Hubble-normalised) data
\[
\widehat\Omega_\tau \;:=\; \tau\,\Omega\big|_{\text{unit tangential directions at time } \tau},
\]
the rotation-gauge field $\Omega$ in the $D$-parallel physical frame, evaluated on the unit vectors of the $\tau$-slice and multiplied by $\tau$; a tangential direction carries weight $p_i$ in the sense that its unit vector contracts by the factor $\tau^{p_i}$ relative to the coordinate vector, which is exactly what the frame normalisation implements. A gravitational field $(\hb, \Omega)$ on the collar (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), in a synchronous gauge and with derived metric singular at $\tau = 0$, is \emph{admissible} (Einstein velocity-dominated) if it is Einstein, $\mathcal{R}(a) = \Lambda a$ with $\Lambda$ constant (in the store's sign, so that the derived metric has $\Ric_{ab} = \Lambda\, g_{ab}$; the field-equation hypothesis the tractor clauses of Theorem \claimref{interior.weighted-limit-theorem} consume; the Levi-Civita clauses, those about $\Omega$, use only the decay conditions), and in some $D$-parallel orthonormal physical frame, with boosts $B_i = e_0 \wedge e_i$, the Hubble-normalised connection satisfies $\widehat\Omega_\tau = -\sum_i p_i B_i \otimes \hat\theta^i + E_\tau$ with constants $p_i \neq 0$ (the sign is that of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, $D_a M = a \cdot \nabla M + \Omega(a) \times M$, in which the Cartan forms $\omega^{i}{}_{0} = (p_i/\tau)\,\theta^i$ of a Kasner field assemble to $-\sum_i p_i B_i$) satisfying the Kasner-type constraint $\sum_i p_i^2 = 1$ (the Schwarzschild exponents $(-\tfrac13, \tfrac23, \tfrac23)$ satisfy it, Lemma \claimref{interior.kasner-form-interior}; the constraint is what Theorem \claimref{interior.transport-level-convergence-along-tangential-curves} uses, through Cauchy-Schwarz, to bound the model generator on unit directions by $1$) and an error $E_\tau$ which tends to zero as $\tau \to 0$ and for which $\|E_\tau\|/\tau$ is integrable on $(0, \tau_0]$, both locally uniformly on $\mathcal{B}$. A synchronous metric is called admissible when it is the derived metric of an admissible gravitational field. Two boundary objects are part of the same data. The \emph{boundary bundle} is the trivial extension of the parallel trivialisation: the tractor fibre in the parallel tractor frame, extended over $\{\tau = 0\} \times \mathcal{B}$ as a product, so that a section defined for $\tau > 0$ extends to the boundary exactly when its components in that frame converge. The \emph{boundary holonomy algebra} is the Lie subalgebra of $\mathfrak{so}(2,4)$ generated by the limiting values of the Hubble-normalised connection on unit tangential directions, over all boundary points: a values-level definition, which is what the theorem computes; along the directions where the connection is abelian it agrees with the transport-level reading (Theorem \claimref{interior.weighted-limit-theorem}, final clause). By Lemmas \claimref{interior.exact-parallelism-convergence-rate} and \claimref{interior.interior-connection-exactly} the Schwarzschild interior ($\Lambda = 0$) is admissible, with $\|E_\tau\| = O(\tau^{2/3}) + O(\tau/r) = O(\tau^{1/3})$ tending to zero and $\|E_\tau\|/\tau = O(\tau^{-2/3})$ integrable at $0$. On the sphere factor the frame, and with it the display, is taken patchwise (no global orthonormal frame on $S^2$ exists); admissibility and the limiting values are patch-independent statements, the values transforming by the constant rotation between patches.

## technical
The interior is blown up along its singular locus by adjoining the boundary $\{\tau = 0\}$ to the collar $(0, \tau_0] \times \mathcal B$, $\mathcal B = \R_t \times S^2$, with direction-dependent weights $p_i$. The boundary is probed by the Hubble-normalised rotation-gauge field $\widehat\Omega_\tau = \tau\,\Omega$ on unit tangential directions in the $D$-parallel frame. A gravitational field $(\hb, \Omega)$ on the collar of flat spacetime, in synchronous gauge with derived metric singular at $\tau = 0$, is admissible if it is Einstein, $\mathcal{R}(a) = \Lambda a$ with $\Lambda$ constant (the derived metric has $\Ric_{ab} = \Lambda g_{ab}$), and in some parallel orthonormal physical frame $\widehat\Omega_\tau = -\sum_i p_i B_i \otimes \hat\theta^i + E_\tau$ with constants $p_i \neq 0$ satisfying $\sum_i p_i^2 = 1$, and an error with $E_\tau \to 0$ and $\|E_\tau\|/\tau$ integrable on $(0, \tau_0]$, both locally uniformly on $\mathcal B$. A synchronous metric is admissible when it is the derived metric of such a field.

The boundary bundle is the product extension of the parallel tractor trivialisation, so a section extends exactly when its components converge. The boundary holonomy algebra is the Lie subalgebra of $\mathfrak{so}(2,4)$ generated by the limiting connection values on unit tangential directions, a values-level notion. The Schwarzschild interior is admissible, with $\|E_\tau\| = O(\tau^{1/3})$; on the sphere the frame is taken patchwise.

## lay
To study the singularity, the definition adds an idealised boundary at the moment of the singularity and measures the gravitational field there with a clock-rescaled version of the rules for carrying directions. Different directions are rescaled with different weights, matching how fast each one stretches or shrinks. A gravitational field counts as admissible when, after this rescaling, it approaches the simple Kasner pattern fast enough, and the algebra of the limiting rules is the object the main theorem computes.

## one-liner
The weighted blow-up adjoins the boundary $\tau = 0$, probed by the Hubble-normalised connection $\tau\,\Omega$, and an Einstein gravitational field in synchronous gauge is admissible when $\tau\,\Omega = -\sum_i p_i B_i \otimes \hat\theta^i + E_\tau$ with $\sum_i p_i^2 = 1$ and a suitably decaying error.
