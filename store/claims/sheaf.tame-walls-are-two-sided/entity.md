---
id: sheaf.tame-walls-are-two-sided
kind: claim
version: 3
title: Tame walls are two-sided
status: proved
region: sheaf
subject: walls
tags: [tameness]
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
  uses:
  - sheaf.imported-real-line-bundles@1
  - sheaf.metrics-residue-square-root-twist@5
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T04
  number: Cor 7.1
  label: cor:twosided
  line: 810
extraction:
  env: corollary
  context_refs:
  - sheaf.metrics-residue-square-root-twist
  typing:
    by: ai-typing-pass
    added:
    - sheaf.metrics-residue-square-root-twist
    - sheaf.tameness
    note: 'Added the residue theorem, which supplies the isomorphism the corollary starts from, and the
      tameness postulate the statement assumes. Levels pass: the tameness condition was kept only as the
      adjective "tame"; all three plain levels now name it as the hypothesis.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.metrics-residue-square-root-twist
    - sheaf.tameness
    note: 'the assumed tameness postulate, not on the cite list, was also uncited; cited where the residue isomorphism is applied.'
---

## formal
For any tame corank-one degeneration, the conormal bundle of $\Sig$ satisfies $N^*\Sig \cong \shL^{\otimes 2}$ (Theorem \claimref{sheaf.metrics-residue-square-root-twist}), hence has vanishing first Stiefel-Whitney class: $w_1(N^*\Sig) = 2\,w_1(\shL) = 0$. So $N\Sig$ is trivial, $\Sig$ is two-sided in $M$, and a global side choice (a co-orientation, hence the meaning of ``the physical side'') always exists. Tameness itself forbids one-sided walls: a hypersurface with M\"obius normal bundle admits no corank-one degeneration satisfying (T1)-(T3) along it.

## technical
Under the tameness hypothesis (T1) to (T3), for any tame corank-one degeneration the residue theorem gives $N^*\Sig \cong \shL^{\otimes 2}$, so $w_1(N^*\Sig) = 2w_1(\shL) = 0$. By the imported facts on real line bundles, $N\Sig$ is therefore trivial and $\Sig$ is two-sided in $M$. A global choice of side, and with it a meaning for the physical side, always exists, and no hypersurface with M\"obius normal bundle carries a corank-one degeneration satisfying the tameness conditions.

## lay
Some surfaces, like a M\"obius band, have only one side. This result shows that, if a geometry degenerates along a wall in the tame way, as the tameness hypothesis requires, the wall can never be one-sided. So it always makes sense to speak of the physical side of the wall and the other side.

## one-liner
Under tameness, because $N^*\Sig \cong \shL^{\otimes 2}$, every tame wall has trivial normal bundle and is two-sided, so one-sided walls admit no tame degeneration.
