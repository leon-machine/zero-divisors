---
id: synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen
kind: claim
version: 1
title: 'Order-four structure on real projective walls; the signed count is defined modulo 16'
status: proved
region: synthesis
subject: walls
tags: [pseudoscalar-and-centre, spinor-modules, hypercharge-and-anomalies, obstruction-types]
proposed_by:
  kind: ai
  session: 2026-11-16-anomaly
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-16-anomaly
review: draft
derivations:
- name: main
  uses:
  - synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element@1
  - synthesis.wall-rung-count-is-height-of-dying-line-class@2
  - synthesis.imported-whitney-product-formula-and-projective-space@1
  - synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure@1
  - synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pseudoscalar_lifts_of_the_antipodal_map_square_to_a_sign_set_by_the_signature
- kind: check
  ref: check.py::check_classes_of_real_projective_and_lens_walls
- kind: check
  ref: check.py::check_signed_count_of_the_order_four_element_is_defined_modulo_sixteen
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.slot-module-hypothesis
  - synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial
  - synthesis.slot-module-light-ray-arrays-are-weyl-components
extraction:
  open_problem: op.order-four-anomaly-and-sixteen
  note: >-
    Filed against the third attack item (what a wall with cross-section real projective five-space requires
    of the content) and the link to the wall theory asked for by the problem. The outcome is mixed. Positive:
    the stored wall theory does carry the order-four structure, on exactly one side of a real projective wall
    with tautological dying line, and the lift of the dying line's monodromy across the stored Clifford jump is
    the pseudoscalar of the jump plane, an order-four element of square -1; the signed count of the
    pseudoscalar of the ten Majoranas is well defined modulo 16 on its class modulo the Standard Model group.
    Negative: nothing stored identifies the wall's order-four element with the pseudoscalar of the ten
    Majoranas, the count lives on a five-dimensional cross-section (a six-dimensional wall theory, not the
    four-dimensional tower), and a count is a condition on the content only for a gauged element. The
    mathematics is classical (the structure is the Spin-Z_4 structure of the literature; the classes are
    textbook) and transport-absent; what is new for the store is its form in the wall theory. The spectral
    asymmetry 1/16 per component is derived, in geometric algebra, in the proposal
    synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials, which is not yet a
    stored result and is entered here as a hypothesis. Literature, not stored as Facts: Garcia-Etxebarria and
    Montero, Dai-Freed anomalies in particle physics, arXiv:1808.00009 (J. High Energy Phys. 2019), checked
    at source: section 4.3, the generator of the bordism group of five-manifolds with this structure is real
    projective five-space, with eta invariant 1/16; appendix C.4, equation (C.21), the group is Z_16 and the
    group in dimension three is 0; section 2.1, an anomaly in a global symmetry is not an inconsistency, it
    means that the symmetry cannot be gauged; the order-four element there is the one inside
    X = -2Y + 5(B - L) in that paper's normalisation of hypercharge, the mass term of the right-handed
    neutrino breaks it, and when it sits in a U(1) the condition follows from the local conditions. Cited
    from memory: Dai and Freed 1994 and Witten 2016 (Rev. Mod. Phys. 88, 035001) for the phase of the
    partition function as the exponentiated eta invariant; Hsieh, arXiv:1808.02881, and Tachikawa and
    Yonekura 2019 for the same count; Karoubi 1968 for spin structures on bundles with indefinite forms;
    Milnor and Stasheff for the classes of plane bundles. Leon's decision of 9 November 2026 stands: the
    modulo-16 statement is not imported here; clause (vi) is conditional on it and says so.
---

## formal
Let $\Sig = \mathbb{RP}^{n}$, $n = 2m - 1$, be the cross-section of a tame corank-one wall with tautological dying line $\shL$, $x = w_{1}(\shL)$, as in Theorem \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}(3) (a wall on $\Sig \times \R$). By Fact \claimref{synthesis.imported-whitney-product-formula-and-projective-space}(iii), $T^{*}M|_{\Sig} \cong T\Sig \oplus \underline{\R} \cong 2m\,\shL$, the flat bundle $S^{n} \times_{\pm 1} \R^{2m}$ whose monodromy is the antipodal map $-1$. A \emph{side} is a nondegenerate form on this bundle with maximal positive and negative subbundles $E_{+}$, $E_{-}$ of ranks $p$, $q$; it is \emph{flat} if the form is a constant form of signature $(p,q)$ on $\R^{2m}$, so that $E_{+} \cong p\,\shL$, $E_{-} \cong q\,\shL$ and the Clifford bundle of the side is $S^{n} \times_{\pm 1} \Cl(p,q)$ with $-1$ acting by the grade involution; a definite side is flat. For a line bundle $\ell$ over a manifold $X$ call a spin structure on $TX \oplus (\ell \otimes \R^{2})$ an \emph{order-four structure on $(X, \ell)$}: its transition elements are pairs of a rotor and a power of the unit bivector of the plane, of square $-1$. Two classical facts are used where named and are not in the store: (L2) a bundle is orientable iff $w_{1} = 0$ and an orientable bundle is spin iff $w_{2} = 0$, and $w_{2}$ of an oriented plane bundle is the reduction of its Euler class (the first half is the (L2) of Theorem \claimref{synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial}); (K) an orientable bundle with a nondegenerate form has a bundle of irreducible modules for its Clifford bundle with structure group the spin group iff $w_{2}(E_{+}) + w_{2}(E_{-}) = 0$ (Karoubi), of which the definite case is (L2).
\begin{enumerate}
\item[(i)] \emph{(Lifts of the antipodal map.)} In $\Cl(p,q)$ with $p + q = 2m$ the pseudoscalar $J_{p,q}$ anticommutes with every vector, so $\mathrm{Ad}(J_{p,q})$ is the grade involution and $J_{p,q}$ is a lift of $-1$; $J_{p,q}^{2} = (-1)^{m+q}$. Changing the sign of the square of one direction changes the sign of $J^{2}$. In particular $J^{2} = -1$ for $(6,0)$, $(4,2)$, $(2,4)$, $(0,6)$, for $(1,3)$ and $(3,1)$, for the plane $(0,2)$, and for the ten Majoranas $(10,0)$, where $J = \omega$ (\claimref{synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element}(ii)); $J^{2} = +1$ for $(5,1)$, $(3,3)$, $(1,5)$ and for $(4,0)$, $(2,2)$, $(0,4)$.
\item[(ii)] \emph{(Modules on a flat side.)} Let $S$ be a module of $\Cl(p,q)$ and $u$ an invertible operator on a space $W$. The identification $(v, s \otimes w) \sim (-v, J_{p,q}s \otimes uw)$ on $S^{n} \times (S \otimes W)$ defines a bundle over $\Sig$ exactly when $(J_{p,q} \otimes u)^{2} = 1$, and it is then a bundle of modules for the Clifford bundle of the flat side. So a flat side with $m + q$ even carries the untwisted module bundle ($u = 1$), and a flat side with $m + q$ odd carries the module bundle twisted by any $u$ with $u^{2} = -1$ on $W$: an order-four element of square $-1$ acting on every component of $W$.
\item[(iii)] \emph{(Classes.)} For every side, $w_{1}(E_{+}) = w_{1}(E_{-}) =: t$ and $w_{2}(E_{+}) + w_{2}(E_{-}) = m\,x^{2} + t^{2}$; on a flat side this is $(m + q)\,x^{2}$, the exponent of (i). For a wall with a definite physical side the two sides have the classes $m\,x^{2}$ (definite) and $(m + 1)\,x^{2}$ (the far side, on which the dying line is the negative direction): exactly one of them is $x^{2}$, which is nonzero for $n \geq 3$. Given (K), that side has no untwisted module bundle. For $n = 5$ it is the definite side, and the far side of signature $(5,1)$ has $J^{2} = +1$; for $n = 3$ it is the far side, of signature $(3,1)$, where the lift is the pseudoscalar of the spacetime algebra of that signature.
\item[(iv)] \emph{(The jump.)} In $\Cl(6,2)$, with $J_{6,0}$ the pseudoscalar of the six positive directions and $j$ that of the negative plane, $J_{6,0}$ and $j$ commute, $J_{6,0}^{2} = j^{2} = -1$, and $J_{6,0}\,j$ is the pseudoscalar, of square $+1$; it equals, up to sign, $J_{5,1}E$, with $J_{5,1}$ the pseudoscalar of five positive directions and one negative one and $E$ that of the remaining hyperbolic plane, $E^{2} = 1$, $E$ anticommuting with the two vectors of its plane and commuting with the other six. So under the equivalence of clause (4) of the cited rung-count theorem, in which the far side's Clifford bundle is the definite side's tensored with $\Cl(\shL \otimes \R^{0,2})$ up to a hyperbolic plane, the far side's lift of the monodromy is the pair $(J_{6,0}, j)$: the element $u$ of (ii) on the definite side is the pseudoscalar of the jump plane, which is a global section of $\Cl(\shL \otimes \R^{0,2})$ because $-1$ on the plane fixes it.
\item[(v)] \emph{(Which cross-sections.)} $w_{1}(\mathbb{RP}^{n}) = 0$ and $w_{2}(\mathbb{RP}^{n}) = x^{2}$ hold together exactly for $n \equiv 1 \pmod 4$, and $w_{1} = w_{2} = 0$ exactly for $n \equiv 3 \pmod 4$. Given (L2): $(\mathbb{RP}^{n}, \shL)$ has an order-four structure and no spin structure for $n \equiv 1 \pmod 4$, $n \geq 5$; $\mathbb{RP}^{n}$ is spin and $(\mathbb{RP}^{n}, \shL)$ has no order-four structure for $n \equiv 3 \pmod 4$. On the quarter-turn lens spaces $\Sig_{k} = L^{2k+1}(4)$ of Theorem \claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure}, $w_{2}(\Sig_{k}) = (k + 1)u$ and every class of $H^{1}(\Sig_{k}; \Z_{2}) = \{0, x\}$ has square $0$: given (L2), $L^{5}(4)$ is not spin and has no order-four structure with either of its two flat real lines.
\item[(vi)] \emph{(The signed count modulo 16.)} On the sixteen of one generation every element $g$ of the maximal torus of the Standard Model group with $g^{2} = 1$ acts by $\pm 1$ on the occupation states, reverses none of them or exactly eight, and fixes the neutral singlet; there are sixteen such elements. Hence for every such $g$ the element $\omega g$ has square $-1$, and the difference between the numbers of states on which it acts by one unit and by the other is $-16$ or $0$ on sixteen components and $-15$ or $+1$ on fifteen (the neutral singlet removed): the class modulo $16$ is $0$ on sixteen and $1$ on fifteen, the same for every $g$. For $n_{g}$ generations it is $0$ for sixteen-component generations and $n_{g}$ modulo $16$ for fifteen-component ones, which vanishes only when $16$ divides $n_{g}$; for three generations it is $3$.
\end{enumerate}
\emph{Reading (argued, and conditional where marked).} Hypotheses, neither a stored result: (H1) on $\mathbb{RP}^{5}$ with the structure of (ii) on the definite side, the spectral asymmetry of the twisted Dirac operator is $\pm\tfrac{1}{16}$ per four-dimensional Weyl component, with the sign of the unit by which $u$ acts on it (derived in the algebra in a proposal not yet stored; classical); (H2) the exponential of $2\pi$ times the unit times the total asymmetry is the phase by which the partition function of the four-dimensional fields is undefined on that space, and it must be trivial exactly when $u$ is a gauge symmetry, the fields then being required on every space that carries only the order-four structure (literature; not imported, by the maintainer's decision of 9 November 2026). (a) \emph{What the count says.} Given (H1) and (H2), by (vi) the phase depends only on the class of $\omega$ modulo the Standard Model group and is trivial for sixteen components per generation, for any number of generations, and nontrivial for fifteen unless $16$ divides the number of generations. (b) \emph{Whether it constrains the content.} Not in the stored chain. With the Majorana element $\omega$ is broken to the grading and no structure of (ii) exists for the fields (stored). At a stage whose gauge group contains $\omega$ (Pati-Salam, $\so(10)$, or $\uu(5)$ with its abelian factor gauged) the neutral singlet is already forced, by the multiplet or by the local conditions on that factor (\claimref{synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5}); at a stage whose group does not contain it and without the Majorana element, $\omega$ modulo the group is a global symmetry, and on (H2) a nontrivial phase for a global symmetry is no inconsistency. So the count would be a condition on the content only under a premise the store does not hold: that $\omega$ is gauged at a stage whose continuous gauge group does not contain it. (c) \emph{The link to the walls.} By (ii) to (iv) the wall theory supplies the structure on which the count is made, on the definite side of a wall with cross-section $\mathbb{RP}^{5}$ and tautological dying line, with the pseudoscalar of the jump plane as the order-four element. Three things are missing for a link to the sixteen, and no stored result supplies any of them: an identification of that element with $\omega$, which acts on the slot module, not on the jump; fields of the slot module on a six-dimensional $M$, the tower being four-dimensional, where the cross-sections are three-dimensional, the side that needs the twist on $\mathbb{RP}^{3}$ is the Lorentzian one, and in dimension three the literature's group of such structures is zero, so no count arises; and (H2). (d) \emph{The lens space.} By (v) $L^{5}(4)$ carries no order-four structure, so it is not a space on which the count could be made; this is the same fact as the stored remark that the rotor lift of the quarter turn in three planes has fourth power $-1$, an order-eight structure. (e) The conformal ambient $\R^{2,4}$ is among the signatures of (i) with $J^{2} = -1$, $J = I_{6}$, and $\mathbb{RP}^{5}$ is its space of lines; whether fields on lines of the ambient are to be twisted by $\omega$ is not a stored statement and is not claimed.

## technical
On a wall with cross-section $\mathbb{RP}^{2m-1}$ and tautological dying line, the restricted cotangent bundle is $2m$ copies of the line, with monodromy $-1$. On a side of signature $(p,q)$ the lift of $-1$ to the Clifford algebra is the pseudoscalar, whose square is $(-1)^{m+q}$; the Stiefel-Whitney class that obstructs spinors on the side is $(m+q)x^{2}$, the same exponent. So across the wall, where one direction changes sign, exactly one side has a lift of square $-1$ and needs an internal order-four element of square $-1$ to carry spinor fields; in the stored Clifford jump that element is the pseudoscalar of the jump plane $\shL \otimes \R^{0,2}$. For $\mathbb{RP}^{5}$ the side that needs it is the definite one, for $\mathbb{RP}^{3}$ the Lorentzian one. $\mathbb{RP}^{n}$ itself has the order-four structure with its tautological line exactly for $n \equiv 1 \pmod 4$; the lens space $L^{5}(4)$ has none.

On the sixteen, the involutions of the Standard Model torus reverse zero or eight states and fix the neutral singlet, so the signed count of the pseudoscalar of the ten Majoranas times any of them is $0$ modulo $16$ on sixteen components and $1$ modulo $16$ on fifteen. If the spectral asymmetry on $\mathbb{RP}^{5}$ is $1/16$ per component and its exponential is the anomaly phase, both of which are not stored, sixteen components per generation pass and fifteen fail; but the phase obstructs only a gauged element, the Majorana element breaks this one, and the stages that gauge it already force the neutral singlet. No stored result ties the wall's order-four element to the slot module.

## lay
Some spaces cannot carry the fields that describe particles like electrons unless those fields are also turned by an extra internal quarter-turn each time one goes around a loop. This result shows that the series' own theory of walls produces such spaces: on a wall whose cross-section is a five-dimensional projective space, one of the two sides is of this kind, and the wall itself provides the quarter-turn. A known argument from the literature would then say that the number of particle components must be a multiple of sixteen, which is the number in one generation when the right-handed neutrino is included, and not fifteen. The result also shows where that argument does not reach: it applies only if the quarter-turn symmetry is exact and gauged, whereas in the series the heavy neutrino mass breaks it; the wall's quarter-turn is not shown to be the particles' one; and the walls of four-dimensional spacetime are three-dimensional, where no such count exists.

## one-liner
On a real projective wall $\mathbb{RP}^{2m-1}$ with tautological dying line the lift of the monodromy on a side of signature $(p,q)$ is the pseudoscalar, of square $(-1)^{m+q}$, matching the class $(m+q)x^{2}$, so exactly one side needs an order-four twist, supplied in the stored jump by the pseudoscalar of the jump plane (the definite side for $\mathbb{RP}^{5}$, the Lorentzian one for $\mathbb{RP}^{3}$; none on $L^{5}(4)$); the signed count of $\omega$ modulo the Standard Model group is $0$ modulo $16$ on sixteen components and $1$ on fifteen, a condition on the content only for a gauged $\omega$, which the stored chain does not have.
