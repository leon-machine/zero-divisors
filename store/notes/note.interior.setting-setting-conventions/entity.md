---
id: note.interior.setting-setting-conventions
kind: note
version: 2
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
- name: Claude Opus 5.5
  role: 'GA rewrite (de Sitter curvature)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- interior.imported-equivalence-einstein-equations
locators:
  paper: T06
  number: Setting
  section: Setting and conventions
  line: 351
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The de Sitter normalisation Ric_{ab} = Lambda g_{ab}, R = 4 Lambda is stated for the curvature operator of the GTG definition, R(a) = Lambda a and scalar 4 Lambda in the store''s sign (dictionary C6), with the component form as a labelled reading; the rest of the note was already in GTG; notation only. Reader fix (R03): the field equation is written in the store''s sign, R(a) - a R/2 = -kappa T(a) for R(B) = -R(hb(B)), with the LDG-sign form as a labelled reading.'
---

## formal
Spacetime algebra $\Cl(1,3)$ with orthonormal generators $\gamma_0, \gamma_1, \gamma_2, \gamma_3$, $\gamma_0^2 = +1$, $\gamma_i^2 = -1$; in the $(t,r)$ plane write $\et := \gamma_0$, $\er := \gamma_1$. The pseudoscalar is $I := \gamma_0\gamma_1\gamma_2\gamma_3$, with $I^2 = -1$; $I$ commutes with every even element and anticommutes with every vector. Units $G = c = 1$; metric signature $(+,-,-,-)$. Curvature conventions are those fixed by the Cartan structure equations exactly as in T5's appendix \cite[App.~A]{ButlerT5}; in these conventions de Sitter space has $\mathcal{R}(a) = \Lambda a$ on physical vectors and scalar curvature $\mathcal{R} = 4\Lambda$ (in components $\Ric_{ab} = \Lambda\, g_{ab}$, $R = 4\Lambda$), where $\mathcal{R}(B) = -R(\hb(B))$ is the curvature operator of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields} in the store's sign.

In gauge theory gravity, gravity is a pair of gauge fields on the flat background: the position-dependent linear map $\hb(a)$ on vectors, gauging local frame rescalings, and the connection bivector $\Omega(a)$, gauging local Lorentz rotations. The covariant derivative and field strength are
\[
D_a M = a \cdot \nabla M + \Omega(a) \times M, \qquad
R(a \wedge b) = a\cdot\nabla\,\Omega(b) - b\cdot\nabla\,\Omega(a) + \Omega(a) \times \Omega(b),
\]
with $A \times B := \tfrac12(AB - BA)$, and the field equations are, in the store's curvature sign, $\mathcal{R}(a) - \tfrac12 a\,\mathcal{R} = -\kappa\, T(a)$ for $\mathcal{R}(B) = -R(\hb(B))$ (in the sign of \cite{LDG1998}, $R(a) - \tfrac12 a R = \kappa\, T(a)$), together with the vanishing of torsion, which determines $\Omega$ algebraically from $\hb$; the metric is $g(a,b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$ \cite{LDG1998}. Every operation in these displays is interior to $\Cl(1,3)$: nothing invokes a curved manifold beyond the flat background. The theory is a field theory of an invertibility-demanding map, which is exactly the condition the transport principle addresses.

## technical
pending

## lay
pending

## one-liner
pending
