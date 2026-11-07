---
id: pairing.curvature-which-loops-move-vacuum
kind: claim
version: 6
title: 'Curvature: which loops move the vacuum'
status: proved
region: pairing
subject: einstein
tags: [schwarzschild, curvature-and-field-equations, pairing-and-bogoliubov, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 5
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'consistency pass, the transverse null vector written m = e2 + I5 e3, the normalisation the stated classes and the check use'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.pairing.pairing-class-transport
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - pairing.imported-schwarzschild-connection-curvature@5
  - synthesis.imported-gtg-dictionary@1
  proof: proof-main.tex
- name: standard-route
  uses:
  - pairing.imported-weyl-scalars-petrov-type-schwarzschild@2
  - pairing.loop-classes-are-weyl-components@4
  proof: proof-standard-route.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_frame_plane_classes
- kind: check
  ref: check.py::check_null_rotation_about_l_and_radial_loop
- kind: check
  ref: check.py::check_complex_loops
- kind: check
  ref: check.py::check_class_supported_on_n_wedge_mbar
locators:
  paper: T05-pairing
  number: Prop 5.5
  label: prop:curvature
  line: 343
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The GA-units pass wrote m = (e2 + I5 e3)/sqrt 2, which divides every stated class by sqrt 2; the classes M/r^3, I5 M/r^3, 2M/r^3 and 4M/r^3 and the check (pv(B) = <B.l, m>, m = e2 + i e3) use m = e2 + I5 e3 with <m, mbar> = -2, checked exactly in Cl(2,3) in the reader script v/r03_checks.py (class of (e0, e2) equals M/r^3 with the unnormalised m).'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U3) the classes +-iM/r^3 are +-I_5 M/r^3, numbers of span{1, I_5}: the complex null vector m = (e_2 + I_5 e_3)/sqrt 2 is complexified by the central pseudoscalar I_5 of Cl(2,3) (std-algebra.complexification-is-the-odd-extension), and since i -> I_5 is a field isomorphism the values are unchanged; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the values +-iM/r^3 are pairing classes <B.l, m> against the transverse complex null vector m = (e_2 + i e_3)/sqrt 2, whose i stands next to spacetime vectors (no pseudoscalar commutes with them), so it stays and is declared (version and levels unchanged).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: field strength of the static Schwarzschild gauge fields: the six frame-plane classes, the null rotation R(l,e2), complex loops, class supported on n^mbar. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    removed:
    - pairing.loop-classes-are-weyl-components
    added:
    - pairing.imported-weyl-scalars-petrov-type-schwarzschild
    note: 'The loop lemma gives only the Weyl reading, which is not part of the statement, so it moved from main to the standard-route the paper''s type-D remark describes; that route also uses the lemma, which is series-proved but completion-free; the pairing-class definition went into about.'
  env: proposition
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "$\\pm i\\,M/r^3$: values of the pairing class on the complexified spacetime $\\C^4$ (the null vector $m$ carries $i$ next to a spacetime vector), not the quantum unit"
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the curvature bivector of a loop is the covariant field strength of the Schwarzschild field on the physical plane of the loop, R(e_c, e_d) = R(hb(e_c ^ e_d)) = -R(e_c ^ e_d) with the store-sign operator (sign fixed from the stated identity R(l, e_2) = (M/r^3) l e_2 and the mixed-plane eigenvalue -M/r^3 of the stored spectrum); the static frame is the orthonormal physical frame of the static gauge. Classes and conclusions unchanged; the dictionary Fact added to uses for that identification; proof given a pointer.'
---

## formal
For the Schwarzschild gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) and the loop spanned by physical vectors $e_{c}, e_{d}$, let $R(e_{c}, e_{d}) = R(\hb(e_{c} \wedge e_{d})) = -\mathcal{R}(e_{c} \wedge e_{d})$ be the curvature bivector, the covariant field strength on the physical plane $e_{c} \wedge e_{d}$ in the sign of \cite{LDG1998}, so that the holonomy of a small loop of area $\epsilon$ is $\exp(\epsilon R)$ to first order. In the static orthonormal frame of physical vectors the pairing classes are
\begin{gather*}
\pv(R(e_{0},e_{1})) = \pv(R(e_{2},e_{3})) = 0, \\
\pv(R(e_{0},e_{2})) = \frac{M}{r^{3}}, \qquad \pv(R(e_{1},e_{2})) = -\frac{M}{r^{3}}, \qquad \pv(R(e_{0},e_{3})) = I_5\frac{M}{r^{3}}, \qquad \pv(R(e_{1},e_{3})) = -I_5\frac{M}{r^{3}} .
\end{gather*}
The classes are numbers of $\mathrm{span}\{1, I_5\}$: the transverse null vector against which the class pairs is $m = e_{2} + I_5e_{3}$, complexified by the central pseudoscalar $I_5$ of $\Cl(2,3)$, the unit that commutes with every spacetime vector (\claimref{std-algebra.complexification-is-the-odd-extension}), and $\mb = e_{2} - I_5e_{3}$, so $\ip{m}{\mb} = -2$ (the normalisation for which the classes take the values stated).
Hence $R(\ell, e_{2}) = (M/r^{3})\,\ell e_{2}$ is a null rotation about $\ell$ with zero class, while $R(n, e_{2})$ has class $2M/r^{3}$; on the complex loops, $(\ell, m)$, $(\ell, \mb)$, $(m, \mb)$ and $(n, m)$ have zero class and $(n, \mb)$ has class $4M/r^{3}$. The holonomy therefore moves the vacuum exactly for loops with an $n \wedge \mb$ component, and for no loop lying in the null hypersurface generated by $\ell$.

## technical
For the Schwarzschild field on flat spacetime and the loop spanned by physical vectors $e_c, e_d$, the holonomy of a small loop of area $\epsilon$ is $\exp(\epsilon R(e_c, e_d))$ to first order, with $R(e_c, e_d) = -\mathcal{R}(e_c \wedge e_d)$ the field strength on the plane of the loop, and its pairing class $\pv(R(e_c, e_d))$ records whether it moves the vacuum. In the static orthonormal frame the classes vanish for the loops $(e_0, e_1)$ and $(e_2, e_3)$, and are $M/r^3$, $-M/r^3$, $I_5M/r^3$ and $-I_5M/r^3$ (numbers of $\mathrm{span}\{1, I_5\}$, the unit of the complex null vector $m = e_2 + I_5e_3$) for $(e_0, e_2)$, $(e_1, e_2)$, $(e_0, e_3)$ and $(e_1, e_3)$.

By bilinearity $R(\ell, e_2) = (M/r^3)\,\ell e_2$ is a null rotation about $\ell$ with zero class, while $R(n, e_2)$ has class $2M/r^3$; among the complex loops only $(n, \mb)$ has nonzero class, $4M/r^3$. So the holonomy moves the vacuum exactly for loops with an $n \wedge \mb$ component, and for no loop lying in the null hypersurface generated by $\ell$.

## lay
Carrying the vacuum around a tiny closed loop in the gravitational field of a black hole can leave it unchanged or tilt it, depending on the loop's orientation; what tilts it is the strength of the field on the loop's plane. For Schwarzschild, loops lying in the light-like surface swept out by outgoing light rays never move the vacuum; only loops with a component along one particular ingoing complex direction do. This is a component form of the classical fact that the Schwarzschild field strength is of the simplest special algebraic type.

## one-liner
For the Schwarzschild field on flat spacetime the holonomy of the field strength moves the outgoing vacuum exactly for loops with an $n \wedge \mb$ component, and for no loop in the null hypersurface generated by $\ell$.
