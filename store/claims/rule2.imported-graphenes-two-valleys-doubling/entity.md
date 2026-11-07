---
id: rule2.imported-graphenes-two-valleys-doubling
kind: claim
version: 2
title: 'Imported: graphene''s two valleys, and the doubling'
status: imported
region: rule2
subject: completion
tags: [classical-theorem, no-go]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'GA rewrite (the two valleys stated as the two representations of the planar algebra)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: typed
imported_from:
- citation: G. W. Semenoff, Condensed-matter simulation of a three-dimensional anomaly, Phys. Rev. Lett.
    53 (1984) 2449--2452.
  key: Semenoff1984
- citation: H. B. Nielsen, M. Ninomiya, Absence of neutrinos on a lattice (I). Proof by homotopy theory,
    Nucl. Phys. B 185 (1981) 20--40.
  key: NielsenNinomiya1981
- citation: 'V. P. Gusynin, S. G. Sharapov, J. P. Carbotte, AC conductivity of graphene: from tight-binding
    model to 2+1-dimensional quantum electrodynamics, Int. J. Mod. Phys. B 21 (2007) 4611--4658.'
  key: GSC2007
locators:
  paper: T17-rule2
  number: Fact 4.2
  label: fact:graphene
  line: 241
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Imported Fact restated in GA (status imported kept): the valleys'' gamma matrices differing by the sign of one spatial gamma matrix are written as the two inequivalent two-component representations of Cl(1,2), whose frames differ by the sign of one spatial vector, equivalently by the sign of the central pseudoscalar I_3 = gamma_0gamma_1gamma_2. Verified with lib/GA.py in Cl(1,2) and Cl(2,1): I_3 is central with square -1, and flipping one vector flips it. The source''s form moved to extraction.source_formal. Reader R11 had proposed a declaration; the restatement is exact, so none is needed.'
  source_formal: |-
    The low-energy theory of electrons on the honeycomb lattice consists of two two-component Dirac fermions, one at each of the two inequivalent corners $K, K'$ of the Brillouin zone, whose gamma matrices differ by the sign of one spatial gamma matrix; a lattice regularisation of a single two-component species is excluded by the fermion-doubling theorem, so the pair is forced. \emph{Provenance:} \cite{Semenoff1984, NielsenNinomiya1981, GSC2007}.
    
    The source states the two species with gamma matrices that differ by the sign of one spatial gamma matrix; the store restates this in the planar algebra Cl(1,2): the two inequivalent two-component representations, whose frames differ by the sign of one spatial vector, equivalently by the sign of the central pseudoscalar gamma_0 gamma_1 gamma_2.
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported physics result; levels describe the cited condensed-matter statement only.
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: 'Imported condensed-matter physics used only in a reading remark of the Rule 2 note; the planar proposition does not rest on it.'
---

## formal
The low-energy theory of electrons on the honeycomb lattice consists of two two-component Dirac fermions, one at each of the two inequivalent corners $K, K'$ of the Brillouin zone. In the planar algebra $\Cl(1,2)$, with frame $\gamma_{0}, \gamma_{1}, \gamma_{2}$ and central pseudoscalar $I_{3} = \gamma_{0}\gamma_{1}\gamma_{2}$ ($I_{3}^{2} = -1$), the two species carry the two inequivalent two-component representations, whose frames differ by the sign of one spatial vector ($\gamma_{k} \mapsto -\gamma_{k}$ for one $k$), equivalently by the sign of $I_{3}$; a lattice regularisation of a single two-component species is excluded by the fermion-doubling theorem, so the pair is forced. \emph{Provenance:} \cite{Semenoff1984, NielsenNinomiya1981, GSC2007}.

## technical
Near the two inequivalent corners $K$ and $K'$ of the Brillouin zone, electrons on the honeycomb lattice are described at low energy by two two-component Dirac fermions, carrying the two inequivalent representations of the planar algebra $\Cl(1,2)$: their frames differ by the sign of one spatial vector, which flips the central pseudoscalar.

The fermion-doubling theorem rules out a lattice regularisation of a single two-component species, so the pair is forced.

## lay
At low energies the electrons in graphene behave like two kinds of massless relativistic particles, one at each of two special points in momentum space. The two kinds are mirror images of each other along one direction. A general theorem about lattices says they must come as a pair, since a single kind cannot be put on a lattice.

## one-liner
Graphene's low-energy electrons form two two-component Dirac fermions at the valleys $K$ and $K'$, the two representations of the planar algebra $\Cl(1,2)$ (frames differing by the sign of one spatial vector), and the fermion-doubling theorem forces the pair.
