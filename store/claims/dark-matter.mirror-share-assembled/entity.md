---
id: dark-matter.mirror-share-assembled
kind: claim
version: 8
title: The mirror share, assembled
status: proved
region: dark-matter
subject: dark-matter
tags: [dark-matter-ratio, mirror-sector]
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
  role: 'maintainer pass, mass ratio restated onto the common-ceiling-coupling premise at Leon''s decisions'
  version: 8
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation@7
  - dark-matter.imported-derived-generation-flag@6
  - dark-matter.imported-inputs-standard-model-chain@6
  - dark-matter.mirror-share-one-how-fragile@7
  - dark-matter.mirror-tower-copy-one@9
  - dark-matter.mode-counts-two-modules-which-one@6
  - dark-matter.population-count-one-share-half-percent@6
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - dark-matter.stored-asymmetry-charge-not-number@10
  - standard-model.hyp-s-slot-statistics@10
  assumes:
  - dark-matter.p1-single-frozen-point@1
  - dark-matter.p2-indifference@2
  - synthesis.common-ceiling-coupling-premise@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_mode_ratio_is_one
- kind: check
  ref: check.py::check_mass_ratio_half_percent
locators:
  paper: T14
  number: Thm 4.8
  label: thm:share
  line: 474
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.mirror-share-one-how-fragile repinned 6 -> 7 after reviewing its C1 restatement ((i) now rests on the common-ceiling-coupling premise, with an assumes edge, where it said P2-protected; the values are unchanged); the use here holds as cited. Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited. Pin review: dark-matter.population-count-one-share-half-percent repinned 5 -> 6 after reviewing its C1 restatement (the share of one now rests also on the common-ceiling-coupling premise, with an assumes edge; the numbers are unchanged); the use here holds as cited. Pin review: dark-matter.stored-asymmetry-charge-not-number repinned 8 -> 9 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the charge reading and the numbers are unchanged); the use here holds as cited. Pin review (second round): dark-matter.asymmetry-arrow-counted-fifteenth-refutation repinned 6 -> 7 (an extraction note only (Leon confirmed the theta-angle reading); N).'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 7 -> 8. Leon''s answer 2 (C1): the mass ratio (ii) is now given the new premise synthesis.common-ceiling-coupling-premise (assumes edge added) instead of P2, which at version 2 does not reach a coupling; levels, proof and coverage note to match. Restatement at Leon''s decision.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the signature-reversal isomorphism of the even subalgebras of Cl(2,4) and Cl(4,2) behind n_2 = n_6, and the half-percent mass ratio on the burning branch. Version 6 -> 7.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: 'P4 removed from assumes: clause (iii) states that P4 is discharged for the mirror, not assumed,
      by Theorem 4.3(v) (dark-matter.mirror-tower-copy-one; T14 line 332), and the proof says so. The
      formal (the paper''s "Under Premises P1, P2 and P4") and the technical, lay and one-liner levels
      now list P1, P2, (S) and the input list, with P4 named as discharged (CONTRADICTIONS_VALUES L1).
      The fragility proposition this uses no longer assumes P4 either; P4 still reaches the holds_given
      through the population-count proposition (T14 Prop 4.5, under P1 to P4 for every oriented tower),
      whose tower factor the proof evaluates at r = 2, and that edge is left. Original in source_formal.'
  source_formal: |-
    Under Premises \claimref{dark-matter.p1-single-frozen-point}, \claimref{dark-matter.p2-indifference} and \claimref{dark-matter.p4-democracy-asymmetry-over-oriented-towers}, the Standard-Model paper's Hypothesis (S) as carried in Fact \claimref{dark-matter.imported-derived-generation-flag}, and the input list of Fact \claimref{dark-matter.imported-inputs-standard-model-chain}, the mirror tower contributes exactly one visible share:
    \[
    f_{2} \;=\; \underbrace{\frac{\epsilon_{2}}{\epsilon_{6}}}_{\text{P2}}\cdot\;\underbrace{\frac{n_{2}}{n_{6}}}_{\text{derived}}\;\cdot\;\underbrace{\frac{m_{2}}{m_{6}}}_{\text{derived, given P2}} \;=\; 1\cdot 1\cdot 1 \;=\; 1, \qquad \Omega_{\mathrm{mirror}} \;=\; \Omega_{b},
    \]
    exactly on the proton-only branch and to half a percent on the burning branch (Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i)). The three factors are stated separately because they have three standings, and the exposure of the share is the weakest of them.
    \begin{enumerate}
    \item[(i)] \emph{(The mode ratio: derived, on no premise of this paper.)} $n_{2} = n_{6}$, the same state space.
    \item[(ii)] \emph{(The mass ratio: derived, given P2.)} $m_{2} = m_{6}$ up to the two sectors' composition, the common ceiling coupling being P2 along the reversal orbit.
    \item[(iii)] \emph{(The asymmetry ratio: premised on P2.)} $\epsilon_{2} = \epsilon_{6}$ by the audit along the same orbit (P1's orientation clause a weaker second route); P4 is discharged for the mirror, not assumed.
    \item[(iv)] \emph{(No temperature in it.)} The share is one anywhere in the interval of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(iii).
    \end{enumerate}
  env: theorem
  context_refs:
  - dark-matter.imported-derived-generation-flag
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.imported-derived-generation-flag
    - standard-model.hyp-s-slot-statistics
    note: 'Added the derived-generation fact because the theorem is stated under Hypothesis (S) as that
      fact carries it; the arrow proposition stays because the source''s level line rests clause (iv)
      on its classification. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because
      its statement holds under Hypothesis (S). Levels pass: the lay replaced ''given the framework''s
      assumptions'' by the named premises P1, P2, P4, the Standard-Model inputs and Hypothesis (S), and
      kept the half-percent burning-branch qualifier; the one-liner now names (S).'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.imported-derived-generation-flag
    - dark-matter.p4-democracy-asymmetry-over-oriented-towers
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
payload:
- kind: value
  clause: record masses
  quantity: quantity.helium-4-nucleus-mass
  python: M_HE4 == F('3727.379')
- kind: value
  clause: record masses
  quantity: quantity.proton-mass
  python: M_P == F('938.272')
  note: M_P is the proton mass in this check
- kind: inequality
  clause: to half a percent on the burning branch
  python: F(4, 1000) < 1 - burning_branch_ratio()[2] < F(6, 1000)
  note: the mirror's mean nucleon mass is 0.5 % below ours at Y_p = 0.245
---

## formal
Under Premises \claimref{dark-matter.p1-single-frozen-point}, \claimref{dark-matter.p2-indifference} and \claimref{synthesis.common-ceiling-coupling-premise} (Premise \claimref{dark-matter.p4-democracy-asymmetry-over-oriented-towers} being discharged for the mirror, clause (iii)), the Standard-Model paper's Hypothesis (S) as carried in Fact \claimref{dark-matter.imported-derived-generation-flag}, and the input list of Fact \claimref{dark-matter.imported-inputs-standard-model-chain}, the mirror tower contributes exactly one visible share:
\[
f_{2} \;=\; \underbrace{\frac{\epsilon_{2}}{\epsilon_{6}}}_{\text{P2}}\cdot\;\underbrace{\frac{n_{2}}{n_{6}}}_{\text{derived}}\;\cdot\;\underbrace{\frac{m_{2}}{m_{6}}}_{\text{derived, given the common ceiling coupling}} \;=\; 1\cdot 1\cdot 1 \;=\; 1, \qquad \Omega_{\mathrm{mirror}} \;=\; \Omega_{b},
\]
exactly on the proton-only branch and to half a percent on the burning branch (Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i)). The three factors are stated separately because they have three standings, and the exposure of the share is the weakest of them.
\begin{enumerate}
\item[(i)] \emph{(The mode ratio: derived, on no premise of this paper.)} $n_{2} = n_{6}$, the same state space.
\item[(ii)] \emph{(The mass ratio: derived, given the common ceiling coupling.)} $m_{2} = m_{6}$ up to the two sectors' composition, the common ceiling and coupling being Premise \claimref{synthesis.common-ceiling-coupling-premise} along the reversal orbit (Premise \claimref{dark-matter.p2-indifference}, scoped to sector labels, does not reach a coupling).
\item[(iii)] \emph{(The asymmetry ratio: premised on P2.)} $\epsilon_{2} = \epsilon_{6}$ by the audit along the same orbit (P1's orientation clause a weaker second route); P4 is discharged for the mirror, not assumed.
\item[(iv)] \emph{(No temperature in it.)} The share is one anywhere in the interval of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(iii).
\end{enumerate}

## technical
Under the single frozen point, indifference and the common ceiling coupling, with Hypothesis (S) and the input list of the Standard-Model chain (the democracy of the asymmetry being discharged for the mirror, not assumed), the mirror tower's share factorises as $f_{2} = (\epsilon_{2}/\epsilon_{6})(n_{2}/n_{6})(m_{2}/m_{6}) = 1 \cdot 1 \cdot 1 = 1$, so $\Omega_{\mathrm{mirror}} = \Omega_{b}$, exactly on the proton-only branch and to half a percent on the burning branch. The three factors have three standings. The mode ratio $n_{2} = n_{6}$ is derived from the shared state space, on no premise of the dark-matter analysis. The mass ratio is derived given the common-ceiling-coupling premise, which supplies the common ceiling and coupling along the reversal orbit (indifference, scoped to sector labels, does not reach a coupling), up to the two sectors' composition. The asymmetry ratio $\epsilon_{2} = \epsilon_{6}$ is premised on indifference along the same orbit, which discharges the democracy premise for the mirror.

No temperature enters: the share is one anywhere in the allowed interval for the stored asymmetry. The exposure of the share is that of its weakest factor, the premised asymmetry ratio.

## lay
The mirror world, our world with the roles of time and space reversed, contributes exactly as much matter as our ordinary matter (exactly on one branch of the analysis, to within half a percent on the other), given two of the paper's premises (a single frozen point and indifference between mirror towers; a third, that the oriented towers share one asymmetry, follows for the mirror and is not assumed), the assumption that the two worlds start with equal force strengths at one common highest scale (the common ceiling coupling), the Standard-Model inputs, and the assumption that the slots behave like the pairs (Hypothesis (S)). The three ingredients, how many kinds of particle there are, how heavy they are and how large the matter excess is, each come out equal, but on different footings: the first is derived outright, the second depends on the equal-strengths assumption, and the third is assumed through the indifference symmetry. The answer does not depend on how hot the mirror world is.

## one-liner
Under the single frozen point, indifference, the common ceiling coupling and Hypothesis (S), the democracy of the asymmetry being discharged for the mirror, the mirror tower's share is $f_{2} = 1 \cdot 1 \cdot 1 = 1$, so $\Omega_{\mathrm{mirror}} = \Omega_{b}$ (to half a percent on the burning branch), the asymmetry ratio being the premised factor.
