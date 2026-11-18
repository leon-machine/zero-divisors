---
id: synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial
kind: claim
version: 1
title: 'Completion with a fixed exterior form over a ball: stable triviality suffices'
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
  - std-algebra.spin-double-cover@1
  - synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_rotation_homotopy_joins_f_plus_f_inverse_to_the_identity
- kind: check
  ref: check.py::check_two_copies_of_the_plane_family_complete_with_a_fixed_form
- kind: check
  ref: check.py::check_winding_two_family_needs_one_added_direction
- kind: check
  ref: check.py::check_one_copy_has_no_frame
- kind: check
  ref: check.py::check_double_lift_of_the_winding_two_loop
lineage:
  motivated_by:
  - synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump
  - transport.obstructions-are-moved-never-destroyed
extraction:
  note: >-
    Fourth attack item of the problem (sufficiency over a contractible base). The stored transfer clause is a
    necessary condition; this proves the converse over R^m when the degeneration set lies in a ball, once flat
    directions are added, by an explicit form: the rotation that joins F (+) F^{-1} to the identity in the
    orthogonal group of doubled rank. It also shows by one family (winding two) that the directions are needed:
    vanishing of the class with the given exterior form does not suffice on the same bundle. That step uses the
    lifting clause (L) of the result on the position vector in codimension three, filed in the same session,
    which must therefore be accepted first. The completions built are continuous, not smooth. The number of
    added directions used is an upper bound, not claimed least. Not treated: bases other than R^m,
    neighbourhoods that are not balls (a ring with a solid torus around it), completions that restrict to the
    family inside the ball. The values of the group of stable classes over spheres (the periodicity theorem of
    Bott) are from memory and are not used.
  open_problem: op.eigenbundle-class-of-degenerations
---

## formal
Let $m \geq 1$, let $G$ be a continuous family of symmetric bilinear forms on $\R^{n}$ parametrised by $y \in \R^{m}$ (a form on the trivial bundle), $g(y)$ its self-adjoint map for the standard product, and $B \subset \R^{m}$ an open ball such that $G$ is nondegenerate at every point of $\R^{m} \setminus B$; so the degeneration set $\Sig$ is a compact subset of $B$, of any kind. On the sphere $\partial B$ let $G_{+}$, $G_{-}$ be the positive and negative eigenbundles of $g$, of ranks $p$ and $q$ (for $m = 1$, where $\partial B$ is two points, the statements below include that the ranks agree at the two points). A family of subspaces over $\partial B$ is \emph{trivial} if it has a continuous frame, and \emph{stably trivial} if its sum with a fixed space $\R^{c}$ is trivial for some $c \geq 0$. As in Theorem \claimref{synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump}, a \emph{model completion standard outside $B$} is a continuous symmetric form $h$ on $\R^{n} \oplus W_{0}$ over $\R^{m}$ that equals $G \perp K_{0}$ on $\R^{m} \setminus B$, for one fixed nondegenerate form $K_{0}$ on a fixed space $W_{0}$.
\begin{enumerate}
\item[(1)] \emph{(Necessity; the stored transfer clause.)} If a model completion standard outside $B$ is nondegenerate at every point, and $K_{0}$ has signature $(c, c')$, then $G_{+} \oplus \R^{c}$ and $G_{-} \oplus \R^{c'}$ are trivial over $\partial B$.
\item[(2)] \emph{(Sufficiency.)} If $G_{+} \oplus \R^{c}$ and $G_{-} \oplus \R^{c'}$ are trivial over $\partial B$, then with $N = n + c + c'$, $W_{0} = \R^{c} \oplus \R^{c'} \oplus \R^{N}$ and $K_{0} = 1_{c} \oplus (-1_{c'}) \oplus 1_{N}$ (the identity on the first and third summands, minus the identity on the second), there is a model completion standard outside $B$ that is nondegenerate at every point of $\R^{m}$; and then there is one for every nondegenerate form on $W_{0}$ of the same signature $(c + N, c')$, obtained from it by a constant change of basis of $W_{0}$. Explicitly, for $K_{0}$ as displayed, let $F(y) \in \mathrm{O}(N)$, $y \in \partial B$, have as columns an orthonormal frame of $G_{+} \oplus \R^{c}$ followed by one of $G_{-} \oplus \R^{c'}$, let $D = \operatorname{diag}(1_{p+c}, -1_{q+c'}, 1_{N})$, let $R_{t}$ be the rotation through the angle $t$ in each of the $N$ planes spanned by a basis vector of $\R^{n} \oplus \R^{c} \oplus \R^{c'}$ and the corresponding basis vector of the last summand $\R^{N}$, and
\[
\Phi_{t}(y) \;=\; (F(y) \oplus 1)\,R_{t}\,(1 \oplus F(y)^{-1})\,R_{t}^{-1} \;\in\; \mathrm{O}(2N), \qquad \Phi_{0} = F \oplus F^{-1}, \quad \Phi_{\pi/2} = 1 .
\]
With $\rho$ the radius of $B$, $y = r\omega$ in polar coordinates about its centre and $\hat y = \rho\,\omega$, the form with map
\[
\hat h(y) = \begin{cases}
g(y) \oplus K_{0}, & r \geq \rho,\\
\bigl((1-\lambda)\,g(\hat y) + \lambda\,\operatorname{sgn} g(\hat y)\bigr) \oplus K_{0}, \quad \lambda = 3(\rho - r)/\rho, & \tfrac23\rho \leq r \leq \rho,\\
\Phi_{t}(\hat y)\,D\,\Phi_{t}(\hat y)^{-1}, \quad t = \tfrac\pi2\,(2 - 3r/\rho), & \tfrac13\rho \leq r \leq \tfrac23\rho,\\
D, & r \leq \tfrac13\rho,
\end{cases}
\]
where $\operatorname{sgn} g$ is $+1$ on $G_{+}$ and $-1$ on $G_{-}$, is continuous, symmetric and invertible at every point. It does not restrict to $G$ inside $B$.
\item[(3)] \emph{(One condition.)} $G_{+}$ is stably trivial over $\partial B$ if and only if $G_{-}$ is. Hence: a model completion standard outside $B$, for some $W_{0}$ and $K_{0}$, nondegenerate at every point, exists if and only if the positive eigenbundle of the family is stably trivial on the bounding sphere. The stable class of $G_{+}$ on $\partial B$ is the whole obstruction.
\item[(4)] \emph{(Added directions are needed.)} Over $\R^{2}$ let $G = \begin{psmallmatrix} x^{2} - y^{2} & 2xy \\ 2xy & y^{2} - x^{2}\end{psmallmatrix}$, degenerate at the origin only, with eigenlines spanned by $(x,y)$ and $(-y,x)$, both trivial on every circle about the origin: the hypothesis of (2) holds with $c = c' = 0$. No continuous symmetric form on the same bundle of rank two (a model completion with $W_{0} = 0$) that equals $G$ outside a bounded set is nondegenerate at every point (by the lifting clause (L) of Theorem \claimref{synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two}, applied twice). With one added positive direction there is one: for $\beta \colon \R^{2} \to [0,1]$ continuous, $0$ near the origin and $1$ outside a disc, and $\nu = (-\beta y, \beta x, 1 - \beta)$, the reflection $1 - 2\,\nu\nu^{\mathsf T}/Q(\nu)$ has signature $(2,1)$ at every point and where $\beta = 1$ equals $\operatorname{sgn} G \oplus 1$, which a positive rescaling of the first two directions, as in the second line of (2), joins to $G \oplus 1$. So triviality of the eigenbundles together with those of a given exterior form does not suffice for that form; it suffices after flat directions are added.
\item[(5)] \emph{(Instances.)} For $\begin{psmallmatrix} x & y \\ y & -x\end{psmallmatrix}$ the positive eigenline is not stably trivial on a circle (clause (5) of the cited Theorem) and there is no model completion; for two copies of it the eigenbundles have the frames $(C\ell, S\ell)$, $(-S\ell, C\ell)$ with $\ell = (C, S)$ the unit eigenvector in the half angle, quadratic in $(C, S)$ and so continuous on the circle, and (2) gives a model completion on $\R^{8}$ with $K_{0}$ the identity of $\R^{4}$. For $x^{2}$ and $\operatorname{diag}(x,-x)$ over $\R$ the eigenbundles have the same rank at the two points of the sphere, and for $x^{2} + y^{2}$ over $\R^{2}$ the eigenbundle is a constant line; all are trivial, and model completions exist, as clause (6) of the cited Theorem found.
\end{enumerate}
\emph{Reading.} For a degeneration confined to a ball of $\R^{m}$, in particular an isolated one, the question whether a completion with a fixed exterior form exists is decided by one stable class on a sphere of dimension $m - 1$: the transfer clause of the cited Theorem is, for such families, an equivalence. The group in which the class lies, stable classes of real vector bundles over the sphere, is the reduced real K-group; its values by codimension are the periodicity theorem of Bott (cited from memory, not used). The number $N$ of added directions is what the construction uses and is not claimed to be least: in (4) one direction suffices where the construction uses two, and for the position vector on a module that carries one more anticommuting generator none is needed (clause (8) of the cited Theorem).

## technical
For a continuous family $G$ of symmetric forms on $\R^{n}$ over $\R^{m}$ whose degeneration set lies in an open ball $B$:

(1) (stored transfer) a completion with a fixed exterior form $K_{0}$, standard outside $B$ and nondegenerate everywhere, forces $G_{\pm} \oplus (K_{0})_{\pm}$ to be trivial on $\partial B$;

(2) conversely, if $G_{+} \oplus \R^{c}$ and $G_{-} \oplus \R^{c'}$ are trivial on $\partial B$, the frames give $F \colon \partial B \to \mathrm{O}(N)$, $N = n + c + c'$, and the rotation $(F \oplus 1)R_{t}(1 \oplus F^{-1})R_{t}^{-1}$ joins $F \oplus F^{-1}$ to the identity in $\mathrm{O}(2N)$; conjugating a constant diagonal form by it along the radius gives a completion with the fixed exterior form $1_{c} \oplus (-1_{c'}) \oplus 1_{N}$, nondegenerate everywhere (and so one for any fixed form of that signature, by a constant change of basis);

(3) $G_{+}$ is stably trivial iff $G_{-}$ is, so such a completion exists for some fixed form iff the positive eigenbundle is stably trivial on the sphere;

(4) the added directions are needed: for $\begin{psmallmatrix} x^{2} - y^{2} & 2xy \\ 2xy & y^{2} - x^{2}\end{psmallmatrix}$, whose eigenlines are trivial, no completion on the same rank-two bundle exists (the positive line turns twice in the circle of lines; proved with the lifting clause (L) of Theorem \claimref{synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two}), and one added direction gives one.

Ledger: transport-absent in its proof, which is linear algebra, the rotation homotopy of the orthogonal group (the classical step behind the stability of clutching functions; prior art, textbook K-theory) and continuity; transport-convenient in its use: for the series' families (the position vector at its zero divisor) it turns the stored necessary condition into a criterion.

## lay
An earlier result showed that a geometry which degenerates in a bounded region can be repaired, by adding extra directions that look the same everywhere far away, only if a certain twist of the geometry around the region is absent, or more exactly only if the twist can be undone by adding untwisted directions. Whether the absence of that twist is also enough was left open.

This result shows that it is enough, when the region sits inside a ball in ordinary flat space. The repair is written down. On the sphere around the ball the geometry splits the directions into those it counts as positive and those it counts as negative. If each family can be described by a fixed list of reference directions that vary continuously over the sphere, then after adding as many extra positive directions as there were directions in all, the whole arrangement can be rotated, step by step along the radius, into one that does not vary at all, and that one fills the inside of the ball without any degeneration.

The extra directions cannot always be avoided. One example, a geometry whose positive direction points along the radius and so turns once as one walks around the origin, has no twist in the above sense and still cannot be repaired without adding a direction; with one added direction it can.

## one-liner
Over $\R^{m}$, for a family of symmetric forms degenerating only inside a ball, a completion with a fixed exterior form that is nondegenerate everywhere exists iff the positive eigenbundle is stably trivial on the bounding sphere: the stored transfer clause is necessary, and conversely the rotation joining $F \oplus F^{-1}$ to the identity gives an explicit completion after $n + c + c'$ positive directions are added; the added directions are needed in general ($\begin{psmallmatrix} x^{2} - y^{2} & 2xy \\ 2xy & y^{2} - x^{2}\end{psmallmatrix}$ needs one).
