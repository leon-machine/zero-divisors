---
id: sheaf.conservation-degeneracy-absolute-form
kind: claim
version: 4
title: Conservation of degeneracy, absolute form
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
derivations:
- name: main
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:5.1
- kind: check
  ref: check.py::check_exterior_totals_differ
- kind: check
  ref: check.py::check_every_joining_path_degenerates
- kind: check
  ref: check.py::check_switching_sig_k_avoids_degeneracy
locators:
  paper: T04
  number: Thm 5.1
  label: thm:absolute
  line: 684
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the exterior totals differ for 150 cases, every joining polynomial path degenerates, and a K that switches signature avoids degeneracy. Version 3 -> 4.'
  env: theorem
  unresolved_refs:
  - rem:coords
  typing:
    by: ai-typing-pass
    added:
    - sheaf.tameness
    note: 'The statement assumes a tame corank-one degeneration, so the tameness postulate goes in assumes;
      the proof is a self-contained signature count and needs no other premise. Levels pass: the lay level
      now states the tameness premise, connectedness, both sides nonempty and the same complement signature
      on both sides, which it had dropped; the technical and one-liner now mark tameness as an assumption.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.tameness
---

## formal
Let $M$ be connected, let $(M,G)$ be a tame corank-one degeneration whose two open sides $\Mp \setminus \Sig$ and $M \setminus \Mp$ are both nonempty, let $E \to M$ be \emph{any} vector bundle containing $T^*M$ as a subbundle, carrying \emph{any} smooth symmetric form $h$ which is \emph{standard} outside some neighbourhood $U$ of $\Sig$ with $M \setminus U$ meeting both sides: there, $h = G \perp K$ for a nondegenerate form $K$ on a complement, with $\operatorname{sig}(K)$ the same on both exterior regions. Then $h$ is not nondegenerate everywhere: every completion of a signature-change cometric that is standard, in this sense, outside a neighbourhood of the wall degenerates somewhere. Degeneracy can be displaced, never destroyed.

## technical
Assume $M$ is connected and $(M,G)$ is a tame corank-one degeneration (the tameness premise) whose two open sides are both nonempty. Take any vector bundle $E$ containing $T^*M$, with any smooth symmetric form $h$ that is standard outside a neighbourhood $U$ of $\Sig$ whose complement meets both sides: there $h = G \perp K$ with $K$ nondegenerate and $\operatorname{sig}(K)$ the same on both exterior regions. Then $h$ is degenerate somewhere.

The argument is a signature count. A continuous nondegenerate symmetric form on a connected base has constant signature. On the physical exterior $h$ has signature $(p,q) + \operatorname{sig}(K)$, and on the far exterior $(p-1,q+1) + \operatorname{sig}(K)$; these differ, so nondegeneracy must fail somewhere in $U$. The requirement that $\operatorname{sig}(K)$ agree on the two exterior regions is essential: a $K$ allowed to change signature across the wall could make up the difference.

## lay
When a geometry changes signature across a wall, one can try to repair the wall by placing it inside a larger structure. Assuming the wall is tame (the mildest kind of degeneration), the space is connected and there is geometry on both sides, this result shows that any such repair which looks standard away from the wall, with the same kind of extra piece on both sides, must itself break down somewhere. The breakdown can be moved, but not removed.

## one-liner
Assuming a tame signature-change wall on a connected manifold whose two sides are nonempty, every completion that is standard, with one exterior model, outside a neighbourhood of the wall degenerates somewhere.
