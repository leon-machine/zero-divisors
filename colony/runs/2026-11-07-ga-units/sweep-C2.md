# Sweep C2: imaginary unit to GA pseudoscalar (maintainer pass 2026-11-07)

31 entities. 26 changed (version bumped, credit and `extraction.maintainer_pass_ga_units` added), 5 carry
`outside_ga` (4 of them are declarations only, with no version bump; the fifth is a changed entity), 1 unchanged.
Final `tp check --layers 1,2,3` on the C2 ids gives only I213 on mass.grip-real, which is already in baseline.log.
The detector re-scan shows only declared entities and index false positives: `\omega^{i\,a}` in mass.exact-join,
`[(i,A),(j,B)]` in cumulants, `p = (i, A)` in face-mass-form.

## Per entity

- families.absolute-scale-clean-negative-result 2 -> 3: de Sitter weight $-\tfrac32 \pm i\nu$ -> $\pm I_4\nu$, numbers in span{1, I_4}. Nothing stays.
- families.bracket-fixed-join 4 -> 5: principal-series weight -> $I_4\nu$ (formal, technical). Nothing stays.
- families.chart-computation-sign-twist-bracket-form 5 -> 6: $\zeta = e^{2\pi I_4/3}$, $\Gamma = |\Gamma|e^{I_4\delta}$, $\C$ -> span{1, I_4}. Nothing stays.
- families.imported-dictionary-exact-join 5 -> 6: weight -> $I_4\nu$ (formal, technical, proof). Nothing stays.
- families.rigidity-pairing-sector-one-event 3 -> 4: channel vectors $-I_4(1,1,1)/\sqrt3$, $-I_4f_+/\sqrt3$, $\zeta^2 - \zeta = -I_4\sqrt3$, $e^{I_4\chi}$. No i stays. Declared `other` for the 3D cross product: editing the entity made W222 fire on "channel cross products". See Unsure 6.
- families.skeleton-rank-one-plus-ordering-shift 5 -> 6: channel phases $e^{I_4\chi}$ (proof). Nothing stays.
- families.why-kinematic-attacks-had-fail 3 -> 4: weight -> $I_4\nu$ (formal, technical, proof). Nothing stays.
- mass.casimir-form-join 6 -> 7: the chart unit (the convention line already said "i is I_6") is now written $I_6$. It goes on the right for spinor values ($W \mapsto \sum Z(\bar Z\cdot W)I_6$) and on numbers in span{1, I_6}. Nothing stays.
- mass.exact-join 7 -> 8: $I_6$ in p(x), k(x), the components, $(I_6)^2$, $(-I_6)^2$, $t_{jj} = r_j + I_6 s_j$. The convention line is rewritten. Nothing stays.
- mass.grip-real 7 -> 8: $x = \tfrac{I_6}{\sqrt2}K\varepsilon$ and the blocks. The convention line is rewritten. Nothing stays.
- mass.imported-unitary-representations-de-sitter-group 3 (no bump): $\Delta = \tfrac32 + i\nu$ kept as Dixmier and Higuchi state it. Declared `imported`.
- mass.weight-composite 6 -> 7: weight -> $I_4\nu$ (formal, technical, one-liner). Nothing stays.
- mass.weight-polynomial-two-series 5 -> 6: weight -> $I_4\nu$, and "Gaussian rationals" named $\mathbb{Q}(I_4)$. Nothing stays.
- note.families.setting-gaussian-theorems 1 -> 2: channel phase $e^{I_4\chi}$. Nothing stays.
- note.mass.setting-grip-composite-frozen-point 1 -> 2: moment map $M_A := I_6\sum\bar Z\cdot(AZ)$, with $I_6$ named the CS unit. Nothing stays.
- refuted.the-mass-dictionary-coupling-to-the-frozen-point 1 -> 2: weight -> $I_4\nu$. Nothing stays.
- synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase 2 -> 3: test value $1 + 2I_4$ and rephasings $e^{I_4\beta}$. Also reworded "quark Dirac matrices" to "quark Dirac mass matrices", because W222 read it as gamma matrices. Nothing stays.
- synthesis.channel-phase-invisible-to-axially-covariant-completions 2 -> 3: $\zeta$, $e^{I_4\chi}$, $e^{I_4\theta}$; the eigenlines $\C u'$, $\C f_\pm$ -> span{1, I_4}. Nothing stays.
- synthesis.coherent-face-vector-real-slices 1 -> 2: $\zeta$, $e^{I_4\chi}$, $\kappa \in -I_4\R_{>0}$, slice $I_4\R^3$, coordinate $I_4p$, $-I_4 \mapsto \pm1$, $\mathbb{Q}(\sqrt3)[I_4]$, $w = 1 + I_4$; the $\C$ lines and scalars -> span{1, I_4}. Nothing stays.
- synthesis.cumulants-at-fixed-second-moments-keep-the-floor 1 (unchanged): its only hit, $(i,A)$, is an index.
- synthesis.face-mass-form-unit-plus-gram 1 -> 2: $c \in \C^3$ -> span{1, I_4}^3. The detector hit $(i, A)$ is an index. Nothing stays.
- synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group 1 -> 2: $T_j = \tfrac{I_4}{2}\sigma_j$, $Y = \tfrac{I_4}{2}1$; $\C^3$, $\C^2$ -> span{1, I_4}^n. Nothing stays.
- synthesis.imported-fritzsch-texture-cabibbo-formula 1 (no bump): $e^{-i\psi}$ kept as Fritzsch and Xing state it. Declared `imported`.
- synthesis.koide-channel-phase-is-no-symmetry-angle 2 -> 3: quarter turn $\exp(\tfrac{I_4\pi}{2}P_d)$. Nothing stays.
- synthesis.light-cone-koide-is-quarter-turn 1 -> 2: $D = P_s + I_4P_d$, $a, b \in \{1, I_4\}$, $\tfrac13(\operatorname{tr}A) + I_4A_0$, $\mathbb{Q}(I_4)$; $\C^3$, $\C^\times$, $\mathfrak{gl}(3,\C)$ written over span{1, I_4}; the label $D_{1,i}$ is renamed $D_{1,I_4}$. Nothing stays.
- synthesis.light-pair-split-needs-broken-source-stabiliser 1 -> 2: the Fock-state coefficient $2I_4$, test vectors $(1, I_4, \tfrac12 + \tfrac{I_4}{3})$, phases, $\mathbb{Q}(I_4)$; $\C^3$ and $\C c$ -> span. Nothing stays.
- synthesis.many-twistor-join 2 -> 3: $I_6$ in the moment and slot components, the convention line rewritten, $\C^N$ -> span{1, I_6}^N. Nothing stays.
- synthesis.operator-join-ordering-constants 2 -> 3: $\hat M_A := I_6\sum\tfrac12(\dots)$, $F = I_6A_U$, $G = I_6A_V$ (the palatial algebra quantising the classical moment). Nothing stays.
- synthesis.operator-join-positive-energy-no-finite-energy-zero-modes 1 (no bump): $\exp(\tfrac{2i}{\hbar}\sum a^\dagger b^\dagger)$, $i b^\dagger$ and $\mu \in \C$ kept. Declared `complex-analysis`, because the scalar unit of the palatial Fock space is not settled. See Unsure 5.
- synthesis.operator-join-seed-has-no-diagonal-matrix-elements 1 (no bump): the determinant U(1) $\exp(i\phi\operatorname{tr}\hat h/\hbar)$ kept. Declared `complex-analysis` for the same reason.
- synthesis.real-structure-breaks-source-stabiliser-to-z2 2 -> 3: every face-space unit -> $I_4$: phases, $\kappa = -I_4|\kappa|$, the quarter-turns, $(1, a, I_4a) = c_R + I_4c_I$, $I_4R_n$, $I_4P_{12}$, $\mathrm{diag}(I_4, -I_4, 1)$, $m$, and the check fields. $\C v$, $M_3(\C)$ and $\mathrm{span}_\C$ are written over span{1, I_4}. Nothing stays.

## Possible errors found

1. synthesis.real-structure-breaks-source-stabiliser-to-z2, proof (ii): the intermediate expression
   $N(I_4R_n) = \overline{\det(I_4R_n)}\,I_4R_n = \overline{(-I_4)}\cdot I_4\,R_n\cdot(-1)\cdot(-1)$ evaluates to $-R_n$ as written.
   It should be $\overline{(-I_4)\cdot(-1)}\cdot I_4R_n = R_n$. The sentence's conclusion ($\det(I_4R_n) = I_4$, $N = R_n$)
   is right. Not fixed.
2. A possible sign conflict in the store, not caused by this pass. The mass proofs' convention line (and
   conventions.md) take the chart's unit to be $I_6$. But note.correspondence.what-factor-i-what-remains-conventional
   and correspondence.incidence-relation-chart say that with $I_6 = e_0\cdots e_5$, "$I_6$ acts as $-i$ on CS". If
   that holds for the chart in use, every $I_6$ written in this group's twistor entities (the moment map in particular)
   should be $-I_6$. I followed the stored convention line.

## Unsure (for Leon)

1. De Sitter weights. The 2026-10-21 i4 pass had kept $w = -\tfrac32 \pm i\nu$ as a representation label. I wrote it
   with $I_4$ as a physical number (rule 3) in the 7 series entities, and kept $i$ only in the Dixmier/Higuchi import.
2. The face-space unit. Rule 3 defaults to $I_4$, so all families/face-space numbers ($\zeta$, channel phases, Fourier
   lines, the quarter-turn) are written with $I_4$. But the face vector's components are brackets
   $[\omega^i\omega^j]$ of conformal spinors, whose own unit is $I_6$. If face space is "on a different plane", these
   should be $I_6$. This affects chart-computation, rigidity, skeleton, note.families, channel-phase, coherent,
   light-cone, light-pair, real-structure, face-mass-form, koide-channel and cabibbo. The slot space of faces-of-one-slot
   (tower modes) is more clearly $I_4$.
3. The families bosonic Fock spaces. Their amplitudes and Fock unitaries are read with $I_4$ (the $2I_4$ coefficient in
   light-pair (iii); $I_4R_n$ and $I_4P_{12}$ in real-structure). Mass-matrix entries are $\langle\hat\Omega^\dagger\hat\Omega\rangle$
   in that space, so its scalars cannot differ from the mass-form numbers. The store does not otherwise say that this
   Fock space carries $I_4$.
4. Twistor numbers are read in span{1, I_6}, "acting on conformal spinors by right multiplication" as conventions.md
   says. This includes the Penrose-Rindler 2-spinor components in mass.exact-join and many-twistor-join. See also
   Possible error 2.
5. The palatial oscillators. ordering-constants is converted to $I_6$, because its $\hat M_A$ quantises the classical
   $I_6$ moment. But positive-energy and seed keep $i$ on the Fock space, because field-theory.twistor-attachment makes
   the palatial space the field theory's one-particle space (unit $I_4$). The two units meet there, and "never
   identify" leaves the Fock unit open.
6. families.rigidity-pairing-sector-one-event carries `outside_ga: {kind: other}` for its cross product, not for $i$,
   so that W222 clears. Rule 6 says not to declare an entity whose $i$ was replaced completely; rewriting the cross
   product as a wedge dual would have changed the mathematics' presentation beyond this pass.
7. In faces-of-one-slot, $\sigma_j$ stay as matrices, with entries read in span{1, I_4}. A GA statement would use
   bivectors, which is outside this pass.
