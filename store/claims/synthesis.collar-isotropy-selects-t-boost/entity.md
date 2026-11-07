---
id: synthesis.collar-isotropy-selects-t-boost
kind: claim
version: 2
title: 'Collar isotropy selects the $t$-boost'
status: proved
region: synthesis
subject: thermality
tags:
- modular-theory
- kasner
- rotors-and-stabilisers
- no-go
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'unit resolution pass, the frame atom complexified by the central unit I_5 of Cl(2,3)'
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
derivations:
- name: main
  uses:
  - singularity.imported-interior-collar-kasner-form@6
  - singularity.modular-flow-boundary-modes-holonomy-universal@2
  - singularity.kms-uniqueness-factor@6
  - synthesis.phase-flow-is-time-rotor-flow-kms-continuation@3
  - std-algebra.complexification-is-the-odd-extension@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_boost_algebra_and_isotropy_centraliser
- kind: check
  ref: check.py::check_isotropy_invariant_kms_is_t_boost_only
- kind: check
  ref: check.py::check_kasner_rates_fix_isotropy_only
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.collar-kms-extension-three-flows
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the pointwise frame atom is the complexification Cl(1,3)_C, whose unit must commute with every frame vector (the flow acts on odd elements too); it is the central unit I_5 = I_4 e of Cl(2,3) (std-algebra.complexification-is-the-odd-extension, cited and added as a pinned uses edge, since the proof uses I_5 central with square -1), with e a frame generator so that I_5* = -I_5 (computed in the proof). K = (B_b + I_5 B_c)/2 and alpha_t = Ad(e^{I_5 t K}); the formal level says that this unit is not the boundary modes'' J = e_2 e_3, which does not commute with e_2, e_3. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: K = (B_b + iB_c)/2 and Ad(e^{itK}) live in the plain complexification Cl(1,3)_C, whose i must commute with the vectors. Declaration kind set to complex-analysis by Leon''s ruling R1 (atom, boundary-mode and window flows keep i).'
  open_problem: op.collar-kms-extension
  note: Answers the problem's second attack bullet (the SO(3)-invariant states on the sphere holonomies compatible with KMS for B1) positively for B1, on the pointwise frame atom Cl(1,3)_C, a model choice that is neither the completed-pair atom nor an algebra the series constructs for the collar. Invariance under rotations mixing the t-direction with a sphere direction would exclude every faithful KMS state, but those rotations are not symmetries of the collar. It does not decide the extension question, which still rests on hypothesis (C) of the stored three-flows result. Transport-essential in its input (the collar's holonomy boosts and Kasner rates), elementary in its algebra.
---

## formal
At a point of the collar of Fact \claimref{singularity.imported-interior-collar-kasner-form}, with adapted frame $e_{0}$ (along $\partial_{\tau}$, $Q(e_{0}) = 1$), $e_{1}$ (the $t$-direction) and $e_{2}, e_{3}$ (the sphere directions), let the atom be the frame algebra $\Cl(1,3)_{\C} \cong \Mat_{4}(\C)$, realised as $\Cl(2,3) = \Cl(1,3) \oplus \Cl(1,3)I_{5}$ with the central unit $I_{5} = I_{4}e$ of the odd extension ($e$ orthogonal to the frame, $Q(e) = +1$, Theorem \claimref{std-algebra.complexification-is-the-odd-extension}), with the frame $*$-structure ($e$ taken as a frame generator, so $I_{5}^{*} = -I_{5}$) (a model choice: this pointwise frame atom is not the completed-pair atom of Proposition \claimref{singularity.modular-flow-boundary-modes-holonomy-universal}, on which only $B_{1}$ acts, nor an algebra the series constructs for the collar), the boosts $B_{i} = e_{0}e_{i}$ ($*$-symmetric) and the rotations $R_{jk} = e_{j}e_{k}$ ($*$-antisymmetric), as in Theorem \claimref{synthesis.phase-flow-is-time-rotor-flow-kms-continuation}(i). The holonomy boosts of Proposition \claimref{singularity.modular-flow-boundary-modes-holonomy-universal} are $B_{1}$ along the $t$-lines and $B_{2}, B_{3}$ along the sphere. Let $K = \tfrac12(B_{b} + I_{5}B_{c})$ with $B_{b}$ a boost bivector and $B_{c}$ a rotation bivector, so $K = K^{*}$ and $\alpha_{t} = \operatorname{Ad}(e^{I_{5}tK})$ is a flow of $*$-automorphisms. The unit here is $I_{5}$, which commutes with every frame vector, not the boundary modes' unit $J = e_{2}e_{3}$, which does not commute with $e_{2}$, $e_{3}$; the two are not identified.
\begin{enumerate}
\item[(i)] \emph{(Isotropy.)} The rotations of the $(e_{2}, e_{3})$ plane fix the Kasner rate tensor $\operatorname{diag}(p_{1}, p_{2}, p_{3}) = \operatorname{diag}(-\tfrac13, \tfrac23, \tfrac23)$ and the collar's first-order rates $\operatorname{diag}(-\tfrac13 - \tfrac{4}{15}R, \tfrac23 - \tfrac{2}{15}R, \tfrac23 - \tfrac{2}{15}R)$; no rotation of the $(e_{1}, e_{2})$ plane with nonzero angle mod $\pi$ fixes either.
\item[(ii)] \emph{(Selection.)} A faithful state on the atom that is $(\alpha, \beta)$-KMS at some $\beta \ne 0$ and invariant under the isotropy rotations $\exp(\theta R_{23}/2)$ exists if and only if $B_{b} \in \R B_{1}$ and $B_{c} \in \R R_{23}$. In particular, among the boost flows ($B_{c} = 0$) only the $t$-boost qualifies: for every $\beta$ its KMS state $e^{-\beta B_{1}/2}/\Tr e^{-\beta B_{1}/2}$ is isotropy-invariant, while the sphere boosts $B_{2}$, $B_{3}$, and every boost with a sphere component, have no isotropy-invariant faithful KMS state at any $\beta \ne 0$.
\item[(iii)] \emph{(Over the sphere.)} A family of such states over the $S^{2}$ of the collar, carried into itself by the $SO(3)$ isometries, has the same $\beta$ at every point.
\item[(iv)] \emph{(The frame group is not a symmetry.)} Invariance under the whole frame rotation group generated by $R_{12}, R_{13}, R_{23}$ would admit no faithful KMS state at $\beta \ne 0$ for any nonzero $K$ of this form, since nothing nonzero in the bivector span commutes with all three rotations; by (i) that group is not a symmetry of the collar.
\end{enumerate}
So, on this pointwise atom, the spherical symmetry of the collar does not obstruct a $B_{1}$ spectrum: the $SO(3)$-invariant states compatible with KMS for $B_{1}$ are exactly the $B_{1}$-Gibbs states of one $\beta$, and the same symmetry excludes thermality for the sphere holonomies, so the number $2\pi/p_{2} = 3\pi$ belongs to no invariant state.

## technical
On the collar the only symmetries fixing a point are rotations of the two sphere directions, because the Kasner rates of the time direction and the sphere directions differ. A state that is thermal for a Lorentz (bivector) flow on the pointwise frame atom $\Cl(1,3)_{\C}$, a model choice distinct from the completed-pair atom, and invariant under those rotations must have a generator commuting with them, and the only such boost is the one along the time lines. Its thermal state is invariant at every temperature, while thermal states for the sphere boosts are rotated into each other and are never invariant. Imposing invariance under all frame rotations would forbid every thermal state, but that larger group is not a symmetry.

## lay
Near the black hole's singularity one can ask whether a local quantum system built on the four directions at a point can sit in a thermal state for the flow along the time lines, and whether the round symmetry of the sphere gets in the way. It does not: the round symmetry allows exactly one kind of thermal state, the one for the time-line flow, at any temperature, and it rules out thermal states for the flows around the sphere.

## one-liner
On the pointwise frame atom $\Cl(1,3)_{\C}$ at a collar point, under the spherical isotropy the faithful KMS states of bivector flows are exactly those of the $t$-boost (optionally with a rotation about it); the sphere boosts admit none.
