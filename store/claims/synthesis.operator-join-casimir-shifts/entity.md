---
id: synthesis.operator-join-casimir-shifts
kind: claim
version: 3
title: 'Casimir shifts of the operator join'
status: proved
region: synthesis
subject: mass
tags: [conformal-spinors, frozen-point]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'maintainer pass, normalisation hypothesis stated in (iii) at Leon''s decisions'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
review: draft
derivations:
- name: main
  uses:
  - synthesis.operator-join-ordering-constants@3
  - mass.casimir-form-join@7
  - mass.imported-palatial-quadratics-homogeneity-charge@4
  - mass.imported-unitary-representations-de-sitter-group@4
  - mass.mass-weight-dictionary@4
  - mass.weight-polynomial-two-series@6
  - field-theory.imported-standard-field-theory@4
  - mass.de-sitter-scale-frozen-point@6
  - mass.chart-form-spin-isomorphism@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_operator_join_casimir_shifts
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.operator-join-ordering-constants
  - mass.casimir-form-join
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Decision item B6 (routine): (iii) now states the normalisation hypothesis in full (C_2(I_Lambda-perp) of mass.casimir-form-join in the scalar-module normalisation of the imported classification, with no shift) and says it is not proved and not part of the import; the imported Fact no longer asserts it. A hypothesis made explicit; mathematics unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: op.operator-join
  note: 'Cross-check of the stored ordering constants against de Sitter representation theory, and an adversarial finding about the reading of mass. On one conformal spinor every term of the Casimir form is a function of the helicity, so the operator join can be compared with the field side exactly. The constant -(Lambda/3) hbar^2 is what turns the classical Casimirs 3 s^2 and 2 s^2 into 3(s^2 - 1) and 2(s^2 - 1), the standard Casimirs of the massless conformal representation and of the de Sitter representation with Delta = |s| + 1 (standard values cited from memory, Delta(Delta - 4) + 2 j1(j1 + 1) + 2 j2(j2 + 1) and Delta(Delta - 3) + s(s + 1); not used in the proof). On the scalar module the de Sitter Casimir gives the conformally coupled 2H^2 of the weight dictionary, while the grip gives -H^2: the store''s identification of the grip with the field mass (mass.casimir-form-join up to version 3, normalisation remark, corrected in version 4; note.mass.what-join-says, three readings of one number) holds only up to H^2 C_conf, which vanishes on a single spinor only at |s| = 1. Bears on the massless locus: a composite with zero grip has de Sitter mass -H^2 C_conf. Transport-convenient (the frozen point supplies the split).'
---

## formal
Quantise a single conformal spinor ($N = 1$) with the palatial ordering of Proposition \claimref{synthesis.operator-join-ordering-constants}: $\hat{m}^{2} = Q(\hat{P})$ is the operator grip on the frozen point $I_{\Lambda}$ of Lemma \claimref{mass.de-sitter-scale-frozen-point}, $\hat{h}$ the palatial helicity generator (the symmetrised $\bar{Z}\cdot Z$), $\hat{C}_{\mathrm{conf}}$ the conformal Casimir $C_{2}(\Lambda^{2}\CS) = \tr(h^{2}) - \tfrac14(\tr h)^{2}$ of Proposition \claimref{mass.casimir-form-join} with its products Jordan-symmetrised, and define the operator de Sitter Casimir by the split of that proposition's (1), $\hat{C}_{\mathrm{dS}} := \hat{C}_{\mathrm{conf}} - \hat{m}^{2}/Q(I_{\Lambda})$, with $Q(I_{\Lambda}) = \Lambda/3 = H^{2}$. Then:
\begin{enumerate}
\item[(i)] in the oscillator algebra, $\hat{m}^{2} = \tfrac{\Lambda}{12}(\hat{h}^{2} - 4\hbar^{2})$, $\hat{C}_{\mathrm{conf}} = \tfrac34(\hat{h}^{2} - 4\hbar^{2})$ and $\hat{C}_{\mathrm{dS}} = \tfrac12(\hat{h}^{2} - 4\hbar^{2})$, whose classical values are $\tfrac{\Lambda}{12}h^{2}$, $\tfrac34 h^{2}$ and $\tfrac12 h^{2}$;
\item[(ii)] on functions of homogeneity $n$, where $\hat{h} = -(n + 2)\hbar = 2s\hbar$ (Fact \claimref{mass.imported-palatial-quadratics-homogeneity-charge}), $\hat{m}^{2} = H^{2}(s^{2} - 1)\hbar^{2}$, $\hat{C}_{\mathrm{conf}} = 3(s^{2} - 1)\hbar^{2}$ and $\hat{C}_{\mathrm{dS}} = 2(s^{2} - 1)\hbar^{2}$: in all three the ordering replaces $s^{2}$ by $s^{2} - 1$;
\item[(iii)] on the scalar module, $n = -2$, $s = 0$, the Penrose transform's conformally invariant scalar (Fact \claimref{field-theory.imported-standard-field-theory}), $\hat{C}_{\mathrm{dS}} = -2\hbar^{2}$. Under the \emph{normalisation hypothesis}, stated here and not proved (it is not part of the imported classification), that the moment normalisation of the de Sitter Casimir $C_{2}(I_{\Lambda}^{\perp})$ of Proposition \claimref{mass.casimir-form-join} is the scalar-module one of Fact \claimref{mass.imported-unitary-representations-de-sitter-group} (acting as $-m^{2}/H^{2}$), with no shift between the two, this is $m^{2} = 2H^{2}\hbar^{2}$, $\Delta \in \{1, 2\}$, the conformally coupled value $-w(w+3)H^{2}$ at $w = -1$ of Theorem \claimref{mass.mass-weight-dictionary} and Corollary \claimref{mass.weight-polynomial-two-series}(2), whereas the grip is $\hat{m}^{2} = -H^{2}\hbar^{2}$ and the classical de Sitter Casimir gives $0$.
\end{enumerate}
For any number of constituents the de Sitter reading $-H^{2}\hat{C}_{\mathrm{dS}}$ and the grip differ by $H^{2}\hat{C}_{\mathrm{conf}}$; under the same normalisation hypothesis, the grip is the de Sitter mass only on states with $\hat{C}_{\mathrm{conf}} = 0$, which for one spinor means $|s| = 1$.

## technical
For one conformal spinor the operator join, the conformal Casimir and the de Sitter Casimir (defined by the split $m^{2} = H^{2}(C_{\mathrm{conf}} - C_{\mathrm{dS}})$ of the Casimir form) are all functions of the palatial helicity, and exactly: $\hat{m}^{2} = \tfrac{\Lambda}{12}(\hat{h}^{2} - 4\hbar^{2})$, $\hat{C}_{\mathrm{conf}} = \tfrac34(\hat{h}^{2} - 4\hbar^{2})$, $\hat{C}_{\mathrm{dS}} = \tfrac12(\hat{h}^{2} - 4\hbar^{2})$. On helicity $s$ they are $H^{2}(s^{2} - 1)$, $3(s^{2} - 1)$ and $2(s^{2} - 1)$ in units of $\hbar^{2}$, against classical $H^{2}s^{2}$, $3s^{2}$, $2s^{2}$. So the stored ordering constant, $-(\Lambda/3)\hbar^{2}$ at $N = 1$, is the quantum shift that both Casimirs undergo, and the shifted values are the standard Casimirs of the massless conformal representation and of the de Sitter representation it restricts to.

The adversarial consequence concerns what "mass" means. On the scalar module the de Sitter Casimir is $-2\hbar^{2}$, which, if the moment normalisation is the field one, is the conformally coupled mass $2H^{2}$ that the series' own weight dictionary assigns to a weight $-1$ field. The grip gives $-H^{2}$ there. The two readings of mass that the store identifies differ by $H^{2}$ times the conformal Casimir, for any composite; they agree on a single spinor only at $|s| = 1$, and a composite with zero grip has de Sitter mass $-H^{2}C_{\mathrm{conf}}$, not zero.

## lay
The framework turns a classical formula for the mass of a composite into a quantum operator, and the reordering of factors adds one constant. This result checks that constant against the standard theory of particles in an expanding (de Sitter) universe, using the simplest case, a single basic spinor of definite spin. The constant is exactly what is needed: with it, the two symmetry quantities that the mass formula subtracts take their standard quantum values; without it they do not. The check also exposes a mismatch, under one stated assumption about normalisation: for the simplest scalar particle the standard de Sitter mass, which the framework's own field-side dictionary reproduces, is twice the squared expansion rate, while the composite-side mass formula gives minus that rate squared. The two notions of mass the framework treats as one differ by a term set by the particle's conformal symmetry charge.

## one-liner
For one conformal spinor of helicity $s$, the operator join, conformal Casimir and de Sitter Casimir are $H^{2}(s^{2} - 1)$, $3(s^{2} - 1)$ and $2(s^{2} - 1)$ (units $\hbar^{2}$): the ordering constant is the Casimirs' quantum shift, and, if the moment normalisation is the field one, the de Sitter mass of the scalar is the weight dictionary's $2H^{2}$ while the grip gives $-H^{2}$, the two differing by $H^{2}C_{\mathrm{conf}}$.
