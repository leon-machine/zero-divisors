---
id: rungs.rung-spinor-module-mixings
kind: claim
version: 6
title: The $n$-rung spinor module and its mixings
status: proved
region: rungs
subject: tower
tags: [spinor-modules, pairing-and-bogoliubov, ladder-pairs, hypotheses-s-r-c]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 5
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 6
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - rungs.imported-fock-representation-bogoliubov-group@4
  - rungs.imported-ladder-automorphism-group-no-lepton@4
  - rungs.imported-spinor-identification-witt-data-line@4
  - rungs.imported-tower-one-qubit-per-rung@4
  - std-algebra.complexification@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_rungs.py
  tags:
  - label:thm:rungs
- kind: check
  ref: check.py::check_spinor_module_irreducible_graded
- kind: check
  ref: check.py::check_split_unitaries_act_by_exterior_powers
- kind: check
  ref: check.py::check_majoranas_and_bogoliubov_dimension
- kind: check
  ref: check.py::check_number_preserving_part_and_double_cover
- kind: check
  ref: check.py::check_spin10_irreducible_on_each_half
- kind: check
  ref: check.py::check_cell_action_ranks_and_faithfulness
locators:
  paper: T12-rungs
  number: Thm 2.1
  label: thm:rungs
  line: 235
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U3) the module''s complex scalar is the central pseudoscalar of the odd extension, Cl(2+n,4+n) (x) C = Cl(3+n,4+n) with unit I_{7+2n} (I_13 at n = 3; std-algebra.complexification-is-the-odd-extension), stated once in clause (1): the generator (i I_3, -i I_3) of K and its eigenvalue i(j - k) in the proof became (I_13 I_3, -I_13 I_3) and I_13(j - k); the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the generator (i I_3, -i I_3) of u(3) + u(3) and its eigenvalue i(j - k) act on the complexified module of T_n (x) C, whose scalar commutes with every generator, so no pseudoscalar can stand for it.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.complexification where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Fock module of Cl(2+n,4+n) for n <= 3 (relations, irreducibility, bigrading, chirality), Lambda(B + A) for rational unitaries, the Majoranas and dim so(6+2n), Spin(10) irreducible on each half, the det^(-1/2) twist and double cover, and the n = 3 and n = 2 cell-action ranks. Version 1 -> 2. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 2 -> 3.'
  env: theorem
  context_refs:
  - rungs.imported-results-t12-used-registration
  - standard-model.under-s-composites-state-space-spinor
  typing:
    by: ai-typing-pass
    note: 'All four uses are invoked in the proof and kept; the context references to the registration
      fact and the (S) generation fact are comparisons in the statement, not premises of the proof, so
      they were not added. Levels pass: the lay level now says the sixteen-state half is a generation
      only under Hypothesis (S).'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$(iI_3, -iI_3)$ in $\uu(3) \oplus \uu(3)$ and its eigenvalue $i(j - k)$: complex matrices acting
      on the complexified module $\Lambda^\bullet R_3 \otimes \Lambda^\bullet W$ of $T_n \otimes \C$ (matrix
      algebras over $\C$, complexified algebra); $W$ lies in the ground, where $I_4$ does not commute with
      the vectors. Doubtful as a U(1) charge on modes'
---

## formal
Let $\Cl(2{+}n, 4{+}n)$ be the $n$-th rung of the tower above $\Cl(2,4)$, with new isotropic directions $v_{1}, \ldots, v_{n}$ spanning $R_{n} \cong \C^{n}$ after complexification. The complexification is the odd extension $\Cl(2{+}n, 4{+}n) \otimes \C = \Cl(3{+}n, 4{+}n)$, whose complex unit is the central pseudoscalar $I_{7+2n} = I_{6+2n}e$ ($I_{6+2n}^{2} = -1$ at every rung, so $Q(e) = +1$; \claimref{std-algebra.complexification-is-the-odd-extension}); numbers below are read in $\mathrm{span}\{1, I_{7+2n}\}$, $I_{13}$ at $n = 3$. Then:
\begin{enumerate}
\item Its complexified spinor module is $\Lambda^{\bullet}(W \oplus R_{n}) = \Sp \otimes \Lambda^{\bullet}\C^{n}$, of dimension $2^{3+n}$, graded by $(j, k)$ with $j$ the number of new modes and $k$ the number of old pairs occupied, and irreducible; its chirality is the parity of $j + k$. At $n = 2$ this is the five-mode ledger of Hypothesis (S), with the same grading and the same chirality rule.
\item The subgroup of unitaries of $W \oplus R_{n}$ preserving the two summands is $U(3) \times U(n)$, and it acts on the module as $\Lambda^{\bullet}(B \oplus A)$: on $\Lambda^{j}R_{n} \otimes \Lambda^{k}W$ by $\Lambda^{j}(A) \otimes \Lambda^{k}(B)$. At $n = 2$ this is exactly the action Hypothesis (S) prescribes.
\item The Bogoliubov group of the $3 + n$ modes is the compact orthogonal group $O(6{+}2n)$, implemented by $\mathrm{Pin}(6{+}2n)$. At $n = 2$ the connected part is $\mathrm{Spin}(10)$, acting irreducibly on each chirality half; the half of even $j + k$ is the sixteen-dimensional half-spin representation, which under (S) is the generation of Fact \claimref{standard-model.under-s-composites-state-space-spinor}. The number-preserving subgroup of $\mathrm{Spin}(6{+}2n)$ is a double cover of $U(3{+}n)$, acting as $\Lambda^{\bullet} \otimes \det^{-1/2}$; on the determinant-one subgroup this agrees with the action of (2), and it is the determinant-one part that (S) uses (Fact \claimref{rungs.imported-results-t12-used-registration}). At $n = 3$ the group is $\mathrm{Spin}(12)$, and the split-and-number-preserving $U(3) \times U(3)$, of dimension eighteen, acts faithfully on the module, while its action on the cell sector $\Lambda^{1}R_{3} \otimes \Lambda^{1}W = \C^{3} \otimes \C^{3}$ has kernel $K = \{(\lambda I_{3}, \lambda^{-1}I_{3})\}$ and image the seventeen of Fact \claimref{rungs.imported-ladder-automorphism-group-no-lepton}: the seventeen is the $n = 3$ cell action, exactly as the twelve of $S(U(2) \times U(3))$ is the $n = 2$ cell action of a thirteen-dimensional group on the module. (At $n = 3$ the trace-free subalgebra $\{\tr X + \tr X' = 0\}$ contains $K$'s generator, so the seventeen is the quotient and not that subalgebra, unlike $n = 2$ where $\mathfrak{s}(\uu(2) \oplus \uu(3))$ maps isomorphically onto the cell action. This clause is a relabelling: the cell sector is $\C^{3} \otimes \C^{3}$ with the group Fact \claimref{rungs.imported-ladder-automorphism-group-no-lepton} already has, and nothing about the tower enters.)
\item The dimension counts: $2^{3+n} = 8, 16, 32, 64$ for $n = 0, 1, 2, 3$; $\dim \mathfrak{so}(6{+}2n) = 15, 28, 45, 66$; $\dim(\uu(3) \oplus \uu(n)) = 9, 10, 13, 18$.
\end{enumerate}

## technical
For the $n$-th rung $\Cl(2+n,4+n)$ above $\Cl(2,4)$, with new isotropic directions spanning $R_n \cong \C^n$ after complexification, the complexified spinor module is $\Lambda^\bullet(W \oplus R_n) = \Sp \otimes \Lambda^\bullet\C^n$, irreducible of dimension $2^{3+n}$, bigraded by the number $j$ of new modes and $k$ of old pairs occupied, with chirality the parity of $j + k$. The summand-preserving unitaries $U(3) \times U(n)$ act on $\Lambda^j R_n \otimes \Lambda^k W$ by $\Lambda^j(A) \otimes \Lambda^k(B)$; at $n = 2$ the module, grading, chirality and action are those of Hypothesis (S).

The Bogoliubov group of the $3+n$ modes is $O(6+2n)$, implemented by $\Pin(6+2n)$; at $n = 2$ its connected part $\Spin(10)$ acts irreducibly on each chirality half, the even half being the sixteen-dimensional half-spin representation. The number-preserving subgroup of $\Spin(6+2n)$ double covers $U(3+n)$, acting as $\Lambda^\bullet \otimes \det^{-1/2}$, which agrees with the split action on the determinant-one part. At $n = 3$, $U(3) \times U(3)$ acts faithfully on the module, while on the cell sector $\C^3 \otimes \C^3$ it has kernel $K = \{(\lambda I_3, \lambda^{-1} I_3)\}$ and image the seventeen-dimensional group of the ladder. The dimensions are $2^{3+n} = 8, 16, 32, 64$, $\dim \mathfrak{so}(6+2n) = 15, 28, 45, 66$ and $\dim(\uu(3) \oplus \uu(n)) = 9, 10, 13, 18$ for $n = 0, 1, 2, 3$.

## lay
Each rung of the tower above the conformal algebra adds new fermionic modes to the three already present, and the full state space is built by filling any combination of them, doubling in size with every new mode. The symmetries that keep old and new modes separate act on this space in a definite way, and with two new modes they match the structure the series' Hypothesis (S) prescribes; Spin(10) then acts on a sixteen-state half, which under that hypothesis is one generation. With three new modes the symmetry acting on the mixed sector is the seventeen-dimensional group found earlier, which the result records as a relabelling.

## one-liner
The $n$-th rung above $\Cl(2,4)$ has irreducible spinor module $\Sp \otimes \Lambda^\bullet\C^n$ of dimension $2^{3+n}$ and Bogoliubov group $O(6+2n)$, matching at $n = 2$ the five-mode ledger of Hypothesis (S) and at $n = 3$ the seventeen-dimensional cell action.
