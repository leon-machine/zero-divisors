---
id: dark-matter.two-families-are-two-chiralities
kind: claim
version: 7
title: The two families are the two chiralities
status: proved
region: dark-matter
subject: clifford-structure
tags:
- witt-index
- spinor-modules
- chirality
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, garbled annihilation identity corrected; which Witt half annihilates said'
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - dark-matter.flag-insensitive-residue-no-flag-level@3
  - primer.twisted-adjoint-action@4
  - std-algebra.witt-basis-car@1
  - std-algebra.witt-extension@2
  - std-algebra.pseudoscalar-commutation@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:families
- kind: check
  ref: check.py::check_pure_spinors_of_witt_pair
- kind: check
  ref: check.py::check_versor_parity_and_chirality
- kind: check
  ref: check.py::check_two_families_and_witt_pair_parity
- kind: check
  ref: check.py::check_odd_dimension_one_family
locators:
  paper: T14
  number: Prop 3.9
  label: prop:families
  line: 245
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6 -> 7. Proof (i): the expression U(Rf) = +-R(Wf)R^{-1}R was garbled; written +-(R W R^{-1})(Rf) = +-R(Wf) = 0. A clause now says that the w_i annihilate and the v_i create here, the reverse of std-algebra.witt-basis-car''s reading, which the cited relation does not depend on. Mathematics unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-basis-car, std-algebra.witt-extension, std-algebra.pseudoscalar-commutation where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: pure spinors of W and W'' are unique lines spanned by f and the top state (dim 2m <= 8); odd versors flip and even versors keep chirality; Witt pair opposite iff m odd; odd dimension one family. Version 2 -> 3. Check strengthened: sample versors asserted invertible with Q pinned, u u^-1 = 1 and chirality +-1 asserted; samples moved to module level. Version 3 -> 4. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: Kept the edge to the flag proposition, which supplies Witt's transitivity; the versor realisation
      of isometries is used but not cited by the source, so not added. The paper calls the general result
      classical (Chevalley), but no imported Chevalley claim is in the store, so no standard-route derivation.
about:
- obj.dark-matter.null-blades-fock-ideal-chirality
---

## formal
In even dimension $2m$:
\begin{enumerate}
\item[(i)] every maximal isotropic $U$ has a pure spinor, unique up to scale, and it is a chirality eigenstate; the pure spinor of $W$ is the null blade $f$ itself, of Fock grade zero, and the pure spinor of $W'$ is the top state $v_{1}\cdots v_{m}f$, of Fock grade $m$;
\item[(ii)] the chirality of $\psi_{U}$ is preserved by even versors (the spin group) and reversed by odd versors (reflections), so the \emph{family} of $U$, defined as the chirality of its pure spinor, is an invariant of the connected isometry group and not of the full one;
\item[(iii)] there are exactly two families, and a Witt pair $W$, $W'$ lies in opposite families if and only if $m$ is odd.
\end{enumerate}
In odd dimension $2m + 1$ there is one family: the connected isometry group acts transitively on maximal isotropic subspaces, and the spin algebra does not preserve the grade parity of $S$.

## technical
Take a complexified ambient of even dimension $2m$ with a Witt pair $W, W'$ of maximal isotropic subspaces, null blade $f$ and the Fock grading of the spinor module. Every maximal isotropic $U$ has a pure spinor $\psi_U$, unique up to scale and an eigenstate of the pseudoscalar $I$: for $W$ it is $f$, of Fock grade $0$, and for $W'$ it is the top state $v_1 \cdots v_m f$, of grade $m$. Even versors preserve chirality and odd versors reverse it, so the family of $U$, the chirality of $\psi_U$, is invariant under the connected isometry group but not the full one.

There are exactly two families, and since grade-$k$ states have chirality proportional to $(-1)^{m-k}$, the Witt pair lies in opposite families if and only if $m$ is odd. In odd dimension $2m+1$ there is one family: the connected group acts transitively on maximal isotropic subspaces and the spin algebra does not preserve Fock grade parity.

## lay
In a space with an even number of complex dimensions, the largest subspaces made entirely of zero-length directions come in two kinds. Each such subspace picks out a special spinor, and the handedness of that spinor decides its kind; rotations keep the kind and reflections swap it. A matched pair of these subspaces is of opposite kinds exactly when half the dimension is odd. In odd dimensions there is only one kind.

## one-liner
In even dimension $2m$ maximal isotropic subspaces fall into exactly two families, labelled by the chirality of their pure spinors, with a Witt pair in opposite families exactly when $m$ is odd; in odd dimension there is one family.
