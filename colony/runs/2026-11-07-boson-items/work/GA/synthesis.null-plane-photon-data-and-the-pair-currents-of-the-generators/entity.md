---
id: synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators
kind: claim
version: 1
title: Null-plane photon data and the pair currents of the generators
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, bosonisation, car-algebra, ladder-pairs, horizons, pseudoscalar-and-centre, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-07-boson-items
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-boson-items
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  - hawking.current-commutator-exactly-edge-split@4
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays@5
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes@5
  - synthesis.null-vacuum-on-a-horizon-generator@1
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_maxwell_symplectic_current_identity
- kind: check
  ref: check.py::check_null_flux_has_only_transverse_data
- kind: check
  ref: check.py::check_null_energy_duality_and_helicity_phase
- kind: check
  ref: check.py::check_two_channel_currents_on_a_window
- kind: check
  ref: check.py::check_densities_are_helicity_zero_and_flips_helicity_one
- kind: check
  ref: check.py::check_flip_defect_and_the_generator_bound
- kind: proof
  derivation: main
extraction:
  open_problem: bos.gauge-bosons
  note: >-
    Attack on the run target bos.gauge-bosons (the quantum algebra of the gauge bosons: derive the canonical relations of
    a free gauge field from the tower with the unit J or I4, or an obstruction; say what part of photon quantisation the
    ladder gives). Route: the null plane, the series' setting for horizon modes, where gauge fixing needs no indefinite
    form. Everything is derived in the spacetime algebra and the tower planes; no imported Fact is a premise. Stored and
    cited: the generator CAR on a null plane and the null vacuum on each generator
    (synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes,
    synthesis.null-vacuum-on-a-horizon-generator), the two chirality channels of the canonical part and their rotation
    phases about the generator (synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (iii), (iv)), the
    window edge identity for one channel (hawking.current-commutator-exactly-edge-split), the hopping quasi-spin
    (synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum (ii)). Compared, not used:
    the store's photon takes its canonical relations from the palatial polynomial representation
    (field-theory.fock-space-maxwell-modes, with the imported statistics Fact), and the covariant route needs the
    Krein-form premise (synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields); clause (ii) shows the
    null-plane route needs neither for the free field. Prior art, not premises, cited from memory and not verified this
    run: light-front quantisation of electrodynamics in the gauge n.A = 0 (J. B. Kogut and D. E. Soper, Phys. Rev. D 1
    (1970) 2901), whose transverse null data are clause (ii); the level-one u(2) current algebra of two chiral fermions
    (for instance P. Goddard and D. Olive, Int. J. Mod. Phys. A 1 (1986) 303); the composite ("neutrino") theory of
    light (P. Jordan, 1935; M. H. L. Pryce, Proc. Roy. Soc. A 165 (1938) 247, who found that photons built from
    fermion pairs fail to be exact bosons), of which clause (v) is a finite, exact form on a null plane with the
    generators as the copies. New here: (i) and (ii) in the spacetime algebra; (iii) the identification of the field
    theory's unit I4 with the transverse bivector J on null data and of the two helicities as the two relative
    orientations of the rotation and translation phases; (iv) and (v) on the tower. Ledger: (i) to (iii) are
    transport-absent (free Maxwell theory in the spacetime algebra); (iv) and (v) are transport-convenient (the
    generator CAR, its channels and the null vacuum are the series' horizon setting). What is not claimed: the
    transverse dynamics (the part of the null Hamiltonian with transverse derivatives), the coupling of the photon to
    charges, convergence of states (only commutators in mean square on the vacuum), null rotations, gluons, W, Z or
    the Higgs.
---

## formal
Work in $\Cl(1,3)$ with $\gamma_{0}^{2} = 1$, $\gamma_{i}^{2} = -1$, $I_{4} = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$, a null plane $N$ whose generators run along $n = \gamma_{0} + \gamma_{3}$, the second null direction $\bar n = \gamma_{0} - \gamma_{3}$, transverse vectors in the span of $\gamma_{1}, \gamma_{2}$, and $J = \gamma_{1}\gamma_{2}$ ($J = -I_{4}B$, $B = \gamma_{3}\gamma_{0}$, as in \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}). For a vector potential $A$ put $F = \nabla\wedge A$, $F\cdot A = \langle FA\rangle_{1}$, $T(a) = -\tfrac12 FaF$, $\partial_{n} = n\cdot\nabla$, and write $A = \mu\,n + \nu\,\bar n + A_{\perp}$.
\begin{enumerate}
\item[(i)] \emph{(The symplectic current; proved.)} For any two potentials, $\omega = F_{1}\cdot A_{2} - F_{2}\cdot A_{1}$ satisfies $\nabla\cdot\omega = (\nabla\cdot F_{1})\cdot A_{2} - (\nabla\cdot F_{2})\cdot A_{1}$ identically; so $\omega$ is conserved on solutions of the free Maxwell equation $\nabla F = 0$.
\item[(ii)] \emph{(Null data; proved.)} $n\cdot(n\cdot F) = 0$, so $n\cdot F = \kappa n + E_{\perp}$ with $E_{\perp}$ transverse; $E_{\perp}$ is gauge invariant and $n\cdot T(n) = -E_{\perp}^{2} > 0$ for $E_{\perp} \ne 0$: the null energy flux through $N$ is positive definite on $E_{\perp}$ and depends on nothing else. In the gauge $n\cdot A = 0$ ($\nu = 0$), $n\cdot F = \partial_{n}A$ and
\[
n\cdot\omega = \partial_{n}A_{1\perp}\cdot A_{2\perp} - \partial_{n}A_{2\perp}\cdot A_{1\perp}
\]
identically: the flux of $\omega$ through $N$ contains the two transverse components alone, with no longitudinal coefficient and no transverse derivative. Hence the free photon's canonical data on $N$ are $E_{\perp} = \partial_{n}A_{\perp}$, two real fields on each generator, data on distinct generators are independent, and no indefinite form enters. On a generator closed to period $2\pi$ (affine parameter $\lambda$) with transverse cell of area $s$, $A_{\perp} = \sum_{i = 1,2}\sum_{k \ge 1}(a_{ik}\cos k\lambda + b_{ik}\sin k\lambda)\gamma_{i}$ (the zero mode, constant $A_{\perp}$, carries no $E_{\perp}$), the flux of $\omega$ is $2\pi s\sum k(a_{ik}b_{ik}' - b_{ik}a_{ik}')$ and the null energy $P = \pi s\sum k^{2}(a_{ik}^{2} + b_{ik}^{2})$ generates the future null translations for the bracket $\{a_{ik}, b_{jl}\} = \delta_{ij}\delta_{kl}/(2\pi sk)$; with the quantisation rule $[\,,\,] = J\{\,,\,\}$ the modes $\alpha_{ik} = (\pi s)^{1/2}k(a_{ik} + Jb_{ik})$ satisfy $[\alpha_{ik}, \alpha_{jl}^{*}] = k\,\delta_{ij}\delta_{kl}$, $[\alpha_{ik}, \alpha_{jl}] = 0$, $[P, \alpha_{ik}] = -k\alpha_{ik}$: on each generator, two commuting chiral current algebras ($\alpha_{i,-k} = \alpha_{ik}^{*}$). The orientation of $J$ cancels between the quantisation rule and the frequency $e^{-Jk\lambda}$, so the sign $+k$ is fixed by positive null energy alone.
\item[(iii)] \emph{(The unit and the two helicities; proved.)} For transverse $u$, $I_{4}(n\wedge u) = (n\wedge u)J = n\wedge(uJ) = -J(n\wedge u)$: on null data the field theory's unit $I_{4}$ is the transverse quarter turn, right multiplication by $J$. The data form one field $\varepsilon = \gamma_{1}E_{\perp}$ with values in $\mathrm{span}\{1, J\}$, and the rotation $E_{\perp} \mapsto RE_{\perp}\tilde R$ about the generator, $R = e^{-J\phi/2}$, is $\varepsilon \mapsto \varepsilon e^{J\phi}$. So, with $J$ the unit of both the rotation phase and the frequency $e^{-Jk\lambda}$, the helicity $\pm 1$ annihilators $\alpha_{\pm,k} = 2^{-1/2}(\alpha_{1k} \mp J\alpha_{2k})$, multiplied by $e^{\pm J\phi}$ under that rotation and by $e^{-Jk t}$ under the null translation by $t$, are the modes whose rotation phase turns in the same or in the opposite sense as their translation phase: the two helicities are the two relative orientations of the transverse rotation and the null translation.
\item[(iv)] \emph{(Pair currents of the generators; proved.)} On each generator $g$ let $c_{ga,k}$, $a \in \{+, -\}$ the two chirality channels of the canonical part, $k = 1, \dots, L$ the levels of a window, be tower modes ($c^{*} = v$, $c = w$ of distinct planes, Fact \claimref{field-theory.imported-tower-limit}); modes of distinct generators are distinct planes, the generator CAR being transversally ultralocal (\claimref{synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes}(i)). Put $j^{xy}_{m} = \sum_{k}c_{x,k}^{*}c_{y,k+m}$ (sum over $k, k + m$ in the window) for labels $x, y$ (generator and channel). Exactly,
\[
[j^{xy}_{m}, j^{zu}_{l}] = \delta_{yz}\!\!\sum_{k,\,k+m,\,k+m+l}\!\! c_{x,k}^{*}c_{u,k+m+l} \;-\; \delta_{xu}\!\!\sum_{k,\,k+l,\,k+l+m}\!\! c_{z,k}^{*}c_{y,k+l+m},
\]
which on vectors edge-clean at the depth of the indices is $\delta_{yz}j^{xu}_{m+l} - \delta_{xu}j^{zy}_{m+l} + m\,\delta_{xu}\delta_{yz}\delta_{m+l,0}$ (Theorem \claimref{hawking.current-commutator-exactly-edge-split} is the case $x = y = z = u$), and $[H, j^{xy}_{m}] = -mj^{xy}_{m}$ for $H = \sum_{x,k}k\,n_{x,k}$. With the tower's unit $J$ and the channel phases of \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(iv), the rotation about a generator is $U(\phi) = \prod_{a,k}(1 + (z_{a} - 1)n_{a,k})$, $z_{\pm} = e^{\pm J\phi/2}$, unitary for the CAR adjoint; the densities $j^{g\pm,g\pm}_{m}$ are invariant (helicity $0$) and the flip currents $j^{g+,h-}_{m}$, $j^{g-,h+}_{m}$ are multiplied by $e^{J\phi}$, $e^{-J\phi}$ (helicity $\pm 1$), the transformation of $\alpha_{\pm,k}$ in (iii).
\item[(v)] \emph{(The photon's relations are collective; proved, with the limit argued.)} For a matrix $M$ over the generators with entries in $\mathrm{span}\{1, J\}$ let $\varepsilon_{m} = \sum_{g,h}M_{gh}j^{g+,h-}_{m}$, of helicity $+1$, and let $\Omega$ be the bottom-filled window in every channel of every generator, the band restriction of the null vacuum (\claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii), \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(vi)). Then $[\varepsilon_{m}, \varepsilon_{l}] = 0$, $\varepsilon_{m}\Omega = 0$ for $m \ge 1$, the central value of $[\varepsilon_{m}, \varepsilon_{m}^{*}]$ on $\Omega$ is $m\operatorname{tr}MM^{*}$, and for $m < l$ the defect $D = [\varepsilon_{m}, \varepsilon_{l}^{*}]$ has
\[
\|D\Omega\|^{2} = 2(l - m)\,\|MM^{*}\|_{F}^{2} \;\ge\; \frac{2(l - m)\,(\operatorname{tr}MM^{*})^{2}}{N}
\]
on $N$ generators, with equality exactly when $MM^{*}$ is scalar. Normalised to the photon's central term ($\operatorname{tr}MM^{*} = 1$), the defect is at least $2(l - m)/N$: on one generator ($N = 1$) it is $2(l - m)$, so the flip currents of a single generator never carry the photon's relations, and no smearing over finitely many generators removes it. For a transversally smeared field, $M = \mathrm{diag}(s^{1/2}f(y_{g}))$ with $s\sum_{g}|f(y_{g})|^{2} = 1$ ($s$ the transverse cell area), the defect is $2(l - m)\,s\cdot s\sum_{g}|f(y_{g})|^{4}$, which tends to $0$ as $s \to 0$ on the continuum of generators of the null plane (argued, by Riemann sums). So the helicity-covariant relations of (ii) and (iii), $[\alpha_{\pm,k}, \alpha_{\pm,l}^{*}] = k\delta_{kl}$, are carried by transversally smeared flip currents in mean square on the null vacuum in that limit, with the same linear dispersion along the generator, while the densities carry exact canonical pairs of helicity $0$ on every generator.
\end{enumerate}
\emph{Reading.} The ladder gives the kinematics of photon quantisation on a null plane: two transverse chiral fields per generator with positive null energy and no indefinite form, and the sign of their relations fixed by positive null energy whatever the orientation of the unit. From the fermions of the generators it gives exact canonical pairs only of helicity $0$, and the photon's helicity $\pm 1$ relations only collectively, as transversally smeared spin-flip pairs over many generators, with an exact defect of order $1/N$ and a normalisation that vanishes with the cell size, so that the composite is free. It does not give the transverse dynamics, the coupling to charges, convergence of states, null rotations, or the non-abelian bosons.

## technical
On a null plane the free Maxwell field needs no indefinite metric. The spacetime-algebra symplectic current $\omega = F_{1}\cdot A_{2} - F_{2}\cdot A_{1}$ is conserved on free fields, and in the gauge $n\cdot A = 0$ its flux through the plane is $\partial_{n}A_{1\perp}\cdot A_{2\perp} - \partial_{n}A_{2\perp}\cdot A_{1\perp}$: only the two transverse components, with no transverse derivative. The gauge-invariant null data $E_{\perp}$ (the transverse part of $n\cdot F$) carry the positive null energy $-E_{\perp}^{2}$, and quantising with the unit $J$ gives, on each generator, two commuting chiral current algebras $[\alpha_{ik}, \alpha_{jl}^{*}] = k\delta_{ij}\delta_{kl}$, whose sign does not depend on the orientation of $J$. On null data the unit $I_{4}$ acts as right multiplication by the transverse bivector $J$, and the two helicities are the two relative orientations of the rotation phase $e^{\pm J\phi}$ and the translation phase $e^{-Jk\lambda}$.

The fermions of the generators supply two chirality channels per generator, whose pair currents obey the level-one current algebra exactly on edge-clean window vectors, with linear dispersion along the generator. Densities have helicity $0$; spin-flip currents have helicity $\pm 1$. For a flip current $\varepsilon_{m} = \sum M_{gh}j^{g+,h-}_{m}$ smeared over $N$ generators, the central value is $m\operatorname{tr}MM^{*}$ and the defect $[\varepsilon_{m}, \varepsilon_{l}^{*}]$, $m < l$, has norm squared $2(l - m)\|MM^{*}\|_{F}^{2} \ge 2(l - m)(\operatorname{tr}MM^{*})^{2}/N$ on the null vacuum, with equality for uniform smearing. One generator never carries the photon's relations; transversally smeared flip currents do, in mean square, in the limit of the continuum of generators.

## lay
On a light front the electromagnetic field has a simple set of free data: two numbers per light ray, its two transverse components, with positive energy and no unphysical modes. The horizon's fermions, two kinds per light ray, can be paired up into wave-like modes. Pairs that keep the fermion's kind give exact boson waves, but they do not turn under rotations about the light ray as light does. Pairs that flip the kind turn like light's two helicities, but on a single light ray they are not exact bosons; averaged over many neighbouring light rays the error shrinks like one over their number, so on the continuum of rays they reproduce the photon's commutation relations as a collective effect. The result says which part of photon quantisation the series' fermions give and which they do not: the dynamics across rays and the coupling to charges are not given.

## one-liner
On a null plane the free photon's data are two transverse chiral fields per generator (from the spacetime-algebra symplectic current, no indefinite form); the generators' pair currents give them exactly at helicity $0$, and at helicity $\pm 1$ only collectively, with defect $2(l - m)\|MM^{*}\|_{F}^{2} \ge 2(l - m)/N$ over $N$ generators (normalised), vanishing for smeared fields on the continuum of generators.
