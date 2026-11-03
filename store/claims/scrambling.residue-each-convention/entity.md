---
id: scrambling.residue-each-convention
kind: claim
version: 4
title: The residue in each convention
status: proved
region: scrambling
subject: entropy
tags: [mode-counting]
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
  - scrambling.imported-collars-coframe-exceptional-set-helicity@6
  - scrambling.integer-holographic-form-identification@2
  - singularity.area-law-test@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - num:4.12
- kind: check
  ref: check.py::check_residues_in_both_conventions
- kind: check
  ref: check.py::check_conventions_differ_by_ln2
- kind: check
  ref: check.py::check_one_helicity_per_mode
locators:
  paper: T08
  number: Prop 4.12
  label: prop:residue
  line: 816
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: residues 1/4 and (1/4)/ln 2, ratio ln 2 and thinning 16 pi ln 2, qubit entropy and ln 2 < 1, helicity homogeneities distinct. Version 3 -> 4.'
  env: proposition
  context_refs:
  - scrambling.epoch-modular-period-two-unknowns-become
  - scrambling.imported-collars-coframe-exceptional-set-helicity
  unresolved_refs:
  - rem:nu
  typing:
    by: ai-typing-pass
    added:
    - scrambling.imported-collars-coframe-exceptional-set-helicity
    note: 'Kept the holographic corollary and the singularity paper''s area-law test (repinned to version
      2), which fixes the capacity convention compared in (ii); added the collar Fact from context_refs,
      the premise of the helicity clause (iv); the epoch theorem in context_refs is only re-read, not
      used. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - scrambling.imported-collars-coframe-exceptional-set-helicity
---

## formal
Write the epoch count as $N_{\mathrm{epoch}} = \kappa_c \times A \times 1$, horizon-normalised sphere cells times one tick per modular period, with $\kappa_c$ the dimensionless \emph{calibration residue}, a symbol distinct from the surface gravity $\kappa$ of Section \ref{sec:setting}. Then:
\begin{enumerate}
\item[(i)] in the 1-nat convention of this paper, $N_{\mathrm{epoch}} = \SBH$ gives $\kappa_c = \SBH/A = \tfrac14$;
\item[(ii)] in the capacity convention of the singularity paper, $N_{\mathrm{epoch}}\ln 2 = \SBH$ gives $\kappa_c = 1/(4\ln 2)$: one boundary mode per $4\ln 2$ Planck areas of horizon per modular period, which is one mode per Bekenstein-Mukhanov area quantum \cite{BekensteinMukhanov1995};
\item[(iii)] the two differ by exactly $\ln 2$, and only (ii) compares an entropy with an entropy: a fermionic mode carries at most $\ln 2$ nats, so the 1-nat convention credits each mode with more entropy than it can hold, and the exact ``$16\pi$'' of Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become} is a property of that convention, the physical thinning being $16\pi\ln 2$;
\item[(iv)] one boundary mode registers one helicity: by Fact \claimref{scrambling.imported-collars-coframe-exceptional-set-helicity} the two helicities of a massless species are two channels of the lift, so the capacity per boundary mode is $\ln 2$ and not $2\ln 2$, and $\kappa_c$ is $1/(4\ln 2)$, not $1/(8\ln 2)$.
\end{enumerate}

## technical
Write the epoch count as $N_{\mathrm{epoch}} = \kappa_c \times A \times 1$, horizon-normalised sphere cells times one tick per modular period, with $\kappa_c$ the calibration residue (distinct from the surface gravity $\kappa$). In the 1-nat convention $N_{\mathrm{epoch}} = \SBH$ gives $\kappa_c = \tfrac14$; in the capacity convention $N_{\mathrm{epoch}}\ln 2 = \SBH$ gives $\kappa_c = 1/(4\ln 2)$, one mode per Bekenstein-Mukhanov area quantum of horizon per period.

The two differ by $\ln 2$, and only the capacity convention compares an entropy with an entropy, since a fermionic mode carries at most $\ln 2$ nats; the exact $16\pi$ belongs to the 1-nat convention, the physical thinning being $16\pi\ln 2$. One boundary mode registers one helicity, so the capacity per mode is $\ln 2$, not $2\ln 2$, and $\kappa_c = 1/(4\ln 2)$ rather than $1/(8\ln 2)$.

## lay
The number of boundary modes per unit of horizon area can be quoted in two bookkeeping conventions, which differ by a factor of $\ln 2$. Only one of them counts entropy properly, because a single fermionic mode can hold at most $\ln 2$ units of entropy. In that convention the rule is one mode per Bekenstein-Mukhanov quantum of horizon area per thermal cycle.

## one-liner
The calibration residue is $\kappa_c = \tfrac14$ in the 1-nat convention and $1/(4\ln 2)$ in the capacity convention, the only one that compares entropy with entropy.
