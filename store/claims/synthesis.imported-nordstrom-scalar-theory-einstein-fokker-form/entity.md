---
id: synthesis.imported-nordstrom-scalar-theory-einstein-fokker-form
kind: claim
version: 1
title: 'Imported: Nordstr\"om''s scalar theory of gravitation in the Einstein-Fokker form (vanishing Weyl curvature, scalar curvature proportional to the stress trace), which deflects no light and gives minus one sixth of Einstein''s perihelion advance, so is excluded by observation'
status: imported
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, classical-theorem, confronted-with-data]
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'A. Einstein and A. D. Fokker, Die Nordstr\"omsche Gravitationstheorie vom Standpunkt des absoluten Differentialkalk\"uls, Ann. Phys. (Leipzig) 349 (1914), 321--328.'
  key: EinsteinFokker1914
  doi: 10.1002/andp.19143491009
- citation: 'G. Nordstr\"om, Zur Theorie der Gravitation vom Standpunkt des Relativit\"atsprinzips, Ann. Phys. (Leipzig) 42 (1913), 533--554.'
  key: Nordstrom1913
- citation: 'N. Deruelle and M. Sasaki, Conformal transformations and Nordstr\"om''s scalar theory of gravity, Prog. Theor. Phys. Suppl. 190 (2011), 143--154; arXiv:1012.5386.'
  key: DeruelleSasaki2011
  locator: 'Sec. II.3; Sec. III.1, Eq. (3.7)'
  doi: 10.1143/PTPS.190.143
- citation: 'C. W. Misner, K. S. Thorne and J. A. Wheeler, Gravitation, Freeman, San Francisco (1973).'
  key: MTW1973
  locator: 'Exercise 7.1'
extraction:
  note: >-
    Imported so that the result on twistor-flat fields (Nordstrom's equations meet the consistency conditions
    that Einstein's do not single out) can pin Nordstrom's theory and its observational failures instead of
    citing them from memory. Checked on 2026-11-01: the bibliographic data of Einstein and Fokker 1914
    (authors, title, journal, volume 349, issue 10, pages 321-328, DOI) against the Crossref record; the content
    against the arXiv text of Deruelle and Sasaki, arXiv:1012.5386: Sec. III.1, Eq. (3.7), the geometric
    (Einstein-Fokker) form for F(Phi) = Phi, with vanishing Weyl tensor (the metric conformally flat), scalar
    curvature equal to 24 pi G/c^4 times the trace of the matter stress tensor and the matter conserved; Sec.
    II.3, ultra-relativistic particles are not deflected (PPN gamma = -1), and the perihelion shift is
    -(1 + a2)/6 times Einstein's, a2 = 0 for F(Phi) = Phi, so -1/6 of Einstein's (beta = 1/2), and the theories
    are ruled out by observation. Cited from memory, not checked: the bibliographic data of Nordstrom 1913, the
    volume and pages of the Deruelle-Sasaki journal version (the DOI is from the arXiv record), and Misner,
    Thorne and Wheeler's exercise number. The store-sign form of the scalar equation is the one recomputed in
    the citing result.
---

## formal
Let $(\hb, \Omega)$ be a torsion-free gravitational field on four-dimensional flat spacetime, signature $(+,-,-,-)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with store curvature $\mathcal{R}$ and Weyl curvature $\mathcal{W}$, its scalar curvature also written $\mathcal{R}$ in the store's sign (as in Fact \claimref{synthesis.imported-gtg-dictionary}), coupled to matter with a symmetric stress map $T$ of trace $\tau$ ($\tau = \rho$ for dust), conserved by the matter's own equations. \emph{Nordstr\"om's theory in the form of Einstein and Fokker} is the pair of field equations
\[
\mathcal{W} = 0, \qquad \mathcal{R} = -24\pi G\,\tau,
\]
that is, in the signature $(-,+,+,+)$ and round-sphere-positive curvature of the sources, $C_{abcd} = 0$ and $R = 24\pi G\,T$ with $T = -\rho$ for dust: the derived metric is conformally flat and its scalar curvature is sourced by the trace of the stress alone. Its observational consequences: (a) light (any massless particle) moves on null geodesics, which are invariant under conformal rescaling, so it is not deflected (post-Newtonian parameter $\gamma = -1$, where Einstein's equations give $\gamma = 1$); (b) the perihelion advance of a planetary orbit is $-\tfrac16$ of the value Einstein's equations give ($\beta = \tfrac12$). Since light deflection and the perihelion advance agree with Einstein's values, the theory is excluded by observation. \emph{Provenance:} \cite{EinsteinFokker1914}, the scalar theory \cite{Nordstrom1913}; the field equations and both failures in modern form \cite[Sec.~II.3, Eq.~(3.7)]{DeruelleSasaki2011}; \cite[Exercise~7.1]{MTW1973}.

## technical
Nordstr\"om's 1913 theory was the most developed relativistic theory of gravity before general relativity: gravity is one scalar field sourced by the trace of the matter's stress-energy. Einstein and Fokker showed in 1914 that it is a geometric theory: the spacetime metric is conformally flat (the Weyl curvature vanishes) and its scalar curvature is proportional to the stress trace, with matter moving on geodesics. In the store's language the field equations are $\mathcal{W} = 0$ and $\mathcal{R} = -24\pi G\tau$. The theory is consistent and has the Newtonian limit, but it fails two classical tests: because null geodesics do not change under a conformal rescaling of the metric, it predicts no bending of light, and it predicts a perihelion advance of minus one sixth of general relativity's, a retrograde shift. Both are contradicted by observation.

## lay
Before Einstein completed general relativity, Nordstr\"om proposed a simpler theory in which gravity is a single number at each point, produced by the total energy content of matter. Einstein and Fokker showed it can be written as geometry. It reproduces Newton's law, but it predicts that light is not bent by the Sun and that Mercury's orbit turns slightly backwards rather than forwards, both of which observation rules out. These are taken from the literature.

## one-liner
Nordstr\"om's theory in the Einstein-Fokker form, $\mathcal{W} = 0$ and $\mathcal{R} = -24\pi G\tau$ in the store's sign ($R = 24\pi G T$ in the sources'), deflects no light ($\gamma = -1$) and gives $-\tfrac16$ of Einstein's perihelion advance, so it is excluded by observation (Einstein and Fokker 1914; Deruelle and Sasaki 2011).
