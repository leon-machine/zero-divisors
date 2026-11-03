---
id: transport.even-subalgebra-one-dimensional-extension
kind: claim
version: 4
title: The even subalgebra of a one-dimensional extension
status: proved
region: transport
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
  source: authorship disclosure of T01, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:5.13
- kind: check
  ref: check.py::check_images_satisfy_the_relations
- kind: check
  ref: check.py::check_map_is_a_homomorphism
- kind: check
  ref: check.py::check_bijective_onto_even_subalgebra
locators:
  paper: T01
  number: Lem 5.13
  label: lem:even
  line: 1285
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.existence-uniqueness, std-algebra.even-subalgebra-isomorphism (specialises) where the proof uses them. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: Self-contained proof in the source; no edges.
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for both signs of nu and all p + q <= 5, e_i -> e_i nu satisfies the relations of Cl(p,q) or Cl(q,p), is multiplicative on all blade pairs (n <= 4) and is a bijection onto the even subalgebra. Version 1 -> 2. Sample inputs moved to module level; no change to what is tested. Version 2 -> 3.'
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
