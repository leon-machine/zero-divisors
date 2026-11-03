---
id: rule2.even-subalgebra-one-dimensional-extension
kind: claim
version: 4
title: The even subalgebra of a one-dimensional extension
status: proved
region: rule2
subject: clifford-structure
tags: [grading-and-parity]
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
review: typed
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T17_rule2.py
  tags:
  - label:lem:even
- kind: check
  ref: check.py::check_spacelike_nu_gives_cl_pq
- kind: check
  ref: check.py::check_timelike_nu_gives_cl_qp
locators:
  paper: T17-rule2
  number: Lem 2.1
  label: lem:even
  line: 121
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.existence-uniqueness, std-algebra.even-subalgebra-isomorphism (specialises) where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: e_i -> e_i nu is an isomorphism onto the even subalgebra for both signs of nu, every (p,q) with p + q <= 5. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Self-contained proof in the source; no edges. Same statement and proof as the transport-region
      lemma. Linked equivalent_to transport.even-subalgebra-one-dimensional-extension: the companion note
      restates it.'
equivalent_to:
- transport.even-subalgebra-one-dimensional-extension@4
specialises:
- std-algebra.even-subalgebra-isomorphism@1
---

## formal
Let $\nu$ be a generator adjoined orthogonally to $\Cl(p,q)$. If $\nu^2 = -1$ then $e_i \mapsto e_i\nu$ extends to an isomorphism $\Cl(p,q) \cong \Cl^0(p,q{+}1)$; if $\nu^2 = +1$ then the same map gives $\Cl(q,p) \cong \Cl^0(p{+}1,q)$.

## technical
Adjoin to $\Cl(p,q)$ one generator $\nu$ orthogonal to the generating space. The products $e_i\nu$ are even, pairwise anticommute and satisfy $(e_i\nu)^{2} = -Q(e_i)\,Q(\nu)$. So if $Q(\nu) = -1$ they obey the relations of $\Cl(p,q)$ and $e_i \mapsto e_i\nu$ gives $\Cl(p,q) \cong \Cl^{0}(p, q+1)$, while if $Q(\nu) = +1$ they obey those of $\Cl(q,p)$ and the same map gives $\Cl(q,p) \cong \Cl^{0}(p+1, q)$.

The universal property supplies the homomorphisms, the products of images reach every even blade, and both sides have dimension $2^{n}$.

## lay
Add one extra perpendicular direction to a Clifford algebra and then keep only its even part, the products of an even number of directions. The result has the size of the original algebra, and this lemma identifies it exactly. It is the original algebra when the new direction squares to minus one, and the original with its positive and negative directions swapped when the new direction squares to plus one.

## one-liner
Adjoining an orthogonal generator $\nu$ to $\Cl(p,q)$ gives $\Cl^{0}(p, q+1) \cong \Cl(p,q)$ when $Q(\nu) = -1$ and $\Cl^{0}(p+1, q) \cong \Cl(q,p)$ when $Q(\nu) = +1$, via $e_i \mapsto e_i\nu$.
