---
id: dark-matter.premise-cpt-covariance
kind: claim
version: 3
title: 'CPT covariance of the kinematic structures and of every action'
status: postulate
region: dark-matter
subject: dark-matter
tags: [matter-asymmetry, witt-index]
proposed_by:
  kind: ai
  session: decision-pass-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Leon Butler
  role: decision to restate the relation to the CPT operator of quantum field theory
  version: 3
- name: Claude Opus 5.5
  role: drafting of the restated sentence
  version: 3
  source: maintainer pass 2026-11-07
review: typed
locators:
  paper: T14
  number: Prop 5.2 (first premise)
  label: prop:orientation
  line: 519
about:
- obj.dark-matter.witt-flag
- obj.dark-energy.four-ways-number-enters-theory-shape
extraction:
  maintainer_pass_cpt_sentence:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Leon''s decision of 7 November: the sentence saying the conjugation realising the CPT operator of quantum field theory is argued is restated; the conjugation fixes every conformal generator and is antilinear, so it reverses the energy and is not that operator; the covariance clause itself is unchanged.'
  env: premise named in a proposition
  also_stated:
  - 'T14 proof of Prop 5.2: "the gauge sector''s CPT-evenness is imported and carried as a premise", line 529'
  - 'T15 Fact 2.5: "with the gauge sector''s CPT-evenness as a premise there"'
  - 'T16 Fact 2.5 and T17 refutation 17: "CPT covariance of the derived gauge sector"'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: New postulate. The seventeenth refutation and its restatements name CPT covariance as their first premise, but the store had no entity for it, so it never reached holds_given (CONTRADICTIONS_VALUES M3). The formal level is the premise in the paper's words; what the proof checks rather than premises is kept as the paper states it.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 2 rewords the premise per synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation and states the action clause at the strength the store uses it: the composite is an anti-automorphism, under the stated field-action convention it acts on fields as C = Ad(I6) composed with complex conjugation, so it is antilinear (Wigner type, argued) rather than "a real linear Z2 automorphism"; and the action clause now reads S o C = S for every action functional of the four-ways definition with its parameters, gauge couplings included, the clause the seventeenth refutation and the two T16 restatements rely on. This departs from T14''s wording, which describes the conjugation as real linear and states the action clause only in words.'
  locator_divergence: 'T14 Prop 5.2 describes CPT conjugation as a real linear Z2 automorphism of the kinematic data and its action clause in words. This store version states the conjugation as an antilinear anti-automorphism under an explicit field-action convention, and the action clause as invariance of every action functional and its parameters, gauge couplings included.'
---

## formal
\emph{CPT covariance.} CPT conjugation is an isomorphism of every kinematic structure and leaves every action functional invariant (T14, Proposition 5.2, its first premise: ``checked in the proof for the metric, the completion, the pairing and the action; premised for the imported gauge sector and for structures later papers add'').

\emph{The conjugation.} CPT conjugation $\phi$ is the composite of grade involution, reversal and the flag conjugate exchanging the two families of maximal isotropic subspaces (Definition \claimref{obj.dark-matter.witt-flag}). Because of the reversal, $\phi$ is an anti-automorphism of the Clifford algebra.

\emph{Convention (field action).} $\phi$ acts on fields as a symmetry: on a vector field by its vector part, and on a connection $A$ through the Lie algebra automorphism it induces, $A \mapsto -\phi(A)$, so that curvature is carried by that automorphism. In this convention $\phi$ acts on fields as $C = \mathrm{Ad}(I_{6}) \circ \kappa$, with $\kappa$ complex conjugation on $\Cl(2,4) \otimes \C$: its vector part $-1$ is the rotor $I_{6}$ of the identity component, and the flag conjugate that preserves the frozen point's action is complex conjugation, a real-linear one reversing that action (\claimref{synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation}). So CPT conjugation is antilinear on the complexified ambient and on the Fock module, of Wigner's antiunitary type (argued there, not proved).

\emph{Action clause.} For every action functional $S_{\mu}$ of Definition \claimref{obj.dark-energy.four-ways-number-enters-theory-shape}, the gauge couplings among its parameters $\mu$ included, $S_{\mu} \circ C = S_{\mu}$; in particular $C$ does not move $\mu$.

\emph{What is checked and what is premised.} Checked: the fibre metric, the completion, the pairing on the Fock module, and the frozen point's action, which with every functional of real tensor fields invariant under constant $SO_{0}(2,4)$ satisfies the action clause in this convention by the cited result's clause (5). Premised: the imported gauge sector, spinor and fermion fields, and structures later papers add. For the gauge sector the standard CPT theorem for local Lorentz-invariant actions concerns the antiunitary CPT operator of quantum field theory, and this conjugation is not that operator (argued): it fixes every bivector of $\Cl(2,4)$ ($I_{6}$ commutes with the even algebra), so every conformal generator and in particular every translation, and it is antilinear, so on a Hilbert space that carries the translations it reverses their generator and with it the energy, whereas the CPT operator of quantum field theory reverses the translations and keeps the energy positive. The gauge sector's invariance under this conjugation is therefore not supplied by the CPT theorem; it ``is imported and carried as a premise''.

## technical
The premise is that CPT conjugation, the composite of grade involution, reversal and the flag conjugate on each tower's Clifford bundle, is an isomorphism of every kinematic structure of the framework and leaves every action functional, together with the values of its parameters, unchanged. The gauge couplings are among those parameters, so the clause is that conjugation maps every theory of the family onto itself, not merely that it fixes the frozen point's action.

The convention is stated because the composite is an anti-automorphism (reversal reverses products), and an anti-automorphism can be made to act on an action in more than one way. Here it acts as a symmetry acts on fields: vectors by its vector part, connections through the Lie algebra automorphism it induces, so curvature is fixed. In that convention the composite acts on fields as the pseudoscalar rotor $I_{6}$, a rotation of the identity component, followed by complex conjugation, and the flag conjugate compatible with an invariant action has to be complex conjugation. So the conjugation is antilinear, the type of Wigner's antiunitary symmetries, not the real linear map the dark-matter paper's wording describes.

The paper checks the premise for the fibre metric, the completion's hyperbolic plane, the pairing on the Fock module and the frozen point's action; in the convention the action clause also holds for every functional of real tensor fields invariant under constant conformal rotations. For the imported gauge sector, spinor and fermion fields, and any structure a later paper adds, it is assumed. Under it, anything the structures and laws determine is conjugation-invariant, which is the first step of the argument that the particle-antiparticle orientation is not determined by them.

## lay
This is an assumption, partly checked: a particular symmetry that swaps matter with antimatter, reverses time and mirrors space is taken to leave every basic structure of the framework, and every one of its laws including the strengths of the forces, unchanged. Worked out exactly, the symmetry involves complex conjugation, the same kind of operation quantum field theory uses for this symmetry, rather than an ordinary linear swap. The series verifies the assumption for the geometric structures and for gravity, and assumes it for the imported description of the forces and of matter. It is the first premise behind the claim that the matter-antimatter orientation of the universe is a free choice rather than something the framework fixes.

## one-liner
Premise: CPT conjugation, an antilinear anti-automorphism under the field-action convention, is an isomorphism of every kinematic structure and leaves every action functional and its parameters, gauge couplings included, invariant; checked for the metric, completion, pairing and gravitational action, assumed for the gauge and matter sectors.
