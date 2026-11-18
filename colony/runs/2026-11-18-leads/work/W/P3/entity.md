---
id: synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line
kind: claim
version: 1
title: 'The eigenbundle class of a corank-one wall is the dying line; two-sided rungs by transfer'
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, obstruction-types, classification]
proposed_by:
  kind: ai
  session: 2026-11-18-leads
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-leads
review: draft
derivations:
- name: main
  uses:
  - synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump@1
  - synthesis.wall-class-one-rung-obstruction@3
  - synthesis.wall-rung-count-is-height-of-dying-line-class@2
  - synthesis.imported-whitney-product-formula-and-projective-space@1
  - sheaf.imported-real-line-bundles@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_twisted_wall_and_its_eigenbundles
- kind: check
  ref: check.py::check_two_rung_completion_moves_the_twist_into_the_far_form
- kind: check
  ref: check.py::check_transfer_bookkeeping_for_k_rungs
lineage:
  motivated_by:
  - synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump
  - sheaf.wall-class
  - synthesis.wall-class-one-rung-obstruction
extraction:
  note: >-
    Second attack item of the problem. Result of the comparison: agreement. The class of the eigenbundles of a
    corank-one sign-changing wall, relative across the collar, is the dying line: its rank is the signature jump
    and its isomorphism class is w_1(L), so it carries the same information as the stored pair W(Sigma) (with
    w(Sigma) read as the clock mismatch, as in the one-rung theorem), neither finer nor coarser. For two-sided
    completions that are nondegenerate everywhere, with no condition along the wall, transfer gives a necessary
    condition of the same form as the necessity clause of the stored rung-count theorem, with the bundle N the
    negative eigenbundle of the far side's exterior form. The stored clause concerns one-sided completions that
    restrict to G along the wall, which have no far form; neither statement is derived from the other here, and
    whether the two-sided count equals the stored one-sided count is not decided. Overlap with the store: clause
    (3) at k = 1 re-proves the necessity half of clause (3) of the one-rung theorem; in clause (4) the one-rung
    failure is an instance of that clause and the two-rung form is of the kind of clause (2) of the rung-count
    theorem. New: the bookkeeping of the eigenbundles (1), the transfer from slice to slice (2), and N for
    two-sided completions. The class computed is local to the collar; the stored transfer class is relative to
    the whole base and can carry information from the exterior, which this result does not address. The
    hypotheses are stated directly (compact wall, product collar, corank one, the two signatures, the bundle
    pulled back along the collar); the first-order clause (T3) of the tameness hypotheses and smoothness are not
    used, and no assumes edge is proposed. The Whitney step uses the dimension axiom of Stiefel-Whitney classes
    (no class above the rank), which the text of the imported Fact does not state; the stored rung-count proof
    uses it in the same way, and adding it to the Fact is the maintainer's. Naturality and conservation under
    wall induction, clauses (b) and (c) of the wall-class conjecture, are not shown here. A restatement of clause
    (c) of that conjecture around this result is left to the maintainer.
  open_problem: op.eigenbundle-class-of-degenerations
---

## formal
\emph{Setting (W).} Let $M$ be a connected manifold, $V \to M$ a real vector bundle with a bundle metric and a continuous symmetric form $G$ (in the series $V = T^{*}M$ and $G$ a cometric), $\Sig \subset M$ compact with a neighbourhood $C \cong \Sig \times [-1,1]$, $\Sig = \Sig \times \{0\}$, along which $V$ is identified with the pull-back of $V_{\Sig} = V|_{\Sig}$. Suppose that on $C$ the form $G$ is nondegenerate off $\Sig$, of signature $(p,q)$ where $s > 0$ (the physical side) and $(p-1,q+1)$ where $s < 0$ (the far side), and that on $\Sig$ it has corank one, with kernel the line bundle $\shL \subset V_{\Sig}$. The identification of $V$ along $C$ with a pull-back is a hypothesis of (W). A degeneration satisfying the hypotheses of Theorem \claimref{synthesis.wall-class-one-rung-obstruction} (a tame corank-one degeneration in the sense of \claimref{sheaf.tameness}, with compact wall separating two nonempty sides of signatures $(p,q)$ and $(p-1,q+1)$, and a product collar) satisfies (W) once the collar is taken thin enough to meet no other degeneration, given that a bundle over $\Sig \times [-1,1]$ is the pull-back of its restriction to $\Sig$ (homotopy invariance of bundles over a compact base; standard, cited from memory, not in the store). The side signatures are hypotheses of that Theorem, not part of tameness. The first-order clause (T3) and smoothness are not used below. Let $\overline G$ be the form induced on $V_{\Sig}/\shL \cong \shL^{\perp}$, of signature $(p-1,q)$, with eigenbundles $\overline G_{\pm}$, and write $X|_{s}$ for the restriction of a bundle $X$ over $C$ to $\Sig \times \{s\}$, as a bundle over $\Sig$. Eigenbundles $(\cdot)_{\pm}$ are those of Theorem \claimref{synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump}.
\begin{enumerate}
\item[(1)] \emph{(The eigenbundles on the two sides.)} For $s > 0$: $G_{+}|_{s} \cong \overline G_{+} \oplus \shL$ and $G_{-}|_{s} \cong \overline G_{-}$. For $s < 0$: $G_{+}|_{s} \cong \overline G_{+}$ and $G_{-}|_{s} \cong \overline G_{-} \oplus \shL$. So the positive eigenbundle of the family loses, and the negative one gains, exactly the dying line across the wall: the class of the eigenbundles relative across the collar, the comparison of the slices on the two sides, is $\shL$, counted with the sign $+$ for $G_{+}$ and $-$ for $G_{-}$. It is local to the collar: the class of clause (4) of the cited Theorem is relative to the whole base and can carry further information from the exterior, which is not addressed here.
\item[(2)] \emph{(Transfer across the wall.)} Let $W \to M$ be a bundle identified along $C$ with a pull-back from $\Sig$, and $h$ a continuous symmetric form on $V \oplus W$, nondegenerate at every point of $M$, equal to $G \perp K_{\mathrm{ph}}$ on $\Sig \times \{1\}$ and to $G \perp K_{\mathrm{far}}$ on $\Sig \times \{-1\}$ for nondegenerate forms $K_{\mathrm{ph}}$, $K_{\mathrm{far}}$ on $W$ there (a completion standard outside the interior of the collar; no condition on $h$ along $\Sig$, none on the signatures of the two forms). Then over $\Sig$
\[
\overline G_{+} \oplus \shL \oplus (K_{\mathrm{ph}})_{+} \;\cong\; \overline G_{+} \oplus (K_{\mathrm{far}})_{+}, \qquad
\overline G_{-} \oplus (K_{\mathrm{ph}})_{-} \;\cong\; \overline G_{-} \oplus \shL \oplus (K_{\mathrm{far}})_{-} .
\]
The exterior forms carry the opposite of the class of (1): the far form's negative eigenbundle and the physical form's positive eigenbundle absorb the dying line.
\item[(3)] \emph{(Rungs.)} If $W = \underline{\R}^{2k}$ and $K_{\mathrm{ph}} = H_{k}$, the sum of $k$ hyperbolic planes, then $K_{\mathrm{far}}$ has signature $(k+1, k-1)$ and $N := (K_{\mathrm{far}})_{-}|_{-1}$ is a bundle of rank $k - 1$ over $\Sig$ with
\[
\overline G_{-} \oplus \shL \oplus N \;\cong\; \overline G_{-} \oplus \underline{\R}^{k} .
\]
Here $N$ is the negative eigenbundle of the far side's exterior form. The isomorphism has the form of the necessity clause (1) of Theorem \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}; that clause concerns one-sided completions that restrict to $G$ along the wall, which have no far form, and neither statement is derived from the other here. The consequences are of the same form as the stored ones: $\det N \cong \shL$; by the Whitney formula (\claimref{synthesis.imported-whitney-product-formula-and-projective-space}) and the dimension axiom of Stiefel-Whitney classes (no class above the rank; classical, used as in the stored rung-count proof, and not stated in the text of that Fact), $w(N) = (1 + x)^{-1}$ with $x = w_{1}(\shL)$, so $x^{j} = 0$ for $j \geq k$; for $k = 1$, $\shL$ is trivial ($x = 0$, \claimref{sheaf.imported-real-line-bundles}), the two-sided half of clause (3) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction}; for $k = 2$, $N \cong \shL$ and $\overline G_{-} \oplus \shL \oplus \shL \cong \overline G_{-} \oplus \underline{\R}^{2}$.
\item[(4)] \emph{(The class moved, on a twisted wall.)} On the cylinder $S^{1} \times \R$, with $\ell(a) = (\cos\tfrac a2, \sin\tfrac a2)$ and $G = 1 + (s - 1)\,\ell\ell^{\mathsf T}$ on the trivial plane bundle (signature $(2,0)$ for $s > 0$, $(1,1)$ for $s < 0$, kernel the twisted line $\shL = \R\ell$ at $s = 0$): there is no two-sided completion with one rung (a constant hyperbolic form on the trivial plane on either side, a definite form on the other) that is nondegenerate at every point, and there is one with two rungs. The first is an instance of clause (3) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction}. With $n = (\cos\tfrac a2, \sin\tfrac a2)$ and $n^{\perp}$ its rotation by a quarter turn in a fixed plane $\Pi$ of $\R^{4}$, and $b = \cos t\; n^{\perp} + \sin t\; \ell$, the form $1 - 2(nn^{\mathsf T} + bb^{\mathsf T})$ on $\R^{2} \oplus \R^{4}$ has signature $(4,2)$ for every $t$; at $t = 0$ it is $1 \oplus K_{\mathrm{ph}}$ with $K_{\mathrm{ph}} = 1 - 2\pi_{\Pi}$, a constant form of signature $(2,2)$, and at $t = \tfrac\pi2$ it is $(1 - 2\ell\ell^{\mathsf T}) \oplus K_{\mathrm{far}}$ with $K_{\mathrm{far}} = 1 - 2nn^{\mathsf T}$, of signature $(3,1)$, whose negative line $N = \R n$ is twisted like $\shL$, as (3) requires.
\item[(5)] \emph{(Comparison with the stored wall class, relative across the collar.)} The class of (1) has two parts: its rank, the signature jump $(1,-1)$, whose residue is the clock mismatch $2$ of Theorem \claimref{synthesis.wall-class-one-rung-obstruction}; and the isomorphism class of the line $\shL$, which is $w_{1}(\shL)$ (\claimref{sheaf.imported-real-line-bundles}). So on a wall satisfying (W) the eigenbundle class relative across the collar carries exactly the information of the stored pair $W(\Sig) = (w(\Sig), w_{1}(\shL))$, with $w(\Sig)$ read as the coarse part of Theorem \claimref{synthesis.wall-class-one-rung-obstruction}, the clock mismatch: it is neither finer nor coarser. (The store also writes $w(\Sig)$ for a Stiefel-Whitney class of the wall itself, in \claimref{synthesis.lens-space-wall-rung-count-sees-the-integral-twist}; that reading is not the one used here.) What completions ask of it is not that it vanish (its rank never does, which is the stored obstruction to one exterior form on both sides) but, for $k$ rungs, that $\shL$ have a partner $N$ of rank $k - 1$ as in (3).
\end{enumerate}
\emph{Reading.} For two-sided completions, (3) gives lower bounds on the number of rungs of the same form as the stored lower bounds on the one-sided rung count: the height of $x$; for two rungs the triviality of $\shL \oplus \shL$ after adding $\overline G_{-}$; for the complexification $\xi$ of $\shL$, given the exterior-power operations of K-theory (not derived in the store), the vanishing of $(1 - \xi)^{k} = 2^{k-1}(1 - \xi)$, the coefficient of $t^{k}$ in $(1 + t)^{k}/(1 + \xi t)$. Argued, not proved: the two-sided count is the number of flat directions needed to cancel the class of the wall in the presence of $\overline G_{-}$ (the condition of (3) involves $\overline G_{-}$, so the count depends on $q$ and not on the class alone); and the rotation of (4) gives a two-sided completion with $k$ rungs whenever $\shL$ embeds in $\underline{\R}^{k}$ over the wall with a complement that extends over the far exterior. Not decided: whether the two-sided count equals the stored one-sided count $k(\Sig)$; the one-sided necessity clause, the stored sufficiency clauses, the twisted-rung clause (5) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction} and the lens-space counts do not follow from this result. Naturality of the class and its conservation under wall induction, clauses (b) and (c) of Conjecture \claimref{sheaf.wall-class}, are not shown here.

## technical
For a compact wall with a product collar across which a symmetric form has corank one on the wall and signatures $(p,q)$ and $(p-1,q+1)$ on the two sides (every tame corank-one wall with compact cross-section; first-order vanishing is not needed):

(1) across the wall the positive eigenbundle loses the dying line $\shL$ and the negative one gains it: the eigenbundle class of the wall, relative across the collar, is $\shL$;

(2) every two-sided completion that is nondegenerate everywhere, with exterior forms $K_{\mathrm{ph}}$ and $K_{\mathrm{far}}$, has $\overline G_{+} \oplus \shL \oplus (K_{\mathrm{ph}})_{+} \cong \overline G_{+} \oplus (K_{\mathrm{far}})_{+}$ and $\overline G_{-} \oplus (K_{\mathrm{ph}})_{-} \cong \overline G_{-} \oplus \shL \oplus (K_{\mathrm{far}})_{-}$ over the wall, with no condition on the completion along the wall;

(3) with $k$ hyperbolic planes on the physical side the far form's negative eigenbundle $N$ has rank $k - 1$ and $\overline G_{-} \oplus \shL \oplus N \cong \overline G_{-} \oplus \underline{\R}^{k}$: a two-sided statement of the same form as the stored one-sided necessity clause of the rung count, whose relation to the one-sided count is not decided;

(4) on the twisted wall of the cylinder one rung, with a constant hyperbolic plane, fails and an explicit two-rung form is nondegenerate everywhere, its far form having a negative line twisted like $\shL$;

(5) the class carries the information of the stored pair $(w(\Sig), w_{1}(\shL))$, with $w(\Sig)$ read as the clock mismatch: its rank is the signature jump and its isomorphism class is $w_{1}(\shL)$.

Ledger: transport-absent in its proof (bundles of eigenspaces, continuity, the stored transfer clause). It reads the transfer clause for arbitrary families on the walls of the one-rung and rung-count theorems, for two-sided completions; for those, the number of rungs is bounded below by the least rank in which the opposite of the wall's class is realised beside $\overline G_{-}$. The stored one-sided theory is not rederived.

## lay
At a wall where a geometry changes its signature, one direction switches from being counted as positive to being counted as negative. That direction, followed along the wall, can be twisted like a Moebius band. Earlier results showed that the twist bears on how many extra pairs of directions (rungs) a repair of the wall needs, and a separate result showed that any repair of any degeneration must carry, in what it adds, the mirror image of the twist of the geometry.

This result reads the second statement at a wall. Comparing the two sides of the wall, the twist that the general result speaks of is exactly the switching direction: the bundle of positive directions loses it across the wall and the bundle of negative directions gains it. A repair that covers both sides and works everywhere has to compensate, and with a fixed set of rungs on one side the compensation falls on the other side: the added structure there must contain a twisted part that cancels the switching direction. This gives, for repairs covering both sides, conditions of the same shape as those the earlier wall results found for repairs of one side; whether the two kinds of repair need the same number of rungs is not settled here. An explicit example on a cylinder shows the mechanism: one rung cannot repair a wall with a twisted switching direction, two can, and the added structure on the far side is then twisted in the same way.

So, compared across the wall, the twist of the general theorem carries the same information as the pair of data that the earlier wall results used. That this pair is the natural invariant the earlier conjecture asked for, carried from wall to wall, is not shown here.

## one-liner
Across a compact corank-one sign-changing wall the positive eigenbundle loses the dying line $\shL$ and the negative one gains it, so the eigenbundle class relative across the collar is $\shL$, with the information of the stored pair $(w(\Sig), w_{1}(\shL))$; by transfer every two-sided completion that is nondegenerate everywhere has $\overline G_{-} \oplus (K_{\mathrm{ph}})_{-} \cong \overline G_{-} \oplus \shL \oplus (K_{\mathrm{far}})_{-}$, which for $k$ rungs is a necessary condition of the same form as the stored one-sided one, with $N$ the far form's negative eigenbundle; the relation to the one-sided rung count is not decided.
