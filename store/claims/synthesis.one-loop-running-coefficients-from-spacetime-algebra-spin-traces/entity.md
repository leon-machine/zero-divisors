---
id: synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces
kind: claim
version: 3
title: 'One-loop running coefficients from spacetime-algebra spin traces'
status: proved
region: synthesis
subject: quantum-fields
tags: [running-and-unification, gauge-fields, recovers-known-physics, spinor-modules]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (unit of the gauge generators)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - field-theory.second-quantisation@5
  - field-theory.fock-space-maxwell-modes@4
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.imported-one-loop-running-trace-ratio@1
  - synthesis.imported-heat-kernel-coefficients-and-background-field-gauge@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_spin_weights_from_lorentz_generator_traces
- kind: check
  ref: check.py::check_b_weights_per_field_and_ghost_cancellation
- kind: check
  ref: check.py::check_gauge_indices_of_the_derived_algebra
- kind: check
  ref: check.py::check_running_coefficients_of_the_derived_content
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.imported-coefficient-sum-indices
  - standard-model.spectrum-run
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Reader fix (R06): the field of the hermitian gauge generators in proof (3) is written span_Q{1, I_4} (it was Q(i), a bare unit); the remaining indices are components on the STA frame and stay; the mathematics is unchanged.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s decisions of 2026-11-01: an assumes edge to the Krein-form premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@1, which this result states as its hypothesis (the indefinite-form premise of the covariant background Feynman gauge, now cited by claimref at the formal and technical levels and in the proof), and a uses edge to the imported Fact synthesis.imported-heat-kernel-coefficients-and-background-field-gauge@1 (the heat-kernel coefficient, the background-field gauge with ghosts and the determinant weights), which replaces the citation from memory. Statement and check unchanged.'
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    The problem's second attack line (the one-loop beta coefficient of the non-abelian factors and its sign),
    which also serves op.qft-loops-and-renormalisation (the beta coefficients of the derived group with the
    derived content). The store imported the coefficient formula b = -11/3 C2 + 2/3 sum T(Weyl) + 1/3 sum
    T(complex scalar) (standard-model.imported-coefficient-sum-indices, Weinberg vol. II) and evaluated it on
    the derived content (standard-model.spectrum-run). Here the formula's three coefficients are computed:
    the spin coupling of each one-loop operator in a background gauge field is twice the Lorentz generator of
    the field-strength bivector in the field's spin representation, and its trace is a Clifford computation
    (left multiplication on a minimal left ideal of the even algebra, which with the unit I4 is one Weyl
    spinor; a -> a . F on vectors). The bookkeeping that turns spin weights into b is imported
    (synthesis.imported-heat-kernel-coefficients-and-background-field-gauge): the heat-kernel
    coefficient (1/12) Omega^2 + (1/2) E^2 on a flat background (a_2 in DeWitt's numbering, a_4 in
    Vassilevich's, Phys. Rep. 388 (2003), his general form (4.15)), the background-field gauge with
    Faddeev-Popov ghosts (Abbott 1981), and the determinant weights. The background Feynman gauge with its
    ghosts is a covariant gauge and presupposes the indefinite (Krein) form for the gauge field, the premise
    adopted for covariant gauges (synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields); the ghost subtraction is the one of the gauge-fixing result filed
    alongside (synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts, clause
    (iv)). The Dirac weight 4/3 agrees with the vacuum-polarisation coefficient e^2/(12 pi^2) of the one-loop
    electrodynamics result (synthesis.one-loop-qed-in-the-spacetime-algebra). The content is
    recomputed from the stored hypercharge rule (component (j, k) has Y = (3j - 2k)/6, under (S)); the number
    of generations n_g (three is conjectured in the store) and of complex doublets n_h of hypercharge 1/2
    (the rung field's count; recorded as two, the elementary linear field with two doublets) are inputs. At
    (3, 1) the values (41/10, -19/6, -7) agree with the imported running; at (3, 2) they are (21/5, -3, -7).
    Asymptotic freedom of both non-abelian factors does not depend on the doublet count: at n_g = 3 it holds
    for every n_h <= 19; only b_1 and b_2 shift. Transport-absent: no transport structure enters; the
    spacetime algebra is convenient (one trace per spin, the Weyl trace an I4-complex number 2F^2 whose I4
    part is the parity-odd F ^ F). Nothing here quantises the gluons as states; that is the rest of the open
    problem.
---

## formal
Work in a covariant gauge (the background Feynman gauge with Faddeev-Popov ghosts), under the indefinite-form (Krein) premise for the gauge field, Premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}. Let $F = \sum_{\mu<\nu}F^{\mu\nu}\gamma_{\mu}\gamma_{\nu}$ be a field-strength bivector of $\Cl(1,3)$ and $X = F_{\mu\nu}F^{\mu\nu}$, so that $\langle F^{2}\rangle_{0} = -X/2$. Let $M(F)$ be its Lorentz generator in a field's spin representation: $a \mapsto a\cdot F$ on vectors, $\psi \mapsto \tfrac12F\psi$ on the minimal left ideal $\Cl^{+}(1,3)P$, $P = \tfrac12(1 + \gamma_{3}\gamma_{0})$, which is $I_{4}$-stable and so, with the unit $i = I_{4}$ of Definition \claimref{obj.field-theory.single-algebra-field}, a two-dimensional complex space (one Weyl spinor). Define the spin weight $s = 4\,\mathrm{Re}\,\mathrm{tr}\,M(F)^{2}/X$. Then:
\begin{enumerate}
\item $s = 0$ for a scalar, $-1$ for the Weyl ideal, $-2$ for the whole even algebra (a Dirac field of Proposition \claimref{field-theory.second-quantisation}, two ideals of one chirality with $i = I_{4}$) and $-4$ for a vector; on the Weyl ideal the $I_{4}$-complex trace of the squared spin coupling $E = 2M(F)$ is $2F^{2} \in \mathrm{span}\{1, I_{4}\}$, whose $I_{4}$ part is the parity-odd $F \wedge F$.
\item With the heat-kernel coefficient $\tfrac{1}{12}\Omega_{\mu\nu}\Omega^{\mu\nu} + \tfrac12E^{2}$ of a Laplace-type operator on a flat background (imported, Fact \claimref{synthesis.imported-heat-kernel-coefficients-and-background-field-gauge}; $a_{2}$ in DeWitt's numbering, $a_{4}$ in Vassilevich's), a field with $n$ components, statistics $\sigma$ and determinant weight $w$ contributes $b = \tfrac13\sigma w(n + 6s)$ per unit index: $\tfrac13$ for a complex scalar, $\tfrac23$ for a Weyl spinor, $\tfrac43$ for a Dirac spinor, $-\tfrac{10}{3}$ for the gauge vector in the background Feynman gauge and $-\tfrac13$ for its Faddeev-Popov ghosts, so $-\tfrac{11}{3}$ for the gauge field, split as $+\tfrac13$ orbital and $-4$ spin.
\item For the derived algebra $\su(2) \oplus \su(3) \oplus \uu(1)$ of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} acting on $\C^{2}$ and on $\Lambda^{k}\C^{3}$: $T = \tfrac12$ on $\C^{2}$, $\C^{3}$ and $\Lambda^{2}\C^{3}$, $T = 0$ on $\Lambda^{0}$ and $\Lambda^{3}$, and $C_{2} = 2$, $3$ for the adjoints; for $\su(2)$ as the bivectors of $\Cl(3,0)$ acting on the even algebra (a doublet with the central unit $e_{1}e_{2}e_{3}$) and on the bivectors, $C_{2}/T = 4$.
\item Under (S), with $n_{g}$ copies of the content of Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency} and $n_{h}$ complex doublets of hypercharge $\tfrac12$, both counts inputs, in the normalisation $a_{1} = \tfrac35\alpha_{Y}^{-1}$ of Fact \claimref{standard-model.imported-one-loop-running-trace-ratio},
\[
(b_{1}, b_{2}, b_{3}) = \Bigl(\tfrac{4n_{g}}{3} + \tfrac{n_{h}}{10},\; -\tfrac{22}{3} + \tfrac{4n_{g}}{3} + \tfrac{n_{h}}{6},\; -11 + \tfrac{4n_{g}}{3}\Bigr),
\]
which is $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$ at $(n_{g}, n_{h}) = (3, 1)$, the imported values, and $(\tfrac{21}{5}, -3, -7)$ at $(3, 2)$. The $\su(3)$ factor is asymptotically free exactly when $n_{g} \leq 8$ and the $\su(2)$ factor exactly when $8n_{g} + n_{h} < 44$; at $n_{g} = 3$ both are, for every $n_{h} \leq 19$.
\end{enumerate}

## technical
In a covariant gauge, under the indefinite-form (Krein) premise for the gauge field (\claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}), the spin coupling of every one-loop operator in a background gauge field is twice the Lorentz generator of the field-strength bivector $F$ in the field's spin representation, and its trace is a Clifford computation: on vectors ($a \mapsto a\cdot F$) the spin weight $s = 4\,\mathrm{Re}\,\mathrm{tr}\,M(F)^{2}/X$ is $-4$; on a minimal left ideal of the even algebra, which with the unit $I_{4}$ is one Weyl spinor, it is $-1$, the $I_{4}$-complex trace of the squared coupling being $2F^{2}$ with $I_{4}$ part $F \wedge F$; on the whole even algebra it is $-2$; on a scalar $0$.

With the imported heat-kernel coefficient $\tfrac{1}{12}\Omega^{2} + \tfrac12E^{2}$ and the background-field bookkeeping (\claimref{synthesis.imported-heat-kernel-coefficients-and-background-field-gauge}) with Faddeev-Popov ghosts, each field contributes $\tfrac13\sigma w(n + 6s)$ per unit index: $\tfrac13$ (complex scalar), $\tfrac23$ (Weyl), $-\tfrac{11}{3}$ (gauge field and ghosts). With the indices of the derived algebra computed on $\C^{2}$ and $\Lambda^{k}\C^{3}$ and, under (S), the derived content with $n_{g}$ generations and $n_{h}$ doublets taken as inputs, $b = (\tfrac{4n_{g}}{3} + \tfrac{n_{h}}{10}, -\tfrac{22}{3} + \tfrac{4n_{g}}{3} + \tfrac{n_{h}}{6}, -11 + \tfrac{4n_{g}}{3})$: $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$ at three generations and one doublet, $(\tfrac{21}{5}, -3, -7)$ at two doublets. Colour is asymptotically free for $n_{g} \leq 8$ and the weak factor for $8n_{g} + n_{h} < 44$, so at three generations both are for every $n_{h} \leq 19$.

## lay
How fast the strengths of the forces change with energy is fixed, at the first quantum correction, by a sum over the particles, each weighted by a number that depends on its spin. Those weights come out of the series' algebra of spacetime as traces of how a field's spin responds to a force field, once a standard heat-kernel formula and the standard covariant treatment of the force fields are taken from the literature. The number of generations and of Higgs doublets are inputs, since the store has not settled either. Applied to the particle content the series derives under its slot hypothesis, three generations with one doublet give the standard values and two doublets give slightly different ones; with three generations the strong and weak forces weaken at high energy for any number of doublets up to nineteen. The gluons and the weak bosons are not yet built as quantum states here.

## one-liner
In a covariant gauge under the indefinite-form premise, spin traces in the spacetime algebra give the one-loop weights $\tfrac13$, $\tfrac23$, $-\tfrac{11}{3}$, and under (S) with $n_{g}$ generations and $n_{h}$ doublets as inputs the derived content gives $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$ at $(3, 1)$ and $(\tfrac{21}{5}, -3, -7)$ at $(3, 2)$, asymptotically free in colour and weak isospin for every $n_{h} \leq 19$ at three generations.
