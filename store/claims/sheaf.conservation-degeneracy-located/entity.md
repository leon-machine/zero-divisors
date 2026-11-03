---
id: sheaf.conservation-degeneracy-located
kind: claim
version: 3
title: Conservation of degeneracy, located
status: proved
region: sheaf
subject: walls
tags: [degenerate-algebras, no-go]
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
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.determinant-identity-blow-up-expansion@3
  - sheaf.wall-gram@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:5.2
- kind: check
  ref: check.py::check_degeneracy_locus_is_the_zero_of_F
- kind: check
  ref: check.py::check_signatures_mu_nu_positive
- kind: check
  ref: check.py::check_signatures_mu_nu_negative_and_schwarzschild
- kind: check
  ref: check.py::check_no_two_sided_constant_signature
locators:
  paper: T04
  number: Prop 5.2
  label: prop:conservation
  line: 692
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: det h = det G (-F) with the single simple zero tau'' = -2 mu nu beta^2, and the signatures on both sides for both coupling signs. Version 2 -> 3.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: STRUCTURE L7
    open_problem: op.small-findings
    note: 'Physical side here means the side on which the dying eigenvalue is positive (the convention of sheaf.one-sided-completion); the clause now says so and notes that at the Schwarzschild singularity that side is r < 0, outside the manifold, so that T4 Thm 8.12 (no shadow wall in the manifold, mu nu < 0) is consistent with it.'
  source_formal: 'With the sign $\mu\nu > 0$ required for Theorem \claimref{sheaf.one-sided-completion}, the ambient form $h$ of Definition \claimref{obj.sheaf.collar-data-coupling} degenerates exactly on the zero set of $F = 1 + 2\mu\nu\beta^2 s$ within $M \setminus \Sig$, and this zero set is nonempty on the far side of every transversal: a displaced degeneration locus $\Sig''$ (the \emph{shadow wall}) separating $\Sig$ from the far exterior. Between $\Sig$ and the shadow wall the ambient signature remains $(p{+}1, q{+}1)$; across any simple zero of $F$ it passes to $(p, q{+}2)$. Choosing $\mu\nu < 0$ instead exchanges the roles of the two sides: $h|_\Sig$ has signature $(p, q{+}2)$, which is the Rule-1 ascent of the far side''s algebra $\Cl(p{-}1, q{+}1)$, and the degeneration is displaced into the physical side. No choice of coupling sign yields a two-sided completion of constant signature, as Theorem \claimref{sheaf.conservation-degeneracy-absolute-form} independently guarantees.'
  env: proposition
  context_refs:
  - sheaf.conservation-degeneracy-absolute-form
  - sheaf.one-sided-completion
  typing:
    by: ai-typing-pass
    note: 'Kept both edges; the absolute form is cited only as an independent confirmation and the one-sided
      completion only to fix the sign convention, so neither context reference was added. Levels pass:
      conditions already kept.'
---

## formal
With the sign $\mu\nu > 0$ required for Theorem \claimref{sheaf.one-sided-completion}, the ambient form $h$ of Definition \claimref{obj.sheaf.collar-data-coupling} degenerates exactly on the zero set of $F = 1 + 2\mu\nu\beta^2 s$ within $M \setminus \Sig$, and this zero set is nonempty on the far side of every transversal: a displaced degeneration locus $\Sig'$ (the \emph{shadow wall}) separating $\Sig$ from the far exterior. Between $\Sig$ and the shadow wall the ambient signature remains $(p{+}1, q{+}1)$; across any simple zero of $F$ it passes to $(p, q{+}2)$. Choosing $\mu\nu < 0$ instead exchanges the roles of the two sides: $h|_\Sig$ has signature $(p, q{+}2)$, which is the Rule-1 ascent of the far side's algebra $\Cl(p{-}1, q{+}1)$, and the degeneration is displaced into the physical side, meaning the side on which the dying eigenvalue is positive. Which region that is depends on the wall: at the Schwarzschild singularity, where the dying eigenvalue is $-r$, it is the excised region $r < 0$, so the displaced shadow wall lies outside the manifold (Theorem \claimref{sheaf.one-sided-completion-singularity}). No choice of coupling sign yields a two-sided completion of constant signature, as Theorem \claimref{sheaf.conservation-degeneracy-absolute-form} independently guarantees.

## technical
For the ambient form $h$ built from collar data with coupling sign $\mu\nu > 0$, off the wall $\det h = \det G \cdot (-F)$ with $F = 1 + 2\mu\nu\beta^2 s$, so $h$ degenerates exactly on the zero set of $F$ in $M \setminus \Sig$. On every far-side transversal $F \to -\infty$ near the wall and $F = 1$ outside the collar, so $F$ vanishes in between: a displaced degeneration locus $\Sig'$, the shadow wall, separates $\Sig$ from the far exterior.

Between $\Sig$ and $\Sig'$ the signature stays $(p+1,q+1)$; across a simple zero of $F$ a Schur-complement computation shows that a positive direction degenerates, so the signature passes to $(p,q+2)$. With $\mu\nu < 0$ the sides exchange roles: the wall carries signature $(p,q+2)$, the ascent of the far side's algebra $\Cl(p-1,q+1)$, and the degeneration is displaced into the physical side, the side where the dying eigenvalue is positive; at the Schwarzschild singularity that side is $r < 0$, outside the manifold. No choice of coupling sign gives a two-sided completion of constant signature.

## lay
The one-sided repair of a degenerating geometry works on one side of the wall, but the degeneracy reappears as a new shadow wall further away. This result locates that shadow wall exactly, as the zero set of an explicit function, and says how the signature changes across it. Flipping the sign of the coupling moves the shadow wall to the other side but never removes it.

## one-liner
With $\mu\nu > 0$ the ambient form degenerates exactly where $F = 1 + 2\mu\nu\beta^2 s$ vanishes, a nonempty far-side shadow wall across which the signature passes from $(p+1,q+1)$ to $(p,q+2)$, and reversing the sign only moves the shadow wall to the side where the dying eigenvalue is positive (at Schwarzschild, $r < 0$, outside the manifold).
