---
id: interior.imported-mass-inflation-stability
kind: claim
version: 3
title: 'Imported: mass inflation and $C^0$ stability'
status: imported
region: interior
subject: interior
tags: [classical-theorem, kerr, horizons]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: E. Poisson and W. Israel, Internal structure of black holes, Phys. Rev. D 41 (1990), 1796--1809.
  key: PoissonIsrael1990
- citation: 'M. Dafermos and J. Luk, The interior of dynamical vacuum black holes I: the $C^0$-stability
    of the Kerr Cauchy horizon, preprint, arXiv:1710.01722 (2017).'
  key: DafermosLuk2017
- citation: J. Luk and S.-J. Oh, Strong cosmic censorship in spherical symmetry for two-ended asymptotically
    flat initial data I. The interior of the black hole region, Ann. of Math. (2) 190 (2019), 1--111.
  key: LukOh2019a
- citation: J. Luk and S.-J. Oh, Strong cosmic censorship in spherical symmetry for two-ended asymptotically
    flat initial data II. The exterior of the black hole region, Ann. PDE 5 (2019), Art. 6.
  key: LukOh2019b
- citation: 'A. Ori, Inner structure of a charged black hole: an exact mass-inflation solution, Phys.
    Rev. Lett. 67 (1991), 789--792.'
  key: Ori1991
locators:
  paper: T06
  number: Fact 6.10
  label: fact:cauchy
  line: 892
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 2 -> 3. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  typing:
    by: ai-typing-pass
    note: 'Imported fact with no derivation; nothing to edge.'
  env: fact
  flags:
  - 'beyond one flat chart: the Cauchy horizon of the maximal development of two-ended data and the extension across it'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement (MIXED): the regularity statements are read for the gravitational field on flat spacetime through its derived metric and connection (Christoffel symbols as connection components); the Cauchy horizon of the maximal development of two-ended data, and the extension across it, are flagged beyond one flat chart (DICTIONARY.md section 14, item 3). Imported content unchanged.'
---

## formal
(i) Infalling radiation is blueshifted without bound at the Kerr Cauchy horizon, generically driving unbounded growth of the quasi-local (Hawking) mass: mass inflation. (ii) For dynamical vacuum perturbations of Kerr initial data, the derived metric of the gravitational field $(\hb, \Omega)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) extends continuously ($C^0$) across the Cauchy horizon. (ii$'$) In spherical symmetry (the Einstein-Maxwell-scalar field system with two-ended asymptotically flat data), the derived metric extends continuously across the Cauchy horizon while, generically, its Christoffel symbols (the components of the connection, Fact \claimref{synthesis.imported-gtg-dictionary}(ii)) fail to be locally square-integrable: a weak null singularity. The same generic failure, with blow-up of the field strength $\mathcal{R}(B)$, is the expected picture for the Kerr perturbations of (ii); it is stated there as a conjecture and is not proved. (iii) Tidal deformations of infalling observers remain finite through the weak null singularity. \emph{Provenance:} (i) Poisson-Israel \cite{PoissonIsrael1990}; (ii) Dafermos-Luk \cite{DafermosLuk2017}; (ii$'$) Luk-Oh \cite{LukOh2019a,LukOh2019b}; (iii) Ori \cite{Ori1991}. \emph{Beyond one flat chart.} The Cauchy horizon, as the boundary of the maximal development of two-ended data, and the extension of the field across it are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region (the blueshift and mass growth, and the regularity classes of the field and its connection along the approach) are in Gauge Theory Gravity, and the Cauchy horizon and the extension across it are read on the manifold assembled from the derived metric's charts.

## technical
Four imported results on the Kerr Cauchy horizon. Infalling radiation is blueshifted without bound there, generically driving unbounded growth of the Hawking mass: mass inflation. For dynamical vacuum perturbations of Kerr initial data the derived metric of the gravitational field extends continuously ($C^0$) across the Cauchy horizon. In spherical symmetry, for the Einstein-Maxwell-scalar field system with two-ended asymptotically flat data, the derived metric extends continuously while its Christoffel symbols, the connection components, generically fail to be locally square-integrable, a weak null singularity; the same generic failure for Kerr is a conjecture, not proved. Tidal deformations of infalling observers stay finite through the weak null singularity. Its Cauchy horizon of two-ended data, and the extension across it, are global: no single gravitational field on flat spacetime carries them, so that part is read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
The inner horizon of a charged or rotating black hole is unstable. Radiation falling in piles up there and the strength of the gravitational field grows without limit, yet the field itself remains continuous and an infalling object is stretched only by a finite amount. These are established results of mathematical relativity taken from the literature; for rotating black holes part of the picture is still conjectural.

## one-liner
At the perturbed Kerr Cauchy horizon there is mass inflation and the derived metric extends continuously, and in spherical symmetry the connection generically fails to be square-integrable while tidal deformations stay finite; imported from the literature.
