---
id: pairing.regular-frame-class-vanishes-horizon-changes
kind: claim
version: 7
title: 'The regular frame: the class vanishes on the horizon and changes sign inside'
status: proved
region: pairing
subject: thermality
tags: [pairing-and-bogoliubov, schwarzschild, horizons]
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
  role: 'unit resolution pass, the pairing classes written with the central unit I_5 of Cl(2,3)'
  version: 6
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: gauge field solved from the torsion equation, classes in Cl(2,3) with I_5; exact checks'
  version: 7
  source: maintainer pass 2026-11-07 (GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review fixes (referee F2): the formal and technical levels state the rotation-gauge field as bivectors, the forms kept as a labelled reading; uses and pins'
  version: 7
  source: maintainer pass 2026-11-07 (GTG review fixes)
review: typed
about:
- obj.pairing.pairing-class-transport
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - pairing.imported-schwarzschild-connection-curvature@7
  - pairing.pairing-class-transverse-derivative-null-direction@4
  - pairing.two-frames-share-vacuum-selected-transport@6
  - pairing.imported-spin-coefficients-null-tetrad@3
  - std-algebra.complexification-is-the-odd-extension@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_regular_frame_connection_is_torsion_free
- kind: check
  ref: check.py::check_outgoing_classes_expansion_and_acceleration
- kind: check
  ref: check.py::check_ingoing_classes_one_signed
- kind: check
  ref: check.py::check_static_and_regular_frames_agree
- kind: check
  ref: check.py::check_curvature_classes_do_not_vanish_on_the_horizon
- kind: check
  ref: check.py::check_gtg_torsion_solution_is_the_pg_gauge_field
- kind: check
  ref: check.py::check_gtg_classes_and_loop_class_in_cl23
locators:
  paper: T05-pairing
  number: Prop 5.3
  label: prop:pg
  line: 327
extraction:
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee F2 findings applied. (1) Language: the formal and technical levels defined the field only by its coframe and connection one-forms; they now state the frame by hb^{-1}(e_t) = e_0 + beta e_1, hb^{-1}(e_r) = e_1, hb^{-1}(e_theta) = r e_2, hb^{-1}(e_phi) = r sin(theta) e_3 and the rotation-gauge field as the four bivectors of the proof, Omega(e_0) = 0, Omega(e_1) = -beta'' e_1 e_0, Omega(e_2) = (beta e_0 + e_1) ^ e_2/r, Omega(e_3) = (beta e_0 + e_1) ^ e_3/r + (cot/r) e_2 ^ e_3, with the coframe and the connection forms omega^a_b(e_c) = e^a . (Omega(e_c) . e_b) kept as a labelled reading. Notation only: the bivectors are the torsion solution the check computes (rank 24 at five beta), and their components reproduce the stated forms (checked by hand: Omega(e_1) . e_1 = -beta'' e_0, Omega(e_2) . e_0 = -(beta/r) e_2). (2) uses: std-algebra.complexification-is-the-odd-extension@2 added (the I_5 classes and m = e_2 + I_5 e_3 rest on it; cited in the formal and proof). Repinned pairing.imported-schwarzschild-connection-curvature 5 -> 6 (formal unchanged), pairing.imported-spin-coefficients-null-tetrad 2 -> 3 (the unit I_5 named, U3) and pairing.two-frames-share-vacuum-selected-transport 5 -> 6 (clause (ii) now cites this result as a mention; the clause (i) rescaling this proof uses is unchanged). Version kept at 7.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof rewritten in GTG: the PG gauge field hb^{-1}(e_t) = e_0 + beta e_1, the rotation-gauge field solved from the torsion equation hb^T(grad ^ f^a) = sum_b e^b ^ (Omega(e_b) . e^a) (unique, rank 24): Omega(e_0) = 0, Omega(e_1) = -beta'' e_1 e_0, Omega(e_2) = (beta e_0 + e_1) ^ e_2/r, Omega(e_3) = (beta e_0 + e_1) ^ e_3/r + (cot theta/r) e_2 ^ e_3; classes as symmetric products in Cl(2,3) with the central unit I_5 ((u ^ e_2) . l = -(u . l) e_2); the static frame built inside the same gauge for the covariance; the loop class from the field strength of the solved field. Structure equations kept as a labelled reading. Checked exactly: check_gtg_torsion_solution_is_the_pg_gauge_field (solve from the coframe alone, rank 24, the four bivectors at five points beta = 4/5, 1, 2, 1/3, 3/5) and check_gtg_classes_and_loop_class_in_cl23 (I_5 central of square -1; outgoing and ingoing classes, (l.D)l = (beta^3/4M) l, the values 144/125, 2, 12 and the loop class 2M/r^3, all from the solved field). Version 6 -> 7; outside_ga removed (the forms are now a reading).'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The proof works with the coframe and connection one-forms (beta'' dr ^ dT) of the Painleve-Gullstrand frame; the forms are the computation.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the pairing classes are coordinates on the tangent space complexified with the transverse null vector m = e_2 + i e_3, whose unit must commute with every spacetime vector; it is the central unit I_5 = I_4 e of Cl(2,3) (std-algebra.complexification-is-the-odd-extension, cited as a mention), so m = e_2 + I_5 e_3 and the classes -I_5(1 - beta)/r, +I_5(1 + beta)/r are numbers of span{1, I_5}. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: -i(1 - beta)/r and +i(1 + beta)/r are classes on the complex null vector m = e_2 + i e_3 of the complexified tangent space. Declared other.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: PG gauge fields: connection forms torsion-free through the horizon; outgoing and ingoing classes, expansion, (l.D)l; static frame built in the same gauge gives the covariant factor; curvature and the (n,e2) class. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - obj.pairing.pairing-class-transport
    note: 'Kept all three premises (the metric Fact, the scaling law and the frame relation of the two-frames
      proposition); the two-frames proposition in turn cites this one for its clause (ii), an edge not
      added there because it would close a cycle. Levels pass: conditions already kept.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$-i(1 - \beta)/r$, $+i(1 + \beta)/r$: pairing classes valued in the complexified tangent space, $m
      = e_2 + ie_3$ (complexified space, $i$ next to spacetime vectors)'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Painleve-Gullstrand frame is the orthonormal physical frame of the gauge hb = 1 - beta P (coframe = components of hb^{-1}(dx)); Omega(e_c) named as the rotation-gauge field along the physical vector e_c, i.e. Omega(hb(e_c)); nabla_l l -> (l.D)l; curvature -> field strength; horizon -> horizon locus. Formulas and values unchanged; proof given a pointer.'
---

## formal
For the Schwarzschild gravitational field on flat spacetime in the Painlev\'e-Gullstrand gauge $\hb = 1 - \beta P$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), take the constant orthonormal physical frame $\{e_a\}$ with $\hb^{-1}(e_{t}) = e_{0} + \beta e_{1}$, $\hb^{-1}(e_{r}) = e_{1}$, $\hb^{-1}(e_{\vartheta}) = r\,e_{2}$, $\hb^{-1}(e_{\varphi}) = r\sin\vartheta\,e_{3}$ ($e_{t}, \dots, e_{\varphi}$ the background frame of the labels; in components, its coframe, the components of the physical displacement $\hb^{-1}(dx)$, is $\theta^{0} = dT$, $\theta^{1} = dr + \beta\,dT$, $\theta^{2} = r\,d\vartheta$, $\theta^{3} = r\sin\vartheta\,d\varphi$). The rotation-gauge field along this frame, written $\Omega(e_c)$ for $\Omega(\hb(e_c))$ (the bivector of item (b) of the definition along the physical vector $e_c$), is
\[
\Omega(e_{0}) = 0, \quad \Omega(e_{1}) = -\beta'\,e_{1}e_{0}, \quad \Omega(e_{2}) = \frac{(\beta e_{0} + e_{1})\wedge e_{2}}{r}, \quad \Omega(e_{3}) = \frac{(\beta e_{0} + e_{1})\wedge e_{3}}{r} + \frac{\cot\vartheta}{r}\,e_{2}\wedge e_{3},
\]
where $\beta' = d\beta/dr = -\beta^{3}/4M$ (in components, a labelled reading: the connection forms $\omega^{a}{}_{b}(e_{c}) = e^{a}\cdot(\Omega(e_{c})\cdot e_{b})$ are $\omega^{0}{}_{1} = -\beta'\,\theta^{1}$, $\omega^{2}{}_{1} = \theta^{2}/r$, $\omega^{2}{}_{0} = -(\beta/r)\,\theta^{2}$, with $\hat3$ mirroring $\hat2$ and $\omega^{3}{}_{2} = (\cot\vartheta/r)\theta^{3}$). The pairing classes of the outgoing vacuum $\ell = e_{0} + e_{1}$ are
\[
\pv(\Omega(e_{0})) = \pv(\Omega(e_{1})) = 0, \qquad \pv(\Omega(e_{2})) = -\frac{1 - \beta}{r}, \qquad \pv(\Omega(e_{3})) = -\,I_{5}\,\frac{1 - \beta}{r},
\]
numbers of $\mathrm{span}\{1, I_{5}\}$, with $I_{5} = I_{4}e$ the central unit of the odd extension $\Cl(2,3)$, in which the transverse complex null vector is $m = e_{2} + I_{5}e_{3}$ (\claimref{std-algebra.complexification-is-the-odd-extension}); zero on the horizon locus $\beta = 1$, negative outside and positive inside; the transverse expansion is $2(1 - \beta)/r$, the expansion of the outgoing congruence, which vanishes on the horizon locus and is negative in the trapped region; and $(\ell \cdot D)\ell = (\beta^{3}/4M)\,\ell$. For the ingoing flag bit, the vacuum $\operatorname{span}\{n, m\}$ with $n = e_{0} - e_{1}$, the transverse classes are $+(1 + \beta)/r$ and $+I_{5}(1 + \beta)/r$: one sign throughout, $\tfrac{144}{125}$, $2$ and $12$ at $\beta = \tfrac45, 1, 2$, and no horizon zero, the ingoing rays converging everywhere. The two frames agree covariantly: $\pv_{\mathrm{PG}} = \tfrac{F}{1 + \beta}\,\pv_{\mathrm{static}}$ in both transverse directions, the factor being the rescaling $\ell_{\mathrm{PG}} = (F/(1 + \beta))\,\ell_{\mathrm{static}}$; at $(F, \beta) = (\tfrac35, \tfrac45)$ the values are $-\tfrac{16}{125} = \tfrac13\cdot(-\tfrac{48}{125})$. The field strength $\mathcal{R}(B)$ read in the regular frame has the same coefficients as functions of $r$, and the class of the loop $(n, e_{2})$ is $2M/r^{3}$ in this frame too, equal to $1$ on the horizon locus at $M = \tfrac12$: the curvature classes do not vanish where the connection classes do.

## technical
For the Schwarzschild field on flat spacetime in the Painlev\'e-Gullstrand gauge, the orthonormal physical frame is given by $\hb^{-1}(e_t) = e_0 + \beta e_1$, $\hb^{-1}(e_r) = e_1$, $\hb^{-1}(e_\vartheta) = r\,e_2$, $\hb^{-1}(e_\varphi) = r\sin\vartheta\,e_3$ (in components, the coframe $\theta^0 = dT$, $\theta^1 = dr + \beta\,dT$, $\theta^2 = r\,d\vartheta$, $\theta^3 = r\sin\vartheta\,d\varphi$), and the rotation-gauge field along it is $\Omega(e_0) = 0$, $\Omega(e_1) = -\beta' e_1e_0$, $\Omega(e_2) = (\beta e_0 + e_1)\wedge e_2/r$, $\Omega(e_3) = (\beta e_0 + e_1)\wedge e_3/r + (\cot\vartheta/r)\,e_2\wedge e_3$, with $\beta' = -\beta^3/4M$. It gives the outgoing vacuum $\ell = e_0 + e_1$ the pairing classes $\pv(\Omega(e_0)) = \pv(\Omega(e_1)) = 0$, $\pv(\Omega(e_2)) = -(1 - \beta)/r$ and $\pv(\Omega(e_3)) = -I_{5}(1 - \beta)/r$, numbers of $\mathrm{span}\{1, I_{5}\}$ with $I_{5}$ the central unit of $\Cl(2,3)$ that complexifies the transverse null vector $m = e_{2} + I_{5}e_{3}$: zero on the horizon locus $\beta = 1$, negative outside and positive inside. The transverse expansion $2(1 - \beta)/r$ of the outgoing congruence vanishes on the horizon locus and is negative in the trapped region, and $(\ell \cdot D)\ell = (\beta^3/4M)\,\ell$.

For the ingoing vacuum $\operatorname{span}\{n, m\}$, $n = e_0 - e_1$, the transverse classes are $(1 + \beta)/r$ and $I_{5}(1 + \beta)/r$, of one sign throughout with no horizon zero. The two frames agree covariantly, $\pv_{\mathrm{PG}} = \tfrac{F}{1 + \beta}\,\pv_{\mathrm{static}}$, the factor being the rescaling of $\ell$ between them. The curvature class of the loop $(n, e_2)$, read from the field strength, is $2M/r^3$ in this frame too, nonzero on the horizon: the curvature classes do not vanish where the connection classes do.

## lay
In axes carried by an observer falling freely into a non-rotating black hole, which stay regular across the horizon, transport leaves the outgoing light-like vacuum undisturbed exactly on the horizon and disturbs it with opposite signs outside and inside. This matches the familiar behaviour of outgoing light rays, which stop spreading at the horizon and converge inside it. The ingoing choice is disturbed everywhere with one sign, and the gravitational field strength's own contribution does not vanish on the horizon.

## one-liner
For the Schwarzschild field in the Painlev\'e-Gullstrand gauge the transverse pairing classes of the outgoing vacuum are $-(1 - \beta)/r$ and $-I_{5}(1 - \beta)/r$ ($I_{5}$ the central unit of $\Cl(2,3)$), vanishing on the horizon locus and changing sign inside, while the ingoing classes and the curvature class of the loop $(n, e_2)$ do not vanish there.
