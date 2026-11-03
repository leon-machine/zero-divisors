---
id: hawking.imported-exterior-exactly-general-relativity
kind: claim
version: 3
title: 'Imported: the exterior is exactly general relativity'
status: proved
region: hawking
subject: einstein
tags: [curvature-and-field-equations, tractors, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
derivations:
- name: main
  uses:
  - interior.covariant-form-vacuum-equations@5
  - interior.imported-equivalence-einstein-equations@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T07
  number: Fact 2.5
  label: fact:exterior
  line: 420
extraction:
  typing:
    by: ai-typing-pass
    removed:
    - interior.scale-tractor-leaves-cone
    note: 'Removed the Lambda != 0 theorem, which the source cites only as the complementary case while the statement is at Lambda = 0; the Lasenby-Doran-Gull equivalence is already a main premise, so no separate standard-route was added.'
  env: fact
  context_refs:
  - interior.covariant-form-vacuum-equations
  - interior.imported-equivalence-einstein-equations
  - interior.scale-tractor-leaves-cone
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
On the region where the gauge field is invertible, and at $\Lambda = 0$, the series' description coincides exactly with classical general relativity: the field equations are equivalent to the Einstein equations, and the vacuum equations are exactly the covariant constancy of the scale tractor. \emph{Provenance:} \cite[Fact 2.1, Thms.~4.5 and 4.7]{ButlerT6} (Thm.~4.7 is the complementary $\Lambda \neq 0$ case), resting on Lasenby-Doran-Gull's equivalence theorem.

## technical
On the region where the gauge field $\hb$ is invertible, and at $\Lambda = 0$, the series' description is exactly classical general relativity. The gauge field equations are equivalent to the Einstein equations for the metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$, by the equivalence theorem of Lasenby, Doran and Gull, and the vacuum equations are exactly $\nabla I_g = 0$ for the scale tractor of $g$. The entry restates these earlier results; the $\Lambda \neq 0$ case is treated separately.

## lay
Away from the places where the series' new structure matters, its description of gravity is not an approximation to general relativity but the same theory. With no cosmological constant, both the field equations and their geometric repackaging agree exactly with Einstein's theory in that region.

## one-liner
Where the gauge field is invertible and $\Lambda = 0$, the series' description coincides exactly with general relativity, its vacuum equations being the parallelism of the scale tractor.
