---
id: pairing.regular-frame-class-vanishes-horizon-changes
kind: claim
version: 5
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
review: typed
outside_ga:
  kind: other
  why: 'the pairing classes are coordinates on the complexified tangent space of the complex null vector m = e_2 + i e_3, so the values -i(1 - beta)/r and +i(1 + beta)/r carry an i that must commute with the spacetime vectors, which no pseudoscalar does'
about:
- obj.pairing.pairing-class-transport
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - pairing.imported-schwarzschild-connection-curvature@5
  - pairing.pairing-class-transverse-derivative-null-direction@4
  - pairing.two-frames-share-vacuum-selected-transport@5
  - pairing.imported-spin-coefficients-null-tetrad@2
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
locators:
  paper: T05-pairing
  number: Prop 5.3
  label: prop:pg
  line: 327
extraction:
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
For the Schwarzschild gravitational field on flat spacetime in the Painlev\'e-Gullstrand gauge $\hb = 1 - \beta P$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), take the orthonormal physical frame $\{e_a\}$ whose coframe is the set of components of the physical displacement $\hb^{-1}(dx)$: $\theta^{0} = dT$, $\theta^{1} = dr + \beta\,dT$, $\theta^{2} = r\,d\vartheta$, $\theta^{3} = r\sin\vartheta\,d\varphi$. The rotation-gauge field along this frame, written $\Omega(e_c)$ for $\Omega(\hb(e_c))$ (the bivector of item (b) of the definition along the physical vector $e_c$), has the connection forms $\omega^{0}{}_{1} = -\beta'\,\theta^{1}$, $\omega^{2}{}_{1} = \theta^{2}/r$, $\omega^{2}{}_{0} = -(\beta/r)\,\theta^{2}$, with $\hat3$ mirroring $\hat2$ and $\omega^{3}{}_{2} = (\cot\vartheta/r)\theta^{3}$, where $\beta' = d\beta/dr = -\beta^{3}/4M$. The pairing classes of the outgoing vacuum $\ell = e_{0} + e_{1}$ are
\[
\pv(\Omega(e_{0})) = \pv(\Omega(e_{1})) = 0, \qquad \pv(\Omega(e_{2})) = -\frac{1 - \beta}{r}, \qquad \pv(\Omega(e_{3})) = -\,i\,\frac{1 - \beta}{r},
\]
zero on the horizon locus $\beta = 1$, negative outside and positive inside; the transverse expansion is $2(1 - \beta)/r$, the expansion of the outgoing congruence, which vanishes on the horizon locus and is negative in the trapped region; and $(\ell \cdot D)\ell = (\beta^{3}/4M)\,\ell$. For the ingoing flag bit, the vacuum $\operatorname{span}\{n, m\}$ with $n = e_{0} - e_{1}$, the transverse classes are $+(1 + \beta)/r$ and $+i(1 + \beta)/r$: one sign throughout, $\tfrac{144}{125}$, $2$ and $12$ at $\beta = \tfrac45, 1, 2$, and no horizon zero, the ingoing rays converging everywhere. The two frames agree covariantly: $\pv_{\mathrm{PG}} = \tfrac{F}{1 + \beta}\,\pv_{\mathrm{static}}$ in both transverse directions, the factor being the rescaling $\ell_{\mathrm{PG}} = (F/(1 + \beta))\,\ell_{\mathrm{static}}$; at $(F, \beta) = (\tfrac35, \tfrac45)$ the values are $-\tfrac{16}{125} = \tfrac13\cdot(-\tfrac{48}{125})$. The field strength $\mathcal{R}(B)$ read in the regular frame has the same coefficients as functions of $r$, and the class of the loop $(n, e_{2})$ is $2M/r^{3}$ in this frame too, equal to $1$ on the horizon locus at $M = \tfrac12$: the curvature classes do not vanish where the connection classes do.

## technical
For the Schwarzschild field on flat spacetime in the Painlev\'e-Gullstrand gauge, the orthonormal physical frame has coframe $\theta^0 = dT$, $\theta^1 = dr + \beta\,dT$, $\theta^2 = r\,d\vartheta$, $\theta^3 = r\sin\vartheta\,d\varphi$ (the components of $\hb^{-1}(dx)$), with $\beta' = -\beta^3/4M$. Along this frame the rotation-gauge field gives the outgoing vacuum $\ell = e_0 + e_1$ the pairing classes $\pv(\Omega(e_0)) = \pv(\Omega(e_1)) = 0$, $\pv(\Omega(e_2)) = -(1 - \beta)/r$ and $\pv(\Omega(e_3)) = -i(1 - \beta)/r$: zero on the horizon locus $\beta = 1$, negative outside and positive inside. The transverse expansion $2(1 - \beta)/r$ of the outgoing congruence vanishes on the horizon locus and is negative in the trapped region, and $(\ell \cdot D)\ell = (\beta^3/4M)\,\ell$.

For the ingoing vacuum $\operatorname{span}\{n, m\}$, $n = e_0 - e_1$, the transverse classes are $(1 + \beta)/r$ and $i(1 + \beta)/r$, of one sign throughout with no horizon zero. The two frames agree covariantly, $\pv_{\mathrm{PG}} = \tfrac{F}{1 + \beta}\,\pv_{\mathrm{static}}$, the factor being the rescaling of $\ell$ between them. The curvature class of the loop $(n, e_2)$, read from the field strength, is $2M/r^3$ in this frame too, nonzero on the horizon: the curvature classes do not vanish where the connection classes do.

## lay
In axes carried by an observer falling freely into a non-rotating black hole, which stay regular across the horizon, transport leaves the outgoing light-like vacuum undisturbed exactly on the horizon and disturbs it with opposite signs outside and inside. This matches the familiar behaviour of outgoing light rays, which stop spreading at the horizon and converge inside it. The ingoing choice is disturbed everywhere with one sign, and the gravitational field strength's own contribution does not vanish on the horizon.

## one-liner
For the Schwarzschild field in the Painlev\'e-Gullstrand gauge the transverse pairing classes of the outgoing vacuum are $-(1 - \beta)/r$ and $-i(1 - \beta)/r$, vanishing on the horizon locus and changing sign inside, while the ingoing classes and the curvature class of the loop $(n, e_2)$ do not vanish there.
