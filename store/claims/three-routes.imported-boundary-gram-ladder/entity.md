---
id: three-routes.imported-boundary-gram-ladder
kind: claim
version: 4
title: 'Imported: the boundary Gram and the ladder'
status: proved
region: three-routes
subject: walls
tags: [schwarzschild, ladder-pairs, degenerate-algebras]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-three-routes, the series'' standard disclaimer'
review: typed
about:
- obj.sheaf.weighted-coframe-module
derivations:
- name: main
  uses:
  - sheaf.one-sided-completion-singularity@4
  - sheaf.schwarzschild-degeneration-boundary-tame@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_boundary_gram_and_radical
- kind: check
  ref: check.py::check_completed_form_nondegenerate_on_physical_closure
- kind: check
  ref: check.py::check_ladder_pair_exactly_over_boundary
locators:
  paper: T05-three-routes
  number: Fact 1.2
  label: fact:boundary
  line: 106
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: at two masses, the boundary Gram, radical and det -r, the completed form of signature (2,4) on the physical closure, and the ladder pair on E with no null k off E. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    note: 'Fact restating two cited T4 results; both existing edges are those sources and were kept, and
      the T5 restatements were not added. Levels pass: conditions already kept; the lay level now limits
      nondegeneracy to the physical closure, as the formal does.'
  env: fact
  context_refs:
  - sheaf.one-sided-completion-singularity
  - sheaf.schwarzschild-degeneration-boundary-tame
  outside_pilot_cites:
  - ButlerT5
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
At each point of $\Sig$ the Gram $G$ of $\shW$ is symmetric of corank exactly one, its radical the line $\R k$, with $G(k,k) = 0$ there and $\det G = -r$ off the boundary; for exact Schwarzschild, on the frame $(\rho, dt_{\mathrm{PG}}, \mu_1, \mu_2)$,
\[
G(0) \;=\; \begin{pmatrix} m^2 & -m & 0 & 0\\ -m & 1 & 0 & 0\\ 0 & 0 & -1 & 0\\ 0 & 0 & 0 & -1 \end{pmatrix}, \qquad k = \rho + m\,dt_{\mathrm{PG}}, \qquad m = \sqrt{2M}.
\]
The completed form $h$ is nondegenerate at every point of the physical closure, and the ladder pair $k^{*} = \nO/2\nu$, $kk^{*} + k^{*}k = 1$, $k^{2} = (k^{*})^{2} = 0$, exists exactly over $\Sig$. \emph{Provenance:} \cite[Thms 8.7, 8.12]{ButlerT4}, reproduced with hypotheses as \cite[Facts B.1, B.2]{ButlerT5}.

## technical
At each point of the singular boundary $\Sig$ the Gram $G$ of the weighted module $\shW$ is symmetric of corank exactly one, with radical the line $\R k$ and $G(k,k) = 0$; off the boundary $\det G = -r$. For exact Schwarzschild, on the frame $(\rho, dt_{\mathrm{PG}}, \mu_1, \mu_2)$, the boundary Gram has $(\rho, dt_{\mathrm{PG}})$ block $\begin{pmatrix} m^2 & -m \\ -m & 1 \end{pmatrix}$ and entry $-1$ on each angular direction, with $k = \rho + m\,dt_{\mathrm{PG}}$ and $m = \sqrt{2M}$.

The completed form $h$ is nondegenerate at every point of the physical closure, and the ladder pair $k^{*} = \nO/2\nu$, with $kk^{*} + k^{*}k = 1$ and $Q(k) = Q(k^{*}) = 0$, exists exactly over $\Sig$. Both facts are imported from the earlier sheaf paper.

## lay
At the Schwarzschild singularity the geometry collapses in exactly one direction, and this fact records the precise shape of that collapse. Once the completion adds two extra directions the geometry is no longer degenerate anywhere in the physical region, boundary included, and the collapsing direction gains a partner. The pair behaves like the creation and annihilation operators of a single fermion mode. The fact is carried over from earlier in the series.

## one-liner
At the singular boundary the Gram has corank one with radical $\R k$, the completed form is nondegenerate on the physical closure, and the ladder pair $(k, \nO/2\nu)$ exists exactly over $\Sig$.
