---
id: standard-model.one-threshold-exact-criterion
kind: claim
version: 3
title: 'One threshold: the exact criterion'
status: proved
region: standard-model
subject: standard-model
tags:
- running-and-unification
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.complete-multiplets-shift-all-three-coefficients@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_closed_form_solution_and_uniqueness
- kind: check
  ref: check.py::check_complete_multiplets_inert
- kind: check
  ref: check.py::check_interval_criterion_and_monotonicity
locators:
  paper: T12
  number: Thm 8.9
  label: thm:criterion
  line: 1340
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Cramer closed forms, uniqueness and the singular case, inertness under Dl + c(1,1,1), and the interval criterion with the Moebius monotonicity, on a hand instance and sample spectra. Version 2 -> 3.'
  env: theorem
  eqrefs: 3
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.table-exact
    note: 'Removed the table proposition (E301 cycle): the proof only runs its script checks on the table''s
      spectra, and it is the table that applies this criterion; kept the complete-multiplets lemma, which
      (ii) invokes.'
about:
- obj.standard-model.one-threshold-spectrum-admissible
---

## formal
Fix record values with $a_{1} > a_{2} > a_{3}$ at $M_{Z}$, so $D_{12}, D_{23} > 0$, and a one-threshold spectrum $(b, \Dl)$ with $b_{23} > 0$ and $b_{23} + \Dl_{23} > 0$. Then:
\begin{enumerate}
\item[(i)] If $b_{12}\Dl_{23} \ne b_{23}\Dl_{12}$, the system \eqref{eq:run} has exactly one solution,
\[
x = \frac{D_{12}\Dl_{23} - D_{23}\Dl_{12}}{b_{12}\Dl_{23} - b_{23}\Dl_{12}}, \qquad
y = \frac{b_{12}D_{23} - b_{23}D_{12}}{b_{12}\Dl_{23} - b_{23}\Dl_{12}}, \qquad
a_{U} = a_{3} - b_{3}\,x - \Dl_{3}\,y,
\]
with threshold fraction
\[
f \;=\; \frac{y}{x} \;=\; \frac{R\,b_{23} - b_{12}}{\Dl_{12} - R\,\Dl_{23}},
\]
every one of them a rational function of the record values and the coefficients; the transcendental $\ln$ enters only in converting $x$ and $y$ to scales in GeV. If $b_{12}\Dl_{23} = b_{23}\Dl_{12}$ the system has no solution unless $R = r_{0}$.
\item[(ii)] (Inertness.) Replacing $\Dl$ by $\Dl + c\,(1,1,1)$ leaves $x$, $y$, $f$, $M_{U}$ and $M_{I}$ unchanged and lowers $a_{U}$ by $c\,y$. In particular, by Lemma \claimref{standard-model.complete-multiplets-shift-all-three-coefficients}, complete multiplets of a simple unifying group with a common threshold do not move the meeting condition; they lower the unified coupling, that is, raise $\alpha_{U}$.
\item[(iii)] (The interval criterion.) The threshold lies in $[M_{Z}, M_{U}]$, that is $0 \le f \le 1$, if and only if $R$ lies in the closed interval between $r_{0}$ and $r_{\Dl}$. Given that, $x > 0$ holds automatically, and admissibility reduces to $a_{U} > 0$.
\end{enumerate}

## technical
Take record values with $a_{1} > a_{2} > a_{3}$ at $M_{Z}$, so $D_{12}, D_{23} > 0$, and a one-threshold spectrum $(b, \Dl)$ with $b_{23} > 0$ and $b_{23} + \Dl_{23} > 0$. Eliminating $a_{U}$ leaves a linear system in the logarithmic scales $(x, y)$ with determinant $b_{12}\Dl_{23} - b_{23}\Dl_{12}$. When it is nonzero the unique solution is rational in the inputs, with threshold fraction $f = y/x = (R\,b_{23} - b_{12})/(\Dl_{12} - R\,\Dl_{23})$, and the logarithm enters only in converting to GeV; when it vanishes there is no solution unless $R = r_{0}$.

Shifting $\Dl$ by $c(1,1,1)$, as complete multiplets of a simple unifying group with a common threshold do, leaves $x$, $y$, $f$, $M_{U}$ and $M_{I}$ unchanged and lowers $a_{U}$ by $cy$. The threshold lies in $[M_{Z}, M_{U}]$ exactly when $R$ lies in the closed interval between $r_{0}$ and $r_{\Dl}$, and then $x > 0$ automatically, so admissibility reduces to $a_{U} > 0$.

## lay
When extra particles appear at one intermediate energy, the question of whether the three forces' strengths meet at a single higher energy becomes a small problem in linear algebra. This result solves it exactly, giving the threshold position and the meeting point as simple fractions of the measured inputs. It shows that adding complete families of particles at the threshold never changes where the forces meet, only how strong they are there, and it gives a clean test for whether the threshold falls in the allowed energy range.

## one-liner
For a one-threshold spectrum the unification conditions have a unique rational solution when $b_{12}\Dl_{23} \ne b_{23}\Dl_{12}$, are inert under uniform shifts of $\Dl$, and place the threshold in range exactly when $R$ lies between $r_{0}$ and $r_{\Dl}$.
