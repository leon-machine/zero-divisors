---
id: interior.scale-tractor-leaves-cone
kind: claim
version: 7
title: '$\Lambda \neq 0$: the scale tractor leaves the cone'
status: proved
region: interior
subject: einstein
tags: [tractors, cosmological-constant, curvature-and-field-equations]
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
review: typed
derivations:
- name: main
  uses:
  - interior.imported-tractor-connection@2
  - interior.metric-parallelism-trace-schouten-condition@6
  proof: proof-main.tex
- name: standard-route
  uses:
  - dark-energy.imported-frozen-point-geometry-external@1
  proof: proof-standard-route.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:4.7
- kind: check
  ref: check.py::check_einstein_scale_tractor_is_parallel
- kind: check
  ref: check.py::check_only_rho_lambda_over_six_and_only_einstein
- kind: check
  ref: check.py::check_norm_is_lambda_over_three
locators:
  paper: T06
  number: Thm 4.7
  label: thm:lambda
  line: 528
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on GTG Einstein fields (SdS, SAdS, de Sitter, Schwarzschild) calR(a) = Lambda a is computed and ninf + (Lambda/6) n0 is parallel for the Cl(2,4) gauge field; the parallel constant rho is solved and is exactly Lambda/6, none on RN, non-constant rho fails; Q = Lambda/3 with the sign of Lambda. Version 5 -> 6. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 6 -> 7.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: g is the derived metric of a gravitational field on flat spacetime, M-circ its invertible region, the Einstein condition is read on the field strength (R(a) = Lambda a in the store sign) and the scale tractor is the Cl(2,4) vector ninf + rho n0. Proofs prefixed. The tractor theorem is not cited here, since it rests on this result.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    added:
    - interior.imported-tractor-connection
    - dark-energy.imported-frozen-point-geometry-external
    note: 'Added the imported tractor connection, into which the proof substitutes; the standard-route uses the only store entity importing Gover2010 (an external-ingredients entry of the dark-energy paper) and rests on a remark placed after the Lambda = 0 theorem, so it is a judgement call.'
  env: theorem
  eqrefs: 1
---

## formal
Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) and let it satisfy the Einstein condition $\Ric_{ab} = \Lambda\, g_{ab}$ on the invertible region $M^\circ$, that is $\mathcal{R}(a) = \Lambda a$ for the field strength in the conventions of Section \ref{sec:setting}, and set
\[
I_g \;:=\; \Bigl(1,\; 0,\; \tfrac{\Lambda}{6}\Bigr) \;=\; \nInf + \tfrac{\Lambda}{6}\,\nO
\]
in the scale $g$. Then $I_g$ is parallel, and every parallel section of the form $(1, 0, \rho)$ arises this way: $(1,0,\rho)$ is parallel if and only if $\rho$ is constant and $g$ is Einstein with $\Lambda = 6\rho$. The norm is
\[
Q(I_g) \;=\; \tfrac{\Lambda}{3} :
\]
the frozen point is null exactly in the $\Lambda = 0$ vacuum, and for $\Lambda \neq 0$ it leaves the cone, with the cosmological constant as its squared norm (times the positive constant $3$).

## technical
Let a gravitational field on flat spacetime have derived metric $g$ with $\Ric_{ab} = \Lambda g_{ab}$, that is field strength with $\mathcal{R}(a) = \Lambda a$, and set $I_g = (1, 0, \Lambda/6)$, the vector $\nInf + \tfrac{\Lambda}{6}\nO$ of $\Cl(2,4)$, in the scale $g$. Substituting $(1, 0, \rho)$ into the tractor connection shows it is parallel if and only if $\rho$ is constant and $\Sch_{ab} = \rho\,g_{ab}$, which by the trace of the Schouten condition is the Einstein condition with $\Lambda = 6\rho$. So $I_g$ is parallel, and every parallel section of this form arises this way.

Its squared norm is $Q(I_g) = \Lambda/3$. The frozen point is therefore null exactly in the $\Lambda = 0$ vacuum, and for $\Lambda \neq 0$ it leaves the null cone, with the cosmological constant as its squared norm up to the positive factor $3$. The equivalence of the Einstein condition with a parallel scale tractor is the almost-Einstein characterisation of the tractor literature.

## lay
Einstein's equations with a cosmological constant can be written as the statement that one vector of the six-dimensional conformal model, the scale tractor, is unchanged as the gravitational gauge fields carry it from point to point. Its squared length turns out to be the cosmological constant divided by three. With no cosmological constant it has zero length, and any nonzero cosmological constant moves it off the cone of zero-length directions.

## one-liner
For a gravitational field whose derived metric is Einstein with constant $\Lambda$, the section $\nInf + \tfrac{\Lambda}{6}\nO$ is parallel, every parallel section $(1, 0, \rho)$ arises this way, and its squared norm is $\Lambda/3$.
