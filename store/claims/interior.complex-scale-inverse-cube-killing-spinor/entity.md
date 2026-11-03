---
id: interior.complex-scale-inverse-cube-killing-spinor
kind: claim
version: 5
title: The complex scale is the inverse cube of the Killing spinor
status: proved
region: interior
subject: interior
tags: [kerr, pseudoscalar-and-centre]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
derivations:
- name: main
  uses:
  - interior.complex-factorisation-location-ring@5
  - interior.imported-kerr-curvature@2
  - interior.imported-walker-penrose-killing-spinor@2
  proof: proof-main.tex
- name: standard-route
  uses:
  - interior.imported-walker-penrose-killing-spinor@2
  - interior.imported-kerr-curvature@2
  - interior.imported-schwarzschild-curvature-spectrum-external@1
  proof: proof-standard-route.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:6.8
- kind: check
  ref: check.py::check_scale_is_minus_m_inverse_cube_of_killing_scalar
- kind: check
  ref: check.py::check_winding_is_three_times_the_spinor_scalar
locators:
  paper: T06
  number: Prop 6.8
  label: prop:killing
  line: 872
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: chi^3 M_frak = -M with power exactly three, and the winding of M_frak three times that of chi on a rational loop around the ring. Version 3 -> 4. Wording fix (Leon 2026-10-23): the monodromy is -3 times the spinor''s winding (thrice, in the opposite sense), at every level, for the earlier three times. Check strengthened: chi^4 control pinned as chi^4 M_frak = -M chi; product probe moved to module level. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    removed: [interior.imported-schwarzschild-curvature-spectrum]
    note: 'Removed the Schwarzschild spectrum fact from main, since the proof says the derivation runs on the Kerr curvature fact and the Killing-spinor scalar alone and cites that fact only in an aside on Psi_2 conventions; the standard-route rests on the source calling the Walker-Penrose Psi_2 clause the spinor-calculus instance of the computation, which is a judgement call.'
  env: proposition
  context_refs:
  - interior.exact-scale-decoupling
  unresolved_refs:
  - rem:winding
  source_title: 'The complex scale is the inverse cube of the Killing spinor'
  source_formal: |-
    Identify the commutative subalgebra $\R \oplus \R I$ with $\C$ as in Proposition \claimref{interior.complex-factorisation-location-ring}(1), matching $I$ with $i$ (an orientation choice, fixed once). Then the Kerr curvature scale of Fact \claimref{interior.imported-kerr-curvature} is
    \[
    \mathfrak M \;=\; -M\,\chi^{-3}
    \]
    with $\chi = r - Ia\cos\theta$ the Killing-spinor scale of Fact \claimref{interior.imported-walker-penrose-killing-spinor} in the same normalisation. Consequently: the framework's ``scalar-plus-pseudoscalar scale'', discovered in Proposition \claimref{interior.exact-scale-decoupling} as the carrier of the entire approach to the singularity and complexified by rotation in Proposition \claimref{interior.complex-factorisation-location-ring}, is a hidden twistorial object: the very spinor that generates Carter's constant and the hidden symmetries of the Kerr interior. And the duality monodromy of Remark \ref{rem:winding} is thrice the winding of the Killing spinor around the ring.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Only the formal level named a twistor notion ("a hidden twistorial object"); it now says a Killing spinor, keeping the twistor equation by name in parentheses. The identification of $\R \oplus \R I$ with $\C$ is already geometric algebra and is unchanged, as is the proof.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "matching $I$ with $i$ in $\\R \\oplus \\R I \\cong \\C$: complex geometry of the Kerr metric (the complex scale $\\chi = r - Ia\\cos\\theta$), not the quantum unit"
---

## formal
Identify the commutative subalgebra $\R \oplus \R I$ with $\C$ as in Proposition \claimref{interior.complex-factorisation-location-ring}(1), matching $I$ with $i$ (an orientation choice, fixed once). Then the Kerr curvature scale of Fact \claimref{interior.imported-kerr-curvature} is
\[
\mathfrak M \;=\; -M\,\chi^{-3}
\]
with $\chi = r - Ia\cos\theta$ the Killing-spinor scale of Fact \claimref{interior.imported-walker-penrose-killing-spinor} in the same normalisation. Consequently: the framework's ``scalar-plus-pseudoscalar scale'', discovered in Proposition \claimref{interior.exact-scale-decoupling} as the carrier of the entire approach to the singularity and complexified by rotation in Proposition \claimref{interior.complex-factorisation-location-ring}, is a hidden spinor object, a Killing spinor (a solution of Penrose's twistor equation): the very spinor that generates Carter's constant and the hidden symmetries of the Kerr interior. And the duality monodromy of Remark \ref{rem:winding} is $-3$ times (thrice, in the opposite sense) the winding of the Killing spinor around the ring.

## technical
Identify $\R \oplus \R I$ with $\C$ by matching $I$ with $i$. Then the Kerr curvature scale is $\mathfrak M = -M\chi^{-3}$, where $\chi = r - Ia\cos\theta$ is the scalar of the Walker-Penrose Killing spinor, in the normalisation that the spinor's constant-scale freedom permits. The scalar-plus-pseudoscalar scale that carries the approach to the singularity, complexified by rotation, is thus the inverse cube of the spinor that generates Carter's constant and the hidden symmetries of the Kerr interior.

Because the power is three, the duality monodromy of the scale around the ring is $-3$ times (thrice, in the opposite sense) the winding of the Killing spinor. The proof compares the two objects in one convention; the content is that an object built from curvature and the invertibility criterion alone coincides with this spinor invariant.

## lay
A previous result produced a complex number that controls the curvature of a rotating black hole. This result shows that the number is, up to a cube and a constant, a well-known object: the Killing spinor behind Carter's hidden conserved quantity for orbits around a rotating black hole. Going once around the singular ring, the curvature's phase therefore turns three times as often as the spinor's, in the opposite sense.

## one-liner
The Kerr curvature scale is $\mathfrak M = -M\chi^{-3}$ with $\chi = r - Ia\cos\theta$ the Walker-Penrose Killing-spinor scalar, so the duality monodromy around the ring is $-3$ times the spinor's winding.
