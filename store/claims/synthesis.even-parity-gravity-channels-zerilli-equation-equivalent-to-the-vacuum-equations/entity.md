---
id: synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations
kind: claim
version: 1
title: 'Even-parity gravity channels and the Zerilli equation, both directions'
status: proved
region: synthesis
subject: thermality
tags: [boundary-modes, mode-counting, schwarzschild, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-18-leads
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-leads
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - pairing.imported-schwarzschild-connection-curvature@7
  - synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_even_parity_closed_forms_identically_in_radius_and_angle
- kind: check
  ref: check.py::check_odd_parity_closed_forms_identically_in_radius_and_angle
- kind: check
  ref: check.py::check_sampled_controls_other_masses_and_wrong_coefficients
- kind: check
  ref: check.py::check_reconstructed_field_of_a_zerilli_solution_is_a_vacuum_solution
- kind: check
  ref: check.py::check_oscillating_channel_field_is_the_reconstruction_of_its_master_function
lineage:
  motivated_by:
  - hawking.joint-j3-s-wave-reduction
  - synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional
extraction:
  open_problem: op.helicity-per-boundary-mode
  note: >-
    Attack on the first item of the open problem as restated on 9 November: the even-parity converse, with the
    implication proved identically and not only at sample points. Method: the stored linearisation of the gauge
    field about the static Schwarzschild field (lib/gtg.py, the construction of
    synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional), run with jet
    coefficients in an exact ring in sqrt f and in the sine and cosine of the polar angle, in which only units
    are inverted, so that each comparison is an identity in the radius and the angle together; then exact
    differential algebra in r, lambda and omega^2 for the radial identities. Results: closed forms of all
    sixteen components of the first-order Ricci vectors of the even-parity field for an arbitrary angular
    function; the stored odd-parity closed forms as identities in radius and angle (the stored degree bound,
    argued there, is no longer needed); the reconstruction of a vacuum field from any solution of the Zerilli
    equation, with every vacuum equation an explicit differential multiple of the Zerilli operator; and, on an
    oscillating channel, the reduction of the vacuum equations to a first-order system and one algebraic
    relation, under which the Zerilli equation holds and the field is the reconstruction of its own master
    function. So the cited fact (C3) of the stored result (every solution of the Zerilli equation is a master
    function) is proved, and its sample-point clause (3) is superseded on oscillating channels; off them the
    implication from the vacuum equations to the Zerilli equation remains as stored, computed at sample points. What stays cited from memory: (C1) completeness of tensor harmonics and (C2) reachability of
    the Regge-Wheeler gauge. Not attempted: l = 0, 1, charts regular across the horizon, the fuzzy-sphere
    identification. Prior art, cited from memory and not used as input: Zerilli (1970) for the equation and
    the algebraic relation, Moncrief (1974) for the master function, Lousto and Price (1997) for
    reconstruction formulas of this form; the formulas of clause (3) were first written from memory and are
    verified here by exact computation. Decisions for the maintainer: (1) joint J3
    (hawking.joint-j3-s-wave-reduction, a postulate) can be narrowed again, its channel-reduction clause no
    longer being needed for even-parity spin 2 on oscillating channels once (C1) and (C2) are accepted as cited
    hypotheses or imported;
    (2) the stored result's title and clauses (1), (3), (5) can be reworded to cite this one; (3) whether (C1)
    and (C2) are imported as Facts. Transport-absent: the classical Zerilli reduction, re-derived in the
    gauge-field formalism with every step exact.
---

## formal
Use the setting and notation of Theorem \claimref{synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional}: the Schwarzschild field in the static gauge of Fact \claimref{pairing.imported-schwarzschild-connection-curvature} on $r > 2M$, $f = 1 - 2M/r$, physical frame $\gamma_{a}$ of signature $(+,-,-,-)$ with $\hb^{-1}(e_{t}) = \sqrt f\,\gamma_{0}$, $\hb^{-1}(e_{r}) = \gamma_{1}/\sqrt f$, $\hb^{-1}(e_{\vartheta}) = r\gamma_{2}$, $\hb^{-1}(e_{\varphi}) = r\sin\vartheta\,\gamma_{3}$ (\claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $\partial_{r_{*}} = f\partial_{r}$; a linearised field $\hb^{-1}(e_{\mu}) \mapsto \hb^{-1}(e_{\mu}) + \epsilon k_{\mu}$, $\epsilon^{2} = 0$, with $\Omega_{1}$ fixed by the torsion-free condition and first-order Ricci vectors $\mathcal{R}_{1}(\gamma_{b})$; the even-parity field in the Regge-Wheeler gauge
\[
k_{t} = P\bigl(-\tfrac12\sqrt f\,H_{0}\gamma_{0} + \sqrt f\,H_{1}\gamma_{1}\bigr), \quad k_{r} = \tfrac12 f^{-1/2}H_{2}P\,\gamma_{1}, \quad k_{\vartheta} = \tfrac12 rKP\,\gamma_{2}, \quad k_{\varphi} = \tfrac12 r\sin\vartheta\,KP\,\gamma_{3},
\]
with $H_{0}, H_{1}, H_{2}, K$ smooth functions of $(t, r)$ and $P$ a smooth function of $\vartheta$; a prime on them is $\partial_{r}$, respectively $\partial_{\vartheta}$, and $\Delta P := P'' + \cot\vartheta\,P'$. For a separation constant $L > 2$ put $\lambda = (L - 2)/2 > 0$,
\[
V_{\mathrm{e}} = f\,\frac{2\lambda^{2}(\lambda+1)r^{3} + 6\lambda^{2}Mr^{2} + 18\lambda M^{2}r + 18M^{3}}{r^{3}(\lambda r + 3M)^{2}}, \qquad \mathcal{Z}[u] := \partial_{t}^{2}u - \partial_{r_{*}}^{2}u + V_{\mathrm{e}}u, \qquad \Psi := r\Bigl(K + \frac{fr}{\lambda r + 3M}\bigl(H_{2} - rK'\bigr)\Bigr),
\]
the Zerilli potential, operator and Zerilli-Moncrief function of that theorem.
\begin{enumerate}
\item \emph{(Closed forms, for every angular function; proved by exact computation.)} With
\begin{align*}
C_{00} &= \tfrac{f}{2}H_{0}'' + \tfrac{2r - M}{2r^{2}}H_{0}' - \partial_{t}H_{1}' - \tfrac{2r - 3M}{r^{2}f}\partial_{t}H_{1} + \tfrac{M}{2r^{2}}H_{2}' + \tfrac{1}{2f}\partial_{t}^{2}H_{2} - \tfrac{M}{r^{2}}K' + \tfrac{1}{f}\partial_{t}^{2}K, \\
C_{01} &= \partial_{t}K' + \tfrac{r - 3M}{r^{2}f}\partial_{t}K - \tfrac{1}{r}\partial_{t}H_{2}, \qquad C_{02} = \partial_{r}(fH_{1}) - \partial_{t}(H_{2} + K), \\
C_{12} &= f(H_{0}' - K') - \partial_{t}H_{1} - \tfrac{r - 3M}{r^{2}}H_{0} + \tfrac{r - M}{r^{2}}H_{2}, \\
C_{11} &= \tfrac{f}{2}H_{0}'' + \tfrac{3M}{2r^{2}}H_{0}' - \partial_{t}H_{1}' - \tfrac{M}{r^{2}f}\partial_{t}H_{1} + \tfrac{2r - 3M}{2r^{2}}H_{2}' + \tfrac{1}{2f}\partial_{t}^{2}H_{2} - \tfrac{2r - 3M}{r^{2}}K' - fK'', \\
C_{22} &= \tfrac{f}{2r}(H_{0}' + H_{2}') - \tfrac{1}{r}\partial_{t}H_{1} + \tfrac{1}{r^{2}}(H_{2} - K) - \tfrac{2r - 3M}{r^{2}}K' - \tfrac{f}{2}K'' + \tfrac{1}{2f}\partial_{t}^{2}K,
\end{align*}
the first-order Ricci vectors are
\begin{align*}
\mathcal{R}_{1}(\gamma_{0}) &= \bigl(PC_{00} + \tfrac{H_{0}}{2r^{2}}\Delta P\bigr)\gamma_{0} - \bigl(PC_{01} + \tfrac{H_{1}}{2r^{2}}\Delta P\bigr)\gamma_{1} + \tfrac{P'}{2r\sqrt f}C_{02}\,\gamma_{2}, \\
\mathcal{R}_{1}(\gamma_{1}) &= \bigl(PC_{01} + \tfrac{H_{1}}{2r^{2}}\Delta P\bigr)\gamma_{0} + \bigl(PC_{11} - \tfrac{H_{2}}{2r^{2}}\Delta P\bigr)\gamma_{1} + \tfrac{P'}{2r\sqrt f}C_{12}\,\gamma_{2}, \\
\mathcal{R}_{1}(\gamma_{2}) &= -\tfrac{P'}{2r\sqrt f}C_{02}\,\gamma_{0} + \tfrac{P'}{2r\sqrt f}C_{12}\,\gamma_{1} + \bigl(PC_{22} - \tfrac{K}{2r^{2}}\Delta P + \tfrac{H_{0} - H_{2}}{2r^{2}}P''\bigr)\gamma_{2}, \\
\mathcal{R}_{1}(\gamma_{3}) &= \bigl(PC_{22} - \tfrac{K}{2r^{2}}\Delta P + \tfrac{H_{0} - H_{2}}{2r^{2}}\cot\vartheta\,P'\bigr)\gamma_{3},
\end{align*}
at every radius of the exterior and every polar angle with $\sin\vartheta \neq 0$. The evidence: $\mathcal{R}_{1}$ at a point is a linear function of the second-order jet of $k$ there, so both sides are bilinear in the second-order jets of $(H_{0}, H_{1}, H_{2}, K)$ and of $P$ at the point; on the $24$ basis jets of the first and the $3$ basis jets $(P, P', P'')$ of the second every one of the sixteen components agrees as an identity in the ring $\mathbb{Q}[z, z^{-1}, (1 - z^{2})^{-1}, s, s^{-1}, c]/(c^{2} + s^{2} - 1)$, $z = \sqrt f$ with $r = 2M/(1 - z^{2})$, $s = \sin\vartheta$, $c = \cos\vartheta$, at $M = 1$; the expressions are homogeneous under $(t, r, M) \mapsto (at, ar, aM)$. No separation constant enters and no degree bound is used.
\item \emph{(Odd parity, without the degree bound; proved by exact computation.)} The closed forms of clause (1) of Theorem \claimref{synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional} hold as identities in the same ring, on the $12$ basis jets of $(h_{0}, h_{1})$, the $2$ basis data of $(S, S')$ and two values of $L$ (both sides are of degree one in $L$, which enters through $S''$ alone); so that clause holds at every radius and polar angle without the degree bound in $\cot\vartheta$ argued there.
\item \emph{(The radial system; proved from (1).)} Let $P$ be a nonzero solution of $P'' + \cot\vartheta\,P' + LP = 0$ with $L \notin \{0, 2\}$. Then $\mathcal{R}_{1}(\gamma_{b}) = 0$ for all $b$ if and only if
\[
E_{1} := C_{00} - \tfrac{L}{2r^{2}}H_{0}, \quad E_{2} := C_{01} - \tfrac{L}{2r^{2}}H_{1}, \quad E_{3} := C_{02}, \quad E_{4} := C_{12}, \quad E_{5} := C_{11} + \tfrac{L}{2r^{2}}H_{2}, \quad E_{6} := H_{0} - H_{2}, \quad E_{7} := C_{22} + \tfrac{L}{2r^{2}}K
\]
all vanish.
\item \emph{(The converse: every solution of the Zerilli equation is a master function; proved, identically.)} For a smooth function $\Phi(t, r)$ let
\begin{align*}
K &= \frac{\lambda(\lambda+1)r^{2} + 3\lambda Mr + 6M^{2}}{r^{2}(\lambda r + 3M)}\Phi + f\Phi', \qquad H_{1} = \partial_{t}\bigl(r\Phi' + a\Phi\bigr), \quad a := \frac{\lambda r^{2} - 3\lambda Mr - 3M^{2}}{(r - 2M)(\lambda r + 3M)}, \\
H_{0} = H_{2} &= -\frac{\lambda^{2}(\lambda+1)r^{3} + 3\lambda^{2}Mr^{2} + 9\lambda M^{2}r + 9M^{3}}{r^{2}(\lambda r + 3M)^{2}}\Phi + \frac{\lambda r^{2} - \lambda Mr + 3M^{2}}{r(\lambda r + 3M)}\Phi' + (r - 2M)\Phi''.
\end{align*}
Then, identically in $\Phi$: $\Psi = (\lambda + 1)\Phi$; $E_{2} = E_{3} = E_{6} = 0$; $E_{4} = -(r\partial_{r} + a)\mathcal{Z}[\Phi]$; $E_{7} = -\tfrac12\partial_{r}\mathcal{Z}[\Phi] + b\,\mathcal{Z}[\Phi]$ with $b = \bigl(\lambda(\lambda - 1)r^{2} + 9\lambda Mr + 12M^{2}\bigr)/\bigl(2r(r - 2M)(\lambda r + 3M)\bigr)$; and $E_{1}$, $E_{5}$ are second-order differential operators in $r$ applied to $\mathcal{Z}[\Phi]$, with leading coefficient $-r/2$ and coefficients regular on $r > 2M$. Hence if $\mathcal{Z}[\Phi] = 0$ the field is an even-parity vacuum solution with Zerilli-Moncrief function $(\lambda + 1)\Phi$: every solution $\Psi$ of the Zerilli equation is the Zerilli-Moncrief function of the vacuum solution built from $\Phi = \Psi/(\lambda + 1)$. No condition on the time dependence is used.
\item \emph{(An oscillating channel: the master function carries the whole field; proved, identically.)} On functions with $\partial_{t}^{2} = -\omega^{2}$, $\omega^{2}$ a nonzero constant (an oscillating channel when $\omega$ is real; the identities use only $\omega^{2} \neq 0$), let $(H_{0}, H_{1}, H_{2}, K)$ solve $E_{1} = \cdots = E_{7} = 0$ and write $H = H_{0} = H_{2}$. Then $E_{3}$, $E_{4}$ and $\partial_{t}E_{2}$ are the first-order system
\[
K' = -\frac{r - 3M}{r^{2}f}K + \frac{H}{r} - \frac{\lambda + 1}{r^{2}\omega^{2}}\partial_{t}H_{1}, \qquad H' = K' + \frac{1}{f}\Bigl(\partial_{t}H_{1} - \frac{2M}{r^{2}}H\Bigr), \qquad H_{1}' = \frac{1}{f}\Bigl(\partial_{t}H + \partial_{t}K - \frac{2M}{r^{2}}H_{1}\Bigr);
\]
under it $E_{7}$ becomes $(2r^{3})^{-1}$ times the algebraic relation
\[
\mathrm{Rel} := -(\lambda r + 3M)H + \frac{\lambda r(r - 2M) + M(r - 3M) - \omega^{2}r^{4}}{r - 2M}K + \frac{M(\lambda + 1) - \omega^{2}r^{3}}{r\omega^{2}}\partial_{t}H_{1} = 0,
\]
$E_{1}$, $E_{5}$ and $\partial_{r}\mathrm{Rel}$ become multiples of $\mathrm{Rel}$ with coefficients regular on $r > 2M$, and so does $\mathcal{Z}[\Psi]$: the vacuum equations imply the Zerilli equation for $\Psi$. Under the first-order system alone, $(\lambda + 1)(K, H, H_{1})$ is the field built in (4) from $\Phi = \Psi$. So a vacuum solution of the channel with $\Psi = 0$ vanishes, and $(H_{0}, H_{1}, H_{2}, K) \mapsto \Psi$ is a bijection from the even-parity vacuum solutions of the channel in the Regge-Wheeler gauge onto the solutions of the Zerilli equation in the channel, with inverse $\Psi \mapsto$ the field of (4) for $\Phi = \Psi/(\lambda + 1)$.
\item \emph{(At the horizon; given (C1) and (C2).)} By (4), (5) and clauses (4) and (5) of Theorem \claimref{synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional} ($V_{\mathrm{e}}/f$ regular and positive at $r = 2M$, $V_{\mathrm{e}} = O(e^{2\kappa r_{*}})$), an even-parity vacuum solution in the Regge-Wheeler gauge on a channel with $\ell \geq 2$ and real $\omega \neq 0$ is carried by one function obeying a two-dimensional equation in $(t, r_{*})$ whose potential vanishes at the horizon at the rate $e^{2\kappa r_{*}}$, as the odd-parity ones are. Given the cited facts (C1) (completeness of the tensor harmonics, and that the axisymmetric representative suffices) and (C2) (reachability of the Regge-Wheeler gauge) of that theorem, this holds for every even-parity channel with $\ell \geq 2$ and real $\omega \neq 0$. The cited fact (C3) of that theorem, that every solution of the Zerilli equation in an oscillating channel is the function $\Psi$ of an even-parity vacuum solution, is clause (4); what that theorem's clause (5) needs beyond (C3), that the vacuum equations imply the Zerilli equation identically and that $\Psi$ determines the field, is clause (5) here. That theorem's clause (3), the implication from the vacuum equations to the Zerilli equation computed at sample points, is superseded on oscillating channels only: without a condition on the time dependence that implication is not proved identically here and stays as stored. The scope stated there is unchanged: the static frame; $\ell \geq 2$; oscillating channels; (C1) and (C2) remain cited from memory; the current-boson identification and the partial-wave lift of joint J3 (\claimref{hawking.joint-j3-s-wave-reduction}) are not derived.
\end{enumerate}
The identities of (4) and (5) are computed at $M = 1$ in the ring $\mathbb{Q}[r, \lambda, w][r^{-1}, (r - 2)^{-1}, (\lambda r + 3)^{-1}, w^{-1}]$, $w = \omega^{2}$, in which only these units are inverted; every expression is homogeneous under $(t, r, M) \mapsto (at, ar, aM)$ with $H_{0}, H_{1}, H_{2}, K$ of weight $0$, $\Phi$ and $\Psi$ of weight $1$ and $\omega$ of weight $-1$ ($w$ of weight $-2$), which gives general $M$. On $r > 2M$ with $\lambda > 0$ none of the inverted quantities vanishes.

## technical
The stored result on the linearised gravitational field around a static black hole proved that each odd-parity channel is one function obeying a two-dimensional wave equation, and for even parity showed only, at two sample points, that the vacuum equations imply the Zerilli equation; that the Zerilli function carries the whole channel was cited. This result closes the even-parity case. First, the first-order Ricci vectors of the even-parity field are computed in closed form, as identities in the radius and the polar angle together and for an arbitrary angular function, by running the stored linearisation with coefficients in an exact ring in which only $\sqrt f$, $1 - f$ and $\sin\vartheta$ are ever inverted. The same computation turns the stored odd-parity closed forms into identities in both variables, so the degree bound that was argued there is not needed. Second, for a harmonic with $\ell \geq 2$ the vacuum equations are seven radial equations. Third, from any function $\Phi$ a field is written down whose seven equations are explicit differential operators applied to the Zerilli operator on $\Phi$, and whose Zerilli-Moncrief function is $(\lambda + 1)\Phi$: a solution of the Zerilli equation gives a vacuum solution, with no condition on its time dependence. Fourth, on a channel of nonzero real frequency the vacuum equations amount to a first-order system in the radius and one algebraic relation, the system preserves the relation, the Zerilli equation follows from them identically, and the field equals the field rebuilt from its own master function. So the master function is a bijection between even-parity vacuum solutions of the channel and solutions of the Zerilli equation, and with the stored horizon values of the potential each even-parity channel is a two-dimensional mode at the horizon in the static frame, given the two cited facts below. Off oscillating channels the implication from the vacuum equations to the Zerilli equation is not proved identically here and remains as stored, at sample points. What remains outside is what was outside for odd parity: the completeness of the tensor harmonics and the reachability of the gauge, both cited; the cases $\ell = 0, 1$; charts regular across the horizon; and the identification of a channel with a current boson, which stays a premise.

## lay
A small ripple in the gravitational field around a black hole can be sorted into simple patterns, two for each pitch and each angular shape. For one of the two kinds it was already shown that a single wave on a line, running towards or away from the horizon, carries the whole pattern. For the other kind that was known in one direction only, and at a few test points. This result finishes it: every such wave on a line gives a ripple that solves the field equations, every ripple of that kind is rebuilt exactly from its wave, and close to the horizon the wave moves freely. The calculation is exact at every distance and every angle, not sampled. That these patterns are all the ripples there are holds if two textbook facts about sorting ripples into patterns are granted; they are still taken on trust.

## one-liner
For the even-parity linearised gravitational field on the static Schwarzschild exterior in the Regge-Wheeler gauge, $\ell \geq 2$: closed forms of the first-order Ricci vectors as identities in radius and angle; every solution $\Psi$ of the Zerilli equation is the Zerilli-Moncrief function of the vacuum field rebuilt from $\Psi/(\lambda+1)$, each vacuum equation being a differential multiple of the Zerilli operator; and on a channel of real frequency $\omega \neq 0$ the vacuum equations imply the Zerilli equation and the field is the rebuilt one, so the master function carries the whole channel (the stored cited fact (C3) proved; the forward implication identical on oscillating channels only; that the channel is the whole even-parity field holds given (C1) and (C2), which remain cited).
