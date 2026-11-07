# Sweep D2: imaginary unit written as the GA pseudoscalar (2026-11-07)

51 entities: 2 changed by replacement (no declaration needed), 34 declared (no replacement possible; version bumped, credit and `extraction.maintainer_pass_ga_units` added, `outside_ga` added), 15 unchanged (detector false positives only).
Validation: `tp check --layers 1,2,3` shows no error or warning on any D2 entity (only the pre-existing I213 subject notes, also in baseline.log). Re-scan: every entity still listed by the detector carries `outside_ga` or has only index or name false positives (see Unsure for the quaternion names).

## Replaced

- synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst, 1 -> 2: proof phases $e^{i\mu y}$ and $e^{2\pi i k y/L_f}$ become $e^{I_4\mu y}$ (with "the field theory's unit $I_4$, acting on the right") and $e^{2\pi I_4 k y/L_f}$; nothing stays.
- note.programme.setting-seventeen-refutations, 2 -> 3: the weight $-\tfrac32 \pm i\nu$ becomes $-\tfrac32 \pm I_4\nu$ with "(numbers are read in $\mathrm{span}\{1, I_4\}$)"; nothing stays.

## Declared (i stays)

- correspondence.chirality-split-ordering-insensitivity-asd-sector, 4 -> 5: stays $\pm i$ eigenspaces in $\mathfrak{so}(1,3)_\C$ (complexification that has to commute with the duality operator, which is itself $I_4$ on bivectors); other.
- correspondence.fock-model-complexified-ascended-algebra, 7 -> 8: stays $w_3 = b_3 + i b_4$, Fock model over $V_\C$ (the "i.e." hit is a false positive); other.
- correspondence.incidence-relation-chart, 4 -> 5: stays Penrose's $\omega = ix\pi$ and "$I_6$ acts as $-i$ on $\CS$", source notation beside the real form; bridge.
- correspondence.local-twistor-transport-ascended-spinor-connection, 7 -> 8: stays Penrose composite $i\varepsilon(i\mathrm{P}\omega)$ quoted from the imported Fact in two-spinor notation; imported.
- correspondence.lorentzian-duality-complex-structure, 3 -> 4: stays $\pm i$ eigenvalues of the Hodge star on $\Lambda^2_\C$ (complexification); other.
- correspondence.reality-conjugation-twistor-form-factor, 6 -> 7: stays Fock-module scalars over $V_\C$ ($b_4 = -\tfrac i2(\dots)$, $e^{i\theta}$ phases of $\Sigma$, $(3+4i)/5$, $m(i\hat x)$); other.
- dark-matter.premise-flag-as-datum, 1 -> 2: stays the $+i$ eigenspace of $J$ on the complexified $\R^{2,4}$, compared with the Fock module's $i$; other.
- note.correspondence.setting-machine-verification, 2 -> 3: stays $\mathbb{Q}(i)$ as the scalars of the complexified Fock model, plus the script's samples ($i\hat x$, $(3+4i)/5$, $\pm i$); other.
- note.dark-tower-matter.neutral-row, 1 -> 2: stays $(k\,i, -i\,1_k)$ in $\uu(1)\oplus\uu(k)$ on $\C^1\oplus\C^k$; other (see Unsure).
- note.odd-extensions.added-axis-pseudoscalar, 1 -> 2: stays $i\gamma_5$ in the physicists' notation; bridge.
- note.odd-extensions.one-operator-sees-difference, 1 -> 2: stays $\gamma_5$ against $i\gamma_5$ (gamma-matrix notation); bridge.
- note.pairing.setting-machine-verification, 1 -> 2: stays class value $2i$ of the complex functional on $\so(4,\C)$; other.
- note.transport.exotic-embedding-inertness, 1 -> 2: stays the embedding $\HH \hookrightarrow \Mat_2(\C)$ written with complex matrices; bridge.
- pairing.stabiliser-parabolic-algebra-null-direction, 4 -> 5: stays $\pv$ values $\pm i$, $2i$ and the complex tetrad $m = e_2 + ie_3$; other.
- rule2.odd-lorentzian-dimension-exactly-one-real, 5 -> 6: stays $i\omega$, $e_i \mapsto ie_i$ in $\Cl(p,q)\otimes\C$; other.
- rungs.rung-spinor-module-mixings, 4 -> 5: stays $(iI_3, -iI_3)$ and $i(j-k)$ on the complexified module; other.
- scrambling.imported-modes-modular-inventory, 3 -> 4: stays $i\sigma$, which the result states lies outside the real algebra; complex-analysis.
- singularity.modular-theory-matrix-factor-proved-outright, 4 -> 5: stays $\rho^{it}$, $\Delta^{it}$ on $\C^n\otimes\C^n$ (the $|i\rangle$ hits are indices); complex-analysis.
- singularity.schmidt-forcing-proved-outright, 4 -> 5: stays $e^{itG}$ on $\C^2\otimes\C^2$, atom modes ($(i-j)$ hits are indices); complex-analysis.
- std-algebra.complex-clifford-algebra, 1 -> 2: stays every $\mathrm{i}$ of the complex quadratic space; other.
- std-algebra.complex-numbers, 1 -> 2: stays $a + b\,\mathrm{i}$ (the result identifies $\C$ with GA); bridge.
- std-algebra.complexification, 1 -> 2: stays $\epsilon_i = \mathrm{i}e_i$ and $x + \mathrm{i}y$ in $\Cl\otimes\C$; other.
- std-algebra.pauli-algebra, 1 -> 2: stays the Pauli matrix entries and $\sigma_1\sigma_2\sigma_3 = \mathrm{i}1$; bridge.
- std-algebra.square-roots-of-minus-one, 1 -> 2: stays $\pm\mathrm{i}$ in $\Mat_m(\C)$ and the quaternion $R_{\mathrm{i}}$; other.
- synthesis.attachment-conformal-energy-is-generated-by-z, 1 -> 2: stays Jordan-Wigner realisation on $\C^8$ ($e_1 = ig_3$), $h = \ip{\psi}{iZ\phi}$, $Q(\tfrac12Z) = -iE$, oscillator Fock space; complex-analysis (see Unsure).
- synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation, 2 -> 3: stays $\kappa$ on $\Cl(2,4)\otimes\C$, $w_k = e_{2k-2} - ie_{2k-1}$, $I_6\psi_W = \pm i\psi_W$; other.
- synthesis.plane-grading-records-residue-sign, 1 -> 2: stays phase flow on $T_{k,\C}$ and $x_i \mapsto iy_i$; other.
- synthesis.positive-conformal-energy-gives-positive-null-translations, 5 -> 6: stays $-i\,d\pi(Y)$ for an abstract unitary representation; complex-analysis.
- synthesis.residues-zero-four-real-chirality-anomaly, 1 -> 2: stays "the $\pm i$ eigenspaces of the complex structure $I$" (an eigenvalue of the pseudoscalar itself); other.
- synthesis.tower-charge-sector-label-temperature-not, 2 -> 3: stays $e^{i\theta}a_j$, $e^{i\theta Q_F}$ on the boundary-mode CAR algebra over $\ell^2(J)$; complex-analysis (see Unsure).
- synthesis.univalence-even-extension-split, 1 -> 2: stays $\operatorname{Ad}(e^{it\omega_kN_k})$ and its continuation $\alpha_{ip}$ on $\Mat_2(\C)$ (the detector missed these; its $r^{j-i}$ hit is an index); complex-analysis.
- synthesis.univalence-from-even-stationary-dynamics, 2 -> 3: stays $e_{2k} = i(a_k^*-a_k)$, $e^{i\theta N_k}$, $\rho^{it}$ on the boundary-mode Fock space; complex-analysis (see Unsure).
- tower.structure-tower-c-norms, 7 -> 8: stays $y_i = i\,x_i$ on $T_k^{\C}$; other.
- transport.odd-lorentzian-dimension-exactly-one-real, 4 -> 5: same as the rule2 duplicate; other.

## Unchanged (false positives only)

correspondence.twistors-are-states-three-ladder-pairs ($S\setminus i$), descent-lift.imported-stinespring-kraus-choi ($\ket{i}$), note.simulations.setting-time-integration-output ($v_{\mathrm{sig},i}$), std-algebra.contraction-expansion, std-algebra.duality, std-algebra.exterior-isomorphism, std-algebra.fock-representation, std-algebra.product-decomposition, std-algebra.pseudoscalar-commutation, std-algebra.spin-double-cover, std-algebra.z2-grading, synthesis.blade-square-signs-f2-quadratic-form, synthesis.principality-is-genericity (all index letters); std-algebra.quaternions and std-algebra.periodicity (Hamilton's $\mathbf{i}$, $\mathrm{i}$ defined as $e_3e_2$ or $e_1$, a name for a GA element, not a complex unit).

## Possible errors found

None in the mathematics. Detector limitation: it misses an $i$ followed by a letter ($\rho^{it}$, $\alpha_{ip}$, $e^{itG}$, $\omega = ix\pi$). That is how synthesis.univalence-even-extension-split's KMS continuation was missed (found by reading; now declared). rule2.odd-lorentzian-dimension-exactly-one-real and transport.odd-lorentzian-dimension-exactly-one-real have the same text.

## Unsure (left with i, for Leon to rule on)

1. synthesis.tower-charge-sector-label-temperature-not and synthesis.univalence-from-even-stationary-dynamics: SWEEP rule 4 counts the boundary-mode CAR algebras as GA-built with unit $I_4$. But conventions known limit 1 says $I_4$ anticommutes with the atom's mode operators, and the boundary modes are the atom's ladder pairs. Limit 2 adds that the algebra is defined over $\C$. So $e^{I_4\theta}a_j$ would not be the charge rotation. I kept $i$. If Leon rules the dark-tower boundary modes lie in tower planes (where $I_4$ is central), the charge rotations could become $e^{I_4\theta}$.
2. synthesis.attachment-conformal-energy-is-generated-by-z: on $\CS$ alone, the scalar $i$ in $h = \ip{\psi}{iZ\phi}$ is the conformal spinors' unit, right $I_6$ up to a sign that differs between the halves. The entity does not fix that sign relative to the Jordan-Wigner scalar, so I kept $i$.
3. note.dark-tower-matter.neutral-row: $(k\,i, -i\,1_k)$ acts on multiplicity spaces. If those are tower-mode spaces with unit $I_4$, it could read $(k I_4, -I_4 1_k)$.
4. singularity.schmidt-forcing-proved-outright: the earlier pass marked it "doubtful". I declared it on the ground of conventions limit 1 (atom modes).
5. std-algebra.quaternions, std-algebra.periodicity: Hamilton's named units are not index letters. I left them undeclared, since nothing there is a complex unit to replace. Leon may prefer a declaration.
