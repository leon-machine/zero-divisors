---
id: interior.unipotency-across-kerr-family
kind: claim
version: 6
title: Unipotency across the Kerr family
status: proved
region: interior
subject: interior
tags: [kerr, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, square of the null vector written Q(k)'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - interior.gauge-trajectory-unipotent-ray@8
  - interior.imported-kerr-schild-form-kerr-gauge@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:6.2
- kind: check
  ref: check.py::check_null_shear_is_unipotent
- kind: check
  ref: check.py::check_kerr_schild_metric
- kind: check
  ref: check.py::check_kernel_and_image_along_k
locators:
  paper: T06
  number: Prop 6.2
  label: prop:kerrschild
  line: 786
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'House style: the square of the vector k is written Q(k) in the formal level and the proof; notation only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: P_k^2 = 0 and the unipotent group for null k, the Kerr-Schild metric g = eta - 2H k k with the ingoing EF reduction, and the null shear. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'Both uses are premises; the unipotent-ray proposition was re-pinned to its current version
      2; reproducing the Kerr-Schild metric is a consistency check inside the proof, not a standard route
      to the claim. Levels pass: conditions already kept.'
  env: proposition
  unresolved_refs:
  - rem:parabolic
  eqrefs: 1
---

## formal
Let $P_k(a) := (a\cdot k)\,k$ with $Q(k) = 0$. Then, exactly:
\begin{enumerate}
\item $P_k^2 = 0$, so $\{1 + sHP_k\}$ is again a one-parameter unipotent family and $\hb^{-1} = 1 - H P_k$ in closed form wherever the gauge field is defined;
\item $\hb(a)\cdot\hb(b) = a\cdot b + 2H\,(a\cdot k)(b\cdot k)$ with no higher corrections, and equally $\hb^{-1}(a)\cdot\hb^{-1}(b) = a\cdot b - 2H\,(a\cdot k)(b\cdot k)$; since the metric of Section \ref{sec:setting} is $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$, the gauge field reproduces the Kerr-Schild metric $g = \eta - 2H\,k\otimes k$ exactly, in the $(+,-,-,-)$ signature, the first display being the inverse metric;
\item the entire Kerr family, Schwarzschild included, is therefore a unipotent deformation of the identity, and the deformation is now built on a \emph{null} vector: the shear of Proposition \claimref{interior.gauge-trajectory-unipotent-ray}, whose kernel direction was spacelike-orthogonal at finite radius and became null only in the limit, is literally null for rotation, at every point.
\end{enumerate}

## technical
Let $P_k(a) = (a\cdot k)\,k$ with $Q(k) = 0$. Then $P_k^2 = 0$, so $\{1 + sHP_k\}$ is a one-parameter unipotent family and $\hb^{-1} = 1 - HP_k$ in closed form wherever the gauge field is defined. Moreover $\hb(a)\cdot\hb(b) = a\cdot b + 2H(a\cdot k)(b\cdot k)$ and $\hb^{-1}(a)\cdot\hb^{-1}(b) = a\cdot b - 2H(a\cdot k)(b\cdot k)$ with no higher corrections, so the gauge field reproduces the Kerr-Schild metric $g = \eta - 2H\,k\otimes k$ exactly, in signature $(+,-,-,-)$.

Hence the whole Kerr family, Schwarzschild included, is a unipotent deformation of the identity built on a null vector. The shear of the Schwarzschild gauge trajectory, whose kernel direction was spacelike-orthogonal at finite radius and became null only in the limit, is literally null at every point once rotation is included.

## lay
A rotating black hole can be built from flat spacetime by a single shearing operation along a light-like direction. Applying that shear twice gives nothing new, which makes it an especially simple, so-called unipotent, deformation. The result shows that this holds exactly for every member of the rotating family, and that the special direction is light-like at every point, not just in a limit.

## one-liner
For the Kerr-Schild gauge field $\hb = 1 + HP_k$ with $k$ null, $P_k^2 = 0$, so the whole Kerr family is a unipotent deformation of the identity along a null direction, reproducing the Kerr-Schild metric exactly.
