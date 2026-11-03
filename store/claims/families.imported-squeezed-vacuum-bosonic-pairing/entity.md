---
id: families.imported-squeezed-vacuum-bosonic-pairing
kind: claim
version: 3
title: 'Imported: the squeezed vacuum of a bosonic pairing'
status: proved
region: families
subject: generations
tags: [pairing-and-bogoliubov, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.imported-squeezed-vacuum-bosonic-pairing-external@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_bogoliubov_relations
- kind: check
  ref: check.py::check_two_point_functions
- kind: check
  ref: check.py::check_wick_four_point
- kind: check
  ref: check.py::check_takagi_functional_calculus
- kind: proof
  derivation: main
locators:
  paper: T13
  number: Fact 2.6
  label: fact:gaussian
  line: 601
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: exact two-mode Fock model of a = U(C c - S c^dag) at rational hyperbolic points: CCR, N and M formulas, both Wick four-point formulas, and the Takagi functional calculus. Version 2 -> 3.'
  env: fact
  context_refs:
  - correspondence.shared-core-ordering-dictionary
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    removed:
    - correspondence.shared-core-ordering-dictionary
    note: 'Removed the ordering dictionary: it is cited in the provenance only for the later ordering-shift
      reading, and the Gaussian two-point functions and Wick formulas do not depend on it; the external
      literature edge is the real source and was kept.'
---

## formal
Let $a_{p}$, $p = 1, \dots, n$, be bosonic modes and $\xi$ a complex symmetric $n \times n$ matrix, with Takagi factorisation $\xi = U\Sigma U^{\mathsf{T}}$ for a unitary $U$ and $\Sigma = \mathrm{diag}(\sigma_{1}, \dots, \sigma_{n})$, $\sigma_{j} \ge 0$ the singular values of $\xi$. The squeezed vacuum of the pairing $\xi$ is the zero-mean Gaussian state whose only nonvanishing two-point functions are
\[
N_{pq} \;=\; \langle a_{p}^{\dagger}a_{q}\rangle \;=\; \overline{\bigl(U\,\sinh^{2}\!\Sigma\,U^{\dagger}\bigr)}_{pq}, \qquad
M_{pq} \;=\; \langle a_{p}a_{q}\rangle \;=\; -\bigl(U\,\sinh\Sigma\cosh\Sigma\,U^{\mathsf{T}}\bigr)_{pq},
\]

the sign of $M$ a convention; any function $f$ applied in the Takagi basis, $U f(\Sigma) U^{\mathsf{T}}$, equals $g(\xi\xi^{\dagger})\,\xi$ with $g(s) = f(\sqrt{s})/\sqrt{s}$, which is what makes the formulas degenerate-safe. Wick's theorem gives, for zero-mean Gaussian states, $\langle a_{p}^{\dagger}a_{q}^{\dagger}a_{r}a_{s}\rangle = N_{ps}N_{qr} + N_{pr}N_{qs} + \overline{M_{pq}}M_{rs}$ and $\langle a_{r}a_{s}a_{p}^{\dagger}a_{q}^{\dagger}\rangle = D_{rq}D_{sp} + D_{rp}D_{sq} + M_{rs}\overline{M_{pq}}$ with $D_{rp} = \langle a_{r}a_{p}^{\dagger}\rangle = \delta_{rp} + N_{pr}$. \emph{Provenance:} the Takagi factorisation is \cite[Cor.~4.4.4]{HornJohnson}; bosonic Bogoliubov transformations, squeezed vacua and Wick's theorem for quasi-free states are \cite[Ch.~2-3]{Berezin1966} and, in the covariance-matrix form used here, \cite[\S II]{Weedbrook2012}; the series' ordering dictionary is \cite[Thm.~5.7]{ButlerT9}. The bosonic Fock space here is not the fermionic one of the Standard-Model paper.

## technical
For bosonic modes $a_{p}$ and a complex symmetric pairing matrix $\xi$ with Takagi factorisation $\xi = U\Sigma U^{\mathsf{T}}$, the squeezed vacuum is the zero-mean Gaussian state with two-point functions $N_{pq} = \langle a_{p}^{\dagger}a_{q}\rangle = \overline{(U\sinh^{2}\Sigma\,U^{\dagger})}_{pq}$ and $M_{pq} = \langle a_{p}a_{q}\rangle = -(U\sinh\Sigma\cosh\Sigma\,U^{\mathsf{T}})_{pq}$, the sign of $M$ a convention. Any function applied in the Takagi basis can be rewritten as $g(\xi\xi^{\dagger})\,\xi$ with $g(s) = f(\sqrt{s})/\sqrt{s}$, which keeps the formulas valid when singular values coincide.

Wick's theorem then gives every four-point function of a zero-mean Gaussian state from $N$, $M$ and $D_{rp} = \delta_{rp} + N_{pr}$, for example $\langle a_{p}^{\dagger}a_{q}^{\dagger}a_{r}a_{s}\rangle = N_{ps}N_{qr} + N_{pr}N_{qs} + \overline{M_{pq}}M_{rs}$. These are standard results of matrix analysis and of quasi-free bosonic states.

## lay
When pairs of bosonic particles are created together in a controlled way, the resulting state is called a squeezed vacuum. All of its statistics are fixed by two tables of numbers, one counting particles and one measuring the pairing, and both can be read off from a standard factorisation of the pairing matrix. A standard rule, Wick's theorem, then gives every more complicated average from these two tables. These are textbook results used as tools.

## one-liner
The squeezed vacuum of a bosonic pairing $\xi = U\Sigma U^{\mathsf{T}}$ has two-point functions $N = \overline{U\sinh^{2}\Sigma\,U^{\dagger}}$ and $M = -U\sinh\Sigma\cosh\Sigma\,U^{\mathsf{T}}$, and Wick's theorem gives its four-point functions from them.
