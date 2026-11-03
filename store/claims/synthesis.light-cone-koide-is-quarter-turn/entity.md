---
id: synthesis.light-cone-koide-is-quarter-turn
kind: claim
version: 1
title: The Lorentzian slice of face space is a quarter-turn of the doublet, and the Koide angle holds only for the positive square root
status: proved
region: synthesis
subject: generations
tags: [flavour-and-mixing, representation-theory]
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
review: draft
derivations:
- name: main
  uses:
  - families.chart-computation-sign-twist-bracket-form@5
  - families.koide-nullity-condition-one-member-invariant@2
  - synthesis.coherent-face-vector-real-slices@1
  - families.alignment-computed-thirteenth-refutation-democracy-one@4
  - families.linear-conjecture-refuted-data@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_quarter_turn_conjugacy
- kind: check
  ref: check.py::check_physical_vector_never_null
- kind: check
  ref: check.py::check_basis_free_angle_and_lie_real_form
- kind: check
  ref: check.py::check_angle_selects_positive_root
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.koide-nullity-condition-one-member-invariant
  - synthesis.coherent-face-vector-real-slices
extraction:
  open_problem: op.gram-square-and-face-space
  note: 'Answers successor problems (2) and (4) of the families paper in their adversarial form. (4) A real structure with C of signature (1,2) on its slice exists (sigma_{1,-1}, already in the store), but it is the conjugate of complex conjugation by the quarter-turn D = P_s + i P_d of the doublet, and C pulled back by D is the light-cone member q; so finding it adds nothing to the choice of member, and C(v) of the physical real face vector is sum m_k under every real structure. What would promote the light-cone reading is a derivation of the quarter-turn itself. (2) Among positive semidefinite Hermitian forms the Gram-square property is automatic (H = A^2 for A Hermitian), so a non-Gram form with the order-one angle cannot exist and the refutation condition recorded in T13 is vacuous unless the face-space map is restricted (rank one in the source, as in the alignment proposition); what the angle does fix is the root, the positive one. Transport-absent: linear algebra on face space and on Hermitian 3x3 matrices. The tau mass is the stored 1776.93 +- 0.09 MeV (families.linear-conjecture-refuted-data); the electron and muon masses are PDG central values cited from memory. Clause (ii) and the slice signatures in (i) restate stored content; the new content is the quarter-turn conjugacy and pullback in (i), (iii) and (iv).'
---

## formal
Let $C(v) = \sum_{k} v_{k}^{2}$ be the bracket form on face space $\C^{3}$, $P_{s} = \J/3$ and $P_{d} = 1 - P_{s}$ the singlet and doublet projectors (Proposition \claimref{families.chart-computation-sign-twist-bracket-form}), $q(v) = s^{2} - Q(d)$ the equal-coefficient member of Proposition \claimref{families.koide-nullity-condition-one-member-invariant} for real $v$ with $s^{2} = C(P_{s}v)$ and $Q(d) = C(P_{d}v)$, and $\sigma_{x,y} = (xP_{s} + yP_{d}) \circ \overline{\phantom{v}}$ the $S_{3}$-equivariant real structures of Theorem \claimref{synthesis.coherent-face-vector-real-slices}(i). For $a, b \in \C^{\times}$ put $D_{a,b} = aP_{s} + bP_{d}$.
\begin{enumerate}
\item[(i)] \emph{(The Lorentzian slice is a quarter-turn.)} The signatures $\pm(t^{2} - Q(d))$ on the slices of $\sigma_{1,-1}$ and $\sigma_{-1,1}$ are those of Theorem \claimref{synthesis.coherent-face-vector-real-slices}(i), restated; what is added is their source. For $a, b \in \{1, i\}$, $\sigma_{x,y} = D_{a,b} \circ \overline{\phantom{v}} \circ D_{a,b}^{-1}$ with $x = a/\bar{a}$, $y = b/\bar{b}$, so the four $C$-compatible $S_{3}$-equivariant real structures are the conjugates of complex conjugation by $D_{a,b}$; and for real $v$, $C(D_{a,b}v) = a^{2}s^{2} + b^{2}Q(d)$. In particular $D_{1,i} = P_{s} + iP_{d} = \exp(\tfrac{i\pi}{2}P_{d})$ carries the standard real face space onto the slice of $\sigma_{1,-1}$, and $C \circ D_{1,i} = q$ there. So $C$ has signature $(1,2)$ on the slice of $\sigma_{1,-1}$ exactly because that slice is the standard one read through $q$: the real structure and the choice of the light-cone member are one datum, the relative quarter-turn of the doublet.
\item[(ii)] \emph{(The physical vector is null on no slice; a restatement.)} Proposition \claimref{families.chart-computation-sign-twist-bracket-form}(2) already gives $C(v_{\mathrm{lepton}}) = \sum_{k}m_{k} \neq 0$ and that $C$-nullity and $q$-nullity share nothing but the word; in the present terms: $C(v)$ is defined without reference to a real structure, and for a face vector with real components it is $\sum_{k}v_{k}^{2} > 0$. So the physical $\sqrt{m}$ face vector, with $C = \sum_{k}m_{k}$, is $C$-null on the slice of no $C$-compatible real structure; its quarter-turn $D_{1,i}v$ lies on the slice of $\sigma_{1,-1}$ and is $C$-null exactly when $q(v) = 0$, which is the Koide relation.
\item[(iii)] \emph{(The angle is basis-free, and its Lorentzian form is a Lie real form.)} For Hermitian $A$ with eigenvalues $\lambda_{k}$, $\operatorname{tr}A = \sum_{k}\lambda_{k}$ and $\operatorname{tr}A^{2} = \sum_{k}\lambda_{k}^{2}$, so $Q = \operatorname{tr}A^{2}/(\operatorname{tr}A)^{2}$ and $\cos^{2}\theta = (\operatorname{tr}A)^{2}/(3\operatorname{tr}A^{2})$ are the face-space data of the eigenvalue vector whatever the eigenbasis: $\theta$ is the Hilbert-Schmidt angle between $A$ and $1$. The map $A \mapsto \tfrac13(\operatorname{tr}A)1 + iA_{0}$, with $A_{0}$ the traceless part, carries the Hermitian matrices onto $\R 1 \oplus \mathfrak{su}(3)$, the fixed set of the antilinear involutive Lie automorphism $X \mapsto -X^{\dagger} + \tfrac23\,\overline{\operatorname{tr}X}\,1$ of $\mathfrak{gl}(3,\C)$; on it $\operatorname{tr}(X^{2})$ has signature $(1,8)$ (on the Hermitian matrices $(9,0)$), and its value on the image of $A$ is $\tfrac13(\operatorname{tr}A)^{2} - \operatorname{tr}A_{0}^{2}$, which is $q$ of the eigenvalue vector.
\item[(iv)] \emph{(The root.)} Every positive semidefinite Hermitian $H$ is $A^{2}$ with $A$ Hermitian, with $2^{3}$ choices of $A$ when the spectrum is simple, and the Koide angle of $A$ depends on the choice. For the charged-lepton masses, with $m_{\tau} = 1776.93 \pm 0.09$ MeV as stored (Proposition \claimref{families.linear-conjecture-refuted-data}) at its central value and both ends, the positive root gives $Q$ within $10^{-5}$ of $\tfrac23$, while every root with mixed signs gives $Q$ more than $\tfrac{3}{100}$ above it (the root with the electron's sign reversed gives $Q$ between $0.704$ and $0.705$).
\end{enumerate}
So the real-structure question of the families paper has a positive answer that carries no information: the Lorentzian slice exists, but choosing it is choosing the light-cone member, and the physical real vector is never on it. What would make the light-cone reading a consequence is a derivation of the quarter-turn $\exp(\tfrac{i\pi}{2}P_{d})$ from the series' structures. And since every positive semidefinite mass form is the square of a Hermitian face-space map, the Gram-square property as such has no content; the order-one angle fixes only that $\sqrt{m}$ is the spectrum of the positive square root, and a Gram-square premise with content must restrict the map, as the alignment proposition's rank-one square of the source does (Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one}(3)); a derivation of such a restriction from slot covariance is filed alongside, synthesis.slot-covariance-forces-gram-square.

## technical
Face space carries the complex bracket form $C(v) = \sum_{k}v_{k}^{2}$, which is Euclidean on real vectors, and the Koide relation is nullity for a different, Lorentzian form $q = s^{2} - Q(d)$ (singlet squared minus doublet squared). The store already shows a real structure of face space on whose slice $C$ is Lorentzian. This result shows why that is no progress: the slice is the ordinary real face space turned by a quarter-turn on the doublet, $D = P_{s} + iP_{d}$, and $C$ pulled back by $D$ is exactly $q$. So the real structure and the light-cone choice are the same datum. Moreover $C$ of the physical face vector, whose components are the real $\sqrt{m_{k}}$, is $\sum_{k}m_{k}$ whatever real structure is chosen, so that vector is never $C$-null; only its quarter-turned image is, and exactly when Koide holds.

Two further facts. The Koide angle is the Hilbert-Schmidt angle between the square-root mass matrix $A$ and the identity, so it does not depend on the eigenbasis; and the light-cone form is the trace form of the real Lie algebra $\R 1 \oplus \mathfrak{su}(3)$ (signature $(1,8)$), onto which the same quarter-turn, applied to the traceless part, carries the Hermitian matrices. And any positive semidefinite mass form is the square of a Hermitian matrix, eight of them for a simple spectrum, with different Koide angles; for the charged leptons, at the stored tau mass, only the positive root gives $\tfrac23$ within $10^{-5}$ (the electron-flipped root gives a value between $0.704$ and $0.705$). So "the Yukawa form is a Gram square" says nothing by itself; the angle picks the positive root, and a Gram-square premise has content only if it restricts the map, as the rank-one square of the source does.

## lay
The families paper notices that the Koide relation among the electron, muon and tau masses looks like a statement that a certain vector lies on a light cone, if lengths are measured in a relativistic way, and asks whether the framework's own geometry could force that way of measuring. This result shows that the obvious way to do it, choosing a different real section of the paper's complex space, is a relabelling: it amounts to rotating two of the three directions by a quarter turn, which is the same as choosing the relativistic measurement in the first place, and the actual vector of masses never lies on such a light cone without that rotation. A real explanation would have to produce the quarter turn from the theory. The result also notes that the paper's premise that the mass matrix is a square is automatic, and that what the measured angle really fixes is that the masses' square roots are all taken positive.

## one-liner
The face-space real structure on which the bracket form is Lorentzian is complex conjugation conjugated by the doublet quarter-turn $P_{s} + iP_{d}$, under which the bracket form becomes the light-cone member, so it adds nothing to that choice and the physical vector is null on no slice; and the Gram-square property is automatic, the Koide angle selecting only the positive square root.
