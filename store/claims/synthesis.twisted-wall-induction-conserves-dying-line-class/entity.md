---
id: synthesis.twisted-wall-induction-conserves-dying-line-class
kind: claim
version: 2
title: The twisted wall induction carries the dying line's class to every shadow wall
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, tameness, hyperbolic-plane]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (wording of proof (3) aligned with the cited rung result, at reader R09''s request)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.tame-wall-induction@5
  - synthesis.wall-class-one-rung-obstruction@2
  - sheaf.one-sided-completion@4
  - sheaf.infinite-wall-sequence@4
  - sheaf.imported-real-line-bundles@1
  - sheaf.determinant-identity-blow-up-expansion@3
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_determinant_identity
- kind: check
  ref: check.py::check_kernel_at_shadow_wall
- kind: check
  ref: check.py::check_twist_equivariance
- kind: check
  ref: check.py::check_moebius_wall
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - sheaf.wall-class
  - synthesis.wall-class-one-rung-obstruction
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Reader issue (ga-issues-R09.md): proof (3) said the clock coordinates shift by the rung; the rung (1,1) leaves both clock positions fixed, as the cited synthesis.wall-class-one-rung-obstruction states, and the proof now says so. Wording only, the argument unchanged. The Gram matrices and determinants of the entity stay (Gram matrices of forms, which the conventions allow).'
  open_problem: op.wall-class-invariant
  note: >-
    Supplies clause (b) of the wall-class conjecture for the pair W = (signature mismatch, w_1 of the
    dying line), the class that synthesis.wall-class-one-rung-obstruction showed is the obstruction at
    the one-rung level: along the wall induction, untwisted or twisted, the shadow wall's radical line is
    canonically a copy of the line bundle used to twist the rung, so its first Stiefel-Whitney class is
    the original one under the collar identification. Tested on an explicit wall with nonzero torsion
    class (T^2 x R, dying line rotating by pi around one circle), on which untwisted one-rung
    completions are obstructed and the twisted one exists. Transport-absent: bundle algebra of symmetric
    forms. Clause (a) stays unattainable as posed (the earlier result) and clause (c) is not addressed.
---

## formal
Let $(M, G)$ be a tame corank-one degeneration (\claimref{sheaf.tameness}) with $\Sig$ compact, separating $M$ into a physical side $\Mp$ and a far side, with radical line bundle $\shL$, and fix a product collar $C \cong \Sig \times [-1,1]$. Suppose $\shL$ extends to a real line bundle $\Lambda$ over $\Mp \cup C$ with $\Lambda|_\Sig \cong \shL$ (by \claimref{synthesis.wall-class-one-rung-obstruction}(5) this is necessary for any twisted one-rung completion; $\Lambda$ trivial when $w_1(\shL) = 0$). Fix a fibre metric on $\Lambda$. \emph{Twisted collar data} are a section $u$ of $TM \otimes \Lambda$ near $\Sig$ with $\langle k, u \rangle = 1$ for the inclusion $k : \Lambda|_\Sig \cong \shL \hookrightarrow T^*M$, a bump $\beta$ and constants $\mu, \nu \neq 0$; the \emph{twisted ambient form} on $T_\Lambda = T^*M \oplus \Lambda \oplus \Lambda^*$ is $h = G \perp H + \kappa$, with $H$ the hyperbolic pairing of $\Lambda \oplus \Lambda^*$ and $\kappa$ pairing $\alpha \in T^*M$ with $\xi \in \Lambda^*$ by $\nu\beta\,\xi(\langle\alpha, u\rangle)$ and with $\lambda \in \Lambda$ by $\mu\beta$ times the fibre metric of $\langle \alpha, u\rangle$ and $\lambda$.
\begin{enumerate}
\item In a unit frame of $\Lambda$, $h$ is the ambient form of \claimref{obj.sheaf.collar-data-coupling} with transversal the local component of $u$, and a change of frame acts by $D = 1 \oplus (-1) \oplus (-1)$, which preserves $h$. Hence $s = G^{-1}(u,u)$, $F = 1 - 2\mu\nu\beta^2 s$ (hyperbolic pair normalised to $H = 1$) and $\det h = -\det G \cdot F$ are well defined, and for good couplings the conclusions of Lemma \claimref{sheaf.tame-wall-induction} hold verbatim (sign convention: with $H(n_o, n_\infty) = 1$ as here, good couplings are those of the Lemma with $\mu\nu < 0$, so that $F \to -\infty$ as the wall is approached from the far side; the store's normalisation writes $F = 1 + 2\mu\nu\beta^2 s$ and takes $\mu\nu > 0$): the shadow wall $\Sig' = \{F = 0\}$ is a tame corank-one wall of $(T_\Lambda, h)$, a graph over $\Sig$ in the collar.
\item Along $\Sig'$ the radical of $h$ is $\shL' = \{(-G^{-1}u(\xi),\ \beta\mu s\,\xi^\sharp,\ \beta\nu s\,\xi) : \xi \in \Lambda^*\}$, whose projection to $T^*M$ is injective. So $\shL' \cong \Lambda|_{\Sig'}$, and under the collar identification $\Sig' \cong \Sig$, $w_1(\shL') = w_1(\shL)$.
\item $\Lambda$ extends $\shL'$ over the physical side of $\Sig'$, so the induction iterates with the same $\Lambda$, and along the whole wall sequence of \claimref{sheaf.infinite-wall-sequence} the pair $W(\Sig^{(j)}) = (2 \in \mathbb{Z}_8,\ w_1(\shL^{(j)}))$ is constant: the torsion part is transferred to every shadow wall while the clock coordinates shift by one rung per wall.
\item The bound is attained: on $M = T^2 \times \R$ with $G = -\partial_\varphi^2 + t\,K^2 + M^2$, $K = \cos\tfrac\varphi2\,\partial_\psi + \sin\tfrac\varphi2\,\partial_t$, $M = -\sin\tfrac\varphi2\,\partial_\psi + \cos\tfrac\varphi2\,\partial_t$, the wall $\{t = 0\}$ is tame and two-sided, $\shL = \operatorname{span}(\cos\tfrac\varphi2\,d\psi + \sin\tfrac\varphi2\,dt)$ has $w_1(\shL) \neq 0$, untwisted one-rung completions are obstructed, and with $\Lambda$ the same span over $M$, $\beta = 1$, the twisted form has $\det h = t - 2\mu\nu$, is nondegenerate on $\Sig$, and has shadow wall $\{t = 2\mu\nu\}$ whose radical line projects onto the same rotating span, so $w_1(\shL') \neq 0$.
\end{enumerate}

## technical
The wall-class conjecture asks for a torsion-sensitive invariant of tame walls that is conserved under the wall induction. The earlier one-rung result identified the torsion part as the first Stiefel-Whitney class of the dying line, which obstructs the untwisted one-rung completion and forces a twisted rung to use a line bundle extending the dying line. This result runs the induction with that twisted rung. Locally the twisted ambient form is the untwisted one, and the sign ambiguity of the twisting line acts by a reflection of the adjoined plane that preserves the form, so the shadow wall exists and is tame exactly as before. Its radical line is computed explicitly: its cotangent component is the metric dual of the twisted transversal, which carries the twist, so the new dying line is a copy of the twisting line. Hence the class is carried unchanged to every shadow wall, the same line bundle twists every later rung, and the pair made of the signature mismatch and this class is constant along the wall sequence. An explicit torus wall whose dying direction turns by half a revolution around one circle realises a nonzero class.

## lay
Where the geometry changes signature, the direction that dies can twist like a Moebius band as one goes around the wall. An earlier result showed that this twist blocks the most economical repair unless the extra directions added by the repair are twisted in the same way. This result follows the repair forward. Each repair creates a new wall a little further into the unphysical region, and the direction that dies there turns out to twist in exactly the same way as before. So the twist is never removed; it is handed on from wall to wall, as the series' principle that obstructions are moved rather than destroyed expects. A concrete example on a doughnut-shaped wall shows the twist really occurs.

## one-liner
Assuming the tameness hypotheses and that the dying line extends over the physical side, the twisted wall induction makes each shadow wall's dying line a copy of the twisting line, so $w_1$ of the dying line is conserved along the whole wall sequence, nonzero on an explicit torus wall.
