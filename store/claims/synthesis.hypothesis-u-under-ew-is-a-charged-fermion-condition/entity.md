---
id: synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition
kind: claim
version: 1
title: 'Under (EW), (U) is a charged-fermion condition, unmet at diagonal order'
status: proved
region: synthesis
subject: neutrinos
tags: [flavour-and-mixing, seesaw-and-majorana, hypothesis-u]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
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
  - standard-model.neutrino-dirac-matrix-charged-fermions@6
  - standard-model.fits-record-level@6
  - standard-model.hyp-s-slot-statistics@9
  assumes:
  - standard-model.premise-ew-equal-weight@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_ew_elimination_rank_one_up
- kind: check
  ref: check.py::check_rank_one_readings
- kind: check
  ref: check.py::check_diagonal_order_excludes_both_readings
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.hyp-u-equal-rank-one-eigenvalues
  - standard-model.premise-ew-equal-weight
extraction:
  open_problem: pr.u-equal-rank-one
  note: >-
    Adversarial route on pr.u-equal-rank-one. Under (EW) the neutrino Dirac matrix is eliminated
    in favour of the charged fermions, so Hypothesis (U), read as its formal text reads it (an
    eigenvalue statement), becomes a condition on the normalised down-minus-lepton matrix fhat in
    the up-type basis, with no neutrino input. Two consequences for the store. (1) The contradicts
    link between (U) and (EW) recorded at decision pass 11 holds for the entry reading
    ((M_nu)_33 = m_t); for the eigenvalue reading both readings are consistent with (EW) at rank
    one, and when the up-type and down-minus-lepton leading directions coincide (EW) contradicts
    both readings, not only the top one. A decision for Leon on how the link should read. (2) The
    Pati-Salam route's preference for the bottom reading (valuation note) is not supported once
    (EW) is imposed: at diagonal order the second-family entry of M_d - M_e already exceeds the
    bottom reading's target, so (U) in either reading needs off-diagonal lepton-quark structure
    that no stored ceiling symmetry fixes. The masses are the M_I values to which the stored
    coupling sets of standard-model.fits-record-level are fitted (T12's script, Part M), entered
    as rationals. Transport-absent.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Assume Hypothesis (S), the imported Clebsch structure with no $120$, and Premise (EW), so that by Proposition \claimref{standard-model.neutrino-dirac-matrix-charged-fermions}, in the family basis of (EW), $M_{\nu} = M_{u} - m_{t}\hat{f}$ with $\hat{f} = (M_{d} - M_{e})/(M_{d} - M_{e})_{33}$. Work at the leading order of the alignment, $M_{u} = m_{t}\,e_{3}e_{3}^{\mathsf{T}}$, and put $N = \hat{f} - e_{3}e_{3}^{\mathsf{T}}$, so $N_{33} = 0$.
\begin{enumerate}
\item[(i)] \emph{(Reduction.)} $M_{\nu} = -m_{t}N$: the neutrino Dirac masses are $m_{t}$ times the singular values of $N$, and the leading one is $m_{D} = m_{t}\,\sigma_{1}(N)$. Hypothesis (U) of \claimref{dark-matter.hyp-u-equal-rank-one-eigenvalues}, read as its formal text reads it, as a statement about the Dirac eigenvalue, is the condition $\sigma_{1}(N) = 1$ in the top reading and $\sigma_{1}(N) = m_{b}/m_{t}$ in the bottom reading: a condition on the charged-fermion matrix $M_{d} - M_{e}$ alone.
\item[(ii)] \emph{(Rank one.)} If $\hat{f} = ww^{\mathsf{T}}$ with $w = (0, \epsilon, 1)$, the nonzero eigenvalues of $N$ solve $l^{2} - \epsilon^{2}l - \epsilon^{2} = 0$. Aligned sectors, $\epsilon = 0$, give $N = 0$ and $M_{\nu} = 0$ at this order, so (EW) then contradicts both readings. The top reading holds exactly at $\epsilon^{2} = \tfrac12$ (eigenvalues $1$, $-\tfrac12$) and the bottom reading exactly at $\epsilon^{2} = r^{2}/(1 + r)$, $r = m_{b}/m_{t}$ (eigenvalues $r$, $-r/(1+r)$). The witness $\hat{f} = e_{3}e_{3}^{\mathsf{T}} + \mu\,e_{2}e_{2}^{\mathsf{T}}$ gives $M_{\nu} = -\mu m_{t}\,e_{2}e_{2}^{\mathsf{T}}$, exactly rank one with $\sigma_{1} = |\mu| m_{t}$, so $\mu = 1$ and $\mu = r$ realise the two readings with a rank-one neutrino Dirac matrix as well. So in the eigenvalue reading each reading is consistent with (EW), with or without a rank-one presupposition, and the conflict with $(M_{\nu})_{33} = 0$ is a conflict with the entry reading $(M_{\nu})_{33} = m_{t}$ only.
\item[(iii)] \emph{(Diagonal order.)} If $M_{d}$ and $M_{e}$ are diagonal in the same basis, $N = \mathrm{diag}(d_{1}/d_{3}, d_{2}/d_{3}, 0)$ with $d_{k} = m_{d_{k}}u_{k} - m_{e_{k}}v_{k}$, $|u_{k}| = |v_{k}| = 1$, and for every choice of phases
\[
\frac{m_{\mu} - m_{s}}{m_{b} + m_{\tau}} \;\le\; \sigma_{1}(N) \;\le\; \frac{\max(m_{d} + m_{e},\, m_{s} + m_{\mu})}{m_{\tau} - m_{b}} .
\]
At the masses at $M_{I}$ to which the stored fits of Proposition \claimref{standard-model.fits-record-level} are fitted ($m_{t} = 92.45$, $m_{b} = 1.3651$, $m_{\tau} = 1.764$, $m_{s} = 0.0261$, $m_{\mu} = 0.1037$, $m_{d} = 0.00130$, $m_{e} = 0.000502$ GeV) the bounds are $0.0247 < \sigma_{1}(N) < 0.326$, while the bottom reading needs $m_{b}/m_{t} = 0.01477$ and the top reading $1$: at diagonal order neither reading is met, at any phases.
\item[(iv)] \emph{(The stored fits, by citation.)} That the four coupling sets of Proposition \claimref{standard-model.fits-record-level} realise neither reading at $M_{I}$ is shown, with certified brackets, in the result filed alongside, synthesis.stored-fits-are-models-of-not-u; it is not proved here.
\end{enumerate}
So under (EW) whether (U) holds, and in which reading, is decided by the off-diagonal structure of $M_{d} - M_{e}$ in the up-type basis (the CKM rotation and the lepton-quark relative rotation), not by a magnitude equality at the ceiling; no ceiling symmetry in the store fixes that structure.

## technical
Premise (EW) removes the neutrino's Dirac entry along the top's direction, and without a $120$ the remaining neutrino Dirac matrix is fixed by the charged fermions: $M_{\nu} = M_{u} - m_{t}\hat{f}$, $\hat{f}$ the down-minus-lepton matrix normalised on its heavy entry. At the leading order where the up-type matrix is rank one, the neutrino's Dirac masses are $m_{t}$ times the singular values of $N = \hat{f} - e_{3}e_{3}^{\mathsf{T}}$. Hypothesis (U), which equates the neutrino's leading Dirac eigenvalue with the top's or the bottom's, is then a condition on $\hat{f}$ alone.

Three readings follow. If the down-minus-lepton matrix is rank one along the top's direction, $N$ vanishes and both readings of (U) fail. If it is rank one but tilted by $\epsilon$ in the 2-3 plane, the leading Dirac eigenvalue solves $l^{2} - \epsilon^{2}l - \epsilon^{2} = 0$: the top reading needs $\epsilon^{2} = 1/2$ and the bottom reading $\epsilon^{2} = r^{2}/(1+r)$, so in the eigenvalue reading neither conflicts with (EW); the store's recorded conflict is with the entry reading. If the down-type and lepton matrices are diagonal together, the second-family difference alone gives $\sigma_{1}(N) \ge (m_{\mu} - m_{s})/(m_{b} + m_{\tau}) \approx 0.0248$ at $M_{I}$, above the bottom reading's $0.0148$, and the heavy difference keeps $\sigma_{1}(N)$ below $0.33$, far from the top reading's $1$. Which reading, if either, holds is therefore set by the off-diagonal lepton-quark structure.

## lay
One of the series' assumptions, called (U), says that at the highest energy the neutrino's basic mass equals that of another particle, either the top quark or the bottom quark; the two choices give very different answers downstream. Another assumption, (EW), lets the neutrino's mass pattern be computed entirely from the masses of the charged particles. This result shows that once (EW) is accepted, (U) stops being a free choice: it becomes a test the charged particles' masses and mixings either pass or fail. In the simplest arrangement, where quarks and leptons are not mixed with each other, the test fails for both choices: the neutrino comes out heavier than the bottom-quark choice allows and far lighter than the top-quark choice. Only extra mixing between quarks and leptons, which nothing in the series currently fixes, could rescue either.

## one-liner
Under (S), (EW) and no $120$, with $M_{u}$ rank one, the neutrino's leading Dirac mass is $m_{t}\sigma_{1}(\hat{f} - e_{3}e_{3}^{\mathsf{T}})$, so (U) is a condition on $M_{d} - M_{e}$ alone; aligned sectors fail both readings, rank-one tilts and a rank-one witness meet either, and at diagonal order the $M_{I}$ masses give $0.0247 < m_{D}/m_{t} < 0.326$, missing both.
