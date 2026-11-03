---
id: note.transport.setting-transport-algorithm
kind: note
version: 1
title: The transport algorithm
status: setting
subject: completion
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.transport-algorithm
- transport.noinverse
- transport.existence-locus-type-n
- transport.existence-classification-type-c
locators:
  paper: T01
  number: Setting
  section: The transport principle, and the algorithm
  line: 1624
  subsection: The transport algorithm
---

## formal
\begin{tabular}{c>{ \arraybackslash}p{3.5cm}>{ \arraybackslash}p{4.1cm}>{ \arraybackslash}p{4.3cm}}
\toprule
Step & Question answered & Instrument & Warrant \\
\midrule
1 & where does division fail? & the case at hand & Lemma \claimref{transport.noinverse} \\
2 & which of the three obstructions is it? & $pq \neq 0$; $p - q \equiv 1 \bmod 4$ & Prop.\ \claimref{transport.existence-locus-type-n}; Thms \claimref{transport.existence-classification-type-c}, \claimref{transport.exhaustiveness-every-zero-divisor-annihilated-idempotent} \\
3 & what is the minimal repair, and what does it adjoin? & $(+1,+1)$; one generator; nothing & Thms \claimref{transport.minimality}, \claimref{transport.representation-independent-minimality-completion}, \claimref{transport.one-generator-minimal-minimal-completions-classified}, \claimref{transport.embedding-independent-minimality-fusion}; Prop.\ \claimref{transport.type-p-self-repairing} \\
4 & how is the value at the obstruction computed? & lift, then $\iota(s,x,t) = (2t,x,\tfrac12 s)$ & Thm \claimref{transport.totality}, Prop.\ \claimref{transport.swap-rescale-normal-form} \\
5 & what does descent back to the original algebra cost? & read-out $\dsc$; pinching $E$ & Lem.\ \claimref{transport.descent-read-out-map}, Prop.\ \claimref{transport.pinching-kernel}, Thm \claimref{transport.door-one-way} \\
6 & does repeating the repair terminate? & the mod-8 clock & Thm \claimref{transport.rule-1-morita-trivial}, Prop.\ \claimref{transport.fusion-occurs-most-once} \\
\bottomrule
\end{tabular}

\emph{The transport algorithm. Each row is a question a practitioner meets in order, the instrument that answers it, and the theorem that licenses the instrument. Step 3 is the only step where the three obstruction types diverge; Steps 4 and 5 are stated for type N, the only type whose repair is delivered at the level of points rather than elements.}

## technical
pending

## lay
pending

## one-liner
pending
