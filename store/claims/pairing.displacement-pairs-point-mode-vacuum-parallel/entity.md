---
id: pairing.displacement-pairs-point-mode-vacuum-parallel
kind: claim
version: 5
title: "Displacement pairs the point mode; the vacuum is parallel along its ray only"
status: proved
region: pairing
subject: conformal-spacetime
tags: [pairing-and-bogoliubov, conformal-model, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
review: typed
about:
- obj.pairing.pairing-class-transport
derivations:
- name: main
  uses:
  - pairing.imported-flat-conformal-model-twistor-incidence@4
  - std-algebra.contraction-expansion@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_formula_and_translation_identities
- kind: check
  ref: check.py::check_pairing_classes_and_parallel_direction
- kind: check
  ref: check.py::check_vacuum_stabiliser_has_dimension_twelve
locators:
  paper: T05-pairing
  number: Prop 6.1
  label: prop:flat
  line: 388
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.contraction-expansion where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: W(x) isotropic, the translation identities, the pairing classes (<dx,l>, <dx,m>, 0) with the real kernel R l, incidence along l, and the 12-dimensional vacuum stabiliser. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'The one use is a real premise and kept; the note says this proposition is twistor incidence
      and transport-absent, but no imported claim in the store states classical twistor incidence, so
      no standard-route derivation was added. Levels pass: the lay level now says the result is on the
      flat model and that the parallelism statement is for real displacements.'
  source_title: "Displacement pairs the point mode; the vacuum is parallel along its ray only"
  source_formal: |-
    $W(x)$ is totally isotropic of dimension three. The motion of the vacuum field under a displacement $dx = dx^{a}e_{a}$, the flat connection being the ambient derivative, is generated exactly by the translation bivector $\Omega(dx) = dx^{a}\,e_{a}\ninf$: $\tfrac12[e_{a}\ninf, X(x)] = \partial X/\partial x^{a} = e_{a} - x_{a}\ninf$, $\tfrac12[e_{a}\ninf, \ninf] = 0$, and the finite displacement $X(x + dx) - X(x)$ differs from $dx^{a}\,\partial_{a}X$ by $-\tfrac12 Q(dx)\ninf$ alone. The pairing classes of the transport are
    \[
    \bigl(\ip{dx}{\ell},\ \ip{dx}{m},\ 0\bigr):
    \]
    the displacement pairs the point mode with the boost mode by its $n$-component and with the angular mode by its $\mb$-component, and never pairs the boost mode with the angular mode. For a real displacement all three vanish if and only if $dx$ is a real multiple of $\ell$ (for a complex one the equivalence fails, $dx = m$ having all three classes zero): the vacuum is parallel along the point's own null ray and along no other real direction, which is twistor incidence, $X(x + s\ell) = X(x) + s\,\ell(x) \in W(x)$ for every $s$. The stabiliser of a $\nu = 3$ vacuum in $\so(6,\C)$ has dimension $12 = \nu^{2} + \nu(\nu-1)/2$, the three classes being independent functionals.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor incidence to the incidence relation of the conformal spinor space, named once; the formal statement is otherwise unchanged, and the proof has no twistor wording."
---

## formal
$W(x)$ is totally isotropic of dimension three. The motion of the vacuum field under a displacement $dx = dx^{a}e_{a}$, the flat connection being the ambient derivative, is generated exactly by the translation bivector $\Omega(dx) = dx^{a}\,e_{a}\ninf$: $\tfrac12[e_{a}\ninf, X(x)] = \partial X/\partial x^{a} = e_{a} - x_{a}\ninf$, $\tfrac12[e_{a}\ninf, \ninf] = 0$, and the finite displacement $X(x + dx) - X(x)$ differs from $dx^{a}\,\partial_{a}X$ by $-\tfrac12 Q(dx)\ninf$ alone. The pairing classes of the transport are
\[
\bigl(\ip{dx}{\ell},\ \ip{dx}{m},\ 0\bigr):
\]
the displacement pairs the point mode with the boost mode by its $n$-component and with the angular mode by its $\mb$-component, and never pairs the boost mode with the angular mode. For a real displacement all three vanish if and only if $dx$ is a real multiple of $\ell$ (for a complex one the equivalence fails, $dx = m$ having all three classes zero): the vacuum is parallel along the point's own null ray and along no other real direction, which is the incidence relation of the conformal spinor space (twistor incidence), $X(x + s\ell) = X(x) + s\,\ell(x) \in W(x)$ for every $s$. The stabiliser of a $\nu = 3$ vacuum in $\so(6,\C)$ has dimension $12 = \nu^{2} + \nu(\nu-1)/2$, the three classes being independent functionals.

## technical
On the flat model $W(x)$ is totally isotropic of dimension three, and the motion of the vacuum under a displacement $dx$ is generated by the translation bivector $\Omega(dx) = dx^a\, e_a n_\infty$, with $\tfrac12[e_a n_\infty, X(x)] = \partial_a X = e_a - x_a n_\infty$. The pairing classes of the transport are $(\ip{dx}{\ell}, \ip{dx}{m}, 0)$: the displacement pairs the point mode with the boost mode and with the angular mode, and never pairs the boost mode with the angular mode.

For a real $dx$ all three classes vanish exactly when $dx$ is a real multiple of $\ell$ (this fails for complex $dx$, for example $dx = m$), so the vacuum is parallel along the point's own null ray and along no other real direction; this is the incidence relation of the conformal spinor space, $X(x + s\ell) \in W(x)$. The stabiliser of a $\nu = 3$ vacuum in $\so(6, \C)$ has dimension $12$.

## lay
In flat spacetime, each point carries a vacuum state built from three fermionic modes. Moving the point generally disturbs that vacuum, by amounts set by how far the move goes along two particular light-like directions. Among real moves, the vacuum stays unchanged only when the point moves along its own light ray, which is Penrose's incidence rule seen in this language.

## one-liner
A displacement $dx$ has pairing classes $(\ip{dx}{\ell}, \ip{dx}{m}, 0)$, so for real displacements the vacuum is parallel only along the point's own null ray, which is the incidence relation of the conformal spinor space.
