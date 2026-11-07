---
id: note.singularity.setting-step-5-descend-state-what-2
kind: note
version: 2
title: 'Step 5: descend, and state what descent costs'
status: setting
subject: descent
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: 'GA rewrite (the Pauli-string witness written in the mode algebra)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- singularity.p-reduced-metric-level-reading-many
- singularity.descent-what-it-erases
- singularity.descent-parity-average
- singularity.imported-univalence-superselection-rule
locators:
  paper: T05
  number: Setting
  section: 'Step 5: descend, and state what descent costs'
  line: 2125
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The qubit (Pauli-string) label X_{R1}X_{L1}Z_{L2} is written in the mode algebra as (v_{R1} + v_{R1}*)(v_{L1} + v_{L1}*) sigma_{L2}, two Majorana elements and a parity section, with the qubit label kept as a reading up to the Jordan-Wigner sign string, as reader R09 proposed. Verified exactly with lib/GA.py in Cl(3,3) (three modes): the element commutes with the total parity and is odd under Ad(sigma_{R1}), so it is total-parity even and not joint-diagonal, the two properties the text uses.'
---

## formal
What remains of the former premise is the proposition's antecedent, and it is thin. The metric level was defined pointwise: at each mode it is the image of that mode's descent (Proposition \claimref{singularity.descent-what-it-erases}, Theorem \claimref{singularity.descent-parity-average}), and the localisation attaches exactly one descent to each point of $E$; reading a region of the boundary mode space at the metric level means surviving every one of its points' readings, which is the composite. The total-parity average is not an alternative candidate: it is the composite of nothing the closure constructs, there being no ``global pair'' for it to descend. Nor does the reduction touch Fact \claimref{singularity.imported-univalence-superselection-rule}: the superselection rule continues to constrain observability by total parity, and cross-mode even elements such as $(v_{R_1} + v_{R_1}^{*})(v_{L_1} + v_{L_1}^{*})\,\sigma_{L_2}$ (two Majorana elements and a parity section; in qubit notation $X_{R_1}X_{L_1}Z_{L_2}$, up to the Jordan-Wigner sign string) remain perfectly good observables of the ascended description; they are simply not metric-level records, being annihilated by the composite, which is exactly the recoverability of Proposition \claimref{singularity.purity-correlation-transfer-recovery}(3): readable in the completion, invisible in the original space. Had the antecedent been dropped and the total-parity average used in $\EN$'s place, the two-level discrepancy of Steps 5 and 6b would be identically zero, the model's radiation state being even; the script verifies this too. The antecedent enters Table \ref{tab:chain} as the residue of (P$_{\mathrm{loc}}$), definitional rather than physical. Appendix \ref{app:threeroutes} states the residue in structural terms without reducing it: ``the pointwise metric level'' names two algebras, the even part of the mode factor and the even-in-that-mode part of the boundary mode space, and a region can be read by assembling either contravariantly (a sheaf, a limit: survive every point's descent) or covariantly (a net, a colimit: the algebra the points' retained parts generate). On a finite truncation the sheaf assembly gives $\operatorname{range}(\EN)$, at once the meet of the big fibres and the join of the small ones, and the net assembly gives the whole mode algebra with a discrepancy of zero (Theorems \claimref{singularity.finite-truncation-meet-big-fibres-equals}, \claimref{singularity.net-assembly-net-it-everything}). The chain adopts the sheaf assembly; that adoption is the antecedent, restated, and Remark \claimref{note.singularity.what-antecedent-stated-plainly} records that the appendix quantifies both and decides neither. The sheaf exists whenever the completed mode bundle does, that is under the standing hypothesis $w_1(\shL) = 0$, and needs nothing further.

## technical
pending

## lay
pending

## one-liner
pending
