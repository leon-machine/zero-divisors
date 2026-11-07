---
id: synthesis.theta23-at-s3-s2-direction
kind: claim
version: 3
title: Near-maximal theta-23 at the S3 to S2 direction needs the far root and opposite signs
status: proved
subject: neutrinos
tags:
- flavour-and-mixing
- seesaw-and-majorana
- confronted-with-data
proposed_by:
  kind: ai
  session: synthesis-gaps-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
derivations:
- name: main
  uses:
  - neutrino.breaking-relation@3
  proof: proof-main.tex
lineage:
  motivated_by:
  - neutrino.mixing-none-leading-order
checked_by:
- kind: check
  ref: check.py::test_theta23
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F: the eigenvector angle 2 theta = arg(Delta + I_4 B'') of the proof and the point Delta + I_4 B'' that moves in the upper half-plane are written with I_4, numbers read in span{1, I_4}; no bare i remains.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  review_fixes:
    by: ai-review-fix
    date: 2026-10-21
    note: 'Referee fixes: Step 3 proved over the whole branch (exact two-sided charged tilt, neutrino tilt monotone in s, extreme at delta = 1, lambda_M = lambda_D, least |U|^2 in (0.7687, 0.7688)) and certified by rational interval bisection in the check; the measured window cited from the global fit (NuFIT 2024) rather than used through the conjectured Observation, which stays as lineage (the Observation is conjectured because its question was open; this result answers part of it); the conclusion restricted to exactly |delta| = 0.286.'
---

## formal
Take the textures of Lemma \claimref{neutrino.breaking-relation} at the $S_{3} \to S_{2}$ direction $E = e_{3}e_{3}^{\mathsf{T}}$ in both sectors: the charged-lepton matrix $c(\J + \delta_{c}E)$ with $\delta_{c} = 0.286$ (exact singular values give $m_{\mu}/m_{\tau} \in (0.0594, 0.0596)$), $\mD = d(\J + \delta E)$, $M_{R} = \alpha\Pi + M_{3}\J/3$ with $\alpha, M_{3} > 0$, and $m_{\nu} = \mD M_{R}^{-1}\mD^{\mathsf{T}}$; write $|U_{\tau 3}|^{2} = (x_{\tau} \cdot x_{3})^{2}$ for the unit heavy eigenvectors of the two sectors.
\begin{enumerate}
\item[(i)] Exactly, $m_{\nu} = \lambda_{D}E + \lambda_{M}\hat{w}\hat{w}^{\mathsf{T}}$ with $w = (\J + \delta E)(1,1,1)^{\mathsf{T}} = (3, 3, 3 + \delta)$, $\hat{w} = w/|w|$, $\lambda_{D} = 2d^{2}\delta^{2}/3\alpha$ and $\lambda_{M} = d^{2}|w|^{2}/3M_{3}$. The vector $(1,-1,0)$ is in the kernel of $m_{\nu}$ and of the charged matrix ($m_{1} = m_{e} = 0$), so both heavy eigenvectors lie in the plane spanned by $(1,1,0)$ and $e_{3}$, and $|U_{\tau 3}|^{2}$ is the squared cosine of the difference of their angles in that plane.
\item[(ii)] The heavy neutrino eigenvector is nearer $\hat{w}$ than $e_{3}$ exactly when $\lambda_{M} > \lambda_{D}$. At fixed $\delta$ the ratio $m_{2}/m_{3}$, as a function of $M_{3}/\alpha$, peaks at $\lambda_{M} = \lambda_{D}$ with value $\tan^{2}(\varphi/2)$, $\varphi$ the angle between $w$ and $e_{3}$ (at $\delta = 0.286$: $M_{3}/\alpha = 176.0$ and $m_{2}/m_{3} \in (0.240, 0.241)$). The two roots of $m_{2}/m_{3} = \rho$ below the peak are exchanged by $\lambda_{M} \mapsto \lambda_{D}^{2}/\lambda_{M}$, and their heavy eigenvectors are reflections of each other across the bisector of $\hat{w}$ and $e_{3}$.
\item[(iii)] On the perturbative branch $\lambda_{M} \ge \lambda_{D}$, for every $|\delta| \le 1$ of either sign, $|U_{\tau 3}|^{2} > 0.76$: its least value, attained at $\delta = 1$ and $\lambda_{M} = \lambda_{D}$, lies in $(0.7687, 0.7688)$, the heavy eigenvectors there about $28.7^{\circ}$ apart. At the instance of Remark \ref{rem:branch} ($\delta = \delta_{c}$, $M_{3}/\alpha = 66$, $m_{2}/m_{3} \in (0.168, 0.172)$) it exceeds $0.96$, the two heavy eigenvectors about $11^{\circ}$ apart (tilts of about $13^{\circ}$ and $3^{\circ}$, in the same sense).
\item[(iv)] Past the peak, at the remark's size $|\delta| = 0.286$ and $m_{2}/m_{3} \in (0.168, 0.172)$: with $\delta = +\delta_{c}$ ($M_{3}/\alpha = 469.5$), $|U_{\tau 3}|^{2} \in (0.55, 0.58)$, just outside the window; with $\delta = -\delta_{c}$ ($M_{3}/\alpha = 530.7$), $|U_{\tau 3}|^{2} \in (0.50, 0.55)$, inside the measured window $(0.39, 0.55)$ of the global fit \cite{NuFIT2024}, the window Observation \claimref{neutrino.mixing-none-leading-order} reads from the record.
\end{enumerate}
So the open number of that Observation is settled at the $S_{3} \to S_{2}$ direction: a breaking of exactly the remark's size $|\delta| = 0.286$ supplies a near-maximal $\theta_{23}$, but only on the root past the peak of $m_{2}/m_{3}$, where the lemma's remainders dominate and $\alpha/M_{3} \approx 1.9 \times 10^{-3}$, and only with the Dirac neutrino breaking opposite in sign to the charged lepton's; on the perturbative branch the paper takes, it cannot.

## technical
At the direction that breaks the three-family permutation symmetry to a two-family one, the light-neutrino matrix is exactly the sum of two rank-one pieces, one along the third family's axis from the Dirac breaking and one along a nearly democratic vector from the heavy Majorana mass. Both lepton sectors then keep the two-family symmetry, so their heavy eigenvectors lie in one plane and the large mixing angle is the difference of two tilts in that plane. For a sum of two rank-one pieces the heavier eigenvector lies nearer whichever piece is larger; the ratio of the two light masses peaks where the pieces are equal, and the two values of the Majorana ratio that give the measured mass ratio are mirror images, with mirror-image eigenvectors. On the root the paper uses, where the Majorana piece dominates, the neutrino's heavy eigenvector stays near the democratic direction, as the charged lepton's does, and the mixing is small: at the paper's instance about eleven degrees, and at most about twenty-nine degrees for any breaking up to one in size, against the forty-two to fifty-one required. On the mirror root the neutrino eigenvector swings towards the third family's axis, and at the remark's size, with a Dirac breaking opposite in sign to the charged lepton's, the separation reaches forty-four degrees, inside the observed range.

## lay
Neutrinos change type as they travel, and one of the measured mixing angles is close to its largest possible value. The series' structure gives no mixing at first approximation, and asked whether a small correction of the size it suggests could supply the large angle. For the simplest form of the correction this result answers exactly. On the branch the series chose, no: the angle comes out about four times too small. On a second branch, where a different heavy mass ratio reproduces the same neutrino mass ratio, yes at that size, provided the correction to the neutrinos has the opposite sign to the one for the charged leptons. Whether that second branch is acceptable is now the question.

## one-liner
At the $S_{3} \to S_{2}$ direction near-maximal $\theta_{23}$ is excluded on the perturbative root ($|U_{\tau 3}|^{2} > 0.76$) and reached past the peak with opposite-sign breakings ($|U_{\tau 3}|^{2} \approx 0.52$ at $|\delta| = 0.286$).
