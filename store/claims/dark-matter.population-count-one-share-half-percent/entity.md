---
id: dark-matter.population-count-one-share-half-percent
kind: claim
version: 6
title: 'The population count: one share to half a percent, and a symmetric remainder'
status: proved
region: dark-matter
subject: dark-matter
tags: [dark-matter-ratio, mirror-sector, open-problem, needs-continuum]
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
  role: 'maintainer pass, common-ceiling-coupling premise added to the hypotheses at Leon''s decisions'
  version: 6
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Opus 5.5
  role: 'pin review, the scope clause (iii) now cites the established facts of the no-coupling-rule proposition, where it quoted its old conclusion'
  version: 6
  source: maintainer pass 2026-11-07 (pin review)
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-share-one-how-fragile@7
  - dark-matter.mirror-tower-copy-one@9
  - dark-matter.no-coupling-rule-odd-towers-follows@6
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - dark-matter.superselected-hence-dark-exactly-stable@5
  - dark-matter.which-towers-can-carry-arrow@6
  assumes:
  - dark-matter.p1-single-frozen-point@1
  - dark-matter.p2-indifference@2
  - dark-matter.p3-nearest-dimension-representatives@3
  - dark-matter.p4-democracy-asymmetry-over-oriented-towers@1
  - synthesis.common-ceiling-coupling-premise@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:count
- kind: check
  ref: check.py::check_asymmetric_share_is_the_mirror_alone
- kind: check
  ref: check.py::check_observed_ratio_and_uncertainty
- kind: check
  ref: check.py::check_remainder
- kind: check
  ref: check.py::check_unit_ball_expression_returns_the_remainder
locators:
  paper: T14
  number: Prop 4.5
  label: prop:count
  line: 377
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.mirror-share-one-how-fragile repinned 6 -> 7 after reviewing its C1 restatement ((i) now rests on the common-ceiling-coupling premise, with an assumes edge, where it said P2-protected; the values are unchanged); the use here holds as cited. Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited. Pin review: dark-matter.no-coupling-rule-odd-towers-follows repinned 4 -> 5 after reviewing its B2 restatement (the formal is now the three established facts (a) to (c), the claim that no rule follows from the series moved to a marked remark, and (c) names P2, which equates labels and not couplings, and the common-ceiling-coupling premise, both along the reversal orbit only); the scope clause (iii), formal and technical, quoted the old conclusion that no rule follows from the series and now cites the established facts (b) and (c); the derived claim (i) is unchanged. Pin review: dark-matter.which-towers-can-carry-arrow repinned 4 -> 5 after reviewing its C1 restatement (the ceiling coupling is equated for the mirror alone by the common-ceiling-coupling premise, with an assumes edge; the sorting of the towers is unchanged); the use here holds as cited. Version kept at 6 (already raised in this run). Pin review (second round): dark-matter.which-towers-can-carry-arrow repinned 5 -> 6 after reviewing its restatement (assumes edge to the common-ceiling-coupling premise dropped, one-liner reworded; formal unchanged); the sort of the oriented towers, cited here, is unchanged, and the use here holds as cited. Pin review (second round): dark-matter.no-coupling-rule-odd-towers-follows repinned 5 -> 6 after reviewing its restatement (direct assumes edge to the common-ceiling-coupling premise dropped; formal unchanged); facts (a) to (c), cited here, are unchanged, and the use here holds as cited.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Leon''s answer 2 (C1): the share of one now holds under P1 to P4 and the new premise synthesis.common-ceiling-coupling-premise (assumes edge added), which carries the common ceiling coupling that the proof had attributed to P2; levels to match. Restatement at Leon''s decision.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: only the mirror carries asymmetric dark matter (census and bit), mean-mass factor; observed ratio 5.364 +- 0.065, remainder 0.0976 +- 0.0012, unit-ball expression in (4.364, 4.365). Version 3 -> 4. Check strengthened: the observed ratio and its uncertainty pinned to seven figures. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.mirror-share-one-how-fragile
    - dark-matter.projection-every-towers-content-dilutes-ones
    - dark-matter.p2-indifference
    - dark-matter.p3-nearest-dimension-representatives
    note: 'The statement is under Premises P1 to P4, so P2 and P3 were added to the assumptions; the dilution
      lemma is a stated hypothesis and the fragility proposition supplies the half-percent clause, so
      both were added; the assembled mirror-share theorem was left out as a restatement that itself uses
      this claim. Levels pass: lay now names P1 to P4, the dilution hypothesis, the half-percent tolerance
      and the observation level; one-liner adds the dilution hypothesis and the half percent.'
  env: proposition
  context_refs:
  - dark-matter.mirror-share-assembled
  - dark-matter.mirror-share-one-how-fragile
  - dark-matter.projection-every-towers-content-dilutes-ones
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.mirror-share-one-how-fragile
    - dark-matter.projection-every-towers-content-dilutes-ones
    - dark-matter.p4-democracy-asymmetry-over-oriented-towers
    stated_role:
    - dark-matter.p1-single-frozen-point
    - dark-matter.p2-indifference
    - dark-matter.p3-nearest-dimension-representatives
    note: P1 to P3 act only through the cited lemma, theorem and corollary, so their roles are stated in a
      closing sentence.
---

## formal
For an oriented residue $r$ write $\epsilon_{r}$ for the asymmetry per mode, $n_{r}$ for the mode count of its derived matter and $m_{r}$ for the mass per unit of asymmetry, and
\[
f_{r} \;=\; \frac{\epsilon_{r}\,n_{r}\,m_{r}}{\epsilon_{6}\,n_{6}\,m_{6}}
\]
for the tower factor. Under Premises \claimref{dark-matter.p1-single-frozen-point}-\claimref{dark-matter.p4-democracy-asymmetry-over-oriented-towers} and the common-ceiling-coupling Premise \claimref{synthesis.common-ceiling-coupling-premise}, with every tower's matter diluting as this one's (Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}):
\begin{enumerate}
\item[(i)] \emph{(Asymmetric.)} The asymmetric dark matter is the mirror tower's alone (Corollary \claimref{dark-matter.which-towers-can-carry-arrow}: the odd towers carry none; residues $0$ and $4$ are sterile), and its share is exactly one (Theorem \claimref{dark-matter.mirror-tower-copy-one}(iii), assembled with its premises in Theorem \claimref{dark-matter.mirror-share-assembled}):
\begin{equation}
\frac{\Omega^{\mathrm{asym}}_{\mathrm{dark}}}{\Omega_{b}} \;=\; f_{2} \;=\; 1, \qquad\text{against the observed}\qquad \frac{\Omega_{c}}{\Omega_{b}} \approx 5.364 \pm 0.065,
\end{equation}
the one holding to half a percent on the burning branch (Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i)).
\item[(ii)] \emph{(Symmetric.)} The remainder, $4.364\,\Omega_{b}$, that is $\Omega h^{2} = 0.0976 \pm 0.0012$, is not asymmetric relic of anything in the framework. An odd tower's matter, if any, is what the descent deposited, heated afterwards only through gravity, the one channel superselection leaves open (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}, Appendix \ref{app:seeding}): a symmetric relic whose density is set by the sector's own dynamics (its lightest stable state, its number-changing rates, its temperature relative to ours), not by a conserved number.
\item[(iii)] \emph{(Scope: the remainder is not derived here.)} No rule relating an odd tower's dimensionful coupling to this tower's dimensionless one is derived in the series, which derives no coupling value, and neither premise that equates across towers reaches the odd towers (Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}(b), (c)); this paper supplies none: its derived claim on the ratio is the one share of (i). What it says about the remainder is the unit-ball rule of Section \ref{sec:rule}, a fitted relation at observation level on three premises of its own, returning $4.364$ as $2 \cdot \tfrac{4}{3} + 2 \cdot \tfrac{8}{3\pi}$; nothing in this proposition depends on it. Beyond this the framework fixes only a floor on the odd towers' temperature, from gravitational heating after the descent (Appendix \ref{app:seeding}: about three and a half parts in ten thousand of ours at the ceiling reheating for a nine-vector content, the deposit possibly more), which closes their radiation channels near the floor and says nothing about their matter density; supplying the coupling rule is successor problem (3).
\end{enumerate}
The profile: the mirror's dark matter is mirror baryons at the proton mass, cold and dissipative within its own sector; the odd towers' is symmetric, of undetermined mass; both couple to this tower by gravity alone. Two conditional stances are registered at the premises' level: permanent null results in direct detection, and no indirect-detection signal from dark decays or visible annihilation products. Observation level on the flagged premises; the observed ratio is the survey record's \cite{Planck2018}.

## technical
For an oriented residue write $f_{r} = \epsilon_{r}n_{r}m_{r}/(\epsilon_{6}n_{6}m_{6})$ for the tower factor. Under Premises P1 to P4 and the common ceiling coupling, with every tower's matter diluting as this one's, (i) the asymmetric dark matter is the mirror tower's alone, the odd towers carrying none and residues $0$ and $4$ being sterile, with $\Omega^{\mathrm{asym}}_{\mathrm{dark}}/\Omega_{b} = f_{2} = 1$ against the observed $\Omega_{c}/\Omega_{b} \approx 5.364 \pm 0.065$, the one holding to half a percent on the burning branch. (ii) The remainder, $4.364\,\Omega_{b}$ or $\Omega h^{2} = 0.0976 \pm 0.0012$, is not asymmetric relic: an odd tower's matter, if any, is a symmetric relic deposited by the descent and heated afterwards only through gravity, its density set by the sector's own dynamics.

(iii) The remainder is not derived: the series derives no rule relating an odd tower's dimensionful coupling to this tower's dimensionless one, and no premise that equates across towers reaches the odd towers. The profile is mirror baryons at the proton mass, cold and dissipative within their sector, together with symmetric odd-tower matter of undetermined mass, both coupling to us by gravity alone; null results in direct and indirect detection are registered as conditional stances, at observation level on the flagged premises.

## lay
Astronomers find about 5.4 times as much dark matter as ordinary matter. Assuming the four premises P1 to P4 (a single frozen point, indifference, nearest-dimension representatives and a matter excess shared evenly across the oriented towers) and that the mirror world starts with the same force strengths as ours (the common ceiling coupling), and that every hidden sector's matter thins out with cosmic expansion as ours does, this result accounts for one of those units: a mirror copy of ordinary matter holding the same amount as ours to within half a percent. The other 4.4 units are not explained here; they would have to be a different, symmetric kind of matter in the other hidden sectors, felt by us only through gravity. The account is held at observation level on those premises.

## one-liner
Under P1 to P4 and the common ceiling coupling, with every tower's matter diluting as ours, the mirror tower supplies an asymmetric dark share of one $\Omega_{b}$ to half a percent, leaving a symmetric remainder of $4.364\,\Omega_{b}$ that is not derived.
