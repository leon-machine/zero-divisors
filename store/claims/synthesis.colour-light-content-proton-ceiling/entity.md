---
id: synthesis.colour-light-content-proton-ceiling
kind: claim
version: 3
title: Content no heavier in colour than in hypercharge cannot meet the proton condition
status: proved
subject: standard-model
tags:
- running-and-unification
- no-go
- confronted-with-data
proposed_by:
  kind: ai
  session: synthesis-gaps-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
derivations:
- name: main
  uses:
  - standard-model.imported-one-loop-running-trace-ratio@1
  - standard-model.spectrum-run@6
  - standard-model.one-threshold-exact-criterion@3
  - standard-model.table-exact@7
  - standard-model.imported-proton-condition@1
  - standard-model.imported-coefficient-sum-indices@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::test_ceiling
lineage:
  motivated_by:
  - standard-model.table-exact
about:
- obj.standard-model.one-threshold-spectrum-admissible
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  review_fixes:
    by: ai-review-fix
    date: 2026-10-21
    note: 'Referee fixes: the bounds are attained by any content with Delta_1 = Delta_3 = 0 below the crossing; physical content has Delta_3 >= 0; direction result cited by id; lay restricted to one loop.'
  proof_restored:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'proof-main.tex was lost in an earlier sync; reconstructed from the formal statement and its premises'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Statement unchanged; added the index-formula Fact standard-model.imported-coefficient-sum-indices@1 to uses, because the closing remark (colour singlets, the triplet threshold |Y| >= sqrt(5/18), physical content has Delta_3 >= 0) is not derivable from the previously declared premises; check.py, also lost, rewritten in exact arithmetic.'
---

## formal
Work at one loop in the normalisation of Fact \claimref{standard-model.imported-one-loop-running-trace-ratio}(a), with $t = \ln(\mu/M_{Z})/2\pi$, the Standard Model coefficients $b = (\tfrac{41}{10}, -\tfrac{19}{6}, -7)$ below every threshold and the record values $a_{i} = a_{i}(M_{Z})$ of Proposition \claimref{standard-model.spectrum-run}, so that content $\Dl^{(k)}$ switched on at thresholds $t_{k} \ge 0$ gives $a_{i}(t) = a_{i} - b_{i}t - \sum_{k} \Dl^{(k)}_{i}(t - t_{k})_{+}$. Put $t_{13} := (a_{1} - a_{3})/(b_{1} - b_{3})$, where $a_{1}$ and $a_{3}$ cross with no content added ($M_{13} = M_{Z}e^{2\pi t_{13}} = 2.5 \times 10^{14}$ GeV). Suppose every threshold's content has $\Dl^{(k)}_{3} \ge 0$ and $\Dl^{(k)}_{1} \ge \Dl^{(k)}_{3}$: no heavier in colour than in hypercharge. Then:
\begin{enumerate}
\item[(i)] every point with $a_{1}(t) = a_{3}(t)$, in particular any meeting of the three couplings, has $t \le t_{13}$ and $a_{3}(t) \le a_{3} + 7t_{13}$; $t = t_{13}$ exactly when $\Dl^{(k)}_{1} = \Dl^{(k)}_{3}$ at every threshold below the crossing, and content with $\Dl^{(k)}_{1} = \Dl^{(k)}_{3} = 0$ below the crossing, the wino for one, attains both bounds;
\item[(ii)] hence $M_{U} \le M_{13}$ and $\alpha_{U}^{-1} \le a_{3} + 7t_{13} = 40.4$, and the proton figure of Fact \claimref{standard-model.imported-proton-condition} obeys $\tfrac{\alpha_{U}^{-1}}{45}\bigl(M_{U}/10^{15}\,\mathrm{GeV}\bigr)^{2} < \tfrac{1}{10}$, against the condition's $5.2\sqrt{15} > 20$: no such content, at any number of thresholds, meets the proton condition, and it misses by a factor above $200$ in that figure, about $10^{5}$ in lifetime;
\item[(iii)] the three spectra that Proposition \claimref{standard-model.table-exact}(d) finds admissible, $\Dl = (0, \tfrac43, 0)$, $(\tfrac25, 2, 0)$ and $(\tfrac52, \tfrac{25}{6}, 2)$, satisfy the hypothesis, so clause (e) of that proposition follows from (ii) with an argument of its own: they fail the proton condition because none is heavier in colour than in hypercharge.
\end{enumerate}
Colour singlets and complete multiplets always satisfy the hypothesis, and a colour triplet does exactly when $|Y| \ge \sqrt{5/18}$; a gluino ($\Dl_{1} - \Dl_{3} = -2$) and $Q$- or $d^{c}$-type triplets do not. So a one-loop spectrum that meets the proton condition (physical content has $\Dl_{3} \ge 0$) must carry, at some threshold, content with $\Dl_{3} > \Dl_{1}$.

## technical
At one loop the difference $a_{1} - a_{3}$ runs with slope $-(b_{1} - b_{3}) - \sum(\Dl_{1} - \Dl_{3})$, so content with $\Dl_{1} \ge \Dl_{3}$ only makes it fall faster and brings the crossing of $a_{1}$ and $a_{3}$ down: it never lies above the desert's crossing $M_{13} = 2.5 \times 10^{14}$ GeV. Since $b_{3} = -7 < 0$ and $\Dl_{3} \ge 0$, the unified inverse coupling there is at most $a_{3} + 7t_{13} = 40.4$. The proton figure $(\alpha_{U}^{-1}/45)(M_{U}/10^{15}\,\mathrm{GeV})^{2}$ is increasing in both, so it is below $1/10$, far under the $20.1$ the Super-Kamiokande limit demands. The three admissible rows of the one-threshold table (the wino; the wino, bino and higgsinos; the supersymmetric content without the gluino) all satisfy the hypothesis, which supplies an argument for the table's clause (e). The wino, with $\Dl_{1} = \Dl_{3} = 0$, sits exactly on the bound. The general part uses only the imported running and $b_{3} < 0$; Hypothesis (S) enters only through the table's identification of the content. Combined with Corollary \claimref{standard-model.direction-demanded-content-doublet-heavy} (the content must be heavy in $SU(2)$), a proton-safe one-loop spectrum needs coloured content beyond its hypercharge share, as the gluino is.

## lay
When the three forces' strengths are run up in energy, they must meet high enough for the proton to live as long as experiments show. Adding new particles changes how the strengths run. This result shows that particles which affect the strong force no more than they affect the hypercharge force can only pull the meeting point of two of the strengths down, never up, and the meeting point they leave is far too low. So every candidate of that kind, including the three that the series' table found workable, makes the proton decay too fast at one loop. To keep the proton, new particles must lean towards the strong force, as the partner of the gluon does.

## one-liner
At one loop, content no heavier in colour than in hypercharge keeps the meeting scale below $2.5 \times 10^{14}$ GeV and cannot meet the proton condition: clause (e) of the table, argued.
