---
id: dark-matter.imported-inputs-standard-model-chain
kind: claim
version: 6
title: 'Imported: the inputs of the Standard-Model chain'
status: proved
region: dark-matter
subject: standard-model
tags: [ledger-audit]
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
review: typed
about:
- obj.dark-matter.null-blades-fock-ideal-chirality
derivations:
- name: main
  uses:
  - mass.mass-symplectic-area-two-twistor-formula@3
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:fact:sminputs
- kind: check
  ref: check.py::check_even_subalgebra_is_mat4_c
- kind: check
  ref: check.py::check_helicity_form_lives_on_the_twistor_ideal
- kind: check
  ref: check.py::check_mass_formula_identity
- kind: check
  ref: check.py::check_fock_module_is_irreducible_spinor_module
locators:
  paper: T14
  number: Fact 4.2
  label: fact:sminputs
  line: 321
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: computable inputs only: Cl^0(2,4) = Cl(2,3) = Mat(4,C) over I6, the helicity form on Cl^0 f against the null-blade Fock ideal, the mass identity det p = |<pi1 pi2>|^2, and the three-mode Fock module. Version 5 -> 6.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the twistor space to the conformal spinor space S = Cl^0(2,4) f and named the complex unit of Mat(4,C) as the central I6 (E1.2, E1.3c), at every level and in the provenance proof. The complexification V_C of input (b) is kept: it is the Fock structure''s, whose complex unit must commute with vectors, which I6 does not.'
  source_title: |-
    Imported: the inputs of the Standard-Model chain
  source_formal: |-
    The derivation of the Standard-Model paper's Sections 3 to 5 uses these data and nothing else: (a) the conformal completion $\Cl(2,4)$ soldered to $V = \R^{2,4}$; (b) the complexification $V_{\C}$, its maximal isotropic subspaces and null blades (the pair count), pair systems and chirality halves (Definition \claimref{obj.dark-matter.null-blades-fock-ideal-chirality}); (c) the even subalgebra $\Cl^{0}(2,4) \cong \Cl(2,3) \cong \Mat(4,\C)$, its spin group $SU(2,2)$, and the twistor space as the ideal $\Cl^{0}(2,4)\,f$ of a self-reverse primitive idempotent, with the helicity form $\bar{\psi}\varphi$ built from the ambient reversion (Clifford conjugation of $\Cl(2,3)$; read on this ideal, not on the null-blade Fock ideal, where at $m = 3$ it vanishes); (d) the mass formula $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$; (e) the Segre lemma and hypercharge by pair counting; (f) Hypothesis (S) (Fact \claimref{dark-matter.imported-derived-generation-flag}); (g) signature-free imports: the Cauchy decomposition, the anomaly coefficients, the Fock representation with its Bogoliubov group; (h) the tractor bundle, whose fibre is the completion's spinor space; (i) the two-kinds-of-action fact (MacDowell-Mansouri does not reach the internal factors, which enter through Yang-Mills functionals whose four-dimensional Hodge star depends on the conformal class alone, the $\theta$-terms being the singularity-surviving remainder); (j) one-loop running, in a conditional remark. \emph{Provenance:} \cite[\S\S2-5]{ButlerT12}, Facts 2.1 to 2.11 and Hypothesis (S); the list is this paper's reading, carried as a hypothesis.
  typing:
    by: ai-typing-pass
    note: 'Kept the restated mass-formula and Fock-representation imports; the in-paper Fact named in
      item (f) and in context_refs only points to where Hypothesis (S) is printed, and the claim is a
      reading carried as a hypothesis, so it was not added as a premise. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: conditions already kept; the
      lay level now names Hypothesis (S) by its label.'
    added:
    - standard-model.hyp-s-slot-statistics
  env: fact
  context_refs:
  - dark-matter.imported-derived-generation-flag
  - mass.mass-symplectic-area-two-twistor-formula
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov
  flags:
  - 'fact restating several series results: derived from them'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The derivation of the Standard-Model paper's Sections 3 to 5 uses these data and nothing else: (a) the conformal completion $\Cl(2,4)$ soldered to $V = \R^{2,4}$; (b) the complexification $V_{\C}$, its maximal isotropic subspaces and null blades (the pair count), pair systems and chirality halves (Definition \claimref{obj.dark-matter.null-blades-fock-ideal-chirality}); (c) the even subalgebra $\Cl^{0}(2,4) \cong \Cl(2,3) \cong \Mat(4,\C)$, complex over its central unit $I_6$, its spin group $SU(2,2)$, and the conformal spinor space (twistor space) as the ideal $\CS = \Cl^{0}(2,4)\,f$ of a self-reverse primitive idempotent, with the helicity form $\bar{\psi}\varphi$ built from the ambient reversion (Clifford conjugation of $\Cl(2,3)$; read on this ideal, not on the null-blade Fock ideal, where at $m = 3$ it vanishes); (d) the mass formula $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$; (e) the Segre lemma and hypercharge by pair counting; (f) Hypothesis (S) (Fact \claimref{dark-matter.imported-derived-generation-flag}); (g) signature-free imports: the Cauchy decomposition, the anomaly coefficients, the Fock representation with its Bogoliubov group; (h) the tractor bundle, whose fibre is the completion's spinor space; (i) the two-kinds-of-action fact (MacDowell-Mansouri does not reach the internal factors, which enter through Yang-Mills functionals whose four-dimensional Hodge star depends on the conformal class alone, the $\theta$-terms being the singularity-surviving remainder); (j) one-loop running, in a conditional remark. \emph{Provenance:} \cite[\S\S2-5]{ButlerT12}, Facts 2.1 to 2.11 and Hypothesis (S); the list is this paper's reading, carried as a hypothesis.

## technical
The dark-matter paper reads the Standard-Model chain as resting on a fixed list of inputs: the conformal completion $\Cl(2,4)$ soldered to $V = \R^{2,4}$; the complexification $V_{\C}$ with its maximal isotropic subspaces, null blades, pair systems and chirality halves; the even subalgebra $\Cl^{0}(2,4) \cong \Cl(2,3) \cong \Mat(4,\C)$, complex over its central unit $I_6$, its spin group $SU(2,2)$, and the conformal spinor space as the ideal $\CS = \Cl^{0}(2,4)\,f$ with the helicity form built from the ambient reversion; the mass formula $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$; the Segre lemma and hypercharge by pair counting; Hypothesis (S); the signature-free imports (the Cauchy decomposition, the anomaly coefficients, the Fock representation with its Bogoliubov group); the tractor bundle; the two-kinds-of-action fact; and one-loop running, in a conditional remark.

The claim is that these data and nothing else are used. The list is the dark-matter paper's reading of that chain, carried as a hypothesis.

## lay
The Standard-Model results of the series come from a chain of derivations. This entry lists every ingredient that chain uses, from the six-dimensional conformal geometry and its spinors to the mass formula, a counting rule for hypercharge, one structural hypothesis about the slots of the composite's spinor states (Hypothesis (S)) and a few textbook results. The point is that nothing else goes in, so later work can ask which ingredients survive in other settings. That the list is complete is a reading, carried as an assumption.

## one-liner
The Standard-Model chain of the series uses exactly a stated list of inputs, from the conformal completion and its conformal spinor ideal to the mass formula, pair-counting hypercharge, Hypothesis (S) and signature-free imports, a list carried as a hypothesis.
