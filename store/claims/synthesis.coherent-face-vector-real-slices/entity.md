---
id: synthesis.coherent-face-vector-real-slices
kind: claim
version: 2
title: 'The coherent face vector meets no real slice'
status: proved
region: synthesis
subject: generations
tags: [flavour-and-mixing, representation-theory]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - families.rigidity-pairing-sector-one-event@3
  - families.chart-computation-sign-twist-bracket-form@5
  - families.koide-nullity-condition-one-member-invariant@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_fourier_line_isotropic_and_not_real
- kind: check
  ref: check.py::check_real_structures
- kind: check
  ref: check.py::check_projection_and_koide
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.koide-nullity-condition-one-member-invariant
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The Fourier unit in zeta, the channel phase e^{i chi}, the pairing phase kappa in -i R_{>0}, the slice i R^3 and its coordinate i p, the orientation -i -> +1, the channel vectors -i u''/sqrt3, -i f_+/sqrt3, the check field Q(sqrt3)[i] and the instance w = 1 + i became I_4, with numbers and face-vector components read in span{1, I_4} (complex conjugation reversing I_4) and the complex lines C f_+ and scalars in C written in span{1, I_4}; no bare i remains.'
  open_problem: op.gram-square-and-face-space
  note: Clause (i) classifies the real structures by Schur's lemma; clauses (ii)-(iv) test the suggestion that the channel phase chi might supply the relative factor i placing the physical face vector on a Lorentzian slice, and refute it. The statement is mathematics about the coherent vector of the rigidity proposition; reading the projected vector as the physical sqrt(m) vector is a reading, not proved, and differs from the skeleton theorem's reading of masses from the spectrum of H (which in the Gaussian class is (cosh^2 r, cosh^2 r, .) and cannot meet Koide with a degenerate light pair except at the fitted depth). Transport-absent in the sense that it uses only the Z/3 Fourier structure of face space and the Gaussian coherent vector.
---

## formal
Let $u' = (1,1,1)$, $f_{\pm} = (1, \zeta^{\pm 1}, \zeta^{\mp 1})$ with $\zeta = e^{2\pi I_4/3}$ (numbers, and the components of face vectors, are read in $\mathrm{span}\{1, I_4\}$, and the bar reverses $I_4$), $C(v) = \sum_{k} v_{k}^{2}$ the bracket form and $P_{s} = \J/3$, $P_{d} = 1 - P_{s}$, as in Proposition \claimref{families.chart-computation-sign-twist-bracket-form}; write $\|v\|^{2} = \sum_{k}|v_{k}|^{2}$. By Proposition \claimref{families.rigidity-pairing-sector-one-event} the coherent face vector of every antisymmetric pairing is
\[
v \;=\; \kappa\,\bigl(u' + w f_{+}\bigr), \qquad w = \lambda e^{I_4\chi},\ \lambda \ge 0,
\]
with $\kappa \neq 0$, and $\kappa \in -I_4\R_{>0}$ when the pairing strength $\tau$ is real. Call a real structure on face space $S_{3}$-equivariant if it is an antilinear involution commuting with the face action $\Omega \mapsto \pm P\Omega$.
\begin{enumerate}
\item[(i)] The $S_{3}$-equivariant real structures are exactly $\sigma_{x,y} = (xP_{s} + yP_{d}) \circ \overline{\phantom{v}}$ with $|x| = |y| = 1$; $\sigma_{x,y}$ is compatible with $C$, $C(\sigma v) = \overline{C(v)}$, exactly when $x, y \in \{\pm 1\}$, and on the fixed slices of $\sigma_{1,-1}$ and $\sigma_{-1,1}$ the form $C$ restricts to $\pm(t^{2} - Q(d))$, the equal-coefficient member of Proposition \claimref{families.koide-nullity-condition-one-member-invariant}.
\item[(ii)] For $\lambda > 0$ no complex multiple of $v$ lies in the fixed slice of any $\sigma_{x,y}$, whatever the channel phase $\chi$: the doublet part of $v$ lies on the $C$-null Fourier line $\mathrm{span}\{1, I_4\}\,f_{+}$, which contains no complex multiple of a real vector.
\item[(iii)] For every $\sigma_{x,y}$ the doublet part $d$ of the projection $\tfrac12(v + \sigma_{x,y}v)$ has $Q(d) = \tfrac12\|P_{d}v\|^{2} = \tfrac32|\kappa|^{2}\lambda^{2}$, independent of $x$, $y$ and $\chi$. For $\kappa \in -I_4\R_{>0}$ the $C$-compatible structures whose slice contains the singlet $\kappa u'$ are $\sigma_{-1,-1}$ (Euclidean) and $\sigma_{-1,1}$ (Lorentzian, $C = -(t^{2} - Q(d))$ on its slice); in the real coordinates of these slices the projected vector is
\[
p_{k} \;=\; |\kappa|\bigl(1 + \lambda\cos(\delta + \tfrac{2\pi k}{3})\bigr), \qquad \delta = \chi \ \ (\sigma_{-1,-1}), \qquad \delta = \chi - \tfrac{\pi}{2}\ \ (\sigma_{-1,1}),
\]
the second with the singlet coordinate oriented by $-I_4 \mapsto +1$; the opposite orientation gives $\chi + \tfrac{\pi}{2}$ up to an overall sign, with the same $Q$.
\item[(iv)] On either projection $Q_{p} = \tfrac13 + \tfrac{\lambda^{2}}{6}$, so the projected vector is null for the equal-coefficient member (the Koide relation $Q = \tfrac23$) if and only if $\lambda^{2} = 2$; equivalently $\|v\|^{2} = 3|C(v)|$; equivalently $|a \cdot a| = \tfrac13|a|^{2}$ for the family vector $a$ of the pairing $[a]_{\times}$; equivalently the Hermitian weights of $v$ on the singlet and the doublet stand in the ratio $1:2$ of their dimensions. At the universal point $\lambda = 1$, $Q_{p} = \tfrac12$.
\end{enumerate}
So on the coherent vector the real-structure question and the Koide number decouple: the choice of structure moves only the phase $\delta$ by a quarter turn (up to the slice's orientation), never $Q$; and if the projected coherent vector is read as the $\sqrt{m}$ vector, the one number of Proposition \claimref{families.chart-computation-sign-twist-bracket-form}(3) becomes the feeding ratio $\lambda^{2} = 2$, which the Gaussian class leaves free.

## technical
The Gaussian freezing gives a definite complex face vector, $v \propto u' + \lambda e^{I_4\chi}f_{+}$ (numbers read in $\mathrm{span}\{1, I_4\}$): a democratic part and a doublet part on one Fourier line, with $\lambda$ the feeding ratio of the two channels and $\chi$ their relative phase. The real structures of face space that respect the permutation symmetry are $(xP_{s} + yP_{d})$ composed with complex conjugation, and those compatible with the bracket form have $x, y = \pm 1$; two of them make the bracket form the Lorentzian member in which Koide is a nullity statement.

The coherent vector never lies on any of these real slices, for any phase or ratio, because its doublet part sits on a null Fourier line that contains no real direction. Projecting onto a slice is possible, and because that line is null, every projection keeps exactly half the doublet's norm. On the two slices that keep the democratic part, the projected vector has Koide ratio $\tfrac13 + \lambda^{2}/6$ and Koide phase $\chi$ or $\chi - \pi/2$. If the projected coherent vector is read as the vector of square-root masses (a reading, distinct from the skeleton theorem's reading of masses from the spectrum of the mass form), the Koide relation is therefore $\lambda^{2} = 2$, a statement about the channel feeding ratio (equivalently $\|v\|^{2} = 3|C(v)|$, or a $1:2$ split of the norm by dimension), and the choice between the Euclidean and Lorentzian slice only shifts the phase by a quarter turn, up to the slice's orientation.

## lay
The families paper writes the three family masses as a vector and notes that the Koide relation says this vector lies on a light cone, if lengths are measured in a particular relativistic way that the framework does not force. A suggestion was that the framework's own vacuum might supply the missing ingredient, a phase that would put the physical vector on that light cone automatically. This result checks the suggestion against the vector the vacuum actually produces and finds that it fails: that vector never lies in any of the allowed real slices. What can be done is to project it onto one, and then every allowed choice gives the same answer for the Koide ratio, so the choice of geometry carries no information about Koide. If that projected vector is taken to be the physical one, which is a reading and not something shown here, the relation turns into a single condition on how strongly the vacuum's two pairing channels are fed: one must be fed twice as strongly as the other, and nothing in the present theory fixes that.

## one-liner
The Gaussian coherent face vector lies on no permutation-equivariant real slice for any channel phase, every slice projection keeps half its doublet norm, and the projected vector satisfies Koide exactly when the channel feeding ratio is $\lambda^{2} = 2$, the choice of slice moving only the Koide phase by a quarter turn (up to orientation).
