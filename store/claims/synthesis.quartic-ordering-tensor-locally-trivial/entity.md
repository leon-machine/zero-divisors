---
id: synthesis.quartic-ordering-tensor-locally-trivial
kind: claim
version: 3
title: 'The quartic ordering tensor is locally trivial'
status: proved
region: synthesis
subject: conformal-spacetime
tags: [no-go]
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
  - correspondence.spin-representation@6
  - correspondence.symmetrised-quadratics-palatial-algebra@5
  - correspondence.ordering-filtration@3
  - correspondence.chirality-split-ordering-insensitivity-asd-sector@6
  - correspondence.chiral-planes-summand-spaces@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_h2_sl4_vanishes
- kind: check
  ref: check.py::check_spin_two_coboundary_in_googly_slot
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - correspondence.googly-localisation-quartic-order
  - note.correspondence.setting-successor-problems
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 2 -> 3.'
  open_problem: op.googly-analytic-half
  note: 'A filter on part (b) of the googly conjecture, not a refutation. If the deformed product closes on the symmetrised quadratics, the quartic ordering tensor is a formal deformation of the bracket of the conformal algebra sl(4), which is rigid (H^2 = 0, computed exactly on the weight-zero Chevalley-Eilenberg complex); so at a point the tensor carries no invariant data and any googly content is a redefinition of which elements count as the generators q(M). A spin-2 redefinition phi supported on the self-dual factor gives a nonzero tensor in the googly slot that passes the anti-self-dual consistency check (its coboundary is not supported on that factor: it also changes brackets with the translations and special conformal generators, though never those of the anti-self-dual factor), so the conjecture is not killed; it must be read globally, as patching data of local redefinitions, as the nonlinear graviton reads anti-self-dual data globally. The rigidity is classical Lie theory (transport-absent); the series content is the ordering filtration and the chirality split it is applied to.'
---

## formal
Let $\mathfrak{s} := \mathfrak{sl}(\CS) \cong \mathfrak{so}(2,4)_\C$ (Proposition \claimref{correspondence.spin-representation}) and $q$ the symmetrised-quadratic map, $[q(M), q(N)] = \hbar\,q([M,N])$ (Proposition \claimref{correspondence.symmetrised-quadratics-palatial-algebra}). Call a formal deformation $\star$ of the palatial product \emph{closed on the quadratics} (hypothesis (CQ)) if $q(M)\star q(N) - q(N)\star q(M) = \hbar\,q(\mu(M,N))$ for $M, N \in \mathfrak{s}$, with $\mu = [\,,\,] + \hbar\mu_{1} + \hbar^{2}\mu_{2} + \cdots$ a formal Lie bracket on $\mathfrak{s}$; $\mu$ is then the quartic ordering tensor of Lemma \claimref{correspondence.ordering-filtration}(2) for the deformed product.
\begin{enumerate}
\item[(i)] \emph{(Rigidity.)} $H^{1}(\mathfrak{s}, \mathfrak{s}) = H^{2}(\mathfrak{s}, \mathfrak{s}) = 0$ for the adjoint representation. Hence under (CQ) there is a formal linear map $\Phi = 1 + \hbar\phi_{1} + \hbar^{2}\phi_{2} + \cdots$ of $\mathfrak{s}$ with $\mu(M,N) = \Phi^{-1}[\Phi M, \Phi N]$, and with the redefined generators $Q := q\circ\Phi^{-1}$ the deformed defect is the undeformed one, $Q(X)\star Q(Y) - Q(Y)\star Q(X) = \hbar\,Q([X,Y])$. At a point, the quartic ordering tensor of a deformation closed on the quadratics carries no data invariant under the choice of generators; whatever it carries is the redefinition $\Phi$.
\item[(ii)] \emph{(A googly redefinition passes the consistency check.)} In a basis adapted to the chiral planes $\CS = \Som \oplus \Spi$ (Lemma \claimref{correspondence.chiral-planes-summand-spaces}), $\mathfrak{g}^{\pm}$ are the two diagonal $\mathfrak{sl}(2)$ blocks. Let $\phi$ be a Killing-symmetric map of $\mathfrak{g}^{+}$ of spin two (a weight-four vector of $\operatorname{End}\mathfrak{g}^{+} = \mathbf{1} \oplus \mathbf{3} \oplus \mathbf{5}$, for instance $f_{+} \mapsto e_{+}$), extended by zero. Then $\mu_{1} := d\phi$, $d\phi(M,N) = [M, \phi N] - [N, \phi M] - \phi[M,N]$, vanishes on $(\mathfrak{g}^{-}, \mathfrak{g}^{-})$ and on $(\mathfrak{g}^{-}, \mathfrak{g}^{+})$, and is nonzero on $(\mathfrak{g}^{+}, \mathfrak{g}^{+})$ with values in $\mathfrak{g}^{+}$. It is not supported on $\mathfrak{g}^{+}$: writing $\mathfrak{p}$ for the nine-dimensional complement of $\mathfrak{g}^{+} \oplus \mathfrak{g}^{-}$ (translations, special conformal maps and the dilatation-type Cartan element), $d\phi$ vanishes on $(\mathfrak{g}^{-}, \mathfrak{p})$ but is nonzero on $(\mathfrak{g}^{+}, \mathfrak{p})$ and on $(\mathfrak{p}, \mathfrak{p})$, so the redefinition also changes brackets with the non-Lorentz generators. So the first-order deformation $[\,,\,] + \hbar\,d\phi$ leaves every anti-self-dual reordering defect as in Proposition \claimref{correspondence.chirality-split-ordering-insensitivity-asd-sector}(2) and puts a spin-two tensor, the shape of a self-dual Weyl spinor, into the googly slot; by (i) it is the redefinition $\Phi = 1 + \hbar\phi$.
\item[(iii)] \emph{(Reading of Conjecture \claimref{correspondence.googly-localisation-quartic-order}(b).)} Under (CQ), part (b) can hold only globally: self-dual data in the quartic ordering tensor is pointwise a redefinition of the generators, so any invariant content lies in the failure of local redefinitions $\Phi_{U}$ to agree on overlaps. Deformations that do not close on the quadratics are not covered.
\end{enumerate}

## technical
Suppose the deformed palatial product keeps the reordering defects of symmetrised quadratics inside the quadratics, so that the quartic ordering tensor is a deformed Lie bracket on the conformal algebra $\mathfrak{sl}(\CS)$. That bracket is rigid: the second cohomology of $\mathfrak{sl}(4)$ with adjoint coefficients vanishes, which the check computes exactly from the Chevalley-Eilenberg complex at torus weight zero (dimensions $3, 21, 87, 273$, ranks $3, 18, 69$). So every such deformation is undone by redefining which elements count as the generators $q(M)$, and the tensor carries no invariant data at a point.

It can still carry googly-shaped data as a redefinition. A spin-two map of the self-dual factor, extended by zero, gives a first-order deformation whose defects vanish on anti-self-dual and mixed Lorentz words and are nonzero, in the googly slot, on self-dual words (it also changes brackets with the non-Lorentz generators, but never those of the anti-self-dual factor): it passes the anti-self-dual consistency check and has the five components of a self-dual Weyl spinor. Under the closure hypothesis, then, the conjecture's part (b) can hold only globally, as the failure of local redefinitions to patch, much as anti-self-dual data lives in the patching of curved twistor space.

## lay
A long-standing problem in twistor theory is where the "right-handed" half of gravitational curvature can be stored. The series conjectures that it sits in a specific place: in how the order of multiplying certain quantum operators matters at fourth order. This result tests that idea in the case where the reordering of those operators stays among the same kind of operators. In that case the relevant algebra is rigid: any small change of it can be undone by relabelling which operators are called the basic ones. So, assuming that closure, the right-handed curvature cannot be stored at any single point in a way that relabelling cannot remove. It can, however, appear there in exactly the right shape and without disturbing the left-handed half, which the result exhibits. So the conjecture survives only in a global form: the information would have to sit in how local relabellings fail to fit together, which is how twistor theory already stores the left-handed half.

## one-liner
If the deformed palatial product closes on the symmetrised quadratics, the quartic ordering tensor is a deformation of the rigid bracket of $\mathfrak{sl}(4)$ ($H^{2} = 0$, computed exactly), so self-dual data there is pointwise a redefinition of the generators; a spin-two redefinition on $\mathfrak{g}^{+}$ passes the anti-self-dual check, and part (b) can hold only as global patching data.
