---
id: sheaf.residue-square-root-twist-black-hole
kind: claim
version: 2
title: The residue, and the square-root twist at the black hole
status: proved
region: sheaf
subject: singularity
tags: [refutation, schwarzschild, degenerate-algebras]
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
  - sheaf.invariant-form-t3@2
  - sheaf.metrics-residue-square-root-twist@5
  - sheaf.schwarzschild-degeneration-boundary-tame@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_residue_is_minus_k_tensor_k
- kind: check
  ref: check.py::check_transversality_datum_and_scaling
- kind: check
  ref: check.py::check_rescaled_frame_limit
locators:
  paper: T04
  number: Prop 8.15
  label: prop:schwresidue
  line: 1024
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on the Schwarzschild boundary Gram at three masses, r G^{-1} -> -k (x) k (rank one) with the residue formula for other defining functions, g_k = -r so delta(k (x) k) = -dr with c^2 and 1/c scaling of the dying and partner lines, the Killing-time line on E, and the rescaled-frame limit diag(m^2, -1, -1, -1). Version 1 -> 2.'
  typing:
    by: ai-typing-pass
    note: 'kept all three edges: the boundary-tame Gram gives the computation, and the invariant form
      of T3 and the residue theorem give the invariance clauses, applied one-sidedly per a remark that
      is not a store entity. Levels pass: the lay now restricts the statement to the Schwarzschild singularity.'
  env: proposition
  unresolved_refs:
  - rem:boundarytame
---

## formal
$\displaystyle \lim_{r \to 0^+} r\,G^{-1} = -\,k \otimes k$, a rank-one limit; invariantly, the transversality datum $\delta : \shL^{\otimes 2} \to N^*_rE$ (the $r$-conormal line of the Conventions), $k \otimes k \mapsto -dr|_E$, is an isomorphism. The dying line, spanned on $E$ by the Killing-time covector, is a canonical square root of the $r$-conormal bundle of the singularity, and the partner line $\langle k^* \rangle$ adjoined by the completion is a canonical square root of its dual. The tautological twist of Theorem \claimref{sheaf.metrics-residue-square-root-twist} holds at the black hole, read in the $r$-graded conormal.

## technical
At the Schwarzschild singularity, $\lim_{r \to 0^+} r\,G^{-1} = -\,k \otimes k$, a rank-one limit. Invariantly, the transversality datum $\delta : \shL^{\otimes 2} \to N^*_rE$ into the $r$-conormal line, $k \otimes k \mapsto -dr|_E$, is an isomorphism.

Hence the dying line, spanned on $E$ by the Killing-time covector, is a canonical square root of the $r$-conormal bundle of the singularity, and the partner line $\langle k^* \rangle$ adjoined by the completion is a canonical square root of its dual. The general square-root twist therefore holds at the black hole, read in the $r$-graded conormal.

## lay
Near the centre of a non-rotating (Schwarzschild) black hole the metric blows up, but in a controlled way: it grows like one over the radius, and only along a single direction. That direction is the one the geometry loses. The result shows that this lost direction, taken twice over, is canonically the same thing as the direction leading away from the singular surface, matching a general pattern found for such degenerations.

## one-liner
At the Schwarzschild singularity $r\,G^{-1} \to -\,k \otimes k$, so the dying line is a canonical square root of the $r$-conormal bundle and the completion's partner line a canonical square root of its dual.
