---
id: singularity.two-kms-functionals-sign
kind: claim
version: 7
title: The two KMS functionals, and the sign in $Z$
status: proved
region: singularity
subject: descent
tags: [modular-theory, grading-and-parity]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 6
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 7
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - singularity.kms-uniqueness-factor@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.23
- kind: check
  ref: check.py::check_ungraded_kms_is_unique_gibbs_state
- kind: check
  ref: check.py::check_graded_kms_is_parity_twisted_not_a_state
- kind: check
  ref: check.py::check_plus_one_is_the_two_state_sum
locators:
  paper: T05
  number: Prop 7.23
  label: prop:statistics
  line: 1915
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6 -> 7. The flow Ad(e^{it omega K}) and its continuation alpha_{i beta} act on the completed-pair atom''s mode factor, so by U2 the unit is J = e_2 e_3 (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited as a mention): Ad(e^{J t omega K}), alpha_{J beta}(a) = e^{-beta omega K} a e^{beta omega K}, the KMS relation in the core result''s form; the proof reads singularity.kms-uniqueness-factor (stated over span{1, I_4}) over span{1, J}, said where. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the flow Ad(e^{it omega K}) and its continuation alpha_{i beta} act on the atom mode factor, whose modes anticommute with I_4 (conventions, known limit 1), so I_4 is not its unit.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the ungraded and graded KMS functionals on the mode factor as computed one-dimensional kernels (Gibbs state, parity-twisted functional), Z = 1 + x, Z_Gamma = 1 - x, the negative twisted occupancy, and Z as the two-state sum of the module. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'Folded-state-selection (R) fix: the formal level''s (R) now carries a claimref to T05''s premise singularity.r-regularity-fixed-locus, so it is not read as the folded note''s regularity premise.'
  source_formal: "On the mode factor with flow $\\alpha_t = \\operatorname{Ad}(e^{it\\omega K})$, let $\\Gamma := 1 - 2N = -\\sigma$ be the mode's fermion parity, and for homogeneous $b$ write $\\epsilon_b = \\pm 1$ for even and odd $b$. Fix $\\beta > 0$.\n\\begin{enumerate}\n\\item The functionals $\\phi = \\tr(\\varrho\\,\\cdot\\,)$ satisfying the \\emph{ungraded} KMS identity $\\phi(ab) = \\phi\\bigl(b\\,\\alpha_{i\\beta}(a)\\bigr)$ for all $a, b$ are the multiples of $\\tr(e^{-\\beta\\omega K}\\,\\cdot\\,)$; normalised, this is the unique KMS state, with partition function $Z = 1 + e^{-\\beta\\omega}$ and occupancy $(e^{\\beta\\omega} + 1)^{-1}$.\n\\item The functionals satisfying the \\emph{graded} identity $\\phi(ab) = \\epsilon_b\\,\\phi\\bigl(b\\,\\alpha_{i\\beta}(a)\\bigr)$ for all $a$ and homogeneous $b$ are the multiples of $\\tr(\\Gamma e^{-\\beta\\omega K}\\,\\cdot\\,)$; normalised, this is the parity-twisted functional with $Z_\\Gamma = 1 - e^{-\\beta\\omega}$ and ``occupancy'' $-e^{-\\beta\\omega}/(1 - e^{-\\beta\\omega}) < 0$: it is not a state.\n\\item The $+1$ of the Fermi-Dirac denominator is $Z = 1 + e^{-\\beta\\omega}$: the two terms are the two states of the module, one per power of $v^{*}$ before $(v^{*})^{2} = 0$, and the sign between them is $+$ for the KMS state and $-$ for the twisted functional. The gluing condition of (R), which reverses the order of $a$ and $b$ without a sign, is the ungraded identity, and selects the state.\n\\end{enumerate}"
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: Removed the mechanical transport-algorithm edge since the proof is KMS uniqueness plus a trace computation on the mode factor; the Fermi-Dirac and Matsubara statements the paper calls standard have no imported claim in the store, so no standard-route derivation was added.
  env: proposition
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - $\alpha_{i\beta}$ in the graded and ungraded KMS identities (complex analysis)
---

## formal
On the mode factor of the completed pair, whose scalars are $\mathrm{span}\{1, J\}$ with $J = e_{2}e_{3}$ the complex unit of the atom (\claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}), with flow $\alpha_t = \operatorname{Ad}(e^{J t\omega K})$, let $\Gamma := 1 - 2N = -\sigma$ be the mode's fermion parity, and for homogeneous $b$ write $\epsilon_b = \pm 1$ for even and odd $b$. Fix $\beta > 0$.
\begin{enumerate}
\item The functionals $\phi = \tr(\varrho\,\cdot\,)$ satisfying the \emph{ungraded} KMS identity $\phi(ab) = \phi\bigl(b\,\alpha_{J\beta}(a)\bigr)$ for all $a, b$, with $\alpha_{J\beta}(a) = e^{-\beta\omega K}a\,e^{\beta\omega K}$, are the multiples of $\tr(e^{-\beta\omega K}\,\cdot\,)$; normalised, this is the unique KMS state, with partition function $Z = 1 + e^{-\beta\omega}$ and occupancy $(e^{\beta\omega} + 1)^{-1}$.
\item The functionals satisfying the \emph{graded} identity $\phi(ab) = \epsilon_b\,\phi\bigl(b\,\alpha_{J\beta}(a)\bigr)$ for all $a$ and homogeneous $b$ are the multiples of $\tr(\Gamma e^{-\beta\omega K}\,\cdot\,)$; normalised, this is the parity-twisted functional with $Z_\Gamma = 1 - e^{-\beta\omega}$ and ``occupancy'' $-e^{-\beta\omega}/(1 - e^{-\beta\omega}) < 0$: it is not a state.
\item The $+1$ of the Fermi-Dirac denominator is $Z = 1 + e^{-\beta\omega}$: the two terms are the two states of the module, one per power of $v^{*}$ before $(v^{*})^{2} = 0$, and the sign between them is $+$ for the KMS state and $-$ for the twisted functional. The gluing condition of (R) (Premise \claimref{singularity.r-regularity-fixed-locus}), which reverses the order of $a$ and $b$ without a sign, is the ungraded identity, and selects the state.
\end{enumerate}

## technical
On the mode factor, over the atom's complex unit $J = e_2e_3$, with flow $\alpha_t = \operatorname{Ad}(e^{Jt\omega K})$ and fermion parity $\Gamma = 1 - 2N$, fix $\beta > 0$. The functionals satisfying the ungraded KMS identity $\phi(ab) = \phi(b\,\alpha_{J\beta}(a))$ are the multiples of $\tr(e^{-\beta\omega K}\,\cdot\,)$; normalised, this is the unique KMS state, with $Z = 1 + e^{-\beta\omega}$ and occupancy $(e^{\beta\omega} + 1)^{-1}$. The functionals satisfying the graded identity, with a sign $\epsilon_b = -1$ for odd $b$, are the multiples of $\tr(\Gamma e^{-\beta\omega K}\,\cdot\,)$, with $Z_\Gamma = 1 - e^{-\beta\omega}$ and negative occupancy, so this functional is not a state.

The $+1$ of the Fermi-Dirac denominator is therefore the $+$ sign between the two module states in $Z$. The gluing condition of (R), which reverses the order of $a$ and $b$ without a sign, is the ungraded identity, and it selects the state.

## lay
For a single fermionic mode there are two versions of the equilibrium condition, differing by a sign for odd operators. The version without the sign gives the genuine thermal state, with the familiar Fermi-Dirac occupation. The version with the sign gives something with a negative occupation, which is not a physical state at all. The plus sign in the Fermi-Dirac formula comes from this choice, and the paper's regularity condition picks the version without the sign.

## one-liner
On one fermionic mode the ungraded KMS identity gives the Fermi-Dirac state with $Z = 1 + e^{-\beta\omega}$, while the graded identity gives a parity-twisted functional with $Z_\Gamma = 1 - e^{-\beta\omega}$ that is not a state.
