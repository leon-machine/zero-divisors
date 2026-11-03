---
id: sheaf.weights-are-forced-are-kasner-exponents
kind: claim
version: 5
title: The weights are forced and are the Kasner exponents
status: proved
region: sheaf
subject: walls
tags: [kasner, schwarzschild, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - sheaf.exceptional-algebra-black-hole@4
  - sheaf.kasner-data-interior@2
  - sheaf.schwarzschild-degeneration-boundary-tame@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_cometric_and_its_orders
- kind: check
  ref: check.py::check_weights_forced_per_profile
- kind: check
  ref: check.py::check_exceptional_weights_are_kasner_exponents
locators:
  paper: T04
  number: Thm 8.16
  label: thm:weights
  line: 1032
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: cometric of the static interior gauge field and its orders; the three weight profiles each forced uniquely over a half-integer grid; conversion to Kasner exponents. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    added:
    - sheaf.exceptional-algebra-black-hole
    - sheaf.kasner-data-interior
    - sheaf.schwarzschild-degeneration-boundary-tame
    note: 'Added the three cited results because the regime profiles, the named dying Killing-time direction
      and the Kasner identification are taken from them; no standard route, since only the Kasner exponents
      are classical and they enter as an imported premise, not as a standard derivation of the forcing.
      Levels pass: conditions already kept.'
  env: theorem
  context_refs:
  - sheaf.exceptional-algebra-black-hole
  - sheaf.kasner-data-interior
  - sheaf.schwarzschild-degeneration-boundary-tame
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.schwarzschild-degeneration-boundary-tame
    - sheaf.exceptional-algebra-black-hole
    - sheaf.kasner-data-interior
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the rescaled cometric is the derived cometric of the Schwarzschild gravitational field on flat spacetime read on the rescaled Schwarzschild coordinate coframe; read off the geometry becomes read off the gravitational field. Weights, uniqueness and Kasner conversion unchanged. Proof not in metric language beyond the cometric entries; one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
For the Schwarzschild gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), within the class of diagonal rescalings $r^{a_i}$ of the Schwarzschild coordinate coframe, demand that its derived cometric, read on the rescaled coframe, extend continuously to $E$. Then:
\begin{enumerate}
\item requiring a corank-one limit whose dying entry is the Killing-time entry, vanishing at first order, forces $(a_r, a_t, a_\theta) = (\tfrac12, 0, 1)$, uniquely: the degeneration-sheaf regime of Theorem \claimref{sheaf.schwarzschild-degeneration-boundary-tame};
\item requiring a nondegenerate limit forces $(a_r, a_t, a_\theta) = (\tfrac12, -\tfrac12, 1)$, uniquely: the exceptional regime of Proposition \claimref{sheaf.exceptional-algebra-black-hole}.
\end{enumerate}
The naming of the dying entry in (1) is not a free choice but is read off the gravitational field: the radical of the actual degeneration is the Killing-time covector (Theorem \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(4)); without naming it, other slot assignments exist (for instance $(1, -\tfrac12, 1)$ sends the radial entry to zero at first order instead), so the forcing is per named profile. Converted to proper time $\tau_{\mathrm{p}} \propto r^{3/2}$, the exceptional weights are the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$ of Fact \claimref{sheaf.kasner-data-interior}, with $\sum p_i = \sum p_i^2 = 1$. This settles the Kasner-weights conjecture for Schwarzschild within the diagonal class: given the dying direction determined by the field, the weights of the anisotropic completion are not chosen, they are forced, and they are the Kasner exponents.

## technical
Rescale the Schwarzschild coordinate coframe diagonally by powers $r^{a_i}$ and ask that the derived cometric of the Schwarzschild gravitational field on flat spacetime, read on the rescaled coframe, extend continuously to the singular boundary $E$. The diagonal cometric entries have $r$-orders $(-1, +1, -2)$, which the rescaling shifts to $(2a_r - 1,\, 2a_t + 1,\, 2a_\theta - 2)$, so prescribing the target order of each slot fixes every weight by a linear solve. A corank-one limit in which the Killing-time entry dies at first order forces $(a_r, a_t, a_\theta) = (\tfrac12, 0, 1)$, the degeneration-sheaf regime; a nondegenerate limit forces $(\tfrac12, -\tfrac12, 1)$, the exceptional regime.

Which entry dies is read off the gravitational field, since the radical of the actual degeneration is the Killing-time covector; without naming it other assignments exist, so uniqueness is per named profile. Converted to proper time $\tau_{\mathrm{p}} \propto r^{3/2}$, the exceptional weights become the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$, with $\sum p_i = \sum p_i^2 = 1$. Within the diagonal class, the weights of the anisotropic completion are therefore forced, not chosen.

## lay
Near the centre of a Schwarzschild black hole the gravitational field stretches lengths in some directions and squeezes them in others. To describe it smoothly up to the singularity one can rescale each coordinate direction by a power of the radius, and this result shows that, among such direction-by-direction rescalings, the powers are not a free choice: once the limiting behaviour the field dictates is imposed, only one set works. Measured in the infalling observer's own time, those powers are exactly the Kasner exponents that describe how space distorts near such a singularity.

## one-liner
Among diagonal rescalings of the Schwarzschild coframe, each prescribed limit at the singularity forces unique weights, and the exceptional weights are the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$ in proper time.
