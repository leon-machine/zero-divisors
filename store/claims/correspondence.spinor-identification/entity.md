---
id: correspondence.spinor-identification
kind: claim
version: 7
title: "The spinor identification"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors, null-directions, conformal-model]
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
review: typed
derivations:
- name: main
  uses:
  - correspondence.chevalley-pairing@4
  - correspondence.fock-model-complexified-ascended-algebra@8
  - correspondence.imported-forced-completion-fibre-quadric@6
  - std-algebra.vector-squares@1
  - std-algebra.inverse-of-vector@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:thm:spinorid
- kind: check
  ref: check.py::check_canonical_isomorphism_and_form
- kind: check
  ref: check.py::check_null_iff_simple_plane_is_kernel
- kind: check
  ref: check.py::check_rays_double_cover_lines
locators:
  paper: T09
  number: Thm 3.4
  label: thm:spinorid
  line: 395
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares, std-algebra.inverse-of-vector where the proof uses them. Version 6 -> 7.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the spinor identification psi built from the Chevalley pairing: injective, equivariant, eps(psi(v) ^ psi(v'')) = <v, v''>, null iff simple with plane ker c(v), and the ray double cover. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: theorem
  context_refs:
  - correspondence.imported-forced-completion-fibre-quadric
  unresolved_refs:
  - ex:psi
  typing:
    by: ai-typing-pass
    removed:
    - correspondence.reality-conjugation-twistor-form-factor
    added:
    - correspondence.imported-forced-completion-fibre-quadric
    note: 'Removed the reality edge (E301): clause (3) only points forward to the reality proposition
      for which lines arise from real points, and that proposition depends on this theorem; added the
      imported fibre-quadric fact, which clause (3) takes as its object. The Klein correspondence is classical
      but no imported claim for it is in the store, so no standard route. Levels pass: conditions already
      kept.'
  source_title: "The spinor identification"
  source_formal: |-
    With $\T = \Lambda^{\mathrm{even}} W$ as in Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}:
    \begin{enumerate}
    \item there is a canonical isomorphism $V_\C \cong \Lambda^2 \T$ of $\mathrm{Spin}$-modules, under which the quadratic form corresponds to $P \mapsto \varepsilon(P \wedge P)$ for a fixed volume functional $\varepsilon$ on $\Lambda^4\T$;
    \item a vector is null exactly when its bivector is simple (decomposable), that is, represents a 2-plane of $\T$, that is, a line of the projective twistor space $\PT := \mathbb{P}(\T)$;
    \item consequently the completion's fibre quadric (Fact \claimref{correspondence.imported-forced-completion-fibre-quadric}), the space of null rays of $V$, double covers the real slice of the Klein quadric (a ray and its opposite give one point), whose points are the null lines of $V$ and are lines of $\PT$.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space and projective twistor space to the conformal spinor space and its projective space (\\CS, \\PCS) in the statement and proof; the Klein quadric is kept (conformal-model geometry). The complexified vector space $V_\\C$ of the Fock model is kept as it stands."
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - correspondence.imported-forced-completion-fibre-quadric
---

## formal
With $\CS = \Lambda^{\mathrm{even}} W$ as in Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}:
\begin{enumerate}
\item there is a canonical isomorphism $V_\C \cong \Lambda^2 \CS$ of $\mathrm{Spin}$-modules, under which the quadratic form corresponds to $P \mapsto \varepsilon(P \wedge P)$ for a fixed volume functional $\varepsilon$ on $\Lambda^4\CS$;
\item a vector is null exactly when its bivector is simple (decomposable), that is, represents a 2-plane of $\CS$, that is, a line of the projective spinor space $\PCS := \mathbb{P}(\CS)$ (projective twistor space);
\item consequently the completion's fibre quadric (Fact \claimref{correspondence.imported-forced-completion-fibre-quadric}), the space of null rays of $V$, double covers the real slice of the Klein quadric (a ray and its opposite give one point), whose points are the null lines of $V$ and are lines of $\PCS$.
\end{enumerate}

## technical
With $\CS = \Lambda^{\mathrm{even}}W$ from the Fock model, there is a canonical $\Spin$-module isomorphism $\Psi: V_\C \cong \Lambda^2\CS$ under which the quadratic form becomes $P \mapsto \varepsilon(P\wedge P)$ for a fixed volume functional $\varepsilon$ on $\Lambda^4\CS$, so $Q(v) = \varepsilon(\Psi(v)\wedge\Psi(v))$. Hence $v$ is null exactly when $\Psi(v)$ is simple, that is, a $2$-plane of $\CS$ and so a line of $\PCS$.

Consequently the completion's fibre quadric, the space of null rays of $V$, double covers the real slice of the Klein quadric, a ray and its opposite giving one point; those points are the null lines of $V$, and they are lines of $\PCS$.

## lay
This result matches the six complex directions of the completed spacetime algebra with the six independent plane elements that can be formed inside the four-dimensional conformal spinor space. Under the match, the lightlike directions are exactly those plane elements that are single planes rather than sums of planes, and in projective terms these are lines of that spinor space. So the lightlike directions of the completion, taken up to sign, are lines in the projective spinor space: the Klein correspondence, obtained from the completion.

## one-liner
There is a canonical $\Spin$-equivariant isomorphism from $V_\C$ to the bivectors of the conformal spinor space carrying the quadratic form to the wedge square, so null vectors are exactly the simple bivectors, that is, the lines of the projective spinor space.
