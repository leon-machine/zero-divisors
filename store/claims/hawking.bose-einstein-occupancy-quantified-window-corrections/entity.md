---
id: hawking.bose-einstein-occupancy-quantified-window-corrections
kind: claim
version: 5
title: Bose-Einstein occupancy, with quantified window corrections
status: proved
region: hawking
subject: thermality
tags: [radiation-spectrum, bosonisation, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
derivations:
- name: main
  uses:
  - hawking.i-state@3
  - hawking.imported-s-wave-bosonic-sector@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T07.py
  tags:
  - label:prop:planck
- kind: check
  ref: check.py::check_detailed_balance_identity
- kind: check
  ref: check.py::check_bilateral_sum_is_planck_factor
- kind: check
  ref: check.py::check_wick_formula_on_window
- kind: check
  ref: check.py::check_window_tail_bound
locators:
  paper: T07
  number: Prop 6.2
  label: prop:planck
  line: 663
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the detailed-balance identity as rational-function identities, the exact telescoping behind the bilateral Planck sum m/(x^{-m} - 1), the Wick formula on an 8-mode window, and the window tail bound. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  env: proposition
  context_refs:
  - hawking.current-commutator-exactly-edge-split
  - hawking.imported-s-wave-bosonic-sector
  typing:
    by: ai-typing-pass
    added:
    - hawking.imported-s-wave-bosonic-sector
    note: 'Added the s-wave sector fact because the statement adopts its linear weight assignment as a
      hypothesis; the current-commutator proposition is cited only to match the finite-window scalar,
      so it is not an edge; the Wick step tacitly relies on the I-state being gauge-invariant quasi-free,
      which is not claimref-cited and was left unedged. Levels pass: the lay now keeps the window being
      centred on the sea; the s-wave modelling input was already kept.'
  repair:
    notes:
    - 'added hawking.i-state after independent review: the Wick computation uses the I-state being gauge-invariant
      and quasi-free'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - hawking.i-state
    - hawking.imported-s-wave-bosonic-sector
---

## formal
Let the ladder carry the linear s-wave weight assignment (the convention T5's Premise (Q) adopts, a modelling input here as there; Fact \claimref{hawking.imported-s-wave-bosonic-sector}): level spacing $\epsilon$, sea at level $0$, I-state occupancies $n_k = (x^{-k} + 1)^{-1}$ with $x = e^{-\beta\epsilon} \in (0,1)$ the Boltzmann factor of the level spacing. Then:
\begin{enumerate}
\item \emph{(Detailed-balance identity.)} For every $k$ and $m \ge 1$, exactly,
\[
n_k - n_{k+m} \;=\; \bigl(x^{-m} - 1\bigr)\; n_{k+m}\,\bigl(1 - n_k\bigr).
\]
\item \emph{(The Planck factor, exactly, in the bilateral limit.)} Summing (1) over $k \in \Z$,
\[
\sum_{k \in \Z} n_{k+m}\,(1 - n_k) \;=\; \frac{m}{x^{-m} - 1} \;=\; \frac{m}{e^{\beta\epsilon m} - 1}:
\]
the current two-point function $\langle a_m^\dagger a_m\rangle_I = \sum_k n_{k+m}(1 - n_k)$ (a Wick computation) is exactly $m$ times the Bose-Einstein value at $\TH$, with no vacuum correction in this normalisation. The factor $m$ is the free-boson normalisation: on the bilateral ladder the currents are used only inside expectations, and $\langle [a_m, a_m^\dagger]\rangle_I = \sum_k (n_k - n_{k+m}) = m$, the telescoped left side of (1), matching the finite-window scalar of Proposition \claimref{hawking.current-commutator-exactly-edge-split}; the unit-normalised boson is $\hat a_m = a_m/\sqrt{m}$, whose occupancy $\langle \hat a_m^\dagger \hat a_m\rangle_I = 1/(e^{\beta\epsilon m} - 1)$ is the $n_-$ of the lift.
\item \emph{(Window tails.)} For the window $[-K, K]$ with the sea at the centre, i.e.\ the sum of (2) restricted to $k \in [-K, K-m]$ (both mode indices inside the window), the bilateral sum exceeds the window sum by a positive amount bounded by $2m\,x^{K - m}/(1 - x)$: exponentially small in the distance from the sea to the edges, in units of the level spacing.
\end{enumerate}

## technical
On the bilateral ladder with level spacing $\epsilon$ and the sea at level $0$, carrying the linear s-wave weight assignment as a modelling input, the I-state occupancies are $n_k = (x^{-k}+1)^{-1}$ with Boltzmann factor $x = e^{-\beta\epsilon} \in (0,1)$. They obey the exact detailed-balance identity $n_k - n_{k+m} = (x^{-m}-1)\,n_{k+m}(1-n_k)$ for every $k$ and every $m \ge 1$.

Summing over $k \in \Z$, the left side telescopes to $1$ in each of the $m$ residue classes modulo $m$, so $\sum_{k} n_{k+m}(1-n_k) = m/(e^{\beta\epsilon m}-1)$. This sum is the current two-point function $\langle a_m^\dagger a_m\rangle_I$, so the unit-normalised boson $\hat a_m = a_m/\sqrt{m}$ has exactly the Bose-Einstein occupancy $1/(e^{\beta\epsilon m}-1)$ at $\TH$. On the window $[-K, K]$ with the sea at the centre, the bilateral sum exceeds the window sum by a positive amount at most $2m\,x^{K-m}/(1-x)$.

## lay
A ladder of fermion levels, filled thermally in the Fermi-Dirac pattern, can be repackaged into collective boson modes. Given the s-wave modelling convention for the ladder, this result shows by an exact algebraic identity that on the infinite ladder those collective modes have exactly the Bose-Einstein thermal occupancy at the Hawking temperature. On a finite window of levels centred on the filled sea, the answer falls short only by a positive amount that shrinks exponentially as the window edges move away from the filled sea.

## one-liner
Under the linear s-wave weight assignment, the I-state gives each unit-normalised current mode exactly the Bose-Einstein occupancy at the Hawking temperature on the bilateral ladder, with a positive finite-window correction that is exponentially small in the distance from the sea to the edges.
