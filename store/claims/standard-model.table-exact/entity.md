---
id: standard-model.table-exact
kind: claim
version: 7
title: The table, exact
status: proved
region: standard-model
subject: standard-model
tags:
- running-and-unification
- confronted-with-data
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
  - standard-model.complete-multiplets-shift-all-three-coefficients@3
  - standard-model.imported-coefficient-sum-indices@1
  - standard-model.one-threshold-exact-criterion@3
  - standard-model.proton-condition-candidates@5
  - standard-model.spectrum-run@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_table_rows
- kind: check
  ref: check.py::check_full_supersymmetric_content
- kind: check
  ref: check.py::check_three_admissible_rows
- kind: check
  ref: check.py::check_spectrum_run_cross_checks
- kind: check
  ref: check.py::check_admissible_rows_fail_proton_condition
locators:
  paper: T12
  number: Prop 8.11
  label: prop:table
  line: 1379
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: every row''s Dl from its listing with r_Dl, f and verdict, the full content''s 7/5 and 62 GeV, the three admissible rows, the spectrum-run cross-checks and clause (e). Version 5 -> 6. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 6 -> 7.'
  env: proposition
  context_refs:
  - standard-model.proton-condition-candidates
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.spectrum-run
    added:
    - standard-model.proton-condition-candidates
    - standard-model.hyp-s-slot-statistics
    note: 'Removed the spectrum run, used only for its input values and as a cross-check; added the proton-condition
      proposition, which clause (e) rests on; kept the one-threshold criterion as a real premise, the
      circular edge having been the criterion''s script-check citation of this table. Hypothesis pass:
      assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S). Levels pass: conditions already kept; the lay level now names Hypothesis (S) by its label.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.proton-condition-candidates
    stated_role:
    - standard-model.hyp-s-slot-statistics
    note: The premise is used only by clause (e) of the statement, which the proof had not addressed;
      a one-line pointer to it is added rather than removing the edge. Proof is an exact or record-level
      run with no step naming (S); stated its role, the lepton doublet of the derived content, from Theorem
      hypercharge-global-form and Proposition weak-angle, which put the lepton doublet under (S).
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: "Direct assumes of Hypothesis (S) removed and standard-model.spectrum-run restored to uses: the table is evaluated at that proposition's inputs and base coefficients (the typing pass had removed it as inputs and cross-check only), and that is where (S) enters, as the lepton doublet of the derived content; the proof uses no slot statistics of its own. (S) stays in holds_given through spectrum-run, so the statement keeps 'Under Hypothesis (S)'."
about:
- obj.standard-model.one-threshold-spectrum-admissible
---

## formal
Under Hypothesis (S), with the inputs of Proposition \claimref{standard-model.spectrum-run}, Fact \claimref{standard-model.imported-coefficient-sum-indices} and Theorem \claimref{standard-model.one-threshold-exact-criterion} give, for the following one-threshold spectra (the content named is what is added above $M_{I}$; all fermions Weyl, higgsinos a vector-like pair of doublets with $Y = \pm\tfrac12$, gauginos one Weyl adjoint per factor, ``second doublet'' a complex scalar doublet, ``sfermions'' three scalar generations):
\begin{center}\small
\begin{tabular}{@{}lllll@{}}
\toprule
content above $M_{I}$ & $\Dl$ & $r_{\Dl}$ & $f$ & conclusion \\
\midrule
any complete multiplet & $c(1,1,1)$ & $r_{0}$ & no solution & inert \\
gluino & $(0, 0, 2)$ & $218/55 = 3.96$ & $-0.69$ & worsens \\
three gauginos & $(0, \tfrac43, 2)$ & $178/95 = 1.874$ & $4.76$ & short, $a_{U} < 0$ \\
higgsinos & $(\tfrac25, \tfrac23, 0)$ & $14/9 = 1.556$ & $1.61$ & short \\
second doublet & $(\tfrac{1}{10}, \tfrac16, 0)$ & $9/5 = 1.8$ & $6.42$ & short \\
gauginos $+$ higgsinos & $(\tfrac25, 2, 2)$ & $34/23 = 1.478$ & $1.20$ & short \\
gauginos $+$ higgsinos $+$ 2nd doublet & $(\tfrac12, \tfrac{13}{6}, 2)$ & $7/5 = 1.4$ & $1.0116$ & short by $1.2\%$ \\
full supersymmetric content & $(\tfrac52, \tfrac{25}{6}, 4)$ & $7/5 = 1.4$ & $1.0116$ & short by $1.2\%$ \\
wino & $(0, \tfrac43, 0)$ & $178/155 = 1.148$ & $0.60$ & admissible \\
wino $+$ bino $+$ higgsinos & $(\tfrac25, 2, 0)$ & $34/35 = 0.971$ & $0.44$ & admissible \\
supersymmetric content without gluino & $(\tfrac52, \tfrac{25}{6}, 2)$ & $14/15 = 0.933$ & $0.41$ & admissible \\
\bottomrule
\end{tabular}
\end{center}
In particular: (a) a gluino alone raises the ratio and moves the meeting in the wrong direction; (b) the three gauginos, the higgsinos, a second doublet and the gaugino-higgsino spectrum each lower it but not to $R$, so no threshold at or above $M_{Z}$ makes them meet; (c) the full supersymmetric content has $r_{\Dl} = 7/5$ exactly, a gap $7/5 - R = 0.0055$ above the record, and its threshold falls at $f = 1.0116$, that is $M_{I} = 62$ GeV, below $M_{Z}$: at strict one loop with these inputs it is inadmissible by $1.2$ percent in $f$, and adding or removing the sfermions, complete multiplets, changes only $a_{U}$; (d) exactly three of the ten spectra are admissible, and none contains a gluino; their thresholds are $8 \times 10^{6}$, $7 \times 10^{8}$ and $1.5 \times 10^{9}$ GeV with meeting scales of $1.5$ to $2.5 \times 10^{14}$ GeV; (e) none of the three meets the proton condition (Proposition \claimref{standard-model.proton-condition-candidates}). The rationals are exact and script-checked; the GeV values are the one floating-point conversion, printed by the script as records.

## technical
Under Hypothesis (S), with the record inputs, each candidate spectrum is a shift $\Dl$ of the one-loop coefficients above a threshold $M_{I}$, built from the index formula, and the exact one-threshold criterion gives its threshold fraction $f = (Rb_{23} - b_{12})/(\Dl_{12} - R\Dl_{23})$ and its verdict. Complete multiplets are inert, a gluino worsens the miss, and the gauginos, the higgsinos, a second doublet and the gaugino-higgsino spectrum fall short; the full supersymmetric content has $r_{\Dl} = 7/5$ exactly and $f = 1.0116$, a threshold of $62$ GeV below $M_{Z}$, so at strict one loop it is inadmissible by $1.2$ percent in $f$.

Exactly three of the ten spectra are admissible, the wino, the wino with the bino and higgsinos, and the supersymmetric content without the gluino, with thresholds from $8 \times 10^{6}$ to $1.5 \times 10^{9}$ GeV and meeting scales of $1.5$ to $2.5 \times 10^{14}$ GeV; none meets the proton condition. The rationals are exact; the GeV values are a floating-point conversion.

## lay
The paper's derived particles alone do not make the three forces meet, so this table tries adding various hypothetical partner particles above some mass and asks whether any choice of that mass makes them meet. Most additions do nothing, push the wrong way, or fall short, and a full supersymmetric set misses by about one percent at this level of approximation. Three additions work, but they would make protons decay too quickly. The calculation assumes the paper's hypothesis about the composite's modes (Hypothesis (S)).

## one-liner
Under Hypothesis (S), the exact one-threshold criterion finds exactly three of ten candidate spectra admissible at one loop, none with a gluino and none meeting the proton condition, while full supersymmetry falls short by $1.2$ percent.
