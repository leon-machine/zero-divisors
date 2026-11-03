---
id: note.sheaf.setting-introduction
kind: note
version: 1
title: Introduction
status: setting
subject: walls
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
comments_on:
- sheaf.tameness
locators:
  paper: T04
  number: Setting
  section: Introduction
  line: 335
---

## formal
The root paper of this series operates at a single fibre. Given a real quadratic space of mixed signature, the null vectors of its Clifford algebra admit no equivariant element-level repair in any extension, while the space of points is repaired totally and uniquely by the Witt completion $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$; the full taxonomy of zero-divisor obstructions, with the transport rule and minimality theorem belonging to each type, is settled in the same paper \cite{ButlerT1}. It treats one algebra at a time.

Geometry does not. In the gravitational application that motivates the series, the metric degenerates on a \emph{locus} $\Sig$ inside a manifold $M$: the algebra that needs completion is over $\Sig$, while the algebra away from $\Sig$ is nondegenerate and must be left unchanged. The natural demand is therefore a sheaf of Clifford algebras whose fibre is $\Cl(p,q)$ on the nondegenerate region and $\Cl(p{+}1,q{+}1)$ over $\Sig$. Stated naively this is impossible, and the impossibility is instructive: $\Cl(p,q)$ has dimension $2^n$ and $\Cl(p{+}1,q{+}1)$ has dimension $2^{n+2}$ (sixteen against sixty-four in the spacetime case), and the rank of a locally free sheaf is locally constant. The fibre dimension cannot jump. The subject of this paper is the resolution of that tension: the jump must be relocated into \emph{structure}, and there are exactly two natural places for it to go.

The first is a sheaf of constant rank $2^n$, the \emph{degeneration sheaf}: the Clifford sheaf of the degenerate cometric itself. Its fibres over $\Sig$ remain $2^n$-dimensional but degenerate as algebras, acquiring a canonical two-sided ideal that squares to zero. The singular locus registers as non-reducedness, in precise parallel with the appearance of nilpotents in the special fibres of algebraic-geometric degenerations, and the ideal is exactly the kind of object a blow-up is performed along: a canonical sheaf of ideals supported on the singular locus. The second is a sheaf of constant rank $2^{n+2}$, the \emph{ambient sheaf}, whose fibre is $\Cl(p{+}1,q{+}1)$ at every point of the closed physical region; the metric-level description survives inside it as a distinguished subalgebra attached to a splitting, and on $\Sig$ it is the splitting, not the sheaf, that fails. Nothing jumps in the completion. The two sheaves are related by a global embedding, and the embedding is the localised transport.

Two further phenomena complete the picture, and both are theorems rather than constructions. First, a conservation law: the one-sided completion cannot be two-sided; no completion that is standard away from the wall is nondegenerate on both sides. The ambient form necessarily degenerates on a displaced hypersurface on the unphysical side, a \emph{shadow wall}, which for good couplings is itself a tame degeneration, so the completion iterates along an infinite wall sequence; degeneracy is moved, never destroyed. Second, an exceptional fibre: the anisotropic rescaling of the dying direction by $\sqrt{t}$ realises, fibrewise over $\Sig$, the deformation to the normal cone of algebraic geometry, and its special fibre is a genuine nondegenerate Clifford algebra whose metric in the dying direction is the \emph{rate} of the degeneration. The residue theorem then identifies the twist: the physical metric has a canonical simple pole at the wall, its residue induces an isomorphism $N^*\Sig \cong \shL^{\otimes 2}$ with $\shL$ the radical line bundle, so the dying line is a canonical square root of the conormal bundle and the Witt partner line adjoined by the completion, canonically $\shL^*$, is a canonical square root of the normal bundle. The new dimension is not adjoined arbitrarily; it is constructed tautologically from the dying direction and the geometry of its degeneration.

## technical
pending

## lay
pending

## one-liner
pending
