---
id: synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional
kind: claim
version: 1
title: 'Horizon channels of scalar, Dirac and Maxwell fields are two-dimensional'
status: proved
region: synthesis
subject: thermality
tags: [boundary-modes, mode-counting, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - pairing.imported-schwarzschild-connection-curvature@7
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_dirac_channel_reduction
- kind: check
  ref: check.py::check_angular_operator_and_squared_channel
- kind: check
  ref: check.py::check_scalar_channel_potential
- kind: check
  ref: check.py::check_horizon_decay_orders
- kind: check
  ref: check.py::check_maxwell_channels_both_parities
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - hawking.joint-j3-s-wave-reduction
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays
extraction:
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Note only: the request to the maintainer is replaced by the record of what was done (the channel-reduction clause of J3 narrowed to spin 2 by decision of 9 November, the op known text corrected); statement unchanged.'
  open_problem: op.helicity-per-boundary-mode
  note: >-
    Attack on joint J3 (hawking.joint-j3-s-wave-reduction, a modelling premise) at the horizon, by deriving the
    partial-wave reductions in Gauge Theory Gravity instead of importing them: the Schwarzschild field in the static
    gauge of the stored Fact pairing.imported-schwarzschild-connection-curvature, the GTG covariant derivative of
    obj.synthesis.gtg-flat-spacetime-gauge-fields, and exact jet arithmetic (lib/gtg.py static_field, at points where
    1 - 2M/r is a fourth power). Prior art, cited from memory and not used as input: Regge and Wheeler (1957) for the
    odd-parity potentials, Chandrasekhar (The Mathematical Theory of Black Holes, 1983) for the Dirac potentials
    W^2 +- dW/dr_*, Teukolsky (1973), and Lasenby, Doran and Gull's separation of the Dirac equation in the
    Schwarzschild field in GTG (Painleve-Gullstrand gauge). The results reproduce the known potentials; what is new
    for the store is that the channel-reduction clause of J3 is derived at the horizon for spins 0, 1/2 and 1 from
    stored premises (J3 itself is not discharged: spin 2 and the current-boson identification remain), and that the
    spin-1/2 coupling decays as e^{kappa r_*}, not e^{2 kappa r_*}, which corrects the uniform statement recorded in the
    open problem's known text. Spin 2 and the massive spin-1 field are not covered. The rescaling f^{-1/4} of the
    Dirac channel is the boost weight 1/2 of synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays read
    in the static frame (argued). The result is conditional on the classical facts (C1), (C2) of the formal level
    (completeness of spherical and spinor spherical harmonics; the exact/co-exact split of one-forms on S^2), cited
    from memory and not in the store by decision; deriving them is an open item. The sphere operator is
    T~ Phi = gamma^0 gamma^1 (K Phi) gamma_0, which keeps even spinors even. On this derivation Leon decided on 9
    November to narrow the channel-reduction clause of hawking.joint-j3-s-wave-reduction to spin 2 (its version 2;
    the current-boson identification and the partial-wave lift stay premise for every massless field); the op's known text now says that the potentials
    are proportional to 1 - 2M/r for spins 0 and 1 and to sqrt(1 - 2M/r) for spin 1/2.
    Under J3 the integer-weight channels are read as currents of the arrays; nothing here counts them additively.
    Transport-absent.
---

## formal
Given the classical facts (C1) and (C2) below, cited from memory and not in the store, let $(\hb, \Omega)$ be the Schwarzschild field in the static gauge of Fact \claimref{pairing.imported-schwarzschild-connection-curvature}, $f = 1 - 2M/r$, on the exterior $r > 2M$, with physical frame $\gamma_{a}$ (signature $(+,-,-,-)$, reciprocal frame $\gamma^{a}$), the GTG covariant derivative $D$ of \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, the tortoise coordinate $r_{*}$ with $dr_{*}/dr = 1/f$, $\kappa = 1/(4M)$, $A := \gamma^{0}\partial_{t} + \gamma^{1}\partial_{r_{*}}$ and $W := \sqrt{f}/r$.
\begin{enumerate}
\item \emph{(Scalar.)} For $\phi = r^{-1}u(t,r)\,Y_{\ell m}$, $f\,r\,(D \cdot D\phi + \mu^{2}\phi) = \bigl(\partial_{t}^{2}u - \partial_{r_{*}}^{2}u + V_{\ell}u\bigr) Y_{\ell m}$ with $V_{\ell} = f\bigl(\ell(\ell+1)/r^{2} + 2M/r^{3} + \mu^{2}\bigr)$.
\item \emph{(Dirac.)} For an even multivector field $\Phi$ and $\psi = r^{-1}f^{-1/4}\Phi$, $r f^{3/4}\,D\psi = A\Phi + W K\Phi$ with $K = \gamma^{2}(\partial_{\vartheta} + \tfrac12\cot\vartheta) + \gamma^{3}(\sin\vartheta)^{-1}\partial_{\varphi}$, so the Dirac-Hestenes equation $D\psi\, I\sigma_{3} = m\,\psi\gamma_{0}$ is $(A\Phi + WK\Phi)\,I\sigma_{3} = m\sqrt{f}\,\Phi\gamma_{0}$. The factor $f^{-1/4}$ is the rescaling of the channel to boost weight zero (argued: it removes the boost weight $\tfrac12$ of the static frame). The sphere operator on even fields, $\tilde T\Phi := \gamma^{0}\gamma^{1}(K\Phi)\gamma_{0}$, preserves even fields, commutes with $A$, with $\partial_{\varphi}$ and with right multiplication by $I\sigma_{3}$ and $\gamma_{0}$, and $\tilde T^{2} = K^{2}$; on an eigenspace $\tilde T\Phi = \lambda\Phi$ the channel equation is $(A\Phi + \lambda W \gamma^{0}\gamma^{1}\Phi\gamma_{0})\,I\sigma_{3} = m\sqrt{f}\,\Phi\gamma_{0}$, and for $m = 0$ it implies $(\partial_{t}^{2} - \partial_{r_{*}}^{2} + \lambda^{2}W^{2})\Phi + \lambda\,(\partial_{r_{*}}W)\,\gamma^{0}\Phi\gamma_{0} = 0$, with potentials $V_{\pm} = \lambda^{2}f/r^{2} \pm \lambda\sqrt{f}\,(3M - r)/r^{3}$ on the $\pm 1$ eigenspaces of the even involution $\Phi \mapsto \gamma^{0}\Phi\gamma_{0}$.
\item \emph{(Maxwell.)} For the odd-parity potential $A_{\ell m} = \psi(t,r)\bigl((\sin\vartheta)^{-1}\partial_{\varphi}Y_{\ell m}\,d\vartheta - \sin\vartheta\,\partial_{\vartheta}Y_{\ell m}\,d\varphi\bigr)$, read as a physical vector, $F = D \wedge A_{\ell m}$ has $D \wedge F = 0$, $D \cdot A_{\ell m} = 0$ and $D \cdot F = f^{-1}\bigl(\partial_{t}^{2}\psi - \partial_{r_{*}}^{2}\psi + f\,\ell(\ell+1)\psi/r^{2}\bigr)A_{\ell m}/\psi$; and $D(IF) = -I\,DF$, so the even-parity fields $IF$ obey the same channel equation.
\item \emph{(At the horizon.)} $f = C(r)\,e^{2\kappa r_{*}}$ with $C$ regular and positive at $r = 2M$. The scalar and Maxwell potentials are $f$ times functions regular and nonzero at the horizon, so they decay as $e^{2\kappa r_{*}}$; the Dirac coupling $\lambda W$ and mass term $m\sqrt{f}$ decay as $e^{\kappa r_{*}}$, and $V_{\pm}/\sqrt{f} \to \pm\lambda/(8M^{2}) \neq 0$, so the spin-$\tfrac12$ potentials are of exact order $\sqrt{f}$. Hence, channel by channel, as $r_{*} \to -\infty$ every $(\omega, \ell, m, s)$ channel of the massless or massive scalar, the massless or massive Dirac field and the Maxwell field obeys the free two-dimensional equation in $(t, r_{*})$, whose solutions are left and right movers (for the Dirac channel, even $\Phi(t \mp r_{*})$ with $\gamma^{0}\gamma^{1}\Phi = \pm\Phi$): the channel-reduction clause of joint J3 (\claimref{hawking.joint-j3-s-wave-reduction}) holds at the horizon for spins $0$, $\tfrac12$ and $1$. J3 is not discharged: spin $2$ and its identification of the s-wave theory's current boson with these channels remain premise. The approach is not uniform in $\ell$, and the spin-$\tfrac12$ rate is $e^{\kappa r_{*}}$, half the integer-spin rate.
\end{enumerate}
The classical facts assumed, cited from memory and not in the store: (C1) the eigenfunctions of the sphere operator $\tilde T$ (spinor spherical harmonics) and the spherical harmonics $Y_{\ell m}$ span the fields on the sphere; (C2) one-forms on $S^{2}$ split into exact and co-exact parts. They enter the phrase ``every channel'' in (4); the reductions (1) to (3) for a given channel do not use them.

## technical
Joint J3 says, among other things, that near a Schwarzschild horizon each partial-wave channel of a field is a two-dimensional mode. Here that channel-reduction clause is derived in Gauge Theory Gravity rather than imported, for spins zero, one half and one. In the static gauge the Dirac operator splits exactly: after removing the factor $r^{-1}f^{-1/4}$, it is the two-dimensional Dirac operator in time and the tortoise coordinate plus the sphere's Dirac operator multiplied by $\sqrt{f}/r$. The sphere operator, multiplied by the radial-time bivector on the left and by the time vector on the right (so that it keeps even spinors even), commutes with the two-dimensional part, so its eigenvalues label channels, and each channel is a two-dimensional Dirac field with a position-dependent mass $\lambda\sqrt{f}/r$ (and $m\sqrt{f}$ for a massive field). The scalar wave operator reduces to the familiar radial equation with potential $f(\ell(\ell+1)/r^{2} + 2M/r^{3} + \mu^{2})$, and the Maxwell field to the odd-parity equation with potential $f\,\ell(\ell+1)/r^{2}$, the even parity following by multiplying the field by the pseudoscalar, which commutes with the covariant derivative up to sign. Near the horizon $f$ falls off as $e^{2\kappa r_{*}}$, so all couplings vanish and each channel becomes a free massless field in two dimensions, made of left- and right-moving waves. The spin-half couplings carry $\sqrt{f}$, not $f$, so they fall off at half the rate of the integer-spin potentials; the uniform statement that every potential is proportional to $1 - 2M/r$ is false for spin one half, although J3 holds for it. The approach to two dimensions is channel by channel: higher angular momentum needs to be closer to the horizon. This is the channel-reduction part of the modelling premise J3; its identification of the s-wave theory's current boson with these channels, and spin two, stay premise. Spin two and the massive vector field are not treated, and completeness of the angular harmonics is cited from memory.

## lay
Near the horizon of a black hole, a field such as light or an electron's field is often treated as a collection of independent waves moving in one space dimension, one for each way of winding around the sphere. This result derives that picture, rather than assuming it, for scalar fields, electrons (with or without mass) and electromagnetism, in the geometric-algebra form of gravity the series uses. In each winding pattern the field obeys a wave equation in one space dimension, with a barrier that disappears towards the horizon, so each pattern becomes a free one-dimensional wave there, moving in or out. The patterns that wind around the sphere more often have higher barriers, so they reach this free form only closer to the horizon. For electrons the barrier disappears more slowly than for the other fields, as the square root of the factor that measures the horizon's pull, so an earlier statement that all barriers shrink in the same way is corrected. Gravitational waves are not covered.

## one-liner
In the static gauge of Gauge Theory Gravity on the Schwarzschild exterior, every partial-wave channel of the scalar, Dirac and Maxwell fields obeys a two-dimensional equation in time and the tortoise coordinate whose coupling vanishes at the horizon (as $e^{2\kappa r_{*}}$ for spins $0$ and $1$, as $e^{\kappa r_{*}}$ for spin $\tfrac12$), so the channel-reduction clause of joint J3 holds at the horizon for these fields, massive ones included for spins $0$ and $\tfrac12$ (J3 itself, with spin $2$ and its current-boson identification, stays premise).
