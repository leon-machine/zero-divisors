---
id: standard-model.two-threshold-criterion
kind: claim
version: 4
title: The two-threshold criterion
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
  ref: check.py::check_level_line_is_the_meeting_condition
- kind: check
  ref: check.py::check_segment_and_reductions
- kind: check
  ref: check.py::check_complete_multiplets_inert_at_either_threshold
locators:
  paper: T12
  number: Thm 8.15
  label: thm:two
  line: 1440
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: solvability exactly on the stated line, exact segment endpoints, the two reductions to one threshold, and inertness at either threshold. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.one-threshold-exact-criterion
    added:
    - standard-model.complete-multiplets-shift-all-three-coefficients
    note: Removed the one-threshold criterion (its reductions are substitutions into the line and it is
      used only as a script cross-check) and added the complete-multiplets lemma for the inertness clause;
      least sure whether the reduction clause should count the one-threshold theorem as a premise.
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.complete-multiplets-shift-all-three-coefficients
about:
- obj.standard-model.one-threshold-spectrum-admissible
---

## formal
Let content $\Dl$ enter at $M_{I}$ and content $\Dl'$ at $M_{I}' \ge M_{I}$, with $f = \ln(M_{U}/M_{I})/\ln(M_{U}/M_{Z})$ and $f' = \ln(M_{U}/M_{I}')/\ln(M_{U}/M_{Z})$, so that $0 \le f' \le f \le 1$. Then the three couplings meet at one scale $M_{U} \ge M_{I}'$ if and only if $(f, f')$ lies on the line
\[
f\,(\Dl_{12} - R\Dl_{23}) + f'\,(\Dl'_{12} - R\Dl'_{23}) \;=\; Rb_{23} - b_{12}
\]
inside the closed triangle $0 \le f' \le f \le 1$, with $\ln(M_{U}/M_{Z}) = 2\pi(a_{1} - a_{2})/(b_{12} + f\Dl_{12} + f'\Dl'_{12}) > 0$; the admissible set is that segment, its endpoints exact rational functions of the inputs. At $f' = f$ it reduces to the one-threshold criterion for $\Dl + \Dl'$, at $f' = 0$ to the one-threshold criterion for $\Dl$ alone, and a complete multiplet added at either threshold leaves the line unchanged.

## technical
Let content $\Dl$ enter at $M_{I}$ and $\Dl'$ at $M_{I}' \ge M_{I}$, with $f = \ln(M_{U}/M_{I})/\ln(M_{U}/M_{Z})$ and $f'$ defined likewise, so $0 \le f' \le f \le 1$. Subtracting the one-loop equations pairwise shows that the couplings meet at one scale $M_{U} \ge M_{I}'$ exactly when $(f, f')$ lies on the line $f(\Dl_{12} - R\Dl_{23}) + f'(\Dl'_{12} - R\Dl'_{23}) = Rb_{23} - b_{12}$ inside that triangle, with $\ln(M_{U}/M_{Z}) > 0$ given by an explicit rational formula.

The admissible set is that segment, with endpoints exact rational functions of the inputs. At $f' = f$ it reduces to the one-threshold criterion for $\Dl + \Dl'$, at $f' = 0$ to that for $\Dl$ alone, and a complete multiplet added at either threshold leaves the line unchanged.

## lay
When new particles enter at two different masses rather than one, asking whether the three forces meet becomes a question about two unknowns. This theorem shows that the answer is a straight line segment inside a triangle of allowed values, with ends that can be computed exactly. It reduces to the single-mass test in the obvious special cases, and adding complete families of particles changes nothing.

## one-liner
With content entering at two thresholds, the couplings meet at one scale exactly when $(f, f')$ lies on an explicit line segment inside $0 \le f' \le f \le 1$ with exact rational endpoints.
