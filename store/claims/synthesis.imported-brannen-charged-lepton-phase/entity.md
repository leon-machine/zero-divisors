---
id: synthesis.imported-brannen-charged-lepton-phase
kind: claim
version: 1
title: 'Imported: Brannen''s charged-lepton phase (Brannen 2006)'
status: imported
region: synthesis
subject: generations
tags: [flavour-and-mixing, mass-generation, confronted-with-data]
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
imported_from:
- citation: 'C. A. Brannen, The lepton masses, preprint, 2 May 2006, brannenworks.com/MASSWS2.pdf, equations (4) and (14).'
  key: Brannen2006
extraction:
  note: >-
    Imported because synthesis.koide-channel-phase-is-no-symmetry-angle tests the value 2/9 of the channel
    phase and attributes it to Brannen 2006. That result does not rest on it: it fixes the phase from the
    stored electron and muon masses and tests 2/9 as a number, so no uses edge is drawn; this Fact records
    the attribution. Checked on 2026-10-31 against the preprint itself: equation (4) gives the eigenvalues
    lambda_n = mu (1 + 2 eta cos(delta + 2 n pi / 3)), read as square roots of the charged-lepton masses;
    equation (14) gives mu_1 = 17716.13(109) eV^(1/2), eta_1^2 = 0.500003(23), delta_1 = 0.2222220(19); and
    the text says delta_1 is close to 2/9. The fit uses the lepton masses of its time.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created by the maintainer pass of 2026-10-31 (literature cited from memory by an accepted result; Leon''s list of imports).'
---

## formal
Brannen writes the square roots of the three charged-lepton masses as the eigenvalues of a $3 \times 3$ circulant,
\[
\sqrt{m_{n}} \;=\; \mu\bigl(1 + 2\eta\cos(\delta + 2n\pi/3)\bigr), \qquad n = 0, 1, 2,
\]
where $\eta^{2} = \tfrac12$ is the Koide relation, and fits $\mu = 17716.13(109)$ eV$^{1/2}$, $\eta^{2} = 0.500003(23)$ and $\delta = 0.2222220(19)$ to the measured masses, observing that $\delta$ is close to $\tfrac29$. This is an empirical fit, not a derivation. \emph{Provenance:} \cite{Brannen2006}, equations (4) and (14).

## technical
Koide's relation says that the sum of the three charged-lepton masses is two thirds of the square of the sum of their square roots. Brannen wrote the square roots as the eigenvalues of a circulant matrix, $\mu(1 + \sqrt2\cos(\delta + 2n\pi/3))$ when the Koide relation holds exactly, so that the masses are fixed by a scale $\mu$ and one phase $\delta$. Fitted to the lepton masses, the phase came out as $0.2222220$ with an uncertainty in the seventh decimal place, close to $\tfrac29$; the fit is an observation and no mechanism is given for the value.

## lay
The masses of the electron, muon and tau satisfy a surprisingly precise numerical relation found by Koide. Brannen noticed that, written in a natural way, the relation leaves one angle free, and that the measured masses make that angle very close to two ninths. Whether that closeness means anything is not known.

## one-liner
Brannen (2006): $\sqrt{m_{n}} = \mu(1 + \sqrt2\cos(\delta + 2n\pi/3))$ fits the charged leptons with $\delta = 0.2222220(19)$, close to $\tfrac29$.
