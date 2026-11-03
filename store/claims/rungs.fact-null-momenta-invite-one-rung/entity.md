---
id: rungs.fact-null-momenta-invite-one-rung
kind: claim
version: 7
title: 'Null momenta invite one rung, together'
status: proved
region: rungs
subject: completion
tags: [null-directions, ladder-pairs, no-go, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
about:
- obj.transport.equivariance
- obj.transport.extension-quadratic-spaces
- obj.std-algebra.spacetime-algebra
derivations:
- name: main
  uses:
  - rungs.imported-totality-minimality-completion@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_rungs.py
  tags:
  - label:cor:onerung
- kind: check
  ref: check.py::check_no_equivariant_pseudo_inverse_in_any_extension
- kind: check
  ref: check.py::check_one_rung_for_all_momenta
- kind: check
  ref: check.py::check_reciprocal_total_on_quadric
locators:
  paper: T12-rungs
  number: Cor 3.1
  label: cor:onerung
  line: 303
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: about the core definitions it is stated in. Version 6 -> 7.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: no pseudo-inverse of a null momentum fixed by its null rotations in Cl(1,3), Cl(1,4), Cl(2,3) or Cl(2,4) (exact linear systems), one rung R^(2,4) for all momenta, and iota = e+ . e+ total on the quadric. Version 3 -> 4. check.py docstring (2): span counts corrected (null lifts plus 0 span 5, all 6 with one non-null point); minimality marked imported (fix round 2026-10-23). Version 4 -> 5. Check strengthened: ideal-point test read as Y . ninf = 0 (the e-/e+ index form passed with both indices equal); Q at the non-null samples pinned by hand; samples moved to module level. Version 5 -> 6.'
  env: corollary
  typing:
    by: ai-typing-pass
    note: 'Kept the single premise (the imported totality and minimality Fact, applied to R^{1,3}); replaced the title, which began with a dangling locator, by a descriptive one.'
  source_title: 'Null momenta invite one rung, together'
  source_formal: |-
    Let $p^{1}, \ldots, p^{n}$ be null vectors of $\R^{1,3} \subset \Cl(1,3)$, the momenta of $n$ massless twistors. No extension of $\Cl(1,3)$ carries a $\mathrm{Spin}^{0}$-equivariant element-level inverse of the null vectors, so none inverts the $p^{i}$ in the sense the transport principle asks; the minimal completion that the transport principle prescribes is the single rung $\Cl(2,4)$, unique up to isometry and independent of $n$; and on that completion's quadric the transported reciprocal is total, sending every $p^{i}$ to its ideal point $[p^{i} + \tfrac12 n_{\infty}]$ at once. The transport principle completes the quadratic space, not each zero divisor: a second null momentum invites no second rung.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the massless twistors whose momenta are the $p^{i}$ to massless conformal spinors (formal, technical, proof). Everything else is already geometric algebra.'
---

## formal
Let $p^{1}, \ldots, p^{n}$ be null vectors of $\R^{1,3} \subset \Cl(1,3)$, the momenta of $n$ massless conformal spinors (twistors). No extension of $\Cl(1,3)$ carries a $\mathrm{Spin}^{0}$-equivariant element-level inverse of the null vectors, so none inverts the $p^{i}$ in the sense the transport principle asks; the minimal completion that the transport principle prescribes is the single rung $\Cl(2,4)$, unique up to isometry and independent of $n$; and on that completion's quadric the transported reciprocal is total, sending every $p^{i}$ to its ideal point $[p^{i} + \tfrac12 n_{\infty}]$ at once. The transport principle completes the quadratic space, not each zero divisor: a second null momentum invites no second rung.

## technical
Take $n$ null vectors $p^{1}, \ldots, p^{n}$ of $\R^{1,3} \subset \Cl(1,3)$, the momenta of $n$ massless conformal spinors, so $Q(p^{i}) = 0$. Applying the imported totality and minimality results to the quadratic space $(\R^{1,3}, \eta)$, which is nondegenerate of mixed signature, gives three conclusions at once. No extension of $\Cl(1,3)$ carries a $\mathrm{Spin}^{0}$-equivariant element-level inverse of the null vectors, so none inverts the $p^{i}$. The minimal completion is the single rung $\Cl(2,4)$, unique up to isometry and independent of $n$. On its quadric the transported reciprocal is total and sends every $p^{i}$ to its ideal point $[p^{i} + \frac12 \nInf]$ simultaneously.

The completion is a property of the quadratic space, whose null cone contains every $p^{i}$, and not of the individual zero divisors: a second null momentum does not call for a second rung.

## lay
Massless particles have momenta of zero length in spacetime, and such vectors cannot be divided by. The series' repair for this kind of failure adds one extra pair of dimensions, and this result notes that the same single addition deals with every such momentum at once. However many massless particles are present, one extra step, one rung, is enough, because the repair belongs to the geometry of spacetime rather than to any one particle.

## one-liner
Any number of null momenta in $\R^{1,3}$ are handled together by one rung: no extension inverts them as elements, the minimal completion is the single $\Cl(2,4)$, and its transported reciprocal sends each $p^{i}$ to $[p^{i} + \frac12 \nInf]$.
