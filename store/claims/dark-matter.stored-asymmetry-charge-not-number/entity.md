---
id: dark-matter.stored-asymmetry-charge-not-number
kind: claim
version: 12
title: The stored asymmetry is a charge, not a number
status: proved
region: dark-matter
subject: dark-matter
tags: [matter-asymmetry, mirror-sector, dark-matter-ratio, needs-continuum]
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
  role: consistency pass, interval of the eta-prime and thermal-share bounds stated
  version: 9
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the cold-mirror exception stated at P2''s version-1 reach, with P2 as scoped leaving xi free'
  version: 9
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Opus 5.5
  role: wording of the P1 parenthetical, the number pi N^2/ln 2 named a count of registered units and the light-ray count corrected
  version: 10
  source: maintainer pass of 2026-11-09
- name: Claude Fable 5.2
  role: 'restatement of clauses (i) and (ii) at the maintainer''s decision: the residue label, B - L and baryon number named apart; the charge is B - L; no statement that baryon number cannot be produced afterwards; the mirror share made conditional'
  version: 11
  source: maintainer pass 2026-11-12 (asymmetry)
- name: Claude Fable 5.2
  role: 'restatement of the quoted numbers after the production coefficients were corrected: the gravitational yield, the shortfall (three orders, not four), the floor and the mirror''s baryon-to-photon ratio at it; the composition at the floor marked as computed at the earlier floor only'
  version: 12
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'
amendments:
- version: 11
  kind: restatement
  defect: 'clauses (i) and (ii) used the word charge for three objects: the residue label r of the tower (what superselection is about), the descent''s B - L, and baryon number. Clause (ii) inferred from superselection between towers that the baryon charge cannot be produced afterwards within a tower; the 24 slot-pair generators change baryon number, the Majorana element changes B - L, and the anomalous weak equilibrium that a stored check uses produces baryon number from B - L. Restated at the maintainer''s decision of 12 November 2026 that the charge is B - L; clause (i)''s mirror share of one becomes conditional on an equal ratio of baryon number to B - L in the two towers.'
- version: 12
  kind: restatement
  defect: 'clauses (ii) and (iii) quoted the gravitational yield 1.8 to 2.7e-15, a shortfall of more than four orders, the floor 2.8 to 3.2e-4 and eta'' = 19 to 26 from the coefficients proposition at the first published production coefficients, which are too small; with the derived coefficients the yield is 3.9e-14 quanta per unit entropy, the shortfall is more than three orders and not four, the floor is 5.2e-4 and eta'' there is 4.4; the composition quoted at the floor was computed at the earlier floor'
  evidence: check.py::check_origin_gravity_cannot_supply_the_charge
review: typed
derivations:
- name: main
  uses:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation@8
  - dark-matter.coefficients-floors-they-give-what-gravity@5
  - dark-matter.imported-trichotomy-descents-data@6
  - dark-matter.mirror-tower-copy-one@11
  - dark-matter.parallel-boundary-mode-spaces-one-wall@5
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@5
  assumes:
  - dark-matter.p1-single-frozen-point@3
  - dark-matter.p5-boundary-modes-hold-entropy-not@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:charge
- kind: check
  ref: check.py::check_charge_reading_against_thermal_reading
- kind: check
  ref: check.py::check_origin_gravity_cannot_supply_the_charge
- kind: check
  ref: check.py::check_eta_prime_and_radiation_over_the_interval
- kind: check
  ref: check.py::check_bottom_of_ceiling_range_factor
locators:
  paper: T14
  number: Prop 4.6
  label: prop:charge
  line: 399
extraction:
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 11 -> 12, at Leon''s decision of 18 November 2026 (restate the numbers that used the first published production coefficients). Quoted numbers corrected from dark-matter.coefficients-floors-they-give-what-gravity version 5: yield 1.8 to 2.7e-15 -> 3.9e-14 quanta per unit entropy (1.95e-14 creation events of two quanta); shortfall more than four orders -> more than three orders (a factor 2.2e3 counting every quantum); floor 2.8 to 3.2e-4 -> 5.2e-4; eta'' at the floor 19 to 26 -> 4.4. Unchanged: the hot deposit, the crossover 8.5e-4, the bounds 1e7 and 1e-7 (both set at the hot deposit), eight orders below the cap. The statements about degeneracy and neutron fraction at the floor come from dark-tower-matter.mirrors-composition, computed at xi = 2.8 to 3.2e-4, and are now worded as holding there; they are not recomputed at 5.2e-4. The two premises are repinned to their versions of the same day. The series script verify_T14.py (label prop:charge) still evaluates the first imported coefficients.'
  maintainer_pass_2026_11_12:
    by: maintainer-2026-11-12
    date: '2026-11-12'
    note: 'Version 10 -> 11. Leon''s decision D2 of 12 November 2026: the charge Q = epsilon N is named as B - L. Clauses (i) and (ii) are restated at all four levels and a paragraph is added to the proof; clauses (iii) and (iv), the level statement, the caveat, the checks and the coverage file are unchanged. The check of (i) sets the two charges equal and so tests the equal B - L, not the equality of baryon number; it is not edited. No uses edge is drawn to synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them, which uses this result (an edge back would close a cycle), nor to synthesis.baryon-number-centraliser-in-the-five-mode-algebra, and no assumes edge to Premise (R): the new sentences that cite them are a naming and argued statements, labelled so; whether to draw the edges is left to Leon.'
  maintainer_pass_2026_11_09:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Version 9 -> 10. Wording of the P1 parenthetical at all four levels: pi N^2/ln 2 counts registered units (two arrays per unit on average), and the light rays number 2 pi N^2/(c ln 2) for c arrays per light ray, by synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping (iii); version 9 called pi N^2/ln 2 a count of light rays while saying the arrays per light ray depend on the tower. The argument uses only that N is common, so the conclusions are unaffected.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.imported-trichotomy-descents-data repinned 5 -> 6 after reviewing its restatement of clause (2) (the norm of the frozen point is not a field, fixed by a constraint with pure-gauge fluctuations, where it said the frozen action is N-insensitive); clauses (1), (3) and (4) are unchanged; the use here holds as cited. Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited. Pin review (second round): dark-matter.asymmetry-arrow-counted-fifteenth-refutation repinned 6 -> 7 (an extraction note only (Leon confirmed the theta-angle reading); N).'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'G1 (DECISIONS; R05 item 2): the cold-mirror exception now says that it is an exception to P2 at its version-1 reach, that P2 as scoped (version 2, labels not states) leaves xi free (synthesis.tower-charge-sector-label-temperature-not), and that the cold mirror then needs a non-equilibrium descent (synthesis.cold-mirror-needs-non-equilibrium-descent); P2 is unchanged by Leon''s answer 2, so the sentence stands.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Wording: the bounds eta-prime/eta >= 10^7 and f_2 <= 10^-7 hold from the floor to the hot deposit (xi up to about 4.3e-3, xi^3 <= 7.7e-8), not up to the N_eff cap, where 1/xi^3 = 11 and xi^3 = 0.090 (computed); clause (iv) and the technical level now say so, the mathematics unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'P1 parenthetical reworded at all four levels (decision of 2026-10-31): N = M_P/H fixes a count of light rays, about pi N^2/ln 2, common to the towers; the boundary-mode arrays per light ray are tower-dependent, and a five-dimensional field counts one array set per Kaluza-Klein level, equivalently per resolution cell. Previously the parenthetical said N fixes the boundary mode count. The argument, which uses only that N is common, is unchanged. Version 7 -> 8.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: charge against thermal reading (0.448^3 and below 1e-7), gravitational shortfall above 1e4, eta and its cube root, eta'' at the floor and hot deposit, eta''/eta above 1e7, N_eff eight orders below the cap. Version 5 -> 6. Check strengthened: eta exact; crossover, eta'' at the floor ends and hot deposit, eta''/eta and the Delta N_eff margin pinned to six or seven figures. Version 6 -> 7.'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A5 largeness follow-up: N here is the series number M_P/H, which fixes the boundary mode count (about pi N^2/ln 2) without being it; all four levels no longer call N the mode count. Q = eps N unchanged.'
  superseded_in_part_by:
  - dark-tower-matter.mirrors-temperature-p2
  - dark-tower-matter.mirrors-composition
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 1
    note: 'Superseded in part by T14c. Prop 8.2 (dark-tower-matter.mirrors-temperature-p2): P2 with the
      reach of Thm 4.3(iv), (v) fixes xi = 1, so clause (iii)''s free temperature datum is an exception
      to P2; (iii) now says so. Comp 8.3 (dark-tower-matter.mirrors-composition): at the floor the mirror
      is degenerate and 96 to 100 percent neutrons for L <= 0, helium only for xi about 3e-3 to 2e-2,
      so the closing level sentence no longer carries the burning branch as the floor''s expectation.
      (i), (ii), (iv) unchanged. Original in source_formal.'
  source_formal: |-
    Under the classification of Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, with $\epsilon$ initial data of the descent, inherited rather than generated, and the boundary mode count $N$ common to the towers under P1:
    \begin{enumerate}
    \item[(i)] \emph{(Charge.)} The asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, fixed by the descent's data and independent of the tower's temperature; it is not a thermal number $n - \bar{n} \propto g\,\mu T^{2}$. So the mirror share $f_{2} = 1$ holds at any mirror temperature: a cold mirror carries the same baryon charge as this tower in the same number of baryons, with negligible mirror radiation.
    \item[(ii)] \emph{(Origin.)} The charge is the descent's and cannot be produced afterwards: the one channel superselection leaves open, gravitational production from the visible plasma (Appendix \ref{app:seeding}), yields $1.8$ to $2.7 \times 10^{-15}$ mirror quanta per unit entropy at the ceiling reheating against the $8.7 \times 10^{-11}$ baryons per unit entropy that our baryon number requires, more than four orders too few even counting every produced quantum as a baryon. Black holes are a sink for $Q$, not a source (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}(iv), under P5): a mass-preserving rearrangement that erodes each tower's free baryon count and moves no share.
    \item[(iii)] \emph{(Temperature.)} The mirror's temperature ratio $\xi = T'/T$ is a datum of the descent, bounded below by the gravitational floor, $\xi$ between $2.8$ and $3.2 \times 10^{-4}$ at the ceiling reheating (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(ii), the bracket the species-counting ambiguity; four parts in a thousand of this at the bottom of the ceiling range), and above by the $\Neff$ cap at $0.448$; a deposit of each unit of baryon number with energy of order the reheating temperature puts it at $\xi \approx 4 \times 10^{-3}$. The paper carries the whole interval. With $\eta = n_{B}/n_{\gamma} = 6.1 \times 10^{-10}$ here and equal baryon number,
    \[
    \eta' \;=\; \frac{\eta}{\xi^{3}}
    \]
    runs from $19$ to $26$ at the floor down to about $0.008$ at the hot deposit, crossing one at $\xi = \eta^{1/3} = 8.5 \times 10^{-4}$: at least $10^{7}$ times ours throughout, with $\Delta\Neff$ eight orders or more below the cap.
    \item[(iv)] \emph{(The two readings.)} The thermal reading would give $f_{2} \sim \xi_{2}^{3}$ instead, at most $0.090$ under the $\Neff$ cap ($0.448^{3}$) and $10^{-7}$ or less anywhere in the interval; the two readings cannot both hold, and the paper's own classification decides for the charge.
    \end{enumerate}
    Level: the classification is Fact \claimref{dark-matter.imported-trichotomy-descents-data}'s; the incompatibility is arithmetic. The mirror's nucleosynthesis, which is not a copy of ours and on which the burning branch of Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i) and the composition caveat of refutation item 6 rest, follows the proof, at assembly level.
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
    - dark-matter.imported-trichotomy-descents-data
    - dark-matter.parallel-boundary-mode-spaces-one-wall
    - dark-matter.p1-single-frozen-point
    - dark-matter.p5-boundary-modes-hold-entropy-not
    note: 'Added the classification it is stated under (the fifteenth-refutation proposition and the trichotomy
      Fact whose level it carries), the black-hole sink clause (the infall proposition, under P5, possible
      now that its edge back here was removed) and P1 for the common mode count; the fragility proposition
      is downstream context. Levels pass: the lay level now states the classification, P1 and P5, all
      of which it had dropped; the one-liner adds P1.'
  env: proposition
  context_refs:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - dark-matter.imported-trichotomy-descents-data
  - dark-matter.mirror-share-one-how-fragile
  - dark-matter.parallel-boundary-mode-spaces-one-wall
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
    - dark-matter.imported-trichotomy-descents-data
    - dark-matter.parallel-boundary-mode-spaces-one-wall
    - dark-matter.p1-single-frozen-point
    - dark-matter.p5-boundary-modes-hold-entropy-not
---

## formal
Under the classification of Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, with $\epsilon$ initial data of the descent, inherited rather than generated, and the number $N$ common to the towers under P1 ($N = M_{P}/H$, which fixes a count of registered units, about $\pi N^{2}/\ln 2$, without being it: Observation \claimref{standard-model.largeness-number-universes-boundary-modes}; the light rays number $2\pi N^{2}/(c\ln 2)$ for $c$ boundary-mode arrays per light ray (\claimref{synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping}(iii)), and $c$ depends on the tower's content, a five-dimensional field counting one array set per Kaluza-Klein level, equivalently one per resolution cell of the extra direction, so the common count is that of registered units, not of light rays or of boundary modes; the argument uses only that $N$ is common):
\begin{enumerate}
\item[(i)] \emph{(Charge.)} The asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, fixed by the descent's data and independent of the tower's temperature; it is not a thermal number $n - \bar{n} \propto g\,\mu T^{2}$. Three objects have carried the word charge in the stored statements, and they are kept apart here: the residue label $r$ of the tower, constant on the tower's sector, which is what the superselection rule is about (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}, step 1); the total $B - L$ of the tower's matter; and its baryon number $n_{B}$, which is what the measured baryon density reads. By the maintainer's decision of 12 November 2026, $Q$ is the second, the total $B - L$ (Premise \claimref{synthesis.matter-asymmetry-registered-free-input}); the naming is a decision and not a result of this Proposition. What then holds at any mirror temperature is that the mirror carries the same $B - L$ as this tower. The mirror share $f_{2} = 1$ is an equality of baryon number, and it follows from the equal $B - L$ only if the mirror's ratio of baryon number to $B - L$ equals this tower's. That is not shown: in this tower the ratio is the equilibrium coefficient of the anomalous weak process, if that process equilibrated after the descent (a coefficient that is not a stored Fact, $\tfrac{28}{79}$ for one light doublet and $\tfrac{8}{23}$ for two, \claimref{synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them}(vi)), a number for a hot plasma, and at $\xi = 2.8$ to $3.2 \times 10^{-4}$, the floor's value with the production coefficients first imported, the mirror's plasma is degenerate from the moment it is seeded (Computation \claimref{dark-tower-matter.mirrors-composition}; not recomputed at the present floor of (iii)). So $f_{2} = 1$ at any mirror temperature is conditional on that equality of ratios; given it, a cold mirror carries the same baryon number as this tower, with negligible mirror radiation. The words ``equal baryon number'' in (iii) and the comparison of (iv) are read under the same condition.
\item[(ii)] \emph{(Origin.)} The three objects of (i) have three different statements. \emph{Between towers.} The residue $r$ is superselected, and the one channel superselection leaves open, gravitational production from the visible plasma (Appendix \ref{app:seeding}), yields $3.9 \times 10^{-14}$ mirror quanta per unit entropy at the ceiling reheating ($1.95 \times 10^{-14}$ creation events of two quanta each, Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(iii)) against the $8.7 \times 10^{-11}$ baryons per unit entropy that our baryon number requires, more than three orders too few even counting every produced quantum as a baryon. So the mirror's matter is not supplied from this tower after the descent. Superselection of $r$ forbids exchange between towers and implies nothing about a charge within a tower. \emph{Within a tower, $B - L$.} For one family, of the terms the store holds only the Majorana element changes $B - L$: the electroweak mass terms conserve it, the $24$ slot-pair generators carry it, and its mixed weak coefficient vanishes (\claimref{synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them}(ii) to (v)). Premise \claimref{neutrino.r-descent-reheats-below-lower-heavy} states that the descent reheats below the lower heavy scale, so that no heavy state thermalised and the descent's $B - L$ is untouched. So, argued and not proved, the charge $Q$ is the descent's and is not produced afterwards given that Premise, with the Majorana element the named exception: no rate of that element is computed with or without the Premise, the non-thermal injection by descent-populated heavy states vanishes only under the real-breaking assumption (\claimref{neutrino.leptogenesis-suppressed-alignment-reheating-premise-new}), and nothing is shown beyond one family. \emph{Within a tower, baryon number.} That it cannot be produced afterwards is not asserted. The $24$ slot-pair generators do not commute with $n_{B}$ (\claimref{synthesis.baryon-number-centraliser-in-the-five-mode-algebra}(iii); \claimref{synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them}(iv)), and no bound on their rate is stored; and the anomalous weak process, on the imported statement that it changes a charge of non-zero mixed weak coefficient (not a stored Fact), changes $n_{B}$ and keeps $B - L$, and its equilibrium, which the check of Computation \claimref{dark-tower-matter.mirrors-composition} uses, produces baryon number from $B - L$ after the descent. The $8.7 \times 10^{-11}$ baryons per unit entropy are then a figure derived from the datum, conditionally, as the Premise on $\epsilon$ states. Black holes are a sink for $Q$, not a source (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}(iv), under P5): a mass-preserving rearrangement that erodes each tower's free baryon count and moves no share.
\item[(iii)] \emph{(Temperature.)} Taken as a free datum of the descent, which by Proposition \claimref{dark-tower-matter.mirrors-temperature-p2} is an exception to P2 (applied with the reach of Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), (v), P2 gives $\xi = 1$, which the record excludes; that is an exception at P2's version-1 reach, P2 as scoped leaving $\xi$ free, Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}, and the cold mirror then needing a non-equilibrium descent, Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}), the mirror's temperature ratio $\xi = T'/T$ is bounded below by the gravitational floor, $\xi = 5.2 \times 10^{-4}$ at the ceiling reheating (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(ii), with the derived production coefficients, which close the earlier species-counting bracket; four parts in a thousand of this at the bottom of the ceiling range), and above by the $\Neff$ cap at $0.448$; a deposit of each unit of baryon number with energy of order the reheating temperature puts it at $\xi \approx 4 \times 10^{-3}$. The paper carries the whole interval. With $\eta = n_{B}/n_{\gamma} = 6.1 \times 10^{-10}$ here and equal baryon number,
\[
\eta' \;=\; \frac{\eta}{\xi^{3}}
\]
runs from $4.4$ at the floor down to about $0.008$ at the hot deposit, crossing one at $\xi = \eta^{1/3} = 8.5 \times 10^{-4}$: at least $10^{7}$ times ours throughout, with $\Delta\Neff$ eight orders or more below the cap.
\item[(iv)] \emph{(The two readings.)} The thermal reading would give $f_{2} \sim \xi_{2}^{3}$ instead, at most $0.090$ under the $\Neff$ cap ($0.448^{3}$) and $10^{-7}$ or less anywhere between the floor and the hot deposit; the two readings cannot both hold, and the paper's own classification decides for the charge.
\end{enumerate}
Level: the classification is Fact \claimref{dark-matter.imported-trichotomy-descents-data}'s; the incompatibility is arithmetic. The mirror's nucleosynthesis, which is not a copy of ours and on which the burning branch of Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i) and the composition caveat of refutation item 6 rest, follows the proof, at assembly level. Caveat (T14c): the proof's thermal up-down ratio at freeze-out fails at the cold end: at $\xi = 2.8$ to $3.2 \times 10^{-4}$ (the floor's value with the coefficients first imported; the computation has not been repeated at the present floor $5.2 \times 10^{-4}$) the mirror is degenerate and, for a copied lepton number $L \leq 0$, ends $96$ to $100$ percent neutrons; it is helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing the hot-deposit estimate and not the floor (Computation \claimref{dark-tower-matter.mirrors-composition}). The burning branch is therefore not the floor's composition.

## technical
Under the classification in which the asymmetry $\epsilon$ is inherited initial data of the descent, with the number $N = M_{P}/H$ common to the towers under P1 (it fixes a count of registered units, about $\pi N^{2}/\ln 2$, rather than being it; the light rays number $2\pi N^{2}/(c\ln 2)$ for $c$ boundary-mode arrays per light ray, and $c$ depends on the tower), (i) the asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, independent of temperature, not a thermal excess $n - \bar{n} \propto g\,\mu T^{2}$. The word charge is kept apart from two other objects: the residue label $r$ that superselection is about, and baryon number, which the measured density reads; by the maintainer's decision of 12 November 2026, $Q$ is the total $B - L$. The mirror then carries the same $B - L$ at any mirror temperature, and the mirror share $f_{2} = 1$, an equality of baryon number, holds only if the ratio of baryon number to $B - L$ is the same in the two towers, which is not shown. (ii) Between towers, superselection of $r$ leaves only gravitational production, which yields $3.9 \times 10^{-14}$ quanta per unit entropy at the ceiling reheating against the $8.7 \times 10^{-11}$ baryons per unit entropy required, more than three orders too few. Within a tower, $B - L$ is changed among stored terms only by the Majorana element and is protected by Premise (R) of the neutrino paper (argued, no rate computed, one family); baryon number is not protected: the $24$ slot-pair generators change it, and the anomalous weak equilibrium a stored check uses produces it from $B - L$. Black holes are a sink for $Q$, not a source, under P5.

(iii) Taken as a free datum of the descent, the mirror's temperature ratio $\xi$ lies between the gravitational floor, about $5 \times 10^{-4}$, and the $N_{\mathrm{eff}}$ cap at $0.448$, with a hot deposit putting it near $4 \times 10^{-3}$; the mirror baryon-to-photon ratio $\eta' = \eta/\xi^{3}$ is then at least $10^{7}$ times ours from the floor to the hot deposit (only $11$ times ours at the cap). (iv) The thermal reading would give $f_{2} \sim \xi^{3} \le 0.090$, so the two readings cannot both hold, and the classification decides for the charge.

Caveats from the T14c note: a free $\xi$ is an exception to P2 at its version-1 reach, which applied with the reach of the copy theorem gives $\xi = 1$ and $\Delta N_{\mathrm{eff}} = 7.45$ (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}), while P2 as scoped leaves $\xi$ free and the cold mirror then needs a non-equilibrium descent (\claimref{synthesis.tower-charge-sector-label-temperature-not}, \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}); and the mirror is helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, while at $\xi = 2.8$ to $3.2 \times 10^{-4}$, the floor's earlier value, it is degenerate and neutron-rich (Computation \claimref{dark-tower-matter.mirrors-composition}; not recomputed at the present floor, which also lies below the helium interval), so the burning branch does not describe the floor.

## lay
Under the paper's classification, in which the mirror sector's small excess of matter over antimatter is inherited from the descent as initial data, and with the large number that fixes how many basic entropy carriers the horizon has the same for every tower (Premise P1; how many boundary modes each light ray carries, and so how many light rays there are, depends on the tower's content), that excess is fixed at the start, like a stored charge, rather than depending on how hot the sector is. What is fixed in this way is, by a decision recorded on 12 November 2026, the excess of baryons minus leptons, not the excess of baryons alone, and neither is the label that keeps the towers apart. That is why the mirror sector can hold exactly as much of this stored quantity as ours while being far colder; that it then holds exactly as much ordinary-type matter as ours needs one more thing, not yet shown: that baryons make up the same fraction of the stored quantity there as here. Nothing crosses between the sectors later to make up a difference: gravitational production falls short by more than three orders of magnitude, and black holes, under Premise P5, can only remove it. Within one sector the stored quantity is argued, not proved, to be safe under a premise about how hot the beginning was; the baryon excess by itself is not safe, since known processes trade baryons against leptons. A later note (T14c) adds two corrections: leaving the mirror's temperature free is an unstated exception to the paper's indifference principle as first stated (as now scoped it leaves the temperature free, and a cold mirror then needs the descent to have left the towers out of equilibrium), and at the coldest temperature then considered the mirror would end mostly as neutrons rather than helium (an estimate not redone for the somewhat warmer minimum that the corrected rate of gravitational production gives).

## one-liner
Under the inherited-asymmetry classification, with the number $N$ (which fixes a count of registered units) common to the towers under P1, an oriented tower's asymmetry is the temperature-independent charge $Q = \epsilon N$, named as $B - L$ (not the residue label, not baryon number), so the mirror carries the same $B - L$ at any mirror temperature, and the mirror share $f_{2} = 1$ holds if the ratio of baryon number to $B - L$ is the same in the two towers.
