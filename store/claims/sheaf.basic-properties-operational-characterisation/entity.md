---
id: sheaf.basic-properties-operational-characterisation
kind: claim
version: 5
title: Basic properties, and the operational characterisation
status: proved
region: sheaf
subject: walls
tags: [schwarzschild]
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
- obj.sheaf.weighted-coframe-module
derivations:
- name: main
  uses:
  - sheaf.rain-duality@3
  - sheaf.schwarzschild-degeneration-boundary-tame@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_free_of_rank_four_with_bounded_norms
- kind: check
  ref: check.py::check_rain_characterisation_algebra
- kind: check
  ref: check.py::check_rho_not_smooth_at_order_one
locators:
  paper: T04
  number: Prop 8.4
  label: prop:Wframe
  line: 891
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: free of rank four with bounded frame norms, the rain-frame component formulas and Taylor-division identity, and minimality of order two. Version 2 -> 3. Check entries synced with check.py: +1, -1 (added check_rho_not_smooth_at_order_one; removed check_order_two_is_minimal). Version 3 -> 4. check.py: check_order_two_is_minimal renamed check_rho_not_smooth_at_order_one, p(r)^2 = r obstruction asserted on a grid, minimality marked as argued (fix round 2026-10-23). Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Kept both premises, which the proof uses (the rain characterisation and the bounded G-norms
      of the frame); an about edge to the weighted-module definition was not added because it counts as
      a substantive change requiring a version bump. Levels pass: the lay now keeps the u-smoothness condition
      on the rain characterisation.'
---

## formal
$\shW$ is locally free of rank four. Away from $E$ it coincides with the full cotangent module, so nothing in the interior is altered. A $u$-smooth one-form lies in $\shW$ if and only if all four of its components in the infalling orthonormal frame are bounded up to $E$ (the rain characterisation, proved as Proposition \claimref{sheaf.rain-duality}(3)); in particular the module is attached to the geometry and the blow-up, not to the chosen frame. The order two of the quasihomogeneous structure is minimal for $\shW$ to admit a smooth frame, being forced by the half-integer growth of $\beta$: at order one (smooth in $r$) the generator $\rho = r^{1/2}\,dr$ is not smooth.

## technical
The weighted coframe module $\shW$ is locally free of rank four, and away from the boundary $E$ it coincides with the full cotangent module, so nothing in the interior is altered. A $u$-smooth one-form lies in $\shW$ exactly when its four components in the infalling orthonormal frame are bounded up to $E$, so the module is attached to the geometry and the blow-up, not to the chosen frame. Order two is the least order of the quasihomogeneous structure for which $\shW$ has a smooth frame: at order one the generator $\rho = r^{1/2}\,dr$ is not smooth.

## lay
This result lists the basic properties of the rescaled set of one-forms used near the Schwarzschild singularity. It has the right size, changes nothing away from the singularity, and can be described without any choice of frame: among the forms smooth in the rescaled sense, it consists exactly of those that freely falling observers measure as finite. Measuring smoothness in the square root of the radius is the least change that makes this work.

## one-liner
$\shW$ is locally free of rank four, equals the cotangent module in the interior, consists exactly of the $u$-smooth one-forms with bounded infalling-frame components, and needs the order-two smooth structure.
