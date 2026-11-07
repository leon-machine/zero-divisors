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
  - field-theory.fock-space-maxwell-modes@5
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
    form. Everything on the tower is derived in the tower planes; (i) to (iii) are free Maxwell theory in the spacetime
    algebra; no imported Fact is a premise. Stored and cited: the generator CAR on a null plane and the null vacuum on
    each generator (synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes,
    synthesis.null-vacuum-on-a-horizon-generator), the two chirality channels of the canonical part and their weights
    about the generator (synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (iii), (iv)), the window
    edge identity for one channel (hawking.current-commutator-exactly-edge-split), the band restriction of the null
    vacuum (synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum (vi)); compared in (iii):
    field-theory.fock-space-maxwell-modes (ii), (iii). Results stored with this one, cited as mentions: the window
    identity (synthesis.density-modes-bosonise-only-along-one-null-direction (i)), the mode rotation
    (synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (i)), the unit J
    (synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower), the dispersion of band modes
    (synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (ii), (iii)) and the
    quasi-spin capacity of helicity-one pairs (synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins
    (iv)). Compared, not used: the store's photon takes its canonical relations from the palatial polynomial
    representation (field-theory.fock-space-maxwell-modes, with the imported statistics Fact), and the covariant route
    needs the Krein-form premise (synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields); the null-plane
    route needs neither for the free field. Prior art, not premises: light-front quantisation of electrodynamics in the
    gauge n.A = 0, whose transverse null data and complete characteristic data are clause (ii) (J. B. Kogut and D. E.
    Soper, Phys. Rev. D 1 (1970) 2901, verified); the covariant phase space, whose symplectic current is clause (i)
    (C. Crnkovic and E. Witten, 1987; J. Lee and R. M. Wald, J. Math. Phys. 31 (1990) 725; cited from memory);
    discretised light-cone quantisation for the closed generator (T. Maskawa and K. Yamawaki, 1976; H.-C. Pauli and S. J.
    Brodsky, 1985; cited from memory); the level-one u(2) current algebra of two chiral fermions (P. Goddard and D.
    Olive, Int. J. Mod. Phys. A 1 (1986) 303, cited from memory); the composite ("neutrino") theory of light (P. Jordan,
    1935, cited from memory; M. H. L. Pryce, "On the neutrino theory of light", Proc. Roy. Soc. A 165 (1938) 247,
    verified, who found that photons built from fermion pairs fail to be exact bosons), of which clause (v) is a finite,
    exact form on a null plane with the generators as the copies. New here: the spacetime-algebra form of (i) and (ii);
    in (iii) the computed relation that on the null data I4 is right multiplication by -J_perp, and the helicities as
    the relative orientations of rotation and translation phases (a restatement of field-theory.fock-space-maxwell-modes
    (iii) on the null data); and, as the main new content, the exact defect 2(l - m)||MM*||_F^2 of (v) with its 1/N
    bound. Ledger: (i) to (iii) are transport-absent (free Maxwell theory in the spacetime algebra); (iv) and (v) are
    transport-convenient (the generator CAR, its channels and the null vacuum are the series' horizon setting). What
    is not claimed: the transverse dynamics (the part of the null Hamiltonian with transverse derivatives), the
    coupling of the photon to charges, convergence of states (only commutators in mean square on the vacuum), null
    rotations, gluons, W, Z or the Higgs.
---

## formal
Work in $\Cl(1,3)$ with $\gamma_{0}^{2} = 1$, $\gamma_{i}^{2} = -1$, $I_{4} = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$, a null plane $N$ whose generators run along $n = \gamma_{0} + \gamma_{3}$, the second null direction $\bar n = \gamma_{0} - \gamma_{3}$, transverse vectors in the span of $\gamma_{1}, \gamma_{2}$, and the transverse bivector $J_{\perp} = \gamma_{1}\gamma_{2}$ ($J_{\perp} = -I_{4}B$, $B = \gamma_{3}\gamma_{0}$, the bivector written $J$ in \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}). Separately, $J$ denotes the tower's kernel bivector, $J^{2} = -1$, $J^{*} = -J$, commuting with every tower mode (the unit of \claimref{synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower}); $J_{\perp}$ acts on spacetime multivectors, $J$ on the operators, and the two are not identified. For a vector potential $A$ put $F = \nabla\wedge A$, $F\cdot A = \langle FA\rangle_{1}$, $T(a) = -\tfrac12 FaF$, $\partial_{n} = n\cdot\nabla$, and write $A = \mu\,n + \nu\,\bar n + A_{\perp}$.
\begin{enumerate}
\item[(i)] \emph{(The symplectic current; proved.)} For any two potentials, $\omega = F_{1}\cdot A_{2} - F_{2}\cdot A_{1}$ satisfies $\nabla\cdot\omega = (\nabla\cdot F_{1})\cdot A_{2} - (\nabla\cdot F_{2})\cdot A_{1}$ identically; so $\omega$ is conserved on solutions of the free Maxwell equation $\nabla F = 0$.
\item[(ii)] \emph{(Null data; proved, with the quantisation rule a hypothesis.)} $n\cdot(n\cdot F) = 0$, so $n\cdot F = \kappa n + E_{\perp}$ with $E_{\perp}$ transverse; $E_{\perp}$ is gauge invariant and $n\cdot T(n) = -Q(E_{\perp}) > 0$ for $E_{\perp} \ne 0$: the null energy flux through $N$ is positive definite on $E_{\perp}$ and depends on nothing else. In the gauge $n\cdot A = 0$ ($\nu = 0$), $n\cdot F = \partial_{n}A$ and
\[
n\cdot\omega = \partial_{n}A_{1\perp}\cdot A_{2\perp} - \partial_{n}A_{2\perp}\cdot A_{1\perp}
\]
identically: the flux of $\omega$ through $N$ contains the two transverse components alone, with no longitudinal coefficient and no transverse derivative. Taking, as in light-front quantisation, this flux (zero modes dropped) as the symplectic form of the free field, its canonical data on $N$ are $E_{\perp} = \partial_{n}A_{\perp}$, two real fields on each generator, data on distinct generators are independent, and no indefinite form enters. On a generator closed to period $2\pi$ (affine parameter $\lambda$; the discretised light-cone setting) with transverse cell of area $s$, $A_{\perp} = \sum_{i = 1,2}\sum_{k \ge 1}(a_{ik}\cos k\lambda + b_{ik}\sin k\lambda)\gamma_{i}$ (the zero mode carries no $E_{\perp}$), the flux of $\omega$ is $2\pi s\sum k(a_{ik}b_{ik}' - b_{ik}a_{ik}')$ and the null energy $P = \pi s\sum k^{2}(a_{ik}^{2} + b_{ik}^{2})$ generates the future null translations for the bracket $\{a_{ik}, b_{jl}\} = \delta_{ij}\delta_{kl}/(2\pi sk)$. Under the quantisation hypothesis $[\,,\,] = J\{\,,\,\}$ (Dirac's rule, with the tower's unit $J$, chosen because (v) realises these modes on tower pairs; with the field theory's unit $I_{4}$ of the unit principle the algebra is the same), the modes $\alpha_{ik} = (\pi s)^{1/2}k(a_{ik} + Jb_{ik})$ satisfy $[\alpha_{ik}, \alpha_{jl}^{*}] = k\,\delta_{ij}\delta_{kl}$, $[\alpha_{ik}, \alpha_{jl}] = 0$, $[P, \alpha_{ik}] = -k\alpha_{ik}$: on each generator, two commuting chiral current algebras ($\alpha_{i,-k} = \alpha_{ik}^{*}$). The orientation of the unit cancels between the quantisation rule and the modes, so the sign $+k$ is fixed by positive null energy alone.
\item[(iii)] \emph{(The field theory's unit on the null data and the two helicities; proved.)} For transverse $u$, $I_{4}(\bar n\wedge u) = J_{\perp}(\bar n\wedge u) = -(\bar n\wedge u)J_{\perp}$, while $I_{4}(n\wedge u) = (n\wedge u)J_{\perp}$. The null data sit in the $\bar n\wedge E_{\perp}$ part of $F$ ($E_{\perp}(n\wedge u) = 0$), and $E_{\perp}(I_{4}F) = J_{\perp}E_{\perp} = -E_{\perp}J_{\perp}$: on the null data the field theory's unit $I_{4}$ is the transverse quarter turn, right multiplication by $-J_{\perp}$. With $\varepsilon = \gamma_{1}E_{\perp} \in \mathrm{span}\{1, J_{\perp}\}$, $\varepsilon(I_{4}F) = -J_{\perp}\varepsilon(F)$, so the null data of a field of positive frequency relative to $I_{4}$, $e^{-I_{4}k\lambda}$, have $\varepsilon \propto e^{+J_{\perp}k\lambda}$, while the rotation $E_{\perp} \mapsto RE_{\perp}\tilde R$ about the generator, $R = e^{-J_{\perp}\phi/2}$, is $\varepsilon \mapsto \varepsilon e^{J_{\perp}\phi}$: every null datum of positive frequency relative to $I_{4}$ rotates in the same sense as it translates, one helicity, as in \claimref{field-theory.fock-space-maxwell-modes}(ii), (iii) (null bivectors are $I_{4}$-stable, and with the unit $I_{4}$ positive frequency is helicity $+1$); the negative-frequency data rotate in the opposite sense. On the quantised modes of (ii), the rotation acts on the components and multiplies $\alpha_{\pm,k} = 2^{-1/2}(\alpha_{1k} \mp J\alpha_{2k})$ by $e^{\pm J\phi}$, while the null translation by $t$ multiplies both by $e^{-Jkt}$: the two helicities are the two relative orientations of the transverse rotation and the null translation.
\item[(iv)] \emph{(Pair currents of the generators; proved.)} Divide the transverse plane into cells of area $s$, one generator $g$ per cell (the cell form of the transverse delta function of the generator CAR, \claimref{synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes}(i)). On each generator let $c_{ga,k}$, $a \in \{+, -\}$ the two chirality channels of the canonical part, $k = 1, \dots, L$ the levels of a window, be tower modes ($c^{*} = v$, $c = w$ of distinct planes, Fact \claimref{field-theory.imported-tower-limit}), and put $j^{xy}_{m} = \sum_{k}c_{x,k}^{*}c_{y,k+m}$ (sum over $k, k + m$ in the window) for labels $x, y$ (generator and channel). The window identity (\claimref{synthesis.density-modes-bosonise-only-along-one-null-direction}(i), here for unequal shifts $m$, $l$) reads, exactly,
\[
[j^{xy}_{m}, j^{zu}_{l}] = \delta_{yz}\!\!\sum_{k,\,k+m,\,k+m+l}\!\! c_{x,k}^{*}c_{u,k+m+l} \;-\; \delta_{xu}\!\!\sum_{k,\,k+l,\,k+l+m}\!\! c_{z,k}^{*}c_{y,k+l+m},
\]
which on vectors edge-clean at the depth of the indices is $\delta_{yz}j^{xu}_{m+l} - \delta_{xu}j^{zy}_{m+l} + m\,\delta_{xu}\delta_{yz}\delta_{m+l,0}$ (Theorem \claimref{hawking.current-commutator-exactly-edge-split} is the case $x = y = z = u$). By definition, the rotation about a generator acts on the tower modes of channel $\pm$ with weight $\pm\tfrac12$ and the unit $J$: $U(\phi) = \prod_{a,k}(1 + (z_{a} - 1)n_{a,k})$, $z_{\pm} = e^{\pm J\phi/2}$, the mode rotation of \claimref{synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes}(i) with these weights, unitary for the CAR adjoint; the weights are matched to those of \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(iv), which are stated with Hestenes' unit, not derived from them. The densities $j^{g\pm,g\pm}_{m}$ are invariant (helicity $0$) and the flip currents $j^{g+,h-}_{m}$, $j^{g-,h+}_{m}$ are multiplied by $e^{J\phi}$, $e^{-J\phi}$ (helicity $\pm 1$), the transformation of $\alpha_{\pm,k}$ in (iii).
\item[(v)] \emph{(The photon's relations are collective; proved, with the limit argued.)} For a matrix $M$ over the generators with entries in $\mathrm{span}\{1, J\}$ let $\varepsilon_{m} = \sum_{g,h}M_{gh}j^{g+,h-}_{m}$, of helicity $+1$, and let $\Omega$ be the bottom-filled window in every channel of every generator, the band restriction of the null vacuum (\claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii), \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(vi)). Then $[\varepsilon_{m}, \varepsilon_{l}] = 0$, $\varepsilon_{m}\Omega = 0$ for $m \ge 1$, the value of $[\varepsilon_{m}, \varepsilon_{m}^{*}]$ on $\Omega$ is $m\operatorname{tr}MM^{*}$ exactly (no fluctuation), and for $m < l$ the defect $D = [\varepsilon_{m}, \varepsilon_{l}^{*}]$ has
\[
\|D\Omega\|^{2} = 2(l - m)\,\|MM^{*}\|_{F}^{2} \;\ge\; \frac{2(l - m)\,(\operatorname{tr}MM^{*})^{2}}{N}
\]
on $N$ generators, with equality exactly when $MM^{*}$ is scalar. Normalised to the photon's central term ($\operatorname{tr}MM^{*} = 1$), the defect is at least $2(l - m)/N$: on one generator ($N = 1$) it is $2(l - m)$, so the flip currents of a single generator never carry the photon's relations, and no smearing over finitely many generators removes it (the finite number of quanta such a mode holds is the quasi-spin capacity of \claimref{synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins}(iv), of which this is the mean-square side). For a transversally smeared field, $M = \mathrm{diag}(s^{1/2}f(y_{g}))$ with $s\sum_{g}|f(y_{g})|^{2} = 1$, the defect is $2(l - m)\,s\cdot s\sum_{g}|f(y_{g})|^{4}$, which tends to $0$ as $s \to 0$ on the continuum of generators of the null plane (argued, by Riemann sums). So the helicity-covariant relations of (ii) and (iii), $[\alpha_{\pm,k}, \alpha_{\pm,l}^{*}] = k\delta_{kl}$, are carried by transversally smeared flip currents in mean square on the null vacuum in that limit, while the densities carry exact canonical pairs of helicity $0$ on every generator. For the window level operator $H = \sum_{x,k}k\,n_{x,k}$, $[H, j^{xy}_{m}] = -mj^{xy}_{m}$: the flip currents have the linear dispersion of (ii) for the second quantisation of the compression of the null translation generator to the band modes, up to the shift $\tfrac12$ and the band scale (\claimref{synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves}(ii), (iii)), not for the generator itself.
\end{enumerate}
\emph{Reading.} Free Maxwell theory in the spacetime algebra gives, on a null plane, the kinematics of photon quantisation (classical, transverse, as in light-front quantisation): two transverse chiral fields per generator with positive null energy and no indefinite form, the sign of their relations fixed by positive null energy whatever the orientation of the unit, and on the data the unit $I_{4}$ is right multiplication by $-J_{\perp}$. The ladder's fermions add exact canonical pairs of helicity $0$ (density waves, not photons) and the photon's helicity $\pm 1$ relations only collectively, as transversally smeared spin-flip pairs, in mean square on the null vacuum in the continuum of generators, with an exact defect of order $1/N$ and a normalisation that vanishes with the cell size, so that the composite is free. It does not give the transverse dynamics, the coupling to charges, convergence of states, null rotations, or other gauge bosons. So the photon stays elementary (\claimref{field-theory.fock-space-maxwell-modes}) and the Krein form a premise (\claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}): the exact composite bosons of the null vacuum have helicity $0$ and live on one generator each.

## technical
Free Maxwell theory in the spacetime algebra gives the photon's kinematics on a null plane with no indefinite metric. The symplectic current $\omega = F_{1}\cdot A_{2} - F_{2}\cdot A_{1}$ is conserved on free fields, and in the gauge $n\cdot A = 0$ its flux through the plane is $\partial_{n}A_{1\perp}\cdot A_{2\perp} - \partial_{n}A_{2\perp}\cdot A_{1\perp}$: only the two transverse components, with no transverse derivative. The gauge-invariant null data $E_{\perp}$ (the transverse part of $n\cdot F$) carry the positive null energy $-Q(E_{\perp})$, and under Dirac's quantisation rule with a central unit each generator carries two commuting chiral current algebras $[\alpha_{ik}, \alpha_{jl}^{*}] = k\delta_{ij}\delta_{kl}$, whose sign does not depend on the orientation of the unit. On the null data $I_{4}$ is right multiplication by $-J_{\perp}$ ($J_{\perp} = \gamma_{1}\gamma_{2}$), so data of positive frequency relative to $I_{4}$ rotate about the generator in the sense in which they translate, one helicity, as in the stored photon modes; the two helicities are the two relative orientations of the rotation and translation phases.

The ladder adds the following. The fermions of the generators supply two chirality channels per generator, whose pair currents obey the level-one current algebra exactly on edge-clean window vectors. With the tower's kernel unit $J$ and channel weights $\pm\tfrac12$, densities have helicity $0$ and spin-flip currents helicity $\pm 1$. For a flip current $\varepsilon_{m} = \sum M_{gh}j^{g+,h-}_{m}$ over $N$ generators, the value of $[\varepsilon_{m}, \varepsilon_{m}^{*}]$ on the null vacuum is $m\operatorname{tr}MM^{*}$ and the defect $[\varepsilon_{m}, \varepsilon_{l}^{*}]$, $m < l$, has norm squared $2(l - m)\|MM^{*}\|_{F}^{2} \ge 2(l - m)(\operatorname{tr}MM^{*})^{2}/N$, with equality for uniform smearing. One generator never carries the photon's relations; transversally smeared flip currents do, in mean square on the null vacuum, in the limit of the continuum of generators. Not given: the transverse dynamics, the coupling to charges, or other gauge bosons.

## lay
On a light front the electromagnetic field has a simple set of free data: two numbers per light ray, its two transverse components, with positive energy and no unphysical modes; this much is ordinary electromagnetism written in geometric algebra. The horizon's fermions, two kinds per light ray, can be paired up into wave-like modes. Pairs that keep the fermion's kind give exact boson waves, but they do not turn under rotations about the light ray as light does, so they are not photons. Pairs that flip the kind turn like light's two helicities, but on a single light ray they are not exact bosons; averaged over many neighbouring light rays the error shrinks like one over their number, so they reproduce the photon's commutation relations on the vacuum, on average, in the limit of infinitely many light rays. The dynamics across rays, the coupling to charges and the other force carriers are not given.

## one-liner
On a null plane the free photon's data are two transverse chiral fields per generator (free Maxwell theory in the spacetime algebra, no indefinite form); the generators' pair currents give exact canonical pairs only at helicity $0$ (density waves, not photons), and the helicity $\pm 1$ relations only collectively, with defect $2(l - m)\|MM^{*}\|_{F}^{2} \ge 2(l - m)/N$ over $N$ generators (normalised), vanishing in mean square on the null vacuum for smeared fields on the continuum of generators; not the transverse dynamics, the coupling to charges, or other gauge bosons.
