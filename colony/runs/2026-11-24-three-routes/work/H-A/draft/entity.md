---
id: synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none
kind: claim
version: 1
title: '(CW) on a radiation-type descent: a floor under the Dirac deposit, no selection'
status: proved
region: synthesis
subject: quantum-fields
tags: [car-algebra, no-go, pairing-and-bogoliubov, mirror-sector]
proposed_by:
  kind: ai
  session: 2026-11-24-three-routes
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-three-routes
review: draft
outside_ga:
  kind: complex-analysis
  why: "Clause (iv)(c), the value exp(-pi k^2/mu) of the transition probability, uses the asymptotic form and the connection formula of Weber's parabolic cylinder functions and the reflection formula of the Gamma function, with numbers in span{1, I}, I the pseudoscalar unit of the stored two-level form. Everything else is computed with the Clifford product of Cl(1,3) and Cl(3,0) and scalar calculus; the two-point kernels of clause (v) are the stored Hadamard results' language."
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard@4
  - synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state@3
  - synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard@3
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_wall_reflection_and_charge_conjugation_in_the_spacetime_algebra
- kind: check
  ref: check.py::check_exactly_two_reflections_of_bloch_vectors_preserve_the_mode_equation
- kind: check
  ref: check.py::check_invariant_states_are_a_disk_per_mode_and_the_flow_is_isometric
- kind: check
  ref: check.py::check_late_time_vacuum_series_is_on_the_invariant_circle_to_every_order
- kind: check
  ref: check.py::check_invariant_circle_occupations_and_the_minimum
- kind: check
  ref: check.py::check_pair_bound_without_isotropy
- kind: check
  ref: check.py::check_weber_form_and_transition_probability_bookkeeping
lineage:
  motivated_by:
  - synthesis.hadamard-deposit-premise
  - synthesis.cold-mirror-needs-non-equilibrium-descent
  - dark-matter.premise-cpt-covariance
extraction:
  open_problem: op.deposit-state-is-hadamard
  note: >-
    Tests one route to deriving (HD): read the mirror as the far side of the radical-normal wall (the other sign of
    conformal time) and require the deposited state to be invariant under a conjugation across the wall, Hypothesis
    (CW). The result is conditional on three named hypotheses, none a premise of the store: the radiation-type
    descent, the doubling (DF) and (CW); adopting any of them is a decision for the maintainer. Kill conditions
    registered before computing: no invariant quasi-free state or a continuum of them (fired: a disk of Bloch
    vectors per mode, so (CW) selects no state); a power-law tail of the invariant state's occupation (not fired
    for the state of least occupation, whose tail is Gaussian; fired for another invariant state, the wall-instant
    vacuum, with the stored tail $\mu^{2}/(16k^{4})$); a contradiction with a stored result (no stored theorem is
    contradicted; a tension with the series' cold mirror is recorded in the Reading, argued); for the massless field
    the invariant state is not the conformal vacuum (fired for (CW) alone, every stationary charge-symmetric state
    being invariant; not fired once purity, the orientation and least occupation are added). What is proved and
    what is not: clauses (i) to (iv)(b), (v)(a), (vi) and (vii) are proved here, with the exact checks; (iv)(c) is proved
    given classical facts on Weber functions cited from memory, and confirmed by a numerical integration that is
    not part of the check; (v)(b) holds given the imported Fact on adiabatic states, with the identification of the
    late-time vacuum with that Fact's class made as the stored massive result makes it; the statements that the tracial state (for $\mu > 0$) and the Fock states of the energy-reversing
    reflection are not Hadamard are argued; the Reading is argued. The class of states of clauses (i) to (vi) is
    homogeneous, isotropic, diagonal in helicity with equal vectors in the two helicities, and charge-symmetric;
    isotropy is needed because the antilinear conjugation pairs momentum $\vec k$ with $-\vec k$, and clause (vii)
    gives what holds without it (a bound on each pair, not on each sector). States outside the class only enlarge
    the invariant set. The check of the Weber clause tests the exponent arithmetic and the reduction to Weber's
    equation only, not the special-function facts. The background is prescribed: the result filed alongside on the
    trace anomaly (synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall) shows that (RD) and
    (DF) do not hold together with its hypotheses (A) and (E). Ledger: transport-absent. Prior art: L. Boyle, K. Finn and N. Turok, Phys. Rev. Lett. 121 (2018)
    251301 (from memory) and arXiv:1803.08930, Eqs. (3.48), (3.49), (5.13), (5.15), (5.16) (locators confirmed in
    review against the arXiv text): the free function left by CPT invariance, its fixing by least particle number
    and energy, the profile and the number density are theirs; no priority is claimed for clauses (iv)(b), (iv)(c) and (vi). The Landau-Zener
    probability is C. Zener, Proc. R. Soc. A 137 (1932) 696 (from memory); Weber functions from Whittaker and
    Watson, sections 16.5 to 16.52 (from memory).
  flags:
  - 'conditional on three named hypotheses that are not premises of the store: the radiation-type descent, the doubling (DF) of the conformal chart across the wall, and (CW)'
  - 'beyond one flat chart: none; the doubled field is the one flat chart with both signs of the conformal time, the gauge field hb(b) = b/a changing sign with a across the wall, where it is not invertible'
  - 'clause (iv)(c) rests on classical special-function facts cited from memory'
  - 'the Reading (mirror, obstructions) is argued and is not part of the statement'
  - 'prescribed background: (RD) and (DF) are not jointly available with the hypotheses (A) and (E) of the trace-anomaly result filed alongside'
  - 'clauses (i) to (vi) are for the isotropic class; clause (vii) is the statement without isotropy'
---

## formal
Units $\hbar = c = 1$. \emph{Hypotheses.} (RD) The descent is of radiation type: the descended gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) is $\hb(b) = b/a(\eta)$ with $\eta = x\cdot\gamma_{0}$ the conformal time and $a = a'\eta$, $a' > 0$ constant, for $\eta > 0$; its wall $\eta = 0$ is the radical-normal tame wall of Theorem \claimref{synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state}(iv). (DF) The far side of the wall is the region $\eta < 0$ of the same chart with the same formula, so that the rescaled Dirac field $\chi$ ($\chi = a^{3/2}\psi$ for $\eta > 0$), an even multivector field of $\Cl(1,3)$, obeys $\nabla\chi\,I\sigma_{3} = M\chi\gamma_{0}$ with $M = \mu\eta$, $\mu = ma' \ge 0$, for all $\eta$: the mass function is odd across the wall. (CW) The deposited state is invariant under the conjugation across the wall, in one of the two senses of (i). Each momentum $\vec k$ ($k = |\vec k|$) and helicity sector is the two-level system $Iu' = Hu$, $H = M\sigma_{3} + k\sigma_{1}$, of Theorem \claimref{synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard}, with Bloch equation $s' = -2I(h\wedge s)$, $h = k\sigma_{1} + M\sigma_{3}$, in the Pauli algebra $\Cl(3,0)$ with pseudoscalar $I$; write $\omega = |h|$, $\hat h = h/\omega$, $c = k/\omega$, $\sigma = M/\omega$, $\delta = \mu/\omega^{2}$, $\nu = k^{2}/\mu$. The states considered in (i) to (vi) are the gauge-invariant quasi-free states that are homogeneous, isotropic, diagonal in helicity with the same vector in the two helicities, and charge-symmetric: one vector $v_{k}(\eta)$ with $|v_{k}| \le 1$, depending on $k = |\vec k|$ only and the same in every sector of that $k$, solving the Bloch equation, with one-particle density $\tfrac12(1 + v_{k})$, a Fock state exactly when $|v_{k}| = 1$ for all $k$; the occupation of $v$ over a Fock reference $r$ is $n = \tfrac12(1 - v\cdot r)$ per sector. The wall-instant vacuum is the solution with $v(0) = \sigma_{1} = \hat h(0)$, the tracial state is $v = 0$. Clause (vii) drops isotropy. \emph{The background is prescribed.} (RD) and (DF) fix the gravitational field, and the Dirac field is a test field on it; with the expected stress of a Hadamard state of the series' content as the source, the exact radiation field does not reach the wall (the result filed alongside, synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall, given its hypotheses (A) and (E)), so (RD), (DF), (A) and (E) do not hold together and the present result is for a prescribed background, not a self-consistent one.
\begin{enumerate}
\item[(i)] \emph{(The conjugations; proved.)} (a) In $\Cl(1,3)$ the reflection in the wall, $(W\chi)(\eta, \vec x) = \gamma_{0}\,\chi(-\eta, \vec x)\,\gamma_{0}$, the outermorphism of $x \mapsto -\gamma_{0}x\gamma_{0}$ applied to the values and the argument, maps solutions to solutions exactly when $M$ is odd; it commutes with the right unit $I\sigma_{3}$ and with the mass part of the mode generator and anticommutes with its momentum part. The charge conjugation $c\chi = \chi\sigma_{1}$ ($\sigma_{1} = \gamma_{1}\gamma_{0}$) anticommutes with the right unit and maps solutions of momentum $\vec k$ to solutions of momentum $-\vec k$ for every $M$; so $\theta = cW$ is an antilinear symmetry for odd $M$. (b) On Bloch vectors, for $\mu > 0$, the maps $s(\eta) \mapsto Os(-\eta)$, $O$ orthogonal, that preserve the Bloch equation for every $k$ are exactly two: $O_{A}v = -\sigma_{3}v\sigma_{3}$, the reflection along $\sigma_{3}$, and $O_{B}v = \sigma_{3}v\sigma_{3}$, the half turn about $\sigma_{3}$. $O_{B}$ is induced by $W$ acting as an automorphism (on a sector $W$ is the unitary $\sigma_{3}$ up to a phase); it reverses the energy, sending the wall-instant vacuum $\sigma_{1}$ to $-\sigma_{1}$. $O_{A}$ is induced by $\theta$ acting as an automorphism (an antiunitary map of the one-particle space, which carries each sector of momentum $\vec k$ to a sector of momentum $-\vec k$), and, within each sector, by $W$ followed by the exchange of particles and holes, $\tfrac12(1 + s) \mapsto \tfrac12(1 - s)$; it keeps $\sigma_{1}$. For the isotropic class the two give the same condition, sector by sector. For $\mu = 0$ the same maps $W$ and $\theta$ induce the same $O_{B}$ and $O_{A}$ (there the equation has further symmetries, the chiral rotations, and with them further reflections, which fix or reverse $\sigma_{1}$ in the same way). (c) A conjugation that fixes every point and reverses the energy (the type of the stored conjugation of Premise \claimref{dark-matter.premise-cpt-covariance}, which is not used here) acts on Bloch vectors as $s \mapsto -s$ (between the sectors of momenta $\vec k$ and $-\vec k$, being antilinear), exchanges no sides of the wall, and has the tracial state as its only invariant state in the isotropic class; followed by the exchange of particles and holes it is the identity.
\item[(ii)] \emph{(Invariant states; proved.)} A state of the class is $O_{A}$-invariant exactly when $v_{k}(0)\cdot\sigma_{3} = 0$ for every $k$: a disk of Bloch vectors per sector, a circle of Fock states, containing with each $v$ every $tv$, $-1 \le t \le 1$. It is $O_{B}$-invariant exactly when $v_{k}(0) = t_{k}\sigma_{3}$; the two Fock states among these have occupation exactly $\tfrac12$ over the wall-instant vacuum at the wall. The only state invariant under both is the tracial state. So an invariant state exists and is not unique, for either conjugation and every $\mu \ge 0$.
\item[(iii)] \emph{(Massless field; proved.)} For $\mu = 0$ the stationary states of the class are $v = t(k)\sigma_{1}$, $-1 \le t \le 1$, the charge-symmetric deposits diagonal over the conformal vacuum $\sigma_{1}$, with occupation $\tfrac12(1 - t)$; every one of them is $O_{A}$-invariant, the conformal vacuum, the filled sea $-\sigma_{1}$, the tracial state and the thermal states at every temperature included. The other $O_{A}$-invariant states, $v(0) = a\sigma_{1} + b\sigma_{2}$ with $b \ne 0$, are not stationary. The $O_{A}$-invariant stationary Fock states are the conformal vacuum and the filled sea. The same holds with the conjugation composed with any chiral rotation.
\item[(iv)] \emph{(Massive field, $\mu > 0$.)} (a) (Proved.) There is exactly one solution $s_{\mathrm{out}}$ with $s_{\mathrm{out}} - \hat h \to 0$ as $\eta \to +\infty$, the late-time vacuum; $s_{\mathrm{in}}(\eta) = O_{A}s_{\mathrm{out}}(-\eta)$ is the early-time vacuum. The Bloch equation has a formal solution $S = \sum_{n \ge 0}\delta^{n}d_{n}(c, \sigma)$, $d_{0} = \hat h$, $d_{1} = \tfrac12c\,\sigma_{2}$, with $d_{n}$ vector polynomials, and for every $N \ge 1$ there is $C_{N}$ with $|s_{\mathrm{out}}(\eta) - \sum_{n \le N}\delta^{n}d_{n}| \le C_{N}(\mu/k^{2})^{N}$ for all real $\eta$; in particular $s_{\mathrm{out}}$ agrees with the adiabatic series of the cited result to every order, and $|s_{\mathrm{out}}(0)\cdot\sigma_{3}| \le C_{N}(\mu/k^{2})^{N}$ for every $N$. (b) (Proved.) Let $q = \tfrac12(1 - s_{\mathrm{in}}\cdot s_{\mathrm{out}})$, the occupation of the early-time vacuum over the late-time one; then $q = (s_{\mathrm{out}}(0)\cdot\sigma_{3})^{2}$, and where $q < 1$, with $\hat m$ the unit vector along $s_{\mathrm{in}}(0) + s_{\mathrm{out}}(0)$: a Fock state is $O_{A}$-invariant exactly when its occupations over $s_{\mathrm{in}}$ and over $s_{\mathrm{out}}$ are equal (for $q > 0$); the invariant Fock state at angle $\chi$ from $\hat m$ on the circle has occupation $n_{\chi} = \tfrac12\bigl(1 - \sqrt{1 - q}\cos\chi\bigr)$ over $s_{\mathrm{out}}$; every $O_{A}$-invariant state has occupation between $n_{0}$ and $1 - n_{0}$, $n_{0} = \tfrac12\bigl(1 - \sqrt{1 - q}\bigr)$, $4n_{0}(1 - n_{0}) = q$, the value $n_{0}$ being attained only by the Fock state $s_{0}$ with $s_{0}(0) = \hat m$, and every profile $n(k)$ with $n_{0}(k) \le n(k) \le 1 - n_{0}(k)$ is the occupation profile of an invariant state, $v_{k} = t(k)s_{0}$. (c) (Classical; Weber functions, cited from memory.) $q = e^{-\pi k^{2}/\mu}$, so
\[
n_{0}(k) \;=\; \tfrac12\Bigl(1 - \sqrt{1 - e^{-\pi k^{2}/(ma')}}\Bigr),
\]
a function of $k^{2}/(ma')$ alone, equal to $\tfrac12$ at $k = 0$ and $\tfrac14e^{-\pi k^{2}/(ma')}(1 + O(e^{-\pi k^{2}/(ma')}))$ at large $k$; the $O_{B}$-invariant Fock states have occupation $\tfrac12(1 \mp e^{-\pi k^{2}/(2ma')})$ over $s_{\mathrm{out}}$, tending to $\tfrac12$ (so, argued and not proved, they are not Hadamard). \emph{Credit.} The pure-state profile of (b), the transition probability of (c) and the choice of least number in (vi) are those of Boyle, Finn and Turok, arXiv:1803.08930: the free function of the invariant vacua is their Eq. (3.48), the occupation $(1 - \cos 2\eta\cos\lambda)/2$ in their notation their Eq. (3.49), and $|\beta| = e^{-\pi p^{2}/(2\gamma)}$ for the mass $\gamma\tau$ their Eq. (5.13); these locators were confirmed in review against the arXiv text.
\item[(v)] \emph{(The Hadamard property.)} (a) (Proved.) If two states of the class, with sector vectors $v_{k}$ and $r_{k}$, have $\int k^{N}|v_{k} - r_{k}|\,d^{3}k < \infty$ for every $N$ (the modulus is constant in $\eta$), their two-point functions differ by a smooth kernel on every collar $\eta > \varepsilon > 0$; for Fock states it suffices that every moment $\int k^{N}n(k)\,d^{3}k$ of the occupation of one over the other is finite. (b) (Given Fact \claimref{synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard}(c), by which $s_{\mathrm{out}}$, adiabatic of infinite order by (iv)(a), is Hadamard on such a collar.) The state $s_{0}$ of least occupation is Hadamard, and so is every $O_{A}$-invariant state $t(k)\,e_{\chi(k)}$ for which $1 - t(k)$ and $1 - \cos\chi(k)$ decrease faster than every power of $k$. The wall-instant vacuum is $O_{A}$-invariant, has occupation $\mu^{2}/(16k^{4}) + O(k^{-8})$ over $s_{\mathrm{out}}$, and is not Hadamard (clause (ii) of the cited massive result at $M_{1} = \mu$, itself given the same Fact); the tracial state is invariant and is not Hadamard, which is proved for $\mu = 0$ (the stored moment criterion) and argued, not proved, for $\mu > 0$ (its two-point function is one half of the anticommutator distribution, whose wave front set contains both $C^{(+)}$ and $C^{(-)}$; no necessity criterion for massive fields is stored). So, given the Fact, (CW) neither implies (HD) nor is implied by it, and (CW) with (HD) leaves the occupation profile above the floor $n_{0}$ free up to its ultraviolet tail.
\item[(vi)] \emph{(What selects; proved.)} Among the $O_{A}$-invariant states of the isotropic class the one of least occupation over the late-time vacuum in every sector is $s_{0}$, a Fock state: the conformal vacuum for $\mu = 0$ (where $q = 0$ and $s_{\mathrm{in}} = s_{\mathrm{out}} = \sigma_{1}$), and the state of profile $n_{0}$ for $\mu > 0$. The condition uses the orientation, that is the choice of $s_{\mathrm{out}}$ over $-s_{\mathrm{out}}$: the invariant set is symmetric under $v \mapsto -v$, and $-s_{0}$, of greatest occupation, is invariant too. Without (CW) the least occupation is $0$, attained by $s_{\mathrm{out}}$, which is not $O_{A}$-invariant for $\mu > 0$.
\item[(vii)] \emph{(Without isotropy; proved.)} For homogeneous, helicity-diagonal, charge-symmetric states with one vector $v_{\vec k, h}$ per sector, invariance under $\theta$ is $v_{-\vec k, h'}(0) = O_{A}v_{\vec k, h}(0)$ for each pair of sectors $(\vec k, h)$, $(-\vec k, h')$ that $\theta$ exchanges, and it restricts no single sector. For $\mu > 0$ the occupations over $s_{\mathrm{out}}$ of such a pair satisfy, where $q < 1$,
\[
n_{\vec k, h} + n_{-\vec k, h'} \;=\; 1 - \sqrt{1 - q}\;v_{\vec k, h}(0)\cdot\hat m \;\ge\; 2n_{0},
\]
with equality exactly when $v_{\vec k, h}(0) = \hat m$, and the floor of (iv)(b) fails sector by sector: $v_{\vec k, h} = s_{\mathrm{out}}$ with $v_{-\vec k, h'} = s_{\mathrm{in}}$ is invariant, with occupations $0$ and $q$. So $s_{0}$ is still the invariant state of least number in every pair, hence of least total number. Invariance under $W$ followed by the exchange of particles and holes is a condition within each sector, and (ii), (iv)(b) and (vi) hold for it without isotropy.
\end{enumerate}

## technical
The premise (HD) leaves the occupation profile of the descent's deposit free. One proposal for fixing it reads the mirror as the far side of the wall, the other sign of conformal time on a radiation-type descent, and asks the state to be invariant under a conjugation across the wall. For the Dirac field this is decided here. The mass term $M = ma$ is then odd in conformal time, and the reflection in the wall, applied to the even multivector field as $\gamma_{0}\chi\gamma_{0}$, is a symmetry of the equation. On the Bloch vectors of the stored two-level form only two reflections exist. One reverses the energy (the reflection used as an automorphism, the type of the stored conjugation): its invariant pure states sit at occupation one half at the wall and approach one half at large momentum, so, as the tracial state, it gives no Hadamard state (argued: the occupation tends to one half). The other, the reflection combined with charge conjugation or with the exchange of particles and holes, is the one the proposal needs, and its invariant states, among quasi-free states that are homogeneous, isotropic, diagonal in helicity with the same vector in both helicities, and charge-symmetric, form a disk per mode: a continuum. (The conjugation pairs momentum $\vec k$ with $-\vec k$; without isotropy the bound below holds only for the sum of the two occupations of a pair.) For a massless field every stationary charge-symmetric deposit is invariant, thermal ones at every temperature included, so nothing is selected. For a massive field the invariance has one consequence: the occupation over the late-time vacuum cannot be below $n_{0} = \tfrac12(1 - \sqrt{1 - e^{-\pi k^{2}/(ma')}})$, the midpoint between the early-time and late-time vacua, whose separation is the Landau-Zener probability $e^{-\pi k^{2}/(ma')}$; every profile above that floor is allowed. The state that sits on the floor is pure, has a Gaussian tail and no free number, and is Hadamard given the imported theorem on adiabatic states; it is selected only by adding least occupation and the orientation datum that tells the vacuum from the filled sea. The invariant family also contains states that are not Hadamard, among them the instantaneous vacuum at the wall with its stored $k^{-4}$ tail. The late-time vacuum's agreement with the adiabatic series to every order, and with it the faster-than-power decay of the floor, is proved by an elementary bound that needs no special functions; the exact exponent is the classical parabolic-cylinder computation. The background is prescribed and the Dirac field is a test field on it: with the expected stress as the source the exact radiation field does not reach the wall, given the hypotheses of the trace-anomaly result filed alongside. The profile and the non-uniqueness are in the paper of Boyle, Finn and Turok (arXiv:1803.08930, Eqs. (3.48), (3.49), (5.13)); the classification against the stored conjugation, the floor for mixed states and the Hadamard statements are what this entry adds.

## lay
The series assumes that the state of matter left by the descent is of the well-behaved kind that quantum field theory needs, and leaves open which such state it is. One idea for fixing it treats the far side of the descent's wall as a mirror image running the other way in time and demands that the state look the same from both sides. This entry works the idea out for electrons and similar particles when the early universe is filled with radiation. The demand does not pick a state. For particles without mass it allows every steady state, hot ones at any temperature included. For particles with mass it sets a minimum number of particles that must be present, a fixed curve that depends only on the momentum, the mass and the expansion rate, and it allows anything above that minimum. The state that sits exactly on the minimum is well behaved, given a standard theorem on such states, and has no adjustable number, but choosing it takes two more assumptions: that the state is pure and that it has as few particles as possible. A version of the mirror demand based on the conjugation the series already stores gives a state with every level half filled, which is argued not to be well behaved. The demand would also make the two sides equally hot (argued), which sits badly with the series' cold mirror.

## one-liner
Under three named hypotheses (radiation-type descent, the far side as the other sign of conformal time so that $M = ma$ is odd, and (CW), invariance of the state under the conjugation across the wall), the invariant quasi-free Dirac states (homogeneous, isotropic, diagonal in helicity with the same vector in both helicities, charge-symmetric) are a disk of Bloch vectors per mode, not one state: massless, every stationary charge-symmetric deposit, thermal at any temperature, is invariant; massive, the only consequence is the floor $n \ge \tfrac12(1 - \sqrt{1 - e^{-\pi k^{2}/(ma')}})$ over the late-time vacuum, attained by one pure state with a Gaussian tail (Hadamard given the adiabatic Fact) that is selected only with least occupation and the orientation added; without isotropy, for the conjugation with charge conjugation, only the pair bound $n_{\vec k} + n_{-\vec k} \ge 2n_{0}$ holds (the floor holds sector by sector for the reflection followed by the exchange of particles and holes); the energy-reversing conjugation gives occupation one half; the wall-instant vacuum is invariant and not Hadamard (given the same Fact); the background is prescribed, the Dirac field a test field on it.
