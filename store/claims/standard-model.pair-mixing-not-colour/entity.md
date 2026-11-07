---
id: standard-model.pair-mixing-not-colour
kind: claim
version: 4
title: The pair mixing is not colour
status: proved
region: standard-model
subject: standard-model
tags: [gauge-fields, pairing-and-bogoliubov]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.connection-forced@5
  - standard-model.imported-maximal-compact-subgroups@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pair_mixing_is_compact_and_outside_the_real_form
- kind: check
  ref: check.py::check_commutant_is_two_dimensional
- kind: check
  ref: check.py::check_colour_on_the_label_copy_commutes
locators:
  paper: T12
  number: Prop 9.20
  label: prop:notcolour
  line: 1673
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: u(3) compact of dimension 9 against the 7-dimensional compact part of so(2,4) and outside its real span, the commutant C + C of so(2,4) on Lambda(W), and colour on the label copy commuting. Version 2 -> 3. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 3 -> 4.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the twistor, its Fock space, the twistor bundle and the halves T, T'' to the conformal spinor, its Fock space, the conformal spinor bundle and S, S'' at every level and in the proof. The complexified conformal algebra so(6,C) and the complex commutant C (+) C are kept; on S the commutant''s complex unit is I6 (E1.3d), consistent with the statement.'
  source_title: |-
    The pair mixing is not colour
  source_formal: |-
    Let $U(3)$ be the pair mixing of $W$, the unitary group of the Fock structure $v_{i}^{*} = w_{i}$ on the twistor's own three modes. Then:
    \begin{enumerate}
    \item[(i)] $U(3)$ is not a subgroup of the conformal group $SO_{0}(2,4) \cong SU(2,2)/\mathbb{Z}_{2}$: it is compact of dimension $9$, and the maximal compact subgroup has dimension $7$ (Fact \claimref{standard-model.imported-maximal-compact-subgroups}). Its Lie algebra does lie in the complexified conformal algebra $\so(6, \C) = \Lambda^{2}V_{\C}$, its generators $v_{i}w_{j}$ being bivectors, so the statement is one about real forms: $\uu(3)$ is a compact subalgebra of $\so(6,\C)$ that no conjugate of $\so(2,4)$ contains.
    \item[(ii)] $U(3)$ is not an internal symmetry either: the commutant of $\so(2,4)$ acting on $\Lambda^{\bullet}W$ is two-dimensional, the scalars on $\T$ and on $\T'$, so no non-scalar operator on the twistor's Fock space, and in particular no element of $\uu(3)$, commutes with the conformal algebra.
    \item[(iii)] Consequently the $U(3)$ of Proposition \claimref{standard-model.frozen-point-pair-mixing} is a Bogoliubov relabelling of the Fock presentation, a change of which twistor is called the vacuum, and its failure to fix the frozen point says that rotating a twistor into a different twistor changes the momentum, which is true and harmless. The colour group of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} acts on the hierarchy bundle $\mathcal{H}$, a label copy of the pair space carried alongside the twistor bundle, commuting with the conformal connection by construction (Proposition \claimref{standard-model.connection-forced}); the frozen point is insensitive to it. The sentence ``mass breaks colour'' identifies the two copies of $\C^{3}$, the twistor's own annihilator and its label, and is a category error rather than a result. Theorems \claimref{standard-model.moment-map-grip-mass-are-insensitive} and \claimref{standard-model.grip-mass-two-rung-module} need neither identification: their proofs use the slot count and the nullity of a single twistor's momentum, and nothing about the pair mixing.
    \end{enumerate}
  env: proposition
  context_refs:
  - standard-model.frozen-point-pair-mixing
  - standard-model.gauge-algebra-minimal-massive-composite
  - standard-model.grip-mass-two-rung-module
  - standard-model.moment-map-grip-mass-are-insensitive
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.module-factorises-even-ground-elements-act
    - standard-model.imported-grip-area-casimir-form
    note: 'Removed the module-factorisation and grip Facts: the proof cites them only to report what the
      proofs of other theorems invoke, which is not a premise of this claim; kept the maximal-compact
      Fact and the forced connection.'
---

## formal
Let $U(3)$ be the pair mixing of $W$, the unitary group of the Fock structure $v_{i}^{*} = w_{i}$ on the conformal spinor's (twistor's) own three modes. Then:
\begin{enumerate}
\item[(i)] $U(3)$ is not a subgroup of the conformal group $SO_{0}(2,4) \cong SU(2,2)/\mathbb{Z}_{2}$: it is compact of dimension $9$, and the maximal compact subgroup has dimension $7$ (Fact \claimref{standard-model.imported-maximal-compact-subgroups}). Its Lie algebra does lie in the complexified conformal algebra $\so(6, \C) = \Lambda^{2}V_{\C}$, its generators $v_{i}w_{j}$ being bivectors, so the statement is one about real forms: $\uu(3)$ is a compact subalgebra of $\so(6,\C)$ that no conjugate of $\so(2,4)$ contains.
\item[(ii)] $U(3)$ is not an internal symmetry either: the commutant of $\so(2,4)$ acting on $\Lambda^{\bullet}W$ is two-dimensional, the scalars on $\CS = \Lambda^{\mathrm{even}}W$, the conformal spinor space, and on $\CSm{} = \Lambda^{\mathrm{odd}}W$, so no non-scalar operator on the conformal spinor's Fock space, and in particular no element of $\uu(3)$, commutes with the conformal algebra.
\item[(iii)] Consequently the $U(3)$ of Proposition \claimref{standard-model.frozen-point-pair-mixing} is a Bogoliubov relabelling of the Fock presentation, a change of which conformal spinor is called the vacuum, and its failure to fix the frozen point says that rotating a conformal spinor into a different one changes the momentum, which is true and harmless. The colour group of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} acts on the hierarchy bundle $\mathcal{H}$, a label copy of the pair space carried alongside the conformal spinor bundle (the twistor bundle), commuting with the conformal connection by construction (Proposition \claimref{standard-model.connection-forced}); the frozen point is insensitive to it. The sentence ``mass breaks colour'' identifies the two copies of $\C^{3}$, the conformal spinor's own annihilator and its label, and is a category error rather than a result. Theorems \claimref{standard-model.moment-map-grip-mass-are-insensitive} and \claimref{standard-model.grip-mass-two-rung-module} need neither identification: their proofs use the slot count and the nullity of a single conformal spinor's momentum, and nothing about the pair mixing.
\end{enumerate}

## technical
The pair mixing $U(3)$ is the unitary group of the Fock structure $v_{i}^{*} = w_{i}$ on a conformal spinor's own three modes. It is compact of dimension $9$, while the maximal compact subgroup of $SO_{0}(2,4)$ has dimension $7$, so it is not a subgroup of the conformal group; its generators $v_{i}w_{j}$ are bivectors and lie in $\so(6,\C)$, so the statement concerns real forms. Nor is it an internal symmetry: the commutant of $\so(2,4)$ on $\Lambda^{\bullet}W$ is two-dimensional, the scalars on $\CS$ and on $\CSm{}$, so no element of $\uu(3)$ commutes with the conformal algebra.

Hence the pair mixing is a Bogoliubov relabelling of which conformal spinor is called the vacuum. Colour acts on a separate label copy of the pair space carried by the hierarchy bundle, commuting with the conformal connection, so reading ``mass breaks colour'' off the pair mixing identifies two different copies of $\C^{3}$ and is a category error.

## lay
A basic spinor state of the conformal algebra has three internal modes that can be rotated into one another, and so does the colour label of a quark, which invites the idea that the two are the same and that mass breaks colour. This result shows that they are different. Rotating that state's own modes is neither a spacetime symmetry nor an internal symmetry; it only relabels which state counts as empty. Colour acts on a separate copy carried alongside, so the worry comes from confusing the two copies.

## one-liner
The $U(3)$ mixing a conformal spinor's own three pair modes is neither a subgroup of the conformal group nor an internal symmetry, so it is a Bogoliubov relabelling and not colour.
