---
id: sheaf.characterisation-forced-within-rain-bounded-class
kind: claim
version: 4
title: The characterisation is forced, within the rain-bounded class
status: proved
region: sheaf
subject: walls
tags: [forcing-and-uniqueness]
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
- obj.sheaf.extensions
- obj.sheaf.weighted-coframe-module
derivations:
- name: main
  uses:
  - sheaf.one-sided-completion-singularity@4
  - sheaf.rain-duality@3
  - sheaf.uniqueness-weighted-module@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_rain_bounded_is_inclusion_in_w
- kind: check
  ref: check.py::check_tame_rain_bounded_extensions_are_w
- kind: check
  ref: check.py::check_anchoring_class_must_be_named
- kind: check
  ref: check.py::check_completion_is_attached_to_w
locators:
  paper: T04
  number: Cor 8.20
  label: cor:forcedchar
  line: 1077
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on Schwarzschild data, W is the maximal rain-bounded extension, a rain-bounded extension is boundary tame exactly when it equals W, the null-mixing example satisfies (T2d) and (T3d) without being rain-bounded, and the completion on W has det h = m^2 and signature (2,4) on E. Version 2 -> 3. Check strengthened: the hand-entered boundary Gram B0 of ex:nullmix is asserted equal to the C -> m/2 limit of the frame Gram; frame indices named. Version 3 -> 4.'
  env: corollary
  unresolved_refs:
  - ex:nullmix
  typing:
    by: ai-typing-pass
    note: 'Kept all three premises: uniqueness gives the main step, rain duality the equivalence with
      inclusion in W, and the one-sided completion theorem the restated clause about the completion. Levels
      pass: conditions already kept.'
---

## formal
Within the rain-bounded class the characterisation of $\shW$ is not a choice of definition but a consequence of tameness: every rain-bounded boundary-tame extension is automatically the maximal one. The completion, the ladder pair, and the exceptional algebra of this section are therefore attached to the geometry together with the infalling congruence, whose finiteness class picks the module; Example \ref{ex:nullmix} shows some anchoring class must be named.

## technical
Within the class of rain-bounded extensions, the characterisation of $\shW$ is a consequence of tameness rather than a choice of definition: every rain-bounded boundary-tame extension equals $\shW$, which is the maximal rain-bounded extension, since rain-boundedness means exactly $\mathcal{M} \subseteq \shW$. Consequently the completion, the ladder pair and the exceptional algebra built on $\shW$ are attached to the geometry together with the infalling congruence, whose finiteness class selects the module; some anchoring class of this kind has to be named.

## lay
One might worry that the special set of one-forms used near the singularity was merely a convenient choice. This result shows that, once finiteness for freely falling observers and the mildest kind of degeneration are required, there is no other choice. The structures built from it are therefore fixed by the geometry together with the family of infalling observers.

## one-liner
Every rain-bounded boundary-tame extension is $\shW$, so within the rain-bounded class the weighted module, and the completion built on it, are forced by tameness.
