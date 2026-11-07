---
id: rungs.imported-spinor-identification-witt-data-line
kind: claim
version: 4
title: "Imported: the spinor identification, the Witt data, and the line at infinity"
status: proved
region: rungs
subject: conformal-spacetime
tags: [conformal-spinors, conformal-model, witt-index]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - correspondence.fock-model-complexified-ascended-algebra@8
  - correspondence.incidence-relation-chart@5
  - correspondence.reality-conjugation-twistor-form-factor@7
  - correspondence.skew-lines-splittings-hyperbolic-planes-one@4
  - correspondence.spinor-identification@7
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_irreducible_and_klein_identification
- kind: check
  ref: check.py::check_witt_pair_is_the_two_summands
- kind: check
  ref: check.py::check_real_form_and_sigma_null_lines
locators:
  paper: T12-rungs
  number: Fact 1.3
  label: fact:spinorid
  line: 209
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: irreducibility, Pf(M_v) = -Q(v) with null iff decomposable, the Witt pair as the two chart summands with the mixed slot as their orthogonal complement, skew lines as chart points, and the Sigma real form. Version 3 -> 4.'
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.incidence-relation-chart
  - correspondence.reality-conjugation-twistor-form-factor
  - correspondence.skew-lines-splittings-hyperbolic-planes-one
  - correspondence.spinor-identification
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Fact restating series results; all five uses are the cited sources and are kept (the cited
      remark of the twistor paper is not in the store). Levels pass: the lay now says the dictionary is
      for the complexified ambient space and that the real points are those of the conformal compactification.'
  source_title: "Imported: the spinor identification, the Witt data, and the line at infinity"
  source_formal: |-
    The complexified $\Cl(2,4)$ acts irreducibly on $\Sp = \Lambda^{\bullet}W$. There is a canonical isomorphism $V_{\C} \cong \Lambda^{2}\T$ of $\mathrm{Spin}$-modules under which the quadratic form is $P \mapsto \varepsilon(P \wedge P)$ for a fixed volume functional $\varepsilon$ on $\Lambda^{4}\T$, and a vector is null exactly when its bivector is decomposable. In the incidence chart $\T = \Som \oplus \Spi$, a twistor being $Z = (\omega, \pi)$, the lines of $\mathbb{P}(\T)$ skew to the line at infinity $L_{\infty} = \mathbb{P}(\Som)$ are the points of the chart, and the Witt pair $n_{0}, n_{\infty}$ of $V_{\C}$ consists of the bivectors of the two summands, $\Som \wedge \Spi$ being their common orthogonal complement. The real form of the ambient spin group is the conformal $SU(2,2) \cong \mathrm{Spin}(2,4)$, and a line of $\mathbb{P}(\T)$ is a point of the real conformal compactification exactly when it is null for the Hermitian form $\Sigma$. \emph{Provenance:} \cite[Rem.~3.2, Thms.~3.1, 3.4, 4.2, Props.~4.1, 4.5]{ButlerT9}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space and twistors to the conformal spinor space and conformal spinors (\\CS, \\PCS) in all levels and the restating proof; the complexified $V_\\C$ and $\\Cl(2,4)_\\C$ are kept as in the source."
---

## formal
The complexified $\Cl(2,4)$ acts irreducibly on $\Sp = \Lambda^{\bullet}W$. There is a canonical isomorphism $V_{\C} \cong \Lambda^{2}\CS$ of $\mathrm{Spin}$-modules under which the quadratic form is $P \mapsto \varepsilon(P \wedge P)$ for a fixed volume functional $\varepsilon$ on $\Lambda^{4}\CS$, and a vector is null exactly when its bivector is decomposable. In the incidence chart $\CS = \Som \oplus \Spi$ of the conformal spinor space (twistor space), a conformal spinor being $Z = (\omega, \pi)$, the lines of $\PCS = \mathbb{P}(\CS)$ skew to the line at infinity $L_{\infty} = \mathbb{P}(\Som)$ are the points of the chart, and the Witt pair $n_{0}, n_{\infty}$ of $V_{\C}$ consists of the bivectors of the two summands, $\Som \wedge \Spi$ being their common orthogonal complement. The real form of the ambient spin group is the conformal $SU(2,2) \cong \mathrm{Spin}(2,4)$, and a line of $\PCS$ is a point of the real conformal compactification exactly when it is null for the Hermitian form $\Sigma$. \emph{Provenance:} \cite[Rem.~3.2, Thms.~3.1, 3.4, 4.2, Props.~4.1, 4.5]{ButlerT9}.

## technical
The complexified $\Cl(2,4)$ acts irreducibly on $\Sp = \Lambda^\bullet W$, and there is a canonical $\mathrm{Spin}$-isomorphism $V_\C \cong \Lambda^2\CS$ under which the quadratic form is $P \mapsto \varepsilon(P \wedge P)$, a vector being null exactly when its bivector is decomposable.

In the chart $\CS = \Som \oplus \Spi$, $Z = (\omega, \pi)$, the points of the chart are the lines of $\PCS = \mathbb{P}(\CS)$ skew to $L_\infty = \mathbb{P}(\Som)$, the Witt pair $n_0, n_\infty$ consists of the bivectors of the two summands, and $\Som \wedge \Spi$ is their common orthogonal complement. The real spin group is $SU(2,2) \cong \mathrm{Spin}(2,4)$, and a line is a point of the real conformal compactification exactly when it is null for the Hermitian form $\Sigma$.

## lay
This restates the dictionary between the six-dimensional ambient space and the four-dimensional spinor space of the conformal algebra that the rungs note uses. Vectors of the complexified ambient space become pairs of such spinors, light-like vectors become single lines in the projective spinor space, and the two special null vectors of the chart correspond to the two halves into which the spinor space splits. Points of real compactified spacetime are the lines on which a natural Hermitian form vanishes.

## one-liner
Imported: $V_\C \cong \Lambda^2\CS$ with null meaning decomposable, chart points are the lines skew to the line at infinity, the Witt pair is the two summands' bivectors, and real points are the $\Sigma$-null lines.
