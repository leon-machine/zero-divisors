---
id: note.transport.setting-hyperbolic-atom-matrix-algebra-moore
kind: note
version: 1
title: 'The hyperbolic atom as a matrix algebra: the Moore--Penrose pseudoinverse'
status: setting
subject: zero-divisors
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.no-go-level-elements
locators:
  paper: T01
  number: Setting
  section: 'Type N: the isotropic obstruction, and Rule 1'
  line: 1095
  subsection: 'The hyperbolic atom as a matrix algebra: the Moore--Penrose pseudoinverse'
---

## formal
The algebra $\Cl(1,1)$ is isomorphic to the algebra $M_2(\R)$ of real $2 \times 2$ matrices: with $e_0^2 = 1$, $e_1^2 = -1$, the assignment
\[
e_0 \mapsto E = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}, \qquad
e_1 \mapsto F = \begin{psmallmatrix} 0 & 1 \\ -1 & 0 \end{psmallmatrix}
\]
satisfies $E^2 = I$, $F^2 = -I$ and $EF + FE = 0$, hence extends to an algebra isomorphism (both algebras have dimension four; $M_2(\R)$ is simple). A base vector $x e_0 + y e_1$ maps to $\begin{psmallmatrix} 0 & x+y \\ x-y & 0 \end{psmallmatrix}$, of determinant $-(x^2 - y^2) = -Q$: \emph{a vector is null exactly when its matrix is singular}. In particular the hyperbolic pair $v = \tfrac12(e_0 + e_1)$, $w_0 = \tfrac12(e_0 - e_1)$ (so $v \cdot w_0 = \tfrac12$) maps to
\[
v \;\mapsto\; N = \begin{psmallmatrix} 0 & 1 \\ 0 & 0 \end{psmallmatrix}, \qquad
w_0 \;\mapsto\; N^{\mathsf T} = \begin{psmallmatrix} 0 & 0 \\ 1 & 0 \end{psmallmatrix}.
\]
Under this dictionary the objects of Section \ref{sec:nogo} become textbook objects of linear algebra: the equation $v\,\sigma(v)\,v = v$ is Penrose's first equation $AXA = A$ for a \emph{generalized inverse} of a singular matrix, and the abundance of pseudo-inverses noted there is the familiar abundance of generalized inverses.

Matrix theory has a canonical selection among them: the Moore--Penrose pseudoinverse $A^{+}$, which for a rank-one matrix is $A^{+} = A^{\mathsf T}/\lVert A \rVert_F^{\,2}$. Applied to the null vectors of this base,
\[
(\lambda N)^{+} = \lambda^{-1} N^{\mathsf T}, \qquad (\lambda N^{\mathsf T})^{+} = \lambda^{-1} N,
\]
which is, under the isomorphism, \emph{exactly} the equivariant section $\sigma(\lambda v) = \lambda^{-1} w_0$, $\sigma(\lambda w_0) = \lambda^{-1} v$ of Remark \claimref{note.transport.hyperbolic-atom}: the hyperbolic atom's self-completeness is the Moore--Penrose construction expressed in the Clifford algebra. The agreement is not a coincidence of formulas. By \eqref{eq:partners} the partner of a null vector in a hyperbolic plane is unique, so any rule at all that returns a null partner returns this one; the Euclidean transpose supplies it, and so does the metric description.

The agreement extends to the failure, which is the instructive part. It is classical that $A^{+}$ is canonical only relative to a choice of \emph{definite} inner product: it is built from the transpose, the adjoint of the Euclidean metric, and transforms correctly under orthogonal maps, $(UAV)^{+} = V^{\mathsf T} A^{+}\, U^{\mathsf T}$ for orthogonal $U, V$, but not under general invertible ones. Known theory therefore already signals that the obvious candidate for $\sigma$ must fail to respect an \emph{indefinite} symmetry group, which preserves no definite inner product. Theorem \claimref{transport.no-go-level-elements} is the sharp form of that signal. For $n = 2$ the stabiliser of a null direction in $O(1,1)$ contains no null rotations, nothing shears, the partner set \eqref{eq:partners} is a single point, and the Moore--Penrose choice survives as an equivariant section (Remark \claimref{note.transport.hyperbolic-atom}). For $n \geq 3$ the stabiliser acquires a unipotent radical of null rotations, the partner set becomes a torsor under it, and not only the Moore--Penrose rule but \emph{every conceivable rule}, valued in the Clifford algebra of any extension or in a matrix algebra over it, is sheared away. The no-go theorem thus marks the precise boundary of the Moore--Penrose phenomenon: canonical generalized inversion of null directions ends exactly where parabolic stabilisers begin.

## technical
pending

## lay
pending

## one-liner
pending
