---
id: transport.exhaustiveness-every-zero-divisor-annihilated-idempotent
kind: claim
version: 4
title: 'Exhaustiveness: every zero divisor is annihilated by an idempotent'
status: proved
region: transport
subject: zero-divisors
tags: [obstruction-types, idempotents, classification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 4
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.classification-real-clifford-algebras@3
  - transport.existence-classification-type-c@4
  - transport.existence-locus-type-n@5
  - transport.regularity-localises-zero-divisors-idempotents@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_every_zero_divisor_annihilated_both_sides
- kind: check
  ref: check.py::check_simple_signatures_only_noncentral_annihilators
- kind: check
  ref: check.py::check_split_signatures_central_or_type_p
- kind: check
  ref: check.py::check_isotropic_origin_in_mixed_signatures
locators:
  paper: T01
  number: Thm 3.9
  label: thm:annihilator
  line: 642
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Decision item E7 (routine; no retirement): clause (1) overlaps std-algebra.zero-divisors-annihilated (d), (e), the general statement and home; recorded under extraction.overlaps_with (a clause-level overlap, no pinned link).'
  overlaps_with:
  - id: std-algebra.zero-divisors-annihilated
    note: 'Decision E7: clause (1) here is clause (d), (e) of std-algebra.zero-divisors-annihilated, kept as the general statement; overlap in part, so no pinned link.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for 14 zero divisors in 12 signatures, idempotents e, f outside {0, 1} with a(1 - e) = (1 - f)a = 0 from exact annihilator kernels, non-central in the simple signatures, central eps exactly for elements inside one ideal in the split ones, and the hyperbolic idempotent wv for null vectors. Version 1 -> 2. Sample inputs moved to module level; nullity of v and w (the hypothesis) asserted. Version 2 -> 3.'
  env: theorem
  unresolved_refs:
  - ex:hyperbolic-idem
  typing:
    by: ai-typing-pass
    note: 'Edges kept: all four premises are invoked in the proof.'
---

## formal
Let $A = \Cl(p,q)$ be nondegenerate, $a \in A$ a nonzero zero divisor. Then:
\begin{enumerate}
\item There exist idempotents $e, f \notin \{0, 1\}$ with $a(1-e) = 0$ and $(1-f)a = 0$ (so $a$ both left-annihilates and is right-annihilated by nontrivial idempotents).
\item If $p - q \not\equiv 1 \pmod 4$, every such idempotent is non-central: the obstruction carried by $a$ is of type P, refined to type N exactly when the annihilating idempotent is the $wv$ of a hyperbolic pair, as in Example \ref{ex:hyperbolic-idem}.
\item If $p - q \equiv 1 \pmod 4$, the element $a$ may in addition be annihilated by a \emph{central} idempotent (this happens exactly when $\varepsilon_+ a = 0$ or $\varepsilon_- a = 0$, i.e.\ when $a$ lies entirely in one simple ideal): type C. Every zero divisor not of this kind is again of type P within its ideal(s).
\end{enumerate}
Consequently the taxonomy N/P/C of Definition \claimref{obj.transport.obstruction-types} is exhaustive: every failure of invertibility in a real Clifford algebra of nondegenerate form is localised at an idempotent, non-central in the simple signatures, possibly central exactly in the signatures $p - q \equiv 1 \pmod 4$, and of isotropic-vector origin exactly in the mixed signatures.

## technical
Let $A = \Cl(p,q)$ be nondegenerate and $a \neq 0$ a zero divisor. Then there are idempotents $e, f \notin \{0, 1\}$ with $a(1 - e) = 0$ and $(1 - f)a = 0$. If $p - q \not\equiv 1 \pmod 4$ every such idempotent is non-central, so the obstruction is type P, refined to type N exactly when the annihilating idempotent is $wv$ for a hyperbolic pair. If $p - q \equiv 1 \pmod 4$, $a$ may also be annihilated by a central idempotent, which happens exactly when $a$ lies entirely in one simple ideal (type C); otherwise it is again type P within its ideals.

So the taxonomy N, P, C is exhaustive: every failure of invertibility is localised at an idempotent, non-central in the simple signatures, possibly central exactly when $p - q \equiv 1 \pmod 4$, and of isotropic-vector origin exactly in the mixed signatures.

## lay
Whenever division fails in a Clifford algebra with a nondegenerate notion of length, the failure can be traced to an element that equals its own square. This shows that the three kinds of failure already named cover every case. Which kinds occur depends only on the numbers of space and time directions.

## one-liner
Every nonzero zero divisor of a nondegenerate real Clifford algebra is annihilated on each side by a nontrivial idempotent, so the N, P, C taxonomy of obstructions is exhaustive.
