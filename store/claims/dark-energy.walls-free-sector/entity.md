---
id: dark-energy.walls-free-sector
kind: claim
version: 6
title: The wall's free sector
status: proved
region: dark-energy
subject: walls
tags: [degenerate-algebras, curvature-and-field-equations]
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
  role: 'GA rewrite (derived metric; components declared)'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG pass: component proof kept, outside_ga narrowed (the point lies outside the invertible region)'
  version: 6
  source: maintainer pass 2026-11-07 (consistency, GTG proofs)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@3
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:thm:wallfree
- kind: check
  ref: check.py::check_torsion_and_frame_ranks
- kind: check
  ref: check.py::check_connection_rank_and_symbols
- kind: check
  ref: check.py::check_free_sector_is_k_plus_m
- kind: check
  ref: check.py::check_hamiltonian_constraint
locators:
  paper: T10
  number: Thm 4.1
  label: thm:wallfree
  line: 772
extraction:
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'GTG proof not written; the component proof and checks are kept and the outside_ga reason narrowed. The result counts ranks and principal-symbol ranks of the Einstein-Cartan equations, as linear conditions on the components of torsion, curvature and the rotation-gauge field, in the normal form e^a = dx^a (a < 3), e^3 = 0 at a point where hb^{-1} has corank one. There hb does not exist, so the GTG definition, which holds on the invertible region and identifies the physical frame and omega(A) = Omega(hb(A)) through hb, does not apply; the equations themselves are polynomial in hb^{-1} and Omega and could be written as GA expressions, but the counts would still be ranks of these linear maps on components, and stating them as a GTG result needs an extension of the definition to degenerate soldering that the store does not have and that cannot be checked here exactly as a piece of GTG. No change of statement, proof or checks.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The derived metric is written g(a,b) = hb^{-1}(a).hb^{-1}(b) with g_{mu nu} = eta_{ab} e^a_mu e^b_nu as a labelled component reading; the rest stays in components and is declared outside_ga (other): the result counts the ranks of the Einstein-Cartan equations as linear conditions on the components of torsion, curvature and the connection one-forms in a normal form at a point where hb^{-1} is degenerate, outside the invertible region of the GTG definition. Reader fix (R09): the proof says that omega is the rotation-gauge field as Cartan one-forms, whose values on vectors are the negative of the definition''s Omega (C10), and that the ranks and the quadratic identity (d) do not depend on that sign.'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the torsion, frame and connection ranks and symbol ranks at the three normal forms, the K + M free sector, and the Hamiltonian component with its Lambda terms. Version 3 -> 4.'
  env: theorem
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west
  - dark-energy.sheaf-papers-wall-soldering-variables
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added:
    - dark-energy.imported-macdowell-mansouri-theorem-stelle-west
    - dark-energy.frozen-point-makes-stelle-west-vector
    note: 'Added the imported MacDowell-Mansouri fact, since the theorem is stated for the equations as
      imported there, and the action theorem, whose polynomiality clause the hypotheses invoke to keep
      the equations meaningful at the point (a judgement call: that clause is light); the soldering-variables
      proposition is a forward comparison and itself uses this theorem, so it was not added. Levels pass:
      the lay and one-liner now restrict the symmetric free sector to the Lorentzian normal form, and
      the lay says that on a curved wall only the non-propagation is proved.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-energy.frozen-point-makes-stelle-west-vector
    - dark-energy.imported-macdowell-mansouri-theorem-stelle-west
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the soldering form is the physical-vector map hb^{-1} of the gravitational field, here the regular variable, and a corank-one soldering form is a locus where hb^{-1} drops rank (hb fails); g_{mu nu} is the derived metric; the connection omega is the rotation-gauge field Omega in components in the orthonormal physical frame. Ranks, free sector, constraint and cases unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
outside_ga:
  kind: other
  why: 'The result counts ranks and symbol ranks of the Einstein-Cartan equations, as linear conditions on the components of torsion, curvature and the rotation-gauge field omega^{ab}_mu, in the normal form e^a = dx^a, e^3 = 0 at a point where hb^{-1} has corank one. There hb does not exist, so the GTG definition, which holds on the invertible region and reads omega(A) = Omega(hb(A)) and the physical frame through hb, does not apply; a GTG treatment would need an extension of the definition to degenerate soldering that the store does not have. The components in the normal form and the symbol epsilon_{abcd} are what is counted.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose physical-vector map $\hb^{-1}$, here taken as the regular variable and written in an orthonormal frame $\{\gamma_a\}$ as the soldering form $e^a(v) = \gamma^a \cdot \hb^{-1}(v)$, is of corank one at a point, so that $\hb$ fails there: $e$ is a regular map $TM \to \mathbb{R}^{1,3}$ from background to physical vectors with a one-dimensional radical $r$ ($e^a(r) = 0$ for every $a$) and cokernel direction $n$ ($n_a e^a = 0$), so that the derived metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$ (in components $g_{\mu\nu} = \eta_{ab}e^a_\mu e^b_\nu$) is finite and degenerate (this is the degeneration dual to the sheaf paper's; see Proposition \claimref{dark-energy.sheaf-papers-wall-soldering-variables}); the image $e(T_xM)$ is a three-dimensional subspace of the frame space, the wall's tangent space, and it may be of any type (Lorentzian, Riemannian, or null). The Einstein-Cartan equations \eqref{eq:ec} are polynomial in $e$, in the rotation-gauge field written as connection one-forms $\omega$, and in their derivatives, so polynomiality (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(1)) keeps them meaningful at the point. Choose the normal form $e^a = dx^a$ for $a = 0,1,2$, $e^3 = 0$, so that $r = \partial_3$, $n = \delta^3$, and the wall's tangent space carries the frame indices $0,1,2$; write $K^{a}{}_{b} := \omega^{a}{}_{3\,b}$ and $M_{c\mu} := \tfrac12\,\epsilon_{cab}\,\omega^{ab}{}_{\mu}$ for $a, b, c, \mu \in \{0,1,2\}$, the boost components into the dying frame direction and the dualised tangential connection, and lower and raise their indices with the wall metric $\eta_{ab}$. Then:
\begin{enumerate}
\item[(a)] \emph{(Torsion.)} Regarded as linear conditions on the $24$ components of the torsion, the connection equation has rank $24$ on the invertible region and rank $18$ at the point: three of its components are identities $0 = 0$ and six torsion components are freed, all tangential to the wall (every component with a leg along $r$, and the cokernel component $n_dT^d$, are forced to vanish). Regarded as conditions on the $36$ components of the curvature, the frame equation has rank $16$ in both cases: no curvature condition is lost, and the components of the frame equation along the radical do \emph{not} vanish identically.
\item[(b)] \emph{(Connection.)} Regarded as conditions on the $24$ components of $\omega$, the connection equation has rank $12$ at the point. The free sector is exactly two symmetric tensors on the wall's tangent space: $K_{ab}$ symmetric (six components), which is invisible to the torsion because it multiplies $e^3 = 0$, and $M_{c\mu}$ symmetric (six components), which is the connection image of the freed torsion of (a), $t = (\operatorname{tr}M)\,\mathbf{1} - M$. Forced to their Levi-Civita values are the antisymmetric parts of $K$ and $M$ and every component $\omega^{ab}{}_{3}$ along the radical leg.
\item[(c)] \emph{(Propagation.)} The frame equation contains no derivative of the symmetric part of $M$ in any direction. Its principal symbol in the radical direction determines the radial derivatives $\partial_3 K_{ab}$ of all six components of $K$, and its tangential symbols impose first-order conditions on $K$ along the wall. The field equations therefore cannot propagate $M$ across the wall.
\item[(d)] \emph{(The wall's Hamiltonian constraint.)} In the normal form with $de = 0$, on the free sector $K \oplus M$ the frame equation reduces to a single component, $E_3$ evaluated on $(\partial_0, \partial_1, \partial_2)$, which reads
\[
\sigma_2'(M) \;-\; \sigma_2'(K) \;-\; 2\Lambda \;=\; 0, \qquad \sigma_2'(A) := (\operatorname{tr}A)^2 - \operatorname{tr}(A^2),
\]
with traces taken on the mixed tensors $M^{c}{}_{\mu}$, $K^{a}{}_{b}$: $K$ and $M$ enter only there, only quadratically, and with no cross term; the other fifteen components of the frame equation vanish identically on the free sector. On a curved wall the Levi-Civita part of $\omega$ adds the wall's intrinsic curvature to this component and algebraic cross terms with $M$ and $K$ to the others.
\end{enumerate}
Consequently, on the flat model of (d), the field equations at a corank-one wall of the soldering form determine the connection up to a symmetric bilinear form $M$ on the wall's tangent space which they constrain by one scalar relation and never propagate: data on the wall that the bulk equations do not determine. On a wall with intrinsic curvature the statement that survives is (c): $M$ is never propagated; how much of $M$ the fifteen other components then fix algebraically, through their cross terms with the Levi-Civita part and with the first derivatives of the connection, is a jet computation not done here (successor problem (2)). \emph{Level:} proved, for the equations as imported in Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west}; the ranks and symbol ranks are invariant under the changes of frame and coordinates that preserve the normal form. The script confirms in exact arithmetic the counts of (a) to (c) and the single surviving component of (d) for all three types of dying direction, and the $K \oplus M$ description of (b) with the identity of (d) for the Lorentzian and Riemannian types, whose wall metric is nondegenerate; at the Riemannian type, where the boost is into a timelike direction, the cosmological term enters (d) with the opposite sign, $\sigma_2'(K) - \sigma_2'(M) - 2\Lambda = 0$. At the null type the dying direction lies in the wall, the wall metric is degenerate, and the twelve-dimensional free sector does not split as $K \oplus M$; (b) and (d) are stated for the Lorentzian normal form only. Which walls are of this type, and in particular that the sheaf paper's wall is not, is Proposition \claimref{dark-energy.sheaf-papers-wall-soldering-variables}.

## technical
Take a gravitational field on flat spacetime whose soldering form $e$, the physical-vector map $\hb^{-1}$ in components, has corank one at a point, with radical $r$ and cokernel direction $n$, so that $\hb$ fails there and the derived metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$ is finite and degenerate; the Einstein-Cartan equations are polynomial in $e$ and in the rotation-gauge field $\omega$ and so still make sense there. In the normal form $e^a = dx^a$ ($a = 0,1,2$), $e^3 = 0$, the connection equation, as conditions on the torsion, drops from rank $24$ to rank $18$, freeing six tangential torsion components, while the frame equation keeps rank $16$ on the curvature. As conditions on the connection itself it has rank $12$, and the free sector is exactly two symmetric tensors on the wall's tangent space: $K_{ab}$, the boost components into the dying direction, and $M_{c\mu}$, the dualised tangential connection.

The frame equation contains no derivative of the symmetric part of $M$, so the field equations cannot propagate $M$ across the wall. On the flat model with $de = 0$ the only surviving component is $\sigma_2'(M) - \sigma_2'(K) - 2\Lambda = 0$, with $\sigma_2'(A) = (\operatorname{tr}A)^2 - \operatorname{tr}(A^2)$. So on the flat model the connection is fixed up to a symmetric form $M$ constrained by one scalar relation and never propagated; on a curved wall only the non-propagation is proved. The counts hold for all three types of dying direction, and the split $K \oplus M$ with its constraint is stated for the Lorentzian normal form.

## lay
Suppose the gauge field that relates physical directions to directions in the flat background loses one direction at a wall of the ordinary (Lorentzian) type. Einstein-Cartan gravity then no longer fixes all of the connection there: a symmetric piece of data living on the wall is left free, and the equations never carry it across the wall. On a curved wall only this last point is proved. On the simplest flat model they constrain it by a single relation, so the wall holds information that the bulk equations do not determine.

## one-liner
At a corank-one wall of the soldering form with Lorentzian tangent space the Einstein-Cartan equations leave free a symmetric form $M$ on the wall's tangent space, which they never propagate and, on the flat model, constrain only by $\sigma_2'(M) - \sigma_2'(K) - 2\Lambda = 0$.
