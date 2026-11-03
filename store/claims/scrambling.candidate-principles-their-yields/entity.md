---
id: scrambling.candidate-principles-their-yields
kind: claim
version: 2
title: The candidate principles and their yields
status: proved
region: scrambling
subject: entropy
tags: [mode-counting, boundary-modes]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
derivations:
- name: main
  uses:
  - scrambling.exact-factorisation-thinning@3
  - scrambling.imported-collars-coframe-exceptional-set-helicity@6
  - scrambling.per-slice-verification-two-failed-aggregations@4
  - scrambling.scheme-robustness-cutoff@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - num:4.9
- kind: check
  ref: check.py::check_p1_slice_count_scheme_bound
- kind: check
  ref: check.py::check_p3_horizon_normalised_count
- kind: check
  ref: check.py::check_p2_breaks_scaling
locators:
  paper: T08
  number: Prop 4.9
  label: prop:yields
  line: 787
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: P1 yields 16 pi S_BH with scheme ratios 3/2 and 12^(1/4) (irrational) from solved cutoffs; P3 coframe identity 1 - r and yield A = 4 S_BH; P2 scaling M^(5/3). Version 1 -> 2.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'All four uses are premises of the proof (slice count, scheme constants, collar coframe, failed
      aggregation) and are kept; the remaining E204 comes from the collar-coframe Fact, outside this list.
      Levels pass: conditions already kept.'
---

## formal
Let a calibration principle be a rule assigning to the exceptional set $E = \{\tau = 0\} \times \R_t \times S^2$ a count of boundary-mode fermions per modular period. Then:
\begin{enumerate}
\item[(P1)] \emph{one fermion per Planck cell of the slice} returns $N_{\mathrm{epoch}} = 16\pi\,\SBH$, and the coefficient is scheme-bound: the slice count scales as $c_0^{3/2}$, so the proper-time scheme returns exactly $\tfrac32$ times the curvature scheme's count and the Kretschmann scheme $12^{1/4}$ times it, an irrational multiple;
\item[(P3)] \emph{one fermion per Planck cell of the sphere at horizon normalisation, once per modular period} returns $N_{\mathrm{epoch}} = A = 4\,\SBH$, independently of the cutoff scheme, because the horizon-normalised coframe on $E$ is exactly $(dt,\ r_h\,d\theta,\ r_h\sin\theta\,d\varphi)$ (Fact \claimref{scrambling.imported-collars-coframe-exceptional-set-helicity});
\item[(P2)] \emph{fundamentals per sphere aggregated over the epoch} breaks the $M$-scaling (Proposition \claimref{scrambling.per-slice-verification-two-failed-aggregations}).
\end{enumerate}

## technical
A calibration principle assigns to the exceptional set $E = \{\tau = 0\} \times \mathbb{R}_t \times S^2$ a count of boundary-mode fermions per modular period. Of three natural candidates, (P1), one fermion per Planck cell of the slice, gives $N_{\mathrm{epoch}} = 16\pi\,\SBH$, but its coefficient scales as $c_0^{3/2}$ with the cutoff scheme: the proper-time scheme gives $\tfrac32$ times the curvature scheme's value and the Kretschmann scheme $12^{1/4}$ times it, an irrational multiple.

(P3), one fermion per Planck cell of the horizon-normalised sphere once per modular period, gives $N_{\mathrm{epoch}} = A = 4\,\SBH$ in every scheme, because the horizon-normalised coframe on $E$ is exactly $(dt,\ r_h\,d\theta,\ r_h\sin\theta\,d\varphi)$. (P2), fundamentals per sphere aggregated over the epoch, breaks the scaling in $M$.

## lay
To pin down how many modes the black hole interior carries, one needs a rule for counting them on its inner boundary. Of three natural rules, the first gives a number that depends on an arbitrary choice of where to cut off the geometry, the second gives four times the Bekenstein-Hawking entropy whatever that choice, and the third fails to grow with the mass in the right way. So none of the three returns the entropy itself.

## one-liner
One fermion per slice cell gives a scheme-dependent $16\pi\,\SBH$, one per horizon-normalised sphere cell per period gives a scheme-independent $4\,\SBH$, and per-sphere aggregation breaks the mass scaling.
