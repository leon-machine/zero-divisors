---
id: standard-model.transported-frozen-point-doublet-datum-not
kind: claim
version: 8
title: The transported frozen point is a doublet datum, and not the Yukawa sector
status: proved
region: standard-model
subject: mass
tags:
- frozen-point
- flavour-and-mixing
- undetermined-input
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.grip-mass-two-rung-module@7
  - standard-model.imported-grip-area-casimir-form@5
  - standard-model.imported-tower-commuting-copies-fock-module@6
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_rung_plane_is_two_conjugate_doublets
- kind: check
  ref: check.py::check_real_rung_vector_stabiliser
- kind: check
  ref: check.py::check_mixed_bivectors_join_sectors_off_diagonal
- kind: check
  ref: check.py::check_bilinear_pairing_joins_yukawa_pairs
locators:
  paper: T12
  number: Prop 9.21
  label: prop:transported
  line: 1688
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Clause (ii) corrected: a real rung vector c = alpha.v + beta.w breaks the slot U(2) to a U(1) only when beta is a multiple of conj(alpha) and completely otherwise (c = v_4 + w_5 has trivial stabiliser; computed exactly); own exact check added for (i), the corrected (ii) and (iii). Version 5 -> 6. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 6 -> 7. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 7 -> 8.'
  env: proposition
  context_refs:
  - standard-model.grip-mass-two-rung-module
  - standard-model.imported-tower-commuting-copies-fock-module
  - standard-model.reduction
  typing:
    by: ai-typing-pass
    added:
    - standard-model.grip-mass-two-rung-module
    - standard-model.imported-tower-commuting-copies-fock-module
    - standard-model.hyp-s-slot-statistics
    note: 'Added the grip-mass theorem (pure-sector masses are kept from it) and the tower Fact (the hypothesis
      that rung generators are constants), both from context_refs; left out the reduction, cited only
      in the closing interpretive sentence. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S) (for the species reading). Levels pass: lay
      and one-liner now keep the fixed-frames hypothesis and Hypothesis (S) for the species reading; lay
      adds the first-order qualifier.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.grip-mass-two-rung-module
    - standard-model.imported-tower-commuting-copies-fock-module
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
about:
- obj.standard-model.two-rung-module-sectors-slot-components
---

## formal
Let the tower be built with its frames fixed, so that the rung generators are constants (Fact \claimref{standard-model.imported-tower-commuting-copies-fock-module}) and the transported ambient bundle is $V \oplus \R^{2,2}$ with the rung plane a trivial flat summand. Then:
\begin{enumerate}
\item[(i)] the parallel sections of the transported ambient bundle are $I \oplus c$ with $I$ parallel in $V$ and $c \in \R^{2,2}$ constant; the mass paper's frozen point is the parallel scale tractor of the ground conformal structure, so it has $c = 0$ by definition, and a nonzero $c$ is a datum the conformal structure does not fix;
\item[(ii)] under $S(U(2) \times U(3))$, $\R^{2,2} \otimes \C = R_{2} \oplus \overline{R}_{2} = (2,1)_{1/2} \oplus (2,1)_{-1/2}$: a rung component is a weak doublet of hypercharge $\pm\tfrac12$, the quantum numbers of the Higgs doublet; and a nonzero real $c = \alpha\cdot v + \beta\cdot w$ breaks the slot mixing $U(2)$ to a $U(1)$ when $\beta$ is a multiple of $\bar\alpha$ (for instance $c$ along one rung, as for the frozen point's lift), and breaks it completely otherwise;
\item[(iii)] the grip on $I \oplus c$ is $P = M(I) + M(c)$, and the generators $A(U \wedge c)$, $U \in V$, are mixed bivectors, a vector of $V$ times a vector of the rung plane, acting as $x_{W} \otimes y_{R}$: they change the rung number and the pair number by one each and have no matrix element within any sector. Hence pure-sector states keep the masses of Theorem \claimref{standard-model.grip-mass-two-rung-module} at first order in $c$, and the mass-squared acquires cross terms only between slot-doublet and slot-singlet sectors of one chirality: under Hypothesis (S), on the generation, between $Q$ and each of $\nu^{c}, u^{c}, e^{c}, d^{c}$, and between $L$ and $u^{c}, d^{c}$, never between $L$ and $e^{c}$ or $\nu^{c}$. This is not the pattern of the Yukawa couplings, which pair $L$ with $e^{c}$ and $\nu^{c}$; but the grip is a sesquilinear moment, and a mass term between two Weyl species is a bilinear, the invariant pairing of two sixteens through a vector, and through that pairing the same rung component joins exactly the Yukawa pairs, a computation Section \ref{subsec:yukawa} carries out.
\end{enumerate}
So a rung component is exactly what would make the frozen point sensitive to the slots, it has the Higgs doublet's quantum numbers, it is not fixed by anything derived in the series, and it is a Higgs in the sense that matters, the mass-term sense, though not in the grip's: the scalar sector of Proposition \claimref{standard-model.reduction} has, in the frozen point completed, a candidate Sections \ref{subsec:yukawa} and \ref{subsec:lift} take up.

## technical
Build the tower with its frames fixed, so that the transported ambient bundle is $V \oplus \R^{2,2}$ with a flat rung summand. Its parallel sections are $I \oplus c$ with $I$ parallel in $V$ and $c$ constant; the mass paper's frozen point has $c = 0$ by definition, so a nonzero $c$ is a datum the conformal structure does not fix. Under $S(U(2) \times U(3))$, $\R^{2,2} \otimes \C = (2,1)_{1/2} \oplus (2,1)_{-1/2}$, so $c$ has the Higgs doublet's quantum numbers, and a nonzero real $c = \alpha\cdot v + \beta\cdot w$ breaks the slot mixing $U(2)$ to a $U(1)$ when $\beta$ is a multiple of $\bar\alpha$ (for instance $c$ along one rung, as for the frozen point's lift), and breaks it completely otherwise.

The grip on $I \oplus c$ is $M(I) + M(c)$, and the generators $A(U \wedge c)$ change rung and pair number by one each, so pure-sector states keep their masses at first order in $c$ and cross terms join only slot-doublet and slot-singlet sectors of one chirality: under Hypothesis (S), $Q$ with all four singlets and $L$ with $u^{c}, d^{c}$ only. That is not the Yukawa pattern, which pairs $L$ with $e^{c}$ and $\nu^{c}$; the Yukawa pairs arise instead through the bilinear pairing of two sixteens through a vector, not through the sesquilinear grip.

## lay
If the tower is built with its frames held fixed, the larger structure made by transport allows the frozen point to carry an extra constant piece in the new directions. That piece has exactly the charges of the Higgs doublet, but nothing in the series fixes it. Put into the series' grip-based mass formula it leaves the single-sector masses unchanged at first order and, reading the states as one generation under Hypothesis (S), couples the wrong pairs of particles; it gives the Standard Model's pattern only in the different, bilinear form in which a mass term between two particles is built.

## one-liner
With the tower's frames fixed, a rung component of the transported frozen point is an unfixed datum with the Higgs doublet's quantum numbers, which under Hypothesis (S) does not give the Yukawa pattern through the grip but does through the bilinear pairing.
