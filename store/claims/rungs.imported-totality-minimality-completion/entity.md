---
id: rungs.imported-totality-minimality-completion
kind: claim
version: 6
title: 'Imported: totality and minimality of the completion'
status: proved
region: rungs
subject: completion
tags: [transport-algorithm, hyperbolic-plane, no-go, null-directions]
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
- obj.transport.null-lift-completion
- obj.transport.equivariance
- obj.transport.extension-quadratic-spaces
- obj.std-algebra.hyperbolic-plane
derivations:
- name: main
  uses:
  - transport.minimality@5
  - transport.no-go-level-elements@5
  - transport.totality@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_no_equivariant_pseudo_inverse_of_null_vectors
- kind: check
  ref: check.py::check_conformal_model_adjoins_one_hyperbolic_plane
- kind: check
  ref: check.py::check_transported_reciprocal_total_involutive_continuous
locators:
  paper: T12-rungs
  number: Fact 1.2
  label: fact:totality
  line: 205
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: about the core definitions it is stated in. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the no-go core (null rotations move every pseudo-inverse) in Cl(V) and the ascent, one hyperbolic plane, and iota total, involutive, reciprocal and continuous at null points. Version 3 -> 4. Check entries synced with check.py: +1, -1 (added check_conformal_model_adjoins_one_hyperbolic_plane; removed check_minimal_completion_one_hyperbolic_plane). Version 4 -> 5. check.py: renamed check_minimal_completion_one_hyperbolic_plane to check_conformal_model_adjoins_one_hyperbolic_plane (minimality not tested here); continuity check asserts the four-point Lagrange extrapolation too (fix round 2026-10-23).'
  env: fact
  context_refs:
  - transport.minimality
  - transport.no-go-level-elements
  - transport.totality
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Kept as proved: the Fact restates three root-paper theorems that are in the store (no-go, minimality,
      totality), and all three are real premises of the restatement.'
---

## formal
For a nondegenerate $(\mathbb{V}, Q)$ of mixed signature and dimension $p + q \geq 3$, no extension of $\Cl(\mathbb{V})$ carries a $\mathrm{Spin}^{0}$-equivariant element-level inverse of the null vectors; the minimal null-lift completion is the adjunction of a single hyperbolic plane, $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$, unique up to isometry, in every signature; and on that completion's quadric the transported reciprocal $\iota$ is total, continuous and involutive, agreeing with the geometric reciprocal on invertible vectors and sending every null vector $x_{0}$ to the ideal point $[x_{0} + \tfrac12 n_{\infty}]$, as the limit along every invertible path. \emph{Provenance:} \cite[Thms.~4.2, 4.10, 4.13]{ButlerT1}.

## technical
For a nondegenerate quadratic space $(\mathbb{V}, Q)$ of mixed signature with $p + q \geq 3$, three results of the root paper are taken together. First, no extension of $\Cl(\mathbb{V})$ carries a $\mathrm{Spin}^{0}$-equivariant element-level inverse of the null vectors. Second, the minimal null-lift completion adjoins a single hyperbolic plane, $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$, unique up to isometry in every signature.

Third, on that completion's quadric the transported reciprocal $\iota$ is total, continuous and involutive, agrees with the geometric reciprocal on invertible vectors, and sends every null vector $x_{0}$, with $Q(x_{0}) = 0$, to the ideal point $[x_{0} + \frac12 \nInf]$, which is also the limit along every invertible path.

## lay
This collects three results from the series' founding paper for use in a later note. Vectors of zero length cannot be inverted in any symmetric way, however the algebra is enlarged. But adding exactly one extra pair of dimensions, one of positive and one of negative square, makes the reciprocal defined everywhere on the space of points, and a zero-length vector is then sent to a definite point at infinity.

## one-liner
In mixed signature with $p + q \geq 3$, null vectors have no equivariant element-level inverse in any extension, the minimal completion adjoins one hyperbolic plane, and on its quadric the transported reciprocal is total, sending each null $x_{0}$ to $[x_{0} + \frac12 \nInf]$.
