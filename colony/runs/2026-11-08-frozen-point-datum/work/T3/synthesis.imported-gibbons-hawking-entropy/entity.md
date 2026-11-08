---
id: synthesis.imported-gibbons-hawking-entropy
kind: claim
version: 4
title: 'Imported: the entropy of the cosmological horizon (Gibbons-Hawking)'
status: imported
region: synthesis
subject: entropy
tags: [horizons, classical-theorem, cosmological-constant]
proposed_by:
  kind: ai
  session: de-sitter-count-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: restated with H as the rational datum
  version: 4
  source: run 2026-11-08-frozen-point-datum
amendments:
- version: 4
  kind: restatement
  defect: 'Wording only: the formal level defined the Hubble rate as H = sqrt(Lambda/3), a square root of a multiple of Lambda, which over the series'' rational scalars exists only for special Lambda; written now with H as the datum, Lambda = 3H^2. The content, over R, is unchanged.'
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: G. W. Gibbons and S. W. Hawking, Cosmological event horizons, thermodynamics, and particle creation, Phys. Rev. D 15 (1977), 2738--2751.
  key: GibbonsHawking1977cosmo
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: 'Version 3 -> 4. Leon''s decision of 8 November 2026 (op.frozen-point-rational-datum): wording only, with H as the datum (Lambda = 3H^2); the content, over R, is unchanged. The Hubble rate H = sqrt(Lambda/3) of the formal level written H, Lambda = 3H^2; every other formula of the Fact was already in H. Citation and content unchanged.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'de Sitter chart sign corrected: beta = -rH (expanding chart, free fall dr/dt = Hr), so that the chart contains the future cosmological horizon the note sentence names; with beta = +rH it is the contracting chart and contains the past horizon. Checked exactly in verify/dictionary_identities.py.'
  note: Imported for the count of the cosmological horizon's boundary modes; the series states the black-hole area law and its calibration but not the de Sitter one.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity per Leon 2026-10-23 (DICTIONARY, Bifurcation surfaces): the area is that of a cross-section of the horizon locus r = 1/H in the static Painleve-Gullstrand chart of the de Sitter field (area 4 pi/H^2, surface gravity H), replacing the bifurcation sphere; note sentence added. Same entropy and temperature.'
---

## formal
In units $\hbar = c = k_{B} = 1$, the event horizon of a static observer in the de Sitter gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) of Hubble rate $H$, $\Lambda = 3H^{2}$, has the entropy
\[
S_{\Lambda} \;=\; \frac{A_{\Lambda}}{4G}, \qquad A_{\Lambda} \;=\; \frac{4\pi}{H^{2}},
\]
a quarter of the area of a cross-section of the cosmological horizon locus $r = 1/H$ in the static Painlev\'e-Gullstrand chart of de Sitter space ($\hb = 1 - \beta P$, $\beta = -rH$, the expanding chart, whose free-fall observers have $dr/dt = Hr$ and which contains the static observer's future horizon), of area $4\pi/H^{2}$, on which the static Killing field is null and normal with surface gravity $H$, in Planck units, at the temperature $H/2\pi$ \cite{GibbonsHawking1977cosmo}.

The bifurcation surface itself, where the boost flow has its fixed points, lies beyond one flat chart (it is the meeting of the four regions of the maximal extension); the chart contains the future horizon, on whose cross-sections the area, the surface gravity and the boost flow are those stated.

## technical
Gibbons and Hawking showed that the horizon of an observer in de Sitter space carries thermodynamics like a black hole's: the temperature $H/2\pi$ and an entropy equal to a quarter of the horizon's area in Planck units. In Gauge Theory Gravity the de Sitter field on flat spacetime has, in its static Painlev\'e-Gullstrand chart, a horizon locus at $r = 1/H$; each cross-section of it is a sphere of radius $1/H$, so its area is $4\pi/H^{2}$, and there the static Killing field is null with surface gravity $H$. The bifurcation sphere itself lies beyond one flat chart; the chart's cross-sections carry the same area.

## lay
In a universe with a positive cosmological constant, each observer's horizon behaves like the surface of a black hole: it has a temperature and an entropy, and the entropy is a quarter of the horizon's area measured in the smallest natural units of area. This is a standard result of 1977, taken here from the literature.

## one-liner
The cosmological horizon of the de Sitter field has entropy $A/4G = \pi/(GH^{2})$, a quarter of the area of a horizon cross-section in Planck units (Gibbons-Hawking).
