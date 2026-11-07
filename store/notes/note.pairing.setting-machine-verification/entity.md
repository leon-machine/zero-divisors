---
id: note.pairing.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: conformal-spacetime
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
comments_on:
- pairing.imported-null-flags
- pairing.imported-spin-coefficients-null-tetrad
- pairing.imported-flat-conformal-model-twistor-incidence
- pairing.imported-weyl-scalars-petrov-type-schwarzschild
locators:
  paper: T05-pairing
  number: Setting
  section: Machine verification
  line: 438
outside_ga:
  kind: other
  why: 'the class value 2i of n e_3 is a value of the complex functional pi on so(4,C), built on the complex null tetrad m = e_2 + i e_3, where i stands next to a spacetime vector'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the class value 2i of n e_3 is a value of the complex functional pi on so(4,C), built on the complex null tetrad m = e_2 + i e_3, where i stands next to a spacetime vector.'
---

## formal
Every computational identity asserted in this note has been verified in exact arithmetic by the script \texttt{verify\_T05\_pairing.py} \cite{ButlerVerifyT05pairing}, which imports the series' shared library \texttt{GA.py}: its basis-blade Clifford engine over the rationals, its Gaussian rationals for the complex Witt vectors, its rational functions in one variable for the two Schwarzschild frames, and its exact ranks and kernels. Identities in $\Q(F)$ or $\Q(\beta)$ are verified as identities where the text says so, and at rational sample points where the text says so. No floating point is used anywhere; the script exits nonzero on any failure. Fifty-three checks, all passing, in eight parts. On the $(t, r, \vartheta)$ and $(T, r, \vartheta)$ blocks the check covers, the connection forms of both frames are verified against the first structure equations, which with antisymmetry determines them there, the curvature forms are derived from them by the second structure equations, and the block one-forms are tied to the frame matrices that the classes are computed from. The pre-registration is deposited beside the script \cite{ButlerPreregT05pairing}.

\emph{Part A: the stabiliser.} The tetrad's pairings; the action $\tfrac12[e_{a}e_{b}, e_{c}] = \eta_{bc}e_{a} - \eta_{ac}e_{b}$ on all basis bivectors and vectors; the six values of $\pv$ with the two transverse images $e_{02}\cdot\ell = -e_{2}$, $e_{12}\cdot\ell = e_{2}$; the equivalence of $B\cdot W \subseteq W$ with $\pv(B) = 0$ on twenty random complex bivectors, none of which stabilises, with the projection $B + \pv(B)e_{12}$ always stabilising; the null rotations $\ell e_{2}$, $\ell e_{3}$ as bivectors fixing $\ell$; the rank two of $(\operatorname{Re}\pv, \operatorname{Im}\pv)$, the rank four of $\{e_{01}, e_{23}, \ell e_{2}, \ell e_{3}\}$ and the rank five with $e_{02}$ appended; the classes $2$, $2i$ of $ne_{2}$, $ne_{3}$ and $0$, $4$ of $n m$, $n\mb$.

\emph{Part B: the Fock dictionary.} The Clifford relations of the four Jordan-Wigner operators; $c(\ell)$, $c(m)$ annihilating the vacuum and $c(n)$, $c(\mb)$ creating; $\bra{12}B\ket{0} = -\pv(B)$ on all six basis bivectors; the $2 \times 2$ structure of the even sector, including $a_{1}a_{2}\ket{12} = -\ket{0}$.

\emph{Part C: the witness.} $R\tilde R = 1$; $R\ket{0} = \tfrac35\ket{0} + \tfrac45\ket{12}$; $R\ell\tilde R$ with its nullity and its pairing $\tfrac{32}{25}$ with $\ell$; the rotated pair annihilating $R\ket{0}$; the boost rotor acting on $\ket{0}$ as $\tfrac13$.

\emph{Part D: the static frame.} $f'$ and $f''$ by differentiation in $\Q(F)$; the first structure equations on the $(t, r, \vartheta)$ block; the second structure equations giving the three curvature two-forms with their coefficients; the bivectors reproducing all sixteen frame derivatives; the block one-forms evaluated on the frame vectors equal to the frame matrices; the four classes; the scaling law with the derivative term $(e_{1}\lambda)\ell$ modelled and nonzero; the horizon zeros and the value $-\tfrac{48}{125}$; the tetrad components $(0, 0, 0, -2\sqrt f/r)$; the transverse expansion, its equality with $-\pv(\Omega(\mb))$, and $\nabla_{\ell}\ell = (f'/2\sqrt f)\ell$; $\Omega(e_{0}) \propto e_{01}$ and $\Omega(e_{1}) = 0$.

\emph{Part E: curvature.} The two eigenvalues from the derived block forms (the angular one is entered); the six classes; the null rotation $(M/r^{3})\ell e_{2}$ for the loop $(\ell, e_{2})$, the class $2M/r^{3}$ for $(n, e_{2})$, and the six complex loops, $(n, \mb)$ alone carrying $4M/r^{3}$; the Weyl dictionary: Ricci-flatness on all sixteen frame pairs, $\Psi_{0} = \Psi_{1} = 0$, $\Psi_{2} = -4M/r^{3}$, and the six loop classes equal to $(\Psi_{0}, 0, -\Psi_{1}, \Psi_{1}, 0, -\Psi_{2})$, in the adapted tetrad and again in a generic rational tetrad where $\Psi_{0}$ and $\Psi_{1}$ are nonzero.

\emph{Part F: the regular frame.} The first and second structure equations on the $(T, r, \vartheta)$ block as identities in $\Q(\beta)$, with $\beta' = -\beta^{3}/4M$ and the curvature coefficients equal to the static ones as functions of $r$; the bivectors against the frame derivatives; the block one-forms against the frame matrices; the four classes; the values $-\tfrac{16}{125}, 0, 4$ at $\beta = \tfrac45, 1, 2$; the ingoing vacuum's classes $+(1 + \beta)/r$ with the values $\tfrac{144}{125}, 2, 12$; the covariance factor $F/(1 + \beta)$ at five rational points of the circle; $\Omega(e_{0}) = 0$ and $\Omega(e_{1}) \propto e_{01}$; the transverse expansion $2(1 - \beta)/r$ with its sign on both sides and $\nabla_{\ell}\ell = (\beta^{3}/4M)\ell$; the $(n, e_{2})$ curvature class $2M/r^{3}$ in this frame, equal to the static value at three radii and to $1$ on the horizon.

\emph{Part G: gap 1.} $\Lambda^{\mathsf T}\eta\Lambda = \eta$, the images $\tfrac{F}{1 + \beta}\ell$ and $e_{2}$, and the identity on the circle at three rational points; the two Hawking states as vacua of rotated decompositions with the two distinct rational null directions.

\emph{Part H: the flat model.} $\nz$, $\ninf$; isotropy and rank of $W(x)$ at four points; the translation identity, the fixing of $\ninf$, the action on $\ell(x)$, and the second-order remainder of a finite displacement; the classes $(\ip{dx}{\ell}, \ip{dx}{m}, 0)$ at four points for twenty random real displacements; the four named real displacements and the complex $m$, $\mb$; incidence at three values of $s$; the rank three of the three functionals on the fifteen bivectors, their common kernel of dimension twelve, and its coincidence with the stabiliser on ten random kernel elements and on every basis bivector.

What the script does not check: the geometric identifications imported as Facts \claimref{pairing.imported-null-flags}, \claimref{pairing.imported-spin-coefficients-null-tetrad}, \claimref{pairing.imported-flat-conformal-model-twistor-incidence} and \claimref{pairing.imported-weyl-scalars-petrov-type-schwarzschild} (the note computes components and matches them to named quantities; it does not re-derive the formalisms), Lemma \claimref{pairing.loop-classes-are-weyl-components} beyond its Schwarzschild instance; the angular-plane curvature coefficient $(1 - f)/r^{2}$, which lies off the $(t, r, \vartheta)$ block and is taken from the singularity paper's verified appendix; and the $\hat3$ forms of both frames beyond the mirror symmetry, the $e_{23}$ term being in the stabiliser by Part A.

## technical
pending

## lay
pending

## one-liner
pending
