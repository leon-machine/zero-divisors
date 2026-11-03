---
id: synthesis.residual-s2-fixes-120-family-form
kind: claim
version: 1
title: The residual S_2 fixes the 120's family form to the second-third coupling, and an S_3-invariant Majorana sector keeps the 126 family-blind on the light plane, so it cannot act on the second family alone
status: proved
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, seesaw-and-majorana, no-go]
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
review: draft
derivations:
- name: main
  uses:
  - standard-model.imported-spinor-bilinears@1
  - standard-model.imported-clebsch-structure-seesaw@1
  - neutrino.invariant-symmetric-matrices@2
  - neutrino.breaking-relation@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_residual_s2_fixes_120_family_form
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.fits-record-level
  - families.imported-grade-three-direction-between-families
  - synthesis.georgi-jarlskog-majorana-moment-map
extraction:
  open_problem: op.pair-sector-current
  note: 'Answers the Pati-Salam half of the problem in form, not in strength. Imports the family-symmetry structure of the neutrino paper (S_3, broken along e_3 e_3^T) into the charged-fermion Clebsch structure of the standard-model paper. Result: the registered route of standard-model.fits-record-level (factor 3 of the second family through mixing with the third, carried by the 120 and the 10s) is the route that remains once an S_3-invariant Majorana sector excludes a 126 entry on the second family alone (the Georgi-Jarlskog texture), and its 120 family matrix is the unique S_2-invariant antisymmetric matrix, which couples exactly the second and third families. The coupling strength, and so the 126 coefficient relative to the 10, is not derived; it is the 126 doublet admixture that also sets the Majorana scale under (EW). The family labels hold at the S_2 stage, before the second-stage breaking. Transport-absent: finite-group invariant theory on the family index plus the imported Clebsch structure.'
---

## formal
Let $S_{3}$ act on family matrices by $X \mapsto PXP^{\mathsf{T}}$ in the basis $e_{1}, e_{2}, e_{3}$ of Lemma \claimref{neutrino.breaking-relation}, let $S_{2}$ be the stabiliser of its breaking direction $e_{3}e_{3}^{\mathsf{T}}$ (the exchange of $e_{1}$ and $e_{2}$), and put $u' = (1,1,1)$, $s = (1,1,-2)$, $a = (1,-1,0)$.
\begin{enumerate}
\item[(i)] No nonzero antisymmetric family matrix is $S_{3}$-invariant. The $S_{2}$-invariant antisymmetric matrices form a line, spanned by $u' \wedge s = u's^{\mathsf{T}} - su'^{\mathsf{T}} = -3\,(e_{1} + e_{2}) \wedge e_{3}$; it annihilates $a$. The $S_{3}$-invariant symmetric matrices form the plane of $\Pi$ and $\J$ (Lemma \claimref{neutrino.invariant-symmetric-matrices}), the $S_{2}$-invariant ones a four-dimensional space spanned by $u'u'^{\mathsf{T}}$, $ss^{\mathsf{T}}$, $aa^{\mathsf{T}}$ and $u's^{\mathsf{T}} + su'^{\mathsf{T}}$.
\item[(ii)] For every breaking $\J + \varepsilon\,e_{3}e_{3}^{\mathsf{T}}$, $a$ is a null vector and $s$ is not: at the $S_{2}$ stage $a$ is the first family, $s$ the second and $u'$ (mixed with $s$) the third, with the charged-fermion family labels taken from the neutrino-sector breaking direction. Hence a $120$ coupling (antisymmetric, Fact \claimref{standard-model.imported-spinor-bilinears}) that respects the residual $S_{2}$ couples exactly the second and third families and leaves the first uncoupled, and an $S_{3}$-symmetric stage admits no $120$ coupling.
\item[(iii)] Under Fact \claimref{standard-model.imported-clebsch-structure-seesaw}, if the Majorana matrix is $S_{3}$-invariant, $M_{R} = \alpha\Pi + M_{3}\J/3$ as in Lemma \claimref{neutrino.breaking-relation}, then $f = M_{R}/v_{R}$ and $\mathrm{Sym}(M_{d} - M_{e}) = 4w_{d}f$ are $S_{3}$-invariant whatever the $10$s and the $120$: the $126$ enters the two light families through one scalar, $4w_{d}\alpha/v_{R}$ on the whole plane $u'^{\perp}$, and the third through $4w_{d}M_{3}/v_{R}$. A $126$ entry on the second family alone is not of this form.
\end{enumerate}
So, with an $S_{3}$-invariant Majorana sector and the $S_{3} \to S_{2}$ breaking direction, the $126$ cannot supply a factor on the second family alone, the Georgi-Jarlskog texture is unavailable, and the registered route through the $120$ coupling of the second and third families with the $10$s is the route that remains; (i)-(ii) derive that coupling's family form. Its strength is not derived.

## technical
Import the neutrino paper's family symmetry into the Pati-Salam Clebsch structure. Antisymmetric family matrices, the only ones a $120$ can carry, contain no $S_{3}$ singlet, so an unbroken permutation symmetry forbids the $120$ altogether. Under the residual $S_{2}$ of the store's breaking direction $e_{3}e_{3}^{\mathsf{T}}$ exactly one antisymmetric matrix survives, $u' \wedge s$: it couples the heavy direction $u'$ to the $S_{2}$-even light state $s$ and annihilates the $S_{2}$-odd state $a$. Since any breaking along $e_{3}e_{3}^{\mathsf{T}}$ leaves $a$ massless while $s$ acquires mass, $a$ is the first family and $s$ the second at that stage, so the residual symmetry selects precisely the antisymmetric coupling between the second and third families that the registered route uses.

For the $126$: the Majorana matrix is $v_{R}f$, and the symmetric part of $M_{d} - M_{e}$ is $4w_{d}f$ whatever the $10$s and the $120$. If the Majorana sector is $S_{3}$-invariant, as the neutrino paper takes it at leading order, the $126$ is family-blind on the light plane: it cannot put a factor $3$ on the second family alone, so the Georgi-Jarlskog texture is unavailable; any factor the $126$ supplies is shared by the first family. Under these premises the registered route through the $120$ and the $10$s is the route that remains, and its family form is derived; the coupling's size is still an input.

## lay
In the framework's grand-unified picture the muon is about three times heavier than the strange quark at high energy, while the electron and the down quark go the other way, and the series has had to choose how that factor of three arises. This result shows that if the heavy neutrinos are as symmetric among the three families as the neutrino paper assumes, the field that gives them mass cannot be the source of that factor for the second family alone: it treats the two lighter families identically. The remaining route takes the factor from a different field that links families in pairs, and the family symmetry left over after the first stage of breaking allows that field to link only the second and third families. That is the route the series had chosen by fitting; here its shape follows from symmetry, though its strength is still not derived.

## one-liner
If the Majorana sector is $S_{3}$-invariant, the $126$ is family-blind on the light plane and cannot supply a factor on the second family alone, while the residual $S_{2}$ of the breaking direction allows exactly one $120$ family matrix, $u' \wedge s$, coupling the second and third families: the registered route's form is derived, its strength is not.
