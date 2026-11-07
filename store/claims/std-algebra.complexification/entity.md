---
id: std-algebra.complexification
kind: claim
version: 3
title: Complexification, and the odd-dimensional split
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- clifford-classification
- pseudoscalar-and-centre
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
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
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
- obj.std-algebra.even-subalgebra
derivations:
- name: main
  uses:
  - std-algebra.tensor-rules@1
  - std-algebra.periodicity@2
  - std-algebra.z2-grading@1
  - primer.centre@2
  - primer.sign@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_complex_forms
- kind: check
  ref: check.py::check_odd_dimension_split
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
  - key: Lam2005
    locator: 'Ch. V (Clifford algebras: the tensor product rules)'
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle the abstract complex field of the tensor product is read as span{1, I_4} (U1), its unit in the second factor: epsilon_i = e_i (x) I_4 in the proof and x + y I_4 in (ii); the formal level says once that for even n the complexification is the odd extension with central unit I_V e (U3, std-algebra.complexification-is-the-odd-extension) and that in (ii) the unit is omega, the units related by isomorphisms and not identified; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the complexification Cl(V) (x) C is the subject, and its scalar i (epsilon_i = i e_i) commutes with every vector, which no pseudoscalar does; where omega squares to -1 the result already names omega as the imaginary unit.'
  referee_fixes: '2026-10-26: (ii) fixes omega = e_1...e_n for an orthonormal basis, so omega^2 = +-1 exactly (referee part 1, point 4).'
  by: algebra-core-2026-10-26
---

## formal
The complex field is read as $\mathrm{span}\{1, I_4\}$ (conventions, the unit principle, U1), its unit standing in the second tensor factor of $\Cl(V, Q) \otimes_\R \C$, central by construction; for even $n$ the complexification is realised inside a real Clifford algebra as the odd extension, with unit the central pseudoscalar $I_V e$ (\claimref{std-algebra.complexification-is-the-odd-extension}), and in (ii) for odd $n$ with $\omega^{2} = -1$ the unit is $\omega$; these units are related by isomorphisms, not identified.
\begin{enumerate}
\item[(i)] For nondegenerate $V$ of dimension $n$, $\Cl(V, Q) \otimes_\R \C \cong \Cl_n(\C)$, the Clifford algebra of $\C^{n}$ with $Q(z) = \sum z_i^{2}$; it depends only on $n$. $\Cl_n(\C) \cong \Mat_{2^{n/2}}(\C)$ for $n$ even and $\Cl_n(\C) \cong \Mat_{2^{(n-1)/2}}(\C) \oplus \Mat_{2^{(n-1)/2}}(\C)$ for $n$ odd.
\item[(ii)] Let $n$ be odd, $V$ nondegenerate, and $\omega = e_1 \cdots e_n$ for an orthonormal basis ($Q(e_i) = \pm 1$), so that $\omega^{2} = \pm 1$. Then $\omega$ is central and invertible, $\Cl^{-} = \Cl^{+}\omega$, and
\begin{itemize}
\item if $\omega^{2} = 1$, the central idempotents $P_{\pm} = \tfrac12(1 \pm \omega)$ split $\Cl(V) = \Cl(V) P_+ \oplus \Cl(V) P_-$, and $a \mapsto a P_{\pm}$ is an isomorphism $\Cl^{+} \to \Cl(V) P_{\pm}$, so $\Cl(V) \cong \Cl^{+} \oplus \Cl^{+}$;
\item if $\omega^{2} = -1$, $a \otimes (x + yI_4) \mapsto a(x + y\omega)$ is an isomorphism $\Cl^{+} \otimes_\R \C \to \Cl(V)$, with $\omega$ as the imaginary unit.
\end{itemize}
\end{enumerate}

## technical
Over the complex numbers the sign of a generator's square can be changed by multiplying it by the complex unit, so every complexified real Clifford algebra of dimension $n$ is the same algebra, a full complex matrix algebra for even $n$ and a sum of two for odd $n$. For odd $n$ over the reals, the pseudoscalar is central: when it squares to $+1$ it splits the algebra into two copies of the even subalgebra, and when it squares to $-1$ it serves as an imaginary unit that makes the algebra the complexification of the even subalgebra.

## lay
With complex numbers allowed, the difference between space-like and time-like directions disappears and only the number of dimensions matters. In an odd number of real dimensions the volume element either splits the algebra into two identical halves or acts like the square root of minus one.

## one-liner
$\Cl(V) \otimes \C \cong \Cl_n(\C)$, a complex matrix algebra (doubled for odd $n$); for odd $n$, $\Cl \cong \Cl^{+} \oplus \Cl^{+}$ if $\omega^{2} = 1$ and $\Cl \cong \Cl^{+} \otimes \C$ if $\omega^{2} = -1$.
