---
id: note.singularity.setting-chain-transport-algorithm
kind: note
version: 1
title: The chain as the transport algorithm
status: setting
subject: singularity
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
- singularity.degeneration-exactly
locators:
  paper: T05
  number: Setting
  section: Introduction
  line: 1264
  subsection: The chain as the transport algorithm
---

## formal
The transport principle's operational form is the six-step transport algorithm of the root paper, \cite[\S 8.1, Table 1]{ButlerT1}, every step of which is licensed there by a theorem; and the worked-instance remark of that paper, \cite[Rem.~8.3]{ButlerT1}, promises that the present paper mirrors the algorithm row for row. Table \ref{tab:algmap} makes the promise explicit, and the chain is \emph{numbered by the algorithm}: Steps 1 to 3 coincide with the algorithm's; the algorithm's Step 4 (compute in the completion) expands into Steps 4a to 4e, because the computation in the completion is where the temperature, the statistics and the Planck sector are produced; Step 5 (descend, and state what descent costs) is the descent computation, quantified exactly by the deficit theorem; and Step 6 (iterate, or stop) is discharged by the mod-8 clock stopping at $d \equiv 6$, with Steps 6a and 6b counting what the boundary mode space at which it stops holds. The reader who wants each step's licence should read the table's middle column as a citation list into T1 \cite{ButlerT1}. The dictionary is: its Steps 1 to 3 are unchanged; its Steps 4 to 8 are here 4a, 4b, 4c, 4d, 4e; its Steps 9 and 10 are here 6a and 6b; and the quantification of the descent, folded into its Step 4, stands here as Step 5.

 \begin{tabular}{>{ \arraybackslash}p{2.9cm}>{ \arraybackslash}p{3.2cm}>{ \arraybackslash}p{6.6cm}}
\toprule
Algorithm step \cite[\S 8.1]{ButlerT1} & Warrant there & Instantiated here \\
\midrule
1. locate the failure & Lem.~2.1 & Step 1 (\S\ref{sec:locate}): from the field equations; nowhere at $r > 0$, unavoidably at $r = 0$; in $\Omega$, not in $\det \hb$ \\
2. diagnose the type & Prop.~3.3; Thms 3.6, 3.9 & Step 2 (\S\ref{sec:diagnose}): type N (null kernel direction, Prop.~\claimref{singularity.degeneration-exactly}); type C excluded, $p - q \equiv 6 \bmod 8$ \\
3. apply the rule & Thms 4.10, 4.13, 4.19 & Step 3 (\S\ref{sec:ascent}): Rule 1, $\Cl(1,3) \to \Cl(2,4)$, the CAR pair installed \\
4. compute in the completion & Thm 4.10; Prop.~4.21 & Steps 4a to 4e (\S\S\ref{sec:operators}-\ref{sec:photons}): the transport instantiated, the plane and the rate, modular flow, $\TH$, Fermi-Dirac, Planck sector \\
5. descend, and state what descent costs & Lem.~4.23; Prop.~7.5; Thm 7.6 & Step 5 (\S\ref{sec:descent}): $\EN$, the deficit $\rel{\rho}{\EN\rho}$, the quanta correlations; applied in Steps 4d, 6b and the model (\S\ref{subsec:descentapplied} in numbers) \\
6. iterate, or stop & Thm 7.1; Prop.~7.4 & Steps 6a and 6b (\S\S\ref{sec:capacity}-\ref{sec:page}): the tower stops at $d \equiv 6$ by T3 \cite{ButlerT3}, and the boundary mode space at which it stops is counted \\
\bottomrule
\end{tabular}

\emph{The transport algorithm of T1 \cite{ButlerT1}, instantiated. The middle column names the theorems of the root paper licensing each step; the right column names where this paper executes it.}

## technical
pending

## lay
pending

## one-liner
pending
