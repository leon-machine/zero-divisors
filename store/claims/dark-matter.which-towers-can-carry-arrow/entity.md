---
id: dark-matter.which-towers-can-carry-arrow
kind: claim
version: 6
title: Which towers can carry the arrow
status: proved
region: dark-matter
subject: dark-matter
tags: [towers-by-residue, matter-asymmetry]
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
  role: 'maintainer pass, common-ceiling-coupling premise named in the fork''s share-one condition at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Opus 5.5
  role: 'assumes edge to the common-ceiling-coupling premise dropped at Leon''s second-round decisions (scope kept as a text mention); one-liner restored'
  version: 6
  source: maintainer pass 2026-11-07 (decisions, second round)
review: typed
derivations:
- name: main
  uses:
  - dark-matter.flag-bit-exists-exactly-tower-dimension@3
  - dark-matter.towers-are-residues-single-clock-filter@5
  - standard-model.four-dimensions-forces-converse@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:cor:whocarries
- kind: check
  ref: check.py::check_oriented_and_causal_towers
- kind: check
  ref: check.py::check_fork_conformal_spinors_are_real
- kind: check
  ref: check.py::check_mass_begins_at_two_on_the_fork
locators:
  paper: T14
  number: Cor 3.11
  label: cor:whocarries
  line: 281
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Leon''s second-round answer 2: the assumes edge to synthesis.common-ceiling-coupling-premise@1 is dropped, since the corollary cites the premise only for its scope (the reversal orbit) in the fork''s share-one condition and its sort of the towers does not rest on it; the formal and technical keep the scope as a text mention (the premise equates the ceiling coupling for the mirror alone). The one-liner''s parenthesis naming the premise, added at close-out to satisfy W503, is reverted to the version-4 wording, so no plain level states a condition the result does not rest on; the lay never named it. Coverage''s untouched_premises entry for the premise removed. holds_given loses the premise (computed by the build).'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Leon''s answer 2 (C1): the fork''s share-one condition names the new premise synthesis.common-ceiling-coupling-premise as what equates the ceiling coupling for the mirror alone, with the assumes edge Leon asked for; the corollary cites it for its scope (the reversal orbit) and its sort of the towers does not depend on it. Wording and edge at Leon''s decision.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: oriented and causal towers exactly {2, 6}; Cl(3,3) real conformal spinors (ideal 4, corner R, three pairs); the determinant identity for mass at two. Version 3 -> 4.'
  env: corollary
  context_refs:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - dark-matter.mirror-tower-copy-one
  - dark-matter.no-coupling-rule-odd-towers-follows
  - standard-model.four-dimensions-forces-converse
  typing:
    by: ai-typing-pass
    added:
    - standard-model.four-dimensions-forces-converse
    note: 'Added the dimension-four gauge-algebra proposition, which the proof cites for the fork''s Standard-Model
      algebra; the arrow, copy and coupling-rule references are context, and the E204 here comes from
      the flag-bit theorem outside this list. Levels pass: the lay and one-liner now say the causal sort
      is at the P3 representatives and that the two-time instability is imported; the lay keeps the fork''s
      two conditionalities.'
  source_title: 'Which towers can carry the arrow'
  source_formal: |-
    The descent's orientation, and with it the asymmetry the flag sets in Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, is undefined in the odd residues: $1, 3, 5, 7$ cannot be oriented and carry no asymmetry, whatever their content or window. It is defined in the even residues at their P3 representatives, all four-dimensional. Of those, $6$ and $2$ have one time, $4$ has none, and $0$ has two; so the towers that are both oriented and causal are this one and the mirror.

    The two-time fork therefore leads to an \emph{oriented} tower: $(2,2)$ has ambient $\R^{3,3}$, $\mathrm{Spin}(3,3) \cong SL(4,\R)$, real four-component twistors, three pairs, mass beginning at two by
    \[
    \det(\pi^{1}\tilde\pi^{1T} + \pi^{2}\tilde\pi^{2T}) \;=\; \br{\pi^{1}\pi^{2}}\br{\tilde\pi^{1}\tilde\pi^{2}}, \qquad \br{\pi\rho} = \pi_{1}\rho_{2} - \pi_{2}\rho_{1},
    \]
    for the two real spinor parts of $\mathrm{Spin}(2,2) \cong SL(2,\R) \times SL(2,\R)$, and the Standard-Model gauge algebra by that paper's Proposition 4.3 in dimension four \cite[Prop.~4.3]{ButlerT12}, whose two conditionalities (mass-begins-at-two in dimension $n \neq 4$ as a hypothesis, and the identification of the gauge algebra with the automorphisms of minimal massive compositeness) it carries: a Kleinian copy of the Standard Model. Its share would be one only on two equalities the paper cannot supply off this tower's reversal orbit: the asymmetry per mode (P4, a premise on the fork) and the ceiling coupling (Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}(c)). The two-time instability import keeps the fork closed.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the real four-component twistors of the $(2,2)$ fork to real conformal spinors, a minimal left ideal of $\Cl^+(3,3)$, noting that its pseudoscalar squares to $+1$ so no complex unit arises; the Cauchy-Binet mass identity in real 2-spinor components is unchanged.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.four-dimensions-forces-converse
---

## formal
The descent's orientation, and with it the asymmetry the flag sets in Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, is undefined in the odd residues: $1, 3, 5, 7$ cannot be oriented and carry no asymmetry, whatever their content or window. It is defined in the even residues at their P3 representatives, all four-dimensional. Of those, $6$ and $2$ have one time, $4$ has none, and $0$ has two; so the towers that are both oriented and causal are this one and the mirror.

The two-time fork therefore leads to an \emph{oriented} tower: $(2,2)$ has ambient $\R^{3,3}$, $\mathrm{Spin}(3,3) \cong SL(4,\R)$, real four-component conformal spinors (real twistors: a minimal left ideal of $\Cl^+(3,3)$, whose pseudoscalar squares to $+1$, so there is no complex unit), three pairs, mass beginning at two by
\[
\det(\pi^{1}\tilde\pi^{1T} + \pi^{2}\tilde\pi^{2T}) \;=\; \br{\pi^{1}\pi^{2}}\br{\tilde\pi^{1}\tilde\pi^{2}}, \qquad \br{\pi\rho} = \pi_{1}\rho_{2} - \pi_{2}\rho_{1},
\]
for the two real spinor parts of $\mathrm{Spin}(2,2) \cong SL(2,\R) \times SL(2,\R)$, and the Standard-Model gauge algebra by that paper's Proposition 4.3 in dimension four \cite[Prop.~4.3]{ButlerT12}, whose two conditionalities (mass-begins-at-two in dimension $n \neq 4$ as a hypothesis, and the identification of the gauge algebra with the automorphisms of minimal massive compositeness) it carries: a Kleinian copy of the Standard Model. Its share would be one only on two equalities the paper cannot supply off this tower's reversal orbit: the asymmetry per mode (P4, a premise on the fork) and the ceiling coupling, which Premise \claimref{synthesis.common-ceiling-coupling-premise} equates for the mirror alone, along the reversal orbit (Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), Proposition \claimref{dark-matter.no-coupling-rule-odd-towers-follows}(c)). The two-time instability import keeps the fork closed.

## technical
The descent's orientation, and with it the asymmetry set by the flag, is defined only where the flag bit exists: in the even residues at their nearest-dimension representatives, all four-dimensional. Of these, $r = 6$ and $r = 2$ have one time, $r = 4$ none and $r = 0$ two, so the towers that are both oriented and causal are this one and the mirror. The odd residues $1, 3, 5, 7$ cannot be oriented and carry no asymmetry, whatever their content or window.

The two-time fork $(2,2)$ is oriented. Its ambient is $\R^{3,3}$ with $\Spin(3,3) \cong SL(4,\R)$ and real four-component conformal spinors, and mass begins at two by the Cauchy-Binet identity
$$\det(\pi^{1}\tilde\pi^{1T} + \pi^{2}\tilde\pi^{2T}) = \br{\pi^{1}\pi^{2}}\br{\tilde\pi^{1}\tilde\pi^{2}},$$
so with the dimension-four gauge-algebra result, and carrying its two conditionalities, it is a Kleinian copy of the Standard Model. Its share would be one only on two equalities the paper cannot supply off this tower's reversal orbit, the asymmetry per mode and the ceiling coupling (the common-ceiling-coupling premise equates the latter for the mirror alone), and the imported two-time instability keeps the fork closed.

## lay
The excess of matter over antimatter needs an orientation, a choice the theory says can only be made in the towers with even labels. Among those, taken at the dimension nearest four (premise P3), only our world and the mirror tower have a single direction of time, so only they can carry the excess. A tower with two time directions could in principle host a copy of the Standard Model, carrying the same two conditions as the Standard-Model derivation, but the paper keeps it closed by importing the standard result that physics with two times is unstable.

## one-liner
Only the even-residue towers can be oriented, and of them, at their nearest-dimension representatives, only this one and the mirror are also causal, so they alone can carry the matter asymmetry; the oriented two-time fork would be a Kleinian copy of the Standard Model, kept closed by the imported two-time instability.
