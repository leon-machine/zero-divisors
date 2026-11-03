---
id: tower.volume-elements-planes
kind: claim
version: 5
title: Volume elements of the planes
status: proved
region: tower
subject: tower
tags: [pseudoscalar-and-centre, hyperbolic-plane]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
review: typed
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T03.py
  tags:
  - num:3.1
- kind: check
  ref: check.py::check_plane_volume_elements
- kind: check
  ref: check.py::check_product_omega_k
locators:
  paper: T03
  number: Lem 3.1
  label: lem:volumes
  line: 222
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.orthogonal-anticommute where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: omega_j^2 = 1, own-plane anticommutation, commutation with everything else, and the Omega_k properties for n <= 3, k <= 3. Version 2 -> 3. Sample inputs moved to module level; no change to what is tested. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Self-contained parity count with no store references, so no edges.'
---

## formal
Let $\omega_j = e_j f_j$. Then $\omega_j^2 = 1$; $\omega_j$ anticommutes with $e_j$ and $f_j$; $\omega_j$ commutes with $e_i, f_i$ for $i \neq j$ and with every ground generator; and the $\omega_j$ commute pairwise. Hence $\Omega_k := \omega_1 \cdots \omega_k$ satisfies $\Omega_k^2 = 1$, commutes with all ground generators, and anticommutes with each $e_j, f_j$, $j \leq k$.

## technical
For each added plane with generators $e_j, f_j$, the plane volume element $\omega_j = e_j f_j$ satisfies $\omega_j^2 = 1$, anticommutes with $e_j$ and $f_j$, and commutes with the generators of every other plane and with every ground generator; the $\omega_j$ also commute pairwise. Each fact is a count of how many letters anticommute.

Consequently the product $\Omega_k = \omega_1 \cdots \omega_k$ satisfies $\Omega_k^2 = 1$, commutes with all ground generators, and anticommutes with each $e_j$ and $f_j$ for $j \leq k$.

## lay
Each new plane added to the algebra has its own volume element, the product of its two generators. These elements square to one, flip the sign of their own plane's generators, and commute with everything else, including each other. Multiplying them all together gives a single element with the same behaviour towards all the added planes at once.

## one-liner
The plane volume elements $\omega_j = e_j f_j$ square to one, anticommute with their own plane, commute with all other generators and with each other, and their product $\Omega_k$ squares to one, commutes with the ground generators and anticommutes with every plane generator.
