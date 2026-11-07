---
id: singularity.r-regularity-fixed-locus
kind: claim
version: 3
title: '(R): regularity at the fixed locus'
status: postulate
region: singularity
subject: thermality
tags: [thermal-premises, hawking-temperature, modular-theory]
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
outside_ga:
  kind: complex-analysis
  why: 'the KMS strip F(t + ip) and the phase flow Ad(e^{i t omega_k K_k}) act on the ladders {v_k, v_k^*} of T05''s atom in the spacetime radial plane, whose modes anticommute with I_4 (conventions, known limit 1), so the strip''s unit is the complex scalar of the atom, not the field''s I_4'
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
locators:
  paper: T05
  number: Premise 7.19
  label: prem:reg
  line: 1870
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the KMS strip t + ip and the flow Ad(e^{i t omega_k K_k}) are on the ladders of T05''s atom, which anticommute with I_4 (conventions, known limit 1). Declared complex-analysis.'
  env: premise
  context_refs:
  - singularity.euclidean-section-period
  typing:
    by: ai-typing-pass
    note: 'Postulate with no derivation, so the statement''s reliance on the Euclidean-section proposition (its context_ref) is not recorded as an edge; levels and typing record only.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - $F_{a,b}(t + ip)$ on the KMS strip (complex analysis)
  merged_from:
  - id: state-selection.r-regularity-fixed-locus
    version: 1
    locators:
      paper: T05-state-selection
      number: Premise 5.1
      label: prem:reg
      line: 264
    proof_files: []
    formal: The state's two-point functions, continued analytically in the rapidity parameter of the boost flow, are
      single valued and regular at the fixed locus of that flow, equivalently the state is regular in the frame of
      the infalling observer, whose null dyad has constant unit components at every radius up to the wall \cite[Prop.~8.23,
      Rem.~8.24]{ButlerT4}.
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 2 (Leon''s decisions 1 and 13 of 23 October): adds a note that the continuum restatement of (R), for the eternal hole, follows from the new postulate synthesis.n-plus-null-ground-state by synthesis.positive-null-energy-gives-r-premises (iii), and that this point-spectrum wording is its discretisation; the premise keeps postulate status and its statement is unchanged. Version 1 -> 2.'
  maintainer_pass_2026_10_22:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Merged the state-selection note''s Premise 5.1 (state-selection.r-regularity-fixed-locus, retired to tombstones.yaml)
      into this entity: not the same premise: in its one satisfiable contentful reading on the boundary-mode algebra
      the note''s (R) is T05''s (R) plus vanishing inter-mode two-point functions (synthesis.state-selection-r-and-le-against-t05);
      its one consumer, state-selection.rate-discharge-hypothesis-iii, uses only the single-mode content T05''s (R)
      supplies and now assumes T05''s (R). Kept this statement, levels and checks; the note''s entity is recorded
      above and its proof files are kept in this folder. References to the note''s id were repointed here. Extraction-only
      change, so the version and the dependants'' pins are unchanged.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Euclidean section is that of the Schwarzschild field on flat spacetime, and its regularity is named as regularity at the tip, a local condition (DICTIONARY 14 item 5, Bifurcation surfaces section); a parenthetical points to the flag on (N+) for the eternal hole. Premise content, scope and postulate status unchanged (Leon 2026-10-23). Fix (Leon 2026-10-23, referee GR1): the regularity wording "equivalently, the state is regular across the horizon locus" replaced by "for a state that is KMS for the Killing flow, this is also the period at which it is regular across the horizon locus in the PG chart"; clauses, scope and status unchanged.'
---

## formal
For every mode $k$ and every pair $a, b$ of elements of its ladder $\{v_k, v_k^{*}\}$, the correlation function $F_{a,b}(t) := \omega\bigl(a\,\alpha_t(b)\bigr)$ of the Killing flow $\alpha_t = \operatorname{Ad}(e^{it\omega_k K_k})$, an entire function of $t$, continues in imaginary Killing time to a single-valued function on the regular Euclidean section of the Schwarzschild gravitational field on flat spacetime (Proposition \claimref{singularity.euclidean-section-period}; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}): its two orderings are the two sides of the cut, and they meet after one period,
\[
F_{a,b}\bigl(t + i\,p\bigr) \;=\; \omega\bigl(\alpha_t(b)\,a\bigr), \qquad p = \frac{2\pi}{\kappa} .
\]
In words: each single-mode marginal is KMS for the Killing flow at exactly the period the Euclidean section's smoothness at its tip dictates. The regularity is local, posed at the tip of the Euclidean section (a polar chart about the tip of the Wick-rotated flat background); for a state that is KMS for the Killing flow, this is also the period at which it is regular across the horizon locus in the Painlev\'e-Gullstrand chart.

\emph{Note (continuum restatement).} Posed on the continuum of the horizon's null generators (Definition \claimref{obj.hawking.continuum-mode-space}), the content of (R) for the eternal (Kruskal) hole follows from Premise \claimref{synthesis.n-plus-null-ground-state}: by Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(iii) the generators' modes are then jointly KMS for the Killing flow at $\beta = 8\pi M$. The wording above, on the ladders $\{v_{k}, v_{k}^{*}\}$ with a phase-acting flow, is a discretisation of that statement, recovered only for modes of vanishing Mellin width; (N$_{+}$) itself cannot be posed on point spectrum. A hole formed by collapse is not covered by (N$_{+}$), and (R) remains a premise. (The whole generator of the eternal horizon, which that case of (N$_{+}$) uses, lies beyond one flat chart; see that premise.)

## technical
Premise (R) imposes the KMS condition on each single-mode marginal at a fixed period. For mode $k$, with Killing flow $\alpha_t = \operatorname{Ad}(e^{it\omega_k K_k})$ and $a, b \in \{v_k, v_k^{*}\}$, the entire correlation function $F_{a,b}(t) = \omega(a\,\alpha_t(b))$ is required to continue in imaginary Killing time to a single-valued function on the regular Euclidean section of the Schwarzschild field, its two orderings being the two sides of the cut, which meet after one period: $F_{a,b}(t + ip) = \omega(\alpha_t(b)\,a)$ with $p = 2\pi/\kappa$.

The period is the one that smoothness of the Euclidean section at its tip dictates, a local condition. The condition is imposed on the single-mode marginals only.

On the continuum of the horizon's light rays, for the eternal hole, this content follows from the null ground-state premise (N$_{+}$), which has no temperature in it; the ladder wording here is its discretisation. (R) keeps its status as a premise.

## lay
This is an assumption, not a theorem. It asks that each boundary mode, taken on its own, looks thermal with respect to the black hole's time flow. The temperature is fixed by the gravitational field: it is exactly the one for which the imaginary-time version of the field describes a smooth geometry, with no cone-shaped point.

## one-liner
Premise: each single-mode marginal of the boundary-mode state is KMS for the Killing flow at the period $2\pi/\kappa$ dictated by regularity of the Euclidean section at its tip.
