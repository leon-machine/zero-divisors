---
id: rule2.imported-rule-2-matrix-units-forgotten
kind: claim
version: 3
title: 'Imported: Rule 2, the matrix units, and the forgotten bit'
status: proved
region: rule2
subject: completion
tags: [transport-algorithm, idempotents, obstruction-types]
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
  - transport.ascent-renders-grade-involution-inner@3
  - transport.corner-even-subalgebra@5
  - transport.fusion-occurs-most-once@5
  - transport.matrix-units-peirce-isomorphism@3
  - transport.one-generator-minimal-minimal-completions-classified@6
  - transport.rule-2-ideal-fusion-sharp-form@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_matrix_units_simplicity_and_ad_nu
- kind: check
  ref: check.py::check_corner_map_isomorphism
- kind: check
  ref: check.py::check_ascents_isomorphic_not_isometric
- kind: check
  ref: check.py::check_null_generator_never_fuses
- kind: check
  ref: check.py::check_fusion_fires_at_most_once
locators:
  paper: T17-rule2
  number: Fact 1.2
  label: fact:rule2
  line: 105
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: transport.corner-even-subalgebra repinned 4 -> 5 after reviewing the change that its setting (A = Cl(p,q) with p - q = 1 mod 4, the central idempotents, the even subalgebra and the one-generator ascent) is now stated in the formal; the isomorphism is unchanged; the use here holds as cited.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the stated matrix units, simplicity and Ad_nu for n <= 7, the corner isomorphism, the two ascents isomorphic but not isometric, the null generator, and fusion at most once. Version 2 -> 3.'
  env: fact
  context_refs:
  - transport.ascent-renders-grade-involution-inner
  - transport.corner-even-subalgebra
  - transport.fusion-occurs-most-once
  - transport.matrix-units-peirce-isomorphism
  - transport.one-generator-minimal-minimal-completions-classified
  - transport.rule-2-ideal-fusion-sharp-form
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: The six uses are exactly the root-paper results the Fact cites; the forgotten-sign remark it
      also cites has no separate store entry.
---

## formal
Let $p - q \equiv 1 \pmod 4$, $A = \Cl(p,q)$, and let $\nu$ be one adjoined generator orthogonal to the generating space with $\nu^2 = \gamma \in \{\pm 1\}$, so that $B_\gamma = \Cl(p{+}1,q)$ or $\Cl(p,q{+}1)$. Then: conjugation by $\nu$ restricts on $A$ to the grade involution, $\nu a \nu^{-1} = \hat{a}$; the map $a \mapsto \varepsilon_+ a$ is an isomorphism $\Cl^0(p,q) \to \varepsilon_+ A$; the elements $E_{11} = \varepsilon_+$, $E_{22} = \varepsilon_-$, $E_{12} = \varepsilon_+\nu$, $E_{21} = \gamma\varepsilon_-\nu$ form a full $2 \times 2$ system of matrix units in $B_\gamma$; hence $B_\gamma \cong \Mat_2(\Cl^0(p,q))$ is simple, the images of $\varepsilon_\pm$ are a conjugate pair of non-central idempotents exchanged by $\Ad_\nu$, and the two ascents are isomorphic as algebras though non-isometric as quadratic data: the sign $\gamma$ is a geometric datum with no algebraic shadow. One nondegenerate generator is minimal, the null generator never fuses, and fusion fires at most once in any transport history. \emph{Provenance:} \cite[Prop.~5.2, Lemma 5.3, Lemma 5.4, Thm.~5.5, Thm.~5.7, Remark 5.8, Prop.~7.4]{ButlerT1}.

## technical
Let $p-q \equiv 1 \pmod 4$ and $A = \Cl(p,q)$, with central idempotents $\varepsilon_\pm$, and adjoin one generator $\nu$ orthogonal to the generating space with $Q(\nu) = \gamma \in \{\pm 1\}$, giving $B_\gamma = \Cl(p+1,q)$ or $\Cl(p,q+1)$. Conjugation by $\nu$ restricts on $A$ to the grade involution, $a \mapsto \varepsilon_+ a$ is an isomorphism $\Cl^0(p,q) \to \varepsilon_+ A$, and $\varepsilon_+$, $\varepsilon_-$, $\varepsilon_+\nu$, $\gamma\varepsilon_-\nu$ form a full system of $2\times 2$ matrix units. Hence $B_\gamma \cong \Mat_2(\Cl^0(p,q))$ is simple, and $\varepsilon_\pm$ become conjugate non-central idempotents exchanged by conjugation by $\nu$.

The two ascents are isomorphic as algebras but not isometric as quadratic data, so $\gamma$ leaves no algebraic trace. One nondegenerate generator is minimal, a null generator never fuses, and fusion happens at most once in any transport history.

## lay
Some geometric algebras split into two separate halves that no internal symmetry can swap. Adding one new direction, of either sign, merges the halves into a single algebra in which swapping them becomes an internal operation. The merged algebra is the same whichever sign is chosen, so the algebra forgets that choice, and this merging happens at most once along any chain of repairs.

## one-liner
For $p-q \equiv 1 \pmod 4$, adjoining one generator to $\Cl(p,q)$ fuses its two ideals into $\Mat_2(\Cl^0(p,q))$, the same algebra for either sign of the generator, with one generator minimal, a null generator never fusing, and fusion at most once per transport history.
