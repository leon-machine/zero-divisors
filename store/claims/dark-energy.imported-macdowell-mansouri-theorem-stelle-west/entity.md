---
id: dark-energy.imported-macdowell-mansouri-theorem-stelle-west
kind: claim
version: 4
title: 'Imported: the MacDowell-Mansouri theorem, Stelle-West form'
status: imported
region: dark-energy
subject: dark-energy
tags: [classical-theorem, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
- name: Claude Opus 5.5
  role: consistency pass, the sign of l^2 named on the anti-de Sitter branch
  version: 4
  source: maintainer pass 2026-11-07 (consistency, small items)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: S. W. MacDowell and F. Mansouri, Unified geometric theory of gravity and supergravity, Phys.
    Rev. Lett. 38 (1977), 739--742.
  key: MacDowellMansouri1977
- citation: K. S. Stelle and P. C. West, Spontaneously broken de Sitter symmetry and the gravitational
    holonomy group, Phys. Rev. D 21 (1980), 1466--1488.
  key: StelleWest1980
- citation: D. K. Wise, MacDowell-Mansouri gravity and Cartan geometry, Class. Quantum Grav. 27 (2010),
    155010.
  key: Wise2010
locators:
  paper: T10
  number: Fact 2.2
  label: fact:mm
  line: 633
extraction:
  maintainer_pass_small_items:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'l^2 = 3/Lambda is taken with its sign: on the anti-de Sitter branch l^2 < 0 and Q(V) = -l^2 > 0, so A = Omega - hb^-1 ^ V/l^2 = Omega + hb^-1 ^ V/Q(V) holds on both branches (checked against synthesis.macdowell-mansouri-principle v4, which writes (Lambda/3)). Store reading, not the source''''s sentence. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'Imported literature result with no derivation; the lemma that fixes its sign convention is a convention source, not a premise, so no edge was added.'
  env: fact
  context_refs:
  - dark-energy.stelle-west-vector-frozen-point
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (DICTIONARY 13): the fibre is Cl(1,4) = Cl(1,3) plus V; the connection in the V-constant gauge is A(a) = Omega(a) + hb^{-1}(a) ^ V/l^2; Lorentz block F(B) = R(B) - l^{-2} B in the store sign, vanishing on de Sitter; the functional in GA as l^2 int det(hb)^{-1} (-2)<F(a^b) I F(I d_b ^ d_a)>; Euler-Lagrange equations as vanishing torsion and G(a) + Lambda a = 0. The forms of the sources kept as their reading; provenance unchanged, with a sentence that the flat-space reading is the store''s transcription. Sign of the soldering term corrected to minus (so that D_a V = +hb^{-1}(a), the soldering form) and the Lorentz block written -(R(B) - B/l^2), checked exactly in the store''s tractor transcription, clause (v). Fix (referee GR2, 2026-10-23): "up to the sign convention" dropped (D_a V = hb^{-1}(a) exactly); the 2-form F^{ab} = R^{ab} + l^{-2} e^a ^ e^b is stated to equal the operator -(R(B) - l^{-2} B) (DICTIONARY C11).'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), and adjoin to the vectors of $\Cl(1,3)$ one vector $V$ orthogonal to them, of fixed squared norm $Q(V) = -\ell^2$, with $\ell$ the de Sitter radius, $\ell^2 = 3/\Lambda$ (taken with its sign: on the anti-de Sitter branch below $\ell^{2} < 0$, so $Q(V) = -\ell^{2} > 0$ and every display holds unchanged): the vectors of $\Cl(1,4)$ are the fibre of the de Sitter group $SO(1,4)$, of signature $(1,4)$, and the stabiliser of $V$ is the Lorentz group of $V^\perp$, the vectors of $\Cl(1,3)$. Let $A$ be a connection for $SO(1,4)$, a gauge field $A(a)$ with values in the bivectors of $\Cl(1,4)$ (over flat spacetime the rank-five bundle is trivial), and $F$ its field strength. In the gauge where $V$ is constant the connection splits as
\[
A(a) \;=\; \Omega(a) - \hb^{-1}(a)\wedge V/\ell^{2}
\]
(normalisation as stored), with $\Omega$ the Lorentz connection on $V^\perp$ and the soldering form the physical frame $\hb^{-1}$, which is the covariant derivative of $V$, $D_a V = \hb^{-1}(a)$; the field strength splits into a Lorentz block, which on physical bivectors is $\mathcal{F}(B) = -(\mathcal{R}(B) - \ell^{-2}B)$ in the store's sign of the curvature operator and vanishes exactly on de Sitter space, and a translational block (the bivectors containing $V$) proportional to the torsion. In the forms of the sources, $A = \omega + e$, the Lorentz block is $F^{ab} = R^{ab} + \ell^{-2}\,e^a\wedge e^b$, which is exactly the operator $\mathcal{F}(B) = -(\mathcal{R}(B) - \ell^{-2}B)$ (the Riemann endomorphism being $R(u,v) = -\mathcal{R}(u \wedge v)$ as a bivector, and $(e^a \wedge e^b)(u,v)$ acting as $(u \wedge v) \cdot w$), and the torsion is $T^a = D e^a$. The functional
\[
\begin{aligned}
S_{\mathrm{MM}}[A, V] \;&\sim\; \ell^{2}\int \epsilon_{abcd}\,F^{ab}\wedge F^{cd}\\
&=\; \ell^{2}\!\int \epsilon_{abcd}R^{ab}\wedge R^{cd} \;+\; 2\!\int \epsilon_{abcd}\, e^a\wedge e^b\wedge R^{cd} \;+\; \ell^{-2}\!\int \epsilon_{abcd}\, e^a\wedge e^b\wedge e^c\wedge e^d ,
\end{aligned}
\]
where $\epsilon_{abcd}$ is the fibre volume form of the rank-five bundle contracted with the unit vector $V/\ell$, decomposes as displayed into the Gauss-Bonnet term, the Einstein-Cartan term and the cosmological term; in geometric algebra it is $\ell^{2}\int \det(\hb)^{-1}\,(-2)\,\langle\mathcal{F}(a \wedge b)\,I\,\mathcal{F}(I\partial_b \wedge \partial_a)\rangle\,d^{4}x$ up to the stored normalisation, over the background region. Its Euler-Lagrange equations, from varying $\omega$ and $e$, are the Einstein-Cartan equations
\begin{equation}
\epsilon_{abcd}\, e^{c}\wedge T^{d} \;=\; 0, \qquad \epsilon_{abcd}\, e^{b}\wedge\bigl(R^{cd} + \ell^{-2} e^{c}\wedge e^{d}\bigr) \;=\; 0 ,
\end{equation}
which on the invertible region are equivalent to vanishing torsion, $D \wedge \hb^{T}(a) = \hb^{T}(\nabla \wedge a)$, together with the Einstein equations with cosmological constant $\Lambda$, $\mathcal{G}(a) + \Lambda a = 0$. The anti-de Sitter branch, $\Lambda < 0$, reads identically with the group $SO(2,3)$ on a fibre of signature $(2,3)$ (the vectors of $\Cl(1,3)$ with an adjoined $V$ of positive square), $Q(V) = -3/\Lambda > 0$, and the Lorentz group as the stabiliser of $V$; the identity $Q(I)\,Q(V) = -1$ is what the reduction uses, and it is sign-independent. \emph{Provenance:} \cite{MacDowellMansouri1977, StelleWest1980}; the Cartan-geometric form and the contraction $\ell \to \infty$ are \cite{Wise2010}; the variational identity is used at assembly level, and is declared as such here. The sign of the $\ell^{-2}e\wedge e$ term in these conventions is fixed by Lemma \claimref{dark-energy.stelle-west-vector-frozen-point}(iv). The reading on flat spacetime, with the soldering form as the physical frame, is the store's transcription of the cited theorem into Gauge Theory Gravity.

## technical
In Gauge Theory Gravity, adjoin to the vectors of $\Cl(1,3)$ one vector $V$ with $Q(V) = -\ell^2$, $\ell^2 = 3/\Lambda$ (negative on the anti-de Sitter branch), giving the vectors of $\Cl(1,4)$, the fibre of the de Sitter group. A de Sitter connection is then a gauge field $A(a)$ on flat spacetime valued in the bivectors of $\Cl(1,4)$; in the gauge where $V$ is constant it is $A(a) = \Omega(a) - \hb^{-1}(a)\wedge V/\ell^2$, the rotation-gauge field plus a soldering term built from the physical frame. Its field strength has a Lorentz block $\mathcal{F}(B) = -(\mathcal{R}(B) - \ell^{-2}B)$ (in forms exactly $F^{ab} = R^{ab} + \ell^{-2}e^a\wedge e^b$), which vanishes exactly on de Sitter space, and a translational block proportional to the torsion. The functional $S_{\mathrm{MM}} \sim \ell^2\int\epsilon_{abcd}F^{ab}\wedge F^{cd}$ decomposes into the Gauss-Bonnet, Einstein-Cartan and cosmological terms.

Its Euler-Lagrange equations are the Einstein-Cartan equations, equivalent on the invertible region to vanishing torsion together with the field equations $\mathcal{G}(a) + \Lambda a = 0$. The anti-de Sitter branch reads identically with $SO(2,3)$, and the reduction uses the sign-independent identity $Q(I)\,Q(V) = -1$. The variational identity is used at assembly level.

## lay
MacDowell and Mansouri, and later Stelle and West, showed that gravity with a cosmological constant can be written as a theory of a larger symmetry group, the de Sitter group, broken by a vector of fixed length. On flat spacetime this means adding one extra direction to the algebra in which the gravitational fields take their values. The action is then the square of a field strength, and it splits into a topological piece, the usual Einstein term and the cosmological term. Its equations are the Einstein equations with that cosmological constant.

## one-liner
The MacDowell-Mansouri functional of a de Sitter gauge field $A(a) = \Omega(a) - \hb^{-1}(a)\wedge V/\ell^2$ on flat spacetime, with a Stelle-West vector of fixed norm, splits into Gauss-Bonnet, Einstein-Cartan and cosmological terms, and its field equations are the Einstein-Cartan equations with cosmological constant $\Lambda$.
