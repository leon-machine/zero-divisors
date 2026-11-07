---
id: rule2.imported-gamma-matrices-odd-dimension
kind: claim
version: 2
title: 'Imported: gamma matrices in odd dimension'
status: imported
region: rule2
subject: clifford-structure
tags: [spinor-modules, pseudoscalar-and-centre, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: typed
imported_from:
- citation: 'J. Polchinski, String Theory, Vol. II: Superstring Theory and Beyond, Cambridge University
    Press (1998), Appendix B.'
  key: Polchinski1998
  locator: App.~B
- citation: A. Van Proeyen, Tools for supersymmetry, Ann. Univ. Craiova Phys. 9 (1999) 1--48, arXiv:hep-th/9910030.
  key: VanProeyen1999
  locator: \S 3
locators:
  paper: T17-rule2
  number: Fact 3.1
  label: fact:odd
  line: 193
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (imported) and left in its language: The Fact is about the irreducible matrix representations of the complex Clifford algebra in odd dimension as such (two inequivalent ones, related by Gamma^M -> -Gamma^M), quoted as the sources state it; in the series the two representations are the two signs of the central pseudoscalar, which the entities using it say.'
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported standard fact, no derivation edges.
outside_ga:
  kind: imported
  why: 'The Fact is about the irreducible matrix representations of the complex Clifford algebra in odd dimension as such (two inequivalent ones, related by Gamma^M -> -Gamma^M), quoted as the sources state it; in the series the two representations are the two signs of the central pseudoscalar, which the entities using it say.'
---

## formal
In odd spacetime dimension $n$ the complex Clifford algebra has exactly two inequivalent irreducible representations, each of dimension $2^{(n-1)/2}$, related by $\Gamma^M \mapsto -\Gamma^M$ for all $M$ and distinguished by the scalar value of the product $\Gamma^0\Gamma^1\cdots\Gamma^{n-1}$, which is $\pm$ a fixed phase; equivalently, the last gamma matrix is $\pm$ a fixed multiple of the product of the first $n - 1$. \emph{Provenance:} standard; \cite[App.~B]{Polchinski1998}, \cite[\S 3]{VanProeyen1999}.

## technical
In odd spacetime dimension $n$ the complex Clifford algebra has exactly two inequivalent irreducible representations, each of dimension $2^{(n-1)/2}$. They are related by $\Gamma^{M} \mapsto -\Gamma^{M}$ for all $M$ and are distinguished by the scalar value of $\Gamma^{0}\Gamma^{1}\cdots\Gamma^{n-1}$, which is plus or minus a fixed phase; equivalently, the last gamma matrix is plus or minus a fixed multiple of the product of the first $n - 1$. The result is standard and imported from Polchinski and Van Proeyen.

## lay
Physicists represent the directions of spacetime by matrices called gamma matrices. In an odd number of dimensions there are two genuinely different ways to do this, which differ by an overall sign on every matrix. The two can be told apart by multiplying all the matrices together.

## one-liner
In odd dimension $n$ the complex Clifford algebra has exactly two inequivalent irreducible representations, of dimension $2^{(n-1)/2}$, related by $\Gamma^{M} \mapsto -\Gamma^{M}$.
