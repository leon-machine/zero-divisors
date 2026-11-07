---
id: dark-matter.premise-flag-as-datum
kind: claim
version: 3
title: 'The flag as datum: the sign of the Witt flag is configuration data'
status: postulate
region: dark-matter
subject: dark-matter
tags: [matter-asymmetry, witt-index]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
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
  role: notation pass, imaginary units resolved by the unit principle
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
about:
- obj.dark-matter.witt-flag
- obj.dark-energy.four-ways-number-enters-theory-shape
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. The +i eigenspaces of the complex structure J live on the complexification of R^{2,4}, and the premise compares J with the scalar of the Fock module; that scalar commutes with the vectors, so by U3 it is the central pseudoscalar I_7 = I_6 e of Cl(3,4) = Cl(2,4)_C (std-algebra.complexification-is-the-odd-extension, cited as a mention), as in the T09 Fock-model results: +I_7 eigenspaces, the sign of J relative to I_7. The technical level is written the same way. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the flag is the +i eigenspace of a complex structure J on the complexification of R^{2,4}, and the premise compares J with the scalar i of the Fock module; that scalar commutes with the vectors, which no pseudoscalar does.'
  env: premise (store-named reading)
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'New postulate. The corrected seventeenth refutation (dark-matter.orientation-arrow-seventeenth-refutation v6) and its two T16 restatements (one-relation.imported-flag-arrow-superselection, one-relation.record-chain-votes-measurement-without-collapse) used, as an unnamed "reading", that the Witt flag is a datum of each solution planted by the descent and not part of the kinematic structure. No store entity recorded it, so holds_given did not track it. It is stated here in the form the antilinear realisation of CPT conjugation gives it (synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation): the sign of the flag''s complex structure J relative to the Fock module''s unit i. T14 does not name it as a premise; it is made explicit here because the store''s corrected argument depends on it.'
---

## formal
\emph{The flag as datum.} The descent's flag $W$ (Definition \claimref{obj.dark-matter.witt-flag}) is the $+I_7$ eigenspace of an orthogonal complex structure $J$ on $\R^{2,4}$, extended to $\R^{2,4} \oplus I_7\R^{2,4}$, and its conjugate $\overline W$ is the $+I_7$ eigenspace of $-J$; here $I_7 = I_6e$, the central pseudoscalar of the odd extension $\Cl(3,4) = \Cl(2,4)_{\C}$, is the scalar unit of the complexification and of the Fock module (\claimref{std-algebra.complexification-is-the-odd-extension}), and $J$ is a map on vectors, not an element identified with it (\claimref{synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation}, clause (2)). The premise: the sign of $J$ relative to the unit $I_7$ of the Fock module is configuration data of each solution, planted by the descent, and not part of the kinematic structure. That is, in the terms of Definition \claimref{obj.dark-energy.four-ways-number-enters-theory-shape}, a configuration $x$ and the configuration with the opposite sign of $J$ have isomorphic kinematic structures and lie in the configuration space of the same family of action functionals $S_{\mu}$; the orientation bit $q(x) = \pm 1$ is a function of the configuration, not of the theory.

\emph{What it is for.} With CPT covariance (\claimref{dark-matter.premise-cpt-covariance}), whose conjugation exchanges the two signs, it places the orientation bit in clause (I) of the Definition, taking both values on every nonempty solution space, rather than in (K) or (D). It is used by \claimref{dark-matter.orientation-arrow-seventeenth-refutation} and its restatements \claimref{one-relation.imported-flag-arrow-superselection} and \claimref{one-relation.record-chain-votes-measurement-without-collapse}. Without it the conclusion fails in the way those results state: were the sign kinematic, the bit would be constant on every solution space of the theory carrying it, and the two orientations would be two isomorphic theories rather than two solutions of one.

\emph{What would refute it.} A structure of the framework, or a term of one of its action functionals, that distinguishes $J$ from $-J$ relative to the Fock module's $I_7$ and is fixed by the descent's kinematics rather than chosen by a solution: for example a proof that the pairing on the Fock module, the completion or the frozen point's data carry a preferred sign of $J$. Such a result would make the orientation bit kinematic or dynamically fixed. No observation tests the premise directly; it is a modelling choice about where the bit lives.

## technical
The descent's Witt flag can be described as a choice of orthogonal complex structure $J$ on the six-dimensional conformal ambient: the flag is the $+I_7$ eigenspace of $J$, and the conjugate flag, in the other family, is the $+I_7$ eigenspace of $-J$, with $I_7$ the scalar unit of the complexification, the central pseudoscalar of $\Cl(3,4)$. The orientation bit is then the sign of $J$ relative to the imaginary unit of the Fock module on which the modes act.

The premise is that this sign belongs to each solution, planted once by the descent, and is not part of the kinematic structure of the theory. Two configurations differing only in that sign are kinematically isomorphic and are configurations of the same theory. CPT conjugation, which acts antilinearly and exchanges the two signs, then carries every solution to a solution of the same theory with the opposite bit, so the bit is initial data. This is what the seventeenth refutation and its two restatements in the one-relation paper need; if the sign were kinematic, each orientation would define its own theory, the bit would be fixed within each, and their conclusion would fail. The premise would be refuted by a structure or law of the framework that singles out one sign of $J$ from the kinematics alone. It is a modelling choice, not tested by any observation directly.

## lay
The framework's origin event makes one yes-or-no choice, which fixes both which of matter and antimatter is which and the direction of time. This assumption says where that choice lives: it is a fact about our particular universe, set when the universe began, not a built-in feature of the theory's laws or structure. A different universe obeying the same laws could have made the opposite choice. Several results, including the claim that the choice is a starting condition rather than a setting of the laws, rest on this assumption. It would be shown wrong if some part of the theory's fixed structure were found to prefer one answer.

## one-liner
Premise: the sign of the Witt flag's complex structure relative to the Fock module's unit is configuration data of each solution, planted by the descent, not part of the kinematic structure.
