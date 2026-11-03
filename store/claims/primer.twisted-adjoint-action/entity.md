---
id: primer.twisted-adjoint-action
kind: claim
version: 3
title: The twisted adjoint action
status: proved
region: primer
programme: standard
subject: standard-algebra
tags: [rotors-and-stabilisers, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T00.py
  tags:
  - num:9.2
- kind: check
  ref: check.py::check_tau_is_automorphism_and_twisted_adjoint
- kind: check
  ref: check.py::check_vector_is_reflection
- kind: check
  ref: check.py::check_kernel_is_plus_minus_one
- kind: check
  ref: check.py::check_surjectivity_samples
locators:
  paper: T00
  number: Lem 9.2
  label: tk:tau
  line: 458
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: tau_g multiplicative on all blade pairs and equal to the twisted adjoint isometry on vectors, the reflection formula, kernel R.1 for every signature n <= 4, sampled surjectivity. Version 1 -> 2. Sample inputs moved to module level; no change to what is tested. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'No edges: the surjectivity and kernel steps cite Cartan-Dieudonne and Porteous from the literature,
      and neither is an imported claim in the store.'
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [dark-matter.two-families-are-two-chiralities]
    added_about: []
    verdict: connected
    note: 'Its surjectivity step rests on Cartan-Dieudonne, which is not a store entity; the dark-matter chirality proof uses that every isometry is the twisted adjoint of a versor. The root paper uses the action only through the equivariance definition, an object, so no claim edge there.'
---

## formal
Let $g = u_1 \cdots u_k$ be a versor and define, on the whole algebra,
\begin{equation}
\tau_g(x) \;=\;
\begin{cases}
\,g\, x\, g^{-1} & g \text{ even},\\[2pt]
\,g\, \hat{x}\, g^{-1} & g \text{ odd}.
\end{cases}
\end{equation}
Then each $\tau_g$ is an algebra automorphism, and on vectors it restricts to the twisted adjoint $\Ad_g(x) = \hat{g} x g^{-1}$. For a single invertible vector $u$,
\[
\Ad_u(x) \;=\; -\,u x u^{-1} \;=\; x - 2\,\frac{x \cdot u}{Q(u)}\,u ,
\]
the reflection in the hyperplane orthogonal to $u$; consequently $g \mapsto \Ad_g$ maps $\Pin(p,q)$ onto $O(p,q)$ with kernel $\{\pm 1\}$.

## technical
For a versor $g = u_1 \cdots u_k$ set $\tau_g(x) = g x g^{-1}$ if $g$ is even and $\tau_g(x) = g \hat{x} g^{-1}$ if $g$ is odd. Each $\tau_g$ is an algebra automorphism, and on vectors it is the twisted adjoint $\Ad_g(x) = \hat{g} x g^{-1}$. For one invertible vector $u$,
$\Ad_u(x) = -u x u^{-1} = x - 2\,\frac{x \cdot u}{Q(u)}\,u$, the reflection in the hyperplane orthogonal to $u$.

With the Cartan-Dieudonné theorem, which writes every element of $\mathrm{O}(p,q)$ as a product of reflections, this makes $g \mapsto \Ad_g$ a map of $\Pin(p,q)$ onto $\mathrm{O}(p,q)$ with kernel $\{\pm 1\}$.

## lay
Every symmetry of a geometry that preserves lengths can be built from mirror reflections. In a Clifford algebra each reflection is carried out by sandwiching with a single direction, and a product of directions carries out the combined symmetry. This result sets up the sandwich carefully, with a sign twist for products of an odd number of directions, and shows that each length-preserving symmetry comes from exactly two such products, differing by sign.

## one-liner
The twisted adjoint action of a versor is an algebra automorphism acting on vectors by hyperplane reflections, giving a two-to-one map of $\Pin(p,q)$ onto $\mathrm{O}(p,q)$.
