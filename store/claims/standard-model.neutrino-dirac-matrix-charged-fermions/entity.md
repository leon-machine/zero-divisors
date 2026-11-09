---
id: standard-model.neutrino-dirac-matrix-charged-fermions
kind: claim
version: 6
title: The neutrino Dirac matrix from the charged fermions
status: proved
region: standard-model
subject: neutrinos
tags: [flavour-and-mixing, seesaw-and-majorana]
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
  - standard-model.hyp-s-slot-statistics@10
  assumes:
  - standard-model.premise-ew-equal-weight@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_differences_without_120
- kind: check
  ref: check.py::check_neutrino_matrix_fixed_under_ew
- kind: check
  ref: check.py::check_120_unfixes_neutrino_matrix
locators:
  paper: T12
  number: Prop 11.5
  label: prop:elimination
  line: 2065
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on complex rational matrices, M_d - M_e = 4 w_d f and M_u - M_nu = 4 w_u f, M_nu = M_u - m_t fhat under (EW) from two parameter sets, and the loss of fixing once a 120 is added. Version 5 -> 6.'
  env: proposition
  context_refs:
  - standard-model.imported-clebsch-structure-seesaw
  unresolved_refs:
  - rem:equalweight
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-clebsch-structure-seesaw
    - standard-model.hyp-s-slot-statistics
    - standard-model.premise-ew-equal-weight
    note: 'added the imported Clebsch structure, which the statement assumes and the proof uses; Hypothesis
      (S) and Premise (EW) have no store postulates, so they are carried only in the text. Hypothesis
      pass: assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S); assumes standard-model.premise-ew-equal-weight added because its statement holds under Premise
      (EW). Levels pass: the lay level now states Hypothesis (S) and Premise (EW), which it had dropped,
      and the one-liner gains (S); both now keep the residual rotation and phase freedom.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.imported-clebsch-structure-seesaw
    stated_role:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S) and Fact \claimref{standard-model.imported-clebsch-structure-seesaw}, with any number of $10$s and no $120$,
\[
M_{d} - M_{e} \;=\; 4w_{d}f, \qquad M_{u} - M_{\nu} \;=\; 4w_{u}f,
\]
and under Premise (EW), in the basis of Remark \ref{rem:equalweight},
\[
M_{\nu} \;=\; M_{u} - m_{t}\,\hat{f}, \qquad \hat{f} \;=\; \frac{M_{d} - M_{e}}{(M_{d} - M_{e})_{33}}.
\]
The neutrino Dirac matrix, and the Majorana matrix up to its scale, are then fixed by the charged fermions, up to the charged leptons' unitary rotation and the phases that low-energy data do not fix. With a $120$ the two differences gain $(c_{d} - c_{e})h$ and $(c_{u} - c_{\nu})h$, whose coefficients are independent of each other and of $w_{u}$ and $w_{d}$, and $M_{\nu}$ is no longer fixed.

## technical
Under Hypothesis (S) and the imported Clebsch structure, with any number of $10$s and no $120$, each $10$ enters the down-type and charged-lepton matrices, and the up-type and neutrino ones, with the same coefficient, while the $126$ enters with Clebsches $1$ and $-3$: hence $M_{d} - M_{e} = 4w_{d}f$ and $M_{u} - M_{\nu} = 4w_{u}f$. Under Premise (EW), in its family basis, $M_{\nu} = M_{u} - m_{t}\hat{f}$ with $\hat{f} = (M_{d} - M_{e})/(M_{d} - M_{e})_{33}$.

So the neutrino Dirac matrix, and the Majorana matrix up to its scale, are fixed by the charged fermions, up to the charged leptons' unitary rotation and the phases low-energy data do not fix. With a $120$ both differences gain independent terms and $M_{\nu}$ is no longer fixed.

## lay
In this unified setting, assuming the paper's Hypothesis (S) and the standard weights it imports, quark and lepton mass matrices are built from shared ingredients with fixed weights. Subtracting the lepton matrices from the quark ones isolates a single ingredient. Under the further equal-weight premise (EW), that ingredient pins down the neutrino's ordinary mass matrix from the measured charged-particle masses, up to a rotation of the charged leptons and phases that low-energy data do not fix. This works only if one particular extra ingredient, a $120$, is absent.

## one-liner
Under Hypothesis (S) and Premise (EW), and without a $120$, the neutrino Dirac matrix is fixed by the charged fermions as $M_{\nu} = M_{u} - m_{t}\hat{f}$, up to the charged leptons' rotation and unfixed phases.
