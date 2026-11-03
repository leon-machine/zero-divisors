---
id: note.singularity.setting-model
kind: note
version: 1
title: The model
status: setting
subject: descent
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
comments_on:
- singularity.modular-descent
- singularity.no-attic-derived-model
locators:
  paper: T05
  number: Setting
  section: 'The finite-mode model: the dissolution step by step'
  line: 2322
  subsection: The model
---

## formal
Qubits stand for modes. At emission event $k$ ($k = 1, \dots, n$) a thermofield pair is created between a radiation qubit $R_k$ and a window qubit $L_k$:
\[
|\psi_k\rangle \;=\; c_k\,|0_{R_k} 0_{L_k}\rangle + s_k\,|1_{R_k} 1_{L_k}\rangle, \qquad c_k = \cos\theta_k, \quad s_k = \sin\theta_k, \quad \tan^2\theta_k = e^{-\omega_k/\TH} ,
\]
the qubit image of Theorem \claimref{singularity.modular-descent}'s state, with rational data (the script uses $(c_k, s_k) = (\tfrac45, \tfrac35), (\tfrac45, \tfrac35), (\tfrac45, \tfrac35), (\tfrac{12}{13}, \tfrac{5}{13})$ for $k = 1, \dots, 4$; every pair has $c_k > s_k$, so every $\omega_k > 0$). The window holds at most $N_{\max} = 2$ qubits; while $|L| \leq N_{\max}$ nothing else happens (Phase I). When an emission would exceed capacity, the model applies a \emph{scrambling unitary} $U$ to the window, diagonal in the number basis (a circuit of controlled-$Z$ gates, entries $\pm 1$, encoding whatever pattern the dynamics carries, including any infalling message), and then \emph{evicts} the oldest window qubit: the evicted qubit is transferred to the radiation as a late quantum (Phase II). This implements the inputs of Section \ref{subsec:eviction} with a window that fills to $N_{\max} = 2$ over the first two events and then stays full until it is finally emptied: the no-attic property of Proposition \claimref{singularity.no-attic-derived-model} holds because the evicted qubit itself joins $R$, (I) because each pair arrives fresh, and (L$_E$) because the scrambling is diagonal. At the end all window qubits have been evicted and the radiation holds all $2n$ qubits.

## technical
pending

## lay
pending

## one-liner
pending
