---
id: synthesis.boost-evolution-on-generators-is-one-unitary-group
kind: claim
version: 5
title: 'Boost evolution on horizon generators is one unitary dilation group'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, modular-theory, horizons, car-algebra, rotors-and-stabilisers, dictionaries, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'unit resolution pass, the quoted window dynamics written with the transverse unit J'
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the smeared form of the boost evolution in (ii) corrected to a(D_{-lambda} f), with the antilinear step of (iii) written out (restatement), and the spreading-law citation made a mention'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: draft
about:
- obj.hawking.continuum-mode-space
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - field-theory.second-quantisation@5
  - tower.structure-tower-c-norms@9
  - synthesis.phase-flow-is-time-rotor-flow-kms-continuation@3
  - synthesis.affine-cell-boost-spreads-without-scrambling@3
  - synthesis.number-diagonal-dynamics-spreads-nothing@2
  - singularity.euclidean-rotor-where-it-lies@5
  - synthesis.positive-null-energy-gives-r-premises@7
  - hawking.i-state-continuum@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_canonical_component_on_the_null_plane
- kind: check
  ref: check.py::check_rotor_and_transport_are_the_two_factors
- kind: check
  ref: check.py::check_mellin_modes_carry_the_phase_flow
- kind: check
  ref: check.py::check_imaginary_rapidity_is_the_euclidean_rotor
- kind: check
  ref: check.py::check_real_time_anticommutators_stay_bounded
- kind: check
  ref: check.py::check_one_group_comparison
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - note.decisions.two-boost-flows
  - synthesis.n-plus-null-ground-state
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Formal correction (DECISIONS A2, restatement): formal (ii) displayed alpha_l(a(f)) = a(D_l f); with a(f) = int conj(f) psi_m du and alpha_l(psi_m(u)) = e^{-l/2} psi_m(e^{-l} u), the substitution v = e^{-l} u gives alpha_l(a(f)) = a(g), g(v) = e^{l/2} f(e^l v) = (D_{-l} f)(v) (checked by hand by the reconciler and on an exact log-lattice model by the reader), so (ii) now reads a(D_{-lambda} f) and the dilation of the affine-cell result with the time parameter reversed. The proof of (iii) had pulled the phase out of the antilinear a without conjugating (two compensating slips); it now writes a(D_{-lambda} f_w) = a(e^{I_4 w lambda} f_w) = e^{-I_4 w lambda} a(f_w). Clause (iii)''s Hamiltonian +kappa w was right and is unchanged, as are (v) and (vi). The uses edge to scrambling.spreading-law-chaos-bound-saturated is removed (DECISIONS B1 consequence; a uses edge change is routine): this result cites that estimate only to restate its chaos-bound comparison and to contradict its ''saturated by construction'' sentence, never as a premise, so the citation stays as a mention. With B1 lowering the estimate to conjectured, the edge made this result and its dependants (synthesis.modular-period-on-values-is-the-dual-plane-turn, synthesis.wedge-reflections-compose-to-the-two-pi-rotor-...) effectively conjectured (E204). check_one_group_comparison no longer calls premise() on the spreading-law estimate (it computes nothing from it); runcheck and check4 pass.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U2 for the quoted window dynamics: a_j -> e^{-J omega_j t}a_j with J = e_2 e_3, the boundary modes'' complex unit (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited in the proof as a mention); the generator''s continuum keeps I_4 (U1), and the proof now says which unit acts where and that the comparison is of frequencies, the units not identified. Declaration removed: no bare i remains.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The field''s operator unit on the even values of the canonical null component (Definition obj.field-theory.single-algebra-field: i = I_4) is written I_4 throughout: the Mellin modes |u|^{-1/2 + I_4 w}, the phase flow e^{-I_4 kappa w t}, the imaginary rapidity lambda = I_4 theta, the value rotor B_{I_4 theta} = cos + I_4 e1e0 sin with B_{I_4 theta}Lambda(m) = e^{-I_4 theta/2}Lambda(m), the rotation u -> e^{-I_4 theta}u into span{1, I_4} and the factor -I_4 at theta = pi, numbers read in span{1, I_4}; the proof''s quoted window formula a_j -> e^{-i omega_j t}a_j keeps i (Leon''s ruling R1: window flows keep their own unit) and is declared.'
  open_problem: op.which-boost-flow-is-time
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Clause (vi): "argued, not derived" dropped, since synthesis.killing-horizon-value-factor-is-the-generator-boost derives the value factor at every Killing horizon with nonzero surface gravity, off its bifurcation surface; that result is cited in the text and not added as a uses edge, because it uses this entity (clauses (i) and (ii)) and the edge would close a cycle. The citation of the dilation u -> e^{kappa t} u is corrected from item (iii) to the setup (the boost beta_t) of synthesis.positive-null-energy-gives-r-premises. Version 1 -> 2.'
  note: >-
    The problem's first line of attack (the continuum identification) and its second (the restated chaos-bound
    sentence). The stored phase-flow result settles the windows; this settles the continuum and finds one
    evolution, not two. Transport-convenient: the factorisation is the boost rotor of the spacetime algebra acting
    on field values and the transport of the affine parameter by the same rotor; the analytic content (Mellin
    diagonalisation, the strip) is transport-absent. Literature cited from memory: the restriction of the
    Pauli-Jordan function to a null plane, whose generator derivative is a multiple of the delta function on the
    plane (light-front quantisation; used only for the normalisation of the kernel, not for its transformation law),
    and the Mellin-Plancherel theorem (the half-density monomials u^{-1/2+iw} as generalised eigenvectors of the
    dilation, complete on each half-generator). What is new is (i) and (ii): the canonical light-ray component Lambda(m)
    on the null plane and the factorisation of the evolution into rotor and transport. Clauses (iii) to (v) restate,
    on that basis, the stored phase-flow and affine-cell results. Clause (ii) contains the weight-1/2 dilation of the
    edge-scaling result filed alongside (synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit, clause (i));
    the present form adds the factorisation and the canonical component. The conclusion contradicts the sentence
    of scrambling.spreading-law-chaos-bound-saturated that the window saturates the chaos bound by construction:
    at the level of the free continuum dynamics the bound is met, not saturated. The wording of that entity is left
    to the maintainer.
---
## formal
Work in the spacetime algebra $\Cl(1,3)$ of the flat background with the store's signature, on a local Rindler horizon of a region of vanishing field strength (for the Killing horizons see (vi)). Let $k$ be a future null vector, $m$ the null vector with $\ip{k}{m} = 1$ in the plane of $k$ and $e_{0}$, $N_{k} = \{x : \ip{x}{k} = 0\} = \{u\,k + x_{\perp}\}$ the null plane with generators along $k$ and affine parameter $u$, edge $u = 0$. Let $\Lambda(a) = a\gamma_{0}/(2a_{0})$ (Proposition \claimref{field-theory.second-quantisation}(1)), $x^{*}$ the frame $*$-structure (Theorem \claimref{tower.structure-tower-c-norms}), and $B_{\lambda} = \exp(\tfrac{\lambda}{2}\,k\wedge m)$ normalised so that $B_{\lambda}kB_{\lambda}^{\sim} = e^{\lambda}k$ and $B_{\lambda}mB_{\lambda}^{\sim} = e^{-\lambda}m$ (for $k = e_{0} + e_{1}$: $B_{\lambda} = \cosh\tfrac{\lambda}{2} + e_{1}e_{0}\sinh\tfrac{\lambda}{2}$), the boost of the horizon, with rapidity $\lambda = \kappa t$.
\begin{enumerate}
\item[(i)] \emph{(The canonical component.)} $\Lambda(m)\,a\gamma_{0}\,\Lambda(m) = 0$ for $a = k$ and for $a \perp k, m$, and $\Lambda(m)\,m\gamma_{0}\,\Lambda(m) = \Lambda(m)$. With $\nabla = k\,(m\cdot\nabla) + m\,(k\cdot\nabla) + \nabla_{\perp}$, the stored anticommutator $\chi(\nabla D)\gamma_{0}$ compressed to $\Lambda(m)$ is $\chi\,(k\cdot\nabla D)\,\Lambda(m)$: it involves only the derivative along the generators, so $\psi_{m} = \Lambda(m)\psi$ is the canonical component on $N_{k}$, with kernel a multiple of $\delta(u - v)\delta^{2}(x_{\perp} - y_{\perp})\Lambda(m)$, and on each generator its algebra is the continuum mode space $\CAR(L^{2}(\R, du)\otimes\Lambda(m)S)$ of Definition \claimref{obj.hawking.continuum-mode-space}. The other component $\Lambda(k)\psi$ keeps only the $m\cdot\nabla$ part, a derivative off the plane.
\item[(ii)] \emph{(Two factors, one automorphism.)} The covariant action $\psi(x) \mapsto B_{\lambda}\psi(B_{\lambda}^{\sim}xB_{\lambda})$ is, on $\psi_{m}$ along a generator, the product of two factors: the rotor on values, $B_{\lambda}\Lambda(m) = e^{-\lambda/2}\Lambda(m)$, with $B_{\lambda}^{*} = B_{\lambda}$ and $B_{\lambda}\Lambda(m)B_{\lambda}^{*} = e^{-\lambda}\Lambda(m)$; and the transport of the affine parameter, $B_{\lambda}^{\sim}(uk)B_{\lambda} = e^{-\lambda}u\,k$, which multiplies the delta kernel by $e^{\lambda}$. Their product is
\[
\alpha_{\lambda}(\psi_{m}(u)) = e^{-\lambda/2}\psi_{m}(e^{-\lambda}u), \qquad \alpha_{\lambda}(a(f)) = a(D_{-\lambda}f),\quad (D_{\lambda}f)(u) = e^{-\lambda/2}f(e^{-\lambda}u),
\]
with $D_{\lambda}$ unitary and $D_{\lambda}D_{\mu} = D_{\lambda+\mu}$, so $\alpha$ is a one-parameter group of quasi-free $*$-automorphisms; it is the dilation of Proposition \claimref{synthesis.affine-cell-boost-spreads-without-scrambling} with the time parameter reversed. Neither factor alone preserves the anticommutator (they rescale it by $e^{\mp\lambda}$), so neither is a $*$-automorphism, and among weights $e^{-w\lambda}$ only $w = \tfrac12$ makes the product unitary. On $\Lambda(k)\psi$ the rotor weight is $e^{+\lambda/2}$ and the two factors do not cancel.
\item[(iii)] \emph{(The phase flow.)} Numbers are read in $\mathrm{span}\{1, I_{4}\}$, the unit $I_{4}$ being the field's operator unit on the even values (Definition \claimref{obj.field-theory.single-algebra-field}). On each half-generator the half-density monomials $f_{w}(u) = |u|^{-1/2 + I_{4}w}$ satisfy $D_{\lambda}f_{w} = e^{-I_{4}w\lambda}f_{w}$, and a weight $e^{-\lambda(1/2 + s)}$ on $|u|^{s}$, $s \in \mathrm{span}\{1, I_{4}\}$, is a phase exactly when $\mathrm{Re}\,s = -\tfrac12$. So in the Mellin basis $\alpha_{\kappa t}$ is the phase flow $a(f_{w}) \mapsto e^{-I_{4}\kappa wt}a(f_{w})$ of one-particle Hamiltonian $\kappa w$, spectrum all of $\R$: the boost dynamics of the windows (Proposition \claimref{synthesis.phase-flow-is-time-rotor-flow-kms-continuation}) with its point spectrum refined to the continuum.
\item[(iv)] \emph{(Imaginary rapidity.)} Continued to $\lambda = I_{4}\theta$ the two factors are the Euclidean rotor $B_{I_{4}\theta} = \cos\tfrac{\theta}{2} + I_{4}e_{1}e_{0}\sin\tfrac{\theta}{2}$ of Proposition \claimref{singularity.euclidean-rotor-where-it-lies} on values (its unit read on the even values as $I_{4}$, as that proposition's note on values records), $B_{I_{4}\theta}\Lambda(m) = e^{-I_{4}\theta/2}\Lambda(m)$, and the rotation $u \mapsto e^{-I_{4}\theta}u$ of the affine parameter into the plane $\mathrm{span}\{1, I_{4}\}$. At $\theta = \pi$ it carries the half-generator $u > 0$ to $u < 0$ with factor $-I_{4}$; at $\theta = 2\pi$ it returns with factor $-1$, at $4\pi$ with $+1$. On Mellin modes the continued phase is the real factor $e^{w\theta}$: the rotor flow, which rescales the modes, is this group's continuation into the strip, and under (N$_{+}$) the restriction of the ground state to a half-generator is KMS for $\alpha$ at $\theta = 2\pi$ (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}).
\item[(v)] \emph{(Real time.)} For all $f, g$ and all real $\lambda$, $|\{a(D_{\lambda}f), a^{*}(g)\}| = |\ip{g}{D_{\lambda}f}| \le \|f\|\,\|g\|$, and for two fixed affine cells it falls as $e^{-\lambda/2}$. The anticommutator of linear elements is a scalar, so in every state the out-of-time-order correlators built from them are bounded: the real-time Lyapunov exponent of the quasi-free dynamics $\alpha$ on linear elements is $0$. Nothing here bears on non-quadratic dynamics. What grows at rate $\kappa$ in real time is the support, which covers $e^{\kappa t}$ affine cells (Proposition \claimref{synthesis.affine-cell-boost-spreads-without-scrambling}); what grows in imaginary time is the Mellin factor $e^{w\theta}$.
\item[(vi)] \emph{(Killing horizons.)} At the eternal hole's horizon and at the de Sitter cosmological horizon the Killing flow acts on the affine parameter of the generators as $u \mapsto e^{\pm\kappa t}u$ (the boost $\beta_{t}$ of the setup of Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}); by (ii) the anticommutator then forces the weight $\tfrac12$, so the boost time evolution there is the same group $\alpha_{\kappa t}$, and (iii) to (v) hold unchanged. That its value factor is the boost of the frame along the generator, relative to frames parallel along the generators, is derived for every Killing horizon with nonzero surface gravity, off its bifurcation surface and whatever the field strength, in Theorem \claimref{synthesis.killing-horizon-value-factor-is-the-generator-boost}, which builds on (i) and (ii) here.
\end{enumerate}
Hence the two boost flows of the series are one $*$-automorphism group of the continuum read in real and imaginary rapidity: the time evolution is $\alpha_{\kappa t}$, and the rotor flow is its continuation into the KMS strip, as on the windows, with the continuum adding that the real rotor of $\Cl(1,3)$ and the transport of the affine parameter are the two factors of the one unitary evolution. The chaos-bound comparison of Assumption \claimref{scrambling.spreading-law-chaos-bound-saturated} restated on this basis: one unitary group has real-time support-dilation rate $\kappa$ and, under (N$_{+}$), KMS period $2\pi/\kappa$, so the equality of the rate with $2\pi T$ is the identity $\kappa\beta = 2\pi$ of that group, derived from (N$_{+}$) on the continuum and holding on the windows only under (R); the real-time Lyapunov exponent of this quasi-free dynamics is $0$, so the chaos bound is met, not saturated, which contradicts the earlier sentence of Assumption \claimref{scrambling.spreading-law-chaos-bound-saturated} that the window saturates it by construction, at the level of the free continuum dynamics, and $t_{*} = \kappa^{-1}\ln N = (\beta/2\pi)\ln N$ is the time for one affine cell to cover $N$ cells, $\ln N$ units of rapidity. The comparison does not need two distinct evolutions. The equality is a property of the state, not of the group: a stationary state of the half-generator that is KMS for $\alpha$ at rapidity period $2\pi c$ (the continuum I-state at that period exists for every $c > 0$) sees the same real-time rate $\kappa$ and the KMS period $2\pi c/\kappa$, so the identity holds exactly when $c = 1$, which (N$_{+}$) supplies.

## technical
The series names two boost flows with one generator: the real rotor flow, which rescales the modes and drives the scrambling law, and the phase flow, which carries the KMS analysis. On the windows the stored result shows that only the phase flow is a time evolution. On the continuum of a horizon generator the question can be answered more fully, because there both flows are visible inside one unitary map.

The spinor field restricted to the null plane of a horizon has one canonical component, picked out by the projector onto the kernel of the dual null vector $m$: on it the stored anticommutator keeps only the derivative along the generators. The boost rotor acts on that component's values by the weight $e^{-\lambda/2}$, and the same rotor moves the points of each generator by $u \mapsto e^{-\lambda}u$ in the argument. The weight alone shrinks the anticommutator, the transport alone stretches it, and together they preserve it: the product is the unitary dilation that the stored affine-cell result uses. In the Mellin basis of half-density powers of $u$ it is the phase flow with continuous spectrum; continued to imaginary rapidity it is the Euclidean rotor on values times a rotation of $u$ into the complex plane, which at half a turn reaches the other half of the generator and at a full turn gives the spinor sign. So the rotor flow is the same group's imaginary-time continuation.

In real time the anticommutators of linear elements stay bounded and fall off for fixed cells, so the Lyapunov exponent of this quasi-free dynamics is zero, and the stored statement that the window saturates the chaos bound by construction does not hold for it: the bound is met, not saturated; the rate $\kappa$ shows up as the dilation of support, not as growth. The chaos-bound sentence then compares a single group's dilation rate with its own KMS period under (N$_{+}$), whose product $2\pi$ is the rapidity period that premise gives. The claim's checks verify the Clifford identities, the kernel factors, the Mellin exponents, the Euclidean factors and the cell bounds exactly; the light-front normalisation of the kernel and the Mellin-Plancherel theorem are cited from memory, and the value factor at Killing horizons of nonvanishing field strength is argued.

## lay
Near a horizon the series uses two descriptions of "letting time run": one that stretches things and one that turns phases. They looked like two different motions. Along a single light ray of a horizon they turn out to be one motion seen two ways. Running time does two things at once to the field on the ray: it shrinks the field's value and slides its profile further out along the ray. Either on its own would spoil the basic rule fermions obey; together they keep it. Written in the right basis this one motion just turns phases, and run in imaginary time it stretches, which is the other description. Nothing grows exponentially in real time for this free motion: the field only spreads out thinly, so the earlier statement that the horizon reaches the maximal rate of chaos does not hold for it, and, given the series' premise that the modes on each light ray are in their lowest-energy state, the rate at which it spreads matches the temperature because both come from the same motion.

## one-liner
On the continuum of a horizon's generators the boost time evolution is one unitary dilation, the boost rotor on the field's canonical null component (weight $e^{-\lambda/2}$) times the transport of the affine parameter, neither of which preserves the anticommutator alone; it is the phase flow on Mellin modes and the Euclidean rotor at imaginary rapidity, so the two boost flows are one group read in real and imaginary time, the real-time Lyapunov exponent of this quasi-free dynamics on linear elements is $0$ (the chaos bound met, not saturated, contrary to the earlier wording of the stored saturation sentence, since corrected), and the chaos-bound comparison is that group's dilation rate against its own KMS period, $\kappa\beta = 2\pi$ under (N$_{+}$).
