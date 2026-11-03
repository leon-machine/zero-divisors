---
id: note.interior.setting-setting-conventions
kind: note
version: 1
title: Setting and conventions
status: setting
subject: einstein
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
comments_on:
- interior.imported-equivalence-einstein-equations
locators:
  paper: T06
  number: Setting
  section: Setting and conventions
  line: 351
---

## formal
Spacetime algebra $\Cl(1,3)$ with orthonormal generators $\gamma_0, \gamma_1, \gamma_2, \gamma_3$, $\gamma_0^2 = +1$, $\gamma_i^2 = -1$; in the $(t,r)$ plane write $\et := \gamma_0$, $\er := \gamma_1$. The pseudoscalar is $I := \gamma_0\gamma_1\gamma_2\gamma_3$, with $I^2 = -1$; $I$ commutes with every even element and anticommutes with every vector. Units $G = c = 1$; metric signature $(+,-,-,-)$. Curvature conventions are those fixed by the Cartan structure equations exactly as in T5's appendix \cite[App.~A]{ButlerT5}; in these conventions the de Sitter metric has $\Ric_{ab} = \Lambda\, g_{ab}$ and scalar curvature $R = 4\Lambda$.

In gauge theory gravity, gravity is a pair of gauge fields on the flat background: the position-dependent linear map $\hb(a)$ on vectors, gauging local frame rescalings, and the connection bivector $\Omega(a)$, gauging local Lorentz rotations. The covariant derivative and field strength are
\[
D_a M = a \cdot \nabla M + \Omega(a) \times M, \qquad
R(a \wedge b) = a\cdot\nabla\,\Omega(b) - b\cdot\nabla\,\Omega(a) + \Omega(a) \times \Omega(b),
\]
with $A \times B := \tfrac12(AB - BA)$, and the field equations are $R(a) - \tfrac12 a R = \kappa\, T(a)$ together with the vanishing of torsion, which determines $\Omega$ algebraically from $\hb$; the metric is $g(a,b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$ \cite{LDG1998}. Every operation in these displays is interior to $\Cl(1,3)$: nothing invokes a curved manifold beyond the flat background. The theory is a field theory of an invertibility-demanding map, which is exactly the condition the transport principle addresses.

## technical
pending

## lay
pending

## one-liner
pending
