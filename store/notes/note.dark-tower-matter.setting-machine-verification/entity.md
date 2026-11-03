---
id: note.dark-tower-matter.setting-machine-verification
kind: note
version: 1
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
comments_on:
- dark-tower-matter.adjoint-norm
- dark-tower-matter.where-mass-begins
- dark-tower-matter.ladder
- dark-tower-matter.constituents-field
locators:
  paper: T14c
  number: Setting
  section: Machine verification
  line: 916
---

## formal
The script \file{verify\_T14c.py} \cite{ButlerVerifyT14c} imports the series library \file{GA.py} and checks the computational statements of Sections 3 to 10 in exact arithmetic: rational numbers, and a small polynomial ring over $\mathbb{Q}$ in which the identities of Lemma \claimref{dark-tower-matter.adjoint-norm} and Theorems \claimref{dark-tower-matter.where-mass-begins} and \claimref{dark-tower-matter.ladder} are verified as polynomial identities in the spinors' coordinates rather than on samples. Part K alone is decimal and labelled. Without the supplementary scripts it runs $57$ checks, all passing:

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
G & Proposition \claimref{dark-tower-matter.anomalies} & G1 to G3 \\
H & Proposition \claimref{dark-tower-matter.residue-seven-unit} & H1 to H4 \\
I & Theorem \claimref{dark-tower-matter.mirror-algebra} & I1 to I3 \\
J & Proposition \claimref{dark-tower-matter.sterile-kinematics} & J1 to J3 \\
K & Propositions \claimref{dark-tower-matter.mirrors-temperature-p2}, \claimref{dark-tower-matter.survival-sheets}, \claimref{dark-tower-matter.five-dimensional-towers}; Fact \claimref{dark-tower-matter.imported-unit-ball-rule} (decimal) & K1 to K7 \\
\bottomrule
\end{tabular}
\end{center}

Part L runs the supplementary derivation scripts deposited with the paper in the folders \file{MIR}, \file{D3R}, \file{D3C}, \file{D5C}, \file{D5Q}, \file{STE} (one per tower: $24$, $61$, $78$, $86$, $106$ and $68$ checks) and two independent checks, \file{CHECK\_ALG} ($50$ exact checks) and \file{CHECK\_COS} (decimal), and requires each to be present and to run clean, twelve further checks ($69$ in all). The paper cites them for the decimal composition of the mirror (Computation \claimref{dark-tower-matter.mirrors-composition}), the five-dimensional binding, scattering and plasma estimates (Proposition \claimref{dark-tower-matter.five-dimensional-towers}), the invariant forms of Corollary \claimref{dark-tower-matter.same-kind-matter}, the branches of Remark \claimref{note.dark-tower-matter.branches-break-u-what-they-give}, the Kleinian ladder of Remark \claimref{note.dark-tower-matter.kleinian-algebra}, the transported weights of Proposition \claimref{dark-tower-matter.three-dimensional-content}(iii) and the sheet radiation of Proposition \claimref{dark-tower-matter.three-dimensional-phases}. What no script checks: the statement after Theorem \claimref{dark-tower-matter.gauge-algebras} about the mirror (T14's), the imported physics (Redlich's shift, Polyakov, topological mass, flux attachment, five-dimensional Chern-Simons quantisation, plasma instabilities) and the galaxy modelling of T14b.

## technical
pending

## lay
pending

## one-liner
pending
