---
id: dark-energy.stelle-west-vector-frozen-point
kind: claim
version: 6
title: The Stelle-West vector of the frozen point
status: proved
region: dark-energy
subject: dark-energy
tags: [frozen-point, tractors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: the tractor connection as the Cl(2,4) gauge field Omega_T, checked slot by slot'
  version: 6
  source: maintainer pass 2026-11-07 (consistency, GTG proofs)
review: typed
derivations:
- name: main
  uses:
  - dark-energy.imported-frozen-point-geometry@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:lem:sw
- kind: check
  ref: check.py::check_constraints_and_slots
- kind: check
  ref: check.py::check_de_sitter_field_soldering_and_parallel_frozen_point
- kind: check
  ref: check.py::check_gauge_field_is_omega_plus_frame_wedge_w
- kind: check
  ref: check.py::check_bracket_of_soldering_bivectors
- kind: check
  ref: check.py::check_tractor_gauge_field_slots_and_bracket
locators:
  paper: T10
  number: Lem 2.5
  label: lem:sw
  line: 658
extraction:
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof rewritten in Gauge Theory Gravity: tractors as Cl(2,4) vectors sigma ninf + mu + rho n0, the connection of the frozen-point Fact shown slot by slot to be the gauge field Omega_T(a) = Omega(a) - ninf ^ hb^{-1}(a) + n0 ^ P(hb^{-1}(a)) (derived in the proof, not cited from the tractor theorem, which rests on this lemma), Theta(A) = A ^ W at P = (Lambda/6) id, D^T X = (A ^ W) . n0 = A, and the bracket as the commutator product with the four-vector formula; the slot computation kept as a labelled reading at the end. New exact check check_tractor_gauge_field_slots_and_bracket (generic Schouten map and rotation bivector, three values of Lambda, the Jacobi form of the bracket). outside_ga withdrawn: no stand-in remains.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The proof computes the tractor derivative of X and V slot by slot in the scale-g component form of the tractor connection (sigma, mu_b, rho; g_ab, P_ab); on flat spacetime that connection is the Cl(2,4) gauge field Omega_T of synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection, and the slot computation is its component reading.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Stelle-West constraints and slots, and on the de Sitter gauge field D X = D V = hb^{-1}(a), D I = 0, Omega_T = Omega + hb^{-1} ^ W and the soldering bracket. Version 4 -> 5.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Einstein region is that of a gravitational field on flat spacetime, the tractors are Cl(2,4) vectors (I = ninf + (Lambda/6) n0, X = n0, W = ninf - (Lambda/6) n0), the soldering e_a is the physical frame vector hb^{-1}(a), and clause (iii) is read as the tractor gauge field Omega_T(a) = Omega(a) + hb^{-1}(a) ^ W. Proof prefixed. Fix (referee GR2, 2026-10-23): the claimref to the tractor theorem, which rests on this lemma, replaced by a plain description of the gauge field in (iii) and in the proof prefix.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    added: [dark-energy.imported-frozen-point-geometry]
    note: 'Added the frozen-point fact, which supplies the hypotheses ($I$ parallel in its scale) and the tractor connection and metric that the computation uses.'
  env: lemma
  context_refs:
  - dark-energy.imported-frozen-point-geometry
  eqrefs: 5
---

## formal
Let a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) be Einstein with $\Lambda \neq 0$ on its invertible region, and work in the scale $g$ of its derived metric determined by the frozen point, so that $I = (1, 0, \Lambda/6) = \nInf + \tfrac{\Lambda}{6}\nO$ and $\nabla I = 0$ (Fact \claimref{dark-energy.imported-frozen-point-geometry}). Let $X := (0, 0, 1) = \nO$ be the canonical tractor, and define
\[
V \;:=\; X - \frac{\ip{X}{I}}{Q(I)}\, I \;=\; X - \frac{3}{\Lambda}\, I \;=\; \Bigl(-\frac{3}{\Lambda},\; 0,\; \frac12\Bigr),
\qquad
W \;:=\; \frac{V}{Q(V)} \;=\; \Bigl(1,\; 0,\; -\frac{\Lambda}{6}\Bigr) \;=\; \nInf - \tfrac{\Lambda}{6}\nO .
\]
Write $e_a$ for the tractor $(0, g_{ab}, 0)$, the unit vector of the $\mu_a$ slot: on flat spacetime the physical frame vector $\hb^{-1}(a)$. Then:
\begin{enumerate}
\item[(i)] $Q(X) = 0$, $\ip{X}{I} = 1$, $\ip{V}{I} = 0$, and $Q(V) = -3/\Lambda = -\ell^2$.
\item[(ii)] $\nabla_a X = e_a$, the soldering form, and $\nabla_a V = e_a$ as well; $\ip{e_a}{I} = 0$.
\item[(iii)] On a tractor with no $\mu$-component the connection \eqref{eq:conn} acts as $\nabla_a = \partial_a + e_a\wedge W$; on a general tractor it is the Levi-Civita connection on the $\mu$-slot plus the same bivector: $\nabla_a = D_a + e_a\wedge V/Q(V)$. On flat spacetime this is the $\Cl(2,4)$ gauge field $\Omega_{T}(a) = \Omega(a) + \hb^{-1}(a) \wedge W$: the rotation-gauge field plus the soldering bivector built from the physical frame, with Schouten map $\tfrac{\Lambda}{6}\,\mathrm{id}$.
\item[(iv)] $[\,e_a\wedge W,\; e_b\wedge W\,] = -Q(W)\; e_a\wedge e_b = (\Lambda/3)\, e_a\wedge e_b$.
\end{enumerate}

## technical
For a gravitational field on flat spacetime that is Einstein with $\Lambda\neq 0$, in the scale of the frozen point, $I = (1,0,\Lambda/6) = \nInf + \tfrac{\Lambda}{6}\nO$ is parallel. With the canonical tractor $X = (0,0,1) = \nO$ set $V = X - (3/\Lambda)I = (-3/\Lambda, 0, 1/2)$ and $W = V/Q(V) = (1,0,-\Lambda/6)$. Then $Q(X) = 0$, $\langle X,I\rangle = 1$, $\langle V,I\rangle = 0$ and $Q(V) = -3/\Lambda = -\ell^2$, while $\nabla_aX = \nabla_aV = e_a$, the soldering form, on flat spacetime the physical frame vector $\hb^{-1}(a)$, with $\langle e_a, I\rangle = 0$.

The tractor connection is the Levi-Civita connection on the middle slot plus a single bivector, $\nabla_a = D_a + e_a\wedge V/Q(V)$: on flat spacetime the gauge field $\Omega_{T}(a) = \Omega(a) + \hb^{-1}(a) \wedge W$. And $[e_a\wedge W, e_b\wedge W] = -Q(W)\,e_a\wedge e_b = (\Lambda/3)\,e_a\wedge e_b$.

## lay
Starting from the frozen point and one canonical fixed direction of the six-dimensional conformal model, this lemma builds a vector perpendicular to the frozen point whose length is set by the cosmological constant. Its rate of change is exactly the frame that links the conformal model to the physical directions of the gravitational field on flat spacetime. It is the vector that the Stelle-West form of gravity needs, and the lemma records its basic algebra.

## one-liner
In the frozen point's scale, $V = X - (3/\Lambda)I$ is orthogonal to $I$ with $Q(V) = -3/\Lambda$ and $\nabla V = e$, and the tractor gauge field is $\Omega(a) + \hb^{-1}(a)\wedge V/Q(V)$.
