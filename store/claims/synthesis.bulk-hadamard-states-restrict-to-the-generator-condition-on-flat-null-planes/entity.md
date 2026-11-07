---
id: synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes
kind: claim
version: 5
title: 'Flat-field Hadamard states meet the generator condition on null planes'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, car-algebra, null-directions, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: premises repointed to synthesis.canonical-part-of-a-spinor-on-a-null-plane (the algebra it cites), in place of the light-ray and slot-module results; notation declaration
  version: 4
  source: maintainer pass 2026-11-07
- name: Claude Opus 5.5
  role: premises repointed to the premise-free results split out of the null-energy and collapse results
  version: 5
  source: maintainer pass 2026-11-07
- name: Claude Opus 5.5
  role: unit conventions per Leon's rulings of 7 November 2026 (R2, R4)
  version: 5
  source: maintainer pass 2026-11-07 (unit rulings)
review: draft
about:
- obj.hawking.continuum-mode-space
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.canonical-part-of-a-spinor-on-a-null-plane@1
  - synthesis.null-vacuum-on-a-horizon-generator@1
  - field-theory.second-quantisation@5
  - synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state@5
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.imported-null-plane-restriction-of-free-fields-is-mass-independent@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_good_part_projector_drops_the_mass
- kind: check
  ref: check.py::check_shell_density_of_the_good_part_is_one_half
- kind: check
  ref: check.py::check_restricted_vacuum_is_the_null_vacuum_symbol
- kind: check
  ref: check.py::check_shell_energy_bounds_give_decay_at_both_ends
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state
  - synthesis.n-plus-null-ground-state
  - synthesis.attachment-conformal-energy-is-generated-by-z
extraction:
  maintainer_pass_unit_rulings:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Leon''s rulings R1-R4 of 7 November 2026, folded into version 5 of this pass: R2, R4: W_0 and the restricted kernels written with I_4 (u - v + I_4 0), the Fourier integrals with I_4, and the plane-wave phases of the bulk kernels with the right unit e^{-p.(x - x'')I_4}, the numerator (p + m_0)e_0 not being even; no bare i remains, declaration removed'
  maintainer_pass_clause_split_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5, at Leon''s decision of 7 November 2026: it cited synthesis.positive-null-energy-gives-r-premises only for its (i) (the null vacuum and its kernel W_0), which is now synthesis.null-vacuum-on-a-horizon-generator (ii); the uses edge, the claimrefs and the check''s premise calls are repointed to it, and the pin to the microlocal theorem moves to its version 5 (same split, statement unchanged), so this result no longer inherits Premise (N+) through them. Statement, proof argument and checks otherwise unchanged; no assumes edge added or removed; notation as the sweep left it.'
  open_problem: op.qft-on-gtg-fields
  note: >-
    Answers the second attack line of op.qft-on-gtg-fields (derive the generator form of the Hadamard
    condition from a field theory on the gravitational field) on the flat field: the restriction of bulk
    Hadamard states to the generator algebra, which the stored microlocal theorem records as missing, is
    computed for the Dirac field on every null plane, the transverse labels forming the multiplicity space K
    (no s-wave reduction needed). The vacuum of every mass restricts to the null vacuum tensored with the
    identity on K, because the canonical projector removes the mass term and the shell density in the null
    momentum is one half for every mass and transverse momentum; Hadamard states (smooth differences, imported)
    then have smooth generator remainders, hence the generator microlocal condition and, by the stored theorem,
    the local form of (N+) at every point. This extends the stored statement that on Minkowski local horizons
    (N+) is the choice of the attachment's vacuum: the massless restriction is the attachment's case, the
    massive one is the standard light-front result (the null-plane restriction of the free vacuum is
    independent of the mass), reproduced here in the store's generator conventions; the new content is the
    link to (N+): the field theory's state class, not a choice of vacuum, gives the local form. The
    restriction to the plane is not a pullback in Hormander's sense (the wave-front set of the vacuum kernel
    meets the conormal of N x N along the generators); it is defined by the momentum-space computation with
    transverse smearing. Bears on op.einstein-from-the-field-theory: it supplies the short-distance
    content of (R_loc) on the flat field from the field theory; at a point with nonzero field strength the
    same conclusion follows given the adopted premise (HS), synthesis.hadamard-scaling-limit-premise (marked
    note in the formal level; this result does not use it). Transport-absent. Literature: light-front
    quantisation and the mass independence of the null-plane restriction (H. Leutwyler, J. R. Klauder and
    L. Streit, Nuovo Cimento A 66 (1970) 536; A. C. Wall, Phys. Rev. D 85 (2012) 104049, for scalar fields),
    now the imported Fact synthesis.imported-null-plane-restriction-of-free-fields-is-mass-independent; the
    vacuum two-point kernels of the
    free Dirac field, standard; B. Kay and R. Wald, Phys. Rep. 207 (1991) 49, on restrictions to Killing
    horizons, cited from memory and not used.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01: a uses edge to the imported light-front Fact (Leutwyler-Klauder-Streit, Wall) replaces the citation from memory in the proof; the pin to the microlocal generator theorem moves to its version 3 (an added note); a marked note in the formal level records that the adopted premise (HS), synthesis.hadamard-scaling-limit-premise, carries (iii) to points of nonzero field strength. Statement, proof and checks otherwise unchanged; the result does not use (HS).'
  flags:
  - 'flat field only: the plane is a local Rindler horizon of hb = 1, Omega = 0; on a field with nonzero field strength the restriction of the Hadamard parametrix to a null surface is not computed'
  - 'transverse profiles of compact support: the K-components are taken for compactly supported transverse profiles'
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4, at Leon''s decision of 7 November 2026: the result cited the light-ray result and the slot-module result only for the algebra of the canonical part on a null plane (the projector Lambda(m) = (1 + e0 e3)/2 = m k/4, the flux identity, the two-channel image, and that mass terms reach only the constraint), which is now the separate result synthesis.canonical-part-of-a-spinor-on-a-null-plane; the two uses edges are replaced by one to it, and the claimrefs and the check''s premise calls follow. So this result no longer inherits Premise (Q), the slot-module hypothesis or the dark-matter counting premises. Statement, proof argument and checks otherwise unchanged; no assumes edge added or removed. Notation: the bare i of the scalar Fourier analysis and of the null-vacuum kernel W_0 stays (declared under outside_ga, complex-analysis), as in the stored null vacuum.'
  maintainer_pass_hs_bound:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 2 -> 3, at Leon''s decisions of 2 November 2026 (Hadamard scaling bound): (HS), synthesis.hadamard-scaling-limit-premise, is now a theorem (version 4); wording that called it an adopted premise (formal note, technical, proof) now names it as the theorem, formerly a premise. What this entity asserts is unchanged.'
---

## formal
Units $\hbar = c = 1$. On the flat gravitational field ($\hb = 1$, $\Omega = 0$; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) let $N = \{x_{0} + \lambda k + y\}$ be a null plane with generators along $k = e_{0} + e_{3}$, $y$ in the span of $e_{1}, e_{2}$, $m = e_{0} - e_{3}$, and $\Lambda(m) = \tfrac12(1 + e_{0}e_{3})$ the projector onto the canonical part on $N$ (Theorem \claimref{synthesis.canonical-part-of-a-spinor-on-a-null-plane}), with two-channel image $V_{\Lambda}$. For the free Dirac field of mass $m_{0} \ge 0$ (Proposition \claimref{field-theory.second-quantisation}) put $\psi_{N}(\lambda, y) = \sqrt{2}\,\Lambda(m)\psi(x_{0} + \lambda k + y)$ and $K = L^{2}(\R^{2}, d^{2}y)\otimes V_{\Lambda}$.
\begin{enumerate}
\item[(i)] \emph{(The plane carries the generator CAR; computed.)} $\{\psi_{N}(\lambda, y), \psi_{N}^{*}(\lambda', y')\} = \delta(\lambda - \lambda')\,\delta^{2}(y - y')\,\Lambda(m)$: the continuum mode space $\CAR(L^{2}(\R, d\lambda)\otimes K)$ of Definition \claimref{obj.hawking.continuum-mode-space}, with $u = \lambda$ an affine parameter on each generator.
\item[(ii)] \emph{(Every vacuum restricts to the null vacuum; computed exactly.)} $\Lambda(m)(p \pm m_{0})e_{0}\Lambda(m) = \ip{p}{k}\Lambda(m)$ for every vector $p$ and mass $m_{0}$, the positive-energy shell has $\ip{p}{k} > 0$, and in the variables $(\ip{p}{k}, p_{\perp})$ the compressed shell density is $\tfrac12$ for every $m_{0}$ and $p_{\perp}$. Hence for every $m_{0} \ge 0$ the bulk vacuum restricts (the restriction defined by this momentum-space computation with transverse smearing, not as a pullback of distributions, since the wave-front set of the vacuum kernel meets the conormal of $N\times N$ along the generators) to $\omega_{m_{0}}(\psi_{N}^{*}(v)\psi_{N}(u)) = W_{0}(u, v)\otimes\id_{K}$, $W_{0}(u, v) = \tfrac{I_{4}}{2\pi}(u - v + I_{4}0)^{-1}$: the null vacuum $\omega_{0}$ of Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii) on every generator, in every affine parameter.
\item[(iii)] \emph{(Hadamard states give the generator condition; proved, given the imported fact.)} If $\omega$ is a gauge-invariant quasi-free state of the mass-$m_{0}$ field whose two-point kernel differs from $\omega_{m_{0}}$'s by a smooth kernel (a Hadamard state; Fact \claimref{synthesis.imported-microlocal-hadamard-condition}), its restriction to $N$ has smooth remainder $R = W_{\omega} - W_{0}\otimes\id_{K}$ on $J\times J$ for every interval $J$ of every generator, in each $K$-component with compactly supported transverse profiles. So it satisfies the microlocal spectrum condition on every such $J$ and, by Theorem \claimref{synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state}(ii), its scaling limit at every point of $N$ is $\omega_{0}$: the local form of (N$_{+}$) holds at every point of every local Rindler horizon of the flat field, with no stationarity, temperature or symmetry assumed.
\item[(iv)] \emph{(What it does not give.)} Not the ground-state clause of (N$_{+}$) (every Hadamard state passes, the stored affine-KMS states included), not (Loc), and not the statement on a field with nonzero field strength.
\end{enumerate}
\emph{Note (nonzero field strength; added 1 November).} At points of a gravitational field with nonzero field strength the conclusion of (iii) is carried by Theorem \claimref{synthesis.hadamard-scaling-limit-premise}, (HS) (adopted as a premise on 1 November, proved on 2 November): a gauge-invariant quasi-free Hadamard Dirac state there scales to the massless vacuum of the flat field, also on the generators of every local Rindler horizon through the point, and by (ii) at $m_{0} = 0$ that vacuum restricts to the null vacuum; so, by (HS), such states have the local form of (N$_{+}$) at every point of every local Rindler horizon. This result does not use (HS); it is proved on the flat field only. The mass independence in (ii) is the standard light-front statement (Fact \claimref{synthesis.imported-null-plane-restriction-of-free-fields-is-mass-independent}), here computed in the store's generator conventions.

## technical
The stored horizon results pose, on a single horizon generator, the analogue of the Hadamard condition, the standard requirement that physical states look like the vacuum at short distances, and show that it gives the local form of the null ground-state premise (N$_{+}$) at every point. What was missing is the link to the field theory: whether the field theory's own states, the Hadamard states of a four-dimensional Dirac field, satisfy the generator condition.

On the flat gravitational field this link is computed. On a null plane the canonical part of the Dirac field, its image under $\Lambda(m)$, carries the generator algebra with the transverse directions as multiplicity labels. The projector removes the mass term from the vacuum kernels, and in the null momentum the shell density is exactly one half for every mass and transverse momentum, so the vacuum of every mass restricts to the null vacuum on every generator (a standard light-front result, here in the store's generator conventions). A gauge-invariant quasi-free Hadamard state differs from that vacuum by a smooth kernel, which stays smooth when restricted to the plane; so it satisfies the generator condition on every interval and has the local form of (N$_{+}$) at every point of every local Rindler horizon.

It does not give the ground-state clause, since every Hadamard state passes, nor (Loc), and it is proved only where the gravitational field strength vanishes; at points of nonzero field strength the same conclusion follows from the scaling-limit theorem (HS), formerly a premise, which this result does not use. Transport-absent.

## lay
The series' account of horizon temperature rests on an assumption that, very close to any point of a horizon, the quantum field looks like empty space. This result checks that assumption against the field theory in empty flat space. On any light-like plane, the field's vacuum, whatever the particle's mass, looks exactly like the empty state that the assumption names, and every state that physicists regard as reasonable, one that differs from the vacuum only smoothly, looks like it at short distances too. So in flat space the assumption's short-distance part is a consequence of the field theory, though not the part that says the state is the vacuum everywhere, and not yet in a gravitational field.

## one-liner
If the gravitational field is flat, the Dirac vacuum of every mass restricts on every null plane to the null vacuum, and every gauge-invariant quasi-free Dirac state differing from it by a smooth kernel (a Hadamard state) restricts to one satisfying the generator analogue of the microlocal condition, so it has the local form of (N$_{+}$) at every point of every local Rindler horizon; not the ground-state clause, and not where the field strength is nonzero.
