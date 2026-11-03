---
id: interior.imported-kerr-schild-form-kerr-gauge
kind: claim
version: 1
title: 'Imported: the Kerr-Schild form of the Kerr gauge field'
status: imported
region: interior
subject: interior
tags: [classical-theorem, kerr, null-directions]
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
imported_from:
- citation: R. P. Kerr and A. Schild, Some algebraically degenerate solutions of Einstein's gravitational
    field equations, Proc. Symp. Appl. Math. 17 (1965), 199--209.
  key: KerrSchild1965
- citation: C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003).
  key: DoranLasenby2003
  locator: Ch.~14
- citation: A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans.
    R. Soc. Lond. A 356 (1998), 487--582.
  key: LDG1998
locators:
  paper: T06
  number: Fact 6.1
  label: fact:kerrschild
  line: 778
extraction:
  typing:
    by: ai-typing-pass
    note: 'Imported fact with no derivation; nothing to edge.'
  env: fact
---

## formal
The Kerr solution admits a gauge in which the gauge field is
\[
\hb(a) \;=\; a + H(x)\,(a\cdot k)\,k ,
\]
with $k$ a null vector field tangent to the ingoing principal null congruence, $k^2 = 0$, and $H$ a scalar function ($H = Mr^3/(r^4 + a^2\cos^2\theta\, r^2)$ in Boyer-Lindquist-adapted oblate coordinates; only $k^2 = 0$ enters the algebra below). Schwarzschild is the case $a = 0$ in ingoing Eddington-Finkelstein form. \emph{Provenance:} Kerr-Schild \cite{KerrSchild1965}; the GTG form \cite[Ch.~14]{DoranLasenby2003}, \cite{LDG1998}.

## technical
The Kerr solution admits a gauge in which the gauge field is $\hb(a) = a + H(x)\,(a\cdot k)\,k$, with $k$ tangent to the ingoing principal null congruence, $Q(k) = 0$, and $H$ a scalar function, $H = Mr^3/(r^4 + a^2 r^2\cos^2\theta)$ in oblate coordinates adapted to Boyer-Lindquist. Only the nullity of $k$ enters the algebra built on it. Schwarzschild is the case $a = 0$, in ingoing Eddington-Finkelstein form. This is the classical Kerr-Schild form, imported together with its gauge-theory-gravity presentation.

## lay
A rotating black hole can be described as flat spacetime plus a single correction built along a light-like direction. This is the classical Kerr-Schild form of the solution. The result is taken from the literature.

## one-liner
Kerr admits a gauge field of Kerr-Schild form $\hb(a) = a + H(a\cdot k)k$ with $k$ null, reducing to ingoing Eddington-Finkelstein Schwarzschild at $a = 0$; imported from the literature.
