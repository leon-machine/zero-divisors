---
id: synthesis.solar-angle-light-plane-sum-rule
kind: claim
version: 1
title: The solar angle at the S3 to S2 direction needs a lopsided second stage
status: proved
region: synthesis
subject: neutrinos
tags: [flavour-and-mixing]
proposed_by:
  kind: ai
  session: colony-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - neutrino.breaking-relation@3
  - synthesis.theta23-at-s3-s2-direction@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_compression_shape
- kind: check
  ref: check.py::check_svd_identity
- kind: check
  ref: check.py::check_bound_against_data
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.theta23-at-s3-s2-direction
extraction:
  open_problem: op.second-order-breaking
  note: Extends the observation, exact from clause (i) of synthesis.theta23-at-s3-s2-direction, that theta12 = theta13 = 0 at the S3->S2 direction, since (1,-1,0) lies in both kernels. The statement is at the leading order of Lemma neutrino.breaking-relation (light masses and states from the compressions to the light plane). A numerical exploration of the full 3x3 textures (numpy, exploration only, not evidence) at delta_c = 0.286, delta = +-0.286, imposing m_e/m_mu, m1/m2 = 0.01 and m2/m3 = 0.17 on both roots, found the one-type maximum of Delta at 23.5 degrees (leading-order bound 21.6), which is the only support for the exclusion on the past-peak root, and mixed symmetric plus antisymmetric breakings reaching 49 to 56 degrees. The sum rule of clause (iii) is the lepton analogue of the Gatto-Sartori-Tonin and Fritzsch relations (cited from memory, not in the store). The NuFIT 6.0 three-sigma edges (sin^2 theta12 >= 0.275, sin^2 theta13 >= 0.0203) are cited from memory.
---

## formal
Take the textures of Lemma \claimref{neutrino.breaking-relation} at the $S_{3} \to S_{2}$ direction $E = e_{3}e_{3}^{\mathsf{T}}$ of Proposition \claimref{synthesis.theta23-at-s3-s2-direction}, with a second stage in each sector: $M_{e} = c\bigl(\J + \delta_{c}(E + X_{e})\bigr)$, $\mD = d\bigl(\J + \delta(E + X_{\nu})\bigr)$, $M_{R} = \alpha\Pi + M_{3}\J/3$, where each $X_{s}$ is real and odd under the exchange $P_{12}$ of the first two families, $P_{12}X_{s}P_{12} = -X_{s}$ (the $S_{2} \to 1$ stage). Work at the Lemma's order, where the light states and masses of each sector come from the compression $B_{s}$ of $E + X_{s}$ to $u'^{\perp}$, and let $\hat{b}_{e} = (1,1,-2)/\sqrt6$, $\hat{b}_{o} = (1,-1,0)/\sqrt2$.
\begin{enumerate}
\item[(i)] In the basis $(\hat{b}_{e}, \hat{b}_{o})$, exactly, $B_{s} = \bigl[\begin{smallmatrix} 2/3 & x_{s} \\ y_{s} & 0 \end{smallmatrix}\bigr]$, and $\Pi A\Pi A^{\mathsf{T}}\Pi = (\Pi A\Pi)(\Pi A\Pi)^{\mathsf{T}}$. So the charged light states are the left singular vectors of $B_{e}$ with $m_{e}/m_{\mu} = \sigma_{2}/\sigma_{1}$, and the light neutrino states are the left singular vectors of $B_{\nu}$ with $m_{1}/m_{2} = (\sigma_{2}/\sigma_{1})^{2}$. Symmetric $X_{s}$ gives $y_{s} = x_{s}$, antisymmetric $X_{s}$ gives $y_{s} = -x_{s}$.
\item[(ii)] For every real $B = \bigl[\begin{smallmatrix} k & x \\ y & 0 \end{smallmatrix}\bigr]$ with $k \neq 0$ and distinct singular values $\sigma_{1} > \sigma_{2}$, the angles $\theta_{L}$, $\theta_{R}$ of its heavy left and right singular vectors from the first axis satisfy $\sigma_{2}/\sigma_{1} = |\tan\theta_{L}\tan\theta_{R}|$, and $|\theta_{L}| = |\theta_{R}|$ when $y = \pm x$.
\item[(iii)] (The sum rule.) With $\Delta$ the angle between the lightest charged-lepton state and the lightest neutrino state, so that $|U_{e1}| = \cos\Delta$ at this order, $\Delta = |\theta_{L}^{\nu} - \theta_{L}^{e}|$. If each $X_{s}$ is purely symmetric or purely antisymmetric,
\[
\Delta \;\le\; \arctan\sqrt{m_{e}/m_{\mu}} \;+\; \arctan\,(m_{1}/m_{2})^{1/4} ,
\]
and if $m_{1}/m_{2} \le 0.01$ (the inequality of Premise (H), Premise \claimref{neutrino.h-second-stage-hierarchical}, taken here as a hypothesis of the clause) then $\Delta < 21.6^{\circ}$ and $|U_{e1}|^{2} > 0.865$, against $|U_{e1}|^{2} = c_{12}^{2}c_{13}^{2} \le 0.711$ at the three-sigma edges of the global fit. A second stage of one type in each sector, the $120$-like antisymmetric or the $10$/$126$-like symmetric alone, is excluded at this order.
\item[(iv)] The measured angle therefore needs, in at least one sector, an $S_{2}$-odd second stage with both a symmetric and an antisymmetric part and left-right lopsidedness bounded below. Exactly, for the block of (ii), $y/x = \tan\theta_{L}(1 + \tan^{2}\theta_{R})/\bigl(\tan\theta_{R}(1 + \tan^{2}\theta_{L})\bigr)$. With the charged sector of one type and $m_{1}/m_{2} \le 0.01$, the neutrino sector needs $|\tan\theta_{L}^{\nu}/\tan\theta_{R}^{\nu}| > 2.95$, equivalently in the texture entries $|y_{\nu}/x_{\nu}| > 2.35$; so $|y_{\nu}| \ne |x_{\nu}|$, which by (i) needs both a symmetric part $(x + y)/2$ and an antisymmetric part $(y - x)/2$.
\end{enumerate}
Since the antisymmetric family coupling is the one the grade-three direction supplies on the series' registered route, (iv) says the solar angle asks that this direction and a symmetric one act together in one sector's second stage; it does not derive their ratio.

## technical
At the $S_{3} \to S_{2}$ direction both small lepton angles vanish exactly (the vector $(1,-1,0)$ lies in both kernels), so the solar angle must come from the second stage $S_{2} \to 1$. This result computes what that stage can do at the order of the breaking lemma, where each sector's light pair is governed by a $2 \times 2$ block $\bigl[\begin{smallmatrix} 2/3 & x \\ y & 0 \end{smallmatrix}\bigr]$ in the light plane; the zero is exact because the second stage is odd under the surviving exchange. The neutrino's light block is the square of the same compression, so its light states are the left singular vectors and its mass ratio is the square of the singular-value ratio.

A $2 \times 2$ block with a zero corner obeys $\sigma_{2}/\sigma_{1} = |\tan\theta_{L}\tan\theta_{R}|$. When the second stage is purely symmetric or purely antisymmetric the left and right tilts agree, so each sector's left tilt is fixed by its own hierarchy: $\sqrt{m_{e}/m_{\mu}}$ for the charged leptons and $(m_{1}/m_{2})^{1/4}$ for the neutrinos. The angle between the two lightest states is at most the sum, under 21.6 degrees once Premise (H) holds, while the data need about 32 to 36. The solar angle therefore needs a lopsided second stage, symmetric and antisymmetric parts together in one sector with left tilt about three times the right (texture entries in ratio above 2.35) at least on the neutrino side. Scope: the Lemma's order is the perturbative branch, where the democratic seesaw term dominates and the compressions give the light states; on that branch Proposition \claimref{synthesis.theta23-at-s3-s2-direction} already excludes a near-maximal $\theta_{23}$. On the root past the peak, where $\theta_{23}$ can be met, the compression reading fails and the one-type exclusion rests only on a numerical exploration of the full textures (one-type maximum 23.5 degrees, lopsided breakings reaching 50 degrees), not on this proof.

## lay
The framework explains why one family of each kind is much heavier than the other two, but the mixing between electron-type and other neutrinos has to come from a second, smaller symmetry breaking. This result shows that if that second breaking is of a single simple kind in each sector, the largest mixing it can produce is set by two small mass ratios, the electron-to-muon ratio and the ratio of the two lightest neutrino masses, and, at the leading order of the breaking, comes out below about 22 degrees. The measured angle is about 33 degrees. So the second breaking must combine two different kinds of coupling in a lopsided way, which the framework's preferred route happens to contain but does not yet fix.

## one-liner
At the $S_{3} \to S_{2}$ direction a one-type second stage obeys $\Delta \le \arctan\sqrt{m_{e}/m_{\mu}} + \arctan(m_{1}/m_{2})^{1/4} < 21.6^{\circ}$ when $m_{1}/m_{2} \le 0.01$ (Premise (H)), excluding the measured solar angle at leading order; the data need a lopsided symmetric-plus-antisymmetric second stage.
