---
id: sheaf.exceptional-algebra-black-hole
kind: claim
version: 4
title: The exceptional algebra of the black hole
status: proved
region: sheaf
subject: singularity
tags: [schwarzschild, kasner, degenerate-algebras]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
  uses:
  - sheaf.exceptional-algebra-deformation-normal-cone@5
  - sheaf.schwarzschild-degeneration-boundary-tame@6
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_rescaled_gram_and_its_limit
- kind: check
  ref: check.py::check_residue_is_minus_k_tensor_k
- kind: check
  ref: check.py::check_exceptional_algebra_is_cl13
locators:
  paper: T04
  number: Prop 8.14
  label: prop:schwexceptional
  line: 1016
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: at three masses, the rescaled Gram has cross term -sqrt r and dying entry -1 exactly with limit diag(m^2, -1, -1, -1) of signature (1,3), r G^-1 -> -k (x) k, and the limit form generates Cl(1,3). Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    removed:
    - sheaf.invariant-form-t3
    - sheaf.metrics-residue-square-root-twist
    added:
    - sheaf.exceptional-algebra-deformation-normal-cone
    note: 'the shared proof''s invariance clauses (invariant form of T3, residue theorem) serve only the
      companion residue proposition; this one needs the boundary-tame Gram and the general exceptional-algebra
      proposition, which the boundary-tameness remark says applies here and which defines the special
      fibre; the closing Kasner identification is read as interpretation, so the Kasner fact was not added.
      Levels pass: conditions already kept.'
  env: proposition
  flags:
  - no proof environment found
  repair:
    notes:
    - proof shared with the next proposition (the source proves both together, "Proof of both")
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.exceptional-algebra-deformation-normal-cone
---

## formal
In the rescaled frame $(\rho,\, k/\sqrt{r},\, \mu_1,\, \mu_2)$ the Gram extends to $E$ with limit
\[
\mathrm{diag}(m^2,\, -1,\, -1,\, -1),
\]
nondegenerate of signature $(1,3)$; the cross term $G(\rho, k/\sqrt{r}) = -\sqrt{r}$ vanishes at the wall, and the dying entry $G(k/\sqrt r, k/\sqrt r) = -1$ is \emph{exact}, not merely limiting, being the rate of the degeneration. The exceptional algebra of the Schwarzschild singularity is $\Cl(1,3)$: the Clifford algebra of its Kasner form.

## technical
Near the Schwarzschild singularity take the rescaled frame $(\rho,\, k/\sqrt r,\, \mu_1,\, \mu_2)$, in which the dying covector $k$ is divided by $\sqrt r$. The Gram then extends to the boundary $E$ with the nondegenerate limit $\mathrm{diag}(m^2, -1, -1, -1)$, of signature $(1,3)$. The cross term $G(\rho, k/\sqrt r) = -\sqrt r$ vanishes at the wall, and the dying entry $G(k/\sqrt r, k/\sqrt r) = -1$ holds exactly at every radius, not only in the limit, being the rate of the degeneration.

The exceptional algebra, the Clifford algebra of this limit form, is therefore $\Cl(1,3)$: the Clifford algebra of the singularity's Kasner form.

## lay
At the centre of a black hole the geometry loses one direction. If that direction is stretched by just the right amount as one approaches the centre, the geometry has a complete, non-degenerate limit there. This result computes that limit and finds the same kind of algebra as ordinary spacetime, with one time direction and three space directions.

## one-liner
After rescaling the dying direction by $\sqrt r$, the Schwarzschild Gram extends to the singularity as $\mathrm{diag}(m^2, -1, -1, -1)$, so the exceptional algebra there is $\Cl(1,3)$.
