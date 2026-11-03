---
id: singularity.sheaf-assembly-sheaf
kind: claim
version: 3
title: The sheaf assembly is a sheaf
status: proved
region: singularity
subject: descent
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.singularity.two-fibres-two-assemblies
derivations:
- name: main
  uses:
  - singularity.imported-one-sided-completion-singularity@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_parity_section_constant_along_ladder_family
- kind: check
  ref: check.py::check_even_projection_constant_rank_subalgebra
- kind: check
  ref: check.py::check_sign_of_ladder_invisible
locators:
  paper: T05
  number: Prop C.2
  label: prop:mlsheaf
  line: 2656
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: fibrewise content on Cl(1,1): the ladder family keeps sigma constant, (id + Ad sigma)/2 is an idempotent of constant rank 2 onto the subalgebra span{1, sigma}, and the ladder''s sign is invisible. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    added:
    - obj.singularity.two-fibres-two-assemblies
    note: 'Kept the one-sided completion fact as the premise that supplies the mode bundle under w1 =
      0; added the two-assemblies definition as the object the statement is about, with a version bump
      for the new about edge. Levels pass: conditions already kept.'
  env: proposition
---

## formal
$\mathfrak{M}$ is a sheaf of algebras on $E$, with stalk at $x$ the germs valued in $\Aa_x^{+}$. It exists whenever the completed mode bundle $\Aa$ does, that is under the standing hypothesis $w_1(\shL) = 0$, and needs nothing further: the fibrewise projection $\tfrac12(\id + \alpha_x)$ is a smooth idempotent bundle map, so $\Aa^{+}$ is a locally trivial subbundle, and it is defined by $\sigma$, which does not see the sign of the ladder. For $w_1(\shL) \neq 0$ the mode bundle itself, and with it $\mathfrak{M}$, exists only in the $\shL$-twisted variant.

## technical
Given the completed mode bundle $\Aa$ over $E$, with parity section $\sigma$ and fibre automorphism $\alpha_x = \operatorname{Ad}(\sigma(x))$, the sheaf assembly $\mathfrak{M}(U) = \Gamma(U, \Aa^{+})$ assigns to each open $U \subseteq E$ the sections valued in the even fibres $\Aa_x^{+} = \operatorname{span}\{1, \sigma(x)\}$. Because $\tfrac12(\id + \alpha_x)$ is a smooth idempotent bundle map, $\Aa^{+}$ is a locally trivial subbundle, and $\mathfrak{M}$ is a sheaf of algebras with stalk at $x$ the germs valued in $\Aa_x^{+}$.

It exists whenever $\Aa$ does, that is under the standing hypothesis $w_1(\shL) = 0$, and needs nothing further, since $\sigma$ is quadratic in the ladder and does not see its sign. For $w_1(\shL) \neq 0$ the mode bundle, and with it $\mathfrak{M}$, exists only in the $\shL$-twisted variant.

## lay
One way to assemble the classical level over a region is to keep, at each point, only the part that survives that point's descent, and glue those parts together. This result checks that the gluing really does give a sheaf, the standard mathematical structure for locally defined data. It needs nothing beyond the existence of the bundle of completed modes, which holds under the paper's standing topological hypothesis.

## one-liner
The sheaf assembly of the even fibres is a sheaf of algebras on $E$, and it exists whenever the completed mode bundle does, that is under $w_1(\shL) = 0$.
