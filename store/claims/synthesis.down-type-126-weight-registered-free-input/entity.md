---
id: synthesis.down-type-126-weight-registered-free-input
kind: claim
version: 1
title: 'Premise: the down-type 126 weight is a registered free input'
status: postulate
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, undetermined-input]
proposed_by:
  kind: ai
  session: maintainer-2026-11-09
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: maintainer pass 2026-11-09 (Leon's decision)
review: draft
lineage:
  motivated_by:
  - synthesis.georgi-jarlskog-weight-free-on-the-stored-relations
  - synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square
  - standard-model.imported-clebsch-structure-seesaw
  - synthesis.residual-s2-fixes-120-family-form
  - synthesis.number-n-registered-free-input
  - synthesis.matter-asymmetry-registered-free-input
  - synthesis.rung-unit-second-free-number
  - synthesis.majorana-scale-free-input
extraction:
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: >-
      New postulate, adopted by Leon's decision of 2026-11-09 to register the down-type 126 weight as a free
      input, after synthesis.georgi-jarlskog-weight-free-on-the-stored-relations showed that no stored relation
      fixes it (a rescaling of w_d leaves every stored relation in place and moves the second family's factor).
      Registered beside N, the asymmetry epsilon, the D-term level xi G and the Majorana scale, so that the
      premise register counts it. The tower dimension at residues 3 and 5, shown free of the descent the same
      day, is not registered separately: it is already carried by the postulate
      dark-matter.p3-nearest-dimension-representatives. No assumes edges are added.
---

## formal
\emph{Premise ($w_{d}$), the down-type $126$ weight as a registered input.} In the Clebsch structure without a $120$ (Fact \claimref{standard-model.imported-clebsch-structure-seesaw}), the down-type quark and charged-lepton mass matrices are $M_{d} = v_{d}Y + w_{d}f$ and $M_{e} = v_{d}Y - 3w_{d}f$, so the $126$ enters the down-type sector through the weight $w_{d}f$ against the $10$'s $v_{d}Y$; on the sixteen this is the weight $b/a$ of the $(15,1,1)$ part in the coupling $w_{4}(a + bP_{4})$, whose lepton-to-quark ratio is $(32a + 3b)/(32a - b)$ (Theorem \claimref{synthesis.georgi-jarlskog-weight-free-on-the-stored-relations}(ii)). The premise: \emph{$w_{d}$ (equivalently the down-type weight $b/a$ on each family) is a free number of the series}: it is not computed from the transport structure, from another premise of the register, or from any stored relation, and it is not a function of $N$ (Premise \claimref{synthesis.number-n-registered-free-input}), of $\xi G$ (Premise \claimref{synthesis.rung-unit-second-free-number}), of the asymmetry $\epsilon$ (Premise \claimref{synthesis.matter-asymmetry-registered-free-input}) or of the Majorana scale (Premise \claimref{synthesis.majorana-scale-free-input}). Its value is taken from the record: the second family's factor $3$, $m_{\mu} \approx 3m_{s}$ at the intermediate scale $M_{I}$, and with it $m_{b}/m_{\tau}$ there.

\emph{Scope.} The premise registers the weight. The Clebsch coefficient $-3$ stays derived: given that the $(15,1,1)$ part enters, its lepton-to-quark ratio is $-3$ (Theorem \claimref{synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square}). The up-type, neutrino and Majorana sectors do not contain $w_{d}$ and are not registered here.

\emph{What it is for.} The stored fits that use the factor $3$ as coming from the $126$'s second-family entry are fits in that entry (Theorem \claimref{synthesis.georgi-jarlskog-weight-free-on-the-stored-relations}, its cost); registering $w_{d}$ makes that fitted number a counted input of the register. Under an $S_{3}$-invariant Majorana sector the $126$ cannot give the second family alone a factor (Theorem \claimref{synthesis.residual-s2-fixes-120-family-form}(iii)), and there the free number is the light-plane scalar of the same weight.

\emph{What it does not give.} It does not explain the factor $3$ or its family pattern; it does not decide whether a relation outside the store (a potential for the doublet mixing at the intermediate scale) fixes $w_{d}$, which would be new structure, as for the Majorana scale.

\emph{Refutation condition.} The premise is false if $w_{d}$, or the second family's factor, is derived from the transport structure, from another premise of the register or from a dynamics of the series; or if it is shown to be a function of another registered number.

## technical
The Georgi-Jarlskog pattern needs the $126$ in the down-type sector with a Clebsch coefficient $-3$ between leptons and quarks; the series derives the coefficient (it is the pair part of the square of the Majorana element times the rung vector) but not the weight with which that part enters. The stored relations are all unchanged when the down-type $126$ weight $w_{d}$ is rescaled, while the second family's factor moves (exact models give $3$, $2$ and $37/19$ with the same up, neutrino and Majorana sectors). This premise registers $w_{d}$ as a free input beside $N$, $\epsilon$, $\xi G$ and the Majorana scale; its value comes from the record, $m_{\mu} \approx 3m_{s}$ at the intermediate scale, and with it $m_{b}/m_{\tau}$ there. It would be refuted by a derivation of the weight or of the factor, or by showing it is a function of another registered number.

## lay
In grand unified theories the masses of the down quarks and of the charged leptons are tied together, and the observed pattern, the muon about three times the strange quark at very high energies, needs one particular ingredient to enter with a particular strength. This framework produces the ingredient and its factor of three, but not the strength with which it enters: every relation the framework contains stays true if that strength is changed. This entry records the strength as one of the numbers put in by hand, beside the huge number N, the matter asymmetry, the number that sets the weak scale and the Majorana scale. It would be overturned if the framework were found to fix it.

## one-liner
Premise ($w_{d}$): the down-type $126$ weight $w_{d}f$ against $v_{d}Y$ (equivalently the $(15,1,1)$ weight on the sixteen) is a registered free input, not fixed by any stored relation, its value taken from the record ($m_{\mu} \approx 3m_{s}$ at $M_{I}$, and $m_{b}/m_{\tau}$ there); the Clebsch $-3$ stays derived; refuted by a derivation of the weight or the factor, or by showing it a function of another registered number.
