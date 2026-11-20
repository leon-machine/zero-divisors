---
id: note.dark-tower-matter.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: dark-matter
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'restated to the deposited text of T14c version 1.0 (10.5281/zenodo.24403592)'
  version: 2
  source: maintainer pass of 2026-11-20
comments_on:
- dark-tower-matter.adjoint-norm
- dark-tower-matter.where-mass-begins
- dark-tower-matter.ladder
- dark-tower-matter.constituents-field
locators:
  paper: T14c
  number: Setting
  section: Machine verification
  line: 881
extraction:
  maintainer_pass:
    by: maintainer-2026-11-20
    date: '2026-11-20'
    note: 'The formal level restated: T14c deposited as version 1.0 on 20 November 2026 (10.5281/zenodo.24403592), after an independent review: the running text follows the deposited paper. Version 1 -> 2.'
---

## formal
The script \file{verify\_T14c.py} \cite{ButlerVerifyT14c} imports the series library \file{GA.py} and checks the computational statements of Sections 3 to 10 in exact arithmetic: rational numbers, and a small polynomial ring over $\mathbb{Q}$ in which the identities of Lemma \claimref{dark-tower-matter.adjoint-norm} and Theorems \claimref{dark-tower-matter.where-mass-begins} and \claimref{dark-tower-matter.ladder} are verified as polynomial identities in the spinors' coordinates rather than on samples. Part K alone is decimal and labelled. Without the supplementary scripts it runs $56$ checks, all passing:

\begin{center} \begin{tabular}{@{}lll@{}}
\toprule
Part & statements & checks \\
\midrule
A & Theorem \claimref{dark-tower-matter.constituents-field} & A1 to A5 \\
B & Lemma \claimref{dark-tower-matter.adjoint-norm}, Theorem \claimref{dark-tower-matter.where-mass-begins} & B0 to B7 \\
C & Theorem \claimref{dark-tower-matter.ladder} & C1, C2 \\
D & Proposition \claimref{dark-tower-matter.pairs}, Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions} & D1a, D1b, D2 to D12 \\
E & Theorem \claimref{dark-tower-matter.gauge-algebras}, Remark \claimref{note.dark-tower-matter.kleinian-algebra} & E1 to E5 \\
F & Propositions \claimref{dark-tower-matter.three-dimensional-content}, \claimref{dark-tower-matter.five-dimensional-content} & F1 to F4 \\
G & Proposition \claimref{dark-tower-matter.anomalies} & G1, G2 \\
H & Proposition \claimref{dark-tower-matter.residue-seven-unit} & H1 to H4 \\
I & Theorem \claimref{dark-tower-matter.mirror-algebra} & I1 to I3 \\
J & Proposition \claimref{dark-tower-matter.sterile-kinematics} & J1 to J3 \\
K & Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}, Computations \claimref{dark-tower-matter.survival-sheets}, \claimref{dark-tower-matter.five-dimensional-towers}; Fact \claimref{dark-tower-matter.imported-unit-ball-rule} (decimal) & K1 to K7 \\
\bottomrule
\end{tabular}
\end{center}

Part L runs the supplementary scripts, which are deposited with the paper in its folder \file{T14c\_supplement}: the derivation scripts \file{MIR}, \file{D3R}, \file{D3C}, \file{D5C}, \file{D5Q}, \file{STE} (one per tower: $24$, $61$, $78$, $86$, $106$ and $68$ checks) and two independent checks, \file{CHECK\_ALG} ($50$ exact checks) and \file{CHECK\_COS} (decimal, ten checks on the numbers this paper cites), and requires each to be present and to run clean, twelve further checks ($68$ in all). The script needs \texttt{scipy} for Part K and \file{CHECK\_COS}, and takes about two and a half minutes. The supplementary scripts' docstrings refer to working notes of the run that produced them; those notes are not part of the deposit, and nothing here relies on them. The paper cites them for the decimal composition of the mirror (Computation \claimref{dark-tower-matter.mirrors-composition}), the five-dimensional binding, scattering and plasma estimates (Computation \claimref{dark-tower-matter.five-dimensional-towers}), the invariant forms of Corollary \claimref{dark-tower-matter.same-kind-matter}, the branches of Remark \claimref{note.dark-tower-matter.branches-break-u-what-they-give}, the Kleinian ladder of Remark \claimref{note.dark-tower-matter.kleinian-algebra}, the transported weights of Proposition \claimref{dark-tower-matter.three-dimensional-content}(iii) and the sheet radiation of Observation \claimref{dark-tower-matter.three-dimensional-phases}. What no script checks: the statement after Theorem \claimref{dark-tower-matter.gauge-algebras} about the mirror (T14's), the imported physics (Redlich's shift, Polyakov, topological mass, flux attachment, five-dimensional Chern-Simons quantisation, plasma instabilities) and the galaxy modelling of T14b.

## technical
pending

## lay
pending

## one-liner
pending
