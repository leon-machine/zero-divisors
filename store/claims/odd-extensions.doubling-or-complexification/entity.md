---
id: odd-extensions.doubling-or-complexification
kind: claim
version: 6
title: Doubling or complexification
status: proved
region: odd-extensions
subject: clifford-structure
tags: [pseudoscalar-and-centre, grading-and-parity, clifford-classification]
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
- name: Claude Opus 5.5
  role: 'consistency pass, bare imaginary unit replaced by the central volume element (U3)'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 6
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.odd-extensions.single-extension
derivations:
- name: main
  uses:
  - odd-extensions.volume-element-odd-dimension@4
  - std-algebra.z2-grading@1
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14a.py
  tags:
  - num:2.3
- kind: check
  ref: check.py::check_omega_plus_one_doubling
- kind: check
  ref: check.py::check_omega_minus_one_complexification
- kind: check
  ref: check.py::check_even_subalgebra_identities
locators:
  paper: T14a
  number: Thm 2.3
  label: thm:split
  line: 441
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version kept at 6 (already raised in this run). Decision item E7 (routine; no retirement): specialises std-algebra.even-subalgebra-isomorphism@1 added. Clause (iii) here (Cl^0 = Cl(p,q) or Cl(q,p) via e_i e_n) is the odd-dimensional case of the standard even-subalgebra isomorphism, so this result joins the existing chain (rule2.even-subalgebra-one-dimensional-extension already specialises it); the overlap of clauses (i), (ii) with std-algebra.complexification (ii) is recorded under extraction.overlaps_with.'
  overlaps_with:
  - id: std-algebra.complexification
    note: 'Decision E7: clauses (i), (ii) here overlap clause (ii) of std-algebra.complexification; kept both.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Unit principle U3: the bare i of the proof (x (x) (a + bi)) and the abstract C of clause (ii) are written with the central volume element omega, the unit the clause already names, as in std-algebra.complexification-is-the-odd-extension (span{1, I_W}); exact check in scratch: omega central with omega^2 = -1 in Cl(1,2). Mathematics unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.z2-grading, std-algebra.orthogonal-anticommute where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Statement corrected to the proof''s form: e_n acts on the summand of (1 +- omega)/2 as +- s omega'' with s = e_n^2 (the earlier wording +- omega'' fails when s = -1, e.g. Cl(2,1)); also own exact check added: over every odd signature of dimension 1, 3, 5, the doubling by (1 +- omega)/2 with the e_n sign pairing +-s omega'', the complexification Cl^0 + omega Cl^0, and Cl^0 = Cl(p,q) or Cl(q,p) via e_i e_n. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    removed:
    - odd-extensions.four-extensions-oriented-pair
    added:
    - odd-extensions.volume-element-odd-dimension
    note: Removed the edge to the four-extensions corollary, which the proof mentions only for the script's
      checks (and which itself uses this theorem, the E301 cycle); added the volume-element lemma, which
      supplies the centrality of omega the proof uses.
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - odd-extensions.volume-element-odd-dimension
specialises:
- std-algebra.even-subalgebra-isomorphism@1
---

## formal
Let $n$ be odd and let $\Cl^{0}$ be the even subalgebra of $\Cl(p,q)$.
\begin{enumerate}
\item[(i)] If $\omega^{2} = +1$, then $\Cl(p,q) \cong \Cl^{0} \oplus \Cl^{0}$, the two summands the ideals of the complementary central idempotents $(1 \pm \omega)/2$, and on the summand of $(1 \pm \omega)/2$ the generator $e_{n}$ acts as $\pm s\,\omega'$, with $s = e_{n}^{2}$ and $\omega' = e_{1}\cdots e_{n-1}$ the volume element of the shadow (so the two summands carry opposite signs).
\item[(ii)] If $\omega^{2} = -1$, then $\Cl(p,q) \cong \Cl^{0} \otimes_{\R} \mathrm{span}\{1, \omega\}$, the field $\mathrm{span}\{1, \omega\} \cong \C$ having the central $\omega$ as its unit.
\item[(iii)] $\Cl^{0}(p, q+1) \cong \Cl(p,q)$ and $\Cl^{0}(p+1, q) \cong \Cl(q,p)$.
\end{enumerate}

## technical
Let $n$ be odd, so the volume element $\omega$ of $\Cl(p,q)$ is central, and let $\Cl^{0}$ be the even subalgebra. If $\omega^{2} = +1$, the complementary central idempotents $(1 \pm \omega)/2$ split the algebra as $\Cl(p,q) \cong \Cl^{0} \oplus \Cl^{0}$, and on the summand of $(1 \pm \omega)/2$ the generator $e_n$ acts as $\pm s\,\omega'$, with $s = e_n^{2}$ and $\omega' = e_1 \cdots e_{n-1}$ the volume element of the shadow. If $\omega^{2} = -1$, then $\omega$ is a central unit of square $-1$ and $\Cl(p,q) \cong \Cl^{0} \otimes_{\R} \mathrm{span}\{1, \omega\}$, the complexification of $\Cl^{0}$ with unit $\omega$.

Separately, the even subalgebra of a one-generator extension is a Clifford algebra of one dimension fewer: $\Cl^{0}(p, q+1) \cong \Cl(p,q)$ and $\Cl^{0}(p+1, q) \cong \Cl(q,p)$.

## lay
In an odd number of dimensions, the product of all the basis directions commutes with everything. If it squares to plus one, the algebra falls apart into two identical copies of its even part, the part built from products of an even number of directions. If it squares to minus one, it behaves like the imaginary unit and the algebra is that even part with complex coefficients allowed. The even part itself is always a Clifford algebra of one dimension fewer.

## one-liner
An odd-dimensional $\Cl(p,q)$ is two copies of its even subalgebra when $\omega^{2} = +1$ and that subalgebra complexified when $\omega^{2} = -1$, and the even subalgebra is a Clifford algebra of one dimension fewer.
