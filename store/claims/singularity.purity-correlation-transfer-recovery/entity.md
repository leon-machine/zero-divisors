---
id: singularity.purity-correlation-transfer-recovery
kind: claim
version: 3
title: Purity, correlation transfer, and recovery
status: proved
region: singularity
subject: entropy
tags: [finite-models, entanglement, radiation-spectrum]
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
review: typed
derivations:
- name: main
  uses:
  - singularity.parity-protection@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:12.3
- kind: check
  ref: check.py::check_global_purity_and_pure_radiation_at_completion
- kind: check
  ref: check.py::check_pair_coherence_damped_by_visibility
- kind: check
  ref: check.py::check_correlators_carry_the_gate_pattern
locators:
  paper: T05
  number: Prop 12.3
  label: prop:transfer
  line: 2346
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: global purity, the coherence c1 s1 gamma and pair purity, and the exchanged correlators on six pair choices. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: Kept parity protection, used in clause (3) for the thermal single-qubit marginals.
---

## formal
In the model with two pairs and one controlled-$Z$ between $L_1$ and $L_2$ (the minimal scrambled instance; the script runs larger ones):
\begin{enumerate}
\item the global state is pure at every stage, and at completion the radiation alone carries it: $S(R_{\mathrm{all}}) = 0$ exactly;
\item the pair coherence is damped by exactly the visibility $\gamma = c_2^2 - s_2^2 = \cos 2\theta_2$: the two-qubit marginal of $(R_1, L_1)$ has coherence $c_1 s_1 \gamma$ in place of $c_1 s_1$, so its R\'enyi-2 purity drops from $1$ to $c_1^4 + s_1^4 + 2 c_1^2 s_1^2 \gamma^2$: two-body correlations alone no longer hold the whole pair;
\item the deficit is not lost but relocated to three-body correlations, and it is recoverable: the correlator $\langle X_{R_1} X_{L_1} \rangle$ equals $2 c_1 s_1 \gamma$ while the dressed correlator $\langle X_{R_1} X_{L_1} Z_{L_2} \rangle$ equals $2 c_1 s_1$ exactly, the visibility $\gamma$ having moved from the undressed correlator to the dressed one, so the pattern of applied gates (the message) is determined by multi-qubit correlators although every single-qubit state, by Lemma \claimref{singularity.parity-protection}, is identically thermal.
\end{enumerate}

## technical
In the model with two pairs and one controlled-$Z$ between $L_1$ and $L_2$, the global state is pure at every stage and at completion $S(R_{\mathrm{all}}) = 0$. The gate damps the coherence of the pair $(R_1, L_1)$ by the visibility $\gamma = c_2^2 - s_2^2$, so its Rényi-2 purity drops from $1$ to $c_1^4 + s_1^4 + 2c_1^2 s_1^2\gamma^2$.

The deficit is relocated, not lost: $\langle X_{R_1}X_{L_1}\rangle = 2c_1 s_1\gamma$ while the dressed correlator gives $\langle X_{R_1}X_{L_1}Z_{L_2}\rangle = 2c_1 s_1$, so the gate pattern is read from multi-qubit correlators although every single qubit is thermal.

## lay
In the smallest scrambled version of the model, the radiation ends up in a pure state, so nothing is lost. Scrambling weakens the correlation within an emitted pair, but the missing correlation reappears in a three-quantum correlation. Measuring those correlations reveals which scrambling was applied, even though each quantum on its own looks thermal.

## one-liner
In the minimal scrambled model the radiation ends pure, and the pair coherence damped by scrambling reappears exactly in a three-qubit correlator.
