---
id: pairing.imported-spin-coefficients-null-tetrad
kind: claim
version: 3
title: 'Imported: the spin coefficients of a null tetrad'
status: imported
region: pairing
subject: einstein
tags: [classical-theorem, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'GA rewrite (complexification unit named)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: E. Newman, R. Penrose, An approach to gravitational radiation by a method of spin coefficients,
    J. Math. Phys. 3 (1962) 566--578.
  key: NewmanPenrose1962
- citation: 'R. Penrose, W. Rindler, Spinors and Space-Time, Vol. 1: Two-Spinor Calculus and Relativistic
    Fields, Cambridge University Press (1984).'
  key: PenroseRindler1
  locator: Ch.~4
- citation: R. M. Wald, General Relativity, University of Chicago Press (1984).
  key: Wald1984
  locator: Sec.~12.5
locators:
  paper: T05-pairing
  number: Fact 1.4
  label: fact:NP
  line: 196
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The complexification of the tetrad vectors m, m-bar is named: the central pseudoscalar I_5 = I_4 e of the odd extension (U3), the coefficients read in span{1, I_5} (reader R03); the GA statement through (X.D) l was already primary; status imported.'
  typing:
    by: ai-typing-pass
    note: Imported classical result; levels only.
  env: fact
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [pairing.static-frame-only-expansion-survives, pairing.regular-frame-class-vanishes-horizon-changes]
    added_about: []
    verdict: connected
    note: 'Both Schwarzschild propositions read their pairing classes as spin coefficients (geodesic, shear-free, expansion) through this Fact; no definition in the store concerns it, so no about.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the null tetrad is a tetrad of physical vectors of a gravitational field on flat spacetime, the metric pairing is the flat product, the Levi-Civita derivative nabla_X is the covariant derivative X.D, and the Killing horizon is the locus where the Killing field is null and normal. Coefficients, geometric meanings and the horizon statement unchanged.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime with covariant derivative $D$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), and $(\ell, n, m, \mb)$ a null tetrad of physical vector fields on its invertible region (complexified for $m$, $\mb$ by the central pseudoscalar $I_{5} = I_{4}e$ of the odd extension $\Cl(2,3)$, the unit that commutes with every vector, conventions U3; $\mb$ is $m$ with $I_{5} \mapsto -I_{5}$, and the coefficients are numbers of $\mathrm{span}\{1, I_{5}\}$), with $\ip{\cdot}{\cdot}$ the flat product of physical vectors, the derived metric. The four spin coefficients of the first kind are the components on $\ell, n, m, \mb$ of the linear form $X \mapsto \ip{(X \cdot D)\, \ell}{m}$, up to the normalisation of the tetrad and the sign conventions of the formalism:
\[
\kappa \leftrightarrow \ip{(\ell \cdot D)\, \ell}{m}, \qquad \tau \leftrightarrow \ip{(n \cdot D)\, \ell}{m}, \qquad \sigma \leftrightarrow \ip{(m \cdot D)\, \ell}{m}, \qquad \rho \leftrightarrow \ip{(\mb \cdot D)\, \ell}{m}
\]
(in metric language, $\ip{\nabla_X \ell}{m}$ for the Levi-Civita derivative of the derived metric).
Geometrically: $\kappa = 0$ if and only if the integral curves of $\ell$ are geodesics (worldlines along which $\ell$ is $D$-parallel up to rescaling) (this $\kappa$ is the formalism's geodesy coefficient, not the surface gravity the singularity paper writes with the same letter); $\sigma$ is the shear of the congruence of $\ell$; $\rho$ is minus its expansion (real part) and twist (imaginary part) in the standard sign convention, so that an expanding congruence has $\rho < 0$ and the radial rays of a vanishing field ($\hb = 1$, $\Omega = 0$) have $\rho = -1/r$; and $\tau$ is the rate at which $\ell$ turns transversely along $n$. The remaining eight spin coefficients are the components of $\ip{(X \cdot D)\, \ell}{n}$, $\ip{(X \cdot D)\, m}{\mb}$ and $\ip{(X \cdot D)\, n}{\mb}$: they rescale $\ell$, rotate $m$ in its plane, and tilt $n$ and $\mb$ by null rotations about $\ell$, all of which keep $\ell$ and $m$ in their span. On a Killing horizon, the locus where a Killing field $K$ is null and normal to it, the generators have $\kappa = \sigma = \rho = 0$ in any tetrad regular there. \emph{Provenance:} \cite{NewmanPenrose1962}; \cite[Ch.~4]{PenroseRindler1}; the horizon statement \cite[Sec.~12.5]{Wald1984}.

## technical
For a gravitational field on flat spacetime and a null tetrad $(\ell, n, m, \mb)$ of physical vectors, the four spin coefficients of the first kind are the components of the linear form $X \mapsto \ip{(X \cdot D)\,\ell}{m}$, with $D$ the covariant derivative and the flat product of physical vectors: $\kappa$, $\tau$, $\sigma$, $\rho$ correspond to $X = \ell, n, m, \mb$, up to normalisation and sign conventions. $\kappa = 0$ exactly when the integral curves of $\ell$ are geodesics, $\sigma$ is the shear, $\rho$ is minus the expansion (real part) and twist (imaginary part), so that radial rays with no gravitational field have $\rho = -1/r$, and $\tau$ is the rate at which $\ell$ turns transversely along $n$.

The other eight coefficients rescale $\ell$, rotate $m$ in its plane, and tilt $n$ and $\mb$ by null rotations about $\ell$, all keeping $\ell$ and $m$ in their span. On a Killing horizon the generators have $\kappa = \sigma = \rho = 0$ in any tetrad regular there. Imported from Newman and Penrose, Penrose and Rindler, and Wald.

## lay
The Newman-Penrose spin coefficients are a standard set of numbers describing how a family of light rays bends, spreads, shears and twists as it travels. Four of them measure how the ray direction tilts out of its plane; the others only relabel it. On a black hole horizon the light rays that make up the horizon neither bend, shear nor spread.

## one-liner
The four first-kind spin coefficients $\kappa, \tau, \sigma, \rho$ of a null tetrad of physical vectors are the components of $\ip{(X \cdot D)\,\ell}{m}$, measuring geodesy, transverse turning, shear, and expansion with twist.
