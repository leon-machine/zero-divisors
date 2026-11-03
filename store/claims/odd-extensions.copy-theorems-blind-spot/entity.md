---
id: odd-extensions.copy-theorems-blind-spot
kind: claim
version: 5
title: The copy theorem's blind spot
status: proved
region: odd-extensions
subject: dark-matter
tags: [mirror-sector, pseudoscalar-and-centre, towers-by-residue]
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
about:
- obj.odd-extensions.single-extension
derivations:
- name: main
  uses:
  - odd-extensions.twistor-algebra@6
  - odd-extensions.imported-representatives-dimension-nearest-four-types@4
  - odd-extensions.imported-towers-clock@4
  - odd-extensions.two-towers-one-curved-universe@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_even_subalgebra_is_mat4c
- kind: check
  ref: check.py::check_both_shadows_inside
- kind: check
  ref: check.py::check_rungs_not_isomorphic
- kind: check
  ref: check.py::check_odd_extensions_differ
locators:
  paper: T14a
  number: Cor 4.2
  label: cor:blind
  line: 531
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Cl^0(2,4) = Cl(2,3) = Cl(4,1) = Mat(4,C) with the shadows inside it, the rung types H and R, and the differing centres of the odd extensions. Version 4 -> 5.'
  env: corollary
  context_refs:
  - odd-extensions.imported-representatives-dimension-nearest-four-types
  - odd-extensions.imported-towers-clock
  - odd-extensions.two-towers-one-curved-universe
  typing:
    by: ai-typing-pass
    added:
    - odd-extensions.imported-representatives-dimension-nearest-four-types
    - odd-extensions.imported-towers-clock
    - odd-extensions.two-towers-one-curved-universe
    note: 'Added the two Facts the statement invokes with ''by'' for the rungs'' types and the later curved-universe
      proposition for the claim that no derived quantity uses the fifth generator (a forward reference);
      the E204 here comes from the twistor-algebra theorem outside this list. Levels pass: conditions
      already kept.'
  source_title: 'The copy theorem''s blind spot'
  source_formal: |-
    The copy theorem identifies this world and its mirror by working in an algebra, $\Cl^{0}(2,4) \cong \Cl(2,3)$, that contains both real forms and is the complexification of each. It is therefore exactly blind to the distinction that a single extension sees: the two oriented towers have isomorphic conformal spin groups, isomorphic twistor modules and one complexified ambient, but odd extensions that signature reversal does not identify (Theorem \claimref{odd-extensions.twistor-algebra}(iv)), whose centres differ. The shadows themselves are non-isomorphic (Fact \claimref{odd-extensions.imported-representatives-dimension-nearest-four-types}); every object the copy theorem is built from, the even subalgebra of the rung, the conformal spin group and the twistor module (Theorem \claimref{odd-extensions.twistor-algebra}(iii)), identifies the two towers, while the rungs themselves, $\Cl(2,4)$ and $\Cl(4,2)$, do not, being of the two towers' types by Facts \claimref{odd-extensions.imported-towers-clock} and \claimref{odd-extensions.imported-representatives-dimension-nearest-four-types}; the odd extension is the first construction above the shadow, by dimension, that keeps them apart, and it does so through an element, the bare fifth generator, that no derived quantity of the series uses (Proposition \claimref{odd-extensions.two-towers-one-curved-universe}).
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the twistor module to the conformal spinor module $\CS$ and named the complex unit of $\Cl^0(2,4)$ as $I_6$ (TWGA E1.2). Kept the complexified ambient, since the point is that the vector space has no signature over $\C$; the proof is a citation and is unchanged.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - odd-extensions.imported-representatives-dimension-nearest-four-types
    - odd-extensions.imported-towers-clock
    - odd-extensions.two-towers-one-curved-universe
---

## formal
The copy theorem identifies this world and its mirror by working in an algebra, $\Cl^{0}(2,4) \cong \Cl(2,3)$, that contains both real forms and is the complexification of each, its complex unit being the conformal pseudoscalar $I_6$ that spans its centre with $1$. It is therefore exactly blind to the distinction that a single extension sees: the two oriented towers have isomorphic conformal spin groups, isomorphic conformal spinor modules (twistor modules) and one complexified ambient, but odd extensions that signature reversal does not identify (Theorem \claimref{odd-extensions.twistor-algebra}(iv)), whose centres differ. The shadows themselves are non-isomorphic (Fact \claimref{odd-extensions.imported-representatives-dimension-nearest-four-types}); every object the copy theorem is built from, the even subalgebra of the rung, the conformal spin group and the conformal spinor module $\CS$ (Theorem \claimref{odd-extensions.twistor-algebra}(iii)), identifies the two towers, while the rungs themselves, $\Cl(2,4)$ and $\Cl(4,2)$, do not, being of the two towers' types by Facts \claimref{odd-extensions.imported-towers-clock} and \claimref{odd-extensions.imported-representatives-dimension-nearest-four-types}; the odd extension is the first construction above the shadow, by dimension, that keeps them apart, and it does so through an element, the bare fifth generator, that no derived quantity of the series uses (Proposition \claimref{odd-extensions.two-towers-one-curved-universe}).

## technical
The copy theorem identifies this world $(1,3)$ with its mirror $(3,1)$ by working in $\Cl^{0}(2,4) \cong \Cl(2,3)$, an algebra that contains both real forms and is the complexification of each. Every object it is built from (the rung's even subalgebra, the conformal spin group and the conformal spinor module) therefore identifies the two towers. The shadows themselves are not isomorphic, and the rungs $\Cl(2,4)$ and $\Cl(4,2)$ are not identified either, being of the two towers' types. Nor are the odd extensions: $\Cl(2,3) \not\cong \Cl(3,2)$ and $\Cl(1,4) \not\cong \Cl(4,1)$, with centres $\C$ against $\R \oplus \R$. So the odd extension is the first construction above the shadow, by dimension, that keeps the towers apart, and it does so through the bare fifth generator, which no derived quantity of the series uses.

## lay
The series proves that the mirror tower is a copy of ours by working in an algebra in which the two look identical. This result points out that the method is therefore blind to where they do differ: a five-dimensional extension of each, which reversing the signature does not match up. The difference sits in a single element that none of the series' derived quantities uses.

## one-liner
Because the copy theorem works in $\Cl^{0}(2,4)$, which contains both real forms and complexifies each, it is blind to the distinction the odd extensions draw between this world and its mirror, whose centres differ.
