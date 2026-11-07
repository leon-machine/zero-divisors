# Sweep B: the imaginary unit and the GA pseudoscalar (maintainer pass 2026-11-07)

Totals (41 entities): 24 changed (text, version + 1, credit entry, `maintainer_pass_ga_units` note), 7 of them
also declared; 13 declared only (outside_ga plus the extraction note, levels untouched, no version bump);
4 unchanged (detector hits are index letters only).
Leon's rulings (RULINGS.md, recorded while this sweep ran) are applied to this group: R1 reverted three
boundary-mode/window conversions to their 8eef5a4 text (c-loc, local-boost, r-loc, now declaration only);
R3 put the slot-module reading on BRST and triangle; R4 made e+e- one-unit.
Validation (`tp check --layers 1,2,3 --keep-going --author leon`): no errors or warnings on any B entity
(only the store-wide informational I213). Detector re-scan: every B entity still listed carries outside_ga,
except sheaf.degeneration-sheaf, synthesis.diagonal-kasner-momentum-constraint,
synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points and
synthesis.unit-boost-residue-needs-nonpositive-exponent (index letters only).

## Per entity

- correspondence.imported-tractor-connection-local-twistor-transport: 6 -> 7. Replaced: the factors i of local twistor transport (formal, technical, proof) by the conformal spinors' unit, right multiplication by $I_6$ ($\varepsilon_A{}^B\pi_{A'}I_6$, $\mathrm{P}_{AA'BB'}\omega^B I_6$), which the entity already said they stand for. The source's form with i stays under extraction.source_formal. Nothing remains; not declared.
- interior.complex-scale-inverse-cube-killing-spinor: 5 (unchanged). Stays: the identification of $\R \oplus \R I$ with $\C$ matching $I$ with the i of the imported Walker-Penrose scalar $r - ia\cos\theta$. That comparison is the result. Declared bridge.
- note.mass.abstract: 2 -> 3. Replaced: complex weight $-\tfrac32 \pm I_4\nu$, read in span{1, I_4}. Nothing remains.
- note.mass.setting-introduction: 2 -> 3. Same replacement. Nothing remains.
- note.mass.setting-machine-verification: 2 -> 3. Replaced: $w = -\tfrac32 \pm I_4\nu$ (Gaussian rationals stand for Q(I_4)). Stays: Part C's chart on $\Lambda^2\C^4$ (the complexified conformal vector space). Declared complex-analysis.
- pairing.curvature-which-loops-move-vacuum: 4 (unchanged). Stays: classes $\pm iM/r^3$, values of the pairing with the complex null vector $m = (e_2 + ie_3)/\sqrt2$. Declared complex-analysis.
- sheaf.degeneration-sheaf: 6, unchanged. The hit is the inclusion map $i : \Sig \hookrightarrow M$.
- synthesis.c-loc-modular-clause-moves-no-nested-patch: 1 (unchanged). Converted, then reverted by R1. Stays: the boundary-mode phase flow $e^{-i\omega_j t}$, the GNS unitaries, $\Delta^{is}$, and the check's $(3 + 4i)/5$ with $\mathbb{Z}[i]$. Declared complex-analysis.
- synthesis.chiral-abelian-loops-with-i4-as-the-bmhv-gamma5-need-finite-symmetry-restoring-counterterms: 2 -> 3. Replaced: $\gamma_5 = iI_4$ is now the chirality $x \mapsto I_4xI_4$ (left $I_4$ the BMHV element, the right one the unit); the units become the right unit $I_4$, with $(eYI_4)^2I_4^2$ and $(eYI_4)^4I_4^4$ prefactors, and the master-integral values are $\mp I_4/(4\pi)^{D/2}$; "Dirac matrices are the vectors" was reworded (W222). Nothing remains.
- synthesis.clausius-is-window-first-law-plus-boost-charge-conservation: 2 -> 3. Replaced (R2: continuum mode space, unit $I_4$): $T_{vv} = \tfrac{I_4}{2}(\dots)$, $I_4(v\partial_v + \tfrac12)$, $h = \kappa I_4(u\partial_u + \tfrac12)$, Mellin modes $u^{-1/2 + I_4w}$, polarised identity. Nothing remains.
- synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form: 1 (unchanged). Stays: $J = ie_1e_+$, $c = \tfrac12(e_1 + ie_+)$ and $H = S + iA$. These live on the module of the complexified $\Cl(2,4)$, where i must commute with the generators. Declared complex-analysis.
- synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite: 2 -> 3. Replaced: kernel phases $e^{\mp I_4p\cdot(x-y)}$, $\phi(\tau) = \int e^{-I_4\nu\tau}d\mu$ and $I_4\phi'$. The proof's own unit phases were already $c + sI_4$. Nothing remains.
- synthesis.diagonal-kasner-momentum-constraint: 3, unchanged (index $R_{0i}$).
- synthesis.electron-positron-to-muon-pairs-in-the-spacetime-algebra-lsz-tree-cross-section-and-one-loop-unitarity: 2 -> 3. Replaced: the photon factor $-I_4/(q^2(1 - \hat\Pi))$; by R4 also $s - I_40$, $\ln\frac{m^2}{A - I_40} = \ln\frac{m^2}{|A|} + I_4\pi$ and $\mathrm{Im}\,\hat\Pi(s + I_40)$ (Im is the $I_4$ coefficient). "Dirac matrices" was reworded (W222). Nothing remains; the earlier declaration was removed.
- synthesis.imported-bochner-theorem-moment-lemma-and-whitney-even-functions: 1 (unchanged). Stays: Bochner's $\int e^{-i\nu\tau}d\mu$ for $f : \R \to \mathbb{C}$. Declared imported.
- synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field: 2 (unchanged). Stays: the source's normalisation $u = -iSp'\gamma u_0$. Declared imported.
- synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem: 1 (unchanged). Stays: $D_+ = -1/(4\pi^2(Q(\xi) - i0\,\xi_0))$. Declared imported.
- synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport: 2 -> 3. Replaced: $(iD - m)(iD + m)$ is now $(R_{I_4}D - m)(R_{I_4}D + m)$, with $R_{I_4}$ the right unit. Stays: the i0 prescription of the Hadamard form (Kay-Wald, Sahlmann-Verch). Declared imported.
- synthesis.imported-one-loop-integrals-and-pauli-villars-regulators: 1 (unchanged). Stays: $\ell_0 = i\ell_{E,0}$, the integral values, and $-i/(k^2 + i0)$, as the sources state them. Declared imported.
- synthesis.interacting-fields-of-causal-perturbation-theory-keep-the-spin-statistics-connection-at-even-ghost-number: 2 -> 3. Replaced: Bogoliubov's $\delta/(I_4\,\delta h)$ and $I_4^n/n!$ (Fock-space unit $I_4$). Nothing remains.
- synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points: 1, unchanged (index $C_{0i}{}^{0i}$).
- synthesis.lens-space-wall-rung-count-sees-the-integral-twist: 2 -> 3. Replaced: the quaternion $i$ becomes $B = e_2e_3$, with $(z_1, z_2) \mapsto (Bz_1, Bz_2)$ on $R = z_1 + z_2e_1e_2$, $z_j \in$ span{1, B}; the section $f$ is valued in span{1, B} with phase $e^{B\varphi}$. Stays: the unused classical remark on $\shL \otimes \mathbb{C}$ and its Chern class. Declared other.
- synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum: 3 -> 4. Replaced: "$i = I_4$" now names $I_4$ directly; $Y = \tfrac12 I_4\mathbf{1}$. Nothing remains (the stored name $\mathcal{R}_{\C}$ is kept).
- synthesis.local-boost-temperature-is-local-regularity: 3 (unchanged). Converted, then reverted by R1. Stays: boundary-mode/window flows, $\varrho^{is}$, the KMS strip $\lambda + 2\pi i$, and the Wick continuation $\lambda = -i\theta$ of the line element. Declared complex-analysis.
- synthesis.locality-of-the-attached-free-fields-fixes-their-statistics: 2 -> 3. Replaced: plane-wave phases, $P(\pm I_4\partial)$, $R(I_4\partial)$, $-I_4^d/(4\pi^2)$, "powers of $I_4$". Stays: the imported boundary value $Q(\xi) - i0\,\xi_0$. Declared complex-analysis.
- synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard: 2 -> 3. Replaced: $Iu' = Hu$ with the Pauli pseudoscalar $I$ ($I_4$ read in the even subalgebra; the proof already identified it); Bunch-Davies $u = e^{-I_4z}(1 - I_4/z)$, $\chi_z = -I_4$. Nothing remains.
- synthesis.modular-period-on-values-is-the-dual-plane-turn: 2 -> 3. Replaced: "$i = I_4$" names $I_4$; the rotor is $\cos\tfrac\theta2 + I_4e_1e_0\sin\tfrac\theta2 = \cos\tfrac\theta2 - e_2e_3\sin\tfrac\theta2$ (checked by hand); the chiral relation is now "$\pm$ the unit". Stays (R1): $a \mapsto e^{-iw\lambda}a$ on the completed pair of $\Cl(1,1)$. Declared complex-analysis.
- synthesis.one-doublet-field-is-pure-gauge-on-the-null-lift-locus-so-two-doublets-need-the-exact-constraint: 2 -> 3. Replaced: $\mathrm{i}$ by $I_4$ in $T_j$, $Y$, and the check's basis maps; the statement says its $\C$ is span{1, I_4}. Nothing remains.
- synthesis.one-loop-qed-in-the-spacetime-algebra: 2 -> 3. Replaced: units as the right unit $I_4$ (numbers, Wick values included, in span{1, I_4}): $I_4\Pi^{\mu\nu} = -(-eI_4)^2\int\mathrm{Tr}[\gamma^\mu(k+m)\gamma^\nu(k'+m)I_4I_4]$, $\delta\Gamma^\mu = -e^2\int\cdots\gamma_\nu I_4$, integral values $\mp I_4/\ldots$, $d^4\ell = I_4\pi^2u\,du$; chirality $x \mapsto I_4xI_4$; chiral traces $2(\langle X\rangle_0 \mp x_4I_4)$. Stays: the Dirac-matrix reading (matrices over $\mathbb{Q}(i)$, $i\gamma_0\gamma_1\gamma_2\gamma_3$, $-i\sigma^{\mu\nu}q_\nu$). Declared bridge.
- synthesis.positive-energy-selects-rule-2-sign: 3 (unchanged). Stays: $-i\,d\pi(X)$ of a unitary representation on an abstract Hilbert space, and $\so(6,\C)$. Declared complex-analysis.
- synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale: 1 (unchanged). Stays: $J = ie_1e_+$ and the tube point $i\rho e_0$, both next to vectors. Declared complex-analysis.
- synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta: 2 -> 3. Replaced: the hypercharge $\tfrac{i}{2}$ on the rung doublet is now $\tfrac12 I_4$. Nothing remains.
- synthesis.r-loc-needs-sheet-labelled-modes: 3 (unchanged). Converted, then reverted by R1. Stays: window flows $\mathrm{Ad}(e^{isH})$, $i[h, \cdot]$, su(n) as $i$ times self-adjoint, $\Mat_n(\C)$, $\mathfrak{sl}(2,\C)$, and the $\Cl(1,1)$ completed pair. Declared complex-analysis.
- synthesis.rule-2-fusing-plane-lorentzian: 2 (unchanged). The hit is the index in "$i \notin S$". Stays: $\C$ as the isomorphism type of the centre and $\Mat(4,\C)$. Declared other.
- synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet: 1 -> 2. Replaced: $t_2' = I_4t_2$. Nothing remains.
- synthesis.rung-field-quartics-run-to-strong-coupling-within-a-few-tev-on-the-transmutation-branch: 2 -> 3. Replaced: $\tfrac{I_4}{2}\sigma_j$, $\pm\tfrac{I_4}{2}$, $\tfrac{I_4}{2}\sigma_2$, $\lambda_5 = 4(k_8 - I_4k_9)$; "$i = I_4$" names $I_4$. Nothing remains.
- synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts: 2 -> 3. R3: the matter representation $\C^2 \otimes \C^3$ is read over span{1, I_4} on the tower's floors, stated once at the formal level. The hit is the index "$\mu = i$". Nothing remains; first declared other, then the declaration was removed.
- synthesis.spin-product-state-of-the-massless-dirac-field-is-odd-under-chirality-and-never-hadamard: 2 -> 3. Replaced: the unit is named as the right unit; $Iu' = Hu$ with $I = s_1s_2s_3$; the Hermitian product is over span{1, I} (was $\mathbb{C}^2$); $\hat F = \int Fe^{I_4\lambda t}dt$. Nothing remains.
- synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation: 2 -> 3. Replaced: chirality $x \mapsto I_4xI_4$; $\mathrm{Tr}(\gamma_5X) = 4\langle I_4X\rangle_0 I_4$; numerators $M\cdot4\langle\cdots\rangle_0 I_4$; integral $-I_4/(32\pi^2\Delta)$; regulator display $8\langle\cdots\rangle_0 I_4\cdot\frac{-I_4}{32\pi^2M_i^2}$. R3 sentence added for the complexified gauge algebra of (vi). Stays: the check against Dirac matrices over $\mathbb{Q}(i)$. Declared bridge.
- synthesis.two-loop-qed-in-the-spacetime-algebra-continued-in-dimension-gives-the-second-beta-coefficient: 2 -> 3. Replaced: propagator $-k/Q(k)$ and vertex $-e\gamma_\alpha$, each with one unit (right unit $I_4$); factors $(-1)(-eI_4)^2(-I_4)^2 = -e^2$ and $(-1)(-eI_4)^4(-I_4)^4 = -e^4$. Nothing remains.
- synthesis.unit-boost-residue-needs-nonpositive-exponent: 3, unchanged (index "$0i$").

## Possible errors found

None in the mathematics of these entities. One point to watch elsewhere: with the trace $4\langle\cdot\rangle_0$, a single right unit inside a trace is not the unit times the trace ($4\langle XI_4\rangle_0 \ne I_4\cdot 4\langle X\rangle_0$). The rewrites here keep each such unit either paired inside the product ($I_4I_4 = -1$) or outside the trace as a number.

## Unsure (for Leon to rule)

1. Loop entities (one-loop, chiral, triangle, two-loop, e+e-). The values of the Wick-rotated integrals and the e+e- branch cut are read in span{1, I_4} and multiplied with the Feynman-rule units, which identifies the contour's i with the field unit as numbers. R4 supports this. The imported Fact keeps i.
2. The mass notes' weight $-\tfrac32 \pm I_4\nu$ was written with $I_4$. If the weight belongs to the conformal spinors, the unit would be $I_6$ (sweep-C1 raises the same point).
3. $\C$ kept as notation, read as span{1, I_4}: $\mathcal{R}_{\C}$ (linear-rung, one-doublet: "the $\C$ of this statement"), $\C^2 \otimes \C^3$ (BRST) and $\mathfrak{sl}(3) \oplus \mathfrak{sl}(2) \oplus \C$ (triangle). W222 sees only `\mathbb{C}`, so these pass without a declaration.
4. local-boost-temperature: $\lambda = -i\theta$ continues a coordinate of the induced metric. Rule 5's "write the rotation in the dual plane" would change the statement, so it was kept.
5. lens-space: the fibre $\R^2$ of $\shL \oplus \shL$ is coded as span{1, B} with $B = e_2e_3$. This is exact but the choice is arbitrary; any unit bivector would do.
6. tractor connection: the index-form components ($\mathrm{P}_{AA'BB'}$) with $I_6$ on the right rely on the entity's own statement that the factor is $I_6$.
7. imported Hadamard parametrix: the notation $R_{I_4}$ for the right unit is introduced by analogy with the conventions' $R_{I_6}$.
8. locality: the kept $Q(\xi) - i0\,\xi_0$ is the scalar form of the R2 exception (an i0 shift of a spacetime vector). It is quoted from the imported Fact.
9. The orchestrator's checkpoint commits (f4d7ccd, 89f6437) captured the c-loc and local-boost conversions before the R1 revert. The working tree now has the reverted text.
