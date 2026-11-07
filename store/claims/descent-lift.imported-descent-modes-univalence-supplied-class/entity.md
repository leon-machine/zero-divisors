---
id: descent-lift.imported-descent-modes-univalence-supplied-class
kind: claim
version: 8
title: 'Imported: the descent on modes, univalence, and the supplied class'
status: proved
region: descent-lift
subject: descent
tags: [descent-map, univalence, superselection]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - descent-lift.imported-descent-modes-univalence-supplied-class-external@1
  - singularity.class-relative-no-go-no-supplied@3
  - singularity.descent-parity-average@4
  - singularity.envelope-endpoint-why-boundary-mode-locality@7
  - singularity.imported-univalence-superselection-rule@2
  - singularity.l-stabiliser-tangent@6
  - singularity.p-reduced-metric-level-reading-many@6
  - singularity.purity-output-partner-commutant@4
  - singularity.schmidt-forcing-proved-outright@6
  assumes:
  - singularity.l-boundary-mode-locality@2
  - singularity.p-univalence@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_descent_is_parity_average_and_pinching
- kind: check
  ref: check.py::check_even_subalgebra
- kind: check
  ref: check.py::check_supplied_class_is_joint_number_diagonal
- kind: check
  ref: check.py::check_vacuum_stabilisers_and_tangent
- kind: check
  ref: check.py::check_pairing_rotation_witness
- kind: check
  ref: check.py::check_thermofield_marginals_gibbs
locators:
  paper: T05-descent-lift
  number: Fact 1.2
  label: fact:T5
  line: 155
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: parity average and pinching on 1-3 modes, even subalgebra dimensions, the parity monomials spanning the joint-number-diagonal algebra, vacuum stabilisers and the pair-creation tangent (1, 3, 6), the 3/5-4/5 pairing rotor and Gibbs thermofield marginals. Version 5 -> 6. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 6 -> 7. Check strengthened: pairing generator''s commutator with each N_k pinned exactly; sample mode counts moved to module level. Version 7 -> 8.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: STRUCTURE L8
    open_problem: op.small-findings
    note: 'One-liner names the boundary-mode locality premise (L_E) of singularity.l-boundary-mode-locality, not (L), which in T05 is the rate model''s two-sector postulate.'
  env: fact
  context_refs:
  - singularity.descent-parity-average
  - singularity.envelope-endpoint-why-boundary-mode-locality
  - singularity.imported-univalence-superselection-rule
  - singularity.l-stabiliser-tangent
  - singularity.p-reduced-metric-level-reading-many
  - singularity.purity-output-partner-commutant
  - singularity.schmidt-forcing-proved-outright
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - singularity.class-relative-no-go-no-supplied
    note: 'the provenance cites the singularity paper''s supplied-class theorem (its appendix theorem
      on the class-relative no-go), which the extraction missed; added it, and repinned the singularity
      targets to their current versions; every other cited item was already a uses or assumes edge. Levels
      pass: the lay level now names the univalence premise (P) and the locality premise, and the one-liner
      names (L).'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - singularity.l-boundary-mode-locality
---

## formal
On the mode algebra the descent is the parity average $\EN(x) = \tfrac12(x + \sigma x\sigma)$, and on $\nu$ modes the composite of the mode-wise averages is the pinching onto the joint-number-diagonal algebra. Physical states are even (P), which is the univalence superselection rule: coherent superpositions of opposite fermion parity are not observable, and the observable algebra is the even subalgebra. The completion attaches one ladder pair to each point of the exceptional set and supplies, as generators of the boundary-mode dynamics, the parity sections and their products, all joint-number-diagonal; the exclusion of pairing terms is premised. On the Fock space of $\nu \geq 2$ modes the hops and pair annihilations stabilise the vacuum ray and the pair creations span the tangent of its orbit; the rotation $\ket{00} \mapsto \tfrac35\ket{00} + \tfrac45\ket{11}$ is the pairing rotation on one pair that the envelope corollary needs. The thermofield pair $c\ket{00} + s\ket{11}$ with $\tan\theta = s/c = e^{-\omega/2T}$ has both marginals equal to the Gibbs state $\operatorname{diag}(c^{2}, s^{2})$; the sample point $e^{-\omega/T} = \tfrac{9}{16}$ gives $(c, s) = (\tfrac45, \tfrac35)$. \emph{Provenance:} \cite[Thm.~5.7, Prop.~9.6, Prem.~7.8, Fact~7.9, Prem.~7.30, Thm.~C.8, Prop.~13.4, Cor.~11.6, Lem.~7.2, Thm.~7.27]{ButlerT5}; the univalence rule \cite{WWW1952}.

## technical
This collects the singularity paper's results on which the descent-lift note relies. On one mode the descent is the parity average $\EN(x) = \tfrac12(x + \sigma x\sigma)$, and on $\nu$ modes the composite of the mode-wise averages is the pinching onto the joint-number-diagonal algebra. Under the univalence premise (P) physical states are even and the observable algebra is the even subalgebra. Under the boundary-mode locality premise the completion attaches one ladder pair to each point of the exceptional set and supplies as dynamics the parity sections and their products, all joint-number-diagonal, with pairing terms excluded by premise.

On the Fock space of $\nu \geq 2$ modes the hops and pair annihilations stabilise the vacuum ray and the pair creations span the tangent of its orbit; the rotation $\ket{00} \mapsto \tfrac35\ket{00} + \tfrac45\ket{11}$ is the pairing rotation the envelope corollary needs. The thermofield pair $c\ket{00} + s\ket{11}$ with $s/c = e^{-\omega/2T}$ has both marginals equal to the Gibbs state $\operatorname{diag}(c^{2}, s^{2})$, and the sample point $e^{-\omega/T} = \tfrac{9}{16}$ gives $(c, s) = (\tfrac45, \tfrac35)$.

## lay
This entry gathers background results from the earlier black-hole singularity work. Erasing a mode's ladder is the same as averaging over its parity; by the univalence premise (P), physical states are restricted to even fermion parity; and, under the boundary-mode locality premise, the dynamics the framework supplies never creates or destroys pairs of particles, the exclusion of such pairing terms being itself a premise. It also fixes the example used throughout: an entangled pair whose single-mode views are thermal, at amplitudes four fifths and three fifths.

## one-liner
The descent is the parity average and on many modes the joint-number pinching, physical states are even under (P), the supplied dynamics is joint-number-diagonal with pairing excluded by the boundary-mode locality premise (L$_E$), and the thermofield pair has Gibbs marginals.
