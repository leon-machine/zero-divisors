# Resolve sweep, group G2 (18 entities)

All 18 entities were changed. No bare i remains in any level or proof. Every outside_ga declaration is removed: 18 removed, 0 kept.

Versioning follows the coordinator's correction: each entity is + 1 on its current version, with a credit entry for the new version and the extraction note `maintainer_pass_resolve_units`. Every file is kept, and no check.py was edited.

Final state:
- detector (both forms): 0 hits on all 18.
- `tp check --layers 1,2,3 --keep-going --author leon`: no error or warning on any G2 entity. The only finding is a pre-existing I213 (subject) on state-selection-r-and-le-against-t05, which is outside this pass's scope.

## Entities (old -> new version; unit; declaration)

- synthesis.dirac-causal-propagator-between-nearby-null-leaves-tends-to-the-generator-car-on-every-geodesic-null-hypersurface: 3 -> 4.
  - Unit: I_4 (U1 Hadamard chain, U3 scalar form). The regulator is sigma + I_4 epsilon(t(x) - t(x')), and every I_4 0 sgn v, (s - t -+ I_4 0)^{-1} and log(s -+ I_4 0) is written with I_4. Numbers act on the right, as the entity states.
  - Cites std-algebra.complexification-is-the-odd-extension(iii) for "the square of a shifted vector is a number".
  - Declaration removed.
- synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car: 3 -> 4.
  - Unit: I_4 for the regulator sigma + I_4 epsilon s, its I_4 0, and the prose "i0" in the technical level.
  - The Kay-Wald form quoted in the proof becomes (U_1 - U_2 - I_4 epsilon)^{-2}, "the source writes i for I_4".
  - Declaration removed.
- synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces: 4 -> 5.
  - Unit: I_4 for the I_4 0 of a time function, sigma_epsilon = sigma + I_4 epsilon s, and the transverse integrand. This matches the kernels and logarithms, which were already in span{1, I_4}.
  - Declaration removed.
- synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field: 4 -> 5.
  - Unit: I_4, with the vector-form shifts rewritten in scalar form:
    - Q(y - y' - i0 e_0) -> Q(y - y') - I_4 0 <y - y', e_0>
    - Q(z - i0 e_0)/2 -> Q(z)/2 - I_4 0 <z, e_0>
    - -+ I_4 0, sigma_l + I_4 epsilon h_l, Q(z)/2 + I_4 0 h, and D_+ with I_4 0 xi_0.
  - I_5 is not used, because the kernels carry I_4 and the two units would meet in one distribution (I_4 I_5 = -e, not -1).
  - Declaration removed.
- synthesis.hadamard-scaling-limit-premise: 5 -> 6.
  - Unit: I_4. The "I_4 0-regularised" restriction is written so in (c) and in the setting note, and the conventions sentence now says the shift is written in scalar form with I_4.
  - Declaration removed. Postulate status unchanged.
- synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability: 2 -> 3.
  - U4, unit I_4 (abstract Hilbert space, U1): the modular unitaries become Delta_W^{I_4 t}.
  - source_formal holds the source's form plus "The source writes $i$ for $I_4$." J_W is the modular conjugation, not a unit.
  - Declaration removed.
- synthesis.imported-loewner-theorem-and-yafaev-hankel-sign-criterion: 1 -> 2.
  - U4, unit I_4. There was no bare i; the declaration covered the complex analysis.
  - One opening sentence now reads the numbers in span{1, I_4}: upper half-plane x + I_4 y with y > 0, imaginary part y, and the bar as I_4 -> -I_4.
  - source_formal added. Declaration removed.
- synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection: 1 -> 2.
  - U4, unit I_4: Z = (1 + I_4 Theta)/(1 + I_4) and P = I_4 d/du.
  - source_formal added. Declaration removed.
- synthesis.null-ordering-of-counted-units-is-zeta-symmetric: 2 -> 3.
  - Unit: I_4. The twist phase e^{2 pi I_4 delta} belongs to a chiral component of the horizon continuum, so U1 applies.
  - Declaration removed.
- synthesis.phase-flow-is-time-rotor-flow-kms-continuation: 2 -> 3.
  - Unit: J = e_2 e_3 (U2), cited in the formal level.
  - The complexified window is Cl(p,q) + Cl(p,q)J. The window vectors lie in the radial plane and in tower planes, and J commutes with them. The frame star, with e_2 and e_3 as frame generators, has J* = -J, so it is conjugate-linear. h is read in the centre span{1, J}.
  - Written with J: Ad(e^{JtH}), e^{-J kappa t}, the pairing flow, tau_{-J lambda} with tau_z = Ad(e^{JzK}), and the Gaussian-rational field span_Q{1, J}.
  - The KMS swap is written omega_beta(A tau_{J beta}(B)) = omega_beta(BA) with tau_{J beta} = Ad(e^{-beta K}). For beta != 0 this is the KMS condition; at beta = 0 it is the trace property.
  - My first draft used the U3 odd-extension unit. After the coordinator's ruling I rewrote it with J. The odd unit is not used in the levels and is not identified with J.
  - Declaration removed.
- synthesis.point-spectrum-boost-admits-no-half-sided-translations: 3 -> 4.
  - Unit: J (U2) for the boundary-mode algebra and its GNS spaces: e^{-J omega_j t}, Ad(e^{JtK}), [K, P] = JcP, P = X + JY, Delta^{Js}, rho^{Js}, e^{-2 pi J k} and e^{-J pi(2k+1)}.
  - The Borchers relation of the imported Fact is read with that unit in the GNS space.
  - The Definition's mode-set letter J is named once as such.
  - Declaration removed.
- synthesis.positive-null-energy-gives-r-premises: 6 -> 7.
  - Unit: I_4 for the one remaining occurrence, the Borchers relation in the proof of (v): Delta^{I_4 s} U(a) Delta^{-I_4 s}.
  - The window commutator mentioned in the old reason exists only in check.py.
  - Declaration removed.
- synthesis.q-splits-maximum-entropy-affine-weights: 4 -> 5.
  - Unit: J (U2). The array's numbers are read in span{1, J}, and J commutes with the radial plane and with every vector orthogonal to spacetime.
  - Written with J: Ad(e^{JtK_geo}), e^{-J lambda_m t}, e^{J(omega_k - omega_l)t}, alpha_t and e^{-J pi(2k+1)}.
  - The rotation generators J_a of (v) are noted as distinct from the unit.
  - Declaration removed.
- synthesis.r-lambda-regularity-cosmological-horizon: 4 -> 5.
  - Unit: hat-I = I_V e, the U3 odd-extension unit of Cl(|J|,|J|). It is cited in the formal level and gives Ad(e^{hat-I t omega_j K_j}) and F(t + hat-I p). The reason is in "Possible errors found" below.
  - Declaration removed. Postulate status unchanged.
- synthesis.r-le-i-independent-spectrum-condition-separates: 3 -> 4.
  - Unit: J (U2): Ad(e^{J t omega_k K_k}), and imaginary time Jp with alpha^k_{Jp}.
  - Declaration removed.
- synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel: 2 -> 3.
  - Unit: I_4 for sigma_epsilon = sigma + I_4 epsilon(t - t') - epsilon^2/2 and every expression it generates:
    - nabla sigma + epsilon(nabla t)I_4 (unit on the right)
    - A_epsilon, C_epsilon, s_0 + I_4 g epsilon
    - the contour shift eta -> eta + I_4 lambda epsilon M^{-1}s_1
    - the imported I_4 0 prescription
  - Numbers act on the right, as stated. "The the" typo in the proof fixed.
  - Declaration removed.
- synthesis.s-wave-array-is-a-boundary-mode-set: 3 -> 4.
  - Unit: J (U2): e^{-J kappa|k| t}, the conjugation step (using J* = -J), and e^{-J omega t}.
  - The Definition's mode-set letter J is written out as "the mode set Z \ {0}".
  - Declaration removed.
- synthesis.state-selection-r-and-le-against-t05: 3 -> 4.
  - Unit: J (U2): Ad(e^{J t sum omega_k K_k}), e^{+-J omega t}, and F_{a,b}(t + Jp). That last relation is the core result's KMS relation tau_{J beta}.
  - Declaration removed.

Wherever J is the unit, the entity states once that J commutes with the radial plane and with every vector orthogonal to spacetime, hence with every mode. Core result 2 proves this only for e_0 and e_1. The extension to tower planes is immediate, since a bivector commutes with the vectors orthogonal to its plane, but it is stated, not cited.

## Could not resolve

None.

## Possible errors found

1. **Possible sign slip in hadamard-dirac-states-scale..., proof Step 7.** It writes 1/(Q(z)/2 + I_4 0 h), with h of the sign of z^0, and identifies it by time-function independence with the flat boundary value Q(z)/2 - I_4 0 <z, e_0>. On the face of it the I_4 0 terms have opposite signs. Compare also the formal level's sigma_{+-} with -+ I_4 0, and the regulator sigma_l + I_4 epsilon h_l + epsilon^2, where the other entities use - epsilon^2/2. Either an ordering label or a sign of h is off. I have not fixed it.
2. **r-lambda unit (for Leon or the coordinator).** The atom of the cosmological horizon lies in Pi_Lambda = span{e_0, e_W} of the conformal model. e_W is not a spacetime direction, so the transverse plane is not canonical: every spatial bivector e_1e_2, e_2e_3, e_1e_3 commutes with Pi_Lambda. J = e_2 e_3 would therefore be an arbitrary choice. The definition makes the algebra "the complexification of Cl(|J|,|J|)", which is exactly U3, so I used hat-I. This departs from the "one unit, J, for the atom's phase flow" ruling, which was stated for the radial atom.
   - The Definition obj.synthesis.cosmological-horizon-boundary-modes (group G1) should carry the same unit as r-lambda. In that Definition the letter J also names the mode set.
3. **phase-flow, scope of (iii).** The original complexified a general Cl(p,q). The J version rests on a sentence I added: the window vectors lie, as the boundary modes do, in the radial plane and in tower planes. Clauses (i), (ii) and (iv) are real and unaffected. If (iii) is meant for windows not embedded in that way, the U3 reading (complexification by I_V e) is the exact alternative.
4. **Name clashes.** The letter J is the unit, the Definition's mode set (in point-spectrum, s-wave and r-lambda) and the su(2) generators J_a (in q-splits). Each entity now says which is which. A store-wide rename of the mode set would remove the clash.
5. **Metadata and checks still write i.** check.py docstrings and code, for example "[K, P] = i c P" in positive-null-energy, are not edited, per the brief. r-lambda's `extraction.flow_note` still says e^{-i omega_j t}; it is metadata, not a level, and was left as it was.
