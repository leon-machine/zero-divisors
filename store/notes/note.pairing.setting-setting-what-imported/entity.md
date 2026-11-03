---
id: note.pairing.setting-setting-what-imported
kind: note
version: 1
title: Setting, and what is imported
status: setting
subject: one-relation
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
comments_on:
- pairing.imported-stabiliser-tangent
locators:
  paper: T05-pairing
  number: Setting
  section: Setting, and what is imported
  line: 170
---

## formal
The singularity paper reads entanglement as a mismatch of Witt decompositions and locates the generators that can produce it \cite[Prop.~13.4]{ButlerT5}: on the Fock space of $\nu$ modes the bivectors of $\so(2\nu)$ split into hops and pair annihilations, which stabilise the vacuum ray, and pair creations, which span the tangent of its orbit. The same paper then records, in one remark, the two things it does not do \cite[Rem.~13.5]{ButlerT5}: the framework compares two Witt decompositions and does not derive them, and the derivation of the one pairing angle its chain uses, the angle of its regularity premise, lies outside its reach. Its locality premise (L$_E$) \cite[Prem.~7.30]{ButlerT5} excludes pairing terms on the ground that the completion supplies none.

This note asks where, in the framework's own data, a pairing generator would have to come from, and answers: in the connection. The laboratory paper says in words that the connection carries the vacuum's bivector from point to point and returns it tilted \cite[Prop.~4.1(3) and the paragraph following it]{ButlerT16}. Stated exactly, the tilt has a stabiliser part and a pairing part, and the pairing part is the set of Newman-Penrose spin coefficients that measure how the null direction fails to be parallel. The note computes it, in the series' own conventions and in exact arithmetic, and then applies the kill conditions of Section \ref{sec:kill} to the two claims.

Three things are said on this page because the rest depends on them. First, the space. The singularity paper's premise governs the Fock space of its boundary modes, one ladder pair attached to each point of the exceptional set $E$ \cite[Prem.~7.30, Fact~5.9]{ButlerT5}, on which a pairing $v^{*}_{x}v^{*}_{y}$ is cross-point by construction and a single point carries no pairing at all. The fibre of this note is a different space: the pre-ascent Dirac spinor at an exterior point, read as two fermionic modes, the complex capacity two of the laboratory paper \cite[Prop.~3.2(1)]{ButlerT16}. What is found here is found on that fibre, and Section \ref{sec:verdict} says what it does and does not imply for the premise. Second, the risk. The positive claim's kill conditions could not have fired (Section \ref{sec:verdict}); the registration fixed the computation and its conventions in advance, and the note's content is a dictionary between the series' objects and known ones, not a derivation that might have failed. Third, the vocabulary, for a reader of general relativity and geometric algebra who has not read the series: the \emph{ascent} is the adjunction of a hyperbolic plane $(1,1)$ that the transport principle forces where division fails \cite[Thm.~4.13]{ButlerT1}, the \emph{completion} is its result, the \emph{exceptional set} $E$ is the locus where it happens \cite[Thm.~8.12]{ButlerT4}, the \emph{descent} is the one-way map back \cite[Thm.~7.3]{ButlerT5}, the \emph{flag bit} is the orientation choosing which half of a null pair creates \cite[Def.~2.10]{ButlerT14}, and the two-ledger words \emph{transport-essential}, \emph{convenient} and \emph{absent} grade a result by whether the $(1,1)$ increment does irreplaceable work in it, some work, or none \cite{ButlerT17}.

Notation follows the series. $\Cl(1,3)$ has $e_0^2 = 1$ and $e_i^2 = -1$; $\ip{a}{b} = \tfrac12(ab + ba)$ is the scalar product of vectors, extended bilinearly (not sesquilinearly) to $\C^4$; a bivector $B$ acts on vectors by $B\cdot v = \tfrac12[B, v]$, which is the $\so(1,3)$ action. The null tetrad is
\[
\ell = e_0 + e_1, \qquad n = e_0 - e_1, \qquad m = e_2 + i e_3, \qquad \mb = e_2 - i e_3,
\]
with $\ip{\ell}{n} = 2$, $\ip{m}{\mb} = -2$ and all other pairings zero. The framework's vacuum at a point is the maximal isotropic subspace $W = \operatorname{span}\{\ell, m\}$ of $\C^4$: $\ell$ is the radial null direction of the descent, the ladder vector of the singularity paper's Step 3 up to the flag bit \cite[Sec.~4, Lem.~4.1]{ButlerT5}, and the sign of $i$ in $m$ is the chirality bit. The Fock module is that of two modes with annihilators $a_1 = c(\ell)/2$, $a_2 = c(m)/2$ and creators $a_1^{\dagger} = c(n)/2$, $a_2^{\dagger} = -c(\mb)/2$, so that $e_0 = a_1 + a_1^{\dagger}$, $e_1 = a_1 - a_1^{\dagger}$, $e_2 = a_2 - a_2^{\dagger}$, $e_3 = -i(a_2 + a_2^{\dagger})$; this is the two-mode reading of the Dirac spinor, the complex capacity two of the laboratory paper.

## technical
pending

## lay
pending

## one-liner
pending
