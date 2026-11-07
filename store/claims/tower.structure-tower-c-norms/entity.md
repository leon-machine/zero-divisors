---
id: tower.structure-tower-c-norms
kind: claim
version: 8
title: The *-structure of the tower, and its C*-norms
status: proved
region: tower
subject: tower
tags: [car-algebra]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 8
  source: maintainer pass 2026-11-07 (GA units)
review: typed
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.algebraic-limit-even-charge@3
  - tower.commuting-copies@5
  - tower.compatibility-connecting-maps-transported@6
  - transport.rule-1-morita-trivial@5
  - std-algebra.involution-properties@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T03.py
  tags:
  - num:5.4
- kind: check
  ref: check.py::check_star_exists_unique_antimultiplicative
- kind: check
  ref: check.py::check_frame_unitary_and_ladder_adjoint
- kind: check
  ref: check.py::check_maps_and_correctors_compatible
- kind: check
  ref: check.py::check_even_floors_are_full_matrix_star_algebras
locators:
  paper: T03
  number: Lem 5.4
  label: lem:cstar
  line: 409
outside_ga:
  kind: other
  why: 'the result is about the complexified floors T_k^C, and the renormalisation y_i = i x_i applies the complexification''s scalar to ground generators, spacetime vectors among them, which no pseudoscalar commutes with'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the result is about the complexified floors T_k^C, and the renormalisation y_i = i x_i applies the complexification''s scalar to ground generators, spacetime vectors among them, which no pseudoscalar commutes with.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.involution-properties where the proof uses them. Version 6 -> 7.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the * as the generator-determined antiautomorphism, unitarity of frame blades and volumes, v* = w, phi_k and the correctors V_k, W_k compatible with *, and the tensor-Pauli *-isomorphism for even floors. Version 3 -> 4. check_star_exists_unique_antimultiplicative: dropped the m <= 5 guard, so antimultiplicativity on every pair of basis blades now runs on the m = 6 floors too, matching docstring (1). Version 4 -> 5. Sample inputs moved to module level; floor counts read from the case list; no change to what is tested. Version 5 -> 6.'
  env: lemma
  context_refs:
  - tower.algebraic-limit-even-charge
  - tower.commuting-copies
  - tower.compatibility-connecting-maps-transported
  typing:
    by: ai-typing-pass
    added:
    - tower.algebraic-limit-even-charge
    - tower.commuting-copies
    - tower.compatibility-connecting-maps-transported
    note: 'The statement asserts *-compatibility of the maps and correctors constructed in the three context
      results and the proof checks it from their explicit form, so they were added as premises; the rule-1
      matrix units are also used directly. Levels pass: conditions already kept.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$y_i := i\,x_i$: the scalar of the complexified floors $T_k^{\,\C}$, applied to ground generators
      including spacetime vectors (complexified algebra); indices $i$ (index)'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - tower.algebraic-limit-even-charge
    - tower.commuting-copies
    - tower.compatibility-connecting-maps-transported
---

## formal
Fix the tower's frames: an orthogonal ground frame $x_1, \dots, x_n$ diagonalising $Q$, and the plane frames $e_j, f_j$. On each complexified floor $T_k^{\,\C}$ there is a unique conjugate-linear antiautomorphism $*$ with $x^* = x$ for every frame generator with $x^2 = 1$ and $x^* = -x$ for every frame generator with $x^2 = -1$. Under it: every frame generator, every blade in the frame, and every ground or plane volume element is unitary ($z^* z = 1$); the ladder pairs are mutually adjoint, $v_j^* = w_j$; the connecting maps $\iota_k$, the identifications $\varphi_k$ of Theorem \claimref{tower.commuting-copies}, the block doublings $\theta_k$, and the correctors $V_k$ and $W_k$ of Lemma \claimref{tower.compatibility-connecting-maps-transported} and Theorem \claimref{tower.algebraic-limit-even-charge} are all compatible with $*$ (the maps are *-homomorphisms, the correctors unitary). If moreover $p - q$ is even, each $T_k^{\,\C}$ is *-isomorphic to $\Mat_{2^{m/2}}(\C)$, $m := n + 2k$, with $*$ the conjugate transpose; consequently each floor carries a unique C*-norm, every unital *-monomorphism between floors is isometric, and the increasing union $\bigcup_k T_k^{\,\C}$ carries a unique C*-norm.

## technical
On each complexified floor $T_k^{\,\C}$ of the tower, with frame generators fixed, there is a unique conjugate-linear antiautomorphism $*$ fixing every frame generator with $Q(x) = 1$ and negating every frame generator with $Q(x) = -1$. Under it every frame generator, frame blade and ground or plane volume element is unitary, $z^* z = 1$; the ladder pairs are mutually adjoint, $v_j^* = w_j$; the connecting maps $\iota_k$, the identifications $\varphi_k$ and the block doublings $\theta_k$ are *-homomorphisms; and the correctors $V_k$, $W_k$ are unitary.

If moreover $p - q$ is even, a tensor-Pauli representation identifies $T_k^{\,\C}$ with $\Mat_{2^{m/2}}(\C)$, $m = n + 2k$, carrying $*$ to the conjugate transpose. Consequently each floor has a unique C*-norm, every unital *-monomorphism between floors is isometric, and the increasing union $\bigcup_k T_k^{\,\C}$ carries a unique C*-norm.

## lay
Once complex numbers are allowed, each level of the tower of algebras carries a natural notion of adjoint, fixed by how it acts on the basic generators, and every map used to build the tower respects it. When the signature difference is even, every level is an ordinary algebra of complex square matrices. Such an algebra has exactly one way of measuring size that is compatible with the adjoint, and so does the union of all the levels.

## one-liner
Each complexified floor of the tower has a unique frame-adapted *-structure respected by all the tower's maps and correctors, and for $p - q$ even each floor is a full complex matrix algebra, so the floors and their union carry unique C*-norms.
