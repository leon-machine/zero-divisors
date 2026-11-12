---
id: dark-matter.mirror-share-one-how-fragile
kind: claim
version: 8
title: The mirror share is one, and how fragile that is
status: proved
region: dark-matter
subject: dark-matter
tags: [dark-matter-ratio, mirror-sector, hypothesis-u, needs-continuum]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, share protection restated onto the common-ceiling-coupling premise at Leon''s decisions'
  version: 7
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: 'restatement of clauses (i) and (ii) at the maintainer''s decision: exactness is of the mass factor; f_2 = 1 holds under the hypothesis of equal conversion'
  version: 8
  source: maintainer pass 2026-11-12 (asymmetry)
amendments:
- version: 8
  kind: restatement
  defect: 'clauses (i) and (ii) stated f_2 = 1 as following from the equal asymmetry per mode; by the maintainer''s decision of 12 November 2026 the inherited charge is B - L, the copy equates the two towers'' B - L and not their baryon number, so the share of one needs in addition that the mirror''s ratio of baryon number to B - L equals this tower''s, which is not shown. Restated as conditional on that hypothesis; no number changed. The word exact applies to the mass factor.'
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-tower-copy-one@11
  - dark-matter.no-coupling-rule-odd-towers-follows@6
  - dark-matter.ceiling-valued-inherited-success@5
  assumes:
  - synthesis.common-ceiling-coupling-premise@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:massbound
- kind: check
  ref: check.py::check_mean_mass_per_baryon_share
- kind: check
  ref: check.py::check_one_loop_bound_and_chain
- kind: check
  ref: check.py::check_one_flavour_factors_over_the_ceiling_range
- kind: check
  ref: check.py::check_coupling_departure_window
locators:
  paper: T14
  number: Prop 4.7
  label: prop:massbound
  line: 439
extraction:
  maintainer_pass_2026_11_12:
    by: maintainer-2026-11-12
    date: '2026-11-12'
    note: 'Version 7 -> 8. Leon''s decision of 12 November 2026 on the mirror share: f_2 = 1 is restated as holding under the hypothesis of equal conversion (the mirror''s ratio of baryon number to B - L equals this tower''s; not shown; a stated hypothesis, not a registered premise, no assumes edge), citing clause (i) of dark-matter.stored-asymmetry-charge-not-number at version 11. Clause (i), the closing sentence of (ii), the level line, the technical and lay levels, the one-liner and the first sentence of the proof are restated; the one-loop bound, the factors, clause (iii) and the four checks are unchanged. No number, check or pin is changed; the open item is attack item (d) of op.matter-asymmetry-origin.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited. Pin review: dark-matter.no-coupling-rule-odd-towers-follows repinned 4 -> 5 after reviewing its B2 restatement (the formal is now the three established facts (a) to (c), the claim that no rule follows from the series moved to a marked remark, and (c) names P2, which equates labels and not couplings, and the common-ceiling-coupling premise, both along the reversal orbit only); the use here holds as cited. Pin review (second round): dark-matter.no-coupling-rule-odd-towers-follows repinned 5 -> 6 after reviewing its restatement (direct assumes edge to the common-ceiling-coupling premise dropped; formal unchanged); facts (a) to (c), cited here, are unchanged, and the use here holds as cited.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6 -> 7. Leon''s answer 2 (C1): (i) and (ii) now name the common ceiling and coupling as the new premise synthesis.common-ceiling-coupling-premise (assumes edge added), where (ii) called the share P2-protected; P2 at version 2 does not reach a coupling. Restatement at Leon''s decision.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: mean mass per baryon ratio in (0.994, 0.996); the one-loop relation and inequality chain; one-flavour factors 4.89 and 21.4 over the ceiling range by integer powers; e^(2 pi/7) and the 0.106 window by exact exponential brackets. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6.'
  superseded_in_part_by:
  - dark-tower-matter.mirrors-composition
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: [1, 8]
    note: 'Decision 1: superseded in part by T14c Comp 8.3 (dark-tower-matter.mirrors-composition). Clause
      (i) bracketed the share between 0.995 (helium completion limit of the burning branch) and 1 (proton-only);
      at the gravitational floor T14c finds the mirror degenerate and 96 to 100 percent neutrons for L <= 0,
      a composition neither branch describes, so (i) now carries a caveat that the bracket is established
      where the mirror is helium (xi about 3e-3 to 2e-2) and not at the floor. Decision 8: (U) enters only
      through the ceiling range (clause (ii), the two readings of (U)), so the assumes edge to (U) is replaced
      by uses of the ceiling proposition dark-matter.ceiling-valued-inherited-success, cited in the proof;
      P4 is removed from assumes, since Theorem 4.3(v) (dark-matter.mirror-tower-copy-one, T14 line 332)
      discharges it for the mirror, and the formal, technical, lay and one-liner now say so (CONTRADICTIONS_VALUES
      L1). Original in source_formal and orig-proof-main.tex.'
  source_formal: |-
    Write $m_{r} = c_{r}\Lambda_{r}$, with $\Lambda_{r}$ the confinement scale of tower $r$'s non-abelian sector and $c_{r}$ the constituent factor of its lightest charge-carrying composite.
    \begin{enumerate}
    \item[(i)] \emph{(The mirror.)} By Theorem \claimref{dark-matter.mirror-tower-copy-one}(iii), $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$ exactly, hence $f_{2} = 1$ under P4, an isomorphism of theories rather than a one-loop statement. As a ratio of mass densities it is a ratio of mean mass per baryon: ours is about $936.7$ MeV after helium, a mirror burnt entirely to helium (the completion limit of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}'s burning branch) gives $931.8$ MeV, so $f_{2}$ is $0.995$ in that limit and $1$ on the proton-only branch, a one-sided systematic of half a percent at assembly level.
    \item[(ii)] \emph{(Fragility.)} The equality is unstable to any departure from the copy. Suppose the two towers shared a ceiling $M$ and coupling but differed in light content by $\Delta b$ over the running range, with $b_{6} \leq 11$; then at one loop
    \[
    \ln\frac{\Lambda_{2}}{\Lambda_{6}} \;\geq\; \frac{\Delta b}{b_{6} + \Delta b}\,\ln\frac{M}{\Lambda_{6}}.
    \]
    One Dirac flavour is $\Delta b = 2/3$, which with $\Lambda_{6} = 0.3$ GeV moves the mirror share by a factor between $4.89$ (bottom of the ceiling range, $b_{6} = 11$) and $21.4$ (top, $b_{6} = 7$), past the observed $5.364$ everywhere except at the bottom of the range on the most conservative branch. A coupling departure $\delta = \alpha_{2}(M)^{-1} - \alpha_{6}(M)^{-1}$ at the ceiling with identical content moves $\Lambda_{2}/\Lambda_{6}$ by $e^{-2\pi\delta/b}$, a factor $2.45$ per unit at $b = 7$, so the share stays within ten percent of one only for $|\delta| < 0.106$. So $f_{2} = 1$ is exact, P2-protected, and fragile.
    \item[(iii)] \emph{(The odd towers.)} In three and five dimensions the gauge coupling is dimensionful and the confinement scale is set by the coupling itself ($\Lambda_{3} \sim g_{3}^{2}N$, $\Lambda_{5} \sim 1/g_{5}^{2}$), so nothing about $\Lambda_{1,7,3,5}$ follows without a rule the series does not derive (Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}); the unit-ball rule of Section \ref{sec:rule} constrains that rule, as shares per unit of our volume, without supplying it.
    \end{enumerate}
    Level: (i) is Theorem \claimref{dark-matter.mirror-tower-copy-one}; (ii) is one-loop arithmetic under its stated assumptions, flagged; (iii) is a scope statement.
  env: proposition
  context_refs:
  - dark-matter.no-coupling-rule-odd-towers-follows
  - dark-matter.stored-asymmetry-charge-not-number
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.no-coupling-rule-odd-towers-follows
    - dark-matter.p4-democracy-asymmetry-over-oriented-towers
    - dark-matter.hyp-u-equal-rank-one-eigenvalues
    note: 'Added the no-coupling proposition, on which the odd-tower clause rests, and P4, under which
      clause (i) states $f_2 = 1$; the stored-asymmetry proposition is cited only to name the burning
      branch, so it is not edged; clause (ii) is flagged one-loop arithmetic. Hypothesis pass: assumes
      dark-matter.hyp-u-equal-rank-one-eigenvalues added because the paper names Hypothesis (U) as a condition
      of this result (clause (ii), as the ceiling proposition states). Levels pass: lay rewritten to keep
      P4, the one-loop level of clause (ii) and Hypothesis (U); technical and one-liner now carry (U)
      and the one-loop qualifier.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.no-coupling-rule-odd-towers-follows
    - dark-matter.p4-democracy-asymmetry-over-oriented-towers
    - dark-matter.hyp-u-equal-rank-one-eigenvalues
---

## formal
Write $m_{r} = c_{r}\Lambda_{r}$, with $\Lambda_{r}$ the confinement scale of tower $r$'s non-abelian sector and $c_{r}$ the constituent factor of its lightest charge-carrying composite.
\begin{enumerate}
\item[(i)] \emph{(The mirror.)} By Theorem \claimref{dark-matter.mirror-tower-copy-one}(iii), with the common ceiling and coupling of Premise \claimref{synthesis.common-ceiling-coupling-premise}, $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$ exactly, hence $f_{2} = 1$ under P4, which Theorem \claimref{dark-matter.mirror-tower-copy-one}(v) discharges for the mirror as an equality of the charge $B - L$, and under Hypothesis (equal conversion) stated below; the equality of $\Lambda$ and $c$ is an isomorphism of theories rather than a one-loop statement. As a ratio of mass densities it is a ratio of mean mass per baryon: ours is about $936.7$ MeV after helium, a mirror burnt entirely to helium (the completion limit of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}'s burning branch) gives $931.8$ MeV, so $f_{2}$ is $0.995$ in that limit and $1$ on the proton-only branch, a one-sided systematic of half a percent at assembly level. Caveat (T14c): the two branches bracket the share where the mirror is helium or protons; at the gravitational floor the mirror is degenerate and, for a copied lepton number $L \leq 0$, ends $96$ to $100$ percent neutrons, a composition neither branch describes, and it is helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$ (Computation \claimref{dark-tower-matter.mirrors-composition}); the half-percent bracket is established there and not at the floor.
\item[(ii)] \emph{(Fragility.)} The equality is unstable to any departure from the copy. Suppose the two towers shared a ceiling $M$ and coupling but differed in light content by $\Delta b$ over the running range, with $b_{6} \leq 11$; then at one loop
\[
\ln\frac{\Lambda_{2}}{\Lambda_{6}} \;\geq\; \frac{\Delta b}{b_{6} + \Delta b}\,\ln\frac{M}{\Lambda_{6}}.
\]
One Dirac flavour is $\Delta b = 2/3$, which with $\Lambda_{6} = 0.3$ GeV moves the mirror share by a factor between $4.89$ (bottom of the ceiling range, $b_{6} = 11$) and $21.4$ (top, $b_{6} = 7$), past the observed $5.364$ everywhere except at the bottom of the range on the most conservative branch. A coupling departure $\delta = \alpha_{2}(M)^{-1} - \alpha_{6}(M)^{-1}$ at the ceiling with identical content moves $\Lambda_{2}/\Lambda_{6}$ by $e^{-2\pi\delta/b}$, a factor $2.45$ per unit at $b = 7$, so the share stays within ten percent of one only for $|\delta| < 0.106$. So the mass factor of $f_{2}$ is exactly one, protected by the common-ceiling-coupling premise (Premise \claimref{synthesis.common-ceiling-coupling-premise}), and fragile; $f_{2} = 1$ itself holds under Hypothesis (equal conversion) in addition.
\item[(iii)] \emph{(The odd towers.)} In three and five dimensions the gauge coupling is dimensionful and the confinement scale is set by the coupling itself ($\Lambda_{3} \sim g_{3}^{2}N$, $\Lambda_{5} \sim 1/g_{5}^{2}$), so nothing about $\Lambda_{1,7,3,5}$ follows without a rule the series does not derive (Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}); the unit-ball rule of Section \ref{sec:rule} constrains that rule, as shares per unit of our volume, without supplying it.
\end{enumerate}
\emph{Hypothesis (equal conversion).} The mirror's ratio of baryon number to $B - L$ equals this tower's. It is not shown, and it is a stated hypothesis of this result, not a registered premise: the inherited charge is the total $B - L$, and the copy equates the two towers' $B - L$, not their baryon number (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(i), version 11). The mirror's unit of the observed dark-to-baryon total $5.364$ is conditional on it.

Level: (i) is Theorem \claimref{dark-matter.mirror-tower-copy-one}, with the Hypothesis; (ii) is one-loop arithmetic under its stated assumptions, flagged; (iii) is a scope statement.

## technical
Write $m_{r} = c_{r}\Lambda_{r}$, with $\Lambda_{r}$ the confinement scale and $c_{r}$ the constituent factor of the lightest charge-carrying composite. For the mirror, the copy theorem with the common-ceiling-coupling premise gives $\Lambda_{2} = \Lambda_{6}$ and $c_{2} = c_{6}$ exactly, so $f_{2} = 1$ under the hypothesis of equal conversion (the mirror's ratio of baryon number to $B - L$ equals this tower's, which is not shown), the democracy of the asymmetry being discharged for the mirror by the copy theorem as an equality of $B - L$; the equality of scales is an isomorphism of theories rather than a one-loop statement; as a ratio of mass densities it is $0.995$ for a mirror burnt entirely to helium and $1$ on the proton-only branch. The T14c note finds the mirror helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$ and neutron-rich at the gravitational floor (Computation \claimref{dark-tower-matter.mirrors-composition}), so this bracket does not cover the floor.

The equality is fragile. If the two towers shared ceiling and coupling but differed in light content by $\Delta b$, then at one loop $\ln(\Lambda_{2}/\Lambda_{6}) \ge \frac{\Delta b}{b_{6} + \Delta b}\ln(M/\Lambda_{6})$; one Dirac flavour moves the share by a factor between $4.89$ and $21.4$ across the ceiling range, valued in the ceiling proposition under Hypothesis (U). With identical content a ceiling difference $\delta$ in $\alpha^{-1}$ moves $\Lambda_{2}/\Lambda_{6}$ by $e^{-2\pi\delta/b}$, so the share stays within ten percent of one only for $|\delta| < 0.106$: the mass factor of the share is exactly as strong as the premise that equates the ceiling couplings, and the share of one needs the hypothesis of equal conversion as well; the mirror's unit of the observed $5.364$ is conditional on it. For the odd towers the coupling is dimensionful and sets the confinement scale itself, so nothing about their $\Lambda$ follows without a coupling rule the series does not derive.

## lay
The mirror world's matter weighs exactly as much as ours, because the mirror is an exact copy, with the same particles and the same force strengths at the start, and the copy theorem gives it the same inherited excess, so the premise that the flag imprints one asymmetry on every tower (P4) is not needed for it. By a decision of 12 November 2026 the inherited excess is that of baryons minus leptons, so the equal weight also needs baryons to make up the same fraction of it there as here, which has not been shown. How exact that is depends on what the mirror's matter becomes; a later note (T14c) finds it mostly neutrons rather than helium at its coldest, a case this estimate does not cover. A rough one-loop estimate, over the ceiling range that rests on Hypothesis (U), shows that the equality is fragile: one extra kind of light quark or a slightly different starting strength of the strong force would change the mirror's share by large factors. For the odd-dimensional hidden worlds nothing of this kind can be said without a new rule.

## one-liner
Under the hypothesis of equal conversion (the mirror's ratio of baryon number to $B - L$ equals this tower's, which is not shown), the mirror share is exactly one because the mirror copies this tower (which discharges the democracy premise for it), but at one loop, over the ceiling range of Hypothesis (U), one extra Dirac flavour, or a ceiling coupling difference above about $0.1$, would move it far from one, and nothing follows for the odd towers.
