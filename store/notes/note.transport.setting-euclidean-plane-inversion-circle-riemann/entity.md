---
id: note.transport.setting-euclidean-plane-inversion-circle-riemann
kind: note
version: 2
title: 'The Euclidean plane: inversion in a circle on the Riemann sphere'
status: setting
subject: completion
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
comments_on:
- transport.swap-rescale-normal-form
- transport.totality
- transport.minimality
- transport.no-go-level-elements
locators:
  paper: T01
  number: Setting
  section: 'Type N: the isotropic obstruction, and Rule 1'
  line: 1071
  subsection: 'The Euclidean plane: inversion in a circle on the Riemann sphere'
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The identification z = x + iy of the Euclidean plane with the complex plane is written z = e_1(x e_1 + y e_2) = x + I_2 y with I_2 = e_1 e_2 the plane''s unit bivector (a phase in a real two-plane, U1); the rest of the note is unchanged. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F (found by the language check''s bare-unit detector): nothing replaced; the i stays and is declared outside_ga (bridge): the note identifies the Euclidean plane with the complex plane by z = x + iy to set the inversion beside the classical Riemann-sphere picture; the i is the unit of that classical side.'
---

## formal
Take the base $\mathbb{V} = \R^2$ with $Q$ positive definite (signature $(2,0)$), and identify $\mathbb{V}$ with $\C = \mathrm{span}\{1, I_{2}\}$, $I_{2} = e_{1}e_{2}$ the unit bivector of the plane ($I_{2}^{2} = -1$), by $z = e_{1}(xe_{1} + ye_{2}) = x + I_{2}y$, so that $Q(z) = |z|^2$. Definite signature has no null vectors, so the partial locus of $\rho(z) = z/Q(z)$ is the origin alone: this is the oldest division by zero there is. Note which hypotheses are at work. The no-go theorem requires $p, q \geq 1$ and $n \geq 3$ and does not apply here, since with no null vectors there is no element-level question to obstruct, while the theorems this example exercises (totality, minimality, the normal form) hold in every nondegenerate signature, as recorded in the scope paragraph of Section \ref{subsec:quadratic}.

The completion is $\Cl(3,1)$. Because $Q$ is definite, the incidence condition \eqref{eq:incidence} with $s = 0$ forces $z = 0$: the ideal strata (i) and (ii) of Proposition \claimref{transport.swap-rescale-normal-form} are empty, and the only ideal point is $[\nInf]$, stratum (iii). The quadric $\mathcal{Q}$ is therefore the plane with a single point adjoined, and the map
\[
[X(z)] \;\mapsto\; \frac{1}{|z|^2+1}\bigl(\,2x,\; 2y,\; |z|^2 - 1\,\bigr), \qquad [\nInf] \;\mapsto\; (0,0,1)
\]
identifies $\mathcal{Q}$ with the unit sphere $S^2 \subset \R^3$ by inverse stereographic projection from the north pole. This is the Riemann sphere, with $[X(0)]$ the south pole and $[\nInf]$ the point at infinity.

Under this identification, Theorem \claimref{transport.totality} computes
\[
\iota[X(z)] = [X(z/|z|^2)] \ \ (z \neq 0), \qquad \iota[X(0)] = [\nInf], \qquad \iota[\nInf] = [X(0)],
\]
and $z \mapsto z/|z|^2 = 1/\bar{z}$ is inversion in the unit circle. On the sphere it is the reflection
\[
(X, Y, Z) \;\mapsto\; (X, Y, -Z)
\]
in the equatorial plane: the modulus inverts and the argument is unchanged, so the equator $|z| = 1$ is fixed pointwise and the two poles, $0$ and $\infty$, are exchanged. Both statements are Proposition \claimref{transport.swap-rescale-normal-form} read in these coordinates, the second being the fixed locus $\{Q = 1\} \cup \text{(ii)}$ of Remark \claimref{note.transport.where-each-stratum-comes} with the stratum (ii) that definite signature leaves empty. Inversion in a circle is anti-holomorphic; the holomorphic $z \mapsto 1/z$ of complex analysis is its composite with the reflection $y \mapsto -y$, which is a reflection of the base and so a versor of the model. Either way the content tested is the same, and it is the classical one: a reciprocal undefined at a single point of the plane becomes a total involution of a compact surface two dimensions up, with $1/0 = \infty$ and $1/\infty = 0$. Theorem \claimref{transport.totality} reproduces the nineteenth-century resolution of $1/0$ by conformal compactification, as it must, and Theorem \claimref{transport.minimality} adds that the two dimensions it uses are the fewest that will serve.

The same computation over the one-dimensional base $\mathbb{V} = \R$, $Q(x) = x^2$, has completion $\Cl(2,1)$, identifies $\mathcal{Q}$ with the real projective line $\R P^1$ in its classical homogeneous coordinates $[\,x : s\,]$, and returns for $\iota$ the classical inversion matrix $\begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$, with $[\,0:1\,]$ and $[\,1:0\,]$ exchanged.

What no definite signature exhibits, in either dimension, is the null cone. The genuinely new content of Theorems \claimref{transport.no-go-level-elements} and \claimref{transport.totality}(3) lies on the ideal strata (i) and (ii), which are empty here and carry, in mixed signature, one class per null vector and one per null direction respectively. There the compactification adjoins a stratum rather than a point, and the element-level question is both posed and closed.

## technical
pending

## lay
pending

## one-liner
pending
