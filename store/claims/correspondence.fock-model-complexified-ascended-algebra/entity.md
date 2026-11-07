---
id: correspondence.fock-model-complexified-ascended-algebra
kind: claim
version: 8
title: "The Fock model of the complexified ascended algebra"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [spinor-modules, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 8
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  - std-algebra.complex-clifford-algebra@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:thm:purespinor
- kind: check
  ref: check.py::check_isotropic_pair_and_clifford_relations
- kind: check
  ref: check.py::check_blade_products_span_all_endomorphisms
- kind: check
  ref: check.py::check_chirality_halves_and_even_subalgebra
- kind: check
  ref: check.py::check_dual_pairs_conjugate_under_orthogonal_group
locators:
  paper: T09
  number: Thm 3.1
  label: thm:purespinor
  line: 337
outside_ga:
  kind: other
  why: 'the Fock model is built over V_C, and its complex isotropic vector w_3 = b_3 + i b_4 needs a scalar that commutes with the vectors, which no pseudoscalar of Cl(2,4) does'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the Fock model is built over V_C, and its complex isotropic vector w_3 = b_3 + i b_4 needs a scalar that commutes with the vectors, which no pseudoscalar of Cl(2,4) does.'
  maintainer_pass_2026_10_31:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 7: the two steps that read real core results over C now cite std-algebra.complex-clifford-algebra (i) (new uses edge): the existence and universal property of Cl(V_C) over C, which std-algebra.existence-uniqueness gives in the real case, and the spanning of Cl(V_C) by the 64 ordered products of a basis. Statement and argument unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.existence-uniqueness where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Fock model of Cl(2,4)_C over Q(i): isotropic dual pair, Clifford relations, the 64 blade images independent (Cl = End), chirality halves with Cl^0 = End + End, and conjugacy of dual pairs under O(V_C). Version 3 -> 4. Check strengthened: sample inputs moved to module level and the values the mutation test could not see pinned. Version 4 -> 5.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'No edges; the construction is Chevalley''s, but no imported claim stating it is in the store,
      so no standard route. Levels pass: conditions already kept.'
  source_title: "The Fock model of the complexified ascended algebra"
  source_formal: |-
    Let $W \subset V_\C$ be a maximal totally isotropic subspace ($\dim_\C W = 3$) and $W'$ a complementary maximal isotropic subspace, dual to $W$ under the $\C$-bilinear form (such a pair exists, and any two such pairs are conjugate under $O(V_\C)$). On the exterior algebra $\Lambda^\bullet W$ ($\dim_\C = 2^3 = 8$) define
    \[
    c(w) := \sqrt2\; w \wedge (\cdot) \quad (w \in W),
    \qquad
    c(w') := \sqrt2\; \iota_{w'} \quad (w' \in W'),
    \]
    with $\iota$ contraction through the pairing. Then $c(u)^2 = \ip{u}{u}\,\id$ for every $u \in W \oplus W' = V_\C$, so $c$ extends to an algebra map $\Cl(V_\C) \to \End(\Lambda^\bullet W)$; this map is an isomorphism, and $\Lambda^\bullet W$ is the unique irreducible module of $\Cl(2,4)_\C$: the Dirac spinors of the completion. Vectors act oddly, so the even and odd halves
    \[
    \T := \Lambda^{\mathrm{even}} W, \qquad \T' := \Lambda^{\mathrm{odd}} W,
    \]
    each of complex dimension 4, are modules of the even subalgebra $\Cl^0(2,4)_\C \cong \End(\T) \oplus \End(\T')$: the two chiralities.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed the two halves to the conformal spinor space and its opposite chirality (\\CS, \\CSm), twistor names kept once in parentheses. The complexified Fock model itself ($V_\\C$, $\\Cl(2,4)_\\C$, the complex isotropic basis with $w_3 = b_3 + i\\,b_4$) is kept: $I_6$ anticommutes with vectors and $\\Cl^0(2,4)_\\C$ is twice the size of $\\Cl^+(2,4)$, so the dictionary's unit $I_6$ does not replace this complexification."
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "$w_3 = b_3 + i\\,b_4$ and the Fock model over $V_\\C$: the complexified conformal space, kept as the earlier pass kept it"
---

## formal
Let $W \subset V_\C$ be a maximal totally isotropic subspace ($\dim_\C W = 3$) and $W'$ a complementary maximal isotropic subspace, dual to $W$ under the $\C$-bilinear form (such a pair exists, and any two such pairs are conjugate under $O(V_\C)$). On the exterior algebra $\Lambda^\bullet W$ ($\dim_\C = 2^3 = 8$) define
\[
c(w) := \sqrt2\; w \wedge (\cdot) \quad (w \in W),
\qquad
c(w') := \sqrt2\; \iota_{w'} \quad (w' \in W'),
\]
with $\iota$ contraction through the pairing. Then $c(u)^2 = Q(u)\,\id$ for every $u \in W \oplus W' = V_\C$, so $c$ extends to an algebra map $\Cl(V_\C) \to \End(\Lambda^\bullet W)$; this map is an isomorphism, and $\Lambda^\bullet W$ is the unique irreducible module of $\Cl(2,4)_\C$: the Dirac spinors of the completion. Vectors act oddly, so the even and odd halves
\[
\CS := \Lambda^{\mathrm{even}} W, \qquad \CSm := \Lambda^{\mathrm{odd}} W,
\]
each of complex dimension 4, are modules of the even subalgebra $\Cl^0(2,4)_\C \cong \End(\CS) \oplus \End(\CSm)$: the two chiralities, the conformal spinor space $\CS$ and its opposite $\CSm$ (twistor and dual twistor space).

## technical
Choose a maximal totally isotropic subspace $W \subset V_\C$, of complex dimension three, and a dual isotropic complement $W'$; such pairs exist and any two are conjugate under $O(V_\C)$. On $\Lambda^\bullet W$, of dimension $8$, set $c(w) = \sqrt2\,w\wedge(\cdot)$ for $w \in W$ and $c(w') = \sqrt2\,\iota_{w'}$ for $w' \in W'$. Then $c(u)^2 = Q(u)\,\id$ for every $u \in V_\C$, so $c$ extends to an isomorphism $\Cl(V_\C) \cong \End(\Lambda^\bullet W)$, and $\Lambda^\bullet W$ is the unique irreducible module of $\Cl(2,4)_\C$: the Dirac spinors of the completion.

Vectors act oddly, so the even and odd parts $\CS = \Lambda^{\mathrm{even}}W$ and $\CSm = \Lambda^{\mathrm{odd}}W$, each of dimension four, are modules of the even subalgebra $\Cl^0(2,4)_\C \cong \End(\CS)\oplus\End(\CSm)$: the two chiralities, the conformal spinor space and its opposite.

## lay
The completed algebra of six directions can be represented concretely. Pick three complex directions that are mutually lightlike, and let the algebra act on all combinations of them by adding or removing a direction, much as one creates and destroys particles. This gives an eight-dimensional space on which the algebra acts faithfully and irreducibly, the only such space up to equivalence, and it splits into two four-dimensional halves, the two chiralities.

## one-liner
The exterior algebra on a maximal isotropic subspace, with wedge and contraction operators, is the unique irreducible module of the complexified Clifford algebra $\Cl(2,4)_\C$, and its even and odd halves are the two four-dimensional chiralities.
