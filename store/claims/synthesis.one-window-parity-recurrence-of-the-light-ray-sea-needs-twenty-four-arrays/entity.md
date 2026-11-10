---
id: synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays
kind: claim
version: 1
title: 'One-window parity recurrence of the light-ray sea needs twenty-four arrays'
status: proved
region: synthesis
subject: thermality
tags: [boundary-modes, mode-counting, thermal-premises, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
review: draft
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves@1
  - std-algebra.witt-basis-car@1
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric@4
  - synthesis.counted-unit-energy-at-half-offset@3
  - synthesis.slot-module-light-ray-arrays-are-weyl-components@3
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays@5
  - synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators@1
  - synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free@2
  assumes:
  - singularity.q-joint-quasi-freeness-s-wave@3
  - synthesis.window-reading-array-killing-energy@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_one_window_flow_is_the_grading_on_every_window
- kind: check
  ref: check.py::check_window_reading_zero_is_minus_one_twenty_fourth_per_array
- kind: check
  ref: check.py::check_joint_flow_is_the_parity_exactly_when_twenty_four_divides_the_array_count
- kind: check
  ref: check.py::check_integer_weight_content_on_the_light_ray
- kind: check
  ref: check.py::check_two_models_of_the_cone_differ_on_the_condition
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric
  - synthesis.window-reading-array-killing-energy
  - synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free
extraction:
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Leon approved the assumes edges named at acceptance: (Q) singularity.q-joint-quasi-freeness-s-wave@3 and the window reading synthesis.window-reading-array-killing-energy@1, which define the sea, are now assumed directly (the proof cites (Q) by claimref in its audit); statement unchanged.'
  open_problem: op.counted-mode-energy
  note: >-
    Attack on the open question of op.counted-mode-energy recorded as argued on 31 October (which fields form the
    light-ray sea, and the recurrence test with the chiral central charge a multiple of 24), with its consequence for
    op.qft-structural-inputs (three generations). The test is made exact. On every finite window the stored window
    Sugawara identity gives the one-window flow of an array as the grading (-1)^Q, an even product of the window's
    mode bivectors (clause (i), exact on finite windows); the window reading adds the null-ordered constant -kappa/24
    per array, the zeta-regularised value of the infinite band that the reading fixes (clause (ii) uses this band
    value, not a finite-window sum), so the one-window Killing evolution of n arrays is e^{2 pi J n/24} times the
    grading, normalised to +1 on the sea. The automorphism it induces is the parity automorphism of (Q) for every n,
    and the KMS state does not see the constant, so the requirement that the evolution be the grading itself (the
    recurrence condition) is a strengthening of the one-period clause of (Q) from automorphism to operator, not
    implied by (Q), the KMS condition, (N+) or the window reading; it holds iff 24 | n (iff 12 | n if the grading's
    sign is left free). Clause (v) makes the independence a two-model statement: with the stored generation-number
    result (n_g free under the slot-module premise and anomaly freedom), models with one and with three generations
    satisfy every postulate of the past cone (audited in the proof) and differ on the condition. With sixteen Weyl
    components per generation the condition is n_g = 0 mod 3, not n_g = 3; without the neutral singlet n_g = 0 mod 8.
    J3 (hawking.joint-j3-s-wave-reduction, in the cone through the collapse result under the null-ordering result)
    reads the integer-weight channels as currents of the arrays, so under J3 they add nothing to n; clause (iv) is an
    alternative reading outside J3 and outside the CAR scope of (N+) and of the window reading, in which c_B real
    components are added and the condition needs c_B = 0 mod 8 before any n_g passes. Prior art (from the web, 9 November 2026): J. Wang, arXiv:2312.14928
    (2023), proposes that the number of families is a multiple of 3 from framing-anomaly freedom c_- = 0 mod 24 of the
    fermions reduced to a 1+1-dimensional defect, c = 1/2 per Weyl fermion read as a Majorana-Weyl mode, so c_- = 8 per
    family and 8 n_g = 0 mod 24 (three (E8)_1 copies); the conclusion 3 | n_g agrees with clause (iii), the fifteen-
    component case does not (there 45/2, short by 3/2; here 15 n_g = 0 mod 24 gives 8 | n_g). I. Garcia-Etxebarria
    and M. Montero, Dai-Freed anomalies in particle physics, JHEP 08 (2019) 003, arXiv:1808.00009: a Z4 symmetry
    anomaly-free when a generation has a multiple of 16 Weyl fermions, and baryon triality with a Z9 anomaly that
    cancels only if the number of generations is a multiple of 3, a classical anomaly route to 3 | n_g. Z. Wan, J. Wang
    and S.-T. Yau, arXiv:2605.26202 (2026): cancellation of the mixed (B+L)-gauge-gravitational anomaly by a Z3
    topological field theory, with N = N_c = N_f = 3 the minimal solution (abstract read only). Cited from memory: the
    framing anomaly e^{2 pi i c/24} (E. Witten, Commun. Math. Phys. 121 (1989) 351) and the T-transformation phase of
    a chiral character. The conclusion 3 | n_g is therefore prior art by two routes. New here: the condition read as
    the operator form of the one-period parity clause of the horizon's light-ray arrays, its absolute phase fixed by
    (N+) through the window reading with no dimensional reduction or modular forms, the window flow proved exactly on
    finite windows with the spacetime algebra's kernel unit; the two-model independence from the cone's postulates;
    the reading's offset selection for CCR arrays and the mod-8 condition on integer-weight content outside J3.
    Transport-absent.
---

## formal
Units $\hbar = c = 1$. On a half-generator of a horizon with surface gravity $\kappa$, let the light-ray sea be a set of $n$ arrays of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave} version 3 (weights $\kappa(k + \tfrac12)$, $k \in \Z$), each read by Premise \claimref{synthesis.window-reading-array-killing-energy} as one chiral complex component of the light ray on a Killing-time window of length $2\pi/\kappa$. Numbers are read in $\mathrm{span}\{1, J\}$, $J$ the kernel bivector of a tower level $\Cl(L, L + 2)$, $J^{2} = -1$, commuting with every plane generator (Theorem \claimref{synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves}(ii)). Call the \emph{recurrence condition} the requirement that the one-window Killing evolution $U$ of the sea, with energies measured from the null ground state of (N$_{+}$) as the window reading measures them, equal the grading $\Gamma$ of the sea's window algebra.
\begin{enumerate}
\item[(i)] \emph{(The window flow is the grading.)} On a window of $L = 2M$ planes with null pairs $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j})$, $n_{j} = v_{j}w_{j}$, levels $k = j - M$ and $H = \sum_{k}(k + \tfrac12)n_{k} + \tfrac12M^{2}$, which vanishes on the sea, exactly
\[
e^{2\pi JH} = \Gamma_{\mathrm{win}} := (-1)^{M}\prod_{j}e_{j}f_{j} = (-1)^{\mathcal{Q}}, \qquad \mathcal{Q} = \hat N - M ,
\]
an even product of vectors with $\Gamma_{\mathrm{win}}^{2} = 1$, commuting with $J$ and anticommuting with every $v_{j}$ and $w_{j}$, so that conjugation by it is $\psi \mapsto -\psi$; it fixes the sea, and the spectrum of $H$ lies in $\tfrac12\mathcal{Q} + \Z$. The same holds for $H_{\infty}$ on the domain of finite excitations of the infinite band. At the zero offset (weights $k$) the one-window flow is the identity.
\item[(ii)] \emph{(The window-reading constant.)} Under the window reading the Killing energy of one array in the null ordering is $\kappa(H - \tfrac{1}{24})$, the constant being the array's zeta-regularised symmetric sea at the half offset, $-\kappa\zeta(-1, \tfrac12) = -\kappa/24$, which is the null-ordered window value of Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(i), (ii); it is the zeta-regularised value of the infinite band that the window reading fixes, not a sum over a finite window (on a finite window (i) is exact and the sea has $H = 0$). Hence the one-window Killing evolution of the sea is
\[
U = e^{2\pi Jn/24}\,\Gamma, \qquad \Gamma = \prod_{a = 1}^{n}\Gamma_{a} ,
\]
$\Gamma$ the grading of the joint window algebra, normalised by $\Gamma = +1$ on the sea (an operator implementing the grading is fixed only up to sign). For every $n$, conjugation by $U$ is the parity automorphism (the one-period clause of (Q)), and the KMS state at $\beta = 2\pi/\kappa$ does not depend on the additive constant. $U = \Gamma$ exactly if and only if $24 \mid n$; more generally $U^{m} = \Gamma^{m}$ if and only if $24 \mid mn$, and $U^{2} = 1$ if and only if $12 \mid n$; with the sign of $\Gamma$ left free the condition $U = \pm\Gamma$ is $12 \mid n$, which on $n = 16n_{g}$ is again $3 \mid n_{g}$. One array has the phase $e^{2\pi J/24}$, one counted unit of two arrays $e^{2\pi J/12}$, one generation of sixteen arrays $e^{4\pi J/3}$, of order $3$: the condition constrains only the joint sea of the light ray.
\item[(iii)] \emph{(Counts.)} With the sixteen Weyl components per generation of Theorem \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}(ii) and $n_{x}$ further spinor arrays on the light ray (for example one array set per Kaluza-Klein level of a five-dimensional field, as there), the recurrence condition is $16n_{g} + n_{x} \equiv 0 \pmod{24}$. For $n_{x} = 0$ it holds exactly when $n_{g} \equiv 0 \pmod 3$. With fifteen components per generation and $r$ neutral singlets it is $15n_{g} + r \equiv 0 \pmod{24}$: for $r = 0$ exactly when $n_{g} \equiv 0 \pmod 8$, and at $n_{g} = 3$ exactly when $r \equiv 3 \pmod{24}$.
\item[(iv)] \emph{(Integer-weight content, a reading outside J3.)} The postulate \claimref{hawking.joint-j3-s-wave-reduction}, in the past cone of this result through the null-ordering result, reads every $(\omega, \ell, m, s)$ channel of a massless field, integer-weight ones included, as a current boson of the s-wave theory, the bosonised current of the arrays; under J3 the integer-weight fields add nothing to $n$ and (i)-(iii) are the whole count. This clause is an alternative reading, outside J3 and outside the CAR scope of (N$_{+}$) and of the window reading. A complex CCR array with weights $\kappa(k + \delta)$, $0 \le \delta < 1$, has symmetric zero-point energy $\tfrac12\sum_{k}|\omega_{k}| = -\tfrac{\kappa}{2}B_{2}(\delta)$ (zeta-regularised, $B_{2}(a) = a^{2} - a + \tfrac16$), and $-\tfrac{\kappa}{2}B_{2}(\delta) + \tfrac{\kappa}{12} = \tfrac{\kappa}{2}\delta(1 - \delta)$: it equals $-\kappa/12$, twice the per-component value $-\kappa/24$, exactly at $\delta = 0$, the integer weights of vector fields (Theorem \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(vi)); there a real component carries $-\kappa/24$ and the one-window flow on excitations is the identity. So if $c_{B}$ real integer-weight components of the light ray (for example the two transverse chiral fields per massless vector of Theorem \claimref{synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators}) are read in this way and included in the recurrence, $U = e^{2\pi J(16n_{g} + n_{x} + c_{B})/24}\Gamma$; for $n_{x} = 0$, $U = \Gamma$ exactly when $c_{B} \equiv 0 \pmod 8$ and $n_{g} \equiv c_{B}/8 \pmod 3$.
\item[(v)] \emph{(Two models of the cone.)} Let $\mathcal{M}_{1}$ and $\mathcal{M}_{3}$ be the series' content with one and with three separate generations, each light ray carrying their Weyl components as arrays of (Q) read by the window reading and no further spinor arrays. Every postulate in the past cone of this result holds in both (by Theorem \claimref{synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free}(3) for the slot-module premise and anomaly freedom, and by the audit in the proof for the rest, none of which constrains the number of generations or of arrays), while $U = e^{4\pi J/3}\Gamma \neq \Gamma$ in $\mathcal{M}_{1}$ and $U = \Gamma$ in $\mathcal{M}_{3}$. So the recurrence condition is neither implied nor excluded by the postulates of the cone.
\end{enumerate}
Hence the recurrence condition is the one-period clause of (Q) lifted from the automorphism to the operator that implements it, with the operator's normalisation fixed by the window reading; (ii) shows that (Q), the KMS condition and the window reading hold for every $n$, so it is not a consequence of them, and (v) shows it is independent of every postulate of the cone. It gives $n_{g} \equiv 0 \pmod 3$, not $n_{g} = 3$, on the spinor content alone; it needs the neutral singlet in each generation (or $r \equiv 3 \pmod{24}$ singlets at three generations); and including the integer-weight fields as further components, against J3, which reads them as currents of the arrays, changes the condition to one on $c_{B} \bmod 24$. Whether the condition holds is not decided here.

## technical
\emph{(i)} At $t = 2\pi$ the stored factorisation $e^{JtH} = e^{JtM^{2}/2}\prod_{k}(1 + (e^{Jt(k + 1/2)} - 1)n_{k})$ has $e^{J\pi M^{2}} = (-1)^{M}$ and $e^{\pi J(2k + 1)} = -1$, so each factor is $1 - 2n_{k}$; with $Q(e_{j}) = 1$ and $Q(f_{j}) = -1$, $n_{j} = \tfrac12(1 - e_{j}f_{j})$ and $1 - 2n_{j} = e_{j}f_{j}$. The bivectors $e_{j}f_{j}$ square to $1$, commute with each other and with $J$, and anticommute with $e_{j}$ and $f_{j}$; on occupation states $e_{j}f_{j}$ is $(-1)^{n_{j}}$, so the product is $(-1)^{\mathcal{Q}}$. The stored identity $H = \tfrac12\mathcal{Q}^{2} + T$, with $T$ integer-valued, puts the spectrum in $\tfrac12\mathcal{Q} + \Z$, since $\tfrac12\mathcal{Q}(\mathcal{Q} - 1)$ is an integer. The check verifies the operator identity and every occupation state on windows $L = 2, 4$.

\emph{(ii)} By Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(iv), under the window reading the physical ordering is the symmetric one, whose sea at $\delta = \tfrac12$ is $-\tfrac{\kappa}{2}(\zeta(-1, \tfrac12) + \zeta(-1, \tfrac12)) = -\kappa/24$; the excitation energies above the sea are $\kappa H$ in every ordering. The arrays' $H_{a}$ are even in disjoint planes and commute, so $U = \exp(-\tfrac{2\pi}{\kappa}J\sum_{a}\kappa(H_{a} - \tfrac1{24})) = e^{2\pi Jn/24}\prod_{a}\Gamma_{a}^{-1} = e^{2\pi Jn/24}\Gamma$. The phase lies in $\mathrm{span}\{1, J\}$, which commutes with every mode vector, so it drops out of conjugation; $e^{\theta J} = \cos\theta + J\sin\theta = 1$ only for $\theta \in 2\pi\Z$. The check computes $e^{2\pi J/24} = \cos\tfrac{\pi}{12} + J\sin\tfrac{\pi}{12}$ exactly in $\Q(\sqrt2, \sqrt3)$, with sixth power $J$, twelfth power $-1$ and first unit power the twenty-fourth.

\emph{(iii)} $16n_{g} \equiv 0 \pmod{24}$ is $2n_{g} \equiv 0 \pmod 3$; $15n_{g} \equiv 0 \pmod{24}$ is $5n_{g} \equiv 0 \pmod 8$; $45 + r \equiv 0 \pmod{24}$ is $r \equiv 3$.

\emph{(iv)} For $0 < \delta < 1$ the particle and hole towers $\kappa(m + \delta)$, $\kappa(m + 1 - \delta)$, $m \ge 0$, give $\tfrac{\kappa}{2}(\zeta(-1, \delta) + \zeta(-1, 1 - \delta)) = -\tfrac{\kappa}{2}B_{2}(\delta)$ (CCR zero points have the opposite sign to CAR ones); at $\delta = 0$ the zero mode contributes nothing and the towers $\kappa m$, $m \ge 1$, give $\kappa\zeta(-1, 1) = -\kappa/12 = -\tfrac{\kappa}{2}B_{2}(0)$. Since $16n_{g} \equiv 0 \pmod 8$, $16n_{g} + c_{B} \equiv 0 \pmod{24}$ needs $c_{B} = 8m$ and then $2n_{g} + m \equiv 0 \pmod 3$, that is $n_{g} \equiv m \pmod 3$.

\emph{(v)} The past cone holds the postulates (P), (Q), (R), (R$_{\Lambda}$), (N$_{+}$), the window reading, J3, the slot-module hypothesis, the Krein premise, the rung-unit premise, the indifference premise, the dark-matter premises P2, P3, R1-R3, H1 and the four foundation postulates; the generation-number result gives the slot-module premise and anomaly freedom for $n$ copies, and each of the others is stated per mode, array, generator, composite, field or tower and names no count of generations or of arrays, so it holds in $\mathcal{M}_{1}$ exactly when in $\mathcal{M}_{3}$; the condition reads $e^{2\pi J\cdot 16/24} = e^{4\pi J/3} \ne 1$ against $e^{2\pi J\cdot 48/24} = 1$.

## lay
The series pictures each light ray of a black hole's horizon as carrying a sea of fermion modes, sixteen sets per generation of matter. After one recurrence window of the horizon's clock every mode returns with its sign flipped, as the series assumes. Whether the sea as a whole returns exactly as the sign-flip operator, with no leftover phase, depends on its zero-point energy, which the series has fixed: each mode set contributes one twenty-fourth of a turn. So the sea returns exactly only if the number of mode sets is a multiple of 24, which with sixteen per generation needs the number of generations to be a multiple of three. This result proves the sign-flip on finite windows and the leftover phase from the series' zero of energy, shows by two models (one and three generations) that the series' assumptions neither require nor forbid it, and works out what changes without the right-handed neutrino. The series' current assumption about horizon channels counts the force-carrying fields as collective motions of the same fermion modes, so they change nothing; only if they were counted as separate modes, against that assumption, would they change the condition. That the number of generations is a multiple of three has been argued before by other routes, from anomalies.

## one-liner
On every finite window an array's one-window flow is its grading, and the window reading adds $-\kappa/24$ per array, so the light-ray sea's one-window evolution is $e^{2\pi Jn/24}\Gamma$: it equals the grading exactly when $24 \mid n$, a strengthening of (Q)'s parity clause not implied by (Q), the KMS condition, (N$_{+}$) or the window reading and independent of the cone's postulates (two models), giving $n_{g} \equiv 0 \pmod 3$ on sixteen components per generation (not $n_{g} = 3$), $n_{g} \equiv 0 \pmod 8$ without the neutral singlet, and, only in a reading outside J3 that adds integer-weight components, a mod-$8$ condition on them.
