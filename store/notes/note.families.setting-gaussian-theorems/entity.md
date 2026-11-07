---
id: note.families.setting-gaussian-theorems
kind: note
version: 3
title: The Gaussian theorems
status: setting
subject: generations
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: consistency pass, cross products written as duals of outer products
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- families.rigidity-pairing-sector-one-event
- families.chart-computation-sign-twist-bracket-form
- families.imported-squeezed-vacuum-bosonic-pairing
- families.alignment-computed-thirteenth-refutation-democracy-one
locators:
  paper: T13
  number: Setting
  section: The Gaussian theorems
  line: 769
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The cross-product matrix [p x q]_x and the channel vectors f_+ x f_-, u'' x f_+ are written as the duals -I_f(p ^ q), -I_f(f_+ ^ f_-), -I_f(u'' ^ f_+) with I_f the family pseudoscalar, the notation of the proof of families.rigidity-pairing-sector-one-event; a pure notation change (a x b = -I_f(a ^ b) in Cl(3,0)).'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The channel phase e^{i chi} in the channel vector a = a_A + lambda e^{i chi} a_B became e^{I_4 chi}, numbers read in span{1, I_4}; no bare i remains. By Leon''s ruling R3 the face-space reading is stated once in R3''s words: numbers and the module''s complex structure in span{1, I_4}, the module read on the tower''s floors (notational).'
---

## formal
The chain of Section \ref{sec:koide} reduces the Koide relation to one normalisation, and the way to fix a normalisation is to compute the vacuum. This section does the computation in the simplest class that has a vacuum to compute: the Gaussian one. The model, stated once. The six-mode face algebra has bosonic modes $a_{iA}$, $i \in \{1,2,3\}$ a family slot and $A \in \{1,2\}$ a spinor component; the face operators are the bracket quadratics
\[
\hat\Omega_{k} \;=\; \varepsilon_{AB}\,a_{iA}\,a_{jB} \;=\; \tfrac12\,\varepsilon_{kij}\,\varepsilon_{AB}\,a_{iA}a_{jB}, \qquad (i,j) \text{ the cyclic successors of } k,
\]
the operator form of Proposition \claimref{families.chart-computation-sign-twist-bracket-form}'s minors. The frozen vacuum is the squeezed vacuum (Fact \claimref{families.imported-squeezed-vacuum-bosonic-pairing}) of a pairing in the antisymmetric sector,
\[
\xi \;=\; \tau\,\bigl(G \otimes \varepsilon\bigr), \qquad G = [a]_{\times}, \qquad a = a_{A} + \lambda e^{I_4\chi}a_{B},
\]
where a family wedge $p \wedge q$ acts on the family space by contraction, $w \mapsto w \cdot (p \wedge q)$, which is $[a]_{\times}(w) := -I_{f}(a \wedge w)$ for $a = -I_{f}(p \wedge q)$, the dual of the wedge ($I_{f} = f_{1}f_{2}f_{3}$ the family pseudoscalar), and the two channels are the wedges $f_{+} \wedge f_{-}$, the $S_{3}$-safe channel available to the uncaused vacuum, with $a_{A} = -I_{f}(f_{+} \wedge f_{-})$ normalised, and $u' \wedge f_{+}$, $u' = (1,1,1)$, the channel that uses the descent's orientation bit, with $a_{B} = -I_{f}(u' \wedge f_{+})$ normalised; $\tau > 0$ is the strength, $\lambda \ge 0$ the feeding ratio, $\chi$ the channel phase (numbers and the module's complex structure are read in $\mathrm{span}\{1, I_4\}$, the module read on the tower's floors, where $I_4$ commutes with the tower vectors), and $\lambda = 1$ the universal-strength point. The reading is the gauge-invariant symmetric square, forced by the bracket's gauge phase and the mass paper's $m^{2} = 2|B_{\Lambda}|^{2}$: the mass form is
\[
H_{kl} \;=\; \tfrac12\,\bigl\langle \hat\Omega_{k}^{\dagger}\hat\Omega_{l} + \hat\Omega_{l}\hat\Omega_{k}^{\dagger}\bigr\rangle,
\]
and the physical families are its eigenvectors, per Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one}(3). Throughout, $r$ is the freezing depth (the common Takagi value of the pairing, Proposition \claimref{families.rigidity-pairing-sector-one-event}), $x = \sinh^{2}r$, and $s = \sinh r$, $c = \cosh r$.

## technical
pending

## lay
pending

## one-liner
pending
