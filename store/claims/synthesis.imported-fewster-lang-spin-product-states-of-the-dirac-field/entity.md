---
id: synthesis.imported-fewster-lang-spin-product-states-of-the-dirac-field
kind: claim
version: 1
title: 'Imported: spin-product states of the Dirac field (Fewster and Lang 2015)'
status: imported
region: synthesis
subject: quantum-fields
tags: [car-algebra, pairing-and-bogoliubov, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-02
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'C. J. Fewster and B. Lang, Pure quasifree states of the Dirac field from the fermionic projector, Class. Quantum Grav. 32 (2015), 095001; arXiv:1408.1645.'
  key: FewsterLang2015
  locator: 'Sec. 3: the state from the positive spectral projection of the weighted spacetime spin product; Thm. 3.4 (the unsoftened state is not Hadamard for generic lifetimes); Thm. 3.5 (softened states are Hadamard)'
  doi: 10.1088/0264-9381/32/9/095001
- citation: 'F. Finster and M. Reintjes, A non-perturbative construction of the fermionic projector on globally hyperbolic manifolds I: space-times of finite lifetime, Adv. Theor. Math. Phys. 19 (2015), 761--803; arXiv:1301.5420.'
  key: FinsterReintjes2015
extraction:
  note: >-
    Imported so that the result on the massless spin-product state can pin the Fewster-Lang construction and
    its Hadamard theorems instead of citing them. Checked on 2 November 2026 against the arXiv abstract page of
    arXiv:1408.1645: title, authors, DOI 10.1088/0264-9381/32/9/095001 (Class. Quantum Grav. 32, 095001), and
    the content: the quantised free Dirac field on oriented, globally hyperbolic, ultrastatic slab spacetimes
    with compact spatial sections; a gauge-invariant pure quasi-free state extracted from the fermionic
    projector construction of Finster and Reintjes, analogous to the Sorkin-Johnston state of the scalar field;
    the state generically fails to be Hadamard; a modified construction inspired by Brum and Fredenhagen (the
    softened states) gives Hadamard states; the Hadamard condition is related to finite fluctuations of Wick
    polynomials. The introduction (read in the ar5iv text) states that the softened state uses a smooth,
    compactly supported, nonnegative weight and that all softened states are Hadamard. The theorem numbers
    (3.4, 3.5), the assumption m > 0 and the mode formula cos 2 theta = f^(0) m/(lambda Xi) are as stated in the
    citing result and were not rechecked here (the extracted text ended in Section 2). The Finster-Reintjes
    bibliographic data are from memory.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Created by the maintainer pass of 2 November 2026, by Leon''s list of routine imports (Fewster-Lang 2015), for the result on the spin-product state of the massless Dirac field.'
  flags:
  - 'beyond one flat chart: the compact spatial sections of the ultrastatic slab'
---

## formal
Let a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) have an ultrastatic derived metric on a slab, the product of a time interval $(-T/2, T/2)$ with a compact spatial section $\Sigma$, oriented and globally hyperbolic, and consider the quantised free Dirac field of mass $m$ on it. Weight the spacetime spin product $\int\bar{\psi}\phi$ of two solutions by a nonnegative integrable function $f$ of time; on the space of solutions with the conserved-current inner product it is represented by a bounded self-adjoint operator, and the positive spectral projection of that operator defines a gauge-invariant, pure, quasi-free state, the state extracted from the fermionic projector of Finster and Reintjes \cite{FinsterReintjes2015}, the Dirac analogue of the Sorkin-Johnston state of a scalar field \cite{FewsterLang2015}.
\begin{enumerate}
\item[(i)] For the sharp weight, $f$ the indicator function of the slab, the state fails to be Hadamard for generic lifetimes $T$ (\cite{FewsterLang2015}, Thm.~3.4).
\item[(ii)] For $f$ smooth, compactly supported in the slab, nonnegative and not identically zero, the resulting softened state is Hadamard (\cite{FewsterLang2015}, Thm.~3.5).
\item[(iii)] The Hadamard condition of these states is tied to the finiteness of the fluctuations of Wick polynomials \cite{FewsterLang2015}.
\end{enumerate}
\emph{Beyond one flat chart:} the compactness of the spatial section $\Sigma$ is a global ingredient of the setting of the theorems.

## technical
On a short stretch of time, a slab, one can build a state of the Dirac field from the field alone: weight the spin product of two solutions over spacetime, compare it with the conserved charge product, and keep the positive part. Fewster and Lang showed that this state, the finite-time form of Finster and Reintjes's fermionic projector and the Dirac analogue of the Sorkin-Johnston state, is pure and quasi-free, but on an ultrastatic slab with compact spatial sections it is generically not Hadamard if the weight is sharp in time; softened with a smooth weight that vanishes near the ends of the slab, it is Hadamard.

## lay
A natural way to pick out a quantum state of the electron field, using only the field's own structure over a finite stretch of time, gives a state that is too rough at short distances when the stretch has sharp ends. Fewster and Lang proved this, and showed that smoothing the ends repairs it. The series uses their result when testing whether that construction could select the state left behind by the descent.

## one-liner
On an ultrastatic slab with compact sections the Dirac state from the positive part of the weighted spin product (the fermionic projector state) is pure and quasi-free, generically not Hadamard with a sharp time weight, and Hadamard with a smooth compactly supported weight (Fewster-Lang 2015, Thms 3.4, 3.5).
