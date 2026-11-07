# GA and other issues for the GA rewriters, R02 (thermality, second half)

Two entities of R02 are GA-owned; neither was edited by R02.

## synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field (v5)

1. **Known open item settled: proof Step 7, sign and regulator (two slips; the formal level is right).**
   Step 7 writes the scaled leading distribution as the limit of `1/(sigma_l + I_4 eps h_l + eps^2)` and then as
   the pullback of `1/(Q(z)/2 + I_4 0 h)` "with h of the sign of z^0", which it equates with the flat boundary value
   `1/(Q(z)/2 - I_4 0 <z, e_0>)`. Both signs are wrong for the ordering omega(psi psi^dagger) treated there:
   - Formal (i) gives sigma_+ the `-I_4 0` of the time function, and (iii) and Step 6 use
     `D_+(z) = -1/(4 pi^2 (Q(z) - I_4 0 z_0))` (positive frequency `e^{-I_4 p.z}` converges for `z_0 -> z_0 - I_4 eps`).
   - The scalar form of the shift of the separation is `Q(z - eps I_5 e_0)/2 = sigma - eps z_0 I_5 - eps^2/2`
     (computed exactly in Cl(2,3), three rational z): imaginary part of sign `-z_0`, real regulator `-eps^2/2`,
     the form `restricted-dirac...` and `field-strength-cancels...` use (`sigma_eps = sigma + I_4 eps(t - t') - eps^2/2`
     for the other ordering).
   - With `+eps^2` the regularised denominator has real zeros: at z_0 = 0 (h = 0), z = (0, 7, 1, 0), eps = 5,
     sigma = -25 and sigma + eps^2 = 0 exactly; with `-eps^2/2` it is -75/2, never zero at z_0 = 0.
   - Script: /tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/R02/step7.py (9 checks, all pass).
   **Proposed fix (proof only):** "is $\lim_{\epsilon\to 0}$ of $1/(\sigma_{l} - I_{4}\epsilon h_{l} - \tfrac12\epsilon^{2})$" and
   "the pullback $\Psi_{l}^{*}$ of $1/(\tfrac12 Q(z) - I_{4}0\,h)$"; the other ordering with the opposite sign of $I_4$.
   The conclusion (the limit $I_4\nabla D_+ e_0$) is unaffected.
2. Lay level stale: "What it does not prove is the companion statement ... That part stays an assumption." Clause (b) of
   (HS) is now proved (synthesis.hadamard-scaling-limit-premise, a theorem since version 4; formal (v) says so). Proposed:
   "... is not proved here; a later result in the series proves it."
3. Formal (iii) calls (HS) "Premise \claimref{synthesis.hadamard-scaling-limit-premise}"; it is a Theorem now. Proposed:
   "clause (a) of version 2 of (HS), now Theorem \claimref{...}".
4. One-liner is plain text (hb(x0), Delta^(1/2), l^2 Q/2) while every other entity's one-liner is LaTeX; GA content fine.
5. Index readings (`\Gamma^{\lambda}{}_{\mu\nu}`, `\tfrac{l}{2}(\partial_\rho g_{\mu\nu})...`) are marked as readings beside
   the GTG forms; acceptable under the conventions (parenthetical readings), listed for completeness.

## synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state (v4)

1. Premise hygiene (for Leon, an edge change): holds_given is (N+), J3 and (Q). (N+) enters through
   `synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit@4`, cited only for the weight-1/2 boost as the dilation
   (proof (iii)) and the half-thermal products; both are in the premise-free
   `synthesis.stationary-generator-states-and-the-edge-scaling@1` (i), (iii). J3 and (Q) enter through
   `synthesis.attachment-conformal-energy-is-generated-by-z@4`, cited only for the realisation of the Moebius closing by
   conformal rotors in (i). Proposed: repoint the first edge; for the second, either keep (the realisation is part of (i))
   or cite the rotor computation, which the check does itself, and make the attachment a lineage link.
2. Notation: proof (i) names the composite inversion rotor `J`, and (i) uses `nu` for the vector with `nInf = nu + e_-`;
   in this subject J is the boundary-mode unit and J_a the modular conjugations, nu the null translations. Proposed:
   rename the rotor (for example $R_{\mathrm{inv}}$) and the vector (for example $e_{+}$ if that is what it is).
3. GA: the 2x2 matrices of proof (i) are labelled readings of Moebius maps beside the rotor action; acceptable.
