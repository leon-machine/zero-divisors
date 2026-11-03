---
id: standard-model.fits-record-level
kind: claim
version: 6
title: The fits, at record level
status: proved
region: standard-model
subject: generations
tags: [confronted-with-data, flavour-and-mixing]
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
  - standard-model.imported-clebsch-structure-seesaw@1
  - standard-model.what-angle-asks-neutrino-sector@4
  - standard-model.hyp-s-slot-statistics@9
  assumes:
  - standard-model.premise-ew-equal-weight@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:obs:anglefits
- kind: check
  ref: check.py::check_charged_fermion_masses
- kind: check
  ref: check.py::check_neutrino_masses_and_dirac_entries
locators:
  paper: T12
  number: Obs 11.7
  label: obs:anglefits
  line: 2091
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for the four stored coupling sets, exact characteristic cubics place the nine charged-fermion masses, m_3, m_3/m_2, m_1 and the largest Dirac entry as tabulated (mixing angles and Delta not tested). Version 4 -> 5. Check strengthened: the three charged-fermion bands asserted disjoint and ordered (three distinct roots); record values, tables, legacy tolerances and the bisection width moved to module level. Version 5 -> 6.'
  env: observation
  context_refs:
  - standard-model.imported-clebsch-structure-seesaw
  - standard-model.what-angle-asks-neutrino-sector
  outside_pilot_cites:
  - ButlerT15
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-clebsch-structure-seesaw
    - standard-model.what-angle-asks-neutrino-sector
    - standard-model.hyp-s-slot-statistics
    - standard-model.premise-ew-equal-weight
    note: 'Promoted from conjectured to proved at record level, since the paper computes the fits and
      its script recomputes every observable (so a legacy verify_T12.py check was added); Premise (EW)
      and Hypothesis (S) have no store entries to assume, so the result''s dependence on them stays in
      the text. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because its statement
      holds under Hypothesis (S); assumes standard-model.premise-ew-equal-weight added because its statement
      holds under Premise (EW). Levels pass: the lay level and one-liner now name Hypothesis (S) and Premise
      (EW); the one-liner limits the tuning statement to the representative fits.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - standard-model.imported-clebsch-structure-seesaw
    - standard-model.what-angle-asks-neutrino-sector
    - standard-model.hyp-s-slot-statistics
    - standard-model.premise-ew-equal-weight
    note: "Record-level proof with no step naming either premise; stated the roles of (EW) and (S) from their statements."
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), Fact \claimref{standard-model.imported-clebsch-structure-seesaw}, Premise (EW) and the $v_{R}$ of Proposition \claimref{standard-model.what-angle-asks-neutrino-sector}, fit with complex couplings, at $M_{I}$, the nine charged-fermion masses, $|V_{us}|$, $|V_{cb}|$, $|V_{ub}|$, the CKM phase, $m_{3}$, $m_{3}/m_{2}$ and the three lepton mixing angles (the record's values \cite{PDG2024}, run to $M_{I}$ in the Standard Model). Let $\Delta$ be the largest $|d\ln O/d\ln p|$ for $O = m_{3}$ and $O = m_{3}/m_{2}$ over the Lagrangian couplings $p$, with (EW) held exact. Representative fits:
\begin{center}\small
\begin{tabular}{@{}lllll@{}}
\toprule
couplings & factor $3$ of the second family & largest $|M_{\nu}|$ entry & $m_{1}$ & $\Delta$ \\
\midrule
$10$s, $126$, $120$ & through mixing with the third & $0.04$ GeV & $0.03$ meV & $8$, $11$ \\
$10$s, $126$, $120$ & from the $126$'s second-family entry & $2.9$ GeV & $0.1$ meV & $46$, $96$ \\
one $10$, $126$, $120$ & from the $126$ & $4.0$ GeV & $4.9$ meV & $59$, $167$ \\
$10$s, $126$, no $120$ & from the $126$ & $2.2$ GeV & $1.7$ meV & $2400$, $6700$ \\
\bottomrule
\end{tabular}
\end{center}
Every row reproduces every one of the eighteen observables; none is a prediction, the couplings outnumbering the observables. When the $126$ supplies the second family's factor $3$ directly, the neutrino Dirac matrix keeps an entry of $2$ to $4$ GeV, whose seesaw contribution would naturally be of order $1$ eV, and the measured masses arise only from a cancellation among complex terms, tuned to about one part in $\Delta$. In the first row the $126$'s second-family entry supplies about a tenth of $m_{s}$, the splitting comes through mixing with the third family, carried by the $120$ and the $10$s, and nothing cancels; its $m_{1}$ lies below the neutrino paper's bound of about $0.1$ meV \cite{ButlerT15}.

## technical
Under Hypothesis (S), the imported Clebsch structure with the seesaw, Premise (EW) and the triplet vev $v_{R}$ required by the neutrino sector, numerical fits with complex couplings at $M_{I}$ reproduce eighteen observables: the nine charged-fermion masses, $|V_{us}|$, $|V_{cb}|$, $|V_{ub}|$, the CKM phase, $m_{3}$, $m_{3}/m_{2}$ and the three lepton mixing angles. The tuning is measured by $\Delta$, the largest $|d\ln O/d\ln p|$ for $O = m_{3}$ and $O = m_{3}/m_{2}$ over the Lagrangian couplings $p$.

When the $126$ supplies the second family's factor $3$ directly, a neutrino Dirac entry of $2$ to $4$ GeV survives and the measured masses need a cancellation tuned to about one part in $\Delta$, with $\Delta$ from $46$ up to $6700$. When the factor instead comes through mixing with the third family, carried by the $120$ and the $10$s, nothing cancels ($\Delta = 8$, $11$) and $m_{1} \approx 0.03$ meV. None of the fits is a prediction, since the couplings outnumber the observables.

## lay
Granting the slot-statistics hypothesis (S) and the equal-weight premise (EW), on the unified route the paper follows the masses and mixings of all known fermions can be fitted to the recorded values, but there are more adjustable couplings than measurements, so the fits predict nothing. What they show is which arrangements need delicate cancellations. If the factor of three for the second family comes directly from one ingredient, the neutrino masses come out right only through fine tuning; if it comes through mixing with the third family, no tuning is needed.

## one-liner
At record level and under (S) and (EW), fits on the Pati-Salam route reproduce all eighteen fermion observables, and in the representative fits they are untuned only when the second family's factor $3$ comes through mixing with the third.
