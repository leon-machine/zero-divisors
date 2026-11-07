---
id: transport.corner-even-subalgebra
kind: claim
version: 5
title: The corner is the even subalgebra
status: proved
region: transport
subject: clifford-structure
tags: [idempotents, grading-and-parity]
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
  role: 'consistency pass, standing hypotheses of the section stated in the formal level'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - transport.ascent-renders-grade-involution-inner@3
  - transport.decomposition-commutation@3
  - std-algebra.z2-grading@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:5.3
- kind: check
  ref: check.py::check_corner_map_is_unital_homomorphism
- kind: check
  ref: check.py::check_corner_map_is_bijective
- kind: check
  ref: check.py::check_extension_adds_nothing_to_corner
locators:
  paper: T01
  number: Lem 5.3
  label: lem:corner
  line: 1157
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. The formal level used A, eps_pm and B_gamma from the paper''s section setting (note.transport.setting-setting-one-adjoined-generator) without stating them; the standing hypothesis p - q = 1 mod 4, already in the technical level and one-liner, is now in the formal level. No change of mathematics; no edge added.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.z2-grading where the proof uses them. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: Both edges are cited premises and kept; the section's standing type C hypothesis is not added
      as an edge, to avoid a version bump for a setting-level citation.
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for the 10 signatures with p - q = 1 mod 4 and n <= 7, a -> eps_+ a is a unital homomorphism and a bijection Cl^0 -> eps_+ A, and eps_+ B_gamma eps_+ = eps_+ A for both gamma. Version 1 -> 2. Sample inputs moved to module level; even-basis count 2^(n-1) asserted. Version 2 -> 3.'
---

## formal
Let $A = \Cl(p,q)$ with $p - q \equiv 1 \pmod 4$, split by the central idempotents $\varepsilon_\pm = \tfrac12(1 \pm \omega)$, let $\Cl^0(p,q)$ be its even subalgebra, and let $B_\gamma = A \oplus A\nu$ be its one-generator ascent. The map $\phi : \Cl^0(p,q) \to \varepsilon_+ A$, $\phi(a) = \varepsilon_+ a$, is an isomorphism of unital algebras (with unit $\varepsilon_+$ on the right-hand side). Moreover $\varepsilon_+ B_\gamma\, \varepsilon_+ = \varepsilon_+ A$.

## technical
In the setting where $A = \Cl(p,q)$ with $p - q \equiv 1 \pmod 4$ splits along the central idempotents $\varepsilon_\pm = \tfrac12(1 \pm \omega)$, and $B_\gamma$ is its extension by an orthogonal generator $\nu$, the map $\phi(a) = \varepsilon_+ a$ is an isomorphism of unital algebras from the even subalgebra $\Cl^{0}(p,q)$ onto the corner $\varepsilon_+ A$, whose unit is $\varepsilon_+$. Injectivity uses that $\omega$ is odd, and surjectivity a dimension count.

Moreover the extension adds nothing to the corner: $\varepsilon_+ B_\gamma\, \varepsilon_+ = \varepsilon_+ A$, because $B_\gamma = A \oplus A\nu$ and $\nu\,\varepsilon_+ = \varepsilon_-\,\nu$.

## lay
When an algebra splits into two blocks, each block can be compared with the algebra's even part, built from products of an even number of directions. This result shows each block is an exact copy of that even part. It also shows that enlarging the algebra by one extra direction and then cutting back down to the block returns the same block.

## one-liner
For $p - q \equiv 1 \pmod 4$, $a \mapsto \varepsilon_+ a$ is a unital isomorphism $\Cl^{0}(p,q) \to \varepsilon_+ A$, and $\varepsilon_+ B_\gamma \varepsilon_+ = \varepsilon_+ A$.
