---
id: synthesis.imported-taub-nut-field-and-misner-extension
kind: claim
version: 1
title: 'Imported: the Taub-NUT field and Misner''s extension (Taub; NUT; Misner)'
status: imported
region: synthesis
subject: interior
tags: [horizons, kasner, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'A. H. Taub, Empty space-times admitting a three parameter group of motions, Ann. of Math. 53 (1951), 472--490.'
  key: Taub1951
- citation: 'E. Newman, L. Tamburino and T. Unti, Empty-space generalization of the Schwarzschild metric, J. Math. Phys. 4 (1963), 915--923.'
  key: NTU1963
- citation: 'C. W. Misner, The flatter regions of Newman, Unti, and Tamburino''s generalized Schwarzschild space, J. Math. Phys. 4 (1963), 924--937.'
  key: Misner1963
- citation: 'S. W. Hawking and G. F. R. Ellis, The Large Scale Structure of Space-Time, Cambridge University Press (1973), Section 5.8.'
  key: HawkingEllis1973
extraction:
  note: >-
    Imported for the Taub-NUT counter-model of the Hubble-normalised limit, which cites the solution
    and the Cauchy-horizon identification from memory. That result verifies the field equations of
    its Taub region itself, and states that the identification of t = t_+ as a Cauchy horizon is
    cited and not used in its clauses (i) to (iv); this Fact records the citation and is not a
    premise of that result. Misner 1963 (title, J. Math. Phys. 4, 924) was confirmed by a web search
    of its bibliographic record on 2026-10-31; the other citations, page ranges and the Hawking and
    Ellis section number are cited from memory, and the statements were not checked against the
    sources.
  flags:
  - 'beyond one flat chart: the Taub and NUT regions joined across t = t_+ in Misner''s extension, on the U(1) bundle over the two-sphere'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created by the maintainer pass of 2026-10-31 (literature cited from memory by an accepted result; Leon''s list of imports).'
---

## formal
For constants $m$ and $l > 0$ let $U(t) = (-t^{2} + 2mt + l^{2})/(t^{2} + l^{2})$, $t_{\pm} = m \pm \sqrt{m^{2} + l^{2}}$, and let $\sigma_{1}, \sigma_{2}, \sigma_{3}$ be the left-invariant one-forms of $SU(2)$. On $t_{-} < t < t_{+}$, where $U > 0$, the gravitational field on flat spacetime whose derived metric is
\[
U^{-1}dt^{2} - (2l)^{2}\,U\,\sigma_{3}^{2} - (t^{2} + l^{2})(\sigma_{1}^{2} + \sigma_{2}^{2})
\]
is a vacuum field (the Taub region, a diagonal Bianchi IX cosmology with $a_{1} = a_{2}$; Taub 1951), and for $U < 0$ the same expression with $t$ spacelike is the NUT region (Newman, Tamburino and Unti 1963). The metric component along $\sigma_{3}$ vanishes at $t = t_{\pm}$ while the field strength stays bounded there. \emph{Beyond one flat chart.} In Misner's extension, coordinates adapted to the null directions continue the Taub region analytically across $t = t_{+}$ and $t = t_{-}$ into NUT regions, with the slices of constant $t$ compact; the surfaces $t = t_{\pm}$ are compact null hypersurfaces ruled by closed null geodesics, the Cauchy horizons of the Taub region's maximal globally hyperbolic development, beyond which closed timelike curves occur. The extension is not unique: there are two inequivalent ones across each horizon, and the region they produce is not carried by a single gravitational field on flat spacetime. \emph{Provenance:} \cite{Taub1951}; \cite{NTU1963}; \cite{Misner1963}; \cite[Section 5.8]{HawkingEllis1973}.

## technical
Taub-NUT is the vacuum solution of Einstein's equations with a three-sphere's worth of homogeneity: in its Taub region it is a homogeneous, anisotropic cosmology of Bianchi type IX with two equal scale factors, which expands from $t_{-}$ and recollapses toward $t_{+}$, and the third scale factor goes to zero at both ends while the field strength stays finite. Misner showed that the solution extends smoothly past these ends into stationary NUT regions, and that the boundary surfaces are Cauchy horizons: compact null surfaces made of closed light rays, beyond which causality fails. The continuation exists in two inequivalent ways across each horizon. The extended spacetime needs several charts of flat spacetime, glued by gauge transformations; it is not one gravitational field on one flat chart.

## lay
Taub-NUT is a famous exact solution of Einstein's equations describing an empty universe that is the same at every point of a three-dimensional sphere but stretched differently in different directions. It lasts only a finite time, and at its end, rather than crashing into a singularity, it reaches a boundary beyond which the past and future can no longer be predicted from the starting data, and time loops become possible. It is the standard example of a spacetime whose predictability ends at such a boundary.

## one-liner
The Taub-NUT field $U^{-1}dt^{2} - 4l^{2}U\sigma_{3}^{2} - (t^{2} + l^{2})(\sigma_{1}^{2} + \sigma_{2}^{2})$ is vacuum, and in Misner's extension the ends $t = t_{\pm}$ of its Taub region are compact Cauchy horizons of closed null geodesics (Taub 1951; Newman, Tamburino and Unti 1963; Misner 1963).
