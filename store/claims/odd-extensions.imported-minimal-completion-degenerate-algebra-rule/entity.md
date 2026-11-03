---
id: odd-extensions.imported-minimal-completion-degenerate-algebra-rule
kind: claim
version: 5
title: 'Imported: the minimal completion of a degenerate algebra, and Rule 1'
status: proved
region: odd-extensions
subject: completion
tags: [degenerate-algebras, hyperbolic-plane, transport-algorithm, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - conformal.minimal-nondegenerate-completion@6
  - transport.minimality@4
  - transport.one-generator-minimal-minimal-completions-classified@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_lower_bound_dimension
- kind: check
  ref: check.py::check_minimal_completions_signature
- kind: check
  ref: check.py::check_minimal_completion_unique_fixing_v
- kind: check
  ref: check.py::check_type_n_increment_forced
- kind: check
  ref: check.py::check_type_c_sign_forgotten
locators:
  paper: T14a
  number: Fact 8.1
  label: fact:completion
  line: 644
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the lower bound p+q+2r, signature (p+r,q+r) of minimal completions, uniqueness fixing V, the type-N increment and the type-C sign forgotten. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  env: fact
  context_refs:
  - conformal.minimal-nondegenerate-completion
  - transport.minimality
  - transport.one-generator-minimal-minimal-completions-classified
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: The three uses are the cited degenerate-completion, minimality and one-generator classification
      results; the forgotten-sign remark it also cites has no separate store entry.
---

## formal
A real quadratic space with nondegenerate part of signature $(p,q)$ and radical of dimension $r$ admits a nondegenerate completion; every completion has dimension at least $p + q + 2r$; the minimal ones have signature exactly $(p+r, q+r)$; and any two minimal completions are isometric by an isometry fixing the original space pointwise, so the minimal ambient Clifford algebra $\Cl(p+r, q+r)$ is unique up to an isomorphism fixing the embedded $\Cl(p,q;r)$. In the model completion the radical is paired with its dual, $Q(\rho, \varphi) = 1$, $Q(\varphi,\varphi) = 0$, $\varphi$ orthogonal to the nondegenerate part. For a type-N obstruction in a nondegenerate algebra the increment $(+1,+1)$ is forced outright; for a type-C obstruction the completed algebra is unique but the sign of the adjoined generator's square is a geometric datum the algebra forgets. \emph{Provenance:} \cite[Thm.~2.3 and its model]{ButlerT2}; \cite[Thm.~4.13, Thm.~5.7 and Rem.~5.8]{ButlerT1}.

## technical
A real quadratic space with nondegenerate part of signature $(p,q)$ and radical of dimension $r$ has nondegenerate completions, all of dimension at least $p+q+2r$. The minimal ones have signature $(p+r,q+r)$ and are unique up to an isometry fixing the original space, so $\Cl(p+r,q+r)$ is unique up to an isomorphism fixing $\Cl(p,q;r)$. In the model completion each radical vector $\rho$ is paired with a dual $\varphi$, with $Q(\rho,\varphi) = 1$, $Q(\varphi) = 0$ and $\varphi$ orthogonal to the nondegenerate part.

For a type-N obstruction in a nondegenerate algebra the increment $(+1,+1)$ is forced outright. For a type-C obstruction the completed algebra is unique, but the sign $Q(\nu) = \pm 1$ of the adjoined generator is a geometric datum the algebra forgets.

## lay
When a geometric algebra has degenerate directions, the smallest way to remove them adds one partner for each, and the result is unique. For the basic kind of division failure in an ordinary algebra, the repair must add one positive and one negative direction. For another kind, adding a single direction of either sign gives the same algebra, so the algebra alone cannot tell which sign was chosen.

## one-liner
Minimal nondegenerate completions of a space with radical of dimension $r$ add $r$ hyperbolic planes and are unique up to an isometry fixing the space; Rule 1 forces the increment $(+1,+1)$ for type N, while for type C the completed algebra forgets the sign of the adjoined generator.
