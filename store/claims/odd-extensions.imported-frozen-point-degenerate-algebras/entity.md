---
id: odd-extensions.imported-frozen-point-degenerate-algebras
kind: claim
version: 4
title: 'Imported: the frozen point at $\Lambda = 0$, and the degenerate algebras'
status: proved
region: odd-extensions
subject: dark-energy
tags: [frozen-point, degenerate-algebras, rotors-and-stabilisers]
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
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - dark-energy.imported-frozen-point-geometry@7
  - sheaf.degeneration-sheaf@6
  - sheaf.one-sided-completion@4
  - sheaf.resolution-ideal-theoretically@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_qi_times_qv
- kind: check
  ref: check.py::check_stabiliser_reductive_iff_non_null
- kind: check
  ref: check.py::check_degenerate_clifford_ideal
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Fact 6.1
  label: fact:null
  line: 569
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): dark-energy.imported-frozen-point-geometry repinned 6 -> 7 after reviewing its restatement (the sentence naming the tractor gauge-field theorem moved to a text-only remark); the parts cited here (parallel frozen point, Q(I) = Lambda/3, the stabilisers, the scale-g display and the Schouten tensor) are unchanged, and the use here holds as cited.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Q(I)Q(V) = -1; the stabiliser of I in so(2,4) is reductive iff Q(I) != 0 and Poincare-type at Q(I) = 0; n Cl(p,q;1) is a square-zero two-sided ideal for p + q <= 4. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: fact
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  - dark-energy.imported-frozen-point-geometry
  - sheaf.degeneration-sheaf
  - sheaf.one-sided-completion
  - sheaf.resolution-ideal-theoretically
  outside_pilot_cites:
  - ButlerT1
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'All five uses are the cited provenance (dark-energy Fact 2.1 and Theorem 3.1; sheaf Theorem
      3.1, Proposition 3.4, Theorem 4.4) and were kept; the further citation of the root paper''s Section
      4 is to a whole section with no single store claim, so it has no edge. Levels pass: conditions already
      kept.'
---

## formal
At $\Lambda = 0$ the parallel scale tractor is null, its stabiliser is parabolic (the Poincar\'e-type stabiliser of a null direction), and the rotation to the reductive de Sitter stabiliser happens exactly when $Q(I) \neq 0$; the identity $Q(I)\,Q(V) = -1$ holds for $\Lambda \neq 0$. A quadratic space with a one-dimensional radical has Clifford algebra $\Cl(p,q;1)$ with a nilpotent generator $n$, $n^{2} = 0$, and $n\,\Cl(p,q;1)$ is a two-sided ideal of square zero; the series treats these algebras, their nilpotent ideals and their one-sided completions in the sheaf paper, and a nilpotent generator is the vector-type zero divisor whose resolution is the transport. \emph{Provenance:} \cite[Fact~2.1, Thm.~3.1]{ButlerT10}; \cite[Thm.~3.1, Prop.~3.4, Thm.~4.4]{ButlerT4}; \cite[\S 4]{ButlerT1}.

## technical
At $\Lambda = 0$ the parallel scale tractor $I$ is null and its stabiliser is parabolic, the Poincar\'e-type stabiliser of a null direction; the stabiliser rotates to the reductive de Sitter type exactly when $Q(I) \neq 0$, and for $\Lambda \neq 0$ the identity $Q(I)\,Q(V) = -1$ holds.

On the algebraic side, a quadratic space with a one-dimensional radical has Clifford algebra $\Cl(p,q;1)$ with a nilpotent generator $n$, $n^{2} = 0$, and $n\,\Cl(p,q;1)$ is a two-sided ideal of square zero. The series treats these degenerate algebras, their nilpotent ideals and their one-sided completions in the sheaf paper, and a nilpotent generator is the vector-type zero divisor whose resolution is the transport.

## lay
When the cosmological constant is exactly zero, the frozen point becomes a vector of zero length, and the symmetry it preserves changes character. On the algebra side, a geometry with one degenerate direction gives an algebra containing an element whose square is zero. The series has already studied such algebras, and treats that element as exactly the kind of breakdown its transport procedure is built to resolve. This entry collects those facts from earlier papers.

## one-liner
At $\Lambda = 0$ the frozen point is null with parabolic stabiliser, and a quadratic space with one-dimensional radical gives $\Cl(p,q;1)$ with a nilpotent generator spanning a square-zero ideal, the vector-type zero divisor the transport resolves.
