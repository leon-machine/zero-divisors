---
id: synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet
kind: claim
version: 3
title: 'The rung field is odd in the tower; no even doublet in its modes'
status: proved
region: synthesis
subject: quantum-fields
tags: [car-algebra, grading-and-parity, symmetry-breaking, superselection]
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
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'notation: the Hermitian norm renamed sans-serif N'
  version: 3
  source: maintainer pass 2026-11-07 (decisions, second round)
review: draft
derivations:
- name: main
  uses:
  - synthesis.rung-field-on-the-lift-locus@5
  - standard-model.ten-transported-ambient-space-doublets-are@2
  - field-theory.imported-tower-limit@3
  - synthesis.even-slots-need-a-spectator-generator@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_rung_modes_are_a_doublet_pair_of_the_slot_mixing
- kind: check
  ref: check.py::check_even_rung_algebra_has_no_doublet
- kind: check
  ref: check.py::check_rung_field_is_odd_and_its_invariants_are_even_expectations
- kind: check
  ref: check.py::check_spectator_doublet_is_even_and_two_level
- kind: check
  ref: check.py::check_time_direction_gives_a_doublet_that_is_not_a_lorentz_scalar
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.composite-scalars-mean-field-level
  - field-theory.how-close-tower-comes-ccr
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation (Leon, second round, answer 8; DECISIONS H5, consistency-R04 item 4): the rung-field results wrote N for the Hermitian norm of the rung component, N(c) = (|alpha|^2 + |beta|^2)/2, while N = M_P/H is the hierarchy number in the same subject. The norm is now \mathsf{N} (its values \mathsf{N}^*, \mathsf{N}_0, its derivative \partial_{\mathsf{N}}, and W(\mathsf{N})) in formal, proof and the other levels, in every rung-field entity that writes it (14 entities, one batch), so the family stays uniform. The letter was chosen free in the entity and in its subject (standard-model and quantum-fields): R04''s example \mathcal{N} is the store macro \Ncone (the null cone) and the number operator of synthesis.floor-regulator-... in quantum-fields. No content change.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit in the check''s real generator t_2'' = [t_3, t_1] = I_4 t_2 is now the field theory''s unit I_4, which commutes with the rung vectors (coefficients read in span{1, I_4}, as the proof already states); no bare i remains.'
  open_problem: op.qft-bosons-and-the-rung-field
  note: >-
    The problem asks whether the Higgs is elementary (palatial) or composite (tower). The rung field's values are
    the tower's own mode vectors v_4, v_5, w_4, w_5 (the transported doublets of
    standard-model.ten-transported-ambient-space-doublets-are), so the most direct composite reading takes the field
    to be built from those modes. This result closes that reading by exact algebra: the field itself is odd and has
    no expectation in any state invariant under the tower grading (every state of definite mode-number parity, the
    Fock vacuum and every Gibbs state of an even Hamiltonian among them); its invariants are even and appear as
    vacuum expectations of bilinears; and the even algebra of the two rung planes contains no doublet at all, so the
    doublet order parameter of the stored vacuum is not the expectation of anything built from the rung modes. An
    even doublet needs an odd factor from outside the rung planes, as the even slots of
    synthesis.even-slots-need-a-spectator-generator (iv) do; with one such generator it is two-level and obeys the
    canonical anticommutation relations (the time direction gamma_0 meets the hypotheses but gives a doublet that is not a
    Lorentz scalar), so a bosonic doublet in the tower must pair a many-mode doublet fermion field
    with a singlet one and reaches the canonical commutation relations only in the quasi-spin limit of
    field-theory.how-close-tower-comes-ccr (argued in the proof, not checked). What is left for a tower composite is
    therefore a doublet-singlet fermion condensate of the Nambu-Jona-Lasinio kind (stored at mean field), not the
    rung modes. Elementary representation theory: the new content is the reading of the rung field's values as
    tower elements. Transport-convenient.
---

## formal
Let $v_{a}, w_{a}$ ($a = 4, 5$) be the null pairs of the two rung planes, $\{v_{a}, w_{b}\} = \delta_{ab}$ (Fact \claimref{field-theory.imported-tower-limit}), a weak doublet and its conjugate under the slot mixing (\claimref{standard-model.ten-transported-ambient-space-doublets-are}), with $\mathfrak{su}(2)$ acting by commutators with $t_{j} = \sum_{a,b}v_{a}(\tfrac12\sigma_{j})_{ab}w_{b}$, and let $\mathcal{A}$ be the algebra they generate, graded by parity. Let $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$ be the rung field of \claimref{synthesis.rung-field-on-the-lift-locus}, read as an element of $\mathcal{A}$ (coefficients in $\mathrm{span}\{1, I_{4}\}$, which commutes with the rung vectors), and $c^{*} = \bar{\beta}\cdot v + \bar{\alpha}\cdot w$.
\begin{enumerate}
\item \emph{(The field is odd.)} $c$ is odd, so $\omega(c) = 0$ for every state $\omega$ of $\mathcal{A}$ invariant under the grading. Its invariants are even: $c^{2} = Q(c)$, $\{c^{*}, c\} = 2\mathsf{N}(c)$, and in the Fock state annihilated by $w_{4}, w_{5}$, $\omega(c^{*}c) = |\alpha|^{2}$, $\omega(cc^{*}) = |\beta|^{2}$, so $m(c) = \tfrac12\omega(c^{*}c - cc^{*})$.
\item \emph{(No even doublet.)} On $\mathcal{A}$, sixteen-dimensional, the isospin Casimir has eigenvalue $0$ with multiplicity $5$ and $2$ (isospin one) with multiplicity $3$ on the even part, and $\tfrac34$ (isospin one-half) with multiplicity $8$ on the odd part: an element of $\mathcal{A}$ is a doublet only if it is odd. So no even (bosonic) element built from the rung modes alone carries the rung field's doublet quantum numbers, and the doublet order parameter of a charge-preserving vacuum of the rung field is not the expectation of any such element.
\item \emph{(A spectator.)} If $g$, $g^{2} = 1$, anticommutes with the rung vectors and commutes with the $t_{j}$ (a generator outside the rung planes, as in \claimref{synthesis.even-slots-need-a-spectator-generator}(iv)), then $x_{a} = v_{a}g$ is an even doublet with $x_{a}^{*} = gw_{a}$, $\{x_{a}, x_{b}^{*}\} = \delta_{ab}$, $\{x_{a}, x_{b}\} = 0$, $x_{a}^{2} = 0$ and $[x_{a}, x_{a}^{*}] = 2v_{a}w_{a} - 1$: it obeys the canonical anticommutation relations, not $[x, x^{*}] = 1$. The time direction $\gamma_{0}$ meets these hypotheses ($\gamma_{0}^{2} = 1$, anticommuting with the rung vectors), but $v_{a}\gamma_{0}$ does not commute with the boost bivector $\gamma_{0}\gamma_{1}$, so it is not a Lorentz scalar: an even doublet that is a Lorentz scalar needs $g$ outside both spacetime and the rung planes.
\end{enumerate}

## technical
Read as an element of the tower, the rung field $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$ is odd, so every state invariant under the tower grading gives it zero expectation; its invariants are even, $c^{2} = Q(c)$ and $\{c^{*}, c\} = 2\mathsf{N}(c)$, and in the Fock state annihilated by the $w_{a}$, $\omega(c^{*}c) = |\alpha|^{2}$ and $\omega(cc^{*}) = |\beta|^{2}$, so $m = \tfrac12\omega(c^{*}c - cc^{*})$.

On the sixteen-dimensional algebra of the two rung planes the isospin Casimir is $0$ on five and $2$ on three even dimensions and $\tfrac34$ on all eight odd ones: only odd elements are doublets, so nothing bosonic built from the rung modes alone carries the rung field's quantum numbers. With a generator $g$ from outside the rung planes, $x_{a} = v_{a}g$ is an even doublet, but it obeys the canonical anticommutation relations ($\{x_{a}, x_{b}^{*}\} = \delta_{ab}$, $x_{a}^{2} = 0$), not the canonical commutation relations. The time direction $\gamma_{0}$ would serve as $g$, but then $v_{a}\gamma_{0}$ is not a Lorentz scalar; a Lorentz-scalar even doublet needs a generator outside both spacetime and the rung planes.

## lay
The series' Higgs candidate, the rung field, takes its values in four special directions of the series' algebra, the same directions that serve as fermion creation and annihilation operators. Read that way the field itself is fermion-like and can have no average value, so it cannot be the condensate. Built purely from those four directions, no boson-like quantity has the Higgs field's charges at all. Borrowing one further direction gives a boson-like quantity with the right charges, but it still obeys fermion rules, and if the borrowed direction is the time direction the quantity is not even a scalar. The route this leaves for a composite Higgs, argued here rather than proved, is a condensate of further fermion fields, as in the Nambu-Jona-Lasinio picture, not of the rung directions themselves.

## one-liner
The rung field read in the tower is odd (zero expectation in every grading-invariant state) with even invariants $c^{2} = Q$, $\{c^{*}, c\} = 2\mathsf{N}$; the even algebra of the rung planes is five singlets and a triplet, so no bosonic doublet is built from the rung modes, and the even doublet $v_{a}g$ with an outside generator obeys the CAR.
