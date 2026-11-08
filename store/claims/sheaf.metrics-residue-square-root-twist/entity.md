---
id: sheaf.metrics-residue-square-root-twist
kind: claim
version: 5
title: The metric's residue, and the square-root twist
status: proved
region: sheaf
subject: walls
tags: [degenerate-algebras]
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
  - sheaf.localised-transport@6
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:6.2
- kind: check
  ref: check.py::check_residue_is_inverse_transversality
- kind: check
  ref: check.py::check_residue_weights
- kind: check
  ref: check.py::check_partner_line_is_dual_to_dying_line
locators:
  paper: T04
  number: Thm 6.2
  label: thm:residue
  line: 771
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: tau G^-1 -> (1/T) k(x)k exactly in collar models (two frames), extension and scale weights of the residue, and the inverse scaling of the partner line. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  env: theorem
  unresolved_refs:
  - rem:blowup
  - rem:coords
  typing:
    by: ai-typing-pass
    removed:
    - sheaf.exceptional-algebra-deformation-normal-cone
    added:
    - sheaf.tameness
    note: 'The exceptional-rescaling proposition is invoked only in the closing interpretation of the
      rescaling, which the statement defers to a remark, so it was removed; the statement is made at a
      tame wall, so the tameness postulate was added to assumes. Levels pass: all three levels now name
      tameness as the assumed postulate; lay had dropped it.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.tameness
---

## formal
At a tame wall the physical metric (the inverse cometric) has a canonical simple pole: for any defining function $\tau$ of $\Sig$,
\[
O \;:=\; \lim_{\tau \to 0}\, \tau\, G^{-1} \;=\; \frac{k \otimes k}{\delta(k \otimes k)/d\tau} ,
\]
a nowhere-vanishing section of $\shL \otimes \shL$ depending on $\tau$ through the weight of a section of $\shL \otimes \shL \otimes N\Sig$; invariantly, the residue is $\delta^{-1}$, the inverse of the transversality datum of Lemma \claimref{sheaf.invariant-form-t3}, regarded as a section of $\shL \otimes \shL \otimes N\Sig = \operatorname{Hom}(N^*\Sig, \shL^{\otimes 2})$. It is a nondegenerate pairing between $\shL^* \otimes \shL^*$ and $N^*\Sig$, hence induces a canonical isomorphism
\[
N^*\Sig \;\cong\; \shL^{\otimes 2} :
\]
the conormal bundle is the square of the dying direction itself. Dually, $N\Sig \cong (\shL^*)^{\otimes 2}$: the Witt partner line adjoined by the completion, which the pairing normalisation $kk^* + k^*k = 1$ identifies with $\shL^*$, is a canonical square root of the \emph{normal} bundle, and the dying line $\shL$ is a canonical square root of the conormal bundle. (The reading of the blow-up rescaling $k \mapsto k/\sqrt{t}$ as the normalisation of a conormal square root is Remark \ref{rem:blowup}.)

## technical
At a wall satisfying the tameness postulate, the physical metric, the inverse cometric, has a canonical simple pole: for any defining function $\tau$ of $\Sig$, $\lim_{\tau \to 0} \tau\, G^{-1} = (k \otimes k)/(\delta(k \otimes k)/d\tau)$, a nowhere-vanishing section of $\shL \otimes \shL$ that depends on $\tau$ only through the weight of a normal vector. Invariantly the residue is $\delta^{-1}$, the inverse of the transversality datum, viewed as a section of $\operatorname{Hom}(N^*\Sig, \shL^{\otimes 2})$.

Being nowhere zero, it gives a canonical isomorphism $N^*\Sig \cong \shL^{\otimes 2}$: the conormal line is the square of the dying line. Dually $N\Sig \cong (\shL^*)^{\otimes 2}$, and the Witt partner line adjoined by the completion, identified with $\shL^*$ by the normalisation $kk^* + k^*k = 1$, is a canonical square root of the normal bundle.

## lay
Near a degenerate wall of the well-behaved kind the series assumes (a tame wall, where the degeneration is transverse), the ordinary metric blows up like one over the distance to the wall. The coefficient of this blow-up turns out to be the inverse of the canonical rate at which the geometry degenerates. It shows that the direction across the wall is, in a precise sense, the square of the direction that dies, so the extra direction added in the repair is a square root of the direction across the wall.

## one-liner
Assuming the wall is tame, the metric has a canonical simple pole whose residue is the inverse of the transversality datum, giving $N^*\Sig \cong \shL^{\otimes 2}$ and making the completion's partner line a square root of the normal bundle.
