---
id: synthesis.one-type-second-stages-are-twins
kind: claim
version: 1
title: An antisymmetric one-type second stage is the twin of a symmetric one at all orders
status: proved
region: synthesis
subject: neutrinos
tags: [flavour-and-mixing, symmetry-breaking]
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
  - neutrino.breaking-relation@3
  - synthesis.theta23-at-s3-s2-direction@2
  - synthesis.solar-angle-light-plane-sum-rule@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_twin_map
- kind: check
  ref: check.py::check_observables_invariant
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.solar-angle-light-plane-sum-rule
extraction:
  open_problem: op.second-order-breaking
  note: Constructive route on op.second-order-breaking, asking whether the solar sum rule's exclusion of one-type second stages is two statements or one, and what part of a second stage the data can see. The content is the exact twin identity, valid at all orders. Whether the one-type exclusion survives beyond the breaking lemma's order, in particular on the far root, is not decided here; a floating-point exploration is reported in the proof text only, with a counterexample region.
---

## formal
Take the textures of Lemma \claimref{neutrino.breaking-relation} at the $S_{3} \to S_{2}$ direction $E = e_{3}e_{3}^{\mathsf{T}}$, as in Proposition \claimref{synthesis.theta23-at-s3-s2-direction}: in each sector a matrix $M(X) = \J + \delta(E + X)$ (times the sector's scale), with $\delta$ real and $X$ real and odd under the exchange $P_{12}$ of the first two families (the $S_{2} \to 1$ stage of Proposition \claimref{synthesis.solar-angle-light-plane-sum-rule}), the charged leptons reading $M_{e} = M(X_{e})$ with $\delta = \delta_{c}$ and the neutrinos $m_{\nu} = \mD M_{R}^{-1}\mD^{\mathsf{T}}$ with $\mD = M(X_{\nu})$ and $M_{R} = \alpha\Pi + M_{3}\J/3$, $\alpha, M_{3} \neq 0$. Call $XP_{12}$ the \emph{twin} of $X$.
\begin{enumerate}
\item[(i)] The twin map is a linear involution of the $P_{12}$-odd matrices that exchanges the symmetric ones with the antisymmetric ones: with $X_{s}(s,b) = \bigl[\begin{smallmatrix} s & 0 & b \\ 0 & -s & -b \\ b & -b & 0 \end{smallmatrix}\bigr]$ and $X_{a}(c,e) = \bigl[\begin{smallmatrix} 0 & c & e \\ -c & 0 & -e \\ -e & e & 0 \end{smallmatrix}\bigr]$, $X_{s}(s,b)P_{12} = X_{a}(s,b)$ and $X_{a}(c,e)P_{12} = X_{s}(c,e)$. In the basis of the odd line $(1,-1,0)$ and the even plane it keeps the (odd, even) entries $x$ of $X$ and reverses the (even, odd) entries $y$.
\item[(ii)] Exactly, for every $\delta$, every $P_{12}$-odd $X$ and every $\alpha, M_{3}$: $M(XP_{12}) = M(X)P_{12}$, hence $M(XP_{12})M(XP_{12})^{\mathsf{T}} = M(X)M(X)^{\mathsf{T}}$ and, since $P_{12}$ commutes with $M_{R}$, $M(XP_{12})M_{R}^{-1}M(XP_{12})^{\mathsf{T}} = M(X)M_{R}^{-1}M(X)^{\mathsf{T}}$. Replacing $X_{e}$ or $X_{\nu}$ by its twin leaves every charged-lepton mass, every light-neutrino mass, the charged leptons' left states and the light neutrino states unchanged, so the whole PMNS matrix is unchanged, at all orders in $\delta$, $\delta_{c}$, $X$ and the seesaw.
\item[(iii)] Consequently a one-type antisymmetric ($120$-like) second stage and the one-type symmetric ($10$/$126$-like) stage with the same entries $x$ are the same physics at every order, not only at the Lemma's order; the exclusion of one-type stages in Proposition \claimref{synthesis.solar-angle-light-plane-sum-rule}(iii) is one statement, not two. What a sector's second stage shows of itself is $x$ together with $y$ up to sign, so the lopsidedness that the solar angle asks for, $|y_{\nu}| \neq |x_{\nu}|$, is a twin invariant; the data fix the relative weight of the symmetric and antisymmetric parts within one sector, and not which of them is the grade-three ($120$) direction.
\end{enumerate}
Whether the one-type exclusion of that proposition holds beyond the Lemma's order, on the far root in particular, is not decided by this result.

## technical
At the $S_{3} \to S_{2}$ direction the solar angle must come from a second stage $X$ odd under the exchange of the first two families, and the stored sum rule says that, at the breaking lemma's order, a stage of one type in each sector (purely symmetric or purely antisymmetric) cannot reach it; the data ask for a lopsided stage. That analysis is at leading order, while the root of the atmospheric angle that fits the data lies past the peak of $m_{2}/m_{3}$, where the lemma's remainders are not small.

The exact observation here is a twin identity. Multiplying a family-exchange-odd matrix on the right by the exchange swaps its symmetric and antisymmetric types, and because the unbroken parts of the textures and the Majorana matrix are exchange-even, it multiplies the whole sector matrix on the right by the exchange: $M(XP_{12}) = M(X)P_{12}$. A right factor is invisible both to the charged leptons' left states and masses and to the seesaw, since $P_{12}$ commutes with $M_{R}$. So the antisymmetric one-type stage and its symmetric twin give identical masses and an identical PMNS matrix, exactly, at every order. Only the relative weight of the two types inside one sector is observable.

The identity is exact at every order, so it holds on the far root of the atmospheric angle as on the near one. It does not by itself say whether one-type stages are excluded beyond the Lemma's order; that question stays open.

## lay
The pattern of neutrino mixing needs a small extra breaking of the symmetry between the first two families of particles. The series knew, from a leading-order calculation, that this breaking cannot be of one simple kind in each sector. This result shows, exactly and without approximation, that the two simple kinds (a symmetric pattern and an antisymmetric one, which in the unified theory come from different Higgs fields) are mirror images that give identical masses and mixings, so there is really only one simple kind to rule out, and what the data can measure is how the two kinds are mixed inside one sector. Whether the leading-order exclusion survives in the full equations is left open.

## one-liner
For exchange-odd second stages $M(XP_{12}) = M(X)P_{12}$ exactly, so a one-type antisymmetric stage and its symmetric twin give identical lepton masses and PMNS matrix at all orders; only the relative weight of the two types within a sector is observable.
