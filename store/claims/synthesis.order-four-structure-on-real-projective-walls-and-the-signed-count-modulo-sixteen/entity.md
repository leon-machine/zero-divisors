---
id: synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen
kind: claim
version: 2
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
- name: Claude Fable 5.2
  role: 'hypothesis (H1) of the Reading replaced by a uses edge to the stored spectral-asymmetry result; no clause changed'
  version: 2
  source: maintainer pass 2026-11-16 (anomaly)
amendments:
- version: 2
  kind: restatement
  defect: 'the Reading entered half the spectral asymmetry on real projective five-space as hypothesis (H1), a proposal not yet stored; that result is now stored, so the text called a stored result a hypothesis and the derivation carried no edge to it. The formal level now cites it as (H1) and the derivation uses it; clauses (i) to (vi) and the conclusions of the Reading are unchanged, and (H2) stays a hypothesis.'
review: draft
derivations:
- name: main
  uses:
  - synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element@1
  - synthesis.wall-rung-count-is-height-of-dying-line-class@2
  - synthesis.imported-whitney-product-formula-and-projective-space@2
  - synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure@1
  - synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5@3
  - standard-model.imported-anomaly-coefficients@1
  - synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials@1
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
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: 'Version 1 -> 2. The sibling result on the spectral asymmetry of real projective five-space is stored, so hypothesis (H1) of the Reading is now a cited result and a uses edge; the formal Reading, the technical level, the proof''s closing sentence and the note say so. No clause and no conclusion changed; (H2), the anomaly statement of the literature, stays unimported by decision D4 of 16 November 2026.'
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
    textbook) and transport-absent; what is new for the store is its form in the wall theory. Half the spectral asymmetry, xi = 1/16 per component (the asymmetry is 1/8), is derived, in geometric algebra, in the result
    synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials, which is now stored
    and is cited here as (H1), with a uses edge (version 2). Literature, not stored as Facts: Garcia-Etxebarria and
    Montero, Dai-Freed anomalies in particle physics, arXiv:1808.00009 (J. High Energy Phys. 2019), checked
    at source: section 4.3, the generator of the bordism group of five-manifolds with this structure is real
    projective five-space, with eta invariant 1/16; appendix C.4, equation (C.21), the group is Z_16 and the
    group in dimension three is 0; section 2.1, an anomaly in a global symmetry is not an inconsistency, it
    means that the symmetry cannot be gauged; the order-four element there is the one inside
    X = -2Y + 5(B - L) in that paper's normalisation of hypercharge, the mass term of the right-handed
    neutrino breaks it, and when it sits in a U(1) the condition follows from the local conditions. Cited
    from memory: Dai and Freed 1994 and Witten 2016 (Rev. Mod. Phys. 88, 035001) for the phase of the
    partition function as the exponentiated eta invariant; Hsieh, arXiv:1808.02881, for the same count;
    Tachikawa and Yonekura 2019, from memory and not verified at source; Karoubi 1968 for spin structures on bundles with indefinite forms;
    Milnor and Stasheff for the classes of plane bundles. Leon's decision of 9 November 2026 stands: the
    modulo-16 statement is not imported here; the Reading is conditional on it and says so. Where this
    leaves the open problem's success clause: its first branch (the anomaly vanishes exactly for sixteen
    components per generation) is reached only conditionally on that unimported statement, and then for three
    generations, not for every number of generations (fifteen-component generations pass when sixteen divides
    their number); its second branch (the count does not constrain the content) is reached at the argued
    level only, in Reading (b); its third branch (the reading without the Majorana element is excluded) is
    not addressed. Nothing is reached at the proved level. The two classical facts (L2) and (K) named in the
    statement are not stored; the clauses that use them are conditional on them and say so, and they will
    not appear among the postulates the result is listed as holding given.
---

## formal
Let $\Sig = \mathbb{RP}^{n}$, $n = 2m - 1$, be the cross-section of a tame corank-one wall with tautological dying line $\shL$, $x = w_{1}(\shL)$, as in Theorem \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}(3) (a wall on $\Sig \times \R$). By Fact \claimref{synthesis.imported-whitney-product-formula-and-projective-space}(iii), $T^{*}M|_{\Sig} \cong T\Sig \oplus \underline{\R} \cong 2m\,\shL$, the flat bundle $S^{n} \times_{\pm 1} \R^{2m}$ whose monodromy is the antipodal map $-1$. A \emph{side} is a nondegenerate form on this bundle with maximal positive and negative subbundles $E_{+}$, $E_{-}$ of ranks $p$, $q$; it is \emph{flat} if the form is a constant form of signature $(p,q)$ on $\R^{2m}$, so that $E_{+} \cong p\,\shL$, $E_{-} \cong q\,\shL$ and the Clifford bundle of the side is $S^{n} \times_{\pm 1} \Cl(p,q)$ with $-1$ acting by the grade involution; a definite side is flat. For a line bundle $\ell$ over a manifold $X$ call a spin structure on $TX \oplus (\ell \otimes \R^{2})$ an \emph{order-four structure on $(X, \ell)$}: its transition elements are pairs of a rotor and a power of the unit bivector of the plane, of square $-1$. Two classical facts are used where named and are not in the store: (L2) a bundle is orientable iff $w_{1} = 0$ and an orientable bundle is spin iff $w_{2} = 0$, and $w_{2}$ of an oriented plane bundle is the reduction of its Euler class (the first half is the (L2) of Theorem \claimref{synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial}); (K) an orientable bundle with a nondegenerate form has a bundle of irreducible modules for its Clifford bundle with structure group the spin group iff $w_{2}(E_{+}) + w_{2}(E_{-}) = 0$ (Karoubi), of which the definite case is (L2). On a flat side (K) can be replaced by obstruction theory: the obstruction is the pull-back of the class of the extension of the group of order two by the lift of $-1$, which is $x^{2}$ exactly when the lift has square $-1$ and is nonzero on $\mathbb{RP}^{n}$ for $n \geq 2$; that route is not written out here and (K) is kept as the named condition.
\begin{enumerate}
\item[(i)] \emph{(Lifts of the antipodal map.)} In $\Cl(p,q)$ with $p + q = 2m$ the pseudoscalar $J_{p,q}$ anticommutes with every vector, so $\mathrm{Ad}(J_{p,q})$ is the grade involution and $J_{p,q}$ is a lift of $-1$; $J_{p,q}^{2} = (-1)^{m+q}$. Changing the sign of the square of one direction changes the sign of $J^{2}$. In particular $J^{2} = -1$ for $(6,0)$, $(4,2)$, $(2,4)$, $(0,6)$, for $(1,3)$ and $(3,1)$, for the plane $(0,2)$, and for the ten Majoranas $(10,0)$, where $J = \omega$ (\claimref{synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element}(ii)); $J^{2} = +1$ for $(5,1)$, $(3,3)$, $(1,5)$ and for $(4,0)$, $(2,2)$, $(0,4)$.
\item[(ii)] \emph{(Modules on a flat side.)} Let $S$ be a module of $\Cl(p,q)$ and $u$ an invertible operator on a space $W$. The identification $(v, s \otimes w) \sim (-v, J_{p,q}s \otimes uw)$ on $S^{n} \times (S \otimes W)$ defines a bundle over $\Sig$ exactly when $(J_{p,q} \otimes u)^{2} = 1$, and it is then a bundle of modules for the Clifford bundle of the flat side. So a flat side with $m + q$ even carries the untwisted module bundle ($u = 1$), and a flat side with $m + q$ odd carries the module bundle twisted by any $u$ with $u^{2} = -1$ on $W$: an order-four element of square $-1$ acting on every component of $W$.
\item[(iii)] \emph{(Classes.)} For every side, $w_{1}(E_{+}) = w_{1}(E_{-}) =: t$ and $w_{2}(E_{+}) + w_{2}(E_{-}) = m\,x^{2} + t^{2}$; on a flat side this is $(m + q)\,x^{2}$, the exponent of (i). For a wall with a definite physical side the two sides have the classes $m\,x^{2}$ (definite) and $(m + 1)\,x^{2}$ (the far side, on which the dying line is the negative direction): exactly one of them is $x^{2}$, which is nonzero for $n \geq 3$. Given (K), that side has no untwisted module bundle. For $n = 5$ it is the definite side, and the far side of signature $(5,1)$ has $J^{2} = +1$; for $n = 3$ it is the far side, of signature $(3,1)$, where the lift is the pseudoscalar of the spacetime algebra of that signature.
\item[(iv)] \emph{(The jump.)} In $\Cl(6,2)$, with $J_{6,0}$ the pseudoscalar of the six positive directions and $j$ that of the negative plane, $J_{6,0}$ and $j$ commute, $J_{6,0}^{2} = j^{2} = -1$, and $J_{6,0}\,j$ is the pseudoscalar, of square $+1$; it equals, up to sign, $J_{5,1}E$, with $J_{5,1}$ the pseudoscalar of five positive directions and one negative one and $E$ that of the remaining hyperbolic plane, $E^{2} = 1$, $E$ anticommuting with the two vectors of its plane and commuting with the other six. So under the equivalence of clause (4) of the cited rung-count theorem, in which the far side's Clifford bundle is the definite side's tensored with $\Cl(\shL \otimes \R^{0,2})$ up to a hyperbolic plane, the far side's lift of the monodromy is the pair $(J_{6,0}, j)$: the element $u$ of (ii) on the definite side is the pseudoscalar of the jump plane, which is a global section of $\Cl(\shL \otimes \R^{0,2})$ because $-1$ on the plane fixes it.
\item[(v)] \emph{(Which cross-sections.)} $w_{1}(\mathbb{RP}^{n}) = 0$ and $w_{2}(\mathbb{RP}^{n}) = x^{2}$ hold together exactly for $n \equiv 1 \pmod 4$, and $w_{1} = w_{2} = 0$ exactly for $n \equiv 3 \pmod 4$. Given (L2): $(\mathbb{RP}^{n}, \shL)$ has an order-four structure and no spin structure for $n \equiv 1 \pmod 4$, $n \geq 5$; $\mathbb{RP}^{n}$ is spin and $(\mathbb{RP}^{n}, \shL)$ has no order-four structure for $n \equiv 3 \pmod 4$. On the quarter-turn lens spaces $\Sig_{k} = L^{2k+1}(4)$ of Theorem \claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure}, $w_{2}(\Sig_{k}) = (k + 1)u$ and every class of $H^{1}(\Sig_{k}; \Z_{2}) = \{0, x\}$ has square $0$: given (L2), $L^{5}(4)$ is not spin and has no order-four structure with either of its two flat real lines.
\item[(vi)] \emph{(The signed count modulo 16.)} On the sixteen of one generation every element $g$ of the maximal torus of the Standard Model group with $g^{2} = 1$ acts by $\pm 1$ on the occupation states, reverses none of them or exactly eight, and fixes the neutral singlet; they give sixteen sign patterns on the sixteen (the elements of the image), one of them trivial. Every element $h$ of the connected Standard Model group with $h^{2} = 1$ on the sixteen is conjugate into the maximal torus, and the number of reversed states is invariant under conjugation, so the same holds for $h$ (the conjugacy is a classical fact of compact connected Lie groups, not derived here). Hence for every such $g$ the element $\omega g$ has square $-1$, and the difference between the numbers of states on which it acts by one unit and by the other is $-16$ or $0$ on sixteen components and $-15$ or $+1$ on fifteen (the neutral singlet removed): the class modulo $16$ is $0$ on sixteen and $1$ on fifteen, the same for every $g$, and, for one generation, $16$ is the largest modulus with that property, the counts on the class differing by exactly $16$ (for $n_{g}$ generations they differ by $16n_{g}$): the modulus comes from the arithmetic of the involutions (each reverses none or eight states), with no anomaly statement used. For $n_{g}$ generations it is $0$ for sixteen-component generations and $n_{g}$ modulo $16$ for fifteen-component ones, which vanishes only when $16$ divides $n_{g}$; for three generations it is $3$ (the count is $-45$). For the abelian charge $X = 5 - 2N$ of which $\omega$ is the quarter turn, the sums of $X$ and of $X^{3}$ over the components are $0$ and $0$ on sixteen, $-5$ and $-125$ on fifteen, and the sum of $X$ is $-10$ on fifteen with the full state in place of the empty one.
\end{enumerate}
\emph{Reading (argued, and conditional where marked).} Two inputs, the first a stored result and the second a hypothesis that is not stored: (H1) on $\mathbb{RP}^{5}$ with the structure of (ii) on the definite side, half the spectral asymmetry of the twisted Dirac operator is $\xi = \tfrac12\eta(0) = \pm\tfrac{1}{16}$ per component of the sixteen ($\eta(0) = \pm\tfrac18$), with the sign of the unit by which $u$ acts on the component (Theorem \claimref{synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials}(iv), (v), proved there given the classical analysis it names; derived there on the six-space with all squares $-1$, here with all squares $+1$; both have $J^{2} = -1$ by (i) and give the same structure on $\mathbb{RP}^{5}$; classical); (H2) the exponential of $2\pi$ times the unit times the total $\xi$ is the phase by which the partition function of the four-dimensional fields is undefined on that space, and it must be trivial if $u$ is gauged, the fields then being required on every space that carries only the order-four structure (literature, a necessary condition; not imported, by the maintainer's decision of 9 November 2026). (a) \emph{What the count says.} Given (H1) and (H2), by (vi) the phase depends only on the class of $\omega$ modulo the Standard Model group and is trivial for sixteen components per generation, for any number of generations, and nontrivial for fifteen unless $16$ divides the number of generations; so ``exactly for sixteen'' holds for three generations and not for every number of them. (b) \emph{Whether it constrains the content (argued, not proved).} Not in the stored chain, on this reading of it. With the Majorana element $\omega$ is broken to the grading and no structure of (ii) exists for the fields (stored). At a stage whose gauge group contains $\omega$ the neutral singlet is already forced: at Pati-Salam and $\so(10)$ by the multiplet, the gauge algebra there deciding the bit (\claimref{synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5}); at a stage with $\uu(5)$ and its abelian factor gauged, not by that theorem, which leaves the bit free for an algebra inside $\uu(5)$, but by the mixed gravitational and cubic conditions of Fact \claimref{standard-model.imported-anomaly-coefficients} applied to $X$: by (vi) both sums vanish on sixteen components and the linear one is $-5$ on fifteen and $-10$ with the swapped singlet. At a stage whose group does not contain $\omega$ and without the Majorana element, $\omega$ modulo the group is a global symmetry, and on the literature's reading of (H2) a nontrivial phase for a global symmetry is no inconsistency. So the count would be a condition on the content only under a premise the store does not hold: that $\omega$ is gauged at a stage whose continuous gauge group does not contain it. (c) \emph{The link to the walls.} By (ii) to (iv) the wall theory supplies the structure on which the count is made, on the definite side of a wall with cross-section $\mathbb{RP}^{5}$, tautological dying line and definite physical side (with a Lorentzian physical side of signature $(1,5)$ the side that needs the twist is the far one), with the pseudoscalar of the jump plane as the order-four element. Three things are missing for a link to the sixteen, and no stored result supplies any of them: an identification of that element with $\omega$, which acts on the slot module, not on the jump; fields of the slot module on a six-dimensional $M$, the tower being four-dimensional, where the cross-sections are three-dimensional, the side that needs the twist on $\mathbb{RP}^{3}$ is the Lorentzian one, and in dimension three the literature's group of such structures is zero, so no count arises; and (H2). (d) \emph{The lens space.} By (v) $L^{5}(4)$ carries no order-four structure, so it is not a space on which the count could be made; this is the same fact as the stored remark that the rotor lift of the quarter turn in three planes has fourth power $-1$, an order-eight structure. (e) The conformal ambient $\R^{2,4}$ is among the signatures of (i) with $J^{2} = -1$, $J = I_{6}$, and $\mathbb{RP}^{5}$ is its space of lines; whether fields on lines of the ambient are to be twisted by $\omega$ is not a stored statement and is not claimed.

## technical
On a wall with cross-section $\mathbb{RP}^{2m-1}$ and tautological dying line, the restricted cotangent bundle is $2m$ copies of the line, with monodromy $-1$. On a side of signature $(p,q)$ the lift of $-1$ to the Clifford algebra is the pseudoscalar, whose square is $(-1)^{m+q}$; the Stiefel-Whitney class that obstructs spinors on the side is $(m+q)x^{2}$, the same exponent. So across a wall with a definite physical side, where one direction changes sign, exactly one side has a lift of square $-1$ and needs an internal order-four element of square $-1$ to carry spinor fields; in the stored Clifford jump that element is the pseudoscalar of the jump plane $\shL \otimes \R^{0,2}$. For $\mathbb{RP}^{5}$ the side that needs it is the definite one, for $\mathbb{RP}^{3}$ the Lorentzian one. $\mathbb{RP}^{n}$ itself has the order-four structure with its tautological line exactly for $n \equiv 1 \pmod 4$; the lens space $L^{5}(4)$ has none.

On the sixteen, the involutions of the Standard Model torus reverse zero or eight states and fix the neutral singlet, so the signed count of the pseudoscalar of the ten Majoranas times any of them is $0$ modulo $16$ on sixteen components and $1$ modulo $16$ on fifteen. The modulus is intrinsic to that arithmetic: the counts on the class differ by exactly $16$ per generation. Half the spectral asymmetry on $\mathbb{RP}^{5}$ is $\xi = 1/16$ per component (the asymmetry itself $1/8$; a stored result); if its exponential is the anomaly phase, which is not stored, sixteen components per generation pass and fifteen fail for three generations; but, argued, the phase obstructs only a gauged element, the Majorana element breaks this one, and the stages that gauge it already force the neutral singlet, by the multiplet or by the linear and cubic conditions on $X = 5 - 2N$ (sums $0$ on sixteen, $-5$ and $-125$ on fifteen). No stored result ties the wall's order-four element to the slot module.

## lay
Some spaces cannot carry the fields that describe particles like electrons unless those fields are also turned by an extra internal quarter-turn each time one goes around a loop. This result shows that the series' own theory of walls produces such spaces: on a wall whose cross-section is a five-dimensional projective space, one of the two sides is of this kind, and the wall itself provides the quarter-turn. A known argument from the literature would then say that the signed number of components of odd charge must be a multiple of sixteen, if the quarter-turn is gauged; sixteen is the number in one generation when the right-handed neutrino is included, and fifteen without it fails for three generations. The result also shows where that argument does not reach: it applies only if the quarter-turn symmetry is exact and gauged, whereas in the series the heavy neutrino mass breaks it (that the count therefore constrains nothing in the series is argued, not proved); the wall's quarter-turn is not shown to be the particles' one; and the walls of four-dimensional spacetime are three-dimensional, where no such count exists.

## one-liner
Given two classical criteria named in the statement, and under Hypothesis (S) for the count: on a real projective wall $\mathbb{RP}^{2m-1}$ with tautological dying line the lift of the monodromy on a side of signature $(p,q)$ is the pseudoscalar, of square $(-1)^{m+q}$, matching the class $(m+q)x^{2}$, so on a wall with a definite physical side exactly one side needs an order-four twist, supplied in the stored jump by the pseudoscalar of the jump plane (the definite side for $\mathbb{RP}^{5}$, the Lorentzian far side for $\mathbb{RP}^{3}$; none on $L^{5}(4)$); the signed count of $\omega$ modulo the Standard Model group is $0$ modulo $16$ on sixteen components and $1$ on fifteen, with $16$ the largest such modulus; on the unimported anomaly statement it would be a condition on the content only for a gauged $\omega$, which, argued, the stored chain has at no stage that does not already force the singlet.
