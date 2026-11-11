---
id: synthesis.frozen-point-unique-where-weyl-has-no-kernel
kind: claim
version: 7
title: One frozen point up to scale wherever the Weyl tensor has no kernel vector
status: proved
region: synthesis
subject: dark-matter
tags: [tractors, frozen-point, premises-p1-p5]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: the tractor gauge field on the Einstein region as Omega(a) + u ^ hb^{-1}(a), its field strength -W computed in Cl(2,4), the kernel argument on Cl(2,4) vectors; slot route kept as a labelled reading'
  version: 5
  source: maintainer pass 2026-11-07 (GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review fixes (referee F3): uses edges to the GTG dictionary and the tractor gauge-field theorem; the choice of representative of the conformal class justified'
  version: 5
  source: maintainer pass 2026-11-07 (GTG review fixes)
- name: Claude Opus 5.5
  role: 'formal restated at Leon''s second-round decisions: the Consequently clauses for c != 0'
  version: 6
  source: maintainer pass 2026-11-07 (decisions, second round)
- name: Claude Fable 5.2
  role: 'scope note: the statement is for the normal tractor connection'
  version: 7
  source: 'maintainer pass of 2026-11-11 (run 2026-11-11-contradictions)'
amendments:
- version: 7
  kind: restatement
  defect: 'the application to the towers did not say that it is for the normal tractor connection, which under (FS) is not the connection that carries the frozen point on matter regions'
review: draft
derivations:
- name: main
  uses:
  - dark-energy.imported-frozen-point-geometry@7
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - synthesis.imported-gtg-dictionary@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_weyl_kernel_schwarzschild_and_type_n
- kind: check
  ref: check.py::check_tractor_curvature_common_kernel
- kind: check
  ref: check.py::check_parallel_tractors_are_multiples_of_I
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gtg_tractor_field_strength_is_minus_weyl
lineage:
  motivated_by:
  - dark-matter.p1-single-frozen-point
  - dark-energy.point-infinity-has-no-physical-fluctuation
extraction:
  maintainer_pass_2026_11_11:
    by: maintainer-2026-11-11
    date: '2026-11-11'
    note: 'A scope note is added to the formal level, pointing to synthesis.frozen-point-unique-for-the-field-space-connection; the statement and its proof are unchanged.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): dark-energy.imported-frozen-point-geometry repinned 6 -> 7 after reviewing its restatement (the sentence naming the tractor gauge-field theorem moved to a text-only remark); the parts cited here (parallel frozen point, Q(I) = Lambda/3, the stabilisers, the scale-g display and the Schouten tensor) are unchanged, and the use here holds as cited.'
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Leon''s second-round answer 1 (REPORT.md For Leon item 4, fix-F3.md): the formal''s Consequently sentence now reads "Consequently, for c != 0, the Einstein scale of I'' is c times that of I, ...", the text proposed in fix-F3.md; the proof''s Consequences paragraph states the condition. Exact check (GA.py, Cl(2,4), n0 . ninf = 1): for I = ninf + (Lambda/6) n0 at Lambda = 3, -6/5, 0 and c = 2, -3/2, 0, Q(cI) = c^2 Lambda/3 and the top slot of cI is c; at c = 0, I'' = 0 and its top slot vanishes identically, so I'' has no Einstein scale and the Consequently clauses need c != 0. No check asserts c = 0.'
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Blind referee F3: accept with fixes. Applied (5a): the proof cites Fact synthesis.imported-gtg-dictionary (v) for the Weyl decomposition with Sch = (Lambda/6) id; added to uses at version 2 (imported). Applied (5b): one sentence now says why computing with the field whose derived metric is the Einstein scale g loses nothing (another representative of [g] has a tractor gauge field related by a parabolic gauge rotor U, Theorem synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection (i) and its closing gauge law, and V -> U V U~ carries parallel tractors to parallel tractors); that Theorem, proved, is cited for this step and was added to uses at version 1. No mathematics changed; check unchanged (the referee recomputed the Schwarzschild-de Sitter tractor field strength -W, the rank-4 kernel map and the type N kernel symbolically, and two mutations of check_gtg_tractor_field_strength_is_minus_weyl fail). Not applied (formal, for Leon): the Consequently clauses need c != 0.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'GTG proof made the main proof: on the Einstein region P = (Lambda/6) id, so Omega_T(a) = Omega(a) + u ^ hb^{-1}(a) with the constant u = (Lambda/6) n0 - ninf, Q(u) = -Lambda/3; its field strength is R(a ^ b) + u ^ (torsion) + (Lambda/3) hb^{-1}(a) ^ hb^{-1}(b), so F_T(hb(X)) = -calR(X) + (Lambda/3) X = -W(X) (no Cotton or ninf block); a parallel I'' has W(X) . mu'' = 0, the no-kernel hypothesis gives mu'' = 0 near x0, and D^T_a I'' = (a . grad sigma'') ninf + (a . grad rho'') n0 - (u . I'') A forces I'' = c I. The examples use the store-sign Schwarzschild operator; the slot computation is kept as a labelled reading. New check check_gtg_tractor_field_strength_is_minus_weyl (library tractor field strength of the static Schwarzschild-de Sitter field at Lambda = 3/7 and 0 on exact jets equals -W with spacetime blades only, rank-four kernel map, a type N Weyl map with k in its kernel, the algebraic step); runcheck 4/4, check4 clean on a proposals copy. The proof cites the dictionary Fact for the Weyl decomposition, not in uses (a links question left for Leon). outside_ga removed: no stand-in remains. Statement, status, links unchanged.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The proof integrates the tractor parallelism equations in scale-g components (Schouten tensor P_ab, Weyl tensor W_{cabd}, commutators of nabla_a); on flat spacetime the connection is the Cl(2,4) gauge field Omega_T of synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection, and the component integration is the evidence (reader R05).'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 3 -> 4.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the general conformal manifold is kept and its case for a gravitational field on flat spacetime named (a connected open subset of the invertible region with the conformal class of the derived metric, the tractor connection the Cl(2,4) gauge field, the Weyl tensor the trace-free part of the field strength); content unchanged. Checks untouched. Fix (referee GR2, 2026-10-23): the proof prefix reads the gravitational field on flat spacetime as a case, the statement keeping the general conformal manifold.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: pr.p1-single-frozen-point
  note: >-
    Reduces the metric clause of P1 to three ingredients, none of which is a choice of frozen point:
    every tower's frozen point is parallel for the one tractor connection of the shared conformal
    structure; somewhere the Weyl tensor has no kernel vector (true at every point of a
    Schwarzschild or Schwarzschild-de Sitter exterior with M not zero, whose tidal tensor is
    (M/r^3) diag(-2,1,1), cited from memory as standard); and the frozen points share their norm.
    Then the frozen points are proportional with constant ratio, so the towers' Einstein metrics agree up
    to a constant factor and their walls coincide; the residue of P1's metric clause is the normalisation
    constant per tower. Some hypothesis on the Weyl tensor is needed: in a conformally flat region the
    tractor connection is flat and admits six independent parallel tractors (the de Sitter model filed
    alongside, synthesis.two-frozen-points-conformally-flat); at a type N point the null propagation
    vector is a kernel vector, and whether points of type N or III allow several parallel tractors is not
    decided. The argument covers Lambda = 0 (null frozen point, Ricci-flat scale) as well, so the
    Schwarzschild exterior itself is an instance. The orientation clause of P1 (one Witt flag) is not addressed. Transport-convenient:
    the statement is tractor calculus; the transport reading is that one parallel frozen point is all
    the curved geometry permits. Whether every tower's frozen point is parallel for the same
    connection (shared conformal structure) is the remaining structural input and a decision for Leon.
---

## formal
Let $(M, [g])$ be a connected four-dimensional conformal manifold with its tractor connection $\nabla$ (Fact \claimref{dark-energy.imported-frozen-point-geometry}); for a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $M$ is a connected open subset of the invertible region with the conformal class of the derived metric, $\nabla$ is the $\Cl(2,4)$ gauge field $\Omega_{T}$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, and the Weyl tensor below is the trace-free part $\mathcal{W}$ of the field strength, and let $I$ be a parallel tractor with $Q(I) = \Lambda/3$ ($\Lambda = 0$ allowed, $I$ then null), so that on its Einstein region, in the scale $g$ it determines, $I = (1, 0, \Lambda/6)$, $g$ is Einstein with $\Ric = \Lambda g$ and $P_{ab} = (\Lambda/6) g_{ab}$. Suppose that at some point $x_0$ of that region the Weyl tensor has no kernel vector: $W_{abcd} v^d = 0$ for all $a, b, c$ implies $v = 0$. Then every tractor $I'$ parallel for $\nabla$ is a constant multiple of $I$, $I' = c\, I$. Consequently, for $c \neq 0$, the Einstein scale of $I'$ is $c$ times that of $I$, the metrics agree up to the constant factor $c^{-2}$, their zero sets (the walls where the scale vanishes) coincide, and $Q(I') = c^2 \Lambda/3$.

Applied to towers: if the frozen points $I_r$ of all towers are parallel for the one tractor connection of a shared conformal structure ($[g]$, or $[-g]$ for the reversed signature, which has the same parallel tractors), and the universe contains one point of the Einstein region at which the Weyl tensor has no kernel vector, then $I_r = c_r I$ for constants $c_r$, and the metric clause of Premise \claimref{dark-matter.p1-single-frozen-point} holds exactly when the frozen points share their norm, $c_r = \pm 1$. Every point of a Schwarzschild ($\Lambda = 0$) or Schwarzschild-de Sitter ($\Lambda > 0$) exterior with $M \neq 0$ has the no-kernel property. The no-kernel property fails at points of Petrov type N (the null propagation vector is a kernel vector) and on regions where the Weyl part of the field strength vanishes (conformally flat derived metric); on the latter uniqueness itself fails, the tractor connection being flat with a six-dimensional space of parallel tractors.

\emph{Note (scope, 2026-11-11).} $\nabla$ here is the normal tractor connection, for which a tractor is parallel in the physical scale only on Einstein regions, so the application to towers above concerns frozen points parallel for that connection, that is Einstein regions. Under Premise \claimref{synthesis.field-space-premise-parallel-frozen-point} (FS) the frozen point is carried by the connection $A_{\rho}$; the corresponding statement, which reduces to this one on Einstein fields with the same $\Lambda$, is Theorem \claimref{synthesis.frozen-point-unique-for-the-field-space-connection}.

## technical
A parallel tractor is annihilated by the curvature of the tractor connection, which for a gravitational field on flat spacetime is the field strength of its $\Cl(2,4)$ gauge field. In an Einstein scale that curvature acts as the Weyl tensor on the middle slot of a tractor and kills the other two, the Cotton terms vanishing because the Schouten tensor is a constant multiple of the metric. So where the Weyl tensor has no kernel vector the middle slot of every parallel tractor vanishes; by continuity this holds on an open set, where the parallel transport equations then force the top slot to be constant and the bottom slot to equal $\Lambda/6$ times it. A parallel tractor that is a constant multiple of $I$ on an open set is that multiple everywhere on a connected manifold. Hence the gravitational field admits one frozen point up to a constant factor.

For the towers this reduces the metric clause of P1 to a shared conformal structure, one point where the Weyl tensor has no kernel vector (any point near a black hole qualifies), and a common normalisation of the frozen points; the normalisation is the residue. Some hypothesis on the Weyl tensor is needed: where the Weyl part of the field strength vanishes uniqueness fails, a universe with vanishing Weyl part admitting two frozen points with different Einstein metrics (filed alongside, synthesis.two-frozen-points-conformally-flat); whether points of type N or III also allow several parallel tractors is not decided here. The argument holds for every value of $\Lambda$, zero included. The orientation clause of P1 is a separate matter not treated here.

## lay
The series assumes that every hidden sector of the universe feels the same gravity, because they all share one special frozen point fixed at the universe's origin. This result shows that much of that assumption follows from the presence of genuine tidal gravity somewhere, such as around any black hole. Where gravity stretches and squeezes in the way it does near a star, the geometry permits only one frozen point, up to an overall scale. So if every sector's frozen point is compatible with the same shape of spacetime, they must all be the same point, apart from a single number per sector setting its scale. In a universe with no tidal gravity at all, by contrast, there would be room for several different frozen points.

## one-liner
If every tower's frozen point is parallel for one tractor connection and somewhere the Weyl tensor has no kernel vector (as at any Schwarzschild or Schwarzschild-de Sitter exterior point), the frozen points are constant multiples of one another, so P1's metric clause reduces to a common normalisation.
