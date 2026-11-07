---
id: singularity.l-stabiliser-tangent
kind: claim
version: 5
title: (L$_E$) as the stabiliser and the tangent
status: proved
region: singularity
subject: entropy
tags:
- entropy-premises
- pairing-and-bogoliubov
- rotors-and-stabilisers
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.witt-basis-car@1
  - std-algebra.pure-spinors@1
  - std-algebra.bivector-lie-algebra@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:13.4
- kind: check
  ref: check.py::check_so2nu_split_and_closure
- kind: check
  ref: check.py::check_vacuum_stabiliser_and_tangent
- kind: check
  ref: check.py::check_rotations_fix_or_move_the_vacuum
locators:
  paper: T05
  number: Prop 13.4
  label: prop:stabtangent
  line: 2470
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the C of so(2 nu) + C and Spin(2 nu, C) and the i of the Majorana basis are the scalar unit of the atom built in the plane e0e1, where I_4 anticommutes with the modes (the entity''s unit_note, conventions known limit 1); declared (version and levels unchanged). Declaration kind set to complex-analysis by Leon''s ruling R1 (atom, boundary-mode and window flows keep i).'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-basis-car, std-algebra.pure-spinors, std-algebra.bivector-lie-algebra where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: so(2 nu) split and closure for nu = 2, 3, 4, the vacuum stabiliser and tangent ranks, and the hop and pairing rotations at (3/5, 4/5) with the witness. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: proposition
  context_refs:
  - singularity.class-relative-no-go-no-supplied
  - singularity.envelope-endpoint-why-boundary-mode-locality
  unresolved_refs:
  - rem:hopresidual
  typing:
    by: ai-typing-pass
    removed:
    - singularity.l-boundary-mode-locality
    note: 'Removed the assumes edge to (L_E): the proposition is a Lie-algebra computation on Fock space
      that classifies the parts of the premise, and nothing in its proof assumes the premise. Levels pass:
      the lay now keeps the two-or-more-modes condition and says the stabiliser fixes the vacuum ray (the
      Cartan elements act as a scalar), including the pair annihilations.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$\gamma_{2i} = i(v_i - v^*_i)$: Majorana basis of the complex Fock space for $\mathfrak{so}(2\nu)$
      and $\mathrm{Spin}(2\nu, \C)$; the singularity paper builds its atom in the radial plane $e_0e_1$
      of spacetime, so $I_4$ would anticommute with these mode operators (i next to an odd element). Doubtful,
      left for the maintainer'
    - indices $i, j$ (index)
  unit_note: 'The imaginary unit here stays a scalar i: this atom is built in the spacetime radial plane
    sigma = e0 e1, where the field theory''s unit I4 anticommutes with the mode operators, so the convention
    i = I4 (which needs a plane orthogonal to spacetime) does not apply. Recorded 21 October 2026; see
    store/conventions.md, known limit 1.'
outside_ga:
  kind: complex-analysis
  why: 'the complex Fock space of the singularity paper''s atom (so(2 nu) + C, Spin(2 nu, C), the Majorana basis gamma_{2i} = i(v_i - v_i^*)) keeps a scalar i: the atom is built in the spacetime radial plane e0e1, where I_4 anticommutes with the mode operators (conventions, known limit 1)'
---

## formal
On the Fock space of $\nu \geq 2$ boundary modes with creation operators $v^*_i$, the bivectors of $\mathfrak{so}(2\nu)$ are the quadratic elements $v^*_i v_j - \tfrac12\delta_{ij}$, $v_i v_j$ and $v^*_i v^*_j$, and split as hops (the $\nu(\nu - 1)$ elements $v^*_i v_j$ with $i \neq j$ together with the $\nu$ Cartan elements $v^*_i v_i - \tfrac12$), pair annihilations $v_i v_j$ and pair creations $v^*_i v^*_j$ ($\nu(\nu - 1)/2$ each), $\nu^2 + \nu(\nu - 1) = \nu(2\nu - 1) = \dim\mathfrak{so}(2\nu)$; the same elements without the $\tfrac12$ span, with the identity, $\mathfrak{so}(2\nu) \oplus \C$, and are not themselves closed under the bracket. On the vacuum $|0\rangle$ every hop with $i \neq j$ and every pair annihilation vanishes and every Cartan element acts as the scalar $-\tfrac12$, so the hops and the pair annihilations together are the stabiliser of the vacuum ray; the pair creations applied to $|0\rangle$ are linearly independent and span, modulo $|0\rangle$, the tangent space at $|0\rangle$ of the orbit of Witt vacua, of complex dimension $\nu(\nu - 1)/2$, while the tangent space of the orbit of the vector $|0\rangle$ itself, the span of $X|0\rangle$ over $X \in \mathfrak{so}(2\nu)$, has dimension $1 + \nu(\nu - 1)/2$, the extra dimension being the scalar action of the Cartan elements. Consequently every hop rotation $\exp\theta(v^*_i v_j - v^*_j v_i)$ fixes the vacuum and every pairing rotation $\exp\theta(v^*_i v^*_j - v_j v_i)$ moves it; the necessity witness of Corollary \claimref{singularity.envelope-endpoint-why-boundary-mode-locality}, $|00\rangle \mapsto \tfrac35|00\rangle + \tfrac45|11\rangle$, is the pairing rotation on modes $(1,2)$ at $(\cos\theta, \sin\theta) = (\tfrac35, \tfrac45)$. The half of Premise \claimref{singularity.l-boundary-mode-locality} that Theorem \claimref{singularity.class-relative-no-go-no-supplied} proves, within the supplied class, therefore lies in the stabiliser of the vacuum; of the half it premises, the exclusion of unsupplied generators, the pairing terms are the tangent space of the vacuum's orbit, the part that changes the Witt decomposition and the only part that can move the vacuum, and so the only part that can create entanglement from it, at one dimension per pair of modes, while the differential terms of Remark \ref{rem:hopresidual} are hops and lie in the stabiliser.

## technical
On the Fock space of $\nu \geq 2$ modes, the quadratic elements spanning $\mathfrak{so}(2\nu)$ split into hops with the Cartan elements ($\nu^2$ in all), pair annihilations and pair creations ($\nu(\nu-1)/2$ each). On the vacuum, the hops with $i \neq j$ and the pair annihilations vanish and the Cartan elements act as the scalar $-\tfrac12$, so these form the stabiliser of the vacuum ray, while the pair creations span the tangent space of the orbit of Witt vacua, of complex dimension $\nu(\nu-1)/2$.

Hence hop rotations fix the vacuum and pairing rotations move it. The half of boundary-mode locality proved within the supplied class lies in the stabiliser; of the premised half, the pairing terms are the tangent directions, the only ones that can create entanglement from the vacuum, while differential terms are hops.

## lay
The operators acting quadratically on two or more fermionic modes come in two kinds: those that move a particle between modes and those that create or destroy particles in pairs. On the empty state the first kind leaves its direction unchanged, as does pair destruction, while pair creation genuinely changes it. So the only part of the locality assumption that does real work starting from the empty state is the ban on pair creation.

## one-liner
In $\mathfrak{so}(2\nu)$ on Fock space, hops and pair annihilations stabilise the vacuum ray and pair creations span the tangent to its orbit, so only pairing can move the vacuum.

