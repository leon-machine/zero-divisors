---
id: sheaf.infinite-wall-sequence
kind: claim
version: 4
title: The infinite wall sequence
status: proved
region: sheaf
subject: walls
tags: [degenerate-algebras, transport-algorithm]
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
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.one-sided-completion@4
  - sheaf.tame-wall-induction@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_walls_displaced_successively
- kind: check
  ref: check.py::check_each_wall_is_a_simple_corank_one_zero
- kind: check
  ref: check.py::check_one_hyperbolic_plane_per_wall
- kind: check
  ref: check.py::check_radical_lines_have_global_sections
locators:
  paper: T04
  number: Cor 5.5
  label: cor:wallsequence
  line: 732
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: an iterated collar model to stage 4: walls at -k/2 displaced successively, simple corank-one zeros, signatures (2+k, 4+k) one plane per wall, and the global radical section of each shadow wall. Version 2 -> 3. Check strengthened: the block-inversion step s -> s/(1 + 2 mu nu s) is checked to carry wall tau_k onto tau_(k+1); sample wall positions moved to module level. Version 3 -> 4.'
  env: corollary
  unresolved_refs:
  - rem:bundlesetup
  typing:
    by: ai-typing-pass
    note: 'Both edges are real premises (the wall induction is iterated and the one-sided completion supplies
      ranks and signatures at each stage); tameness of the initial wall is carried through the induction
      lemma. Levels pass: lay now keeps compactness and good couplings at every stage.'
---

## formal
Let $\Sig$ be compact. For good couplings at every stage, there is an infinite sequence $\Sig = \Sig^{(0)}, \Sig^{(1)} = \Sig', \Sig^{(2)}, \dots$ of tame walls, each displaced from the last into the unphysical region, carrying Clifford sheaves of ranks $2^n, 2^{n+2}, 2^{n+4}, \dots$ whose physical-side fibres ascend the Witt tower $\Cl(p,q) \to \Cl(p{+}1,q{+}1) \to \Cl(p{+}2,q{+}2) \to \cdots$, one Rule-1 rung per wall. Degeneracy is conserved along the entire sequence: each completion resolves its wall and produces the next, displaced successively further from the physical region.

## technical
Let $\Sig$ be compact and choose a good coupling at every stage. Then there is an infinite sequence of tame walls $\Sig = \Sig^{(0)}, \Sig^{(1)} = \Sig', \Sig^{(2)}, \dots$, each displaced from the last into the unphysical region, carrying Clifford sheaves of ranks $2^n, 2^{n+2}, 2^{n+4}, \dots$ whose physical-side fibres ascend the Witt tower $\Cl(p,q) \to \Cl(p+1,q+1) \to \Cl(p+2,q+2) \to \cdots$, one rung per wall.

The proof iterates the wall induction. Each new wall is compact, so a good coupling exists at the next stage, and the radical line of each shadow wall has an explicit global nowhere-zero spanning section, so collar data for the next coupling exist. Degeneracy is conserved along the whole sequence: each completion resolves its wall and produces the next.

## lay
Provided the wall is compact and each repair is done gently enough (a good coupling at every stage), repairing a degenerate wall on one side creates a new wall a little further away, and that wall can be repaired in the same way. Repeating this forever gives an infinite chain of walls, each carrying an algebra built on two more dimensions than the last. The degeneracy is never destroyed, only pushed further from the physical region at each step.

## one-liner
For a compact wall and good couplings at every stage, the completion iterates indefinitely, giving an infinite sequence of tame shadow walls whose Clifford fibres ascend the Witt tower by one rung per wall.
