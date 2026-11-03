---
id: synthesis.wall-class-one-rung-obstruction
kind: claim
version: 2
title: The torsion part of a tame wall obstructs exactly the one-rung completions
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, tameness, hyperbolic-plane, no-go]
proposed_by:
  kind: ai
  session: colony-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.conservation-degeneracy-absolute-form@4
  - sheaf.degeneration-sheaf@6
  - sheaf.metrics-residue-square-root-twist@5
  - sheaf.imported-real-line-bundles@1
  - sheaf.wall-gram@3
  - sheaf.determinant-identity-blow-up-expansion@3
  - sheaf.one-sided-completion@4
  - sheaf.tame-wall-induction@5
  - sheaf.infinite-wall-sequence@4
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_rung_relaxed_construction
- kind: check
  ref: check.py::check_far_side_negative_bundle_contains_dying_line
- kind: check
  ref: check.py::check_doubling_is_never_obstructed
- kind: check
  ref: check.py::check_isotropic_line_in_rank_three
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - sheaf.wall-class
  - sheaf.conservation-degeneracy-absolute-form
extraction:
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'W503: the one-liner now states the tameness hypotheses and the two-nonempty-sides condition.'
  open_problem: op.wall-class-invariant
  note: >-
    Tests the candidate W = [L] - 1 in KO(Sigma), whose torsion part is w_1(L). Result: clause (a) of the wall-class conjecture cannot see torsion in either reading
    of "standard" (strict: always obstructed by the signature count; fully relaxed: never obstructed,
    by the doubling), and w_1(L) is exactly the obstruction at the one-rung level, one-sided or
    two-sided. The topological steps are elementary bundle algebra (determinant lines, a compactness
    argument for continuous families of subbundles), written out in the proof rather than imported.
    Transport-absent: the statement is about symmetric forms on bundles, with no Clifford input beyond
    the store's wall theory. Clause (5) sharpens the store's remark that the twisted variant is expected
    to be routine: it is obstructed unless the dying line extends over the physical side.
---

## formal
Let $(M, G)$ be a tame corank-one degeneration (Hypotheses \claimref{sheaf.tameness}) with $M$ connected and without boundary, $\Sig$ compact and separating $M$ into a physical side $\Mp$ and a far side, both nonempty, with signatures $(p,q)$ and $(p{-}1,q{+}1)$; let $\shL \subset T^*M|_\Sig$ be the radical line bundle and fix a collar $C \cong \Sig \times [-1,1]$, $\Sig = \Sig \times \{0\}$, the physical side at positive parameter. Write $H$ for the hyperbolic form on the trivial plane $\underline{\R}^2$ and call $T := T^*M \oplus \underline{\R}^2$ the one-rung bundle.
\begin{enumerate}
\item \emph{(Strict reading.)} No smooth symmetric form on any bundle $E \supset T^*M$ that equals $G \perp K$ outside $C$ with one signature of $K$ on both exterior regions is nondegenerate everywhere (Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}). The obstruction is the clock mismatch $2 \in \mathbb{Z}_8$, which is nonzero for every tame wall with two nonempty sides; so on every tame wall satisfying these hypotheses the condition in clause (a) of Conjecture \claimref{sheaf.wall-class} fails, whatever the torsion of $(\shL, N^*\Sig)$.
\item \emph{(Full relaxation.)} If the exterior model may change signature across the wall, nothing obstructs: for any bundle metric $A$ on $T^*M$ and any bump $\beta$ equal to $1$ near $\Sig$ and $0$ outside $C$, the form
\[
h_D(\alpha \oplus \alpha', \gamma \oplus \gamma') \;=\; G(\alpha,\gamma) - G(\alpha',\gamma') + \beta\bigl(A(\alpha,\gamma') + A(\alpha',\gamma)\bigr)
\]
on $T^*M \oplus T^*M$ is nondegenerate of signature $(n,n)$ at every point of $M$, and equals $G \perp (-G)$ outside $C$.
\item \emph{(One rung, two sides.)} There is a smooth symmetric form $h$ on $T$, nondegenerate at every point of $M$, equal to $G \perp H$ outside $C$ on the physical side and to $G \perp K_-$ outside $C$ on the far side with $K_-$ positive definite, if and only if $w_1(\shL) = 0$. The same holds with the roles exchanged ($H$ on the far side, a negative definite plane on the physical side), with $h|_{T^*M} = G$ in the construction.
\item \emph{(One rung, one side.)} There is a smooth symmetric form $h$ on $T$ over $\Mp$, nondegenerate at every point of $\Mp$ including $\Sig$, with $h|_{T^*M} = G$ along $\Sig$ and $h = G \perp H$ outside $C$, if and only if $w_1(\shL) = 0$. The standing hypothesis of Theorem \claimref{sheaf.one-sided-completion} is therefore necessary for every one-sided one-rung completion, not only for the coupling construction.
\item \emph{(Twisted rung.)} If the adjoined plane is $\Lambda \oplus \Lambda^*$ with its hyperbolic pairing, for a line bundle $\Lambda$ over $\Mp$, a form as in (4) with $\Lambda \oplus \Lambda^*$ in place of $\underline{\R}^2$ exists only if $\Lambda|_\Sig \cong \shL$. In particular a twisted one-sided completion requires $w_1(\shL)$ to lie in the image of the restriction $H^1(\Mp; \mathbb{Z}_2) \to H^1(\Sig; \mathbb{Z}_2)$.
\end{enumerate}
Consequently the pair $W(\Sig) := (w(\Sig), w_1(\shL))$ has a precise meaning: its coarse part obstructs the strict two-sided completion and is never zero on a two-sided wall; its torsion part obstructs exactly the one-rung completions, one-sided or two-sided; and no torsion-sensitive class can be characterised by clause (a) of Conjecture \claimref{sheaf.wall-class} in either reading of ``standard''.

## technical
The wall-class conjecture asks for a torsion-sensitive invariant of a tame wall, refining the signature mismatch, whose vanishing is equivalent to the existence of a completion nondegenerate on both sides. This result shows that the equivalence as posed cannot involve torsion, and locates where torsion does act. In the strict reading (one exterior model on both sides) the signature count always obstructs; in the fully relaxed reading (the added form may change signature across the wall) a doubling of the cotangent bundle removes every obstruction. Between the two, with exactly one adjoined hyperbolic plane, the obstruction is exactly the first Stiefel-Whitney class of the dying line: a two-sided completion that is standard on the physical side and positive definite on the far side exists if and only if $w_1(\shL) = 0$, and so does any one-sided one-rung completion that restricts to $G$ along the wall. With a twisted plane $\Lambda \oplus \Lambda^*$ the dying line must extend over the physical side.

The necessity proofs compare negative eigenbundles across the collar: on the physical exterior the negative bundle is that of the induced form on $T^*M/\shL$ plus the trivial negative line of $H$; on the far side, or at the wall itself, it is the same bundle plus a line isomorphic to $\shL$; comparing determinant lines gives $\shL$ trivial. The sufficiency in (3) is an explicit construction from the collar data, with a coupling small enough in the sense of the good-coupling bound.

## lay
At a tame wall where the geometry changes signature, earlier results showed that a repair which looks the same on both sides must fail somewhere. This result asks what happens if the repair may look different on the two sides. With unlimited room, everything can be repaired, so that version of the question detects nothing. With the room the series actually uses, one extra pair of directions, and keeping the original geometry unchanged at the wall itself, a repair exists exactly when the direction that dies at the wall does not twist like a Moebius band as one goes around the wall. That twist is the subtle topological invariant the conjecture was looking for; it decides the economical repair, not the strict one.

## one-liner
Assuming the tameness hypotheses, on a wall with two nonempty sides the signature mismatch always obstructs strict two-sided completions, a doubling removes every obstruction, and with one adjoined hyperbolic plane a completion that restricts to $G$ along the wall (one-sided, or two-sided with a positive far model) exists iff $w_1(\shL) = 0$.
