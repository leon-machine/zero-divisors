---
id: correspondence.imported-nonlinear-graviton
kind: claim
version: 4
title: "Imported: the nonlinear graviton"
status: imported
region: correspondence
subject: conformal-spacetime
tags: [classical-theorem, conformal-spinors, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: R. Penrose, Nonlinear gravitons and curved twistor theory, Gen. Relativ. Gravit. 7 (1976),
    31--52.
  key: Penrose76
locators:
  paper: T09
  number: Fact 6.1
  label: fact:graviton
  line: 787
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 3 -> 4. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  env: fact
  context_refs:
  - correspondence.incidence-relation-chart
  - correspondence.spinor-identification
  typing:
    by: ai-typing-pass
    note: 'Imported result; the context references to the incidence and spinor theorems only translate
      it into the series'' language, so no edges. Levels pass: conditions already kept.'
  source_title: "Imported: the nonlinear graviton"
  source_formal: |-
    For a complex $4$-manifold with anti-self-dual (half-flat) vacuum conformal structure, the $\alpha$-plane distribution defined fibrewise by the ruling of the Klein quadric is integrable; the leaf space of the resulting foliation is a complex $3$-manifold, the \emph{curved twistor space}; spacetime points reappear as rational curves with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$; and the conformal structure is recovered from curve intersection. Conversely such a twistor space determines the half-flat spacetime. \emph{Provenance:} \cite{Penrose76}. In the language of this paper: half-flatness is exactly the condition under which the completion's point space, the fibrewise Klein quadric of Theorem \claimref{correspondence.spinor-identification}, globalises to a deformed twistor space with the incidence dictionary of Theorem \claimref{correspondence.incidence-relation-chart} intact.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Imported result of Penrose's twistor theory: the curved twistor space keeps its name as Penrose's object; the series-language sentence now says the Klein quadric globalises to a deformed projective spinor space. The plain levels avoid the word twistor."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: 'Imported Penrose result: the half-flat proposition mentions it only to explain the signature restriction, and its one user is the googly conjecture, already linked by lineage.'
  flags:
  - 'beyond one flat chart: the complex half-flat four-manifold and its curved twistor space (a leaf space)'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG FLAG: the complex four-manifold with half-flat conformal structure and its curved twistor space are global and complex, not a single real gravitational field on flat spacetime; the flag sentence of DICTIONARY.md section 14 is added, naming and noting that even the pointwise condition (a Weyl map of one handedness only) needs a complexified field, so no part is restated on a real flat chart. Imported content unchanged.'
---

## formal
For a complex $4$-manifold with anti-self-dual (half-flat) vacuum conformal structure, the $\alpha$-plane distribution defined fibrewise by the ruling of the Klein quadric is integrable; the leaf space of the resulting foliation is a complex $3$-manifold, the \emph{curved twistor space}; spacetime points reappear as rational curves with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$; and the conformal structure is recovered from curve intersection. Conversely such a curved twistor space determines the half-flat spacetime. \emph{Provenance:} \cite{Penrose76}. In the language of this paper: half-flatness is exactly the condition under which the completion's point space, the fibrewise Klein quadric of Theorem \claimref{correspondence.spinor-identification}, globalises to a deformed projective spinor space with the incidence dictionary of Theorem \claimref{correspondence.incidence-relation-chart} intact. \emph{Beyond one flat chart.} The complex four-manifold with its half-flat conformal structure, and the curved twistor space as the leaf space of its $\alpha$-plane foliation, are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). Even the pointwise condition needs the complex setting: the Weyl map $\mathcal{W}$ of a real field is linear over $\{1, I\}$ with $I^{2} = -1$, so a nonzero $\mathcal{W}$ of one handedness only exists for a complexified field, and the statement is read on the complex manifold, whose half-flatness is that condition on the Weyl part of its curvature.

## technical
Penrose's nonlinear graviton: on a complex $4$-manifold with anti-self-dual (half-flat) vacuum conformal structure, the $\alpha$-plane distribution given fibrewise by the ruling of the Klein quadric is integrable. Its leaf space is a complex $3$-manifold, Penrose's curved twistor space, in which spacetime points reappear as rational curves with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$, and the conformal structure is recovered from how these curves intersect. Conversely such a curved twistor space determines the half-flat spacetime.

In the language of the series, half-flatness is exactly the condition under which the completion's point space, the fibrewise Klein quadric of the spinor identification, globalises to a deformed projective spinor space with the incidence dictionary intact. Its complex half-flat four-manifold and curved twistor space are global: no single gravitational field on flat spacetime carries them, so that part is read on complexified charts (holomorphic gauge fields on open sets of $\C^{4}$) glued by holomorphic gauge transformations, the twistor space being the leaf space of their $\alpha$-plane foliation.

## lay
Penrose showed that a complex spacetime whose vacuum curvature has one handedness only (anti-self-dual, or half-flat) can be encoded in a curved three-dimensional complex space, a deformation of the projective spinor space of the conformal algebra. Points of spacetime become curves in that space, and the spacetime geometry can be read back from how those curves meet; the construction also runs in reverse. Here it is quoted as an established result and restated in the series' language.

## one-liner
A half-flat complex vacuum spacetime is equivalent to a curved complex 3-manifold (Penrose's curved twistor space) whose rational curves are the spacetime points, which in the series' terms is the globalisation of the fibrewise Klein quadric with the incidence dictionary intact.
