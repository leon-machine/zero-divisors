---
id: field-theory.mass
kind: claim
version: 5
title: Mass with $i = I_4$
status: proved
region: field-theory
subject: quantum-fields
tags: [mass-generation, pseudoscalar-and-centre, symmetry-breaking]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'GA rewrite (the two-component epsilon pairing labelled as a reading)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - field-theory.imported-one-datum-massive-law@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_INT.py
  tags:
  - id:M1.1
  - id:M1.2
  - id:M1.3
  - id:M1.4
  - id:M1.5
  - id:M2.0
  - id:M2.1
  - id:M2.2
  - id:M2.3
- kind: check
  ref: check.py::check_pairing_on_one_chirality
- kind: check
  ref: check.py::check_charge_two_under_common_phase
- kind: check
  ref: check.py::check_massive_plane_wave_couples_opposite_charges
- kind: check
  ref: check.py::check_pseudoscalar_is_not_the_massive_complex_structure
locators:
  paper: FT
  number: Prop 6.1
  label: prop:mass
  line: 159
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. At reader R06''s request, the two-component epsilon pairing lambda^T epsilon lambda beside B_N is labelled as a reading ("in two-component form") in the formal and technical levels; B_N(psi, phi) = <psi~ phi N> stays the statement. Wording only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the four right factors giving the epsilon pairing on chi_+ (antisymmetric, I4-bilinear, Lorentz invariant, nondegenerate, charge two), the massive plane wave as the coupled pair with mass density 2B(chi, eta), and I4 not the massive law''s complex structure. Version 2 -> 3. Check strengthened: chi_+ asserted real 4-dimensional before the charge-two test; the four N moved to module level. Version 3 -> 4.'
  env: proposition
  context_refs:
  - field-theory.imported-one-datum-massive-law
  typing:
    by: ai-typing-pass
    added:
    - field-theory.imported-one-datum-massive-law
    - obj.field-theory.single-algebra-field
    note: 'Added the one-datum fact, which the statement''s last sentence asserts still stands, and the
      single-algebra field (the projection) as about. The source calls the two-component mass standard;
      no imported two-component claim is in the store, so no standard-route derivation was added. Levels
      pass: levels written from scratch, keeping every condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - field-theory.imported-one-datum-massive-law
about:
- obj.field-theory.single-algebra-field
---

## formal
For the four even right factors $N \in \{\gamma_0\gamma_1, \gamma_0\gamma_2, \gamma_1\gamma_3, \gamma_2\gamma_3\}$ that anticommute with $\IS$, $B_N(\psi, \phi) = \proj(\tilde\psi\phi N)$ is a nonzero, antisymmetric, nondegenerate, Lorentz-invariant, $I_4$-bilinear pairing on $\chi_+$ (in two-component form, a labelled reading, the epsilon pairing $\lambda^{\mathsf T}\epsilon\lambda$), of charge two under the common phase. A massive Dirac plane wave splits as $\chi + \psi_-$ with $\eta = \psi_-N \in \chi_+$; $\chi$ and $\eta$ have opposite $I_4$-charges, the Dirac equation is the coupled pair, and the mass density is $2B(\chi, \eta)$. The common $I_4$ phase is axial and the mass breaks it. Fact \claimref{field-theory.imported-one-datum-massive-law} stands: $I_4$ is the field algebra's unit, not the massive law's complex structure.

## technical
For the four even right factors $N \in \{\gamma_0\gamma_1, \gamma_0\gamma_2, \gamma_1\gamma_3, \gamma_2\gamma_3\}$ that anticommute with $\IS$, the pairing $B_N(\psi, \phi) = \proj(\tilde\psi\phi N)$ is nonzero, antisymmetric, nondegenerate, Lorentz-invariant and $I_4$-bilinear on $\chi_+$ (in two-component form, a labelled reading, the epsilon pairing $\lambda^{\mathsf T}\epsilon\lambda$), of charge two under the common phase. A massive Dirac plane wave splits as $\chi + \psi_-$ with $\eta = \psi_-N \in \chi_+$; $\chi$ and $\eta$ have opposite $I_4$-charges, the Dirac equation is the coupled pair, and the mass density is $2B(\chi, \eta)$.

So the common $I_4$ phase is axial and the mass breaks it, and the one-datum fact stands: $I_4$ is the field algebra's unit, not the massive law's complex structure.

## lay
With the spacetime volume element as imaginary unit every field is read in one chirality, and a mass couples a left-handed part to a right-handed one. The mass term then takes exactly the standard two-component form. The unit belongs to the field algebra, not to the massive equation, which still needs its own geometric datum.

## one-liner
With $i = I_4$ a Dirac mass is the standard two-component epsilon pairing $2B(\chi, \eta)$ between opposite $I_4$-charges, breaking the axial phase, and $I_4$ is not the massive law's complex structure.
