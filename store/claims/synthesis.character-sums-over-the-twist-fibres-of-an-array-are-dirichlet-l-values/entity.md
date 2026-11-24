---
id: synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values
kind: claim
version: 1
title: 'Character sums over the twist fibres of an array are Dirichlet L-values at 0 and -1'
status: proved
region: synthesis
subject: thermality
tags: [mode-counting, dictionaries, classical-theorem, boundary-modes]
proposed_by:
  kind: ai
  session: 2026-11-24-number-theory
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-number-theory
review: draft
outside_ga:
  kind: complex-analysis
  why: "The values L(0, chi) and L(-1, chi) are defined by analytic continuation of a Dirichlet series in a scalar variable; the statement is about scalars (grade 0). The one geometric-algebra content is that the character of conductor four is read off the powers of the quarter-turn bivector."
derivations:
- name: main
  uses:
  - synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages@1
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric@4
  - std-algebra.complex-numbers@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_fibre_sums_of_asymmetry_and_sea_energy_are_the_generalised_bernoulli_numbers
- kind: check
  ref: check.py::check_the_values_agree_with_class_numbers_and_with_the_divisor_sum_formula
- kind: check
  ref: check.py::check_the_two_halves_of_the_stored_array_and_the_character_of_the_quarter_turn
lineage:
  motivated_by:
  - singularity.q-joint-quasi-freeness-s-wave
  - synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter
extraction:
  note: >-
    A dictionary, recorded because the question was asked where Dirichlet L-functions meet the series: the
    stored product rule for arrays (an antiperiodic array on $M$ thermal periods is the product of $M$ arrays
    of twists $(2j + 1)/(2M)$, with additive sea energies) is the distribution relation of the Bernoulli
    polynomials, and resolving the fibres by a character of the odd residues modulo $2M$ gives the values of
    that character's L-function at $0$ and $-1$. A test fixed before computing: whether a character
    sum computed directly disagrees with the generalised Bernoulli number, or with an independent value of the
    L-function. It does not: the values agree with the class-number formula for eight negative
    discriminants and with the divisor-sum formula for four positive ones. What it is not: a constraint on the
    arrays, a selection of a twist, or evidence for the framework. The L-functions enter through special
    values at non-positive integers, which are rational numbers fixed by the twists; their zeros do not enter,
    and nothing here bears on the Riemann hypothesis or on masses. The analytic facts are classical and cited
    from memory: the Hurwitz zeta function and its values $\zeta(1 - k, a) = -B_{k}(a)/k$ (Hurwitz 1882;
    Apostol, Introduction to Analytic Number Theory, ch. 12), Dirichlet's class-number formula in the form
    $L(0, \chi_{D}) = 2h(D)/w(D)$ for $D < 0$, and the formula
    $\zeta(-1)L(-1, \chi_{D}) = \tfrac{1}{60}\sum_{b}\sigma((D - b^{2})/4)$ for the real quadratic field of
    discriminant $D$ (Siegel 1969; Cohen 1975). They are used as stated hypotheses; importing them is a
    decision for Leon if anything is built on this entity. The first check compares two evaluations of the same
    finite sum and so tests only the bookkeeping of twists and characters; the independent content is the
    second check. Ledger: transport-absent.
---

## formal
Units and notation as in \claimref{synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages}: $\mathcal{A}(\delta, r)$ is the fermion array with weights $\tfrac{\kappa}{r}(k + \delta)$, $k \in \Z$, and $\tfrac{\pi}{r}B_{2}(\delta)$, $B_{2}(a) = a^{2} - a + \tfrac16$, is its zeta-regularised symmetric sea energy times $\beta$ (\claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(ii)). Define its \emph{spectral asymmetry} as the value at $s = 0$ of $\sum_{k}\operatorname{sgn}(k + \delta)|k + \delta|^{-s}$, continued analytically from $\operatorname{Re}s > 1$. Let $M \ge 1$ and let $\chi$ be a character of the odd residues modulo $2M$: a function on the integers with $\chi(ab) = \chi(a)\chi(b)$, $\chi(a + 2M) = \chi(a)$, $\chi(a) = 0$ when $a$ and $2M$ have a common factor, with values in $\mathrm{span}\{1, I_{4}\}$ (conventions, the unit principle, U1), not identically $1$ on the residues prime to $2M$. $L(s, \chi) = \sum_{m \ge 1}\chi(m)m^{-s}$ is its L-function, continued analytically. Hypotheses, classical and cited from memory, not derived here: (H1) the Hurwitz zeta function $\zeta(s, a) = \sum_{k \ge 0}(k + a)^{-s}$, $0 < a \le 1$, continues analytically to $s = 0, -1$ with $\zeta(0, a) = \tfrac12 - a$ and $\zeta(-1, a) = -\tfrac12 B_{2}(a)$, and $L(s, \chi) = (2M)^{-s}\sum_{a = 1}^{2M}\chi(a)\zeta(s, a/2M)$; (H2) for a negative fundamental discriminant $D$, $L(0, \chi_{D}) = 2h(D)/w(D)$ with $h$ the number of classes of forms and $w$ the number of units; (H3) for a positive fundamental discriminant $D$, $\zeta(-1)L(-1, \chi_{D}) = \tfrac{1}{60}\sum_{b \in \Z,\ b \equiv D\,(2),\ b^{2} < D}\sigma\bigl((D - b^{2})/4\bigr)$.
\begin{enumerate}
\item[(i)] \emph{(The asymmetry of an array; proved given (H1).)} For $0 < \delta < 1$ the spectral asymmetry of $\mathcal{A}(\delta, r)$ is $1 - 2\delta$, independent of $r$; it changes sign under the particle-hole relabelling $\delta \mapsto 1 - \delta$ and vanishes exactly at the antiperiodic twist $\delta = \tfrac12$.
\item[(ii)] \emph{(The fibres resolved by a character; proved given (H1).)} By clause (iii) of the cited theorem, $\mathcal{A}(\tfrac12, Mr)$ is the product of the arrays $\mathcal{A}(\delta_{j}, r)$, $\delta_{j} = \tfrac{2j + 1}{2M}$, $0 \le j < M$. Then
\[
\sum_{j = 0}^{M-1}\chi(2j + 1)\,(1 - 2\delta_{j}) = 2\,L(0, \chi), \qquad \sum_{j = 0}^{M-1}\chi(2j + 1)\,B_{2}(\delta_{j}) = -\frac{L(-1, \chi)}{M},
\]
so the character sum of the spectral asymmetries of the fibres is $2L(0, \chi)$ and that of their sea energies times $\beta$ is $-\tfrac{\pi}{Mr}L(-1, \chi)$. For the trivial character the second sum is the stored rule $\sum_{j}B_{2}(\delta_{j}) = B_{2}(\tfrac12)/M$ and the first is $0$.
\item[(iii)] \emph{(Parity; proved.)} If $\chi(-1) = 1$ the asymmetry sum vanishes ($L(0, \chi) = 0$); if $\chi(-1) = -1$ the energy sum vanishes ($L(-1, \chi) = 0$). An even character sees only the sea energies of the fibres, an odd one only their asymmetries.
\item[(iv)] \emph{(The two halves of the stored array; proved.)} For $M = 2$ the fibres are the particle-hole halves of the array of Premise (Q) version 3, twists $\tfrac14$ and $\tfrac34$, with $B_{2} = -\tfrac{1}{48}$ each and spectral asymmetries $+\tfrac12$ and $-\tfrac12$; the only character is the one of conductor $4$, $\chi_{4}(a) = \langle -J\,J^{a}\rangle_{0}$ for odd $a$ with $J = e_{1}e_{2}$ the quarter-turn bivector of $\Cl(2,0)$ (\claimref{std-algebra.complex-numbers}(ii)); and the difference of the two asymmetries is $1 = 2L(0, \chi_{4})$, $L(0, \chi_{4}) = \tfrac12$.
\item[(v)] \emph{(Class numbers and divisor sums; proved given (H2), (H3).)} Let $\chi_{D}$ be the real character of fundamental discriminant $D$, read modulo $2M$, with $|D|$ dividing $2M$. The L-values in (ii) are those of $\chi_{D}$ at its conductor times the factors $1 - \chi_{D}(p)$ (asymmetry) and $1 - p\,\chi_{D}(p)$ (energy) for the primes $p$ dividing $2M$ and not $D$, among which $p = 2$ whenever $D$ is odd: the asymmetry sum is $\tfrac{4h(D)}{w(D)}\prod_{p}(1 - \chi_{D}(p))$ for $D < 0$, and the energy sum is $-\tfrac1M L(-1, \chi_{D})\prod_{p}(1 - p\chi_{D}(p))$ with $L(-1, \chi_{D}) = -\tfrac15\sum_{b}\sigma((D - b^{2})/4)$ for $D > 0$. Instances: the asymmetry sums are $1, 2, 4$ for $D = -4, -8, -20$ at $M = 2, 4, 10$, $\tfrac43$ and $4$ for $D = -3, -11$ at $M = 3, 11$ (where $\chi_{D}(2) = -1$ doubles $4h/w$), and $0$ for $D = -7, -15, -23$ at $M = 7, 15, 23$ (where $\chi_{D}(2) = 1$: the fibres, having odd numerators only, do not see these class numbers); the energy sums are $\tfrac14, \tfrac13$ for $D = 8, 12$ at $M = 4, 6$ and $\tfrac{6}{25}, \tfrac{6}{13}$ for $D = 5, 13$ at $M = 5, 13$, from $L(-1, \chi_{D}) = -1, -2, -\tfrac25, -2$.
\end{enumerate}
\emph{Reading.} The Dirichlet L-functions meet the stored arrays through their values at $0$ and $-1$: the rational numbers obtained by weighting the fibres' spectral asymmetries and sea energies with a character of the twist. The fibres and their additivity are stored; the identification of the weighted sums is classical. No clause constrains an array or selects a twist.

## technical
The stored theorem on arrays says that an antiperiodic array on a window of $M$ thermal periods is the product of $M$ arrays on one period, with twists the odd multiples of $1/2M$, and that the zeta-regularised sea energies add. That additivity is the distribution relation of the second Bernoulli polynomial. The fibres are labelled by the odd residues modulo $2M$, a group, and weighting them by a character of that group turns the sums into generalised Bernoulli numbers, that is into values of the character's L-function: the sea energies give $L(-1, \chi)$ and the spectral asymmetries $1 - 2\delta$ give $L(0, \chi)$. Even characters see only energies and odd characters only asymmetries. For the two halves of the stored array the character is the one of conductor four, the grade-zero part of the powers of the quarter turn, and the two asymmetries $\pm\tfrac12$ differ by $2L(0, \chi_{4}) = 1$. For real characters the values are class numbers of imaginary quadratic fields and divisor sums attached to real quadratic fields; the check confirms them against a direct count of reduced forms and against the divisor-sum formula. This is a dictionary between a stored structure and classical number theory. It uses only special values, which are rational; it does not involve zeros of L-functions and supplies no premise, selection or prediction.

## lay
The horizon's modes come in families labelled by a twist, and a long window of time splits into shorter ones whose twists are evenly spaced fractions. Number theory has a classical way to weight evenly spaced fractions, by patterns of plus and minus signs called characters, and the weighted sums are famous numbers: values of Dirichlet's L-functions. This result notes that the series' bookkeeping of energies and asymmetries of the families gives exactly those numbers. It is a translation between two languages. It does not predict anything.

## one-liner
For the fibres $\delta_{j} = \tfrac{2j+1}{2M}$ of an antiperiodic array on $M$ thermal periods and a character $\chi$ of the odd residues modulo $2M$ (classical continuation of the Hurwitz zeta function assumed), $\sum_{j}\chi(2j+1)(1 - 2\delta_{j}) = 2L(0, \chi)$ (spectral asymmetries) and $\sum_{j}\chi(2j+1)B_{2}(\delta_{j}) = -L(-1, \chi)/M$ (sea energies); even characters see only energies and odd ones only asymmetries, the two halves of the stored array give $2L(0, \chi_{4}) = 1$ with $\chi_{4}(a) = \langle -J J^{a}\rangle_{0}$, and real characters give class numbers and divisor sums; a dictionary of special values, with no constraint on the arrays.
