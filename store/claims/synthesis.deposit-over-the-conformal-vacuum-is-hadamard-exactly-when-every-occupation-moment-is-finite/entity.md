---
id: synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite
kind: claim
version: 3
title: 'A diagonal deposit is Hadamard exactly when its moments are finite'
status: proved
region: synthesis
subject: quantum-fields
tags: [car-algebra, horizons, thermal-premises, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-deposit-state
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
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise@3
  - synthesis.imported-microlocal-hadamard-condition@2
  - hawking.i-state@3
  - field-theory.second-quantisation@5
  - synthesis.imported-gtg-dictionary@1
  - synthesis.weyl-flat-fields-need-no-scaling-limit-premise-and-robertson-walker-generators-see-the-schwarzian@6
  - synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness@1
  - synthesis.imported-bochner-theorem-moment-lemma-and-whitney-even-functions@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_massless_shell_projectors
- kind: check
  ref: check.py::check_coincidence_differences_have_one_sign
- kind: check
  ref: check.py::check_thermal_profile_has_every_moment
- kind: check
  ref: check.py::check_power_tail_profile_has_finite_shot_term_but_not_every_moment
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.attachment-transport-is-flat-only-where-weyl-vanishes
  - synthesis.hadamard-scaling-limit-premise
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The plane-wave phases of the two-point kernels and the frequency representation phi(tau) = int e^{-I_4 nu tau} d mu, with I_4 phi'', now use the field theory''s unit I_4 (numbers read in span{1, I_4}, as the proof''s unit phases c + s I_4 already were); no bare i remains.'
  open_problem: op.deposit-state-is-hadamard
  note: >-
    Step (1) of op.deposit-state-is-hadamard for the deposit the store states (a homogeneous quasi-free
    state of the fermion modes on the descent slice, the vacuum plus quanta). The criterion itself is
    standard (a homogeneous quasi-free state of a free field is Hadamard when its occupation numbers
    decrease faster than every power), carried to the descended field by conformal covariance; the new
    content is its application to the stored deposit and its comparison with the stored shot-noise data.
    The stored bound uses the number of quanta and their energy spread (the zeroth to second moments of
    the occupation profile); the Hadamard condition needs every moment. So the number of quanta does not
    decide the Hadamard property: the thermal profile has every moment, a power tail with the same finite
    shot term does not. The result is stated here once; the massive case shows the same from the side of
    the reference vacuum (the instantaneous vacuum, a finite number of quanta from an adiabatic state, is
    not Hadamard; synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard). The tracial state (occupation one half at every momentum,
    the inverse-temperature-zero limit of the thermal profile) has every moment infinite and is not
    Hadamard: the descent must not be read as producing it. Hypotheses: the descended field near the
    descent is of Robertson-Walker form with smooth positive scale factor, as for a descent of radiation
    type, which is conformally a regular wall with Cauchy slices from any collar (synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state); the deposit is set on such a collar. A kink in the scale factor makes the derived metric
    non-smooth and the Hadamard condition undefined there. The conformal-covariance lemma (null
    geodesics and their covectors, wave-front sets) and the scaling limit of Hadamard states on
    Weyl-flat fields are proved in synthesis.weyl-flat-fields-need-no-scaling-limit-premise-and-robertson-walker-generators-see-the-schwarzian, a premise here; clause (v) here
    extends that scaling limit to non-Hadamard deposits with a finite number of quanta. With the adopted
    premise that the deposit is Hadamard, this result says which occupation profiles over the conformal
    vacuum the premise admits; it does not say which is deposited. The thermal deposit is diagonal in
    the conformal vacuum's quasi-particle number basis, so the parity average of any of those modes
    (singularity.descent-parity-average) leaves it unchanged. On the Weyl-flat field the conformal
    vacuum is the state the attachment transports (synthesis.attachment-transport-is-flat-only-where-weyl-vanishes,
    type O), an identification argued and not used. Transport-absent for the criterion; the
    conformal-vacuum reading is transport-convenient. Standard results imported as Facts: conformal
    covariance of the massless Dirac field (weight 3/2) and local conformal flatness, synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness; Bochner's theorem and the moment lemma for positive Fourier transforms (E. Lukacs,
    Characteristic Functions, 1970, ch. 2), synthesis.imported-bochner-theorem-moment-lemma-and-whitney-even-functions.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01 (deposit-state imports): uses edges to the imported Facts on conformal covariance and on Bochner''s theorem and the moment lemma replace the citations from memory, and a uses edge to the Weyl-flat result (version 2) records the conformal-covariance lemma and scaling limit it proves; pins move to the microlocal Fact version 2 and the shot-noise result version 3 (added notes, not used here). Statement, proof steps and checks otherwise unchanged.'
  flags:
  - 'massless Dirac field only: a massive field has no conformal vacuum; no massive analogue of the moment criterion is claimed'
  - 'deposit diagonal in the plane-wave quasi-particle modes of the conformal vacuum, occupations independent of helicity; particle-antiparticle pair coherences, helicity coherences and coherences between momenta are not treated'
  - 'descended field of Robertson-Walker form with smooth positive scale factor near the descent (as for a descent of radiation type): a stated hypothesis, not derived; on the Kasner branch the field is Weyl-curved and the result does not apply'
---

## formal
Units $\hbar = c = 1$. \emph{Hypothesis:} the descended field near the descent is the Weyl-flat gravitational field on flat spacetime $\hb(b) = b/a(t)$, $t = x\cdot e_{0}$ the conformal time, $a$ smooth and positive on the collar where the deposit is set (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}; derived metric $a(t)^{2}$ times the flat one, a Robertson-Walker field, read through Fact \claimref{synthesis.imported-gtg-dictionary}), as for a descent of radiation type. Let $\psi$ be the massless Dirac field of Proposition \claimref{field-theory.second-quantisation} on it, $\chi = a^{3/2}\psi$ the conformally rescaled field, which solves the flat massless Dirac equation, and $\omega_{c}$ the conformal vacuum, the flat massless vacuum of $\chi$. A \emph{diagonal homogeneous deposit} is a gauge-invariant quasi-free state $\omega$ diagonal in the plane-wave quasi-particle modes of $\omega_{c}$ (no particle-antiparticle pair coherence, no coherence between momenta or helicities), with particle and antiparticle occupations $n_{+}(p), n_{-}(p) \in [0, 1]$ per comoving momentum $\vec p$ and helicity, $p = |\vec p|$; write $M_{k} = 2\int d^{3}p\,p^{k}\,(n_{+} + n_{-})$ and $R^{(\pm)} = \mathcal{G}_{\omega}^{(\pm)} - \mathcal{G}_{\omega_{c}}^{(\pm)}$ for the remainders of both orderings (Fact \claimref{synthesis.imported-microlocal-hadamard-condition}(b)).
\begin{enumerate}
\item[(i)] \emph{(Reference; standard.)} $\omega_{c}$ is Hadamard.
\item[(ii)] \emph{(Criterion; the standard flat criterion carried by conformal covariance; the converse given the moment lemma.)} If $M_{k} < \infty$ for every $k$, both remainders are smooth on $M \times M$ and $\omega$ is Hadamard. Conversely, if $\omega$ is Hadamard, every $M_{k}$ is finite. More precisely, $M_{0}, \dots, M_{j} < \infty$ gives remainders of class $C^{j}$, and a remainder of class $C^{2m+1}$ along a timelike line gives $M_{2m+1} < \infty$.
\item[(iii)] \emph{(The thermal deposit; proved.)} For the Fermi-Dirac profile $n_{\pm} = (e^{p/T} + 1)^{-1}$ (Theorem \claimref{hawking.i-state}; $T = a_{d}T_{d}$ comoving), $M_{k} \le 16\pi\,(k + 2)!\,T^{k + 3}$ for every $k$, so the thermal deposit is Hadamard; so is every diagonal deposit whose profile is bounded by $C_{N}(1 + p/T)^{-N}$ for every $N$.
\item[(iv)] \emph{(The shot-noise data do not decide it; proved.)} The profile $n_{\pm} = (1 + p/T)^{-6}$ has finite number, mean energy $\tfrac32 T$ and energy spread $c = \langle\omega^{2}\rangle/\langle\omega\rangle^{2} = \tfrac83$, so the shot term of Proposition \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise}(iv) is finite, while $M_{k} = \infty$ for every $k \ge 3$: its remainders are of class $C^{2}$ and not of class $C^{3}$ along a timelike line, and it is not Hadamard.
\item[(v)] \emph{(A finite number alone, Hadamard or not; proved.)} If $M_{0} < \infty$, then $|R^{(\pm)}(x, y)| \le (2\pi)^{-3}M_{0}\,a(x)^{-3/2}a(y)^{-3/2}$, a bounded remainder, so at every point $x_{0}$ the scaling limit of $\omega$ (weight $\tfrac32$ per leg) equals that of $\omega_{c}$, the flat massless vacuum in the local inertial coordinates $a(t_{0})(x - x_{0})$, even when $\omega$ is not Hadamard.
\end{enumerate}
So under the hypothesis the stored thermal deposit is a Hadamard state on the descent's collar; the number of quanta controls the scaling limit, the first two moments the shot noise, and the whole ultraviolet tail the Hadamard class.

## technical
The question is whether the state the descent deposits on the fields is a Hadamard state, the class on which a renormalised stress tensor exists and which the horizon premises need. The store describes the deposit as the vacuum plus quanta, with a bound on its fluctuations in terms of the number of quanta and their energy spread.

The result assumes that the descended field near the descent is of Robertson-Walker form with a smooth scale factor, as for a descent of radiation type; a kink in the scale factor would make the Hadamard condition undefined there. It treats the massless Dirac field, which is conformally the flat one, so the conformal vacuum is Hadamard, and deposits diagonal in that vacuum's particle modes, with no particle-antiparticle pair coherence. Such a deposit is Hadamard exactly when every moment of its occupation profile is finite. This is the standard flat-space criterion, carried over by conformal covariance: sufficiency by differentiating under the integral, necessity because odd time derivatives at coincidence weigh particles and antiparticles with the same sign, so their finiteness forces the moments.

The thermal profile decays exponentially and has every moment, so the thermal deposit is Hadamard. A profile falling as the sixth inverse power has a finite shot term, the kind of data the stored bound uses, yet infinite moments from the third on: it is twice but not three times differentiable at coincidence and not Hadamard. So the number of quanta does not decide the Hadamard property. A finite number alone still makes the remainder bounded, so the deposit looks like the vacuum at short distances even when it is not Hadamard. Transport-absent.

## lay
When the universe's earlier phase handed its contents to the later one, it left the quantum fields in some state. Physics in a gravitational field needs that state to be of a particular well-behaved kind, called Hadamard, which roughly means it looks like empty space at very short distances in a smooth way. This result shows, for massless spin-one-half particles and assuming the young universe was uniform and expanding smoothly, that a thermal hand-over, the kind the series uses, is of that kind. It also shows that the series' earlier calculation of how much the hand-over can disturb things, which uses only how many particles there are and how their energies spread, cannot settle the question: what matters is how fast the number of particles falls off at high energy.

## one-liner
On a descended field of Robertson-Walker form with smooth scale factor (a stated hypothesis, as for a descent of radiation type), a homogeneous deposit of the massless Dirac field diagonal in the conformal vacuum's quasi-particle modes (no pair coherence) is Hadamard exactly when every moment of its occupation profile is finite (the standard criterion, carried by conformal covariance); the thermal deposit is Hadamard, the shot-noise data (number and energy spread) do not decide it (a $(1 + p/T)^{-6}$ tail has them and is not), and a finite number alone gives a bounded remainder and the vacuum's scaling limit.
