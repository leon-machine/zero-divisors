---
id: synthesis.no-120-excludes-hierarchical-second-stage
kind: claim
version: 1
title: At the S3 to S2 direction and the breaking lemma's order, on real textures, no 120 makes every second stage one type, so the solar angle excludes Premise (H) and (H) needs a 120
status: proved
region: synthesis
subject: neutrinos
tags: [flavour-and-mixing, seesaw-and-majorana]
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
review: draft
derivations:
- name: main
  uses:
  - synthesis.solar-angle-light-plane-sum-rule@1
  - standard-model.imported-clebsch-structure-seesaw@1
  - standard-model.neutrino-dirac-matrix-charged-fermions@6
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_no_120_stages_are_one_type
- kind: check
  ref: check.py::check_hierarchy_bound_fails
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.solar-angle-light-plane-sum-rule
  - neutrino.h-second-stage-hierarchical
extraction:
  open_problem: op.second-order-breaking
  note: >-
    Largely a corollary of the stored solar-angle sum rule, whose clauses (iii) and (iv) already
    exclude one-type second stages under (H). What is added: the inverted bound m1/m2 > 0.0874 that
    the measured solar angle forces on one-type stages; the identification, through the imported
    Clebsch structure, of the symmetric one-type case with the absence of a 120; and the consequence
    for the Standard-Model paper's elimination of the neutrino Dirac matrix, which as stated needs no
    120. With a 120 the neutrino Dirac matrix is fixed by the charged fermions only up to the 120's
    neutrino coefficient. Scope: the S3 -> S2 direction, the sum rule's order and its real textures;
    whether the bound survives on the root past the peak of m2/m3, where the lemma's remainders
    dominate, is open. The antisymmetric one-type stage is treated as the twin of the symmetric one in
    the result filed alongside, synthesis.one-type-second-stages-are-twins. Transport-absent.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Work at the $S_{3} \to S_{2}$ direction with the textures of Proposition \claimref{synthesis.solar-angle-light-plane-sum-rule}: $M_{e} = c(\J + \delta_{c}(E + X_{e}))$, $\mD = d(\J + \delta(E + X_{\nu}))$, $M_{R} = \alpha\Pi + M_{3}\J/3$, each $X_{s}$ real and odd under $P_{12}$, at the breaking lemma's order. Assume Hypothesis (S) and the imported Clebsch structure (Fact \claimref{standard-model.imported-clebsch-structure-seesaw}).
\begin{enumerate}
\item[(i)] \emph{(No $120$ means one type.)} With $10$s and a $126$ only, $M_{e} = \sum_{a}v_{d}^{a}Y_{a} - 3w_{d}f$ and $\mD = \sum_{a}v_{u}^{a}Y_{a} - 3w_{u}f$ are combinations of symmetric family matrices, so they are symmetric, and so are $X_{e}$ and $X_{\nu}$; in the sum rule's light-plane compression this is $y_{s} = x_{s}$ in both sectors. A $120$ coupling $h$ (antisymmetric) adds to $X_{s}$ an antisymmetric part proportional to $c_{s}h$, the only source of $y_{s} \neq x_{s}$. The one-type case of the sum rule therefore includes the absence of a $120$ (it also includes the purely antisymmetric stages, which need one).
\item[(ii)] \emph{(The solar angle then excludes (H).)} Without a $120$, clause (iii) of the sum rule applies, $\Delta \le \arctan\sqrt{m_{e}/m_{\mu}} + \arctan(m_{1}/m_{2})^{1/4}$, and the global fit's three-sigma edge $\cos^{2}\Delta = |U_{e1}|^{2} \le 0.711$ forces
\[
\frac{m_{1}}{m_{2}} \;>\; \Bigl(\frac{0.6375 - 0.06955}{1 + 0.6375 \times 0.06955}\Bigr)^{4} \;>\; 0.0874,
\]
which violates the inequality $m_{1}/m_{2} \lesssim 0.01$ of Premise (H) (\claimref{neutrino.h-second-stage-hierarchical}) by a factor above $8.7$.
\item[(iii)] \emph{(Consequence for the elimination.)} Hence, at this direction and order, Premise (H) and the measured solar angle require a $120$ in at least one sector. The elimination of Proposition \claimref{standard-model.neutrino-dirac-matrix-charged-fermions}, which fixes $M_{\nu}$ by the charged fermions, is stated for no $120$ and so does not hold as stated together with (H); with a $120$, $M_{\nu}$ is fixed by the charged fermions only up to the $120$'s neutrino coefficient $c_{\nu}$.
\end{enumerate}

## technical
This is largely a corollary of the stored solar-angle sum rule. That rule bounds the angle between the lightest charged lepton and the lightest neutrino when each sector's second-stage breaking is purely symmetric or purely antisymmetric, and it already excludes such stages under Premise (H). Two things are added. First, without a $120$ the Pati-Salam Clebsch structure builds every Dirac matrix from the $10$s and the $126$, whose family couplings are symmetric, so both second stages are symmetric and the rule applies. Second, inverting the rule against the measured solar angle gives $m_{1}/m_{2} > 0.0874$ for such stages, nearly nine times the bound $0.01$ of (H).

So, at the $S_{3} \to S_{2}$ direction, at the breaking lemma's order and on its real textures, Premise (H) needs an antisymmetric coupling, a $120$, in at least one sector. The Standard-Model paper's elimination of the neutrino Dirac matrix is stated without a $120$; with one, the neutrino Dirac matrix is fixed by the charged fermions only up to the $120$'s neutrino coefficient. Whether the bound survives beyond the lemma's order is open.

## lay
Two assumptions in the series pull against each other. One, from the Standard-Model paper, lets the neutrino's mass pattern be computed from the charged particles, in the form in which it is stated, without a particular extra ingredient (called a 120). The other, from the neutrino paper, says the lightest neutrino is much lighter than the next one, by a factor of at least a hundred. This result shows that, in the simplest arrangement of the masses and to the accuracy of the approximation used, the measured size of one neutrino mixing angle makes these incompatible: without the extra ingredient the mixing angle forces the lightest neutrino to be at least about an eleventh as heavy as the next. So either the extra ingredient is present, and the neutrino pattern is computable from the charged particles only up to one further number, or the lightest neutrino is not as light as the second assumption says.

## one-liner
At the $S_{3} \to S_{2}$ direction, the breaking lemma's order and on real textures, no $120$ makes both second stages symmetric, so the solar sum rule and the measured $\theta_{12}$ force $m_{1}/m_{2} > 0.0874$, contradicting Premise (H): (H) needs a $120$, with which $M_{\nu}$ is fixed by the charged fermions only up to the $120$'s neutrino coefficient.
