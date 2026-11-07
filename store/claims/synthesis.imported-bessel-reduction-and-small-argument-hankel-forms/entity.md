---
id: synthesis.imported-bessel-reduction-and-small-argument-hankel-forms
kind: claim
version: 1
title: 'Imported: Bessel reduction and small-argument Hankel forms (DLMF)'
status: imported
region: synthesis
subject: dark-energy
tags: [classical-theorem, kasner]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'F. W. J. Olver et al. (eds.), NIST Digital Library of Mathematical Functions, Release 1.2.'
  key: DLMF
  locator: 'eq. 10.13.5; Section 10.7'
  url: https://dlmf.nist.gov/10.13
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the Hankel forms are quoted from the literature with the i of complex analysis, as the entity says; declared (version and levels unchanged).'
  note: >-
    Imported so that synthesis.kasner-hidden-scale-coupled-scalars-stay-blue and
    synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling
    can pin the Bessel reduction and the small-argument Hankel forms they cited from memory. Checked
    on 2026-11-01 against DLMF eq. 10.13.5: z^2 w'' + (1 - 2r) z w' + (lambda^2 q^2 z^(2q) + r^2 -
    nu^2 q^2) w = 0 has the solutions w = z^r C_nu(lambda z^q), C_nu any cylinder function of order
    nu; the form stated here is that equation divided by z^2 with r = a, q = c, lambda = 1, nu =
    |a/c|. The small-argument forms (DLMF Section 10.7) are cited from memory; that page could not
    be reached for this check. The DLMF release number is from memory.
    The bare i in the Hankel forms is the unit of complex analysis (special functions of a complex variable), not the field theory's unit.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of the Bessel reduction formula and the small-argument Hankel forms as routine Facts).'
outside_ga:
  kind: imported
  why: 'the small-argument Hankel forms H_nu(z) ~ -(i/pi) Gamma(nu)(2/z)^nu and H_0(z) ~ (2i/pi) ln z are quoted as the source states them, with i the unit of complex analysis'
---

## formal
For constants $a$ and $c \ne 0$, the equation
\[
y'' + \frac{1 - 2a}{x}\,y' + c^{2}x^{2c - 2}\,y = 0
\]
has the general solution $y = x^{a}Z_{\nu}(x^{c})$, $\nu = |a/c|$, with $Z_{\nu}$ any cylinder function of order $\nu$ (a combination of $J_{\nu}$ and $Y_{\nu}$, or of the Hankel functions $H^{(1)}_{\nu}$, $H^{(2)}_{\nu}$); it is the case $r = a$, $q = c$, $\lambda = 1$ of DLMF 10.13.5. As $z \to 0$, for $\Re\nu > 0$, $Y_{\nu}(z) \sim -\tfrac{1}{\pi}\Gamma(\nu)(\tfrac{2}{z})^{\nu}$ and $H^{(1)}_{\nu}(z) \sim -H^{(2)}_{\nu}(z) \sim -\tfrac{i}{\pi}\Gamma(\nu)(\tfrac{2}{z})^{\nu}$, so $|H^{(1)}_{\nu}(z)|^{2} \sim \Gamma(\nu)^{2}(2/z)^{2\nu}/\pi^{2}$; for $\nu = 0$, $H^{(1)}_{0}(z) \sim \tfrac{2i}{\pi}\ln z$. Here $i$ is the unit of complex analysis. \emph{Provenance:} \cite{DLMF} (eq. 10.13.5; Section 10.7).

## technical
A wave equation with a time-dependent friction term and a frequency that grows as a power of time reduces to Bessel's equation after a change of variable; the order of the Bessel function is the ratio of the friction exponent to the frequency exponent. The Hankel functions describe the mode that starts in its vacuum, and their behaviour at small argument, a power set by the order, gives the spectrum of the mode after it has stopped oscillating.

## lay
These are textbook properties of Bessel functions, the standard functions that describe waves whose medium changes as a power of time. They are what turns the equations for field fluctuations near a Kasner singularity into a definite tilt of the spectrum.

## one-liner
$y'' + \tfrac{1 - 2a}{x}y' + c^{2}x^{2c - 2}y = 0$ is solved by $x^{a}Z_{|a/c|}(x^{c})$, and $H^{(1)}_{\nu}(z) \sim -\tfrac{i}{\pi}\Gamma(\nu)(2/z)^{\nu}$ as $z \to 0$ for $\Re\nu > 0$ (DLMF 10.13.5, 10.7).
