---
id: synthesis.operator-join-positive-energy-no-finite-energy-zero-modes
kind: claim
version: 1
title: 'No finite-energy zero modes of the oscillator join for $\Lambda \ge 0$'
status: proved
region: synthesis
subject: mass
tags: [frozen-point, conformal-spinors, no-go, symmetry-breaking]
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
review: draft
derivations:
- name: main
  uses:
  - synthesis.operator-join-ordering-constants@2
  - synthesis.operator-join-seed-has-no-diagonal-matrix-elements@1
  - synthesis.operator-join-casimir-shifts@2
  - mass.imported-palatial-quadratics-homogeneity-charge@4
  - field-theory.twistor-attachment@6
  - synthesis.positive-structure-is-twistor-form-at-imaginary-time@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_positive_energy_realisation_bookkeeping
- kind: check
  ref: check.py::check_join_is_positive_part_plus_isotype_constant
- kind: check
  ref: check.py::check_top_band_and_no_finite_energy_eigenvectors
- kind: check
  ref: check.py::check_controls
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.operator-join-seed-has-no-diagonal-matrix-elements
  - synthesis.operator-join-ordering-constants
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Not rewritten: the i of the generalised state exp((2i/hbar) sum a^dagger b^dagger) and the spectral parameter mu in C are the scalars of the palatial Fock space F, whose unit the store does not fix (twistor numbers are read with I_6, the field theory''s one-particle space with I_4, and the twistor attachment makes F that space); declared outside_ga (complex-analysis).'
  open_problem: op.operator-join
  note: >-
    The problem's second line of attack (decide whether the polynomial and positive-energy
    realisations have the same zero modes) and the structural half of its first (the join sector by
    sector on the positive-energy modules). The identification of the displayed oscillator split with
    the attachment's module (the store's conjugation the Hilbert adjoint, with the energies and
    multiplicities) is proved once, filed alongside, synthesis.attachment-conformal-energy-is-generated-by-z, and is cited, not re-checked;
    until it is accepted, "positive-energy modules" here means the displayed oscillator realisation,
    which is all the proofs use. Filed alongside, synthesis.operator-join-point-spectrum-on-positive-energy-modules: same setting; for Lambda > 0 it
    writes the join through a unitary su(1,1) and shows, modulo a cited decomposition theorem for
    SL(2,R), that the point spectrum starts at Lambda hbar^2/3 (attained by an infinite-sum vector)
    and that the continuum threshold m^2 + j(j+1) - 7/4 <= 0 empties the isotypes this result's bound
    (iii) singles out; (iii) is the weaker, literature-free bound and defers to it. What is distinct
    here, with no cited fact: (a) the per-isotype form of the join and its bound; (b) for Lambda >= 0
    the join raises the oscillator number by at most four and its top band is multiplication by the
    product of the two creation brackets, injective, so no finite linear combination of number states
    is an eigenvector for any eigenvalue, in any sector (the Lambda = 0 case is covered only here);
    (c) the constant, a zero mode of the polynomial realisation, has no counterpart for Lambda >= 0.
    For Lambda < 0 the statement fails and the failure is recorded: at the Fock scale matched to the
    frozen point (lambda = -1 in the units of the check, lambda s^4 = -1 in general) the pure terms of
    the bracket cancel, the join preserves the oscillator number, and its kernel on degree two is
    three-dimensional (sectors (1/2, -1/2), (-1/2, 1/2), (0, 0), internal spin 1, all in ker B); at a
    mismatched scale the same zero modes are infinite sums. The dilation scaling of the spectrum by
    lambda holds for lambda > 0 only; for lambda < 0 the join is |lambda| times its lambda = -1 form.
    Literature cited from memory: the oscillator (ladder) construction of the positive-energy
    massless representations of SU(2,2), and the Friedrichs extension of a semibounded form.
    Transport-convenient: the join and its ordering are the series' objects; the positivity and the
    band argument are standard oscillator algebra.
outside_ga:
  kind: complex-analysis
  why: 'i stays as the scalar unit of the palatial oscillator Fock space F (the generalised state exp((2i/hbar) sum a^dagger b^dagger) applied to the vacuum, and the spectral parameter mu in C), and the store does not settle whether that unit is the twistor unit I_6 or the field unit I_4'
---

## formal
Let $Z^{\alpha}_{i}$, $\bar{Z}_{i\alpha}$ ($i = 1, 2$; $\alpha = 0, \dots, 3$) be the palatial oscillators of two constituents, $[Z^{\alpha}_{i}, \bar{Z}_{l\beta}] = \hbar\,\delta_{il}\delta^{\alpha}_{\beta}$, with $\omega^{A} = Z^{A}$, $\pi_{A'} = Z^{A+2}$, and the stored conjugation $Z^{\alpha} \mapsto \bar{Z}_{\sigma(\alpha)}$, $\sigma = (0\,2)(1\,3)$ (so that $\bar{Z}_{A} = \bar{\pi}_{A}$, $\bar{Z}_{A+2} = \bar{\omega}^{A'}$). Let $\hat{B} = \br{\pi^{1}\pi^{2}} + \lambda[\omega^{1}\omega^{2}]$, $\lambda = \Lambda/6$, $\hat{B}^{\dagger}$ its conjugate, $\hat{h}_{il}$ the symmetrised Gram operators, $\hat{C} = \tfrac12\sum_{i,l}\hat{h}_{il}\hat{h}_{li} - \tfrac14(\tr\hat{h})^{2}$, and $\hat{m}^{2} = \hat{B}^{\dagger}\hat{B} + \hat{B}\hat{B}^{\dagger} + \tfrac{\Lambda}{3}\hat{C} - \tfrac{2\Lambda}{3}\hbar^{2}$ the operator join of Proposition \claimref{synthesis.operator-join-ordering-constants}(3). The positive-energy realisation is the oscillator model of Proposition \claimref{field-theory.twistor-attachment}: for each constituent, $Z^{A} = a_{A} + b^{\dagger}_{A}$, $Z^{A+2} = a_{A} - b^{\dagger}_{A}$, $\bar{Z}_{A} = a^{\dagger}_{A} - b_{A}$, $\bar{Z}_{A+2} = a^{\dagger}_{A} + b_{A}$, with $a_{A}$, $b_{A}$ ($A = 0, 1$) four annihilation operators, $[a_{A}, a^{\dagger}_{B}] = [b_{A}, b^{\dagger}_{B}] = \tfrac{\hbar}{2}\delta_{AB}$, on the Fock space $\mathcal{F}$ of their vacuum; $\mathcal{F}_{0} \subset \mathcal{F}$ is the algebraic Fock space, the finite linear combinations of number states (the states of finite energy content). The sector $(s_{1}, s_{2})$ is the joint eigenspace $\hat{h}_{ii} = 2s_{i}\hbar$, and an isotype $(s_{1}, s_{2}, j)$ its intersection with the spin-$j$ isotypic component of the internal $\mathfrak{su}(2)$ spanned by $\hat{h}_{12}$, $\hat{h}_{21}$, $\tfrac12(\hat{h}_{11} - \hat{h}_{22})$.
\begin{enumerate}
\item[(i)] \emph{(Setting.)} In the oscillator realisation the Hilbert adjoint of $Z^{\alpha}_{i}$ is $\bar{Z}_{i\sigma(\alpha)}$ (the adjoint of $a + b^{\dagger}$ is $a^{\dagger} + b$); that this realisation is the attachment's positive-energy module, with the twistor form the grading of the central rotation, energies $|s| + 1 + n$ and multiplicities $(n+1)(n + 2|s| + 1)$, is proved once (filed alongside, synthesis.attachment-conformal-energy-is-generated-by-z) and is used here, not re-proved. Hence $\hat{B}^{\dagger}$ is the adjoint of $\hat{B}$, each $\hat{h}_{ii} = \hbar(N_{a,i} - N_{b,i})$ is self-adjoint with spectrum $\hbar\Z$, so $s_{i} \in \tfrac12\Z$, and $\hat{h}_{12}^{\dagger} = \hat{h}_{21}$; the $\hat{h}_{il}$ preserve the oscillator number $N = \sum_{i}(N_{a,i} + N_{b,i})$ and generate a unitary action of the internal $U(2)$ on each finite-dimensional level of $\mathcal{F}_{0}$. The realisation is at the Fock scale of the units chosen; $\lambda = \Lambda/6$ is measured in that scale.
\item[(ii)] \emph{(The join on an isotype.)} In every realisation of the canonical relations, $\hat{m}^{2} = 2\hat{B}^{\dagger}\hat{B} + \hbar\lambda\tr\hat{h} + \tfrac{\Lambda}{3}\hat{C} - \tfrac{2\Lambda}{3}\hbar^{2}$, and $\hat{C}$ is the Casimir of the internal $\mathfrak{su}(2)$, equal to $j(j+1)\hbar^{2}$ on the spin-$j$ isotype. Hence on the isotype $(s_{1}, s_{2}, j)$, with $j \ge |s_{1} - s_{2}|$ and $j - (s_{1} - s_{2}) \in \Z$,
\[
\hat{m}^{2} \;=\; 2\hat{B}^{\dagger}\hat{B} \;+\; \frac{\Lambda}{3}\hbar^{2}\bigl(s_{1} + s_{2} + j(j+1) - 2\bigr) .
\]
\item[(iii)] \emph{(Lower bound and the sectors that can be massless.)} On the positive-energy realisation $\langle\psi, \hat{m}^{2}\psi\rangle \ge \tfrac{\Lambda}{3}\hbar^{2}(s_{1} + s_{2} + j(j+1) - 2)\langle\psi, \psi\rangle$ for every $\psi \in \mathcal{F}_{0}$ in the isotype $(s_{1}, s_{2}, j)$, with equality exactly on $\ker\hat{B}$. So (for $\Lambda > 0$) the massless locus of the join, in the sense of eigenvectors or of the spectrum of the Friedrichs extension of the restricted form, is empty on every isotype with $s_{1} + s_{2} + j(j+1) > 2$; a massless two-constituent state needs $\max(s_{1}, s_{2}) \le 1$ and $2\max(s_{1}, s_{2}) + (s_{1} - s_{2})^{2} \le 2$; on an isotype with $s_{1} + s_{2} + j(j+1) = 2$ (for instance $(1, 1, 0)$, $(\tfrac12, -\tfrac12, 1)$, $(0, 0, 1)$) the massless locus is $\ker\hat{B}$, and on one with $s_{1} + s_{2} + j(j+1) < 2$ it is the eigenspace $2\hat{B}^{\dagger}\hat{B} = \tfrac{\Lambda}{3}\hbar^{2}(2 - s_{1} - s_{2} - j(j+1))$. This is a necessary condition only: the continuum threshold of the join (filed alongside, synthesis.operator-join-point-spectrum-on-positive-energy-modules) is sharper and empties these three isotypes for $\Lambda > 0$.
\item[(iv)] \emph{(No eigenvector of finite energy content for $\Lambda \ge 0$.)} The join changes the oscillator number by $-4, -2, 0, 2, 4$ only, and its part raising it by four is $2(1+\lambda)^{2}\,[a^{\dagger}_{1}a^{\dagger}_{2}]\,[b^{\dagger}_{1}b^{\dagger}_{2}]$, the product of the two creation brackets $[a^{\dagger}_{1}a^{\dagger}_{2}] = \epsilon^{AB}a^{\dagger}_{1A}a^{\dagger}_{2B}$ and $[b^{\dagger}_{1}b^{\dagger}_{2}]$, which is injective on $\mathcal{F}_{0}$ for $\lambda \ne -1$. Hence for every $\mu \in \C$ the kernel of $\hat{m}^{2} - \mu$ on $\mathcal{F}_{0}$ is zero whenever $\lambda \ne -1$, in particular for every $\Lambda \ge 0$: there the join has no eigenvector of finite energy content in any sector, massless or massive, so no zero modes of finite energy content in any two neighbouring sectors, and the constant, which is a zero mode in the polynomial realisation $\bar{Z} = -\hbar\partial$, has no counterpart. \emph{For $\Lambda < 0$ this fails:} at $\lambda = -1$, the Fock scale matched to a frozen point of negative $\Lambda$ (in general $\lambda s^{4} = -1$), the pure terms of $\hat{B}$ cancel, $\hat{B} = -2([a_{1}b^{\dagger}_{2}] + [b^{\dagger}_{1}a_{2}])$ preserves the oscillator number, so does $\hat{m}^{2}$, and its kernel on the states of oscillator number two is three-dimensional, one zero mode in each of the sectors $(\tfrac12, -\tfrac12)$, $(-\tfrac12, \tfrac12)$, $(0, 0)$, of internal spin $1$ and in $\ker\hat{B}$ (for $(0, 0)$: $a^{\dagger}_{1}\cdot b^{\dagger}_{1} - a^{\dagger}_{2}\cdot b^{\dagger}_{2}$ on the vacuum); at a mismatched scale the same zero modes are infinite sums, so for $\Lambda < 0$ the finite-energy statement is realisation-dependent and the join has normalisable zero modes.
\item[(v)] \emph{(Reading, argued.)} For $\lambda > 0$ the dilation of the flat chart by $\rho$ sends $I_{1}$ to $\rho^{-1}I_{\rho^{2}}$ and is implemented unitarily on $\mathcal{F}$, so the spectrum of the join at $\lambda$ is $\lambda$ times its spectrum at $\lambda = 1$, where $\hat{B} = 2([a_{1}a_{2}] + [b^{\dagger}_{1}b^{\dagger}_{2}])$; for $\lambda < 0$ it is $|\lambda|$ times its $\lambda = -1$ form, which commutes with the oscillator number and has pure point spectrum. For $\Lambda > 0$ the massless states of the positive-energy modules, where (iii) allows them, are generalised eigenvectors, not in $\mathcal{F}_{0}$ by (iv) and not in $\mathcal{F}$ by the point-spectrum result filed alongside, so the seed of Proposition \claimref{synthesis.operator-join-seed-has-no-diagonal-matrix-elements} between neighbouring massless sectors is a matrix element between generalised states of the join, not an expectation in a normalisable massless state.
\end{enumerate}

## technical
The operator join of two conformal spinors is written here on the oscillator realisation of the positive-energy modules, the Fock space in which each constituent's four twistor oscillators are split into two annihilation and two creation operators by the positive Hermitian structure. In that space the store's conjugation of the bracket is the genuine adjoint, so the join is twice a positive operator plus a number fixed by the two constituent helicities and the internal spin. That number is a lower bound on the join, which for positive cosmological constant rules out massless states in every sector with s_1 + s_2 + j(j+1) above 2 (the continuum threshold, filed alongside, rules out more). Independently, for nonnegative cosmological constant the join raises the oscillator number by at most four, and its top part is multiplication by the product of two creation brackets, which never annihilates a nonzero finite combination of number states; so the join has no eigenvector of finite energy content at all, in any sector and for any eigenvalue, and the zero mode of the polynomial realisation (the constant) has no counterpart. For negative cosmological constant the picture is different: at the Fock scale matched to the frozen point the join conserves the oscillator number and has normalisable zero modes already at oscillator number two.

## lay
A particle made of two twistors has a mass operator built from their joint bracket. This result places that operator on the states that have positive energy. There it is a positive piece plus a fixed number set by the two handednesses and their relative spin; for a positive cosmological constant that number alone forbids massless states in most sectors. Separately, for a cosmological constant that is zero or positive, the operator always pushes some of the state up to a higher energy level and cannot be made to cancel there, so no state built from finitely many energy levels can be an exact eigenstate, massless or not; that no normalisable massless state exists at all, for positive cosmological constant, is the companion result filed alongside. For a negative cosmological constant the conclusion reverses: in the matched description the operator conserves the energy level and has exact massless states at the second level.

## one-liner
In the oscillator realisation of the positive-energy modules $\hat{m}^{2} = 2\hat{B}^{\dagger}\hat{B} + \tfrac{\Lambda}{3}\hbar^{2}(s_{1} + s_{2} + j(j+1) - 2)$ on each isotype, so for $\Lambda > 0$ massless states need $2\max(s_{1}, s_{2}) + (s_{1} - s_{2})^{2} \le 2$ (a bound the continuum threshold sharpens); for $\Lambda \ge 0$ the join's top band is the product of the two creation brackets, so it has no eigenvector of finite energy content in any sector and the polynomial realisation's constant zero mode has no counterpart; for $\Lambda < 0$ at the matched Fock scale the join conserves the oscillator number and has three zero modes of finite energy content at oscillator number two.
