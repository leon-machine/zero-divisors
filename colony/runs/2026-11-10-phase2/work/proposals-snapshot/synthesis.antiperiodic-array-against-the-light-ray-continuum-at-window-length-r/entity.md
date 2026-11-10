---
id: synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r
kind: claim
version: 1
title: 'Antiperiodic array against a light ray''s continuum at window length r'
status: proved
region: synthesis
subject: entropy
tags: [thermal-premises, boundary-modes, mode-counting, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-10-phase2
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase2
review: draft
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.imported-theta-function-identities@2
  - synthesis.half-integer-weight-array-carries-half-ln2@5
  - synthesis.counted-unit-energy-at-half-offset@3
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric@4
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.residue-from-mode-entropy@4
  - synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_self_duality_of_the_partition_function
- kind: check
  ref: check.py::check_energy_matches_only_at_the_fixed_point
- kind: check
  ref: check.py::check_entropy_difference_as_a_function_of_window_length
- kind: check
  ref: check.py::check_energy_variance_against_the_continuum
- kind: check
  ref: check.py::check_residue_if_the_continuum_value_were_counted
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.window-reading-array-killing-energy
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric
  - synthesis.counted-unit-energy-at-half-offset
extraction:
  open_problem: op.residue-killing-weights
  note: >-
    Attack item 4 of op.residue-killing-weights (which object's entropy the count compares with A/4): the exact
    form of the comparison recorded there as computed evidence. What is new against the stored results: the
    comparison at every window length r, not only r = 1; the proof that each of the three stored energy equalities
    (sea, thermal energy above the sea, symmetric-ordered thermal energy) holds only at r = 1 and that they are
    one identity; the entropy difference as a function of r with its sign at every r and a remainder bound; the
    variance in dual form; the conditional arithmetic of the residue. The stored values at r = 1 ((1/2) ln 2,
    pi/12, the variance per unit) are used, not re-proved. Clauses (i) to (iv) are mathematics of the array as
    defined in the statement and of the stored continuum energy density; they do not assume Premise (Q), (N+) or
    the window reading (the cited null-ordering theorem assumes the window reading only for its clause (iv),
    which is not used here; its clauses (i) to (iii) are used). Clause (v) is conditional arithmetic under the
    area-law hypothesis of the cited residue theorems; it is not a derivation of the residue and it neither meets
    nor fails the kill condition of pred.boundary-mode-density. Units: the array's Killing flow uses the boundary
    modes' unit J = e_2 e_3; the theta-function computation is complex analysis of scalar functions with numbers
    in span{1, I_4}, tau = I_4/r, as in the stored theta Fact. Prior art, cited from memory and not used as
    premises: modular invariance of the free fermion characters and the high-temperature (Cardy) form of the
    partition function on a circle (J. Cardy, Nucl. Phys. B 270 (1986) 186); the series
    sum (2n - 1)/(e^{(2n - 1) pi} + 1) = 1/24 is classical (Ramanujan's notebooks; from memory). A closed form
    of the variance at r = 1, pi^4/(24 Gamma(3/4)^8), follows from Jacobi's derivative formulas and the
    lemniscatic value of theta_3, neither of which is in the stored Fact; it agrees with the bounds of (iv) to
    twelve digits in floating point and is not claimed. Transport-absent: nothing here uses the transport
    structure. Intended citation for the sibling results of the same topic: this entity is the base statement of
    the array-against-continuum comparison.
---

## formal
Units $\hbar = c = 1$; numbers are read in $\mathrm{span}\{1, I_4\}$. Let $\kappa > 0$, $\beta = 2\pi/\kappa$, and let $r > 0$. Let $\mathcal{A}(r)$ be the fermion array $\{\psi_{k}\}_{k \in \Z}$ with weights $\omega_{k} = \tfrac{\kappa}{r}(k + \tfrac12)$, the single-particle spectrum of one chiral complex component on a circle of Killing time of length $L = r\beta$ with the antiperiodic condition, in its Gibbs product state at $\beta$, so that $x_{k} = \beta\omega_{k} = 2\pi(k + \tfrac12)/r$. $\mathcal{A}(1)$ is the array of version 3 of Premise (Q) at the Hawking temperature, and the array of spacing $\kappa$ at the temperature $r\kappa/2\pi$ has the same $x_{k}$, so $r$ is the window length in thermal periods on either reading. With $a_{n} = n - \tfrac12$, $n \ge 1$, put
\[
f(r) = \frac{\pi}{12r} + 2\sum_{n \ge 1}\ln\bigl(1 + e^{-2\pi a_{n}/r}\bigr), \qquad e(r) = \frac{4\pi}{r}\sum_{n \ge 1}\frac{a_{n}}{e^{2\pi a_{n}/r} + 1}, \qquad e_{\mathrm{sym}}(r) = e(r) - \frac{\pi}{12r},
\]
the logarithm of the partition function in the zeta-regularised symmetric ordering (sea energy $-\kappa/(24r)$, Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(ii) at spacing $\kappa/r$), $\beta$ times the energy above the sea, and $\beta$ times the symmetric-ordered energy; let $S(r) = f(r) + e_{\mathrm{sym}}(r)$ be the entropy and $v(r) = \beta^{2}\operatorname{Var}(E)$. The \emph{continuum values} for a window of $r$ thermal periods of one chiral complex component of a light ray at $\beta$ are: $\beta E = \pi r/12$ in the boost ordering and $0$ in the null ordering, the boost ground state carrying $-\pi r/12$ in the null ordering (Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(i): density $\kappa^{2}/(48\pi)$); and the extensive entropy and variance $\pi r/6$, the entropy rate times the window, defined here as $r\lim_{R \to \infty}S(R)/R$ and $r\lim_{R \to \infty}v(R)/R$ (the limits exist by (iii), (iv) and equal the density integrals $\tfrac{r}{2\pi}\int_{\R}s(x)\,dx$ and $\tfrac{r}{2\pi}\int_{\R}x^{2}n(x)(1 - n(x))\,dx$, with $s$ the entropy of one mode of Theorem \claimref{synthesis.boundary-mode-thermal-entropy} and $n(x) = 1/(e^{x} + 1)$). Then:
\begin{enumerate}
\item[(i)] \emph{(Self-duality; proved given the imported theta identities.)} $f(r) = f(1/r)$, that is $f(r) = \pi r/12 + c(r)$ with $c(r) = 2\sum_{n \ge 1}\ln(1 + e^{-2\pi ra_{n}}) > 0$: the array's $\ln Z$ is the continuum's $\pi r/12$ plus $c(r)$. At $r = 1$, $f = \tfrac12\ln 2$ (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}) and $c(1) = \tfrac12\ln 2 - \pi/12 \in (0.08477, 0.08478)$.
\item[(ii)] \emph{(The energy match is the fixed point; proved given the identities.)} $e_{\mathrm{sym}}(r) = \pi r/12 - 4\pi r\sum_{n \ge 1}a_{n}/(e^{2\pi ra_{n}} + 1) = -e_{\mathrm{sym}}(1/r)$, and $e_{\mathrm{sym}}(r) < 0$ for $r < 1$, $> 0$ for $r > 1$. The three comparisons of energy with the continuum are (a) the sea against the boost ground state, $-\pi/(12r)$ against $-\pi r/12$; (b) the energy above the sea against the boost-ordered value, $D(r) := e(r) - \pi r/12 = \pi/(12r) - 4\pi r\sum_{n}a_{n}/(e^{2\pi ra_{n}} + 1)$, with $D(1/r) = -D(r)$ and $D(r) > 0$ for $r > 1$; (c) the symmetric-ordered energy against the null-ordered value $0$. Each holds exactly when $r = 1$, and at $r = 1$ (b) and (c) are the one identity $\sum_{n \ge 1}(2n - 1)/(e^{(2n - 1)\pi} + 1) = \tfrac{1}{24}$, the vanishing of $f'$ at the fixed point of $r \mapsto 1/r$, with (a) the equality of $1/r$ and $r$ there. For the array of spacing $\kappa$ at the temperature $r\kappa/2\pi$, the symmetric-ordered energy minus the continuum's null-ordered energy over the window $2\pi/\kappa$ at that temperature is $\tfrac{\kappa}{2\pi}\,rD(r)$: it vanishes at the Hawking temperature and at no other positive temperature. Values: $e_{\mathrm{sym}}(2) \in (0.50017, 0.50018)$; $D(2) \in (0.1074, 0.1076)$, $D(4) \in (0.0653, 0.0654)$.
\item[(iii)] \emph{(The entropy difference; proved given the identities.)} $S(r) = \pi r/6 + \Delta(r)$ with
\[
\Delta(r) = 2\sum_{n \ge 1}\Bigl[\ln\bigl(1 + e^{-y_{n}}\bigr) - \frac{y_{n}}{e^{y_{n}} + 1}\Bigr], \qquad y_{n} = 2\pi ra_{n} .
\]
$\Delta(r) < 0$ for every $r > 0$; $\Delta(1) = \tfrac12\ln 2 - \pi/6 \in (-0.17703, -0.17702)$ exactly; for $r \ge 1$, $\Delta(r) = -2(\pi r - 1)e^{-\pi r} + \rho(r)$ with $|\rho(r)| \le 3\pi r\,e^{-2\pi r}$, so $S(R)/R \to \pi/6$. Values: $\Delta(2) \in (-0.019693, -0.019692)$, $\Delta(4) \in (-8.068, -8.067) \times 10^{-5}$, $\Delta(8) \in (-5.88, -5.86) \times 10^{-10}$, $\Delta(\tfrac12) \in (-0.23465, -0.23464)$, $\Delta(\tfrac14) \in (-0.13081, -0.13080)$. At $r = 1$ the entropy is $\ln Z$ itself, since $e_{\mathrm{sym}}(1) = 0$. Moreover $\Delta'(r) = \tfrac1r\,\tfrac{d}{dr}\bigl(rD(r)\bigr)$ and $\Delta(r) \to 0$ as $r \to 0$, so $\Delta(r) = \int_{0}^{r}\rho^{-1}\,d\bigl(\rho D(\rho)\bigr)$: at fixed window the entropy difference is the Clausius integral, from zero temperature, of the energy difference of (ii).
\item[(iv)] \emph{(The variance; proved given the identities.)} $v(r) = 2\sum_{k \ge 0}x_{k}^{2}n(x_{k})(1 - n(x_{k})) = \pi r/6 + 2\sum_{n \ge 1}y_{n}n(y_{n})\bigl[y_{n}(1 - n(y_{n})) - 2\bigr]$, so $v(r) > \pi r/6$ for $r \ge 1$ and $v(R)/R \to \pi/6$. At $r = 1$, $v \in (0.79821, 0.79822)$ per array (half the stored value per counted unit, Theorem \claimref{synthesis.counted-unit-energy-at-half-offset}(iv)), above $\pi/6$ by an amount in $(0.2746, 0.2747)$; $v(2) - \pi/3 \in (0.1000, 0.1002)$.
\item[(v)] \emph{(Conditional arithmetic of the residue; computed.)} Under the area-law hypothesis of Theorem \claimref{synthesis.residue-from-mode-entropy}, with units of $\bar u$ components on average, the count of the series uses the array's $\tfrac12\ln 2$ per component and gives $\kappa_{c} = 1/(2\bar u\ln 2)$, the registered $1/(4\ln 2) \in (0.36067, 0.36068)$ at $\bar u = 2$ (Theorem \claimref{synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping}). If the continuum value $\pi/6$ per component per modular period were counted in its place, the same formula would give $\kappa_{c} = 3/(2\pi\bar u)$: $3/(4\pi) \in (0.23873, 0.23874)$ units of two components per Planck area per modular period, $3/(2\pi) \in (0.47746, 0.47747)$ components against the arrays' $1/(2\ln 2)$; the ratio of the two residues is $3\ln 2/\pi \in (0.66190, 0.66191)$ for every grouping; the registered value would need $\bar u = 6\ln 2/\pi \in (1.3238, 1.3239)$, which is not an integer; and the cosmological count $4\pi\kappa_{c}N^{2}$ would be $3N^{2}$ in place of $\pi N^{2}/\ln 2$. For arrays of window $r$ the components per Planck area per modular period are $r/(4S(r))$: $1/(2\ln 2)$ at $r = 1$, a value in $(0.4866, 0.4867)$ at $r = 2$, tending to $3/(2\pi)$; so the value $\ln 2$ for two arrays belongs to $r = 1$. This clause compares numbers under a hypothesis; it does not derive the residue, and it does not say that the continuum value should be counted.
\end{enumerate}
So, given the imported theta identities, the array and the continuum agree in mean energy at window length one thermal period because that length is the fixed point of the duality, and at no other length; in $\ln Z$, entropy and variance they differ at every finite length, by amounts that vanish exponentially for long windows and are of order one at $r = 1$.

## technical
The window reading equates the mean Killing energy of an array with that of a light ray's continuum over one window, and its scope sentence records that the array's entropy, $\tfrac12\ln 2$, and the continuum's entropy rate times the window, $\pi/6$, are different numbers. This result makes the comparison exact at every window length. The array with the antiperiodic condition on a circle of $r$ thermal periods has partition function $\vartheta_{3}/\eta$ at $\tau = I_4/r$, which, given the imported theta-function identities, is unchanged when $r$ is replaced by $1/r$; written in the dual form it is the continuum's extensive value $\pi r/12$ plus a positive correction that is exponentially small for long windows.

The energy is the derivative of $\ln Z$ along the family, so it is odd under $r \mapsto 1/r$ and vanishes at $r = 1$. The three stored equalities of energy (the sea against the boost ground state, the thermal energy above the sea against the continuum's, and the symmetric-ordered thermal energy against zero) each hold only at $r = 1$, and they are one identity. Read at fixed spacing and varied temperature, the array's energy agrees with the continuum's only at the Hawking temperature. The entropy at $r = 1$ is $\ln Z$ itself and lies below the continuum's value at every window length: by $0.177$ at one thermal period, $0.0197$ at two, $8 \times 10^{-5}$ at four. The variance of the energy lies above the continuum's for $r \ge 1$, by $0.275$ at $r = 1$.

Under the area-law hypothesis, counting the continuum's $\pi/6$ per component in place of the array's $\tfrac12\ln 2$ would change the residue from $1/(4\ln 2)$ to $3/(4\pi)$ per unit of two components, for every grouping in the same ratio; this is arithmetic under a hypothesis, not a derivation, and it does not bear on the boundary-mode prediction's kill condition.

## lay
The series counts a black hole's entropy with small ladders of quantum modes on the horizon, and one of its assumptions says that a ladder's average energy is that of one stretch of a light ray on the horizon. The ladder and the stretch of light ray are different systems, so it matters how far the agreement goes. This result works that out exactly, given classical identities of special functions. The average energies agree only when the stretch is exactly one thermal cycle long, because that length is a point of symmetry of the ladder's mathematics; at any other length they differ. The entropies never agree: the ladder holds less than the light ray's share, by an amount that is large at one thermal cycle and fades quickly for longer stretches. The energy fluctuations differ too. If, under the area law, the light ray's share were counted instead of the ladder's, the density of counted units would be $3/(4\pi)$ in place of $1/(4\ln 2)$; this is a comparison of numbers under an assumption, not a new derivation.

## one-liner
Given the imported theta identities, the antiperiodic array on $r$ thermal periods has $\ln Z(r) = \ln Z(1/r)$, so its mean energy matches a light ray's continuum only at the fixed point $r = 1$ (all three stored energy equalities are that one identity), while its entropy is $\pi r/6 + \Delta(r)$ with $\Delta < 0$ at every $r$ ($\tfrac12\ln 2 - \pi/6$ at $r = 1$, $-0.0197$ at $r = 2$) and its energy variance exceeds $\pi r/6$ for $r \ge 1$; under the area-law hypothesis the continuum value would give $3/(4\pi)$ in place of $1/(4\ln 2)$.
